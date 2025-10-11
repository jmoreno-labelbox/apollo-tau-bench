# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetResource(Tool):
    """
    Retrieve resources by ID, name, owner, criticality, or compliance scope.

    kwargs:
      resource_id: str (optional) - Specific resource ID to retrieve
      name: str (optional) - Filter by resource name
      owner_id: str (optional) - Filter by resource owner
      criticality: str (optional) - Filter by criticality (CRITICAL, HIGH, MEDIUM, LOW)
      compliance_scope: str (optional) - Filter by compliance scope (ISO-27001, GDPR, SOX, PCI-DSS, ALL)
    """
    @staticmethod
    def invoke(data: Dict[str, Any], compliance_scope, criticality, name, owner_id, resource_id) -> str:

        resources = data.get("resources", [])

        # Return the single resource if resource_id is specified.
        if resource_id:
            resource = _find_by_id(resources, "resource_id", resource_id)
            if not resource:
                return json.dumps({"error": f"resource_id {resource_id} not found"})
            return json.dumps({"ok": True, "resource": resource})

        # Select resources according to specified parameters.
        filtered_resources = []
        for resource in resources:
            # Name-based filtering
            if name and name not in resource.get("name", ""):
                continue
            # Apply filter based on owner_id if specified.
            if owner_id and resource.get("owner_id") != owner_id:
                continue
            # Apply a filter based on criticality if it is specified.
            if criticality and resource.get("criticality") != criticality:
                continue
            # Filter by compliance_scope if available (manage null values)
            if compliance_scope:
                resource_scope = resource.get("compliance_scope")
                if resource_scope != compliance_scope:
                    continue
            filtered_resources.append(resource)

        return json.dumps({"ok": True, "resources": filtered_resources})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_resource",
                "description": "Retrieve resources by ID, name, owner, criticality, or compliance scope.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "resource_id": {"type": "string", "description": "Specific resource ID to retrieve."},
                        "name": {"type": "string", "description": "Filter by resource name (partial match)."},
                        "owner_id": {"type": "string", "description": "Filter by resource owner ID."},
                        "criticality": {"type": "string", "description": "Filter by criticality (CRITICAL, HIGH, MEDIUM, LOW)."},
                        "compliance_scope": {"type": "string", "description": "Filter by compliance scope (ISO-27001, GDPR, SOX, PCI-DSS, ALL)."}
                    },
                    "required": [],
                    "additionalProperties": False
                }
            }
        }
