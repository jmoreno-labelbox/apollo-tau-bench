# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateNewRelease(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], figma_file_id, owner_email, release_name, thread_id, version_id, version_tag) -> str:
        required = ["figma_file_id", "version_id", "version_tag", "release_name", "owner_email"]
        missing = [f for f in required if f not in kwargs or kwargs[f] is None]
        if missing:
            return json.dumps({"error": f"Missing required fields: {', '.join(missing)}"}, indent=2)

        releases: List[Dict[str, Any]] = list(data.get("releases", {}).values())
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
            "thread_id_nullable": thread_id
        }

        releases.append(new_release)
        data["releases"] = releases
        return json.dumps(new_release, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_new_release",
                "description": "Create a new release row in releases.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "figma_file_id": {"type": "string"},
                        "version_id": {"type": "string"},
                        "version_tag": {"type": "string"},
                        "release_name": {"type": "string"},
                        "owner_email": {"type": "string"},
                        "thread_id": {"type": ["string", "null"]}
                    },
                    "required": ["figma_file_id", "version_id", "version_tag", "release_name", "owner_email"]
                }
            }
        }
