from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateAndDeliverFixPlan(Tool):  #WRITE
    @staticmethod
    def invoke(data: dict[str, Any], plan_id: str) -> str:
        pass
        #Check the input for validity
        if not isinstance(plan_id, str) or not plan_id:
            payload = {"error": "plan_id must be a non-empty string"}
            out = json.dumps(payload)
            return out

        #Identify the fix plan
        fix_plans = data.get("fix_plans", [])
        fix_plan = next(
            (plan for plan in fix_plans if plan.get("plan_id") == plan_id), None
        )

        if not fix_plan:
            payload = {"error": f"Fix plan with ID '{plan_id}' not found"}
            out = json.dumps(payload)
            return out

        delivery_method = fix_plan.get("delivery_method")
        audit_id = fix_plan.get("audit_id")
        owner_email = fix_plan.get("owner_email")

        #Locate the audit to retrieve artifact_id
        audits = data.get("audits", [])
        audit = next((a for a in audits if a.get("audit_id") == audit_id), None)

        if not audit:
            payload = {"error": f"Audit with ID '{audit_id}' not found"}
            out = json.dumps(payload)
            return out

        artifact_id = audit.get("artifact_id")

        if delivery_method == "TICKETS":
            #Create a JIRA ticket ID using a custom hash
            hash_value = custom_hash(f"{plan_id}_ticket")
            ticket_digits = f"{hash_value % 10000:04d}"  #Four random digits
            ticket_id = f"JIRA-{ticket_digits}"

            #Modify all fix_items associated with this plan_id to establish external_ticket_ref_nullable
            fix_items = data.get("fix_items", [])
            updated_count = 0
            for item in fix_items:
                if item.get("plan_id") == plan_id:
                    item["external_ticket_ref_nullable"] = ticket_id
                    updated_count += 1
            payload = {
                    "ticket_id": ticket_id,
                    "message": f"{ticket_id} created",
                    "updated_fix_items": updated_count,
                }
            out = json.dumps(
                payload)
            return out

        elif delivery_method == "COMMENTS":
            #Establish a new figma comment
            figma_comments = data.get("figma_comments", [])
            next_num = len(figma_comments) + 1
            comment_id = f"comment_{next_num:03d}"

            new_comment = {
                "comment_id": comment_id,
                "artifact_id": artifact_id,
                "author_email": owner_email,
                "content": "Fix comment",
                "source_message_id_nullable": None,
                "created_ts": "2024-08-25T11:00:00Z",
                "resolved_flag": False,
            }

            figma_comments.append(new_comment)
            payload = {
                    "comment_id": comment_id,
                    "message": f"{comment_id} created",
                    "new_comment": new_comment,
                }
            out = json.dumps(
                payload)
            return out

        elif delivery_method == "PDF":
            #Establish a new asset
            assets = data.get("assets", [])
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
                "dlp_scan_details_nullable": None,
            }

            assets.append(new_asset)
            payload = {
                    "asset_id": asset_id,
                    "message": f"{asset_id} created",
                    "new_asset": new_asset,
                }
            out = json.dumps(
                payload)
            return out

        else:
            payload = {"error": f"Unknown delivery method: {delivery_method}"}
            out = json.dumps(payload)
            return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateAndDeliverFixPlan",
                "description": "Create and deliver a fix plan based on its delivery method (TICKETS, COMMENTS, or PDF). Handles ticket creation, figma comments, or PDF asset generation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {
                            "type": "string",
                            "description": "The fix plan ID to create and deliver.",
                        }
                    },
                    "required": ["plan_id"],
                },
            },
        }
