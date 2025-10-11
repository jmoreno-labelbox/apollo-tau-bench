# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool








def _small_fields(row: Dict[str, Any], fields: List[str]) -> Dict[str, Any]:
    """Return selected fields only (simple outputs)."""
    return {k: row.get(k) for k in fields}

def _require_str(arg: Any, name: str) -> Optional[str]:
    """Return arg as str if valid, else None."""
    return arg if isinstance(arg, str) and arg.strip() else None

def _get_config_json(data: Dict[str, Any], key: str) -> Dict[str, Any]:
    """Read a config row from system_config and parse its JSON value."""
    rows = data.get("system_config", [])
    for r in rows:
        if r.get("config_key") == key:
            try:
                return json.loads(r.get("config_value_json") or "{}")
            except Exception:
                return {}
    return {}

class FindStaleReviewsTool(Tool):
    """Return cycles exceeding SLA (status not APPROVED) by comparing last_updated with SLA hours."""

    @staticmethod
    def invoke(data: Dict[str, Any], now_iso) -> str:
        now_iso = _require_str(now_iso, "now_iso")  # reference point for comparison
        if not now_iso:
            return json.dumps({"error":"now_iso is required (ISO timestamp baseline)"})

        cycles = data.get("review_cycles", [])
        sla_hours = _get_config_json(data, "sla_deadlines").get("design_review", 72)

        def overdue(c: Dict[str, Any]) -> bool:
            return c.get("status") != "APPROVED" and c.get("last_updated","") < now_iso

        out = []
        for c in cycles:
            if overdue(c):
                out.append(_small_fields(c, ["cycle_id","artifact_id","status","last_updated"]))
        out.sort(key=lambda r: r.get("cycle_id",""))
        return json.dumps({"sla_hours": sla_hours, "stale_cycles": out}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"find_stale_reviews",
            "description":"Find review cycles not APPROVED and older than 'now_iso' (approximation for SLA breach).",
            "parameters":{"type":"object","properties":{
                "now_iso":{"type":"string","description":"Current timestamp baseline (ISO)."}
            },"required":["now_iso"]}
        }}