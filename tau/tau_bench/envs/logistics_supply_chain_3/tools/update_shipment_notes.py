# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateShipmentNotes(Tool):
    """Updates the notes for a specific inbound shipment."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        shipment_id = kwargs.get("shipment_id")
        new_note = kwargs.get("new_note")
        inbound_shipments = list(data.get("inbound_shipments", {}).values())

        for shipment in inbound_shipments:
            if shipment.get("shipment_id") == shipment_id:
                original_note = shipment.get("notes")
                # Append new note to existing notes if they exist, separated by a pipe
                if original_note:
                    shipment["notes"] = f"{original_note} | {new_note}"
                else:
                    shipment["notes"] = new_note

                return json.dumps(
                    {
                        "status": "success",
                        "shipment_id": shipment_id,
                        "updated_notes": shipment["notes"],
                    }
                )
        return json.dumps({"error": "Shipment ID not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_shipment_notes",
                "description": "Updates the notes field for a specific inbound shipment record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "shipment_id": {
                            "type": "string",
                            "description": "The ID of the shipment to update (e.g., 'SHIP-0001').",
                        },
                        "new_note": {
                            "type": "string",
                            "description": "The new note to add to the shipment record.",
                        },
                    },
                    "required": ["shipment_id", "new_note"],
                },
            },
        }
