# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _get_table(data: Dict[str, Any], name: str) -> List[Dict[str, Any]]:
    return data.setdefault(name, [])

class FindCanonicalDuplicateV2(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], ticket_key: str) -> str:
        dedups = _get_table(data, "bug_deduplication")
        links = _get_table(data, "bug_links")
        # Prioritize the explicit deduplication table initially.
        row = next((d for d in dedups if d.get("new_bug_id") == ticket_key and (d.get("status") in ("confirmed_duplicate", "new_bug") or d.get("status"))), None)
        if row and row.get("canonical_bug_id"):
            return json.dumps({"canonical_bug_id": row.get("canonical_bug_id")}, indent=2)
        # Revert to bug_links for duplicate relation_type.
        link = next((l for l in links if l.get("relation_type") == "duplicate" and (l.get("primary_bug_id") == ticket_key or l.get("related_bug_id") == ticket_key)), None)
        if link:
            if link.get("primary_bug_id") == ticket_key:
                other = link.get("related_bug_id")
            else:
                other = link.get("primary_bug_id")
            return json.dumps({"canonical_bug_id": other}, indent=2)
        return json.dumps({"canonical_bug_id": None}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "find_canonical_duplicate_v2", "description": "Looks up canonical duplicate for a ticket from bug_deduplication or bug_links.", "parameters": {"type": "object", "properties": {"ticket_key": {"type": "string"}}, "required": ["ticket_key"]}}}