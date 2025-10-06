import json
from datetime import datetime, timedelta
from typing import Any

from tau_bench.envs.tool import Tool


def _next_numeric_suffix(prefix: str, items: list[dict[str, Any]], key: str) -> str:
    pass
    mx = 0
    for it in items:
        s = it.get(key)
        if not isinstance(s, str) or not s.startswith(prefix):
            continue
        try:
            num = int(s[len(prefix) :])
            mx = max(mx, num)
        except Exception:
            pass
    return f"{prefix}{mx+1:03d}"


def _j(v):
    pass
    return (
        v
        if isinstance(v, str)
        else json.dumps(v, separators=(",", ":"), ensure_ascii=False)
    )


class GetAirportByCode(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], iata_code: str) -> str:
        for a in data.get("airports", []):
            if a.get("iata_code") == iata_code:
                return _j(a)
        return _j(
            {
                "airport_id": "ARP_" + iata_code,
                "iata_code": iata_code,
            }
        )
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAirportByCode",
                "description": "Return one airport by IATA code.",
                "parameters": {
                    "type": "object",
                    "properties": {"iata_code": {"type": "string"}},
                    "required": ["iata_code"],
                },
            },
        }


class GetAircraftByTail(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], tail_number: str) -> str:
        for a in data.get("aircraft", []):
            if a.get("tail_number") == tail_number:
                return _j(a)
        return _j({})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAircraftByTail",
                "description": "Return an aircraft row by tail number.",
                "parameters": {
                    "type": "object",
                    "properties": {"tail_number": {"type": "string"}},
                    "required": ["tail_number"],
                },
            },
        }


class GetAircraftByAirport(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], airport_id: str) -> str:
        res = []
        for a in data.get("aircraft", []):
            if a.get("location").get("airport_id") == airport_id:
                res.append(_j(a))
        return _j(res)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAircraftByAirport",
                "description": "Return aircraft by their base airport.",
                "parameters": {
                    "type": "object",
                    "properties": {"airport_id": {"type": "string"}},
                    "required": ["airport_id"],
                },
            },
        }


class LookupFlightDay(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], date: str, flight_number: str | None = None
    ) -> str:
        for f in data.get("flights", []):
            if flight_number and f.get("flight_number") != flight_number:
                continue
            day = (f.get("dates") or {}).get(date)
            if day is not None:
                # merge the main schedule with daily status and times
                out = {
                    "flight_number": f.get("flight_number"),
                    "origin": f.get("origin"),
                    "destination": f.get("destination"),
                    "scheduled_departure_time_est": f.get(
                        "scheduled_departure_time_est"
                    ),
                    "scheduled_arrival_time_est": f.get("scheduled_arrival_time_est"),
                    "date": date,
                    "day": day,
                }
                return _j(out)
        return _j({})


    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LookupFlightDay",
                "description": "Return combined schedule + per-day status for a flight_number on a specific date (YYYY-MM-DD).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "date": {"type": "string"},
                        "flight_number": {"type": "string"},
                    },
                    "required": ["date"],
                },
            },
        }


class ScanFlightsByDate(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        date: str,
        flight_numbers: list[str] | None = None,
        origin: str | None = None,
        destination: str | None = None,
        status: list[str] | None = None,
    ) -> str:
        out = []
        for f in data.get("flights", []):
            day = (f.get("dates") or {}).get(date)
            if not isinstance(day, dict):
                continue
            if origin and f.get("origin") != origin:
                continue
            if destination and f.get("destination") != destination:
                continue
            if status and day.get("status") not in set(status):
                continue
            if flight_numbers and f.get("flight_number") not in set(flight_numbers):
                continue
            out.append(
                {
                    "flight_number": f.get("flight_number"),
                    "origin": f.get("origin"),
                    "destination": f.get("destination"),
                    "date": date,
                    "status": day.get("status"),
                    "scheduled_departure_time_est": f.get(
                        "scheduled_departure_time_est"
                    ),
                }
            )
        # organize by scheduled time followed by flight number
        out.sort(
            key=lambda x: (
                x.get("scheduled_departure_time_est", ""),
                x.get("flight_number", ""),
            )
        )
        return _j(out)

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ScanFlightsByDate",
                "description": "Search flights by date with optional origin/destination/status filters; sorted by scheduled_departure_time_est.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "date": {"type": "string"},
                        "flight_numbers": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "origin": {"type": "string"},
                        "destination": {"type": "string"},
                        "status": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["date"],
                },
            },
        }


