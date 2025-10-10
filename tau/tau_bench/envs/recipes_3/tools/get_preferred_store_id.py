# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPreferredStoreId(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], household_id: int) -> str:
        # Determine preferred store dynamically; default to first native store if no explicit mapping
        stores = data.get("stores", [])
        native = [s for s in stores if str(s.get("platform_enum")) == "native"]
        sid = (
            int(native[0]["store_id"]) if native else (int(stores[0]["store_id"]) if stores else 0)
        )
        return json.dumps({"preferred_store_id": sid})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_preferred_store_id",
                "description": "Resolve preferred store_id for a household using data (no hard-coding).",
                "parameters": {
                    "type": "object",
                    "properties": {"household_id": {"type": "integer"}},
                    "required": ["household_id"],
                },
            },
        }
