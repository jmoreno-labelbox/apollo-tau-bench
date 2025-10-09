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

class CheckEmailCommunicationGapsTool(Tool):
    """Examines the emails table to find candidates lacking anticipated communications (welcome, orientation, reminders)."""

    @staticmethod
    def invoke(data: dict[str, Any], candidate_id: str = None, expected_email_types: list = None) -> str:
        if not expected_email_types or not isinstance(expected_email_types, list):
            return _err("expected_email_types (array) is required")

        candidates_to_check = []
        if candidate_id:
            candidate = next(
                (
                    c
                    for c in data.get("candidates", {}).values()
                    if str(c.get("candidate_id")) == str(candidate_id)
                ),
                None,
            )
            if not candidate:
                return _err(f"Candidate '{candidate_id}' not found", code="not_found")
            data["candidates"][candidate_id] = candidate
        else:
            candidates_to_check = data.get("candidates", {}).values()

        emails = data.get("emails", {}).values()
        results = []
        for candidate in candidates_to_check:
            cid = str(candidate.get("candidate_id"))
            candidate_emails = [
                e for e in emails.values() if str(e.get("candidate_id_nullable")) == cid
            ]

            sent_email_subjects = [
                str(e.get("subject", "")).lower() for e in candidate_emails
            ]

            missing_types = []
            for email_type in expected_email_types:
                if not any(
                    email_type.lower().replace("_", " ") in subject
                    for subject in sent_email_subjects
                ):
                    missing_types.append(email_type)

            if missing_types:
                results.append(
                    {
                        "candidate_id": cid,
                        "candidate_name": candidate.get("candidate_name"),
                        "missing_email_types": missing_types,
                    }
                )
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CheckEmailCommunicationGaps",
                "description": "Analyzes emails table to identify candidates missing expected communications (welcome, orientation, reminders).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {
                            "type": "string",
                            "description": "Specific candidate or null for all",
                        },
                        "expected_email_types": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Email types to verify presence of",
                        },
                    },
                    "required": ["expected_email_types"],
                },
            },
        }
