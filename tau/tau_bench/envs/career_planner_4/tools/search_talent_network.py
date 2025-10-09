from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class SearchTalentNetwork(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], candidate_id: str) -> str:
        talent_network = data.get("talent_network", [])
        for candidate in talent_network:
            if candidate.get("candidate_id") == candidate_id:
                payload = candidate
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": "Candidate not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "searchTalentNetwork",
                "description": "Search for an external candidate by candidate_id in the talent network.",
                "parameters": {
                    "type": "object",
                    "properties": {"candidate_id": {"type": "string"}},
                    "required": ["candidate_id"],
                },
            },
        }
