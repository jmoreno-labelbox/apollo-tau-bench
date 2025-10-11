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
        order_id: str,
        contact_id: str,
        subject: str,
        created_at: Any,
    ) -> str:
        if not order_id or not contact_id or not subject or not created_at:
            return _err("case_id, order_id, contact_id, subject, created_at are required.")

        cases = data.setdefault("cases", [])
        nums = []
        for c in cases:
            existing = _as_id(c.get("cases"))
            if existing is not None and str(existing).isdigit():
                nums.append(int(existing))
        next_id = (max(nums) + 1) if nums else 5001
        case_id = str(next_id)

        order_id = _as_id(order_id)
        contact_id = _as_id(contact_id)
        cases = data.setdefault("cases", [])
        case = {
            "case_id": case_id,
            "order_id": order_id,
            "contact_id": contact_id,
            "subject": subject,
            "status": "New",
            "created_at": created_at,
        }
        cases.append(case)
        return json.dumps(case, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_case",
                "description": "Create a support case linked to an order and contact.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "contact_id": {"type": "string"},
                        "subject": {"type": "string"},
                        "created_at": {"type": "string"},
                    },
                    "required": ["order_id", "contact_id", "subject", "created_at"],
                },
            },
        }