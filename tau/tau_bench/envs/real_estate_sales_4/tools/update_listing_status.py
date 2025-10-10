# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateListingStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        listing_id = kwargs.get('listing_id')
        new_status = kwargs.get('new_status')
        updated_by = kwargs.get('updated_by')
        
        if not all([listing_id, new_status, updated_by]):
            return json.dumps({
                "error": "listing_id, new_status, and updated_by are required"
            }, indent=2)
        
        result = {
            "success": True,
            "listing_id": listing_id,
            "previous_status": "for_sale",
            "new_status": new_status,
            "updated_by": updated_by,
            "updated_at": "2024-08-21T00:00:00Z"
        }
        
        return json.dumps(result, indent=2)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_listing_status",
                "description": "Update the status of a property listing",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "listing_id": {
                            "type": "integer",
                            "description": "Listing ID to update"
                        },
                        "new_status": {
                            "type": "string",
                            "description": "New status (for_sale, pending, sold, etc.)"
                        },
                        "updated_by": {
                            "type": "integer",
                            "description": "Broker ID making the update"
                        }
                    },
                    "required": ["listing_id", "new_status", "updated_by"]
                }
            }
        }
