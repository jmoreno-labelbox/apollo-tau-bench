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

class AssignReviewer(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], submission_id: Any = None, reviewer_user_id: Any = None, overwrite: Any = None) -> str:
        submissions = data.get("submissions", {}).values()
        for sub in submissions.values():
            if sub.get("submission_id") == submission_id or sub.get("proposal_id") == submission_id:
                if overwrite:
                    sub["allocated_evaluators"] = [reviewer_user_id]
                else:
                    if "allocated_evaluators" not in sub:
                        sub["allocated_evaluators"] = []
                    if reviewer_user_id not in sub["allocated_evaluators"]:
                        sub["allocated_evaluators"].append(reviewer_user_id)

                sub["status"] = "under_review"
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
                "name": "AssignReviewer",
                "description": "Assigns a reviewer to an article submission, with an option to overwrite the existing list.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "submission_id": {
                            "type": "string",
                            "description": "The ID of the submission.",
                        },
                        "reviewer_user_id": {
                            "type": "string",
                            "description": "The user ID of the person assigned to review.",
                        },
                        "overwrite": {
                            "type": "boolean",
                            "description": "If true, replaces the reviewer list. Defaults to false (append).",
                        },
                    },
                    "required": ["submission_id", "reviewer_user_id"],
                },
            },
        }
