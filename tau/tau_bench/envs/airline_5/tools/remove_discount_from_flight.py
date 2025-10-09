from tau_bench.envs.tool import Tool
from __future__ import annotations
import json
from datetime import date, datetime, timedelta  #required for fallback window enlargement
from decimal import ROUND_HALF_UP, Decimal
from typing import Any
import re
from datetime import date as _date



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class RemoveDiscountFromFlight(Tool):
    """
    Undo a discount applied to a flight/date/fare_class.

    Order of strategies:
      1) Revert based on audit (preferred)
      2) Revert to specified 'original_price'
      3) Revert to 'percent' inversion
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        flight_number: str,
        date: str,
        fare_class: str,
        discount_id: str | None = None,
        original_price: float | None = None,
        percent: float | None = None,
        strict: bool = False
    ) -> str:
        pass
        fare_class_req = (fare_class or "").lower().strip()

        flight = _get_flight(data, flight_number)
        if not flight:
            return _json({"error": "flight_not_found"})

        rec = _get_date_record(flight, date)
        if not rec or _norm_status(rec.get("status")) != "available":
            return _json({"error": "price_not_available_for_date"})

        prices = rec.get("prices") or {}
        if not isinstance(prices, dict) or fare_class_req not in prices:
            return _json({"error": "fare_class_not_found"})

        resolved_cabin = fare_class_req
        override_used = False

        #--- Approach 1: revert based on audit ---
        audits = [
            a
            for a in data.get("price_changes", {}).values()
            if isinstance(a, dict) and a.get("type") == "discount"
        ]

        def id_seq(aid: str) -> int:
            pass
            try:
                return int(str(aid)[2:])
            except Exception:
                return -1

        def match_base(a):
            pass
            return a.get("flight_number") == flight_number and a.get("date") == date

        audit_row = None
        if discount_id:
            audit_row = next(
                (a for a in audits if a.get("id") == discount_id and match_base(a)),
                None,
            )
            if not audit_row and strict:
                return _json({"error": "discount_not_found"})
        else:
            candidates = [
                a
                for a in audits
                if match_base(a) and a.get("fare_class") == resolved_cabin
            ] or [a for a in audits.values() if match_base(a)]
            candidates.sort(key=lambda x: id_seq(x.get("id")), reverse=True)
            audit_row = candidates[0] if candidates else None

        if audit_row:
            audit_cab = (audit_row.get("fare_class") or "").lower().strip()
            if audit_cab and audit_cab != resolved_cabin:
                if strict:
                    return _json(
                        {
                            "error": "fare_class_mismatch",
                            "expected": audit_cab,
                            "provided": resolved_cabin,
                        }
                    )
                resolved_cabin = audit_cab
                override_used = True

            if resolved_cabin not in prices:
                return _json({"error": "fare_class_not_found"})

            try:
                current_f = float(prices[resolved_cabin])
                old_f = float(audit_row.get("old"))
                new_f = float(audit_row.get("new"))
            except Exception:
                if strict:
                    return _json({"error": "discount_not_found"})
                audit_row = None
            else:
                if strict and round(current_f, 2) != round(new_f, 2):
                    return _json(
                        {
                            "error": "price_mismatch",
                            "expected_current": round(new_f, 2),
                            "found_current": round(current_f, 2),
                        }
                    )
                prices[resolved_cabin] = round(old_f, 2)
                revert_id = _next_change_id(data, prefix="PC")
                (data.setdefault("price_changes", [])).append(
                    {
                        "id": revert_id,
                        "type": "revert_discount",
                        "flight_number": flight_number,
                        "date": date,
                        "fare_class": resolved_cabin,
                        "old": round(current_f, 2),
                        "new": round(old_f, 2),
                        "reverts_audit_id": audit_row.get("id"),
                    }
                )
                return _json(
                    {
                        "success": True,
                        "strategy": "audit",
                        "audit_id": revert_id,
                        "reverted_from_audit": True,
                        "discount_id_used": audit_row.get("id"),
                        "flight_number": flight_number,
                        "date": date,
                        "fare_class": resolved_cabin,
                        "fare_class_overridden_from_audit": override_used or None,
                        "previous_price": round(current_f, 2),
                        "restored_price": round(old_f, 2),
                    }
                )

        #--- Approach 2: specific original_price ---
        if original_price is not None:
            try:
                orig_f = round(float(original_price), 2)
            except Exception:
                return _json({"error": "invalid_original_price"})
            try:
                current_f = round(float(prices[resolved_cabin]), 2)
            except Exception:
                return _json({"error": "fare_class_not_found"})

            prices[resolved_cabin] = orig_f
            revert_id = _next_change_id(data, prefix="PC")
            (data.setdefault("price_changes", [])).append(
                {
                    "id": revert_id,
                    "type": "revert_discount",
                    "flight_number": flight_number,
                    "date": date,
                    "fare_class": resolved_cabin,
                    "old": current_f,
                    "new": orig_f,
                    "reverts_audit_id": discount_id,
                }
            )
            return _json(
                {
                    "success": True,
                    "strategy": "original_price",
                    "audit_id": revert_id,
                    "reverted_from_audit": False,
                    "discount_id_used": discount_id,
                    "flight_number": flight_number,
                    "date": date,
                    "fare_class": resolved_cabin,
                    "previous_price": current_f,
                    "restored_price": orig_f,
                }
            )

        #--- Approach 3: reverse by percentage ---
        if percent is not None:
            try:
                pct = float(percent)
            except Exception:
                return _json({"error": "invalid_percent"})
            if pct <= 0 or pct > 100:
                return _json({"error": "invalid_percent"})

            try:
                current_f = float(prices[resolved_cabin])
            except Exception:
                return _json({"error": "fare_class_not_found"})

            denom = 1 - pct / 100.0
            if denom <= 0:
                return _json({"error": "invalid_percent"})
            restored = round(current_f / denom, 2)

            prices[resolved_cabin] = restored
            revert_id = _next_change_id(data, prefix="PC")
            (data.setdefault("price_changes", [])).append(
                {
                    "id": revert_id,
                    "type": "revert_discount",
                    "flight_number": flight_number,
                    "date": date,
                    "fare_class": resolved_cabin,
                    "old": round(current_f, 2),
                    "new": restored,
                    "reverts_percent": pct,
                    "reverts_audit_id": discount_id,
                }
            )
            return _json(
                {
                    "success": True,
                    "strategy": "percent",
                    "audit_id": revert_id,
                    "reverted_from_audit": False,
                    "discount_id_used": discount_id,
                    "flight_number": flight_number,
                    "date": date,
                    "fare_class": resolved_cabin,
                    "previous_price": round(current_f, 2),
                    "restored_price": restored,
                }
            )

        #No valid audit and no fallback data
        return _json(
            {
                "error": "missing_params",
                "reason": "Provide discount_id (preferred) or original_price/percent.",
            }
        )
        pass
        fare_class_req = (fare_class or "").lower().strip()

        flight = _get_flight(data, flight_number)
        if not flight:
            return _json({"error": "flight_not_found"})

        rec = _get_date_record(flight, date)
        if not rec or _norm_status(rec.get("status")) != "available":
            return _json({"error": "price_not_available_for_date"})

        prices = rec.get("prices") or {}
        if not isinstance(prices, dict) or fare_class_req not in prices:
            return _json({"error": "fare_class_not_found"})

        resolved_cabin = fare_class_req
        override_used = False

        #--- Approach 1: revert based on audit ---
        audits = [
            a
            for a in data.get("price_changes", {}).values()
            if isinstance(a, dict) and a.get("type") == "discount"
        ]

        def id_seq(aid: str) -> int:
            pass
            try:
                return int(str(aid)[2:])
            except Exception:
                return -1

        def match_base(a):
            pass
            return a.get("flight_number") == flight_number and a.get("date") == date

        audit_row = None
        if discount_id:
            audit_row = next(
                (a for a in audits if a.get("id") == discount_id and match_base(a)),
                None,
            )
            if not audit_row and strict:
                return _json({"error": "discount_not_found"})
        else:
            candidates = [
                a
                for a in audits
                if match_base(a) and a.get("fare_class") == resolved_cabin
            ] or [a for a in audits.values() if match_base(a)]
            candidates.sort(key=lambda x: id_seq(x.get("id")), reverse=True)
            audit_row = candidates[0] if candidates else None

        if audit_row:
            audit_cab = (audit_row.get("fare_class") or "").lower().strip()
            if audit_cab and audit_cab != resolved_cabin:
                if strict:
                    return _json(
                        {
                            "error": "fare_class_mismatch",
                            "expected": audit_cab,
                            "provided": resolved_cabin,
                        }
                    )
                resolved_cabin = audit_cab
                override_used = True

            if resolved_cabin not in prices:
                return _json({"error": "fare_class_not_found"})

            try:
                current_f = float(prices[resolved_cabin])
                old_f = float(audit_row.get("old"))
                new_f = float(audit_row.get("new"))
            except Exception:
                if strict:
                    return _json({"error": "discount_not_found"})
                audit_row = None
            else:
                if strict and round(current_f, 2) != round(new_f, 2):
                    return _json(
                        {
                            "error": "price_mismatch",
                            "expected_current": round(new_f, 2),
                            "found_current": round(current_f, 2),
                        }
                    )
                prices[resolved_cabin] = round(old_f, 2)
                revert_id = _next_change_id(data, prefix="PC")
                (data.setdefault("price_changes", [])).append(
                    {
                        "id": revert_id,
                        "type": "revert_discount",
                        "flight_number": flight_number,
                        "date": date,
                        "fare_class": resolved_cabin,
                        "old": round(current_f, 2),
                        "new": round(old_f, 2),
                        "reverts_audit_id": audit_row.get("id"),
                    }
                )
                return _json(
                    {
                        "success": True,
                        "strategy": "audit",
                        "audit_id": revert_id,
                        "reverted_from_audit": True,
                        "discount_id_used": audit_row.get("id"),
                        "flight_number": flight_number,
                        "date": date,
                        "fare_class": resolved_cabin,
                        "fare_class_overridden_from_audit": override_used or None,
                        "previous_price": round(current_f, 2),
                        "restored_price": round(old_f, 2),
                    }
                )

        #--- Approach 2: specific original_price ---
        if original_price is not None:
            try:
                orig_f = round(float(original_price), 2)
            except Exception:
                return _json({"error": "invalid_original_price"})
            try:
                current_f = round(float(prices[resolved_cabin]), 2)
            except Exception:
                return _json({"error": "fare_class_not_found"})

            prices[resolved_cabin] = orig_f
            revert_id = _next_change_id(data, prefix="PC")
            (data.setdefault("price_changes", [])).append(
                {
                    "id": revert_id,
                    "type": "revert_discount",
                    "flight_number": flight_number,
                    "date": date,
                    "fare_class": resolved_cabin,
                    "old": current_f,
                    "new": orig_f,
                    "reverts_audit_id": discount_id,
                }
            )
            return _json(
                {
                    "success": True,
                    "strategy": "original_price",
                    "audit_id": revert_id,
                    "reverted_from_audit": False,
                    "discount_id_used": discount_id,
                    "flight_number": flight_number,
                    "date": date,
                    "fare_class": resolved_cabin,
                    "previous_price": current_f,
                    "restored_price": orig_f,
                }
            )

        #--- Approach 3: reverse by percentage ---
        if percent is not None:
            try:
                pct = float(percent)
            except Exception:
                return _json({"error": "invalid_percent"})
            if pct <= 0 or pct > 100:
                return _json({"error": "invalid_percent"})

            try:
                current_f = float(prices[resolved_cabin])
            except Exception:
                return _json({"error": "fare_class_not_found"})

            denom = 1 - pct / 100.0
            if denom <= 0:
                return _json({"error": "invalid_percent"})
            restored = round(current_f / denom, 2)

            prices[resolved_cabin] = restored
            revert_id = _next_change_id(data, prefix="PC")
            (data.setdefault("price_changes", [])).append(
                {
                    "id": revert_id,
                    "type": "revert_discount",
                    "flight_number": flight_number,
                    "date": date,
                    "fare_class": resolved_cabin,
                    "old": round(current_f, 2),
                    "new": restored,
                    "reverts_percent": pct,
                    "reverts_audit_id": discount_id,
                }
            )
            return _json(
                {
                    "success": True,
                    "strategy": "percent",
                    "audit_id": revert_id,
                    "reverted_from_audit": False,
                    "discount_id_used": discount_id,
                    "flight_number": flight_number,
                    "date": date,
                    "fare_class": resolved_cabin,
                    "previous_price": round(current_f, 2),
                    "restored_price": restored,
                }
            )

        #No valid audit and no fallback data
        return _json(
            {
                "error": "missing_params",
                "reason": "Provide discount_id (preferred) or original_price/percent.",
            }
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RemoveDiscountFromFlight",
                "description": "Revert a discount; prefer audit, else original_price, else percent.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {"type": "string"},
                        "date": {"type": "string"},
                        "fare_class": {
                            "type": "string",
                            "enum": ["basic_economy", "economy", "business"],
                        },
                        "discount_id": {"type": "string"},
                        "original_price": {"type": "number"},
                        "percent": {"type": "number"},
                        "strict": {"type": "boolean"},
                    },
                    "required": ["flight_number", "date", "fare_class"],
                    "additionalProperties": False,
                },
            },
        }
