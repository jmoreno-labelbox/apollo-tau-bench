from tau_bench.envs.tool import Tool
import json
import re
import uuid
from collections import Counter
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class SetSubmissionOutcome(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], submission_id: Any = None, new_status: Any = None) -> str:
        if not all([submission_id, new_status]):
            payload = {"error": "submission_id and new_status are required."}
            out = json.dumps(payload)
            return out

        submissions = data.get("submissions", {}).values()
        for sub in submissions.values():
            if sub.get("submission_id") == submission_id:
                sub["status"] = new_status
                payload = {"success": True, "submission": sub}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Submission with ID '{submission_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetSubmissionOutcome",
                "description": "Sets the outcome or status for a submission (e.g., 'accepted', 'rejected').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "submission_id": {
                            "type": "string",
                            "description": "The ID of the submission to update.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new status to set for the submission.",
                        },
                    },
                    "required": ["submission_id", "new_status"],
                },
            },
        }
