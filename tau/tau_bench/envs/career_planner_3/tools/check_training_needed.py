from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CheckTrainingNeeded(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, target_role: str = None) -> str:
        gaps = data.get("skill_gap_analysis", {}).values()
        user_gaps = [
            g
            for g in gaps.values() if g["user_id"] == user_id and g["target_role"] == target_role
        ]

        if not user_gaps:
            payload = {"training_needed": False, "reason": "No skill gap analysis found"}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        gap = user_gaps[0]
        readiness_score = gap.get("overall_readiness_score", 0)

        if readiness_score < 70:
            payload = {
                    "training_needed": True,
                    "readiness_score": readiness_score,
                    "reason": f"Readiness score {readiness_score} is below threshold of 70",
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = {
                "training_needed": False,
                "readiness_score": readiness_score,
                "reason": f"Readiness score {readiness_score} meets threshold",
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CheckTrainingNeeded",
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
