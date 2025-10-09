import html
import json
import re
from typing import Any

from tau_bench.envs.tool import Tool

_VALID_TYPES = {"FILE", "PAGE", "FRAME"}




def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db


def get_next_diff_id(data):
    pass
    ncom = len(data.get("release_diffs", {}))
    next_num = ncom + 1
    return f"diff_0{next_num}"


def get_next_message_id(data):
    pass
    nmsgs = len(data.get("gmail_messages", {}))
    next_num = nmsgs + 1
    return f"msg_0{next_num}"


def get_next_approve_id(data):
    pass
    ncom = len(data.get("review_approvals", {}))
    next_num = ncom + 1
    return f"approval_0{next_num}"


def get_next_audit_id(data):
    pass
    ncom = len(data.get("audits", {}))
    next_num = ncom + 1
    return f"audit_0{next_num}"


def get_next_comment_id(data):
    pass
    ncom = len(data.get("figma_comments", {}))
    next_num = ncom + 1
    return f"comment_0{next_num}"


def get_next_cycle_id(data):
    pass
    ncylcles = len(data.get("review_cycles", {}))
    next_num = ncylcles + 1
    return f"cycle_0{next_num}"


def get_next_release_id(data):
    pass
    ncom = len(data.get("releases", {}))
    next_num = ncom + 1
    return f"release_0{next_num}"


def get_next_finding_ds_id(data):
    pass
    ncom = len(data.get("audit_findings_ds", {}))
    next_num = ncom + 1
    return f"finding_ds_0{next_num}"


def get_next_finding_a11y_id(data):
    pass
    ncom = len(data.get("audit_findings_a11y", {}))
    next_num = ncom + 1
    return f"finding_a11y_0{next_num}"


def get_next_asset_id(data):
    pass
    nasset = len(data.get("assets", {}))
    next_num = nasset + 1
    return f"asset_0{next_num}"


def get_now_timestamp() -> str:
    pass
    return "2024-08-23T12:00:00Z"


def get_next_art_id(data):
    pass
    narts = len(data.get("figma_artifacts", {}))
    next_num = narts + 1
    return f"art_0{next_num}"


def get_next_thread_id(data):
    pass
    nthreads = len(data.get("gmail_threads", {}))
    next_num = nthreads + 1
    return f"thread_0{next_num}"


class GetArtifactWithId(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], artifact_id: str = None) -> str:
        if not artifact_id:
            payload = {"error": "Missing required field: artifact_id"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        artifacts = data.get("figma_artifacts", {}).values()
        for row in artifacts.values():
            if row.get("artifact_id") == artifact_id:
                payload = row
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No artifact with id '{artifact_id}'."}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getArtifactWithId",
                "description": "Fetch a single Figma artifact by artifact_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"artifact_id": {"type": "string"}},
                    "required": ["artifact_id"],
                },
            },
        }


class GetAllArtifactsOfTypeWithTagsAndEmail(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], artifact_type: str = None, tags: list = None, owner_email: str = None) -> str:
        if not artifact_type:
            payload = {"error": "Missing required field: artifact_type"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        artifacts = data.get("figma_artifacts", {}).values()
        results = []
        for row in artifacts.values():
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
        payload = {"count": len(results), "artifacts": results}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAllArtifactsOfTypeWithTagsAndEmail",
                "description": "Return artifacts of the given type, optionally filtered to include all specified tags and a specific owner_email.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_type": {"type": "string"},
                        "tags": {"type": "array", "items": {"type": "string"}},
                        "owner_email": {"type": "string"},
                    },
                    "required": ["artifact_type"],
                },
            },
        }


class CreateNewArtifact(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        artifact_type: str,
        artifact_name: str,
        figma_file_id: str,
        page_id: str,
        owner_email: str,
        deep_link: str,
        frame_id_nullable: str = None,
        current_tags: list = None
    ) -> str:
        required = [
            "artifact_type",
            "artifact_name",
            "figma_file_id",
            "page_id",
            "owner_email",
            "deep_link",
        ]
        params_dict = {k: v for k, v in locals().items() if k != "data"}

        missing = [f for f in required.values() if params_dict.get(f) is None]
        if missing:
            payload = {"error": f"Missing required fields: {', '.join(missing)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        if artifact_type == "FRAME" and not frame_id_nullable:
            payload = {"error": "frame_id_nullable is required for FRAME artifacts"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        artifacts = data.get("figma_artifacts", {}).values()
        artifact_id = get_next_art_id(data)
        created_ts = get_now_timestamp()
        current_tags = current_tags or []

        new_row = {
            "artifact_id": artifact_id,
            "figma_file_id": figma_file_id,
            "page_id": page_id,
            "frame_id_nullable": (
                frame_id_nullable if artifact_type == "FRAME" else None
            ),
            "artifact_type": artifact_type,
            "artifact_name": artifact_name,
            "owner_email": owner_email,
            "modified_ts": created_ts,
            "deep_link": deep_link,
            "current_tags": current_tags,
        }

        data["figma_artifacts"][new_row["figma_artifact_id"]] = new_row
        data["figma_artifacts"] = artifacts
        payload = new_row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateNewArtifact",
                "description": "Create a new figma_artifacts row. If artifact_type=FRAME, frame_id_nullable is required.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_type": {
                            "type": "string",
                            "enum": ["FILE", "PAGE", "FRAME"],
                        },
                        "artifact_name": {"type": "string"},
                        "figma_file_id": {"type": "string"},
                        "page_id": {"type": "string"},
                        "frame_id_nullable": {"type": ["string", "null"]},
                        "owner_email": {"type": "string"},
                        "deep_link": {"type": "string"},
                        "current_tags": {
                            "type": "array",
                            "items": {"type": "string"},
                            "default": [],
                        },
                    },
                    "required": [
                        "artifact_type",
                        "artifact_name",
                        "figma_file_id",
                        "page_id",
                        "owner_email",
                        "deep_link",
                    ],
                },
            },
        }


