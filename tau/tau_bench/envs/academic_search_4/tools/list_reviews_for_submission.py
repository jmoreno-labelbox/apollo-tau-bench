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

class ListReviewsForSubmission(Tool):
    """Lists all evaluations submitted for a specific submission."""
    @staticmethod
    def invoke(data: dict[str, Any], *, submission_id: Any = None) -> str:
        if not submission_id:
            payload = {"error": "submission_id is required."}
            out = json.dumps(payload)
            return out

        reviews = data.get("reviews", {}).values()
        submission_reviews = [
            r for r in reviews.values() if r.get("submission_id") == submission_id
        ]
        payload = submission_reviews
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListReviewsForSubmission",
                "description": "Lists all submitted reviews for a specific submission ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "submission_id": {
                            "type": "string",
                            "description": "The ID of the submission to get reviews for.",
                        }
                    },
                    "required": ["submission_id"],
                },
            },
        }
