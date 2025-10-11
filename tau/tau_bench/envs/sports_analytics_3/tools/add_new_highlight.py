# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddNewHighlight(Tool):
    """
    Add to an existing highlight playlist'sclip_count, or create a new one if it doesn't exist.

    Inputs (exact names):
      - name (string)       [required]  # The suffix; code will add 'Game Highlights - ' at the beginning.
      -clip_count (integer) [required]

    Behavior:
      - Compute full_name = "Game Highlights - " + name (no normalization).
      - If a playlist with playlist_name == full_name exists, incrementclip_count byclip_count.
      - Else, create a new row with:
          playlist_id = max existing + 1 (or 1 if none),
          report_id = null,
          internal_portal_link = null,
        clip_count =clip_count.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], clip_count, name, report_id = None) -> str:

        # 1) Verify
        if not isinstance(name, str) or name == "":
            return json.dumps({"error": "Missing required field: name"}, indent=2)
        if clip_count is None:
            return json.dumps({"error": "Missing required field: clip_count"}, indent=2)

        full_name = f"Game Highlights - {name}"

        # Retrieve database.
        playlists: List[Dict[str, Any]] = list(data.get("video_playlists", {}).values())

        # 3) Attempt to locate existing
        target = None
        for p in playlists:
            if p.get("playlist_name") == full_name:
                target = p
                break

        # 4) Modify or generate
        if target is not None:
            # Increase clip_count
            current = int(target.get("clip_count", 0))
            target["clip_count"] = current + int(clip_count)
            return json.dumps(target, indent=2)

        # Generate new
        new_id = get_next_highlight_id(data)
        new_row = {
            "playlist_id": new_id,
            "report_id": report_id,
            "playlist_name": full_name,
            "internal_portal_link": f"https://internal.baseball.com/playlists/{new_id}",
            "clip_count": int(clip_count)
        }
        playlists.append(new_row)
        return json.dumps(new_row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_new_highlight",
                "description": "Add clip_count to an existing 'Game Highlights - <name>' playlist, or create it if missing. Optionally set report_id if creating.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Suffix to append after 'Game Highlights - '."
                        },
                        "clip_count": {
                            "type": "integer",
                            "description": "Number of clips to add (used as initial count if created)."
                        },
                        "report_id": {
                            "type": ["integer", "null"],
                            "description": "Optional report ID to associate when creating new."
                        }
                    },
                    "required": ["name", "clip_count"]
                }
            }
        }
