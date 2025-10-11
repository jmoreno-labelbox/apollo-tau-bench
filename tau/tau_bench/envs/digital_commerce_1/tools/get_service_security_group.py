# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _ensure_table
def _slugify(text: str, max_len: int = 40) -> str:
    s = str(text).lower()
    out = []
    prev_dash = False
    for ch in s:
        if ch.isalnum():
            out.append(ch)
            prev_dash = False
        else:
            if not prev_dash:
                out.append("-")
                prev_dash = True
    slug = "".join(out).strip("-")
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug[:max_len] if max_len > 0 else slug


def _stable_id(prefix: str, *parts: str) -> str:
    base = "-".join(_slugify(p) for p in parts if p is not None and str(p) != "")
    return f"{prefix}-{base}" if base else prefix

def _json(x: Any) -> str:
    return json.dumps(x, separators=(",", ":"))

def _find_all(rows: List[Dict[str, Any]], ) -> List[Dict[str, Any]]:
    out = []
    crit_items = sorted(crit.items(), key=lambda kv: kv[0])
    for r in rows:
        match = True
        for k, v in crit_items:
            if str(r.get(k)) != str(v):
                match = False
                break
        if match:
            out.append(r)
    return out

def _ensure_table(db: Dict[str, Any], name: str):
    if name not in db:
        db[name] = []
    return db[name]

class GetServiceSecurityGroup(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], environment: str, service_name: str) -> str:
        rules = _ensure_table(data, "aws_security_group_rules")
        matches = _find_all(rules, environment=environment, service_name=service_name)
        if matches:
            sg_id = matches[0]["sg_id"]
            ingress = [
                {"port": r["port"], "cidr": r["cidr"]}
                for r in matches
                if r.get("direction") == "ingress"
            ]
            egress = [
                {"port": r["port"], "cidr": r["cidr"]}
                for r in matches
                if r.get("direction") == "egress"
            ]
        else:
            sg_id = _stable_id("sg", environment, service_name)
            ingress, egress = [], []
        return _json(
            {
                "environment": environment,
                "service_name": service_name,
                "sg_id": sg_id,
                "name": f"{service_name} [{environment}]",
                "ingress_rules": ingress,
                "egress_rules": egress,
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_service_security_group",
                "description": "Find the security group for a service in an environment.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "environment": {"type": "string", "enum": ["DEV", "UAT", "PROD"]},
                        "service_name": {"type": "string"},
                    },
                    "required": ["environment", "service_name"],
                },
            },
        }