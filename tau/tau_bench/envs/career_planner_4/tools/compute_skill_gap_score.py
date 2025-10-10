# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class compute_skill_gap_score(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str) -> str:
        # Simulated calculation - in a real system, it would assess genuine skill deficiencies.
        score = 45  # Simulated score under limit
        return json.dumps({"readiness_score": score, "user_id": user_id}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "compute_skill_gap_score",
                "description": "Compute skill gap readiness score for a user",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }
