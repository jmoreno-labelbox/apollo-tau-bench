# Copyright Sierra Inc.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class Pithcmapping(Tool):
    @staticmethod
        # primary execution method
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        # return outcome
        return json.dumps({"canonical_table": "pitches_canonical"}, indent=2)

    @staticmethod
        # metadata information
    def get_info() -> Dict[str, Any]:
        # return outcome
        return {"type": "function", "function": {"name": "mappings", "description": "Transforms raw pitch types to canonical labels.", "parameters": {"type": "object", "properties": {"source_table": {"type": "string"}}}, "required": []}}
