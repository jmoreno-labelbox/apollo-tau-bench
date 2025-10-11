# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _max_int_suffix(items: List[Dict[str, Any]], key: str, prefix: str, default: int = 0) -> int:
    max_val = default
    for it in items:
        raw = it.get(key)
        if isinstance(raw, str) and raw.startswith(prefix + "-"):
            try:
                num = int(raw.split("-")[-1])
                if num > max_val:
                    max_val = num
            except ValueError:
                continue
    return max_val

def _get_table(data: Dict[str, Any], name: str) -> List[Dict[str, Any]]:
    return data.setdefault(name, [])

class LinkTicketV2(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], project_key: str, run_id: str) -> str:
        work_items = _get_table(data, "work_items")
        prs = _get_table(data, "pull_requests")
        pr = next((p for p in prs if (p.get("links") or {}).get("run_id") == run_id), None)
        existing = next((w for w in work_items if w.get("run_id") == run_id and w.get("project_key") == project_key), None)
        if existing:
            existing.update({"pr_number": pr.get("pr_number") if pr else None})
            return json.dumps({"ticket_key": existing.get("ticket_key")}, indent=2)
        max_id = _max_int_suffix(work_items, "ticket_key", project_key, 0)
        ticket_key = f"{project_key}-{max_id + 1}"
        rec = {
            "ticket_key": ticket_key,
            "project_key": project_key,
            "summary": f"CI failure {run_id}",
            "description": f"Automated triage for {run_id}",
            "run_id": run_id,
            "pr_number": pr.get("pr_number") if pr else None,
            "state": "Open",
        }
        work_items.append(rec)
        return json.dumps({"ticket_key": ticket_key}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "link_ticket_v2", "description": "Creates or updates a work item linked deterministically to the run and PR.", "parameters": {"type": "object", "properties": {"project_key": {"type": "string"}, "run_id": {"type": "string"}}, "required": ["project_key", "run_id"]}}}