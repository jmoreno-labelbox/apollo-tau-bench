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

class ConsolidateEmailThreadsAndCleanupTool(Tool):
    """Organizes emails into threads and removes outdated drafts."""

    @staticmethod
    def invoke(data: dict[str, Any], candidate_id: str = None, draft_cleanup_age_days: int = 30) -> str:
        all_emails = data.get("emails", [])
        candidate_emails = [
            e for e in all_emails if e.get("candidate_id_nullable") == candidate_id
        ]
        updated_emails = []

        # Organizing by subject
        subject_groups = {}
        for email in candidate_emails:
            subject = str(email.get("subject", "")).strip()
            # Standardize subject by eliminating Re: Fwd: etc.
            clean_subject = re.sub(r"^(Re|Fwd|RE|FWD):\s*", "", subject)
            if clean_subject not in subject_groups:
                subject_groups[clean_subject] = []
            subject_groups[clean_subject].append(email)

        for subject, group in subject_groups.items():
            if len(group) > 1:
                thread_id = _generate_new_thread_id(all_emails)
                for email in group:
                    if not email.get("thread_id_nullable"):
                        email["thread_id_nullable"] = thread_id
                        updated_emails.append(email)

        # Remove outdated drafts
        for email in candidate_emails:
            if (
                email.get("draft_flag")
                and _days_between(email.get("date_ts", "0"), HARD_TS) > draft_cleanup_age_days
            ):
                email["draft_flag"] = False
                email["sent_flag"] = False  # It was not dispatched
                if email not in updated_emails:
                    updated_emails.append(email)
        payload = updated_emails
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "consolidateEmailThreadsAndCleanup",
                "description": "Groups emails into threads and cleans up old drafts.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "draft_cleanup_age_days": {"type": "integer"},
                    },
                    "required": ["candidate_id"],
                },
            },
        }
