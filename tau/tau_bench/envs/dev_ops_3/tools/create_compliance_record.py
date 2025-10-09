from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class create_compliance_record(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        project_id: str,
        compliance_type: str,
        requirement: str,
        status: str,
        details: str,
        assignee_id: str,
    ) -> str:
        pass
        compliance_records = data.get("compliance", [])
        existing_ids = [item["id"] for item in compliance_records]
        new_id = _get_next_id("compliance", existing_ids)

        new_record = {
            "id": new_id,
            "project_id": project_id,
            "compliance_type": compliance_type,
            "requirement": requirement,
            "status": status,
            "details": details,
            "due_date": None,
            "assigned_to": assignee_id,
            "created_at": FIXED_TIMESTAMP,
        }

        compliance_records.append(new_record)
        data["compliance"] = compliance_records
        payload = {
                "success": f"Created compliance record '{new_id}'.",
                "compliance_id": new_id,
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
                "name": "CreateComplianceRecord",
                "description": "Creates a new compliance record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string"},
                        "compliance_type": {"type": "string"},
                        "requirement": {"type": "string"},
                        "status": {"type": "string"},
                        "details": {"type": "string"},
                        "assignee_id": {"type": "string"},
                    },
                    "required": [
                        "project_id",
                        "compliance_type",
                        "requirement",
                        "status",
                        "details",
                        "assignee_id",
                    ],
                },
            },
        }
