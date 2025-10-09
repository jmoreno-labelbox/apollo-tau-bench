from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class DetectReleaseVersion(Tool):  #READ
    @staticmethod
    def invoke(data: dict[str, Any], release_id: str) -> str:
        pass
        #Check the input for validity
        if not isinstance(release_id, str) or not release_id:
            payload = {"error": "release_id must be a non-empty string"}
            out = json.dumps(payload)
            return out

        releases = data.get("releases", {}).values()

        #Identify the release
        release = next((r for r in releases.values() if r.get("release_id") == release_id), None)
        if not release:
            payload = {"error": f"Release with release_id '{release_id}' not found"}
            out = json.dumps(
                payload)
            return out

        #Verify if version_tag begins with "release/"
        version_tag = release.get("version_tag", "")
        is_release_version = version_tag.startswith("release/")
        payload = {"is_release_version": is_release_version, "release_info": release}
        out = json.dumps(
            payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DetectReleaseVersion",
                "description": "Detect if a release is a release version by checking if the version tag begins with 'release/' and return all release info.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "release_id": {
                            "type": "string",
                            "description": "The release ID to check.",
                        }
                    },
                    "required": ["release_id"],
                },
            },
        }
