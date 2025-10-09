from tau_bench.envs.tool import Tool
import json
from typing import Any

class LogTeamTraining(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str, course_id: str, skill_name: str) -> str:
        # Create a consistent date derived from user_id and course_id

        # Develop a straightforward hash-based method for date generation to ensure uniformity
        import hashlib

        hash_input = f"{user_id}_{course_id}"
        hash_value = int(hashlib.md5(hash_input.encode()).hexdigest()[:8], 16)
        days_offset = hash_value % 30  # A duration of 0 to 29 days from the reference date

        # Adopt a constant base date for predictable outcomes
        base_date = "2025-07-01"
        from datetime import datetime, timedelta

        base_dt = datetime.strptime(base_date, "%Y-%m-%d")
        log_date = (base_dt + timedelta(days=days_offset)).strftime("%Y-%m-%d")

        entry = {
            "user_id": user_id,
            "skill_name": skill_name,
            "course_id": course_id,
            "log_date": log_date,
        }
        # This line locates the 'team_training_log' array in the data and appends the new entry.
        # If the array is absent, it initializes it first.
        data.setdefault("team_training_log", []).append(entry)
        payload = {"message": "Training logged.", "entry": entry}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LogTeamTraining",
                "description": "Logs a course training entry for a user for a specific skill with deterministic date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the employee.",
                        },
                        "skill_name": {
                            "type": "string",
                            "description": "The skill being trained.",
                        },
                        "course_id": {
                            "type": "string",
                            "description": "The ID of the course used.",
                        },
                    },
                    "required": ["user_id", "skill_name", "course_id"],
                },
            },
        }
