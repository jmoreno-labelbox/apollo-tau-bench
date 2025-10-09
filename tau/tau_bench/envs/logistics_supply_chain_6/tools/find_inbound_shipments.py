from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class FindInboundShipments(Tool):
    """Utility for locating inbound shipments according to specified criteria."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        status: str | None = None,
        supplier_id: str | None = None,
        warehouse_id: str | None = None
    ) -> str:
        """Run the tool using the specified parameters."""
        shipments = data.get("inbound_shipments", [])
        results = []
        for shipment in shipments:
            if (
                (not status or shipment.get("status") == status)
                and (not supplier_id or shipment.get("supplier_id") == supplier_id)
                and (
                    not warehouse_id
                    or shipment.get("destination_warehouse_id") == warehouse_id
                )
            ):
                results.append(shipment)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
        """Run the tool using the specified parameters."""
        pass
        shipments = data.get("inbound_shipments", [])
        results = []
        for shipment in shipments:
            if (
                (not status or shipment.get("status") == status)
                and (not supplier_id or shipment.get("supplier_id") == supplier_id)
                and (
                    not warehouse_id
                    or shipment.get("destination_warehouse_id") == warehouse_id
                )
            ):
                results.append(shipment)
        payload = results
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Provide tool specifications for the AI agent."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "FindInboundShipments",
                "description": "Finds inbound shipments based on status, supplier, or destination warehouse.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {
                            "type": "string",
                            "description": "Filter by shipment status (e.g., 'In Transit', 'Received', 'Delayed').",
                        },
                        "supplier_id": {
                            "type": "string",
                            "description": "Filter by the supplier's ID.",
                        },
                        "warehouse_id": {
                            "type": "string",
                            "description": "Filter by the destination warehouse ID.",
                        },
                    },
                },
            },
        }