class GetFlightScheduledTimes(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], flight_number: str) -> str:
        for f in data.get("flights", []):
            if f.get("flight_number") == flight_number:
                return _j(
                    {
                        "flight_number": flight_number,
                        "scheduled_departure_time_est": f.get(
                            "scheduled_departure_time_est"
                        ),
                        "scheduled_arrival_time_est": f.get(
                            "scheduled_arrival_time_est"
                        ),
                    }
                )
        return _j({"error": "flight_not_found", "flight_number": flight_number})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetFlightScheduledTimes",
                "description": "Return the estimated scheduled departure/arrival times for a flight.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {"type": "string"},
                    },
                    "required": ["flight_number"],
                },
            },
        }


class FindReservationsByUser(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str) -> str:
        res = [r for r in data.get("reservations", []) if r.get("user_id") == user_id]
        return _j(res)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindReservationsByUser",
                "description": "Return all reservations for a user_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }


class FindReservationsByFlightDay(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], flight_number: str, date: str) -> str:
        out = []
        for r in data.get("reservations", []):
            for seg in r.get("flights", []):
                if (
                    seg.get("flight_number") == flight_number
                    and seg.get("date") == date
                ):
                    r["pets"] = {"cats": 0, "dogs": 0}
                    out.append(r)
                    break
        return _j(out)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindReservationsByFlightDay",
                "description": "Return reservations that include a segment with the given flight_number on the given date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {"type": "string"},
                        "date": {"type": "string"},
                    },
                    "required": ["flight_number", "date"],
                },
            },
        }


class GetCrewMemberByEmployeeCode(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_code: str) -> str:
        for c in data.get("crew_members", []):
            if c.get("employee_code") == employee_code:
                return _j(c)
        return _j({})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCrewMemberByEmployeeCode",
                "description": "Return one crew member by employee_code.",
                "parameters": {
                    "type": "object",
                    "properties": {"employee_code": {"type": "string"}},
                    "required": ["employee_code"],
                },
            },
        }


class GetCrewAssignments(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        crew_member_id: str | None = None,
        flight_number: str | None = None,
    ) -> str:
        out = []
        for a in data.get("flight_crew_assignments", []):
            if (
                crew_member_id
                and (a.get("crew_member") or {}).get("crew_member_id") != crew_member_id
            ):
                continue
            if (
                flight_number
                and (a.get("flight") or {}).get("flight_number") != flight_number
            ):
                continue
            out.append(a)
        return _j(out)

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCrewAssignments",
                "description": "List flight crew assignments filtered by crew_member_id and/or flight_number.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "crew_member_id": {"type": "string"},
                        "flight_number": {"type": "string"},
                    },
                },
            },
        }


class GetCrewCertifications(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], crew_member_id: str, certification_code: str | None = None
    ) -> str:
        out = []
        for c in data.get("crew_certifications", []):
            cmid = (c.get("crew_member") or {}).get("crew_member_id")
            if cmid != crew_member_id:
                continue
            if certification_code and c.get("certification_code") != certification_code:
                continue
            out.append(c)
        return _j(out)

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCrewCertifications",
                "description": "List certifications for a crew member; optionally filter by certification_code.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "crew_member_id": {"type": "string"},
                        "certification_code": {"type": "string"},
                    },
                    "required": ["crew_member_id"],
                },
            },
        }


class EventsAtAirportOn(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], airport_id: str, date: str) -> str:
        out = []
        for e in data.get("operational_events", []):
            ap = (e.get("airport") or {}).get("airport_id")
            ts = e.get("event_timestamp_utc", "")
            if ap == airport_id and isinstance(ts, str) and ts[:10] == date:
                out.append(e)
        return _j(out)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "EventsAtAirportOn",
                "description": "Return operational events at an airport on a date (UTC).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "airport_id": {"type": "string"},
                        "date": {"type": "string"},
                    },
                    "required": ["airport_id", "date"],
                },
            },
        }


class MaintenanceLogsForAircraft(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], aircraft_id: str) -> str:
        out = [
            m
            for m in data.get("MaintenanceLogs", [])
            if (m.get("aircraft") or {}).get("aircraft_id") == aircraft_id
        ]
        return _j(out)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "MaintenanceLogsForAircraft",
                "description": "List maintenance logs for a given aircraft_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"aircraft_id": {"type": "string"}},
                    "required": ["aircraft_id"],
                },
            },
        }


class MaintenanceLogs(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        MaintenanceLogs: list = None
    ) -> str:
        return _j(MaintenanceLogs or [])
        return _j(data.get("MaintenanceLogs", []))

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "MaintenanceLogs",
                "description": "List maintenance logs for a given aircraft_id.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }


