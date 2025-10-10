# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class list_compensations(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id: str) -> str:
        all_compensations = data.get("compensation_records", [])
        history = [
            comp for comp in all_compensations
            if comp.get("employee_id") == employee_id
        ]
        if not history:
            return json.dumps({"count": 0, "results": []}, indent=2)
        history.sort(key=lambda c: c.get("effective_date", ""), reverse=True)
        return json.dumps({"count": len(history), "results": history}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_compensations",
                "description": "Return an employee's full compensation history, sorted from most to least recent.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The ID of the employee."
                        }
                    },
                    "required": ["employee_id"],
                },
            },
        }
