import json
from typing import Any

from domains.dto import Tool


def custom_hash(input_string):
    pass
    hash_value = 0
    modulo = 10**9 + 7
    for char in input_string:
        #Obtain the numeric representation of a character (e.g., ASCII)
        char_value = ord(char)
        hash_value = (hash_value * 31 + char_value) % modulo
    return hash_value


def get_config_options(data: dict[str, Any], key: str) -> list[str]:
    pass
    system_config = data.get("system_config", [])
    for item in system_config:
        if item.get("config_key") == key:
            try:
                value = json.loads(item.get("config_value_json", "{}"))
                if isinstance(value, dict):
                    return list(value.values())
                elif isinstance(value, list):
                    return value
            except Exception:
                return []
    return []


class CreateReviewCycle(Tool):  #WRITE
    @staticmethod
    def invoke(
        data: dict[str, Any],
        artifact_id: str,
        status: str,
        thread_id_nullable: str = None,
    ) -> str:
        pass
        #Check the input for validity
        if not isinstance(artifact_id, str) or not artifact_id:
            payload = {"error": "artifact_id must be a non-empty string"}
            out = json.dumps(payload)
            return out
        allowed_status = [
            "NEEDS_REVIEW",
            "APPROVED",
            "CHANGES_REQUESTED",
            "ESCALATED",
            "IN_FLIGHT",
        ]
        if status not in allowed_status:
            payload = {"error": f"Invalid status. Allowed: {allowed_status}"}
            out = json.dumps(payload)
            return out
        review_cycles = data.get("review_cycles", [])
        #Create a new cycle_id
        next_num = len(review_cycles) + 1
        cycle_id = f"cycle_{next_num:03d}"
        now = "2025-08-21T16:00:00Z"
        created_ts = now
        #Standard SLA: 3 days ahead
        sla_deadline_ts = "2025-08-24T16:00:00Z"
        new_cycle = {
            "cycle_id": cycle_id,
            "artifact_id": artifact_id,
            "thread_id_nullable": thread_id_nullable,
            "status": status,
            "created_ts": created_ts,
            "sla_deadline_ts": sla_deadline_ts,
            "sla_breached_flag": False,
            "escalated_ts_nullable": None,
        }
        review_cycles.append(new_cycle)
        payload = {"new_cycle": new_cycle}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateReviewCycle",
                "description": "Create a new review cycle for a Figma artifact.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {
                            "type": "string",
                            "description": "The artifact ID for the review cycle.",
                        },
                        "status": {
                            "type": "string",
                            "description": "Review cycle status (NEEDS_REVIEW, APPROVED, CHANGES_REQUESTED, ESCALATED, IN_FLIGHT).",
                        },
                        "thread_id_nullable": {
                            "type": "string",
                            "description": "Optional thread ID for the review cycle.",
                        },
                    },
                    "required": ["artifact_id", "status"],
                },
            },
        }


class ExportFigmaArtifactsToAssets(Tool):  #WRITE
    @staticmethod
    def invoke(
        data: dict[str, Any],
        artifact_ids: list[str],
        export_profile: dict[str, Any] = None,
    ) -> str:
        pass
        #Check the input for validity
        if not isinstance(artifact_ids, list) or not all(
            isinstance(aid, str) for aid in artifact_ids
        ):
            payload = {"error": "artifact_ids must be a list of strings"}
            out = json.dumps(payload)
            return out
        artifacts = data.get("figma_artifacts", [])
        assets = data.get("assets", [])
        #Standard export profile
        default_profile = {"format": "PNG", "scale": "2x"}
        profile = export_profile if export_profile else default_profile
        #Check the profile for validity
        allowed_formats = ["PNG", "JPG", "SVG", "PDF"]
        allowed_scales = ["1x", "2x", "4x"]
        if export_profile is not None and (
            "format" not in export_profile.keys()
            or "scale" not in export_profile.keys()
        ):
            payload = {"error": "Invalid export profile. Must include 'format' and 'scale'."}
            out = json.dumps(
                payload)
            return out
        fmt = profile.get("format", "PNG")
        scale = profile.get("scale", "2x")
        if fmt not in allowed_formats or scale not in allowed_scales:
            payload = {
                    "error": f"Invalid export profile. Allowed formats: {allowed_formats}, scales: {allowed_scales}"
                }
            out = json.dumps(
                payload)
            return out
        exported = []
        for aid in artifact_ids:
            artifact = next((a for a in artifacts if a.get("artifact_id") == aid), None)
            if not artifact:
                continue
            #Construct the export_profile string similar to assets.json
            if fmt == "SVG" or fmt == "PDF":
                export_profile_str = fmt
            else:
                export_profile_str = f"{fmt} {scale}"
            asset = {
                "asset_id": f"asset_{aid}_{fmt.lower()}_{scale}",
                "artifact_id_nullable": aid,
                "export_profile": export_profile_str,
                #Default values for additional fields
                "file_size_bytes": 205500,
                "storage_ref": f"gs://company-assets/figma-exports/{artifact.get('artifact_name').replace(' ', '-').lower()}-{scale}.{fmt.lower()}",
                "created_ts": "2025-08-26T00:00:00Z",
                "dlp_scan_status": "CLEAN",
                "dlp_scan_details_nullable": None,
            }
            assets.append(asset)
            exported.append(asset["asset_id"])
        payload = {"exported_asset_ids": exported, "profile": profile}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ExportFigmaArtifactsToAssets",
                "description": "Export Figma artifacts to assets with a customizable profile (default PNG 2x).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of Figma artifact IDs to export.",
                        },
                        "export_profile": {
                            "type": "object",
                            "properties": {
                                "format": {
                                    "type": "string",
                                    "description": "Export format (PNG, JPG, SVG, PDF).",
                                },
                                "scale": {
                                    "type": "string",
                                    "description": "Export scale (1x, 2x, 4x).",
                                },
                            },
                            "description": "Custom export profile. Defaults to PNG 2x.",
                            "default": {"format": "PNG", "scale": "2x"},
                        },
                    },
                    "required": ["artifact_ids"],
                },
            },
        }


class FilterFigmaArtifactsByTags(Tool):  #READ
    @staticmethod
    def invoke(data: dict[str, Any], tags: list[str]) -> str:
        pass
        #Check the input for validity
        if not isinstance(tags, list) or not all(isinstance(tag, str) for tag in tags):
            payload = {"error": "tags must be a list of strings"}
            out = json.dumps(payload)
            return out
        artifacts = data.get("figma_artifacts", [])
        #Gather all distinct tags from artifacts
        all_tags = set()
        for artifact in artifacts:
            all_tags.update(artifact.get("current_tags", []))
        #Verify that all provided tags are plausible
        unrealistic = [tag for tag in tags if tag not in all_tags]
        if unrealistic:
            payload = {
                    "error": f"Unrealistic tags: {unrealistic}. These tags do not appear in any artifact."
                }
            out = json.dumps(
                payload)
            return out
        matching_ids = []
        for artifact in artifacts:
            artifact_tags = artifact.get("current_tags", [])
            if all(tag in artifact_tags for tag in tags):
                matching_ids.append(artifact.get("artifact_id"))
        if not matching_ids:
            payload = {"artifact_ids": "No matching artifacts found."}
            out = json.dumps(payload)
            return out
        payload = {"artifact_ids": matching_ids}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FilterFigmaArtifactsByTags",
                "description": "Filter Figma artifacts by tags and return matching artifact IDs.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "tags": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of tags to filter artifacts by. All tags must be present in the artifact.",
                        }
                    },
                    "required": ["tags"],
                },
            },
        }


