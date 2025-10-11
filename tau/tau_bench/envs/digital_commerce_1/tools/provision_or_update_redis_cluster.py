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

class ProvisionOrUpdateRedisCluster(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], cluster_name: str, node_type: str, replicas: int, environment: str
    ) -> str:
        clusters = _ensure_table(data, "aws_elasticache_clusters")
        cluster_id = _stable_id("rc", cluster_name, environment)
        endpoint = f"{cluster_name}.{environment.lower()}.cache.local:6379"
        row = _find_one(clusters, cluster_id=cluster_id)
        if row:
            row.update(
                {
                    "cluster_name": cluster_name,
                    "node_type": node_type,
                    "replicas": int(replicas),
                    "environment": environment,
                    "endpoint": endpoint,
                    "status": "available",
                }
            )
        else:
            clusters.append(
                {
                    "cluster_id": cluster_id,
                    "cluster_name": cluster_name,
                    "node_type": node_type,
                    "replicas": int(replicas),
                    "environment": environment,
                    "endpoint": endpoint,
                    "status": "available",
                    "require_auth": False,
                    "tls_in_transit": False,
                }
            )
        return _json({"cluster_id": cluster_id, "endpoint": endpoint, "status": "available"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "provision_or_update_redis_cluster",
                "description": "Provision or update an ElastiCache/Redis cluster for an environment.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cluster_name": {"type": "string"},
                        "node_type": {"type": "string"},
                        "replicas": {"type": "integer", "minimum": 0},
                        "environment": {"type": "string", "enum": ["DEV", "UAT", "PROD"]},
                    },
                    "required": ["cluster_name", "node_type", "replicas", "environment"],
                },
            },
        }