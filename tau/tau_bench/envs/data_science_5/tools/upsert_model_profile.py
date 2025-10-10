# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpsertModelProfile(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cfgs = list(data.get("model_config", {}).values())
        model_name = kwargs.get("model_name")
        config_name = kwargs.get("config_name")
        params = kwargs.get("params") or {}
        row = next((c for c in cfgs if c.get("model_name") == model_name and c.get("config_name") == config_name), None)
        if row:
            row["params"] = params
            row["updated_at"] = _fixed_now_iso()
            out = {"model_name": model_name, "config_name": config_name, "action": "updated"}
        else:
            max_id = 0
            for c in cfgs:
                try:
                    cid = int(c.get("config_id", 0))
                    if cid > max_id:
                        max_id = cid
                except (ValueError, TypeError):
                    continue
            new_id = max_id + 1
            row = {
                "config_id": new_id,
                "model_name": model_name,
                "config_name": config_name,
                "params": params,
                "created_at": _fixed_now_iso(),
            }
            cfgs.append(row)
            out = {"config_id": new_id, "model_name": model_name, "config_name": config_name, "action": "inserted"}
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "upsert_model_profile",
            "description": "Insert or update a named configuration for a model.",
            "parameters": {"type": "object", "properties": {
                "model_name": {"type": "string"},
                "config_name": {"type": "string"},
                "params": {"type": "object"}
            }, "required": ["model_name", "config_name", "params"]}
        }}
