from tau_bench.envs.tool import Tool
import json
from typing import Any

class ComputeSituationalSplits(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], **kwargs) -> str:
        pass
        team_id = kwargs.get("team_id")
        kwargs.get("situations", [])
        payload = {"situational_splits": f"splits_data_team_{team_id}"}
        out = json.dumps(
            payload, indent=2
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "computeSituationalSplits",
                "description": "Computes situational performance splits for a team.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {"type": "integer"},
                        "situations": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["team_id"],
                },
            },
        }
