from tau_bench.envs.tool import Tool
import json
import random
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetReturnAuthorizationDetails(Tool):
    """Fetches details for a particular RMA."""

    @staticmethod
    def invoke(data: dict[str, Any], rma_id: str = None) -> str:
        if not rma_id:
            payload = {"error": "rma_id is required."}
            out = json.dumps(payload, indent=2)
            return out

        rma = next(
            (
                r
                for r in data.get("rma_authorizations", [])
                if r.get("rma_id") == rma_id
            ),
            None,
        )
        if not rma:
            payload = {"error": f"RMA '{rma_id}' not found."}
            out = json.dumps(payload, indent=2)
            return out
        payload = rma
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetReturnAuthorizationDetails",
                "description": "Retrieves the details of a specific Return Merchandise Authorization (RMA) by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "rma_id": {
                            "type": "string",
                            "description": "The RMA ID to search for.",
                        }
                    },
                    "required": ["rma_id"],
                },
            },
        }
