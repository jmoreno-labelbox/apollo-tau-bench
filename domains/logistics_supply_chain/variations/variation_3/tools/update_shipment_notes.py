from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any

class UpdateShipmentNotes(Tool):
    """Revises the notes for a particular inbound shipment."""

    @staticmethod
    def invoke(data: dict[str, Any], shipment_id: str = None, new_note: str = None) -> str:
        inbound_shipments = data.get("inbound_shipments", [])

        for shipment in inbound_shipments:
            if shipment.get("shipment_id") == shipment_id:
                original_note = shipment.get("notes")
                if original_note:
                    shipment["notes"] = f"{original_note} | {new_note}"
                else:
                    shipment["notes"] = new_note
                payload = {
                    "status": "success",
                    "shipment_id": shipment_id,
                    "updated_notes": shipment["notes"],
                }
                out = json.dumps(payload)
                return out
        payload = {"error": "Shipment ID not found"}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateShipmentNotes",
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