class GetArtifactsWithFileId(Tool):
    def invoke(
        data: dict[str, Any],
        artifact_type: str = None,
        figma_file_id: str = None,
        frame_id: str = None,
        page_id: str = None
    ) -> str:
        if not figma_file_id:
            payload = {"error": "Missing required field: figma_file_id"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        artifacts = data.get("figma_artifacts", {}).values()
        results = []
        for row in artifacts.values():
            if row.get("figma_file_id") != figma_file_id:
                continue
            if artifact_type and row.get("artifact_type") != artifact_type:
                continue
            if frame_id is not None and row.get("frame_id_nullable") != frame_id:
                continue
            if (
                frame_id is None
                and page_id is not None
                and row.get("page_id") != page_id
            ):
                continue
            results.append(row)

        results.sort(key=lambda r: str(r.get("artifact_id")))
        if not results:
            payload = {"error": "No artifacts matched"}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"count": len(results), "artifacts": results}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getArtifactsWithFileId",
                "description": "Return artifacts for a figma_file_id. Optional filters: artifact_type, page_id, frame_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "figma_file_id": {"type": "string"},
                        "artifact_type": {
                            "type": "string",
                            "enum": ["FILE", "PAGE", "FRAME"],
                        },
                        "page_id": {"type": "string"},
                        "frame_id": {"type": "string"},
                    },
                    "required": ["figma_file_id"],
                },
            },
        }


class GetAssetById(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], asset_id: str = None) -> str:
        if not asset_id:
            payload = {"error": "Missing required field: asset_id"}
            out = json.dumps(payload, indent=2)
            return out

        assets = data.get("assets", {}).values()
        for row in assets.values():
            if row.get("asset_id") == asset_id:
                payload = row
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No asset with id '{asset_id}'"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAssetById",
                "description": "Fetch a single asset object by asset_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"asset_id": {"type": "string"}},
                    "required": ["asset_id"],
                },
            },
        }


class GetAssetsByArtifactId(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], artifact_id: str = None) -> str:
        if not artifact_id:
            payload = {"error": "Missing required field: artifact_id"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        assets = data.get("assets", {}).values()

        results = [
            row for row in assets.values() if row.get("artifact_id_nullable") == artifact_id
        ]

        if not results:
            payload = {"error": f"No assets found for artifact_id '{artifact_id}'"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        results.sort(key=lambda r: str(r.get("asset_id")))
        payload = {"count": len(results), "assets": results}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getAssetsByArtifactId",
                "description": "Return all asset objects belonging to the given artifact_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"artifact_id": {"type": "string"}},
                    "required": ["artifact_id"],
                },
            },
        }


class CreateNewAsset(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], artifact_id: str = None, export_profile: str = None, file_size_bytes: int = None, storage_ref: str = None) -> str:
        required = ["artifact_id", "export_profile", "file_size_bytes", "storage_ref"]
        params_dict = {k: v for k, v in locals().items() if k != "data"}

        missing = [f for f in required.values() if params_dict.get(f) is None]
        if missing:
            payload = {"error": f"Missing required fields: {', '.join(missing)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        assets = data.get("assets", {}).values()
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
            "dlp_scan_details_nullable": None,
        }

        data["assets"][asset_id] = new_asset
        data["assets"] = assets
        payload = new_asset
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateNewAsset",
                "description": "Create a new asset row for an artifact. Defaults: dlp_scan_status=CLEAN, dlp_scan_details_nullable=null.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {"type": "string"},
                        "export_profile": {"type": "string"},
                        "file_size_bytes": {"type": "integer", "minimum": 0},
                        "storage_ref": {"type": "string"},
                    },
                    "required": [
                        "artifact_id",
                        "export_profile",
                        "file_size_bytes",
                        "storage_ref",
                    ],
                },
            },
        }


