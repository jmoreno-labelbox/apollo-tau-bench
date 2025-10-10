# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCertificationDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cert_id = kwargs.get("certification_id")
        for cert in data.get('certifications', []):
            if cert.get('certification_id') == cert_id:
                return json.dumps(cert)
        return json.dumps({"error": "Certification not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_certification_details",
                        "description": "Retrieves details for a specific certification.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "certification_id": {"type": "string"}
                                },
                                "required": ["certification_id"]
                        }
                }
        }
