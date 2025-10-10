# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class BulkUpgradeTicketPrices(Tool):
    """
    No-charge upgrade: copy from_cabin price to to_cabin in [start_date, end_date] for a flight.
      - Only dates with status == 'available' are changed (compliant).
      - Emits one deterministic audit per (date, from_cabin -> to_cabin) actually changed.
      - Idempotent: if the (date, from_cabin, to_cabin) audit already exists with the same resulting price, no-ops.
      - Returns counts and a capped preview of first N changes.
    """
    @staticmethod
    def invoke(
        data: Dict[str, Any], *,
        flight_number: str,
        start_date: str,
        end_date: str,
        from_cabin: str,
        to_cabin: str,
        max_preview: int = 0,
    ) -> str:
        # validate dates
        try:
            sd = date.fromisoformat(start_date)
            ed = date.fromisoformat(end_date)
        except Exception:
            return _json({"error": "invalid_date_format"})
        if sd > ed:
            return _json({"error": "invalid_date_range", "start_date": start_date, "end_date": end_date})

        # normalize cabins
        from_cabin = (from_cabin or "").strip().lower()
        to_cabin   = (to_cabin or "").strip().lower()
        if from_cabin == to_cabin:
            return _json({"error": "invalid_cabins", "reason": "from_cabin and to_cabin must differ"})

        f = _get_flight(data, flight_number)
        if not f:
            return _json({"error": "flight_not_found"})

        changed = 0
        preview: List[Dict[str, Any]] = []
        audits = data.setdefault("upgrade_audits", [])  # bucket-scoped no-charge audits

        # iterate deterministically
        for d in sorted((f.get("dates") or {}).keys()):
            if not (start_date <= d <= end_date):
                continue
            rec = (f.get("dates") or {}).get(d) or {}
            if _norm_status(rec.get("status")) != "available":
                continue
            prices = rec.get("prices") or {}
            if from_cabin not in prices or to_cabin not in prices:
                continue

            # source/target rounded values
            try:
                src = float(Decimal(str(prices[from_cabin])).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))
                dst = float(Decimal(str(prices[to_cabin])).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))
            except Exception:
                continue

            # idempotent: if already equal AND audit exists, skip
            audit_exists = next((
                a for a in audits
                if a.get("flight_number") == flight_number
                and a.get("date") == d
                and a.get("from_cabin") == from_cabin
                and a.get("to_cabin") == to_cabin
                and float(a.get("price_to_cabin")) == src
            ), None)
            if dst == src and audit_exists:
                continue

            if dst != src:
                rec.setdefault("prices", {})[to_cabin] = src
                changed += 1
                if len(preview) < max_preview:
                    preview.append({
                        "date": d,
                        "from_cabin": from_cabin,
                        "to_cabin": to_cabin,
                        "old_to_cabin": dst,
                        "new_to_cabin": src
                    })

            # write deterministic audit (bucket-scoped; no reservation_id)
            audit_id = _next_change_id(data, prefix="UG")
            audits.append({
                "id": audit_id,
                "type": "no_charge_upgrade",
                "flight_number": flight_number,
                "date": d,
                "from_cabin": from_cabin,
                "to_cabin": to_cabin,
                "price_to_cabin": src,
                "no_charge": True
            })

        return _json({
            "success": True,
            "flight_number": flight_number,
            "start_date": start_date,
            "end_date": end_date,
            "from_cabin": from_cabin,
            "to_cabin": to_cabin,
            "changed": changed,
            "preview": preview
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type":"function",
            "function":{
                "name":"bulk_upgrade_ticket_prices",
                "description":"No-charge upgrade (bucket-scoped) with deterministic audits and idempotency.",
                "parameters":{
                    "type":"object",
                    "properties":{
                        "flight_number": {"type": "string"},
                        "start_date": {"type": "string"},
                        "end_date": {"type": "string"},
                        "from_cabin":{"type": "string", "enum":["basic_economy", "economy", "business"]},
                        "to_cabin":{"type": "string","enum":["basic_economy","economy","business"]},
                        "max_preview":{"type": "integer"},
                    },
                    "required":["flight_number", "start_date", "end_date", "from_cabin", "to_cabin"],
                    "additionalProperties": False
                }
            }
        }
