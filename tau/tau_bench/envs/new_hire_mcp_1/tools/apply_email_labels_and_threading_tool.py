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

class ApplyEmailLabelsAndThreadingTool(Tool):
    """Refreshes existing records in the `emails` array by altering labels and thread IDs."""

    @staticmethod
    def invoke(data: dict[str, Any], label_assignments: dict = None, thread_assignments: dict = None) -> str:
        label_assignments = label_assignments or {}
        thread_assignments = thread_assignments or {}
        message_ids = set(label_assignments.keys()) | set(thread_assignments.keys())

        emails = data.get("emails", {}).values()
        labels_map = {l.get("label_id") for l in data.get("email_labels", {}).values()}
        updated_emails = []

        for msg_id in message_ids:
            email = next((e for e in emails.values() if e.get("message_id") == msg_id), None)
            if email:
                if msg_id in label_assignments:
                    valid_labels = [
                        l for l in label_assignments[msg_id] if l in labels_map
                    ]
                    email["labels_ids"] = valid_labels
                if msg_id in thread_assignments:
                    email["thread_id_nullable"] = thread_assignments[msg_id]
                updated_data["emails"][email["email_id"]] = email
        payload = updated_emails
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ApplyEmailLabelsAndThreading",
                "description": "Updates emails with specified labels and thread IDs.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "label_assignments": {"type": "object"},
                        "thread_assignments": {"type": "object"},
                    },
                    "required": [],
                },
            },
        }
