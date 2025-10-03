from tau_bench.envs.tool import Tool
import json
from typing import Any

class get_unused_review_id(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], reviews: list = None) -> str:
        reviews = reviews if reviews is not None else data.get("reviews", [])
        prefix = "PR"
        start_num = 10000
        if not reviews:
            payload = f"{prefix}{start_num}"
            out = json.dumps(payload, indent=2)
            return out
        max_id_num = 0
        for review in reviews:
            review_id = review.get("review_id", "")
            if review_id.startswith(prefix):
                try:
                    num = int(review_id[len(prefix):])
                    if num > max_id_num:
                        max_id_num = num
                except (ValueError, TypeError):
                    continue
        next_id = f"{prefix}{max(start_num, max_id_num) + 1}"
        payload = next_id
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUnusedReviewId",
                "description": "Return a performance review ID that is not currently in use.",
                "parameters": {},
            },
        }
