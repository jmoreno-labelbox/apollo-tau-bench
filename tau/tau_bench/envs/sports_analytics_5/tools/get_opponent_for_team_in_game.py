# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require_tables


class GetOpponentForTeamInGame(Tool):
    """Given a team_id and a game_pk, return the opponent team_id."""
    @staticmethod
    def invoke(data, game_pk, team_id)->str:
        err = _require_tables(data, ["games"])
        if err:
            return json.dumps({"error": err}, indent=2)
        need = _check_required(kwargs, ["game_pk","team_id"])
        if need:
            return json.dumps({"error": need}, indent=2)
        g = next((g for g in data["games"] if g.get("game_pk")==game_pk), None)
        if not g:
            return json.dumps({"error":"Game not found."}, indent=2)
        team = team_id
        if g.get("home_team_id")==team:
            opp = g.get("away_team_id")
        elif g.get("away_team_id")==team:
            opp = g.get("home_team_id")
        else:
            return json.dumps({"error":"team_id not in specified game."}, indent=2)
        return json.dumps({"opponent_team_id": opp}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"get_opponent_for_team_in_game","description":"Finds the opponent team_id for a team in a given game.","parameters":{"type":"object","properties":{"game_pk":{"type":"integer"},"team_id":{"type":"integer"}},"required":["game_pk","team_id"]}}}
