from tau_bench.envs.tool import Tool
import json
import re
from typing import Any

class ListVideoPlaylists(Tool):
    """Retrieve playlists associated with a specific report_id."""

    @staticmethod
    def invoke(data, report_id: str = None) -> str:
        err = _require_tables(data, ["video_playlists"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload, indent=2)
            return out
        if report_id is None:
            payload = {"error": "report_id is required."}
            out = json.dumps(payload, indent=2)
            return out
        rows = [v for v in data["video_playlists"] if v.get("report_id") == report_id]
        payload = rows
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "ListVideoPlaylists",
                "description": "Lists video_playlists rows for a report.",
                "parameters": {
                    "type": "object",
                    "properties": {"report_id": {"type": "integer"}},
                    "required": ["report_id"],
                },
            },
        }
