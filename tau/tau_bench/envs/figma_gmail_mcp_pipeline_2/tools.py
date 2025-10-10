import json
from typing import Any, Dict, List, Optional
from domains.dto import Tool
import re
import html

_VALID_TYPES = {"FILE", "PAGE", "FRAME"}


def get_now_timestamp() -> str:
    return "2024-08-23T12:00:00Z"


def get_next_art_id(data):
    narts = len(data.get("figma_artifacts", []))
    next_num = narts + 1
    return f"art_0{next_num}"

def get_next_asset_id(data):
    nasset = len(data.get("assets", []))
    next_num = nasset + 1
    return f"asset_0{next_num}"

def get_next_cycle_id(data):
    ncylcles = len(data.get("review_cycles", []))
    next_num = ncylcles + 1
    return f"cycle_0{next_num}"

def get_next_thread_id(data):
    nthreads = len(data.get("gmail_threads", []))
    next_num = nthreads + 1
    return f"thread_0{next_num}"

def get_next_message_id(data):
    nmsgs = len(data.get("gmail_messages", []))
    next_num = nmsgs + 1
    return f"msg_0{next_num}"

def get_next_comment_id(data):
    ncom = len(data.get("figma_comments", []))
    next_num = ncom + 1
    return f"comment_0{next_num}"

def get_next_approve_id(data):
    ncom = len(data.get("review_approvals", []))
    next_num = ncom + 1
    return f"approval_0{next_num}"

def get_next_release_id(data):
    ncom = len(data.get("releases", []))
    next_num = ncom + 1
    return f"release_0{next_num}"

def get_next_diff_id(data):
    ncom = len(data.get("release_diffs", []))
    next_num = ncom + 1
    return f"diff_0{next_num}"

def get_next_audit_id(data):
    ncom = len(data.get("audits", []))
    next_num = ncom + 1
    return f"audit_0{next_num}"

def get_next_finding_ds_id(data):
    ncom = len(data.get("audit_findings_ds", []))
    next_num = ncom + 1
    return f"finding_ds_0{next_num}"

def get_next_finding_a11y_id(data):
    ncom = len(data.get("audit_findings_a11y", []))
    next_num = ncom + 1
    return f"finding_a11y_0{next_num}"




class GetArtifactWithId(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        if not kwargs.get("artifact_id"):
            return json.dumps({"error": "Missing required field: artifact_id"}, indent=2)

        artifact_id = kwargs.get("artifact_id")
        artifacts = data.get("figma_artifacts", [])
        for row in artifacts:
            if row.get("artifact_id") == artifact_id:
                return json.dumps(row, indent=2)

        return json.dumps({"error": f"No artifact with id '{artifact_id}'."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_artifact_with_id",
                "description": "Fetch a single Figma artifact by artifact_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {"type": "string"}
                    },
                    "required": ["artifact_id"]
                }
            }
        }


class GetAllArtifactsOfTypeWithTagsAndEmail(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        if not kwargs.get("artifact_type"):
            return json.dumps({"error": "Missing required field: artifact_type"}, indent=2)

        artifact_type = kwargs.get("artifact_type")
        tags = kwargs.get("tags")
        owner_email = kwargs.get("owner_email")

        artifacts = data.get("figma_artifacts", [])
        results = []
        for row in artifacts:
            if row.get("artifact_type") != artifact_type:
                continue
            if tags:
                row_tags = row.get("current_tags") or []
                if not set(tags).issubset(set(row_tags)):
                    continue
            if owner_email and row.get("owner_email") != owner_email:
                continue
            results.append(row)

        results.sort(key=lambda r: str(r.get("artifact_id")))
        return json.dumps({"count": len(results), "artifacts": results}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_all_artifacts_of_type_with_tags_and_email",
                "description": "Return artifacts of the given type, optionally filtered to include all specified tags and a specific owner_email.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_type": {"type": "string"},
                        "tags": {"type": "array", "items": {"type": "string"}},
                        "owner_email": {"type": "string"}
                    },
                    "required": ["artifact_type"]
                }
            }
        }


class CreateNewArtifact(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        required = ["artifact_type", "artifact_name", "figma_file_id", "page_id", "owner_email", "deep_link"]
        missing = [f for f in required if f not in kwargs or kwargs[f] is None]
        if missing:
            return json.dumps({"error": f"Missing required fields: {', '.join(missing)}"}, indent=2)

        if kwargs.get("artifact_type") == "FRAME" and not kwargs.get("frame_id_nullable"):
            return json.dumps({"error": "frame_id_nullable is required for FRAME artifacts"}, indent=2)

        artifacts = data.get("figma_artifacts", [])
        artifact_id = get_next_art_id(data)
        created_ts = get_now_timestamp()
        current_tags = kwargs.get("current_tags") or []

        new_row = {
            "artifact_id": artifact_id,
            "figma_file_id": kwargs["figma_file_id"],
            "page_id": kwargs["page_id"],
            "frame_id_nullable": kwargs.get("frame_id_nullable") if kwargs.get("artifact_type") == "FRAME" else None,
            "artifact_type": kwargs["artifact_type"],
            "artifact_name": kwargs["artifact_name"],
            "owner_email": kwargs["owner_email"],
            "modified_ts": created_ts,
            "deep_link": kwargs["deep_link"],
            "current_tags": current_tags,
        }

        artifacts.append(new_row)
        data["figma_artifacts"] = artifacts
        return json.dumps(new_row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_new_artifact",
                "description": "Create a new figma_artifacts row. If artifact_type=FRAME, frame_id_nullable is required.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_type": {"type": "string", "enum": ["FILE", "PAGE", "FRAME"]},
                        "artifact_name": {"type": "string"},
                        "figma_file_id": {"type": "string"},
                        "page_id": {"type": "string"},
                        "frame_id_nullable": {"type": ["string", "null"]},
                        "owner_email": {"type": "string"},
                        "deep_link": {"type": "string"},
                        "current_tags": {"type": "array", "items": {"type": "string"}, "default": []}
                    },
                    "required": ["artifact_type", "artifact_name", "figma_file_id", "page_id", "owner_email", "deep_link"]
                }
            }
        }


