# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require




def _require(kwargs: Dict[str, Any], required: List[str]) -> Optional[str]:
    missing = [k for k in required if kwargs.get(k) is None]
    if missing:
        return json.dumps({"error": f"Missing required arguments: {', '.join(missing)}"}, indent=2)
    return None

class SetPrimaryStation(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], station_id) -> str:
        err = _require(kwargs, ["station_id"])
        if err: return err
        cfg = (data.get("project_config") or [{}])[0] if data.get("project_config") else {}
        cfg["primary_station_id_nullable"] = station_id
        data["project_config"] = [cfg] if data.get("project_config") else [cfg]
        return json.dumps(cfg, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "set_primary_station",
            "description": "Sets the chosen primary station_id on project_config.",
            "parameters": {"type": "object", "properties": {"station_id": {"type": "string"}}, "required": ["station_id"]}}}