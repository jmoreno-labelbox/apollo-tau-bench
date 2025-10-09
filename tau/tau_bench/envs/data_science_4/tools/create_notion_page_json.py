from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateNotionPageJson(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        title: str = None,
        parent_database_id_nullable: str = None,
        parent_page_id_nullable: str = None,
        icon_emoji_nullable: str = None,
        cover_image_url_nullable: str = None,
        tags: list = None,
        status_nullable: str = None,
        properties: dict = None,
        blocks: list = None,
        attachments_paths: list = None
    ) -> str:
        """Generates a Notion-like page JSON (including metadata and block structure). Does NOT interact with Notion; solely documents a consistent JSON artifact."""
        if not title:
            payload = {"error": "title is required"}
            out = json.dumps(payload)
            return out

        page_id = "NOTION_PAGE_001"  # consistent for evaluations
        slug = "_".join(title.lower().split())
        json_path = f"/notion/pages/{page_id}.json"

        page_entry = {
            "page_id": page_id,
            "title": title,
            "parent_database_id_nullable": parent_database_id_nullable,
            "parent_page_id_nullable": parent_page_id_nullable,
            "icon_emoji_nullable": icon_emoji_nullable,
            "cover_image_url_nullable": cover_image_url_nullable,
            "tags": tags or [],
            "status_nullable": status_nullable,
            "properties": properties or {},  # for example, {"Model":"SF_V1","AUC":0.87}
            "blocks": blocks or [],  # for instance, [{"type":"heading_2","text":"Overview"}, ...]
            "attachments_paths": attachments_paths or [],
            "json_path": json_path,
            "slug": slug,
        }

        data.setdefault("notion_pages.json", []).append(page_entry)
        payload = {"page_id": page_id, "json_path": json_path}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createNotionPageJson",
                "description": "Creates a Notion-style page JSON (metadata + block structure + attachments).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "title": {"type": "string"},
                        "parent_database_id_nullable": {"type": "string"},
                        "parent_page_id_nullable": {"type": "string"},
                        "icon_emoji_nullable": {"type": "string"},
                        "cover_image_url_nullable": {"type": "string"},
                        "tags": {"type": "array", "items": {"type": "string"}},
                        "status_nullable": {"type": "string"},
                        "properties": {"type": "object"},
                        "blocks": {"type": "array", "items": {"type": "object"}},
                        "attachments_paths": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                    "required": ["title"],
                },
            },
        }
