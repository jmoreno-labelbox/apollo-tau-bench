# Copyright Sierra

import re, datetime
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _generate_new_thread_id(emails: List[Dict[str, Any]]) -> str:
    """Generates a new sequential thread ID."""
    max_id = 0
    for email in emails:
        thread_id = email.get("thread_id_nullable")
        if thread_id and thread_id.startswith("thread_"):
            try:
                num_part = int(thread_id.split('_')[1])
                if num_part > max_id:
                    max_id = num_part
            except (ValueError, IndexError):
                continue
    return f"thread_{max_id + 1}"

def _days_between(d1_str: str, d2_str: str) -> int:
    """A deterministic way to calculate days between two ISO date strings."""
    try:
        # Assumes ISO format with 'Z' for UTC
        d1 = datetime.fromisoformat(d1_str.replace("Z", "+00:00"))
        d2 = datetime.fromisoformat(d2_str.replace("Z", "+00:00"))
        return abs((d2 - d1).days)
    except (ValueError, TypeError):
        return 9999  # Return a large number for invalid formats

class ConsolidateEmailThreadsAndCleanupTool(Tool):
    """Groups emails into threads and cleans up old drafts."""

    @staticmethod
    def invoke(data: Dict[str, Any], candidate_id, draft_cleanup_age_days = 30) -> str:
        age_days = draft_cleanup_age_days

        all_emails = data.get("emails", [])
        candidate_emails = [e for e in all_emails if e.get("candidate_id_nullable") == candidate_id]
        updated_emails = []

        # Organizing by topic
        subject_groups = {}
        for email in candidate_emails:
            subject = str(email.get("subject", "")).strip()
            # Standardize the subject line by eliminating prefixes like Re: and Fwd:.
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
            if email.get("draft_flag") and _days_between(email.get("date_ts", "0"), HARD_TS) > age_days:
                email["draft_flag"] = False
                email["sent_flag"] = False # It was not dispatched.
                if email not in updated_emails:
                    updated_emails.append(email)

        return json.dumps(updated_emails, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function", "function": {"name": "consolidate_email_threads_and_cleanup",
            "description": "Groups emails into threads and cleans up old drafts.",
            "parameters": {"type": "object", "properties": {
                "candidate_id": {"type": "string"}, "draft_cleanup_age_days": {"type": "integer"}
            }, "required": ["candidate_id"]}}}