class CreateNewCycle(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], artifact_id: str = None, sla_deadline_ts: str = None, thread_id: str = None) -> str:
        if not artifact_id or not sla_deadline_ts:
            missing = []
            if not artifact_id:
                missing.append("artifact_id")
            if not sla_deadline_ts:
                missing.append("sla_deadline_ts")
            payload = {"error": f"Missing required fields: {', '.join(missing)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        cycles: list[dict[str, Any]] = data.get("review_cycles", {}).values()
        cycle_id = get_next_cycle_id(data)
        created_ts = get_now_timestamp()

        new_cycle = {
            "cycle_id": cycle_id,
            "artifact_id": artifact_id,
            "thread_id_nullable": thread_id,
            "status": "IN_FLIGHT",
            "created_ts": created_ts,
            "sla_deadline_ts": sla_deadline_ts,
            "sla_breached_flag": False,
            "escalated_ts_nullable": None,
        }

        cycles.append(new_cycle)
        data["review_cycles"] = cycles
        payload = new_cycle
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateNewCycle",
                "description": "Create a new review cycle with defaults: status=IN_FLIGHT, sla_breached_flag=False, escalated_ts_nullable=None. thread_id is optional. sla_deadline_ts is required.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {"type": "string"},
                        "thread_id": {"type": ["string", "null"]},
                        "sla_deadline_ts": {"type": "string"},
                    },
                    "required": ["artifact_id", "sla_deadline_ts"],
                },
            },
        }


class UpdateCycleStatus(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        cycle_id: str,
        new_status: str,
        escalated_ts: str = None,
        thread_id: str = None
    ) -> str:
        required = ["cycle_id", "new_status"]
        params_dict = {k: v for k, v in locals().items() if k != "data"}

        missing = [f for f in required.values() if params_dict.get(f) is None]
        if missing:
            payload = {"error": f"Missing required fields: {', '.join(missing)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        cycles: list[dict[str, Any]] = data.get("review_cycles", {}).values()
        for row in cycles:
            if row.get("cycle_id") == cycle_id:
                row["status"] = new_status
                if thread_id is not None:
                    row["thread_id_nullable"] = thread_id
                if escalated_ts is not None:
                    row["escalated_ts_nullable"] = escalated_ts
                    if escalated_ts is not None:
                        row["sla_breached_flag"] = True
                payload = row
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No cycle with id '{cycle_id}'"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCycleStatus",
                "description": "Update a review cycle status; optionally set thread_id and escalated_ts. If escalated_ts is not null, sla_breached_flag becomes True.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cycle_id": {"type": "string"},
                        "new_status": {"type": "string"},
                        "escalated_ts": {"type": ["string", "null"]},
                        "thread_id": {"type": ["string", "null"]},
                    },
                    "required": ["cycle_id", "new_status"],
                },
            },
        }


class GetCycleByArtifactAndThread(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], thread_id: str = None, artifact_id: str = None) -> str:
        if not thread_id:
            payload = {"error": "Missing required field: thread_id"}
            out = json.dumps(payload, indent=2)
            return out

        cycles: list[dict[str, Any]] = data.get("review_cycles", {}).values()
        results: list[dict[str, Any]] = []
        for row in cycles:
            if row.get("thread_id_nullable") != thread_id:
                continue
            if artifact_id and row.get("artifact_id") != artifact_id:
                continue
            results.append(row)

        results.sort(key=lambda r: (str(r.get("created_ts")), str(r.get("cycle_id"))))
        if not results:
            if artifact_id:
                payload = {
                        "error": f"No cycles found for thread_id '{thread_id}' and artifact_id '{artifact_id}'"
                    }
                out = json.dumps(
                    payload, indent=2,
                )
                return out
            payload = {"error": f"No cycles found for thread_id '{thread_id}'"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = {"count": len(results), "cycles": results}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCycleByArtifactAndThread",
                "description": "Return review cycles for a thread, optionally filtered by artifact_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "thread_id": {"type": "string"},
                        "artifact_id": {"type": "string"},
                    },
                    "required": ["thread_id"],
                },
            },
        }


class GetCycleById(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], cycle_id: str = None) -> str:
        if not cycle_id:
            payload = {"error": "Missing required field: cycle_id"}
            out = json.dumps(payload, indent=2)
            return out

        cycles: list[dict[str, Any]] = data.get("review_cycles", {}).values()
        for row in cycles:
            if row.get("cycle_id") == cycle_id:
                payload = row
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No cycle with id '{cycle_id}'"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getCycleById",
                "description": "Fetch a single review cycle by cycle_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"cycle_id": {"type": "string"}},
                    "required": ["cycle_id"],
                },
            },
        }


