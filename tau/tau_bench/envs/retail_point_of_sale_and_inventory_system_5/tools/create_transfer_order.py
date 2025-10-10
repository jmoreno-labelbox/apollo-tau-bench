# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateTransferOrder(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        from_store = kwargs["from_store"]
        to_store = kwargs["to_store"]
        sku = kwargs["sku"]
        quantity = kwargs["quantity"]
        # Only use hash-based transfer_id for all cases
        transfer_id = f"TRF-{hashlib.sha256(f'{from_store}-{to_store}-{sku}'.encode()).hexdigest()[:6].upper()}"
        entry = {
            "from_store": from_store,
            "to_store": to_store,
            "sku": sku,
            "quantity": quantity
        }
        data.setdefault("transfer_orders", []).append(entry)
        resp = {"message": "Transfer order created.", "transfer_id": transfer_id, "entry": entry}
        if quantity > 25:
            resp["compliance_review_required"] = True
        return json.dumps(resp)
    @staticmethod
    def get_info() -> Dict[str, Any]:
