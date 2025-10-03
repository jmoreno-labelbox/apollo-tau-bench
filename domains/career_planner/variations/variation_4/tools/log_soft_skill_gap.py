from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class LogSoftSkillGap(Tool):
    @staticmethod
    def invoke(data, user_id: str, analysis: dict) -> str:
        data.setdefault("skill_gap_analysis", []).append(analysis)
        payload = {
                "success": f"Soft skill gap analysis {analysis['analysis_id']} logged for {user_id}"
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "logSoftSkillGap",
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