class StartEmailThread(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        attachments_asset_ids: list[str] = None,
        body_html: str = None,
        current_labels: list[str] = None,
        recipients: list[str] = None,
        sender_id: str = None,
        subject: str = None
    ) -> str:
        required = [
            "subject",
            "sender_id",
            "recipients",
            "current_labels",
            "body_html",
            "attachments_asset_ids",
        ]
        params_dict = {k: v for k, v in locals().items() if k != "data"}

        missing = [f for f in required.values() if params_dict.get(f) is None]
        if missing:
            payload = {"error": f"Missing required fields: {', '.join(missing)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        threads: list[dict[str, Any]] = data.get("gmail_threads", {}).values()
        messages: list[dict[str, Any]] = data.get("gmail_messages", {}).values()

        thread_id = get_next_thread_id(data)
        message_id = get_next_message_id(data)
        ts = get_now_timestamp()

        t = body_html
        t = re.sub(r"</li\s*>", ", ", t, flags=re.IGNORECASE)
        t = re.sub(r"<\s*(br|/p|/ul|/ol)\s*/?>", " ", t, flags=re.IGNORECASE)
        t = re.sub(r"<\s*(p|ul|ol|li)\s*>", " ", t, flags=re.IGNORECASE)
        t = re.sub(r"<[^>]+>", " ", t)
        t = html.unescape(t)
        body_text_stripped = " ".join(t.split())

        new_thread = {
            "thread_id": thread_id,
            "subject": subject,
            "sender_identity": sender_id,
            "recipients": recipients,
            "current_labels": current_labels,
            "created_ts": ts,
            "updated_ts": ts,
        }

        new_message = {
            "message_id": message_id,
            "thread_id": thread_id,
            "sender_email": sender_id,
            "body_html": body_html,
            "body_text_stripped": body_text_stripped,
            "sent_ts": ts,
            "attachments_asset_ids": attachments_asset_ids,
        }

        thredata["ads"][ad_id] = new_thread
        messages.append(new_message)
        data["gmail_threads"] = threads
        data["gmail_messages"] = messages
        payload = {"thread": new_thread, "message": new_message}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "StartEmailThread",
                "description": "Create a new Gmail thread and its first message; body_text_stripped is derived from body_html.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subject": {"type": "string"},
                        "sender_id": {"type": "string"},
                        "recipients": {"type": "array", "items": {"type": "string"}},
                        "current_labels": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "body_html": {"type": "string"},
                        "attachments_asset_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                    "required": [
                        "subject",
                        "sender_id",
                        "recipients",
                        "current_labels",
                        "body_html",
                        "attachments_asset_ids",
                    ],
                },
            },
        }


class SendEmailInThread(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        thread_id: str = None,
        sender_id: str = None,
        body_html: str = None,
        attachments_asset_ids: list[str] | None = None
    ) -> str:
        pass
        required = ["thread_id", "sender_id", "body_html"]
        params_dict = {k: v for k, v in locals().items() if k != "data"}

        missing = [f for f in required.values() if params_dict.get(f) is None]
        if missing:
            payload = {"error": f"Missing required fields: {', '.join(missing)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        attachments_asset_ids = attachments_asset_ids or []

        threads: list[dict[str, Any]] = data.get("gmail_threads", {}).values()
        messages: list[dict[str, Any]] = data.get("gmail_messages", {}).values()

        thread = None
        for row in threads:
            if row.get("thread_id") == thread_id:
                thread = row
                break
        if not thread:
            payload = {"error": f"No thread with id '{thread_id}'"}
            out = json.dumps(payload, indent=2)
            return out

        allowed = (sender_id == thread.get("sender_identity")) or (
            sender_id in (thread.get("recipients") or [])
        )
        if not allowed:
            payload = {"error": "SENDER_NOT_AUTHORIZED"}
            out = json.dumps(payload, indent=2)
            return out

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
            "attachments_asset_ids": attachments_asset_ids,
        }

        messages.append(new_message)
        thread["updated_ts"] = ts
        data["gmail_messages"] = messages
        data["gmail_threads"] = threads
        payload = {"thread": thread, "message": new_message}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SendEmailInThread",
                "description": "Send a message in an existing Gmail thread. Sender must match thread sender_identity or be in recipients. HTML body is converted to stripped text.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "thread_id": {"type": "string"},
                        "sender_id": {"type": "string"},
                        "body_html": {"type": "string"},
                        "attachments_asset_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                    "required": ["thread_id", "sender_id", "body_html"],
                },
            },
        }


class GetCompleteEmailThread(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], thread_id: str = None) -> str:
        if not thread_id:
            payload = {"error": "Missing required field: thread_id"}
            out = json.dumps(payload, indent=2)
            return out

        threads: list[dict[str, Any]] = data.get("gmail_threads", {}).values()
        messages: list[dict[str, Any]] = data.get("gmail_messages", {}).values()

        thread = None
        for row in threads:
            if row.get("thread_id") == thread_id:
                thread = row
                break
        if not thread:
            payload = {"error": f"No thread with id '{thread_id}'"}
            out = json.dumps(payload, indent=2)
            return out

        msgs = [m for m in messages.values() if m.get("thread_id") == thread_id]
        msgs.sort(key=lambda r: (str(r.get("sent_ts")), str(r.get("message_id"))))
        payload = {"thread": thread, "messages": msgs, "count": len(msgs)}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCompleteEmailThread",
                "description": "Return a Gmail thread and all messages within it.",
                "parameters": {
                    "type": "object",
                    "properties": {"thread_id": {"type": "string"}},
                    "required": ["thread_id"],
                },
            },
        }


