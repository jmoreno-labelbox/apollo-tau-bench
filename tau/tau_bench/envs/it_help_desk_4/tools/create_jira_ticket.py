# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateJiraTicket(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        issue_type = kwargs.get("issue_type")
        summary = kwargs.get("summary")
        priority = kwargs.get("priority", "P2")
        tickets = data.setdefault("jira_tickets", [])
        jira_id = f"ITSD-{1001 + len(tickets)}"
        new_ticket = {"jira_id": jira_id, "issue_type": issue_type, "summary": summary, "priority": priority, "status": "To Do", "created_at": FIXED_NOW, "updated_at": FIXED_NOW}
        tickets.append(new_ticket)
        return json.dumps(new_ticket, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_jira_ticket", "description": "Create a Jira ticket for tracking issues.", "parameters": {"type": "object", "properties": {"issue_type": {"type": "string"}, "summary": {"type": "string"}, "priority": {"type": "string"}}, "required": ["issue_type", "summary"]}}}
