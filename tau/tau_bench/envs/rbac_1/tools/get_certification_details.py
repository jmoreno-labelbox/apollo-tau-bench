from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetCertificationDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], certification_id: str = None,
    user_id: Any = None,
    ) -> str:
        cert_id = certification_id
        for cert in data.get("certifications", {}).values():
            if cert.get("certification_id") == cert_id:
                payload = cert
                out = json.dumps(payload)
                return out
        payload = {"error": "Certification not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCertificationDetails",
                "description": "Retrieves details for a specific certification.",
                "parameters": {
                    "type": "object",
                    "properties": {"certification_id": {"type": "string"}},
                    "required": ["certification_id"],
                },
            },
        }
