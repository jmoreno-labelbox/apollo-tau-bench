# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPreferredSuppliers(Tool):
    """Tool to list suppliers with 'Preferred' relationship status."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        list_of_suppliers = kwargs.get("list_of_ids", None)
        suppliers = data.get("supplier_master", [])
        result = [s['supplier_id'] for s in suppliers if s["relationship_status"].lower() == "preferred"]
        if list_of_suppliers:
            result = [r for r in result if r in list_of_suppliers]
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_preferred_suppliers",
                "description": "List all suppliers with 'Preferred' relationship status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_of_ids": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "List of suppliers to choose from."
                        }
                    }
                }
            }
        }
