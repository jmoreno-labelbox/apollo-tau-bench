# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateInboundReturnShipment(Tool):
    """Creates a new 'Planned' inbound shipment specifically for a customer return."""
    @staticmethod
    def invoke(data: Dict[str, Any], carrier_scac, from_customer_id, rma_id, to_warehouse_id) -> str:

        if not all([rma_id, from_customer_id, to_warehouse_id, carrier_scac]):
            return json.dumps({"error": "rma_id, from_customer_id, to_warehouse_id, and carrier_scac are required."}, indent=2)

        inbound_shipments = list(data.get('inbound_shipments', {}).values())
        max_ship_id = max((int(s.get('shipment_id', 'SHIP-0').split('-')[1]) for s in inbound_shipments), default=0)
        new_shipment_id = f"SHIP-{max_ship_id + 1:04d}"

        customer = next((o for o in data.get('outbound_orders', []) if o.get('customer_id') == from_customer_id), {})
        warehouse = next((w for w in data.get('warehouses', []) if w.get('warehouse_id') == to_warehouse_id), {})

        new_shipment = {
            "shipment_id": new_shipment_id,
            "purchase_order_number": rma_id, # Utilizing RMA as the identifier.
            "supplier_id": from_customer_id,
            "supplier_name": "CUSTOMER_RETURN",
            "origin_address": customer.get("customer_address"),
            "origin_city": customer.get("customer_city"),
            "origin_country": customer.get("customer_country"),
            "destination_warehouse_id": to_warehouse_id,
            "destination_warehouse_name": warehouse.get("warehouse_name"),
            "carrier_name": next((c.get("carrier_name") for c in data.get('carriers', []) if c.get("scac") == carrier_scac), "Unknown"),
            "carrier_scac": carrier_scac,
            "status": "Planned",
            "priority_level": "Medium"
        }
        inbound_shipments.append(new_shipment)
        return json.dumps(new_shipment, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_inbound_return_shipment",
                "description": "Creates a new 'Planned' inbound shipment to track the physical return of goods from a customer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "rma_id": {"type": "string", "description": "The RMA number authorizing this return shipment."},
                        "from_customer_id": {"type": "string", "description": "The ID of the customer returning the items."},
                        "to_warehouse_id": {"type": "string", "description": "The ID of the warehouse designated to receive the return."},
                        "carrier_scac": {"type": "string", "description": "The SCAC code of the carrier handling the return."}
                    },
                    "required": ["rma_id", "from_customer_id", "to_warehouse_id", "carrier_scac"]
                }
            }
        }
