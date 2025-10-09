from tau_bench.envs.tool import Tool
import json
from typing import Any

class LinkDuplicateIssue(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        primary_ticket_key: str,
        duplicate_ticket_key: str,
        confidence: float,
    ) -> str:
        links = _get_table(data, "bug_links")
        link_id = f"LINK-{len(links) + 1}"
        rec = {
            "link_id": link_id,
            "primary_bug_id": primary_ticket_key,
            "related_bug_id": duplicate_ticket_key,
            "relation_type": "duplicate",
            "confidence": confidence,
        }
        links.append(rec)
        payload = {"link_id": link_id}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LinkDuplicateIssue",
                "description": "Links two tickets as duplicate with provided confidence.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "primary_ticket_key": {"type": "string"},
                        "duplicate_ticket_key": {"type": "string"},
                        "confidence": {"type": "number"},
                    },
                    "required": [
                        "primary_ticket_key",
                        "duplicate_ticket_key",
                        "confidence",
                    ],
                },
            },
        }
