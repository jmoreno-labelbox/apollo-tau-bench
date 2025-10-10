from domains.dto import Tool

import json
from typing import Dict, Any
from datetime import datetime

def _fixed_now_iso():
    return datetime.utcnow().isoformat() + "Z"

# -------------------- Candidates --------------------
class ModifyCandidate(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        updates = kwargs.get("updates") or {}
        candidate_id = kwargs.get("candidate_id")
        candidates = data.get("candidates", [])

        # Find the candidate in the list and update
        for c in candidates:
            if c.get("candidate_id") == candidate_id:
                c.update(updates)
                c["updated_at"] = _fixed_now_iso()
                break
        else:
            return json.dumps({"error": f"Candidate {candidate_id} not found"}, indent=2)

        return json.dumps({"updated": updates}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_candidate",
                "description": "Update candidate details.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "updates": {"type": "object"}
                    },
                    "required": ["candidate_id", "updates"]
                }
            }
        }


class AddCandidate(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        new_candidate = kwargs.get("candidate") or {}
        candidates = data.get("candidates", [])
        candidates.append(new_candidate)
        data["candidates"] = candidates
        return json.dumps({"added_candidate": new_candidate}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type":"function",
            "function":{
                "name":"add_candidate",
                "description":"Add a new candidate.",
                "parameters":{"type":"object","properties":{"candidate":{"type":"object"}},"required":["candidate"]}
            }
        }

class RemoveCandidate(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        candidate_id = kwargs.get("candidate_id")
        candidates = data.get("candidates", [])
        data["candidates"] = [c for c in candidates if c.get("candidate_id") != candidate_id]
        return json.dumps({"removed_candidate_id": candidate_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type":"function",
            "function":{
                "name":"remove_candidate",
                "description":"Remove a candidate by ID.",
                "parameters":{"type":"object","properties":{"candidate_id":{"type":"string"}},"required":["candidate_id"]}
            }
        }

# -------------------- Asset Requests --------------------
class ModifyAssetRequest(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        updates = kwargs.get("updates") or {}
        request_id = kwargs.get("request_id")
        requests = data.get("asset_requests", [])
        for r in requests:
            if r.get("request_id") == request_id:
                r.update(updates)
                r["updated_at"] = _fixed_now_iso()
        return json.dumps({"updated_request_id": request_id, "updates": updates}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"update_asset_request",
            "description":"Update an asset request.",
            "parameters":{"type":"object","properties":{"request_id":{"type":"string"},"updates":{"type":"object"}},"required":["request_id","updates"]}
        }}

class AddAssetRequest(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        new_request = kwargs.get("request") or {}
        requests = data.get("asset_requests", [])
        requests.append(new_request)
        data["asset_requests"] = requests
        return json.dumps({"added_request": new_request}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"add_asset_request",
            "description":"Add a new asset request.",
            "parameters":{"type":"object","properties":{"request":{"type":"object"}},"required":["request"]}
        }}

class RemoveAssetRequest(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        request_id = kwargs.get("request_id")
        requests = data.get("asset_requests", [])
        data["asset_requests"] = [r for r in requests if r.get("request_id") != request_id]
        return json.dumps({"removed_request_id": request_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"remove_asset_request",
            "description":"Remove an asset request by ID.",
            "parameters":{"type":"object","properties":{"request_id":{"type":"string"}},"required":["request_id"]}
        }}

# -------------------- Access Checks --------------------
class ModifyAccessCheck(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        updates = kwargs.get("updates") or {}
        check_id = kwargs.get("check_id")
        checks = data.get("access_checks", [])
        for c in checks:
            if c.get("check_id") == check_id:
                c.update(updates)
                c["updated_at"] = _fixed_now_iso()
        return json.dumps({"updated_check_id": check_id, "updates": updates}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"update_access_check",
            "description":"Update an access check status.",
            "parameters":{"type":"object","properties":{"check_id":{"type":"string"},"updates":{"type":"object"}},"required":["check_id","updates"]}
        }}

class AddAccessCheck(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        new_check = kwargs.get("check") or {}
        checks = data.get("access_checks", [])
        checks.append(new_check)
        data["access_checks"] = checks
        return json.dumps({"added_check": new_check}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"add_access_check",
            "description":"Add a new access check.",
            "parameters":{"type":"object","properties":{"check":{"type":"object"}},"required":["check"]}
        }}

class RemoveAccessCheck(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        check_id = kwargs.get("check_id")
        checks = data.get("access_checks", [])
        data["access_checks"] = [c for c in checks if c.get("check_id") != check_id]
        return json.dumps({"removed_check_id": check_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"remove_access_check",
            "description":"Remove an access check by ID.",
            "parameters":{"type":"object","properties":{"check_id":{"type":"string"}},"required":["check_id"]}
        }}

# -------------------- Checklist Items --------------------
class ModifyChecklistItem(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        updates = kwargs.get("updates") or {}
        item_id = kwargs.get("item_id")
        items = data.get("checklist_items", [])
        for i in items:
            if i.get("item_id") == item_id:
                i.update(updates)
                i["updated_at"] = _fixed_now_iso()
        return json.dumps({"updated_item_id": item_id, "updates": updates}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"update_checklist_item",
            "description":"Update a checklist task.",
            "parameters":{"type":"object","properties":{"item_id":{"type":"string"},"updates":{"type":"object"}},"required":["item_id","updates"]}
        }}

class AddChecklistItem(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        new_item = kwargs.get("item") or {}
        items = data.get("checklist_items", [])
        items.append(new_item)
        data["checklist_items"] = items
        return json.dumps({"added_item": new_item}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"add_checklist_item",
            "description":"Add a new checklist item.",
            "parameters":{"type":"object","properties":{"item":{"type":"object"}},"required":["item"]}
        }}

class RemoveChecklistItem(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        item_id = kwargs.get("item_id")
        items = data.get("checklist_items", [])
        data["checklist_items"] = [i for i in items if i.get("item_id") != item_id]
        return json.dumps({"removed_item_id": item_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"remove_checklist_item",
            "description":"Remove a checklist item by ID.",
            "parameters":{"type":"object","properties":{"item_id":{"type":"string"}},"required":["item_id"]}
        }}

# -------------------- Attachments --------------------
class ModifyAttachment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        updates = kwargs.get("updates") or {}
        attach_id = kwargs.get("attachment_id")
        attachments = data.get("attachments", [])
        for a in attachments:
            if a.get("attachment_id") == attach_id:
                a.update(updates)
                a["updated_at"] = _fixed_now_iso()
        return json.dumps({"updated_attachment_id": attach_id, "updates": updates}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"update_attachment",
            "description":"Update an attachment metadata.",
            "parameters":{"type":"object","properties":{"attachment_id":{"type":"string"},"updates":{"type":"object"}},"required":["attachment_id","updates"]}
        }}

class AddAttachment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        new_attach = kwargs.get("attachment") or {}
        attachments = data.get("attachments", [])
        attachments.append(new_attach)
        data["attachments"] = attachments
        return json.dumps({"added_attachment": new_attach}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"add_attachment",
            "description":"Add a new attachment.",
            "parameters":{"type":"object","properties":{"attachment":{"type":"object"}},"required":["attachment"]}
        }}

class RemoveAttachment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        attach_id = kwargs.get("attachment_id")
        attachments = data.get("attachments", [])
        data["attachments"] = [a for a in attachments if a.get("attachment_id") != attach_id]
        return json.dumps({"removed_attachment_id": attach_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"remove_attachment",
            "description":"Remove an attachment by ID.",
            "parameters":{"type":"object","properties":{"attachment_id":{"type":"string"}},"required":["attachment_id"]}
        }}

# -------------------- Email Labels --------------------
class ModifyEmailLabel(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        updates = kwargs.get("updates") or {}
        label_id = kwargs.get("label_id")
        labels = data.get("email_labels", [])
        for l in labels:
            if l.get("label_id") == label_id:
                l.update(updates)
                l["updated_at"] = _fixed_now_iso()
        return json.dumps({"updated_label_id": label_id, "updates": updates}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"update_email_label",
            "description":"Update an email label.",
            "parameters":{"type":"object","properties":{"label_id":{"type":"string"},"updates":{"type":"object"}},"required":["label_id","updates"]}
        }}

class AddEmailLabel(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        new_label = kwargs.get("label") or {}
        labels = data.get("email_labels", [])
        labels.append(new_label)
        data["email_labels"] = labels
        return json.dumps({"added_label": new_label}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"add_email_label",
            "description":"Add a new email label.",
            "parameters":{"type":"object","properties":{"label":{"type":"object"}},"required":["label"]}
        }}

class RemoveEmailLabel(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        label_id = kwargs.get("label_id")
        labels = data.get("email_labels", [])
        data["email_labels"] = [l for l in labels if l.get("label_id") != label_id]
        return json.dumps({"removed_label_id": label_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"remove_email_label",
            "description":"Remove an email label by ID.",
            "parameters":{"type":"object","properties":{"label_id":{"type":"string"}},"required":["label_id"]}
        }}

# -------------------- Emails --------------------
class ModifyEmail(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        updates = kwargs.get("updates") or {}
        message_id = kwargs.get("message_id")
        emails = data.get("emails", [])
        for e in emails:
            if e.get("message_id") == message_id:
                e.update(updates)
                e["updated_at"] = _fixed_now_iso()
        return json.dumps({"updated_message_id": message_id, "updates": updates}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"update_email",
            "description":"Update an email record.",
            "parameters":{"type":"object","properties":{"message_id":{"type":"string"},"updates":{"type":"object"}},"required":["message_id","updates"]}
        }}

class SendEmail(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        new_email = kwargs.get("email") or {}
        emails = data.get("emails", [])
        emails.append(new_email)
        data["emails"] = emails
        return json.dumps({"sent_email": new_email}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"send_email",
            "description":"Send a new email and add it to the record.",
            "parameters":{"type":"object","properties":{"email":{"type":"object"}},"required":["email"]}
        }}

class DeleteEmail(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        message_id = kwargs.get("message_id")
        emails = data.get("emails", [])
        data["emails"] = [e for e in emails if e.get("message_id") != message_id]
        return json.dumps({"deleted_message_id": message_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"delete_email",
            "description":"Delete an email by message ID.",
            "parameters":{"type":"object","properties":{"message_id":{"type":"string"}},"required":["message_id"]}
        }}

# -------------------- Inventory Assets --------------------
class ModifyAsset(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        updates = kwargs.get("updates") or {}
        asset_tag = kwargs.get("asset_tag")
        assets = data.get("inventory_assets", [])
        for a in assets:
            if a.get("asset_tag") == asset_tag:
                a.update(updates)
                a["updated_at"] = _fixed_now_iso()
        return json.dumps({"updated_asset_tag": asset_tag, "updates": updates}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"update_asset",
            "description":"Update an inventory asset.",
            "parameters":{"type":"object","properties":{"asset_tag":{"type":"string"},"updates":{"type":"object"}},"required":["asset_tag","updates"]}
        }}

class AssignAsset(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        asset_tag = kwargs.get("asset_tag")
        candidate_id = kwargs.get("candidate_id")
        assets = data.get("inventory_assets", [])
        for a in assets:
            if a.get("asset_tag") == asset_tag:
                a["assigned_candidate_id_nullable"] = candidate_id
                a["status"] = "Assigned"
                a["updated_at"] = _fixed_now_iso()
        return json.dumps({"assigned_asset_tag": asset_tag, "candidate_id": candidate_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"assign_asset",
            "description":"Assign an asset to a candidate.",
            "parameters":{"type":"object","properties":{"asset_tag":{"type":"string"},"candidate_id":{"type":"string"}},"required":["asset_tag","candidate_id"]}
        }}

class ReleaseAsset(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        asset_tag = kwargs.get("asset_tag")
        assets = data.get("inventory_assets", [])
        for a in assets:
            if a.get("asset_tag") == asset_tag:
                a["assigned_candidate_id_nullable"] = None
                a["status"] = "Available"
                a["updated_at"] = _fixed_now_iso()
        return json.dumps({"released_asset_tag": asset_tag}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"release_asset",
            "description":"Release an assigned asset.",
            "parameters":{"type":"object","properties":{"asset_tag":{"type":"string"}},"required":["asset_tag"]}
        }}

# -------------------- Onboarding Files --------------------
class ModifyOnboardingFile(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        updates = kwargs.get("updates") or {}
        file_path = kwargs.get("file_path")
        files = data.get("onboarding_files", [])
        for f in files:
            if f.get("file_path") == file_path:
                f.update(updates)
                f["updated_at"] = _fixed_now_iso()
        return json.dumps({"updated_file_path": file_path, "updates": updates}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"update_onboarding_file",
            "description":"Update an onboarding file content or metadata.",
            "parameters":{"type":"object","properties":{"file_path":{"type":"string"},"updates":{"type":"object"}},"required":["file_path","updates"]}
        }}

class AddOnboardingFile(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        new_file = kwargs.get("file") or {}
        files = data.get("onboarding_files", [])
        files.append(new_file)
        data["onboarding_files"] = files
        return json.dumps({"added_file": new_file}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"add_onboarding_file",
            "description":"Add a new onboarding file.",
            "parameters":{"type":"object","properties":{"file":{"type":"object"}},"required":["file"]}
        }}

class RemoveOnboardingFile(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        file_path = kwargs.get("file_path")
        files = data.get("onboarding_files", [])
        data["onboarding_files"] = [f for f in files if f.get("file_path") != file_path]
        return json.dumps({"removed_file_path": file_path}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"remove_onboarding_file",
            "description":"Remove an onboarding file by file path.",
            "parameters":{"type":"object","properties":{"file_path":{"type":"string"}},"required":["file_path"]}
        }}


class RecordTerminalLog(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        event_type = kwargs.get("event_type")
        message = kwargs.get("message")
        candidate_id = kwargs.get("candidate_id")
        terminal_logs = data.setdefault("terminal_logs", [])
        log_entry = {
            "event_type": event_type,
            "message": message,
            "candidate_id": candidate_id,
            "timestamp": _fixed_now_iso()
        }
        terminal_logs.append(log_entry)
        return json.dumps({"logged_event": log_entry}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "record_terminal_log",
                "description": "Logs a terminal event for audit/debug purposes.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "event_type": {"type": "string"},
                        "message": {"type": "string"},
                        "candidate_id": {"type": "string"}
                    },
                    "required": ["event_type", "message"]
                }
            }
        }

class ApplyLabelToEmail(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        email_id = kwargs.get("email_id")
        label_id = kwargs.get("label_id")
        email_labels = data.get("email_labels", [])

        # Find the email in the list and apply the label
        for e in email_labels:
            if e.get("email_id") == email_id:
                applied_labels = e.setdefault("labels", [])
                if label_id not in applied_labels:
                    applied_labels.append(label_id)
                break
        else:
            # If email not found, optionally create a new entry
            email_labels.append({"email_id": email_id, "labels": [label_id]})
            data["email_labels"] = email_labels

        return json.dumps({
            "email_id": email_id,
            "applied_label_id": label_id,
            "status": "Success"
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "apply_label_to_email",
                "description": "Applies a label to an email.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "email_id": {"type": "string"},
                        "label_id": {"type": "string"}
                    },
                    "required": ["email_id", "label_id"]
                }
            }
        }




# End of 30 tools
TOOLS = [
    ModifyCandidate(),
    AddCandidate(), RemoveCandidate(),
    ModifyAssetRequest(), AddAssetRequest(), RemoveAssetRequest(),
    ModifyAccessCheck(), AddAccessCheck(), RemoveAccessCheck(),
    ModifyChecklistItem(), AddChecklistItem(), RemoveChecklistItem(),
    ModifyAttachment(), AddAttachment(), RemoveAttachment(),
    ModifyEmailLabel(), AddEmailLabel(), RemoveEmailLabel(),
    ModifyEmail(), SendEmail(), DeleteEmail(),
    ModifyAsset(), AssignAsset(), ReleaseAsset(),
    ModifyOnboardingFile(), AddOnboardingFile(), RemoveOnboardingFile(),
    RecordTerminalLog(), ApplyLabelToEmail()
]
