from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any, Dict



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class SearchPurchaseOrders(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], supplier_id: str = None, status: str = None) -> str:
        # Due to the absence of purchase_orders data, we will look into inbound_shipments
        # that signify orders that have been made and are currently being processed
        inbound_shipments = data.get("inbound_shipments", {}).values()
        results = []

        for shipment in inbound_shipments.values():
            match = True

            if supplier_id and shipment.get("supplier_id") != supplier_id:
                match = False
            if status:
                # Align shipment status with the corresponding purchase order status
                po_status = "Delivered" if shipment.get("status") == "Received" else shipment.get("status")
                if po_status != status:
                    match = False
            if match:
                # Transform shipment information into purchase order format

                po_data = {
                    "po_id": shipment.get("purchase_order_number"),
                    "supplier_id": shipment.get("supplier_id"),
                    "supplier_name": shipment.get("supplier_name"),
                    "status": "Delivered" if shipment.get("status") == "Received" else shipment.get("status"),
                    "total_value": shipment.get("total_value"),
                    "value_currency": shipment.get("value_currency"),
                    "expected_delivery": shipment.get("expected_arrival_date"),
                    "actual_delivery": shipment.get("actual_arrival_date"),
                    "destination_warehouse": shipment.get("destination_warehouse_id"),
                    "tracking_number": shipment.get("tracking_number"),
                    "shipment_id": shipment.get("shipment_id")
                }
                results.append(po_data)

        return json.dumps(results)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchPurchaseOrders",
                "description": "Search for purchase orders based on criteria (uses inbound shipment data)",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {"type": "string", "description": "Supplier identifier"},
                        "status": {"type": "string", "description": "Purchase order status"}
                    },
                    "required": []
                }
            }
        }
