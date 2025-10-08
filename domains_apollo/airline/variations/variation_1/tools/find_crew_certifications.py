from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timedelta
from typing import Any

class FindCrewCertifications(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], crew_member_id: str, certification_code: str | None = None
    ) -> str:
        cert_records = data.get("crew_certifications", [])
        results = []
        for record in cert_records:
            if record.get("crew_member", {}).get("crew_member_id") == crew_member_id:
                if (
                    certification_code
                    and record.get("certification", {}).get("certification_code")
                    != certification_code
                ):
                    continue
                results.append(record)
        payload = results
        out = json.dumps(payload)
        return out
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindCrewCertifications",
                "description": "Finds all certification records for a given crew member, optionally filtering by a specific certification code.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "crew_member_id": {
                            "type": "string",
                            "description": "The unique ID of the crew member.",
                        },
                        "certification_code": {
                            "type": "string",
                            "description": "Optional: The specific code of the certification to find (e.g., 'B787_FAMILY_TR').",
                        },
                    },
                    "required": ["crew_member_id"],
                },
            },
        }
