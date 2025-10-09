from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ProcessLoyaltyProgram(Tool):
    """Oversee enrollment in the customer loyalty program and associated rewards."""

    @staticmethod
    def invoke(
        data: dict[str, Any], contact_id: Any, action: Any, points: Any = 0
    ) -> str:
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

        # registration route
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

        # standardize frequent synonyms for action
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

        _append_audit(data, "loyalty_program_activity", contact_id, {"action": action})
        payload = {
            "contact_id": contact_id,
            "action": action,
            "points": points,
            "points_balance": member.get("points_balance", 0) if member else 0,
            "tier": member.get("tier", "bronze") if member else "bronze",
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
        pass
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

        #registration route
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

        #standardize frequent synonyms for action
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
            member["points_balance"] = int(member.get("points_balance", 0)) + int(
                points
            )

        _append_audit(data, "loyalty_program_activity", contact_id, {"action": action})
        payload = {
                "contact_id": contact_id,
                "action": action,
                "points": points,
                "points_balance": member.get("points_balance", 0) if member else 0,
                "tier": member.get("tier", "bronze") if member else "bronze",
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
                "name": "ProcessLoyaltyProgram",
                "description": "Manage customer loyalty program enrollment and rewards.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "contact_id": {"type": "string"},
                        "action": {"type": "string"},
                        "points": {"type": "integer"},
                    },
                    "required": ["contact_id", "action"],
                },
            },
        }
