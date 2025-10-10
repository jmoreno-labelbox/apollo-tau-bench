# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CategorizeAging(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        aging = kwargs.get("aging") or []
        buckets = []
        for a in aging:
            days = int(a.get("days_outstanding",0))
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
        return json.dumps({"buckets": buckets}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"categorize_aging",
            "description":"Map days outstanding to aging buckets including 'upcoming_due'.",
            "parameters":{"type":"object","properties":{"aging":{"type":"array","items":{"type":"object"}}},"required":["aging"]}
        }}
