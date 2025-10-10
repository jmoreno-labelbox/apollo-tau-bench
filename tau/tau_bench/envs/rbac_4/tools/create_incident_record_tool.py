# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateIncidentRecordTool(Tool):
    """Create a new incident record for tracking security or operational events."""

    @staticmethod
    def invoke(data, created_by, summary, timestamp, linked_alerts = [], linked_resources = [], linked_users = []):
        incident_id = f"INC-{len(list(data.get('incidents', {}).values())) + 1:03d}"
        record = {
            "incident_id": incident_id,
            "timestamp": timestamp,
            "created_by": created_by,
            "summary": summary,
            "linked_alerts": linked_alerts,
            "linked_users": linked_users,
            "linked_resources": linked_resources,
            "status": "OPEN"
        }
        data.setdefault("incidents", []).append(record)

        return json.dumps(
            {
                "success": f"Incident {incident_id} created",
                "incident_id": incident_id
            },
            indent=2
        )

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "create_incident_record",
                "description": "Create a new incident record with linked alerts, users, and resources.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "timestamp": {"type": "string", "description": "ISO 8601 UTC timestamp."},
                        "created_by": {"type": "string", "description": "user_id of creator."},
                        "summary": {"type": "string", "description": "Brief summary of the incident."},
                        "linked_alerts": {"type": "array", "items": {"type": "string"}},
                        "linked_users": {"type": "array", "items": {"type": "string"}},
                        "linked_resources": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["timestamp", "created_by", "summary"]
                }
            }
        }
