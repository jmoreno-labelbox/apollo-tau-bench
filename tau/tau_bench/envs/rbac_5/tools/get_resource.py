from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetResource(Tool):
    """
    Retrieve resources based on ID, name, owner, criticality, or compliance scope.

    kwargs:
      resource_id: str (optional) - Specific resource ID to retrieve
      name: str (optional) - Filter by resource name
      owner_id: str (optional) - Filter by resource owner
      criticality: str (optional) - Filter by criticality (CRITICAL, HIGH, MEDIUM, LOW)
      compliance_scope: str (optional) - Filter by compliance scope (ISO-27001, GDPR, SOX, PCI-DSS, ALL)
    """

    @staticmethod
    def invoke(data: dict[str, Any], resource_id: str = None, name: str = None, owner_id: str = None, criticality: str = None, compliance_scope: str = None) -> str:
        resources = data.get("resources", [])

        # If resource_id is given, return the specific resource
        if resource_id:
            resource = _find_by_id(resources, "resource_id", resource_id)
            if not resource:
                payload = {"error": f"resource_id {resource_id} not found"}
                out = json.dumps(payload)
                return out
            payload = {"ok": True, "resource": resource}
            out = json.dumps(payload)
            return out

        # Narrow down resources according to the supplied criteria
        filtered_resources = []
        for resource in resources:
            # Narrow down by name
            if name and name not in resource.get("name", ""):
                continue
            # Narrow down by owner_id if supplied
            if owner_id and resource.get("owner_id") != owner_id:
                continue
            # Narrow down by criticality if supplied
            if criticality and resource.get("criticality") != criticality:
                continue
            # Narrow down by compliance_scope if supplied (manage null values)
            if compliance_scope:
                resource_scope = resource.get("compliance_scope")
                if resource_scope != compliance_scope:
                    continue
            filtered_resources.append(resource)
        payload = {"ok": True, "resources": filtered_resources}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetResource",
                "description": "Retrieve resources by ID, name, owner, criticality, or compliance scope.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "resource_id": {
                            "type": "string",
                            "description": "Specific resource ID to retrieve.",
                        },
                        "name": {
                            "type": "string",
                            "description": "Filter by resource name (partial match).",
                        },
                        "owner_id": {
                            "type": "string",
                            "description": "Filter by resource owner ID.",
                        },
                        "criticality": {
                            "type": "string",
                            "description": "Filter by criticality (CRITICAL, HIGH, MEDIUM, LOW).",
                        },
                        "compliance_scope": {
                            "type": "string",
                            "description": "Filter by compliance scope (ISO-27001, GDPR, SOX, PCI-DSS, ALL).",
                        },
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }
