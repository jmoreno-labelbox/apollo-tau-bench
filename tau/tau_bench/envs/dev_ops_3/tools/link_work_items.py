from tau_bench.envs.tool import Tool
import json
from typing import Any

class link_work_items(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], parent_id: str, child_id: str, link_type: str
    ) -> str:
        pass
        links = data.get("work_item_links", [])
        new_link = {
            "parent_id": parent_id,
            "child_id": child_id,
            "link_type": link_type,
        }
        links.append(new_link)
        data["work_item_links"] = links
        link_id = f"link_{parent_id}_{child_id}"
        payload = {
                "success": f"Link of type '{link_type}' created between '{parent_id}' and '{child_id}'.",
                "link_id": link_id,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LinkWorkItems",
                "description": "Links two work items together with a specific relationship type.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "parent_id": {"type": "string"},
                        "child_id": {"type": "string"},
                        "link_type": {"type": "string"},
                    },
                    "required": ["parent_id", "child_id", "link_type"],
                },
            },
        }
