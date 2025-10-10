# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateJiraTicket(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        jira_id: str,
        issue_type: str,
        summary: str,
        priority: str,
        status: str,
        created_at: str,
        updated_at: Optional[str] = None,
    ) -> str:
        row = {
            "jira_id": jira_id,
            "issue_type": issue_type,
            "summary": summary,
            "priority": priority,
            "status": status,
            "created_at": created_at,
            "updated_at": updated_at or created_at,
        }
        _append_row(data["jira_tickets"], row)
        return json.dumps({"status": "ok", "jira": row})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_jira_ticket",
                "description": "Create a Jira ticket (e.g., License Shortage, Hardware Shortage, Incident).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "jira_id": {"type": "string"},
                        "issue_type": {"type": "string"},
                        "summary": {"type": "string"},
                        "priority": {"type": "string"},
                        "status": {"type": "string"},
                        "created_at": {"type": "string"},
                        "updated_at": {"type": "string"},
                    },
                    "required": ["jira_id", "issue_type", "summary", "priority", "status", "created_at"],
                },
            },
        }
