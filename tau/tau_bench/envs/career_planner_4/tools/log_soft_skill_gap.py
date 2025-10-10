# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class log_soft_skill_gap(Tool):
    @staticmethod
    def invoke(data, user_id: str, analysis: dict) -> str:
        data.setdefault("skill_gap_analysis", []).append(analysis)
        return json.dumps(
            {
                "success": f"Soft skill gap analysis {analysis['analysis_id']} logged for {user_id}"
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "log_soft_skill_gap",
                "description": "Add a soft-skill gap analysis record for a user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "analysis": {"type": "object"},
                    },
                    "required": ["user_id", "analysis"],
                },
            },
        }
