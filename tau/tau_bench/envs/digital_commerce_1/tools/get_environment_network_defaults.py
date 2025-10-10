# Copyright by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _get_network_defaults


class GetEnvironmentNetworkDefaults(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], environment: str) -> str:
        res = _get_network_defaults(data, environment)
        res.update({"environment": environment})
        return _json(res)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_environment_network_defaults",
                "description": "Resolve VPC/subnets/allowlist and standard ports for an environment.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "environment": {"type": "string", "enum": ["DEV", "UAT", "PROD"]}
                    },
                    "required": ["environment"],
                },
            },
        }
