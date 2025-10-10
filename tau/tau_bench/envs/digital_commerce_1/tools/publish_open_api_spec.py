# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class PublishOpenAPISpec(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], spec_name: str, spec_version: str, spec_blob_id: str) -> str:
        settings = _ensure_table(data, "custom_settings")
        spec_id = _stable_id("spec", spec_name, spec_version)
        name = f"OpenAPI:{spec_name}"
        value = json.dumps({"spec_id": spec_id, "version": spec_version, "blob": spec_blob_id})
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
        return _json({"spec_id": spec_id, "version": spec_version})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "publish_openapi_spec",
                "description": "Publish/register an OpenAPI spec artifact.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "spec_name": {"type": "string"},
                        "spec_version": {"type": "string"},
                        "spec_blob_id": {"type": "string"},
                    },
                    "required": ["spec_name", "spec_version", "spec_blob_id"],
                },
            },
        }
