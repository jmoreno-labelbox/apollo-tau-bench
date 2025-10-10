from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class AddMentorshipRelationship(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        mentor_id: str,
        mentee_id: str,
        start_date: str,
        status: str,
        focus_areas: list[str],
    ) -> str:
        relationships = data.setdefault("user_mentorship_relationships", [])

        # --- Mechanism for automatically creating relationship_id ---
        if not relationships:
            new_id_num = 1
        else:
            # Determine the maximum current ID value to avoid conflicts.
            max_id = 0
            for rel in relationships:
                try:
                    num = int(rel["relationship_id"][2:])  #Presumes the format MR### Assumes the structure MR###
                    if num > max_id:
                        max_id = num
                except (ValueError, IndexError):
                    continue  # Exclude improperly formatted IDs.
            new_id_num = max_id + 1

        new_relationship_id = f"MR{new_id_num:03d}"  # Formatted as MR001, MR015, etc.

        new_relationship = {
            "relationship_id": new_relationship_id,
            "mentor_id": mentor_id,
            "mentee_id": mentee_id,
            "start_date": start_date,
            "status": status,
            "focus_areas": focus_areas,
        }

        relationships.append(new_relationship)
        payload = {
                "success": f"Mentorship relationship {new_relationship_id} created",
                "relationship_id": new_relationship_id,
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
                "name": "AddMentorshipRelationship",
                "description": "Create a new mentorship relationship with an auto-generated ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "mentor_id": {"type": "string"},
                        "mentee_id": {"type": "string"},
                        "start_date": {"type": "string"},
                        "status": {"type": "string"},
                        "focus_areas": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": [
                        "mentor_id",
                        "mentee_id",
                        "start_date",
                        "status",
                        "focus_areas",
                    ],
                },
            },
        }
