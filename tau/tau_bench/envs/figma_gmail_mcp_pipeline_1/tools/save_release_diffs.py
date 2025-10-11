# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SaveReleaseDiffs(Tool):  # CREATE
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        release_id: str,
        prior_release_id_nullable: str,
        frames_added: List[str],
        frames_updated: List[str],
        frames_removed: List[str],
        component_version_bumps: List[str],
        changelog_highlights: List[str]
    ) -> str:
        # Verify user input
        if not isinstance(release_id, str) or not release_id:
            return json.dumps({"error": "release_id must be a non-empty string"})

        # Verify list arguments.
        if not isinstance(frames_added, list) or not all(isinstance(item, str) for item in frames_added):
            return json.dumps({"error": "frames_added must be a list of strings"})

        if not isinstance(frames_updated, list) or not all(isinstance(item, str) for item in frames_updated):
            return json.dumps({"error": "frames_updated must be a list of strings"})

        if not isinstance(frames_removed, list) or not all(isinstance(item, str) for item in frames_removed):
            return json.dumps({"error": "frames_removed must be a list of strings"})

        if not isinstance(component_version_bumps, list) or not all(isinstance(item, str) for item in component_version_bumps):
            return json.dumps({"error": "component_version_bumps must be a list of strings"})

        if not isinstance(changelog_highlights, list) or not all(isinstance(item, str) for item in changelog_highlights):
            return json.dumps({"error": "changelog_highlights must be a list of strings"})

        if prior_release_id_nullable is not None and (not isinstance(prior_release_id_nullable, str) or not prior_release_id_nullable):
            return json.dumps({"error": "prior_release_id_nullable must be a non-empty string or None"})

        release_diffs = data["release_diffs"]

        # Verify if a difference is already present for this release_id.
        existing_diff = next((diff for diff in release_diffs if diff.get("release_id") == release_id), None)
        if existing_diff:
            # Modify the current diff instead of generating an error (for testing purposes).
            existing_diff.update({
                "prior_release_id_nullable": prior_release_id_nullable,
                "frames_added": frames_added,
                "frames_updated": frames_updated,
                "frames_removed": frames_removed,
                "component_version_bumps": component_version_bumps,
                "changelog_highlights": changelog_highlights
            })
            return json.dumps({"updated_release_diff": existing_diff})

        # Create a new diff_id
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
            "changelog_highlights": changelog_highlights
        }

        release_diffs.append(new_release_diff)

        return json.dumps({"new_release_diff": new_release_diff})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "save_release_diffs",
                "description": "Save computed release diffs to the database by creating a new release_diff entry.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "release_id": {"type": "string", "description": "The release ID for the diff entry."},
                        "prior_release_id_nullable": {"type": "string", "description": "The previous release ID, or null if none exists."},
                        "frames_added": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of frame IDs that were added."
                        },
                        "frames_updated": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of frame IDs that were updated."
                        },
                        "frames_removed": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of frame IDs that were removed."
                        },
                        "component_version_bumps": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of component version bumps."
                        },
                        "changelog_highlights": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of changelog highlights for the release."
                        }
                    },
                    "required": ["release_id", "prior_release_id_nullable", "frames_added", "frames_updated", "frames_removed", "component_version_bumps", "changelog_highlights"]
                }
            }
        }
