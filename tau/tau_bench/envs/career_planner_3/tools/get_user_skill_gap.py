# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUserSkillGap(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], target_role, user_id) -> str:
        gaps = data.get("skill_gap_analysis", [])
        result = [
            g
            for g in gaps
            if g["user_id"] == user_id and g["target_role"] == target_role
        ]

        if not result:
            return json.dumps(
                {
                    "error": "No skill gap found",
                    "user_id": user_id,
                    "target_role": target_role,
                    "available_analyses": [
                        f"{g['user_id']} -> {g['target_role']}" for g in gaps
                    ],
                },
                indent=2,
            )

        return json.dumps(result[0], indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_skill_gap",
                "description": "Gets the skill gap for a user targeting a specific role.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the user.",
                        },
                        "target_role": {
                            "type": "string",
                            "description": "The role the user wants to target.",
                        },
                    },
                    "required": ["user_id", "target_role"],
                },
            },
        }
