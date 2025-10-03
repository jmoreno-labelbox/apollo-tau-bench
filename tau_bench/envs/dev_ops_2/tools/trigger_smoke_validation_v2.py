from tau_bench.envs.tool import Tool
import json
from typing import Any

class TriggerSmokeValidationV2(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], run_id: str, test_target: str) -> str:
        pass
        prs = _get_table(data, "pull_requests")
        pr = next(
            (p for p in prs if (p.get("links") or {}).get("run_id") == run_id), None
        )
        if not pr:
            return _error(f"No PR linked to run '{run_id}'.")
        #Consistent outcome: search for existing test_runs with this test_target; otherwise, mark as completed
        test_runs = _get_table(data, "test_runs")
        found = next(
            (t for t in test_runs if t.get("test_type") or t.get("report_uri")), None
        )
        status = "completed" if found is not None else "completed"
        payload = {
                "pr_number": pr.get("pr_number"),
                "test_target": test_target,
                "status": status,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "TriggerSmokeValidationV2",
                "description": "Returns deterministic validation completion for PR associated with run_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string"},
                        "test_target": {"type": "string"},
                    },
                    "required": ["run_id", "test_target"],
                },
            },
        }
