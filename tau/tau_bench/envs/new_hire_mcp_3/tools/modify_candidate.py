from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ModifyCandidate(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], updates: dict = None, candidate_id: str = None) -> str:
        updates = updates or {}
        candidates = data.get("candidates", [])

        # Locate the candidate within the list and modify
        for c in candidates:
            if c.get("candidate_id") == candidate_id:
                c.update(updates)
                c["updated_at"] = _fixed_now_iso()
                break
        else:
            payload = {"error": f"Candidate {candidate_id} not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = {"updated": updates}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCandidate",
                "description": "Update candidate details.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "updates": {"type": "object"},
                    },
                    "required": ["candidate_id", "updates"],
                },
            },
        }
