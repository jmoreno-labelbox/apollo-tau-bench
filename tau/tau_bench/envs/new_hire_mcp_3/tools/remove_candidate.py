from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class RemoveCandidate(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], candidate_id: str = None) -> str:
        candidates = data.get("candidates", {}).values()
        data["candidates"] = [
            c for c in candidates.values() if c.get("candidate_id") != candidate_id
        ]
        payload = {"removed_candidate_id": candidate_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "removeCandidate",
                "description": "Remove a candidate by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"candidate_id": {"type": "string"}},
                    "required": ["candidate_id"],
                },
            },
        }
