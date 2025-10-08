from tau_bench.envs.tool import Tool
import json
from typing import Any

class NotionAppendSections(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], page_id: str, sections: list = None, updated_ts: str = None) -> str:
        if sections is None:
            sections = []
        req = ["page_id"]
        err = _require({"page_id": page_id}, req)
        if err:
            return err
        page = next(
            (
                p
                for p in data.setdefault("notion_pages", [])
                if p.get("page_id") == page_id
            ),
            None,
        )
        if not page:
            payload = {"error": f"page_id '{page_id}' not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        existing = set(page.get("sections_present", []))
        page["sections_present"] = list(existing.union(sections))
        page["updated_ts"] = updated_ts if updated_ts is not None else page.get("updated_ts")
        payload = page
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "NotionAppendSections",
                "description": "Appends sections to a Notion page's sections_present.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "page_id": {"type": "string"},
                        "sections": {"type": "array", "items": {"type": "string"}},
                        "updated_ts": {"type": "string"},
                    },
                    "required": ["page_id"],
                },
            },
        }
