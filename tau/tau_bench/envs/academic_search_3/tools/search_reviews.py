from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class SearchReviews(Tool):
    """Utility for finding reviews based on submission and reviewer."""

    @staticmethod
    def invoke(data: dict[str, Any], submission_id: str = None, reviewer_user_id: str = None) -> str:
        reviews = data.get("reviews", [])
        results = [
            r
            for r in reviews
            if r.get("submission_id") == submission_id
            and r.get("reviewer_user_id") == reviewer_user_id
        ]
        payload = results
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchReviews",
                "description": "Searches for specific reviews by submission and reviewer ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "submission_id": {
                            "type": "string",
                            "description": "The submission's ID.",
                        },
                        "reviewer_user_id": {
                            "type": "string",
                            "description": "The reviewer's ID.",
                        },
                    },
                    "required": ["submission_id", "reviewer_user_id"],
                },
            },
        }
