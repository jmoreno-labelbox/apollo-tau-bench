import json
import uuid
from datetime import datetime
from typing import Any

from tau_bench.envs.tool import Tool




def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db


class UpdateReviewCycleStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], cycle_id: str = None, new_status: str = None, approver_id: str = None, comments: str = "", reviewer_email: str = None, status_notes: str = None, completion_notes: str = None, updated_by: str = None) -> str:
        # Support reviewer_email as alternative to approver_id
        if reviewer_email is not None:
            approver_id = reviewer_email
        # Support status_notes or completion_notes as alternative to comments
        if status_notes is not None:
            comments = status_notes
        if completion_notes is not None:
            comments = completion_notes
        # Support updated_by as alternative to approver_id
        if updated_by is not None:
            approver_id = updated_by
        """
        Modifies the status of a review cycle and manages status transitions.
        """
        if not all([cycle_id, new_status]):
            payload = {"error": "cycle_id and new_status are required."}
            out = json.dumps(payload)
            return out

        # Check the validity of status values
        valid_statuses = [
            "IN_FLIGHT",
            "NEEDS_REVIEW",
            "APPROVED",
            "CHANGES_REQUESTED",
            "ESCALATED",
        ]
        if new_status not in valid_statuses:
            payload = {
                "error": f"Invalid status. Must be one of: {', '.join(valid_statuses)}"
            }
            out = json.dumps(payload)
            return out

        review_cycles = data.get("review_cycles", {}).values()
        review_approvals = data.get("review_approvals", {}).values()

        # Locate the review cycle
        cycle_found = False
        for cycle in review_cycles.values():
            if cycle.get("cycle_id") == cycle_id:
                cycle_found = True
                old_status = cycle.get("status")

                # Modify the status of the cycle
                cycle["status"] = new_status
                cycle["last_updated"] = datetime.now().isoformat()

                # Manage logic based on status
                if new_status == "APPROVED" and approver_id:
                    # Generate an approval record
                    approval_id = f"approval_{uuid.uuid4().hex[:8]}"
                    new_approval = {
                        "approval_id": approval_id,
                        "cycle_id": cycle_id,
                        "approver_id": approver_id,
                        "approval_date": datetime.now().isoformat(),
                        "comments": comments,
                        "status": "APPROVED",
                    }
                    data["review_approvals"][new_approval["review_approval_id"]] = new_approval

                elif new_status == "CHANGES_REQUESTED" and comments:
                    # Include change request in comments
                    if "change_requests" not in cycle:
                        cycle["change_requests"] = []
                    cycle["change_requests"].append(
                        {
                            "request_id": f"req_{uuid.uuid4().hex[:8]}",
                            "requester_id": approver_id,
                            "request_date": datetime.now().isoformat(),
                            "comments": comments,
                        }
                    )

                # Record the change in status
                if "status_history" not in cycle:
                    cycle["status_history"] = []
                cycle["status_history"].append(
                    {
                        "from_status": old_status,
                        "to_status": new_status,
                        "changed_by": approver_id,
                        "changed_at": datetime.now().isoformat(),
                        "comments": comments,
                    }
                )

                break

        if not cycle_found:
            payload = {"error": f"Review cycle with ID '{cycle_id}' not found."}
            out = json.dumps(payload)
            return out
        payload = {
            "success": True,
            "cycle_id": cycle_id,
            "old_status": old_status,
            "new_status": new_status,
            "updated_at": datetime.now().isoformat(),
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateReviewCycleStatus",
                "description": "Updates the status of a design review cycle and handles status transitions including approvals and change requests.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cycle_id": {
                            "type": "string",
                            "description": "The ID of the review cycle to update.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new status for the review cycle. Must be one of: IN_FLIGHT, NEEDS_REVIEW, APPROVED, CHANGES_REQUESTED, ESCALATED.",
                        },
                        "approver_id": {
                            "type": "string",
                            "description": "The ID of the person making the status change.",
                        },
                        "comments": {
                            "type": "string",
                            "description": "Optional comments about the status change or change request.",
                        },
                    },
                    "required": ["cycle_id", "new_status"],
                },
            },
        }


class GetFigmaArtifactsByStatus(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        artifact_id: str = None,
        status: str = None,
        tags: list[str] = None,
        review_status: str = None,
        artifact_type: str = None
    ) -> str:
        """
        Obtains Figma artifacts filtered by different criteria such as status, tags, and review state.
        """
        if tags is None:
            tags = []

        figma_artifacts = data.get("figma_artifacts", {}).values()
        review_cycles = data.get("review_cycles", {}).values()

        # Return the specific artifact if artifact_id is given
        if artifact_id:
            for artifact in figma_artifacts.values():
                if artifact.get("artifact_id") == artifact_id:
                    # Enhance with details from the review cycle
                    artifact_copy = artifact.copy()
                    for cycle in review_cycles.values():
                        if cycle.get("artifact_id") == artifact_id:
                            artifact_copy["review_cycle"] = cycle
                            break
                    payload = artifact_copy
                    out = json.dumps(payload, indent=2)
                    return out
            payload = {"error": f"Artifact with ID '{artifact_id}' not found."}
            out = json.dumps(payload)
            return out

        # Sort artifacts based on specified criteria
        results = []
        for artifact in figma_artifacts.values():
            # Implement filters
            if status and artifact.get("status") != status:
                continue

            if artifact_type and artifact.get("artifact_type") != artifact_type:
                continue

            if tags:
                artifact_tags = artifact.get("current_tags", [])
                if not any(tag in artifact_tags for tag in tags.values()):
                    continue

            # Augment with review cycle details
            artifact_copy = artifact.copy()
            for cycle in review_cycles.values():
                if cycle.get("artifact_id") == artifact.get("artifact_id"):
                    artifact_copy["review_cycle"] = cycle
                    break

            # Implement filter for review status
            if review_status:
                if "review_cycle" not in artifact_copy:
                    continue
                if artifact_copy["review_cycle"].get("status") != review_status:
                    continue

            results.append(artifact_copy)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetFigmaArtifactsByStatus",
                "description": "Retrieves Figma artifacts filtered by various criteria including status, tags, review state, and artifact type. Enriches results with review cycle information.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {
                            "type": "string",
                            "description": "The ID of a specific artifact to retrieve.",
                        },
                        "status": {
                            "type": "string",
                            "description": "Filter by artifact status (e.g., 'active', 'archived').",
                        },
                        "tags": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Filter by tags (e.g., ['needs-review', 'design-system']).",
                        },
                        "review_status": {
                            "type": "string",
                            "description": "Filter by review cycle status (e.g., 'NEEDS_REVIEW', 'APPROVED').",
                        },
                        "artifact_type": {
                            "type": "string",
                            "description": "Filter by artifact type (e.g., 'frame', 'component', 'page').",
                        },
                    },
                },
            },
        }


class GetAuditFindingsSummary(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        audit_id: str = None,
        finding_type: str = None,
        severity: str = None,
        violation_type: str = None,
        include_resolved: bool = None
    ) -> str:
        """
        Obtains a detailed summary of audit findings, including violations from the design system and accessibility.
        """
        audits = data.get("audits", {}).values()
        audit_findings_ds = data.get("audit_findings_ds", {}).values()
        audit_findings_a11y = data.get("audit_findings_a11y", {}).values()

        # Return specific audit findings if audit_id is supplied
        if audit_id:
            audit_info = None
            for audit in audits.values():
                if audit.get("audit_id") == audit_id:
                    audit_info = audit
                    break

            if not audit_info:
                payload = {"error": f"Audit with ID '{audit_id}' not found."}
                out = json.dumps(payload)
                return out

            # Retrieve findings related to this audit
            ds_findings = [
                f for f in audit_findings_ds.values() if f.get("audit_id") == audit_id
            ]
            a11y_findings = [
                f for f in audit_findings_a11y.values() if f.get("audit_id") == audit_id
            ]

            summary = {
                "audit_info": audit_info,
                "design_system_findings": {
                    "total": len(ds_findings),
                    "unmapped": len(
                        [f for f in ds_findings.values() if f.get("finding_type") == "UNMAPPED"]
                    ),
                    "substitute_recommended": len(
                        [
                            f
                            for f in ds_findings.values() if f.get("finding_type") == "SUBSTITUTE_RECOMMENDED"
                        ]
                    ),
                    "ambiguous": len(
                        [f for f in ds_findings.values() if f.get("finding_type") == "AMBIGUOUS"]
                    ),
                },
                "accessibility_findings": {
                    "total": len(a11y_findings),
                    "touch_target": len(
                        [
                            f
                            for f in a11y_findings.values() if f.get("violation_type") == "TOUCH_TARGET"
                        ]
                    ),
                    "contrast": len(
                        [
                            f
                            for f in a11y_findings.values() if f.get("violation_type") == "CONTRAST"
                        ]
                    ),
                    "text_sizing": len(
                        [
                            f
                            for f in a11y_findings.values() if f.get("violation_type") == "TEXT_SIZING"
                        ]
                    ),
                    "rtl": len(
                        [f for f in a11y_findings.values() if f.get("violation_type") == "RTL"]
                    ),
                },
                "findings": {
                    "design_system": ds_findings,
                    "accessibility": a11y_findings,
                },
            }
            payload = summary
            out = json.dumps(payload, indent=2)
            return out

        # Provide a summary for all audits
        all_ds_findings = audit_findings_ds
        all_a11y_findings = audit_findings_a11y

        # Enforce filters
        if finding_type:
            all_ds_findings = [
                f for f in all_ds_findings if f.get("finding_type") == finding_type
            ]

        if violation_type:
            all_a11y_findings = [
                f
                for f in all_a11y_findings
                if f.get("violation_type") == violation_type
            ]

        if severity:
            all_ds_findings = [
                f for f in all_ds_findings if f.get("severity") == severity
            ]
            all_a11y_findings = [
                f for f in all_a11y_findings if f.get("severity") == severity
            ]

        summary = {
            "total_audits": len(audits),
            "design_system_findings": {
                "total": len(all_ds_findings),
                "by_type": {},
                "by_severity": {},
            },
            "accessibility_findings": {
                "total": len(all_a11y_findings),
                "by_type": {},
                "by_severity": {},
            },
        }

        # Categorize findings from the design system
        for finding in all_ds_findings:
            finding_type = finding.get("finding_type")
            severity = finding.get("severity")

            if finding_type not in summary["design_system_findings"]["by_type"]:
                summary["design_system_findings"]["by_type"][finding_type] = 0
            summary["design_system_findings"]["by_type"][finding_type] += 1

            if severity not in summary["design_system_findings"]["by_severity"]:
                summary["design_system_findings"]["by_severity"][severity] = 0
            summary["design_system_findings"]["by_severity"][severity] += 1

        # Classify accessibility findings
        for finding in all_a11y_findings:
            violation_type = finding.get("violation_type")
            severity = finding.get("severity")

            if violation_type not in summary["accessibility_findings"]["by_type"]:
                summary["accessibility_findings"]["by_type"][violation_type] = 0
            summary["accessibility_findings"]["by_type"][violation_type] += 1

            if severity not in summary["accessibility_findings"]["by_severity"]:
                summary["accessibility_findings"]["by_severity"][severity] = 0
            summary["accessibility_findings"]["by_severity"][severity] += 1
        payload = summary
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAuditFindingsSummary",
                "description": "Retrieves a comprehensive summary of audit findings including design system and accessibility violations, with filtering and grouping capabilities.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {
                            "type": "string",
                            "description": "The ID of a specific audit to retrieve findings for.",
                        },
                        "finding_type": {
                            "type": "string",
                            "description": "Filter design system findings by type (e.g., 'UNMAPPED', 'SUBSTITUTE_RECOMMENDED', 'AMBIGUOUS').",
                        },
                        "severity": {
                            "type": "string",
                            "description": "Filter findings by severity (e.g., 'HIGH', 'MEDIUM', 'LOW').",
                        },
                        "violation_type": {
                            "type": "string",
                            "description": "Filter accessibility findings by violation type (e.g., 'TOUCH_TARGET', 'CONTRAST', 'TEXT_SIZING', 'RTL').",
                        },
                    },
                },
            },
        }


class UpdateGmailThreadLabels(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        new_labels: list[str] = [],
        remove_labels: list[str] = [],
        status_notes: str = "",
        thread_id: str = None,
        update_recipients: list[str] = []
    ) -> str:
        """
        Modifies Gmail thread labels and oversees email workflow status.
        """
        if not thread_id:
            payload = {"error": "thread_id is required."}
            out = json.dumps(payload)
            return out

        gmail_threads = data.get("gmail_threads", {}).values()

        # Locate the thread
        thread_found = False
        for thread in gmail_threads.values():
            if thread.get("thread_id") == thread_id:
                thread_found = True
                old_labels = thread.get("current_labels", []).copy()

                # Revise labels
                if new_labels:
                    for label in new_labels:
                        if label not in old_labels:
                            old_labels.append(label)

                if remove_labels:
                    for label in remove_labels:
                        if label in old_labels:
                            old_labels.remove(label)

                thread["current_labels"] = old_labels
                thread["updated_ts"] = datetime.now().isoformat()

                # Modify recipients if they are specified
                if update_recipients:
                    thread["recipients"] = update_recipients

                # Include notes regarding the status
                if status_notes:
                    if "status_history" not in thread:
                        thread["status_history"] = []
                    thread["status_history"].append(
                        {
                            "timestamp": datetime.now().isoformat(),
                            "action": "labels_updated",
                            "notes": status_notes,
                            "old_labels": thread.get("current_labels", []),
                            "new_labels": old_labels,
                        }
                    )

                break

        if not thread_found:
            payload = {"error": f"Gmail thread with ID '{thread_id}' not found."}
            out = json.dumps(payload)
            return out

        payload = {
            "success": True,
            "thread_id": thread_id,
            "old_labels": old_labels,
            "new_labels": old_labels,
            "updated_at": datetime.now().isoformat(),
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateGmailThreadLabels",
                "description": "Updates Gmail thread labels, recipients, and manages email workflow status with comprehensive tracking.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "thread_id": {
                            "type": "string",
                            "description": "The ID of the Gmail thread to update.",
                        },
                        "new_labels": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "New labels to add to the thread.",
                        },
                        "remove_labels": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Labels to remove from the thread.",
                        },
                        "update_recipients": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "New list of recipients for the thread.",
                        },
                        "status_notes": {
                            "type": "string",
                            "description": "Optional notes about the label update for tracking purposes.",
                        },
                    },
                    "required": ["thread_id"],
                },
            },
        }


