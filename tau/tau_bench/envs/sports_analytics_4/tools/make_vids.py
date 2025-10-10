# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class MakeVids(Tool):
    @staticmethod
        # primary execution function
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        playlists = _load_table(data, "video_playlists")
        playlists.append({
            "report_id": kwargs.get("report_id"),
            "internal_portal_link": kwargs.get("internal_portal_link"),
            "clip_count": kwargs.get("clip_count", 0)
        })
        # return outcome
        return json.dumps({"status": "ok"}, indent=2)

    @staticmethod
        # metadata information
    def get_info() -> Dict[str, Any]:
        # return output
        return {"type": "function", "function": {"name": "makeVid", "description": "Persists a video playlist row linked to a report.", "parameters": {"type": "object", "properties": {"report_id": {"type": "string"}, "internal_portal_link": {"type": "string"}, "clip_count": {"type": "integer"}}, "required": ["internal_portal_link"]}}}
