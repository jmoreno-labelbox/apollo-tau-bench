from tau_bench.envs.tool import Tool
import csv
import json
import re
from datetime import datetime
from typing import Any

class AppliedStateVerifier(Tool):
    """
    Assess expected versus actual ad set states.
    If the runtime can retrieve from storage using plan_id/adset_ids, that's ideal; otherwise, callers can directly provide expected_rows/actual_rows.
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        expected_rows: list[dict[str, Any]] = [],
        actual_rows: list[dict[str, Any]] = [],
        key_fields: list[str] = ["adset_id", "budget", "bid_strategy", "bid_amount"]
,
    plan_id: Any = None,
    ) -> str:
        mismatches: list[dict[str, Any]] = []

        idx = {str(r.get("adset_id")): r for r in actual_rows}
        for exp in expected_rows:
            aid = str(exp.get("adset_id"))
            act = idx.get(aid, {})
            for k in key_fields:
                ev = exp.get(k)
                av = act.get(k)
                if ev != av:
                    mismatches.append(
                        {"adset_id": aid, "field": k, "expected": ev, "actual": av}
                    )

        ok = len(mismatches) == 0
        payload = {"success": True, "ok": ok, "mismatches": mismatches}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AppliedStateVerifier",
                "description": "Deterministically compare expected vs actual ad set states.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "expected_rows": {"type": "array", "items": {"type": "object"}},
                        "actual_rows": {"type": "array", "items": {"type": "object"}},
                        "key_fields": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["expected_rows", "actual_rows"],
                    "additionalProperties": False,
                },
            },
        }