class UpdateReleaseStatus(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        release_id: str,
        new_status: str = None,
        release_metadata: dict[str, Any] = None,
        thread_id: str = None,
        version_notes: str = "",
        release_notes: str = None,
        updated_by: str = None
    ) -> str:
        # Support release_notes as alternative to version_notes
        if release_notes is not None:
            version_notes = release_notes
        """
        Changes release status and oversees release workflow metadata.
        """
        if release_metadata is None:
            release_metadata = {}

        if not all([release_id, new_status]):
            payload = {"error": "release_id and new_status are required."}
            out = json.dumps(payload)
            return out

        # Verify the correctness of status values
        valid_statuses = ["DRAFT", "IN_REVIEW", "APPROVED", "PUBLISHED", "ARCHIVED"]
        if new_status not in valid_statuses:
            payload = {
                "error": f"Invalid status. Must be one of: {', '.join(valid_statuses)}"
            }
            out = json.dumps(payload)
            return out

        releases = data.get("releases", {}).values()

        # Identify the release
        release_found = False
        for release in releases.values():
            if release.get("release_id") == release_id:
                release_found = True
                old_status = release.get("status", "DRAFT")

                # Change the status of the release
                release["status"] = new_status
                release["last_updated"] = datetime.now().isoformat()

                # Modify the association of the thread
                if thread_id:
                    release["thread_id_nullable"] = thread_id

                # Include notes about the version
                if version_notes:
                    if "version_history" not in release:
                        release["version_history"] = []
                    release["version_history"].append(
                        {
                            "timestamp": datetime.now().isoformat(),
                            "status": new_status,
                            "notes": version_notes,
                        }
                    )

                # Revise metadata
                if release_metadata:
                    for key, value in release_metadata.items():
                        release[key] = value

                # Document the status change
                if "status_history" not in release:
                    release["status_history"] = []
                release["status_history"].append(
                    {
                        "from_status": old_status,
                        "to_status": new_status,
                        "changed_at": datetime.now().isoformat(),
                        "notes": version_notes,
                    }
                )

                break

        if not release_found:
            payload = {"error": f"Release with ID '{release_id}' not found."}
            out = json.dumps(payload)
            return out
        payload = {
            "success": True,
            "release_id": release_id,
            "old_status": old_status,
            "new_status": new_status,
            "updated_at": datetime.now().isoformat(),
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateReleaseStatus",
                "description": "Updates release status and manages release workflow metadata including version notes and thread associations.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "release_id": {
                            "type": "string",
                            "description": "The ID of the release to update.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new status for the release. Must be one of: DRAFT, IN_REVIEW, APPROVED, PUBLISHED, ARCHIVED.",
                        },
                        "version_notes": {
                            "type": "string",
                            "description": "Optional notes about the version update or status change.",
                        },
                        "thread_id": {
                            "type": "string",
                            "description": "Optional Gmail thread ID to associate with the release.",
                        },
                        "release_metadata": {
                            "type": "object",
                            "description": "Additional metadata fields to update on the release.",
                        },
                    },
                    "required": ["release_id", "new_status"],
                },
            },
        }


class GetGmailThreadsByLabels(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        thread_id: str = None,
        labels: list[str] = [],
        sender_email: str = None,
        subject_keywords: list[str] = [],
        created_after: str = None,
        created_before: str = None
    ) -> str:
        """
        Obtains Gmail threads filtered by labels, sender, and additional criteria.
        """
        gmail_threads = data.get("gmail_threads", {}).values()

        # Return the specific thread if thread_id is given
        if thread_id:
            for thread in gmail_threads.values():
                if thread.get("thread_id") == thread_id:
                    payload = thread
                    out = json.dumps(payload, indent=2)
                    return out
            payload = {"error": f"Thread with ID '{thread_id}' not found."}
            out = json.dumps(payload)
            return out

        # Sort threads based on specified criteria
        results = []
        for thread in gmail_threads.values():
            # Implement filters
            if labels:
                thread_labels = thread.get("current_labels", [])
                if not any(label in thread_labels for label in labels.values()):
                    continue

            if sender_email:
                if thread.get("sender_identity") != sender_email:
                    continue

            if subject_keywords:
                subject = thread.get("subject", "").lower()
                if not any(keyword.lower() in subject for keyword in subject_keywords.values()):
                    continue

            # Enforce date filters
            if created_after:
                thread_created = thread.get("created_ts", "")
                if thread_created < created_after:
                    continue

            if created_before:
                thread_created = thread.get("created_ts", "")
                if thread_created > created_before:
                    continue

            results.append(thread)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetGmailThreadsByLabels",
                "description": "Retrieves Gmail threads filtered by labels, sender email, subject keywords, and date ranges for comprehensive email workflow management.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "thread_id": {
                            "type": "string",
                            "description": "The ID of a specific thread to retrieve.",
                        },
                        "labels": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Filter by thread labels (e.g., ['design-review', 'urgent']).",
                        },
                        "sender_email": {
                            "type": "string",
                            "description": "Filter by sender email address.",
                        },
                        "subject_keywords": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Filter by keywords in subject line.",
                        },
                        "created_after": {
                            "type": "string",
                            "description": "Filter threads created after this ISO timestamp.",
                        },
                        "created_before": {
                            "type": "string",
                            "description": "Filter threads created before this ISO timestamp.",
                        },
                    },
                },
            },
        }


class GetReleaseSummary(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        release_id: str = None,
        figma_file_id: str = None,
        owner_email: str = None,
        version_tag_pattern: str = None,
        status: str = None
    ) -> str:
        """
        Obtains detailed release information and metrics.
        """
        releases = data.get("releases", {}).values()
        gmail_threads = data.get("gmail_threads", {}).values()

        # Return the specific release if release_id is supplied
        if release_id:
            release_info = None
            for release in releases.values():
                if release.get("release_id") == release_id:
                    release_info = release
                    break

            if not release_info:
                payload = {"error": f"Release with ID '{release_id}' not found."}
                out = json.dumps(payload)
                return out

            # Enhance with details from the thread
            thread_id = release_info.get("thread_id_nullable")
            thread_info = None
            if thread_id:
                for thread in gmail_threads.values():
                    if thread.get("thread_id") == thread_id:
                        thread_info = thread
                        break

            summary = {"release_info": release_info, "thread_info": thread_info}
            payload = summary
            out = json.dumps(payload, indent=2)
            return out

        # Provide a summary for all releases
        all_releases = releases

        # Enforce filters
        if figma_file_id:
            all_releases = [
                r for r in all_releases if r.get("figma_file_id") == figma_file_id
            ]

        if owner_email:
            all_releases = [
                r for r in all_releases if r.get("owner_email") == owner_email
            ]

        if version_tag_pattern:
            all_releases = [
                r
                for r in all_releases
                if version_tag_pattern in r.get("version_tag", "")
            ]

        if status:
            all_releases = [r for r in all_releases.values() if r.get("status") == status]

        summary = {
            "total_releases": len(all_releases),
            "by_owner": {},
            "by_file": {},
            "by_status": {},
            "releases": all_releases,
        }

        # Categorize releases based on owner
        for release in all_releases:
            owner = release.get("owner_email")
            if owner not in summary["by_owner"]:
                summary["by_owner"][owner] = 0
            summary["by_owner"][owner] += 1

            # Classify by file
            file_id = release.get("figma_file_id")
            if file_id not in summary["by_file"]:
                summary["by_file"][file_id] = 0
            summary["by_file"][file_id] += 1

            # Categorize by status
            release_status = release.get("status", "DRAFT")
            if release_status not in summary["by_status"]:
                summary["by_status"][release_status] = 0
            summary["by_status"][release_status] += 1
        payload = summary
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetReleaseSummary",
                "description": "Retrieves comprehensive release information and metrics including owner distribution, file associations, and status breakdowns.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "release_id": {
                            "type": "string",
                            "description": "The ID of a specific release to retrieve details for.",
                        },
                        "figma_file_id": {
                            "type": "string",
                            "description": "Filter releases by Figma file ID.",
                        },
                        "owner_email": {
                            "type": "string",
                            "description": "Filter releases by owner email address.",
                        },
                        "version_tag_pattern": {
                            "type": "string",
                            "description": "Filter releases by version tag pattern (e.g., 'design-system').",
                        },
                        "status": {
                            "type": "string",
                            "description": "Filter releases by status (e.g., 'PUBLISHED', 'DRAFT').",
                        },
                    },
                },
            },
        }


class UpdateAssetExportStatus(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        asset_id: str,
        new_status: str,
        export_notes: str = "",
        notes: str = None,
        dlp_scan_status: str = None,
        storage_ref: str = None
    ) -> str:
        # Support 'notes' as an alternative to 'export_notes'
        if notes is not None:
            export_notes = notes
        """
        Modifies asset export status and oversees export workflow metadata.
        """
        if not all([asset_id, new_status]):
            payload = {"error": "asset_id and new_status are required."}
            out = json.dumps(payload)
            return out

        # Check the validity of status values
        valid_statuses = ["PENDING", "EXPORTING", "COMPLETED", "FAILED", "ARCHIVED"]
        if new_status not in valid_statuses:
            payload = {
                "error": f"Invalid status. Must be one of: {', '.join(valid_statuses)}"
            }
            out = json.dumps(payload)
            return out

        assets = data.get("assets", {}).values()

        # Locate the asset
        asset_found = False
        for asset in assets.values():
            if asset.get("asset_id") == asset_id:
                asset_found = True
                old_status = asset.get("export_status", "PENDING")

                # Change the status of the asset
                asset["export_status"] = new_status
                asset["last_updated"] = datetime.now().isoformat()

                # Modify DLP scan status if specified
                if dlp_scan_status:
                    asset["dlp_scan_status"] = dlp_scan_status
                    asset["dlp_scan_timestamp"] = datetime.now().isoformat()

                # Revise storage reference if supplied
                if storage_ref:
                    asset["storage_ref"] = storage_ref

                # Include notes regarding the export
                if export_notes:
                    if "export_history" not in asset:
                        asset["export_history"] = []
                    asset["export_history"].append(
                        {
                            "timestamp": datetime.now().isoformat(),
                            "status": new_status,
                            "notes": export_notes,
                        }
                    )

                # Document the change in status
                if "status_history" not in asset:
                    asset["status_history"] = []
                asset["status_history"].append(
                    {
                        "from_status": old_status,
                        "to_status": new_status,
                        "changed_at": datetime.now().isoformat(),
                        "notes": export_notes,
                    }
                )

                break

        if not asset_found:
            payload = {"error": f"Asset with ID '{asset_id}' not found."}
            out = json.dumps(payload)
            return out
        payload = {
            "success": True,
            "asset_id": asset_id,
            "old_status": old_status,
            "new_status": new_status,
            "updated_at": datetime.now().isoformat(),
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAssetExportStatus",
                "description": "Updates asset export status and manages export workflow metadata including DLP scan status and storage references.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_id": {
                            "type": "string",
                            "description": "The ID of the asset to update.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new export status. Must be one of: PENDING, EXPORTING, COMPLETED, FAILED, ARCHIVED.",
                        },
                        "export_notes": {
                            "type": "string",
                            "description": "Optional notes about the export process or status change.",
                        },
                        "dlp_scan_status": {
                            "type": "string",
                            "description": "Optional DLP scan status update (e.g., 'CLEAN', 'FLAGGED', 'PENDING').",
                        },
                        "storage_ref": {
                            "type": "string",
                            "description": "Optional new storage reference for the asset.",
                        },
                    },
                    "required": ["asset_id", "new_status"],
                },
            },
        }


class UpdateFigmaCommentStatus(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        comment_id: str,
        new_status: str,
        resolution_notes: str = "",
        assignee_email: str = None,
        priority_level: str = None,
        resolved_by: str = None
    ) -> str:
        # Support resolved_by as alternative to assignee_email
        if resolved_by is not None:
            assignee_email = resolved_by
        """
        Changes Figma comment status and oversees comment workflow.
        """
        if not all([comment_id, new_status]):
            payload = {"error": "comment_id and new_status are required."}
            out = json.dumps(payload)
            return out

        # Check the correctness of status values
        valid_statuses = ["OPEN", "IN_PROGRESS", "RESOLVED", "CLOSED", "ARCHIVED"]
        if new_status not in valid_statuses:
            payload = {
                "error": f"Invalid status. Must be one of: {', '.join(valid_statuses)}"
            }
            out = json.dumps(payload)
            return out

        figma_comments = data.get("figma_comments", {}).values()

        # Locate the comment
        comment_found = False
        for comment in figma_comments.values():
            if comment.get("comment_id") == comment_id:
                comment_found = True
                old_status = comment.get("comment_status", "OPEN")
                old_resolved = comment.get("resolved_flag", False)

                # Change the status of the comment
                comment["comment_status"] = new_status
                comment["last_updated"] = datetime.now().isoformat()

                # Modify the resolved flag according to status
                if new_status in ["RESOLVED", "CLOSED", "ARCHIVED"]:
                    comment["resolved_flag"] = True
                    comment["resolved_at"] = datetime.now().isoformat()
                else:
                    comment["resolved_flag"] = False

                # Revise assignee if specified
                if assignee_email:
                    comment["assignee_email"] = assignee_email
                elif "assignee_email" in comment:
                    del comment["assignee_email"]

                # Change priority if supplied
                if priority_level:
                    comment["priority_level"] = priority_level
                elif "priority_level" in comment:
                    del comment["priority_level"]

                # Include notes regarding the resolution
                if resolution_notes:
                    if "resolution_history" not in comment:
                        comment["resolution_history"] = []
                    comment["resolution_history"].append(
                        {
                            "timestamp": datetime.now().isoformat(),
                            "status": new_status,
                            "notes": resolution_notes,
                            "assignee": assignee_email,
                        }
                    )

                # Document the change in status
                if "status_history" not in comment:
                    comment["status_history"] = []
                comment["status_history"].append(
                    {
                        "from_status": old_status,
                        "to_status": new_status,
                        "resolved_changed": old_resolved != comment["resolved_flag"],
                        "changed_at": datetime.now().isoformat(),
                        "notes": resolution_notes,
                    }
                )

                break

        if not comment_found:
            payload = {"error": f"Comment with ID '{comment_id}' not found."}
            out = json.dumps(payload)
            return out
        payload = {
            "success": True,
            "comment_id": comment_id,
            "old_status": old_status,
            "new_status": new_status,
            "resolved_flag": comment["resolved_flag"],
            "updated_at": datetime.now().isoformat(),
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateFigmaCommentStatus",
                "description": "Updates Figma comment status and manages comment workflow including resolution tracking and assignment.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "comment_id": {
                            "type": "string",
                            "description": "The ID of the comment to update.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new comment status. Must be one of: OPEN, IN_PROGRESS, RESOLVED, CLOSED, ARCHIVED.",
                        },
                        "resolution_notes": {
                            "type": "string",
                            "description": "Optional notes about the resolution or status change.",
                        },
                        "assignee_email": {
                            "type": "string",
                            "description": "Optional email of the person assigned to handle the comment.",
                        },
                        "priority_level": {
                            "type": "string",
                            "description": "Optional priority level (e.g., 'LOW', 'MEDIUM', 'HIGH', 'CRITICAL').",
                        },
                    },
                    "required": ["comment_id", "new_status"],
                },
            },
        }


