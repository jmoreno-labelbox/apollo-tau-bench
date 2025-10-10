# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _fixed_now_iso


class ModifyEnvironment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        updates = kwargs.get("updates") or {}
        env = data.get("environment", {})
        if env is None or isinstance(env, list):
            env = {}
            data["environment"] = env
        env.update(updates)
        env["updated_at"] = _fixed_now_iso()
        return json.dumps({"updated": updates}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"update_environment",
            "description":"Update environment variables/secrets.",
            "parameters":{"type":"object","properties":{"updates":{"type":"object"}},"required":["updates"]}
        }}
