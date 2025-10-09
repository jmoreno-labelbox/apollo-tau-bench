from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timedelta
from typing import Any

class VerifyCrewDutyTime(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], crew_member_id: str, reference_date: str) -> str:
        crew_members = data.get("crew_members", [])
        target_logs = []
        for member in crew_members:
            if member.get("crew_member_id") == crew_member_id:
                target_logs.extend(member.get("flight_log", []))

        if not target_logs:
            payload = {
                "crew_member_id": crew_member_id,
                "is_compliant": True,
                "hours_past_24h": 0,
                "hours_past_30d": 0,
                "hours_past_365d": 0,
                "details": "No flight logs found, compliant by default.",
            }
            out = json.dumps(payload)
            return out

        ref_date = datetime.fromisoformat(reference_date)
        hours_24h, hours_30d, hours_365d = 0.0, 0.0, 0.0

        for log in target_logs:
            log_date = datetime.fromisoformat(log.get("date"))
            delta = ref_date - log_date

            raw_hours = log.get("hours_flown", {}).get("total")
            hours = raw_hours if isinstance(raw_hours, (int, float)) else 0.0

            if delta.days < 1:
                hours_24h += hours
            if delta.days < 30:
                hours_30d += hours
            if delta.days < 365:
                hours_365d += hours

        is_compliant = all([hours_24h <= 8, hours_30d <= 100, hours_365d <= 1000])
        payload = {
            "crew_member_id": crew_member_id,
            "is_compliant": is_compliant,
            "hours_past_24h": round(hours_24h, 2),
            "hours_past_30d": round(hours_30d, 2),
            "hours_past_365d": round(hours_365d, 2),
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "VerifyCrewDutyTime",
                "description": "Verifies if a crew member is compliant with cumulative flight duty time limits based on their flight log.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "crew_member_id": {
                            "type": "string",
                            "description": "The unique ID of the crew member to verify.",
                        },
                        "reference_date": {
                            "type": "string",
                            "description": "The date of the prospective flight assignment (YYYY-MM-DD), used as the reference point for calculations.",
                        },
                    },
                    "required": ["crew_member_id", "reference_date"],
                },
            },
        }