class GetAssetExportSummary(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        asset_id: str = None,
        artifact_id: str = None,
        export_profile: str = None,
        dlp_scan_status: str = None,
        created_after: str = None,
        created_before: str = None
    ) -> str:
        """
        Obtains detailed asset export information and metrics.
        """
        assets = data.get("assets", {}).values()
        figma_artifacts = data.get("figma_artifacts", {}).values()

        # Return the specific asset if asset_id is given
        if asset_id:
            asset_info = None
            for asset in assets.values():
                if asset.get("asset_id") == asset_id:
                    asset_info = asset
                    break

            if not asset_info:
                payload = {"error": f"Asset with ID '{asset_id}' not found."}
                out = json.dumps(payload)
                return out

            # Enhance with details from the artifact
            artifact_id_ref = asset_info.get("artifact_id_nullable")
            artifact_info = None
            if artifact_id_ref:
                for artifact in figma_artifacts.values():
                    if artifact.get("artifact_id") == artifact_id_ref:
                        artifact_info = artifact
                        break

            summary = {"asset_info": asset_info, "artifact_info": artifact_info}
            payload = summary
            out = json.dumps(payload, indent=2)
            return out

        # Provide a summary for all assets
        all_assets = assets

        # Implement filters
        if artifact_id:
            all_assets = [
                a for a in all_assets if a.get("artifact_id_nullable") == artifact_id
            ]

        if export_profile:
            all_assets = [
                a for a in all_assets if a.get("export_profile") == export_profile
            ]

        if dlp_scan_status:
            all_assets = [
                a for a in all_assets if a.get("dlp_scan_status") == dlp_scan_status
            ]

        # Enforce date filters
        if created_after:
            all_assets = [
                a for a in all_assets if a.get("created_ts", "") >= created_after
            ]

        if created_before:
            all_assets = [
                a for a in all_assets if a.get("created_ts", "") <= created_before
            ]

        summary = {
            "total_assets": len(all_assets),
            "by_profile": {},
            "by_artifact": {},
            "by_dlp_status": {},
            "total_file_size_bytes": sum(
                a.get("file_size_bytes", 0) for a in all_assets
            ),
            "assets": all_assets,
        }

        # Categorize assets based on profile
        for asset in all_assets:
            profile = asset.get("export_profile")
            if profile not in summary["by_profile"]:
                summary["by_profile"][profile] = 0
            summary["by_profile"][profile] += 1

            # Classify by artifact
            artifact_ref = asset.get("artifact_id_nullable")
            if artifact_ref not in summary["by_artifact"]:
                summary["by_artifact"][artifact_ref] = 0
            summary["by_artifact"][artifact_ref] += 1

            # Categorize by DLP status
            dlp_status = asset.get("dlp_scan_status", "UNKNOWN")
            if dlp_status not in summary["by_dlp_status"]:
                summary["by_dlp_status"][dlp_status] = 0
            summary["by_dlp_status"][dlp_status] += 1
        payload = summary
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAssetExportSummary",
                "description": "Retrieves comprehensive asset export information and metrics including profile distribution, artifact associations, and DLP scan status breakdowns.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_id": {
                            "type": "string",
                            "description": "The ID of a specific asset to retrieve details for.",
                        },
                        "artifact_id": {
                            "type": "string",
                            "description": "Filter assets by associated artifact ID.",
                        },
                        "export_profile": {
                            "type": "string",
                            "description": "Filter assets by export profile (e.g., 'PNG 2x', 'SVG', 'PDF').",
                        },
                        "dlp_scan_status": {
                            "type": "string",
                            "description": "Filter assets by DLP scan status (e.g., 'CLEAN', 'FLAGGED', 'PENDING').",
                        },
                        "created_after": {
                            "type": "string",
                            "description": "Filter assets created after this ISO timestamp.",
                        },
                        "created_before": {
                            "type": "string",
                            "description": "Filter assets created before this ISO timestamp.",
                        },
                    },
                },
            },
        }


class GetFigmaCommentsByArtifact(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        comment_id: str = None,
        artifact_id: str = None,
        author_email: str = None,
        resolved_status: bool = None,
        content_keywords: list[str] = [],
        created_after: str = None,
        created_before: str = None
    ) -> str:
        """
        Obtains Figma comments filtered by artifact, author, and additional criteria.
        """
        figma_comments = data.get("figma_comments", {}).values()

        # Return the specific comment if comment_id is supplied
        if comment_id:
            for comment in figma_comments.values():
                if comment.get("comment_id") == comment_id:
                    payload = comment
                    out = json.dumps(payload, indent=2)
                    return out
            payload = {"error": f"Comment with ID '{comment_id}' not found."}
            out = json.dumps(payload)
            return out

        # Sort comments based on specified criteria
        results = []
        for comment in figma_comments.values():
            # Implement filters
            if artifact_id:
                if comment.get("artifact_id") != artifact_id:
                    continue

            if author_email:
                if comment.get("author_email") != author_email:
                    continue

            if resolved_status is not None:
                if comment.get("resolved_flag") != resolved_status:
                    continue

            if content_keywords:
                content = comment.get("content", "").lower()
                if not any(keyword.lower() in content for keyword in content_keywords.values()):
                    continue

            # Enforce date filters
            if created_after:
                comment_created = comment.get("created_ts", "")
                if comment_created < created_after:
                    continue

            if created_before:
                comment_created = comment.get("created_ts", "")
                if comment_created > created_before:
                    continue

            results.append(comment)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetFigmaCommentsByArtifact",
                "description": "Retrieves Figma comments filtered by artifact ID, author email, resolution status, content keywords, and date ranges for comprehensive comment management.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "comment_id": {
                            "type": "string",
                            "description": "The ID of a specific comment to retrieve.",
                        },
                        "artifact_id": {
                            "type": "string",
                            "description": "Filter comments by associated artifact ID.",
                        },
                        "author_email": {
                            "type": "string",
                            "description": "Filter comments by resolution status (true for resolved, false for unresolved).",
                        },
                        "resolved_status": {
                            "type": "boolean",
                            "description": "Filter comments by resolution status (true for resolved, false for unresolved).",
                        },
                        "content_keywords": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Filter comments by keywords in the content.",
                        },
                        "created_after": {
                            "type": "string",
                            "description": "Filter comments created after this ISO timestamp.",
                        },
                        "created_before": {
                            "type": "string",
                            "description": "Filter comments created before this ISO timestamp.",
                        },
                    },
                },
            },
        }


class UpdateSystemConfig(Tool):
    def invoke(
        data: dict[str, Any],
        config_key: str,
        config_category: str = None,
        config_value_json: str = None,
        description: str = ""
    ) -> str:
        """
        Modifies system configuration values for managing workflows.
        """
        if not all([config_key, config_value_json]):
            payload = {"error": "config_key and config_value_json are required."}
            out = json.dumps(
                payload)
            return out

        system_config = data.get("system_config", {}).values()

        # Locate existing configuration or generate a new one
        config_found = False
        for config in system_config.values():
            if config.get("config_key") == config_key:
                config_found = True
                old_value = config.get("config_value_json")

                # Revise configuration
                config["config_value_json"] = config_value_json
                config["last_updated"] = datetime.now().isoformat()

                # Include optional fields
                if description:
                    config["description"] = description
                if config_category:
                    config["category"] = config_category

                # Document the change
                if "change_history" not in config:
                    config["change_history"] = []
                config["change_history"].append(
                    {
                        "timestamp": datetime.now().isoformat(),
                        "old_value": old_value,
                        "new_value": config_value_json,
                        "change_description": description,
                    }
                )

                break

        # Generate a new configuration if none exists
        if not config_found:
            new_config = {
                "config_key": config_key,
                "config_value_json": config_value_json,
                "created_at": datetime.now().isoformat(),
                "last_updated": datetime.now().isoformat(),
            }

            if description:
                new_config["description"] = description
            if config_category:
                new_config["category"] = config_category

            new_config["change_history"] = [
                {
                    "timestamp": datetime.now().isoformat(),
                    "old_value": None,
                    "new_value": config_value_json,
                    "change_description": f"Created new config: {description}",
                }
            ]

            data["system_config"][new_config["system_config_id"]] = new_config
        payload = {
                "success": True,
                "config_key": config_key,
                "updated_at": datetime.now().isoformat(),
                "action": "updated" if config_found else "created",
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateSystemConfig",
                "description": "Updates system configuration values for workflow management including design system mappings, email templates, and SLA settings.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "config_key": {
                            "type": "string",
                            "description": "The configuration key to update (e.g., 'design_system_aliases', 'email_templates').",
                        },
                        "config_value_json": {
                            "type": "string",
                            "description": "The JSON string value for the configuration.",
                        },
                        "description": {
                            "type": "string",
                            "description": "Optional description of the configuration change.",
                        },
                        "config_category": {
                            "type": "string",
                            "description": "Optional category for the configuration (e.g., 'workflow', 'email', 'system').",
                        },
                    },
                    "required": ["config_key", "config_value_json"],
                },
            },
        }


class UpdateTerminalLogLevel(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        message: str,
        log_level: str = "INFO",
        source_component: str = None,
        workflow_id: str = None,
        max_log_entries: int = 1000
    ) -> str:
        """
        Includes new terminal log entries and oversees log retention.
        """
        if not message:
            payload = {"error": "message is required."}
            out = json.dumps(payload)
            return out

        # Check the correctness of log level
        valid_levels = ["DEBUG", "INFO", "WARN", "ERROR", "CRITICAL"]
        if log_level not in valid_levels:
            payload = {
                "error": f"Invalid log_level. Must be one of: {', '.join(valid_levels)}"
            }
            out = json.dumps(payload)
            return out

        terminal_logs = data.get("terminal_logs", {}).values()

        # Generate a new log entry
        new_log_entry = {
            "log_ts": datetime.now().isoformat(),
            "message": f"{log_level}: {message}",
            "level": log_level,
            "component": source_component,
            "workflow_id": workflow_id,
        }

        # Include entry in logs
        data["terminal_logs"][new_log_entry["terminal_log_id"]] = new_log_entry

        # Enforce log retention by retaining only the latest entries
        if len(terminal_logs) > max_log_entries:
            # Order by timestamp and retain the latest
            terminal_logs.sort(key=lambda x: x.get("log_ts", ""))
            # Eliminate the oldest entries
            excess_count = len(terminal_logs) - max_log_entries
            for _ in range(excess_count):
                terminal_logs.pop(0)
        payload = {
            "success": True,
            "log_entry": new_log_entry,
            "total_log_entries": len(terminal_logs),
            "logged_at": datetime.now().isoformat(),
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateTerminalLogLevel",
                "description": "Adds new terminal log entries with specified log levels and manages log retention for workflow tracking and debugging.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "message": {
                            "type": "string",
                            "description": "The log message to add.",
                        },
                        "log_level": {
                            "type": "string",
                            "description": "The log level. Must be one of: DEBUG, INFO, WARN, ERROR, CRITICAL.",
                        },
                        "source_component": {
                            "type": "string",
                            "description": "Optional component or service generating the log entry.",
                        },
                        "workflow_id": {
                            "type": "string",
                            "description": "Optional workflow ID to associate with the log entry.",
                        },
                        "max_log_entries": {
                            "type": "integer",
                            "description": "Maximum number of log entries to retain (default: 1000).",
                        },
                    },
                    "required": ["message"],
                },
            },
        }


class GetSystemConfigByCategory(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], 
        config_key: str = None, 
        config_category: str = None,
        category: str = None,
        key_pattern: str = None, 
        include_history: bool = False
    ) -> str:
        # Support 'category' as an alternative to 'config_category'
        if category is not None:
            config_category = category
        """
        Obtains system configuration entries filtered by category and key patterns.
        """
        system_config = data.get("system_config", {}).values()

        # Return the specific configuration if config_key is supplied
        if config_key:
            for config in system_config.values():
                if config.get("config_key") == config_key:
                    config_copy = config.copy()
                    if not include_history and "change_history" in config_copy:
                        del config_copy["change_history"]
                    payload = config_copy
                    out = json.dumps(payload, indent=2)
                    return out
            payload = {"error": f"Config with key '{config_key}' not found."}
            out = json.dumps(payload)
            return out

        # Sort configurations based on specified criteria
        results = []
        for config in system_config.values():
            # Implement filters
            if config_category:
                if config.get("category") != config_category:
                    continue

            if key_pattern:
                if key_pattern.lower() not in config.get("config_key", "").lower():
                    continue

            config_copy = config.copy()
            if not include_history and "change_history" in config_copy:
                del config_copy["change_history"]

            results.append(config_copy)

        # Categorize results for summary
        summary = {"total_configs": len(results), "by_category": {}, "configs": results}

        for config in results:
            category = config.get("category", "uncategorized")
            if category not in summary["by_category"]:
                summary["by_category"][category] = 0
            summary["by_category"][category] += 1
        payload = summary
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSystemConfigByCategory",
                "description": "Retrieves system configuration entries filtered by category, key patterns, and optionally includes change history for workflow management.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "config_key": {
                            "type": "string",
                            "description": "The specific configuration key to retrieve.",
                        },
                        "config_category": {
                            "type": "string",
                            "description": "Filter configurations by category (e.g., 'workflow', 'email', 'system').",
                        },
                        "key_pattern": {
                            "type": "string",
                            "description": "Filter configurations by key pattern (e.g., 'email' to find email-related configs).",
                        },
                        "include_history": {
                            "type": "boolean",
                            "description": "Include change history in the results (default: false).",
                        },
                    },
                },
            },
        }


