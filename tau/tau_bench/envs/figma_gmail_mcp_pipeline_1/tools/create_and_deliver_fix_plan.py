# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateAndDeliverFixPlan(Tool):  # CREATE
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        plan_id: str
    ) -> str:
        # Verify input data.
        if not isinstance(plan_id, str) or not plan_id:
            return json.dumps({"error": "plan_id must be a non-empty string"})

        # Identify the resolution strategy.
        fix_plans = list(data.get("fix_plans", {}).values())
        fix_plan = next((plan for plan in fix_plans if plan.get("plan_id") == plan_id), None)

        if not fix_plan:
            return json.dumps({"error": f"Fix plan with ID '{plan_id}' not found"})

        delivery_method = fix_plan.get("delivery_method")
        audit_id = fix_plan.get("audit_id")
        owner_email = fix_plan.get("owner_email")

        # Retrieve the artifact_id by locating the audit.
        audits = list(data.get("audits", {}).values())
        audit = next((a for a in audits if a.get("audit_id") == audit_id), None)

        if not audit:
            return json.dumps({"error": f"Audit with ID '{audit_id}' not found"})

        artifact_id = audit.get("artifact_id")

        if delivery_method == "TICKETS":
            # Create a JIRA ticket identifier utilizing a custom hash function.
            hash_value = custom_hash(f"{plan_id}_ticket")
            ticket_digits = f"{hash_value % 10000:04d}"  # Four random numbers.
            ticket_id = f"JIRA-{ticket_digits}"

            # Modify all fix_items associated with this plan_id to update external_ticket_ref_nullable.
            fix_items = list(data.get("fix_items", {}).values())
            updated_count = 0
            for item in fix_items:
                if item.get("plan_id") == plan_id:
                    item["external_ticket_ref_nullable"] = ticket_id
                    updated_count += 1

            return json.dumps({
                "ticket_id": ticket_id,
                "message": f"{ticket_id} created",
                "updated_fix_items": updated_count
            })

        elif delivery_method == "COMMENTS":
            # Add a new comment in Figma.
            figma_comments = list(data.get("figma_comments", {}).values())
            next_num = len(figma_comments) + 1
            comment_id = f"comment_{next_num:03d}"

            new_comment = {
                "comment_id": comment_id,
                "artifact_id": artifact_id,
                "author_email": owner_email,
                "content": "Fix comment",
                "source_message_id_nullable": None,
                "created_ts": "2024-08-25T11:00:00Z",
                "resolved_flag": False
            }

            figma_comments.append(new_comment)

            return json.dumps({
                "comment_id": comment_id,
                "message": f"{comment_id} created",
                "new_comment": new_comment
            })

        elif delivery_method == "PDF":
            # Generate a new asset.
            assets = list(data.get("assets", {}).values())
            next_num = len(assets) + 1
            asset_id = f"asset_{next_num:03d}"

            new_asset = {
                "asset_id": asset_id,
                "artifact_id_nullable": artifact_id,
                "export_profile": "PDF",
                "file_size": 95000,
                "storage_ref": "gs://company-assets/figma-exports/fix-plan.pdf",
                "created_ts": "2024-08-25T11:00:00Z",
                "dlp_scan_status": "CLEAN",
                "dlp_scan_details_nullable": None
            }

            assets.append(new_asset)

            return json.dumps({
                "asset_id": asset_id,
                "message": f"{asset_id} created",
                "new_asset": new_asset
            })

        else:
            return json.dumps({"error": f"Unknown delivery method: {delivery_method}"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_and_deliver_fix_plan",
                "description": "Create and deliver a fix plan based on its delivery method (TICKETS, COMMENTS, or PDF). Handles ticket creation, figma comments, or PDF asset generation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {
                            "type": "string",
                            "description": "The fix plan ID to create and deliver."
                        }
                    },
                    "required": ["plan_id"]
                }
            }
        }