class GetArtifactsWithFileId(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        if not kwargs.get("figma_file_id"):
            return json.dumps({"error": "Missing required field: figma_file_id"}, indent=2)

        figma_file_id = kwargs.get("figma_file_id")
        artifact_type = kwargs.get("artifact_type")
        page_id = kwargs.get("page_id")
        frame_id = kwargs.get("frame_id")

        artifacts = data.get("figma_artifacts", [])
        results = []
        for row in artifacts:
            if row.get("figma_file_id") != figma_file_id:
                continue
            if artifact_type and row.get("artifact_type") != artifact_type:
                continue
            if frame_id is not None and row.get("frame_id_nullable") != frame_id:
                continue
            if frame_id is None and page_id is not None and row.get("page_id") != page_id:
                continue
            results.append(row)

        results.sort(key=lambda r: str(r.get("artifact_id")))
        if not results:
            return json.dumps({"error": "No artifacts matched"}, indent=2)
        return json.dumps({"count": len(results), "artifacts": results}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_artifacts_with_file_id",
                "description": "Return artifacts for a figma_file_id. Optional filters: artifact_type, page_id, frame_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "figma_file_id": {"type": "string"},
                        "artifact_type": {"type": "string", "enum": ["FILE", "PAGE", "FRAME"]},
                        "page_id": {"type": "string"},
                        "frame_id": {"type": "string"}
                    },
                    "required": ["figma_file_id"]
                }
            }
        }


class GetAssetById(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        if not kwargs.get("asset_id"):
            return json.dumps({"error": "Missing required field: asset_id"}, indent=2)

        asset_id = kwargs.get("asset_id")
        assets = data.get("assets", [])
        for row in assets:
            if row.get("asset_id") == asset_id:
                return json.dumps(row, indent=2)
        return json.dumps({"error": f"No asset with id '{asset_id}'"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_asset_by_id",
                "description": "Fetch a single asset object by asset_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_id": {"type": "string"}
                    },
                    "required": ["asset_id"]
                }
            }
        }


class GetAssetsByArtifactId(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        if not kwargs.get("artifact_id"):
            return json.dumps({"error": "Missing required field: artifact_id"}, indent=2)

        artifact_id = kwargs.get("artifact_id")
        assets = data.get("assets", [])

        results = [row for row in assets if row.get("artifact_id_nullable") == artifact_id]

        if not results:
            return json.dumps({"error": f"No assets found for artifact_id '{artifact_id}'"}, indent=2)

        results.sort(key=lambda r: str(r.get("asset_id")))
        return json.dumps({"count": len(results), "assets": results}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_assets_by_artifact_id",
                "description": "Return all asset objects belonging to the given artifact_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {"type": "string"}
                    },
                    "required": ["artifact_id"]
                }
            }
        }


class CreateNewAsset(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        required = ["artifact_id", "export_profile", "file_size_bytes", "storage_ref"]
        missing = [f for f in required if f not in kwargs or kwargs[f] is None]
        if missing:
            return json.dumps({"error": f"Missing required fields: {', '.join(missing)}"}, indent=2)

        artifact_id = kwargs.get("artifact_id")
        export_profile = kwargs.get("export_profile")
        file_size_bytes = kwargs.get("file_size_bytes")
        storage_ref = kwargs.get("storage_ref")

        assets = data.get("assets", [])
        asset_id = get_next_asset_id(data)
        created_ts = get_now_timestamp()

        new_asset = {
            "asset_id": asset_id,
            "artifact_id_nullable": artifact_id,
            "export_profile": export_profile,
            "file_size_bytes": file_size_bytes,
            "storage_ref": storage_ref,
            "created_ts": created_ts,
            "dlp_scan_status": "CLEAN",
            "dlp_scan_details_nullable": None
        }

        assets.append(new_asset)
        data["assets"] = assets
        return json.dumps(new_asset, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_new_asset",
                "description": "Create a new asset row for an artifact. Defaults: dlp_scan_status=CLEAN, dlp_scan_details_nullable=null.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {"type": "string"},
                        "export_profile": {"type": "string"},
                        "file_size_bytes": {"type": "integer", "minimum": 0},
                        "storage_ref": {"type": "string"}
                    },
                    "required": ["artifact_id", "export_profile", "file_size_bytes", "storage_ref"]
                }
            }
        }


class CreateNewCycle(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        if not kwargs.get("artifact_id") or not kwargs.get("sla_deadline_ts"):
            missing = []
            if not kwargs.get("artifact_id"):
                missing.append("artifact_id")
            if not kwargs.get("sla_deadline_ts"):
                missing.append("sla_deadline_ts")
            return json.dumps({"error": f"Missing required fields: {', '.join(missing)}"}, indent=2)

        cycles: List[Dict[str, Any]] = data.get("review_cycles", [])
        cycle_id = get_next_cycle_id(data)
        created_ts = get_now_timestamp()
        thread_id: Optional[str] = kwargs.get("thread_id")
        sla_deadline_ts: str = kwargs.get("sla_deadline_ts")

        new_cycle = {
            "cycle_id": cycle_id,
            "artifact_id": kwargs["artifact_id"],
            "thread_id_nullable": thread_id,
            "status": "IN_FLIGHT",
            "created_ts": created_ts,
            "sla_deadline_ts": sla_deadline_ts,
            "sla_breached_flag": False,
            "escalated_ts_nullable": None
        }

        cycles.append(new_cycle)
        data["review_cycles"] = cycles
        return json.dumps(new_cycle, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_new_cycle",
                "description": "Create a new review cycle with defaults: status=IN_FLIGHT, sla_breached_flag=False, escalated_ts_nullable=None. thread_id is optional. sla_deadline_ts is required.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {"type": "string"},
                        "thread_id": {"type": ["string", "null"]},
                        "sla_deadline_ts": {"type": "string"}
                    },
                    "required": ["artifact_id", "sla_deadline_ts"]
                }
            }
        }


class UpdateCycleStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        required = ["cycle_id", "new_status"]
        missing = [f for f in required if f not in kwargs or kwargs[f] is None]
        if missing:
            return json.dumps({"error": f"Missing required fields: {', '.join(missing)}"}, indent=2)

        cycle_id = kwargs.get("cycle_id")
        new_status = kwargs.get("new_status")
        escalated_ts: Optional[str] = kwargs.get("escalated_ts")
        thread_id: Optional[str] = kwargs.get("thread_id")

        cycles: List[Dict[str, Any]] = data.get("review_cycles", [])
        for row in cycles:
            if row.get("cycle_id") == cycle_id:
                row["status"] = new_status
                if "thread_id" in kwargs:
                    row["thread_id_nullable"] = thread_id
                if "escalated_ts" in kwargs:
                    row["escalated_ts_nullable"] = escalated_ts
                    if escalated_ts is not None:
                        row["sla_breached_flag"] = True
                return json.dumps(row, indent=2)

        return json.dumps({"error": f"No cycle with id '{cycle_id}'"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_cycle_status",
                "description": "Update a review cycle status; optionally set thread_id and escalated_ts. If escalated_ts is not null, sla_breached_flag becomes True.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cycle_id": {"type": "string"},
                        "new_status": {"type": "string"},
                        "escalated_ts": {"type": ["string", "null"]},
                        "thread_id": {"type": ["string", "null"]}
                    },
                    "required": ["cycle_id", "new_status"]
                }
            }
        }


class GetCycleByArtifactAndThread(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        if not kwargs.get("thread_id"):
            return json.dumps({"error": "Missing required field: thread_id"}, indent=2)

        thread_id = kwargs.get("thread_id")
        artifact_id: Optional[str] = kwargs.get("artifact_id")

        cycles: List[Dict[str, Any]] = data.get("review_cycles", [])
        results: List[Dict[str, Any]] = []
        for row in cycles:
            if row.get("thread_id_nullable") != thread_id:
                continue
            if artifact_id and row.get("artifact_id") != artifact_id:
                continue
            results.append(row)

        results.sort(key=lambda r: (str(r.get("created_ts")), str(r.get("cycle_id"))))
        if not results:
            if artifact_id:
                return json.dumps({"error": f"No cycles found for thread_id '{thread_id}' and artifact_id '{artifact_id}'"}, indent=2)
            return json.dumps({"error": f"No cycles found for thread_id '{thread_id}'"}, indent=2)

        return json.dumps({"count": len(results), "cycles": results}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_cycle_by_artifact_and_thread",
                "description": "Return review cycles for a thread, optionally filtered by artifact_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "thread_id": {"type": "string"},
                        "artifact_id": {"type": "string"}
                    },
                    "required": ["thread_id"]
                }
            }
        }


class GetCycleById(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        if not kwargs.get("cycle_id"):
            return json.dumps({"error": "Missing required field: cycle_id"}, indent=2)

        cycle_id = kwargs.get("cycle_id")
        cycles: List[Dict[str, Any]] = data.get("review_cycles", [])
        for row in cycles:
            if row.get("cycle_id") == cycle_id:
                return json.dumps(row, indent=2)

        return json.dumps({"error": f"No cycle with id '{cycle_id}'"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_cycle_by_id",
                "description": "Fetch a single review cycle by cycle_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cycle_id": {"type": "string"}
                    },
                    "required": ["cycle_id"]
                }
            }
        }


