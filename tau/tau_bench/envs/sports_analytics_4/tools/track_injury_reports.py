from tau_bench.envs.tool import Tool
import json
from typing import Any

class TrackInjuryReports(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], player_id: str = None) -> str:
        injuries = data.get("injury_reports", [])
        player_injuries = [i for i in injuries if i.get("player_id") == player_id]
        payload = {"player_id": player_id, "injury_history": player_injuries}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        pass
        #return result
        return {
            "type": "function",
            "function": {
                "name": "trackInjuryReports",
                "description": "Retrieves injury history for a given player from injury_reports.",
                "parameters": {
                    "type": "object",
                    "properties": {"player_id": {"type": "integer"}},
                    "required": ["player_id"],
                },
            },
        }
