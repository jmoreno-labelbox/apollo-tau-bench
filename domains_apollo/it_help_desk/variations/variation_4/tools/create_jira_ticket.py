from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateJiraTicket(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], issue_type: str = None, summary: str = None, priority: str = "P2") -> str:
        tickets = data.setdefault("jira_tickets", [])
        jira_id = f"ITSD-{1001 + len(tickets)}"
        new_ticket = {
            "jira_id": jira_id,
            "issue_type": issue_type,
            "summary": summary,
            "priority": priority,
            "status": "To Do",
            "created_at": FIXED_NOW,
            "updated_at": FIXED_NOW,
        }
        tickets.append(new_ticket)
        payload = new_ticket
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateJiraTicket",
                "description": "Create a Jira ticket for tracking issues.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "issue_type": {"type": "string"},
                        "summary": {"type": "string"},
                        "priority": {"type": "string"},
                    },
                    "required": ["issue_type", "summary"],
                },
            },
        }
