from tau_bench.envs.tool import Tool
import json
from typing import Any

class FindCanonicalDuplicateV2(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], ticket_key: str) -> str:
        pass
        dedups = _get_table(data, "bug_deduplication")
        links = _get_table(data, "bug_links")
        #Prioritize the explicit deduplication table initially
        row = next(
            (
                d
                for d in dedups
                if d.get("new_bug_id") == ticket_key
                and (
                    d.get("status") in ("confirmed_duplicate", "new_bug")
                    or d.get("status")
                )
            ),
            None,
        )
        if row and row.get("canonical_bug_id"):
            payload = {"canonical_bug_id": row.get("canonical_bug_id")}
            out = json.dumps(
                payload, indent=2
            )
            return out
        #Revert to bug_links with relation_type set to duplicate
        link = next(
            (
                l
                for l in links
                if l.get("relation_type") == "duplicate"
                and (
                    l.get("primary_bug_id") == ticket_key
                    or l.get("related_bug_id") == ticket_key
                )
            ),
            None,
        )
        if link:
            if link.get("primary_bug_id") == ticket_key:
                other = link.get("related_bug_id")
            else:
                other = link.get("primary_bug_id")
            payload = {"canonical_bug_id": other}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"canonical_bug_id": None}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindCanonicalDuplicateV2",
                "description": "Looks up canonical duplicate for a ticket from bug_deduplication or bug_links.",
                "parameters": {
                    "type": "object",
                    "properties": {"ticket_key": {"type": "string"}},
                    "required": ["ticket_key"],
                },
            },
        }
