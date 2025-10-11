# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateAccessCheckStatusTool(Tool):
    """Updates the status of a specific system access check for a candidate."""

    @staticmethod
    def invoke(data: Dict[str, Any], candidate_id, new_status, note, system_name) -> str:

        if not all([candidate_id, system_name, new_status]):
            return _err("candidate_id, system_name, and new_status are required.")

        access_check = next((ac for ac in data.get("access_checks", []) if ac.get("candidate_id") == candidate_id and ac.get("system_name") == system_name), None)

        if not access_check:
            return _err(f"No access check found for candidate '{candidate_id}' and system '{system_name}'.", code="not_found")

        access_check["status"] = new_status
        access_check["note_nullable"] = note
        access_check["checked_ts"] = HARD_TS

        return json.dumps(access_check, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_access_check_status",
                "description": "Updates the status of a specific system access check for a candidate.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "system_name": {"type": "string"},
                        "new_status": {"type": "string"},
                        "note": {"type": "string"}
                    },
                    "required": ["candidate_id", "system_name", "new_status"],
                },
            },
        }
