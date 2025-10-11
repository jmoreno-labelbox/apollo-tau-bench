# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _json_dump
from . import _first_user_id
def _latest_order_for_household(data: Dict[str, Any], household_id: Optional[int]) -> Optional[Dict[str, Any]]:
    if household_id is None:
        return None
    orders = [o for o in data.get("orders", []) if o.get("household_id") == household_id]
    if not orders:
        return None
    return sorted(orders, key=lambda o: int(o.get("order_id", 0)), reverse=True)[0]

def _household_for_user(data: Dict[str, Any], user_id: Optional[int]) -> Optional[Dict[str, Any]]:
    if user_id is not None:
        h = next((h for h in data.get("households", []) if h.get("primary_user_id") == user_id), None)
        if h:
            return h
    households = data.get("households", [])
    if not households:
        return None
    return sorted(households, key=lambda h: int(h.get("household_id", 10**9)))[0]

def _store_products_for_ingredient(data: Dict[str, Any], store_id: int, ingredient_id: int) -> List[Dict[str, Any]]:
    return [
        p for p in data.get("store_products", [])
        if p.get("store_id") == store_id and p.get("ingredient_id") == ingredient_id
    ]

def _max_id(records: List[Dict[str, Any]], key: str, default: int) -> int:
    if not records:
        return default
    return max(int(r.get(key, default)) for r in records)

def _lowest_price_in_stock(products: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    in_stock = [p for p in products if p.get("stock_status_enum") in ("in_stock", "low")]
    if not in_stock:
        return None
    return sorted(in_stock, key=lambda x: int(x.get("price_cents", 10**9)))[0]

def _latest_order_id(data: Dict[str, Any], household_id: Optional[int]) -> Optional[int]:
    o = _latest_order_for_household(data, household_id)
    return int(o["order_id"]) if o else None

def _json_dump(obj: Any) -> str:
    return json.dumps(obj, indent=2, ensure_ascii=False)

def _first_user_id(data: Dict[str, Any]) -> Optional[int]:
    users = data.get("users", [])
    if not users:
        return None
    return int(sorted(users, key=lambda u: int(u.get("user_id", 10**9)))[0]["user_id"])

def _default_household_id(data: Dict[str, Any], user_id: Optional[int] = None) -> Optional[int]:
    hh = _household_for_user(data, user_id)
    return hh.get("household_id") if hh else None

class AddOrderItemsFromList(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], order_id, store_id, product_overrides = {}) -> str:
        if order_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
            order_id = _latest_order_id(data, household_id)
        order = next((o for o in list(data.get("orders", {}).values()) if o.get("order_id") == order_id), None)
        if not order:
            return _json_dump({"error": "no order available"})
        if store_id is None:
            store_id = int(order.get("store_id"))
        list_id = order.get("list_id")
        items = [i for i in data.get("grocery_list_items", []) if i.get("list_id") == list_id]
        oi_tbl = data.get("order_items", [])
        next_oi = _max_id(oi_tbl, "order_item_id", 10100)
        created_ids = []
        subtotal = 0
        for item in items:
            ingr_id = int(item.get("ingredient_id"))
            override_pid = product_overrides.get(str(ingr_id)) or product_overrides.get(ingr_id)
            product = None
            if override_pid is not None:
                product = next((p for p in data.get("store_products", []) if p.get("product_id") == int(override_pid)), None)
            if product is None:
                products = _store_products_for_ingredient(data, store_id, ingr_id)
                product = _lowest_price_in_stock(products)
            if product is None:
                continue
            next_oi += 1
            oi = {"order_item_id": next_oi,"order_id": order_id,"product_id": int(product.get("product_id")),"requested_qty": 1,"fulfilled_qty": 1,"substitute_product_id": None}
            oi_tbl.append(oi)
            created_ids.append(next_oi)
            subtotal += int(product.get("price_cents", 0))
        order["subtotal_cents"] = subtotal
        order["total_cents"] = subtotal + 200
        return _json_dump({"created_order_item_ids": created_ids, "subtotal_cents": order["subtotal_cents"], "total_cents": order["total_cents"]})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"add_order_items_from_list","description":"Populate order_items using lowest-price in-stock products; infers order and store.","parameters":{"type":"object","properties":{"order_id":{"type":"integer"},"store_id":{"type":"integer"},"product_overrides":{"type":"object"}},"required":[]}}}