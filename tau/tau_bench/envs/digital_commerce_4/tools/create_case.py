# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _err(msg: str) -> str:
    return json.dumps({"error": msg}, indent=2)

def _as_id(x: Any) -> str:
    if x is None:
        return x
    if isinstance(x, str):
        return x
    if isinstance(x, int):
        return str(x)
    if isinstance(x, float) and x.is_integer():
        return str(int(x))
    return str(x)

class CreateCase(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        order_id: Any,
        contact_id: Any,
        subject: Any,
    ) -> str:
        case_id = None
        if not order_id or not contact_id or not subject:
            return _err("order_id, contact_id, subject are required.")
        order_id = _as_id(order_id)
        contact_id = _as_id(contact_id)
        subject = subject.capitalize()

        cases = data.setdefault("cases", [])

        cid = _as_id(case_id)
        if not cid:
            nums = []
            for c in cases:
                existing = _as_id(c.get("case_id"))
                if existing is not None and str(existing).isdigit():
                    nums.append(int(existing))
            next_id = (max(nums) + 1) if nums else 5001
            cid = str(next_id)

        exist = next((c for c in cases if _as_id(c.get("case_id")) == cid), None)
        if exist:
            return json.dumps(exist, indent=2)

        case = {
            "case_id": cid,
            "order_id": order_id,
            "contact_id": contact_id,
            "subject": subject,
            "status": "New",
            "created_at": FIXED_NOW,
        }
        cases.append(case)
        return json.dumps(case, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_case",
                "description": "Create a support case linked to an order and contact. ",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "contact_id": {"type": "string"},
                        "subject": {"type": "string"},
                    },
                    "required": ["order_id", "contact_id", "subject"],
                },
            },
        }