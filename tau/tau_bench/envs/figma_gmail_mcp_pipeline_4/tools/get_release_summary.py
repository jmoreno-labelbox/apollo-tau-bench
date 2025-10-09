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

class GetReleaseSummary(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        release_id: str = None,
        figma_file_id: str = None,
        owner_email: str = None,
        version_tag_pattern: str = None,
        status: str = None
    ) -> str:
        """
        Obtains detailed release information and metrics.
        """
        releases = data.get("releases", [])
        gmail_threads = data.get("gmail_threads", [])

        # Return the specific release if release_id is supplied
        if release_id:
            release_info = None
            for release in releases:
                if release.get("release_id") == release_id:
                    release_info = release
                    break

            if not release_info:
                payload = {"error": f"Release with ID '{release_id}' not found."}
                out = json.dumps(payload)
                return out

            # Enhance with details from the thread
            thread_id = release_info.get("thread_id_nullable")
            thread_info = None
            if thread_id:
                for thread in gmail_threads:
                    if thread.get("thread_id") == thread_id:
                        thread_info = thread
                        break

            summary = {"release_info": release_info, "thread_info": thread_info}
            payload = summary
            out = json.dumps(payload, indent=2)
            return out

        # Provide a summary for all releases
        all_releases = releases

        # Enforce filters
        if figma_file_id:
            all_releases = [
                r for r in all_releases if r.get("figma_file_id") == figma_file_id
            ]

        if owner_email:
            all_releases = [
                r for r in all_releases if r.get("owner_email") == owner_email
            ]

        if version_tag_pattern:
            all_releases = [
                r
                for r in all_releases
                if version_tag_pattern in r.get("version_tag", "")
            ]

        if status:
            all_releases = [r for r in all_releases if r.get("status") == status]

        summary = {
            "total_releases": len(all_releases),
            "by_owner": {},
            "by_file": {},
            "by_status": {},
            "releases": all_releases,
        }

        # Categorize releases based on owner
        for release in all_releases:
            owner = release.get("owner_email")
            if owner not in summary["by_owner"]:
                summary["by_owner"][owner] = 0
            summary["by_owner"][owner] += 1

            # Classify by file
            file_id = release.get("figma_file_id")
            if file_id not in summary["by_file"]:
                summary["by_file"][file_id] = 0
            summary["by_file"][file_id] += 1

            # Categorize by status
            release_status = release.get("status", "DRAFT")
            if release_status not in summary["by_status"]:
                summary["by_status"][release_status] = 0
            summary["by_status"][release_status] += 1
        payload = summary
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetReleaseSummary",
                "description": "Retrieves comprehensive release information and metrics including owner distribution, file associations, and status breakdowns.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "release_id": {
                            "type": "string",
                            "description": "The ID of a specific release to retrieve details for.",
                        },
                        "figma_file_id": {
                            "type": "string",
                            "description": "Filter releases by Figma file ID.",
                        },
                        "owner_email": {
                            "type": "string",
                            "description": "Filter releases by owner email address.",
                        },
                        "version_tag_pattern": {
                            "type": "string",
                            "description": "Filter releases by version tag pattern (e.g., 'design-system').",
                        },
                        "status": {
                            "type": "string",
                            "description": "Filter releases by status (e.g., 'PUBLISHED', 'DRAFT').",
                        },
                    },
                },
            },
        }
