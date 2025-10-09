from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetSkillGapAnalysis(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = "", analysis_id: str = "") -> str:
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
            payload = {"error": "Either user_id or analysis_id required"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        return (
            json.dumps(analysis, indent=2)
            if analysis
            else json.dumps({"error": "Analysis not found"}, indent=2)
        )
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "getSkillGapAnalysis",
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
