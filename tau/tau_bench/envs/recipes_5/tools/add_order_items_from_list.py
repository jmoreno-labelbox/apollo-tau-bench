from tau_bench.envs.tool import Tool
import json
from datetime import date, timedelta
from typing import Any

class AddOrderItemsFromList(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], order_id: int = None, store_id: int = None, product_overrides: dict = {},
    allowed_stock_statuses_json: Any = None,
    ) -> str:
        if order_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
            order_id = _latest_order_id(data, household_id)
        order = next(
            (o for o in data.get("orders", []) if o.get("order_id") == order_id), None
        )
        if not order:
            return _json_dump({"error": "no order available"})
        if store_id is None:
            store_id = int(order.get("store_id"))
        list_id = order.get("list_id")
        items = [
            i for i in data.get("grocery_list_items", []) if i.get("list_id") == list_id
        ]
        oi_tbl = data.get("order_items", [])
        next_oi = _max_id(oi_tbl, "order_item_id", 10100)
        created_ids = []
        subtotal = 0
        for item in items:
            ingr_id = int(item.get("ingredient_id"))
            override_pid = product_overrides.get(str(ingr_id)) or product_overrides.get(
                ingr_id
            )
            product = None
            if override_pid is not None:
                product = next(
                    (
                        p
                        for p in data.get("store_products", [])
                        if p.get("product_id") == int(override_pid)
                    ),
                    None,
                )
            if product is None:
                products = _store_products_for_ingredient(data, store_id, ingr_id)
                product = _lowest_price_in_stock(products)
            if product is None:
                continue
            next_oi += 1
            oi = {
                "order_item_id": next_oi,
                "order_id": order_id,
                "product_id": int(product.get("product_id")),
                "requested_qty": 1,
                "fulfilled_qty": 1,
                "substitute_product_id": None,
            }
            oi_tbl.append(oi)
            created_ids.append(next_oi)
            subtotal += int(product.get("price_cents", 0))
        order["subtotal_cents"] = subtotal
        order["total_cents"] = subtotal + 200
        return _json_dump(
            {
                "created_order_item_ids": created_ids,
                "subtotal_cents": order["subtotal_cents"],
                "total_cents": order["total_cents"],
            }
        )
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "addOrderItemsFromList",
                "description": "Populate order_items using lowest-price in-stock products; infers order and store.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "integer"},
                        "store_id": {"type": "integer"},
                        "product_overrides": {"type": "object"},
                    },
                    "required": [],
                },
            },
        }