class GetArtifactIdFromName(Tool):  #READ
    @staticmethod
    def invoke(data: dict[str, Any], artifact_name: str) -> str:
        _artifact_nameL = artifact_name or ''.lower()
        pass
        #Check the input for validity
        if not isinstance(artifact_name, str) or not artifact_name:
            payload = {"error": "artifact_name must be a non-empty string"}
            out = json.dumps(payload)
            return out

        artifacts = data.get("figma_artifacts", [])

        #Look for an exact match initially
        exact_match = None
        for artifact in artifacts:
            if artifact.get("artifact_name") == artifact_name:
                exact_match = artifact
                break

        if exact_match:
            payload = {
                    "artifact_id": exact_match.get("artifact_id"),
                    "artifact_name": exact_match.get("artifact_name"),
                    "artifact_type": exact_match.get("artifact_type"),
                    "owner_email": exact_match.get("owner_email"),
                }
            out = json.dumps(
                payload)
            return out

        #If an exact match is not found, search for partial matches (case-insensitive)
        partial_matches = []
        artifact_name_lower = artifact_name.lower()
        for artifact in artifacts:
            artifact_artifact_name = artifact.get("artifact_name", "").lower()
            if (
                artifact_name_lower in artifact_artifact_name
                or artifact_artifact_name in artifact_name_lower
            ):
                partial_matches.append(
                    {
                        "artifact_id": artifact.get("artifact_id"),
                        "artifact_name": artifact.get("artifact_name"),
                        "artifact_type": artifact.get("artifact_type"),
                        "owner_email": artifact.get("owner_email"),
                    }
                )

        if partial_matches:
            payload = {
                    "exact_match": False,
                    "partial_matches": partial_matches,
                    "message": f"No exact match found for '{artifact_name}'. Found {len(partial_matches)} partial matches.",
                }
            out = json.dumps(
                payload)
            return out
        payload = {"error": f"No artifact found with name '{artifact_name}'"}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetArtifactIdFromName",
                "description": "Get artifact ID and details by searching for artifact name. Returns exact match if found, otherwise returns partial matches.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_name": {
                            "type": "string",
                            "description": "The name of the artifact to search for.",
                        }
                    },
                    "required": ["artifact_name"],
                },
            },
        }


class CreateGmailMessage(Tool):  #WRITE
    @staticmethod
    def invoke(
        data: dict[str, Any],
        sender_email: str,
        workflow_type: str,
        thread_id: str = None,
        attachments_asset_ids: list[str] = None,
    ) -> str:
        pass
        #Check the input for validity
        if not isinstance(sender_email, str) or not sender_email:
            payload = {"error": "sender_email must be a non-empty string"}
            out = json.dumps(payload)
            return out
        if (
            not isinstance(workflow_type, str)
            or not workflow_type
            or workflow_type not in ["review", "release"]
        ):
            payload = {"error": "workflow_type must be a non-empty string"}
            out = json.dumps(payload)
            return out
        gmail_messages = data.get("gmail_messages", [])
        next_num = len(gmail_messages) + 1
        message_id = f"msg_{next_num:03d}"
        sent_ts = "2025-08-26T12:00:00Z"  #Utilize the current date/time in production
        if workflow_type == "review":
            body_text_stripped = "Hi, please review the attached design."
        elif workflow_type == "release":
            body_text_stripped = "Hi, please find the designs for release attached."
        new_message = {
            "message_id": message_id,
            "thread_id": thread_id,
            "sender_email": sender_email,
            "body_html": f"<p>{body_text_stripped.replace(',', ',</p><p>', 1)}</p>",
            "body_text_stripped": body_text_stripped,
            "sent_ts": sent_ts,
            "attachments_asset_ids": (
                attachments_asset_ids if attachments_asset_ids else []
            ),
        }
        gmail_messages.append(new_message)
        payload = {"new_message": new_message}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateGmailMessage",
                "description": "Create a new Gmail message.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sender_email": {
                            "type": "string",
                            "description": "Sender's email address.",
                        },
                        "body_text_stripped": {
                            "type": "string",
                            "description": "Plain text body of the message.",
                        },
                        "thread_id": {
                            "type": "string",
                            "description": "Optional thread ID for the message.",
                        },
                        "attachments_asset_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Optional list of asset IDs for attachments.",
                        },
                    },
                    "required": ["sender_email", "body_text_stripped"],
                },
            },
        }


class CreateGmailThread(Tool):  #WRITE
    @staticmethod
    def invoke(
        data: dict[str, Any],
        sender_email: str,
        recipients_emails: list[str],
        workflow_type: str,
        current_labels: list[str],
    ) -> str:
        pass
        #Check the input for validity
        if not isinstance(sender_email, str) or not sender_email:
            payload = {"error": "sender_email must be a non-empty string"}
            out = json.dumps(payload)
            return out
        if not isinstance(recipients_emails, list) or not all(
            isinstance(e, str) for e in recipients_emails
        ):
            payload = {"error": "recipients_emails must be a list of strings"}
            out = json.dumps(payload)
            return out
        if (
            not isinstance(workflow_type, str)
            or not workflow_type
            or workflow_type not in ["review", "release"]
        ):
            payload = {"error": "workflow_type must be a non-empty string"}
            out = json.dumps(payload)
            return out
        if not isinstance(current_labels, list) or not all(
            isinstance(l, str) for l in current_labels
        ):
            payload = {"error": "current_labels must be a list of strings"}
            out = json.dumps(payload)
            return out
        gmail_labels = get_config_options(data, "gmail_labels")
        invalid_labels = [l for l in current_labels if l not in gmail_labels]
        if invalid_labels:
            payload = {"error": f"Invalid labels: {invalid_labels}. Allowed: {gmail_labels}"}
            out = json.dumps(
                payload)
            return out
        gmail_threads = data.get("gmail_threads", [])
        next_num = len(gmail_threads) + 1
        thread_id = f"thread_{next_num:03d}"
        created_ts = "2025-08-26T12:00:00Z"  #Utilize the current date/time in production
        if workflow_type == "review":
            subject = f"Review designs for {sender_email}"
        elif workflow_type == "release":
            subject = f"Release designs for {sender_email}"
        new_thread = {
            "thread_id": thread_id,
            "sender_email": sender_email,
            "recipients_emails": recipients_emails,
            "subject": subject,
            "current_labels": current_labels,
            "created_ts": created_ts,
        }
        gmail_threads.append(new_thread)
        payload = {"new_thread": new_thread}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateGmailThread",
                "description": "Create a new Gmail thread.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sender_email": {
                            "type": "string",
                            "description": "Sender's email address.",
                        },
                        "recipients_emails": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of recipient email addresses.",
                        },
                        "subject": {
                            "type": "string",
                            "description": "Subject of the thread.",
                        },
                        "current_labels": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Current labels for the thread.",
                        },
                    },
                    "required": [
                        "sender_email",
                        "recipients_emails",
                        "subject",
                        "current_labels",
                    ],
                },
            },
        }


class CreateFigmaCommentFromGmailMessage(Tool):  #WRITE
    @staticmethod
    def invoke(
        data: dict[str, Any],
        artifact_id: str,
        gmail_message_id: str,
    ) -> str:
        pass
        #Check the input for validity
        if not isinstance(artifact_id, str) or not artifact_id:
            payload = {"error": "artifact_id must be a non-empty string"}
            out = json.dumps(payload)
            return out
        if not isinstance(gmail_message_id, str) or not gmail_message_id:
            payload = {"error": "gmail_message_id must be a non-empty string"}
            out = json.dumps(payload)
            return out
        gmail_messages = data.get("gmail_messages", [])
        figma_comments = data.get("figma_comments", [])
        #Locate the Gmail message
        gmail_msg = next(
            (m for m in gmail_messages if m.get("message_id") == gmail_message_id), None
        )
        if not gmail_msg:
            payload = {"error": "gmail_message_id not found in gmail_messages"}
            out = json.dumps(payload)
            return out
        commenter_email = gmail_msg.get("sender_email")
        comment_text = gmail_msg.get("body_text_stripped")
        next_num = len(figma_comments) + 1
        comment_id = f"comment_{next_num:03d}"
        created_ts = "2025-08-26T12:00:00Z"  #Utilize the current date/time in production
        new_comment = {
            "comment_id": comment_id,
            "artifact_id": artifact_id,
            "message_id": gmail_message_id,
            "commenter_email": commenter_email,
            "comment_text": comment_text,
            "created_ts": created_ts,
        }
        figma_comments.append(new_comment)
        payload = {"new_comment": new_comment}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateFigmaCommentFromGmailMessage",
                "description": "Create a new Figma comment using a Gmail message ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {
                            "type": "string",
                            "description": "The artifact ID the comment is for.",
                        },
                        "gmail_message_id": {
                            "type": "string",
                            "description": "The Gmail message ID used for the comment.",
                        },
                        "created_ts": {
                            "type": "string",
                            "description": "Timestamp of comment creation (optional).",
                        },
                    },
                    "required": ["artifact_id", "gmail_message_id"],
                },
            },
        }


