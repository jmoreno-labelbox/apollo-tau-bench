# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _get_table(data: Dict[str, Any], name: str) -> List[Dict[str, Any]]:
    return data.setdefault(name, [])

def _error(msg: str) -> str:
    return json.dumps({"error": msg}, indent=2)

class TriggerSmokeValidationV2(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], run_id: str, test_target: str) -> str:
        prs = _get_table(data, "pull_requests")
        pr = next((p for p in prs if (p.get("links") or {}).get("run_id") == run_id), None)
        if not pr:
            return _error(f"No PR linked to run '{run_id}'.")
        # Guaranteed outcome: search for existing test_runs associated with this test_target; if none, mark as completed.
        test_runs = _get_table(data, "test_runs")
        found = next((t for t in test_runs if t.get("test_type") or t.get("report_uri")), None)
        status = "completed" if found is not None else "completed"
        return json.dumps({"pr_number": pr.get("pr_number"), "test_target": test_target, "status": status}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "trigger_smoke_validation_v2", "description": "Returns deterministic validation completion for PR associated with run_id.", "parameters": {"type": "object", "properties": {"run_id": {"type": "string"}, "test_target": {"type": "string"}}, "required": ["run_id", "test_target"]}}}