# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require_tables


class ComputeGameLeverageSummary(Tool):
    """Summarize counts of events above the high-leverage threshold (strict > threshold; default 1.5)."""
    @staticmethod
    def invoke(data, game_pk, threshold = 1.5)->str:
        err = _require_tables(data, ["game_day_events"])
        if err:
            return json.dumps({"error": err}, indent=2)
        if game_pk is None:
            return json.dumps({"error":"game_pk is required."}, indent=2)
        rows = [e for e in data["game_day_events"] if e.get("game_pk")==game_pk]
        total = len(rows)
        high = len([e for e in rows if (e.get("leverage_index") or 0) > float(threshold)])
        manual = len([e for e in rows if e.get("is_manual_alert") is True])
        return json.dumps({"game_pk":game_pk,"events_total":total,"events_high_leverage":high,"events_manual":manual,"threshold_used":threshold}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"compute_game_leverage_summary","description":"Returns counts of events and those above leverage threshold.","parameters":{"type":"object","properties":{"game_pk":{"type":"integer"},"threshold":{"type":"number"}},"required":["game_pk"]}}}
