# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AllocateTrackingId(Tool):
    """Allocate a new tracking_id string based on courier_id and a caller-provided seed."""
    @staticmethod
    def invoke(data, courier_id, seed) -> str:
        if not courier_id or seed is None:
            return json.dumps({"error":"courier_id and seed are required"}, indent=2)
        new_id = f"TRK-{courier_id.strip('#')}-{str(seed)}"
        return json.dumps({"tracking_id": new_id}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"allocate_tracking_id","description":"Return a tracking id for a courier based on a numeric/string seed.","parameters":{"type":"object","properties":{"courier_id":{"type":"string"},"seed":{}},"required":["courier_id","seed"]}}}
