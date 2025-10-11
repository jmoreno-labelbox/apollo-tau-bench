# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ApplyDeductibilityRules(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], expense_id) -> str:
        if not expense_id:
            return json.dumps({"error": "expense_id is required"}, indent=2)
        exp = next((e for e in list(data.get("expenses", {}).values()) if e.get("expense_id") == expense_id), None)
        if not exp:
            return json.dumps({"error": f"Expense {expense_id} not found"}, indent=2)
        cat = exp.get("category_code")
        cat_obj = next((c for c in list(data.get("expense_categories", {}).values()) if c.get("category_code") == cat), None)
        if not cat_obj:
            return json.dumps({"error": f"Category {cat} not found"}, indent=2)
        pct = float(cat_obj.get("deductible_percent", 100)) / 100.0
        allowed = round(float(exp.get("gross_amount", 0.0)) * pct, 2)
        result = {"expense_id": expense_id,"category_code": cat,"deductible_percent": pct * 100,"allowed_amount": allowed}
        exp["allowed_amount"] = allowed
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "apply_deductibility_rules","description": "Apply expense category deductibility to compute allowed_amount.","parameters": {"type": "object","properties": {"expense_id": {"type": "string"}},"required": ["expense_id"]}}}
