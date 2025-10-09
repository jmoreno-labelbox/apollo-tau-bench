from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ApplyDeductibilityRules(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], expense_id: str = None) -> str:
        if not expense_id:
            payload = {"error": "expense_id is required"}
            out = json.dumps(payload, indent=2)
            return out
        exp = next(
            (e for e in data.get("expenses", {}).values() if e.get("expense_id") == expense_id),
            None,
        )
        if not exp:
            payload = {"error": f"Expense {expense_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        cat = exp.get("category_code")
        cat_obj = next(
            (
                c
                for c in data.get("expense_categories", {}).values()
                if c.get("category_code") == cat
            ),
            None,
        )
        if not cat_obj:
            payload = {"error": f"Category {cat} not found"}
            out = json.dumps(payload, indent=2)
            return out
        pct = float(cat_obj.get("deductible_percent", 100)) / 100.0
        allowed = round(float(exp.get("gross_amount", 0.0)) * pct, 2)
        result = {
            "expense_id": expense_id,
            "category_code": cat,
            "deductible_percent": pct * 100,
            "allowed_amount": allowed,
        }
        exp["allowed_amount"] = allowed
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ApplyDeductibilityRules",
                "description": "Apply expense category deductibility to compute allowed_amount.",
                "parameters": {
                    "type": "object",
                    "properties": {"expense_id": {"type": "string"}},
                    "required": ["expense_id"],
                },
            },
        }
