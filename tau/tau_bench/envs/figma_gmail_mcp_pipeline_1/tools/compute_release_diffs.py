# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ComputeReleaseDiffs(Tool):  # READ
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        release_id: str,
        changelog_highlights: List[str]
    ) -> str:
        # Validate input
        if not isinstance(release_id, str) or not release_id:
            return json.dumps({"error": "release_id must be a non-empty string"})

        if not isinstance(changelog_highlights, list) or not all(isinstance(item, str) for item in changelog_highlights):
            return json.dumps({"error": "changelog_highlights must be a list of strings"})

        releases = data.get("releases", [])
        figma_artifacts = data.get("figma_artifacts", [])

        # Find the current release
        current_release = next((r for r in releases if r.get("release_id") == release_id), None)
        if not current_release:
            return json.dumps({"error": f"Release with release_id '{release_id}' not found"})

        current_figma_file_id = current_release.get("figma_file_id")
        current_created_ts = current_release.get("created_ts")

        # Find the previous release with the same figma_file_id (based on created_ts)
        same_file_releases = [
            r for r in releases
            if r.get("figma_file_id") == current_figma_file_id and r.get("release_id") != release_id
        ]

        # Sort by created_ts and find the most recent one before current release
        previous_release = None
        if same_file_releases:
            # Filter releases that are before the current release
            prior_releases = [
                r for r in same_file_releases
                if r.get("created_ts", "") < current_created_ts
            ]
            if prior_releases:
                # Sort by created_ts descending and take the first (most recent)
                prior_releases.sort(key=lambda x: x.get("created_ts", ""), reverse=True)
                previous_release = prior_releases[0]

        prior_release_id_nullable = previous_release.get("release_id") if previous_release else None
        previous_created_ts = previous_release.get("created_ts") if previous_release else None

        # Find all figma_artifacts with the same figma_file_id
        same_file_artifacts = [
            artifact for artifact in figma_artifacts
            if artifact.get("figma_file_id") == current_figma_file_id
        ]

        frames_added = []
        frames_updated = []
        frames_removed = []  # Always empty as specified
        component_version_bumps = []

        for artifact in same_file_artifacts:
            artifact_modified_ts = artifact.get("modified_ts")
            frame_id = artifact.get("frame_id_nullable")
            artifact_name = artifact.get("artifact_name", "")

            # Only process artifacts that have a frame_id
            if frame_id:
                if previous_created_ts and artifact_modified_ts:
                    if artifact_modified_ts > previous_created_ts:
                        frames_updated.append(frame_id)
                    else:
                        frames_added.append(frame_id)
                else:
                    # If no previous release, consider all as added
                    frames_added.append(frame_id)

            # Generate component version bump for each artifact
            if artifact_name:
                # Remove spaces and generate random version
                component_name = artifact_name.replace(" ", "")
                version_num = len(component_name)
                component_version_bumps.append(f"{component_name}-v1.{version_num}")

        return json.dumps({
            "release_id": release_id,
            "prior_release_id_nullable": prior_release_id_nullable,
            "frames_added": frames_added,
            "frames_updated": frames_updated,
            "frames_removed": frames_removed,
            "component_version_bumps": component_version_bumps,
            "changelog_highlights": changelog_highlights
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "compute_release_diffs",
                "description": "Compute release diffs by comparing current release with previous release of the same Figma file.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "release_id": {"type": "string", "description": "The release ID to compute diffs for."},
                        "changelog_highlights": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of changelog highlights for the release."
                        }
                    },
                    "required": ["release_id", "changelog_highlights"]
                }
            }
        }
