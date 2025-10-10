# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class perform_soft_skill_gap_analysis(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, skills: list) -> str:
        analysis = {
            "analysis_id": f"SGA{int(datetime.now().timestamp() * 1000) % 10000}",
            "user_id": user_id,
            "skills_analyzed": skills,
            "readiness_score": 65,  # Simulated score
            "date": "2025-07-04",
        }
        data.setdefault("skill_gap_analysis", []).append(analysis)
        return json.dumps(
            {"success": f"Analysis completed for user {user_id}", "analysis": analysis},
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "perform_soft_skill_gap_analysis",
                "description": "Perform soft skill gap analysis for a user",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "skills": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["user_id", "skills"],
                },
            },
        }
