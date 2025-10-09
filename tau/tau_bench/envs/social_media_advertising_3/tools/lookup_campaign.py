from tau_bench.envs.tool import Tool
import csv
import json
import re
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class LookupCampaign(Tool):
    """Provide information about a campaign based on its name."""

    @staticmethod
    def invoke(data: dict[str, Any], name: str = None) -> str:
        for c in data.get("campaigns", []):
            if c.get("name") == name:
                payload = c
                out = json.dumps(payload)
                return out
        payload = {"error": f"Campaign {name} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LookupCampaign",
                "description": "Return details for a campaign by its exact name.",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"],
                },
            },
        }
