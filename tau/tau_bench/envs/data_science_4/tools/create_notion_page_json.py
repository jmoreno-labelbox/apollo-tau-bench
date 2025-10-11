# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateNotionPageJson(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], cover_image_url_nullable, icon_emoji_nullable, parent_database_id_nullable, parent_page_id_nullable, status_nullable, title, attachments_paths = [], blocks = [], properties = {}, tags = []) -> str:
        """
        Creates a Notion-style page JSON (metadata + block structure).
        Does NOT call Notion; only records a deterministic JSON artifact.
        """
        if not title:
            return json.dumps({"error": "title is required"})

        page_id = "NOTION_PAGE_001"  # predictable for evaluations
        slug = "_".join(title.lower().split())
        json_path = f"/notion/pages/{page_id}.json"

        page_entry = {
            "page_id": page_id,
            "title": title,
            "parent_database_id_nullable": parent_database_id_nullable,
            "parent_page_id_nullable": parent_page_id_nullable,
            "icon_emoji_nullable": icon_emoji_nullable,
            "cover_image_url_nullable": cover_image_url_nullable,
            "tags": tags,
            "status_nullable": status_nullable,
            "properties": properties,  # for example, {"Model":"SF_V1","AUC":0.87}
            "blocks": blocks,  # for example, [{"type":"heading_2","text":"Summary"}, ...]
            "attachments_paths": attachments_paths,
            "json_path": json_path,
            "slug": slug,
        }

        data.setdefault("notion_pages.json", []).append(page_entry)
        return json.dumps({"page_id": page_id, "json_path": json_path})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateNotionPageJson",
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
