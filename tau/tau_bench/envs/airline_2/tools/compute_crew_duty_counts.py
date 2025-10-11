# Copyright Sierra

import datetime
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _j(v):
    return v if isinstance(v, str) else json.dumps(v, separators=(",", ":"), ensure_ascii=False)

class ComputeCrewDutyCounts(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], crew_member_id: str, reference_date: str) -> str:
        # Utilize crew_members[].flight_log dates combined with assignments[].flight.flight_number and reference flights.json using flight_number through operational_events if necessary.
        # Count past assignments using the crew member's flight_log, which contains dates.
        # Counts are deterministic only (excluding hours).
        ref = datetime.fromisoformat(reference_date + "T00:00:00+00:00")
        windows = {"24h": ref - timedelta(hours=24), "30d": ref - timedelta(days=30), "365d": ref - timedelta(days=365)}
        counts = {"24h":0,"30d":0,"365d":0}
        # Source from flight_log
        for c in list(data.get("crew_members", {}).values()):
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