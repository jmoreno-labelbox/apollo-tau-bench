# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateIncidentReport(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        id = kwargs.get("id")
        incident_type = kwargs.get("incident_type")
        severity = kwargs.get("severity", "medium")

        incident_id = f"INC-{id}-{severity}"

        incident_report = {
            "incident_id": incident_id,
            "id": id,
            "incident_type": incident_type,
            "severity": severity,
            "reported_date": get_current_timestamp(),
            "reported_by": "SYSTEM",
            "status": "Open",
            "investigation_required": True,
            "regulatory_notification": severity in ["high", "critical"],
            "customer_notification": True,
            "estimated_impact": "TBD"
        }

        if "incident_reports" not in data:
            data["incident_reports"] = []
        data["incident_reports"].append(incident_report)

        return json.dumps({
            "incident_id": incident_id,
            "status": "Created",
            "investigation_required": True,
            "regulatory_notification_required": incident_report["regulatory_notification"]
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_incident_report",
                "description": "Create incident report for supply chain issues",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string", "description": "Related identifier"},
                        "incident_type": {"type": "string", "description": "Type of incident"},
                        "severity": {"type": "string", "description": "Incident severity (low/medium/high/critical)"}
                    },
                    "required": ["id", "incident_type"]
                }
            }
        }
