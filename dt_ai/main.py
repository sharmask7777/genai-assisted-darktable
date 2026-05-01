import click
import os
from dt_ai.discovery import discover_raw_files
from dt_ai.processor import extract_preview
from dt_ai.ai import analyze_image, AESTHETIC_PROMPT

def needs_denoise_interaction(recommendations): 
    """Returns True if any denoise-related module is recommended.""" 
    denoise_terms = {"denoise", "denoiseprofile", "denoise (profiled)"} 
    return any(term in [r.lower() for r in recommendations] for term in denoise_terms) 

def save_audit_report(raw_path: str, audit_text: str) -> str:
    """Saves the AI audit text to a Markdown file alongside the RAW image."""
    base, _ = os.path.splitext(raw_path)
    report_path = f"{base}_audit.md"
    
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(audit_text)
        
    return report_path

@click.group()
def cli():
    """Darktable GenAI Assistant"""
    pass

@cli.command()
@click.argument('path', type=click.Path(exists=True))
@click.option('--dry-run', is_flag=True, help="Don't perform any actual edits")
def audit(path, dry_run):
    """Discover RAW files and perform an aesthetic audit."""
    if dry_run:
        click.echo("Running in DRY-RUN mode. No files will be modified.")
    
    files = discover_raw_files(path)
    
    if not files:
        click.echo(f"No RAW files found at: {path}")
        return

    click.echo(f"Discovered {len(files)} RAW file(s).")
    
    for f in files:
        basename = os.path.basename(f)
        click.echo(f"Processing {basename}...")
        try:
            # 1. Extract Preview
            preview_path = extract_preview(f)
            click.echo(f"  ✓ Extracting preview: {os.path.relpath(preview_path)}")
            
            # 2. Analyze Image
            click.echo(f"  ... Performing AI aesthetic audit")
            audit_text = analyze_image(preview_path, AESTHETIC_PROMPT)
            
            # 3. Save Report
            report_path = save_audit_report(f, audit_text)
            click.echo(f"  ✓ Audit report saved: {os.path.basename(report_path)}")
            
        except Exception as e:
            click.echo(f"  ✗ Error: {str(e)}")

if __name__ == "__main__":
    cli()
