# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RelocateAircraft(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], aircraft_id: str, new_location_airport_id: str, new_location_iata: Optional[str]=None) -> str:
        for a in list(data.get("aircraft", {}).values()):
            if a.get("aircraft_id") == aircraft_id:
                a["location"] = {"airport_id": new_location_airport_id, "iata_code": new_location_iata} if new_location_iata else {"airport_id": new_location_airport_id}
                return _j(a)
        return _j({"error":"aircraft_not_found","aircraft_id":aircraft_id})

    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"relocate_aircraft",
            "description":"Update aircraft.location to a new airport deterministically.",
            "parameters":{"type":"object","properties":{
                "aircraft_id":{"type":"string"},
                "new_location_airport_id":{"type":"string"},
                "new_location_iata":{"type":"string"}
            },"required":["aircraft_id","new_location_airport_id"]}
        }}
