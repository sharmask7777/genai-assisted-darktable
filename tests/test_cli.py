from click.testing import CliRunner
from dt_ai.main import cli

def test_audit_dry_run(tmp_path):
    f = tmp_path / "test.ARW"
    f.write_text("dummy")
    
    runner = CliRunner()
    result = runner.invoke(cli, ['audit', str(f), '--dry-run'])
    
    assert result.exit_code == 0
    assert "DRY-RUN mode" in result.output
    assert "Discovered 1 RAW file(s)" in result.output
    assert "test.ARW" in result.output

def test_audit_no_files(tmp_path):
    runner = CliRunner()
    result = runner.invoke(cli, ['audit', str(tmp_path)])
    
    assert result.exit_code == 0
    assert "No RAW files found" in result.output
