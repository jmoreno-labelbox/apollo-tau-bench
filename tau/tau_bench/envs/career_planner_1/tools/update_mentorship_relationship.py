# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateMentorshipRelationship(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], relationship_id: str, updates: Dict[str, Any]
    ) -> str:
        rel = next(
            (
                r
                for r in data.get("user_mentorship_relationships", [])
                if r["relationship_id"] == relationship_id
            ),
            None,
        )
        if not rel:
            return json.dumps({"error": "relationship not found"})

        # --- SIMPLIFIED LOGIC ---
        # The tool now only performs a direct update.
        rel.update(updates)
        # --- END OF SIMPLIFICATION ---

        return json.dumps({"success": f"relationship {relationship_id} updated"})

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "update_mentorship_relationship",
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
