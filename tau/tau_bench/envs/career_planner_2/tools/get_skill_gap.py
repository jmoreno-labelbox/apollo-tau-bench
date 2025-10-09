from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class GetSkillGap(Tool):
    """Identify skills that a user lacks compared to the target role."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, target_role: str = None) -> str:
        for g in data.get("skill_gap_analysis", []):
            if g.get("user_id") == user_id and g.get("target_role") == target_role:
                payload = g.get("skill_gaps", [])
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": "Gap data not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSkillGap",
                "description": "Retrieve missing skills.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "target_role": {"type": "string"},
                    },
                    "required": ["user_id", "target_role"],
                },
            },
        }
