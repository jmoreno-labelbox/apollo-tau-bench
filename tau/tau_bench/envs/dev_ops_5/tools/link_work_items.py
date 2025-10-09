from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class LinkWorkItems(Tool):
    """Connects two work items (e.g., as duplicates or related items)."""

    @staticmethod
    def invoke(data: dict[str, Any], parent_id: str = None, child_id: str = None, link_type: str = None) -> str:
        links = data.get("work_item_links", {}).values()
        max([int(w["parent_id"].split("_")[1]) for w in links]) + 1

        new_link = {
            "parent_id": parent_id,
            "child_id": child_id,
            "link_type": link_type,
        }
        data["work_item_links"][new_link["work_item_link_id"]] = new_link
        payload = {
            "status": "success",
            "message": f"Linked {child_id} to {parent_id} as {link_type}.",
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LinkWorkItems",
                "description": "Links two work items together.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "parent_id": {"type": "string"},
                        "child_id": {"type": "string"},
                        "link_type": {
                            "type": "string",
                            "enum": [
                                "epic",
                                "dependency",
                                "related",
                                "blocks",
                                "implements",
                                "duplicate",
                            ],
                        },
                    },
                    "required": ["parent_id", "child_id", "link_type"],
                },
            },
        }
