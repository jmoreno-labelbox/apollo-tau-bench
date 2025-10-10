# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FlagHighValueMeals(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        ref = kwargs.get("expenses_ref", {})
        threshold = float(kwargs.get("threshold", 150.0))
        items = ref.get("expenses", [])
        decisions = []
        for e in items:
            if e.get("category_code") == "MEALS_ENTERTAIN" and float(e.get("gross_amount",0.0)) > threshold:
                decisions.append({"invoice_id": None, "action": "email_reminder", "notes": f"High value meal: {e.get('expense_id')} > {threshold}"})
        return json.dumps({"decisions": decisions, "count": len(decisions)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"flag_high_value_meals",
            "description":"Produce decisions for meals exceeding threshold (for audit entries).",
            "parameters":{"type":"object","properties":{
                "expenses_ref":{"type":"object"},
                "threshold":{"type":"number"}
            },"required":["expenses_ref"]}
        }}
