from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetCandidateWithFullContextTool(Tool):
    """Fetches candidate record along with all associated emails, asset requests, checklist items, and access checks for a complete overview."""

    @staticmethod
    def invoke(data: dict[str, Any], candidate_id: str = None) -> str:
        if not candidate_id:
            return _err("candidate_id is required")

        candidates = data.get("candidates", {}).values()
        candidate = next(
            (c for c in candidates.values() if str(c.get("candidate_id")) == str(candidate_id)),
            None,
        )

        if not candidate:
            return _err(
                f"Candidate with id '{candidate_id}' not found", code="not_found"
            )

        result = {
            "candidate": candidate,
            "emails": [
                e
                for e in data.get("emails", {}).values()
                if str(e.get("candidate_id_nullable")) == str(candidate_id)
            ],
            "asset_requests": [
                ar
                for ar in data.get("asset_requests", {}).values()
                if str(ar.get("candidate_id")) == str(candidate_id)
            ],
            "checklist_items": [
                ci
                for ci in data.get("checklist_items", {}).values()
                if str(ci.get("candidate_id")) == str(candidate_id)
            ],
            "access_checks": [
                ac
                for ac in data.get("access_checks", {}).values()
                if str(ac.get("candidate_id")) == str(candidate_id)
            ],
        }
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCandidateWithFullContext",
                "description": "Retrieves candidate record with all linked emails, asset requests, checklist items, and access checks for comprehensive view.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {
                            "type": "string",
                            "description": "Target candidate identifier",
                        }
                    },
                    "required": ["candidate_id"],
                },
            },
        }