class CreateReviewApproval(Tool):  #WRITE
    @staticmethod
    def invoke(
        data: dict[str, Any],
        cycle_id: str,
        approval_comment_id: str = None,
        approver_email: str = None,
    ) -> str:
        pass
        #Check the input for validity
        if not isinstance(cycle_id, str) or not cycle_id:
            payload = {"error": "cycle_id must be a non-empty string"}
            out = json.dumps(payload)
            return out
        if not approval_comment_id and not approver_email:
            payload = {"error": "Must provide either approval_comment_id or approver_email"}
            out = json.dumps(
                payload)
            return out
        review_approvals = data.get("review_approvals", [])
        next_num = len(review_approvals) + 1
        approval_id = f"approval_{next_num:03d}"
        approved_ts = "2025-08-26T12:00:00Z"  #Utilize the current date/time in production
        #If a comment is given, attempt to retrieve approver_email from figma_comments
        if approval_comment_id:
            figma_comments = data.get("figma_comments", [])
            comment = next(
                (
                    c
                    for c in figma_comments
                    if c.get("comment_id") == approval_comment_id
                ),
                None,
            )
            if comment:
                approver_email = comment.get("commenter_email")
        new_approval = {
            "approval_id": approval_id,
            "cycle_id": cycle_id,
            "approver_email": approver_email,
            "approved_ts": approved_ts,
            "approval_comment_ref_nullable": approval_comment_id,
        }
        review_approvals.append(new_approval)
        payload = {"new_approval": new_approval}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateReviewApproval",
                "description": "Create a new review approval for a cycle, using either a figma comment id or approver email.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cycle_id": {
                            "type": "string",
                            "description": "The review cycle ID.",
                        },
                        "approval_comment_ref_nullable": {
                            "type": "string",
                            "description": "Optional figma comment ID for the approval.",
                        },
                        "approver_email": {
                            "type": "string",
                            "description": "Optional approver email if no comment is provided.",
                        },
                        "approved_ts": {
                            "type": "string",
                            "description": "Timestamp of approval (optional).",
                        },
                    },
                    "required": ["cycle_id"],
                },
            },
        }


class UpdateReviewCycleStatus(Tool):  #WRITE
    @staticmethod
    def invoke(data: dict[str, Any], cycle_id: str, new_status: str) -> str:
        pass
        #Check the input for validity
        if not isinstance(cycle_id, str) or not cycle_id:
            payload = {"error": "cycle_id must be a non-empty string"}
            out = json.dumps(payload)
            return out

        allowed_status = [
            "NEEDS_REVIEW",
            "APPROVED",
            "CHANGES_REQUESTED",
            "ESCALATED",
            "IN_FLIGHT",
        ]
        if new_status not in allowed_status:
            payload = {"error": f"Invalid status. Allowed: {allowed_status}"}
            out = json.dumps(payload)
            return out

        review_cycles = data.get("review_cycles", [])

        #Identify the review cycle that needs updating
        cycle_found = False
        for cycle in review_cycles:
            if cycle.get("cycle_id") == cycle_id:
                cycle_found = True
                old_status = cycle.get("status")
                cycle["status"] = new_status

                #If the status is being updated to ESCALATED, record the escalated timestamp
                if new_status == "ESCALATED" and old_status != "ESCALATED":
                    cycle["escalated_ts_nullable"] = "2025-08-26T12:00:00Z"
                elif new_status != "ESCALATED":
                    cycle["escalated_ts_nullable"] = None
                payload = {
                        "updated_cycle": cycle,
                        "previous_status": old_status,
                        "new_status": new_status,
                    }
                out = json.dumps(
                    payload)
                return out

        if not cycle_found:
            payload = {"error": f"Review cycle with cycle_id '{cycle_id}' not found"}
            out = json.dumps(
                payload)
            return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateReviewCycleStatus",
                "description": "Update the status of an existing review cycle.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cycle_id": {
                            "type": "string",
                            "description": "The review cycle ID to update.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "New review cycle status (NEEDS_REVIEW, APPROVED, CHANGES_REQUESTED, ESCALATED, IN_FLIGHT).",
                        },
                    },
                    "required": ["cycle_id", "new_status"],
                },
            },
        }


class DetectReleaseVersion(Tool):  #READ
    @staticmethod
    def invoke(data: dict[str, Any], release_id: str) -> str:
        pass
        #Check the input for validity
        if not isinstance(release_id, str) or not release_id:
            payload = {"error": "release_id must be a non-empty string"}
            out = json.dumps(payload)
            return out

        releases = data.get("releases", [])

        #Identify the release
        release = next((r for r in releases if r.get("release_id") == release_id), None)
        if not release:
            payload = {"error": f"Release with release_id '{release_id}' not found"}
            out = json.dumps(
                payload)
            return out

        #Verify if version_tag begins with "release/"
        version_tag = release.get("version_tag", "")
        is_release_version = version_tag.startswith("release/")
        payload = {"is_release_version": is_release_version, "release_info": release}
        out = json.dumps(
            payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DetectReleaseVersion",
                "description": "Detect if a release is a release version by checking if the version tag begins with 'release/' and return all release info.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "release_id": {
                            "type": "string",
                            "description": "The release ID to check.",
                        }
                    },
                    "required": ["release_id"],
                },
            },
        }


class ComputeReleaseDiffs(Tool):  #READ
    @staticmethod
    def invoke(
        data: dict[str, Any], release_id: str, changelog_highlights: list[str]
    ) -> str:
        pass
        #Check the input for validity
        if not isinstance(release_id, str) or not release_id:
            payload = {"error": "release_id must be a non-empty string"}
            out = json.dumps(payload)
            return out

        if not isinstance(changelog_highlights, list) or not all(
            isinstance(item, str) for item in changelog_highlights
        ):
            payload = {"error": "changelog_highlights must be a list of strings"}
            out = json.dumps(
                payload)
            return out

        releases = data.get("releases", [])
        figma_artifacts = data.get("figma_artifacts", [])

        #Identify the active release
        current_release = next(
            (r for r in releases if r.get("release_id") == release_id), None
        )
        if not current_release:
            payload = {"error": f"Release with release_id '{release_id}' not found"}
            out = json.dumps(
                payload)
            return out

        current_figma_file_id = current_release.get("figma_file_id")
        current_created_ts = current_release.get("created_ts")

        #Locate the last release with the same figma_file_id (using created_ts)
        same_file_releases = [
            r
            for r in releases
            if r.get("figma_file_id") == current_figma_file_id
            and r.get("release_id") != release_id
        ]

        #Order by created_ts and identify the latest one prior to the current release
        previous_release = None
        if same_file_releases:
            #Select releases that occurred before the current release
            prior_releases = [
                r
                for r in same_file_releases
                if r.get("created_ts", "") < current_created_ts
            ]
            if prior_releases:
                #Order by created_ts in descending order and select the first (most recent)
                prior_releases.sort(key=lambda x: x.get("created_ts", ""), reverse=True)
                previous_release = prior_releases[0]

        prior_release_id_nullable = (
            previous_release.get("release_id") if previous_release else None
        )
        previous_created_ts = (
            previous_release.get("created_ts") if previous_release else None
        )

        #Locate all figma_artifacts sharing the same figma_file_id
        same_file_artifacts = [
            artifact
            for artifact in figma_artifacts
            if artifact.get("figma_file_id") == current_figma_file_id
        ]

        frames_added = []
        frames_updated = []
        frames_removed = []  #Consistently empty as indicated
        component_version_bumps = []

        for artifact in same_file_artifacts:
            artifact_modified_ts = artifact.get("modified_ts")
            frame_id = artifact.get("frame_id_nullable")
            artifact_name = artifact.get("artifact_name", "")

            #Process solely those artifacts that possess a frame_id
            if frame_id:
                if previous_created_ts and artifact_modified_ts:
                    if artifact_modified_ts > previous_created_ts:
                        frames_updated.append(frame_id)
                    else:
                        frames_added.append(frame_id)
                else:
                    #If there is no prior release, treat all as newly added
                    frames_added.append(frame_id)

            #Create a version increment for each artifact
            if artifact_name:
                #Eliminate spaces and produce a random version
                component_name = artifact_name.replace(" ", "")
                version_num = len(component_name)
                component_version_bumps.append(f"{component_name}-v1.{version_num}")
        payload = {
                "release_id": release_id,
                "prior_release_id_nullable": prior_release_id_nullable,
                "frames_added": frames_added,
                "frames_updated": frames_updated,
                "frames_removed": frames_removed,
                "component_version_bumps": component_version_bumps,
                "changelog_highlights": changelog_highlights,
            }
        out = json.dumps(
            payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ComputeReleaseDiffs",
                "description": "Compute release diffs by comparing current release with previous release of the same Figma file.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "release_id": {
                            "type": "string",
                            "description": "The release ID to compute diffs for.",
                        },
                        "changelog_highlights": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of changelog highlights for the release.",
                        },
                    },
                    "required": ["release_id", "changelog_highlights"],
                },
            },
        }


