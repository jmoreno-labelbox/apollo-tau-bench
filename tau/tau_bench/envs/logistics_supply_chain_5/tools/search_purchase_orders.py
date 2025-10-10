# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchPurchaseOrders(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        supplier_id = kwargs.get("supplier_id")
        status = kwargs.get("status")

        # Since we don't have purchase_orders data, we'll search inbound_shipments
        # which represent orders that have been placed and are being fulfilled
        inbound_shipments = data.get("inbound_shipments", [])
        results = []

        for shipment in inbound_shipments:
            match = True

            if supplier_id and shipment.get("supplier_id") != supplier_id:
                match = False
            if status:
                # Map shipment status to purchase order equivalent status
                po_status = "Delivered" if shipment.get("status") == "Received" else shipment.get("status")
                if po_status != status:
                    match = False
            if match:
                # Convert shipment data to purchase order format

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
