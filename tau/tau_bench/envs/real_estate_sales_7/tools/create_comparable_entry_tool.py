# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _next_int_id(rows: List[Dict[str, Any]], key: str) -> int:
    mx = 0
    for r in rows:
        try:
            v = int(r.get(key, 0))
            if v > mx:
                mx = v
        except Exception:
            continue
    return mx + 1

def _err(msg: str, code: str = "bad_request", ) -> str:
    out = {"error": msg, "code": code}
    if extra:
        out.update(extra)
    return json.dumps(out, indent=2)

class CreateComparableEntryTool(Tool):
    """Creates single comparable entry in comparables table."""

    @staticmethod
    def invoke(data: Dict[str, Any], comp_property_id, report_id, selection_reason, similarity_score) -> str:

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