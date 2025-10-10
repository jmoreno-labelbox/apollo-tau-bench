# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AssignCertificationTool(Tool):
    """Create/assign a certification record to a user (write operation, deterministic)."""

    @staticmethod
    def invoke(data: Dict[str, Any], assigned_on, certification_id, status, user_id) -> str:
        certifications = data.get("certifications", [])
        users = list(data.get("users", {}).values())

        if not isinstance(certifications, list):
            return json.dumps({"error": "certifications must be a list"}, indent=2)
        if not isinstance(users, list):
            return json.dumps({"error": "users must be a list"}, indent=2)
        status = status or "ASSIGNED"

        if not isinstance(certification_id, str) or not certification_id.strip():
            return json.dumps({"error": "certification_id must be a non-empty string"}, indent=2)
        if not isinstance(user_id, str) or not user_id.strip():
            return json.dumps({"error": "user_id must be a non-empty string"}, indent=2)
        if assigned_on is not None and not isinstance(assigned_on, str):
            return json.dumps({"error": "assigned_on must be a string if provided"}, indent=2)
        if not isinstance(status, str) or not status.strip():
            return json.dumps({"error": "status must be a non-empty string"}, indent=2)

        # Check if the user is present.
        user = next((u for u in users if u.get("user_id") == user_id), None)
        if not user:
            return json.dumps({"error": f"user_id {user_id} not found in users"}, indent=2)

        # Verify that certification_id is distinct.
        if any(c.get("certification_id") == certification_id for c in certifications):
            return json.dumps({"error": f"certification_id {certification_id} already exists"}, indent=2)

        # Add a minimal record that adheres to the schema, utilizing only recognized field names from the datasets.
        new_record = {
            "certification_id": certification_id,
            "user_id": user_id,
            "status": status,
        }
        if assigned_on:
            new_record["assigned_on"] = assigned_on  # field name is present in project datasets (e.g., user_roles)

        certifications.append(new_record)
        return json.dumps(
            {"success": f"Certification {certification_id} assigned to user {user_id}", "certification": new_record},
            indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "assign_certification",
                "description": "Create/assign a certification record to a user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "certification_id": {"type": "string", "description": "Unique certification identifier"},
                        "user_id": {"type": "string", "description": "Target user_id"},
                        "assigned_on": {"type": "string", "description": "Deterministic assignment timestamp"},
                        "status": {"type": "string", "description": "Initial status (defaults to ASSIGNED)"}
                    },
                    "required": ["certification_id", "user_id"]
                },
            },
        }
