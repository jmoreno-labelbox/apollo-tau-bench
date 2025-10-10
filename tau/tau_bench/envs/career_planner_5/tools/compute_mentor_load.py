# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class compute_mentor_load(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], mentor_id: str) -> str:
        """Count active mentees for a mentor."""
        count = sum(
            1
            for rel in data.get("user_mentorship_relationships", [])
            if rel["mentor_id"] == mentor_id and rel["status"] == "Active"
        )
        return json.dumps({"current_mentees": count})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "compute_mentor_load",
                "description": "Return the number of active mentees a mentor currently has.",
                "parameters": {
                    "type": "object",
                    "properties": {"mentor_id": {"type": "string"}},
                    "required": ["mentor_id"],
                },
            },
        }
