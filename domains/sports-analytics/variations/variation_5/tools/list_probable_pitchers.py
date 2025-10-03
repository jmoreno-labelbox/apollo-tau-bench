from tau_bench.envs.tool import Tool
import json
import re
from typing import Any

class ListProbablePitchers(Tool):
    """Provides probable pitchers for a team: consistent sample from players table (position 'P' if available), sorted by full_name in ascending order."""

    @staticmethod
    def invoke(data, team_id, limit=2, use_eb_shrinkage: Any = None, order_by: str = None) -> str:
        pass
        err = _require_tables(data, ["players"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload, indent=2)
            return out
        need = _check_required({"team_id": team_id}, ["team_id"])
        if need:
            payload = {"error": need}
            out = json.dumps(payload, indent=2)
            return out

        # Take into account variations in position fields
        def _is_pitcher(p):
            pass
            pos = (p.get("position") or p.get("primary_position") or "").upper()
            return pos in ("P", "RP", "SP", "PITCHER")

        candidates = [
            p
            for p in data["players"]
            if p.get("current_team_id") == team_id and _is_pitcher(p)
        ]
        # Consistent sorting
        candidates = sorted(
            candidates,
            key=lambda p: (str(p.get("full_name") or ""), int(p.get("player_id") or 0)),
        )
        out = [
            {"player_id": p.get("player_id"), "full_name": p.get("full_name")}
            for p in candidates[: int(limit)]
        ]
        payload = {"probable_pitchers": out}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "ListProbablePitchers",
                "description": "Lists probable pitchers for a team, sorted by full_name ASC (deterministic sample from roster).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {"type": "integer"},
                        "limit": {"type": "integer"},
                    },
                    "required": ["team_id"],
                },
            },
        }