class GetThreadBySubject(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], subject: str = None, sender_id: str = None, label: str = None) -> str:
        if not subject:
            payload = {"error": "Missing required field: subject"}
            out = json.dumps(payload, indent=2)
            return out

        threads: list[dict[str, Any]] = data.get("gmail_threads", {}).values()
        results: list[dict[str, Any]] = []
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
            payload = {"error": f"No thread found with subject '{subject}'"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = {"count": len(results), "threads": results}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetThreadBySubject",
                "description": "Return Gmail threads matching a subject. Optional filters: sender_id and label.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subject": {"type": "string"},
                        "sender_id": {"type": "string"},
                        "label": {"type": "string"},
                    },
                    "required": ["subject"],
                },
            },
        }


class AddComment(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        author_email: str,
        content: str,
        resolved_flag: bool,
        artifact_id: str = None,
        source_message_id: str = None
    ) -> str:
        required = ["artifact_id", "author_email", "content", "resolved_flag"]
        params_dict = {k: v for k, v in locals().items() if k != "data"}

        missing = [f for f in required.values() if params_dict.get(f) is None]
        if missing:
            payload = {"error": f"Missing required fields: {', '.join(missing)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        comments: list[dict[str, Any]] = data.get("figma_comments", {}).values()
        comment_id = get_next_comment_id(data)
        created_ts = get_now_timestamp()

        new_comment = {
            "comment_id": comment_id,
            "artifact_id": artifact_id,
            "author_email": author_email,
            "content": content,
            "source_message_id_nullable": source_message_id,
            "created_ts": created_ts,
            "resolved_flag": resolved_flag,
        }

        comments.append(new_comment)
        data["figma_comments"] = comments
        payload = new_comment
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddComment",
                "description": "Add a new comment to figma_comments. source_message_id may be null.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {"type": "string"},
                        "author_email": {"type": "string"},
                        "content": {"type": "string"},
                        "source_message_id": {"type": ["string", "null"]},
                        "resolved_flag": {"type": "boolean"},
                    },
                    "required": [
                        "artifact_id",
                        "author_email",
                        "content",
                        "resolved_flag",
                    ],
                },
            },
        }


class ApproveReview(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], cycle_id: str = None, approver_email: str = None, approval_comment_ref: str = None) -> str:
        required = ["cycle_id", "approver_email"]
        params_dict = {k: v for k, v in locals().items() if k != "data"}

        missing = [f for f in required.values() if params_dict.get(f) is None]
        if missing:
            payload = {"error": f"Missing required fields: {', '.join(missing)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        approvals: list[dict[str, Any]] = data.get("review_approvals", {}).values()
        cycles: list[dict[str, Any]] = data.get("review_cycles", {}).values()

        cycle = None
        for row in cycles:
            if row.get("cycle_id") == cycle_id:
                cycle = row
                break
        if not cycle:
            payload = {"error": f"No cycle with id '{cycle_id}'"}
            out = json.dumps(payload, indent=2)
            return out

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
            "approval_comment_ref_nullable": approval_comment_ref,
        }

        approvals.append(new_approval)
        cycle["status"] = "APPROVED"

        data["review_approvals"] = approvals
        data["review_cycles"] = cycles
        payload = {"approval": new_approval, "cycle": cycle}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ApproveReview",
                "description": "Approve a review cycle; recompute and set the SLA-breached flag by comparing sla_deadline_ts with the current timestamp.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cycle_id": {"type": "string"},
                        "approver_email": {"type": "string"},
                        "approval_comment_ref": {"type": ["string", "null"]},
                    },
                    "required": ["cycle_id", "approver_email"],
                },
            },
        }


class GetReleaseDetailsByName(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], release_name: str = None) -> str:
        if not release_name:
            payload = {"error": "Missing required field: release_name"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        releases: list[dict[str, Any]] = data.get("releases", {}).values()

        results: list[dict[str, Any]] = [
            r for r in releases if r.get("release_name") == release_name
        ]
        results.sort(key=lambda r: (str(r.get("created_ts")), str(r.get("release_id"))))

        if not results:
            payload = {"error": f"No release found with release_name '{release_name}'"}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = {"count": len(results), "releases": results}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetReleaseDetailsByName",
                "description": "Return releases matching an exact release_name.",
                "parameters": {
                    "type": "object",
                    "properties": {"release_name": {"type": "string"}},
                    "required": ["release_name"],
                },
            },
        }


