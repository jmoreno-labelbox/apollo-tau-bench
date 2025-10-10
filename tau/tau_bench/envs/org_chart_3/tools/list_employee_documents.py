# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class list_employee_documents(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id: str) -> str:
        container = data.get("employee_documents", [])
        target = next((e for e in container if e["employee_id"] == employee_id), None)
        docs = target["documents"] if target else []
        return json.dumps({"count": len(docs), "results": docs}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_employee_documents",
                "description": "Return the documents array for the specified employee_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"employee_id": {"type": "string"}},
                    "required": ["employee_id"],
                    "additionalProperties": False
                }
            }
        }
