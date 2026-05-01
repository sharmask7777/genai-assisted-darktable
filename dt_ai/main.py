import click
import os
import json
from dt_ai.discovery import discover_raw_files, get_neighboring_files
from dt_ai.processor import extract_preview
from dt_ai.ai import analyze_image, AESTHETIC_PROMPT, parse_ai_response
from dt_ai.xmp import generate_variations
from dt_ai.gui import open_in_darktable
from dt_ai.state import load_state, save_state, get_state_path

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

@cli.command()
@click.argument('image_path', type=click.Path(exists=True))
def agent_next(image_path):
    """Internal command for Agent SOP: returns JSON payload for next steps."""
    abs_path = os.path.abspath(image_path)
    dir_path = os.path.dirname(abs_path)
    
    # 1. Load context
    state = load_state(dir_path)
    neighbors = get_neighboring_files(abs_path)
    
    # 2. Extract Previews (Target + Neighbors)
    previews = {}
    
    # Extract target (must succeed)
    target_preview = extract_preview(abs_path)
    previews[abs_path] = target_preview
    
    # Extract neighbors (resilient)
    for n in neighbors:
        try:
            previews[n] = extract_preview(n)
        except Exception:
            # Skip neighbors that fail to extract
            pass
    
    # 3. Analyze Target
    raw_response = analyze_image(target_preview, AESTHETIC_PROMPT)
    ai_result = parse_ai_response(raw_response)
    
    # 4. Build Payload
    payload = {
        "nudge": ai_result.get("audit", "I've analyzed your photo. Ready to proceed?"),
        "target_image": abs_path,
        "neighbor_images": neighbors,
        "previews": previews,
        "ai_result": ai_result
    }
    
    click.echo(json.dumps(payload))

def run_pipeline(path, dry_run, mode='audit'):
    if dry_run:
        click.echo("Running in DRY-RUN mode. No files will be modified.")
    files = discover_raw_files(path)
    if not files:
        click.echo(f"No RAW files found at: {path}")
        return
    click.echo(f"Discovered {len(files)} RAW file(s). Starting {mode} pipeline...")
    total_versions = 0
    for f in files:
        basename = os.path.basename(f)
        click.echo(f"\nProcessing {basename}...")
        try:
            preview_path = extract_preview(f)
            click.echo(f"  ✓ Extracted preview: {os.path.relpath(preview_path)}")
            raw_response = analyze_image(preview_path, AESTHETIC_PROMPT)
            ai_result = parse_ai_response(raw_response)
            report_path = save_audit_report(f, ai_result.get("audit", "No audit provided"))
            click.echo(f"  ✓ Audit report saved: {os.path.basename(report_path)}")
            if mode == 'edit' and not dry_run:
                versions = generate_variations(f, ai_result)
                click.echo(f"  ✓ Generated {len(versions)} versions")
                total_versions += len(versions)
                if needs_denoise_interaction(ai_result.get("recommendations", [])):
                    click.echo("  ! Take a Call: Denoise recommended. Opening Darktable for validation...")
                    open_in_darktable(f)
                    click.confirm("    Please adjust denoise settings if needed. Continue with next file?", default=True)
        except Exception as e:
            click.echo(f"  ✗ Error: {str(e)}")
    click.echo("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    click.echo(f" PIPELINE COMPLETE")
    click.echo(f" Files processed: {len(files)}")
    if mode == 'edit':
        click.echo(f" Versions created: {total_versions}")
    click.echo("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

@cli.command()
@click.argument('path', type=click.Path(exists=True))
@click.option('--dry-run', is_flag=True, help="Don't perform any actual edits")
def audit(path, dry_run):
    """Discover RAW files and perform an aesthetic audit."""
    run_pipeline(path, dry_run, mode='audit')

@cli.command()
@click.argument('path', type=click.Path(exists=True))
@click.option('--dry-run', is_flag=True, help="Don't write XMP files")
def edit(path, dry_run):
    """Perform audit and generate AI edit variations."""
    run_pipeline(path, dry_run, mode='edit')

if __name__ == "__main__":
    cli()
