# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require


class NotionAppendSections(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], page_id, sections = [], updated_ts = page.get("updated_ts")) -> str:
        req = ["page_id"]
        err = _require(kwargs, req)
        if err: return err
        page = next((p for p in data.setdefault("notion_pages", []) if p.get("page_id") == page_id), None)
        if not page:
            return json.dumps({"error": f"page_id '{page_id}' not found"}, indent=2)
        existing = set(page.get("sections_present", []))
        page["sections_present"] = list(existing.union(sections))
        page["updated_ts"] = updated_ts
        return json.dumps(page, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "notion_append_sections",
            "description": "Appends sections to a Notion page's sections_present.",
            "parameters": {"type": "object", "properties": {
                "page_id": {"type": "string"},
                "sections": {"type": "array", "items": {"type": "string"}},
                "updated_ts": {"type": "string"}}, "required": ["page_id"]}}}
