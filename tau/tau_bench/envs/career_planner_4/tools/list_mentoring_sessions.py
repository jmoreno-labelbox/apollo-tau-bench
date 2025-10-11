# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class list_mentoring_sessions(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], mentee_id: str) -> str:
        sessions = [
            s
            for s in data.get("mentoring_sessions", [])
            if s.get("mentee_id") == mentee_id
        ]
        return json.dumps({"sessions": sessions}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "list_mentoring_sessions",
                "description": "List mentoring sessions for a mentee",
                "parameters": {
                    "type": "object",
                    "properties": {"mentee_id": {"type": "string"}},
                    "required": ["mentee_id"],
                },
            },
        }