class GetTerminalLogsSummary(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        log_level: str = None,
        source_component: str = None,
        component: str = None,
        workflow_id: str = None,
        message_keywords: list[str] = [],
        created_after: str = None,
        created_before: str = None,
        limit: int = 100
    ) -> str:
        # Support 'component' as an alternative to 'source_component'
        if component is not None:
            source_component = component
        """
        Obtains terminal logs with filtering and summarization features.
        """
        terminal_logs = data.get("terminal_logs", {}).values()

        # Sort logs based on specified criteria
        results = []
        for log in terminal_logs.values():
            # Implement filters
            if log_level:
                log_message = log.get("message", "")
                if not log_message.startswith(f"{log_level}:"):
                    continue

            if source_component:
                if log.get("component") != source_component:
                    continue

            if workflow_id:
                if log.get("workflow_id") != workflow_id:
                    continue

            if message_keywords:
                message = log.get("message", "").lower()
                if not any(keyword.lower() in message for keyword in message_keywords.values()):
                    continue

            # Enforce date filters
            if created_after:
                log_ts = log.get("log_ts", "")
                if log_ts < created_after:
                    continue

            if created_before:
                log_ts = log.get("log_ts", "")
                if log_ts > created_before:
                    continue

            results.append(log)

        # Order by timestamp (latest first) and enforce limit
        results.sort(key=lambda x: x.get("log_ts", ""), reverse=True)
        if limit:
            results = results[:limit]

        # Generate a summary showing log level distribution
        summary = {
            "total_matching_logs": len(results),
            "by_level": {},
            "by_component": {},
            "by_workflow": {},
            "logs": results,
        }

        for log in results:
            # Retrieve log level from the message
            message = log.get("message", "")
            level = "UNKNOWN"
            for lvl in ["DEBUG", "INFO", "WARN", "ERROR", "CRITICAL"]:
                if message.startswith(f"{lvl}:"):
                    level = lvl
                    break

            if level not in summary["by_level"]:
                summary["by_level"][level] = 0
            summary["by_level"][level] += 1

            # Categorize by component
            component = log.get("component", "unknown")
            if component not in summary["by_component"]:
                summary["by_component"][component] = 0
            summary["by_component"][component] += 1

            # Classify by workflow
            workflow = log.get("workflow_id", "unknown")
            if workflow not in summary["by_workflow"]:
                summary["by_workflow"][workflow] = 0
            summary["by_workflow"][workflow] += 1
        payload = summary
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTerminalLogsSummary",
                "description": "Retrieves terminal logs with filtering and summarization capabilities including log level distribution, component breakdown, and workflow tracking.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "log_level": {
                            "type": "string",
                            "description": "Filter logs by level (e.g., 'INFO', 'ERROR', 'WARN').",
                        },
                        "source_component": {
                            "type": "string",
                            "description": "Filter logs by source component or service.",
                        },
                        "workflow_id": {
                            "type": "string",
                            "description": "Filter logs by workflow ID.",
                        },
                        "message_keywords": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Filter logs by keywords in the message content.",
                        },
                        "created_after": {
                            "type": "string",
                            "description": "Filter logs created after this ISO timestamp.",
                        },
                        "created_before": {
                            "type": "string",
                            "description": "Filter logs created before this ISO timestamp.",
                        },
                        "limit": {
                            "type": "integer",
                            "description": "Maximum number of log entries to return (default: 100).",
                        },
                    },
                },
            },
        }


class UpdateGmailMessageStatus(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        message_id: str = None,
        sender_email: str = None,
        body_html: str = None,
        body_text_stripped: str = None,
        attachments_asset_ids: list = None,
        message_metadata: dict = None,
        new_status: str = None,
        updated_by: str = None
    ) -> str:
        """
        Modifies Gmail message metadata and oversees message workflow tracking.
        """
        if attachments_asset_ids is None:
            attachments_asset_ids = []
        if message_metadata is None:
            message_metadata = {}

        if not message_id:
            payload = {"error": "message_id is required."}
            out = json.dumps(payload)
            return out

        gmail_messages = data.get("gmail_messages", {}).values()

        # Locate the message
        message_found = False
        for message in gmail_messages.values():
            if message.get("message_id") == message_id:
                message_found = True

                # Revise fields of the message
                if sender_email:
                    message["sender_email"] = sender_email
                if body_html:
                    message["body_html"] = body_html
                if body_text_stripped:
                    message["body_text_stripped"] = body_text_stripped
                if attachments_asset_ids:
                    message["attachments_asset_ids"] = attachments_asset_ids

                message["last_updated"] = datetime.now().isoformat()

                # Include metadata
                if message_metadata:
                    for key, value in message_metadata.items():
                        message[key] = value

                # Document the update
                if "update_history" not in message:
                    message["update_history"] = []
                message["update_history"].append(
                    {
                        "timestamp": datetime.now().isoformat(),
                        "updated_fields": [
                            "message_id",
                            "sender_email",
                            "body_html",
                            "body_text_stripped",
                            "attachments_asset_ids",
                            "message_metadata",
                        ],
                        "metadata": message_metadata,
                    }
                )

                break

        if not message_found:
            payload = {"error": f"Gmail message with ID '{message_id}' not found."}
            out = json.dumps(payload)
            return out

        payload = {
            "success": True,
            "message_id": message_id,
            "updated_at": datetime.now().isoformat(),
            "updated_fields": [
                "message_id",
                "sender_email",
                "body_html",
                "body_text_stripped",
                "attachments_asset_ids",
                "message_metadata",
            ],
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateGmailMessageStatus",
                "description": "Updates Gmail message metadata including sender, body content, attachments, and custom metadata for message workflow tracking.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "message_id": {
                            "type": "string",
                            "description": "The ID of the Gmail message to update.",
                        },
                        "sender_email": {
                            "type": "string",
                            "description": "Optional updated sender email address.",
                        },
                        "body_html": {
                            "type": "string",
                            "description": "Optional updated HTML body content.",
                        },
                        "body_text_stripped": {
                            "type": "string",
                            "description": "Optional updated plain text body content.",
                        },
                        "attachments_asset_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Optional updated list of attachment asset IDs.",
                        },
                        "message_metadata": {
                            "type": "object",
                            "description": "Optional additional metadata fields for the message.",
                        },
                    },
                    "required": ["message_id"],
                },
            },
        }


class UpdateFixPlanStatus(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        plan_id: str = None,
        new_status: str = None,
        owner_email: str = None,
        delivery_method: str = None,
        delivery_notes: str = "",
        notes: str = None
    ) -> str:
        # Support notes as alternative to delivery_notes
        if notes is not None:
            delivery_notes = notes
        """
        Changes fix plan status and oversees the lifecycle workflow of the fix plan.
        """
        if not all([plan_id, new_status]):
            payload = {"error": "plan_id and new_status are required."}
            out = json.dumps(payload)
            return out

        # Check the validity of status values
        valid_statuses = ["DRAFTED", "IN_PROGRESS", "DELIVERED", "ARCHIVED"]
        if new_status not in valid_statuses:
            payload = {
                "error": f"Invalid status. Must be one of: {', '.join(valid_statuses)}"
            }
            out = json.dumps(payload)
            return out

        # Check the correctness of delivery method if specified
        valid_delivery_methods = ["COMMENTS", "TICKETS", "PDF"]
        if delivery_method and delivery_method not in valid_delivery_methods:
            payload = {
                "error": f"Invalid delivery_method. Must be one of: {', '.join(valid_delivery_methods)}"
            }
            out = json.dumps(payload)
            return out

        fix_plans = data.get("fix_plans", {}).values()

        # Locate the fix plan
        plan_found = False
        for plan in fix_plans.values():
            if plan.get("plan_id") == plan_id:
                plan_found = True
                old_status = plan.get("status")

                # Change the status of the plan
                plan["status"] = new_status
                plan["last_updated"] = datetime.now().isoformat()

                # Revise owner if specified
                if owner_email:
                    plan["owner_email"] = owner_email

                # Change delivery method if supplied
                if delivery_method:
                    plan["delivery_method"] = delivery_method

                # Manage logic based on status
                if new_status == "DELIVERED":
                    plan["delivered_at"] = datetime.now().isoformat()
                    if delivery_notes:
                        plan["delivery_notes"] = delivery_notes

                elif new_status == "ARCHIVED":
                    plan["archived_at"] = datetime.now().isoformat()
                    if delivery_notes:
                        plan["archive_reason"] = delivery_notes

                # Document the change in status
                if "status_history" not in plan:
                    plan["status_history"] = []
                plan["status_history"].append(
                    {
                        "from_status": old_status,
                        "to_status": new_status,
                        "changed_at": datetime.now().isoformat(),
                        "notes": delivery_notes,
                        "delivery_method": delivery_method,
                    }
                )

                break

        if not plan_found:
            payload = {"error": f"Fix plan with ID '{plan_id}' not found."}
            out = json.dumps(payload)
            return out
        payload = {
            "success": True,
            "plan_id": plan_id,
            "old_status": old_status,
            "new_status": new_status,
            "updated_at": datetime.now().isoformat(),
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateFixPlanStatus",
                "description": "Updates fix plan status and manages fix plan lifecycle workflow including delivery method and ownership tracking.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {
                            "type": "string",
                            "description": "The ID of the fix plan to update.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new status for the fix plan. Must be one of: DRAFTED, IN_PROGRESS, DELIVERED, ARCHIVED.",
                        },
                        "owner_email": {
                            "type": "string",
                            "description": "Optional updated owner email address.",
                        },
                        "delivery_method": {
                            "type": "string",
                            "description": "Optional delivery method. Must be one of: COMMENTS, TICKETS, PDF.",
                        },
                        "delivery_notes": {
                            "type": "string",
                            "description": "Optional notes about the delivery or status change.",
                        },
                    },
                    "required": ["plan_id", "new_status"],
                },
            },
        }


class GetGmailMessagesByThread(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        message_id: str = None,
        thread_id: str = None,
        sender_email: str = None,
        content_keywords: list[str] = [],
        has_attachments: bool = None,
        sent_after: str = None,
        sent_before: str = None
    ) -> str:
        """
        Obtains Gmail messages filtered by thread ID, sender, and additional criteria.
        """
        gmail_messages = data.get("gmail_messages", {}).values()

        # Return the specific message if message_id is given
        if message_id:
            for message in gmail_messages.values():
                if message.get("message_id") == message_id:
                    payload = message
                    out = json.dumps(payload, indent=2)
                    return out
            payload = {"error": f"Message with ID '{message_id}' not found."}
            out = json.dumps(payload)
            return out

        # Sort messages based on specified criteria
        results = []
        for message in gmail_messages.values():
            # Implement filters
            if thread_id:
                if message.get("thread_id") != thread_id:
                    continue

            if sender_email:
                if message.get("sender_email") != sender_email:
                    continue

            if content_keywords:
                content = message.get("body_text_stripped", "").lower()
                if not any(keyword.lower() in content for keyword in content_keywords.values()):
                    continue

            if has_attachments is not None:
                attachments = message.get("attachments_asset_ids", [])
                if has_attachments and not attachments:
                    continue
                if not has_attachments and attachments:
                    continue

            # Enforce date filters
            if sent_after:
                sent_ts = message.get("sent_ts", "")
                if sent_ts < sent_after:
                    continue

            if sent_before:
                sent_ts = message.get("sent_ts", "")
                if sent_ts > sent_before:
                    continue

            results.append(message)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getGmailMessagesByThread",
                "description": "Retrieves Gmail messages filtered by thread ID, sender email, content keywords, attachment status, and date ranges for comprehensive message management.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "message_id": {
                            "type": "string",
                            "description": "The ID of a specific message to retrieve.",
                        },
                        "thread_id": {
                            "type": "string",
                            "description": "Filter messages by thread ID.",
                        },
                        "sender_email": {
                            "type": "string",
                            "description": "Filter messages by sender email address.",
                        },
                        "content_keywords": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Filter messages by keywords in the content.",
                        },
                        "has_attachments": {
                            "type": "boolean",
                            "description": "Filter messages by attachment presence (true for messages with attachments, false for without).",
                        },
                        "sent_after": {
                            "type": "string",
                            "description": "Filter messages sent after this ISO timestamp.",
                        },
                        "sent_before": {
                            "type": "string",
                            "description": "Filter messages sent before this ISO timestamp.",
                        },
                    },
                },
            },
        }


