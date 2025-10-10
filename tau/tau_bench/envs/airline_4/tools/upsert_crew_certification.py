from __future__ import annotations
from tau_bench.envs.tool import Tool
import json
from datetime import date, datetime, timedelta  #required for fallback window enlargement
from decimal import ROUND_HALF_UP, Decimal
from typing import Any
import re
from datetime import date as _date

class UpsertCrewCertification(Tool):
    """
    Create or modify a crew member's certification with validation and predictable IDs/audit.
    """

    @staticmethod
    def _normalize_date_str(d):
        """Standardize incoming date-like values to ISO 'YYYY-MM-DD' or None (accepts None, '', 'null')."""
        pass
        if d in (None, "", "null"):
            return None
        date.fromisoformat(d)  #throws an error if invalid
        return d

    @staticmethod
    def _overlaps(a_start, a_end, b_start, b_end):
        """Inclusive day-level overlap; None/''/'null' expiry is considered open-ended."""
        pass
        a_s = date.fromisoformat(a_start)
        a_e = date.max if a_end in (None, "", "null") else date.fromisoformat(a_end)
        b_s = date.fromisoformat(b_start)
        b_e = date.max if b_end in (None, "", "null") else date.fromisoformat(b_end)
        return not (a_e < b_s or b_e < a_s)

    @staticmethod
    def invoke(
        data: dict[str, Any],
        *,
        crew_member_id: str,
        certification_code: str | None = None,
        certification_id: str | None = None,
        issue_date: str,
        expiry_date: str | None = None,
        upsert_strategy: str = "create_new",
        reason: str | None = None
    ) -> str:
        pass
        cert_id = certification_id
        strategy = upsert_strategy

        #check crew for validity
        if not crew_member_id:
            return _json(
                {"error": "missing_params", "reason": "crew_member_id is required"}
            )
        crew = _find_crew_member(data, crew_member_id)
        if not crew:
            return _json(
                {"error": "crew_member_not_found", "crew_member_id": crew_member_id}
            )

        #precisely one of code or id
        if bool(certification_code) == bool(cert_id):
            return _json(
                {
                    "error": "invalid_params",
                    "reason": "Provide exactly one of certification_code or certification_id.",
                }
            )

        #determine certification
        cert = (
            _get_cert_by_code(data, certification_code)
            if certification_code
            else _get_cert_by_id(data, cert_id)
        )
        if not cert:
            return _json(
                {
                    "error": "certification_not_found",
                    "certification_code": certification_code,
                    "certification_id": cert_id,
                }
            )

        resolved_code = cert.get("certification_code")
        resolved_id = cert.get("certification_id")

        #standardize and verify strategy
        strategy = (
            strategy.strip().lower() if isinstance(strategy, str) else "create_new"
        )
        if strategy not in ("create_new", "replace_if_overlap"):
            return _json(
                {
                    "error": "invalid_params",
                    "reason": "upsert_strategy must be 'create_new' or 'replace_if_overlap'.",
                }
            )

        #date verification and standardization
        if not issue_date:
            return _json(
                {"error": "missing_params", "reason": "issue_date is required"}
            )
        try:
            issue_date = UpsertCrewCertification._normalize_date_str(issue_date)
            expiry_date = UpsertCrewCertification._normalize_date_str(expiry_date)
        except Exception:
            return _json(
                {
                    "error": "invalid_date_format",
                    "reason": "Dates must be YYYY-MM-DD or null",
                }
            )

        #groups
        existing_list = data.setdefault("crew_certifications", [])
        audits = data.setdefault("crew_cert_audits", [])

        #correspondences for this crew and cert_code
        matches = [
            cc
            for cc in existing_list
            if ((cc.get("crew_member") or {}).get("crew_member_id") == crew_member_id)
            and (
                (cc.get("certification") or {}).get("certification_code")
                == resolved_code
            )
        ]

        #predictable IDs
        det_cc_id = f"CC-{crew_member_id}-{resolved_code}-{issue_date}"
        audit_id = f"CA-{crew_member_id}-{issue_date}"

        def _make_record():
            pass
            return {
                "crew_certification_id": det_cc_id,
                "crew_member": {
                    "crew_member_id": crew_member_id,
                    "employee_code": crew.get("employee_code"),
                    "full_name": (
                        crew.get("first_name", "") + " " + crew.get("last_name", "")
                    ).strip(),
                },
                "certification": {
                    "certification_id": resolved_id,
                    "certification_code": resolved_code,
                },
                "issue_date": issue_date,
                "expiry_date": expiry_date,
            }

        existing_by_id = next(
            (
                cc
                for cc in existing_list
                if cc.get("crew_certification_id") == det_cc_id
            ),
            None,
        )

        if matches:
            overlapping = None
            for cc in matches:
                if UpsertCrewCertification._overlaps(
                    cc.get("issue_date"), cc.get("expiry_date"), issue_date, expiry_date
                ):
                    overlapping = cc
                    break

            if overlapping and strategy == "replace_if_overlap":
                overlapping["certification"] = {
                    "certification_id": resolved_id,
                    "certification_code": resolved_code,
                }
                overlapping["issue_date"] = issue_date
                overlapping["expiry_date"] = expiry_date
                overlapping["crew_certification_id"] = det_cc_id
                new_cc_id = det_cc_id
                action = "replaced"
            else:
                if existing_by_id:
                    new_cc_id = det_cc_id
                    action = "noop_exists"
                else:
                    existing_list.append(_make_record())
                    new_cc_id = det_cc_id
                    action = "created"
        else:
            if existing_by_id:
                new_cc_id = det_cc_id
                action = "noop_exists"
            else:
                existing_list.append(_make_record())
                new_cc_id = det_cc_id
                action = "created"

        #predictable audit (prevent duplicate audits with the same id)
        if not any(a.get("id") == audit_id for a in audits.values()):
            audits.append(
                {
                    "id": audit_id,
                    "type": "UpsertCrewCertification",
                    "crew_member_id": crew_member_id,
                    "certification_code": resolved_code,
                    "issue_date": issue_date,
                    "expiry_date": expiry_date,
                    "strategy": strategy,
                    "reason": reason,
                }
            )

        return _json(
            {
                "success": True,
                "action": action,
                "crew_certification_id": new_cc_id,
                "crew_member_id": crew_member_id,
                "certification_code": resolved_code,
                "issue_date": issue_date,
                "expiry_date": expiry_date,
                "audit_id": audit_id,
            }
        )
        pass
        cert_id = certification_id
        strategy = upsert_strategy

        #check crew for validity
        if not crew_member_id:
            return _json(
                {"error": "missing_params", "reason": "crew_member_id is required"}
            )
        crew = _find_crew_member(data, crew_member_id)
        if not crew:
            return _json(
                {"error": "crew_member_not_found", "crew_member_id": crew_member_id}
            )

        #precisely one of code or id
        if bool(certification_code) == bool(cert_id):
            return _json(
                {
                    "error": "invalid_params",
                    "reason": "Provide exactly one of certification_code or certification_id.",
                }
            )

        #determine certification
        cert = (
            _get_cert_by_code(data, certification_code)
            if certification_code
            else _get_cert_by_id(data, cert_id)
        )
        if not cert:
            return _json(
                {
                    "error": "certification_not_found",
                    "certification_code": certification_code,
                    "certification_id": cert_id,
                }
            )

        resolved_code = cert.get("certification_code")
        resolved_id = cert.get("certification_id")

        #standardize and verify strategy
        strategy = (
            strategy.strip().lower() if isinstance(strategy, str) else "create_new"
        )
        if strategy not in ("create_new", "replace_if_overlap"):
            return _json(
                {
                    "error": "invalid_params",
                    "reason": "upsert_strategy must be 'create_new' or 'replace_if_overlap'.",
                }
            )

        #date verification and standardization
        if not issue_date:
            return _json(
                {"error": "missing_params", "reason": "issue_date is required"}
            )
        try:
            issue_date = UpsertCrewCertification._normalize_date_str(issue_date)
            expiry_date = UpsertCrewCertification._normalize_date_str(expiry_date)
        except Exception:
            return _json(
                {
                    "error": "invalid_date_format",
                    "reason": "Dates must be YYYY-MM-DD or null",
                }
            )

        #groups
        existing_list = data.setdefault("crew_certifications", [])
        audits = data.setdefault("crew_cert_audits", [])

        #correspondences for this crew and cert_code
        matches = [
            cc
            for cc in existing_list
            if ((cc.get("crew_member") or {}).get("crew_member_id") == crew_member_id)
            and (
                (cc.get("certification") or {}).get("certification_code")
                == resolved_code
            )
        ]

        #predictable IDs
        det_cc_id = f"CC-{crew_member_id}-{resolved_code}-{issue_date}"
        audit_id = f"CA-{crew_member_id}-{issue_date}"

        def _make_record():
            pass
            return {
                "crew_certification_id": det_cc_id,
                "crew_member": {
                    "crew_member_id": crew_member_id,
                    "employee_code": crew.get("employee_code"),
                    "full_name": (
                        crew.get("first_name", "") + " " + crew.get("last_name", "")
                    ).strip(),
                },
                "certification": {
                    "certification_id": resolved_id,
                    "certification_code": resolved_code,
                },
                "issue_date": issue_date,
                "expiry_date": expiry_date,
            }

        existing_by_id = next(
            (
                cc
                for cc in existing_list
                if cc.get("crew_certification_id") == det_cc_id
            ),
            None,
        )

        if matches:
            overlapping = None
            for cc in matches:
                if UpsertCrewCertification._overlaps(
                    cc.get("issue_date"), cc.get("expiry_date"), issue_date, expiry_date
                ):
                    overlapping = cc
                    break

            if overlapping and strategy == "replace_if_overlap":
                overlapping["certification"] = {
                    "certification_id": resolved_id,
                    "certification_code": resolved_code,
                }
                overlapping["issue_date"] = issue_date
                overlapping["expiry_date"] = expiry_date
                overlapping["crew_certification_id"] = det_cc_id
                new_cc_id = det_cc_id
                action = "replaced"
            else:
                if existing_by_id:
                    new_cc_id = det_cc_id
                    action = "noop_exists"
                else:
                    existing_list.append(_make_record())
                    new_cc_id = det_cc_id
                    action = "created"
        else:
            if existing_by_id:
                new_cc_id = det_cc_id
                action = "noop_exists"
            else:
                existing_list.append(_make_record())
                new_cc_id = det_cc_id
                action = "created"

        #predictable audit (prevent duplicate audits with the same id)
        if not any(a.get("id") == audit_id for a in audits.values()):
            audits.append(
                {
                    "id": audit_id,
                    "type": "UpsertCrewCertification",
                    "crew_member_id": crew_member_id,
                    "certification_code": resolved_code,
                    "issue_date": issue_date,
                    "expiry_date": expiry_date,
                    "strategy": strategy,
                    "reason": reason,
                }
            )

        return _json(
            {
                "success": True,
                "action": action,
                "crew_certification_id": new_cc_id,
                "crew_member_id": crew_member_id,
                "certification_code": resolved_code,
                "issue_date": issue_date,
                "expiry_date": expiry_date,
                "audit_id": audit_id,
            }
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpsertCrewCertification",
                "description": (
                    "Create or update a crew member's certification with overlap handling and deterministic IDs. "
                    "crew_certification_id = 'CC-{crew_member_id}-{certification_code}-{issue_date}', "
                    "audit_id = 'CA-{crew_member_id}-{issue_date}'. Dates are ISO (YYYY-MM-DD) or null."
                ),
                "parameters": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "crew_member_id": {
                            "type": "string",
                            "description": "Crew member ID, e.g., CM001",
                        },
                        "certification_code": {
                            "type": "string",
                            "description": "e.g., B737-800, A320neo",
                        },
                        "certification_id": {
                            "type": "string",
                            "description": "e.g., CERT_B738",
                        },
                        "issue_date": {"type": "string", "description": "YYYY-MM-DD"},
                        "expiry_date": {
                            "type": ["string", "null"],
                            "description": "YYYY-MM-DD or null",
                        },
                        "upsert_strategy": {
                            "type": "string",
                            "enum": ["create_new", "replace_if_overlap"],
                            "default": "create_new",
                        },
                        "reason": {
                            "type": "string",
                            "description": "Audit text (optional)",
                        },
                    },
},
            },
        }
