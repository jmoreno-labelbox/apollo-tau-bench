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

class GetReleasesByOwner(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        owner_email: str = None,
        release_id: str = None,
        version_tag: str = None,
        created_after: str = None,
        created_before: str = None
    ) -> str:
        """
        Obtains releases filtered by owner and additional criteria.
        """
        if not owner_email:
            payload = {"error": "owner_email is required."}
            out = json.dumps(payload)
            return out

        releases = data.get("releases", {}).values()

        # Sort releases based on specified criteria
        results = []
        for release in releases.values():
            # Main filter - owner email
            if release.get("owner_email") != owner_email:
                continue

            # Implement optional filters
            if release_id:
                if release.get("release_id") != release_id:
                    continue

            if version_tag:
                if version_tag not in release.get("version_tag", ""):
                    continue

            # Enforce date filters
            if created_after:
                release_created = release.get("created_ts", "")
                if release_created < created_after:
                    continue

            if created_before:
                release_created = release.get("created_ts", "")
                if release_created > created_before:
                    continue

            results.append(release)

        # Generate a summary
        summary = {
            "owner_email": owner_email,
            "total_releases": len(results),
            "version_tags": list({r.get("version_tag", "") for r in results}),
            "releases": results,
        }
        payload = summary
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetReleasesByOwner",
                "description": "Retrieves releases filtered by owner email with optional filtering by release ID, version tag, and date ranges.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner_email": {
                            "type": "string",
                            "description": "The owner email to filter releases by.",
                        },
                        "release_id": {
                            "type": "string",
                            "description": "Optional specific release ID to retrieve.",
                        },
                        "version_tag": {
                            "type": "string",
                            "description": "Optional version tag pattern to filter by.",
                        },
                        "created_after": {
                            "type": "string",
                            "description": "Filter releases created after this ISO timestamp.",
                        },
                        "created_before": {
                            "type": "string",
                            "description": "Filter releases created before this ISO timestamp.",
                        },
                    },
                    "required": ["owner_email"],
                },
            },
        }
