from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateFixPlan(Tool):  #WRITE
    @staticmethod
    def invoke(
        data: dict[str, Any],
        audit_id: str,
        owner_email: str,
        delivery_method: str = None,
    ) -> str:
        pass
        #Check the input for validity
        if not isinstance(audit_id, str) or not audit_id:
            payload = {"error": "audit_id must be a non-empty string"}
            out = json.dumps(payload)
            return out

        if not isinstance(owner_email, str) or not owner_email:
            payload = {"error": "owner_email must be a non-empty string"}
            out = json.dumps(payload)
            return out

        #Verify the existence of the audit
        audits = data.get("audits", [])
        audit_exists = any(audit.get("audit_id") == audit_id for audit in audits)
        if not audit_exists:
            payload = {"error": f"Audit with ID '{audit_id}' not found"}
            out = json.dumps(payload)
            return out

        #Retrieve current fix plans to identify the next plan_id
        fix_plans = data.get("fix_plans", [])
        next_num = len(fix_plans) + 1
        plan_id = f"plan_{next_num:03d}"

        #Utilize custom_hash to establish delivery_method based on owner_email if not provided
        if delivery_method is None:
            delivery_methods = ["TICKETS", "COMMENTS", "PDF"]
            hash_value = custom_hash(owner_email)
            delivery_method = delivery_methods[hash_value % len(delivery_methods)]

        #Establish a new fix plan entry
        new_fix_plan = {
            "plan_id": plan_id,
            "audit_id": audit_id,
            "status": "DRAFTED",
            "created_ts": "2024-08-25T10:00:00Z",
            "owner_email": owner_email,
            "delivery_method": delivery_method,
        }

        #Include in fix_plans
        fix_plans.append(new_fix_plan)
        payload = {"new_fix_plan": new_fix_plan}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateFixPlan",
                "description": "Create a new fix plan for an audit with specified owner. Automatically determines delivery method based on owner email using hash function.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {
                            "type": "string",
                            "description": "The audit ID for which to create the fix plan.",
                        },
                        "owner_email": {
                            "type": "string",
                            "description": "Email address of the fix plan owner.",
                        },
                    },
                    "required": ["audit_id", "owner_email"],
                },
            },
        }
