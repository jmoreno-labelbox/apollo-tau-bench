# Copyright Sierra

import datetime
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateGmailThreadLabels(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], thread_id, new_labels = [], remove_labels = [], status_notes = '', update_recipients = []) -> str:
        """
        Updates Gmail thread labels and manages email workflow status.
        """

        if not thread_id:
            return json.dumps({"error": "thread_id is required."})

        gmail_threads = list(data.get('gmail_threads', {}).values())

        # Locate the thread.
        thread_found = False
        for thread in gmail_threads:
            if thread.get('thread_id') == thread_id:
                thread_found = True
                old_labels = thread.get('current_labels', []).copy()

                # Revise labels
                if new_labels:
                    for label in new_labels:
                        if label not in old_labels:
                            old_labels.append(label)

                if remove_labels:
                    for label in remove_labels:
                        if label in old_labels:
                            old_labels.remove(label)

                thread['current_labels'] = old_labels
                thread['updated_ts'] = datetime.now().isoformat()

                # Modify recipients if available
                if update_recipients:
                    thread['recipients'] = update_recipients

                # Include status updates.
                if status_notes:
                    if 'status_history' not in thread:
                        thread['status_history'] = []
                    thread['status_history'].append({
                        "timestamp": datetime.now().isoformat(),
                        "action": "labels_updated",
                        "notes": status_notes,
                        "old_labels": thread.get('current_labels', []),
                        "new_labels": old_labels
                    })

                break

        if not thread_found:
            return json.dumps({"error": f"Gmail thread with ID '{thread_id}' not found."})

        return json.dumps({
            "success": True,
            "thread_id": thread_id,
            "old_labels": old_labels,
            "new_labels": old_labels,
            "updated_at": datetime.now().isoformat()
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_gmail_thread_labels",
                "description": "Updates Gmail thread labels, recipients, and manages email workflow status with comprehensive tracking.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "thread_id": {"type": "string", "description": "The ID of the Gmail thread to update."},
                        "new_labels": {"type": "array", "items": {"type": "string"}, "description": "New labels to add to the thread."},
                        "remove_labels": {"type": "array", "items": {"type": "string"}, "description": "Labels to remove from the thread."},
                        "update_recipients": {"type": "array", "items": {"type": "string"}, "description": "New list of recipients for the thread."},
                        "status_notes": {"type": "string", "description": "Optional notes about the label update for tracking purposes."}
                    },
                    "required": ["thread_id"]
                }
            }
        }
