from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class FetchRecentSalesByProperty(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], property_id: str, limit: int = 3) -> str:
        sales = [
            s for s in data.get("sales", {}).values() if s.get("property_id") == property_id
        ]
        sales = sorted(sales, key=lambda s: s.get("sale_date") or "", reverse=True)[
            :limit
        ]
        payload = {"property_id": property_id, "sales": sales}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FetchRecentSalesByProperty",
                "description": "Return up to N recent sales rows for a property.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "property_id": {"type": "string"},
                        "limit": {"type": "integer"},
                    },
                    "required": ["property_id"],
                },
            },
        }
