# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class compute_skill_gap_score(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str) -> str:
        # Mock computation - in real system would analyze actual skill gaps
        score = 45  # Mock score below threshold
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
