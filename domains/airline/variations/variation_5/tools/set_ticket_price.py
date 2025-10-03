from tau_bench.envs.tool import Tool
from __future__ import annotations
import json
from datetime import date, datetime, timedelta  #required for fallback window enlargement
from decimal import ROUND_HALF_UP, Decimal
from typing import Any
import re
from datetime import date as _date

class SetTicketPrice(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        *,
        flight_number: str,
        date: str,
        fare_class: str,
        price: float,
        require_available: bool = False
    ) -> str:
        flights = data.get("flights", [])
        if isinstance(flights, dict):
            f = flights.get(flight_number)
        elif isinstance(flights, list):
            f = next(
                (row for row in flights if row.get("flight_number") == flight_number),
                None,
            )
        else:
            f = None

        if not f:
            return _json({"error": "flight_not_found", "flight_number": flight_number})

        d = f.get("dates", {}).get(date) if isinstance(f.get("dates"), dict) else None
        if not d:
            return _json({"error": "date_not_found", "date": date})

        #standardize status and enforce if necessary
        status = _norm_status(d.get("status"))
        if require_available and status != "available":
            return _json(
                {
                    "error": "invalid_status",
                    "reason": f"Flight {flight_number} on {date} has status '{status}', "
                    f"cannot set ticket price unless 'available'.",
                }
            )

        inv = d.setdefault("inventory", {}).setdefault(fare_class, {})
        inv["price"] = float(price)

        return _json(
            {
                "success": True,
                "flight_number": flight_number,
                "date": date,
                "fare_class": fare_class,
                "price": inv["price"],
                "status": status,
            }
        )
        pass
        flights = data.get("flights", [])
        if isinstance(flights, dict):
            f = flights.get(flight_number)
        elif isinstance(flights, list):
            f = next(
                (row for row in flights if row.get("flight_number") == flight_number),
                None,
            )
        else:
            f = None

        if not f:
            return _json({"error": "flight_not_found", "flight_number": flight_number})

        d = f.get("dates", {}).get(date) if isinstance(f.get("dates"), dict) else None
        if not d:
            return _json({"error": "date_not_found", "date": date})

        #standardize status and enforce if necessary
        status = _norm_status(d.get("status"))
        if require_available and status != "available":
            return _json(
                {
                    "error": "invalid_status",
                    "reason": f"Flight {flight_number} on {date} has status '{status}', "
                    f"cannot set ticket price unless 'available'.",
                }
            )

        inv = d.setdefault("inventory", {}).setdefault(fare_class, {})
        inv["price"] = float(price)

        return _json(
            {
                "success": True,
                "flight_number": flight_number,
                "date": date,
                "fare_class": fare_class,
                "price": inv["price"],
                "status": status,
            }
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetTicketPrice",
                "description": "Set the ticket price for a given fare_class on a flight date. "
                "Optionally enforce that the flight must be 'available'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {"type": "string"},
                        "date": {"type": "string", "description": "YYYY-MM-DD"},
                        "fare_class": {"type": "string"},
                        "price": {"type": "number"},
                        "require_available": {
                            "type": "boolean",
                            "description": "If true, only allow when status=='available'. Default false.",
                        },
                    },
                    "required": ["flight_number", "date", "fare_class", "price"],
                },
            },
        }
