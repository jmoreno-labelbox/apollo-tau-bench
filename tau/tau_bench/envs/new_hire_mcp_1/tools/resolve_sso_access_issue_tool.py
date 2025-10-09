from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ResolveSSOAccessIssueTool(Tool):
    """Imitates an IT intervention to address a failed SSO access verification for a candidate."""

    @staticmethod
    def invoke(data: dict[str, Any], candidate_id: str = None) -> str:
        if not candidate_id:
            return _err("candidate_id is required.")

        access_checks = data.get("access_checks", [])
        updated_checks = []

        # Locate and resolve the unsuccessful SSO verification
        sso_check = next(
            (
                ac
                for ac in access_checks
                if ac.get("candidate_id") == candidate_id
                and ac.get("system_name") == "SSO"
                and ac.get("status") == "Failed"
            ),
            None,
        )

        if not sso_check:
            return _err(
                f"No failed SSO access check found for candidate '{candidate_id}'.",
                code="not_found",
            )

        sso_check["status"] = "Success"
        sso_check["note_nullable"] = "Resolved by IT."
        sso_check["checked_ts"] = HARD_TS
        updated_checks.append(sso_check)

        # Refresh related systems
        dependent_systems = ["Slack", "GitHub"]
        for system in dependent_systems:
            dependent_check = next(
                (
                    ac
                    for ac in access_checks
                    if ac.get("candidate_id") == candidate_id
                    and ac.get("system_name") == system
                ),
                None,
            )
            if dependent_check and dependent_check.get("status") in [
                "Failed",
                "Pending",
            ]:
                dependent_check["status"] = "Pending"
                dependent_check["note_nullable"] = (
                    "Ready for re-check after SSO resolution."
                )
                dependent_check["checked_ts"] = HARD_TS
                updated_checks.append(dependent_check)
        payload = updated_checks
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ResolveSsoAccessIssue",
                "description": "Simulates an IT intervention to resolve a failed SSO access check for a candidate, updating their status to 'Success'.",
                "parameters": {
                    "type": "object",
                    "properties": {"candidate_id": {"type": "string"}},
                    "required": ["candidate_id"],
                },
            },
        }
