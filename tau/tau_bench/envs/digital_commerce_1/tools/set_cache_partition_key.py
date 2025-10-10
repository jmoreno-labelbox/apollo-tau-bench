# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SetCachePartitionKey(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], partition_key: str, version: str) -> str:
        settings = _ensure_table(data, "custom_settings")
        name = "CacheAPI.ExternalSystemPartitionKeyVersion"
        row = _find_one(settings, name=name)
        if row:
            row["value"] = version
            row["updated_at"] = FIXED_NOW
        else:
            settings.append(
                {
                    "setting_id": _stable_id("cs", name),
                    "name": name,
                    "value": version,
                    "updated_at": FIXED_NOW,
                }
            )
        return _json({"applied_version": version})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "set_cache_partition_key",
                "description": "Set the cache partition key version.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "partition_key": {"type": "string"},
                        "version": {"type": "string"},
                    },
                    "required": ["partition_key", "version"],
                },
            },
        }
