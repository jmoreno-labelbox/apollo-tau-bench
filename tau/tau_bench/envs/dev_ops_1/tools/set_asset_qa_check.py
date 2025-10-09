from tau_bench.envs.tool import Tool
import json
from typing import Any

class SetAssetQaCheck(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], pr_number: int, conclusion: str, details_uri: str
    ) -> str:
        prs = _get_table(data, "pull_requests")
        pr = next((p for p in prs if p.get("pr_number") == pr_number), None)
        if not pr:
            return _error(f"PR '{pr_number}' not found.")
        checks = pr.setdefault("checks", [])
        checks.append(
            {"name": "Asset QA", "conclusion": conclusion, "details_uri": details_uri}
        )
        payload = {"check_count": len(checks)}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetAssetQaCheck",
                "description": "Sets a deterministic PR check result named 'Asset QA'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pr_number": {"type": "integer"},
                        "conclusion": {"type": "string"},
                        "details_uri": {"type": "string"},
                    },
                    "required": ["pr_number", "conclusion", "details_uri"],
                },
            },
        }