class SaveReleaseDiffs(Tool):  #WRITE
    @staticmethod
    def invoke(
        data: dict[str, Any],
        release_id: str,
        prior_release_id_nullable: str,
        frames_added: list[str],
        frames_updated: list[str],
        frames_removed: list[str],
        component_version_bumps: list[str],
        changelog_highlights: list[str],
    ) -> str:
        pass
        #Check the input for validity
        if not isinstance(release_id, str) or not release_id:
            payload = {"error": "release_id must be a non-empty string"}
            out = json.dumps(payload)
            return out

        #Check the parameters of the list for validity
        if not isinstance(frames_added, list) or not all(
            isinstance(item, str) for item in frames_added
        ):
            payload = {"error": "frames_added must be a list of strings"}
            out = json.dumps(payload)
            return out

        if not isinstance(frames_updated, list) or not all(
            isinstance(item, str) for item in frames_updated
        ):
            payload = {"error": "frames_updated must be a list of strings"}
            out = json.dumps(payload)
            return out

        if not isinstance(frames_removed, list) or not all(
            isinstance(item, str) for item in frames_removed
        ):
            payload = {"error": "frames_removed must be a list of strings"}
            out = json.dumps(payload)
            return out

        if not isinstance(component_version_bumps, list) or not all(
            isinstance(item, str) for item in component_version_bumps
        ):
            payload = {"error": "component_version_bumps must be a list of strings"}
            out = json.dumps(
                payload)
            return out

        if not isinstance(changelog_highlights, list) or not all(
            isinstance(item, str) for item in changelog_highlights
        ):
            payload = {"error": "changelog_highlights must be a list of strings"}
            out = json.dumps(
                payload)
            return out

        if prior_release_id_nullable is not None and (
            not isinstance(prior_release_id_nullable, str)
            or not prior_release_id_nullable
        ):
            payload = {
                    "error": "prior_release_id_nullable must be a non-empty string or None"
                }
            out = json.dumps(
                payload)
            return out

        release_diffs = data["release_diffs"]

        #Verify if a diff is already present for this release_id
        existing_diff = next(
            (diff for diff in release_diffs if diff.get("release_id") == release_id),
            None,
        )
        if existing_diff:
            #Modify the existing diff rather than returning an error (for testing purposes)
            existing_diff.update(
                {
                    "prior_release_id_nullable": prior_release_id_nullable,
                    "frames_added": frames_added,
                    "frames_updated": frames_updated,
                    "frames_removed": frames_removed,
                    "component_version_bumps": component_version_bumps,
                    "changelog_highlights": changelog_highlights,
                }
            )
            payload = {"updated_release_diff": existing_diff}
            out = json.dumps(payload)
            return out

        #Create a new diff_id
        next_num = len(release_diffs) + 1
        diff_id = f"diff_{next_num:03d}"

        new_release_diff = {
            "diff_id": diff_id,
            "release_id": release_id,
            "prior_release_id_nullable": prior_release_id_nullable,
            "frames_added": frames_added,
            "frames_updated": frames_updated,
            "frames_removed": frames_removed,
            "component_version_bumps": component_version_bumps,
            "changelog_highlights": changelog_highlights,
        }

        release_diffs.append(new_release_diff)
        payload = {"new_release_diff": new_release_diff}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SaveReleaseDiffs",
                "description": "Save computed release diffs to the database by creating a new release_diff entry.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "release_id": {
                            "type": "string",
                            "description": "The release ID for the diff entry.",
                        },
                        "prior_release_id_nullable": {
                            "type": "string",
                            "description": "The previous release ID, or null if none exists.",
                        },
                        "frames_added": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of frame IDs that were added.",
                        },
                        "frames_updated": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of frame IDs that were updated.",
                        },
                        "frames_removed": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of frame IDs that were removed.",
                        },
                        "component_version_bumps": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of component version bumps.",
                        },
                        "changelog_highlights": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of changelog highlights for the release.",
                        },
                    },
                    "required": [
                        "release_id",
                        "prior_release_id_nullable",
                        "frames_added",
                        "frames_updated",
                        "frames_removed",
                        "component_version_bumps",
                        "changelog_highlights",
                    ],
                },
            },
        }


class GenerateBeforeAfterVisuals(Tool):  #WRITE
    @staticmethod
    def invoke(
        data: dict[str, Any], release_id: str, hero_artifact_ids: list[str]
    ) -> str:
        pass
        #Check the input for validity
        if not isinstance(release_id, str) or not release_id:
            payload = {"error": "release_id must be a non-empty string"}
            out = json.dumps(payload)
            return out

        if not isinstance(hero_artifact_ids, list) or not all(
            isinstance(aid, str) for aid in hero_artifact_ids
        ):
            payload = {"error": "hero_artifact_ids must be a list of strings"}
            out = json.dumps(payload)
            return out

        #Create a consistent visual name derived from release_id
        visual_name = f"before_after_visual_{release_id}"

        #Generate a consistent hash-like suffix using hero_artifact_ids
        artifacts_string = "".join(sorted(hero_artifact_ids))
        artifacts_hash = custom_hash(artifacts_string) % 10000
        visual_name_with_hash = f"{visual_name}_{artifacts_hash:04d}"
        payload = {
                "visual_name": visual_name_with_hash,
                "success": True,
                "message": f"Before/after visual successfully created for release {release_id}",
                "hero_artifacts_processed": len(hero_artifact_ids),
                "artifacts_included": hero_artifact_ids,
            }
        out = json.dumps(
            payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GenerateBeforeAfterVisuals",
                "description": "Generate before/after visuals for a release using hero artifacts.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "release_id": {
                            "type": "string",
                            "description": "The release ID to generate visuals for.",
                        },
                        "hero_artifact_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of hero artifact IDs to include in the visual.",
                        },
                    },
                    "required": ["release_id", "hero_artifact_ids"],
                },
            },
        }


class CreateAuditSession(Tool):  #WRITE
    @staticmethod
    def invoke(data: dict[str, Any], artifact_id: str, audit_type: str) -> str:
        pass
        #Check the input for validity
        if not isinstance(artifact_id, str) or not artifact_id:
            raise ValueError("artifact_id must be a non-empty string")

        allowed_audit_types = ["DS_MAPPING", "A11Y", "COMBINED_DS_A11Y"]
        if audit_type not in allowed_audit_types:
            raise ValueError(f"audit_type must be one of: {allowed_audit_types}")

        audits = data.get("audits", [])

        #Create a new audit_id by incrementing from current audits
        next_num = len(audits) + 1
        audit_id = f"audit_{next_num:03d}"

        #Assign created_ts to a time following the latest audit (2024-08-23T14:00:00Z)
        #Select a random time thereafter, for example, 2024-08-24T09:15:00Z
        created_ts = "2024-08-24T09:15:00Z"

        new_audit = {
            "audit_id": audit_id,
            "artifact_id": artifact_id,
            "audit_type": audit_type,
            "created_ts": created_ts,
            "status": "RUNNING",
            "report_asset_id_nullable": None,
        }

        audits.append(new_audit)
        payload = {"new_audit": new_audit}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateAuditSession",
                "description": "Create a new audit session for a Figma artifact.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {
                            "type": "string",
                            "description": "The artifact ID to audit.",
                        },
                        "audit_type": {
                            "type": "string",
                            "description": "Type of audit (DS_MAPPING, A11Y, COMBINED_DS_A11Y).",
                        },
                    },
                    "required": ["artifact_id", "audit_type"],
                },
            },
        }


