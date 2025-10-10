# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class EnforceTexturePoliciesV2(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], files: List[str]) -> str:
        report = [{"file": f, "ok": True} for f in files]
        return json.dumps({"tex_report": report}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "enforce_texture_policies_v2", "description": "Deterministic texture checks (simulated).", "parameters": {"type": "object", "properties": {"files": {"type": "array", "items": {"type": "string"}}}, "required": ["files"]}}}
