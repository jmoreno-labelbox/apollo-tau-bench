# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ComputeCrewDutyCounts(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], crew_member_id: str, reference_date: str) -> str:
        # Use crew_members[].flight_log dates + assignments[].flight.flight_number + flights.json (by flight_number via operational_events link if needed)
        # Here: count assignments in prior windows based on crew member's flight_log (has dates).
        # Deterministic counts only (no hours).
        ref = datetime.fromisoformat(reference_date + "T00:00:00+00:00")
        windows = {"24h": ref - timedelta(hours=24), "30d": ref - timedelta(days=30), "365d": ref - timedelta(days=365)}
        counts = {"24h":0,"30d":0,"365d":0}
        # From flight_log
        for c in data.get("crew_members", []):
            if c.get("crew_member_id") != crew_member_id:
                continue
            for entry in c.get("flight_log", []):
                d = entry.get("date")
                try:
                    dt = datetime.fromisoformat(d + "T00:00:00+00:00")
                except Exception:
                    continue
                for k, start in OrderedDict(windows).items():
                    if start <= dt <= ref:
                        counts[k] += 1
            break
        return _j({"crew_member_id": crew_member_id, "counts": counts})

    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"compute_crew_duty_counts",
            "description":"Compute counts of crew flight_log entries within 24h/30d/365d windows relative to reference_date.",
            "parameters":{"type":"object","properties":{
                "crew_member_id":{"type":"string"},
                "reference_date":{"type":"string"}
            },"required":["crew_member_id","reference_date"]}
        }}
