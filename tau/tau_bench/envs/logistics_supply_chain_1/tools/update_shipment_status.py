# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateShipmentStatus(Tool):
    """Updates the status and notes of a specific inbound shipment."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        shipment_id = kwargs.get('shipment_id')
        new_status = kwargs.get('new_status')
        notes = kwargs.get('notes')
        if not all([shipment_id, new_status, notes]):
            return json.dumps({"error": "shipment_id, new_status, and notes are required."}, indent=2)
        shipment_to_update = next((s for s in data.get('inbound_shipments', []) if s.get('shipment_id') == shipment_id), None)
        if not shipment_to_update:
            return json.dumps({"error": f"Shipment '{shipment_id}' not found."}, indent=2)
        shipment_to_update['status'] = new_status
        shipment_to_update['notes'] = notes
        return json.dumps(shipment_to_update, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_shipment_status", "description": "Updates the status and notes for a specific inbound shipment.", "parameters": {"type": "object", "properties": {"shipment_id": {"type": "string"}, "new_status": {"type": "string"}, "notes": {"type": "string"}}, "required": ["shipment_id", "new_status", "notes"]}}}
