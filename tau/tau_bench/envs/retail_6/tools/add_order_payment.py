# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _find_order(data, order_id):
    return next((o for o in data.get('orders', []) if o.get('order_id') == order_id), None)

def _ensure_list(dct, key):
    if key not in dct or not isinstance(dct[key], list):
        dct[key] = []
    return dct[key]

class AddOrderPayment(Tool):
    """Append a payment record."""
    @staticmethod
    def invoke(data, amount, order_id, payment_method_id, transaction_id) -> str:
        txn_id = transaction_id
        if not order_id or amount is None or not payment_method_id or not txn_id:
            return json.dumps({"error":"order_id, amount, payment_method_id, transaction_id are required"}, indent=2)
        o = _find_order(data, order_id)
        if not o:
            return json.dumps({"error":f"order_id {order_id} not found"}, indent=2)
        hist = _ensure_list(o, 'payment_history')
        # idempotent: substitute existing with identical txn_id
        existing = next((h for h in hist if h.get('transaction_id') == txn_id), None)
        record = {"transaction_type":"payment","amount": float(amount),"payment_method_id": payment_method_id,"transaction_id": txn_id}
        if existing:
            existing.update(record)
        else:
            hist.append(record)
        return json.dumps({"success": True, "order_id": order_id, "transaction_id": txn_id}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"add_order_payment","description":"Add or upsert a payment record for an order (by transaction_id).","parameters":{"type":"object","properties":{"order_id":{"type":"string"},"amount":{"type":"number"},"payment_method_id":{"type":"string"},"transaction_id":{"type":"string"}},"required":["order_id","amount","payment_method_id","transaction_id"]}}}