class ComputeCrewDutyCounts(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], crew_member_id: str, reference_date: str) -> str:
        # Utilize crew_members[].flight_log dates along with assignments[].flight.flight_id and flights.json (by flight_number through operational_events link if necessary)
        # In this section: tally assignments in previous windows using the crew member's flight_log (which contains dates).
        # Only deterministic counts are allowed (excluding hours).
        ref = datetime.fromisoformat(reference_date + "T00:00:00+00:00")
        windows = {
            "24h": ref - timedelta(hours=24),
            "30d": ref - timedelta(days=30),
            "365d": ref - timedelta(days=365),
        }
        counts = {"24h": 0, "30d": 0, "365d": 0}
        # Derived from flight_log
        for c in data["crew_members"]:
            if c["crew_member_id"] != crew_member_id:
                continue
            for entry in c["flight_log"]:
                d = entry["date"]
                try:
                    dt = datetime.fromisoformat(d + "T00:00:00+00:00")
                except Exception:
                    continue
                for k, start in windows.items():
                    if start <= dt <= ref:
                        counts[k] += 1
            break
        return _j({"crew_member_id": crew_member_id, "counts": counts})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ComputeCrewDutyCounts",
                "description": "Compute counts of crew flight_log entries within 24h/30d/365d windows relative to reference_date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "crew_member_id": {"type": "string"},
                        "reference_date": {"type": "string"},
                    },
                    "required": ["crew_member_id", "reference_date"],
                },
            },
        }


#=========================
#AUTHORS
#=========================


class CreateOperationalEvent(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        airport_id: str,
        event_type: str,
        details: str,
        event_timestamp_utc: str,
        flight_id: str | None = None,
        aircraft_id: str | None = None,
    ) -> str:
        events = data.setdefault("operational_events", [])
        new_id = _next_numeric_suffix("OE", events, "event_id")
        rec = {
            "event_id": new_id,
            "flight": {"flight_id": flight_id} if flight_id else None,
            "aircraft": {"aircraft_id": aircraft_id} if aircraft_id else None,
            "airport": {"airport_id": airport_id},
            "event_type": event_type,
            "event_timestamp_utc": event_timestamp_utc or "2025-01-05T09:00:00Z",
            "status": "Logged",
            "details": details,
        }
        events.append(rec)
        return _j(rec)
        return _j(rec)

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateOperationalEvent",
                "description": "Append an operational event; deterministic ID (OE###); ",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "airport_id": {"type": "string"},
                        "event_type": {"type": "string"},
                        "details": {"type": "string"},
                        "event_timestamp_utc": {"type": "string"},
                        "flight_id": {"type": "string"},
                        "aircraft_id": {"type": "string"},
                    },
                    "required": [
                        "airport_id",
                        "event_type",
                        "details",
                        "event_timestamp_utc",
                    ],
                },
            },
        }


class SetAircraftStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], aircraft_id: str, new_status: str) -> str:
        new_status = new_status[:1].upper() + new_status[1:]
        for a in data.get("aircraft", []):
            if a.get("aircraft_id") == aircraft_id:
                a["status"] = new_status
                return _j(a)
        return _j({"error": "aircraft_not_found", "aircraft_id": aircraft_id})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetAircraftStatus",
                "description": "Set status on an aircraft deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "aircraft_id": {"type": "string"},
                        "new_status": {"type": "string"},
                    },
                    "required": ["aircraft_id", "new_status"],
                },
            },
        }


class RelocateAircraft(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        aircraft_id: str,
        new_location_airport_id: str,
        new_location_iata: str | None = None,
    ) -> str:
        for a in data.get("aircraft", []):
            if a.get("aircraft_id") == aircraft_id:
                a["location"] = (
                    {
                        "airport_id": new_location_airport_id,
                        "iata_code": new_location_iata,
                    }
                    if new_location_iata
                    else {"airport_id": new_location_airport_id}
                )
                return _j(a)
        return _j({"error": "aircraft_not_found", "aircraft_id": aircraft_id})


    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RelocateAircraft",
                "description": "Update aircraft.location to a new airport deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "aircraft_id": {"type": "string"},
                        "new_location_airport_id": {"type": "string"},
                        "new_location_iata": {"type": "string"},
                    },
                    "required": ["aircraft_id", "new_location_airport_id"],
                },
            },
        }


