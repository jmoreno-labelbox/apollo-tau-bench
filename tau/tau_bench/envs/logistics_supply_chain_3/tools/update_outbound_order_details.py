# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateOutboundOrderDetails(Tool):
    """Updates one or more fields for a specific outbound order."""

    @staticmethod
    def invoke(data: Dict[str, Any], order_id) -> str:
        if not order_id:
            return json.dumps({"error": "order_id is a required argument."})

        outbound_orders = list(data.get("outbound_orders", {}).values())
        order_to_update = next(
            (o for o in outbound_orders if o.get("order_id") == order_id), None
        )

        if not order_to_update:
            return json.dumps({"error": f"Order with ID '{order_id}' not found."})

        updated_fields = []

        # Loop through the fields that can be modified.
        for key, value in kwargs.items():
            if key == "order_id":
                continue

            if key == "notes":
                # Add a new note to the current notes.
                original_note = order_to_update.get("notes", "")
                if original_note:
                    order_to_update["notes"] = f"{original_note} | {value}"
                else:
                    order_to_update["notes"] = value
                updated_fields.append(key)
            elif key in order_to_update:
                order_to_update[key] = value
                updated_fields.append(key)

        if not updated_fields:
            return json.dumps({"message": "No valid fields provided to update."})

        return json.dumps(
            {
                "status": "success",
                "order_id": order_id,
                "updated_fields": updated_fields,
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_outbound_order_details",
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
