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

class GetEmailThreadConversationsTool(Tool):
    """Tracks email threads by utilizing thread_id and reply relationships to recreate conversation flows."""

    @staticmethod
    def invoke(data: dict[str, Any], candidate_id: str = None, include_draft_responses: bool = False) -> str:
        if not candidate_id:
            return _err("candidate_id is required")

        emails = data.get("emails", {}).values()

        candidate_emails = [
            e
            for e in emails.values() if str(e.get("candidate_id_nullable")) == str(candidate_id)
        ]

        if not include_draft_responses:
            candidate_emails = [e for e in candidate_emails.values() if not e.get("draft_flag")]

        # Organize by thread_id
        threads = {}
        for email in candidate_emails:
            thread_id = email.get("thread_id_nullable")
            if thread_id:
                if thread_id not in threads:
                    threads[thread_id] = []
                threads[thread_id].append(email)

        # Arrange emails in each thread by date
        for thread_id in threads:
            threads[thread_id].sort(key=lambda e: e.get("date_ts", ""))
        payload = threads
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetEmailThreadConversations",
                "description": "Traces email threads using thread_id and reply relationships to reconstruct conversation flows.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {
                            "type": "string",
                            "description": "Target candidate",
                        },
                        "include_draft_responses": {
                            "type": "boolean",
                            "description": "Include unsent draft replies",
                        },
                    },
                    "required": ["candidate_id"],
                },
            },
        }
