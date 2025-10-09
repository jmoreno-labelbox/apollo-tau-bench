from tau_bench.envs.tool import Tool
import json
from typing import Any

class LookupRelationV2(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], ticket_key: str) -> str:
        pass
        links = _get_table(data, "bug_links")
        link = next(
            (
                l
                for l in links
                if l.get("primary_bug_id") == ticket_key
                or l.get("related_bug_id") == ticket_key
            ),
            None,
        )
        if not link:
            payload = {"relation_type": None, "other": None}
            out = json.dumps(payload, indent=2)
            return out
        if link.get("primary_bug_id") == ticket_key:
            other = link.get("related_bug_id")
        else:
            other = link.get("primary_bug_id")
        payload = {
                "relation_type": link.get("relation_type"),
                "primary": link.get("primary_bug_id"),
                "related": link.get("related_bug_id"),
                "other": other,
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
                "name": "LookupRelationV2",
                "description": "Finds a relation link (duplicate/related/etc.) for a ticket from bug_links.json.",
                "parameters": {
                    "type": "object",
                    "properties": {"ticket_key": {"type": "string"}},
                    "required": ["ticket_key"],
                },
            },
        }
