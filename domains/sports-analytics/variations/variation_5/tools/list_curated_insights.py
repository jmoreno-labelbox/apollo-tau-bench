from tau_bench.envs.tool import Tool
import json
import re
from typing import Any

class ListCuratedInsights(Tool):
    """Retrieve curated_insights by player_id and/or report_id, with an optional minimum supporting_stat_value. Sorted by value in descending order, player_id in ascending order."""

    @staticmethod
    def invoke(data, player_id=None, report_id=None, min_supporting_stat_value=None) -> str:
        err = _require_tables(data, ["curated_insights"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload, indent=2)
            return out
        rows = data["curated_insights"]
        if player_id is not None:
            rows = [r for r in rows if r.get("player_id") == player_id]
        if report_id is not None:
            rows = [r for r in rows if r.get("report_id") == report_id]
        if min_supporting_stat_value is not None:
            rows = [
                r
                for r in rows
                if (r.get("supporting_stat_value") or 0) >= float(min_supporting_stat_value)
            ]
        rows = sorted(
            rows,
            key=lambda r: (
                -float(r.get("supporting_stat_value") or 0),
                int(r.get("player_id") or 0),
            ),
        )
        payload = rows
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "ListCuratedInsights",
                "description": "Lists curated insights filtered by player/report and threshold.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "player_id": {"type": "integer"},
                        "report_id": {"type": "integer"},
                        "min_supporting_stat_value": {"type": "number"},
                    },
                    "required": [],
                },
            },
        }
