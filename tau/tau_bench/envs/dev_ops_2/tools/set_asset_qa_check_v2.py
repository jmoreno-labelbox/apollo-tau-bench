from tau_bench.envs.tool import Tool
import json
from typing import Any

class SetAssetQaCheckV2(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], pr_number: int, conclusion: str, details_uri: str
    ) -> str:
        pass
        checks = _get_table(data, "test_results")
        check_id = f"check-{len(checks)+1}"
        checks.append(
            {
                "id": check_id,
                "pr_number": pr_number,
                "name": "Asset QA",
                "conclusion": conclusion,
                "details_uri": details_uri,
            }
        )
        payload = {"check_id": check_id}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetAssetQaCheckV2",
                "description": "Set the PR check for Asset QA deterministically.",
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
