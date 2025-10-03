from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class BucketizeAging(Tool):
    """Assign days overdue to standard Accounts Receivable aging categories."""

    @staticmethod
    def invoke(data: dict[str, Any], aging: list[dict[str, Any]] = None) -> str:
        aging = aging or []
        buckets = []
        for a in aging:
            days = int(a.get("days_outstanding", 0))
            if days < 0 and days >= -7:
                b = "upcoming_due"
            elif 0 <= days <= 30:
                b = "0-30"
            elif 31 <= days <= 60:
                b = "31-60"
            elif 61 <= days <= 90:
                b = "61-90"
            elif days > 90:
                b = "90+"
            else:
                b = "not_due"
            buckets.append({"invoice_number": a.get("invoice_number"), "bucket": b})
        payload = {"buckets": buckets}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "BucketizeAging",
                "description": "Convert days-outstanding to buckets (incl. 'upcoming_due').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "aging": {"type": "array", "items": {"type": "object"}}
                    },
                    "required": ["aging"],
                },
            },
        }
