from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateMentorshipRelationship(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], relationship_id: str, updates: dict[str, Any]
    ) -> str:
        rel = next(
            (
                r
                for r in data.get("user_mentorship_relationships", {}).values()
                if r["relationship_id"] == relationship_id
            ),
            None,
        )
        if not rel:
            payload = {"error": "relationship not found"}
            out = json.dumps(payload)
            return out

        #--- SIMPLIFIED LOGIC ---
        #The tool now solely executes a direct update.
        rel.update(updates)
        payload = {"success": f"relationship {relationship_id} updated"}
        out = json.dumps(payload)
        return out


        #--- SIMPLIFIED LOGIC ---
        #The tool now solely executes a direct update.
        rel.update(updates)
        payload = {"success": f"relationship {relationship_id} updated"}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "UpdateMentorshipRelationship",
                "description": "Modify attributes of an existing mentorship relationship by overwriting them with new values.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "relationship_id": {"type": "string"},
                        "updates": {"type": "object"},
                    },
                    "required": ["relationship_id", "updates"],
                },
            },
        }
