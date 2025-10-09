from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class GetReviewBySubmission(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], *, submission_id: Any = None) -> str:
        submission_id = submission_id
        if not submission_id:
            payload = {"error": "submission_id is required."}
            out = json.dumps(payload)
            return out

        reviews = data.get("reviews", [])
        for review in reviews:
            if review.get("proposal_id") == submission_id:
                payload = review
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No review found for submission_id '{submission_id}'."}
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetReviewBySubmission",
                "description": "Retrieves a review's details using the ID of the submission.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "submission_id": {
                            "type": "string",
                            "description": "The unique ID of the submission to find the review for.",
                        }
                    },
                    "required": ["submission_id"],
                },
            },
        }