class IdentifyCustomGroupsAndMapToDsComponents(Tool):  #READ
    @staticmethod
    def invoke(data: dict[str, Any], audit_id: str) -> str:
        pass
        #Check the input for validity
        if not isinstance(audit_id, str) or not audit_id:
            payload = {"error": "audit_id must be a non-empty string"}
            out = json.dumps(payload)
            return out

        audits = data.get("audits", [])
        artifacts = data.get("figma_artifacts", [])

        #Identify the audit
        audit = next((a for a in audits if a.get("audit_id") == audit_id), None)
        if not audit:
            payload = {"error": f"Audit {audit_id} not found"}
            out = json.dumps(payload)
            return out

        artifact_id = audit.get("artifact_id")
        if not artifact_id:
            payload = {"error": f"No artifact_id found for audit {audit_id}"}
            out = json.dumps(payload)
            return out

        #Locate the artifact
        artifact = next(
            (a for a in artifacts if a.get("artifact_id") == artifact_id), None
        )
        if not artifact:
            payload = {"error": f"Artifact {artifact_id} not found"}
            out = json.dumps(payload)
            return out

        #Utilize page_id as layer_id and artifact_name as layer_name
        layer_id = artifact.get("page_id")
        layer_name = artifact.get("artifact_name")

        if not layer_id or not layer_name:
            payload = {
                    "error": f"Missing page_id or artifact_name for artifact {artifact_id}"
                }
            out = json.dumps(
                payload)
            return out

        #Create consistent yet "random" values by hashing audit_id + artifact_id
        seed_string = f"{audit_id}_{artifact_id}"
        hash_value = custom_hash(seed_string)

        #Choose finding_type in a consistent manner
        finding_types = ["SUBSTITUTE_RECOMMENDED", "UNMAPPED", "AMBIGUOUS"]
        finding_type = finding_types[abs(hash_value) % len(finding_types)]

        #Create recommended_component_id based on layer_name
        #Extract the first word from layer_name and append the version
        words = layer_name.split()
        if words:
            component_word = words[0]
            version_major = (abs(hash_value) % 2) + 1  #1 or 2
            version_minor = abs(hash_value) % 10  #0-9
            recommended_component_id_nullable = (
                f"{component_word}-v{version_major}.{version_minor}"
            )
        else:
            recommended_component_id_nullable = None

        #Create severity in a consistent manner
        severities = ["LOW", "MEDIUM", "HIGH"]
        severity = severities[
            abs(hash_value // 7) % len(severities)
        ]  #Apply various hash divisions for diversity
        payload = {
                "audit_id": audit_id,
                "layer_id": layer_id,
                "layer_name": layer_name,
                "finding_type": finding_type,
                "recommended_component_id_nullable": recommended_component_id_nullable,
                "code_connect_link_nullable": None,
                "severity": severity,
            }
        out = json.dumps(
            payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "IdentifyCustomGroupsAndMapToDsComponents",
                "description": "Identify custom groups in a Figma artifact and map them to design system components.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {
                            "type": "string",
                            "description": "The audit ID to process.",
                        }
                    },
                    "required": ["audit_id"],
                },
            },
        }


