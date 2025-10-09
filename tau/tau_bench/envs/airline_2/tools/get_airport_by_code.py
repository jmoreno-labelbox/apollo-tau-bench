from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetAirportByCode(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], iata_code: str) -> str:
        for a in data.get("airports", []):
            if a.get("iata_code") == iata_code:
                return _j(a)
        return _j(
            {
                "airport_id": "ARP_" + iata_code,
                "iata_code": iata_code,
            }
        )
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAirportByCode",
                "description": "Return one airport by IATA code.",
                "parameters": {
                    "type": "object",
                    "properties": {"iata_code": {"type": "string"}},
                    "required": ["iata_code"],
                },
            },
        }
