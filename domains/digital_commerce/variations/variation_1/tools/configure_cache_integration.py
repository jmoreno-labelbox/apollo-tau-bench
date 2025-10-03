from tau_bench.envs.tool import Tool
import json
from typing import Any

class ConfigureCacheIntegration(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        external_url: str,
        auth_header_secret_arn: str,
        partition_key: str
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
        _upsert("CacheAPI.ExternalSystemPartitionKey", partition_key)
        return _json(
            {
                "setting_ids": [
                    "CacheAPI.ExternalSystemURL",
                    "CacheAPI.ExternalSystemAuthHeader",
                    "CacheAPI.ExternalSystemPartitionKey",
                ],
                "verified": True,
            }
        )
        pass
        settings = _ensure_table(data, "custom_settings")

        def _upsert(name: str, value: str):
            pass
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
        _upsert("CacheAPI.ExternalSystemPartitionKey", partition_key)
        return _json(
            {
                "setting_ids": [
                    "CacheAPI.ExternalSystemURL",
                    "CacheAPI.ExternalSystemAuthHeader",
                    "CacheAPI.ExternalSystemPartitionKey",
                ],
                "verified": True,
            }
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ConfigureCacheIntegration",
                "description": "Point Commerce to the external cache (URL/auth/partition key).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "external_url": {"type": "string"},
                        "auth_header_secret_arn": {"type": "string"},
                        "partition_key": {"type": "string"},
                    },
                    "required": [
                        "external_url",
                        "auth_header_secret_arn",
                        "partition_key",
                    ],
                },
            },
        }
