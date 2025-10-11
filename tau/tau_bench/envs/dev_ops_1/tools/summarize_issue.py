# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _get_table(data: Dict[str, Any], name: str) -> List[Dict[str, Any]]:
    return data.setdefault(name, [])

def _error(msg: str) -> str:
    return json.dumps({"error": msg}, indent=2)

class SummarizeIssue(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], ticket_key: str) -> str:
        work_items = _get_table(data, "work_items")
        item = next((w for w in work_items if w.get("ticket_key") == ticket_key), None)
        if not item:
            return _error(f"Ticket '{ticket_key}' not found.")
        norm = item.get("normalized") or {}
        desc = (norm.get("description") or "")[:140]
        summary = f"{norm.get('title') or 'Issue'} :: {desc}"
        item["summary_text"] = summary
        return json.dumps({"summary_text": summary}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "summarize_issue", "description": "Creates a deterministic short summary from normalized fields.", "parameters": {"type": "object", "properties": {"ticket_key": {"type": "string"}}, "required": ["ticket_key"]}}}