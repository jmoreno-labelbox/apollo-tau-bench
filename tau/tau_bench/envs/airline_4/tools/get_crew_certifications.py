# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool










def _to_iso_day(v):
    if v in (None, "", "null"):
        return "9999-12-31"
    s = str(v)
    # Try strict ISO parse (accepts full ISO datetimes too)
    try:
        return datetime.fromisoformat(s).date().isoformat()
    except Exception:
        # Fallback: first 10 chars, if they form a valid YYYY-MM-DD
        day = s[:10]
        try:
            _date.fromisoformat(day)
            return day
        except Exception:
            return "9999-12-31"

def _json(data: Any) -> str:
    return json.dumps(data, indent=2, sort_keys=True, default=str)

def _get_cert_by_code(data: Dict[str, Any], code: str) -> Optional[Dict[str, Any]]:
    target = _norm(code)
    for c in data.get("certifications", []):
        c_code = _norm(c.get("certification_code"))
        if c_code == target:
            return c
    # fallback: try common alias field names if present (no-ops if absent)
    for c in data.get("certifications", []):
        # sometimes datasets have 'model_id' or 'code'
        for alt_key in ("model_id", "code", "name", "model"):
            if _norm(c.get(alt_key)) == target:
                return c
    return None

def _find_crew_member(data: Dict[str, Any], crew_member_id: str) -> Optional[Dict[str, Any]]:
    target = _norm(crew_member_id)
    for cm in data.get("crew_members", []):
        if _norm(cm.get("crew_member_id")) == target:
            return cm
    return None

class GetCrewCertifications(Tool):
    """
    Read-only lookup of a crew member's certifications with optional filters.

    Filtering:
      • certification_code (exact match against canonical code in data['certifications'])
      • active_on (YYYY-MM-DD): returns records whose [issue_date .. expiry_date] covers this day.
        - expiry_date None/''/'null' is treated as open-ended.
      • include_history: if True with active_on, include both active and inactive; if False, only active.

    Deterministic:
      • Output is sorted by (certification_code, issue_date ASC).
      • No writes; stable formatting/keys.
    """

    @staticmethod
    def _is_active_on(issue_date: Optional[str], expiry_date: Optional[str], day: str) -> bool:
        # Treat None/''/'null' as flexible; all dates are inherently in ISO format due to the upsert design.
        from datetime import date
        d = date.fromisoformat(day)
        start = date.fromisoformat(issue_date) if issue_date else date.min
        end = date.max if expiry_date in (None, "", "null") else date.fromisoformat(expiry_date)
        return start <= d <= end

    @staticmethod
    def invoke(
        data: Dict[str, Any], *,
        crew_member_id: str,
        certification_code: Optional[str] = None,
        active_on: Optional[str] = None,
        include_history: bool = False,
    ) -> str:
        # Verify crew members.
        if not crew_member_id:
            return _json({"error": "missing_params", "reason": "crew_member_id is required"})
        crew = _find_crew_member(data, crew_member_id)
        if not crew:
            return _json({"error": "crew_member_not_found", "crew_member_id": crew_member_id})

        # Translate the certification_code (if available) to its standard form in the master list.
        resolved_code = None
        if certification_code:
            cert = _get_cert_by_code(data, certification_code)
            if not cert:
                return _json({"error": "certification_not_found", "certification_code": certification_code})
            resolved_code = cert.get("certification_code")

        # Standardize active_on if it is supplied.
        day = None
        if active_on not in (None, "", "null"):
            try:
                # enforce strict ISO; allow full ISO datetime through a helper if needed
                day = _to_iso_day(active_on)
                from datetime import date as _date
                _date.fromisoformat(day)
            except Exception:
                return _json({"error": "invalid_date_format", "reason": "active_on must be YYYY-MM-DD"})

        # Aggregate and refine
        rows = []
        for cc in data.get("crew_certifications", []):
            cm = (cc.get("crew_member") or {}).get("crew_member_id")
            cert = (cc.get("certification") or {})
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

            rows.append({
                "crew_certification_id": cc.get("crew_certification_id"),
                "crew_member_id": crew_member_id,
                "certification_code": code,
                "issue_date": i_date,
                "expiry_date": e_date,
                "active_on": active_flag,  # Returns None if active_on is absent.
            })

        # Predictable sorting
        rows.sort(key=lambda r: ((r.get("certification_code") or ""), (r.get("issue_date") or "")))

        return _json({
            "success": True,
            "crew_member_id": crew_member_id,
            "certification_code_filter": resolved_code,
            "active_on": day,
            "include_history": include_history,
            "count": len(rows),
            "results": rows
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_crew_certifications",
                "description": (
                    "List certifications for a crew member with optional filters: certification_code, "
                    "active_on (YYYY-MM-DD), include_history. Read-only, deterministic, sorted."
                ),
                "parameters": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "crew_member_id": {"type": "string", "description": "e.g. CM001"},
                        "certification_code": {"type": "string", "description": "Filter to a specific code (e.g. A320neo)"},
                        "active_on": {"type": "string", "description": "YYYY-MM-DD; return records active on this date"},
                        "include_history": {"type": "boolean", "description": "When active_on is given, include inactive too", "default": False}
                    },
                    "required": ["crew_member_id"]
                }
            }
        }