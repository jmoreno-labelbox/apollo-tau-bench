# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require_tables


class ListVideoPlaylists(Tool):
    """List playlists for a given report_id."""
    @staticmethod
    def invoke(data, **kwargs)->str:
        err = _require_tables(data, ["video_playlists"])
        if err:
            return json.dumps({"error": err}, indent=2)
        rid = kwargs.get("report_id")
        if rid is None:
            return json.dumps({"error":"report_id is required."}, indent=2)
        rows = [v for v in data["video_playlists"] if v.get("report_id")==rid]
        return json.dumps(rows, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"list_video_playlists","description":"Lists video_playlists rows for a report.","parameters":{"type":"object","properties":{"report_id":{"type":"integer"}},"required":["report_id"]}}}
