# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _find_one(collection: List[Dict[str, Any]], ) -> Optional[Dict[str, Any]]:
    for row in collection:
        if all(row.get(k) == v for k, v in filters.items()):
            return row
    return None

class GetEmployeeById(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id: str) -> str:
        emp = _find_one(data["employees"], employee_id=employee_id)
        return json.dumps({"status": "ok", "employee": emp})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_employee_by_id",
                "description": "Retrieve a single employee record by employee_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"employee_id": {"type": "string"}},
                    "required": ["employee_id"],
                },
            },
        }