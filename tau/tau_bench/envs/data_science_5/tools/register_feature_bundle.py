from tau_bench.envs.tool import Tool
import json
from typing import Any

class RegisterFeatureBundle(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], feature_set_name: str = None, version: str = None, columns: list = None) -> str:
        feats = data.get("features", [])
        max_id = 0
        for f in feats:
            try:
                fid = int(f.get("feature_set_id", 0))
                if fid > max_id:
                    max_id = fid
            except (ValueError, TypeError):
                continue
        new_id = max_id + 1
        row = {
            "feature_set_id": new_id,
            "feature_set_name": feature_set_name,
            "version": version,
            "columns": columns,
            "created_at": _now_iso_fixed(),
        }
        feats.append(row)
        payload = {"feature_set_id": new_id, "feature_set_name": row["feature_set_name"]}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RegisterFeatureBundle",
                "description": "Create a feature-set descriptor record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "feature_set_name": {"type": "string"},
                        "version": {"type": "string"},
                        "columns": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["feature_set_name", "version", "columns"],
                },
            },
        }
