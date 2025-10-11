# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindCrewCertifications(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], crew_member_id: str, certification_code: Optional[str] = None) -> str:
        cert_records = list(data.get("crew_certifications", {}).values())
        results = []
        for record in cert_records:
            if record.get("crew_member", {}).get("crew_member_id") == crew_member_id:
                if certification_code and record.get("certification", {}).get("certification_code") != certification_code:
                    continue
                results.append(record)
        return json.dumps(results)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_crew_certifications",
                "description": "Finds all certification records for a given crew member, optionally filtering by a specific certification code.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "crew_member_id": {
                            "type": "string",
                            "description": "The unique ID of the crew member."
                        },
                        "certification_code": {
                            "type": "string",
                            "description": "Optional: The specific code of the certification to find (e.g., 'B787_FAMILY_TR')."
                        }
                    },
                    "required": ["crew_member_id"]
                }
            }
        }
