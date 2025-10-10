# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RefundOrderPayment(Tool):
    """Append a refund record with provided refund_id."""
    @staticmethod
    def invoke(data, **kwargs) -> str:
        order_id = kwargs.get('order_id')
        amount = kwargs.get('amount')
        reason_code = kwargs.get('reason_code')
        refund_id = kwargs.get('refund_id')
        if not order_id or amount is None or not reason_code or not refund_id:
            return json.dumps({"error":"order_id, amount, reason_code, refund_id are required"}, indent=2)
        o = _find_order(data, order_id)
        if not o:
            return json.dumps({"error":f"order_id {order_id} not found"}, indent=2)
        hist = _ensure_list(o, 'payment_history')
        existing = next((h for h in hist if h.get('refund_id') == refund_id), None)
        record = {"transaction_type":"refund","amount": float(amount),"reason_code": reason_code,"refund_id": refund_id}
        if existing:
            existing.update(record)
        else:
            hist.append(record)
        return json.dumps({"success": True, "order_id": order_id, "refund_id": refund_id}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"refund_order_payment","description":"Add or upsert a refund record for an order (by refund_id).","parameters":{"type":"object","properties":{"order_id":{"type":"string"},"amount":{"type":"number"},"reason_code":{"type":"string"},"refund_id":{"type":"string"}},"required":["order_id","amount","reason_code","refund_id"]}}}
