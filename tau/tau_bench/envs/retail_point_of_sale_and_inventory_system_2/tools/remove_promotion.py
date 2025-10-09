from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class RemovePromotion(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], promotion_id: str) -> str:
        promotions = data.get("promotions", [])
        original_len = len(promotions)
        promotions[:] = [p for p in promotions if p.get("promotion_id") != promotion_id]

        if len(promotions) == original_len:
            payload = {"error": f"Promotion with ID {promotion_id} not found."}
            out = json.dumps(payload)
            return out

        data["promotions"] = promotions
        payload = {"success": f"Promotion {promotion_id} removed successfully."}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "removePromotion",
                "description": "Remove a promotion from the system.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "promotion_id": {
                            "type": "string",
                            "description": "Unique identifier of the promotion to remove.",
                        }
                    },
                    "required": ["promotion_id"],
                },
            },
        }
