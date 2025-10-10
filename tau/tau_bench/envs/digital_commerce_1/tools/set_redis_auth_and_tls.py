# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SetRedisAuthAndTLS(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        cluster_id: str,
        require_auth: bool = True,
        tls_in_transit: bool = True,
    ) -> str:
        clusters = _ensure_table(data, "aws_elasticache_clusters")
        row = _find_one(clusters, cluster_id=cluster_id) or _find_one(
            clusters, cluster_name=cluster_id
        )
        if not row:
            raise ValueError(f"Cluster not found: {cluster_id}")
        env = row.get("environment", "UAT")
        kms_key_alias = f"alias/dcomm-{env.lower()}"
        row.update(
            {
                "require_auth": bool(require_auth),
                "tls_in_transit": bool(tls_in_transit),
                "kms_key_alias": kms_key_alias,
                "secret_arn": f"arn:aws:secretsmanager:local:000000000000:secret:{row.get('cluster_id', cluster_id)}",
                "updated_at": FIXED_NOW,
            }
        )
        return _json(
            {
                "secret_arn": row["secret_arn"],
                "tls_status": "enabled" if row["tls_in_transit"] else "disabled",
                "kms_key_alias": kms_key_alias,
            }
        )

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "set_redis_auth_and_tls",
                "description": "Enable AUTH/TLS; booleans default to True if omitted.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cluster_id": {"type": "string"},
                        "require_auth": {"type": "boolean"},
                        "tls_in_transit": {"type": "boolean"},
                    },
                    "required": ["cluster_id"],
                },
            },
        }
