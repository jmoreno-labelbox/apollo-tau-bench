from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class DeleteReview(Tool):
    """Utility for removing a review record."""

    @staticmethod
    def invoke(data: dict[str, Any], review_id: Any = None) -> str:
        reviews = data.get("reviews", [])
        original_count = len(reviews)
        data["reviews"] = [r for r in reviews if r.get("review_id") != review_id]
        if len(data["reviews"]) < original_count:
            payload = {
                "status": "success",
                "review_id": review_id,
                "message": "Review deleted.",
            }
            out = json.dumps(payload)
            return out
        else:
            payload = {"error": f"Review with ID {review_id} not found."}
            out = json.dumps(payload)
            return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DeleteReview",
                "description": "Deletes a specific review record by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "review_id": {
                            "type": "string",
                            "description": "The unique ID of the review to delete.",
                        }
                    },
                    "required": ["review_id"],
                },
            },
        }
