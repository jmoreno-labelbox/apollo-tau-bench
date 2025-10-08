from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetEnvironmentNetworkDefaults(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], environment: str) -> str:
        res = _get_network_defaults(data, environment)
        res.update({"environment": environment})
        return _json(res)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetEnvironmentNetworkDefaults",
                "description": "Resolve VPC/subnets/allowlist and standard ports for an environment.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "environment": {
                            "type": "string",
                            "enum": ["DEV", "UAT", "PROD"],
                        }
                    },
                    "required": ["environment"],
                },
            },
        }
