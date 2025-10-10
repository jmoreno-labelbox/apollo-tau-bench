# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class EnrichNotion(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], model_id, page_id) -> str:

        zotero_id = "ZOTERO_001"
        entry = {
            "page_id": page_id,
            "model_id": model_id,
            "zotero_id": zotero_id,
        }

        data.setdefault("zotero_metadata", []).append(entry)

        return json.dumps(entry)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "EnrichNotion",
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
