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

class GetCrewCertifications(Tool):
    """
    Read-only access to a crew member's certifications with optional filters.

    Filtering:
      • certification_code (exact match against the standard code in data['certifications'])
      • active_on (YYYY-MM-DD): returns records whose [issue_date .. expiry_date] encompasses this day.
        - expiry_date None/''/'null' is considered open-ended.
      • include_history: if True with active_on, include both active and inactive; if False, only active.

    Predictable:
      • Output is sorted by (certification_code, issue_date ASC).
      • No modifications; consistent formatting/keys.
    """

    @staticmethod
    def _is_active_on(
        issue_date: str | None, expiry_date: str | None, day: str
    ) -> bool:
        pass
        #Accept None/''/'null' as indefinite; all dates are ISO by the nature of upsert.
        from datetime import date

        d = date.fromisoformat(day)
        start = date.fromisoformat(issue_date) if issue_date else date.min
        end = (
            date.max
            if expiry_date in (None, "", "null")
            else date.fromisoformat(expiry_date)
        )
        return start <= d <= end

    @staticmethod
    def invoke(
        data: dict[str, Any],
        *,
        crew_member_id: str,
        certification_code: str | None = None,
        active_on: str | None = None,
        include_history: bool = False
    ) -> str:
        # Check crew for validity
        if not crew_member_id:
            return _json(
                {"error": "missing_params", "reason": "crew_member_id is required"}
            )
        crew = _find_crew_member(data, crew_member_id)
        if not crew:
            return _json(
                {"error": "crew_member_not_found", "crew_member_id": crew_member_id}
            )

        # Translate certification_code (if given) to the standard one in the master list
        resolved_code = None
        if certification_code:
            cert = _get_cert_by_code(data, certification_code)
            if not cert:
                return _json(
                    {
                        "error": "certification_not_found",
                        "certification_code": certification_code,
                    }
                )
            resolved_code = cert.get("certification_code")

        # Standardize active_on if supplied
        day = None
        if active_on not in (None, "", "null"):
            try:
                # strict ISO; accept complete ISO datetime by utilizing a helper if needed
                day = _to_iso_day(active_on)
                from datetime import date as _date

                _date.fromisoformat(day)
            except Exception:
                return _json(
                    {
                        "error": "invalid_date_format",
                        "reason": "active_on must be YYYY-MM-DD",
                    }
                )

        # Gather and filter
        rows = []
        for cc in data.get("crew_certifications", {}).values():
            cm = (cc.get("crew_member") or {}).get("crew_member_id")
            cert = cc.get("certification") or {}
            code = cert.get("certification_code")

            if cm != crew_member_id:
                continue
            if resolved_code and code != resolved_code:
                continue

            i_date = cc.get("issue_date")
            e_date = cc.get("expiry_date")

            # Implement active_on filter
            active_flag = None
            if day:
                active_flag = GetCrewCertifications._is_active_on(i_date, e_date, day)
                if not active_flag and not include_history:
                    continue

            rows.append(
                {
                    "crew_certification_id": cc.get("crew_certification_id"),
                    "crew_member_id": crew_member_id,
                    "certification_code": code,
                    "issue_date": i_date,
                    "expiry_date": e_date,
                    "active_on": active_flag,  # None if active_on is not supplied
                }
            )

        # Predictable sorting
        rows.sort(
            key=lambda r: (
                (r.get("certification_code") or ""),
                (r.get("issue_date") or ""),
            )
        )

        return _json(
            {
                "success": True,
                "crew_member_id": crew_member_id,
                "certification_code_filter": resolved_code,
                "active_on": day,
                "include_history": include_history,
                "count": len(rows),
                "results": rows,
            }
        )
        pass
        #Check crew for validity
        if not crew_member_id:
            return _json(
                {"error": "missing_params", "reason": "crew_member_id is required"}
            )
        crew = _find_crew_member(data, crew_member_id)
        if not crew:
            return _json(
                {"error": "crew_member_not_found", "crew_member_id": crew_member_id}
            )

        #Translate certification_code (if given) to the standard one in the master list
        resolved_code = None
        if certification_code:
            cert = _get_cert_by_code(data, certification_code)
            if not cert:
                return _json(
                    {
                        "error": "certification_not_found",
                        "certification_code": certification_code,
                    }
                )
            resolved_code = cert.get("certification_code")

        #Standardize active_on if supplied
        day = None
        if active_on not in (None, "", "null"):
            try:
                #strict ISO; accept complete ISO datetime by utilizing a helper if needed
                day = _to_iso_day(active_on)
                from datetime import date as _date

                _date.fromisoformat(day)
            except Exception:
                return _json(
                    {
                        "error": "invalid_date_format",
                        "reason": "active_on must be YYYY-MM-DD",
                    }
                )

        #Gather and filter
        rows = []
        for cc in data.get("crew_certifications", {}).values():
            cm = (cc.get("crew_member") or {}).get("crew_member_id")
            cert = cc.get("certification") or {}
            code = cert.get("certification_code")

            if cm != crew_member_id:
                continue
            if resolved_code and code != resolved_code:
                continue

            i_date = cc.get("issue_date")
            e_date = cc.get("expiry_date")

            #Implement active_on filter
            active_flag = None
            if day:
                active_flag = GetCrewCertifications._is_active_on(i_date, e_date, day)
                if not active_flag and not include_history:
                    continue

            rows.append(
                {
                    "crew_certification_id": cc.get("crew_certification_id"),
                    "crew_member_id": crew_member_id,
                    "certification_code": code,
                    "issue_date": i_date,
                    "expiry_date": e_date,
                    "active_on": active_flag,  #None if active_on is not supplied
                }
            )

        #Predictable sorting
        rows.sort(
            key=lambda r: (
                (r.get("certification_code") or ""),
                (r.get("issue_date") or ""),
            )
        )

        return _json(
            {
                "success": True,
                "crew_member_id": crew_member_id,
                "certification_code_filter": resolved_code,
                "active_on": day,
                "include_history": include_history,
                "count": len(rows),
                "results": rows,
            }
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCrewCertifications",
                "description": (
                    "List certifications for a crew member with optional filters: certification_code, "
                    "active_on (YYYY-MM-DD), include_history. Read-only, deterministic, sorted."
                ),
                "parameters": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "crew_member_id": {
                            "type": "string",
                            "description": "e.g. CM001",
                        },
                        "certification_code": {
                            "type": "string",
                            "description": "Filter to a specific code (e.g. A320neo)",
                        },
                        "active_on": {
                            "type": "string",
                            "description": "YYYY-MM-DD; return records active on this date",
                        },
                        "include_history": {
                            "type": "boolean",
                            "description": "When active_on is given, include inactive too",
                            "default": False,
                        },
                    },
                    "required": ["crew_member_id"],
                },
            },
        }
