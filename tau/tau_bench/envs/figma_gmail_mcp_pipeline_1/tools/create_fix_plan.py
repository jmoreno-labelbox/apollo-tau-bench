# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateFixPlan(Tool):  # WRITE
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        audit_id: str,
        owner_email: str,
        delivery_method: str = None
    ) -> str:
        # Validate input
        if not isinstance(audit_id, str) or not audit_id:
            return json.dumps({"error": "audit_id must be a non-empty string"})

        if not isinstance(owner_email, str) or not owner_email:
            return json.dumps({"error": "owner_email must be a non-empty string"})

        # Check if audit exists
        audits = data.get("audits", [])
        audit_exists = any(audit.get("audit_id") == audit_id for audit in audits)
        if not audit_exists:
            return json.dumps({"error": f"Audit with ID '{audit_id}' not found"})

        # Get existing fix plans to determine next plan_id
        fix_plans = data.get("fix_plans", [])
        next_num = len(fix_plans) + 1
        plan_id = f"plan_{next_num:03d}"

        # Use custom_hash to determine delivery_method based on owner_email if not given
        if delivery_method is None:
            delivery_methods = ["TICKETS", "COMMENTS", "PDF"]
            hash_value = custom_hash(owner_email)
            delivery_method = delivery_methods[hash_value % len(delivery_methods)]

        # Create new fix plan entry
        new_fix_plan = {
            "plan_id": plan_id,
            "audit_id": audit_id,
            "status": "DRAFTED",
            "created_ts": "2024-08-25T10:00:00Z",
            "owner_email": owner_email,
            "delivery_method": delivery_method
        }

        # Add to fix_plans
        fix_plans.append(new_fix_plan)

        return json.dumps({"new_fix_plan": new_fix_plan})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_fix_plan",
                "description": "Create a new fix plan for an audit with specified owner. Automatically determines delivery method based on owner email using hash function.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {
                            "type": "string",
                            "description": "The audit ID for which to create the fix plan."
                        },
                        "owner_email": {
                            "type": "string",
                            "description": "Email address of the fix plan owner."
                        }
                    },
                    "required": ["audit_id", "owner_email"]
                }
            }
        }
