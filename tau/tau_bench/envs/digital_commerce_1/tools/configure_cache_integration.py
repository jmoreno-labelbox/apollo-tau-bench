# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _ensure_table


class ConfigureCacheIntegration(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], external_url: str, auth_header_secret_arn: str, partition_key: Optional[str] = None
    ) -> str:
        settings = _ensure_table(data, "custom_settings")

        def _upsert(name: str, value: str):
            row = _find_one(settings, name=name)
            if row:
                row["value"] = value
                row["updated_at"] = FIXED_NOW
            else:
                settings.append(
                    {
                        "setting_id": _stable_id("cs", name),
                        "name": name,
                        "value": value,
                        "updated_at": FIXED_NOW,
                    }
                )

        _upsert("CacheAPI.ExternalSystemURL", external_url)
        _upsert("CacheAPI.ExternalSystemAuthHeader", auth_header_secret_arn)
        if partition_key:
            _upsert("CacheAPI.ExternalSystemPartitionKey", partition_key)
        return _json(
            {
                "setting_ids": [
                    "CacheAPI.ExternalSystemURL",
                    "CacheAPI.ExternalSystemAuthHeader",
                    *([
                        "CacheAPI.ExternalSystemPartitionKey",
                    ] if partition_key else []),
                ],
                "verified": True,
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "configure_cache_integration",
                "description": "Point Commerce to the external cache (URL/auth/partition key).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "external_url": {"type": "string"},
                        "auth_header_secret_arn": {"type": "string"},
                        "partition_key": {"type": "string", "description": "Optional, uses default value if omitted."},
                    },
                    "required": ["external_url", "auth_header_secret_arn"],
                },
            },
        }
