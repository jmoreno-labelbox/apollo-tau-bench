from tau_bench.envs.tool import Tool
import json
from typing import Any

class EnrichNotion(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], page_id: str = None, model_id: str = None) -> str:
        zotero_id = "ZOTERO_001"
        entry = {
            "page_id": page_id,
            "model_id": model_id,
            "zotero_id": zotero_id,
        }

        data.setdefault("zotero_metadata", []).append(entry)
        payload = entry
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "enrichNotion",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "predictions_id": {
                            "type": "string",
                            "description": "The ID of the final predictions.",
                        },
                        "metrics_id": {
                            "type": "string",
                            "description": "The ID of the final metrics.",
                        },
                    },
                    "required": [],
                },
            },
        }
