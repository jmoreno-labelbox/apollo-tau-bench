from tau_bench.envs.tool import Tool
import json
from typing import Any

class FlagHighValueMeals(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], expenses_ref: dict = None, threshold: float = 150.0) -> str:
        ref = expenses_ref if expenses_ref is not None else {}
        items = ref.get("expenses", [])
        decisions = []
        for e in items:
            if (
                e.get("category_code") == "MEALS_ENTERTAIN"
                and float(e.get("gross_amount", 0.0)) > threshold
            ):
                decisions.append(
                    {
                        "invoice_id": None,
                        "action": "email_reminder",
                        "notes": f"High value meal: {e.get('expense_id')} > {threshold}",
                    }
                )
        payload = {"decisions": decisions, "count": len(decisions)}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FlagHighValueMeals",
                "description": "Produce decisions for meals exceeding threshold (for audit entries).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "expenses_ref": {"type": "object"},
                        "threshold": {"type": "number"},
                    },
                    "required": ["expenses_ref"],
                },
            },
        }
