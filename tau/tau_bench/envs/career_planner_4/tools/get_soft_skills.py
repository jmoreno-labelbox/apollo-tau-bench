from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class GetSoftSkills(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], skill: str) -> str:
        payload = data.get("soft_skills", {}).get(skill, {})
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "getSoftSkills",
                "description": "Return details for a specific soft skill.",
                "parameters": {
                    "type": "object",
                    "properties": {"skill": {"type": "string"}},
                    "required": ["skill"],
                },
            },
        }
