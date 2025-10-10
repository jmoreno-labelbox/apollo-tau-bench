# © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_skill_gap_analysis(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str = "", analysis_id: str = "") -> str:
        skill_gaps = data.get("skill_gap_analysis", [])
        if analysis_id:
            analysis = next(
                (s for s in skill_gaps if s.get("analysis_id") == analysis_id), None
            )
        elif user_id:
            analysis = next(
                (s for s in skill_gaps if s.get("user_id") == user_id), None
            )
        else:
            return json.dumps(
                {"error": "Either user_id or analysis_id required"}, indent=2
            )

        return (
            json.dumps(analysis, indent=2)
            if analysis
            else json.dumps({"error": "Analysis not found"}, indent=2)
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "get_skill_gap_analysis",
                "description": "Get skill gap analysis by user ID or analysis ID",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "analysis_id": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }
