import json
from datetime import datetime
from typing import Any

from tau_bench.envs.tool import Tool




def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db


def _fixed_now_iso():
    pass
    return datetime.utcnow().isoformat() + "Z"


#-------------------- Prospects --------------------
class ModifyCandidate(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], updates: dict = None, candidate_id: str = None) -> str:
        updates = updates or {}
        candidates = data.get("candidates", {}).values()

        # Locate the candidate within the list and modify
        for c in candidates.values():
            if c.get("candidate_id") == candidate_id:
                c.update(updates)
                c["updated_at"] = _fixed_now_iso()
                break
        else:
            payload = {"error": f"Candidate {candidate_id} not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = {"updated": updates}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCandidate",
                "description": "Update candidate details.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "updates": {"type": "object"},
                    },
                    "required": ["candidate_id", "updates"],
                },
            },
        }


class AddCandidate(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], candidate: dict = None) -> str:
        new_candidate = candidate or {}
        candidates = data.get("candidates", {}).values()
        data["candidates"][candidate_id] = new_candidate
        data["candidates"] = candidates
        payload = {"added_candidate": new_candidate}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "addCandidate",
                "description": "Add a new candidate.",
                "parameters": {
                    "type": "object",
                    "properties": {"candidate": {"type": "object"}},
                    "required": ["candidate"],
                },
            },
        }


class RemoveCandidate(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], candidate_id: str = None) -> str:
        candidates = data.get("candidates", {}).values()
        data["candidates"] = [
            c for c in candidates.values() if c.get("candidate_id") != candidate_id
        ]
        payload = {"removed_candidate_id": candidate_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "removeCandidate",
                "description": "Remove a candidate by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"candidate_id": {"type": "string"}},
                    "required": ["candidate_id"],
                },
            },
        }


#-------------------- Resource Requests --------------------
class ModifyAssetRequest(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], updates: dict[str, Any] = None, request_id: str = None) -> str:
        updates = updates or {}
        requests = data.get("asset_requests", {}).values()
        for r in requests.values():
            if r.get("request_id") == request_id:
                r.update(updates)
                r["updated_at"] = _fixed_now_iso()
        payload = {"updated_request_id": request_id, "updates": updates}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAssetRequest",
                "description": "Update an asset request.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {"type": "string"},
                        "updates": {"type": "object"},
                    },
                    "required": ["request_id", "updates"],
                },
            },
        }


class AddAssetRequest(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], request: dict = None) -> str:
        new_request = request or {}
        requests = data.get("asset_requests", {}).values()
        data["asset_requests"][new_request["asset_request_id"]] = new_request
        data["asset_requests"] = requests
        payload = {"added_request": new_request}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "addAssetRequest",
                "description": "Add a new asset request.",
                "parameters": {
                    "type": "object",
                    "properties": {"request": {"type": "object"}},
                    "required": ["request"],
                },
            },
        }


class RemoveAssetRequest(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], request_id: str = None) -> str:
        requests = data.get("asset_requests", {}).values()
        data["asset_requests"] = [
            r for r in requests.values() if r.get("request_id") != request_id
        ]
        payload = {"removed_request_id": request_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "removeAssetRequest",
                "description": "Remove an asset request by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"request_id": {"type": "string"}},
                    "required": ["request_id"],
                },
            },
        }


#-------------------- Permission Verifications --------------------
class ModifyAccessCheck(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], updates: dict[str, Any] = None, check_id: str = None) -> str:
        updates = updates or {}
        checks = data.get("access_checks", {}).values()
        for c in checks.values():
            if c.get("check_id") == check_id:
                c.update(updates)
                c["updated_at"] = _fixed_now_iso()
        payload = {"updated_check_id": check_id, "updates": updates}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAccessCheck",
                "description": "Update an access check status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "check_id": {"type": "string"},
                        "updates": {"type": "object"},
                    },
                    "required": ["check_id", "updates"],
                },
            },
        }


class AddAccessCheck(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], check: dict = None) -> str:
        new_check = check or {}
        checks = data.get("access_checks", {}).values()
        data["access_checks"][new_check["access_check_id"]] = new_check
        data["access_checks"] = checks
        payload = {"added_check": new_check}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddAccessCheck",
                "description": "Add a new access check.",
                "parameters": {
                    "type": "object",
                    "properties": {"check": {"type": "object"}},
                    "required": ["check"],
                },
            },
        }


class RemoveAccessCheck(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], check_id: str = None) -> str:
        checks = data.get("access_checks", {}).values()
        data["access_checks"] = [c for c in checks.values() if c.get("check_id") != check_id]
        payload = {"removed_check_id": check_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RemoveAccessCheck",
                "description": "Remove an access check by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"check_id": {"type": "string"}},
                    "required": ["check_id"],
                },
            },
        }


#-------------------- Task List Entries --------------------
class ModifyChecklistItem(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], updates: dict[str, Any] = None, item_id: str = None) -> str:
        updates = updates or {}
        items = data.get("checklist_items", {}).values()
        for i in items.values():
            if i.get("item_id") == item_id:
                i.update(updates)
                i["updated_at"] = _fixed_now_iso()
        payload = {"updated_item_id": item_id, "updates": updates}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateChecklistItem",
                "description": "Update a checklist task.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "item_id": {"type": "string"},
                        "updates": {"type": "object"},
                    },
                    "required": ["item_id", "updates"],
                },
            },
        }


class AddChecklistItem(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], item: dict = None) -> str:
        new_item = item or {}
        items = data.get("checklist_items", {}).values()
        data["checklist_items"][new_item["checklist_item_id"]] = new_item
        data["checklist_items"] = items
        payload = {"added_item": new_item}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "addChecklistItem",
                "description": "Add a new checklist item.",
                "parameters": {
                    "type": "object",
                    "properties": {"item": {"type": "object"}},
                    "required": ["item"],
                },
            },
        }


class RemoveChecklistItem(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], item_id: str = None) -> str:
        items = data.get("checklist_items", {}).values()
        data["checklist_items"] = [i for i in items.values() if i.get("item_id") != item_id]
        payload = {"removed_item_id": item_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RemoveChecklistItem",
                "description": "Remove a checklist item by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"item_id": {"type": "string"}},
                    "required": ["item_id"],
                },
            },
        }


#-------------------- Files Attached --------------------
class ModifyAttachment(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], updates: dict[str, Any] = None, attachment_id: str = None) -> str:
        updates = updates or {}
        attach_id = attachment_id
        attachments = data.get("attachments", {}).values()
        for a in attachments.values():
            if a.get("attachment_id") == attach_id:
                a.update(updates)
                a["updated_at"] = _fixed_now_iso()
        payload = {"updated_attachment_id": attach_id, "updates": updates}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateAttachment",
                "description": "Update an attachment metadata.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "attachment_id": {"type": "string"},
                        "updates": {"type": "object"},
                    },
                    "required": ["attachment_id", "updates"],
                },
            },
        }


class AddAttachment(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], attachment: dict = None) -> str:
        new_attach = attachment or {}
        attachments = data.get("attachments", {}).values()
        data["attachments"][attachment_id] = new_attach
        data["attachments"] = attachments
        payload = {"added_attachment": new_attach}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddAttachment",
                "description": "Add a new attachment.",
                "parameters": {
                    "type": "object",
                    "properties": {"attachment": {"type": "object"}},
                    "required": ["attachment"],
                },
            },
        }


class RemoveAttachment(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], attachment_id: str = None) -> str:
        attachments = data.get("attachments", {}).values()
        data["attachments"] = [
            a for a in attachments.values() if a.get("attachment_id") != attachment_id
        ]
        payload = {"removed_attachment_id": attachment_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RemoveAttachment",
                "description": "Remove an attachment by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"attachment_id": {"type": "string"}},
                    "required": ["attachment_id"],
                },
            },
        }


#-------------------- Email Tags --------------------
class ModifyEmailLabel(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], 
        updates: dict[str, Any] = None, 
        label_id: str = None,
        email_id: str = None
    ) -> str:
        updates = updates or {}
        labels = data.get("email_labels", {}).values()
        for l in labels.values():
            if l.get("label_id") == label_id:
                l.update(updates)
                l["updated_at"] = _fixed_now_iso()
        payload = {"updated_label_id": label_id, "updates": updates}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateEmailLabel",
                "description": "Update an email label.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "label_id": {"type": "string"},
                        "updates": {"type": "object"},
                    },
                    "required": ["label_id", "updates"],
                },
            },
        }


