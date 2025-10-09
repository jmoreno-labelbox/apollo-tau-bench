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

class UpdateReleaseVersion(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        release_id: str = None,
        version_id: str = None,
        release_name: str = None,
        owner_email: str = None,
        thread_id: str = None
    ) -> str:
        """
        Modifies release version information and oversees the release lifecycle.
        """
        if not all([release_id, version_id]):
            payload = {"error": "release_id and version_id are required."}
            out = json.dumps(payload)
            return out

        releases = data.get("releases", {}).values()

        # Locate the release
        release_found = False
        for release in releases.values():
            if release.get("release_id") == release_id:
                release_found = True
                old_version = release.get("version_id")

                # Revise release details
                release["version_id"] = version_id
                release["last_updated"] = datetime.now().isoformat()

                # Change optional fields if specified
                if release_name:
                    release["release_name"] = release_name
                if owner_email:
                    release["owner_email"] = owner_email
                if thread_id:
                    release["thread_id_nullable"] = thread_id

                # Document the change in version
                if "version_history" not in release:
                    release["version_history"] = []
                release["version_history"].append(
                    {
                        "from_version": old_version,
                        "to_version": version_id,
                        "changed_at": datetime.now().isoformat(),
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
            "old_version": old_version,
            "new_version": version_id,
            "updated_at": datetime.now().isoformat(),
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateReleaseVersion",
                "description": "Updates release version information and manages release lifecycle with optional metadata updates.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "release_id": {
                            "type": "string",
                            "description": "The ID of the release to update.",
                        },
                        "version_id": {
                            "type": "string",
                            "description": "The new version ID for the release.",
                        },
                        "release_name": {
                            "type": "string",
                            "description": "Optional new release name.",
                        },
                        "owner_email": {
                            "type": "string",
                            "description": "Optional new owner email.",
                        },
                        "thread_id": {
                            "type": "string",
                            "description": "Optional thread ID for release coordination.",
                        },
                    },
                    "required": ["release_id", "version_id"],
                },
            },
        }
