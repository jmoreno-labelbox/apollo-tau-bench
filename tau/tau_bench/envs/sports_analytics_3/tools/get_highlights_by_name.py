from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetHighlightsByName(Tool):
    """
    Retrieve a highlight playlist using its name.
    Inputs:
      - name (string) [required]  # The suffix; code will prepend 'Game Highlights - '
    Behavior:
      - Compute full_name = "Game Highlights - " + name and return the corresponding playlist.
      - If multiple matches occur (unlikely), return the one with the smallest playlist_id for determinism.
    """

    @staticmethod
    def invoke(data: dict[str, Any], name: str = None) -> str:
        #1) Confirm validity
        if not isinstance(name, str) or name == "":
            payload = {"error": "Missing required field: name"}
            out = json.dumps(payload, indent=2)
            return out

        full_name = f"Game Highlights - {name}"

        #2) Retrieve DB
        playlists: list[dict[str, Any]] = data.get("video_playlists", [])

        #3) Search for exact matches (without normalization)
        matches = [p for p in playlists if p.get("playlist_name") == full_name]

        if not matches:
            payload = {"error": f"No playlist found with name '{full_name}'"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        matches.sort(key=lambda p: int(p.get("playlist_id", 0)))
        payload = matches[0]
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getHighlightsByName",
                "description": "Return the 'Game Highlights - <name>' playlist (exact match).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Suffix after 'Game Highlights - ' to look up.",
                        }
                    },
                    "required": ["name"],
                },
            },
        }
