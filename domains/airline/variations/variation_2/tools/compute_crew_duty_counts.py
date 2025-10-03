from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any

class ComputeCrewDutyCounts(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], crew_member_id: str, reference_date: str) -> str:
        # Utilize crew_members[].flight_log dates along with assignments[].flight.flight_id and flights.json (by flight_number through operational_events link if necessary)
        # In this section: tally assignments in previous windows using the crew member's flight_log (which contains dates).
        # Only deterministic counts are allowed (excluding hours).
        ref = datetime.fromisoformat(reference_date + "T00:00:00+00:00")
        windows = {
            "24h": ref - timedelta(hours=24),
            "30d": ref - timedelta(days=30),
            "365d": ref - timedelta(days=365),
        }
        counts = {"24h": 0, "30d": 0, "365d": 0}
        # Derived from flight_log
        for c in data["crew_members"]:
            if c["crew_member_id"] != crew_member_id:
                continue
            for entry in c["flight_log"]:
                d = entry["date"]
                try:
                    dt = datetime.fromisoformat(d + "T00:00:00+00:00")
                except Exception:
                    continue
                for k, start in windows.items():
                    if start <= dt <= ref:
                        counts[k] += 1
            break
        return _j({"crew_member_id": crew_member_id, "counts": counts})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ComputeCrewDutyCounts",
                "description": "Compute counts of crew flight_log entries within 24h/30d/365d windows relative to reference_date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "crew_member_id": {"type": "string"},
                        "reference_date": {"type": "string"},
                    },
                    "required": ["crew_member_id", "reference_date"],
                },
            },
        }
