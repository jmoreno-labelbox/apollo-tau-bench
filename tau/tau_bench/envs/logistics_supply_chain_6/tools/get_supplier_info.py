from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetSupplierInfo(Tool):
    """Utility for retrieving details regarding a supplier."""

    @staticmethod
    def invoke(data: dict[str, Any], supplier_id: str) -> str:
        """Run the tool with the provided parameters."""
        suppliers = data.get("supplier_master", {}).values()
        for supplier in suppliers.values():
            if supplier.get("supplier_id") == supplier_id:
                payload = supplier
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Supplier with ID {supplier_id} not found"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        """Provide the specifications of the tool for the AI agent."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetSupplierInfo",
                "description": "Retrieves detailed information about a specific supplier.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "The ID of the supplier.",
                        }
                    },
                    "required": ["supplier_id"],
                },
            },
        }
