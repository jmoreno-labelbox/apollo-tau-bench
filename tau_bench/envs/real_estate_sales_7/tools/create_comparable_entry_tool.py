from tau_bench.envs.tool import Tool
import json
import math
import re
from typing import Any

class CreateComparableEntryTool(Tool):
    """Inserts a single comparable record into the comparables table."""

    @staticmethod
    def invoke(data: dict[str, Any], report_id: int = None, comp_property_id: str = None, similarity_score: float = None, selection_reason: str = None) -> str:
        if report_id is None or not comp_property_id or similarity_score is None:
            return _err("report_id, comp_property_id, similarity_score are required")

        rows = data.setdefault("comparables", [])
        comp_id = _next_int_id(rows, "comp_id")
        rec = {
            "comp_id": comp_id,
            "report_id": int(report_id),
            "comp_property_id": str(comp_property_id),
            "similarity_score": float(similarity_score),
            "selection_reason": selection_reason,
            "tie_breaker_notes": None,
        }
        rows.append(rec)
        payload = rec
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createComparableEntry",
                "description": "Creates single comparable entry in comparables table.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "report_id": {"type": "integer"},
                        "comp_property_id": {"type": "string"},
                        "similarity_score": {"type": "number"},
                        "selection_reason": {"type": ["string", "null"]},
                    },
                    "required": ["report_id", "comp_property_id", "similarity_score"],
                },
            },
        }
