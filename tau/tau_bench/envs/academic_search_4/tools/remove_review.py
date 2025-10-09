from tau_bench.envs.tool import Tool
import json
import re
import uuid
from collections import Counter
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class RemoveReview(Tool):
    """Removes a review entry from the system."""

    @staticmethod
    def invoke(data: dict[str, Any], review_id: Any = None) -> str:
        review_id = review_id
        if not review_id:
            payload = {"error": "review_id is required."}
            out = json.dumps(payload)
            return out

        reviews = data.get("reviews", {}).values()
        original_count = len(reviews)
        # Reminder: In an actual database, this would perform a direct deletion. Here, we filter the array.
        data["reviews"] = [r for r in reviews.values() if r.get("review_id") != review_id]

        if len(data["reviews"]) < original_count:
            payload = {"success": True, "message": f"Review {review_id} has been deleted."}
            out = json.dumps(payload)
            return out
        else:
            payload = {"error": f"Review with ID '{review_id}' not found."}
            out = json.dumps(payload)
            return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RemoveReview",
                "description": "Deletes a specific review by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "review_id": {
                            "type": "string",
                            "description": "The ID of the review to delete.",
                        }
                    },
                    "required": ["review_id"],
                },
            },
        }
