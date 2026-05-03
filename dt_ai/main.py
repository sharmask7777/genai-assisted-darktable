import click
import os
import json
from dt_ai.discovery import discover_raw_files, get_neighboring_files, get_raw_metadata
from dt_ai.processor import extract_preview
from dt_ai.ai import AESTHETIC_PROMPT, parse_ai_response, synthesize_nudge, get_composition_prompt, get_aesthetic_prompt
from dt_ai.xmp import generate_variations, generate_crop_previews, promote_variation
from dt_ai.gui import open_in_darktable
from dt_ai.state import load_state, save_state, get_state_path
from dt_ai.research import get_subject_tips

def get_and_validate_metadata(image_path: str) -> dict:
    """Gets metadata and prompts user for missing essential fields."""
    meta = get_raw_metadata(image_path)
    
    essential_fields = {
        'model': 'Camera Model',
        'lens': 'Lens Model',
        'iso': 'ISO',
        'exposure': 'Exposure Time',
        'aperture': 'Aperture'
    }
    
    missing = []
    for field, label in essential_fields.items():
        if not meta.get(field):
            missing.append((field, label))
            
    if missing:
        click.echo(f"\n[!] Warning: Missing metadata for: {os.path.basename(image_path)}")
        for field, label in missing:
            click.echo(f"    - {label} not found in EXIF.")
            meta[field] = "Unknown"
            
    return meta

# Educational snippets for modern modules
MODULE_SNIPPETS = {
    "sigmoid": "A modern scene-referred tone mapper that preserves hue and handles highlight roll-off gracefully (AgX-style).",
    "exposure": "Sets the mid-gray anchor point. Essential for the scene-referred pipeline.",
    "colorcalibration": "A high-precision module for white balance and channel mixing using modern color science.",
    "diffuse": "Used for surgical sharpening or local contrast without halo artifacts."
}

def generate_preflight_report(image_path: str, ai_result: dict, metadata: dict) -> str:
    """Generates an educational summary of planned edits."""
    image_name = os.path.basename(image_path)
    subject = ai_result.get("subject", "general").upper()
    report = [
        f"\n{'='*60}",
        f" 🦉 MENTOR PRE-FLIGHT REVIEW: {image_name}",
        f"{'='*60}\n",
        f"🏷️ [SUBJECT] {subject}",
        f"📸 [METADATA] {metadata.get('model', 'Unknown')} | {metadata.get('lens', 'Unknown')} | ISO {metadata.get('iso', 'Unknown')}",
        f"🎯 [ANALYSIS] {ai_result.get('analysis', 'Standard enhancement')}\n",
        "🛠 [PLANNED ACTIONS]:"
    ]
    
    # Rationale for technical fixes
    from dt_ai.xmp import apply_hardware_corrections
    hw = apply_hardware_corrections(metadata)
    if hw["black_offset"] > 0:
        report.append(f"  • SENSOR FIX: Detected {metadata.get('model')}. Applying black-point offset of {hw['black_offset']} to stabilize shadows.")
        
    # AgX Enforcement
    report.append("  • WORKFLOW: Enforcing modern AgX/Scene-referred pipeline. Legacy modules (Filmic/Basecurve) will be disabled.")
    
    # Educational Snippets
    report.append("\n📚 [TECHNICAL MENTORSHIP]:")
    for mod, snippet in MODULE_SNIPPETS.items():
        report.append(f"  • {mod.capitalize()}: {snippet}")
        
    # Research Rationale
    rationale = ai_result.get("research_rationale")
    if rationale:
        report.append(f"\n🌍 [RESEARCH INSIGHT]: {rationale}")
    
    # Variations
    variations = ai_result.get("variations", {})
    if variations:
        report.append("\n🎨 [STYLES TO GENERATE]:")
        for style, params in variations.items():
            exp = params.get("exposure", 0.0)
            kel = params.get("kelvin", 5500.0)
            report.append(f"  → {style.upper()}: Exposure {exp:+.1f} EV | Temp {kel}K")
            
    report.append(f"\n{'='*60}\n")
    return "\n".join(report)

def save_audit_report(raw_path: str, audit_text: str) -> str:
    """Saves the AI audit text to a Markdown file alongside the RAW image."""
    base, _ = os.path.splitext(raw_path)
    report_path = f"{base}_audit.md"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(audit_text)
    return report_path

def needs_denoise_interaction(recommendations):
    """Returns True if any denoise-related module is recommended."""
    denoise_terms = {"denoise", "denoiseprofile", "denoise (profiled)"}
    return any(term in [r.lower() for r in recommendations] for term in denoise_terms)

@click.group()
def cli():
    """Darktable GenAI Assistant"""
    pass

@cli.command()
@click.argument('path', type=click.Path(exists=True, file_okay=False))
def init_session(path):
    """Initialize or resume an editing session for a directory."""
    state_path = get_state_path(path)
    is_resuming = state_path.exists()
    state = load_state(path)
    save_state(path, state)
    if is_resuming:
        click.echo(f"Resuming existing session for: {path}")
    else:
        click.echo(f"Started new session for: {path}")

