from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class SearchLogsTool(Tool):
    """Query system logs using search text."""

    @staticmethod
    def invoke(data: dict[str, Any], query: str = "", resource_id: str = None, since: str = None) -> str:
        logs = data.get("audit_logs", [])
        results = []
        for l in logs:
            details_val = l.get("details")
            # Perform the containment check solely if both are strings
            if not (
                isinstance(details_val, str)
                and isinstance(query, str)
                and query in details_val
            ):
                continue
            if resource_id and l.get("target_id") != resource_id:
                continue
            if since and l.get("timestamp") < since:
                continue
            results.append(l)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchLogs",
                "description": "Search logs by keyword, resource filter, and optional date cutoff",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string"},
                        "resource_id": {"type": "string"},
                        "since": {"type": "string"},
                    },
                    "required": ["query"],
                },
            },
        }