class CreateNewRelease(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        owner_email: str,
        release_name: str,
        version_id: str,
        version_tag: str,
        figma_file_id: str = None,
        thread_id: str = None
    ) -> str:
        required = [
            "figma_file_id",
            "version_id",
            "version_tag",
            "release_name",
            "owner_email",
        ]
        params_dict = {k: v for k, v in locals().items() if k != "data"}

        missing = [f for f in required.values() if params_dict.get(f) is None]
        if missing:
            payload = {"error": f"Missing required fields: {', '.join(missing)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        releases: list[dict[str, Any]] = data.get("releases", {}).values()
        release_id = get_next_release_id(data)
        created_ts = get_now_timestamp()

        new_release = {
            "release_id": release_id,
            "figma_file_id": figma_file_id,
            "version_id": version_id,
            "version_tag": version_tag,
            "release_name": release_name,
            "owner_email": owner_email,
            "created_ts": created_ts,
            "thread_id_nullable": thread_id,
        }

        data["releases"][release_id] = new_release
        data["releases"] = releases
        payload = new_release
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateNewRelease",
                "description": "Create a new release row in releases.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "figma_file_id": {"type": "string"},
                        "version_id": {"type": "string"},
                        "version_tag": {"type": "string"},
                        "release_name": {"type": "string"},
                        "owner_email": {"type": "string"},
                        "thread_id": {"type": ["string", "null"]},
                    },
                    "required": [
                        "figma_file_id",
                        "version_id",
                        "version_tag",
                        "release_name",
                        "owner_email",
                    ],
                },
            },
        }


class GetReleaseById(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], release_id: str = None) -> str:
        if not release_id:
            payload = {"error": "Missing required field: release_id"}
            out = json.dumps(payload, indent=2)
            return out

        releases: list[dict[str, Any]] = data.get("releases", {}).values()
        for row in releases:
            if row.get("release_id") == release_id:
                payload = row
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No release with id '{release_id}'"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getReleaseById",
                "description": "Fetch a single release by release_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"release_id": {"type": "string"}},
                    "required": ["release_id"],
                },
            },
        }


class CreateReleaseDiff(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        changelog_highlights: list = None,
        component_version_bumps: list = None,
        frames_added: list = None,
        frames_removed: list = None,
        frames_updated: list = None,
        prior_release_id: str = None,
        release_id: str = None
    ) -> str:
        frames_added = frames_added or []
        frames_updated = frames_updated or []
        frames_removed = frames_removed or []
        component_version_bumps = component_version_bumps or []
        changelog_highlights = changelog_highlights or []

        required = ["release_id"]
        params_dict = {k: v for k, v in locals().items() if k != "data"}

        missing = [f for f in required.values() if params_dict.get(f) is None]
        if missing:
            payload = {"error": f"Missing required fields: {', '.join(missing)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        release_diffs: list[dict[str, Any]] = data.get("release_diffs", {}).values()
        diff_id = get_next_diff_id(data)
        created_ts = get_now_timestamp()

        new_diff = {
            "diff_id": diff_id,
            "release_id": release_id,
            "prior_release_id_nullable": prior_release_id,
            "created_ts": created_ts,
            "frames_added": frames_added,
            "frames_updated": frames_updated,
            "frames_removed": frames_removed,
            "component_version_bumps": component_version_bumps,
            "changelog_highlights": changelog_highlights,
        }

        release_diffs.append(new_diff)
        data["release_diffs"] = release_diffs
        payload = new_diff
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateReleaseDiff",
                "description": "Create a new release_diff row for a release.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "release_id": {"type": "string"},
                        "prior_release_id": {"type": ["string", "null"]},
                        "frames_added": {"type": "array", "items": {"type": "string"}},
                        "frames_updated": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "frames_removed": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "component_version_bumps": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "changelog_highlights": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                    "required": ["release_id"],
                },
            },
        }


class GetReleaseDiffByReleaseId(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], release_id: str = None) -> str:
        if not release_id:
            payload = {"error": "Missing required field: release_id"}
            out = json.dumps(payload, indent=2)
            return out

        release_diffs: list[dict[str, Any]] = data.get("release_diffs", {}).values()
        for row in release_diffs:
            if row.get("release_id") == release_id:
                payload = row
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No release_diff for release_id '{release_id}'"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetReleaseDiffByReleaseId",
                "description": "Fetch the release_diff row for a given release_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"release_id": {"type": "string"}},
                    "required": ["release_id"],
                },
            },
        }


