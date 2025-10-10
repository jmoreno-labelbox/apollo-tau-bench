# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class EngineBudgetProbeV2(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], files: List[str], scene: str) -> str:
        report = {"scene": scene, "files": files, "violations": []}
        return json.dumps({"engine_report": report}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "engine_budget_probe_v2", "description": "Runs deterministic engine budget checks (simulated).", "parameters": {"type": "object", "properties": {"files": {"type": "array", "items": {"type": "string"}}, "scene": {"type": "string"}}, "required": ["files", "scene"]}}}
