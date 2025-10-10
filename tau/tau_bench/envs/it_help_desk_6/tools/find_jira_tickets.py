# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindJiraTickets(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        issue_type: Optional[str] = None,
        status: Optional[str] = None,
        priority: Optional[str] = None,
        summary: Optional[str] = None,
    ) -> str:
        results = []
        for j in data["jira_tickets"]:
            if issue_type and j["issue_type"] != issue_type:
                continue
            if status and j["status"] != status:
                continue
            if priority and j["priority"] != priority:
                continue
            if summary and summary not in j["summary"]:
                continue
            results.append(j)
        return json.dumps({"status": "ok", "jira_tickets": results})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_jira_tickets",
                "description": "Find Jira tickets filtered by type, status, priority, or summary substring.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "issue_type": {"type": "string"},
                        "status": {"type": "string"},
                        "priority": {"type": "string"},
                        "summary": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }
