# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class list_department_headcount(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        department_id = kwargs.get("department_id")
        headcount = len(
            [
                e
                for e in list(data.get("employees", {}).values())
                if e.get("department_id") == department_id
                and e.get("status") == "Active"
            ]
        )
        return json.dumps(
            {"department_id": department_id, "active_headcount": headcount}, indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_department_headcount",
                "description": "Return current headcount of active employees for a department.",
                "parameters": {
                    "type": "object",
                    "properties": {"department_id": {"type": "string"}},
                    "required": ["department_id"],
                },
            },
        }
