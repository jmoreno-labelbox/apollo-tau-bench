from tau_bench.envs.tool import Tool
import html
import json
import re
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CreateNewRelease(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        owner_email: str,
        release_name: str,
        version_id: str,
        version_tag: str,
        figma_file_id: str = None,
        thread_id: str = None
    ) -> str:
        required = [
            "figma_file_id",
            "version_id",
            "version_tag",
            "release_name",
            "owner_email",
        ]
        params_dict = {k: v for k, v in locals().items() if k != "data"}

        missing = [f for f in required if params_dict.get(f) is None]
        if missing:
            payload = {"error": f"Missing required fields: {', '.join(missing)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        releases: list[dict[str, Any]] = data.get("releases", [])
        release_id = get_next_release_id(data)
        created_ts = get_now_timestamp()

        new_release = {
            "release_id": release_id,
            "figma_file_id": figma_file_id,
            "version_id": version_id,
            "version_tag": version_tag,
            "release_name": release_name,
            "owner_email": owner_email,
            "created_ts": created_ts,
            "thread_id_nullable": thread_id,
        }

        releases.append(new_release)
        data["releases"] = releases
        payload = new_release
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateNewRelease",
                "description": "Create a new release row in releases.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "figma_file_id": {"type": "string"},
                        "version_id": {"type": "string"},
                        "version_tag": {"type": "string"},
                        "release_name": {"type": "string"},
                        "owner_email": {"type": "string"},
                        "thread_id": {"type": ["string", "null"]},
                    },
                    "required": [
                        "figma_file_id",
                        "version_id",
                        "version_tag",
                        "release_name",
                        "owner_email",
                    ],
                },
            },
        }
