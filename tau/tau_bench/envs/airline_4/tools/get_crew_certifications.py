from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any

class GetCrewCertifications(Tool):
    """API tool for obtaining crew member certifications and their validity status."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        crew_member_id: str | None = None,
        employee_code: str | None = None,
    ) -> str:
        pass
        if not crew_member_id and not employee_code:
            payload = {"error": "Either crew_member_id or employee_code must be provided"}
            out = json.dumps(
                payload)
            return out

        crew_certifications = data.get("crew_certifications", [])
        crew_members = data.get("crew_members", [])

        #Confirm the crew member's existence and retrieve their information
        target_crew_member = None
        for crew_member in crew_members:
            if (
                crew_member_id and crew_member.get("crew_member_id") == crew_member_id
            ) or (employee_code and crew_member.get("employee_code") == employee_code):
                target_crew_member = crew_member
                break

        if not target_crew_member:
            search_term = crew_member_id if crew_member_id else employee_code
            search_type = "crew_member_id" if crew_member_id else "employee_code"
            payload = {"error": "Crew member not found", search_type: search_term}
            out = json.dumps(
                payload)
            return out

        #Locate all certifications associated with this crew member
        crew_member_id_to_search = target_crew_member.get("crew_member_id")
        matching_certifications = []

        for cert_record in crew_certifications:
            cert_crew_member = cert_record.get("crew_member", {})
            if cert_crew_member.get("crew_member_id") == crew_member_id_to_search:
                matching_certifications.append(cert_record)

        if not matching_certifications:
            payload = {
                    "crew_member": {
                        "crew_member_id": target_crew_member.get("crew_member_id"),
                        "employee_code": target_crew_member.get("employee_code"),
                        "full_name": f"{target_crew_member.get('first_name', '')} {target_crew_member.get('last_name', '')}".strip(),
                        "role": target_crew_member.get("role"),
                    },
                    "certifications": [],
                    "certification_summary": {
                        "total_certifications": 0,
                        "valid_certifications": 0,
                        "expired_certifications": 0,
                        "permanent_certifications": 0,
                    },
                }
            out = json.dumps(
                payload)
            return out

        #Obtain the current date for validity assessments
        from datetime import date

        current_date = date(2025, 9, 15)

        #Handle certifications and assess their validity
        processed_certifications = []
        valid_count = 0
        expired_count = 0
        permanent_count = 0

        for cert_record in matching_certifications:
            #Generate a record for processed certification
            processed_cert = dict(cert_record)  #Duplicate the original record

            #Assess the validity status
            expiry_date_str = cert_record.get("expiry_date")

            if expiry_date_str is None:
                #Absence of an expiry date indicates permanent certification
                processed_cert["validity_status"] = "permanent"
                processed_cert["is_valid"] = True
                processed_cert["days_until_expiry"] = None
                permanent_count += 1
                valid_count += 1
            else:
                #Analyze the expiry date and verify its validity
                try:
                    expiry_date = datetime.fromisoformat(expiry_date_str).date()
                    days_until_expiry = (expiry_date - current_date).days

                    if days_until_expiry > 0:
                        processed_cert["validity_status"] = "valid"
                        processed_cert["is_valid"] = True
                        processed_cert["days_until_expiry"] = days_until_expiry
                        valid_count += 1

                        #Include a warning for certifications nearing expiration
                        if days_until_expiry <= 30:
                            processed_cert["validity_status"] = "expiring_soon"
                            processed_cert["warning"] = (
                                f"Certification expires in {days_until_expiry} days"
                            )
                    else:
                        processed_cert["validity_status"] = "expired"
                        processed_cert["is_valid"] = False
                        processed_cert["days_until_expiry"] = days_until_expiry
                        processed_cert["expired_days_ago"] = abs(days_until_expiry)
                        expired_count += 1

                except ValueError:
                    #Date format is not valid
                    processed_cert["validity_status"] = "unknown"
                    processed_cert["is_valid"] = False
                    processed_cert["days_until_expiry"] = None
                    processed_cert["error"] = "Invalid expiry date format"

            processed_certifications.append(processed_cert)

        #Categorize certifications based on their validity status
        certifications_by_status = {
            "valid": [],
            "expiring_soon": [],
            "expired": [],
            "permanent": [],
        }

        for cert in processed_certifications:
            status = cert.get("validity_status", "unknown")
            if status in certifications_by_status:
                certifications_by_status[status].append(cert)

        #Formulate response
        response = {
            "crew_member": {
                "crew_member_id": target_crew_member.get("crew_member_id"),
                "employee_code": target_crew_member.get("employee_code"),
                "full_name": f"{target_crew_member.get('first_name', '')} {target_crew_member.get('last_name', '')}".strip(),
                "role": target_crew_member.get("role"),
            },
            "certification_summary": {
                "total_certifications": len(processed_certifications),
                "valid_certifications": valid_count,
                "expired_certifications": expired_count,
                "permanent_certifications": permanent_count,
            },
            "certifications_by_status": certifications_by_status,
            "all_certifications": processed_certifications,
        }
        payload = response
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCrewCertifications",
                "description": "Get crew member certifications and validity status using either crew member ID or employee code. Includes validity checks and expiry warnings.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "crew_member_id": {
                            "type": "string",
                            "description": "Crew member ID (e.g., 'CM001'). Either this or employee_code must be provided.",
                        },
                        "employee_code": {
                            "type": "string",
                            "description": "Employee code (e.g., 'EMP001'). Either this or crew_member_id must be provided.",
                        },
                    },
                    "required": [],
                },
            },
        }
