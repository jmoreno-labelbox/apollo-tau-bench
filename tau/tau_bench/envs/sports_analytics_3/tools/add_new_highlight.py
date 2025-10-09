from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class AddNewHighlight(Tool):
    """
    Increase an existing highlight playlist's clip_count, or establish a new one if it doesn't exist.

    Inputs (exact names):
      - name (string)       [required]  # The suffix; code will prepend 'Game Highlights - '
      - clip_count (integer) [required]

    Behavior:
      - Compute full_name = "Game Highlights - " + name (no normalization).
      - If a playlist with playlist_name == full_name exists, increase clip_count by clip_count.
      - Otherwise, create a new row with:
          playlist_id = max existing + 1 (or 1 if none),
          report_id = null,
          internal_portal_link = null,
        clip_count = clip_count.
    """

    @staticmethod
    def invoke(data: dict[str, Any], name: str = None, clip_count: int = None, report_id: int = None) -> str:
        #1) Confirm validity
        if not isinstance(name, str) or name == "":
            payload = {"error": "Missing required field: name"}
            out = json.dumps(payload, indent=2)
            return out
        if clip_count is None:
            payload = {"error": "Missing required field: clip_count"}
            out = json.dumps(payload, indent=2)
            return out

        full_name = f"Game Highlights - {name}"

        #2) Retrieve DB
        playlists: list[dict[str, Any]] = data.get("video_playlists", {}).values()

        #3) Attempt to locate existing
        target = None
        for p in playlists:
            if p.get("playlist_name") == full_name:
                target = p
                break

        #4) Modify or establish
        if target is not None:
            #Increase clip_count
            current = int(target.get("clip_count", 0))
            target["clip_count"] = current + int(clip_count)
            payload = target
            out = json.dumps(payload, indent=2)
            return out

        #Establish new
        new_id = get_next_highlight_id(data)
        new_row = {
            "playlist_id": new_id,
            "report_id": report_id,
            "playlist_name": full_name,
            "internal_portal_link": f"https://internal.baseball.com/playlists/{new_id}",
            "clip_count": int(clip_count),
        }
        playlists.append(new_row)
        payload = new_row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddNewHighlight",
                "description": "Add clip_count to an existing 'Game Highlights - <name>' playlist, or create it if missing. Optionally set report_id if creating.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Suffix to append after 'Game Highlights - '.",
                        },
                        "clip_count": {
                            "type": "integer",
                            "description": "Number of clips to add (used as initial count if created).",
                        },
                        "report_id": {
                            "type": ["integer", "null"],
                            "description": "Optional report ID to associate when creating new.",
                        },
                    },
                    "required": ["name", "clip_count"],
                },
            },
        }
