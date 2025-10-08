from tau_bench.envs.tool import Tool
import json
from typing import Any

class ShortlistSuccessorCandidate(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str, target_role: str) -> str:
        # Create a consistent date derived from user_id and target_role
        import hashlib

        hash_input = f"{user_id}_{target_role}"
        hash_value = int(hashlib.md5(hash_input.encode()).hexdigest()[:8], 16)
        days_offset = hash_value % 30  # A range of 0 to 29 days from the reference date

        # Employ a constant base date to ensure consistent outcomes
        base_date = "2025-06-01"
        from datetime import datetime, timedelta

        base_dt = datetime.strptime(base_date, "%Y-%m-%d")
        shortlist_date = (base_dt + timedelta(days=days_offset)).strftime("%Y-%m-%d")

        entry = {
            "user_id": user_id,
            "target_role": target_role,
            "status": "shortlisted",
            "shortlist_date": shortlist_date,
        }
        data.setdefault("hr_workflows", []).append(entry)
        payload = {"message": "Candidate shortlisted.", "record": entry}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ShortlistSuccessorCandidate",
                "description": "Marks a user as a shortlisted candidate for succession into a target role with deterministic date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The user being shortlisted.",
                        },
                        "target_role": {
                            "type": "string",
                            "description": "The target role under consideration.",
                        },
                    },
                    "required": ["user_id", "target_role"],
                },
            },
        }
