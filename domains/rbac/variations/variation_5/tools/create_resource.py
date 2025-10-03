from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta, timezone
from typing import Any

class CreateResource(Tool):
    """
    Establish a new resource with consistent ID generation.

    kwargs:
      name: str (mandatory)
      owner_id: str (mandatory)
      criticality: str (mandatory) - CRITICAL, HIGH, MEDIUM, LOW
      compliance_scope: str (optional) - ISO-27001, GDPR, SOX, PCI-DSS, ALL, or null
    """

    @staticmethod
    def invoke(data: dict[str, Any], name: str = "", owner_id: str = "", criticality: str = "", compliance_scope: str = None) -> str:
        name = name.strip()
        owner_id = owner_id.strip()
        criticality = criticality.strip().upper()

        if not name or not owner_id or not criticality:
            payload = {"error": "name, owner_id, and criticality are required"}
            out = json.dumps(payload)
            return out

        # Confirm criticality
        valid_criticalities = ["CRITICAL", "HIGH", "MEDIUM", "LOW"]
        if criticality not in valid_criticalities:
            payload = {
                "error": f"criticality must be one of: {', '.join(valid_criticalities)}"
            }
            out = json.dumps(payload)
            return out

        # Check compliance_scope if it is supplied
        if compliance_scope is not None:
            valid_compliance_scopes = [
                "ISO-27001",
                "GDPR",
                "SOX",
                "PCI-DSS",
                "ALL",
                "All",
            ]
            if compliance_scope not in valid_compliance_scopes:
                payload = {
                    "error": f"compliance_scope must be one of: {', '.join(valid_compliance_scopes)} or null"
                }
                out = json.dumps(payload)
                return out

        # Confirm the existence of the owner
        if not _find_by_id(data.get("users", []), "user_id", owner_id):
            payload = {"error": f"owner_id {owner_id} not found"}
            out = json.dumps(payload)
            return out

        # Ensure uniqueness based on name (case-insensitive)
        existing_resources = data.get("resources", [])
        for r in existing_resources:
            if str(r.get("name", "")).strip().lower() == name.lower():
                payload = {"error": f"resource name '{name}' already exists"}
                out = json.dumps(payload)
                return out

        new_resource = {
            "resource_id": _next_id(data, "resources", "RES"),
            "name": name,
            "owner_id": owner_id,
            "criticality": criticality,
            "compliance_scope": compliance_scope,
        }

        data.setdefault("resources", []).append(new_resource)
        payload = {"ok": True, "resource": new_resource}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateResource",
                "description": "Create a new resource with deterministic ID generation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Unique resource name (case-insensitive).",
                        },
                        "owner_id": {
                            "type": "string",
                            "description": "User ID of the resource owner.",
                        },
                        "criticality": {
                            "type": "string",
                            "enum": ["CRITICAL", "HIGH", "MEDIUM", "LOW"],
                            "description": "Resource criticality level.",
                        },
                        "compliance_scope": {
                            "type": ["string", "null"],
                            "description": "Compliance scope (ISO-27001, GDPR, SOX, PCI-DSS, ALL) or null.",
                            "enum": [
                                "ISO-27001",
                                "GDPR",
                                "SOX",
                                "PCI-DSS",
                                "ALL",
                                "All",
                                None,
                            ],
                        },
                    },
                    "required": ["name", "owner_id", "criticality"],
                    "additionalProperties": False,
                },
            },
        }
