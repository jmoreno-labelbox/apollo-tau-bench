# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RunCanonicalPitchMap(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return json.dumps({"canonical_table": "pitches_canonical"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "run_canonical_pitch_map", "description": "Maps raw pitch types to canonical labels.", "parameters": {"type": "object", "properties": {"source_table": {"type": "string"}}}, "required": []}}
