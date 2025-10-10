# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindStaleReviewsTool(Tool):
    """Return cycles exceeding SLA (status not APPROVED) by comparing last_updated with SLA hours."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        now_iso = _require_str(kwargs.get("now_iso"), "now_iso")  # comparison baseline
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
