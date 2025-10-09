from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class UpdateGmailThreadPriority(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], thread_id: str = None, new_priority: str = None, urgency_reason: str = "", escalate_to: list = []) -> str:
        """
        Changes Gmail thread priority and oversees the urgency of thread workflow.
        """
        if not all([thread_id, new_priority]):
            payload = {"error": "thread_id and new_priority are required."}
            out = json.dumps(payload)
            return out

        # Check the correctness of priority values
        valid_priorities = ["LOW", "NORMAL", "HIGH", "URGENT", "CRITICAL"]
        if new_priority not in valid_priorities:
            payload = {
                "error": f"Invalid priority. Must be one of: {', '.join(valid_priorities)}"
            }
            out = json.dumps(payload)
            return out

        gmail_threads = data.get("gmail_threads", [])

        # Locate the thread
        thread_found = False
        for thread in gmail_threads:
            if thread.get("thread_id") == thread_id:
                thread_found = True
                old_priority = thread.get("priority", "NORMAL")

                # Change the priority of the thread
                thread["priority"] = new_priority
                thread["updated_ts"] = datetime.now().isoformat()

                # Manage logic for high priority
                if new_priority in ["HIGH", "URGENT", "CRITICAL"]:
                    thread["escalated_at"] = datetime.now().isoformat()
                    if urgency_reason:
                        thread["urgency_reason"] = urgency_reason
                    if escalate_to:
                        # Include escalation recipients with current recipients
                        current_recipients = thread.get("recipients", [])
                        for recipient in escalate_to:
                            if recipient not in current_recipients:
                                current_recipients.append(recipient)
                        thread["recipients"] = current_recipients

                # Document the change in priority
                if "priority_history" not in thread:
                    thread["priority_history"] = []
                thread["priority_history"].append(
                    {
                        "from_priority": old_priority,
                        "to_priority": new_priority,
                        "changed_at": datetime.now().isoformat(),
                        "reason": urgency_reason,
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
            "old_priority": old_priority,
            "new_priority": new_priority,
            "updated_at": datetime.now().isoformat(),
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateGmailThreadPriority",
                "description": "Updates Gmail thread priority and manages thread workflow urgency including escalation to additional recipients.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "thread_id": {
                            "type": "string",
                            "description": "The ID of the Gmail thread to update.",
                        },
                        "new_priority": {
                            "type": "string",
                            "description": "The new priority level. Must be one of: LOW, NORMAL, HIGH, URGENT, CRITICAL.",
                        },
                        "urgency_reason": {
                            "type": "string",
                            "description": "Optional reason for the priority change.",
                        },
                        "escalate_to": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Optional list of additional recipients to escalate to for high priority threads.",
                        },
                    },
                    "required": ["thread_id", "new_priority"],
                },
            },
        }
