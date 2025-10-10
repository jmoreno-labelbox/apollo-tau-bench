# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LookupRelationV2(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], ticket_key: str) -> str:
        links = _get_table(data, "bug_links")
        link = next((l for l in links if l.get("primary_bug_id") == ticket_key or l.get("related_bug_id") == ticket_key), None)
        if not link:
            return json.dumps({"relation_type": None, "other": None}, indent=2)
        if link.get("primary_bug_id") == ticket_key:
            other = link.get("related_bug_id")
        else:
            other = link.get("primary_bug_id")
        return json.dumps({"relation_type": link.get("relation_type"), "primary": link.get("primary_bug_id"), "related": link.get("related_bug_id"), "other": other}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "lookup_relation_v2", "description": "Finds a relation link (duplicate/related/etc.) for a ticket from bug_links.json.", "parameters": {"type": "object", "properties": {"ticket_key": {"type": "string"}}, "required": ["ticket_key"]}}}
