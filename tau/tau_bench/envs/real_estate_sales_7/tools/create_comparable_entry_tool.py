# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateComparableEntryTool(Tool):
    """Creates single comparable entry in comparables table."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        report_id = kwargs.get("report_id")
        comp_property_id = kwargs.get("comp_property_id")
        similarity_score = kwargs.get("similarity_score")
        selection_reason = kwargs.get("selection_reason")

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
        return json.dumps(rec, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_comparable_entry",
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
