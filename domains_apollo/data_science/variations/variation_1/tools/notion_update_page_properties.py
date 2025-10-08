from tau_bench.envs.tool import Tool
import json
from typing import Any

class NotionUpdatePageProperties(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        page_id: str = None,
        properties_json: str = None,
        updated_ts: str = None
    ) -> str:
        req = ["page_id", "properties_json"]
        err = _require({"page_id": page_id, "properties_json": properties_json}, req)
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
        page["properties_json_nullable"] = properties_json
        page["updated_ts"] = updated_ts if updated_ts is not None else page.get("updated_ts")
        payload = page
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "NotionUpdatePageProperties",
                "description": "Updates page properties JSON and updated_ts.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "page_id": {"type": "string"},
                        "properties_json": {"type": "string"},
                        "updated_ts": {"type": "string"},
                    },
                    "required": ["page_id", "properties_json"],
                },
            },
        }