class StartEmailThread(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        required = ["subject", "sender_id", "recipients", "current_labels", "body_html", "attachments_asset_ids"]
        missing = [f for f in required if f not in kwargs or kwargs[f] is None]
        if missing:
            return json.dumps({"error": f"Missing required fields: {', '.join(missing)}"}, indent=2)

        threads: List[Dict[str, Any]] = data.get("gmail_threads", [])
        messages: List[Dict[str, Any]] = data.get("gmail_messages", [])

        thread_id = get_next_thread_id(data)
        message_id = get_next_message_id(data)
        ts = get_now_timestamp()

        body_html = kwargs["body_html"]
        t = body_html
        t = re.sub(r"</li\s*>", ", ", t, flags=re.IGNORECASE)
        t = re.sub(r"<\s*(br|/p|/ul|/ol)\s*/?>", " ", t, flags=re.IGNORECASE)
        t = re.sub(r"<\s*(p|ul|ol|li)\s*>", " ", t, flags=re.IGNORECASE)
        t = re.sub(r"<[^>]+>", " ", t)
        t = html.unescape(t)
        body_text_stripped = " ".join(t.split())

        new_thread = {
            "thread_id": thread_id,
            "subject": kwargs["subject"],
            "sender_identity": kwargs["sender_id"],
            "recipients": kwargs["recipients"],
            "current_labels": kwargs["current_labels"],
            "created_ts": ts,
            "updated_ts": ts
        }

        new_message = {
            "message_id": message_id,
            "thread_id": thread_id,
            "sender_email": kwargs["sender_id"],
            "body_html": kwargs["body_html"],
            "body_text_stripped": body_text_stripped,
            "sent_ts": ts,
            "attachments_asset_ids": kwargs["attachments_asset_ids"]
        }

        threads.append(new_thread)
        messages.append(new_message)
        data["gmail_threads"] = threads
        data["gmail_messages"] = messages

        return json.dumps({"thread": new_thread, "message": new_message}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "start_email_thread",
                "description": "Create a new Gmail thread and its first message; body_text_stripped is derived from body_html.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subject": {"type": "string"},
                        "sender_id": {"type": "string"},
                        "recipients": {"type": "array", "items": {"type": "string"}},
                        "current_labels": {"type": "array", "items": {"type": "string"}},
                        "body_html": {"type": "string"},
                        "attachments_asset_ids": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["subject", "sender_id", "recipients", "current_labels", "body_html", "attachments_asset_ids"]
                }
            }
        }


class SendEmailInThread(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        required = ["thread_id", "sender_id", "body_html"]
        missing = [f for f in required if f not in kwargs or kwargs[f] is None]
        if missing:
            return json.dumps({"error": f"Missing required fields: {', '.join(missing)}"}, indent=2)

        thread_id = kwargs.get("thread_id")
        sender_id = kwargs.get("sender_id")
        body_html = kwargs.get("body_html")
        attachments_asset_ids: Optional[List[str]] = kwargs.get("attachments_asset_ids") or []

        threads: List[Dict[str, Any]] = data.get("gmail_threads", [])
        messages: List[Dict[str, Any]] = data.get("gmail_messages", [])

        thread = None
        for row in threads:
            if row.get("thread_id") == thread_id:
                thread = row
                break
        if not thread:
            return json.dumps({"error": f"No thread with id '{thread_id}'"}, indent=2)

        allowed = (sender_id == thread.get("sender_identity")) or (sender_id in (thread.get("recipients") or []))
        if not allowed:
            return json.dumps({"error": "SENDER_NOT_AUTHORIZED"}, indent=2)

        t = body_html
        t = re.sub(r"</li\s*>", ", ", t, flags=re.IGNORECASE)
        t = re.sub(r"<\s*(br|/p|/ul|/ol)\s*/?>", " ", t, flags=re.IGNORECASE)
        t = re.sub(r"<\s*(p|ul|ol|li)\s*>", " ", t, flags=re.IGNORECASE)
        t = re.sub(r"<[^>]+>", " ", t)
        t = html.unescape(t)
        body_text_stripped = " ".join(t.split())

        message_id = get_next_message_id(data)
        ts = get_now_timestamp()

        new_message = {
            "message_id": message_id,
            "thread_id": thread_id,
            "sender_email": sender_id,
            "body_html": body_html,
            "body_text_stripped": body_text_stripped,
            "sent_ts": ts,
            "attachments_asset_ids": attachments_asset_ids
        }

        messages.append(new_message)
        thread["updated_ts"] = ts
        data["gmail_messages"] = messages
        data["gmail_threads"] = threads

        return json.dumps({"thread": thread, "message": new_message}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "send_email_in_thread",
                "description": "Send a message in an existing Gmail thread. Sender must match thread sender_identity or be in recipients. HTML body is converted to stripped text.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "thread_id": {"type": "string"},
                        "sender_id": {"type": "string"},
                        "body_html": {"type": "string"},
                        "attachments_asset_ids": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["thread_id", "sender_id", "body_html"]
                }
            }
        }


class GetCompleteEmailThread(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        if not kwargs.get("thread_id"):
            return json.dumps({"error": "Missing required field: thread_id"}, indent=2)

        thread_id = kwargs.get("thread_id")
        threads: List[Dict[str, Any]] = data.get("gmail_threads", [])
        messages: List[Dict[str, Any]] = data.get("gmail_messages", [])

        thread = None
        for row in threads:
            if row.get("thread_id") == thread_id:
                thread = row
                break
        if not thread:
            return json.dumps({"error": f"No thread with id '{thread_id}'"}, indent=2)

        msgs = [m for m in messages if m.get("thread_id") == thread_id]
        msgs.sort(key=lambda r: (str(r.get("sent_ts")), str(r.get("message_id"))))
        return json.dumps({"thread": thread, "messages": msgs, "count": len(msgs)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_complete_email_thread",
                "description": "Return a Gmail thread and all messages within it.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "thread_id": {"type": "string"}
                    },
                    "required": ["thread_id"]
                }
            }
        }