class AddEmailLabel(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], label: dict = None) -> str:
        new_label = label or {}
        labels = data.get("email_labels", {}).values()
        data["email_labels"][new_label["email_label_id"]] = new_label
        data["email_labels"] = labels
        payload = {"added_label": new_label}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "addEmailLabel",
                "description": "Add a new email label.",
                "parameters": {
                    "type": "object",
                    "properties": {"label": {"type": "object"}},
                    "required": ["label"],
                },
            },
        }


class RemoveEmailLabel(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], label_id: str = None) -> str:
        labels = data.get("email_labels", {}).values()
        data["email_labels"] = [l for l in labels.values() if l.get("label_id") != label_id]
        payload = {"removed_label_id": label_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "removeEmailLabel",
                "description": "Remove an email label by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"label_id": {"type": "string"}},
                    "required": ["label_id"],
                },
            },
        }


#-------------------- Messages --------------------
class ModifyEmail(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], updates: dict = None, message_id: str = None, email_id: str = None) -> str:
        updates = updates or {}
        emails = data.get("emails", {}).values()
        for e in emails.values():
            if e.get("message_id") == message_id:
                e.update(updates)
                e["updated_at"] = _fixed_now_iso()
        payload = {"updated_message_id": message_id, "updates": updates}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateEmail",
                "description": "Update an email record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "message_id": {"type": "string"},
                        "updates": {"type": "object"},
                    },
                    "required": ["message_id", "updates"],
                },
            },
        }


class SendEmail(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], email: dict = None, email_id: Any = None,
    updates: Any = None,
    ) -> str:
        new_email = email or {}
        emails = data.get("emails", {}).values()
        data["emails"][email_id] = new_email
        data["emails"] = emails
        payload = {"sent_email": new_email}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SendEmail",
                "description": "Send a new email and add it to the record.",
                "parameters": {
                    "type": "object",
                    "properties": {"email": {"type": "object"}},
                    "required": ["email"],
                },
            },
        }


class DeleteEmail(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], message_id: str = None, email_id: Any = None) -> str:
        emails = data.get("emails", {}).values()
        data["emails"] = [e for e in emails.values() if e.get("message_id") != message_id]
        payload = {"deleted_message_id": message_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DeleteEmail",
                "description": "Delete an email by message ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"message_id": {"type": "string"}},
                    "required": ["message_id"],
                },
            },
        }


#-------------------- Stock Items --------------------
class ModifyAsset(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], updates: dict = None, asset_tag: str = None) -> str:
        updates = updates or {}
        assets = data.get("inventory_assets", {}).values()
        for a in assets.values():
            if a.get("asset_tag") == asset_tag:
                a.update(updates)
                a["updated_at"] = _fixed_now_iso()
        payload = {"updated_asset_tag": asset_tag, "updates": updates}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAsset",
                "description": "Update an inventory asset.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_tag": {"type": "string"},
                        "updates": {"type": "object"},
                    },
                    "required": ["asset_tag", "updates"],
                },
            },
        }


class AssignAsset(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], asset_tag: str = None, candidate_id: str = None) -> str:
        assets = data.get("inventory_assets", {}).values()
        for a in assets.values():
            if a.get("asset_tag") == asset_tag:
                a["assigned_candidate_id_nullable"] = candidate_id
                a["status"] = "Assigned"
                a["updated_at"] = _fixed_now_iso()
        payload = {"assigned_asset_tag": asset_tag, "candidate_id": candidate_id}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AssignAsset",
                "description": "Assign an asset to a candidate.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_tag": {"type": "string"},
                        "candidate_id": {"type": "string"},
                    },
                    "required": ["asset_tag", "candidate_id"],
                },
            },
        }


class ReleaseAsset(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], asset_tag: str = None) -> str:
        assets = data.get("inventory_assets", {}).values()
        for a in assets.values():
            if a.get("asset_tag") == asset_tag:
                a["assigned_candidate_id_nullable"] = None
                a["status"] = "Available"
                a["updated_at"] = _fixed_now_iso()
        payload = {"released_asset_tag": asset_tag}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ReleaseAsset",
                "description": "Release an assigned asset.",
                "parameters": {
                    "type": "object",
                    "properties": {"asset_tag": {"type": "string"}},
                    "required": ["asset_tag"],
                },
            },
        }


#-------------------- Induction Documents --------------------
class ModifyOnboardingFile(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], updates: dict[str, Any] = None, file_path: str = None,
    candidate_id: Any = None,
    ) -> str:
        updates = updates or {}
        files = data.get("onboarding_files", {}).values()
        for f in files.values():
            if f.get("file_path") == file_path:
                f.update(updates)
                f["updated_at"] = _fixed_now_iso()
        payload = {"updated_file_path": file_path, "updates": updates}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateOnboardingFile",
                "description": "Update an onboarding file content or metadata.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "file_path": {"type": "string"},
                        "updates": {"type": "object"},
                    },
                    "required": ["file_path", "updates"],
                },
            },
        }


class AddOnboardingFile(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], file: dict = None, candidate_id: Any = None, file_name: str = None, file_path: str = None) -> str:
        new_file = file or {}
        files = data.get("onboarding_files", {}).values()
        data["onboarding_files"][new_file["onboarding_file_id"]] = new_file
        data["onboarding_files"] = files
        payload = {"added_file": new_file}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddOnboardingFile",
                "description": "Add a new onboarding file.",
                "parameters": {
                    "type": "object",
                    "properties": {"file": {"type": "object"}},
                    "required": ["file"],
                },
            },
        }


class RemoveOnboardingFile(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], file_path: str = None) -> str:
        files = data.get("onboarding_files", {}).values()
        data["onboarding_files"] = [f for f in files.values() if f.get("file_path") != file_path]
        payload = {"removed_file_path": file_path}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RemoveOnboardingFile",
                "description": "Remove an onboarding file by file path.",
                "parameters": {
                    "type": "object",
                    "properties": {"file_path": {"type": "string"}},
                    "required": ["file_path"],
                },
            },
        }


class RecordTerminalLog(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], event_type: str = None, message: str = None, candidate_id: str = None) -> str:
        terminal_logs = data.setdefault("terminal_logs", [])
        log_entry = {
            "event_type": event_type,
            "message": message,
            "candidate_id": candidate_id,
            "timestamp": _fixed_now_iso(),
        }
        terminal_logs.append(log_entry)
        payload = {"logged_event": log_entry}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RecordTerminalLog",
                "description": "Logs a terminal event for audit/debug purposes.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "event_type": {"type": "string"},
                        "message": {"type": "string"},
                        "candidate_id": {"type": "string"},
                    },
                    "required": ["event_type", "message"],
                },
            },
        }


class ApplyLabelToEmail(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], email_id: str = None, label_id: str = None) -> str:
        email_labels = data.get("email_labels", {}).values()

        # Search for the email in the list and assign the tag
        for e in email_labels.values():
            if e.get("email_id") == email_id:
                applied_labels = e.setdefault("labels", [])
                if label_id not in applied_labels:
                    applied_data["email_labels"][label_id["email_label_id"]] = label_id
                break
        else:
            # If the email is not located, you may create a new record
            email_labels.append({"email_id": email_id, "labels": [label_id]})
            data["email_labels"] = email_labels
        payload = {"email_id": email_id, "applied_label_id": label_id, "status": "Success"}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ApplyLabelToEmail",
                "description": "Applies a label to an email.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "email_id": {"type": "string"},
                        "label_id": {"type": "string"},
                    },
                    "required": ["email_id", "label_id"],
                },
            },
        }


#Conclusion of 30 utilities
TOOLS = [
    ModifyCandidate(),
    AddCandidate(),
    RemoveCandidate(),
    ModifyAssetRequest(),
    AddAssetRequest(),
    RemoveAssetRequest(),
    ModifyAccessCheck(),
    AddAccessCheck(),
    RemoveAccessCheck(),
    ModifyChecklistItem(),
    AddChecklistItem(),
    RemoveChecklistItem(),
    ModifyAttachment(),
    AddAttachment(),
    RemoveAttachment(),
    ModifyEmailLabel(),
    AddEmailLabel(),
    RemoveEmailLabel(),
    ModifyEmail(),
    SendEmail(),
    DeleteEmail(),
    ModifyAsset(),
    AssignAsset(),
    ReleaseAsset(),
    ModifyOnboardingFile(),
    AddOnboardingFile(),
    RemoveOnboardingFile(),
    RecordTerminalLog(),
    ApplyLabelToEmail(),
]
