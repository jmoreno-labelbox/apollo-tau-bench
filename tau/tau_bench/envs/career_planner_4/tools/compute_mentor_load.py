# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class compute_mentor_load(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], mentor_id: str) -> str:
        relationships = [
            r
            for r in data.get("user_mentorship_relationships", [])
            if r.get("mentor_id") == mentor_id and r.get("status") == "Active"
        ]
        load = len(relationships)
        return json.dumps({"mentor_load": load, "mentor_id": mentor_id}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "compute_mentor_load",
                "description": "Compute the current active mentee load for a mentor",
                "parameters": {
                    "type": "object",
                    "properties": {"mentor_id": {"type": "string"}},
                    "required": ["mentor_id"],
                },
            },
        }