class GetThreadBySubject(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        if not kwargs.get("subject"):
            return json.dumps({"error": "Missing required field: subject"}, indent=2)

        subject = kwargs.get("subject")
        sender_id: Optional[str] = kwargs.get("sender_id")
        label: Optional[str] = kwargs.get("label")

        threads: List[Dict[str, Any]] = data.get("gmail_threads", [])
        results: List[Dict[str, Any]] = []
        for row in threads:
            if row.get("subject") != subject:
                continue
            if sender_id and row.get("sender_identity") != sender_id:
                continue
            if label and label not in (row.get("current_labels") or []):
                continue
            results.append(row)

        results.sort(key=lambda r: str(r.get("thread_id")))
        if not results:
            return json.dumps({"error": f"No thread found with subject '{subject}'"}, indent=2)
        return json.dumps({"count": len(results), "threads": results}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_thread_by_subject",
                "description": "Return Gmail threads matching a subject. Optional filters: sender_id and label.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subject": {"type": "string"},
                        "sender_id": {"type": "string"},
                        "label": {"type": "string"}
                    },
                    "required": ["subject"]
                }
            }
        }


class AddComment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        required = ["artifact_id", "author_email", "content", "resolved_flag"]
        missing = [f for f in required if f not in kwargs or kwargs[f] is None]
        if missing:
            return json.dumps({"error": f"Missing required fields: {', '.join(missing)}"}, indent=2)

        comments: List[Dict[str, Any]] = data.get("figma_comments", [])
        comment_id = get_next_comment_id(data)
        created_ts = get_now_timestamp()
        source_message_id: Optional[str] = kwargs.get("source_message_id")

        new_comment = {
            "comment_id": comment_id,
            "artifact_id": kwargs["artifact_id"],
            "author_email": kwargs["author_email"],
            "content": kwargs["content"],
            "source_message_id_nullable": source_message_id,
            "created_ts": created_ts,
            "resolved_flag": kwargs["resolved_flag"]
        }

        comments.append(new_comment)
        data["figma_comments"] = comments
        return json.dumps(new_comment, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_comment",
                "description": "Add a new comment to figma_comments. source_message_id may be null.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {"type": "string"},
                        "author_email": {"type": "string"},
                        "content": {"type": "string"},
                        "source_message_id": {"type": ["string", "null"]},
                        "resolved_flag": {"type": "boolean"}
                    },
                    "required": ["artifact_id", "author_email", "content", "resolved_flag"]
                }
            }
        }


class ApproveReview(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        required = ["cycle_id", "approver_email"]
        missing = [f for f in required if f not in kwargs or kwargs[f] is None]
        if missing:
            return json.dumps({"error": f"Missing required fields: {', '.join(missing)}"}, indent=2)

        cycle_id = kwargs.get("cycle_id")
        approver_email = kwargs.get("approver_email")
        approval_comment_ref: Optional[str] = kwargs.get("approval_comment_ref")

        approvals: List[Dict[str, Any]] = data.get("review_approvals", [])
        cycles: List[Dict[str, Any]] = data.get("review_cycles", [])

        cycle = None
        for row in cycles:
            if row.get("cycle_id") == cycle_id:
                cycle = row
                break
        if not cycle:
            return json.dumps({"error": f"No cycle with id '{cycle_id}'"}, indent=2)

        now_ts = get_now_timestamp()
        deadline_ts = cycle.get("sla_deadline_ts")
        if deadline_ts is not None and str(now_ts) > str(deadline_ts):
            cycle["sla_breached_flag"] = True
        else:
            cycle["sla_breached_flag"] = False

        sla_breached_flag = bool(cycle.get("sla_breached_flag"))
        ts = get_now_timestamp()
        approval_id = get_next_approve_id(data)

        new_approval = {
            "approval_id": approval_id,
            "cycle_id": cycle_id,
            "approver_email": approver_email,
            "approved_ts": ts,
            "sla_breached_flag": sla_breached_flag,
            "approval_comment_ref_nullable": approval_comment_ref
        }

        approvals.append(new_approval)
        cycle["status"] = "APPROVED"

        data["review_approvals"] = approvals
        data["review_cycles"] = cycles

        return json.dumps({"approval": new_approval, "cycle": cycle}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "approve_review",
                "description": "Approve a review cycle; recompute and set the SLA-breached flag by comparing sla_deadline_ts with the current timestamp.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cycle_id": {"type": "string"},
                        "approver_email": {"type": "string"},
                        "approval_comment_ref": {"type": ["string", "null"]}
                    },
                    "required": ["cycle_id", "approver_email"]
                }
            }
        }
    

class GetReleaseDetailsByName(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        if not kwargs.get("release_name"):
            return json.dumps({"error": "Missing required field: release_name"}, indent=2)

        release_name = kwargs.get("release_name")
        releases: List[Dict[str, Any]] = data.get("releases", [])

        results: List[Dict[str, Any]] = [r for r in releases if r.get("release_name") == release_name]
        results.sort(key=lambda r: (str(r.get("created_ts")), str(r.get("release_id"))))

        if not results:
            return json.dumps({"error": f"No release found with release_name '{release_name}'"}, indent=2)

        return json.dumps({"count": len(results), "releases": results}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_release_details_by_name",
                "description": "Return releases matching an exact release_name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "release_name": {"type": "string"}
                    },
                    "required": ["release_name"]
                }
            }
        }
    

