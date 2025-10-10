# Copyright by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchLogsTool(Tool):
    """Search system logs by query text."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        query = kwargs.get("query") or ""
        res_id = kwargs.get("resource_id")
        since = kwargs.get("since")
        logs = data.get("audit_logs", [])
        results = []
        for l in logs:
            details_val = l.get("details")
            # Perform the containment check only if both variables are of type str.
            if not (isinstance(details_val, str) and isinstance(query, str) and query in details_val):
                continue
            if res_id and l.get("target_id") != res_id:
                continue
            if since and l.get("timestamp") < since:
                continue
            results.append(l)
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_logs",
                "description": "Search logs by keyword, resource filter, and optional date cutoff",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string"},
                        "resource_id": {"type": "string"},
                        "since": {"type": "string"}
                    },
                    "required": ["query"]
                }
            }
        }
