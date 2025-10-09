from tau_bench.envs.tool import Tool
import json
from typing import Any

class FindJiraTickets(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        issue_type: str | None = None,
        status: str | None = None,
        priority: str | None = None,
        summary: str | None = None,
    ) -> str:
        pass
        results = []
        for j in data["jira_tickets"].values():
            if issue_type and j["issue_type"] != issue_type:
                continue
            if status and j["status"] != status:
                continue
            if priority and j["priority"] != priority:
                continue
            if summary and summary not in j["summary"]:
                continue
            results.append(j)
        payload = {"status": "ok", "jira_tickets": results}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindJiraTickets",
                "description": "Find TaskTrack tickets filtered by type, status, priority, or summary substring.",
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
