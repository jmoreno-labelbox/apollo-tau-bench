# Copyright Sierra Technologies

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ShortlistSuccessorCandidate(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs["user_id"]
        target_role = kwargs["target_role"]

        # Create a consistent date using user_id and target_role.
        import hashlib

        hash_input = f"{user_id}_{target_role}"
        hash_value = int(hashlib.md5(hash_input.encode()).hexdigest()[:8], 16)
        days_offset = hash_value % 30  # 0-29 days from the reference date

        # Utilize a constant base date for consistent outcomes.
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
        return json.dumps(
            {"message": "Candidate shortlisted.", "record": entry}, indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "shortlist_successor_candidate",
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
                    "required": ["user_id", "target_role", "succession_for_role"],
                },
            },
        }
