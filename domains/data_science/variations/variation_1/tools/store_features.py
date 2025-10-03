from tau_bench.envs.tool import Tool
import json
from typing import Any

class StoreFeatures(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        csv_path: str = None,
        definitions_nullable: Any = None,
        feature_names: list[str] = None,
        generated_ts: Any = None
    ) -> str:
        err = _require({"csv_path": csv_path, "feature_names": feature_names}, ["csv_path", "feature_names"])
        if err:
            return err
        row = {
            "csv_path": csv_path,
            "feature_names": feature_names,
            "definitions_nullable": definitions_nullable,
            "generated_ts": generated_ts,
        }
        payload = _append(data.setdefault("features", []), row)
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "StoreFeatures",
                "description": "Stores feature list metadata for a generated CSV.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "csv_path": {"type": "string"},
                        "feature_names": {"type": "array", "items": {"type": "string"}},
                        "definitions_nullable": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "generated_ts": {"type": "string"},
                    },
                    "required": ["csv_path", "feature_names"],
                },
            },
        }
