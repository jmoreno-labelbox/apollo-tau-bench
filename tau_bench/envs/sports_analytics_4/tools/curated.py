from tau_bench.envs.tool import Tool
import json
from typing import Any

class Curated(Tool):
    @staticmethod
    #primary invocation function
    def invoke(
        data: dict[str, Any],
        report_id: str = None,
        player_id: str = None,
        insight_text: str = None,
        insight_type: str = None,
        supporting_stat_value: Any = None,
        game_pk: Any = None,
        pitcher_id: Any = None
    ) -> str:
        curated = data.get("curated_insights", [])
        curated.append(
            {
                "report_id": report_id,
                "player_id": player_id,
                "insight_text": insight_text,
                "insight_type": insight_type,
                "supporting_stat_value": supporting_stat_value,
            }
        )
        payload = {"status": "ok"}
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
                "name": "makeIn",
                "description": "Persists a curated insight row.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "report_id": {"type": "string"},
                        "player_id": {"type": "integer"},
                        "insight_text": {"type": "string"},
                        "insight_type": {"type": "string"},
                        "supporting_stat_value": {"type": "number"},
                    },
                    "required": [
                        "report_id",
                        "player_id",
                        "insight_text",
                        "insight_type",
                    ],
                },
            },
        }
