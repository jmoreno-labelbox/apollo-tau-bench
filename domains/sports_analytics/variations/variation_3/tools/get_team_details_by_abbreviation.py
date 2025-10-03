from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetTeamDetailsByAbbreviation(Tool):
    """Retrieve a team record using its abbreviation (exact, case-sensitive)."""

    @staticmethod
    def invoke(data: dict[str, Any], abbreviation: str = None) -> str:
        #1) Confirm validity
        if not isinstance(abbreviation, str) or abbreviation == "":
            payload = {"error": "Missing required field: abbreviation"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        #2) Retrieve DB using provided data
        teams = data.get("teams", [])

        #3) Lookup for exact matches (without normalization)
        for team in teams:
            if team.get("abbreviation") == abbreviation:
                payload = team
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No team found with abbreviation {abbreviation}"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTeamDetailsByAbbreviation",
                "description": "Fetch a single team's full details by exact abbreviation (case-sensitive).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "abbreviation": {
                            "type": "string",
                            "description": "Exact team abbreviation to retrieve (e.g., 'NYM').",
                        }
                    },
                    "required": ["abbreviation"],
                },
            },
        }
