# Copyright by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateReleaseDiff(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        required = ["release_id"]
        missing = [f for f in required if f not in kwargs or kwargs[f] is None]
        if missing:
            return json.dumps({"error": f"Missing required fields: {', '.join(missing)}"}, indent=2)

        release_diffs: List[Dict[str, Any]] = list(data.get("release_diffs", {}).values())
        diff_id = get_next_diff_id(data)
        created_ts = get_now_timestamp()

        frames_added = kwargs.get("frames_added") or []
        frames_updated = kwargs.get("frames_updated") or []
        frames_removed = kwargs.get("frames_removed") or []
        component_version_bumps = kwargs.get("component_version_bumps") or []
        changelog_highlights = kwargs.get("changelog_highlights") or []
        prior_release_id = kwargs.get("prior_release_id")

        new_diff = {
            "diff_id": diff_id,
            "release_id": kwargs["release_id"],
            "prior_release_id_nullable": prior_release_id,
            "created_ts": created_ts,
            "frames_added": frames_added,
            "frames_updated": frames_updated,
            "frames_removed": frames_removed,
            "component_version_bumps": component_version_bumps,
            "changelog_highlights": changelog_highlights
        }

        release_diffs.append(new_diff)
        data["release_diffs"] = release_diffs
        return json.dumps(new_diff, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_release_diff",
                "description": "Create a new release_diff row for a release.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "release_id": {"type": "string"},
                        "prior_release_id": {"type": ["string", "null"]},
                        "frames_added": {"type": "array", "items": {"type": "string"}},
                        "frames_updated": {"type": "array", "items": {"type": "string"}},
                        "frames_removed": {"type": "array", "items": {"type": "string"}},
                        "component_version_bumps": {"type": "array", "items": {"type": "string"}},
                        "changelog_highlights": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["release_id"]
                }
            }
        }
