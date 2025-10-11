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

def _err(msg: str, code: str = "bad_request", **extra) -> str:
    out = {"error": msg, "code": code}
    if extra:
        out.update(extra)
    return json.dumps(out, indent=2)

def _as_int(x) -> Optional[int]:
    try:
        return int(x)
    except Exception:
        return None

class BulkCreateComparableEntriesTool(Tool):
    """Batch insert comparables for a report."""

    @staticmethod
    def invoke(data: Dict[str, Any], comparables, report_id) -> str:
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

        return json.dumps(
            {"created_count": len(created), "comparables": created}, indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "bulk_create_comparable_entries",
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