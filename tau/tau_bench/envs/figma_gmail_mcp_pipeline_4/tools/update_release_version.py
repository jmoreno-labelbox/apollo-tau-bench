# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateReleaseVersion(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Updates release version information and manages release lifecycle.
        """
        release_id = kwargs.get('release_id')
        version_id = kwargs.get('version_id')
        release_name = kwargs.get('release_name')
        owner_email = kwargs.get('owner_email')
        thread_id = kwargs.get('thread_id')

        if not all([release_id, version_id]):
            return json.dumps({"error": "release_id and version_id are required."})

        releases = data.get('releases', [])

        # Find the release
        release_found = False
        for release in releases:
            if release.get('release_id') == release_id:
                release_found = True
                old_version = release.get('version_id')

                # Update release information
                release['version_id'] = version_id
                release['last_updated'] = datetime.now().isoformat()

                # Update optional fields if provided
                if release_name:
                    release['release_name'] = release_name
                if owner_email:
                    release['owner_email'] = owner_email
                if thread_id:
                    release['thread_id_nullable'] = thread_id

                # Log the version change
                if 'version_history' not in release:
                    release['version_history'] = []
                release['version_history'].append({
                    "from_version": old_version,
                    "to_version": version_id,
                    "changed_at": datetime.now().isoformat()
                })

                break

        if not release_found:
            return json.dumps({"error": f"Release with ID '{release_id}' not found."})

        return json.dumps({
            "success": True,
            "release_id": release_id,
            "old_version": old_version,
            "new_version": version_id,
            "updated_at": datetime.now().isoformat()
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_release_version",
                "description": "Updates release version information and manages release lifecycle with optional metadata updates.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "release_id": {"type": "string", "description": "The ID of the release to update."},
                        "version_id": {"type": "string", "description": "The new version ID for the release."},
                        "release_name": {"type": "string", "description": "Optional new release name."},
                        "owner_email": {"type": "string", "description": "Optional new owner email."},
                        "thread_id": {"type": "string", "description": "Optional thread ID for release coordination."}
                    },
                    "required": ["release_id", "version_id"]
                }
            }
        }
