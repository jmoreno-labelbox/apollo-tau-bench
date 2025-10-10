# Intellectual property owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchPurchaseOrders(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], status, supplier_id) -> str:

        # Lacking purchase_orders data, we will query inbound_shipments instead.
        # denotes orders that have been submitted and are currently in the fulfillment process
        inbound_shipments = data.get("inbound_shipments", [])
        results = []

        for shipment in inbound_shipments:
            match = True

            if supplier_id and shipment.get("supplier_id") != supplier_id:
                match = False
            if status:
                # Associate shipment status with corresponding purchase order status.
                po_status = "Delivered" if shipment.get("status") == "Received" else shipment.get("status")
                if po_status != status:
                    match = False
            if match:
                # Transform shipment information into purchase order structure.

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
                "name": "search_purchase_orders",
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
