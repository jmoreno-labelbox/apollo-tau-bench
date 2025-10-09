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

class CheckTeamTrainingThreshold(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], team_id: str, threshold: int, comparison: str
    ) -> str:
        # Simulated calculation of team training hours
        training_data = data.get("team_training_log", [])
        team_sessions = [t for t in training_data if t.get("team_id") == team_id]

        # Simulated calculation - in a real system, actual training hours would be totaled
        total_hours = len(team_sessions) * 25  # Presume 25 hours for each session

        if comparison == "below":
            condition_met = total_hours < threshold
            payload = {
                "condition_met": condition_met,
                "team_id": team_id,
                "total_hours": total_hours,
                "threshold": threshold,
                "comparison": comparison,
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        else:
            condition_met = total_hours >= threshold
            payload = {
                "condition_met": condition_met,
                "team_id": team_id,
                "total_hours": total_hours,
                "threshold": threshold,
                "comparison": comparison,
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out


    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "checkTeamTrainingThreshold",
                "description": "Check if team training hours meet threshold",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {"type": "string"},
                        "threshold": {"type": "integer"},
                        "comparison": {"type": "string", "enum": ["below", "above"]},
                    },
                    "required": ["team_id", "threshold", "comparison"],
                },
            },
        }
