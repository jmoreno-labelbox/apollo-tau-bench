# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateGmailThreadPriority(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], new_priority, thread_id, escalate_to = [], urgency_reason = '') -> str:
        """
        Updates Gmail thread priority and manages thread workflow urgency.
        """

        if not all([thread_id, new_priority]):
            return json.dumps({"error": "thread_id and new_priority are required."})

        # Check the validity of priority values.
        valid_priorities = ['LOW', 'NORMAL', 'HIGH', 'URGENT', 'CRITICAL']
        if new_priority not in valid_priorities:
            return json.dumps({"error": f"Invalid priority. Must be one of: {', '.join(valid_priorities)}"})

        gmail_threads = list(data.get('gmail_threads', {}).values())

        # Locate the thread.
        thread_found = False
        for thread in gmail_threads:
            if thread.get('thread_id') == thread_id:
                thread_found = True
                old_priority = thread.get('priority', 'NORMAL')

                # Adjust thread priority.
                thread['priority'] = new_priority
                thread['updated_ts'] = datetime.now().isoformat()

                # Manage critical priority logic
                if new_priority in ['HIGH', 'URGENT', 'CRITICAL']:
                    thread['escalated_at'] = datetime.now().isoformat()
                    if urgency_reason:
                        thread['urgency_reason'] = urgency_reason
                    if escalate_to:
                        # Append escalation recipients to the current list of recipients.
                        current_recipients = thread.get('recipients', [])
                        for recipient in escalate_to:
                            if recipient not in current_recipients:
                                current_recipients.append(recipient)
                        thread['recipients'] = current_recipients

                # Record the modification in priority.
                if 'priority_history' not in thread:
                    thread['priority_history'] = []
                thread['priority_history'].append({
                    "from_priority": old_priority,
                    "to_priority": new_priority,
                    "changed_at": datetime.now().isoformat(),
                    "reason": urgency_reason
                })

                break

        if not thread_found:
            return json.dumps({"error": f"Gmail thread with ID '{thread_id}' not found."})

        return json.dumps({
            "success": True,
            "thread_id": thread_id,
            "old_priority": old_priority,
            "new_priority": new_priority,
            "updated_at": datetime.now().isoformat()
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_gmail_thread_priority",
                "description": "Updates Gmail thread priority and manages thread workflow urgency including escalation to additional recipients.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "thread_id": {"type": "string", "description": "The ID of the Gmail thread to update."},
                        "new_priority": {"type": "string", "description": "The new priority level. Must be one of: LOW, NORMAL, HIGH, URGENT, CRITICAL."},
                        "urgency_reason": {"type": "string", "description": "Optional reason for the priority change."},
                        "escalate_to": {"type": "array", "items": {"type": "string"}, "description": "Optional list of additional recipients to escalate to for high priority threads."}
                    },
                    "required": ["thread_id", "new_priority"]
                }
            }
        }
