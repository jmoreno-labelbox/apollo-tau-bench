# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DetectReleaseVersion(Tool):  # READ.
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        release_id: str
    ) -> str:
        # Verify input correctness.
        if not isinstance(release_id, str) or not release_id:
            return json.dumps({"error": "release_id must be a non-empty string"})

        releases = data.get("releases", [])

        # Locate the deployment
        release = next((r for r in releases if r.get("release_id") == release_id), None)
        if not release:
            return json.dumps({"error": f"Release with release_id '{release_id}' not found"})

        # Verify if version_tag begins with "release/"
        version_tag = release.get("version_tag", "")
        is_release_version = version_tag.startswith("release/")

        return json.dumps({
            "is_release_version": is_release_version,
            "release_info": release
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "detect_release_version",
                "description": "Detect if a release is a release version by checking if the version tag begins with 'release/' and return all release info.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "release_id": {"type": "string", "description": "The release ID to check."}
                    },
                    "required": ["release_id"]
                }
            }
        }
