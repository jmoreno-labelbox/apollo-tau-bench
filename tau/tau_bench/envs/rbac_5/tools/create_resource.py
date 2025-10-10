# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateResource(Tool):
    """
    Create a new resource with deterministic ID generation.

    kwargs:
      name: str (required)
      owner_id: str (required)
      criticality: str (required) - CRITICAL, HIGH, MEDIUM, LOW
      compliance_scope: str (optional) - ISO-27001, GDPR, SOX, PCI-DSS, ALL, or null
    """
    @staticmethod
    def invoke(data: Dict[str, Any], compliance_scope, criticality = "", name = "", owner_id = "") -> str:
        name = (name or "").strip()
        owner_id = (owner_id or "").strip()
        criticality = (criticality or "").strip().upper()

        if not name or not owner_id or not criticality:
            return json.dumps({"error": "name, owner_id, and criticality are required"})

        # Assess importance
        valid_criticalities = ["CRITICAL", "HIGH", "MEDIUM", "LOW"]
        if criticality not in valid_criticalities:
            return json.dumps({"error": f"criticality must be one of: {', '.join(valid_criticalities)}"})

        # Check the compliance_scope if it has been specified.
        if compliance_scope is not None:
            valid_compliance_scopes = ["ISO-27001", "GDPR", "SOX", "PCI-DSS", "ALL", "All"]
            if compliance_scope not in valid_compliance_scopes:
                return json.dumps({"error": f"compliance_scope must be one of: {', '.join(valid_compliance_scopes)} or null"})

        # Check if the owner is present.
        if not _find_by_id(list(data.get("users", {}).values()), "user_id", owner_id):
            return json.dumps({"error": f"owner_id {owner_id} not found"})

        # Ensure name uniqueness (case-insensitive).
        existing_resources = data.get("resources", [])
        for r in existing_resources:
            if str(r.get("name", "")).strip().lower() == name.lower():
                return json.dumps({"error": f"resource name '{name}' already exists"})

        new_resource = {
            "resource_id": _next_id(data, "resources", "RES"),
            "name": name,
            "owner_id": owner_id,
            "criticality": criticality,
            "compliance_scope": compliance_scope,
        }

        data.setdefault("resources", []).append(new_resource)
        return json.dumps({"ok": True, "resource": new_resource})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_resource",
                "description": "Create a new resource with deterministic ID generation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string", "description": "Unique resource name (case-insensitive)."},
                        "owner_id": {"type": "string", "description": "User ID of the resource owner."},
                        "criticality": {"type": "string", "enum": ["CRITICAL", "HIGH", "MEDIUM", "LOW"], "description": "Resource criticality level."},
                        "compliance_scope": {"type": ["string", "null"], "description": "Compliance scope (ISO-27001, GDPR, SOX, PCI-DSS, ALL) or null.", "enum": ["ISO-27001", "GDPR", "SOX", "PCI-DSS", "ALL", "All", None]}
                    },
                    "required": ["name", "owner_id", "criticality"],
                    "additionalProperties": False
                }
            }
        }
