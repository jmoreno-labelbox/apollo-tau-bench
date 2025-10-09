from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class list_employee_documents(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str) -> str:
        container = data.get("employee_documents", [])
        target = next((e for e in container if e["employee_id"] == employee_id), None)
        docs = target["documents"] if target else []
        payload = {"count": len(docs), "results": docs}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListEmployeeDocuments",
                "description": "Return the documents array for the specified employee_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"employee_id": {"type": "string"}},
                    "required": ["employee_id"],
                    "additionalProperties": False,
                },
            },
        }
