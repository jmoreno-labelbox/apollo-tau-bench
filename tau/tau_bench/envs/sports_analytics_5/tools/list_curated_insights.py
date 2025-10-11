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

class ListCuratedInsights(Tool):
    """List curated_insights by player_id and/or report_id, optional min supporting_stat_value. Sorted by value desc, player_id asc."""
    @staticmethod
    def invoke(data, min_supporting_stat_value, player_id, report_id)->str:
        err = _require_tables(data, ["curated_insights"])
        if err:
            return json.dumps({"error": err}, indent=2)
        pid = player_id
        rid = report_id
        min_val = min_supporting_stat_value
        rows = list(data.get("curated_insights", {}).values())
        if pid is not None:
            rows = [r for r in rows if r.get("player_id")==pid]
        if rid is not None:
            rows = [r for r in rows if r.get("report_id")==rid]
        if min_val is not None:
            rows = [r for r in rows if (r.get("supporting_stat_value") or 0) >= float(min_val)]
        rows = sorted(rows, key=lambda r: (-float(r.get("supporting_stat_value") or 0), int(r.get("player_id") or 0)))
        return json.dumps(rows, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"list_curated_insights","description":"Lists curated insights filtered by player/report and threshold.","parameters":{"type":"object","properties":{"player_id":{"type":"integer"},"report_id":{"type":"integer"},"min_supporting_stat_value":{"type":"number"}},"required":[]}}}