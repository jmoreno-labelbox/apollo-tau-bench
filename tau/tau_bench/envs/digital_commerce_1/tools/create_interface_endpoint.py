# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _ensure_table


class CreateInterfaceEndpoint(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], vpc_id: str, service_name: str, subnet_ids: List[str]) -> str:
        endpoints = _ensure_table(data, "aws_vpc_endpoints")
        endpoint_id = _stable_id("vpce", vpc_id, service_name, *subnet_ids)
        dns = f"{endpoint_id}.vpce.local"
        row = _find_one(endpoints, endpoint_id=endpoint_id)
        if row:
            row["dns_entries"] = [dns]
        else:
            endpoints.append(
                {
                    "endpoint_id": endpoint_id,
                    "vpc_id": vpc_id,
                    "service_name": service_name,
                    "subnet_ids": list(subnet_ids),
                    "dns_entries": [dns],
                }
            )
        return _json({"endpoint_id": endpoint_id, "dns_entries": [dns]})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_interface_endpoint",
                "description": "Create a VPC Interface Endpoint for a service.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "vpc_id": {"type": "string"},
                        "service_name": {"type": "string"},
                        "subnet_ids": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["vpc_id", "service_name", "subnet_ids"],
                },
            },
        }
