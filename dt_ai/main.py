import click
import os
from dt_ai.discovery import discover_raw_files

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

    click.echo(f"Discovered {len(files)} RAW file(s):")
    for f in files:
        click.echo(f"  - {os.path.basename(f)}")

if __name__ == "__main__":
    cli()
