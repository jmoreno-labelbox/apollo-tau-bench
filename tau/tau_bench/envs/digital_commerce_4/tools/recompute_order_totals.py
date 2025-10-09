from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class RecomputeOrderTotals(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], order_id: str) -> str:
        pass
        order_id = _sid(order_id)
        orders = data.get("orders", {}).values()
        items = data.get("order_items", {}).values()
        accounts = data.get("accounts", {}).values()
        pbes = data.get("pricebook_entries", {}).values()
        offers = data.get("offers", {}).values()
        data.get("products", {}).values()

        order = next((o for o in orders.values() if o.get("order_id") == order_id), None)
        if not order:
            payload = {"error": f"order {order_id} not found"}
            out = json.dumps(payload, indent=2)
            return out

        account = next(
            (a for a in accounts.values() if a.get("account_id") == order.get("account_id")),
            None,
        )
        pricebook_id = account.get("default_pricebook_id") if account else None
        line_items = [i for i in items.values() if i.get("order_id") == order_id]
        subtotal = 0.0
        for li in line_items:
            pbe = next(
                (
                    p
                    for p in pbes.values() if p.get("pricebook_id") == pricebook_id
                    and p.get("product_id") == li.get("product_id")
                ),
                None,
            )
            #revert to the current price if the pricebook entry is absent
            price = pbe.get("price") if pbe else li.get("price", 0.0)
            subtotal += float(price) * int(li.get("quantity", 0))

        discount_amount = 0.0
        applied_offer = _active_offer(offers, order.get("applied_offer_id"))
        if applied_offer:
            if applied_offer.get("discount_type") == "PERCENTAGE":
                discount_amount = round(
                    subtotal * float(applied_offer.get("discount_value", 0.0)) / 100.0,
                    2,
                )
            elif applied_offer.get("discount_type") == "FIXED_AMOUNT":
                discount_amount = float(applied_offer.get("discount_value", 0.0))
            discount_amount = min(discount_amount, subtotal)

        total_amount = round(subtotal - discount_amount, 2)
        order["subtotal"] = round(subtotal, 2)
        order["discount_amount"] = round(discount_amount, 2)
        order["total_amount"] = total_amount
        _append_audit(data, "RECOMPUTE_TOTALS", order_id, {}).values()
        _ws_append(data, order_id, "RECOMPUTE_TOTALS", {}).values()
        payload = order
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RecomputeOrderTotals",
                "description": "Recompute order subtotal, discount and total using account pricebook and active offer.",
                "parameters": {
                    "type": "object",
                    "properties": {"order_id": {"type": "string"}},
                    "required": ["order_id"],
                },
            },
        }