class EvaluateAccessibility(Tool):  #READ
    @staticmethod
    def invoke(data: dict[str, Any], artifact_id: str) -> str:
        pass
        #Check the input for validity
        if not isinstance(artifact_id, str) or not artifact_id:
            payload = {"error": "artifact_id must be a non-empty string"}
            out = json.dumps(payload)
            return out

        artifacts = data.get("figma_artifacts", [])

        #Locate the artifact
        artifact = next(
            (a for a in artifacts if a.get("artifact_id") == artifact_id), None
        )
        if not artifact:
            payload = {"error": f"Artifact {artifact_id} not found"}
            out = json.dumps(payload)
            return out

        #Utilize page_id as layer_id and artifact_name as layer_name
        layer_id = artifact.get("page_id")
        layer_name = artifact.get("artifact_name")

        if not layer_id or not layer_name:
            payload = {
                    "error": f"Missing page_id or artifact_name for artifact {artifact_id}"
                }
            out = json.dumps(
                payload)
            return out

        #Create consistent yet "random" values by hashing artifact_id
        hash_value = custom_hash(artifact_id)

        #Choose violation_type in a consistent manner
        violation_types = ["TOUCH_TARGET", "CONTRAST", "TEXT_SIZING", "RTL"]
        violation_type = violation_types[abs(hash_value) % len(violation_types)]

        #Create violation_details_json and recommended_fix_summary according to violation_type
        if violation_type == "TOUCH_TARGET":
            sizes = ["32x32px", "36x36px", "40x40px"]
            current_size = sizes[abs(hash_value // 3) % len(sizes)]
            violation_details_json = f'{{"current_size": "{current_size}", "required_size": "44x44px", "description": "Touch target too small for mobile accessibility"}}'
            recommended_fix_summary = (
                "Increase button size to minimum 44x44px for touch accessibility"
            )

        elif violation_type == "CONTRAST":
            ratios = ["2.1:1", "2.8:1", "3.2:1"]
            colors = [
                {"foreground": "#666666", "background": "#ffffff"},
                {"foreground": "#888888", "background": "#ffffff"},
                {"foreground": "#777777", "background": "#ffffff"},
            ]
            current_ratio = ratios[abs(hash_value // 5) % len(ratios)]
            color_set = colors[abs(hash_value // 7) % len(colors)]
            violation_details_json = f'{{"current_ratio": "{current_ratio}", "required_ratio": "4.5:1", "colors": {{"foreground": "{color_set["foreground"]}", "background": "{color_set["background"]}"}}}}'
            recommended_fix_summary = (
                "Increase text color contrast to meet WCAG AA standards"
            )

        elif violation_type == "TEXT_SIZING":
            sizes = ["12px", "14px"]
            current_size = sizes[abs(hash_value // 11) % len(sizes)]
            violation_details_json = f'{{"current_size": "{current_size}", "required_size": "16px", "description": "Text too small for readability"}}'
            recommended_fix_summary = (
                "Increase font size to minimum 16px for better readability"
            )

        else:  #RTL
            issues = ["Fixed positioning", "Hardcoded margins", "Icon alignment"]
            issue = issues[abs(hash_value // 13) % len(issues)]
            violation_details_json = f'{{"issue": "{issue}", "description": "Layout doesn\'t adapt to RTL languages"}}'
            recommended_fix_summary = (
                "Implement flexible layout that supports RTL languages"
            )

        #Create severity in a consistent manner
        severities = ["LOW", "MEDIUM", "HIGH"]
        severity = severities[
            abs(hash_value // 17) % len(severities)
        ]  #Apply various hash divisions for diversity
        payload = {
                "artifact_id": artifact_id,
                "layer_id": layer_id,
                "layer_name": layer_name,
                "violation_type": violation_type,
                "violation_details_json": violation_details_json,
                "recommended_fix_summary": recommended_fix_summary,
                "severity": severity,
            }
        out = json.dumps(
            payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "EvaluateAccessibility",
                "description": "Evaluate accessibility of a Figma artifact and identify potential violations.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {
                            "type": "string",
                            "description": "The artifact ID to evaluate for accessibility.",
                        }
                    },
                    "required": ["artifact_id"],
                },
            },
        }


class RecordDsAuditFindings(Tool):  #WRITE
    @staticmethod
    def invoke(
        data: dict[str, Any],
        audit_id: str,
        layer_id: str,
        layer_name: str,
        finding_type: str,
        recommended_component_id_nullable: str = None,
        code_connect_link_nullable: str = None,
        severity: str = "MEDIUM",
    ) -> str:
        pass
        #Check the parameters for validity
        if not isinstance(audit_id, str) or not audit_id:
            payload = {"error": "audit_id must be a non-empty string"}
            out = json.dumps(payload)
            return out

        if not isinstance(layer_id, str) or not layer_id:
            payload = {"error": "layer_id must be a non-empty string"}
            out = json.dumps(payload)
            return out

        if not isinstance(layer_name, str) or not layer_name:
            payload = {"error": "layer_name must be a non-empty string"}
            out = json.dumps(payload)
            return out

        #Check the finding_type for validity
        allowed_finding_types = ["UNMAPPED", "AMBIGUOUS", "SUBSTITUTE_RECOMMENDED"]
        if finding_type not in allowed_finding_types:
            payload = {"error": f"Invalid finding_type. Allowed: {allowed_finding_types}"}
            out = json.dumps(
                payload)
            return out

        #Check the severity for validity
        allowed_severities = ["HIGH", "MEDIUM", "LOW"]
        if severity not in allowed_severities:
            payload = {"error": f"Invalid severity. Allowed: {allowed_severities}"}
            out = json.dumps(
                payload)
            return out

        #Check if the audit_id is present
        audits = data.get("audits", [])
        audit_exists = any(audit.get("audit_id") == audit_id for audit in audits)
        if not audit_exists:
            payload = {"error": f"Audit with ID '{audit_id}' not found"}
            out = json.dumps(payload)
            return out

        #Check the nullable fields for validity
        if recommended_component_id_nullable is not None and not isinstance(
            recommended_component_id_nullable, str
        ):
            payload = {"error": "recommended_component_id_nullable must be a string or None"}
            out = json.dumps(
                payload)
            return out

        if code_connect_link_nullable is not None and not isinstance(
            code_connect_link_nullable, str
        ):
            payload = {"error": "code_connect_link_nullable must be a string or None"}
            out = json.dumps(
                payload)
            return out

        #Retrieve audit_findings_ds data
        audit_findings_ds = data.get("audit_findings_ds", [])

        #Create a new finding_id
        next_num = len(audit_findings_ds) + 1
        finding_id = f"finding_ds_{next_num:03d}"

        #Establish a new finding entry
        new_finding = {
            "finding_id": finding_id,
            "audit_id": audit_id,
            "layer_id": layer_id,
            "layer_name": layer_name,
            "finding_type": finding_type,
            "recommended_component_id_nullable": recommended_component_id_nullable,
            "code_connect_link_nullable": code_connect_link_nullable,
            "severity": severity,
        }

        #Include in data
        audit_findings_ds.append(new_finding)
        payload = {"new_finding": new_finding}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RecordDsAuditFindings",
                "description": "Record design system audit findings for a specific layer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {
                            "type": "string",
                            "description": "The audit ID to record findings for.",
                        },
                        "layer_id": {
                            "type": "string",
                            "description": "The layer ID in the Figma artifact.",
                        },
                        "layer_name": {
                            "type": "string",
                            "description": "The name of the layer.",
                        },
                        "finding_type": {
                            "type": "string",
                            "description": "Type of finding (UNMAPPED, AMBIGUOUS, SUBSTITUTE_RECOMMENDED).",
                        },
                        "recommended_component_id_nullable": {
                            "type": "string",
                            "description": "Optional recommended component ID.",
                        },
                        "code_connect_link_nullable": {
                            "type": "string",
                            "description": "Optional code connect link.",
                        },
                        "severity": {
                            "type": "string",
                            "description": "Severity level (HIGH, MEDIUM, LOW). Defaults to MEDIUM.",
                        },
                    },
                    "required": ["audit_id", "layer_id", "layer_name", "finding_type"],
                },
            },
        }


class RecordAccessibilityAuditFindings(Tool):  #WRITE
    @staticmethod
    def invoke(
        data: dict[str, Any],
        audit_id: str,
        layer_id: str,
        layer_name: str,
        violation_type: str,
        violation_details_json: str,
        severity: str,
        recommended_fix_summary: str,
    ) -> str:
        pass
        #Check the parameters for validity
        if not isinstance(audit_id, str) or not audit_id:
            payload = {"error": "audit_id must be a non-empty string"}
            out = json.dumps(payload)
            return out

        if not isinstance(layer_id, str) or not layer_id:
            payload = {"error": "layer_id must be a non-empty string"}
            out = json.dumps(payload)
            return out

        if not isinstance(layer_name, str) or not layer_name:
            payload = {"error": "layer_name must be a non-empty string"}
            out = json.dumps(payload)
            return out

        if not isinstance(violation_type, str) or not violation_type:
            payload = {"error": "violation_type must be a non-empty string"}
            out = json.dumps(payload)
            return out

        if not isinstance(recommended_fix_summary, str) or not recommended_fix_summary:
            payload = {"error": "recommended_fix_summary must be a non-empty string"}
            out = json.dumps(
                payload)
            return out

        #Check the violation_type for validity
        allowed_violation_types = ["TOUCH_TARGET", "CONTRAST", "TEXT_SIZING", "RTL"]
        if violation_type not in allowed_violation_types:
            payload = {"error": f"Invalid violation_type. Allowed: {allowed_violation_types}"}
            out = json.dumps(
                payload)
            return out

        #Check the severity for validity
        allowed_severities = ["HIGH", "MEDIUM", "LOW"]
        if severity not in allowed_severities:
            payload = {"error": f"Invalid severity. Allowed: {allowed_severities}"}
            out = json.dumps(
                payload)
            return out

        #Check if the audit_id is present
        audits = data.get("audits", [])
        audit_exists = any(audit.get("audit_id") == audit_id for audit in audits)
        if not audit_exists:
            payload = {"error": f"Audit with ID '{audit_id}' not found"}
            out = json.dumps(payload)
            return out

        #Retrieve audit_findings_a11y data
        audit_findings_a11y = data.get("audit_findings_a11y", [])

        #Create a new finding_id
        next_num = len(audit_findings_a11y) + 1
        finding_id = f"finding_a11y_{next_num:03d}"

        #Establish a new finding entry
        new_finding = {
            "finding_id": finding_id,
            "audit_id": audit_id,
            "layer_id": layer_id,
            "layer_name": layer_name,
            "violation_type": violation_type,
            "violation_details_json": violation_details_json,
            "severity": severity,
            "recommended_fix_summary": recommended_fix_summary,
        }

        #Include in data
        audit_findings_a11y.append(new_finding)
        payload = {"new_finding": new_finding}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RecordAccessibilityAuditFindings",
                "description": "Record accessibility audit findings for a specific layer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {
                            "type": "string",
                            "description": "The audit ID to record findings for.",
                        },
                        "layer_id": {
                            "type": "string",
                            "description": "The layer ID in the Figma artifact.",
                        },
                        "layer_name": {
                            "type": "string",
                            "description": "The name of the layer.",
                        },
                        "violation_type": {
                            "type": "string",
                            "description": "Type of violation (TOUCH_TARGET, CONTRAST, TEXT_SIZING, RTL).",
                        },
                        "violation_details_json": {
                            "type": "string",
                            "description": "JSON string containing violation details.",
                        },
                        "severity": {
                            "type": "string",
                            "description": "Severity level (HIGH, MEDIUM, LOW).",
                        },
                        "recommended_fix_summary": {
                            "type": "string",
                            "description": "Summary of recommended fix for the violation.",
                        },
                    },
                    "required": [
                        "audit_id",
                        "layer_id",
                        "layer_name",
                        "violation_type",
                        "violation_details_json",
                        "severity",
                        "recommended_fix_summary",
                    ],
                },
            },
        }


class GenerateAuditReport(Tool):  #WRITE
    @staticmethod
    def invoke(data: dict[str, Any], audit_id: str) -> str:
        pass
        #Check the input for validity
        if not isinstance(audit_id, str) or not audit_id:
            payload = {"error": "audit_id must be a non-empty string"}
            out = json.dumps(payload)
            return out

        #Retrieve audits and assets data
        audits = data.get("audits", [])
        assets = data.get("assets", [])
        figma_artifacts = data.get("figma_artifacts", [])

        #Identify the audit
        audit = next((a for a in audits if a.get("audit_id") == audit_id), None)
        if not audit:
            payload = {"error": f"Audit with ID '{audit_id}' not found"}
            out = json.dumps(payload)
            return out

        #Obtain artifact_id from the audit
        artifact_id = audit.get("artifact_id")
        if not artifact_id:
            payload = {"error": f"No artifact_id found for audit {audit_id}"}
            out = json.dumps(payload)
            return out

        #Locate the artifact to retrieve the layer_name
        artifact = next(
            (a for a in figma_artifacts if a.get("artifact_id") == artifact_id), None
        )
        if not artifact:
            payload = {"error": f"Artifact with ID '{artifact_id}' not found"}
            out = json.dumps(payload)
            return out

        artifact_name = artifact.get("artifact_name")
        if not artifact_name:
            payload = {"error": f"No artifact_name found for artifact {artifact_id}"}
            out = json.dumps(
                payload)
            return out

        #Create a new asset_id
        next_num = len(assets) + 1
        asset_id = f"asset_{next_num:03d}"

        #Create storage_ref using the artifact name (spaces substituted with hyphens)
        clean_name = artifact_name.lower().replace(" ", "-")
        storage_ref = f"gs://company-assets/audit-reports/{clean_name}-audit-report.pdf"

        #Establish a new asset entry
        new_asset = {
            "asset_id": asset_id,
            "artifact_id_nullable": artifact_id,
            "export_profile": "PDF",
            "file_size_bytes": 2048000,  #Standard size for PDF audit reports
            "storage_ref": storage_ref,
            "created_ts": "2025-08-28T15:00:00Z",
            "dlp_scan_status": "CLEAN",
            "dlp_scan_details_nullable": None,
        }

        #Include in assets data
        assets.append(new_asset)
        payload = {"new_asset": new_asset}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GenerateAuditReport",
                "description": "Generate a PDF audit report and create an asset entry for it.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {
                            "type": "string",
                            "description": "The audit ID to generate a report for.",
                        }
                    },
                    "required": ["audit_id"],
                },
            },
        }


