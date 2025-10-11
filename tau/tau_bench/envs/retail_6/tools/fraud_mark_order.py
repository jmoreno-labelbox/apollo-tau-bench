# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _find_order(data, order_id):
    return next((o for o in data.get('orders', []) if o.get('order_id') == order_id), None)

class FraudMarkOrder(Tool):
    """Attach a fraud_check dict to an order."""
    @staticmethod
    def invoke(data, order_id, reason_code, risk_level) -> str:
        if not order_id or not risk_level or not reason_code:
            return json.dumps({"error":"order_id, risk_level, reason_code are required"}, indent=2)
        o = _find_order(data, order_id)
        if not o:
            return json.dumps({"error": f"order_id {order_id} not found"}, indent=2)
        o['fraud_check'] = {"risk_level": risk_level, "reason_code": reason_code}
        return json.dumps({"success": True, "order_id": order_id, "risk_level": risk_level}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"fraud_mark_order","description":"Mark an order with fraud_check metadata.","parameters":{"type":"object","properties":{"order_id":{"type":"string"},"risk_level":{"type":"string"},"reason_code":{"type":"string"}},"required":["order_id","risk_level","reason_code"]}}}