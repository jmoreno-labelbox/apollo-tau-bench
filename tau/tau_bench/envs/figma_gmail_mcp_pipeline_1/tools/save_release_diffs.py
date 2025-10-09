from tau_bench.envs.tool import Tool
import json
from typing import Any

class SaveReleaseDiffs(Tool):  #WRITE
    @staticmethod
    def invoke(
        data: dict[str, Any],
        release_id: str,
        prior_release_id_nullable: str,
        frames_added: list[str],
        frames_updated: list[str],
        frames_removed: list[str],
        component_version_bumps: list[str],
        changelog_highlights: list[str],
    ) -> str:
        pass
        #Check the input for validity
        if not isinstance(release_id, str) or not release_id:
            payload = {"error": "release_id must be a non-empty string"}
            out = json.dumps(payload)
            return out

        #Check the parameters of the list for validity
        if not isinstance(frames_added, list) or not all(
            isinstance(item, str) for item in frames_added
        ):
            payload = {"error": "frames_added must be a list of strings"}
            out = json.dumps(payload)
            return out

        if not isinstance(frames_updated, list) or not all(
            isinstance(item, str) for item in frames_updated
        ):
            payload = {"error": "frames_updated must be a list of strings"}
            out = json.dumps(payload)
            return out

        if not isinstance(frames_removed, list) or not all(
            isinstance(item, str) for item in frames_removed
        ):
            payload = {"error": "frames_removed must be a list of strings"}
            out = json.dumps(payload)
            return out

        if not isinstance(component_version_bumps, list) or not all(
            isinstance(item, str) for item in component_version_bumps
        ):
            payload = {"error": "component_version_bumps must be a list of strings"}
            out = json.dumps(
                payload)
            return out

        if not isinstance(changelog_highlights, list) or not all(
            isinstance(item, str) for item in changelog_highlights
        ):
            payload = {"error": "changelog_highlights must be a list of strings"}
            out = json.dumps(
                payload)
            return out

        if prior_release_id_nullable is not None and (
            not isinstance(prior_release_id_nullable, str)
            or not prior_release_id_nullable
        ):
            payload = {
                    "error": "prior_release_id_nullable must be a non-empty string or None"
                }
            out = json.dumps(
                payload)
            return out

        release_diffs = data["release_diffs"]

        #Verify if a diff is already present for this release_id
        existing_diff = next(
            (diff for diff in release_diffs.values() if diff.get("release_id") == release_id),
            None,
        )
        if existing_diff:
            #Modify the existing diff rather than returning an error (for testing purposes)
            existing_diff.update(
                {
                    "prior_release_id_nullable": prior_release_id_nullable,
                    "frames_added": frames_added,
                    "frames_updated": frames_updated,
                    "frames_removed": frames_removed,
                    "component_version_bumps": component_version_bumps,
                    "changelog_highlights": changelog_highlights,
                }
            )
            payload = {"updated_release_diff": existing_diff}
            out = json.dumps(payload)
            return out

        #Create a new diff_id
        next_num = len(release_diffs) + 1
        diff_id = f"diff_{next_num:03d}"

        new_release_diff = {
            "diff_id": diff_id,
            "release_id": release_id,
            "prior_release_id_nullable": prior_release_id_nullable,
            "frames_added": frames_added,
            "frames_updated": frames_updated,
            "frames_removed": frames_removed,
            "component_version_bumps": component_version_bumps,
            "changelog_highlights": changelog_highlights,
        }

        release_diffs.append(new_release_diff)
        payload = {"new_release_diff": new_release_diff}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SaveReleaseDiffs",
                "description": "Save computed release diffs to the database by creating a new release_diff entry.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "release_id": {
                            "type": "string",
                            "description": "The release ID for the diff entry.",
                        },
                        "prior_release_id_nullable": {
                            "type": "string",
                            "description": "The previous release ID, or null if none exists.",
                        },
                        "frames_added": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of frame IDs that were added.",
                        },
                        "frames_updated": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of frame IDs that were updated.",
                        },
                        "frames_removed": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of frame IDs that were removed.",
                        },
                        "component_version_bumps": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of component version bumps.",
                        },
                        "changelog_highlights": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of changelog highlights for the release.",
                        },
                    },
                    "required": [
                        "release_id",
                        "prior_release_id_nullable",
                        "frames_added",
                        "frames_updated",
                        "frames_removed",
                        "component_version_bumps",
                        "changelog_highlights",
                    ],
                },
            },
        }
