from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class SearchVulnerabilitiesByCVE(Tool):
    """Looks for vulnerabilities that correspond to a particular CVE identifier."""

    @staticmethod
    def invoke(data: dict[str, Any], cve: str = None) -> str:
        cve_id = cve
        vulnerabilities = data.get("vulnerabilities", [])

        matching_vulnerabilities = [
            vuln for vuln in vulnerabilities if vuln.get("cve") == cve_id
        ]
        payload = {"vulnerabilities": matching_vulnerabilities}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchVulnerabilitiesByCve",
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
