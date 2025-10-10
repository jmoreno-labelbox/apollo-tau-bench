# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateFixItem(Tool):  # WRITE
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        plan_id: str,
        finding_id: str
    ) -> str:
        # Validate input
        if not isinstance(plan_id, str) or not plan_id:
            return json.dumps({"error": "plan_id must be a non-empty string"})

        if not isinstance(finding_id, str) or not finding_id:
            return json.dumps({"error": "finding_id must be a non-empty string"})

        # Check if plan exists
        fix_plans = data.get("fix_plans", [])
        plan_exists = any(plan.get("plan_id") == plan_id for plan in fix_plans)
        if not plan_exists:
            return json.dumps({"error": f"Fix plan with ID '{plan_id}' not found"})

        # Check if finding exists in either DS or A11Y findings
        audit_findings_ds = data.get("audit_findings_ds", [])
        audit_findings_a11y = data.get("audit_findings_a11y", [])

        finding_exists_ds = any(finding.get("finding_id") == finding_id for finding in audit_findings_ds)
        finding_exists_a11y = any(finding.get("finding_id") == finding_id for finding in audit_findings_a11y)

        if not (finding_exists_ds or finding_exists_a11y):
            return json.dumps({"error": f"Finding with ID '{finding_id}' not found in either DS or A11Y findings"})

        # Get existing fix items to determine next item_id
        fix_items = data.get("fix_items", [])
        next_num = len(fix_items) + 1
        item_id = f"item_{next_num:03d}"

        # Use hash of input parameters to select proposed_change_type
        input_hash = custom_hash(f"{plan_id}_{finding_id}")
        change_types = ["SPACING_ADJUST", "TOKEN_SWAP", "COMPONENT_SWAP"]
        proposed_change_type = change_types[input_hash % len(change_types)]

        # Find existing items with the same proposed_change_type to pick details from
        same_type_items = [item for item in fix_items if item.get("proposed_change_type") == proposed_change_type]

        if same_type_items:
            # Pick a details from existing items with same type using hash
            details_hash = custom_hash(f"{finding_id}_{proposed_change_type}")
            selected_item = same_type_items[details_hash % len(same_type_items)]
            proposed_change_details_json = selected_item.get("proposed_change_details_json", "{}")
        else:
            # Fallback if no items of this type exist
            proposed_change_details_json = '{"action": "placeholder", "reason": "Generated item"}'

        # Create new fix item entry
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

        # Add to fix_items
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
