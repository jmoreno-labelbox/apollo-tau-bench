from tau_bench.envs.tool import Tool
import json
import re
from typing import Any

class CreateCase(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        case_id: Any,
        order_id: Any,
        contact_id: Any,
        subject: Any,
        created_at: Any,
    ) -> str:
        if (
            not case_id
            or not order_id
            or not contact_id
            or not subject
            or not created_at
        ):
            return _err(
                "case_id, order_id, contact_id, subject, created_at are required."
            )
        case_id = _as_id(case_id)
        order_id = _as_id(order_id)
        contact_id = _as_id(contact_id)
        cases = data.setdefault("cases", [])
        exist = next((c for c in cases if _as_id(c.get("case_id")) == case_id), None)
        if exist:
            payload = exist
            out = json.dumps(payload, indent=2)
            return out
        case = {
            "case_id": case_id,
            "order_id": order_id,
            "contact_id": contact_id,
            "subject": subject,
            "status": "New",
            "created_at": created_at,
        }
        data["cases"][case["case_id"]] = case
        payload = case
        out = json.dumps(payload, indent=2)
        return out
        

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateCase",
                "description": "Create a support case linked to an order and contact.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "case_id": {"type": "string"},
                        "order_id": {"type": "string"},
                        "contact_id": {"type": "string"},
                        "subject": {"type": "string"},
                        "created_at": {"type": "string"},
                    },
                    "required": [
                        "case_id",
                        "order_id",
                        "contact_id",
                        "subject",
                        "created_at",
                    ],
                },
            },
        }
