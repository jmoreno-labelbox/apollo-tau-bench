# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCertificationTool(Tool):
    """Return a single certification record by certification_id (read operation, deterministic)."""

    @staticmethod
    def invoke(data: Dict[str, Any], certification_id) -> str:
        certifications = data.get("certifications", [])
        if not isinstance(certifications, list):
            return json.dumps({"error": "certifications must be a list"}, indent=2)
        if not isinstance(certification_id, str) or not certification_id.strip():
            return json.dumps({"error": "certification_id must be a non-empty string"}, indent=2)

        for c in certifications:
            if c.get("certification_id") == certification_id:
                return json.dumps(c, indent=2)
        return json.dumps({"error": f"Certification {certification_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_certification",
                "description": "Retrieve a certification by certification_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "certification_id": {"type": "string"}
                    },
                    "required": ["certification_id"]
                }
            }
        }
