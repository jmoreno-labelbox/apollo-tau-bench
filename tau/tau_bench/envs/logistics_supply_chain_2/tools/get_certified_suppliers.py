# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCertifiedSuppliers(Tool):
    """Tool to filter suppliers by certification keyword."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        keyword = kwargs.get("certification", "").lower()
        list_of_suppliers = kwargs.get("list_of_ids", None)
        suppliers = data.get("supplier_master", [])
        result = [
            s['supplier_id'] for s in suppliers
            if any(keyword in cert.lower() for cert in s.get("certifications", []))
        ]
        if list_of_suppliers:
            result = [r for r in result if r in list_of_suppliers]
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_certified_suppliers",
                "description": "Find suppliers that hold a specific certification.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "certification": {
                            "type": "string",
                            "description": "Certification name or keyword (e.g., 'ISO')"
                        },
                        "list_of_ids": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "List of suppliers to choose from."
                        }
                    },
                    "required": []
                }
            }
        }
