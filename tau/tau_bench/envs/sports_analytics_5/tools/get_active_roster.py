# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require_tables


class GetActiveRoster(Tool):
    """Active roster snapshot for a team, excluding IL/Taxi unless include_il=True."""
    @staticmethod
    def invoke(data, **kwargs)->str:
        err = _require_tables(data, ["players"])
        if err:
            return json.dumps({"error": err}, indent=2)
        team_id = kwargs.get("team_id")
        include_il = kwargs.get("include_il", False)
        if team_id is None:
            return json.dumps({"error":"team_id is required."}, indent=2)
        def _eligible(p):
            rs = (p.get("roster_status") or "").upper()
            if include_il:
                return True
            return (rs == "ACTIVE")
        rows = [p for p in data["players"] if p.get("current_team_id")==team_id and _eligible(p)]
        return json.dumps(rows, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"get_active_roster","description":"Returns active roster for a team_id. Excludes IL/Taxi by default.","parameters":{"type":"object","properties":{"team_id":{"type":"integer"},"include_il":{"type":"boolean"}},"required":["team_id"]}}}
