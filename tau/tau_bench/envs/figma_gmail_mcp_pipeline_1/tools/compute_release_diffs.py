# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ComputeReleaseDiffs(Tool):  # READ DATA
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        release_id: str,
        changelog_highlights: List[str]
    ) -> str:
        # Verify the input.
        if not isinstance(release_id, str) or not release_id:
            return json.dumps({"error": "release_id must be a non-empty string"})

        if not isinstance(changelog_highlights, list) or not all(isinstance(item, str) for item in changelog_highlights):
            return json.dumps({"error": "changelog_highlights must be a list of strings"})

        releases = list(data.get("releases", {}).values())
        figma_artifacts = list(data.get("figma_artifacts", {}).values())

        # Locate the latest version.
        current_release = next((r for r in releases if r.get("release_id") == release_id), None)
        if not current_release:
            return json.dumps({"error": f"Release with release_id '{release_id}' not found"})

        current_figma_file_id = current_release.get("figma_file_id")
        current_created_ts = current_release.get("created_ts")

        # Retrieve the prior release that shares the same figma_file_id, using created_ts for reference.
        same_file_releases = [
            r for r in releases
            if r.get("figma_file_id") == current_figma_file_id and r.get("release_id") != release_id
        ]

        # Order by created_ts and identify the latest entry prior to the current release.
        previous_release = None
        if same_file_releases:
            # Select releases that precede the current release.
            prior_releases = [
                r for r in same_file_releases
                if r.get("created_ts", "") < current_created_ts
            ]
            if prior_releases:
                # Order by created_ts in descending order and select the first entry (latest).
                prior_releases.sort(key=lambda x: x.get("created_ts", ""), reverse=True)
                previous_release = prior_releases[0]

        prior_release_id_nullable = previous_release.get("release_id") if previous_release else None
        previous_created_ts = previous_release.get("created_ts") if previous_release else None

        # Retrieve all figma_artifacts sharing the same figma_file_id.
        same_file_artifacts = [
            artifact for artifact in figma_artifacts
            if artifact.get("figma_file_id") == current_figma_file_id
        ]

        frames_added = []
        frames_updated = []
        frames_removed = []  # Consistently cleared as required
        component_version_bumps = []

        for artifact in same_file_artifacts:
            artifact_modified_ts = artifact.get("modified_ts")
            frame_id = artifact.get("frame_id_nullable")
            artifact_name = artifact.get("artifact_name", "")

            # Process artifacts solely with a frame_id.
            if frame_id:
                if previous_created_ts and artifact_modified_ts:
                    if artifact_modified_ts > previous_created_ts:
                        frames_updated.append(frame_id)
                    else:
                        frames_added.append(frame_id)
                else:
                    # Treat everything as newly added if there are no prior releases.
                    frames_added.append(frame_id)

            # Create a version increment for each artifact component.
            if artifact_name:
                # Eliminate spaces and create a random variant.
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
