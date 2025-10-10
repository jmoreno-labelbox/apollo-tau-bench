# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class reassign_mentor(Tool):
    @staticmethod
    def invoke(
        data, user_id: str, old_mentor_id: str, new_mentor_id: str, relationship_id: str
    ) -> str:
        # To streamline, create a new entry to reflect the modification.
        record = {
            "relationship_id": relationship_id,
            "user_id": user_id,
            "mentor_id": new_mentor_id,
            "reassigned_from": old_mentor_id,
            "updated_date": "2023-10-05",
        }
        data.setdefault("mentorship_reassignments", []).append(record)
        return json.dumps(
            {
                "success": f"Mentor reassigned for {user_id}: now under mentor {new_mentor_id}"
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "reassign_mentor",
                "description": "Reassign a mentorship from an old mentor to a new mentor for a specific user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "old_mentor_id": {"type": "string"},
                        "new_mentor_id": {"type": "string"},
                        "relationship_id": {"type": "string"},
                    },
                    "required": [
                        "user_id",
                        "old_mentor_id",
                        "new_mentor_id",
                        "relationship_id",
                    ],
                },
            },
        }
