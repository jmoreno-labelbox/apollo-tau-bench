from tau_bench.envs.tool import Tool
import json
from collections import Counter
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class upload_employee_document(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None, document_data: dict = None) -> str:
        main_container = data.get("employee_documents", {}).values().get(
            "employee_documents", []
        )

        emp_doc_record = next(
            (
                d
                for d in data.get("employee_documents", {}).values().get(
                    "employee_documents", []
                )
                if d.get("employee_id") == employee_id
            ),
            None,
        )
        if not emp_doc_record:
            employee = find_employee(data.get("employees", {}).values()), employee_id)
            employee_name = (
                f"{employee.get('first_name')} {employee.get('last_name')}"
                if employee
                else "Unknown"
            )

            emp_doc_record = {
                "employee_id": employee_id,
                "name": employee_name,
                "documents": [],
            }
            data["employee_documents"][emp_doc_record["employee_document_id"]] = emp_doc_record

        emp_doc_record["documents"].append(document_data)
        payload = {"success": f"Document uploaded for {employee_id}"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UploadEmployeeDocument",
                "description": "Upload or attach a new document to an employee's record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "document_data": {
                            "type": "object",
                            "description": "Document metadata and content",
                        },
                    },
                    "required": ["employee_id", "document_data"],
                },
            },
        }
