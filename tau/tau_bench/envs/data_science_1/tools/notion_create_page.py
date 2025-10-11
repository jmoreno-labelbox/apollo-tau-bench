# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require






def _require(kwargs: Dict[str, Any], required: List[str]) -> Optional[str]:
    missing = [k for k in required if kwargs.get(k) is None]
    if missing:
        return json.dumps({"error": f"Missing required arguments: {', '.join(missing)}"}, indent=2)
    return None

def _append(table: List[Dict[str, Any]], row: Dict[str, Any]) -> Dict[str, Any]:
    table.append(row)
    return row

class NotionCreatePage(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], created_ts, page_id, properties_json_nullable, title, updated_ts, url_nullable, sections_present = []) -> str:
        req = ["page_id", "title"]
        err = _require(kwargs, req)
        if err: return err
        row = {"page_id": page_id, "title": title, "url_nullable": url_nullable,
               "properties_json_nullable": properties_json_nullable,
               "sections_present": sections_present,
               "created_ts": created_ts, "updated_ts": updated_ts}
        return json.dumps(_append(data.setdefault("notion_pages", []), row), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "notion_create_page",
            "description": "Creates a Notion page record.",
            "parameters": {"type": "object", "properties": {
                "page_id": {"type": "string"}, "title": {"type": "string"},
                "url_nullable": {"type": "string"}, "properties_json_nullable": {"type": "string"},
                "sections_present": {"type": "array", "items": {"type": "string"}},
                "created_ts": {"type": "string"}, "updated_ts": {"type": "string"}},
                "required": ["page_id", "title"]}}}