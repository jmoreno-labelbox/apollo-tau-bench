# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListPolicyExceptionsTool(Tool):
    """List policy exceptions."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        status = kwargs.get("status")
        uid = kwargs.get("user_id")
        exes = data.get("policy_exceptions", [])
        results = []
        for e in exes:
            if status and e["status"] != status:
                continue
            if uid and e["user_id"] != uid:
                continue
            results.append(e)
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_policy_exceptions",
                "description": "List policy exceptions optionally filtered by status or user_id",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {"type": "string"},
                        "user_id": {"type": "string"}
                    }
                }
            }
        }
