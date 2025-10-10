# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class list_soft_skill_gap(Tool):
    @staticmethod
    def invoke(data, user_id: str, skill: str) -> str:
        analyses = [
            a
            for a in data.get("skill_gap_analysis", [])
            if a.get("skill") == skill and a.get("user_id", user_id) == user_id
        ]
        return json.dumps({"soft_skill_gap": analyses}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "list_soft_skill_gap",
                "description": "List soft skill gap analysis records for a user for a specific skill.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "skill": {"type": "string"},
                    },
                    "required": ["user_id", "skill"],
                },
            },
        }
