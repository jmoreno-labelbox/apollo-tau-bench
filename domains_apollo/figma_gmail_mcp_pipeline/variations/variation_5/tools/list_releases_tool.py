from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any

class ListReleasesTool(Tool):
    """Enumerate releases filtered by version_tag prefix or artifact_id reference."""

    @staticmethod
    def invoke(data: dict[str, Any], version_prefix: str = "release/", artifact_id: str = None) -> str:
        releases = data.get("releases", [])
        out = []
        for r in releases:
            if version_prefix and not str(r.get("version_tag", "")).startswith(version_prefix):
                continue
            if artifact_id and r.get("artifact_id") != artifact_id:
                continue
            out.append(
                _small_fields(
                    r,
                    [
                        "release_id",
                        "version_tag",
                        "artifact_id",
                        "created_ts",
                        "thread_id_nullable",
                    ],
                )
            )
        out.sort(key=lambda r: r.get("version_tag", ""))
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListReleases",
                "description": "List releases with optional version prefix and artifact filter.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "version_prefix": {
                            "type": "string",
                            "description": "Default 'release/'.",
                        },
                        "artifact_id": {"type": "string"},
                    },
                },
            },
        }
