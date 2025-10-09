from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetHighlightByReportId(Tool):
    """Retrieve all video playlists linked to a specific report_id."""

    @staticmethod
    def invoke(data: dict[str, Any], report_id: str = None) -> str:
        #1) Confirm validity
        if report_id is None:
            payload = {"error": "Missing required field: report_id"}
            out = json.dumps(payload, indent=2)
            return out

        #2) Retrieve DB using provided data
        playlists: list[dict[str, Any]] = data.get("video_playlists", [])

        #3) Lookup for exact matches (without normalization)
        matches = [p for p in playlists if p.get("report_id") == report_id]

        if not matches:
            payload = {"error": f"No video playlists found for report_id {report_id}"}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        #4) Order deterministically
        matches.sort(key=lambda p: int(p.get("playlist_id", 0)))
        payload = matches
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getHighlightByReportId",
                "description": "Fetch all video playlists whose report_id exactly matches the provided value.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "report_id": {
                            "type": ["integer", "string"],
                            "description": "Exact report ID to filter by.",
                        }
                    },
                    "required": ["report_id"],
                },
            },
        }
