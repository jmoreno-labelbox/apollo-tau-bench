# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FetchEnvironment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], ) -> str:
        env = data.get("environment", {}) or {}
        return json.dumps(env, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"get_environment",
            "description":"Read environment variables/secrets map.",
            "parameters":{"type":"object","properties":{},"required":[]}
        }}
