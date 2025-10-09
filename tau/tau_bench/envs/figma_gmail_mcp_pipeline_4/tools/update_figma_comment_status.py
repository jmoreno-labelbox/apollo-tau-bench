from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateFigmaCommentStatus(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        comment_id: str,
        new_status: str,
        resolution_notes: str = "",
        assignee_email: str = None,
        priority_level: str = None,
        resolved_by: str = None
    ) -> str:
        # Support resolved_by as alternative to assignee_email
        if resolved_by is not None:
            assignee_email = resolved_by
        """
        Changes Figma comment status and oversees comment workflow.
        """
        if not all([comment_id, new_status]):
            payload = {"error": "comment_id and new_status are required."}
            out = json.dumps(payload)
            return out

        # Check the correctness of status values
        valid_statuses = ["OPEN", "IN_PROGRESS", "RESOLVED", "CLOSED", "ARCHIVED"]
        if new_status not in valid_statuses:
            payload = {
                "error": f"Invalid status. Must be one of: {', '.join(valid_statuses)}"
            }
            out = json.dumps(payload)
            return out

        figma_comments = data.get("figma_comments", [])

        # Locate the comment
        comment_found = False
        for comment in figma_comments:
            if comment.get("comment_id") == comment_id:
                comment_found = True
                old_status = comment.get("comment_status", "OPEN")
                old_resolved = comment.get("resolved_flag", False)

                # Change the status of the comment
                comment["comment_status"] = new_status
                comment["last_updated"] = datetime.now().isoformat()

                # Modify the resolved flag according to status
                if new_status in ["RESOLVED", "CLOSED", "ARCHIVED"]:
                    comment["resolved_flag"] = True
                    comment["resolved_at"] = datetime.now().isoformat()
                else:
                    comment["resolved_flag"] = False

                # Revise assignee if specified
                if assignee_email:
                    comment["assignee_email"] = assignee_email
                elif "assignee_email" in comment:
                    del comment["assignee_email"]

                # Change priority if supplied
                if priority_level:
                    comment["priority_level"] = priority_level
                elif "priority_level" in comment:
                    del comment["priority_level"]

                # Include notes regarding the resolution
                if resolution_notes:
                    if "resolution_history" not in comment:
                        comment["resolution_history"] = []
                    comment["resolution_history"].append(
                        {
                            "timestamp": datetime.now().isoformat(),
                            "status": new_status,
                            "notes": resolution_notes,
                            "assignee": assignee_email,
                        }
                    )

                # Document the change in status
                if "status_history" not in comment:
                    comment["status_history"] = []
                comment["status_history"].append(
                    {
                        "from_status": old_status,
                        "to_status": new_status,
                        "resolved_changed": old_resolved != comment["resolved_flag"],
                        "changed_at": datetime.now().isoformat(),
                        "notes": resolution_notes,
                    }
                )

                break

        if not comment_found:
            payload = {"error": f"Comment with ID '{comment_id}' not found."}
            out = json.dumps(payload)
            return out
        payload = {
            "success": True,
            "comment_id": comment_id,
            "old_status": old_status,
            "new_status": new_status,
            "resolved_flag": comment["resolved_flag"],
            "updated_at": datetime.now().isoformat(),
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateFigmaCommentStatus",
                "description": "Updates Figma comment status and manages comment workflow including resolution tracking and assignment.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "comment_id": {
                            "type": "string",
                            "description": "The ID of the comment to update.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new comment status. Must be one of: OPEN, IN_PROGRESS, RESOLVED, CLOSED, ARCHIVED.",
                        },
                        "resolution_notes": {
                            "type": "string",
                            "description": "Optional notes about the resolution or status change.",
                        },
                        "assignee_email": {
                            "type": "string",
                            "description": "Optional email of the person assigned to handle the comment.",
                        },
                        "priority_level": {
                            "type": "string",
                            "description": "Optional priority level (e.g., 'LOW', 'MEDIUM', 'HIGH', 'CRITICAL').",
                        },
                    },
                    "required": ["comment_id", "new_status"],
                },
            },
        }
