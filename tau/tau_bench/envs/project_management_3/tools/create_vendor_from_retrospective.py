from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timezone
from typing import Any

class CreateVendorFromRetrospective(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        vendor_name: str,
        vendor_type: str,
        payment_terms: str = "Net 30",
        team_feedback: dict = {},
        retrospective_id: str = None
    ) -> str:
        if not all([vendor_name, vendor_type]):
            payload = {"error": "vendor_name and vendor_type are required"}
            out = json.dumps(payload)
            return out

        vendors = data.get("vendors", [])
        retrospectives = data.get("retrospectives", [])
        teams = data.get("teams", [])

        existing = next(
            (
                v
                for v in vendors
                if v.get("vendor_name", "").lower() == vendor_name.lower()
            ),
            None,
        )
        if existing:
            payload = {"error": f"Vendor {vendor_name} already exists"}
            out = json.dumps(payload)
            return out

        team_skills = []
        if retrospective_id:
            retro = next(
                (
                    r
                    for r in retrospectives
                    if r.get("retrospective_id") == retrospective_id
                ),
                None,
            )
            if retro:
                team_id = retro.get("team_id")
                team = next((t for t in teams if t.get("team_id") == team_id), None)
                if team:
                    action_items = retro.get("action_items", [])
                    for item in action_items:
                        if "vendor" in item.lower() or "contractor" in item.lower():
                            skills = [
                                "development",
                                "testing",
                                "design",
                                "security",
                                "devops",
                            ]
                            for skill in skills:
                                if skill in item.lower():
                                    team_skills.append(skill)

        vendor_id = f"vendor_{uuid.uuid4().hex[:8]}"

        new_vendor = {
            "vendor_id": vendor_id,
            "vendor_name": vendor_name,
            "vendor_type": vendor_type,
            "payment_terms": payment_terms,
            "status": "pending_review",
            "late_payments": 0,
            "capability_match": team_skills,
            "team_feedback": team_feedback,
            "created_from_retrospective": (
                retrospective_id if retrospective_id else None
            ),
            "created_date": datetime.now().isoformat(),
            "requires_assessment": True,
            "preferred_for_skills": team_skills,
        }

        vendors.append(new_vendor)
        payload = {"success": True, "vendor": new_vendor}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateVendorFromRetrospective",
                "description": "Create a vendor record based on team retrospective feedback",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "vendor_name": {"type": "string", "description": "Vendor name"},
                        "vendor_type": {
                            "type": "string",
                            "description": "Type of vendor services",
                        },
                        "payment_terms": {
                            "type": "string",
                            "description": "Payment terms (default Net 30)",
                        },
                        "team_feedback": {
                            "type": "object",
                            "description": "Team feedback from retrospective",
                        },
                        "retrospective_id": {
                            "type": "string",
                            "description": "Related retrospective ID",
                        },
                    },
                    "required": ["vendor_name", "vendor_type"],
                },
            },
        }
