# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class Pithcmapping(Tool):
    @staticmethod
        # main invoke function
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        # return result
        return json.dumps({"canonical_table": "pitches_canonical"}, indent=2)

    @staticmethod
        # info metadata
    def get_info() -> Dict[str, Any]:
        # return result
        return {"type": "function", "function": {"name": "mappings", "description": "Transforms raw pitch types to canonical labels.", "parameters": {"type": "object", "properties": {"source_table": {"type": "string"}}}, "required": []}}
