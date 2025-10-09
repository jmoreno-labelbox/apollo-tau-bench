from tau_bench.envs.tool import Tool
import json
from collections import Counter
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class get_document_compliance_status(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None) -> str:
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
            payload = {"employee_id": employee_id, "status": "No documents on file"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        docs = emp_doc_record.get("documents", [])
        doc_categories = {doc.get("category") for doc in docs}

        status = {
            "employee_id": employee_id,
            "has_nda": "NDA" in doc_categories,
            "has_id_verification": "ID Verification" in doc_categories,
            "document_count": len(docs),
        }
        payload = status
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetDocumentComplianceStatus",
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
