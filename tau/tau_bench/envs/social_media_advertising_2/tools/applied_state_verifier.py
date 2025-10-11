# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AppliedStateVerifier(Tool):
    """
    Compare expected vs actual ad set states.
    If the runtime can fetch from storage by plan_id/adset_ids, great; otherwise callers may pass expected_rows/actual_rows directly.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], actual_rows = [], expected_rows = [], key_fields = ["adset_id", "budget", "bid_strategy", "bid_amount"]) -> str:
        expected_rows: List[Dict[str, Any]] = expected_rows
        actual_rows: List[Dict[str, Any]] = actual_rows
        mismatches: List[Dict[str, Any]] = []

        idx = {str(r.get("adset_id")): r for r in actual_rows}
        for exp in expected_rows:
            aid = str(exp.get("adset_id"))
            act = idx.get(aid, {})
            for k in key_fields:
                ev = exp.get(k)
                av = act.get(k)
                if ev != av:
                    mismatches.append({"adset_id": aid, "field": k, "expected": ev, "actual": av})

        ok = len(mismatches) == 0
        return json.dumps({"success": True, "ok": ok, "mismatches": mismatches}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "applied_state_verifier",
                "description": "Deterministically compare expected vs actual ad set states.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "expected_rows": {"type": "array", "items": {"type": "object"}},
                        "actual_rows": {"type": "array", "items": {"type": "object"}},
                        "key_fields": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["expected_rows", "actual_rows"],
                    "additionalProperties": False
                }
            }
        }
