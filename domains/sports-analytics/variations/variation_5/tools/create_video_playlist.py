from tau_bench.envs.tool import Tool
import json
import re
from typing import Any

class CreateVideoPlaylist(Tool):
    """Generate a video_playlists entry for a report. Requires non-negative counts; when utilizing dev categories, enforces clip ranges."""

    @staticmethod
    def invoke(data, report_id: str = None, playlist_name: str = None, clip_count: int = None, internal_portal_link: str = None) -> str:
        err = _require_tables(data, ["video_playlists"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload, indent=2)
            return out
        need = _check_required({"report_id": report_id, "playlist_name": playlist_name, "clip_count": clip_count}, ["report_id", "playlist_name", "clip_count"])
        if need:
            payload = {"error": need}
            out = json.dumps(payload, indent=2)
            return out
        name = playlist_name
        cc = clip_count
        try:
            cc_int = int(cc)
        except Exception:
            payload = {"error": "clip_count must be an integer."}
            out = json.dumps(payload, indent=2)
            return out
        if cc_int < 0:
            payload = {"error": "clip_count must be a non-negative integer."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        if name in ("Positive Reinforcement", "Teaching Moments"):
            rng = (3, 5) if name == "Positive Reinforcement" else (2, 3)
            if not (rng[0] <= cc_int <= rng[1]):
                payload = {"error": f"{name} requires clip_count in {rng}."}
                out = json.dumps(
                    payload, indent=2
                )
                return out

        rows = data["video_playlists"]
        new_id = _next_id(rows, "playlist_id")
        link = internal_portal_link or f"https://portal.internal/videos/report/{report_id}/playlist/{new_id}"
        row = {
            "playlist_id": new_id,
            "report_id": report_id,
            "playlist_name": name,
            "internal_portal_link": link,
            "clip_count": cc_int,
        }
        rows.append(row)
        payload = {"playlist_id": new_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "CreateVideoPlaylist",
                "description": "Creates a video_playlists row for a report with validation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "report_id": {"type": "integer"},
                        "playlist_name": {"type": "string"},
                        "clip_count": {"type": "integer"},
                        "internal_portal_link": {"type": "string"},
                    },
                    "required": ["report_id", "playlist_name", "clip_count"],
                },
            },
        }