class CreateNewRelease(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        required = ["figma_file_id", "version_id", "version_tag", "release_name", "owner_email"]
        missing = [f for f in required if f not in kwargs or kwargs[f] is None]
        if missing:
            return json.dumps({"error": f"Missing required fields: {', '.join(missing)}"}, indent=2)

        releases: List[Dict[str, Any]] = data.get("releases", [])
        release_id = get_next_release_id(data)
        created_ts = get_now_timestamp()
        thread_id = kwargs.get("thread_id")

        new_release = {
            "release_id": release_id,
            "figma_file_id": kwargs["figma_file_id"],
            "version_id": kwargs["version_id"],
            "version_tag": kwargs["version_tag"],
            "release_name": kwargs["release_name"],
            "owner_email": kwargs["owner_email"],
            "created_ts": created_ts,
            "thread_id_nullable": thread_id
        }

        releases.append(new_release)
        data["releases"] = releases
        return json.dumps(new_release, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_new_release",
                "description": "Create a new release row in releases.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "figma_file_id": {"type": "string"},
                        "version_id": {"type": "string"},
                        "version_tag": {"type": "string"},
                        "release_name": {"type": "string"},
                        "owner_email": {"type": "string"},
                        "thread_id": {"type": ["string", "null"]}
                    },
                    "required": ["figma_file_id", "version_id", "version_tag", "release_name", "owner_email"]
                }
            }
        }


class GetReleaseById(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        if not kwargs.get("release_id"):
            return json.dumps({"error": "Missing required field: release_id"}, indent=2)

        release_id = kwargs.get("release_id")
        releases: List[Dict[str, Any]] = data.get("releases", [])
        for row in releases:
            if row.get("release_id") == release_id:
                return json.dumps(row, indent=2)

        return json.dumps({"error": f"No release with id '{release_id}'"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_release_by_id",
                "description": "Fetch a single release by release_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "release_id": {"type": "string"}
                    },
                    "required": ["release_id"]
                }
            }
        }


class CreateReleaseDiff(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        required = ["release_id"]
        missing = [f for f in required if f not in kwargs or kwargs[f] is None]
        if missing:
            return json.dumps({"error": f"Missing required fields: {', '.join(missing)}"}, indent=2)

        release_diffs: List[Dict[str, Any]] = data.get("release_diffs", [])
        diff_id = get_next_diff_id(data)
        created_ts = get_now_timestamp()

        frames_added = kwargs.get("frames_added") or []
        frames_updated = kwargs.get("frames_updated") or []
        frames_removed = kwargs.get("frames_removed") or []
        component_version_bumps = kwargs.get("component_version_bumps") or []
        changelog_highlights = kwargs.get("changelog_highlights") or []
        prior_release_id = kwargs.get("prior_release_id")

        new_diff = {
            "diff_id": diff_id,
            "release_id": kwargs["release_id"],
            "prior_release_id_nullable": prior_release_id,
            "created_ts": created_ts,
            "frames_added": frames_added,
            "frames_updated": frames_updated,
            "frames_removed": frames_removed,
            "component_version_bumps": component_version_bumps,
            "changelog_highlights": changelog_highlights
        }

        release_diffs.append(new_diff)
        data["release_diffs"] = release_diffs
        return json.dumps(new_diff, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_release_diff",
                "description": "Create a new release_diff row for a release.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "release_id": {"type": "string"},
                        "prior_release_id": {"type": ["string", "null"]},
                        "frames_added": {"type": "array", "items": {"type": "string"}},
                        "frames_updated": {"type": "array", "items": {"type": "string"}},
                        "frames_removed": {"type": "array", "items": {"type": "string"}},
                        "component_version_bumps": {"type": "array", "items": {"type": "string"}},
                        "changelog_highlights": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["release_id"]
                }
            }
        }


class GetReleaseDiffByReleaseId(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        if not kwargs.get("release_id"):
            return json.dumps({"error": "Missing required field: release_id"}, indent=2)

        release_id = kwargs.get("release_id")
        release_diffs: List[Dict[str, Any]] = data.get("release_diffs", [])
        for row in release_diffs:
            if row.get("release_id") == release_id:
                return json.dumps(row, indent=2)

        return json.dumps({"error": f"No release_diff for release_id '{release_id}'"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_release_diff_by_release_id",
                "description": "Fetch the release_diff row for a given release_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "release_id": {"type": "string"}
                    },
                    "required": ["release_id"]
                }
            }
        }


class CompareBeforeAfterVisuals(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        if not kwargs.get("before_release_id") or not kwargs.get("after_release_id"):
            missing = []
            if not kwargs.get("before_release_id"):
                missing.append("before_release_id")
            if not kwargs.get("after_release_id"):
                missing.append("after_release_id")
            return json.dumps({"error": f"Missing required fields: {', '.join(missing)}"}, indent=2)

        release_diffs: List[Dict[str, Any]] = data.get("release_diffs", [])
        diff_by_id = {d.get("release_id"): d for d in release_diffs}

        def lineage(rid: str) -> List[str]:
            ids = []
            cur = rid
            seen = set()
            while cur and cur not in seen and cur in diff_by_id:
                ids.append(cur)
                seen.add(cur)
                cur = diff_by_id[cur].get("prior_release_id_nullable")
            ids.reverse()
            return ids

        def artifacts_for_release(rid: str) -> List[str]:
            if rid not in diff_by_id:
                return []
            s = set()
            for lr in lineage(rid):
                d = diff_by_id.get(lr, {})
                for a in d.get("frames_added") or []:
                    s.add(a)
                for u in d.get("frames_updated") or []:
                    s.add(u)
                for r in d.get("frames_removed") or []:
                    if r in s:
                        s.remove(r)
            return sorted(s)

        before_release_id = kwargs.get("before_release_id")
        after_release_id = kwargs.get("after_release_id")

        if before_release_id not in diff_by_id:
            return json.dumps({"error": f"No release_diff for release_id '{before_release_id}'"}, indent=2)
        if after_release_id not in diff_by_id:
            return json.dumps({"error": f"No release_diff for release_id '{after_release_id}'"}, indent=2)

        before_list = artifacts_for_release(before_release_id)
        after_list = set(before_list)
        after_diff = diff_by_id[after_release_id]
        for a in (after_diff.get("frames_removed") or []):
            after_list.discard(a)
        for a in (after_diff.get("frames_added") or []):
            after_list.add(a)
        for a in (after_diff.get("frames_updated") or []):
            after_list.add(a)
        final_after_list = sorted(after_list)

        return json.dumps(
            {
                "before": {"release_id": before_release_id, "artifacts": before_list},
                "after": {"release_id": after_release_id, "artifacts": final_after_list}
            },
            indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "compare_before_after_visuals",
                "description": "Return artifact lists for a before release and an after release, carrying all before artifacts forward unless removed in the after release.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "before_release_id": {"type": "string"},
                        "after_release_id": {"type": "string"}
                    },
                    "required": ["before_release_id", "after_release_id"]
                }
            }
        }


