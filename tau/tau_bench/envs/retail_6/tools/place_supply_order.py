# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class PlaceSupplyOrder(Tool):
    """Create or update a supply order by provided supply_order_id."""
    @staticmethod
    def invoke(data, **kwargs) -> str:
        supply_order_id = kwargs.get('supply_order_id')
        supplier_id = kwargs.get('supplier_id')
        product_id = kwargs.get('product_id')
        item_id = kwargs.get('item_id')
        quantity = kwargs.get('quantity')
        unit_cost = kwargs.get('unit_cost')
        status = kwargs.get('status', 'pending')
        if not all([supply_order_id, supplier_id, product_id, item_id]) or quantity is None or unit_cost is None:
            return json.dumps({"error":"supply_order_id, supplier_id, product_id, item_id, quantity, unit_cost are required"}, indent=2)
        so_list = data.setdefault('supply_orders', [])
        existing = next((s for s in so_list if s.get('supply_order_id') == supply_order_id), None)
        record = {"supply_order_id": supply_order_id, "supplier_id": supplier_id, "product_id": product_id, "item_id": item_id, "quantity": int(quantity), "status": status, "order_date": "2025-01-01T00:00:00", "unit_cost": float(unit_cost), "total_cost": round(float(unit_cost)*int(quantity),2)}
        if existing:
            existing.update(record)
        else:
            so_list.append(record)
        return json.dumps({"success": True, "supply_order_id": supply_order_id}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"place_supply_order","description":"Create or overwrite a supply order by supply_order_id.","parameters":{"type":"object","properties":{"supply_order_id":{"type":"string"},"supplier_id":{"type":"string"},"product_id":{"type":"string"},"item_id":{"type":"string"},"quantity":{"type":"integer"},"unit_cost":{"type":"number"},"status":{"type":"string"}},"required":["supply_order_id","supplier_id","product_id","item_id","quantity","unit_cost"]}}}
