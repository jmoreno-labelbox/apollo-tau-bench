from tau_bench.envs.tool import Tool
import json
import random
from typing import Any

class UpdateShipmentStatus(Tool):
    """Modifies the status and remarks of a specific inbound shipment."""

    @staticmethod
    def invoke(data: dict[str, Any], shipment_id: str = None, new_status: str = None, notes: str = None) -> str:
        if not all([shipment_id, new_status, notes]):
            payload = {"error": "shipment_id, new_status, and notes are required."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        shipment_to_update = next(
            (
                s
                for s in data.get("inbound_shipments", [])
                if s.get("shipment_id") == shipment_id
            ),
            None,
        )
        if not shipment_to_update:
            payload = {"error": f"Shipment '{shipment_id}' not found."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        shipment_to_update["status"] = new_status
        shipment_to_update["notes"] = notes
        payload = shipment_to_update
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateShipmentStatus",
                "description": "Updates the status and notes for a specific inbound shipment.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "shipment_id": {"type": "string"},
                        "new_status": {"type": "string"},
                        "notes": {"type": "string"},
                    },
                    "required": ["shipment_id", "new_status", "notes"],
                },
            },
        }
