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

class UpdateCandidateStatusFields(Tool):
    """Update permissible candidate fields (status, invitation timestamps, welcome message id, asset tag link, follow-up timestamp, etc.)."""

    @staticmethod
    def invoke(data: dict[str, Any], candidate_id: str, fields: dict[str, Any] = {}) -> str:
        cand_id = candidate_id
        for row in data.get("candidates", []):
            if row.get("candidate_id") == cand_id:
                for k, v in fields.items():
                    if v is None:
                        row[k] = None
                    else:
                        row[k] = v
                payload = {"candidate_id": cand_id, "updated_fields": list(fields.keys())}
                out = json.dumps(
                    payload, indent=2,
                )
                return out
        payload = {"error": f"candidate_id {cand_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCandidateStatusFields",
                "description": "Update selected candidate fields deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "fields": {"type": "object"},
                    },
                    "required": ["candidate_id", "fields"],
                },
            },
        }
