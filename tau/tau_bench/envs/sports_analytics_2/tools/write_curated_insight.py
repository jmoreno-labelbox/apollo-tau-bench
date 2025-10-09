from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class WriteCuratedInsight(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], **kwargs) -> str:
        pass
        curated = data.get("curated_insights", {}).values()
        curated.append(
            {
                "report_id": kwargs.get("report_id"),
                "player_id": kwargs.get("player_id"),
                "insight_text": kwargs.get("insight_text"),
                "insight_type": kwargs.get("insight_type"),
                "supporting_stat_value": kwargs.get("supporting_stat_value"),
            }
        )
        payload = {"status": "ok"}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "WriteCuratedInsight",
                "description": "Writes a curated insight row.",
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
