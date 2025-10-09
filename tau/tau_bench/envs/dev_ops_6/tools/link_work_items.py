from tau_bench.envs.tool import Tool
import json
from typing import Any

class LinkWorkItems(Tool):
    """Establish or verify a link {parent_id, child_id, link_type} (idempotent)."""

    @staticmethod
    def invoke(data: dict[str, Any], parent_id: str = None, child_id: str = None, link_type: str = "relates_to") -> str:
        if not parent_id or not child_id:
            return _err("parent_id and child_id are required")
        if parent_id == child_id:
            return _err("cannot link an item to itself")
        links = _table(data, "work_item_links")
        for l in links:
            if (
                l.get("parent_id") == parent_id
                and l.get("child_id") == child_id
                and (l.get("link_type") == link_type)
            ):
                return _ok(
                    {
                        "message": "link already exists",
                        "parent_id": parent_id,
                        "child_id": child_id,
                        "link_type": link_type,
                    }
                )
        links.append(
            {"parent_id": parent_id, "child_id": child_id, "link_type": link_type}
        )
        return _ok(
            {
                "created_link": {
                    "parent_id": parent_id,
                    "child_id": child_id,
                    "link_type": link_type,
                }
            }
        )
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "linkWorkItems",
                "description": "Link two work items (parent/child/link_type).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "parent_id": {"type": "string"},
                        "child_id": {"type": "string"},
                        "link_type": {"type": "string"},
                    },
                    "required": ["parent_id", "child_id"],
                },
            },
        }