class AppendMaintenanceLog(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        aircraft_id: str,
        maintenance_type: str,
        description: str,
        event_timestamp_utc: str,
        technician_id: str | None = None,
        work_order_id: str | None = None,
        ata_chapter: str | None = None,
        corrective_action: str | None = None,
        mel_cdl_reference: str | None = None,
        next_due: str | None = None,
    ) -> str:
        logs = data.setdefault("MaintenanceLogs", [])
        new_id = _next_numeric_suffix("ML", logs, "log_id")
        rec = {
            "log_id": new_id,
            "aircraft": {"aircraft_id": aircraft_id},
            "event_timestamp_utc": event_timestamp_utc,
            "maintenance_type": maintenance_type,
            "description": description,
            "status": "Logged",
            "technician_id": technician_id,
            "work_order_id": work_order_id,
            "ata_chapter": ata_chapter,
            "corrective_action": corrective_action,
            "mel_cdl_reference": mel_cdl_reference,
            "next_due": next_due,
        }
        logs.append(rec)
        return _j(rec)
        return _j(rec)

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AppendMaintenanceLog",
                "description": "Append a maintenance log with deterministic ID (ML###).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "aircraft_id": {"type": "string"},
                        "maintenance_type": {"type": "string"},
                        "description": {"type": "string"},
                        "event_timestamp_utc": {"type": "string"},
                        "technician_id": {"type": "string"},
                        "work_order_id": {"type": "string"},
                        "ata_chapter": {"type": "string"},
                        "corrective_action": {"type": "string"},
                        "mel_cdl_reference": {"type": "string"},
                        "next_due": {"type": "string"},
                    },
                    "required": [
                        "aircraft_id",
                        "maintenance_type",
                        "description",
                        "event_timestamp_utc",
                    ],
                },
            },
        }


class UpdateCrewMemberStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], crew_member_id: str, new_status: str) -> str:
        for c in data.get("crew_members", []):
            if c.get("crew_member_id") == crew_member_id:
                c["status"] = new_status
                return _j(c)
        return _j({"error": "crew_member_not_found", "crew_member_id": crew_member_id})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCrewMemberStatus",
                "description": "Set status on a crew member deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "crew_member_id": {"type": "string"},
                        "new_status": {"type": "string"},
                    },
                    "required": ["crew_member_id", "new_status"],
                },
            },
        }


class CreateCrewAssignment(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        flight_number: str,
        crew_member_id: str,
        assigned_role: str,
    ) -> str:
        assigns = data.setdefault("flight_crew_assignments", [])
        new_id = _next_numeric_suffix("AS", assigns, "assignment_id")
        rec = {
            "assignment_id": new_id,
            "flight": {"flight_number": flight_number},
            "crew_member": {"crew_member_id": crew_member_id},
            "assigned_role": assigned_role,
        }
        assigns.append(rec)
        return _j(rec)
        return _j(rec)

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateCrewAssignment",
                "description": "Create a flight crew assignment with deterministic ID (AS###).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {"type": "string"},
                        "crew_member_id": {"type": "string"},
                        "assigned_role": {"type": "string"},
                    },
                    "required": ["flight_number", "crew_member_id", "assigned_role"],
                },
            },
        }


class UpdateFlightStatusForDate(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        flight_numbers: list[str] | None,
        date: str,
        new_status: str,
    ) -> str:
        _new_statusL = new_status or ''.lower()
        for f in data.get("flights", []):
            if f.get("flight_number") not in set(flight_numbers):
                continue
            day = (f.get("dates") or {}).get(date)
            if not isinstance(day, dict):
                return _j(
                    {
                        "error": "date_not_found",
                        "flight_number": flight_numbers,
                        "date": date,
                    }
                )
            day["status"] = new_status.lower()
            return _j(
                {
                    "flight_numbers": flight_numbers,
                    "date": date,
                    "status": new_status.lower(),
                }
            )
        return _j({"error": "flight_not_found", "flight_number": flight_numbers})
    

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateFlightStatusForDate",
                "description": "Set per-day status on a flight_number's date entry deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_numbers": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "date": {"type": "string"},
                        "new_status": {"type": "string"},
                    },
                    "required": ["flight_numbers", "date", "new_status"],
                },
            },
        }

class DelayFlightActualTimesForDate(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        flight_number: str,
        date: str,
        delay_minutes: int,
        also_mark_status: str | None = None,
    ) -> str:
        pass
        for f in data.get("flights", []):
            if f.get("flight_number") != flight_number:
                continue
            dates = f.get("dates") or {}
            day = dates.get(date)
            if not isinstance(day, dict):
                return _j(
                    {
                        "error": "date_not_found",
                        "flight_number": flight_number,
                        "date": date,
                    }
                )

            def _bump(ts: str | None):
                pass
                if not ts:
                    return ts
                #timestamp formatted as 2024-05-01T06:26:00 (without timezone)
                try:
                    dt = datetime.fromisoformat(ts)
                    dt = dt + timedelta(minutes=delay_minutes)
                    return dt.isoformat()
                except Exception:
                    return ts

            day["actual_departure_time_est"] = _bump(
                day.get("actual_departure_time_est")
            )
            day["actual_arrival_time_est"] = _bump(day.get("actual_arrival_time_est"))
            if also_mark_status:
                day["status"] = also_mark_status
            return _j(
                {
                    "flight_number": flight_number,
                    "date": date,
                    "delay_applied_minutes": delay_minutes,
                    "status": day.get("status"),
                }
            )
        return _j({"error": "flight_not_found", "flight_number": flight_number})

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DelayFlightActualTimesForDate",
                "description": "Add delay_minutes to actual_*_time_est fields for specific flight_number/date; optionally set status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {"type": "string"},
                        "date": {"type": "string"},
                        "delay_minutes": {"type": "integer"},
                        "also_mark_status": {"type": "string"},
                    },
                    "required": ["flight_number", "date", "delay_minutesdelay_minutes"],
                },
            },
        }

