# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetEmailThreadConversationsTool(Tool):
    """Traces email threads using thread_id and reply relationships to reconstruct conversation flows."""

    @staticmethod
    def invoke(data: Dict[str, Any], candidate_id, include_draft_responses = False) -> str:
        include_drafts = include_draft_responses

        if not candidate_id:
            return _err("candidate_id is required")

        emails = data.get("emails", [])

        candidate_emails = [
            e for e in emails
            if str(e.get("candidate_id_nullable")) == str(candidate_id)
        ]

        if not include_drafts:
            candidate_emails = [e for e in candidate_emails if not e.get("draft_flag")]

        # Aggregate by thread_id
        threads = {}
        for email in candidate_emails:
            thread_id = email.get("thread_id_nullable")
            if thread_id:
                if thread_id not in threads:
                    threads[thread_id] = []
                threads[thread_id].append(email)

        # Organize emails in each thread chronologically.
        for thread_id in threads:
            threads[thread_id].sort(key=lambda e: e.get("date_ts", ""))

        return json.dumps(threads, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_email_thread_conversations",
                "description": "Traces email threads using thread_id and reply relationships to reconstruct conversation flows.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string", "description": "Target candidate"},
                        "include_draft_responses": {"type": "boolean", "description": "Include unsent draft replies"}
                    },
                    "required": ["candidate_id"],
                },
            },
        }
