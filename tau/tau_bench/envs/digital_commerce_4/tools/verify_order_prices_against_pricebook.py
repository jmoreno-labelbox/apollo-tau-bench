from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class VerifyOrderPricesAgainstPricebook(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        order_id: str,
        pricebook_id: str | None = None
    ) -> str:
        pass
        order_id = _sid(order_id)
        eff_pb = _sid(pricebook_id) if pricebook_id is not None else None
        orders = data.get("orders", [])
        items = data.get("order_items", [])
        accounts = data.get("accounts", [])
        pbes = data.get("pricebook_entries", [])
        order = next((o for o in orders if _eq(o.get("order_id"), order_id)), None)
        if not order:
            payload = {"error": f"order {order_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        if eff_pb is None:
            acct = next(
                (
                    a
                    for a in accounts
                    if _eq(a.get("account_id"), order.get("account_id"))
                ),
                None,
            )
            eff_pb = acct.get("default_pricebook_id") if acct else None
        if not eff_pb:
            payload = {"error": "no pricebook context available"}
            out = json.dumps(payload, indent=2)
            return out
        lines = [li for li in items if _eq(li.get("order_id"), order_id)]
        checks = []
        for li in lines:
            pbe = next(
                (
                    p
                    for p in pbes
                    if _eq(p.get("pricebook_id"), eff_pb)
                    and _eq(p.get("product_id"), li.get("product_id"))
                ),
                None,
            )
            op = float(li.get("price", 0.0))
            pb = float(pbe.get("price")) if pbe else None
            checks.append(
                {
                    "product_id": li.get("product_id"),
                    "order_price": op,
                    "pricebook_price": pb,
                    "quantity": int(li.get("quantity", 0)),
                    "matches": (pb is not None and abs(op - pb) < 1e-9),
                }
            )
        all_match = all(c["matches"] for c in checks) if checks else False
        _append_audit(
            data,
            "PRICEBOOK_VERIFICATION",
            order_id,
            {"pricebook_id": eff_pb, "all_match": all_match},
        )
        _ws_append(
            data,
            order_id,
            "PRICEBOOK_VERIFICATION",
            {"pricebook_id": eff_pb, "all_match": all_match},
        )
        payload = {"order_id": order_id, "pricebook_id": eff_pb, "checks": checks}
        out = json.dumps(
            payload, indent=2
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "VerifyOrderPricesAgainstPricebook",
                "description": "Verify all order line prices against a given or inferred pricebook.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "pricebook_id": {"type": "string"},
                    },
                    "required": ["order_id"],
                },
            },
        }
