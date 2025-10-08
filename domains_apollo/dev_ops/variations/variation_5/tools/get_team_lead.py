from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetTeamLead(Tool):
    """Obtains the lead engineer/lead operations for a particular team."""

    @staticmethod
    def invoke(data: dict[str, Any], team_id: str = None) -> str:
        teams = data.get("teams", [])
        for team in teams:
            if team.get("id") == team_id:
                lead_id = (
                    team.get("lead_engineer")
                    or team.get("lead_ops")
                    or team.get("lead_security")
                    or team.get("lead_analytics")
                    or team.get("lead_server_ops")
                )
                if lead_id:
                    payload = {"lead_id": lead_id}
                    out = json.dumps(payload)
                    return out

        teams = data.get("team_members", [])
        for team in teams:
            if team.get("team_id") == team_id:
                if team.get("role") == "team_lead":
                    payload = {"lead_id": team.get("user_id")}
                    out = json.dumps(payload)
                    return out
        payload = {"error": f"Lead for team ID '{team_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTeamLead",
                "description": "Retrieves the lead for a specific team.",
                "parameters": {
                    "type": "object",
                    "properties": {"team_id": {"type": "string"}},
                    "required": ["team_id"],
                },
            },
        }
