# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require_tables








def _require_tables(data: Dict[str, Any], required: List[str]) -> Optional[str]:
    missing = [t for t in required if t not in data or data.get(t) is None]
    if missing:
        return f"Missing required table(s): {', '.join(missing)}"
    return None

def _next_id(rows: List[Dict[str, Any]], key: str) -> int:
    max_id = 0
    for r in rows:
        try:
            max_id = max(max_id, int(r.get(key, 0)))
        except Exception:
            pass
    return max_id + 1

def _check_required(kwargs: Dict[str, Any], required: List[str]) -> Optional[str]:
    missing = [k for k in required if kwargs.get(k) is None]
    if missing:
        return f"Missing required argument(s): {', '.join(missing)}"
    return None

class AddCuratedInsight(Tool):
    """Add a curated_insights row linked to a report and player. Enforces templated insight_text and allowed insight_type."""
    @staticmethod
    def invoke(data, insight_text, insight_type, player_id, report_id, supporting_stat_value)->str:
        err = _require_tables(data, ["curated_insights"])
        if err:
            return json.dumps({"error": err}, indent=2)
        need = _check_required(kwargs, ["report_id","player_id","insight_text","insight_type","supporting_stat_value"])
        if need:
            return json.dumps({"error": need}, indent=2)
        # Ensure consistent template and permitted types.
        allowed_types = {"tendency","execution","stamina","situational","predictability"}
        t = insight_type
        if t not in allowed_types:
            return json.dumps({"error": f"insight_type must be one of {sorted(list(allowed_types))}"}, indent=2)
        pattern = r"^(tendency|execution|stamina|situational|predictability)_[a-z0-9]+_[a-z0-9]+$"
        if not re.match(pattern, insight_text):
            return json.dumps({"error":"insight_text must match '{category}_{metric}_{bucket}' using lowercase letters/digits."}, indent=2)

        rows = list(data.get("curated_insights", {}).values())
        new_id = _next_id(rows, "insight_id")
        row = {
            "insight_id": new_id,
            "report_id": report_id,
            "player_id": player_id,
            "insight_text": insight_text,
            "insight_type": insight_type,
            "supporting_stat_value": supporting_stat_value
        }
        rows.append(row)
        return json.dumps({"insight_id": new_id}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"add_curated_insight","description":"Inserts a curated insight row (templated text enforced).","parameters":{"type":"object","properties":{"report_id":{"type":"integer"},"player_id":{"type":"integer"},"insight_text":{"type":"string"},"insight_type":{"type":"string"},"supporting_stat_value":{"type":"number"}},"required":["report_id","player_id","insight_text","insight_type","supporting_stat_value"]}}}