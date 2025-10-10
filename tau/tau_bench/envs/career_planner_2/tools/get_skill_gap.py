# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetSkillGap(Tool):
    """List missing skills for a user vs target role."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        uid = kwargs.get("user_id")
        role = kwargs.get("target_role")
        for g in data.get("skill_gap_analysis", []):
            if g.get("user_id") == uid and g.get("target_role") == role:
                return json.dumps(g.get("skill_gaps", []), indent=2)
        return json.dumps({"error": "Gap data not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_skill_gap",
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