class UpdateAuditStatus(Tool):  #WRITE
    @staticmethod
    def invoke(data: dict[str, Any], audit_id: str, status: str) -> str:
        pass
        #Check the input for validity
        if not isinstance(audit_id, str) or not audit_id:
            payload = {"error": "audit_id must be a non-empty string"}
            out = json.dumps(payload)
            return out

        if not isinstance(status, str) or not status:
            payload = {"error": "status must be a non-empty string"}
            out = json.dumps(payload)
            return out

        #Check the status value for validity
        allowed_statuses = ["RUNNING", "COMPLETED", "FAILED", "CANCELLED"]
        if status not in allowed_statuses:
            payload = {"error": f"Invalid status. Allowed: {allowed_statuses}"}
            out = json.dumps(payload)
            return out

        #Retrieve audits data
        audits = data.get("audits", [])

        #Identify the audit that needs updating
        audit_to_update = None
        for audit in audits:
            if audit.get("audit_id") == audit_id:
                audit_to_update = audit
                break

        if not audit_to_update:
            payload = {"error": f"Audit with ID '{audit_id}' not found"}
            out = json.dumps(payload)
            return out

        #Modify the status
        old_status = audit_to_update.get("status")
        audit_to_update["status"] = status
        payload = {
                "updated_audit": audit_to_update,
                "old_status": old_status,
                "new_status": status,
            }
        out = json.dumps(
            payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAuditStatus",
                "description": "Update the status of an audit.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {
                            "type": "string",
                            "description": "The audit ID to update.",
                        },
                        "status": {
                            "type": "string",
                            "description": "New status (RUNNING, COMPLETED, FAILED, CANCELLED).",
                        },
                    },
                    "required": ["audit_id", "status"],
                },
            },
        }


class LinkAuditReportAsset(Tool):  #WRITE
    @staticmethod
    def invoke(data: dict[str, Any], audit_id: str, report_asset_id: str) -> str:
        pass
        #Check the input for validity
        if not isinstance(audit_id, str) or not audit_id:
            payload = {"error": "audit_id must be a non-empty string"}
            out = json.dumps(payload)
            return out

        if not isinstance(report_asset_id, str) or not report_asset_id:
            payload = {"error": "report_asset_id must be a non-empty string"}
            out = json.dumps(payload)
            return out

        #Retrieve audits and assets data
        audits = data.get("audits", [])
        assets = data.get("assets", [])

        #Check for the existence of the asset
        asset_exists = any(asset.get("asset_id") == report_asset_id for asset in assets)
        if not asset_exists:
            payload = {"error": f"Asset with ID '{report_asset_id}' not found"}
            out = json.dumps(payload)
            return out

        #Identify the audit that needs updating
        audit_to_update = None
        for audit in audits:
            if audit.get("audit_id") == audit_id:
                audit_to_update = audit
                break

        if not audit_to_update:
            payload = {"error": f"Audit with ID '{audit_id}' not found"}
            out = json.dumps(payload)
            return out

        #Modify the report_asset_id_nullable
        old_asset_id = audit_to_update.get("report_asset_id_nullable")
        audit_to_update["report_asset_id_nullable"] = report_asset_id
        payload = {
                "updated_audit": audit_to_update,
                "old_report_asset_id": old_asset_id,
                "new_report_asset_id": report_asset_id,
            }
        out = json.dumps(
            payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LinkAuditReportAsset",
                "description": "Link an asset to an audit as its report.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {
                            "type": "string",
                            "description": "The audit ID to update.",
                        },
                        "report_asset_id": {
                            "type": "string",
                            "description": "The asset ID to link as the audit report.",
                        },
                    },
                    "required": ["audit_id", "report_asset_id"],
                },
            },
        }


class LoadAuditFindings(Tool):  #READ
    @staticmethod
    def invoke(data: dict[str, Any], audit_id: str) -> str:
        pass
        #Check the input for validity
        if not isinstance(audit_id, str) or not audit_id:
            payload = {"error": "Invalid audit_id parameter"}
            out = json.dumps(payload)
            return out

        #Identify the audit
        audits = data.get("audits", [])
        audit = None
        for a in audits:
            if a.get("audit_id") == audit_id:
                audit = a
                break

        if not audit:
            payload = {"error": f"Audit with ID '{audit_id}' not found"}
            out = json.dumps(payload)
            return out

        #Retrieve details about the audit
        audit_type = audit.get("audit_type")
        artifact_id = audit.get("artifact_id")

        #Locate associated DS findings
        ds_findings = []
        audit_findings_ds = data.get("audit_findings_ds", [])
        for finding in audit_findings_ds:
            if finding.get("audit_id") == audit_id:
                ds_findings.append(
                    {
                        "finding_id": finding.get("finding_id"),
                        "layer_id": finding.get("layer_id"),
                        "layer_name": finding.get("layer_name"),
                        "finding_type": finding.get("finding_type"),
                        "severity": finding.get("severity"),
                    }
                )

        #Locate associated A11Y findings
        a11y_findings = []
        audit_findings_a11y = data.get("audit_findings_a11y", [])
        for finding in audit_findings_a11y:
            if finding.get("audit_id") == audit_id:
                a11y_findings.append(
                    {
                        "finding_id": finding.get("finding_id"),
                        "layer_id": finding.get("layer_id"),
                        "layer_name": finding.get("layer_name"),
                        "violation_type": finding.get("violation_type"),
                        "severity": finding.get("severity"),
                    }
                )
        payload = {
                "audit_id": audit_id,
                "audit_type": audit_type,
                "artifact_id": artifact_id,
                "ds_findings": ds_findings,
                "a11y_findings": a11y_findings,
                "total_ds_findings": len(ds_findings),
                "total_a11y_findings": len(a11y_findings),
            }
        out = json.dumps(
            payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LoadAuditFindings",
                "description": "Load audit information and all associated findings for a given audit ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {
                            "type": "string",
                            "description": "The audit ID to load findings for.",
                        }
                    },
                    "required": ["audit_id"],
                },
            },
        }


