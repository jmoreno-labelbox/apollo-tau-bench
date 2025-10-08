from tau_bench.envs.tool import Tool
import json
import math
import re
from typing import Any

class BulkCreateComparableEntriesTool(Tool):
    """Perform batch insertion of comparables for a report."""

    @staticmethod
    def invoke(data: dict[str, Any], report_id: int = None, comparables: list = None) -> str:
        report_id = _as_int(report_id)
        items = comparables or []
        if report_id is None:
            return _err("report_id is required")
        if not isinstance(items, list) or not items:
            return _err("comparables must be a non-empty list")

        rows = data.setdefault("comparables", [])
        created = []
        for it in items:
            pid = (it or {}).get("comp_property_id")
            if not pid:
                continue
            rec = {
                "comp_id": _next_int_id(rows, "comp_id"),
                "report_id": report_id,
                "comp_property_id": str(pid),
                "similarity_score": float((it or {}).get("similarity_score") or 0.0),
                "selection_reason": (it or {}).get("selection_reason") or "",
                "tie_breaker_notes": (it or {}).get("tie_breaker_notes"),
            }
            rows.append(rec)
            created.append(rec)
        payload = {"created_count": len(created), "comparables": created}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "BulkCreateComparableEntries",
                "description": "Create multiple comparables for a comp report.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "report_id": {"type": "integer"},
                        "comparables": {"type": "array", "items": {"type": "object"}},
                    },
                    "required": ["report_id", "comparables"],
                },
            },
        }
