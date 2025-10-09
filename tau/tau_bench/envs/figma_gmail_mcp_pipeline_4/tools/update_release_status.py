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

class UpdateReleaseStatus(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        release_id: str,
        new_status: str = None,
        release_metadata: dict[str, Any] = None,
        thread_id: str = None,
        version_notes: str = "",
        release_notes: str = None,
        updated_by: str = None
    ) -> str:
        # Support release_notes as alternative to version_notes
        if release_notes is not None:
            version_notes = release_notes
        """
        Changes release status and oversees release workflow metadata.
        """
        if release_metadata is None:
            release_metadata = {}

        if not all([release_id, new_status]):
            payload = {"error": "release_id and new_status are required."}
            out = json.dumps(payload)
            return out

        # Verify the correctness of status values
        valid_statuses = ["DRAFT", "IN_REVIEW", "APPROVED", "PUBLISHED", "ARCHIVED"]
        if new_status not in valid_statuses:
            payload = {
                "error": f"Invalid status. Must be one of: {', '.join(valid_statuses)}"
            }
            out = json.dumps(payload)
            return out

        releases = data.get("releases", {}).values()

        # Identify the release
        release_found = False
        for release in releases.values():
            if release.get("release_id") == release_id:
                release_found = True
                old_status = release.get("status", "DRAFT")

                # Change the status of the release
                release["status"] = new_status
                release["last_updated"] = datetime.now().isoformat()

                # Modify the association of the thread
                if thread_id:
                    release["thread_id_nullable"] = thread_id

                # Include notes about the version
                if version_notes:
                    if "version_history" not in release:
                        release["version_history"] = []
                    release["version_history"].append(
                        {
                            "timestamp": datetime.now().isoformat(),
                            "status": new_status,
                            "notes": version_notes,
                        }
                    )

                # Revise metadata
                if release_metadata:
                    for key, value in release_metadata.items():
                        release[key] = value

                # Document the status change
                if "status_history" not in release:
                    release["status_history"] = []
                release["status_history"].append(
                    {
                        "from_status": old_status,
                        "to_status": new_status,
                        "changed_at": datetime.now().isoformat(),
                        "notes": version_notes,
                    }
                )

                break

        if not release_found:
            payload = {"error": f"Release with ID '{release_id}' not found."}
            out = json.dumps(payload)
            return out
        payload = {
            "success": True,
            "release_id": release_id,
            "old_status": old_status,
            "new_status": new_status,
            "updated_at": datetime.now().isoformat(),
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateReleaseStatus",
                "description": "Updates release status and manages release workflow metadata including version notes and thread associations.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "release_id": {
                            "type": "string",
                            "description": "The ID of the release to update.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new status for the release. Must be one of: DRAFT, IN_REVIEW, APPROVED, PUBLISHED, ARCHIVED.",
                        },
                        "version_notes": {
                            "type": "string",
                            "description": "Optional notes about the version update or status change.",
                        },
                        "thread_id": {
                            "type": "string",
                            "description": "Optional Gmail thread ID to associate with the release.",
                        },
                        "release_metadata": {
                            "type": "object",
                            "description": "Additional metadata fields to update on the release.",
                        },
                    },
                    "required": ["release_id", "new_status"],
                },
            },
        }
