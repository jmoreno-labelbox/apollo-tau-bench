# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require_tables


class ListProbablePitchers(Tool):
    """Returns probable pitchers for a team: deterministic sample from players table (position 'P' if present), sorted by full_name ASC."""
    @staticmethod
    def invoke(data, team_id, limit = 2)->str:
        err = _require_tables(data, ["players"])
        if err:
            return json.dumps({"error": err}, indent=2)
        need = _check_required(kwargs, ["team_id"])
        if need:
            return json.dumps({"error": need}, indent=2)
        # Account for variations in position fields.
        def _is_pitcher(p):
            pos = (p.get("position") or p.get("primary_position") or "").upper()
            return pos in ("P","RP","SP","PITCHER")
        candidates = [p for p in data["players"] if p.get("current_team_id")==team_id and _is_pitcher(p)]
        # Predictable ordering
        candidates = sorted(candidates, key=lambda p: (str(p.get("full_name") or ""), int(p.get("player_id") or 0)))
        out = [{"player_id": p.get("player_id"), "full_name": p.get("full_name")} for p in candidates[:int(limit)]]
        return json.dumps({"probable_pitchers": out}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{
            "name":"list_probable_pitchers",
            "description":"Lists probable pitchers for a team, sorted by full_name ASC (deterministic sample from roster).",
            "parameters":{"type":"object","properties":{
                "team_id":{"type":"integer"},
                "limit":{"type":"integer"}}, "required":["team_id"]}
        }}
