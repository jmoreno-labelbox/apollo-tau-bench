from tau_bench.envs.tool import Tool
import json
from typing import Any

class SummarizePlayerPerformance(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], player_id: str = None) -> str:
        games = data.get("games", [])
        stats = [g for g in games if player_id in g.get("player_stats", {})]
        summary = {
            "player_id": player_id,
            "games_played": len(stats),
            "avg_batting_avg": sum(
                s["player_stats"][player_id].get("batting_avg", 0) for s in stats
            )
            / max(len(stats), 1),
            "avg_ops": sum(s["player_stats"][player_id].get("ops", 0) for s in stats)
            / max(len(stats), 1),
        }
        payload = summary
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        pass
        #return result
        return {
            "type": "function",
            "function": {
                "name": "summarizePlayerPerformance",
                "description": "Creates an aggregated summary of a player's recent performance over available games.",
                "parameters": {
                    "type": "object",
                    "properties": {"player_id": {"type": "integer"}},
                    "required": ["player_id"],
                },
            },
        }