class GetReleaseDiffSummary(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        diff_id: str = None,
        release_id: str = None,
        component_filter: str = None,
        change_type: str = None,
        include_changelog: bool = True
    ) -> str:
        """
        Obtains release diff information and summaries of changes between releases.
        """
        release_diffs = data.get("release_diffs", {}).values()
        releases = data.get("releases", {}).values()

        # Return the specific diff if diff_id is supplied
        if diff_id:
            diff_info = None
            for diff in release_diffs.values():
                if diff.get("diff_id") == diff_id:
                    diff_info = diff
                    break

            if not diff_info:
                payload = {"error": f"Release diff with ID '{diff_id}' not found."}
                out = json.dumps(payload)
                return out

            # Enhance with details from the release
            release_info = None
            for release in releases.values():
                if release.get("release_id") == diff_info.get("release_id"):
                    release_info = release
                    break

            summary = {
                "diff_info": diff_info,
                "release_info": release_info,
                "change_summary": {
                    "frames_added": len(diff_info.get("frames_added", [])),
                    "frames_updated": len(diff_info.get("frames_updated", [])),
                    "frames_removed": len(diff_info.get("frames_removed", [])),
                    "component_versions": len(
                        diff_info.get("component_version_bumps", [])
                    ),
                },
            }
            payload = summary
            out = json.dumps(payload, indent=2)
            return out

        # Sort diffs based on specified criteria
        results = []
        for diff in release_diffs.values():
            # Implement filters
            if release_id:
                if diff.get("release_id") != release_id:
                    continue

            if component_filter:
                components = diff.get("component_version_bumps", [])
                if not any(
                    component_filter.lower() in comp.lower() for comp in components
                ):
                    continue

            if change_type:
                if change_type == "added" and not diff.get("frames_added", []):
                    continue
                elif change_type == "updated" and not diff.get("frames_updated", []):
                    continue
                elif change_type == "removed" and not diff.get("frames_removed", []):
                    continue

            # Enhance with a summary of changes
            diff_copy = diff.copy()
            diff_copy["change_summary"] = {
                "frames_added": len(diff.get("frames_added", [])),
                "frames_updated": len(diff.get("frames_updated", [])),
                "frames_removed": len(diff.get("frames_removed", [])),
                "component_versions": len(diff.get("component_version_bumps", [])),
            }

            if not include_changelog:
                diff_copy.pop("changelog_highlights", None)

            results.append(diff_copy)

        summary = {
            "total_diffs": len(results),
            "aggregate_changes": {
                "total_frames_added": sum(
                    len(d.get("frames_added", [])) for d in results
                ),
                "total_frames_updated": sum(
                    len(d.get("frames_updated", [])) for d in results
                ),
                "total_frames_removed": sum(
                    len(d.get("frames_removed", [])) for d in results
                ),
                "total_component_bumps": sum(
                    len(d.get("component_version_bumps", [])) for d in results
                ),
            },
            "diffs": results,
        }
        payload = summary
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetReleaseDiffSummary",
                "description": "Retrieves release diff information and change summaries between releases including frame changes, component updates, and changelog highlights.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "diff_id": {
                            "type": "string",
                            "description": "The ID of a specific release diff to retrieve.",
                        },
                        "release_id": {
                            "type": "string",
                            "description": "Filter diffs by associated release ID.",
                        },
                        "component_filter": {
                            "type": "string",
                            "description": "Filter diffs by component name pattern (e.g., 'Button' to find button-related changes).",
                        },
                        "change_type": {
                            "type": "string",
                            "description": "Filter diffs by change type ('added', 'updated', or 'removed').",
                        },
                        "include_changelog": {
                            "type": "boolean",
                            "description": "Include changelog highlights in the results (default: true).",
                        },
                    },
                },
            },
        }


class UpdateAuditReportStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], audit_id: str = None, new_status: str = None, report_asset_id: str = None, completion_notes: str = "") -> str:
        """
        Modifies audit report status and oversees the workflow for audit completion.
        """
        if not all([audit_id, new_status]):
            payload = {"error": "audit_id and new_status are required."}
            out = json.dumps(payload)
            return out

        # Check the correctness of status values
        valid_statuses = ["RUNNING", "COMPLETED", "FAILED", "CANCELLED"]
        if new_status not in valid_statuses:
            payload = {
                "error": f"Invalid status. Must be one of: {', '.join(valid_statuses)}"
            }
            out = json.dumps(payload)
            return out

        audits = data.get("audits", {}).values()

        # Locate the audit
        audit_found = False
        for audit in audits.values():
            if audit.get("audit_id") == audit_id:
                audit_found = True
                old_status = audit.get("status")

                # Change the status of the audit
                audit["status"] = new_status
                audit["last_updated"] = datetime.now().isoformat()

                # Manage logic based on status
                if new_status == "COMPLETED":
                    audit["completed_at"] = datetime.now().isoformat()
                    if report_asset_id:
                        audit["report_asset_id_nullable"] = report_asset_id

                elif new_status == "FAILED":
                    audit["failed_at"] = datetime.now().isoformat()
                    if completion_notes:
                        audit["failure_reason"] = completion_notes

                # Document the change in status
                if "status_history" not in audit:
                    audit["status_history"] = []
                audit["status_history"].append(
                    {
                        "from_status": old_status,
                        "to_status": new_status,
                        "changed_at": datetime.now().isoformat(),
                        "notes": completion_notes,
                    }
                )

                break

        if not audit_found:
            payload = {"error": f"Audit with ID '{audit_id}' not found."}
            out = json.dumps(payload)
            return out
        payload = {
            "success": True,
            "audit_id": audit_id,
            "old_status": old_status,
            "new_status": new_status,
            "updated_at": datetime.now().isoformat(),
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAuditReportStatus",
                "description": "Updates audit report status and manages audit completion workflow including report asset associations.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {
                            "type": "string",
                            "description": "The ID of the audit to update.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new status for the audit. Must be one of: RUNNING, COMPLETED, FAILED, CANCELLED.",
                        },
                        "report_asset_id": {
                            "type": "string",
                            "description": "Optional asset ID for the generated report.",
                        },
                        "completion_notes": {
                            "type": "string",
                            "description": "Optional notes about the completion or failure.",
                        },
                    },
                    "required": ["audit_id", "new_status"],
                },
            },
        }


class UpdateGmailThreadPriority(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], thread_id: str = None, new_priority: str = None, urgency_reason: str = "", escalate_to: list = []) -> str:
        """
        Changes Gmail thread priority and oversees the urgency of thread workflow.
        """
        if not all([thread_id, new_priority]):
            payload = {"error": "thread_id and new_priority are required."}
            out = json.dumps(payload)
            return out

        # Check the correctness of priority values
        valid_priorities = ["LOW", "NORMAL", "HIGH", "URGENT", "CRITICAL"]
        if new_priority not in valid_priorities:
            payload = {
                "error": f"Invalid priority. Must be one of: {', '.join(valid_priorities)}"
            }
            out = json.dumps(payload)
            return out

        gmail_threads = data.get("gmail_threads", {}).values()

        # Locate the thread
        thread_found = False
        for thread in gmail_threads.values():
            if thread.get("thread_id") == thread_id:
                thread_found = True
                old_priority = thread.get("priority", "NORMAL")

                # Change the priority of the thread
                thread["priority"] = new_priority
                thread["updated_ts"] = datetime.now().isoformat()

                # Manage logic for high priority
                if new_priority in ["HIGH", "URGENT", "CRITICAL"]:
                    thread["escalated_at"] = datetime.now().isoformat()
                    if urgency_reason:
                        thread["urgency_reason"] = urgency_reason
                    if escalate_to:
                        # Include escalation recipients with current recipients
                        current_recipients = thread.get("recipients", [])
                        for recipient in escalate_to:
                            if recipient not in current_recipients:
                                current_recipients.append(recipient)
                        thread["recipients"] = current_recipients

                # Document the change in priority
                if "priority_history" not in thread:
                    thread["priority_history"] = []
                thread["priority_history"].append(
                    {
                        "from_priority": old_priority,
                        "to_priority": new_priority,
                        "changed_at": datetime.now().isoformat(),
                        "reason": urgency_reason,
                    }
                )

                break

        if not thread_found:
            payload = {"error": f"Gmail thread with ID '{thread_id}' not found."}
            out = json.dumps(payload)
            return out
        payload = {
            "success": True,
            "thread_id": thread_id,
            "old_priority": old_priority,
            "new_priority": new_priority,
            "updated_at": datetime.now().isoformat(),
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateGmailThreadPriority",
                "description": "Updates Gmail thread priority and manages thread workflow urgency including escalation to additional recipients.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "thread_id": {
                            "type": "string",
                            "description": "The ID of the Gmail thread to update.",
                        },
                        "new_priority": {
                            "type": "string",
                            "description": "The new priority level. Must be one of: LOW, NORMAL, HIGH, URGENT, CRITICAL.",
                        },
                        "urgency_reason": {
                            "type": "string",
                            "description": "Optional reason for the priority change.",
                        },
                        "escalate_to": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Optional list of additional recipients to escalate to for high priority threads.",
                        },
                    },
                    "required": ["thread_id", "new_priority"],
                },
            },
        }


#New tool 1: Modify Audit Status
class UpdateAuditStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], audit_id: str = None, new_status: str = None, notes: str = "") -> str:
        """
        Modifies the status of an audit and oversees the state of the audit workflow.
        """
        if not audit_id or not new_status:
            payload = {"error": "audit_id and new_status are required"}
            out = json.dumps(payload)
            return out

        audits = data.get("audits", {}).values()
        for audit in audits.values():
            if audit.get("audit_id") == audit_id:
                old_status = audit.get("status")
                audit["status"] = new_status
                audit["last_updated"] = datetime.now().isoformat()

                # Include in audit history if it doesn't already exist
                if "history" not in audit:
                    audit["history"] = []
                audit["history"].append(
                    {
                        "timestamp": datetime.now().isoformat(),
                        "status": new_status,
                        "notes": notes,
                    }
                )
                payload = {
                    "success": True,
                    "audit_id": audit_id,
                    "old_status": old_status,
                    "new_status": new_status,
                    "updated_at": datetime.now().isoformat(),
                }
                out = json.dumps(payload)
                return out
        payload = {"error": f"Audit with ID {audit_id} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAuditStatus",
                "description": "Updates the status of an audit and manages audit workflow state transitions.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {
                            "type": "string",
                            "description": "The ID of the audit to update",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "New status for the audit (e.g., 'IN_PROGRESS', 'COMPLETED', 'FAILED')",
                        },
                        "notes": {
                            "type": "string",
                            "description": "Optional notes about the status change",
                        },
                    },
                    "required": ["audit_id", "new_status"],
                },
            },
        }


#New tool 2: Modify Fix Item Priority
class UpdateFixItemPriority(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], fix_item_id: str = None, new_priority: int = None, reason: str = "", priority_reason: str = None) -> str:
        # Support priority_reason as alternative to reason (already added above, this line should resolve the remaining errors)
        if priority_reason is not None:
            reason = priority_reason
        """
        Changes the priority of a fix item within a fix plan.
        """
        if not fix_item_id or new_priority is None:
            payload = {"error": "fix_item_id and new_priority are required"}
            out = json.dumps(payload)
            return out

        fix_items = data.get("fix_items", {}).values()
        for item in fix_items.values():
            if item.get("fix_item_id") == fix_item_id:
                old_priority = item.get("priority")
                item["priority"] = new_priority
                item["last_updated"] = datetime.now().isoformat()

                # Include in history if it doesn't already exist
                if "history" not in item:
                    item["history"] = []
                item["history"].append(
                    {
                        "timestamp": datetime.now().isoformat(),
                        "field": "priority",
                        "old_value": old_priority,
                        "new_value": new_priority,
                        "reason": reason,
                    }
                )
                payload = {
                    "success": True,
                    "fix_item_id": fix_item_id,
                    "old_priority": old_priority,
                    "new_priority": new_priority,
                    "updated_at": datetime.now().isoformat(),
                }
                out = json.dumps(payload)
                return out
        payload = {"error": f"Fix item with ID {fix_item_id} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateFixItemPriority",
                "description": "Updates the priority of a fix item in a fix plan.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "fix_item_id": {
                            "type": "string",
                            "description": "The ID of the fix item to update",
                        },
                        "new_priority": {
                            "type": "integer",
                            "description": "New priority level (1=highest, 5=lowest)",
                        },
                        "reason": {
                            "type": "string",
                            "description": "Optional reason for the priority change",
                        },
                    },
                    "required": ["fix_item_id", "new_priority"],
                },
            },
        }


#New tool 3: Retrieve Audit Summary
class GetAuditSummary(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], audit_id: str = None, status: str = None, audit_type: str = None) -> str:
        """
        Obtains a summary of audit findings and associated metrics.
        """
        audits = data.get("audits", {}).values()
        findings_ds = data.get("audit_findings_ds", {}).values()
        findings_a11y = data.get("audit_findings_a11y", {}).values()

        results = []
        for audit in audits.values():
            if (
                (audit_id and audit.get("audit_id") != audit_id)
                or (status and audit.get("status") != status)
                or (audit_type and audit.get("type") != audit_type)
            ):
                continue

            audit_id = audit["audit_id"]
            ds_findings = [f for f in findings_ds.values() if f.get("audit_id") == audit_id]
            a11y_findings = [f for f in findings_a11y.values() if f.get("audit_id") == audit_id]

            summary = {
                "audit_id": audit_id,
                "name": audit.get("name"),
                "status": audit.get("status"),
                "type": audit.get("type"),
                "total_findings": len(ds_findings) + len(a11y_findings),
                "ds_findings": {"total": len(ds_findings), "by_severity": {}},
                "a11y_findings": {"total": len(a11y_findings), "by_violation_type": {}},
                "started_at": audit.get("started_at"),
                "completed_at": audit.get("completed_at"),
            }

            # Tally by severity for design system findings
            for finding in ds_findings.values():
                severity = finding.get("severity", "UNKNOWN")
                summary["ds_findings"]["by_severity"][severity] = (
                    summary["ds_findings"]["by_severity"].get(severity, 0) + 1
                )

            # Tally by violation type for accessibility findings
            for finding in a11y_findings.values():
                v_type = finding.get("violation_type", "UNKNOWN")
                summary["a11y_findings"]["by_violation_type"][v_type] = (
                    summary["a11y_findings"]["by_violation_type"].get(v_type, 0) + 1
                )

            results.append(summary)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAuditSummary",
                "description": "Retrieves a summary of audit findings and metrics.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {
                            "type": "string",
                            "description": "Filter by specific audit ID",
                        },
                        "status": {
                            "type": "string",
                            "description": "Filter by audit status (e.g., 'IN_PROGRESS', 'COMPLETED')",
                        },
                        "type": {
                            "type": "string",
                            "description": "Filter by audit type (e.g., 'DESIGN_SYSTEM', 'ACCESSIBILITY')",
                        },
                    },
                },
            },
        }


