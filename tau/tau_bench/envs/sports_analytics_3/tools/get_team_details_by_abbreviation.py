# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetTeamDetailsByAbbreviation(Tool):
    """Fetch a team record by its abbreviation (exact, case-sensitive)."""

    @staticmethod
    def invoke(data: Dict[str, Any], abbreviation) -> str:

        # 1) Verify
        if not isinstance(abbreviation, str) or abbreviation == "":
            return json.dumps({"error": "Missing required field: abbreviation"}, indent=2)

        # Obtain the database from the provided data.
        teams = list(data.get("teams", {}).values())

        # 3) Precise match retrieval (without normalization)
        for team in teams:
            if team.get("abbreviation") == abbreviation:
                return json.dumps(team, indent=2)

        return json.dumps({"error": f"No team found with abbreviation {abbreviation}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_team_details_by_abbreviation",
                "description": "Fetch a single team's full details by exact abbreviation (case-sensitive).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "abbreviation": {
                            "type": "string",
                            "description": "Exact team abbreviation to retrieve (e.g., 'NYM')."
                        }
                    },
                    "required": ["abbreviation"]
                }
            }
        }
