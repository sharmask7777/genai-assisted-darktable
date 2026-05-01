import os
import shutil
from dt_ai.parity import (
    InternalScanner, 
    ExternalResearcher, 
    AuditEngine, 
    TDDOrchestrator, 
    DocUpdater, 
    get_progress_dir
)

def test_parity_sync_e2e_dry_run():
    # 1. Setup Environment
    progress_dir = get_progress_dir()
    os.makedirs(progress_dir, exist_ok=True)
    temp_repo = os.path.join(progress_dir, "repo")
    os.makedirs(temp_repo, exist_ok=True)
    
    # Create dummy README
    readme_path = os.path.join(temp_repo, "README.md")
    with open(readme_path, "w") as f:
        f.write("# Darktable AI Project\n")

    print(f"\n[E2E] Starting Parity Sync Dry-Run in {progress_dir}")

    # 2. Internal Scan
    scanner = InternalScanner(codebase_path=".")
    internal_data = scanner.run()
    assert "aesthetic" in internal_data["prompts"]
    print("[E2E] Internal Scan Complete")

    # 3. External Research
    researcher = ExternalResearcher(progress_dir=progress_dir)
    mock_search = lambda query: f"Latest research results for {query}: AgX is standard."
    research_results = researcher.perform_search(mock_search, "darktable 2026 standards")
    assert "AgX" in research_results
    print("[E2E] External Research Complete")

    # 4. Audit & Reporting
    auditor = AuditEngine(progress_dir=progress_dir)
    report_path = auditor.generate_report(internal_data, research_results)
    assert os.path.exists(report_path)
    print("[E2E] Audit Report Generated")

    # 5. TDD Planning
    orchestrator = TDDOrchestrator(progress_dir=progress_dir)
    plan_path = orchestrator.create_plan(report_path)
    assert os.path.exists(plan_path)
    print("[E2E] TDD Plan Created")

    # 6. TDD Execution (Simulated)
    # Create a dummy test file for the orchestrator to "run"
    dummy_test = os.path.join(temp_repo, "test_parity_mock.py")
    with open(dummy_test, "w") as f:
        f.write("def test_parity(): assert True")
    
    success = orchestrator.run_test(dummy_test)
    assert success is True
    print("[E2E] TDD Test Execution Verified")

    # 7. Documentation Update
    doc_updater = DocUpdater(repo_root=temp_repo)
    doc_updater.update_readme()
    
    with open(readme_path, "r") as f:
        content = f.read()
        assert "GenAI Skills" in content
    print("[E2E] Documentation Updated")

    # 8. Cleanup
    shutil.rmtree(progress_dir)
    print("[E2E] Dry-Run Successful. Environment Cleaned.")

if __name__ == "__main__":
    test_parity_sync_e2e_dry_run()
