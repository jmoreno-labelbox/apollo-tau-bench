from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class BuildFeatureValidationRunId(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], city_slug: str = None, model_name: str = None, created_ts: str = None) -> str:
        if not city_slug or not model_name or not created_ts:
            payload = {"error": "Missing city_slug, model_name or created_ts"}
            out = json.dumps(payload)
            return out
        ymd = created_ts[:10].replace("-", "")
        run_id = f"fv_{city_slug}_{model_name}_{ymd}_v1"
        payload = {"run_id": run_id, "ymd": ymd}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "BuildFeatureValidationRunId",
                "description": "Builds canonical run_id for feature validation from city_slug, model_name, and created_ts.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city_slug": {"type": "string"},
                        "model_name": {"type": "string"},
                        "created_ts": {"type": "string"},
                    },
                    "required": ["city_slug", "model_name", "created_ts"],
                },
            },
        }
