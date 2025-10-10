# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_unused_review_id(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        reviews = list(data.get("reviews", {}).values())
        prefix = "PR"
        start_num = 10000
        if not reviews:
            return json.dumps(f"{prefix}{start_num}", indent=2)
        max_id_num = 0
        for review in reviews:
            review_id = review.get("review_id", "")
            if review_id.startswith(prefix):
                try:
                    num = int(review_id[len(prefix) :])
                    if num > max_id_num:
                        max_id_num = num
                except (ValueError, TypeError):
                    continue
        next_id = f"{prefix}{max(start_num, max_id_num) + 1}"
        return json.dumps(next_id, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_unused_review_id",
                "description": "Return a performance review ID that is not currently in use.",
                "parameters": {},
            },
        }
