# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_unused_employee_id(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        employees = list(data.get("employees", {}).values())
        used_ids = [e["employee_id"] for e in employees]
        for i in range(10000, 100000):
            if f"E{i:05d}" not in used_ids:
                return json.dumps(f"E{i:05d}", indent=2)
        return json.dumps({"error": "no unused employee ID found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_unused_employee_id",
                "description": "Return an employee ID that is not currently in use.",
                "parameters": {}
            }
        }
