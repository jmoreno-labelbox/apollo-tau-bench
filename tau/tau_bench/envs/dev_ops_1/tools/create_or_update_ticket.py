# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateOrUpdateTicket(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], project_key: str, summary: str, description: str, run_id: str, pr_number: Optional[int] = None) -> str:
        work_items = _get_table(data, "work_items")
        existing = next((w for w in work_items if w.get("run_id") == run_id and w.get("project_key") == project_key), None)
        if existing:
            existing.update({"summary": summary, "description": description, "pr_number": pr_number})
            return json.dumps({"ticket_key": existing.get("ticket_key")}, indent=2)
        max_id = _max_int_suffix(work_items, "ticket_key", project_key, 0)
        ticket_key = f"{project_key}-{max_id + 1}"
        rec = {"ticket_key": ticket_key, "project_key": project_key, "summary": summary, "description": description, "run_id": run_id, "pr_number": pr_number, "state": "Open"}
        work_items.append(rec)
        return json.dumps({"ticket_key": ticket_key}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_or_update_ticket", "description": "Creates or updates a deterministic work item ticket keyed by project and run_id.", "parameters": {"type": "object", "properties": {"project_key": {"type": "string"}, "summary": {"type": "string"}, "description": {"type": "string"}, "run_id": {"type": "string"}, "pr_number": {"type": "integer"}}, "required": ["project_key", "summary", "description", "run_id"]}}}
