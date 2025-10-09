from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any

class UpdateOutboundOrderDetails(Tool):
    """Modifies one or more fields for a particular outbound order."""

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None, notes: str = None,
    destination_address: Any = None,
    return_status: Any = None,
    status: Any = None,
    destination_city: str = None,
    destination_country: str = None,
    carrier_name: str = None,
    carrier_scac: str = None,
    ) -> str:
        if not order_id:
            payload = {"error": "order_id is a required argument."}
            out = json.dumps(payload)
            return out

        outbound_orders = data.get("outbound_orders", [])
        order_to_update = next(
            (o for o in outbound_orders if o.get("order_id") == order_id), None
        )

        if not order_to_update:
            payload = {"error": f"Order with ID '{order_id}' not found."}
            out = json.dumps(payload)
            return out

        updated_fields = []

        if notes is not None:
            original_note = order_to_update.get("notes", "")
            if original_note:
                order_to_update["notes"] = f"{original_note} | {notes}"
            else:
                order_to_update["notes"] = notes
            updated_fields.append("notes")

        if not updated_fields:
            payload = {"message": "No valid fields provided to update."}
            out = json.dumps(payload)
            return out
        payload = {
            "status": "success",
            "order_id": order_id,
            "updated_fields": updated_fields,
        }
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateOutboundOrderDetails",
                "description": "Updates details of an existing outbound order. Use this to change status, destination, or add notes.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "The unique ID of the order to update (e.g., 'ORD-0002').",
                        },
                        "destination_address": {
                            "type": "string",
                            "description": "The new destination street address.",
                        },
                        "destination_city": {
                            "type": "string",
                            "description": "The new destination city.",
                        },
                        "destination_country": {
                            "type": "string",
                            "description": "The new destination country.",
                        },
                        "status": {
                            "type": "string",
                            "description": "The new status of the order (e.g., 'Diverted', 'Cancelled').",
                        },
                        "notes": {
                            "type": "string",
                            "description": "A new note to append to the order's existing notes.",
                        },
                    },
                    "required": ["order_id"],
                },
            },
        }
