# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateOutboundOrder(Tool):
    """A tool to create a new outbound order in the system."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_name = kwargs.get('customer_name')
        destination_city = kwargs.get('destination_city')
        priority_level = kwargs.get('priority_level')
        line_items = kwargs.get('line_items')
        if not all([customer_name, destination_city, priority_level, line_items]):
            return json.dumps({"error": "customer_name, destination_city, priority_level, and line_items are required."}, indent=2)
        outbound_orders = list(data.get('outbound_orders', {}).values())
        max_id = max((int(o.get('order_id', 'ORD-0').split('-')[1]) for o in outbound_orders), default=0)
        new_order_id = f"ORD-{max_id + 1:04d}"
        customer_details = next((o for o in outbound_orders if o.get('customer_name') == customer_name), {})
        new_order = {"order_id": new_order_id, "sales_order_number": f"SO-2025-{max_id + 1:04d}", "customer_id": customer_details.get("customer_id"), "customer_name": customer_name, "customer_address": customer_details.get("customer_address"), "customer_city": destination_city, "customer_country": customer_details.get("customer_country"), "destination_address": customer_details.get("customer_address"), "destination_city": destination_city, "destination_country": customer_details.get("customer_country"), "status": "Pending", "number_of_line_items": len(line_items), "total_units": sum(item.get('quantity', 0) for item in line_items), "priority_level": priority_level, "line_items": line_items, "warehouse_id": None, "actual_ship_date": None, "carrier_name": None, "tracking_number": None}
        outbound_orders.append(new_order)
        return json.dumps({"order_id": new_order_id}, indent=2)


    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_outbound_order", "description": "Creates a new outbound customer order with a 'Pending' status.", "parameters": {"type": "object", "properties": {"customer_name": {"type": "string"}, "destination_city": {"type": "string"}, "priority_level": {"type": "string"}, "line_items": {"type": "array", "items": {"type": "object", "properties": {"sku": {"type": "string"}, "quantity": {"type": "integer"}}, "required": ["sku", "quantity"]}}}, "required": ["customer_name", "destination_city", "priority_level", "line_items"]}}}
