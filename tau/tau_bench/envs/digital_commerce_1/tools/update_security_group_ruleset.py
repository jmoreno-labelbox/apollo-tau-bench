# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _ensure_table










def _stable_id(prefix: str, *parts: str) -> str:
    base = "-".join(_slugify(p) for p in parts if p is not None and str(p) != "")
    return f"{prefix}-{base}" if base else prefix

def _json(x: Any) -> str:
    return json.dumps(x, separators=(",", ":"))

def _find_one(rows: List[Dict[str, Any]], **crit):
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

class UpdateSecurityGroupRuleset(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        sg_id: str,
        environment: str,
        service_name: str,
        tcp_ports: List[int],
        allowlist_cidrs: List[str],
    ) -> str:
        rules = _ensure_table(data, "aws_security_group_rules")
        for port in tcp_ports:
            for cidr in allowlist_cidrs:
                row = _find_one(
                    rules,
                    sg_id=sg_id,
                    environment=environment,
                    service_name=service_name,
                    direction="ingress",
                    protocol="tcp",
                    port=int(port),
                    cidr=cidr,
                )
                if row:
                    row["updated_at"] = FIXED_NOW
                else:
                    rules.append(
                        {
                            "sg_id": sg_id,
                            "environment": environment,
                            "service_name": service_name,
                            "direction": "ingress",
                            "protocol": "tcp",
                            "port": int(port),
                            "cidr": cidr,
                            "description": f"{service_name} [{environment}] ingress {port}/{cidr}",
                            "created_at": FIXED_NOW,
                        }
                    )
        summary = f"{service_name} [{environment}] ports={sorted(set(tcp_ports))} cidrs={sorted(set(allowlist_cidrs))}"
        return _json(
            {
                "change_set_id": _stable_id(
                    "chg-sg",
                    sg_id,
                    environment,
                    service_name,
                    *map(str, tcp_ports),
                    *allowlist_cidrs,
                ),
                "labels": {"summary": summary},
                "applied": True,
            }
        )

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "update_security_group_ruleset",
                "description": "Upsert ingress rules for an SG using env/service context.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sg_id": {"type": "string"},
                        "environment": {"type": "string", "enum": ["DEV", "UAT", "PROD"]},
                        "service_name": {"type": "string"},
                        "tcp_ports": {"type": "array", "items": {"type": "integer"}},
                        "allowlist_cidrs": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": [
                        "sg_id",
                        "environment",
                        "service_name",
                        "tcp_ports",
                        "allowlist_cidrs",
                    ],
                },
            },
        }