# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require_tables


class CreateVideoPlaylist(Tool):
    """Create a video_playlists row for a report. Enforces non-negative counts; when using dev categories, enforces clip ranges."""
    @staticmethod
    def invoke(data, **kwargs)->str:
        err = _require_tables(data, ["video_playlists"])
        if err:
            return json.dumps({"error": err}, indent=2)
        need = _check_required(kwargs, ["report_id","playlist_name","clip_count"])
        if need:
            return json.dumps({"error": need}, indent=2)
        name = kwargs.get("playlist_name")
        cc = kwargs.get("clip_count")
        try:
            cc_int = int(cc)
        except Exception:
            return json.dumps({"error":"clip_count must be an integer."}, indent=2)
        if cc_int < 0:
            return json.dumps({"error":"clip_count must be a non-negative integer."}, indent=2)
        if name in ("Positive Reinforcement","Teaching Moments"):
            rng = (3,5) if name=="Positive Reinforcement" else (2,3)
            if not (rng[0] <= cc_int <= rng[1]):
                return json.dumps({"error":f"{name} requires clip_count in {rng}."}, indent=2)

        rows = data["video_playlists"]
        new_id = _next_id(rows, "playlist_id")
        link = kwargs.get("internal_portal_link", f"https://portal.internal/videos/report/{kwargs.get('report_id')}/playlist/{new_id}")
        row = {
            "playlist_id": new_id,
            "report_id": kwargs.get("report_id"),
            "playlist_name": name,
            "internal_portal_link": link,
            "clip_count": cc_int
        }
        rows.append(row)
        return json.dumps({"playlist_id": new_id}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"create_video_playlist","description":"Creates a video_playlists row for a report with validation.","parameters":{"type":"object","properties":{"report_id":{"type":"integer"},"playlist_name":{"type":"string"},"clip_count":{"type":"integer"},"internal_portal_link":{"type":"string"}},"required":["report_id","playlist_name","clip_count"]}}}
