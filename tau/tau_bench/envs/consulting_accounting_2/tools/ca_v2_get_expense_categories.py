from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CaV2GetExpenseCategories(Tool):
    """Retrieve all expense categories along with their deductibility guidelines."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        expense_categories = data.get("expense_categories", [])
        payload = expense_categories
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2GetExpenseCategories",
                "description": "Get all expense categories with their deductibility percentages and rules.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }
