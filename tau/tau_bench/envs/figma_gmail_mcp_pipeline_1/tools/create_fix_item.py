# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateFixItem(Tool):  # CREATE
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        plan_id: str,
        finding_id: str
    ) -> str:
        # Check input for validity.
        if not isinstance(plan_id, str) or not plan_id:
            return json.dumps({"error": "plan_id must be a non-empty string"})

        if not isinstance(finding_id, str) or not finding_id:
            return json.dumps({"error": "finding_id must be a non-empty string"})

        # Verify the existence of the plan.
        fix_plans = list(data.get("fix_plans", {}).values())
        plan_exists = any(plan.get("plan_id") == plan_id for plan in fix_plans)
        if not plan_exists:
            return json.dumps({"error": f"Fix plan with ID '{plan_id}' not found"})

        # Verify if the finding is present in either DS or A11Y findings.
        audit_findings_ds = list(data.get("audit_findings_ds", {}).values())
        audit_findings_a11y = list(data.get("audit_findings_a11y", {}).values())

        finding_exists_ds = any(finding.get("finding_id") == finding_id for finding in audit_findings_ds)
        finding_exists_a11y = any(finding.get("finding_id") == finding_id for finding in audit_findings_a11y)

        if not (finding_exists_ds or finding_exists_a11y):
            return json.dumps({"error": f"Finding with ID '{finding_id}' not found in either DS or A11Y findings"})

        # Retrieve current fix items to identify the next item_id.
        fix_items = list(data.get("fix_items", {}).values())
        next_num = len(fix_items) + 1
        item_id = f"item_{next_num:03d}"

        # Utilize the hash of the input parameters to determine proposed_change_type.
        input_hash = custom_hash(f"{plan_id}_{finding_id}")
        change_types = ["SPACING_ADJUST", "TOKEN_SWAP", "COMPONENT_SWAP"]
        proposed_change_type = change_types[input_hash % len(change_types)]

        # Locate current items that share the same proposed_change_type to extract details from.
        same_type_items = [item for item in fix_items if item.get("proposed_change_type") == proposed_change_type]

        if same_type_items:
            # Select attributes from existing items of the same type utilizing a hash.
            details_hash = custom_hash(f"{finding_id}_{proposed_change_type}")
            selected_item = same_type_items[details_hash % len(same_type_items)]
            proposed_change_details_json = selected_item.get("proposed_change_details_json", "{}")
        else:
            # Alternative action when no items of this type are present.
            proposed_change_details_json = '{"action": "placeholder", "reason": "Generated item"}'

        # Generate a new entry for the fix item.
        new_fix_item = {
            "item_id": item_id,
            "plan_id": plan_id,
            "finding_id": finding_id,
            "proposed_change_type": proposed_change_type,
            "proposed_change_details_json": proposed_change_details_json,
            "status": "PENDING",
            "external_ticket_ref_nullable": None,
            "figma_comment_id_nullable": None
        }

        # Include in fix_items
        fix_items.append(new_fix_item)

        return json.dumps({"new_fix_item": new_fix_item})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_fix_item",
                "description": "Create a new fix item for a fix plan with specified finding. Automatically determines change type and details based on existing patterns using hash functions.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {
                            "type": "string",
                            "description": "The fix plan ID for which to create the fix item."
                        },
                        "finding_id": {
                            "type": "string",
                            "description": "The finding ID from audit_findings_ds or audit_findings_a11y to address."
                        }
                    },
                    "required": ["plan_id", "finding_id"]
                }
            }
        }
