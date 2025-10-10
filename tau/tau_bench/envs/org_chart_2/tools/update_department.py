# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class update_department(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], department_id: str, updates: Dict[str, Any]
    ) -> str:
        depts = list(data.get("departments", {}).values())
        changes = updates

        for d in depts:
            if d["department_id"] == department_id:
                d.update(changes)
                data["departments"] = depts
                return json.dumps(
                    {"success": f"department {department_id} updated"}, indent=2
                )

        return json.dumps(
            {"error": f"department_id {department_id} not found"}, indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_department",
                "description": "Patch mutable department attributes (head_id, budget …).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "department_id": {"type": "string"},
                        "updates": {"type": "object"},
                    },
                    "required": ["department_id", "updates"],
                    "additionalProperties": False,
                },
            },
        }
