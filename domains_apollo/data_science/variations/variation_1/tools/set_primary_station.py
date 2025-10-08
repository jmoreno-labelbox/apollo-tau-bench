from tau_bench.envs.tool import Tool
import json
from typing import Any

class SetPrimaryStation(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], station_id: str = None) -> str:
        err = _require({"station_id": station_id}, ["station_id"])
        if err:
            return err
        cfg = (
            (data.get("project_config") or [{}])[0]
            if data.get("project_config")
            else {}
        )
        cfg["primary_station_id_nullable"] = station_id
        data["project_config"] = [cfg] if data.get("project_config") else [cfg]
        payload = cfg
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetPrimaryStation",
                "description": "Sets the chosen primary station_id on project_config.",
                "parameters": {
                    "type": "object",
                    "properties": {"station_id": {"type": "string"}},
                    "required": ["station_id"],
                },
            },
        }
