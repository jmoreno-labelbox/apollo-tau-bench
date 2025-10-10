# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListAccessRequestsTool(Tool):
    """List access requests by status or resource."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        status = kwargs.get("status")
        res_id = kwargs.get("resource_id")
        reqs = data.get("access_requests", [])
        results = []
        for r in reqs:
            if status and r["status"] != status:
                continue
            if res_id and r["resource_id"] != res_id:
                continue
            results.append(r)
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_access_requests",
                "description": "List access requests filtered by status or resource",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {"type": "string"},
                        "resource_id": {"type": "string"}
                    }
                }
            }
        }
