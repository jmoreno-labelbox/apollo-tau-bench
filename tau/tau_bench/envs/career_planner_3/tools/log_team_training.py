# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LogTeamTraining(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], course_id, skill_name, user_id) -> str:

        # Implement a basic hash-based method for generating consistent dates.
        import hashlib

        hash_input = f"{user_id}_{course_id}"
        hash_value = int(hashlib.md5(hash_input.encode()).hexdigest()[:8], 16)
        days_offset = hash_value % 30  # 0 to 29 days from the reference date

        # Utilize a constant base date for predictable outcomes.
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
        # This line retrieves the 'team_training_log' list from the data and appends the new entry.
        # It first creates the list if it does not already exist.
        data.setdefault("team_training_log", []).append(entry)
        return json.dumps({"message": "Training logged.", "entry": entry}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "log_team_training",
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
