from tau_bench.envs.tool import Tool
import json
from typing import Any

class RunMatchupAnalysis(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], **kwargs) -> str:
        pass
        opponent_team = kwargs.get("opponent_team")
        kwargs.get("our_lineup")
        payload = {"matchup_analysis": f"matchups_vs_team_{opponent_team}"}
        out = json.dumps(
            payload, indent=2
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "runMatchupAnalysis",
                "description": "Runs tactical matchup analysis between lineups.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "opponent_team": {"type": "integer"},
                        "our_lineup": {"type": "string"},
                    },
                    "required": ["opponent_team"],
                },
            },
        }