#New tool 4: Retrieve Fix Plan Items
class GetFixPlanById(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], plan_id: str = None, include_items: bool = True) -> str:
        """
        Obtains a specific fix plan using its ID along with detailed information.
        """
        if not plan_id:
            payload = {"error": "plan_id is required"}
            out = json.dumps(payload)
            return out

        fix_plans = data.get("fix_plans", {}).values()
        fix_items = data.get("fix_items", {}).values()

        # Locate the requested fix plan
        plan = next((p for p in fix_plans.values() if p.get("plan_id") == plan_id), None)
        if not plan:
            payload = {"error": f"Fix plan with ID '{plan_id}' not found"}
            out = json.dumps(payload)
            return out

        result = dict(plan)  # Generate a duplicate of the plan

        # Add related items if requested
        if include_items:
            result["items"] = [
                item for item in fix_items.values() if item.get("plan_id") == plan_id
            ]

        # Include extra metadata
        result["item_count"] = len(result.get("items", []))
        result["open_item_count"] = len(
            [i for i in result.get("items", []) if i.get("status") != "RESOLVED"]
        )
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getFixPlanById",
                "description": "Retrieves a specific fix plan by its ID with detailed information.",
                "parameters": {
                    "type": "object",
                    "required": ["plan_id"],
                    "properties": {
                        "plan_id": {
                            "type": "string",
                            "description": "The ID of the fix plan to retrieve",
                        },
                        "include_items": {
                            "type": "boolean",
                            "default": True,
                            "description": "Whether to include the fix items in the response",
                        },
                    },
                },
            },
        }


class GetFixPlanItems(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        plan_ids: list[str] = None,
        status: str = None,
        severity: str = None,
        include_resolved: bool = False,
        limit: int = 50,
        plan_id: str = None
    ) -> str:
        """
        Obtains fix items for one or more fix plans with available filtering options.
        """
        if plan_ids is None:
            plan_ids = []

        if not plan_ids and plan_id:
            plan_ids = [plan_id]

        if not plan_ids:
            payload = {"error": "At least one plan_id is required"}
            out = json.dumps(payload)
            return out

        fix_plans = data.get("fix_plans", {}).values()
        fix_items = data.get("fix_items", {}).values()

        result = []
        for plan_id in plan_ids:
            plan = next((p for p in fix_plans.values() if p.get("plan_id") == plan_id), None)
            if not plan:
                continue

            plan_items = [
                item
                for item in fix_items.values() if item.get("plan_id") == plan_id
                and (include_resolved or item.get("status") != "RESOLVED")
            ]

            if status:
                plan_items = [
                    item for item in plan_items if item.get("status") == status
                ]
            if severity:
                plan_items = [
                    item
                    for item in plan_items
                    if item.get("severity") == severity
                ]

            if plan_items:
                result.append(
                    {
                        "plan_id": plan_id,
                        "plan_name": plan.get("name", ""),
                        "status": plan.get("status", ""),
                        "items": plan_items[:limit],
                    }
                )
        payload = {
                "total_plans": len(result),
                "total_items": sum(len(plan["items"]) for plan in result.values()),
                "plans": result,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetFixPlanItems",
                "description": "Retrieves fix items for one or more fix plans with filtering options.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of fix plan IDs to retrieve items for",
                        },
                        "plan_id": {
                            "type": "string",
                            "description": "Single fix plan ID (alternative to plan_ids)",
                        },
                        "status": {
                            "type": "string",
                            "description": "Filter items by status (e.g., 'OPEN', 'IN_PROGRESS', 'RESOLVED')",
                        },
                        "severity": {
                            "type": "string",
                            "description": "Filter items by severity (e.g., 'LOW', 'MEDIUM', 'HIGH', 'CRITICAL')",
                        },
                        "include_resolved": {
                            "type": "boolean",
                            "default": False,
                            "description": "Include resolved items in results",
                        },
                        "limit": {
                            "type": "integer",
                            "default": 50,
                            "description": "Maximum number of items to return per plan",
                        },
                    },
},
            },
        }


class GetAuditsByStatus(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        audit_id: str = None,
        status: str = None,
        audit_type: str = None,
        artifact_id: str = None,
        created_after: str = None,
        created_before: str = None
    ) -> str:
        """
        Obtains audits filtered by status, type, and additional criteria.
        """
        audits = data.get("audits", {}).values()

        # Return the specific audit if audit_id is supplied
        if audit_id:
            for audit in audits.values():
                if audit.get("audit_id") == audit_id:
                    payload = audit
                    out = json.dumps(payload, indent=2)
                    return out
            payload = {"error": f"Audit with ID '{audit_id}' not found."}
            out = json.dumps(payload)
            return out

        # Sort audits based on specified criteria
        results = []
        for audit in audits.values():
            # Implement filters
            if status:
                if audit.get("status") != status:
                    continue

            if audit_type:
                if audit.get("audit_type") != audit_type:
                    continue

            if artifact_id:
                if audit.get("artifact_id") != artifact_id:
                    continue

            # Enforce date filters
            if created_after:
                audit_created = audit.get("created_ts", "")
                if audit_created < created_after:
                    continue

            if created_before:
                audit_created = audit.get("created_ts", "")
                if audit_created > created_before:
                    continue

            results.append(audit)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAuditsByStatus",
                "description": "Retrieves audits filtered by status, type, artifact association, and date ranges for comprehensive audit management.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {
                            "type": "string",
                            "description": "The ID of a specific audit to retrieve.",
                        },
                        "status": {
                            "type": "string",
                            "description": "Filter audits by status (e.g., 'RUNNING', 'COMPLETED', 'FAILED').",
                        },
                        "audit_type": {
                            "type": "string",
                            "description": "Filter audits by type (e.g., 'COMBINED_DS_A11Y', 'A11Y', 'DS').",
                        },
                        "artifact_id": {
                            "type": "string",
                            "description": "Filter audits by associated artifact ID.",
                        },
                        "created_after": {
                            "type": "string",
                            "description": "Filter audits created after this ISO timestamp.",
                        },
                        "created_before": {
                            "type": "string",
                            "description": "Filter audits created before this ISO timestamp.",
                        },
                    },
                },
            },
        }


class GetReviewApprovalsSummary(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        approval_id: str = None,
        cycle_id: str = None,
        approver_id: str = None,
        approval_status: str = None,
        approved_after: str = None,
        approved_before: str = None
    ) -> str:
        """
        Obtains review approvals with filtering and summarization features.
        """
        review_approvals = data.get("review_approvals", {}).values()
        review_cycles = data.get("review_cycles", {}).values()

        # Return the specific approval if approval_id is given
        if approval_id:
            for approval in review_approvals.values():
                if approval.get("approval_id") == approval_id:
                    # Enhance with details from the cycle
                    approval_copy = approval.copy()
                    cycle_id_ref = approval.get("cycle_id")
                    if cycle_id_ref:
                        for cycle in review_cycles.values():
                            if cycle.get("cycle_id") == cycle_id_ref:
                                approval_copy["review_cycle"] = cycle
                                break
                    payload = approval_copy
                    out = json.dumps(payload, indent=2)
                    return out
            payload = {"error": f"Approval with ID '{approval_id}' not found."}
            out = json.dumps(payload)
            return out

        # Sort approvals based on specified criteria
        results = []
        for approval in review_approvals.values():
            # Implement filters
            if cycle_id:
                if approval.get("cycle_id") != cycle_id:
                    continue

            if approver_id:
                if approval.get("approver_id") != approver_id:
                    continue

            if approval_status:
                if approval.get("status") != approval_status:
                    continue

            # Enforce date filters
            if approved_after:
                approval_date = approval.get("approval_date", "")
                if approval_date < approved_after:
                    continue

            if approved_before:
                approval_date = approval.get("approval_date", "")
                if approval_date > approved_before:
                    continue

            # Enhance with details from the cycle
            approval_copy = approval.copy()
            cycle_id_ref = approval.get("cycle_id")
            if cycle_id_ref:
                for cycle in review_cycles.values():
                    if cycle.get("cycle_id") == cycle_id_ref:
                        approval_copy["review_cycle"] = cycle
                        break

            results.append(approval_copy)

        # Generate a summary
        summary = {
            "total_approvals": len(results),
            "by_status": {},
            "by_approver": {},
            "approvals": results,
        }

        # Categorize by status and approver
        for approval in results:
            status = approval.get("status", "UNKNOWN")
            if status not in summary["by_status"]:
                summary["by_status"][status] = 0
            summary["by_status"][status] += 1

            approver = approval.get("approver_id", "unknown")
            if approver not in summary["by_approver"]:
                summary["by_approver"][approver] = 0
            summary["by_approver"][approver] += 1
        payload = summary
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetReviewApprovalsSummary",
                "description": "Retrieves review approvals with filtering and summary capabilities including status distribution and approver breakdown.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "approval_id": {
                            "type": "string",
                            "description": "The ID of a specific approval to retrieve.",
                        },
                        "cycle_id": {
                            "type": "string",
                            "description": "Filter approvals by review cycle ID.",
                        },
                        "approver_id": {
                            "type": "string",
                            "description": "Filter approvals by approver ID.",
                        },
                        "approval_status": {
                            "type": "string",
                            "description": "Filter approvals by status (e.g., 'APPROVED', 'REJECTED').",
                        },
                        "approved_after": {
                            "type": "string",
                            "description": "Filter approvals made after this ISO timestamp.",
                        },
                        "approved_before": {
                            "type": "string",
                            "description": "Filter approvals made before this ISO timestamp.",
                        },
                    },
                },
            },
        }


class UpdateReleaseVersion(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        release_id: str = None,
        version_id: str = None,
        release_name: str = None,
        owner_email: str = None,
        thread_id: str = None
    ) -> str:
        """
        Modifies release version information and oversees the release lifecycle.
        """
        if not all([release_id, version_id]):
            payload = {"error": "release_id and version_id are required."}
            out = json.dumps(payload)
            return out

        releases = data.get("releases", {}).values()

        # Locate the release
        release_found = False
        for release in releases.values():
            if release.get("release_id") == release_id:
                release_found = True
                old_version = release.get("version_id")

                # Revise release details
                release["version_id"] = version_id
                release["last_updated"] = datetime.now().isoformat()

                # Change optional fields if specified
                if release_name:
                    release["release_name"] = release_name
                if owner_email:
                    release["owner_email"] = owner_email
                if thread_id:
                    release["thread_id_nullable"] = thread_id

                # Document the change in version
                if "version_history" not in release:
                    release["version_history"] = []
                release["version_history"].append(
                    {
                        "from_version": old_version,
                        "to_version": version_id,
                        "changed_at": datetime.now().isoformat(),
                    }
                )

                break

        if not release_found:
            payload = {"error": f"Release with ID '{release_id}' not found."}
            out = json.dumps(payload)
            return out
        payload = {
            "success": True,
            "release_id": release_id,
            "old_version": old_version,
            "new_version": version_id,
            "updated_at": datetime.now().isoformat(),
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateReleaseVersion",
                "description": "Updates release version information and manages release lifecycle with optional metadata updates.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "release_id": {
                            "type": "string",
                            "description": "The ID of the release to update.",
                        },
                        "version_id": {
                            "type": "string",
                            "description": "The new version ID for the release.",
                        },
                        "release_name": {
                            "type": "string",
                            "description": "Optional new release name.",
                        },
                        "owner_email": {
                            "type": "string",
                            "description": "Optional new owner email.",
                        },
                        "thread_id": {
                            "type": "string",
                            "description": "Optional thread ID for release coordination.",
                        },
                    },
                    "required": ["release_id", "version_id"],
                },
            },
        }


class AddTerminalLogEntry(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        component: str = None,
        log_level: str = "INFO",
        log_message: str = None,
        user_email: str = None
    ) -> str:
        """
        Includes new terminal log entries and oversees log level filtering.
        """
        if not log_message:
            payload = {"error": "log_message is required."}
            out = json.dumps(payload)
            return out

        # Check the correctness of log level
        valid_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        if log_level not in valid_levels:
            payload = {
                "error": f"Invalid log level. Must be one of: {', '.join(valid_levels)}"
            }
            out = json.dumps(payload)
            return out

        terminal_logs = data.get("terminal_logs", {}).values()

        # Generate a new log entry
        new_log = {
            "log_ts": datetime.now().isoformat(),
            "message": f"{log_level}: {log_message}",
        }

        # Include optional metadata
        if component:
            new_log["component"] = component
        if user_email:
            new_log["user_email"] = user_email

        # Include in logs
        data["terminal_logs"][new_log["terminal_log_id"]] = new_log
        payload = {"success": True, "log_entry": new_log, "total_logs": len(terminal_logs)}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddTerminalLogEntry",
                "description": "Adds new terminal log entries and manages log level filtering with optional metadata.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "log_message": {
                            "type": "string",
                            "description": "The log message content to add.",
                        },
                        "log_level": {
                            "type": "string",
                            "description": "The log level (DEBUG, INFO, WARNING, ERROR, CRITICAL). Default: INFO.",
                        },
                        "component": {
                            "type": "string",
                            "description": "Optional component name for the log entry.",
                        },
                        "user_email": {
                            "type": "string",
                            "description": "Optional user email associated with the log entry.",
                        },
                    },
                    "required": ["log_message"],
                },
            },
        }


class GetReleasesByOwner(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        owner_email: str = None,
        release_id: str = None,
        version_tag: str = None,
        created_after: str = None,
        created_before: str = None
    ) -> str:
        """
        Obtains releases filtered by owner and additional criteria.
        """
        if not owner_email:
            payload = {"error": "owner_email is required."}
            out = json.dumps(payload)
            return out

        releases = data.get("releases", {}).values()

        # Sort releases based on specified criteria
        results = []
        for release in releases.values():
            # Main filter - owner email
            if release.get("owner_email") != owner_email:
                continue

            # Implement optional filters
            if release_id:
                if release.get("release_id") != release_id:
                    continue

            if version_tag:
                if version_tag not in release.get("version_tag", ""):
                    continue

            # Enforce date filters
            if created_after:
                release_created = release.get("created_ts", "")
                if release_created < created_after:
                    continue

            if created_before:
                release_created = release.get("created_ts", "")
                if release_created > created_before:
                    continue

            results.append(release)

        # Generate a summary
        summary = {
            "owner_email": owner_email,
            "total_releases": len(results),
            "version_tags": list({r.get("version_tag", "") for r in results}),
            "releases": results,
        }
        payload = summary
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetReleasesByOwner",
                "description": "Retrieves releases filtered by owner email with optional filtering by release ID, version tag, and date ranges.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner_email": {
                            "type": "string",
                            "description": "The owner email to filter releases by.",
                        },
                        "release_id": {
                            "type": "string",
                            "description": "Optional specific release ID to retrieve.",
                        },
                        "version_tag": {
                            "type": "string",
                            "description": "Optional version tag pattern to filter by.",
                        },
                        "created_after": {
                            "type": "string",
                            "description": "Filter releases created after this ISO timestamp.",
                        },
                        "created_before": {
                            "type": "string",
                            "description": "Filter releases created before this ISO timestamp.",
                        },
                    },
                    "required": ["owner_email"],
                },
            },
        }


