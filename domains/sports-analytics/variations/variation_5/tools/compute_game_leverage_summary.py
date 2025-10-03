from tau_bench.envs.tool import Tool
import json
import re
from typing import Any

class ComputeGameLeverageSummary(Tool):
    """Summarize the number of events exceeding the high-leverage threshold (strict > threshold; default 1.5)."""

    @staticmethod
    def invoke(data, game_pk: int = None, threshold: float = 1.5, leverage_threshold: float = None) -> str:
        # Use leverage_threshold if provided, otherwise use threshold
        if leverage_threshold is not None:
            threshold = leverage_threshold
        err = _require_tables(data, ["game_day_events"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload, indent=2)
            return out
        if game_pk is None:
            payload = {"error": "game_pk is required."}
            out = json.dumps(payload, indent=2)
            return out
        rows = [e for e in data["game_day_events"] if e.get("game_pk") == game_pk]
        total = len(rows)
        high = len(
            [e for e in rows if (e.get("leverage_index") or 0) > float(threshold)]
        )
        manual = len([e for e in rows if e.get("is_manual_alert") is True])
        payload = {
                "game_pk": game_pk,
                "events_total": total,
                "events_high_leverage": high,
                "events_manual": manual,
                "threshold_used": threshold,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "ComputeGameLeverageSummary",
                "description": "Returns counts of events and those above leverage threshold.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "game_pk": {"type": "integer"},
                        "threshold": {"type": "number"},
                    },
                    "required": ["game_pk"],
                },
            },
        }
