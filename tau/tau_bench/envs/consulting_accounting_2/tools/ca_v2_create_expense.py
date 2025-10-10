# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CaV2CreateExpense(Tool):
    """Create a new expense record."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        expense_id = kwargs.get("expense_id")
        vendor = kwargs.get("vendor")
        expense_date = kwargs.get("expense_date")
        gross_amount = kwargs.get("gross_amount")
        currency = kwargs.get("currency", "CAD")
        description = kwargs.get("description")
        payment_method = kwargs.get("payment_method")
        category_code = kwargs.get("category_code")

        if not all([expense_id, vendor, expense_date, gross_amount, description, category_code]):
            return _error("Required fields: expense_id, vendor, expense_date, gross_amount, description, category_code")

        # Retrieve category for determining permissible amount.
        expense_categories = data.get("expense_categories", [])
        category = _find_one(expense_categories, "category_code", category_code)

        if not category:
            return _error(f"Expense category '{category_code}' not found.")

        deductible_percent = category.get("deductible_percent", 100) / 100
        allowed_amount = round(gross_amount * deductible_percent, 2)

        new_expense = {
            "expense_id": expense_id,
            "vendor": vendor,
            "expense_date": expense_date,
            "gross_amount": gross_amount,
            "currency": currency,
            "description": description,
            "payment_method": payment_method,
            "category_code": category_code,
            "allowed_amount": allowed_amount,
            "receipt_path": kwargs.get("receipt_path", f"/receipts/{expense_date[:4]}/{expense_id}_receipt.pdf"),
            "created_at": kwargs.get("created_at", expense_date + "T00:00:00Z")
        }

        data.setdefault("expenses", []).append(new_expense)

        return _ok(
            expense_id=expense_id,
            allowed_amount=allowed_amount,
            deductible_percent=category.get("deductible_percent")
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_create_expense",
                "description": "Create a new expense record with automatic deductible amount calculation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "expense_id": {"type": "string"},
                        "vendor": {"type": "string"},
                        "expense_date": {"type": "string", "format": "date"},
                        "gross_amount": {"type": "number"},
                        "currency": {"type": "string", "default": "CAD"},
                        "description": {"type": "string"},
                        "payment_method": {"type": "string"},
                        "category_code": {"type": "string"},
                        "receipt_path": {"type": "string"},
                        "created_at": {"type": "string"}
                    },
                    "required": ["expense_id", "vendor", "expense_date", "gross_amount", "description", "category_code"],
                },
            },
        }
