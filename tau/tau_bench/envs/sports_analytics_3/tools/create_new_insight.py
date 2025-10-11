# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateNewInsight(Tool):
    """
    Create a new curated insight.

    Required inputs (exact names):
      - report_id (int)
      - player_id (int)
      - insight_text (string, non-empty)
      - insight_type (string, non-empty)
      - supporting_stat_value (number)

    Behavior:
      - insight_id is auto-generated as max existing + 1 (starts at 1).
    """

    @staticmethod
    def invoke(data: Dict[str, Any], insight_text, insight_type, player_id, report_id, supporting_stat_value) -> str:

        # 1) Check for necessary inputs
        missing = []
        if report_id is None: missing.append("report_id")
        if player_id is None: missing.append("player_id")
        if not isinstance(insight_text, str) or insight_text.strip() == "": missing.append("insight_text")
        if not isinstance(insight_type, str) or insight_type.strip() == "": missing.append("insight_type")
        if supporting_stat_value is None: missing.append("supporting_stat_value")

        if missing:
            return json.dumps({"error": f"Missing required field(s): {', '.join(missing)}"}, indent=2)

        # Retrieve database.
        insights: List[Dict[str, Any]] = list(data.get("curated_insights", {}).values())

        # 3) Create a new insight_id in a deterministic manner.
        new_id = get_next_insight_id(data)

        # 4) Create and add the row.
        new_row = {
            "insight_id": new_id,
            "report_id": report_id,
            "player_id": player_id,
            "insight_text": insight_text,
            "insight_type": insight_type,
            "supporting_stat_value": supporting_stat_value
        }
        insights.append(new_row)

        return json.dumps(new_row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_new_insight",
                "description": "Create a new curated insight; insight_id auto-generated (max existing + 1).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "report_id": {
                            "type": "integer",
                            "description": "Report ID this insight is associated with."
                        },
                        "player_id": {
                            "type": "integer",
                            "description": "Player ID this insight refers to."
                        },
                        "insight_text": {
                            "type": "string",
                            "description": "Human-readable insight text."
                        },
                        "insight_type": {
                            "type": "string",
                            "description": "Category/type of the insight (case-sensitive)."
                        },
                        "supporting_stat_value": {
                            "type": "number",
                            "description": "Numeric value that supports the insight."
                        }
                    },
                    "required": [
                        "report_id",
                        "player_id",
                        "insight_text",
                        "insight_type",
                        "supporting_stat_value"
                    ]
                }
            }
        }
