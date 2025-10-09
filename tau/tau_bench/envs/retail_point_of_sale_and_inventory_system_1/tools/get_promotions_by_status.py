from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetPromotionsByStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], status: str = None) -> str:
        promotions = data.get("promotions", {}).values()
        results = [promo for promo in promotions.values() if promo.get("status") == status]
        payload = results
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPromotionsByStatus",
                "description": "Retrieves all promotions with a specific status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {
                            "type": "string",
                            "description": "The status of the promotions to retrieve (e.g., 'active', 'scheduled', 'planned', 'inactive').",
                        },
                    },
                    "required": ["status"],
                },
            },
        }