class CancelReservation(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], reservation_id: str) -> str:
        """If a reservation exists, cancel it and return either a success or error message."""
        reservations = data.get("reservations", [])

        for reservation in reservations:
            if reservation.get("reservation_id") == reservation_id:
                reservation["status"] = "cancelled"
                payload = {"success": f"Reservation {reservation_id} has been cancelled."}
                out = json.dumps(
                    payload)
                return out
        payload = {"error": f"Reservation with ID {reservation_id} not found."}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        """Provide metadata regarding the function signature of the tool."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "CancelReservation",
                "description": "Cancels a reservation by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {
                            "type": "string",
                            "description": "The ID of the reservation to cancel.",
                        }
                    },
                    "required": ["reservation_id"],
                },
            },
        }


class RefundReservation(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], reservation_id: str) -> str:
        """If a reservation is present, refund it and return a success or error message."""
        reservations = data.get("reservations", [])

        for reservation in reservations:
            if reservation.get("reservation_id") == reservation_id:
                reservation["status"] = "refunded"
                payload = {"success": f"Reservation {reservation_id} has been refunded."}
                out = json.dumps(
                    payload)
                return out
        payload = {"error": f"Reservation with ID {reservation_id} not found."}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        """Provide metadata for the function signature of the tool."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "RefundReservation",
                "description": "refunds a reservation by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {
                            "type": "string",
                            "description": "The ID of the reservation to refund.",
                        }
                    },
                    "required": ["reservation_id"],
                },
            },
        }


class RefundReservationsByFlightDay(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], flight_number: str, date: str) -> str:
        out = []
        for r in data.get("reservations", []):
            for seg in r.get("flights", []):
                if (
                    seg.get("flight_number") == flight_number
                    and seg.get("date") == date
                ):
                    seg["status"] = "refunded"
                    out.append(r)

        return _j(out)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RefundReservationsByFlightDay",
                "description": "Refund reservations that include a segment with the given flight_number on the given date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {"type": "string"},
                        "date": {"type": "string"},
                    },
                    "required": ["flight_number", "date"],
                },
            },
        }


class SendUserNotification(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], channel_or_user_id: str, message: str) -> str:
        pass
        #This tool does not store notifications — it provides a deterministic response
        return _j({"notified": channel_or_user_id, "message": message})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SendUserNotification",
                "description": "Send a message to a specified user or operations channel (non-persistent, returns confirmation).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "channel_or_user_id": {"type": "string"},
                        "message": {"type": "string"},
                    },
                    "required": ["channel_or_user_id", "message"],
                },
            },
        }


class FindAvailableCrew(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        role: str,
        home_base_iata: str | None = None,
        status: str | None = None,
    ) -> str:
        crew = data.get("crew_members", [])
        out = []
        for m in crew:
            if m.get("role") != role:
                continue
            if home_base_iata and (
                (m.get("home_base") or {}).get("iata_code") != home_base_iata
            ):
                continue
            if status and m.get("status") != status:
                continue
            out.append(m)
        return _j(out)

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindAvailableCrew",
                "description": "Find crew members by role, optionally filtering by home base IATA and status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role": {"type": "string"},
                        "home_base_iata": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": ["role"],
                },
            },
        }


class UpdateReservationStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], reservation_id: str, new_status: str) -> str:
        reservations = data.get("reservations", [])
        for r in reservations:
            if r.get("reservation_id") == reservation_id:
                r["status"] = new_status
                return _j(r)
        return _j({"error": "reservation_not_found", "reservation_id": reservation_id})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateReservationStatus",
                "description": "Update the status of a reservation (e.g., confirmed, ticketed, cancelled).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {"type": "string"},
                        "new_status": {"type": "string"},
                    },
                    "required": ["reservation_id", "new_status"],
                },
            },
        }


