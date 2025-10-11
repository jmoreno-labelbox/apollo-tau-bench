# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _get_network_defaults
def _find_one(rows: List[Dict[str, Any]], ):
    crit_items = sorted(crit.items(), key=lambda kv: kv[0])
    for r in rows:
        match = True
        for k, v in crit_items:
            if str(r.get(k)) != str(v):
                match = False
                break
        if match:
            return r
    return None


def _ensure_table(db: Dict[str, Any], name: str):
    if name not in db:
        db[name] = []
    return db[name]


def _json(x: Any) -> str:
    return json.dumps(x, separators=(",", ":"))

def _get_network_defaults(db: Dict[str, Any], environment: str) -> Dict[str, Any]:
    subnets = _ensure_table(db, "aws_subnet_groups")
    row = _find_one(subnets, environment=environment)
    vpc_id = row.get("vpc_id") if row else f"vpc-{environment.lower()}-0001"
    sn = (
        row.get("subnet_ids")
        if row and row.get("subnet_ids")
        else [f"subnet-{environment.lower()}-a", f"subnet-{environment.lower()}-b"]
    )
    allow = row.get("allowlist_cidrs") if row and row.get("allowlist_cidrs") else ["10.0.0.0/16"]
    return {
        "vpc_id": vpc_id,
        "subnet_ids": sn,
        "allowlist_cidrs": allow,
        "tls_ports": [443],
        "redis_ports": [6379],
    }

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