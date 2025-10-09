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

class UpdateGmailThreadLabels(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        new_labels: list[str] = [],
        remove_labels: list[str] = [],
        status_notes: str = "",
        thread_id: str = None,
        update_recipients: list[str] = []
    ) -> str:
        """
        Modifies Gmail thread labels and oversees email workflow status.
        """
        if not thread_id:
            payload = {"error": "thread_id is required."}
            out = json.dumps(payload)
            return out

        gmail_threads = data.get("gmail_threads", [])

        # Locate the thread
        thread_found = False
        for thread in gmail_threads:
            if thread.get("thread_id") == thread_id:
                thread_found = True
                old_labels = thread.get("current_labels", []).copy()

                # Revise labels
                if new_labels:
                    for label in new_labels:
                        if label not in old_labels:
                            old_labels.append(label)

                if remove_labels:
                    for label in remove_labels:
                        if label in old_labels:
                            old_labels.remove(label)

                thread["current_labels"] = old_labels
                thread["updated_ts"] = datetime.now().isoformat()

                # Modify recipients if they are specified
                if update_recipients:
                    thread["recipients"] = update_recipients

                # Include notes regarding the status
                if status_notes:
                    if "status_history" not in thread:
                        thread["status_history"] = []
                    thread["status_history"].append(
                        {
                            "timestamp": datetime.now().isoformat(),
                            "action": "labels_updated",
                            "notes": status_notes,
                            "old_labels": thread.get("current_labels", []),
                            "new_labels": old_labels,
                        }
                    )

                break

        if not thread_found:
            payload = {"error": f"Gmail thread with ID '{thread_id}' not found."}
            out = json.dumps(payload)
            return out

        payload = {
            "success": True,
            "thread_id": thread_id,
            "old_labels": old_labels,
            "new_labels": old_labels,
            "updated_at": datetime.now().isoformat(),
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateGmailThreadLabels",
                "description": "Updates Gmail thread labels, recipients, and manages email workflow status with comprehensive tracking.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "thread_id": {
                            "type": "string",
                            "description": "The ID of the Gmail thread to update.",
                        },
                        "new_labels": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "New labels to add to the thread.",
                        },
                        "remove_labels": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Labels to remove from the thread.",
                        },
                        "update_recipients": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "New list of recipients for the thread.",
                        },
                        "status_notes": {
                            "type": "string",
                            "description": "Optional notes about the label update for tracking purposes.",
                        },
                    },
                    "required": ["thread_id"],
                },
            },
        }
