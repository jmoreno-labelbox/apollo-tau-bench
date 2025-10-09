from tau_bench.envs.tool import Tool
from __future__ import annotations
import json
from datetime import date, datetime, timedelta  #required for fallback window enlargement
from decimal import ROUND_HALF_UP, Decimal
from typing import Any
import re
from datetime import date as _date

class LogUpgradeNoCharge(Tool):
    """
    Create a predictable audit entry for a no-charge upgrade in price_changes.
    Returns audit_id. The timestamp is derived predictably from 'date' (T00:00:00Z) if supplied.
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        *,
        reservation_id: str | None = None,
        flight_number: str | None = None,
        date: str | None = None,
        from_cabin: str,
        to_cabin: str,
        reason: str | None = None
    ) -> str:
        pass
        date_str = date  # YYYY-MM-DD (optional yet advisable)
        from_cabin = (from_cabin or "").lower()
        to_cabin = (to_cabin or "").lower()
        reason = reason or "no_charge_upgrade"

        if not reservation_id and not (flight_number and date_str):
            return _json(
                {
                    "error": "missing_params",
                    "reason": "Provide reservation_id or (flight_number and date).",
                }
            )
        if not from_cabin or not to_cabin or from_cabin == to_cabin:
            return _json({"error": "invalid_cabins"})

        # Predictable id and timestamp
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
        pass
        date_str = date  #YYYY-MM-DD (optional yet advisable)
        from_cabin = (from_cabin or "").lower()
        to_cabin = (to_cabin or "").lower()
        reason = reason or "no_charge_upgrade"

        if not reservation_id and not (flight_number and date_str):
            return _json(
                {
                    "error": "missing_params",
                    "reason": "Provide reservation_id or (flight_number and date).",
                }
            )
        if not from_cabin or not to_cabin or from_cabin == to_cabin:
            return _json({"error": "invalid_cabins"})

        #Predictable id and timestamp
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
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LogUpgradeNoCharge",
                "description": "Write an audit entry for a no-charge upgrade to the price_changes log.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {"type": "string"},
                        "flight_number": {"type": "string"},
                        "date": {"type": "string"},
                        "from_cabin": {
                            "type": "string",
                            "enum": ["basic_economy", "economy", "business"],
                        },
                        "to_cabin": {
                            "type": "string",
                            "enum": ["basic_economy", "economy", "business"],
                        },
                        "reason": {"type": "string"},
                    },
                    "required": ["from_cabin", "to_cabin"],
                },
            },
        }
