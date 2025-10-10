# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetTeamLead(Tool):
    """Retrieves the lead engineer/lead ops for a specific team."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        team_id = kwargs.get("team_id")
        teams = data.get("teams", [])
        for team in teams:
            if team.get("id") == team_id:
                lead_id = team.get("lead_engineer") or team.get("lead_ops") or team.get("lead_security") or team.get("lead_analytics") or team.get("lead_server_ops")
                if lead_id:
                    return json.dumps({"lead_id": lead_id})

        teams = data.get("team_members", [])
        for team in teams:
            if team.get("team_id") == team_id:
                if team.get('role') == 'team_lead':
                    return json.dumps({"lead_id": team.get('user_id')})

        return json.dumps({"error": f"Lead for team ID '{team_id}' not found."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_team_lead",
                "description": "Retrieves the lead for a specific team.",
                "parameters": {
                    "type": "object",
                    "properties": {"team_id": {"type": "string"}},
                    "required": ["team_id"],
                },
            },
        }
