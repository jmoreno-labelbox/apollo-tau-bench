# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import FIXED_NOW, _find_one


class ProcessLoyaltyProgram(Tool):
    """Manage customer loyalty program enrollment and rewards."""

    @staticmethod
    def invoke(data: Dict[str, Any], contact_id: Any, action: Any, points: Any = 0) -> str:
        contact_id = _idstr(contact_id)
        action = f"{action}".strip().lower()
        try:
            points = int(points)
        except Exception:
            points = 0

        if not contact_id or not action:
            return _error("contact_id and action are required.")

        contacts = data.get("contacts", [])
        contact = _find_one(contacts, "contact_id", contact_id)
        if not contact:
            return _error(f"Contact '{contact_id}' not found.")

        loyalty_members = data.setdefault("loyalty_program", [])
        member = _find_one(loyalty_members, "contact_id", contact_id)

        # registration pathway
        if action == "enroll" and not member:
            member = {
                "contact_id": contact_id,
                "member_id": f"LOY_{len(loyalty_members) + 1:04d}",
                "points_balance": 100,
                "tier": "bronze",
                "enrolled_at": FIXED_NOW,
                "status": "active",
            }
            loyalty_members.append(member)

        # standardize frequent alternatives for action
        _LOY_MAP = {"add_points": "add", "adjust_points": "adjust"}
        action = _LOY_MAP.get(action, action)

        if action in ("add", "adjust"):
            if not member:
                member = {
                    "contact_id": contact_id,
                    "member_id": f"LOY_{len(loyalty_members) + 1:04d}",
                    "points_balance": 0,
                    "tier": "bronze",
                    "enrolled_at": FIXED_NOW,
                    "status": "active",
                }
                loyalty_members.append(member)
            member["points_balance"] = int(member.get("points_balance", 0)) + int(points)

        return json.dumps(
            {
                "contact_id": contact_id,
                "action": action,
                "points": points,
                "points_balance": member.get("points_balance", 0) if member else 0,
                "tier": member.get("tier", "bronze") if member else "bronze",
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "process_loyalty_program",
                "description": "Manage customer loyalty program enrollment and rewards.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "contact_id": {"type": "string"},
                        "action": {"type": "string", "enum": ["enroll", "add_points", "adjust_points", "add","adjust"]},
                        "points": {"type": "integer"},
                    },
                    "required": ["contact_id", "action"],
                },
            },
        }
