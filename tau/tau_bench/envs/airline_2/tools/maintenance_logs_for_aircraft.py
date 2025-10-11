# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class MaintenanceLogsForAircraft(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], aircraft_id: str) -> str:
        out=[m for m in list(data.get("maintenance_logs", {}).values()) if (m.get("aircraft") or {}).get("aircraft_id")==aircraft_id]
        return _j(out)

    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"maintenance_logs_for_aircraft",
            "description":"List maintenance logs for a given aircraft_id.",
            "parameters":{"type":"object","properties":{"aircraft_id":{"type":"string"}},"required":["aircraft_id"]}
        }}
