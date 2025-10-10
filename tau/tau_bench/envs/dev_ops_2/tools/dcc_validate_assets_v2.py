# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DccValidateAssetsV2(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], files: List[str]) -> str:
        results = [{"file": f, "issues": []} for f in files]
        return json.dumps({"qa_json": results}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "dcc_validate_assets_v2", "description": "Returns deterministic headless DCC validation results (simulated).", "parameters": {"type": "object", "properties": {"files": {"type": "array", "items": {"type": "string"}}}, "required": ["files"]}}}
