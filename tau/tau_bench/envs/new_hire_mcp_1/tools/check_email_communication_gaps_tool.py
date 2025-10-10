# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CheckEmailCommunicationGapsTool(Tool):
    """Analyzes emails table to identify candidates missing expected communications (welcome, orientation, reminders)."""

    @staticmethod
    def invoke(data: Dict[str, Any], candidate_id, expected_email_types) -> str:

        if not expected_email_types or not isinstance(expected_email_types, list):
            return _err("expected_email_types (array) is required")

        candidates_to_check = []
        if candidate_id:
            candidate = next((c for c in data.get("candidates", []) if str(c.get("candidate_id")) == str(candidate_id)), None)
            if not candidate:
                return _err(f"Candidate '{candidate_id}' not found", code="not_found")
            candidates_to_check.append(candidate)
        else:
            candidates_to_check = data.get("candidates", [])

        emails = data.get("emails", [])
        results = []
        for candidate in candidates_to_check:
            cid = str(candidate.get("candidate_id"))
            candidate_emails = [e for e in emails if str(e.get("candidate_id_nullable")) == cid]

            sent_email_subjects = [str(e.get("subject", "")).lower() for e in candidate_emails]

            missing_types = []
            for email_type in expected_email_types:
                if not any(email_type.lower().replace("_", " ") in subject for subject in sent_email_subjects):
                    missing_types.append(email_type)

            if missing_types:
                results.append({
                    "candidate_id": cid,
                    "candidate_name": candidate.get("candidate_name"),
                    "missing_email_types": missing_types
                })

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "check_email_communication_gaps",
                "description": "Analyzes emails table to identify candidates missing expected communications (welcome, orientation, reminders).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string", "description": "Specific candidate or null for all"},
                        "expected_email_types": {"type": "array", "items": {"type": "string"}, "description": "Email types to verify presence of"}
                    },
                    "required": ["expected_email_types"],
                },
            },
        }
