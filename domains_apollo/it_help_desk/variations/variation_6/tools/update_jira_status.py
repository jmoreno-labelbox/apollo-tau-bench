from tau_bench.envs.tool import Tool
import json
from typing import Any

class UpdateJiraStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], jira_id: str, status: str, updated_at: str) -> str:
        pass
        row = _find_one(data["jira_tickets"], jira_id=jira_id)
        if not row:
            payload = {"status": "error", "reason": "jira_not_found"}
            out = json.dumps(payload)
            return out
        row["status"] = status
        row["updated_at"] = updated_at
        payload = {"status": "ok", "jira": row}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateJiraStatus",
                "description": "Update the status of a TaskTrack ticket.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "jira_id": {"type": "string"},
                        "status": {"type": "string"},
                        "updated_at": {"type": "string"},
                    },
                    "required": ["jira_id", "status", "updated_at"],
                },
            },
        }
