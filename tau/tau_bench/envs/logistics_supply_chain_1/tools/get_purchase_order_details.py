from tau_bench.envs.tool import Tool
import json
import random
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetPurchaseOrderDetails(Tool):
    """Fetches details of an inbound shipment using its Purchase Order number."""

    @staticmethod
    def invoke(data: dict[str, Any], po_number: str = None) -> str:
        if not po_number:
            payload = {"error": "po_number is required."}
            out = json.dumps(payload, indent=2)
            return out

        shipment = next(
            (
                s
                for s in data.get("inbound_shipments", [])
                if s.get("purchase_order_number") == po_number
            ),
            None,
        )

        if not shipment:
            payload = {"error": f"Shipment for Purchase Order '{po_number}' not found."}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = shipment
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPurchaseOrderDetails",
                "description": "Retrieves the shipment details associated with a given Purchase Order (PO) number.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "po_number": {
                            "type": "string",
                            "description": "The Purchase Order number to search for.",
                        }
                    },
                    "required": ["po_number"],
                },
            },
        }