@cli.command(name='promote-variation')
@click.argument('image_path', type=click.Path(exists=True))
@click.argument('version_id', type=int)
def promote_variation_cmd(image_path, version_id):
    """Internal command: promotes a versioned sidecar to the base sidecar."""
    abs_path = os.path.abspath(image_path)
    try:
        promote_variation(abs_path, version_id)
        click.echo(f"Successfully promoted version {version_id} to base.")
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)
        exit(1)

@cli.command()
@click.argument('image_path', type=click.Path(exists=True))
@click.option('--mode', type=click.Choice(['compose', 'aesthetic']), default='aesthetic')
@click.option('--crop-rationale', default="")
def agent_next(image_path, mode, crop_rationale):
    """Internal command: returns preview paths and the mentorship prompt."""
    abs_path = os.path.abspath(image_path)
    dir_path = os.path.dirname(abs_path)
    
    # 1. Load context
    state = load_state(dir_path)
    neighbors = get_neighboring_files(abs_path)
    
    # 2. Extract Previews (Target + Neighbors)
    previews = {}
    target_preview = extract_preview(abs_path)
    previews[abs_path] = target_preview
    for n in neighbors:
        try:
            previews[n] = extract_preview(n)
        except Exception:
            pass
    
    # 3. Metadata Extraction
    metadata = get_and_validate_metadata(abs_path)
    
    # 4. Prompt Selection & XMP Review
    from dt_ai.xmp import get_xmp_history_summary
    xmp_path = f"{abs_path}.xmp"
    user_edits = get_xmp_history_summary(xmp_path)
    
    if mode == 'compose':
        prompt = get_composition_prompt()
    else:
        prompt = get_aesthetic_prompt(crop_rationale, user_edits)
    
    # 5. Build Payload for the Agent
    payload = {
        "prompt": prompt,
        "target_image": abs_path,
        "target_preview": target_preview,
        "neighbors": neighbors,
        "metadata": metadata,
        "user_edits": user_edits,
        "state": state,
        "research_database": {
            "wildlife": get_subject_tips("WILDLIFE"),
            "landscape": get_subject_tips("LANDSCAPE"),
            "macro": get_subject_tips("MACRO")
        }
    }
    
    click.echo(json.dumps(payload))

@cli.command()
@click.argument('image_path', type=click.Path(exists=True))
@click.argument('ai_result_json')
@click.option('--mode', type=click.Choice(['crop-preview', 'aesthetic']), default='aesthetic')
@click.option('--yolo', is_flag=True, help="Skip confirmation and apply edits immediately")
def apply_variations(image_path, ai_result_json, mode, yolo):
    """Applies the AI-generated variations and saves the audit report."""
    abs_path = os.path.abspath(image_path)
    dir_path = os.path.dirname(abs_path)
    ai_result = json.loads(ai_result_json)
    
    if mode == 'crop-preview':
        metadata = get_raw_metadata(abs_path)
        versions = generate_crop_previews(abs_path, ai_result, metadata=metadata)
        click.echo(json.dumps({"versions": versions}))
        return

    # 1. Get metadata for hardware corrections and reporting
    metadata = get_raw_metadata(abs_path)
    
    # 2. Show Pre-flight Report
    report = generate_preflight_report(abs_path, ai_result, metadata)
    click.echo(report)
    
    # 3. Confirmation
    if not yolo:
        if not click.confirm("Apply these variations to Darktable?"):
            click.echo("Edits cancelled.")
            return

    # 4. Generate variations
    versions = generate_variations(abs_path, ai_result, metadata=metadata)
    
    # 5. Save report
    report_path = save_audit_report(abs_path, ai_result.get("audit", "No audit provided"))
    
    # 6. Update state
    state = load_state(dir_path)
    state["history"].append({
        "image": os.path.basename(abs_path),
        "styles": list(ai_result.get("variations", {}).keys()),
        "timestamp": "now" # In a real app, use ISO time
    })
    state["last_processed"] = os.path.basename(abs_path)
    save_state(dir_path, state)
    
    # 7. Result for Agent
    result = {
        "versions": versions,
        "report_path": report_path,
        "needs_interaction": needs_denoise_interaction(ai_result.get("recommendations", []))
    }
    click.echo(json.dumps(result))

def run_pipeline(path, dry_run, mode='audit'):
    """Legacy pipeline for standalone CLI usage."""
    if dry_run:
        click.echo("Running in DRY-RUN mode. No files will be modified.")
    files = discover_raw_files(path)
    if not files:
        click.echo(f"No RAW files found at: {path}")
        return
    click.echo(f"Discovered {len(files)} RAW file(s). Starting {mode} pipeline...")
    for f in files:
        try:
            click.echo(f"Processing {os.path.basename(f)}...")
        except Exception as e:
            click.echo(f"  ✗ Error: {str(e)}")

@cli.command()
@click.argument('path', type=click.Path(exists=True))
@click.option('--dry-run', is_flag=True, help="Don't perform any actual audit")
def audit(path, dry_run):
    """Discover RAW files and perform an aesthetic audit."""
    run_pipeline(path, dry_run, mode='audit')

@cli.command()
@click.argument('path', type=click.Path(exists=True))
@click.option('--dry-run', is_flag=True, help="Don't write XMP files")
def edit(path, dry_run):
    """Discover RAW files and generate AI edit variations."""
    run_pipeline(path, dry_run, mode='edit')

if __name__ == "__main__":
    cli()