class UpdateReservationDetails(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        reservation_id: str,
        flights: list[dict[str, str]] | None = None,
        passengers: list[dict[str, str]] | None = None,
        cabin: str | None = None,
        seat: str | None = None,
        contact_email: str | None = None,
        contact_phone: str | None = None,
        insurance: str | None = None,
        total_baggages: int | None = None,
        nonfree_baggages: int | None = None,
    ) -> str:
        reservations = data.get("reservations", [])
        for r in reservations:
            if r.get("reservation_id") == reservation_id:
                if cabin is not None:
                    r["cabin"] = cabin
                if seat is not None:
                    r["seat"] = seat
                if insurance is not None:
                    r["insurance"] = insurance
                if total_baggages is not None:
                    r["total_baggages"] = total_baggages
                if nonfree_baggages is not None:
                    r["nonfree_baggages"] = nonfree_baggages

                if flights is not None:
                    r["flights"] = flights
                if passengers is not None:
                    r["passengers"] = passengers
                if contact_email is not None:
                    r.setdefault("contact", {})["email"] = contact_email
                if contact_phone is not None:
                    r.setdefault("contact", {})["phone"] = contact_phone
                return _j(r)
        return _j({"error": "reservation_not_found", "reservation_id": reservation_id})
                
                
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateReservationDetails",
                "description": "Update editable reservation fields (cabin, seat, contact email/phone).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {"type": "string"},
                        "cabin": {"type": "string"},
                        "seat": {"type": "string"},
                        "contact_email": {"type": "string"},
                        "contact_phone": {"type": "string"},
                        "insurance": {"type": "string"},
                        "total_baggages": {"type": "integer"},
                        "nonfree_baggages": {"type": "integer"},
                        "flights": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "flight_number": {"type": "string"},
                                    "date": {
                                        "type": "string",
                                        "description": "Date in YYYY-MM-DD format.",
                                    },
                                    "origin": {"type": "string"},
                                    "destination": {"type": "string"},
                                },
                                "required": [
                                    "flight_number",
                                    "date",
                                    "origin",
                                    "destination",
                                ],
                            },
                        },
                        "passengers": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "first_name": {"type": "string"},
                                    "last_name": {"type": "string"},
                                    "dob": {
                                        "type": "string",
                                        "description": "Date of birth in YYYY-MM-DD format.",
                                    },
                                },
                                "required": ["first_name", "last_name", "dob"],
                            },
                        },
                    },
                    "required": ["reservation_id"],
                },
            },
        }


class FindFlights(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any],
        origin: str,
        destination: str,
        start_date: str,
        end_date: str | None = None,
        status: list[str] | None = None,
    ) -> str:
        # Check the necessary parameters for validity
        if not (origin and destination and start_date):
            return _j(
                {
                    "error": "Missing required parameters",
                    "required": ["origin", "destination", "start_date"],
                }
            )

        # Interpret dates
        try:
            start_dt = datetime.strptime(start_date, "%Y-%m-%d").date()
        except ValueError:
            return _j(
                {
                    "error": "Invalid start_date format. Expected YYYY-MM-DD",
                    "received": start_date,
                }
            )

        if end_date is None or end_date == "":
            end_dt = start_dt
            end_date = start_date
        else:
            try:
                end_dt = datetime.strptime(end_date, "%Y-%m-%d").date()
            except ValueError:
                return _j(
                    {
                        "error": "Invalid end_date format. Expected YYYY-MM-DD",
                        "received": end_date,
                    }
                )
            if end_dt < start_dt:
                return _j(
                    {
                        "error": "end_date cannot be before start_date",
                        "start_date": start_date,
                        "end_date": end_date,
                    }
                )

        # Create a date range that includes all specified dates
        date_range: list[str] = []
        d = start_dt
        while d <= end_dt:
            date_range.append(d.strftime("%Y-%m-%d"))
            d += timedelta(days=1)

        flights = data.get("flights", [])
        matching_flights: list[dict[str, Any]] = []

        # Route and scan within the date range
        for f in flights:
            if f.get("origin") != origin or f.get("destination") != destination:
                continue

            per_day = f.get("dates", {})
            for day in date_range:
                if day not in per_day:
                    continue

                info = per_day[day]
                f_status = info.get("status")

                if status and f_status not in status:
                    continue

                result = {
                    "flight_number": f.get("flight_number"),
                    "origin": f.get("origin"),
                    "destination": f.get("destination"),
                    "scheduled_departure_time_est": f.get(
                        "scheduled_departure_time_est"
                    ),
                    "scheduled_arrival_time_est": f.get("scheduled_arrival_time_est"),
                    "date": day,
                    "status": f_status,
                }

                if f_status == "available":
                    if "available_seats" in info:
                        result["available_seats"] = info["available_seats"]
                    if "prices" in info:
                        result["prices"] = info["prices"]
                elif f_status == "delayed":
                    if "estimated_departure_time_est" in info:
                        result["estimated_departure_time_est"] = info[
                            "estimated_departure_time_est"
                        ]
                    if "estimated_arrival_time_est" in info:
                        result["estimated_arrival_time_est"] = info[
                            "estimated_arrival_time_est"
                        ]
                elif f_status == "landed":
                    if "actual_departure_time_est" in info:
                        result["actual_departure_time_est"] = info[
                            "actual_departure_time_est"
                        ]
                    if "actual_arrival_time_est" in info:
                        result["actual_arrival_time_est"] = info[
                            "actual_arrival_time_est"
                        ]

                matching_flights.append(result)

        matching_flights.sort(
            key=lambda x: (x["date"], x["scheduled_departure_time_est"])
        )

        flights_by_date: dict[str, list[dict[str, Any]]] = {}
        for r in matching_flights:
            flights_by_date.setdefault(r["date"], []).append(r)

        best_prices = None
        avail_with_prices = [
            r
            for r in matching_flights
            if r.get("status") == "available" and "prices" in r
        ]
        if avail_with_prices:
            all_prices = []
            for r in avail_with_prices:
                for cabin_class, price in r.get("prices", {}).items():
                    all_prices.append(
                        {
                            "cabin_class": cabin_class,
                            "price": price,
                            "flight": r["flight_number"],
                            "date": r["date"],
                        }
                    )
            if all_prices:
                all_prices.sort(key=lambda p: p["price"])
                best_prices = {"lowest_overall": all_prices[0], "by_cabin_class": {}}
                # Minimum for each cabin class
                seen = {}
                for p in all_prices:
                    cc = p["cabin_class"]
                    if cc not in seen:
                        seen[cc] = p
                best_prices["by_cabin_class"] = seen

        resp: dict[str, Any] = {
            "flights": matching_flights,
            "flights_by_date": flights_by_date,
        }
        if best_prices:
            resp["pricing_analysis"] = best_prices

        return _j(resp)
        

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindFlights",
                "description": "Find flights between airports with date ranges and filtering options. Returns comprehensive flight information with pricing analysis and status breakdowns.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "origin": {
                            "type": "string",
                            "description": "Origin airport IATA code",
                        },
                        "destination": {
                            "type": "string",
                            "description": "Destination airport IATA code",
                        },
                        "start_date": {
                            "type": "string",
                            "description": "Start date for search in YYYY-MM-DD format",
                        },
                        "end_date": {
                            "type": "string",
                            "description": "End date for search in YYYY-MM-DD format.",
                        },
                        "status": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Optional filter by flight status: 'available', 'delayed', 'landed', 'cancelled', 'departed', 'boarding', 'in_air'",
                        },
                    },
                    "required": ["origin", "destination", "start_date"],
                },
            },
        }


