# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_document_compliance_status(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id) -> str:
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
            return json.dumps(
                {"employee_id": employee_id, "status": "No documents on file"}, indent=2
            )

        docs = emp_doc_record.get("documents", [])
        doc_categories = {doc.get("category") for doc in docs}

        status = {
            "employee_id": employee_id,
            "has_nda": "NDA" in doc_categories,
            "has_id_verification": "ID Verification" in doc_categories,
            "document_count": len(docs),
        }
        return json.dumps(status, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_document_compliance_status",
                "description": "Check if an employee has key required documents like an NDA and ID verification.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "department_id": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }
