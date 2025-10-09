from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CaV2CreateExpense(Tool):
    """Generate a new expense entry."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        category_code: str = None,
        created_at: str = None,
        currency: str = "CAD",
        description: str = None,
        expense_date: str = None,
        expense_id: str = None,
        gross_amount: float = None,
        payment_method: str = None,
        receipt_path: str = None,
        vendor: str = None
    ) -> str:
        if not all(
            [expense_id, vendor, expense_date, gross_amount, description, category_code]
        ):
            return _error(
                "Required fields: expense_id, vendor, expense_date, gross_amount, description, category_code"
            )

        # Retrieve category to determine permissible amount
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
            "receipt_path": receipt_path or f"/receipts/{expense_date[:4]}/{expense_id}_receipt.pdf",
            "created_at": created_at or expense_date + "T00:00:00Z",
        }

        data.setdefault("expenses", []).append(new_expense)

        return _ok(
            expense_id=expense_id,
            allowed_amount=allowed_amount,
            deductible_percent=category.get("deductible_percent"),
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2CreateExpense",
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
                        "created_at": {"type": "string"},
                    },
                    "required": [
                        "expense_id",
                        "vendor",
                        "expense_date",
                        "gross_amount",
                        "description",
                        "category_code",
                    ],
                },
            },
        }
