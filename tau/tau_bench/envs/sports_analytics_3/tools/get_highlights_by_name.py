# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetHighlightsByName(Tool):
    """
    Fetch a highlight playlist by name.
    Inputs:
      - name (string) [required]  # The suffix; code will add 'Game Highlights - ' at the beginning.
    Behavior:
      - Compute full_name = "Game Highlights - " + name and return the matching playlist.
      - If multiple match (unlikely), return the one with the smallest playlist_id for determinism.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        name = kwargs.get("name")

        # 1) Verify
        if not isinstance(name, str) or name == "":
            return json.dumps({"error": "Missing required field: name"}, indent=2)

        full_name = f"Game Highlights - {name}"

        # Retrieve database.
        playlists: List[Dict[str, Any]] = list(data.get("video_playlists", {}).values())

        # 3) Precise match query (without normalization)
        matches = [p for p in playlists if p.get("playlist_name") == full_name]

        if not matches:
            return json.dumps({"error": f"No playlist found with name '{full_name}'"}, indent=2)

        matches.sort(key=lambda p: int(p.get("playlist_id", 0)))
        return json.dumps(matches[0], indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_highlights_by_name",
                "description": "Return the 'Game Highlights - <name>' playlist (exact match).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Suffix after 'Game Highlights - ' to look up."
                        }
                    },
                    "required": ["name"]
                }
            }
        }
