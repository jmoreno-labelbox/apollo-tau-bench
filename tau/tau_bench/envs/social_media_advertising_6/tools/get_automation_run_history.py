# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAutomationRunHistory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        # optional filters by type
        rtype = kwargs.get("run_type")
        runs = _assert_table(data, "automation_runs")
        out = [r for r in runs if (rtype is None or r.get("run_type") == rtype)]
        return json.dumps(out)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_automation_run_history",
                                                 "description": "Read automation_runs (optionally filter by run_type).",
                                                 "parameters": {"type": "object",
                                                                "properties": {"run_type": {"type": "string"}}}}}
