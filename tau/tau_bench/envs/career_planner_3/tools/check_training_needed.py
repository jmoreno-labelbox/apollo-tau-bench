# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CheckTrainingNeeded(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id")
        target_role = kwargs.get("target_role")
        gaps = data.get("skill_gap_analysis", [])
        user_gaps = [
            g
            for g in gaps
            if g["user_id"] == user_id and g["target_role"] == target_role
        ]

        if not user_gaps:
            return json.dumps(
                {"training_needed": False, "reason": "No skill gap analysis found"},
                indent=2,
            )

        gap = user_gaps[0]
        readiness_score = gap.get("overall_readiness_score", 0)

        if readiness_score < 70:
            return json.dumps(
                {
                    "training_needed": True,
                    "readiness_score": readiness_score,
                    "reason": f"Readiness score {readiness_score} is below threshold of 70",
                },
                indent=2,
            )

        return json.dumps(
            {
                "training_needed": False,
                "readiness_score": readiness_score,
                "reason": f"Readiness score {readiness_score} meets threshold",
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "check_training_needed",
                "description": "Checks if training is needed for a user targeting a specific role based on readiness score.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The user to check.",
                        },
                        "target_role": {
                            "type": "string",
                            "description": "The target role to evaluate.",
                        },
                    },
                    "required": ["user_id", "target_role"],
                },
            },
        }