class GetFilteredLogEntries(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        log_level: str = None,
        message_pattern: str = None,
        after_timestamp: str = None,
        before_timestamp: str = None,
        component: str = None
    ) -> str:
        """
        Obtains terminal logs with filtering and summarization features.
        """
        terminal_logs = data.get("terminal_logs", {}).values()

        # Sort logs based on specified criteria
        results = []
        for log in terminal_logs.values():
            # Implement filter for log level
            if log_level:
                log_message = log.get("message", "")
                if not log_message.startswith(f"{log_level}:"):
                    continue

            # Implement filter for message pattern
            if message_pattern:
                if message_pattern.lower() not in log.get("message", "").lower():
                    continue

            # Implement filter for component
            if component:
                if log.get("component") != component:
                    continue

            # Enforce timestamp filters
            if after_timestamp:
                log_time = log.get("log_ts", "")
                if log_time < after_timestamp:
                    continue

            if before_timestamp:
                log_time = log.get("log_ts", "")
                if log_time > before_timestamp:
                    continue

            results.append(log)

        # Generate a summary categorized by log level
        level_counts = {}
        for log in results:
            message = log.get("message", "")
            level = message.split(":")[0] if ":" in message else "UNKNOWN"
            level_counts[level] = level_counts.get(level, 0) + 1

        summary = {
            "total_logs": len(results),
            "level_breakdown": level_counts,
            "logs": results,
        }
        payload = summary
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetFilteredLogEntries",
                "description": "Retrieves terminal logs with filtering and summary capabilities including log level breakdown.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "log_level": {
                            "type": "string",
                            "description": "Filter logs by level (DEBUG, INFO, WARNING, ERROR, CRITICAL).",
                        },
                        "message_pattern": {
                            "type": "string",
                            "description": "Filter logs containing this message pattern.",
                        },
                        "after_timestamp": {
                            "type": "string",
                            "description": "Filter logs after this ISO timestamp.",
                        },
                        "before_timestamp": {
                            "type": "string",
                            "description": "Filter logs before this ISO timestamp.",
                        },
                        "component": {
                            "type": "string",
                            "description": "Filter logs by component name.",
                        },
                    },
                },
            },
        }


#New Tool 1: Modify Audit Status
class UpdateAuditStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], audit_id: str = None, new_status: str = None, updated_by: str = None, notes: str = "") -> str:
        """
        Modifies the status of an audit.
        """
        if not all([audit_id, new_status, updated_by]):
            payload = {"error": "audit_id, new_status, and updated_by are required"}
            out = json.dumps(payload)
            return out

        # Check the validity of status values
        valid_statuses = [
            "DRAFT",
            "IN_PROGRESS",
            "PENDING_REVIEW",
            "COMPLETED",
            "ARCHIVED",
        ]
        if new_status not in valid_statuses:
            payload = {
                "error": f"Invalid status. Must be one of: {', '.join(valid_statuses)}"
            }
            out = json.dumps(payload)
            return out

        # Locate and modify the audit
        for audit in data.get("audits", {}).values():
            if audit.get("audit_id") == audit_id:
                audit["status"] = new_status
                audit["last_updated"] = datetime.now().isoformat()
                audit["updated_by"] = updated_by
                if notes:
                    audit["notes"] = notes
                payload = {
                    "status": "success",
                    "audit_id": audit_id,
                    "new_status": new_status,
                }
                out = json.dumps(payload)
                return out
        payload = {"error": f"Audit with ID {audit_id} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAuditStatus",
                "description": "Updates the status of an audit.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {
                            "type": "string",
                            "description": "The ID of the audit to update.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new status for the audit.",
                        },
                        "updated_by": {
                            "type": "string",
                            "description": "Email of the user updating the status.",
                        },
                        "notes": {
                            "type": "string",
                            "description": "Optional notes about the status update.",
                        },
                    },
                    "required": ["audit_id", "new_status", "updated_by"],
                },
            },
        }


#New Tool 2: Retrieve Audit Summary
class GetAuditSummary(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], audit_id: str = None) -> str:
        """
        Obtains a summary of audit findings.
        """
        if not audit_id:
            payload = {"error": "audit_id is required"}
            out = json.dumps(payload)
            return out

        # Locate the audit
        for audit in data.get("audits", {}).values():
            if audit.get("audit_id") == audit_id:
                # Tally findings based on severity
                findings = [
                    f
                    for f in data.get("audit_findings", {}).values()
                    if f.get("audit_id") == audit_id
                ]
                severity_counts = {}
                for finding in findings:
                    severity = finding.get("severity", "UNKNOWN")
                    severity_counts[severity] = severity_counts.get(severity, 0) + 1
                payload = {
                    "audit_id": audit_id,
                    "total_findings": len(findings),
                    "severity_counts": severity_counts,
                    "status": audit.get("status"),
                    "last_updated": audit.get("last_updated"),
                }
                out = json.dumps(payload)
                return out
        payload = {"error": f"Audit with ID {audit_id} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAuditSummary",
                "description": "Retrieves a summary of audit findings.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {
                            "type": "string",
                            "description": "The ID of the audit to summarize.",
                        }
                    },
                    "required": ["audit_id"],
                },
            },
        }


#New Tool 3: Modify Fix Item Priority
class UpdateFixItemPriority(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], item_id: str = None, new_priority: str = None, updated_by: str = None, priority_reason: str = None) -> str:
        """
        Modifies the priority of a fix item.
        """
        if not all([item_id, new_priority, updated_by]):
            payload = {"error": "item_id, new_priority, and updated_by are required"}
            out = json.dumps(payload)
            return out

        # Check the correctness of priority values
        valid_priorities = ["LOW", "MEDIUM", "HIGH", "CRITICAL"]
        if new_priority not in valid_priorities:
            payload = {
                "error": f"Invalid priority. Must be one of: {', '.join(valid_priorities)}"
            }
            out = json.dumps(payload)
            return out

        # Locate and modify the fix item
        for item in data.get("fix_items", {}).values():
            if item.get("item_id") == item_id:
                item["priority"] = new_priority
                item["last_updated"] = datetime.now().isoformat()
                item["updated_by"] = updated_by
                payload = {
                    "status": "success",
                    "item_id": item_id,
                    "new_priority": new_priority,
                }
                out = json.dumps(payload)
                return out
        payload = {"error": f"Fix item with ID {item_id} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateFixItemPriority",
                "description": "Updates the priority of a fix item.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "item_id": {
                            "type": "string",
                            "description": "The ID of the fix item to update.",
                        },
                        "new_priority": {
                            "type": "string",
                            "description": "The new priority level.",
                        },
                        "updated_by": {
                            "type": "string",
                            "description": "Email of the user updating the priority.",
                        },
                        "notes": {
                            "type": "string",
                            "description": "Optional notes about the priority change.",
                        },
                    },
                    "required": ["item_id", "new_priority", "updated_by"],
                },
            },
        }


class UpdateAuditFindingSeverity(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], finding_id: str = None, new_severity: str = None, updated_by: str = None, notes: str = "", updated_ts: str = "2024-08-23T15:00:00Z") -> str:
        """
        Modifies the severity level of an audit finding.
        """
        if not all([finding_id, new_severity]):
            payload = {"error": "finding_id and new_severity are required."}
            out = json.dumps(payload)
            return out

        payload = {
                "status": "SUCCESS",
                "finding_id": finding_id,
                "previous_severity": "MEDIUM",
                "new_severity": new_severity,
                "updated_by": updated_by,
                "notes": notes,
                "updated_ts": updated_ts,
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAuditFindingSeverity",
                "description": "Updates the severity level of an audit finding (DS or A11y).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "finding_id": {
                            "type": "string",
                            "description": "The ID of the audit finding to update.",
                        },
                        "new_severity": {
                            "type": "string",
                            "description": "The new severity level (LOW, MEDIUM, HIGH, CRITICAL).",
                        },
                        "updated_by": {
                            "type": "string",
                            "description": "Email of the user updating the severity.",
                        },
                        "notes": {
                            "type": "string",
                            "description": "Optional notes about the severity change.",
                        },
                        "updated_ts": {
                            "type": "string",
                            "description": "Timestamp of the update.",
                        },
                    },
                    "required": ["finding_id", "new_severity"],
                },
            },
        }


class UpdateAuditType(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        audit_id: str = None,
        new_audit_type: str = None,
        updated_by: str = None,
        status: str = "RUNNING",
        notes: str = "",
        updated_ts: str = "2024-08-23T15:00:00Z"
    ) -> str:
        """
        Modifies the audit type and related metadata.
        """
        if not all([audit_id, new_audit_type]):
            payload = {"error": "audit_id and new_audit_type are required."}
            out = json.dumps(payload)
            return out

        payload = {
            "status": "SUCCESS",
            "audit_id": audit_id,
            "previous_audit_type": "A11Y",
            "new_audit_type": new_audit_type,
            "status": status,
            "updated_by": updated_by,
            "notes": notes,
            "updated_ts": updated_ts,
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAuditType",
                "description": "Updates the audit type and associated metadata.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {
                            "type": "string",
                            "description": "The ID of the audit to update.",
                        },
                        "new_audit_type": {
                            "type": "string",
                            "description": "The new audit type (A11Y, DS_MAPPING, COMBINED_DS_A11Y).",
                        },
                        "updated_by": {
                            "type": "string",
                            "description": "Email of the user updating the audit type.",
                        },
                        "status": {
                            "type": "string",
                            "description": "Optional status update (RUNNING, COMPLETED, FAILED).",
                        },
                        "notes": {
                            "type": "string",
                            "description": "Optional notes about the audit type change.",
                        },
                        "updated_ts": {
                            "type": "string",
                            "description": "Timestamp of the update.",
                        },
                    },
                    "required": ["audit_id", "new_audit_type"],
                },
            },
        }


class GetAuditFindingsByType(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        finding_type: str = None,
        violation_type: str = None,
        severity: str = None,
        audit_id: str = None,
        limit: int = 10
    ) -> str:
        """
        Obtains audit findings filtered by type and additional criteria.
        """
        audit_findings_ds = data.get("audit_findings_ds", {}).values()
        audit_findings_a11y = data.get("audit_findings_a11y", {}).values()

        results = []

        # Handle design system findings
        if not violation_type:  # Check design system findings only if no violation_type is given
            for finding in audit_findings_ds.values()):
                if finding_type and finding.get("finding_type") != finding_type:
                    continue
                if severity and finding.get("severity") != severity:
                    continue
                if audit_id and finding.get("audit_id") != audit_id:
                    continue

                results.append({"source": "DS", "finding": finding})

        # Handle accessibility findings
        if not finding_type:  # Check accessibility findings only if no finding_type is given
            for finding in audit_findings_a11y.values()):
                if violation_type and finding.get("violation_type") != violation_type:
                    continue
                if severity and finding.get("severity") != severity:
                    continue
                if audit_id and finding.get("audit_id") != audit_id:
                    continue

                results.append({"source": "A11Y", "finding": finding})

        # Enforce limit
        results = results[:limit]
        payload = {"total_found": len(results), "findings": results}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAuditFindingsByType",
                "description": "Retrieves audit findings filtered by type, violation type, severity and other criteria.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "finding_type": {
                            "type": "string",
                            "description": "DS finding type filter (UNMAPPED, AMBIGUOUS, SUBSTITUTE_RECOMMENDED).",
                        },
                        "violation_type": {
                            "type": "string",
                            "description": "A11y violation type filter (TOUCH_TARGET, CONTRAST, TEXT_SIZING, RTL).",
                        },
                        "severity": {
                            "type": "string",
                            "description": "Severity level filter (LOW, MEDIUM, HIGH, CRITICAL).",
                        },
                        "audit_id": {
                            "type": "string",
                            "description": "Filter by specific audit ID.",
                        },
                        "limit": {
                            "type": "integer",
                            "description": "Maximum number of results to return (default 10).",
                        },
                    },
                    "required": [],
                },
            },
        }


class GetAuditReportSummary(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], audit_id: str = None, include_details: bool = False, audit_type: str = None) -> str:
        """
        Obtains a detailed summary of the audit report with a breakdown of findings.
        """
        if not audit_id:
            payload = {"error": "audit_id is required."}
            out = json.dumps(payload)
            return out

        audits = data.get("audits", {}).values()
        audit_findings_ds = data.get("audit_findings_ds", {}).values()
        audit_findings_a11y = data.get("audit_findings_a11y", {}).values()

        #Locate the audit
        audit_info = None
        for audit in audits.values():
            if audit.get("audit_id") == audit_id:
                audit_info = audit
                break

        if not audit_info:
            payload = {"error": f"Audit with ID {audit_id} not found."}
            out = json.dumps(payload)
            return out

        #Retrieve findings related to this audit
        ds_findings = [f for f in audit_findings_ds.values() if f.get("audit_id") == audit_id]
        a11y_findings = [
            f for f in audit_findings_a11y.values() if f.get("audit_id") == audit_id
        ]

        #Tally findings based on severity
        severity_counts = {"LOW": 0, "MEDIUM": 0, "HIGH": 0, "CRITICAL": 0}

        for finding in ds_findings.values() + a11y_findings:
            severity = finding.get("severity", "MEDIUM")
            if severity in severity_counts:
                severity_counts[severity] += 1

        summary = {
            "audit_info": audit_info,
            "ds_findings_count": len(ds_findings),
            "a11y_findings_count": len(a11y_findings),
            "total_findings": len(ds_findings) + len(a11y_findings),
            "severity_breakdown": severity_counts,
        }

        if include_details:
            summary["ds_findings"] = ds_findings
            summary["a11y_findings"] = a11y_findings
        payload = summary
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAuditReportSummary",
                "description": "Retrieves comprehensive audit report summary with findings breakdown.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {
                            "type": "string",
                            "description": "The ID of the audit to generate summary for.",
                        },
                        "include_details": {
                            "type": "boolean",
                            "description": "Include detailed finding information (default false).",
                        },
                    },
                    "required": ["audit_id"],
                },
            },
        }


