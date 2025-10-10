# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ComputeUserFillRate(Tool):
    """Compute a naive fill rate for a user's orders: delivered_items / total_items across all orders."""
    @staticmethod
    def invoke(data, **kwargs) -> str:
        user_id = kwargs.get('user_id')
        if not user_id:
            return json.dumps({"error":"user_id is required"}, indent=2)
        user_orders = [o for o in list(data.get('orders', {}).values()) if o.get('user_id') == user_id]
        total = sum(len(o.get('items', [])) for o in user_orders)
        delivered = 0
        for o in user_orders:
            # count items in fulfillments for which tracking shows delivered
            for f in o.get('fulfillments', []):
                for tid in f.get('tracking_id', []):
                    tr = _find_tracking(data, tid)
                    if tr and tr.get('tracking_history', {}).get('delivered'):
                        delivered += len(f.get('item_ids', []))
        rate = (delivered/total) if total else 0.0
        return json.dumps({"user_id": user_id, "fill_rate": round(rate,4)}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"compute_user_fill_rate","description":"Compute delivered item share across a user's orders.","parameters":{"type":"object","properties":{"user_id":{"type":"string"}},"required":["user_id"]}}}
