# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require_tables


class ListCuratedInsights(Tool):
    """List curated_insights by player_id and/or report_id, optional min supporting_stat_value. Sorted by value desc, player_id asc."""
    @staticmethod
    def invoke(data, **kwargs)->str:
        err = _require_tables(data, ["curated_insights"])
        if err:
            return json.dumps({"error": err}, indent=2)
        pid = kwargs.get("player_id")
        rid = kwargs.get("report_id")
        min_val = kwargs.get("min_supporting_stat_value")
        rows = data["curated_insights"]
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
