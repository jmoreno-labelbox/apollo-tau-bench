from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetCrewCertifications(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], crew_member_id: str, certification_code: str | None = None
    ) -> str:
        out = []
        for c in data.get("crew_certifications", {}).values():
            cmid = (c.get("crew_member") or {}).get("crew_member_id")
            if cmid != crew_member_id:
                continue
            if certification_code and c.get("certification_code") != certification_code:
                continue
            out.append(c)
        return _j(out)

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCrewCertifications",
                "description": "List certifications for a crew member; optionally filter by certification_code.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "crew_member_id": {"type": "string"},
                        "certification_code": {"type": "string"},
                    },
                    "required": ["crew_member_id"],
                },
            },
        }
