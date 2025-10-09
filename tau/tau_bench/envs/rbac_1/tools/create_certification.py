from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CreateCertification(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], reviewer_id: str = None, resource_id: str = None, due_date: str = None) -> str:
        certifications = data.get("certifications", {}).values()
        new_id_num = (
            max((int(c["certification_id"][2:]) for c in certifications.values()), default=0) + 1
        )
        new_cert_id = f"C-{new_id_num:03d}"
        new_cert = {
            "certification_id": new_cert_id,
            "reviewer_id": reviewer_id,
            "resource_id": resource_id,
            "status": "PENDING",
            "due_date": due_date,
        }
        data["certifications"][certification_id] = new_cert
        data["certifications"] = certifications
        payload = new_cert
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateCertification",
                "description": "Creates a new access certification request.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reviewer_id": {"type": "string"},
                        "resource_id": {"type": "string"},
                        "due_date": {"type": "string", "format": "date-time"},
                    },
                    "required": ["reviewer_id", "resource_id", "due_date"],
                },
            },
        }
