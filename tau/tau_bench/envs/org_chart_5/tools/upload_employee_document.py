# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class upload_employee_document(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        employee_id = kwargs.get("employee_id")
        document_data = kwargs.get("document_data")
        main_container = data.get("employee_documents", {}).get(
            "employee_documents", []
        )

        emp_doc_record = next(
            (
                d
                for d in data.get("employee_documents", {}).get(
                    "employee_documents", []
                )
                if d.get("employee_id") == employee_id
            ),
            None,
        )
        if not emp_doc_record:
            employee = find_employee(list(data.get("employees", {}).values()), employee_id)
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
            main_container.append(emp_doc_record)

        emp_doc_record["documents"].append(document_data)
        return json.dumps({"success": f"Document uploaded for {employee_id}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "upload_employee_document",
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
