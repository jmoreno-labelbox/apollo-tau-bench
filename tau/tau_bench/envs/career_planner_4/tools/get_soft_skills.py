# Copyright belongs to Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_soft_skills(Tool):
    @staticmethod
    def invoke(data, skill: str) -> str:
        return json.dumps(data.get("soft_skills", {}).get(skill, {}), indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "get_soft_skills",
                "description": "Return details for a specific soft skill.",
                "parameters": {
                    "type": "object",
                    "properties": {"skill": {"type": "string"}},
                    "required": ["skill"],
                },
            },
        }
