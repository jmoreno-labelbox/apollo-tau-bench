from tau_bench.envs.tool import Tool
import json
from typing import Any

class UpdateListingStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], listing_id: str = None, new_status: str = None, updated_by: str = None) -> str:
        if not all([listing_id, new_status, updated_by]):
            payload = {"error": "listing_id, new_status, and updated_by are required"}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        result = {
            "success": True,
            "listing_id": listing_id,
            "previous_status": "for_sale",
            "new_status": new_status,
            "updated_by": updated_by,
            "updated_at": "2024-08-21T00:00:00Z",
        }
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateListingStatus",
                "description": "Update the status of a property listing",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "listing_id": {
                            "type": "integer",
                            "description": "Listing ID to update",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "New status (for_sale, pending, sold, etc.)",
                        },
                        "updated_by": {
                            "type": "integer",
                            "description": "Broker ID making the update",
                        },
                    },
                    "required": ["listing_id", "new_status", "updated_by"],
                },
            },
        }
