# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCertificationDetailsById(Tool):
    """ Get the full details of a specific access certification campaign using its ID. """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        certification_id = kwargs.get("certification_id")
        try:
            certifications = data.get('certifications', [])
        except:
            certifications = []

        for cert in certifications:
            if cert.get("certification_id") == certification_id:
                return json.dumps(cert)

        return json.dumps({"error": f"Certification with ID '{certification_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_certification_details_by_id",
                "description": "Retrieves the full details of a specific access certification campaign using its unique ID (e.g., 'C-005').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "certification_id": {
                            "type": "string",
                            "description": "The unique ID of the certification campaign to retrieve."
                        }
                    },
                    "required": ["certification_id"]
                }
            }
        }
