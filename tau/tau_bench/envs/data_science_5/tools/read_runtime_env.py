# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ReadRuntimeEnv(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        env = data.get("environment", {}) or {}
        return json.dumps(env, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "read_runtime_env",
            "description": "Read the environment variables/secrets map.",
            "parameters": {"type": "object", "properties": {}, "required": []}
        }}