class CreateReservation(Tool):

    #--- utility functions (internal style) ---
    @staticmethod
    def _find_user(
        users: list[dict[str, Any]], user_email: str
    ) -> dict[str, str] | None:
        pass
        for u in users:
            if u.get("email") == user_email:
                first = (u.get("name", {}).get("first_name") or "").lower()
                last = (u.get("name", {}).get("last_name") or "").lower()
                return {"email": user_email, "id": f"{first}_{last}_1234"}
        return None

    @staticmethod
    def _next_reservation_id(reservations: list[dict[str, Any]]) -> str:
        pass
        last_num = 0
        if reservations:
            nums = [
                int(r.get("reservation_id", "0")[-4:])
                for r in reservations
                if r.get("reservation_id", "")[-4:].isdigit()
            ]
            if nums:
                last_num = max(nums)
        return f"RES{last_num + 1:04d}"

    @staticmethod
    def _attach_reservation_to_user(
        users: list[dict[str, Any]], user_email: str, res_id: str
    ) -> None:
        pass
        for u in users:
            if u.get("email") == user_email:
                u.setdefault("reservations", []).append(res_id)
                break

    #--- tool main entry point ---
    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_email: str,
        flight_details: list[dict[str, str]],
        passengers: list[dict[str, str]],
        cabin: str,
    ) -> str:
        users = data.get("users", [])
        reservations = data.get("reservations", [])

        # find user and generate a deterministic user_id (maintaining original logic)
        target_user = CreateReservation._find_user(users, user_email)
        if not target_user:
            payload = {"error": "User not found", "email": user_email}
            out = json.dumps(payload)
            return out

        # create the next reservation id (following the same format: RES####)
        new_res_id = CreateReservation._next_reservation_id(reservations)

        # construct reservation record (field names/values remain the same)
        new_reservation = {
            "reservation_id": new_res_id,
            "user_id": target_user["id"],
            "origin": flight_details[0]["origin"],
            "destination": flight_details[-1]["destination"],
            "flight_type": "one_way" if len(flight_details) == 1 else "round_trip",
            "cabin": cabin,
            "flights": flight_details,
            "passengers": passengers,
            "payment_history": [],
            # "created_at": datetime.now().isoformat(),
            "total_baggages": len(passengers),
            "nonfree_baggages": 0,
            "insurance": "no",
            "status": "CONFIRMED",
        }

        # store in the supplied data dictionary
        reservations.append(new_reservation)
        CreateReservation._attach_reservation_to_user(users, user_email, new_res_id)
        payload = new_reservation
        out = json.dumps(payload)
        return out
        

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateReservation",
                "description": "Creates a new flight reservation for a user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_email": {
                            "type": "string",
                            "description": "The email of the user making the reservation.",
                        },
                        "flight_details": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "flight_number": {"type": "string"},
                                    "date": {
                                        "type": "string",
                                        "description": "Date in YYYY-MM-DD format.",
                                    },
                                    "origin": {"type": "string"},
                                    "destination": {"type": "string"},
                                },
                                "required": [
                                    "flight_number",
                                    "date",
                                    "origin",
                                    "destination",
                                ],
                            },
                        },
                        "passengers": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "first_name": {"type": "string"},
                                    "last_name": {"type": "string"},
                                    "dob": {
                                        "type": "string",
                                        "description": "Date of birth in YYYY-MM-DD format.",
                                    },
                                },
                                "required": ["first_name", "last_name", "dob"],
                            },
                        },
                        "cabin": {
                            "type": "string",
                            "description": "The cabin class (e.g., 'economy', 'business', 'basic_economy').",
                        },
                    },
                    "required": ["user_email", "flight_details", "passengers", "cabin"],
                },
            },
        }


