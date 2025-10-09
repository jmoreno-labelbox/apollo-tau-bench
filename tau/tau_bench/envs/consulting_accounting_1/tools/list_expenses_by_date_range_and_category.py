from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ListExpensesByDateRangeAndCategory(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], start_date: str = None, end_date: str = None, categories: list = None) -> str:
        if not start_date or not end_date or not categories:
            payload = {"error": "start_date, end_date, categories are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        exp = []
        for e in data.get("expenses", []):
            d = str(e.get("expense_date", ""))
            if start_date <= d <= end_date and e.get("category_code") in categories:
                exp.append(e)
        payload = {"expenses": exp}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListExpensesByDateRangeAndCategory",
                "description": "Return expenses in [start_date, end_date] for given categories.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "start_date": {"type": "string"},
                        "end_date": {"type": "string"},
                        "categories": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["start_date", "end_date", "categories"],
                },
            },
        }
