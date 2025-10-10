# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchVulnerabilitiesByCVE(Tool):
    """Searches for vulnerabilities matching a specific CVE identifier."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cve_id = kwargs.get("cve")
        vulnerabilities = data.get("vulnerabilities", [])
        
        matching_vulnerabilities = [
            vuln for vuln in vulnerabilities if vuln.get("cve") == cve_id
        ]
        
        return json.dumps({"vulnerabilities": matching_vulnerabilities})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_vulnerabilities_by_cve",
                "description": "Searches for vulnerabilities matching a specific CVE identifier.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cve": {
                            "type": "string",
                            "description": "The CVE identifier to search for (e.g., 'CVE-2024-1234').",
                        }
                    },
                    "required": ["cve"],
                },
            },
        }
