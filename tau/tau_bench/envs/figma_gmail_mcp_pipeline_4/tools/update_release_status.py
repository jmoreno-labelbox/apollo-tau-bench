# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateReleaseStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], new_status, release_id, thread_id, release_metadata = {}, version_notes = '') -> str:
        """
        Updates release status and manages release workflow metadata.
        """

        if not all([release_id, new_status]):
            return json.dumps({"error": "release_id and new_status are required."})

        # Check the validity of status values.
        valid_statuses = ['DRAFT', 'IN_REVIEW', 'APPROVED', 'PUBLISHED', 'ARCHIVED']
        if new_status not in valid_statuses:
            return json.dumps({"error": f"Invalid status. Must be one of: {', '.join(valid_statuses)}"})

        releases = data.get('releases', [])

        # Locate the deployment.
        release_found = False
        for release in releases:
            if release.get('release_id') == release_id:
                release_found = True
                old_status = release.get('status', 'DRAFT')

                # Modify the release state.
                release['status'] = new_status
                release['last_updated'] = datetime.now().isoformat()

                # Revise thread linkage
                if thread_id:
                    release['thread_id_nullable'] = thread_id

                # Include version details.
                if version_notes:
                    if 'version_history' not in release:
                        release['version_history'] = []
                    release['version_history'].append({
                        "timestamp": datetime.now().isoformat(),
                        "status": new_status,
                        "notes": version_notes
                    })

                # Revise metadata
                if release_metadata:
                    for key, value in release_metadata.items():
                        release[key] = value

                # Record the status update.
                if 'status_history' not in release:
                    release['status_history'] = []
                release['status_history'].append({
                    "from_status": old_status,
                    "to_status": new_status,
                    "changed_at": datetime.now().isoformat(),
                    "notes": version_notes
                })

                break

        if not release_found:
            return json.dumps({"error": f"Release with ID '{release_id}' not found."})

        return json.dumps({
            "success": True,
            "release_id": release_id,
            "old_status": old_status,
            "new_status": new_status,
            "updated_at": datetime.now().isoformat()
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_release_status",
                "description": "Updates release status and manages release workflow metadata including version notes and thread associations.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "release_id": {"type": "string", "description": "The ID of the release to update."},
                        "new_status": {"type": "string", "description": "The new status for the release. Must be one of: DRAFT, IN_REVIEW, APPROVED, PUBLISHED, ARCHIVED."},
                        "version_notes": {"type": "string", "description": "Optional notes about the version update or status change."},
                        "thread_id": {"type": "string", "description": "Optional Gmail thread ID to associate with the release."},
                        "release_metadata": {"type": "object", "description": "Additional metadata fields to update on the release."}
                    },
                    "required": ["release_id", "new_status"]
                }
            }
        }
