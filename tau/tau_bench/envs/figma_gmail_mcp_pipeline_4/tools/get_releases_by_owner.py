# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetReleasesByOwner(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Retrieves releases filtered by owner and other criteria.
        """
        owner_email = kwargs.get('owner_email')
        release_id = kwargs.get('release_id')
        version_tag = kwargs.get('version_tag')
        created_after = kwargs.get('created_after')
        created_before = kwargs.get('created_before')

        if not owner_email:
            return json.dumps({"error": "owner_email is required."})

        releases = data.get('releases', [])

        # Select releases based on specified criteria.
        results = []
        for release in releases:
            # Main filter - owner's email address
            if release.get('owner_email') != owner_email:
                continue

            # Implement optional filtering.
            if release_id:
                if release.get('release_id') != release_id:
                    continue

            if version_tag:
                if version_tag not in release.get('version_tag', ''):
                    continue

            # Implement date filtering.
            if created_after:
                release_created = release.get('created_ts', '')
                if release_created < created_after:
                    continue

            if created_before:
                release_created = release.get('created_ts', '')
                if release_created > created_before:
                    continue

            results.append(release)

        # Generate a concise overview.
        summary = {
            "owner_email": owner_email,
            "total_releases": len(results),
            "version_tags": list(set(r.get('version_tag', '') for r in results)),
            "releases": results
        }

        return json.dumps(summary, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_releases_by_owner",
                "description": "Retrieves releases filtered by owner email with optional filtering by release ID, version tag, and date ranges.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner_email": {"type": "string", "description": "The owner email to filter releases by."},
                        "release_id": {"type": "string", "description": "Optional specific release ID to retrieve."},
                        "version_tag": {"type": "string", "description": "Optional version tag pattern to filter by."},
                        "created_after": {"type": "string", "description": "Filter releases created after this ISO timestamp."},
                        "created_before": {"type": "string", "description": "Filter releases created before this ISO timestamp."}
                    },
                    "required": ["owner_email"]
                }
            }
        }
