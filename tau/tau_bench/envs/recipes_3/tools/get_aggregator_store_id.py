# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAggregatorStoreId(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], household_id: int) -> str:
        # Dynamically identify the aggregator store; select the initial aggregator platform store.
        stores = data.get("stores", [])
        agg = [s for s in stores if str(s.get("platform_enum")) == "aggregator"]
        sid = int(agg[0]["store_id"]) if agg else (int(stores[0]["store_id"]) if stores else 0)
        return json.dumps({"aggregator_store_id": sid})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_aggregator_store_id",
                "description": "Resolve aggregator store_id for a household using data (no hard-coding).",
                "parameters": {
                    "type": "object",
                    "properties": {"household_id": {"type": "integer"}},
                    "required": ["household_id"],
                },
            },
        }
