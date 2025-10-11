# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class PatchRuntimeEnv(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], updates) -> str:
        updates = updates or {}
        env = data.get("environment", {})
        if env is None or isinstance(env, list):
            env = {}
            data["environment"] = env
        env.update(updates)
        env["updated_at"] = _fixed_now_iso()
        return json.dumps({"updated": updates}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "patch_runtime_env",
            "description": "Update environment variables/secrets.",
            "parameters": {"type": "object", "properties": {"updates": {"type": "object"}}, "required": ["updates"]}
        }}
