from tau_bench.envs.tool import Tool
import json
import random
from typing import Any

class IssueCustomerCreditMemo(Tool):
    """Generates a credit memo for a customer and records the financial transaction."""

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None, customer_id: str = None, returned_items: list = None) -> str:
        if not all([order_id, customer_id, returned_items]):
            payload = {"error": "order_id, customer_id, and returned_items are required."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # Predictable ID creation according to policy
        order_id_num = order_id.split("-")[1]
        credit_memo_id = f"CM-{order_id_num}"

        total_credit_value = 0
        product_master = data.get("product_master", [])
        for item in returned_items:
            product = next(
                (p for p in product_master if p.get("sku") == item["sku"]), None
            )
            if product:
                total_credit_value += product.get("unit_price", 0) * item["quantity"]

        if "credit_memos" not in data:
            data["credit_memos"] = []

        credit_memo = {
            "credit_memo_id": credit_memo_id,
            "original_order_id": order_id,
            "customer_id": customer_id,
            "credited_items": returned_items,
            "total_credit_value": round(total_credit_value, 2),
            "currency": "USD",
            "status": "Issued",
        }
        data["credit_memos"].append(credit_memo)
        payload = credit_memo
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "IssueCustomerCreditMemo",
                "description": "Issues a credit memo for a customer for returned goods and logs the financial transaction.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "The original order ID that is being credited.",
                        },
                        "customer_id": {
                            "type": "string",
                            "description": "The ID of the customer receiving the credit.",
                        },
                        "returned_items": {
                            "type": "array",
                            "description": "A list of items for which credit is being issued.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "sku": {"type": "string"},
                                    "quantity": {"type": "integer"},
                                },
                                "required": ["sku", "quantity"],
                            },
                        },
                    },
                    "required": ["order_id", "customer_id", "returned_items"],
                },
            },
        }
