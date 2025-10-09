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

class UpdateAccessCheckStatusTool(Tool):
    """Refreshes the status of a particular system access verification for a candidate."""

    @staticmethod
    def invoke(data: dict[str, Any], candidate_id: str = None, system_name: str = None, new_status: str = None, note: str = None) -> str:
        if not all([candidate_id, system_name, new_status]):
            return _err("candidate_id, system_name, and new_status are required.")

        access_check = next(
            (
                ac
                for ac in data.get("access_checks", {}).values()
                if ac.get("candidate_id") == candidate_id
                and ac.get("system_name") == system_name
            ),
            None,
        )

        if not access_check:
            return _err(
                f"No access check found for candidate '{candidate_id}' and system '{system_name}'.",
                code="not_found",
            )

        access_check["status"] = new_status
        access_check["note_nullable"] = note
        access_check["checked_ts"] = HARD_TS
        payload = access_check
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAccessCheckStatus",
                "description": "Updates the status of a specific system access check for a candidate.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "system_name": {"type": "string"},
                        "new_status": {"type": "string"},
                        "note": {"type": "string"},
                    },
                    "required": ["candidate_id", "system_name", "new_status"],
                },
            },
        }
