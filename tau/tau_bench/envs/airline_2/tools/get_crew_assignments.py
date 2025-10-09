from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any

class GetCrewAssignments(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        crew_member_id: str | None = None,
        flight_number: str | None = None,
    ) -> str:
        out = []
        for a in data.get("flight_crew_assignments", []):
            if (
                crew_member_id
                and (a.get("crew_member") or {}).get("crew_member_id") != crew_member_id
            ):
                continue
            if (
                flight_number
                and (a.get("flight") or {}).get("flight_number") != flight_number
            ):
                continue
            out.append(a)
        return _j(out)

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCrewAssignments",
                "description": "List flight crew assignments filtered by crew_member_id and/or flight_number.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "crew_member_id": {"type": "string"},
                        "flight_number": {"type": "string"},
                    },
                },
            },
        }
