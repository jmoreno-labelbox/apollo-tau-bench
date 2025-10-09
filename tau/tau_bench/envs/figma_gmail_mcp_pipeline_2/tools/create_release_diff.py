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

class CreateReleaseDiff(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        changelog_highlights: list = None,
        component_version_bumps: list = None,
        frames_added: list = None,
        frames_removed: list = None,
        frames_updated: list = None,
        prior_release_id: str = None,
        release_id: str = None
    ) -> str:
        frames_added = frames_added or []
        frames_updated = frames_updated or []
        frames_removed = frames_removed or []
        component_version_bumps = component_version_bumps or []
        changelog_highlights = changelog_highlights or []

        required = ["release_id"]
        params_dict = {k: v for k, v in locals().items() if k != "data"}

        missing = [f for f in required if params_dict.get(f) is None]
        if missing:
            payload = {"error": f"Missing required fields: {', '.join(missing)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        release_diffs: list[dict[str, Any]] = data.get("release_diffs", [])
        diff_id = get_next_diff_id(data)
        created_ts = get_now_timestamp()

        new_diff = {
            "diff_id": diff_id,
            "release_id": release_id,
            "prior_release_id_nullable": prior_release_id,
            "created_ts": created_ts,
            "frames_added": frames_added,
            "frames_updated": frames_updated,
            "frames_removed": frames_removed,
            "component_version_bumps": component_version_bumps,
            "changelog_highlights": changelog_highlights,
        }

        release_diffs.append(new_diff)
        data["release_diffs"] = release_diffs
        payload = new_diff
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateReleaseDiff",
                "description": "Create a new release_diff row for a release.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "release_id": {"type": "string"},
                        "prior_release_id": {"type": ["string", "null"]},
                        "frames_added": {"type": "array", "items": {"type": "string"}},
                        "frames_updated": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "frames_removed": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "component_version_bumps": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "changelog_highlights": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                    "required": ["release_id"],
                },
            },
        }
