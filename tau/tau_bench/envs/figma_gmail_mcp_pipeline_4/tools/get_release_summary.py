# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetReleaseSummary(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Retrieves comprehensive release information and metrics.
        """
        release_id = kwargs.get('release_id')
        figma_file_id = kwargs.get('figma_file_id')
        owner_email = kwargs.get('owner_email')
        version_tag_pattern = kwargs.get('version_tag_pattern')
        status = kwargs.get('status')

        releases = data.get('releases', [])
        gmail_threads = list(data.get('gmail_threads', {}).values())

        # If release_id is provided, return specific release
        if release_id:
            release_info = None
            for release in releases:
                if release.get('release_id') == release_id:
                    release_info = release
                    break

            if not release_info:
                return json.dumps({"error": f"Release with ID '{release_id}' not found."})

            # Enrich with thread information
            thread_id = release_info.get('thread_id_nullable')
            thread_info = None
            if thread_id:
                for thread in gmail_threads:
                    if thread.get('thread_id') == thread_id:
                        thread_info = thread
                        break

            summary = {
                "release_info": release_info,
                "thread_info": thread_info
            }

            return json.dumps(summary, indent=2)

        # Return summary across all releases
        all_releases = releases

        # Apply filters
        if figma_file_id:
            all_releases = [r for r in all_releases if r.get('figma_file_id') == figma_file_id]

        if owner_email:
            all_releases = [r for r in all_releases if r.get('owner_email') == owner_email]

        if version_tag_pattern:
            all_releases = [r for r in all_releases if version_tag_pattern in r.get('version_tag', '')]

        if status:
            all_releases = [r for r in all_releases if r.get('status') == status]

        summary = {
            "total_releases": len(all_releases),
            "by_owner": {},
            "by_file": {},
            "by_status": {},
            "releases": all_releases
        }

        # Group releases by owner
        for release in all_releases:
            owner = release.get('owner_email')
            if owner not in summary["by_owner"]:
                summary["by_owner"][owner] = 0
            summary["by_owner"][owner] += 1

            # Group by file
            file_id = release.get('figma_file_id')
            if file_id not in summary["by_file"]:
                summary["by_file"][file_id] = 0
            summary["by_file"][file_id] += 1

            # Group by status
            release_status = release.get('status', 'DRAFT')
            if release_status not in summary["by_status"]:
                summary["by_status"][release_status] = 0
            summary["by_status"][release_status] += 1

        return json.dumps(summary, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_release_summary",
                "description": "Retrieves comprehensive release information and metrics including owner distribution, file associations, and status breakdowns.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "release_id": {"type": "string", "description": "The ID of a specific release to retrieve details for."},
                        "figma_file_id": {"type": "string", "description": "Filter releases by Figma file ID."},
                        "owner_email": {"type": "string", "description": "Filter releases by owner email address."},
                        "version_tag_pattern": {"type": "string", "description": "Filter releases by version tag pattern (e.g., 'design-system')."},
                        "status": {"type": "string", "description": "Filter releases by status (e.g., 'PUBLISHED', 'DRAFT')."}
                    }
                }
            }
        }
