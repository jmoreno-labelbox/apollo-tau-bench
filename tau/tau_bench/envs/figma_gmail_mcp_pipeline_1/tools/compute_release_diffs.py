from tau_bench.envs.tool import Tool
import json
from typing import Any

class ComputeReleaseDiffs(Tool):  #READ
    @staticmethod
    def invoke(
        data: dict[str, Any], release_id: str, changelog_highlights: list[str]
    ) -> str:
        pass
        #Check the input for validity
        if not isinstance(release_id, str) or not release_id:
            payload = {"error": "release_id must be a non-empty string"}
            out = json.dumps(payload)
            return out

        if not isinstance(changelog_highlights, list) or not all(
            isinstance(item, str) for item in changelog_highlights
        ):
            payload = {"error": "changelog_highlights must be a list of strings"}
            out = json.dumps(
                payload)
            return out

        releases = data.get("releases", [])
        figma_artifacts = data.get("figma_artifacts", [])

        #Identify the active release
        current_release = next(
            (r for r in releases if r.get("release_id") == release_id), None
        )
        if not current_release:
            payload = {"error": f"Release with release_id '{release_id}' not found"}
            out = json.dumps(
                payload)
            return out

        current_figma_file_id = current_release.get("figma_file_id")
        current_created_ts = current_release.get("created_ts")

        #Locate the last release with the same figma_file_id (using created_ts)
        same_file_releases = [
            r
            for r in releases
            if r.get("figma_file_id") == current_figma_file_id
            and r.get("release_id") != release_id
        ]

        #Order by created_ts and identify the latest one prior to the current release
        previous_release = None
        if same_file_releases:
            #Select releases that occurred before the current release
            prior_releases = [
                r
                for r in same_file_releases
                if r.get("created_ts", "") < current_created_ts
            ]
            if prior_releases:
                #Order by created_ts in descending order and select the first (most recent)
                prior_releases.sort(key=lambda x: x.get("created_ts", ""), reverse=True)
                previous_release = prior_releases[0]

        prior_release_id_nullable = (
            previous_release.get("release_id") if previous_release else None
        )
        previous_created_ts = (
            previous_release.get("created_ts") if previous_release else None
        )

        #Locate all figma_artifacts sharing the same figma_file_id
        same_file_artifacts = [
            artifact
            for artifact in figma_artifacts
            if artifact.get("figma_file_id") == current_figma_file_id
        ]

        frames_added = []
        frames_updated = []
        frames_removed = []  #Consistently empty as indicated
        component_version_bumps = []

        for artifact in same_file_artifacts:
            artifact_modified_ts = artifact.get("modified_ts")
            frame_id = artifact.get("frame_id_nullable")
            artifact_name = artifact.get("artifact_name", "")

            #Process solely those artifacts that possess a frame_id
            if frame_id:
                if previous_created_ts and artifact_modified_ts:
                    if artifact_modified_ts > previous_created_ts:
                        frames_updated.append(frame_id)
                    else:
                        frames_added.append(frame_id)
                else:
                    #If there is no prior release, treat all as newly added
                    frames_added.append(frame_id)

            #Create a version increment for each artifact
            if artifact_name:
                #Eliminate spaces and produce a random version
                component_name = artifact_name.replace(" ", "")
                version_num = len(component_name)
                component_version_bumps.append(f"{component_name}-v1.{version_num}")
        payload = {
                "release_id": release_id,
                "prior_release_id_nullable": prior_release_id_nullable,
                "frames_added": frames_added,
                "frames_updated": frames_updated,
                "frames_removed": frames_removed,
                "component_version_bumps": component_version_bumps,
                "changelog_highlights": changelog_highlights,
            }
        out = json.dumps(
            payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ComputeReleaseDiffs",
                "description": "Compute release diffs by comparing current release with previous release of the same Figma file.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "release_id": {
                            "type": "string",
                            "description": "The release ID to compute diffs for.",
                        },
                        "changelog_highlights": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of changelog highlights for the release.",
                        },
                    },
                    "required": ["release_id", "changelog_highlights"],
                },
            },
        }
