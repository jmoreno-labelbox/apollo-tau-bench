# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class check_readiness_threshold(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], user_id: str, threshold: int, comparison: str
    ) -> str:
        # Stub implementation - in a production environment, it would verify true readiness metrics.
        readiness_score = 75  # Simulated score

        if comparison == "below":
            meets_condition = readiness_score < threshold
        elif comparison == "above":
            meets_condition = readiness_score > threshold
        else:
            meets_condition = readiness_score == threshold

        return json.dumps(
            {
                "user_id": user_id,
                "readiness_score": readiness_score,
                "threshold": threshold,
                "comparison": comparison,
                "meets_condition": meets_condition,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "check_readiness_threshold",
                "description": "Check if user's readiness score meets threshold",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "threshold": {"type": "integer"},
                        "comparison": {"type": "string"},
                    },
                    "required": ["user_id", "threshold", "comparison"],
                },
            },
        }
