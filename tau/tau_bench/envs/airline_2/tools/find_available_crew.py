from tau_bench.envs.tool import Tool
import json
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
        data: dict[str, Any],
        role: str,
        home_base_iata: str | None = None,
        status: str | None = None,
    ) -> str:
        crew = data.get("crew_members", [])
        out = []
        for m in crew:
            if m.get("role") != role:
                continue
            if home_base_iata and (
                (m.get("home_base") or {}).get("iata_code") != home_base_iata
            ):
                continue
            if status and m.get("status") != status:
                continue
            out.append(m)
        return _j(out)

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindAvailableCrew",
                "description": "Find crew members by role, optionally filtering by home base IATA and status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role": {"type": "string"},
                        "home_base_iata": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": ["role"],
                },
            },
        }
