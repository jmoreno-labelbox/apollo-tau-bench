from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CreateFixItem(Tool):  #WRITE
    @staticmethod
    def invoke(data: dict[str, Any], plan_id: str, finding_id: str) -> str:
        pass
        #Check the input for validity
        if not isinstance(plan_id, str) or not plan_id:
            payload = {"error": "plan_id must be a non-empty string"}
            out = json.dumps(payload)
            return out

        if not isinstance(finding_id, str) or not finding_id:
            payload = {"error": "finding_id must be a non-empty string"}
            out = json.dumps(payload)
            return out

        #Verify the existence of the plan
        fix_plans = data.get("fix_plans", {}).values()
        plan_exists = any(plan.get("plan_id") == plan_id for plan in fix_plans.values()
        if not plan_exists:
            payload = {"error": f"Fix plan with ID '{plan_id}' not found"}
            out = json.dumps(payload)
            return out

        #Verify if the finding is present in either DS or A11Y findings
        audit_findings_ds = data.get("audit_findings_ds", {}).values()
        audit_findings_a11y = data.get("audit_findings_a11y", {}).values()

        finding_exists_ds = any(
            finding.get("finding_id") == finding_id for finding in audit_findings_ds.values()
        )
        finding_exists_a11y = any(
            finding.get("finding_id") == finding_id for finding in audit_findings_a11y.values()
        )

        if not (finding_exists_ds or finding_exists_a11y):
            payload = {
                    "error": f"Finding with ID '{finding_id}' not found in either DS or A11Y findings"
                }
            out = json.dumps(
                payload)
            return out

        #Retrieve current fix items to identify the next item_id
        fix_items = data.get("fix_items", {}).values()
        next_num = len(fix_items) + 1
        item_id = f"item_{next_num:03d}"

        #Utilize a hash of input parameters to determine proposed_change_type
        input_hash = custom_hash(f"{plan_id}_{finding_id}")
        change_types = ["SPACING_ADJUST", "TOKEN_SWAP", "COMPONENT_SWAP"]
        proposed_change_type = change_types[input_hash % len(change_types)]

        #Locate existing items with the same proposed_change_type to extract details
        same_type_items = [
            item
            for item in fix_items.values() if item.get("proposed_change_type") == proposed_change_type
        ]

        if same_type_items:
            #Select details from existing items of the same type using a hash
            details_hash = custom_hash(f"{finding_id}_{proposed_change_type}")
            selected_item = same_type_items[details_hash % len(same_type_items)]
            proposed_change_details_json = selected_item.get(
                "proposed_change_details_json", "{}"
            )
        else:
            #Provide a fallback if no items of this type are available
            proposed_change_details_json = (
                '{"action": "placeholder", "reason": "Generated item"}'
            )

        #Establish a new fix item entry
        new_fix_item = {
            "item_id": item_id,
            "plan_id": plan_id,
            "finding_id": finding_id,
            "proposed_change_type": proposed_change_type,
            "proposed_change_details_json": proposed_change_details_json,
            "status": "PENDING",
            "external_ticket_ref_nullable": None,
            "figma_comment_id_nullable": None,
        }

        #Include in fix_items
        data["fix_items"][new_fix_item["fix_item_id"]] = new_fix_item
        payload = {"new_fix_item": new_fix_item}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateFixItem",
                "description": "Create a new fix item for a fix plan with specified finding. Automatically determines change type and details based on existing patterns using hash functions.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {
                            "type": "string",
                            "description": "The fix plan ID for which to create the fix item.",
                        },
                        "finding_id": {
                            "type": "string",
                            "description": "The finding ID from audit_findings_ds or audit_findings_a11y to address.",
                        },
                    },
                    "required": ["plan_id", "finding_id"],
                },
            },
        }
