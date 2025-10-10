# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCreativeRotationHistory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        aid = kwargs.get("adset_id")
        rows = _assert_table(data, "creative_rotations")
        out = [r for r in rows if (aid is None or str(r.get("adset_id")) == str(aid))]
        return json.dumps(out)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_creative_rotation_history",
                                                 "description": "List rotation logs (optionally by adset).",
                                                 "parameters": {"type": "object",
                                                                "properties": {"adset_id": {"type": "string"}}}}}
