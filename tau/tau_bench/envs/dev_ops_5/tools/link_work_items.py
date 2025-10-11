# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LinkWorkItems(Tool):
    """Links two work items together (e.g., as duplicate or related)."""
    @staticmethod
    def invoke(data: Dict[str, Any], child_id, link_type, parent_id) -> str:
        links = data.get("work_item_links", [])
        new_id_num = max([int(w["parent_id"].split("_")[1]) for w in links]) + 1
        
        new_link = {
            "parent_id": parent_id,
            "child_id": child_id,
            "link_type": link_type,
        }
        links.append(new_link)
        return json.dumps({"status": "success", "message": f"Linked {child_id} to {parent_id} as {link_type}."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "link_work_items",
                "description": "Links two work items together.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "parent_id": {"type": "string"},
                        "child_id": {"type": "string"},
                        "link_type": {"type": "string", "enum": ["epic", "dependency", "related", "blocks", "implements", "duplicate"]}
                    },
                    "required": ["parent_id", "child_id", "link_type"],
                },
            },
        }
