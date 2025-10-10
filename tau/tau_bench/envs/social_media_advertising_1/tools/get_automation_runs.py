# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAutomationRuns(Tool):
    """Retrieves all automation run IDs."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        runs = list(data.get("automation_runs", {}).values())
        ids_ = []
        for i in runs:
            ids_ += [i.get("run_id")]
        return json.dumps({"automation_run_ids": ids_})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_automation_runs",
                "description": "Retrieves all automation run IDs.",
                "parameters": {},
            },
        }
