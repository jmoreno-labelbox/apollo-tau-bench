# © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _j(v):
    return v if isinstance(v, str) else json.dumps(v, separators=(",", ":"), ensure_ascii=False)

class MaintenanceLogs(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], ) -> str:
        return _j(list(data.get("maintenance_logs", {}).values()))

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "maintenance_logs",
            "description": "List maintenance logs for a given aircraft_id.",
            "parameters": {"type": "object", "properties": {},
                           "required": []}
        }}