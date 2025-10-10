# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListTimeEntries(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], month, project_id) -> str:
        pid = project_id
        entries = [t for t in list(data.get("time_entries", {}).values()) if t.get("project_id") == pid]
        if month:
            entries = [t for t in entries if str(t.get("entry_date", "")).startswith(month)]
        return json.dumps({"project_id": pid,"month": month,"time_entries": entries}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "list_time_entries","description": "List time entries filtered by project and optional month.","parameters": {"type": "object","properties": {"project_id": {"type": "string"},"month": {"type": "string"}},"required": ["project_id"]}}}
