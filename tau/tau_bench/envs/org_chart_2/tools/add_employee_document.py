# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class add_employee_document(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], document: Dict[str, Any]) -> str:
        container = data.setdefault("employee_documents", [])
        target = next(
            (e for e in container if e["employee_id"] == document["employee_id"]), None
        )
        if target is None:
            target = {
                "employee_id": document["employee_id"],
                "name": "",
                "documents": [],
            }
            container.append(target)

        target["documents"].append(document)
        return json.dumps(
            {"success": f'doc {document.get("doc_id") or document.get("id")} added'},
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_employee_document",
                "description": "Attach a document object to the employee_documents nested list.",
                "parameters": {
                    "type": "object",
                    "properties": {"document": {"type": "object"}},
                    "required": ["document"],
                    "additionalProperties": False,
                },
            },
        }
