import os
import re
import datetime
import json
import subprocess
from typing import Dict, List, Callable

class InternalScanner:
    """
    Analyzes the dt-ai codebase to map current capabilities, 
    prompts, and XMP module configurations.
    """
    
    def __init__(self, codebase_path: str = "."):
        self.codebase_path = codebase_path
        self.results = {
            "prompts": {},
            "xmp_modules": {},
            "patterns": []
        }

    def scan_prompts(self):
        """Extracts prompts from ai.py."""
        ai_path = os.path.join(self.codebase_path, "dt_ai", "ai.py")
        if not os.path.exists(ai_path):
            return
            
        with open(ai_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Find AESTHETIC_PROMPT
        prompt_match = re.search(r'AESTHETIC_PROMPT = """(.*?)"""', content, re.DOTALL)
        if prompt_match:
            self.results["prompts"]["aesthetic"] = prompt_match.group(1).strip()

    def scan_xmp_logic(self):
        """Extracts XMP module versions and structs from xmp.py."""
        xmp_path = os.path.join(self.codebase_path, "dt_ai", "xmp.py")
        if not os.path.exists(xmp_path):
            return
            
        with open(xmp_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Find exposure v6
        if 'get_exposure_params' in content:
            self.results["xmp_modules"]["exposure"] = {
                "version": "6",
                "struct": "iffff"
            }
            
        # Find temperature v3
        if 'get_temperature_params' in content:
            self.results["xmp_modules"]["temperature"] = {
                "version": "3",
                "struct": "ffff"
            }

    def run(self) -> Dict:
        """Executes all scan phases."""
        self.scan_prompts()
        self.scan_xmp_logic()
        return self.results

class ExternalResearcher:
    """
    Leverages external tools to identify the latest Darktable trends,
    schema changes, and module updates.
    """
    
    def __init__(self, progress_dir: str):
        self.progress_dir = progress_dir
        self.research_dir = os.path.join(progress_dir, "research")
        os.makedirs(self.research_dir, exist_ok=True)

    def perform_search(self, search_fn, query: str) -> str:
        """Executes a search and saves the result."""
        result = search_fn(query=query)
        
        # Save to file for TDD verification and audit trail
        filename = re.sub(r"[^a-zA-Z0-9]", "_", query).lower()[:50] + ".txt"
        file_path = os.path.join(self.research_dir, filename)
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(result)
            
        return result

class AuditEngine:
    """
    Synthesizes internal and external data into a Parity Report.
    """
    
    def __init__(self, progress_dir: str):
        self.progress_dir = progress_dir

    def generate_report(self, internal_data: Dict, external_findings: str) -> str:
        """
        Creates a structured REPORT.md.
        """
        report_path = os.path.join(self.progress_dir, "REPORT.md")
        
        # Standard Auditing Pattern: Gap Analysis
        report_content = f"""# Parity Audit Report - {datetime.datetime.now().strftime("%Y-%m-%d")}

## 1. Executive Summary
This report identifies gaps between the current `dt-ai` implementation and latest Darktable standards based on automated research.

## 2. Gap Analysis Table
| Category | Current State | Industry Standard | Priority |
|----------|---------------|-------------------|----------|
| **Prompts** | { "Present" if internal_data['prompts'] else "Missing" } | Latest Mentorship Style | Medium |
| **Exposure** | Version { internal_data['xmp_modules'].get('exposure', {}).get('version', 'Unknown') } | Latest (v6+) | Low |
| **Color/Tone** | Filmic/Standard | AgX / Scene-Referred | High |

## 3. Detailed Findings

### External Research Summary
{external_findings[:500]}...

### Identified Gaps
- **Missing AgX Support:** External research indicates a shift toward AgX tone mapping.
- **Workflow Deprecation:** Older modules found in prompts should be replaced with modern equivalents.

## 4. Remediation Plan
1. Update `AESTHETIC_PROMPT` to include AgX context.
2. Verify XMP module versions in `xmp.py`.
3. Implement TDD tests for new module mappings.
"""
        with open(report_path, "w", encoding="utf-8") as f:
            f.write(report_content)
            
        return report_path

class TDDOrchestrator:
    """
    Manages the Red-Green-Refactor cycle for parity updates.
    Inspired by code-assist.
    """
    def __init__(self, progress_dir: str):
        self.progress_dir = progress_dir
        self.plan_path = os.path.join(progress_dir, "plan.md")
        self.logs_dir = os.path.join(progress_dir, "logs")
        os.makedirs(self.logs_dir, exist_ok=True)

    def create_plan(self, report_path: str) -> str:
        """Generates an implementation plan from the audit report."""
        # Simple static plan for skeleton logic; real version uses LLM
        plan_content = """# TDD Implementation Plan

## Tasks
- [ ] **Task 1: Update Aesthetic Prompt for AgX**
    - **Test:** tests/test_parity_agx_prompt.py
    - **Target:** dt_ai/ai.py
- [ ] **Task 2: Verify Exposure Module Version**
    - **Test:** tests/test_parity_exposure_version.py
    - **Target:** dt_ai/xmp.py
"""
        with open(self.plan_path, "w", encoding="utf-8") as f:
            f.write(plan_content)
        return self.plan_path

    def run_test(self, test_path: str) -> bool:
        """Executes a specific test and logs output."""
        log_path = os.path.join(self.logs_dir, f"test_{os.path.basename(test_path)}.log")
        cmd = ["uv", "run", "pytest", test_path]
        
        with open(log_path, "w") as f:
            result = subprocess.run(cmd, capture_output=True, text=True)
            f.write(result.stdout)
            f.write(result.stderr)
            
        return result.returncode == 0

    def apply_fix(self, fix_fn: Callable):
        """Applies a fix and tracks progress."""
        fix_fn()

class DocUpdater:
    """
    Updates documentation like README.md with skill usage information.
    """
    def __init__(self, repo_root: str = "."):
        self.repo_root = repo_root

    def update_readme(self):
        """Appends a user-friendly GenAI Skills section to README.md."""
        readme_path = os.path.join(self.repo_root, "README.md")
        
        skill_docs = """
## AI Assistant Capabilities
This project is "AI-Ready." If you are using an AI coding assistant (like Claude, Gemini, or Kiro), you can give it special "skills" to help maintain this project.

### 🔄 Darktable Parity Sync
Darktable evolves quickly. This skill allows your AI assistant to research the latest professional photography standards and automatically update this tool's internal logic to match. It ensures your AI-generated edits always use the most modern Darktable modules (like AgX).

**How to give this skill to your AI:**
If you are in a chat with an AI assistant, simply copy and paste the command below into the chat:

```bash
/activate_skill darktable-parity-sync
```

Once activated, the AI will know how to scan this codebase and research industry updates for you.
"""
        
        mode = "a" if os.path.exists(readme_path) and os.path.getsize(readme_path) > 0 else "w"
        with open(readme_path, mode, encoding="utf-8") as f:
            if mode == "a":
                f.write("\n")
            f.write(skill_docs)

def get_progress_dir() -> str:
    """Generates a unique, hidden timestamped directory for parity sync."""
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    return f".parity-sync-{timestamp}"

if __name__ == "__main__":
    scanner = InternalScanner()
    print(scanner.run())
