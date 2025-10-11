# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _get_table(data: Dict[str, Any], name: str) -> List[Dict[str, Any]]:
    return data.setdefault(name, [])

class OpenDraftPullRequest(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], head: str, base: str, title: str, body: str, run_id: str) -> str:
        prs = _get_table(data, "pull_requests")
        build_runs = _get_table(data, "build_runs")
        artifacts = _get_table(data, "artifacts")
        # Identify the highest current PR number, accommodating both 'number' (data file) and 'pr_number' (records from our tool).
        current_max = 0
        for p in prs:
            val = p.get("pr_number")
            if isinstance(val, int) and val > current_max:
                current_max = val
            val2 = p.get("number")
            if isinstance(val2, int) and val2 > current_max:
                current_max = val2
        pr_number = current_max + 1
        # Extract structured links from current entries.
        br = next((r for r in build_runs if r.get("run_id") == run_id), {})
        art = next((a for a in artifacts if a.get("run_id") == run_id), {})
        links = {
            "run_id": run_id,
            "logs_uri": br.get("logs_uri") or art.get("logs_uri"),
            "artifacts_uri": br.get("artifacts_uri") or art.get("reports_uri"),
        }
        record = {"pr_number": pr_number, "head": head, "base": base, "title": title, "body": body, "draft": True, "links": links}
        prs.append(record)
        return json.dumps({"pr_number": pr_number}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "open_draft_pull_request", "description": "Opens a draft pull request with deterministic pr_number sequencing.", "parameters": {"type": "object", "properties": {"head": {"type": "string"}, "base": {"type": "string"}, "title": {"type": "string"}, "body": {"type": "string"}, "run_id": {"type": "string"}}, "required": ["head", "base", "title", "body", "run_id"]}}}