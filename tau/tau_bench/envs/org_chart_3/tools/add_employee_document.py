from tau_bench.envs.tool import Tool
import json
from typing import Any

class add_employee_document(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], document: dict[str, Any]) -> str:
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
        payload = {"success": f'doc {document.get("doc_id") or document.get("id")} added'}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddEmployeeDocument",
                "description": "Attach a document object to the employee_documents nested list.",
                "parameters": {
                    "type": "object",
                    "properties": {"document": {"type": "object"}},
                    "required": ["document"],
                    "additionalProperties": False,
                },
            },
        }
