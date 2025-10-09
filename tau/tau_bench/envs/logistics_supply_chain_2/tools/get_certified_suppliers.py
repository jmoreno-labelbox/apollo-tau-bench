from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetCertifiedSuppliers(Tool):
    """Utility for fetching suppliers based on a certification keyword."""

    @staticmethod
    def invoke(data: dict[str, Any], certification: str = "", list_of_ids: list = None) -> str:
        keyword = certification.lower()
        list_of_suppliers = list_of_ids
        suppliers = data.get("supplier_master", [])
        result = [
            s["supplier_id"]
            for s in suppliers
            if any(keyword in cert.lower() for cert in s.get("certifications", []))
        ]
        if list_of_suppliers:
            result = [r for r in result if r in list_of_suppliers]
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCertifiedSuppliers",
                "description": "Find suppliers that hold a specific certification.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "certification": {
                            "type": "string",
                            "description": "Certification name or keyword (e.g., 'ISO')",
                        },
                        "list_of_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of suppliers to choose from.",
                        },
                    },
                    "required": [],
                },
            },
        }
