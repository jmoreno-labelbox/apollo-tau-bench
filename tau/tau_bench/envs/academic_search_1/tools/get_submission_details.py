from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetSubmissionDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], submission_id: Any = None) -> str:
        if not submission_id:
            payload = {"error": "submission_id is required."}
            out = json.dumps(payload)
            return out

        submissions = data.get("submissions", {}).values()
        for sub in submissions.values():
            if sub.get("proposal_id") == submission_id:
                payload = sub
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Submission with ID '{submission_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSubmissionDetails",
                "description": "Retrieves the full details for a single submission by its unique ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "submission_id": {
                            "type": "string",
                            "description": "The unique ID of the submission to retrieve.",
                        }
                    },
                    "required": ["submission_id"],
                },
            },
        }
