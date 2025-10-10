# Copyright by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LinkWorkItems(Tool):
    """Links two work items together (e.g., as duplicate or related)."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        links = data.get("work_item_links", [])
        new_id_num = max([int(w["parent_id"].split("_")[1]) for w in links]) + 1
        
        new_link = {
            "parent_id": kwargs.get("parent_id"),
            "child_id": kwargs.get("child_id"),
            "link_type": kwargs.get("link_type"),
        }
        links.append(new_link)
        return json.dumps({"status": "success", "message": f"Linked {kwargs.get('child_id')} to {kwargs.get('parent_id')} as {kwargs.get('link_type')}."})

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
