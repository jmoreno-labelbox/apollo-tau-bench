from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class FilterLicenses(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], utilization: float = None) -> str:
        if all([param is None for param in [utilization]]):
            payload = {
                "status": "error",
                "reason": "Input parameters to filter by are required.",
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        licenses = data.get("license_inventory")
        filtered_licenses = []

        for license in licenses:
            util = (license["used_seats"] + license["reserved_seats"]) / license[
                "total_seats"
            ]
            if util < utilization:
                filtered_licenses.append(license["license_id"])
        payload = filtered_licenses
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "filterLicenses",
                "description": "Reterns the licenses that match input criteria.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "utilization": {
                            "type": "number",
                            "description": "Filters liceses by utilization.",
                        },
                    },
                },
            },
        }
