# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class IssueCustomerCreditMemo(Tool):
    """Issues a credit memo for a customer and logs the financial transaction."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        order_id = kwargs.get('order_id')
        customer_id = kwargs.get('customer_id')
        returned_items = kwargs.get('returned_items')

        if not all([order_id, customer_id, returned_items]):
            return json.dumps({"error": "order_id, customer_id, and returned_items are required."}, indent=2)

        # Deterministic ID generation based on policy
        order_id_num = order_id.split('-')[1]
        credit_memo_id = f"CM-{order_id_num}"

        total_credit_value = 0
        product_master = data.get('product_master', [])
        for item in returned_items:
            product = next((p for p in product_master if p.get('sku') == item['sku']), None)
            if product:
                total_credit_value += product.get('unit_price', 0) * item['quantity']

        if 'credit_memos' not in data:
            data['credit_memos'] = []

        credit_memo = {
            "credit_memo_id": credit_memo_id,
            "original_order_id": order_id,
            "customer_id": customer_id,
            "credited_items": returned_items,
            "total_credit_value": round(total_credit_value, 2),
            "currency": "USD",
            "status": "Issued",
        }
        data['credit_memos'].append(credit_memo)

        return json.dumps(credit_memo, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "issue_customer_credit_memo",
                "description": "Issues a credit memo for a customer for returned goods and logs the financial transaction.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The original order ID that is being credited."},
                        "customer_id": {"type": "string", "description": "The ID of the customer receiving the credit."},
                        "returned_items": {
                            "type": "array", "description": "A list of items for which credit is being issued.",
                            "items": {"type": "object", "properties": {"sku": {"type": "string"}, "quantity": {"type": "integer"}}, "required": ["sku", "quantity"]}
                        }
                    },
                    "required": ["order_id", "customer_id", "returned_items"]
                }
            }
        }
