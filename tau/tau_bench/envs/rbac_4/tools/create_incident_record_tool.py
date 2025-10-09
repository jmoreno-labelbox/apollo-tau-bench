from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateIncidentRecordTool(Tool):
    """Initiate a new incident record to monitor security or operational events."""

    @staticmethod
    def invoke(data, timestamp, created_by, summary, linked_alerts=None, linked_users=None, linked_resources=None, severity=None):
        incident_id = f"INC-{len(data.get('incidents', [])) + 1:03d}"
        record = {
            "incident_id": incident_id,
            "timestamp": timestamp,
            "created_by": created_by,
            "summary": summary,
            "linked_alerts": linked_alerts or [],
            "linked_users": linked_users or [],
            "linked_resources": linked_resources or [],
            "status": "OPEN",
        }
        data.setdefault("incidents", []).append(record)
        payload = {"success": f"Incident {incident_id} created", "incident_id": incident_id}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "CreateIncidentRecord",
                "description": "Create a new incident record with linked alerts, users, and resources.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "timestamp": {
                            "type": "string",
                            "description": "ISO 8601 UTC timestamp.",
                        },
                        "created_by": {
                            "type": "string",
                            "description": "user_id of creator.",
                        },
                        "summary": {
                            "type": "string",
                            "description": "Brief summary of the incident.",
                        },
                        "linked_alerts": {"type": "array", "items": {"type": "string"}},
                        "linked_users": {"type": "array", "items": {"type": "string"}},
                        "linked_resources": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                    "required": ["timestamp", "created_by", "summary"],
                },
            },
        }
