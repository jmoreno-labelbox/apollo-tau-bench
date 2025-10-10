# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class search_employees(Tool):
    """
    Performs simple AND-style filtering on any top-level employee fields
    (e.g. {"department_id": "DEPT1001", "status": "Active"}).
    """

    @staticmethod
    def invoke(data: Dict[str, Any], filters: Dict[str, Any]) -> str:
        employees = list(data.get("employees", {}).values())
        hits = [
            e for e in employees
            if all(e.get(k) == v for k, v in filters.items())
        ]
        return json.dumps({"count": len(hits), "results": hits}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_employees",
                "description": "Return employees' full records that match ALL supplied attribute/value pairs.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "filters": {
                            "type": "object",
                            "description": "Key/value pairs to filter on (case-sensitive match)"
                        }
                    },
                    "required": ["filters"],
                    "additionalProperties": False
                }
            }
        }
