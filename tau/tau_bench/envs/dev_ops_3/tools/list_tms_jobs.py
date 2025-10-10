# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class list_tms_jobs(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        tms_jobs = data.get("tms_jobs", [])
        return json.dumps({"count": len(tms_jobs), "results": tms_jobs}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return { "type": "function", "function": { "name": "list_tms_jobs", "description": "Retrieves a list of all jobs in the Translation Management System (TMS).", "parameters": { "type": "object", "properties": {} } } }
