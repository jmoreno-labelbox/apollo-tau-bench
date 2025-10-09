from tau_bench.envs.tool import Tool
import json
from typing import Any

class NotionCreatePage(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        created_ts: str = None,
        page_id: str = None,
        properties_json_nullable: str = None,
        sections_present: list = None,
        title: str = None,
        updated_ts: str = None,
        url_nullable: str = None
    ) -> str:
        if sections_present is None:
            sections_present = []
        req = ["page_id", "title"]
        err = _require({"page_id": page_id, "title": title}, req)
        if err:
            return err
        row = {
            "page_id": page_id,
            "title": title,
            "url_nullable": url_nullable,
            "properties_json_nullable": properties_json_nullable,
            "sections_present": sections_present,
            "created_ts": created_ts,
            "updated_ts": updated_ts,
        }
        payload = _append(data.setdefault("notion_pages", []), row)
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "NotionCreatePage",
                "description": "Creates a Notion page record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "page_id": {"type": "string"},
                        "title": {"type": "string"},
                        "url_nullable": {"type": "string"},
                        "properties_json_nullable": {"type": "string"},
                        "sections_present": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "created_ts": {"type": "string"},
                        "updated_ts": {"type": "string"},
                    },
                    "required": ["page_id", "title"],
                },
            },
        }
