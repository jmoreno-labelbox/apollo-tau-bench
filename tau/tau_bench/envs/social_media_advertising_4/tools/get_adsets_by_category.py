from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetAdsetsByCategory(Tool):
    """Identifies ad sets aimed at a particular product category."""

    @staticmethod
    def invoke(data: dict[str, Any], category: str = None) -> str:
        adsets = [
            adset
            for adset in data.get("adsets", {}).values()
            if adset.get("category") == category
        ]
        payload = {"adsets": adsets}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAdsetsByCategory",
                "description": "Retrieves a list of ad sets that are targeting a specific product category.",
                "parameters": {
                    "type": "object",
                    "properties": {"category": {"type": "string"}},
                    "required": ["category"],
                },
            },
        }
