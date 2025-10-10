# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetGmailThreadsByLabels(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], created_after, created_before, sender_email, thread_id, labels = [], subject_keywords = []) -> str:
        """
        Retrieves Gmail threads filtered by labels, sender, and other criteria.
        """

        gmail_threads = list(data.get('gmail_threads', {}).values())

        # Return the specified thread if thread_id is given.
        if thread_id:
            for thread in gmail_threads:
                if thread.get('thread_id') == thread_id:
                    return json.dumps(thread, indent=2)
            return json.dumps({"error": f"Thread with ID '{thread_id}' not found."})

        # Sort threads based on specified criteria.
        results = []
        for thread in gmail_threads:
            # Implement filters
            if labels:
                thread_labels = thread.get('current_labels', [])
                if not any(label in thread_labels for label in labels):
                    continue

            if sender_email:
                if thread.get('sender_identity') != sender_email:
                    continue

            if subject_keywords:
                subject = thread.get('subject', '').lower()
                if not any(keyword.lower() in subject for keyword in subject_keywords):
                    continue

            # Implement date filtering.
            if created_after:
                thread_created = thread.get('created_ts', '')
                if thread_created < created_after:
                    continue

            if created_before:
                thread_created = thread.get('created_ts', '')
                if thread_created > created_before:
                    continue

            results.append(thread)

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_gmail_threads_by_labels",
                "description": "Retrieves Gmail threads filtered by labels, sender email, subject keywords, and date ranges for comprehensive email workflow management.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "thread_id": {"type": "string", "description": "The ID of a specific thread to retrieve."},
                        "labels": {"type": "array", "items": {"type": "string"}, "description": "Filter by thread labels (e.g., ['design-review', 'urgent'])."},
                        "sender_email": {"type": "string", "description": "Filter by sender email address."},
                        "subject_keywords": {"type": "array", "items": {"type": "string"}, "description": "Filter by keywords in subject line."},
                        "created_after": {"type": "string", "description": "Filter threads created after this ISO timestamp."},
                        "created_before": {"type": "string", "description": "Filter threads created before this ISO timestamp."}
                    }
                }
            }
        }