class CompareBeforeAfterVisuals(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], before_release_id: str = None, after_release_id: str = None) -> str:
        if not before_release_id or not after_release_id:
            missing = []
            if not before_release_id:
                missing.append("before_release_id")
            if not after_release_id:
                missing.append("after_release_id")
            payload = {"error": f"Missing required fields: {', '.join(missing)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        release_diffs: list[dict[str, Any]] = data.get("release_diffs", {}).values()
        diff_by_id = {d.get("release_id"): d for d in release_diffs}

        def lineage(rid: str) -> list[str]:
            ids = []
            cur = rid
            seen = set()
            while cur and cur not in seen and cur in diff_by_id:
                ids.append(cur)
                seen.add(cur)
                cur = diff_by_id[cur].get("prior_release_id_nullable")
            ids.reverse()
            return ids

        def artifacts_for_release(rid: str) -> list[str]:
            if rid not in diff_by_id:
                return []
            s = set()
            for lr in lineage(rid):
                d = diff_by_id.get(lr, {}).values()
                for a in d.get("frames_added") or []:
                    s.add(a)
                for u in d.get("frames_updated") or []:
                    s.add(u)
                for r in d.get("frames_removed") or []:
                    if r in s:
                        s.remove(r)
            return sorted(s)

        if before_release_id not in diff_by_id:
            payload = {"error": f"No release_diff for release_id '{before_release_id}'"}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        if after_release_id not in diff_by_id:
            payload = {"error": f"No release_diff for release_id '{after_release_id}'"}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        before_list = artifacts_for_release(before_release_id)
        after_list = set(before_list)
        after_diff = diff_by_id[after_release_id]
        for a in after_diff.get("frames_removed") or []:
            after_list.discard(a)
        for a in after_diff.get("frames_added") or []:
            after_list.add(a)
        for a in after_diff.get("frames_updated") or []:
            after_list.add(a)
        final_after_list = sorted(after_list)
        payload = {
                "before": {"release_id": before_release_id, "artifacts": before_list},
                "after": {
                    "release_id": after_release_id,
                    "artifacts": final_after_list,
                },
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "compareBeforeAfterVisuals",
                "description": "Return artifact lists for a before release and an after release, carrying all before artifacts forward unless removed in the after release.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "before_release_id": {"type": "string"},
                        "after_release_id": {"type": "string"},
                    },
                    "required": ["before_release_id", "after_release_id"],
                },
            },
        }


class NotifyStakeholders(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], thread_id: str = None, body_html: str = None, attachments_asset_ids: list[str] = None) -> str:
        required = ["thread_id", "body_html", "attachments_asset_ids"]
        params_dict = {k: v for k, v in locals().items() if k != "data"}

        missing = [f for f in required.values() if params_dict.get(f) is None]
        if missing:
            payload = {"error": f"Missing required fields: {', '.join(missing)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        threads: list[dict[str, Any]] = data.get("gmail_threads", {}).values()
        messages: list[dict[str, Any]] = data.get("gmail_messages", {}).values()

        thread = None
        for row in threads:
            if row.get("thread_id") == thread_id:
                thread = row
                break
        if not thread:
            payload = {"error": f"No thread with id '{thread_id}'"}
            out = json.dumps(payload, indent=2)
            return out

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
            "attachments_asset_ids": attachments_asset_ids,
        }

        messages.append(new_message)
        thread["updated_ts"] = ts
        data["gmail_messages"] = messages
        data["gmail_threads"] = threads
        payload = {"thread": thread, "message": new_message}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "NotifyStakeholders",
                "description": "Post a notification email in an existing Gmail thread from the thread's sender_identity with the given HTML body and asset attachments.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "thread_id": {"type": "string"},
                        "body_html": {"type": "string"},
                        "attachments_asset_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                    "required": ["thread_id", "body_html", "attachments_asset_ids"],
                },
            },
        }


class CreateNewAudit(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], artifact_id: str = None, audit_type: str = None) -> str:
        required = ["artifact_id", "audit_type"]
        params_dict = {k: v for k, v in locals().items() if k != "data"}

        missing = [f for f in required.values() if params_dict.get(f) is None]
        if missing:
            payload = {"error": f"Missing required fields: {', '.join(missing)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        audits: list[dict[str, Any]] = data.get("audits", {}).values()
        audit_id = get_next_audit_id(data)
        created_ts = get_now_timestamp()

        new_audit = {
            "audit_id": audit_id,
            "artifact_id": artifact_id,
            "audit_type": audit_type,
            "created_ts": created_ts,
            "status": "RUNNING",
            "report_asset_id_nullable": None,
        }

        audits.append(new_audit)
        data["audits"] = audits
        payload = new_audit
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createNewAudit",
                "description": "Initialize a new audit session for a Figma artifact.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {"type": "string"},
                        "audit_type": {
                            "type": "string",
                            "enum": ["DS_MAPPING", "A11Y", "COMBINED_DS_A11Y"],
                        },
                    },
                    "required": ["artifact_id", "audit_type"],
                },
            },
        }