class NotifyStakeholders(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        required = ["thread_id", "body_html", "attachments_asset_ids"]
        missing = [f for f in required if f not in kwargs or kwargs[f] is None]
        if missing:
            return json.dumps({"error": f"Missing required fields: {', '.join(missing)}"}, indent=2)

        thread_id = kwargs.get("thread_id")
        body_html = kwargs.get("body_html")
        attachments_asset_ids: List[str] = kwargs.get("attachments_asset_ids")

        threads: List[Dict[str, Any]] = data.get("gmail_threads", [])
        messages: List[Dict[str, Any]] = data.get("gmail_messages", [])

        thread = None
        for row in threads:
            if row.get("thread_id") == thread_id:
                thread = row
                break
        if not thread:
            return json.dumps({"error": f"No thread with id '{thread_id}'"}, indent=2)

        sender_id = thread.get("sender_identity")

        t = body_html
        t = re.sub(r"</li\s*>", ", ", t, flags=re.IGNORECASE)
        t = re.sub(r"<\s*(br|/p|/ul|/ol)\s*/?>", " ", t, flags=re.IGNORECASE)
        t = re.sub(r"<\s*(p|ul|ol|li)\s*>", " ", t, flags=re.IGNORECASE)
        t = re.sub(r"<[^>]+>", " ", t)
        t = html.unescape(t)
        body_text_stripped = " ".join(t.split())

        message_id = get_next_message_id(data)
        ts = get_now_timestamp()

        new_message = {
            "message_id": message_id,
            "thread_id": thread_id,
            "sender_email": sender_id,
            "body_html": body_html,
            "body_text_stripped": body_text_stripped,
            "sent_ts": ts,
            "attachments_asset_ids": attachments_asset_ids
        }

        messages.append(new_message)
        thread["updated_ts"] = ts
        data["gmail_messages"] = messages
        data["gmail_threads"] = threads

        return json.dumps({"thread": thread, "message": new_message}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "notify_stakeholders",
                "description": "Post a notification email in an existing Gmail thread from the thread's sender_identity with the given HTML body and asset attachments.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "thread_id": {"type": "string"},
                        "body_html": {"type": "string"},
                        "attachments_asset_ids": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["thread_id", "body_html", "attachments_asset_ids"]
                }
            }
        }


class CreateNewAudit(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        required = ["artifact_id", "audit_type"]
        missing = [f for f in required if f not in kwargs or kwargs[f] is None]
        if missing:
            return json.dumps({"error": f"Missing required fields: {', '.join(missing)}"}, indent=2)

        audits: List[Dict[str, Any]] = data.get("audits", [])
        audit_id = get_next_audit_id(data)
        created_ts = get_now_timestamp()

        new_audit = {
            "audit_id": audit_id,
            "artifact_id": kwargs["artifact_id"],
            "audit_type": kwargs["audit_type"],
            "created_ts": created_ts,
            "status": "RUNNING",
            "report_asset_id_nullable": None
        }

        audits.append(new_audit)
        data["audits"] = audits
        return json.dumps(new_audit, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_new_audit",
                "description": "Initialize a new audit session for a Figma artifact.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {"type": "string"},
                        "audit_type": {"type": "string", "enum": ["DS_MAPPING", "A11Y", "COMBINED_DS_A11Y"]}
                    },
                    "required": ["artifact_id", "audit_type"]
                }
            }
        }


