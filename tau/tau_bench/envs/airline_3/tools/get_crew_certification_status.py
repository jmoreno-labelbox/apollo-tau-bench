from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetCrewCertificationStatus(Tool):
    """
    API tool for retrieving crew member certification status and expiration details.
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        crew_id: str = None,
        crew_member_id: str = None,
        certification_type: str = None,
        expiry_threshold_days: int = 90,
    ) -> str:
        pass
        from datetime import datetime, timedelta
        import json

        crew_certifications = data.get("crew_certifications", {}).values()
        crew_members = data.get("crew_members", {}).values()
        filtered_certifications = []

        # Establish a default expiry threshold if none is given
        if expiry_threshold_days is None:
            expiry_threshold_days = 90

        # Manage both crew_id and crew_member_id parameters
        target_crew_id = crew_id or crew_member_id

        today = datetime.now().date()
        threshold_date = today + timedelta(days=expiry_threshold_days)

        for cert in crew_certifications.values():
            # Implement filters
            if (
                target_crew_id
                and cert.get("crew_member", {}).values().get("crew_member_id") != target_crew_id
            ):
                continue
            if (
                certification_type
                and cert.get("certification", {}).values().get("certification_code")
                != certification_type
            ):
                continue

            # Retrieve details about the crew member
            crew_member_id = cert.get("crew_member", {}).values().get("crew_member_id")
            crew_details = None
            for crew in crew_members.values():
                if crew.get("crew_member_id") == crew_member_id:
                    crew_details = crew
                    break

            # Determine certification status
            expiry_date = cert.get("expiry_date")
            if expiry_date:
                try:
                    expiry_date_obj = datetime.strptime(expiry_date, "%Y-%m-%d").date()
                    days_until_expiry = (expiry_date_obj - today).days

                    if expiry_date_obj < today:
                        status = "expired"
                        days_until_expiry = abs(days_until_expiry)
                    elif expiry_date_obj <= threshold_date:
                        status = "expiring_soon"
                    else:
                        status = "valid"
                except ValueError:
                    status = "unknown"
                    days_until_expiry = None
            else:
                status = "no_expiry"
                days_until_expiry = None

            cert_info = {
                "certification_id": cert.get("crew_certification_id"),
                "crew_id": crew_member_id,
                "crew_name": cert.get("crew_member", {}).values().get("full_name"),
                "crew_role": crew_details.get("role") if crew_details else None,
                "certification_type": cert.get("certification", {}).values().get(
                    "certification_code"
                ),
                "issue_date": cert.get("issue_date"),
                "expiry_date": expiry_date,
                "status": status,
                "days_until_expiry": days_until_expiry,
            }

            filtered_data["certifications"][certification_id] = cert_info

        # Arrange by status priority and expiry date
        status_priority = {
            "expired": 1,
            "expiring_soon": 2,
            "valid": 3,
            "no_expiry": 4,
            "unknown": 5,
        }
        filtered_certifications.sort(
            key=lambda x: (
                status_priority.get(x["status"], 6),
                (
                    x["days_until_expiry"]
                    if x["days_until_expiry"] is not None
                    else float("inf")
                ),
            )
        )

        # Determine summary statistics
        total_certifications = len(filtered_certifications)
        status_counts = {}
        type_counts = {}
        expiring_soon_count = 0
        expired_count = 0

        for cert in filtered_certifications:
            status_counts[cert["status"]] = status_counts.get(cert["status"], 0) + 1
            type_counts[cert["certification_type"]] = (
                type_counts.get(cert["certification_type"], 0) + 1
            )

            if cert["status"] == "expiring_soon":
                expiring_soon_count += 1
            elif cert["status"] == "expired":
                expired_count += 1

        response = {
            "filters_applied": {
                "crew_id": target_crew_id,
                "crew_member_id": crew_member_id,
                "certification_type": certification_type,
                "expiry_threshold_days": expiry_threshold_days,
            },
            "summary": {
                "total_certifications_found": total_certifications,
                "status_breakdown": status_counts,
                "certification_type_breakdown": type_counts,
                "expiring_soon_count": expiring_soon_count,
                "expired_count": expired_count,
            },
            "certifications": filtered_certifications,
        }

        # Include notifications for essential certifications
        if expired_count > 0 or expiring_soon_count > 0:
            response["alerts"] = {}
            if expired_count > 0:
                response["alerts"]["expired_certifications"] = expired_count
            if expiring_soon_count > 0:
                response["alerts"]["expiring_soon_certifications"] = expiring_soon_count

        # Include suggestions if no specific filters are applied
        if not any([target_crew_id, certification_type]) and total_certifications > 0:
            if expired_count > 0:
                response["recommendations"] = {
                    "priority": "high",
                    "message": f"Immediate attention required: {expired_count} expired certification(s) need renewal",
                }
            elif expiring_soon_count > 0:
                response["recommendations"] = {
                    "priority": "medium",
                    "message": f"Plan renewals: {expiring_soon_count} certification(s) expiring within {expiry_threshold_days} days",
                }
        payload = response
        out = json.dumps(payload, indent=2)
        return out
    
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCrewCertificationStatus",
                "description": "Get crew member certification status and expiry information with filtering options. Provides overview of certification validity, expiring soon alerts, and compliance status. Critical for regulatory compliance and operational safety.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "crew_id": {
                            "type": "string",
                            "description": "Optional crew member identifier to get specific crew certifications. Format: CM followed by 3-digit number.",
                        },
                        "crew_member_id": {
                            "type": "string",
                            "description": "Alternative parameter name for crew_id. Format: CM followed by 3-digit number.",
                        },
                        "certification_type": {
                            "type": "string",
                            "description": "Optional certification type filter. Aircraft-specific certifications are required for specific aircraft models.",
                        },
                        "expiry_threshold_days": {
                            "type": "integer",
                            "description": "Number of days to consider certifications as 'expiring soon' (default: 90 days). Values: 30, 60, 90, 120. Used for proactive renewal planning.",
                        },
                    },
                    "required": [],
                },
            },
        }
