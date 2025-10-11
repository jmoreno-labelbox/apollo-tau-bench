# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ShipOutboundOrder(Tool):
    """Updates an order to 'Shipped', assigns a carrier, allocates inventory, and calculates shipping cost."""
    @staticmethod
    def invoke(data: Dict[str, Any], carrier_scac, order_id, warehouse_id) -> str:
        if not all([order_id, warehouse_id, carrier_scac]):
            return json.dumps({"error": "order_id, warehouse_id, and carrier_scac are required."}, indent=2)

        order_to_update = next((o for o in data.get('outbound_orders', []) if o.get('order_id') == order_id), None)
        if not order_to_update:
            return json.dumps({"error": f"Order '{order_id}' not found."}, indent=2)

        # --- INITIATING NEW LOGIC ---
        total_weight_kg = 0
        line_items = order_to_update.get("line_items", [])
        product_master = list(data.get('product_master', {}).values())
        for item in line_items:
            product = next((p for p in product_master if p.get('sku') == item['sku']), None)
            if product:
                total_weight_kg += product.get('weight_kg', 0) * item['quantity']

        # Fixed shipping cost computation
        shipping_cost = round((total_weight_kg * 2.5) + 100, 2)
        order_to_update['shipping_cost'] = shipping_cost
        # --- END OF NEW LOGIC ---

        order_to_update['status'] = 'Shipped'
        order_to_update['warehouse_id'] = warehouse_id
        carrier_name = next((c.get('carrier_name') for c in data.get('carriers', []) if c.get('scac') == carrier_scac), "Unknown")
        order_to_update['carrier_name'] = carrier_name
        order_to_update['carrier_scac'] = carrier_scac
        order_id_number = order_id.split('-')[1]
        order_to_update['tracking_number'] = f"{carrier_scac}-{order_id_number}"

        for item in line_items:
            for inv_record in list(data.get('inventory', {}).values()):
                if inv_record.get('sku') == item.get('sku') and inv_record.get('warehouse_id') == warehouse_id:
                    inv_record['quantity_available'] -= item.get('quantity', 0)
                    inv_record['quantity_allocated'] += item.get('quantity', 0)
                    break

        return json.dumps(order_to_update, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "ship_outbound_order", "description": "Updates an order's status to 'Shipped', adjusts inventory, and assigns a carrier.", "parameters": {"type": "object", "properties": {"order_id": {"type": "string"}, "warehouse_id": {"type": "string"}, "carrier_scac": {"type": "string"}}, "required": ["order_id", "warehouse_id", "carrier_scac"]}}}