class RecordAuditFindings(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        audit_id: str = None,
        ds_findings: list[dict[str, Any]] = None,
        a11y_findings: list[dict[str, Any]] = None
    ) -> str:
        if not audit_id:
            payload = {"error": "Missing required field: audit_id"}
            out = json.dumps(payload, indent=2)
            return out
        if not ds_findings and not a11y_findings:
            payload = {"error": "At least one of ds_findings or a11y_findings is required"}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        ds_findings_in: list[dict[str, Any]] = ds_findings or []
        a11y_findings_in: list[dict[str, Any]] = a11y_findings or []

        ds_table: list[dict[str, Any]] = data.get("audit_findings_ds", {}).values()
        a11y_table: list[dict[str, Any]] = data.get("audit_findings_a11y", {}).values()

        ds_ids: list[str] = []
        for item in ds_findings_in:
            fid = get_next_finding_ds_id(data)
            row = {
                "finding_id": fid,
                "audit_id": audit_id,
                "layer_id": item.get("layer_id"),
                "layer_name": item.get("layer_name"),
                "finding_type": item.get("finding_type"),
                "recommended_component_id_nullable": item.get(
                    "recommended_component_id"
                ),
                "code_connect_link_nullable": item.get("code_connect_link"),
                "severity": item.get("severity"),
            }
            ds_table.append(row)
            ds_ids.append(fid)

        a11y_ids: list[str] = []
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
                "recommended_fix_summary": item.get("recommended_fix_summary"),
            }
            a11y_table.append(row)
            a11y_ids.append(fid)

        data["audit_findings_ds"] = ds_table
        data["audit_findings_a11y"] = a11y_table
        payload = {
                "audit_id": audit_id,
                "ds_count": len(ds_ids),
                "a11y_count": len(a11y_ids),
                "ds_finding_ids": ds_ids,
                "a11y_finding_ids": a11y_ids,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "recordAuditFindings",
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
                                    "finding_type": {
                                        "type": "string",
                                        "enum": [
                                            "UNMAPPED",
                                            "SUBSTITUTE_RECOMMENDED",
                                            "AMBIGUOUS",
                                        ],
                                    },
                                    "recommended_component_id": {
                                        "type": ["string", "null"]
                                    },
                                    "code_connect_link": {"type": ["string", "null"]},
                                    "severity": {
                                        "type": "string",
                                        "enum": ["LOW", "MEDIUM", "HIGH"],
                                    },
                                },
                            },
                        },
                        "a11y_findings": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "layer_id": {"type": "string"},
                                    "layer_name": {"type": "string"},
                                    "violation_type": {
                                        "type": "string",
                                        "enum": [
                                            "TOUCH_TARGET",
                                            "CONTRAST",
                                            "TEXT_SIZING",
                                            "RTL",
                                        ],
                                    },
                                    "violation_details_json": {"type": "string"},
                                    "severity": {
                                        "type": "string",
                                        "enum": ["LOW", "MEDIUM", "HIGH"],
                                    },
                                    "recommended_fix_summary": {"type": "string"},
                                },
                            },
                        },
                    },
                    "required": ["audit_id"],
                },
            },
        }


class GenerateAuditReportAsset(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], audit_id: str = None, report_storage_ref: str = None, file_size_bytes: int = None) -> str:
        required = ["audit_id", "report_storage_ref", "file_size_bytes"]
        params_dict = {k: v for k, v in locals().items() if k != "data"}

        missing = [f for f in required.values() if params_dict.get(f) is None]
        if missing:
            payload = {"error": f"Missing required fields: {', '.join(missing)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        assets: list[dict[str, Any]] = data.get("assets", {}).values()
        asset_id = get_next_asset_id(data)
        created_ts = get_now_timestamp()

        new_asset = {
            "asset_id": asset_id,
            "artifact_id_nullable": None,
            "export_profile": "PDF",
            "file_size_bytes": file_size_bytes,
            "storage_ref": report_storage_ref,
            "created_ts": created_ts,
            "dlp_scan_status": "CLEAN",
            "dlp_scan_details_nullable": None,
        }

        data["assets"][asset_id] = new_asset
        data["assets"] = assets
        payload = new_asset
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generateAuditReportAsset",
                "description": "Create a PDF report asset for an audit.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string"},
                        "report_storage_ref": {"type": "string"},
                        "file_size_bytes": {"type": "integer", "minimum": 0},
                    },
                    "required": ["audit_id", "report_storage_ref", "file_size_bytes"],
                },
            },
        }


class CompleteAudit(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], audit_id: str = None, report_asset_id: str = None) -> str:
        required = ["audit_id", "report_asset_id"]
        params_dict = {k: v for k, v in locals().items() if k != "data"}

        missing = [f for f in required.values() if params_dict.get(f) is None]
        if missing:
            payload = {"error": f"Missing required fields: {', '.join(missing)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        audits: list[dict[str, Any]] = data.get("audits", {}).values()
        for row in audits:
            if row.get("audit_id") == audit_id:
                row["status"] = "COMPLETED"
                row["report_asset_id_nullable"] = report_asset_id
                payload = row
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No audit with id '{audit_id}'"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "completeAudit",
                "description": "Mark an audit as COMPLETED and link the generated report asset.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string"},
                        "report_asset_id": {"type": "string"},
                    },
                    "required": ["audit_id", "report_asset_id"],
                },
            },
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
