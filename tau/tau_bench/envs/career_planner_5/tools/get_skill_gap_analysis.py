# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_skill_gap_analysis(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], analysis_id: str = "", user_id: str = "") -> str:
        analyses = data.get("skill_gap_analysis", [])
        if analysis_id:
            analysis = next(
                (a for a in analyses if a.get("analysis_id") == analysis_id), None
            )
        elif user_id:
            analysis = next((a for a in analyses if a.get("user_id") == user_id), None)
        else:
            return json.dumps(
                {"error": "Must provide either analysis_id or user_id"}, indent=2
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
                "description": "Get skill gap analysis by ID or user ID",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "analysis_id": {"type": "string"},
                        "user_id": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }
