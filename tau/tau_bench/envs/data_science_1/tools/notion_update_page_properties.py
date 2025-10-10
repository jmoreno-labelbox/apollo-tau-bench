# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require


class NotionUpdatePageProperties(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        req = ["page_id", "properties_json"]
        err = _require(kwargs, req)
        if err: return err
        page = next((p for p in data.setdefault("notion_pages", []) if p.get("page_id") == kwargs["page_id"]), None)
        if not page:
            return json.dumps({"error": f"page_id '{kwargs['page_id']}' not found"}, indent=2)
        page["properties_json_nullable"] = kwargs["properties_json"]
        page["updated_ts"] = kwargs.get("updated_ts", page.get("updated_ts"))
        return json.dumps(page, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "notion_update_page_properties",
            "description": "Updates page properties JSON and updated_ts.",
            "parameters": {"type": "object", "properties": {
                "page_id": {"type": "string"}, "properties_json": {"type": "string"}, "updated_ts": {"type": "string"}},
                "required": ["page_id", "properties_json"]}}}
