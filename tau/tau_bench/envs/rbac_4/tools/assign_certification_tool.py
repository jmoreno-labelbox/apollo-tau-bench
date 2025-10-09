from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class AssignCertificationTool(Tool):
    """Establish/assign a certification record to a user (write operation, predictable)."""

    @staticmethod
    def invoke(data: dict[str, Any], certification_id: str, user_id: str, assigned_on: str = None, status: str = "ASSIGNED") -> str:
        certifications = data.get("certifications", [])
        users = data.get("users", [])

        if not isinstance(certifications, list):
            payload = {"error": "certifications must be a list"}
            out = json.dumps(payload, indent=2)
            return out
        if not isinstance(users, list):
            payload = {"error": "users must be a list"}
            out = json.dumps(payload, indent=2)
            return out

        if not isinstance(certification_id, str) or not certification_id.strip():
            payload = {"error": "certification_id must be a non-empty string"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        if not isinstance(user_id, str) or not user_id.strip():
            payload = {"error": "user_id must be a non-empty string"}
            out = json.dumps(payload, indent=2)
            return out
        if assigned_on is not None and not isinstance(assigned_on, str):
            payload = {"error": "assigned_on must be a string if provided"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        if not isinstance(status, str) or not status.strip():
            payload = {"error": "status must be a non-empty string"}
            out = json.dumps(payload, indent=2)
            return out

        #Confirm user existence
        user = next((u for u in users if u.get("user_id") == user_id), None)
        if not user:
            payload = {"error": f"user_id {user_id} not found in users"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        #Verify that certification_id is distinct
        if any(c.get("certification_id") == certification_id for c in certifications):
            payload = {"error": f"certification_id {certification_id} already exists"}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        #Add a minimal, schema-compliant record utilizing only recognized field names from datasets
        new_record = {
            "certification_id": certification_id,
            "user_id": user_id,
            "status": status,
        }
        if assigned_on:
            new_record["assigned_on"] = (
                assigned_on  #field name is present in project datasets (e.g., user_roles)
            )

        certifications.append(new_record)
        payload = {
                "success": f"Certification {certification_id} assigned to user {user_id}",
                "certification": new_record,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AssignCertification",
                "description": "Create/assign a certification record to a user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "certification_id": {
                            "type": "string",
                            "description": "Unique certification identifier",
                        },
                        "user_id": {"type": "string", "description": "Target user_id"},
                        "assigned_on": {
                            "type": "string",
                            "description": "Deterministic assignment timestamp",
                        },
                        "status": {
                            "type": "string",
                            "description": "Initial status (defaults to ASSIGNED)",
                        },
                    },
                    "required": ["certification_id", "user_id"],
                },
            },
        }
