from tau_bench.envs.tool import Tool
import json
from typing import Any

class RunValidationChecks(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], pr_number: int, test_target: str) -> str:
        test_runs = _get_table(data, "test_runs")
        found = next(
            (
                t
                for t in test_runs
                if t.get("pr_number") == pr_number
                and t.get("test_target") == test_target
            ),
            None,
        )
        status = found.get("status") if found else "completed"
        result = {"pr_number": pr_number, "test_target": test_target, "status": status}
        payload = result
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RunValidationChecks",
                "description": "Returns a deterministic validation status for the PR based on existing test_runs rows.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pr_number": {"type": "integer"},
                        "test_target": {"type": "string"},
                    },
                    "required": ["pr_number", "test_target"],
                },
            },
        }