class PrioritizeAuditFindings(Tool):  #READ
    @staticmethod
    def invoke(data: dict[str, Any], finding_ids_list: list[str]) -> str:
        pass
        #Check the input for validity
        if not isinstance(finding_ids_list, list) or not all(
            isinstance(fid, str) for fid in finding_ids_list
        ):
            payload = {"error": "finding_ids_list must be a list of strings"}
            out = json.dumps(payload)
            return out

        if not finding_ids_list:
            payload = {"error": "finding_ids_list cannot be empty"}
            out = json.dumps(payload)
            return out

        #Retrieve findings data
        audit_findings_ds = data.get("audit_findings_ds", [])
        audit_findings_a11y = data.get("audit_findings_a11y", [])

        #Gather all findings along with their details
        findings_with_details = []

        for finding_id in finding_ids_list:
            #Prioritize searching in DS findings
            ds_finding = next(
                (f for f in audit_findings_ds if f.get("finding_id") == finding_id),
                None,
            )
            if ds_finding:
                findings_with_details.append(
                    {
                        "finding_id": finding_id,
                        "severity": ds_finding.get("severity", "MEDIUM"),
                        "finding_type": "DS",
                        "layer_name": ds_finding.get("layer_name", ""),
                        "details": ds_finding,
                    }
                )
                continue

            #Search within A11Y findings
            a11y_finding = next(
                (f for f in audit_findings_a11y if f.get("finding_id") == finding_id),
                None,
            )
            if a11y_finding:
                findings_with_details.append(
                    {
                        "finding_id": finding_id,
                        "severity": a11y_finding.get("severity", "MEDIUM"),
                        "finding_type": "A11Y",
                        "layer_name": a11y_finding.get("layer_name", ""),
                        "details": a11y_finding,
                    }
                )
                continue
            payload = {
                    "error": f"Finding with ID '{finding_id}' not found in either DS or A11Y findings"
                }
            out = json.dumps(
                payload)
            return out

        #Establish severity priority (higher number indicates higher priority)
        severity_priority = {"HIGH": 3, "MEDIUM": 2, "LOW": 1}

        #Obtain the finding number from finding_id for resolving ties
        def get_finding_number(finding_id):
            pass
            try:
                #Retrieve the number from finding_id such as "finding_ds_001" or "finding_a11y_001"
                parts = finding_id.split("_")
                if len(parts) >= 3:
                    return int(parts[-1])
                return 0
            except (ValueError, IndexError):
                return 0

        #Order findings by severity (descending) followed by finding number (ascending)
        sorted_findings = sorted(
            findings_with_details,
            key=lambda x: (
                -severity_priority.get(
                    x["severity"], 0
                ),  #Use negative for descending order
                get_finding_number(x["finding_id"]),  #Use ascending order for resolving ties
            ),
        )

        #Establish a mapping for priorities
        priority_mapping = {}
        for i, finding in enumerate(sorted_findings, 1):
            priority_mapping[finding["finding_id"]] = i

        #Generate a comprehensive result
        prioritized_findings = []
        for i, finding in enumerate(sorted_findings, 1):
            prioritized_findings.append(
                {
                    "priority": i,
                    "finding_id": finding["finding_id"],
                    "severity": finding["severity"],
                }
            )
        payload = {
                "priority_mapping": priority_mapping,
                "prioritized_findings": prioritized_findings,
                "total_findings": len(finding_ids_list),
            }
        out = json.dumps(
            payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "PrioritizeAuditFindings",
                "description": "Prioritize a list of audit findings by severity (HIGH > MEDIUM > LOW) and then by finding number for tie-breaking.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "finding_ids_list": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of finding IDs from either audit_findings_ds or audit_findings_a11y to prioritize.",
                        }
                    },
                    "required": ["finding_ids_list"],
                },
            },
        }


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
        fix_plans = data.get("fix_plans", [])
        plan_exists = any(plan.get("plan_id") == plan_id for plan in fix_plans)
        if not plan_exists:
            payload = {"error": f"Fix plan with ID '{plan_id}' not found"}
            out = json.dumps(payload)
            return out

        #Verify if the finding is present in either DS or A11Y findings
        audit_findings_ds = data.get("audit_findings_ds", [])
        audit_findings_a11y = data.get("audit_findings_a11y", [])

        finding_exists_ds = any(
            finding.get("finding_id") == finding_id for finding in audit_findings_ds
        )
        finding_exists_a11y = any(
            finding.get("finding_id") == finding_id for finding in audit_findings_a11y
        )

        if not (finding_exists_ds or finding_exists_a11y):
            payload = {
                    "error": f"Finding with ID '{finding_id}' not found in either DS or A11Y findings"
                }
            out = json.dumps(
                payload)
            return out

        #Retrieve current fix items to identify the next item_id
        fix_items = data.get("fix_items", [])
        next_num = len(fix_items) + 1
        item_id = f"item_{next_num:03d}"

        #Utilize a hash of input parameters to determine proposed_change_type
        input_hash = custom_hash(f"{plan_id}_{finding_id}")
        change_types = ["SPACING_ADJUST", "TOKEN_SWAP", "COMPONENT_SWAP"]
        proposed_change_type = change_types[input_hash % len(change_types)]

        #Locate existing items with the same proposed_change_type to extract details
        same_type_items = [
            item
            for item in fix_items
            if item.get("proposed_change_type") == proposed_change_type
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
        fix_items.append(new_fix_item)
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


class NotifyStakeholders(Tool):  #WRITE
    @staticmethod
    def invoke(
        data: dict[str, Any],
        plan_id: str,
        stakeholder_emails: list[str],
        audit_id: str,
        status: str,
        owner_email: str,
    ) -> str:
        pass
        #Check the input for validity
        if not isinstance(plan_id, str) or not plan_id:
            payload = {"error": "plan_id must be a non-empty string"}
            out = json.dumps(payload)
            return out
        if not isinstance(stakeholder_emails, list) or not all(
            isinstance(e, str) for e in stakeholder_emails
        ):
            payload = {"error": "stakeholder_emails must be a list of strings"}
            out = json.dumps(payload)
            return out
        if not isinstance(audit_id, str) or not audit_id:
            payload = {"error": "audit_id must be a non-empty string"}
            out = json.dumps(payload)
            return out
        if not isinstance(status, str) or not status:
            payload = {"error": "status must be a non-empty string"}
            out = json.dumps(payload)
            return out
        if not isinstance(owner_email, str) or not owner_email:
            payload = {"error": "owner_email must be a non-empty string"}
            out = json.dumps(payload)
            return out

        #Retrieve valid Gmail labels for the notification workflow
        gmail_labels = get_config_options(data, "gmail_labels")
        notification_labels = ["fix-plan", "audit", "notification"]
        valid_labels = [label for label in notification_labels if label in gmail_labels]
        if not valid_labels:
            #Revert to available labels
            valid_labels = gmail_labels[:2] if len(gmail_labels) >= 2 else gmail_labels

        #Initiate the Gmail thread first
        gmail_threads = data.get("gmail_threads", [])
        next_thread_num = len(gmail_threads) + 1
        thread_id = f"thread_{next_thread_num:03d}"
        created_ts = "2025-08-29T12:00:00Z"

        subject = f"Fix Plan Notification - {status} - {plan_id}"

        new_thread = {
            "thread_id": thread_id,
            "sender_email": owner_email,
            "recipients_emails": stakeholder_emails,
            "subject": subject,
            "current_labels": valid_labels,
            "created_ts": created_ts,
        }
        gmail_threads.append(new_thread)

        #Compose a Gmail message within the thread
        gmail_messages = data.get("gmail_messages", [])
        next_msg_num = len(gmail_messages) + 1
        message_id = f"msg_{next_msg_num:03d}"
        sent_ts = created_ts

        #Generate the content for the notification message
        body_text_stripped = f"Hello, this is a notification regarding fix plan {plan_id} for audit {audit_id}. Current status: {status}. Please review the attached fix plan details."

        new_message = {
            "message_id": message_id,
            "thread_id": thread_id,
            "sender_email": owner_email,
            "body_html": f"<p>{body_text_stripped}</p>",
            "body_text_stripped": body_text_stripped,
            "sent_ts": sent_ts,
            "attachments_asset_ids": [],
        }
        gmail_messages.append(new_message)
        payload = {
                "thread_created": new_thread,
                "message_created": new_message,
                "notification_sent": True,
                "stakeholders_notified": len(stakeholder_emails),
            }
        out = json.dumps(
            payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "NotifyStakeholders",
                "description": "Notify stakeholders about fix plan status by creating a Gmail thread and message.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {
                            "type": "string",
                            "description": "The fix plan ID to notify about.",
                        },
                        "stakeholder_emails": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of stakeholder email addresses to notify.",
                        },
                        "audit_id": {
                            "type": "string",
                            "description": "The audit ID associated with the fix plan.",
                        },
                        "status": {
                            "type": "string",
                            "description": "The current status of the fix plan.",
                        },
                        "owner_email": {
                            "type": "string",
                            "description": "The email address of the fix plan owner (sender).",
                        },
                    },
                    "required": [
                        "plan_id",
                        "stakeholder_emails",
                        "audit_id",
                        "status",
                        "owner_email",
                    ],
                },
            },
        }


TOOLS = [
    CreateReviewCycle(),
    ExportFigmaArtifactsToAssets(),
    FilterFigmaArtifactsByTags(),
    GetArtifactIdFromName(),
    CreateGmailMessage(),
    CreateGmailThread(),
    CreateFigmaCommentFromGmailMessage(),
    CreateReviewApproval(),
    UpdateReviewCycleStatus(),
    DetectReleaseVersion(),
    ComputeReleaseDiffs(),
    SaveReleaseDiffs(),
    GenerateBeforeAfterVisuals(),
    CreateAuditSession(),
    IdentifyCustomGroupsAndMapToDsComponents(),
    EvaluateAccessibility(),
    RecordDsAuditFindings(),
    RecordAccessibilityAuditFindings(),
    GenerateAuditReport(),
    UpdateAuditStatus(),
    LinkAuditReportAsset(),
    LoadAuditFindings(),
    PrioritizeAuditFindings(),
    CreateFixPlan(),
    CreateFixItem(),
    CreateAndDeliverFixPlan(),
    NotifyStakeholders(),
]
