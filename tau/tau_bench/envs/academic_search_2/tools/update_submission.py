from tau_bench.envs.tool import Tool
import json
import uuid
from collections import Counter
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateSubmission(Tool):
    """Modifies a submission's status or replaces its list of reviewers."""

    @staticmethod
    def invoke(data: dict[str, Any], submission_id: Any = None, reviewers: Any = None, status: str = None) -> str:
        submission_id = submission_id
        if not submission_id:
            payload = {"error": "submission_id is required."}
            out = json.dumps(payload)
            return out

        submission = next(
            (
                s
                for s in data.get("submissions", [])
                if s.get("proposal_id") == submission_id
            ),
            None,
        )
        if not submission:
            payload = {"error": "Submission not found."}
            out = json.dumps(payload)
            return out

        if reviewers is not None:
            provided_reviewers = reviewers
            users = data.get("users", [])

            valid_reviewer_ids = []
            for reviewer_item in provided_reviewers:
                if any(u.get("person_id") == reviewer_item for u in users):
                    valid_reviewer_ids.append(reviewer_item)
                else:
                    found_user = next(
                        (u for u in users if u.get("label") == reviewer_item), None
                    )
                    if found_user:
                        valid_reviewer_ids.append(found_user["person_id"])

            submission["allocated_evaluators"] = sorted(list(set(valid_reviewer_ids)))

        if status is not None:
            submission["state"] = status
        payload = {"success": True, "submission": submission}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateSubmission",
                "description": "Updates a submission's status or overwrites its list of reviewers.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "submission_id": {"type": "string"},
                        "reviewers": {
                            "type": "array",
                            "items": {
                                "type": "string",
                                "description": "List of reviewer user_ids or names to assign.",
                            },
                        },
                        "status": {"type": "string"},
                    },
                    "required": ["submission_id"],
                },
            },
        }
