from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ListCandidateEmails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], candidate_id: str) -> str:
        cand_id = candidate_id
        rows = [
            e
            for e in data.get("emails", [])
            if e.get("candidate_id_nullable") == cand_id
        ]
        payload = {"emails": rows}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listCandidateEmails",
                "description": "List emails for a candidate.",
                "parameters": {
                    "type": "object",
                    "properties": {"candidate_id": {"type": "string"}},
                    "required": ["candidate_id"],
                },
            },
        }
