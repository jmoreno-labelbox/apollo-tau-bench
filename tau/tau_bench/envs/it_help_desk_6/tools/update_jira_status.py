# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _find_one(collection: List[Dict[str, Any]], **filters: Any) -> Optional[Dict[str, Any]]:
    for row in collection:
        if all(row.get(k) == v for k, v in filters.items()):
            return row
    return None

class UpdateJiraStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], jira_id: str, status: str, updated_at: str) -> str:
        row = _find_one(data["jira_tickets"], jira_id=jira_id)
        if not row:
            return json.dumps({"status": "error", "reason": "jira_not_found"})
        row["status"] = status
        row["updated_at"] = updated_at
        return json.dumps({"status": "ok", "jira": row})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_jira_status",
                "description": "Update the status of a Jira ticket.",
                "parameters": {
                    "type": "object",
                    "properties": {"jira_id": {"type": "string"}, "status": {"type": "string"}, "updated_at": {"type": "string"}},
                    "required": ["jira_id", "status", "updated_at"],
                },
            },
        }