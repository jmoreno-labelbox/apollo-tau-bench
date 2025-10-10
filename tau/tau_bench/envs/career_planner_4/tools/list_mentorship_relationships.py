# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class list_mentorship_relationships(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], filters: dict) -> str:
        relationships = data.get("user_mentorship_relationships", [])
        if "mentor_id" in filters:
            relationships = [
                r for r in relationships if r.get("mentor_id") == filters["mentor_id"]
            ]
        if "status" in filters:
            relationships = [
                r for r in relationships if r.get("status") == filters["status"]
            ]
        return json.dumps({"relationships": relationships}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "list_mentorship_relationships",
                "description": "List mentorship relationships by filters",
                "parameters": {
                    "type": "object",
                    "properties": {"filters": {"type": "object"}},
                    "required": ["filters"],
                },
            },
        }
