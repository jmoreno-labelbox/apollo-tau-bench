from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class LinkCacheToOrg(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], org_id: str, cluster_id: str, partition_key: str
    ) -> str:
        org_id, cluster_id = _sid(org_id), _sid(cluster_id)
        partition_key = _sid(partition_key)
        clusters = data.get("aws_elasticache_clusters", [])
        cl = next((c for c in clusters if c.get("cluster_id") == cluster_id), None)
        if not cl:
            payload = {"error": f"cluster {cluster_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        if not (
            cl.get("status") == "available"
            and cl.get("endpoint_url") not in (None, "NULL", "")
        ):
            payload = {"error": "cluster not usable"}
            out = json.dumps(payload, indent=2)
            return out
        settings = data.get("custom_settings", [])
        url_setting = next(
            (
                s
                for s in settings
                if s.get("org_id") == org_id
                and s.get("setting_name") == "CacheAPI.ExternalSystemURL"
            ),
            None,
        )
        if url_setting:
            url_setting["value"] = cl.get("endpoint_url")
        pk_setting = next(
            (
                s
                for s in settings
                if s.get("org_id") == org_id
                and s.get("setting_name") == "CacheAPI.ExternalSystemPartitionKey"
            ),
            None,
        )
        if pk_setting:
            pk_setting["value"] = partition_key
        payload = {
            "org_id": org_id,
            "endpoint": cl.get("endpoint_url"),
            "partition_key": partition_key,
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
            

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "linkCacheToOrg",
                "description": "Set CacheAPI external URL and partition key for an org using a validated cluster.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "org_id": {"type": "string"},
                        "cluster_id": {"type": "string"},
                        "partition_key": {"type": "string"},
                    },
                    "required": ["org_id", "cluster_id", "partition_key"],
                },
            },
        }
