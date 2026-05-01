import click
import os
import json
from dt_ai.discovery import discover_raw_files, get_neighboring_files
from dt_ai.processor import extract_preview
from dt_ai.ai import AESTHETIC_PROMPT, parse_ai_response, synthesize_nudge
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
    
    # 3. Build Payload for the Agent
    payload = {
        "prompt": AESTHETIC_PROMPT,
        "target_image": abs_path,
        "target_preview": target_preview,
        "neighbors": neighbors,
        "state": state
    }
    
    click.echo(json.dumps(payload))

@cli.command()
@click.argument('image_path', type=click.Path(exists=True))
@click.argument('ai_result_json')
def apply_variations(image_path, ai_result_json):
    """Applies the AI-generated variations and saves the audit report."""
    abs_path = os.path.abspath(image_path)
    dir_path = os.path.dirname(abs_path)
    ai_result = json.loads(ai_result_json)
    
    # 1. Generate variations
    versions = generate_variations(abs_path, ai_result)
    
    # 2. Save report
    report_path = save_audit_report(abs_path, ai_result.get("audit", "No audit provided"))
    
    # 3. Update state
    state = load_state(dir_path)
    state["history"].append({
        "image": os.path.basename(abs_path),
        "styles": list(ai_result.get("variations", {}).keys()),
        "timestamp": "now" # In a real app, use ISO time
    })
    state["last_processed"] = os.path.basename(abs_path)
    save_state(dir_path, state)
    
    # 4. Result for Agent
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
            # Note: This part remains simple for legacy compatibility 
            # In a real app, we'd refactor this to call the new logic
            click.echo(f"Processing {os.path.basename(f)}...")
        except Exception as e:
            click.echo(f"  ✗ Error: {str(e)}")

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
