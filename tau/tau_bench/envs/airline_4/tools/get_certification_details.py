from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetCertificationDetails(Tool):
    """API tool for retrieving certification details using either the certification ID or certification code."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        certification_id: str | None = None,
        certification_code: str | None = None,
    ) -> str:
        pass
        if not certification_id and not certification_code:
            payload = {
                    "error": "Either certification_id or certification_code must be provided"
                }
            out = json.dumps(
                payload)
            return out

        certifications = data.get("certifications", {}).values()

        for cert in certifications.values():
            #Verify by ID if supplied
            if certification_id and cert.get("certification_id") == certification_id:
                payload = cert
                out = json.dumps(payload)
                return out
            #Verify by code if given
            if (
                certification_code
                and cert.get("certification_code") == certification_code
            ):
                payload = cert
                out = json.dumps(payload)
                return out

        #Provide a suitable error message according to the search conducted
        search_term = certification_id if certification_id else certification_code
        search_type = "certification_id" if certification_id else "certification_code"
        payload = {"error": "Certification not found", search_type: search_term}
        out = json.dumps(
            payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCertificationDetails",
                "description": "Get certification details using either certification ID (e.g., 'CERT_B738') or certification code (e.g., 'B737-800').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "certification_id": {
                            "type": "string",
                            "description": "Certification ID (e.g., 'CERT_B738', 'CERT_ATPL'). Either this or certification_code must be provided.",
                        },
                        "certification_code": {
                            "type": "string",
                            "description": "Certification code (e.g., 'B737-800', 'ATPL'). Either this or certification_id must be provided.",
                        },
                    },
                    "required": [],
                },
            },
        }
