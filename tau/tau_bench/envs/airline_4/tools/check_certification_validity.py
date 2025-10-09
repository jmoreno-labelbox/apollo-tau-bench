from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CheckCertificationValidity(Tool):
    """API tool for verifying the validity of a certification for a crew member."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        crew_certification_id: str | None = None,
        crew_member_id: str | None = None,
        certification_id: str | None = None,
        check_date: str | None = None,
    ) -> str:
        pass
        from datetime import date, datetime

        #Check the validity of input parameters
        if crew_certification_id:
            #Approach 1: Direct lookup of certification ID
            search_method = "certification_id"
            search_criteria = {"crew_certification_id": crew_certification_id}
        elif crew_member_id and certification_id:
            #Approach 2: Lookup of crew member and certification
            search_method = "crew_and_cert"
            search_criteria = {
                "crew_member_id": crew_member_id,
                "certification_id": certification_id,
            }
        else:
            payload = {
                    "error": "Invalid parameters",
                    "required": "Either 'crew_certification_id' OR both 'crew_member_id' and 'certification_id' must be provided",
                }
            out = json.dumps(
                payload)
            return out

        #Analyze the check date (defaulting to today)
        if check_date:
            try:
                check_date_obj = datetime.strptime(check_date, "%Y-%m-%d").date()
            except ValueError:
                payload = {
                        "error": "Invalid check_date format. Expected YYYY-MM-DD",
                        "received": check_date,
                    }
                out = json.dumps(
                    payload)
                return out
        else:
            check_date_obj = date.today()
            check_date = check_date_obj.strftime("%Y-%m-%d")

        #Locate the certification record
        crew_certifications = data.get("crew_certifications", [])
        target_certification = None

        for cert in crew_certifications:
            if search_method == "certification_id":
                if cert.get("crew_certification_id") == crew_certification_id:
                    target_certification = cert
                    break
            elif search_method == "crew_and_cert":
                crew_info = cert.get("crew_member", {})
                cert_info = cert.get("certification", {})
                if (
                    crew_info.get("crew_member_id") == crew_member_id
                    and cert_info.get("certification_id") == certification_id
                ):
                    target_certification = cert
                    break

        if not target_certification:
            payload = {
                    "error": "Certification record not found",
                    "search_criteria": search_criteria,
                }
            out = json.dumps(
                payload)
            return out

        #Obtain details of the certification
        issue_date_str = target_certification.get("issue_date")
        expiry_date_str = target_certification.get("expiry_date")
        crew_info = target_certification.get("crew_member", {})
        cert_info = target_certification.get("certification", {})

        #Analyze dates
        try:
            issue_date = (
                datetime.strptime(issue_date_str, "%Y-%m-%d").date()
                if issue_date_str
                else None
            )
        except ValueError:
            issue_date = None

        try:
            expiry_date = (
                datetime.strptime(expiry_date_str, "%Y-%m-%d").date()
                if expiry_date_str
                else None
            )
        except ValueError:
            expiry_date = None

        #Assess the validity status
        is_valid = True
        status = "Valid"
        reasons = []

        #Verify if issued prior to the check date
        if issue_date and check_date_obj < issue_date:
            is_valid = False
            status = "Not Yet Valid"
            reasons.append(f"Certification not issued until {issue_date}")

        #Verify if expired
        if expiry_date and check_date_obj > expiry_date:
            is_valid = False
            status = "Expired"
            reasons.append(f"Certification expired on {expiry_date}")

        #Compute the number of days until or since expiry
        days_info = None
        if expiry_date:
            days_diff = (expiry_date - check_date_obj).days
            if days_diff > 0:
                days_info = f"Expires in {days_diff} days"
            elif days_diff == 0:
                days_info = "Expires today"
            else:
                days_info = f"Expired {abs(days_diff)} days ago"
        else:
            days_info = "No expiry date (permanent certification)"

        #Retrieve complete certification details
        certifications = data.get("certifications", [])
        certification_details = None
        for cert_detail in certifications:
            if cert_detail.get("certification_id") == cert_info.get("certification_id"):
                certification_details = cert_detail
                break

        #Formulate response
        response = {
            "certification_record": {
                "crew_certification_id": target_certification.get(
                    "crew_certification_id"
                ),
                "crew_member": crew_info,
                "certification": cert_info,
                "issue_date": issue_date_str,
                "expiry_date": expiry_date_str,
            },
            "validity_check": {
                "check_date": check_date,
                "is_valid": is_valid,
                "status": status,
                "reasons": reasons if reasons else ["Certification is valid"],
                "days_info": days_info,
            },
        }

        #Include complete certification details if located
        if certification_details:
            response["certification_details"] = certification_details
        payload = response
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CheckCertificationValidity",
                "description": "Check if a crew member's certification is valid on a specific date. Can search by certification ID directly or by crew member and certification combination.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "crew_certification_id": {
                            "type": "string",
                            "description": "Direct certification record ID (e.g., 'CC001'). Use this for direct lookup.",
                        },
                        "crew_member_id": {
                            "type": "string",
                            "description": "Crew member ID (e.g., 'CM001'). Must be used with certification_id.",
                        },
                        "certification_id": {
                            "type": "string",
                            "description": "Certification ID (e.g., 'CERT_ATPL'). Must be used with crew_member_id.",
                        },
                        "check_date": {
                            "type": "string",
                            "description": "Date to check validity against in YYYY-MM-DD format. Defaults to current date if not provided.",
                        },
                    },
                    "required": [],
                },
            },
        }