class FindUserByEmail(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], user_email: str) -> str:
        users: list[dict[str, Any]] = data.get("users", [])
        for u in users:
            if u.get("email") == user_email:
                first = (u.get("name", {}).get("first_name") or "").lower()
                last = (u.get("name", {}).get("last_name") or "").lower()
                payload = {
                    "email": user_email,
                    "name": first,
                    "last": last,
                    "dob": u.get("dob"),
                }
                out = json.dumps(payload)
                return out
        payload = {"error": "User not found", "email": user_email}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindUserByEmail",
                "description": "Find an existing user by email and return a deterministic user_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_email": {
                            "type": "string",
                            "description": "Email of the user to look up.",
                        }
                    },
                    "required": ["user_email"],
                },
            },
        }


class UpdateFlightScheduledTimes(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        flight_number: str,
        scheduled_departure_time_est: str | None = None,
        scheduled_arrival_time_est: str | None = None,
    ) -> str:
        pass
        for f in data.get("flights", []):
            if f.get("flight_number") != flight_number:
                continue
            #update solely the fields that are supplied
            if scheduled_departure_time_est is not None:
                f["scheduled_departure_time_est"] = scheduled_departure_time_est
            if scheduled_arrival_time_est is not None:
                f["scheduled_arrival_time_est"] = scheduled_arrival_time_est
            return _j(
                {
                    "flight_number": flight_number,
                    "scheduled_departure_time_est": f.get(
                        "scheduled_departure_time_est"
                    ),
                    "scheduled_arrival_time_est": f.get("scheduled_arrival_time_est"),
                }
            )
        return _j({"error": "flight_not_found", "flight_number": flight_number})

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateFlightScheduledTimes",
                "description": "Update the estimated scheduled departure/arrival times for a flight (top-level schedule fields).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {"type": "string"},
                        "scheduled_departure_time_est": {
                            "type": "string",
                            "description": "Time-only (24-hour): HH:MM:SS",
                        },
                        "scheduled_arrival_time_est": {
                            "type": "string",
                            "description": "Time-only (24-hour): HH:MM:SS",
                        },
                    },
                    "required": ["flight_number"],
                },
            },
        }


TOOLS = [
    GetAirportByCode(),
    GetAircraftByTail(),
    GetAircraftByAirport(),
    LookupFlightDay(),
    ScanFlightsByDate(),
    FindReservationsByUser(),
    FindReservationsByFlightDay(),
    GetCrewMemberByEmployeeCode(),
    GetCrewAssignments(),
    GetCrewCertifications(),
    EventsAtAirportOn(),
    MaintenanceLogsForAircraft(),
    MaintenanceLogs(),
    ComputeCrewDutyCounts(),
    CreateOperationalEvent(),
    SetAircraftStatus(),
    RelocateAircraft(),
    AppendMaintenanceLog(),
    UpdateCrewMemberStatus(),
    CreateCrewAssignment(),
    UpdateFlightStatusForDate(),
    UpdateFlightScheduledTimes(),
    GetFlightScheduledTimes(),
    DelayFlightActualTimesForDate(),
    CancelReservation(),
    RefundReservationsByFlightDay(),
    RefundReservation(),
    SendUserNotification(),
    FindAvailableCrew(),
    UpdateReservationStatus(),
    UpdateReservationDetails(),
    FindFlights(),
    CreateReservation(),
    FindUserByEmail(),
]
