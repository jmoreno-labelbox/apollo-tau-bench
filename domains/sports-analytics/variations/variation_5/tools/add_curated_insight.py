from tau_bench.envs.tool import Tool
import json
import re
from typing import Any

class AddCuratedInsight(Tool):
    """Insert a curated_insights entry associated with a report and player. Enforces structured insight_text and permitted insight_type."""

    @staticmethod
    def invoke(
        data,
        report_id: str = None,
        player_id: str = None,
        insight_text: str = None,
        insight_type: str = None,
        supporting_stat_value: float = None,
    ) -> str:
        err = _require_tables(data, ["curated_insights"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload, indent=2)
            return out
        need = _check_required(
            {
                "report_id": report_id,
                "player_id": player_id,
                "insight_text": insight_text,
                "insight_type": insight_type,
                "supporting_stat_value": supporting_stat_value,
            },
            [
                "report_id",
                "player_id",
                "insight_text",
                "insight_type",
                "supporting_stat_value",
            ],
        )
        if need:
            payload = {"error": need}
            out = json.dumps(payload, indent=2)
            return out
        # Ensure a consistent template and permitted types
        allowed_types = {
            "tendency",
            "execution",
            "stamina",
            "situational",
            "predictability",
        }
        if insight_type not in allowed_types:
            payload = {"error": f"insight_type must be one of {sorted(list(allowed_types))}"}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        pattern = r"^(tendency|execution|stamina|situational|predictability)_[a-z0-9]+_[a-z0-9]+$"
        if not re.match(pattern, insight_text):
            payload = {
                "error": "insight_text must match '{category}_{metric}_{bucket}' using lowercase letters/digits."
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        rows = data["curated_insights"]
        new_id = _next_id(rows, "insight_id")
        row = {
            "insight_id": new_id,
            "report_id": report_id,
            "player_id": player_id,
            "insight_text": insight_text,
            "insight_type": insight_type,
            "supporting_stat_value": supporting_stat_value,
        }
        rows.append(row)
        payload = {"insight_id": new_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "AddCuratedInsight",
                "description": "Inserts a curated insight row (templated text enforced).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "report_id": {"type": "integer"},
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
                        "supporting_stat_value",
                    ],
                },
            },
        }
