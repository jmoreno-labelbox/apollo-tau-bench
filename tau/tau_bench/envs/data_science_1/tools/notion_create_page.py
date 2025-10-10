# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require


class NotionCreatePage(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        req = ["page_id", "title"]
        err = _require(kwargs, req)
        if err: return err
        row = {"page_id": kwargs["page_id"], "title": kwargs["title"], "url_nullable": kwargs.get("url_nullable"),
               "properties_json_nullable": kwargs.get("properties_json_nullable"),
               "sections_present": kwargs.get("sections_present", []),
               "created_ts": kwargs.get("created_ts"), "updated_ts": kwargs.get("updated_ts")}
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
