# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class list_user_certifications(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str) -> str:
        certs = [
            c for c in data.get("user_certification", []) if c.get("user_id") == user_id
        ]
        return json.dumps({"certifications": certs}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "list_user_certifications",
                "description": "List certifications for a user",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }
