# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LinkDuplicateIssue(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], primary_ticket_key: str, duplicate_ticket_key: str, confidence: float) -> str:
        links = _get_table(data, "bug_links")
        link_id = f"LINK-{len(links) + 1}"
        rec = {"link_id": link_id, "primary_bug_id": primary_ticket_key, "related_bug_id": duplicate_ticket_key, "relation_type": "duplicate", "confidence": confidence}
        links.append(rec)
        return json.dumps({"link_id": link_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "link_duplicate_issue", "description": "Links two tickets as duplicate with provided confidence.", "parameters": {"type": "object", "properties": {"primary_ticket_key": {"type": "string"}, "duplicate_ticket_key": {"type": "string"}, "confidence": {"type": "number"}}, "required": ["primary_ticket_key", "duplicate_ticket_key", "confidence"]}}}
