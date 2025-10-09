from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetGmailThreadsByLabels(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        thread_id: str = None,
        labels: list[str] = [],
        sender_email: str = None,
        subject_keywords: list[str] = [],
        created_after: str = None,
        created_before: str = None
    ) -> str:
        """
        Obtains Gmail threads filtered by labels, sender, and additional criteria.
        """
        gmail_threads = data.get("gmail_threads", [])

        # Return the specific thread if thread_id is given
        if thread_id:
            for thread in gmail_threads:
                if thread.get("thread_id") == thread_id:
                    payload = thread
                    out = json.dumps(payload, indent=2)
                    return out
            payload = {"error": f"Thread with ID '{thread_id}' not found."}
            out = json.dumps(payload)
            return out

        # Sort threads based on specified criteria
        results = []
        for thread in gmail_threads:
            # Implement filters
            if labels:
                thread_labels = thread.get("current_labels", [])
                if not any(label in thread_labels for label in labels):
                    continue

            if sender_email:
                if thread.get("sender_identity") != sender_email:
                    continue

            if subject_keywords:
                subject = thread.get("subject", "").lower()
                if not any(keyword.lower() in subject for keyword in subject_keywords):
                    continue

            # Enforce date filters
            if created_after:
                thread_created = thread.get("created_ts", "")
                if thread_created < created_after:
                    continue

            if created_before:
                thread_created = thread.get("created_ts", "")
                if thread_created > created_before:
                    continue

            results.append(thread)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetGmailThreadsByLabels",
                "description": "Retrieves Gmail threads filtered by labels, sender email, subject keywords, and date ranges for comprehensive email workflow management.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "thread_id": {
                            "type": "string",
                            "description": "The ID of a specific thread to retrieve.",
                        },
                        "labels": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Filter by thread labels (e.g., ['design-review', 'urgent']).",
                        },
                        "sender_email": {
                            "type": "string",
                            "description": "Filter by sender email address.",
                        },
                        "subject_keywords": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Filter by keywords in subject line.",
                        },
                        "created_after": {
                            "type": "string",
                            "description": "Filter threads created after this ISO timestamp.",
                        },
                        "created_before": {
                            "type": "string",
                            "description": "Filter threads created before this ISO timestamp.",
                        },
                    },
                },
            },
        }
