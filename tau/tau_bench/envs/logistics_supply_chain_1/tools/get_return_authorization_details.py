# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetReturnAuthorizationDetails(Tool):
    """Retrieves details of a specific RMA."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        rma_id = kwargs.get('rma_id')
        if not rma_id:
            return json.dumps({"error": "rma_id is required."}, indent=2)

        rma = next((r for r in data.get('rma_authorizations', []) if r.get('rma_id') == rma_id), None)
        if not rma:
            return json.dumps({"error": f"RMA '{rma_id}' not found."}, indent=2)

        return json.dumps(rma, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_return_authorization_details",
                "description": "Retrieves the details of a specific Return Merchandise Authorization (RMA) by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"rma_id": {"type": "string", "description": "The RMA ID to search for."}},
                    "required": ["rma_id"]
                }
            }
        }
