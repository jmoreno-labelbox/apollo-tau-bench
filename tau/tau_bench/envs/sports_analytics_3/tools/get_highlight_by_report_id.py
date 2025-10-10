# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetHighlightByReportId(Tool):
    """Fetch all video playlists associated with a given report_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], report_id) -> str:

        # 1) Verify
        if report_id is None:
            return json.dumps({"error": "Missing required field: report_id"}, indent=2)

        # Retrieve the database from the provided input data.
        playlists: List[Dict[str, Any]] = list(data.get("video_playlists", {}).values())

        # 3) Precise match retrieval (without normalization)
        matches = [p for p in playlists if p.get("report_id") == report_id]

        if not matches:
            return json.dumps({"error": f"No video playlists found for report_id {report_id}"}, indent=2)

        # 4) Fixed sequence
        matches.sort(key=lambda p: int(p.get("playlist_id", 0)))

        return json.dumps(matches, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_highlight_by_report_id",
                "description": "Fetch all video playlists whose report_id exactly matches the provided value.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "report_id": {
                            "type": ["integer", "string"],
                            "description": "Exact report ID to filter by."
                        }
                    },
                    "required": ["report_id"]
                }
            }
        }
