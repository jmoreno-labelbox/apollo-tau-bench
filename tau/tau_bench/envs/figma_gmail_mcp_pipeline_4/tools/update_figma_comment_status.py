# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateFigmaCommentStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Updates Figma comment status and manages comment workflow.
        """
        comment_id = kwargs.get('comment_id')
        new_status = kwargs.get('new_status')
        resolution_notes = kwargs.get('resolution_notes', '')
        assignee_email = kwargs.get('assignee_email')
        priority_level = kwargs.get('priority_level')

        if not all([comment_id, new_status]):
            return json.dumps({"error": "comment_id and new_status are required."})

        # Validate status values
        valid_statuses = ['OPEN', 'IN_PROGRESS', 'RESOLVED', 'CLOSED', 'ARCHIVED']
        if new_status not in valid_statuses:
            return json.dumps({"error": f"Invalid status. Must be one of: {', '.join(valid_statuses)}"})

        figma_comments = data.get('figma_comments', [])

        # Find the comment
        comment_found = False
        for comment in figma_comments:
            if comment.get('comment_id') == comment_id:
                comment_found = True
                old_status = comment.get('comment_status', 'OPEN')
                old_resolved = comment.get('resolved_flag', False)

                # Update comment status
                comment['comment_status'] = new_status
                comment['last_updated'] = datetime.now().isoformat()

                # Update resolved flag based on status
                if new_status in ['RESOLVED', 'CLOSED', 'ARCHIVED']:
                    comment['resolved_flag'] = True
                    comment['resolved_at'] = datetime.now().isoformat()
                else:
                    comment['resolved_flag'] = False

                # Update assignee if provided
                if assignee_email:
                    comment['assignee_email'] = assignee_email
                elif 'assignee_email' in comment:
                    del comment['assignee_email']

                # Update priority if provided
                if priority_level:
                    comment['priority_level'] = priority_level
                elif 'priority_level' in comment:
                    del comment['priority_level']

                # Add resolution notes
                if resolution_notes:
                    if 'resolution_history' not in comment:
                        comment['resolution_history'] = []
                    comment['resolution_history'].append({
                        "timestamp": datetime.now().isoformat(),
                        "status": new_status,
                        "notes": resolution_notes,
                        "assignee": assignee_email
                    })

                # Log the status change
                if 'status_history' not in comment:
                    comment['status_history'] = []
                comment['status_history'].append({
                    "from_status": old_status,
                    "to_status": new_status,
                    "resolved_changed": old_resolved != comment['resolved_flag'],
                    "changed_at": datetime.now().isoformat(),
                    "notes": resolution_notes
                })

                break

        if not comment_found:
            return json.dumps({"error": f"Comment with ID '{comment_id}' not found."})

        return json.dumps({
            "success": True,
            "comment_id": comment_id,
            "old_status": old_status,
            "new_status": new_status,
            "resolved_flag": comment['resolved_flag'],
            "updated_at": datetime.now().isoformat()
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_figma_comment_status",
                "description": "Updates Figma comment status and manages comment workflow including resolution tracking and assignment.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "comment_id": {"type": "string", "description": "The ID of the comment to update."},
                        "new_status": {"type": "string", "description": "The new comment status. Must be one of: OPEN, IN_PROGRESS, RESOLVED, CLOSED, ARCHIVED."},
                        "resolution_notes": {"type": "string", "description": "Optional notes about the resolution or status change."},
                        "assignee_email": {"type": "string", "description": "Optional email of the person assigned to handle the comment."},
                        "priority_level": {"type": "string", "description": "Optional priority level (e.g., 'LOW', 'MEDIUM', 'HIGH', 'CRITICAL')."}
                    },
                    "required": ["comment_id", "new_status"]
                }
            }
        }