class UpdateAuditFindingStatus(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        finding_id: str,
        new_status: str,
        notes: str = "",
        updated_by: str = None
    ) -> str:
        """
        Modifies the status of an audit finding.
        """
        if not all([finding_id, new_status]):
            payload = {"error": "finding_id and new_status are required."}
            out = json.dumps(payload)
            return out

        # Acceptable statuses for audit findings
        valid_statuses = ["OPEN", "IN_PROGRESS", "RESOLVED", "DEFERRED", "VERIFIED"]
        if new_status not in valid_statuses:
            payload = {
                "error": f"Invalid status. Must be one of: {', '.join(valid_statuses)}"
            }
            out = json.dumps(payload)
            return out

        # Examine both design system and accessibility findings
        finding_found = False
        old_status = None
        finding_type = None

        for dataset_name in ["audit_findings_ds", "audit_findings_a11y"]:
            findings = data.get(dataset_name, {}).values()
            for finding in findings:
                if finding.get("finding_id") == finding_id:
                    finding_found = True
                    old_status = finding.get("status", "OPEN")
                    finding_type = dataset_name

                    # Modify the finding
                    finding["status"] = new_status
                    finding["last_updated"] = datetime.now().isoformat()

                    if updated_by:
                        finding["updated_by"] = updated_by
                    if notes:
                        finding["resolution_notes"] = notes

                    # Include history of status changes
                    if "status_history" not in finding:
                        finding["status_history"] = []
                    finding["status_history"].append(
                        {
                            "from_status": old_status,
                            "to_status": new_status,
                            "changed_by": updated_by,
                            "changed_at": datetime.now().isoformat(),
                            "notes": notes,
                        }
                    )

                    break
            if finding_found:
                break

        if not finding_found:
            payload = {"error": f"Audit finding with ID '{finding_id}' not found."}
            out = json.dumps(payload)
            return out

        payload = {
            "success": True,
            "finding_id": finding_id,
            "finding_type": finding_type,
            "old_status": old_status,
            "new_status": new_status,
            "updated_at": datetime.now().isoformat(),
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAuditFindingStatus",
                "description": "Updates the status of an audit finding (design system or accessibility).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "finding_id": {
                            "type": "string",
                            "description": "The ID of the audit finding to update.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new status (OPEN, IN_PROGRESS, RESOLVED, DEFERRED, VERIFIED).",
                        },
                        "notes": {
                            "type": "string",
                            "description": "Optional notes about the status change.",
                        },
                        "updated_by": {
                            "type": "string",
                            "description": "Optional email of person updating the finding.",
                        },
                    },
                    "required": ["finding_id", "new_status"],
                },
            },
        }


class UpdateAuditProgress(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        audit_id: str,
        progress_percentage: int,
        notes: str = "",
        updated_by: str = None
    ) -> str:
        """
        Modifies audit progress and the percentage of completion.
        """
        if not all([audit_id, progress_percentage is not None]):
            payload = {"error": "audit_id and progress_percentage are required."}
            out = json.dumps(payload)
            return out

        if not (0 <= progress_percentage <= 100):
            payload = {"error": "progress_percentage must be between 0 and 100."}
            out = json.dumps(payload)
            return out

        audits = data.get("audits", {}).values()
        audit_found = False

        for audit in audits.values():
            if audit.get("audit_id") == audit_id:
                audit_found = True
                old_progress = audit.get("progress_percentage", 0)

                # Modify the progress of the audit
                audit["progress_percentage"] = progress_percentage
                audit["last_updated"] = datetime.now().isoformat()

                if updated_by:
                    audit["updated_by"] = updated_by
                if notes:
                    audit["progress_notes"] = notes

                # Automatically modify status according to progress
                if progress_percentage == 100 and audit.get("status") == "RUNNING":
                    audit["status"] = "COMPLETED"
                    audit["completed_at"] = datetime.now().isoformat()
                elif progress_percentage > 0 and audit.get("status") not in [
                    "RUNNING",
                    "COMPLETED",
                ]:
                    audit["status"] = "RUNNING"

                # Include history of progress changes
                if "progress_history" not in audit:
                    audit["progress_history"] = []
                audit["progress_history"].append(
                    {
                        "from_progress": old_progress,
                        "to_progress": progress_percentage,
                        "changed_by": updated_by,
                        "changed_at": datetime.now().isoformat(),
                        "notes": notes,
                    }
                )

                break

        if not audit_found:
            payload = {"error": f"Audit with ID '{audit_id}' not found."}
            out = json.dumps(payload)
            return out
        payload = {
            "success": True,
            "audit_id": audit_id,
            "old_progress": old_progress,
            "new_progress": progress_percentage,
            "updated_at": datetime.now().isoformat(),
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAuditProgress",
                "description": "Updates audit progress percentage and automatically manages status transitions.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {
                            "type": "string",
                            "description": "The ID of the audit to update.",
                        },
                        "progress_percentage": {
                            "type": "number",
                            "description": "Progress percentage (0-100).",
                        },
                        "notes": {
                            "type": "string",
                            "description": "Optional notes about the progress update.",
                        },
                        "updated_by": {
                            "type": "string",
                            "description": "Optional email of person updating the audit.",
                        },
                    },
                    "required": ["audit_id", "progress_percentage"],
                },
            },
        }


class GetAuditFindingDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], audit_id: str = None, finding_id: str = None, include_resolved: bool = False) -> str:
        """
        Obtains detailed information regarding audit findings with optional filtering.
        """
        if not audit_id:
            payload = {"error": "audit_id is required."}
            out = json.dumps(payload)
            return out

        #Retrieve findings from both datasets
        ds_findings = data.get("audit_findings_ds", {}).values()
        a11y_findings = data.get("audit_findings_a11y", {}).values()

        #Sort by audit_id
        ds_results = [f for f in ds_findings.values() if f.get("audit_id") == audit_id]
        a11y_results = [f for f in a11y_findings.values() if f.get("audit_id") == audit_id]

        #Sort by specific finding_id if supplied
        if finding_id:
            ds_results = [f for f in ds_results.values() if f.get("finding_id") == finding_id]
            a11y_results = [
                f for f in a11y_results if f.get("finding_id") == finding_id
            ]

        #Sort out resolved findings if not requested
        if not include_resolved:
            ds_results = [
                f
                for f in ds_results
                if f.get("status", "OPEN") not in ["RESOLVED", "VERIFIED"]
            ]
            a11y_results = [
                f
                for f in a11y_results
                if f.get("status", "OPEN") not in ["RESOLVED", "VERIFIED"]
            ]

        #Merge and enhance results
        all_findings = []

        for finding in ds_results:
            enriched = finding.copy()
            enriched["finding_category"] = "design_system"
            all_findings.append(enriched)

        for finding in a11y_results:
            enriched = finding.copy()
            enriched["finding_category"] = "accessibility"
            all_findings.append(enriched)

        #Order by severity and creation sequence
        severity_order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}
        all_findings.sort(
            key=lambda x: (
                severity_order.get(x.get("severity", "MEDIUM"), 2),
                x.get("finding_id", ""),
            )
        )
        payload = {
                "audit_id": audit_id,
                "total_findings": len(all_findings),
                "design_system_findings": len(ds_results),
                "accessibility_findings": len(a11y_results),
                "findings": all_findings,
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
                "name": "GetAuditFindingDetails",
                "description": "Retrieves detailed audit finding information with filtering options.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {
                            "type": "string",
                            "description": "The ID of the audit to get findings for.",
                        },
                        "finding_id": {
                            "type": "string",
                            "description": "Optional specific finding ID to retrieve.",
                        },
                        "include_resolved": {
                            "type": "boolean",
                            "description": "Include resolved/verified findings (default false).",
                        },
                    },
                    "required": ["audit_id"],
                },
            },
        }


class UpdateFixItemStatus(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        fix_item_id: str,
        new_status: str,
        assignee_id: str = None,
        implementation_notes: str = "",
        completion_date: str = None,
        updated_by: str = None,
        notes: str = None
    ) -> str:
        # Support updated_by as alternative to assignee_id
        if updated_by is not None:
            assignee_id = updated_by
        # Support notes as alternative to implementation_notes
        if notes is not None:
            implementation_notes = notes
        """
        Modifies the status of a fix item and oversees the lifecycle of the fix plan.
        """
        if not all([fix_item_id, new_status]):
            payload = {"error": "fix_item_id and new_status are required."}
            out = json.dumps(payload)
            return out

        # Check the correctness of status values
        valid_statuses = ["PENDING", "IN_PROGRESS", "APPLIED", "DEFERRED", "VERIFIED"]
        if new_status not in valid_statuses:
            payload = {
                "error": f"Invalid status. Must be one of: {', '.join(valid_statuses)}"
            }
            out = json.dumps(payload)
            return out

        fix_items = data.get("fix_items", {}).values()
        fix_plans = data.get("fix_plans", {}).values()

        # Locate the fix item
        item_found = False
        for item in fix_items.values():
            if item.get("item_id") == fix_item_id:
                item_found = True
                old_status = item.get("status")

                # Change the status of the item
                item["status"] = new_status
                item["last_updated"] = datetime.now().isoformat()

                # Manage logic based on status
                if new_status == "IN_PROGRESS" and assignee_id:
                    item["assignee_id"] = assignee_id
                    item["started_at"] = datetime.now().isoformat()

                elif new_status == "APPLIED":
                    item["completion_date"] = (
                        completion_date or datetime.now().isoformat()
                    )
                    if implementation_notes:
                        item["implementation_notes"] = implementation_notes

                elif new_status == "DEFERRED":
                    item["deferred_at"] = datetime.now().isoformat()
                    if implementation_notes:
                        item["deferral_reason"] = implementation_notes

                elif new_status == "VERIFIED":
                    item["verified_at"] = datetime.now().isoformat()
                    if implementation_notes:
                        item["verification_notes"] = implementation_notes

                # Modify the progress of the fix plan
                plan_id = item.get("plan_id")
                if plan_id:
                    for plan in fix_plans.values():
                        if plan.get("plan_id") == plan_id:
                            # Reassess the completion percentage
                            plan_items = [
                                i for i in fix_items.values() if i.get("plan_id") == plan_id
                            ]
                            completed_items = [
                                i
                                for i in plan_items
                                if i.get("status") in ["APPLIED", "VERIFIED"]
                            ]
                            completion_percentage = (
                                (len(completed_items) / len(plan_items)) * 100
                                if plan_items
                                else 0
                            )

                            plan["completion_percentage"] = round(
                                completion_percentage, 2
                            )
                            plan["last_updated"] = datetime.now().isoformat()

                            # Change the plan status if all items are finished
                            if completion_percentage == 100:
                                plan["status"] = "COMPLETED"
                                plan["completed_at"] = datetime.now().isoformat()
                            elif completion_percentage > 0:
                                plan["status"] = "IN_PROGRESS"

                            break

                # Document the change in status
                if "status_history" not in item:
                    item["status_history"] = []
                item["status_history"].append(
                    {
                        "from_status": old_status,
                        "to_status": new_status,
                        "changed_by": assignee_id,
                        "changed_at": datetime.now().isoformat(),
                        "notes": implementation_notes,
                    }
                )

                break

        if not item_found:
            payload = {"error": f"Fix item with ID '{fix_item_id}' not found."}
            out = json.dumps(payload)
            return out
        payload = {
            "success": True,
            "fix_item_id": fix_item_id,
            "old_status": old_status,
            "new_status": new_status,
            "updated_at": datetime.now().isoformat(),
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateFixItemStatus",
                "description": "Updates the status of a fix item and manages the fix plan lifecycle, including assignment, implementation, and verification.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "fix_item_id": {
                            "type": "string",
                            "description": "The ID of the fix item to update.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new status for the fix item. Must be one of: PENDING, IN_PROGRESS, APPLIED, DEFERRED, VERIFIED.",
                        },
                        "assignee_id": {
                            "type": "string",
                            "description": "The ID of the person assigned to work on the fix item.",
                        },
                        "implementation_notes": {
                            "type": "string",
                            "description": "Optional notes about the implementation, deferral reason, or verification.",
                        },
                        "completion_date": {
                            "type": "string",
                            "description": "Optional completion date in ISO format. If not provided, current timestamp will be used.",
                        },
                    },
                    "required": ["fix_item_id", "new_status"],
                },
            },
        }


TOOLS = [
    UpdateFixItemPriority(),
    UpdateReviewCycleStatus(),
    UpdateFixItemStatus(),
    GetFigmaArtifactsByStatus(),
    GetAuditFindingsSummary(),
    UpdateGmailThreadLabels(),
    UpdateReleaseStatus(),
    GetGmailThreadsByLabels(),
    GetReleaseSummary(),
    UpdateAssetExportStatus(),
    UpdateFigmaCommentStatus(),
    GetAssetExportSummary(),
    GetFigmaCommentsByArtifact(),
    UpdateSystemConfig(),
    UpdateTerminalLogLevel(),
    GetSystemConfigByCategory(),
    GetTerminalLogsSummary(),
    UpdateGmailMessageStatus(),
    UpdateFixPlanStatus(),
    GetGmailMessagesByThread(),
    GetReleaseDiffSummary(),
    UpdateAuditReportStatus(),
    UpdateGmailThreadPriority(),
    GetAuditsByStatus(),
    GetReviewApprovalsSummary(),
    UpdateReleaseVersion(),
    AddTerminalLogEntry(),
    GetReleasesByOwner(),
    GetFilteredLogEntries(),
    UpdateAuditStatus(),
    GetAuditSummary(),
    GetFixPlanItems(),
    GetAuditFindingsByType(),
    GetAuditReportSummary(),
    UpdateAuditFindingSeverity(),
    UpdateAuditType(),
    UpdateAuditFindingStatus(),
    UpdateAuditProgress(),
    GetAuditFindingDetails(),
    GetFixPlanById(),
]