class RecordAuditFindings(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        if not kwargs.get("audit_id"):
            return json.dumps({"error": "Missing required field: audit_id"}, indent=2)
        if not kwargs.get("ds_findings") and not kwargs.get("a11y_findings"):
            return json.dumps({"error": "At least one of ds_findings or a11y_findings is required"}, indent=2)

        audit_id = kwargs.get("audit_id")
        ds_findings_in: List[Dict[str, Any]] = kwargs.get("ds_findings") or []
        a11y_findings_in: List[Dict[str, Any]] = kwargs.get("a11y_findings") or []

        ds_table: List[Dict[str, Any]] = data.get("audit_findings_ds", [])
        a11y_table: List[Dict[str, Any]] = data.get("audit_findings_a11y", [])

        ds_ids: List[str] = []
        for item in ds_findings_in:
            fid = get_next_finding_ds_id(data)
            row = {
                "finding_id": fid,
                "audit_id": audit_id,
                "layer_id": item.get("layer_id"),
                "layer_name": item.get("layer_name"),
                "finding_type": item.get("finding_type"),
                "recommended_component_id_nullable": item.get("recommended_component_id"),
                "code_connect_link_nullable": item.get("code_connect_link"),
                "severity": item.get("severity")
            }
            ds_table.append(row)
            ds_ids.append(fid)

        a11y_ids: List[str] = []
        for item in a11y_findings_in:
            fid = get_next_finding_a11y_id(data)
            row = {
                "finding_id": fid,
                "audit_id": audit_id,
                "layer_id": item.get("layer_id"),
                "layer_name": item.get("layer_name"),
                "violation_type": item.get("violation_type"),
                "violation_details_json": item.get("violation_details_json"),
                "severity": item.get("severity"),
                "recommended_fix_summary": item.get("recommended_fix_summary")
            }
            a11y_table.append(row)
            a11y_ids.append(fid)

        data["audit_findings_ds"] = ds_table
        data["audit_findings_a11y"] = a11y_table

        return json.dumps(
            {
                "audit_id": audit_id,
                "ds_count": len(ds_ids),
                "a11y_count": len(a11y_ids),
                "ds_finding_ids": ds_ids,
                "a11y_finding_ids": a11y_ids
            },
            indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "record_audit_findings",
                "description": "Record design system mapping findings and accessibility findings for an audit.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string"},
                        "ds_findings": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "layer_id": {"type": "string"},
                                    "layer_name": {"type": "string"},
                                    "finding_type": {"type": "string", "enum": ["UNMAPPED", "SUBSTITUTE_RECOMMENDED", "AMBIGUOUS"]},
                                    "recommended_component_id": {"type": ["string", "null"]},
                                    "code_connect_link": {"type": ["string", "null"]},
                                    "severity": {"type": "string", "enum": ["LOW", "MEDIUM", "HIGH"]}
                                }
                            }
                        },
                        "a11y_findings": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "layer_id": {"type": "string"},
                                    "layer_name": {"type": "string"},
                                    "violation_type": {"type": "string", "enum": ["TOUCH_TARGET", "CONTRAST", "TEXT_SIZING", "RTL"]},
                                    "violation_details_json": {"type": "string"},
                                    "severity": {"type": "string", "enum": ["LOW", "MEDIUM", "HIGH"]},
                                    "recommended_fix_summary": {"type": "string"}
                                }
                            }
                        }
                    },
                    "required": ["audit_id"]
                }
            }
        }


class GenerateAuditReportAsset(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        required = ["audit_id", "report_storage_ref", "file_size_bytes"]
        missing = [f for f in required if f not in kwargs or kwargs[f] is None]
        if missing:
            return json.dumps({"error": f"Missing required fields: {', '.join(missing)}"}, indent=2)

        assets: List[Dict[str, Any]] = data.get("assets", [])
        asset_id = get_next_asset_id(data)
        created_ts = get_now_timestamp()

        new_asset = {
            "asset_id": asset_id,
            "artifact_id_nullable": None,
            "export_profile": "PDF",
            "file_size_bytes": kwargs["file_size_bytes"],
            "storage_ref": kwargs["report_storage_ref"],
            "created_ts": created_ts,
            "dlp_scan_status": "CLEAN",
            "dlp_scan_details_nullable": None
        }

        assets.append(new_asset)
        data["assets"] = assets
        return json.dumps(new_asset, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generate_audit_report_asset",
                "description": "Create a PDF report asset for an audit.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string"},
                        "report_storage_ref": {"type": "string"},
                        "file_size_bytes": {"type": "integer", "minimum": 0}
                    },
                    "required": ["audit_id", "report_storage_ref", "file_size_bytes"]
                }
            }
        }


class CompleteAudit(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        required = ["audit_id", "report_asset_id"]
        missing = [f for f in required if f not in kwargs or kwargs[f] is None]
        if missing:
            return json.dumps({"error": f"Missing required fields: {', '.join(missing)}"}, indent=2)

        audit_id = kwargs.get("audit_id")
        report_asset_id = kwargs.get("report_asset_id")

        audits: List[Dict[str, Any]] = data.get("audits", [])
        for row in audits:
            if row.get("audit_id") == audit_id:
                row["status"] = "COMPLETED"
                row["report_asset_id_nullable"] = report_asset_id
                return json.dumps(row, indent=2)

        return json.dumps({"error": f"No audit with id '{audit_id}'"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "complete_audit",
                "description": "Mark an audit as COMPLETED and link the generated report asset.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string"},
                        "report_asset_id": {"type": "string"}
                    },
                    "required": ["audit_id", "report_asset_id"]
                }
            }
        }














TOOLS = [
    GetArtifactWithId(),
    GetAllArtifactsOfTypeWithTagsAndEmail(),
    CreateNewArtifact(),
    GetArtifactsWithFileId(),

    GetAssetById(),
    GetAssetsByArtifactId(),
    CreateNewAsset(),

    CreateNewCycle(),
    UpdateCycleStatus(),
    GetCycleById(),
    GetCycleByArtifactAndThread(),

    StartEmailThread(),
    SendEmailInThread(),
    GetCompleteEmailThread(),
    GetThreadBySubject(),
    

    AddComment(),

    ApproveReview(),

    GetReleaseDetailsByName(),
    CreateNewRelease(),
    GetReleaseById(),

    CreateReleaseDiff(),
    GetReleaseDiffByReleaseId(),
    CompareBeforeAfterVisuals(),

    NotifyStakeholders(),

    CompleteAudit(),
    GenerateAuditReportAsset(),
    RecordAuditFindings(),
    CreateNewAudit(),


]