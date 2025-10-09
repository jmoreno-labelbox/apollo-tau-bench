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

class UpdateCandidatesRecordTool(Tool):
    """Refreshes one or more fields for a collection of candidate records."""

    @staticmethod
    def invoke(data: dict[str, Any], candidate_ids: list = None, fields_to_update: dict = None) -> str:
        if not candidate_ids or not isinstance(candidate_ids, list):
            return _err("candidate_ids (array) is required")
        if not fields_to_update or not isinstance(fields_to_update, dict):
            return _err("fields_to_update (object) is required")

        candidates = data.get("candidates", {}).values()
        updated_candidates = []

        for candidate in candidates.values():
            if candidate.get("candidate_id") in candidate_ids:
                for field, value in fields_to_update.items():
                    if field in candidate:
                        candidate[field] = value
                updated_data["candidates"][candidate_id] = candidate
        payload = updated_candidates
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCandidatesRecord",
                "description": "Updates one or more fields for a list of candidate records. Useful for setting timestamps or notes after an action has been performed.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of candidate IDs to update.",
                        },
                        "fields_to_update": {
                            "type": "object",
                            "description": 'A dictionary of fields to update. e.g., {"checklist_follow_up_ts_nullable": "2024-08-15T12:00:00Z"}',
                        },
                    },
                    "required": ["candidate_ids", "fields_to_update"],
                },
            },
        }
