from tau_bench.envs.tool import Tool
import json
import re
from typing import Any

class GetActiveRoster(Tool):
    """Snapshot of the active roster for a team, omitting IL/Taxi unless include_il=True."""

    @staticmethod
    def invoke(data, team_id, include_il=False) -> str:
        pass
        err = _require_tables(data, ["players"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload, indent=2)
            return out
        if team_id is None:
            payload = {"error": "team_id is required."}
            out = json.dumps(payload, indent=2)
            return out

        def _eligible(p):
            pass
            rs = (p.get("roster_status") or "").upper()
            if include_il:
                return True
            return rs == "ACTIVE"

        rows = [
            p
            for p in data["players"]
            if p.get("current_team_id") == team_id and _eligible(p)
        ]
        payload = rows
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetActiveRoster",
                "description": "Returns active roster for a team_id. Excludes IL/Taxi by default.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {"type": "integer"},
                        "include_il": {"type": "boolean"},
                    },
                    "required": ["team_id"],
                },
            },
        }
