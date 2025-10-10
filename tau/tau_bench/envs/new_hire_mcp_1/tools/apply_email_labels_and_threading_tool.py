# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ApplyEmailLabelsAndThreadingTool(Tool):
    """Updates existing records in `emails` array by modifying labels and thread IDs."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        label_assignments = kwargs.get("label_assignments", {})
        thread_assignments = kwargs.get("thread_assignments", {})
        message_ids = set(label_assignments.keys()) | set(thread_assignments.keys())

        emails = data.get("emails", [])
        labels_map = {l.get("label_id") for l in data.get("email_labels", [])}
        updated_emails = []

        for msg_id in message_ids:
            email = next((e for e in emails if e.get("message_id") == msg_id), None)
            if email:
                if msg_id in label_assignments:
                    valid_labels = [l for l in label_assignments[msg_id] if l in labels_map]
                    email["labels_ids"] = valid_labels
                if msg_id in thread_assignments:
                    email["thread_id_nullable"] = thread_assignments[msg_id]
                updated_emails.append(email)

        return json.dumps(updated_emails, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "apply_email_labels_and_threading",
                "description": "Updates emails with specified labels and thread IDs.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "label_assignments": {"type": "object"},
                        "thread_assignments": {"type": "object"}
                    },
                    "required": [],
                },
            },
        }
