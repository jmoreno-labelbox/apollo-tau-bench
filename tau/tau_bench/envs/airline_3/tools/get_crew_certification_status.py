# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCrewCertificationStatus(Tool):
    """
    API tool to get crew member certification status and expiry information.
    """

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        crew_id: str = None,
        crew_member_id: str = None,
        certification_type: str = None,
        expiry_threshold_days: int = 90
    ) -> str:
        from datetime import datetime, timedelta
        from typing import Optional

        crew_certifications = data.get("crew_certifications", [])
        crew_members = data.get("crew_members", [])
        filtered_certifications = []

        # Set default expiry threshold if not provided
        if expiry_threshold_days is None:
            expiry_threshold_days = 90

        # Handle both crew_id and crew_member_id parameters
        target_crew_id = crew_id or crew_member_id

        today = datetime(2025, 9, 15, 0, 0, 0).date()
        threshold_date = today + timedelta(days=expiry_threshold_days)

        for cert in crew_certifications:
            # Apply filters
            if target_crew_id and cert.get("crew_member", {}).get("crew_member_id") != target_crew_id:
                continue
            if certification_type and cert.get("certification", {}).get("certification_code") != certification_type:
                continue

            # Get crew member details
            crew_member_id = cert.get("crew_member", {}).get("crew_member_id")
            crew_details = None
            for crew in crew_members:
                if crew.get("crew_member_id") == crew_member_id:
                    crew_details = crew
                    break

            # Calculate certification status
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
                "crew_name": cert.get("crew_member", {}).get("full_name"),
                "crew_role": crew_details.get("role") if crew_details else None,
                "certification_type": cert.get("certification", {}).get("certification_code"),
                "issue_date": cert.get("issue_date"),
                "expiry_date": expiry_date,
                "status": status,
                "days_until_expiry": days_until_expiry
            }

            filtered_certifications.append(cert_info)

        # Sort by status priority and expiry date
        status_priority = {"expired": 1, "expiring_soon": 2, "valid": 3, "no_expiry": 4, "unknown": 5}
        filtered_certifications.sort(key=lambda x: (
            status_priority.get(x["status"], 6),
            x["days_until_expiry"] if x["days_until_expiry"] is not None else float('inf')
        ))

        # Calculate summary statistics
        total_certifications = len(filtered_certifications)
        status_counts = {}
        type_counts = {}
        expiring_soon_count = 0
        expired_count = 0

        for cert in filtered_certifications:
            status_counts[cert["status"]] = status_counts.get(cert["status"], 0) + 1
            type_counts[cert["certification_type"]] = type_counts.get(cert["certification_type"], 0) + 1
            
            if cert["status"] == "expiring_soon":
                expiring_soon_count += 1
            elif cert["status"] == "expired":
                expired_count += 1

        response = {
            "filters_applied": {
                "crew_id": target_crew_id,
                "crew_member_id": crew_member_id,
                "certification_type": certification_type,
                "expiry_threshold_days": expiry_threshold_days
            },
            "summary": {
                "total_certifications_found": total_certifications,
                "status_breakdown": status_counts,
                "certification_type_breakdown": type_counts,
                "expiring_soon_count": expiring_soon_count,
                "expired_count": expired_count
            },
            "certifications": filtered_certifications
        }

        # Add alerts for critical certifications
        if expired_count > 0 or expiring_soon_count > 0:
            response["alerts"] = {}
            if expired_count > 0:
                response["alerts"]["expired_certifications"] = expired_count
            if expiring_soon_count > 0:
                response["alerts"]["expiring_soon_certifications"] = expiring_soon_count

        # Add recommendations if no specific filters
        if not any([target_crew_id, certification_type]) and total_certifications > 0:
            if expired_count > 0:
                response["recommendations"] = {
                    "priority": "high",
                    "message": f"Immediate attention required: {expired_count} expired certification(s) need renewal"
                }
            elif expiring_soon_count > 0:
                response["recommendations"] = {
                    "priority": "medium",
                    "message": f"Plan renewals: {expiring_soon_count} certification(s) expiring within {expiry_threshold_days} days"
                }

        return json.dumps(response, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_crew_certification_status",
                "description": "Get crew member certification status and expiry information with filtering options. Provides overview of certification validity, expiring soon alerts, and compliance status. Critical for regulatory compliance and operational safety.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "crew_id": {
                            "type": "string",
                            "description": "Optional crew member identifier to get specific crew certifications. Format: CM followed by 3-digit number."
                        },
                        "crew_member_id": {
                            "type": "string",
                            "description": "Alternative parameter name for crew_id. Format: CM followed by 3-digit number."
                        },
                        "certification_type": {
                            "type": "string",
                            "description": "Optional certification type filter. Aircraft-specific certifications are required for specific aircraft models."
                        },
                        "expiry_threshold_days": {
                            "type": "integer",
                            "description": "Number of days to consider certifications as 'expiring soon' (default: 90 days). Values: 30, 60, 90, 120. Used for proactive renewal planning."
                        }
                    },
                    "required": []
                }
            }
        }
