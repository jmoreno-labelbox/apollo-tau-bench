from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class FindAvailableCrew(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any], role: str, home_base_iata: str, status: str
    ) -> str:
        crew_members = data.get("crew_members", [])
        results = [
            m
            for m in crew_members
            if m["role"] == role
            and m["home_base"]["iata_code"] == home_base_iata
            and m["status"] == status
        ]
        payload = results
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindAvailableCrew",
                "description": "Finds available crew members matching specified criteria.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role": {
                            "type": "string",
                            "description": "The role of the crew member (e.g., 'Captain', 'First Officer').",
                        },
                        "home_base_iata": {
                            "type": "string",
                            "description": "The IATA code of the crew member's home base.",
                        },
                        "status": {
                            "type": "string",
                            "description": "The current status of the crew member (e.g., 'Active').",
                        },
                    },
                    "required": ["role", "home_base_iata", "status"],
                },
            },
        }
