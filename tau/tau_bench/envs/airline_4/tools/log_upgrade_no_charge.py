# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LogUpgradeNoCharge(Tool):
    """
    Write a deterministic audit entry for a no-charge upgrade into price_changes.
    Returns audit_id. Timestamp is derived deterministically from 'date' (T00:00:00Z) if provided.
    """

    @staticmethod
    def invoke(
        data: Dict[str, Any], *,
        reservation_id: Optional[str] = None,
        flight_number: Optional[str] = None,
        date: Optional[str] = None,
        from_cabin: str,
        to_cabin: str,
        reason: Optional[str] = None
    ) -> str:
        date_str       = date # Format: YYYY-MM-DD (optional, but advisable)
        from_cabin     = (from_cabin or "").lower()
        to_cabin       = (to_cabin or "").lower()
        reason         = reason or "no_charge_upgrade"

        if not reservation_id and not (flight_number and date_str):
            return _json({"error":"missing_params", "reason":"Provide reservation_id or (flight_number and date)."})
        if not from_cabin or not to_cabin or from_cabin == to_cabin:
            return _json({"error":"invalid_cabins"})

        # Predictable identifier and time marker
        change_id = _next_change_id(data, prefix="PC")
        det_ts = f"{str(date_str)[:10]}T00:00:00Z" if date_str else None

        entry = {
            "id": change_id,
            "type": "upgrade_no_charge",
            "reservation_id": reservation_id,
            "flight_number": flight_number,
            "date": date_str,
            "from_cabin": from_cabin,
            "to_cabin": to_cabin,
            "reason": reason,
        }
        if det_ts is not None:
            entry["timestamp"] = det_ts

        (data.setdefault("price_changes", [])).append(entry)

        return _json({"success": True, "audit_id": change_id, "logged": entry})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type":"function",
            "function": {
                "name": "log_upgrade_no_charge",
                "description": "Write an audit entry for a no-charge upgrade to the price_changes log.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {"type": "string"},
                        "flight_number": {"type": "string"},
                        "date": {"type": "string"},
                        "from_cabin": {"type": "string", "enum": ["basic_economy", "economy", "business"]},
                        "to_cabin": {"type": "string", "enum": ["basic_economy", "economy", "business"]},
                        "reason": {"type": "string"}
                    },
                    "required":["from_cabin","to_cabin"]
                }
            }
        }
