import json
import uuid
from datetime import datetime
from typing import Any, Dict
from domains.dto import Tool

class UpdateReviewCycleStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Updates the status of a review cycle and handles status transitions.
        """
        cycle_id = kwargs.get('cycle_id')
        new_status = kwargs.get('new_status')
        approver_id = kwargs.get('approver_id')
        comments = kwargs.get('comments', '')

        if not all([cycle_id, new_status]):
            return json.dumps({"error": "cycle_id and new_status are required."})

        # Validate status values
        valid_statuses = ['IN_FLIGHT', 'NEEDS_REVIEW', 'APPROVED', 'CHANGES_REQUESTED', 'ESCALATED']
        if new_status not in valid_statuses:
            return json.dumps({"error": f"Invalid status. Must be one of: {', '.join(valid_statuses)}"})

        review_cycles = data.get('review_cycles', [])
        review_approvals = data.get('review_approvals', [])

        # Find the review cycle
        cycle_found = False
        for cycle in review_cycles:
            if cycle.get('cycle_id') == cycle_id:
                cycle_found = True
                old_status = cycle.get('status')

                # Update the cycle status
                cycle['status'] = new_status
                cycle['last_updated'] = datetime.now().isoformat()

                # Handle status-specific logic
                if new_status == 'APPROVED' and approver_id:
                    # Create approval record
                    approval_id = f"approval_{uuid.uuid4().hex[:8]}"
                    new_approval = {
                        "approval_id": approval_id,
                        "cycle_id": cycle_id,
                        "approver_id": approver_id,
                        "approval_date": datetime.now().isoformat(),
                        "comments": comments,
                        "status": "APPROVED"
                    }
                    review_approvals.append(new_approval)

                elif new_status == 'CHANGES_REQUESTED' and comments:
                    # Add change request to comments
                    if 'change_requests' not in cycle:
                        cycle['change_requests'] = []
                    cycle['change_requests'].append({
                        "request_id": f"req_{uuid.uuid4().hex[:8]}",
                        "requester_id": approver_id,
                        "request_date": datetime.now().isoformat(),
                        "comments": comments
                    })

                # Log the status change
                if 'status_history' not in cycle:
                    cycle['status_history'] = []
                cycle['status_history'].append({
                    "from_status": old_status,
                    "to_status": new_status,
                    "changed_by": approver_id,
                    "changed_at": datetime.now().isoformat(),
                    "comments": comments
                })

                break

        if not cycle_found:
            return json.dumps({"error": f"Review cycle with ID '{cycle_id}' not found."})

        return json.dumps({
            "success": True,
            "cycle_id": cycle_id,
            "old_status": old_status,
            "new_status": new_status,
            "updated_at": datetime.now().isoformat()
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_review_cycle_status",
                "description": "Updates the status of a design review cycle and handles status transitions including approvals and change requests.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cycle_id": {"type": "string", "description": "The ID of the review cycle to update."},
                        "new_status": {"type": "string", "description": "The new status for the review cycle. Must be one of: IN_FLIGHT, NEEDS_REVIEW, APPROVED, CHANGES_REQUESTED, ESCALATED."},
                        "approver_id": {"type": "string", "description": "The ID of the person making the status change."},
                        "comments": {"type": "string", "description": "Optional comments about the status change or change request."}
                    },
                    "required": ["cycle_id", "new_status"]
                }
            }
        }



class GetFigmaArtifactsByStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Retrieves Figma artifacts filtered by various criteria including status, tags, and review state.
        """
        artifact_id = kwargs.get('artifact_id')
        status = kwargs.get('status')
        tags = kwargs.get('tags', [])
        review_status = kwargs.get('review_status')
        artifact_type = kwargs.get('artifact_type')

        figma_artifacts = data.get('figma_artifacts', [])
        review_cycles = data.get('review_cycles', [])

        # If artifact_id is provided, return specific artifact
        if artifact_id:
            for artifact in figma_artifacts:
                if artifact.get('artifact_id') == artifact_id:
                    # Enrich with review cycle information
                    artifact_copy = artifact.copy()
                    for cycle in review_cycles:
                        if cycle.get('artifact_id') == artifact_id:
                            artifact_copy['review_cycle'] = cycle
                            break
                    return json.dumps(artifact_copy, indent=2)
            return json.dumps({"error": f"Artifact with ID '{artifact_id}' not found."})

        # Filter artifacts by criteria
        results = []
        for artifact in figma_artifacts:
            # Apply filters
            if status and artifact.get('status') != status:
                continue

            if artifact_type and artifact.get('artifact_type') != artifact_type:
                continue

            if tags:
                artifact_tags = artifact.get('current_tags', [])
                if not any(tag in artifact_tags for tag in tags):
                    continue

            # Enrich with review cycle information
            artifact_copy = artifact.copy()
            for cycle in review_cycles:
                if cycle.get('artifact_id') == artifact.get('artifact_id'):
                    artifact_copy['review_cycle'] = cycle
                    break

            # Apply review status filter
            if review_status:
                if 'review_cycle' not in artifact_copy:
                    continue
                if artifact_copy['review_cycle'].get('status') != review_status:
                    continue

            results.append(artifact_copy)

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_figma_artifacts_by_status",
                "description": "Retrieves Figma artifacts filtered by various criteria including status, tags, review state, and artifact type. Enriches results with review cycle information.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {"type": "string", "description": "The ID of a specific artifact to retrieve."},
                        "status": {"type": "string", "description": "Filter by artifact status (e.g., 'active', 'archived')."},
                        "tags": {"type": "array", "items": {"type": "string"}, "description": "Filter by tags (e.g., ['needs-review', 'design-system'])."},
                        "review_status": {"type": "string", "description": "Filter by review cycle status (e.g., 'NEEDS_REVIEW', 'APPROVED')."},
                        "artifact_type": {"type": "string", "description": "Filter by artifact type (e.g., 'frame', 'component', 'page')."}
                    }
                }
            }
        }

class GetAuditFindingsSummary(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Retrieves a comprehensive summary of audit findings including design system and accessibility violations.
        """
        audit_id = kwargs.get('audit_id')
        finding_type = kwargs.get('finding_type')
        severity = kwargs.get('severity')
        violation_type = kwargs.get('violation_type')

        audits = data.get('audits', [])
        audit_findings_ds = data.get('audit_findings_ds', [])
        audit_findings_a11y = data.get('audit_findings_a11y', [])

        # If audit_id is provided, return specific audit findings
        if audit_id:
            audit_info = None
            for audit in audits:
                if audit.get('audit_id') == audit_id:
                    audit_info = audit
                    break

            if not audit_info:
                return json.dumps({"error": f"Audit with ID '{audit_id}' not found."})

            # Get findings for this audit
            ds_findings = [f for f in audit_findings_ds if f.get('audit_id') == audit_id]
            a11y_findings = [f for f in audit_findings_a11y if f.get('audit_id') == audit_id]

            summary = {
                "audit_info": audit_info,
                "design_system_findings": {
                    "total": len(ds_findings),
                    "unmapped": len([f for f in ds_findings if f.get('finding_type') == 'UNMAPPED']),
                    "substitute_recommended": len([f for f in ds_findings if f.get('finding_type') == 'SUBSTITUTE_RECOMMENDED']),
                    "ambiguous": len([f for f in ds_findings if f.get('finding_type') == 'AMBIGUOUS'])
                },
                "accessibility_findings": {
                    "total": len(a11y_findings),
                    "touch_target": len([f for f in a11y_findings if f.get('violation_type') == 'TOUCH_TARGET']),
                    "contrast": len([f for f in a11y_findings if f.get('violation_type') == 'CONTRAST']),
                    "text_sizing": len([f for f in a11y_findings if f.get('violation_type') == 'TEXT_SIZING']),
                    "rtl": len([f for f in a11y_findings if f.get('violation_type') == 'RTL'])
                },
                "findings": {
                    "design_system": ds_findings,
                    "accessibility": a11y_findings
                }
            }

            return json.dumps(summary, indent=2)

        # Return summary across all audits
        all_ds_findings = audit_findings_ds
        all_a11y_findings = audit_findings_a11y

        # Apply filters
        if finding_type:
            all_ds_findings = [f for f in all_ds_findings if f.get('finding_type') == finding_type]

        if violation_type:
            all_a11y_findings = [f for f in all_a11y_findings if f.get('violation_type') == violation_type]

        if severity:
            all_ds_findings = [f for f in all_ds_findings if f.get('severity') == severity]
            all_a11y_findings = [f for f in all_a11y_findings if f.get('severity') == severity]

        summary = {
            "total_audits": len(audits),
            "design_system_findings": {
                "total": len(all_ds_findings),
                "by_type": {},
                "by_severity": {}
            },
            "accessibility_findings": {
                "total": len(all_a11y_findings),
                "by_type": {},
                "by_severity": {}
            }
        }

        # Group design system findings
        for finding in all_ds_findings:
            finding_type = finding.get('finding_type')
            severity = finding.get('severity')

            if finding_type not in summary["design_system_findings"]["by_type"]:
                summary["design_system_findings"]["by_type"][finding_type] = 0
            summary["design_system_findings"]["by_type"][finding_type] += 1

            if severity not in summary["design_system_findings"]["by_severity"]:
                summary["design_system_findings"]["by_severity"][severity] = 0
            summary["design_system_findings"]["by_severity"][severity] += 1

        # Group accessibility findings
        for finding in all_a11y_findings:
            violation_type = finding.get('violation_type')
            severity = finding.get('severity')

            if violation_type not in summary["accessibility_findings"]["by_type"]:
                summary["accessibility_findings"]["by_type"][violation_type] = 0
            summary["accessibility_findings"]["by_type"][violation_type] += 1

            if severity not in summary["accessibility_findings"]["by_severity"]:
                summary["accessibility_findings"]["by_severity"][severity] = 0
            summary["accessibility_findings"]["by_severity"][severity] += 1

        return json.dumps(summary, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_audit_findings_summary",
                "description": "Retrieves a comprehensive summary of audit findings including design system and accessibility violations, with filtering and grouping capabilities.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string", "description": "The ID of a specific audit to retrieve findings for."},
                        "finding_type": {"type": "string", "description": "Filter design system findings by type (e.g., 'UNMAPPED', 'SUBSTITUTE_RECOMMENDED', 'AMBIGUOUS')."},
                        "severity": {"type": "string", "description": "Filter findings by severity (e.g., 'HIGH', 'MEDIUM', 'LOW')."},
                        "violation_type": {"type": "string", "description": "Filter accessibility findings by violation type (e.g., 'TOUCH_TARGET', 'CONTRAST', 'TEXT_SIZING', 'RTL')."}
                    }
                }
            }
        }

class UpdateGmailThreadLabels(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Updates Gmail thread labels and manages email workflow status.
        """
        thread_id = kwargs.get('thread_id')
        new_labels = kwargs.get('new_labels', [])
        remove_labels = kwargs.get('remove_labels', [])
        update_recipients = kwargs.get('update_recipients', [])
        status_notes = kwargs.get('status_notes', '')

        if not thread_id:
            return json.dumps({"error": "thread_id is required."})

        gmail_threads = data.get('gmail_threads', [])

        # Find the thread
        thread_found = False
        for thread in gmail_threads:
            if thread.get('thread_id') == thread_id:
                thread_found = True
                old_labels = thread.get('current_labels', []).copy()

                # Update labels
                if new_labels:
                    for label in new_labels:
                        if label not in old_labels:
                            old_labels.append(label)

                if remove_labels:
                    for label in remove_labels:
                        if label in old_labels:
                            old_labels.remove(label)

                thread['current_labels'] = old_labels
                thread['updated_ts'] = datetime.now().isoformat()

                # Update recipients if provided
                if update_recipients:
                    thread['recipients'] = update_recipients

                # Add status notes
                if status_notes:
                    if 'status_history' not in thread:
                        thread['status_history'] = []
                    thread['status_history'].append({
                        "timestamp": datetime.now().isoformat(),
                        "action": "labels_updated",
                        "notes": status_notes,
                        "old_labels": thread.get('current_labels', []),
                        "new_labels": old_labels
                    })

                break

        if not thread_found:
            return json.dumps({"error": f"Gmail thread with ID '{thread_id}' not found."})

        return json.dumps({
            "success": True,
            "thread_id": thread_id,
            "old_labels": old_labels,
            "new_labels": old_labels,
            "updated_at": datetime.now().isoformat()
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_gmail_thread_labels",
                "description": "Updates Gmail thread labels, recipients, and manages email workflow status with comprehensive tracking.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "thread_id": {"type": "string", "description": "The ID of the Gmail thread to update."},
                        "new_labels": {"type": "array", "items": {"type": "string"}, "description": "New labels to add to the thread."},
                        "remove_labels": {"type": "array", "items": {"type": "string"}, "description": "Labels to remove from the thread."},
                        "update_recipients": {"type": "array", "items": {"type": "string"}, "description": "New list of recipients for the thread."},
                        "status_notes": {"type": "string", "description": "Optional notes about the label update for tracking purposes."}
                    },
                    "required": ["thread_id"]
                }
            }
        }

class UpdateReleaseStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Updates release status and manages release workflow metadata.
        """
        release_id = kwargs.get('release_id')
        new_status = kwargs.get('new_status')
        version_notes = kwargs.get('version_notes', '')
        thread_id = kwargs.get('thread_id')
        release_metadata = kwargs.get('release_metadata', {})

        if not all([release_id, new_status]):
            return json.dumps({"error": "release_id and new_status are required."})

        # Validate status values
        valid_statuses = ['DRAFT', 'IN_REVIEW', 'APPROVED', 'PUBLISHED', 'ARCHIVED']
        if new_status not in valid_statuses:
            return json.dumps({"error": f"Invalid status. Must be one of: {', '.join(valid_statuses)}"})

        releases = data.get('releases', [])

        # Find the release
        release_found = False
        for release in releases:
            if release.get('release_id') == release_id:
                release_found = True
                old_status = release.get('status', 'DRAFT')

                # Update release status
                release['status'] = new_status
                release['last_updated'] = datetime.now().isoformat()

                # Update thread association
                if thread_id:
                    release['thread_id_nullable'] = thread_id

                # Add version notes
                if version_notes:
                    if 'version_history' not in release:
                        release['version_history'] = []
                    release['version_history'].append({
                        "timestamp": datetime.now().isoformat(),
                        "status": new_status,
                        "notes": version_notes
                    })

                # Update metadata
                if release_metadata:
                    for key, value in release_metadata.items():
                        release[key] = value

                # Log the status change
                if 'status_history' not in release:
                    release['status_history'] = []
                release['status_history'].append({
                    "from_status": old_status,
                    "to_status": new_status,
                    "changed_at": datetime.now().isoformat(),
                    "notes": version_notes
                })

                break

        if not release_found:
            return json.dumps({"error": f"Release with ID '{release_id}' not found."})

        return json.dumps({
            "success": True,
            "release_id": release_id,
            "old_status": old_status,
            "new_status": new_status,
            "updated_at": datetime.now().isoformat()
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_release_status",
                "description": "Updates release status and manages release workflow metadata including version notes and thread associations.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "release_id": {"type": "string", "description": "The ID of the release to update."},
                        "new_status": {"type": "string", "description": "The new status for the release. Must be one of: DRAFT, IN_REVIEW, APPROVED, PUBLISHED, ARCHIVED."},
                        "version_notes": {"type": "string", "description": "Optional notes about the version update or status change."},
                        "thread_id": {"type": "string", "description": "Optional Gmail thread ID to associate with the release."},
                        "release_metadata": {"type": "object", "description": "Additional metadata fields to update on the release."}
                    },
                    "required": ["release_id", "new_status"]
                }
            }
        }

class GetGmailThreadsByLabels(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Retrieves Gmail threads filtered by labels, sender, and other criteria.
        """
        thread_id = kwargs.get('thread_id')
        labels = kwargs.get('labels', [])
        sender_email = kwargs.get('sender_email')
        subject_keywords = kwargs.get('subject_keywords', [])
        created_after = kwargs.get('created_after')
        created_before = kwargs.get('created_before')

        gmail_threads = data.get('gmail_threads', [])

        # If thread_id is provided, return specific thread
        if thread_id:
            for thread in gmail_threads:
                if thread.get('thread_id') == thread_id:
                    return json.dumps(thread, indent=2)
            return json.dumps({"error": f"Thread with ID '{thread_id}' not found."})

        # Filter threads by criteria
        results = []
        for thread in gmail_threads:
            # Apply filters
            if labels:
                thread_labels = thread.get('current_labels', [])
                if not any(label in thread_labels for label in labels):
                    continue

            if sender_email:
                if thread.get('sender_identity') != sender_email:
                    continue

            if subject_keywords:
                subject = thread.get('subject', '').lower()
                if not any(keyword.lower() in subject for keyword in subject_keywords):
                    continue

            # Apply date filters
            if created_after:
                thread_created = thread.get('created_ts', '')
                if thread_created < created_after:
                    continue

            if created_before:
                thread_created = thread.get('created_ts', '')
                if thread_created > created_before:
                    continue

            results.append(thread)

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_gmail_threads_by_labels",
                "description": "Retrieves Gmail threads filtered by labels, sender email, subject keywords, and date ranges for comprehensive email workflow management.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "thread_id": {"type": "string", "description": "The ID of a specific thread to retrieve."},
                        "labels": {"type": "array", "items": {"type": "string"}, "description": "Filter by thread labels (e.g., ['design-review', 'urgent'])."},
                        "sender_email": {"type": "string", "description": "Filter by sender email address."},
                        "subject_keywords": {"type": "array", "items": {"type": "string"}, "description": "Filter by keywords in subject line."},
                        "created_after": {"type": "string", "description": "Filter threads created after this ISO timestamp."},
                        "created_before": {"type": "string", "description": "Filter threads created before this ISO timestamp."}
                    }
                }
            }
        }

class GetReleaseSummary(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Retrieves comprehensive release information and metrics.
        """
        release_id = kwargs.get('release_id')
        figma_file_id = kwargs.get('figma_file_id')
        owner_email = kwargs.get('owner_email')
        version_tag_pattern = kwargs.get('version_tag_pattern')
        status = kwargs.get('status')

        releases = data.get('releases', [])
        gmail_threads = data.get('gmail_threads', [])

        # If release_id is provided, return specific release
        if release_id:
            release_info = None
            for release in releases:
                if release.get('release_id') == release_id:
                    release_info = release
                    break

            if not release_info:
                return json.dumps({"error": f"Release with ID '{release_id}' not found."})

            # Enrich with thread information
            thread_id = release_info.get('thread_id_nullable')
            thread_info = None
            if thread_id:
                for thread in gmail_threads:
                    if thread.get('thread_id') == thread_id:
                        thread_info = thread
                        break

            summary = {
                "release_info": release_info,
                "thread_info": thread_info
            }

            return json.dumps(summary, indent=2)

        # Return summary across all releases
        all_releases = releases

        # Apply filters
        if figma_file_id:
            all_releases = [r for r in all_releases if r.get('figma_file_id') == figma_file_id]

        if owner_email:
            all_releases = [r for r in all_releases if r.get('owner_email') == owner_email]

        if version_tag_pattern:
            all_releases = [r for r in all_releases if version_tag_pattern in r.get('version_tag', '')]

        if status:
            all_releases = [r for r in all_releases if r.get('status') == status]

        summary = {
            "total_releases": len(all_releases),
            "by_owner": {},
            "by_file": {},
            "by_status": {},
            "releases": all_releases
        }

        # Group releases by owner
        for release in all_releases:
            owner = release.get('owner_email')
            if owner not in summary["by_owner"]:
                summary["by_owner"][owner] = 0
            summary["by_owner"][owner] += 1

            # Group by file
            file_id = release.get('figma_file_id')
            if file_id not in summary["by_file"]:
                summary["by_file"][file_id] = 0
            summary["by_file"][file_id] += 1

            # Group by status
            release_status = release.get('status', 'DRAFT')
            if release_status not in summary["by_status"]:
                summary["by_status"][release_status] = 0
            summary["by_status"][release_status] += 1

        return json.dumps(summary, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_release_summary",
                "description": "Retrieves comprehensive release information and metrics including owner distribution, file associations, and status breakdowns.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "release_id": {"type": "string", "description": "The ID of a specific release to retrieve details for."},
                        "figma_file_id": {"type": "string", "description": "Filter releases by Figma file ID."},
                        "owner_email": {"type": "string", "description": "Filter releases by owner email address."},
                        "version_tag_pattern": {"type": "string", "description": "Filter releases by version tag pattern (e.g., 'design-system')."},
                        "status": {"type": "string", "description": "Filter releases by status (e.g., 'PUBLISHED', 'DRAFT')."}
                    }
                }
            }
        }

class UpdateAssetExportStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Updates asset export status and manages export workflow metadata.
        """
        asset_id = kwargs.get('asset_id')
        new_status = kwargs.get('new_status')
        export_notes = kwargs.get('export_notes', '')
        dlp_scan_status = kwargs.get('dlp_scan_status')
        storage_ref = kwargs.get('storage_ref')

        if not all([asset_id, new_status]):
            return json.dumps({"error": "asset_id and new_status are required."})

        # Validate status values
        valid_statuses = ['PENDING', 'EXPORTING', 'COMPLETED', 'FAILED', 'ARCHIVED']
        if new_status not in valid_statuses:
            return json.dumps({"error": f"Invalid status. Must be one of: {', '.join(valid_statuses)}"})

        assets = data.get('assets', [])

        # Find the asset
        asset_found = False
        for asset in assets:
            if asset.get('asset_id') == asset_id:
                asset_found = True
                old_status = asset.get('export_status', 'PENDING')

                # Update asset status
                asset['export_status'] = new_status
                asset['last_updated'] = datetime.now().isoformat()

                # Update DLP scan status if provided
                if dlp_scan_status:
                    asset['dlp_scan_status'] = dlp_scan_status
                    asset['dlp_scan_timestamp'] = datetime.now().isoformat()

                # Update storage reference if provided
                if storage_ref:
                    asset['storage_ref'] = storage_ref

                # Add export notes
                if export_notes:
                    if 'export_history' not in asset:
                        asset['export_history'] = []
                    asset['export_history'].append({
                        "timestamp": datetime.now().isoformat(),
                        "status": new_status,
                        "notes": export_notes
                    })

                # Log the status change
                if 'status_history' not in asset:
                    asset['status_history'] = []
                asset['status_history'].append({
                    "from_status": old_status,
                    "to_status": new_status,
                    "changed_at": datetime.now().isoformat(),
                    "notes": export_notes
                })

                break

        if not asset_found:
            return json.dumps({"error": f"Asset with ID '{asset_id}' not found."})

        return json.dumps({
            "success": True,
            "asset_id": asset_id,
            "old_status": old_status,
            "new_status": new_status,
            "updated_at": datetime.now().isoformat()
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_asset_export_status",
                "description": "Updates asset export status and manages export workflow metadata including DLP scan status and storage references.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_id": {"type": "string", "description": "The ID of the asset to update."},
                        "new_status": {"type": "string", "description": "The new export status. Must be one of: PENDING, EXPORTING, COMPLETED, FAILED, ARCHIVED."},
                        "export_notes": {"type": "string", "description": "Optional notes about the export process or status change."},
                        "dlp_scan_status": {"type": "string", "description": "Optional DLP scan status update (e.g., 'CLEAN', 'FLAGGED', 'PENDING')."},
                        "storage_ref": {"type": "string", "description": "Optional new storage reference for the asset."}
                    },
                    "required": ["asset_id", "new_status"]
                }
            }
        }

class UpdateFigmaCommentStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Updates Figma comment status and manages comment workflow.
        """
        comment_id = kwargs.get('comment_id')
        new_status = kwargs.get('new_status')
        resolution_notes = kwargs.get('resolution_notes', '')
        assignee_email = kwargs.get('assignee_email')
        priority_level = kwargs.get('priority_level')

        if not all([comment_id, new_status]):
            return json.dumps({"error": "comment_id and new_status are required."})

        # Validate status values
        valid_statuses = ['OPEN', 'IN_PROGRESS', 'RESOLVED', 'CLOSED', 'ARCHIVED']
        if new_status not in valid_statuses:
            return json.dumps({"error": f"Invalid status. Must be one of: {', '.join(valid_statuses)}"})

        figma_comments = data.get('figma_comments', [])

        # Find the comment
        comment_found = False
        for comment in figma_comments:
            if comment.get('comment_id') == comment_id:
                comment_found = True
                old_status = comment.get('comment_status', 'OPEN')
                old_resolved = comment.get('resolved_flag', False)

                # Update comment status
                comment['comment_status'] = new_status
                comment['last_updated'] = datetime.now().isoformat()

                # Update resolved flag based on status
                if new_status in ['RESOLVED', 'CLOSED', 'ARCHIVED']:
                    comment['resolved_flag'] = True
                    comment['resolved_at'] = datetime.now().isoformat()
                else:
                    comment['resolved_flag'] = False

                # Update assignee if provided
                if assignee_email:
                    comment['assignee_email'] = assignee_email
                elif 'assignee_email' in comment:
                    del comment['assignee_email']

                # Update priority if provided
                if priority_level:
                    comment['priority_level'] = priority_level
                elif 'priority_level' in comment:
                    del comment['priority_level']

                # Add resolution notes
                if resolution_notes:
                    if 'resolution_history' not in comment:
                        comment['resolution_history'] = []
                    comment['resolution_history'].append({
                        "timestamp": datetime.now().isoformat(),
                        "status": new_status,
                        "notes": resolution_notes,
                        "assignee": assignee_email
                    })

                # Log the status change
                if 'status_history' not in comment:
                    comment['status_history'] = []
                comment['status_history'].append({
                    "from_status": old_status,
                    "to_status": new_status,
                    "resolved_changed": old_resolved != comment['resolved_flag'],
                    "changed_at": datetime.now().isoformat(),
                    "notes": resolution_notes
                })

                break

        if not comment_found:
            return json.dumps({"error": f"Comment with ID '{comment_id}' not found."})

        return json.dumps({
            "success": True,
            "comment_id": comment_id,
            "old_status": old_status,
            "new_status": new_status,
            "resolved_flag": comment['resolved_flag'],
            "updated_at": datetime.now().isoformat()
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_figma_comment_status",
                "description": "Updates Figma comment status and manages comment workflow including resolution tracking and assignment.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "comment_id": {"type": "string", "description": "The ID of the comment to update."},
                        "new_status": {"type": "string", "description": "The new comment status. Must be one of: OPEN, IN_PROGRESS, RESOLVED, CLOSED, ARCHIVED."},
                        "resolution_notes": {"type": "string", "description": "Optional notes about the resolution or status change."},
                        "assignee_email": {"type": "string", "description": "Optional email of the person assigned to handle the comment."},
                        "priority_level": {"type": "string", "description": "Optional priority level (e.g., 'LOW', 'MEDIUM', 'HIGH', 'CRITICAL')."}
                    },
                    "required": ["comment_id", "new_status"]
                }
            }
        }

class GetAssetExportSummary(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Retrieves comprehensive asset export information and metrics.
        """
        asset_id = kwargs.get('asset_id')
        artifact_id = kwargs.get('artifact_id')
        export_profile = kwargs.get('export_profile')
        dlp_scan_status = kwargs.get('dlp_scan_status')
        created_after = kwargs.get('created_after')
        created_before = kwargs.get('created_before')

        assets = data.get('assets', [])
        figma_artifacts = data.get('figma_artifacts', [])

        # If asset_id is provided, return specific asset
        if asset_id:
            asset_info = None
            for asset in assets:
                if asset.get('asset_id') == asset_id:
                    asset_info = asset
                    break

            if not asset_info:
                return json.dumps({"error": f"Asset with ID '{asset_id}' not found."})

            # Enrich with artifact information
            artifact_id_ref = asset_info.get('artifact_id_nullable')
            artifact_info = None
            if artifact_id_ref:
                for artifact in figma_artifacts:
                    if artifact.get('artifact_id') == artifact_id_ref:
                        artifact_info = artifact
                        break

            summary = {
                "asset_info": asset_info,
                "artifact_info": artifact_info
            }

            return json.dumps(summary, indent=2)

        # Return summary across all assets
        all_assets = assets

        # Apply filters
        if artifact_id:
            all_assets = [a for a in all_assets if a.get('artifact_id_nullable') == artifact_id]

        if export_profile:
            all_assets = [a for a in all_assets if a.get('export_profile') == export_profile]

        if dlp_scan_status:
            all_assets = [a for a in all_assets if a.get('dlp_scan_status') == dlp_scan_status]

        # Apply date filters
        if created_after:
            all_assets = [a for a in all_assets if a.get('created_ts', '') >= created_after]

        if created_before:
            all_assets = [a for a in all_assets if a.get('created_ts', '') <= created_before]

        summary = {
            "total_assets": len(all_assets),
            "by_profile": {},
            "by_artifact": {},
            "by_dlp_status": {},
            "total_file_size_bytes": sum(a.get('file_size_bytes', 0) for a in all_assets),
            "assets": all_assets
        }

        # Group assets by profile
        for asset in all_assets:
            profile = asset.get('export_profile')
            if profile not in summary["by_profile"]:
                summary["by_profile"][profile] = 0
            summary["by_profile"][profile] += 1

            # Group by artifact
            artifact_ref = asset.get('artifact_id_nullable')
            if artifact_ref not in summary["by_artifact"]:
                summary["by_artifact"][artifact_ref] = 0
            summary["by_artifact"][artifact_ref] += 1

            # Group by DLP status
            dlp_status = asset.get('dlp_scan_status', 'UNKNOWN')
            if dlp_status not in summary["by_dlp_status"]:
                summary["by_dlp_status"][dlp_status] = 0
            summary["by_dlp_status"][dlp_status] += 1

        return json.dumps(summary, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_asset_export_summary",
                "description": "Retrieves comprehensive asset export information and metrics including profile distribution, artifact associations, and DLP scan status breakdowns.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_id": {"type": "string", "description": "The ID of a specific asset to retrieve details for."},
                        "artifact_id": {"type": "string", "description": "Filter assets by associated artifact ID."},
                        "export_profile": {"type": "string", "description": "Filter assets by export profile (e.g., 'PNG 2x', 'SVG', 'PDF')."},
                        "dlp_scan_status": {"type": "string", "description": "Filter assets by DLP scan status (e.g., 'CLEAN', 'FLAGGED', 'PENDING')."},
                        "created_after": {"type": "string", "description": "Filter assets created after this ISO timestamp."},
                        "created_before": {"type": "string", "description": "Filter assets created before this ISO timestamp."}
                    }
                }
            }
        }

class GetFigmaCommentsByArtifact(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Retrieves Figma comments filtered by artifact, author, and other criteria.
        """
        comment_id = kwargs.get('comment_id')
        artifact_id = kwargs.get('artifact_id')
        author_email = kwargs.get('author_email')
        resolved_status = kwargs.get('resolved_status')
        content_keywords = kwargs.get('content_keywords', [])
        created_after = kwargs.get('created_after')
        created_before = kwargs.get('created_before')

        figma_comments = data.get('figma_comments', [])

        # If comment_id is provided, return specific comment
        if comment_id:
            for comment in figma_comments:
                if comment.get('comment_id') == comment_id:
                    return json.dumps(comment, indent=2)
            return json.dumps({"error": f"Comment with ID '{comment_id}' not found."})

        # Filter comments by criteria
        results = []
        for comment in figma_comments:
            # Apply filters
            if artifact_id:
                if comment.get('artifact_id') != artifact_id:
                    continue

            if author_email:
                if comment.get('author_email') != author_email:
                    continue

            if resolved_status is not None:
                if comment.get('resolved_flag') != resolved_status:
                    continue

            if content_keywords:
                content = comment.get('content', '').lower()
                if not any(keyword.lower() in content for keyword in content_keywords):
                    continue

            # Apply date filters
            if created_after:
                comment_created = comment.get('created_ts', '')
                if comment_created < created_after:
                    continue

            if created_before:
                comment_created = comment.get('created_ts', '')
                if comment_created > created_before:
                    continue

            results.append(comment)

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_figma_comments_by_artifact",
                "description": "Retrieves Figma comments filtered by artifact ID, author email, resolution status, content keywords, and date ranges for comprehensive comment management.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "comment_id": {"type": "string", "description": "The ID of a specific comment to retrieve."},
                        "artifact_id": {"type": "string", "description": "Filter comments by associated artifact ID."},
                        "author_email": {"type": "string", "description": "Filter comments by resolution status (true for resolved, false for unresolved)."},
                        "resolved_status": {"type": "boolean", "description": "Filter comments by resolution status (true for resolved, false for unresolved)."},
                        "content_keywords": {"type": "array", "items": {"type": "string"}, "description": "Filter comments by keywords in the content."},
                        "created_after": {"type": "string", "description": "Filter comments created after this ISO timestamp."},
                        "created_before": {"type": "string", "description": "Filter comments created before this ISO timestamp."}
                    }
                }
            }
        }

class UpdateSystemConfig(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Updates system configuration values for workflow management.
        """
        config_key = kwargs.get('config_key')
        config_value_json = kwargs.get('config_value_json')
        description = kwargs.get('description', '')
        config_category = kwargs.get('config_category')

        if not all([config_key, config_value_json]):
            return json.dumps({"error": "config_key and config_value_json are required."})

        system_config = data.get('system_config', [])

        # Find existing config or create new one
        config_found = False
        for config in system_config:
            if config.get('config_key') == config_key:
                config_found = True
                old_value = config.get('config_value_json')

                # Update config
                config['config_value_json'] = config_value_json
                config['last_updated'] = datetime.now().isoformat()

                # Add optional fields
                if description:
                    config['description'] = description
                if config_category:
                    config['category'] = config_category

                # Log the change
                if 'change_history' not in config:
                    config['change_history'] = []
                config['change_history'].append({
                    "timestamp": datetime.now().isoformat(),
                    "old_value": old_value,
                    "new_value": config_value_json,
                    "change_description": description
                })

                break

        # Create new config if not found
        if not config_found:
            new_config = {
                "config_key": config_key,
                "config_value_json": config_value_json,
                "created_at": datetime.now().isoformat(),
                "last_updated": datetime.now().isoformat()
            }

            if description:
                new_config['description'] = description
            if config_category:
                new_config['category'] = config_category

            new_config['change_history'] = [{
                "timestamp": datetime.now().isoformat(),
                "old_value": None,
                "new_value": config_value_json,
                "change_description": f"Created new config: {description}"
            }]

            system_config.append(new_config)

        return json.dumps({
            "success": True,
            "config_key": config_key,
            "updated_at": datetime.now().isoformat(),
            "action": "updated" if config_found else "created"
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_system_config",
                "description": "Updates system configuration values for workflow management including design system mappings, email templates, and SLA settings.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "config_key": {"type": "string", "description": "The configuration key to update (e.g., 'design_system_aliases', 'email_templates')."},
                        "config_value_json": {"type": "string", "description": "The JSON string value for the configuration."},
                        "description": {"type": "string", "description": "Optional description of the configuration change."},
                        "config_category": {"type": "string", "description": "Optional category for the configuration (e.g., 'workflow', 'email', 'system')."}
                    },
                    "required": ["config_key", "config_value_json"]
                }
            }
        }

class UpdateTerminalLogLevel(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Adds new terminal log entries and manages log retention.
        """
        message = kwargs.get('message')
        log_level = kwargs.get('log_level', 'INFO')
        source_component = kwargs.get('source_component')
        workflow_id = kwargs.get('workflow_id')
        max_log_entries = kwargs.get('max_log_entries', 1000)

        if not message:
            return json.dumps({"error": "message is required."})

        # Validate log level
        valid_levels = ['DEBUG', 'INFO', 'WARN', 'ERROR', 'CRITICAL']
        if log_level not in valid_levels:
            return json.dumps({"error": f"Invalid log_level. Must be one of: {', '.join(valid_levels)}"})

        terminal_logs = data.get('terminal_logs', [])

        # Create new log entry
        new_log_entry = {
            "log_ts": datetime.now().isoformat(),
            "message": f"{log_level}: {message}",
            "level": log_level,
            "component": source_component,
            "workflow_id": workflow_id
        }

        # Add entry to logs
        terminal_logs.append(new_log_entry)

        # Implement log retention - keep only the most recent entries
        if len(terminal_logs) > max_log_entries:
            # Sort by timestamp and keep the most recent
            terminal_logs.sort(key=lambda x: x.get('log_ts', ''))
            # Remove oldest entries
            excess_count = len(terminal_logs) - max_log_entries
            for _ in range(excess_count):
                terminal_logs.pop(0)

        return json.dumps({
            "success": True,
            "log_entry": new_log_entry,
            "total_log_entries": len(terminal_logs),
            "logged_at": datetime.now().isoformat()
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_terminal_log_level",
                "description": "Adds new terminal log entries with specified log levels and manages log retention for workflow tracking and debugging.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "message": {"type": "string", "description": "The log message to add."},
                        "log_level": {"type": "string", "description": "The log level. Must be one of: DEBUG, INFO, WARN, ERROR, CRITICAL."},
                        "source_component": {"type": "string", "description": "Optional component or service generating the log entry."},
                        "workflow_id": {"type": "string", "description": "Optional workflow ID to associate with the log entry."},
                        "max_log_entries": {"type": "integer", "description": "Maximum number of log entries to retain (default: 1000)."}
                    },
                    "required": ["message"]
                }
            }
        }

class GetSystemConfigByCategory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Retrieves system configuration entries filtered by category and key patterns.
        """
        config_key = kwargs.get('config_key')
        config_category = kwargs.get('config_category')
        key_pattern = kwargs.get('key_pattern')
        include_history = kwargs.get('include_history', False)

        system_config = data.get('system_config', [])

        # If config_key is provided, return specific config
        if config_key:
            for config in system_config:
                if config.get('config_key') == config_key:
                    config_copy = config.copy()
                    if not include_history and 'change_history' in config_copy:
                        del config_copy['change_history']
                    return json.dumps(config_copy, indent=2)
            return json.dumps({"error": f"Config with key '{config_key}' not found."})

        # Filter configs by criteria
        results = []
        for config in system_config:
            # Apply filters
            if config_category:
                if config.get('category') != config_category:
                    continue

            if key_pattern:
                if key_pattern.lower() not in config.get('config_key', '').lower():
                    continue

            config_copy = config.copy()
            if not include_history and 'change_history' in config_copy:
                del config_copy['change_history']

            results.append(config_copy)

        # Group results by category for summary
        summary = {
            "total_configs": len(results),
            "by_category": {},
            "configs": results
        }

        for config in results:
            category = config.get('category', 'uncategorized')
            if category not in summary["by_category"]:
                summary["by_category"][category] = 0
            summary["by_category"][category] += 1

        return json.dumps(summary, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_system_config_by_category",
                "description": "Retrieves system configuration entries filtered by category, key patterns, and optionally includes change history for workflow management.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "config_key": {"type": "string", "description": "The specific configuration key to retrieve."},
                        "config_category": {"type": "string", "description": "Filter configurations by category (e.g., 'workflow', 'email', 'system')."},
                        "key_pattern": {"type": "string", "description": "Filter configurations by key pattern (e.g., 'email' to find email-related configs)."},
                        "include_history": {"type": "boolean", "description": "Include change history in the results (default: false)."}
                    }
                }
            }
        }

class GetTerminalLogsSummary(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Retrieves terminal logs with filtering and summarization capabilities.
        """
        log_level = kwargs.get('log_level')
        source_component = kwargs.get('source_component')
        workflow_id = kwargs.get('workflow_id')
        message_keywords = kwargs.get('message_keywords', [])
        created_after = kwargs.get('created_after')
        created_before = kwargs.get('created_before')
        limit = kwargs.get('limit', 100)

        terminal_logs = data.get('terminal_logs', [])

        # Filter logs by criteria
        results = []
        for log in terminal_logs:
            # Apply filters
            if log_level:
                log_message = log.get('message', '')
                if not log_message.startswith(f"{log_level}:"):
                    continue

            if source_component:
                if log.get('component') != source_component:
                    continue

            if workflow_id:
                if log.get('workflow_id') != workflow_id:
                    continue

            if message_keywords:
                message = log.get('message', '').lower()
                if not any(keyword.lower() in message for keyword in message_keywords):
                    continue

            # Apply date filters
            if created_after:
                log_ts = log.get('log_ts', '')
                if log_ts < created_after:
                    continue

            if created_before:
                log_ts = log.get('log_ts', '')
                if log_ts > created_before:
                    continue

            results.append(log)

        # Sort by timestamp (most recent first) and apply limit
        results.sort(key=lambda x: x.get('log_ts', ''), reverse=True)
        if limit:
            results = results[:limit]

        # Create summary with log level distribution
        summary = {
            "total_matching_logs": len(results),
            "by_level": {},
            "by_component": {},
            "by_workflow": {},
            "logs": results
        }

        for log in results:
            # Extract log level from message
            message = log.get('message', '')
            level = 'UNKNOWN'
            for lvl in ['DEBUG', 'INFO', 'WARN', 'ERROR', 'CRITICAL']:
                if message.startswith(f"{lvl}:"):
                    level = lvl
                    break

            if level not in summary["by_level"]:
                summary["by_level"][level] = 0
            summary["by_level"][level] += 1

            # Group by component
            component = log.get('component', 'unknown')
            if component not in summary["by_component"]:
                summary["by_component"][component] = 0
            summary["by_component"][component] += 1

            # Group by workflow
            workflow = log.get('workflow_id', 'unknown')
            if workflow not in summary["by_workflow"]:
                summary["by_workflow"][workflow] = 0
            summary["by_workflow"][workflow] += 1

        return json.dumps(summary, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_terminal_logs_summary",
                "description": "Retrieves terminal logs with filtering and summarization capabilities including log level distribution, component breakdown, and workflow tracking.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "log_level": {"type": "string", "description": "Filter logs by level (e.g., 'INFO', 'ERROR', 'WARN')."},
                        "source_component": {"type": "string", "description": "Filter logs by source component or service."},
                        "workflow_id": {"type": "string", "description": "Filter logs by workflow ID."},
                        "message_keywords": {"type": "array", "items": {"type": "string"}, "description": "Filter logs by keywords in the message content."},
                        "created_after": {"type": "string", "description": "Filter logs created after this ISO timestamp."},
                        "created_before": {"type": "string", "description": "Filter logs created before this ISO timestamp."},
                        "limit": {"type": "integer", "description": "Maximum number of log entries to return (default: 100)."}
                    }
                }
            }
        }

class UpdateGmailMessageStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Updates Gmail message metadata and manages message workflow tracking.
        """
        message_id = kwargs.get('message_id')
        sender_email = kwargs.get('sender_email')
        body_html = kwargs.get('body_html')
        body_text_stripped = kwargs.get('body_text_stripped')
        attachments_asset_ids = kwargs.get('attachments_asset_ids', [])
        message_metadata = kwargs.get('message_metadata', {})

        if not message_id:
            return json.dumps({"error": "message_id is required."})

        gmail_messages = data.get('gmail_messages', [])

        # Find the message
        message_found = False
        for message in gmail_messages:
            if message.get('message_id') == message_id:
                message_found = True

                # Update message fields
                if sender_email:
                    message['sender_email'] = sender_email
                if body_html:
                    message['body_html'] = body_html
                if body_text_stripped:
                    message['body_text_stripped'] = body_text_stripped
                if attachments_asset_ids:
                    message['attachments_asset_ids'] = attachments_asset_ids

                message['last_updated'] = datetime.now().isoformat()

                # Add metadata
                if message_metadata:
                    for key, value in message_metadata.items():
                        message[key] = value

                # Log the update
                if 'update_history' not in message:
                    message['update_history'] = []
                message['update_history'].append({
                    "timestamp": datetime.now().isoformat(),
                    "updated_fields": list(kwargs.keys()),
                    "metadata": message_metadata
                })

                break

        if not message_found:
            return json.dumps({"error": f"Gmail message with ID '{message_id}' not found."})

        return json.dumps({
            "success": True,
            "message_id": message_id,
            "updated_at": datetime.now().isoformat(),
            "updated_fields": list(kwargs.keys())
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_gmail_message_status",
                "description": "Updates Gmail message metadata including sender, body content, attachments, and custom metadata for message workflow tracking.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "message_id": {"type": "string", "description": "The ID of the Gmail message to update."},
                        "sender_email": {"type": "string", "description": "Optional updated sender email address."},
                        "body_html": {"type": "string", "description": "Optional updated HTML body content."},
                        "body_text_stripped": {"type": "string", "description": "Optional updated plain text body content."},
                        "attachments_asset_ids": {"type": "array", "items": {"type": "string"}, "description": "Optional updated list of attachment asset IDs."},
                        "message_metadata": {"type": "object", "description": "Optional additional metadata fields for the message."}
                    },
                    "required": ["message_id"]
                }
            }
        }

class UpdateFixPlanStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Updates fix plan status and manages fix plan lifecycle workflow.
        """
        plan_id = kwargs.get('plan_id')
        new_status = kwargs.get('new_status')
        owner_email = kwargs.get('owner_email')
        delivery_method = kwargs.get('delivery_method')
        delivery_notes = kwargs.get('delivery_notes', '')

        if not all([plan_id, new_status]):
            return json.dumps({"error": "plan_id and new_status are required."})

        # Validate status values
        valid_statuses = ['DRAFTED', 'IN_PROGRESS', 'DELIVERED', 'ARCHIVED']
        if new_status not in valid_statuses:
            return json.dumps({"error": f"Invalid status. Must be one of: {', '.join(valid_statuses)}"})

        # Validate delivery method if provided
        valid_delivery_methods = ['COMMENTS', 'TICKETS', 'PDF']
        if delivery_method and delivery_method not in valid_delivery_methods:
            return json.dumps({"error": f"Invalid delivery_method. Must be one of: {', '.join(valid_delivery_methods)}"})

        fix_plans = data.get('fix_plans', [])

        # Find the fix plan
        plan_found = False
        for plan in fix_plans:
            if plan.get('plan_id') == plan_id:
                plan_found = True
                old_status = plan.get('status')

                # Update plan status
                plan['status'] = new_status
                plan['last_updated'] = datetime.now().isoformat()

                # Update owner if provided
                if owner_email:
                    plan['owner_email'] = owner_email

                # Update delivery method if provided
                if delivery_method:
                    plan['delivery_method'] = delivery_method

                # Handle status-specific logic
                if new_status == 'DELIVERED':
                    plan['delivered_at'] = datetime.now().isoformat()
                    if delivery_notes:
                        plan['delivery_notes'] = delivery_notes

                elif new_status == 'ARCHIVED':
                    plan['archived_at'] = datetime.now().isoformat()
                    if delivery_notes:
                        plan['archive_reason'] = delivery_notes

                # Log the status change
                if 'status_history' not in plan:
                    plan['status_history'] = []
                plan['status_history'].append({
                    "from_status": old_status,
                    "to_status": new_status,
                    "changed_at": datetime.now().isoformat(),
                    "notes": delivery_notes,
                    "delivery_method": delivery_method
                })

                break

        if not plan_found:
            return json.dumps({"error": f"Fix plan with ID '{plan_id}' not found."})

        return json.dumps({
            "success": True,
            "plan_id": plan_id,
            "old_status": old_status,
            "new_status": new_status,
            "updated_at": datetime.now().isoformat()
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_fix_plan_status",
                "description": "Updates fix plan status and manages fix plan lifecycle workflow including delivery method and ownership tracking.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {"type": "string", "description": "The ID of the fix plan to update."},
                        "new_status": {"type": "string", "description": "The new status for the fix plan. Must be one of: DRAFTED, IN_PROGRESS, DELIVERED, ARCHIVED."},
                        "owner_email": {"type": "string", "description": "Optional updated owner email address."},
                        "delivery_method": {"type": "string", "description": "Optional delivery method. Must be one of: COMMENTS, TICKETS, PDF."},
                        "delivery_notes": {"type": "string", "description": "Optional notes about the delivery or status change."}
                    },
                    "required": ["plan_id", "new_status"]
                }
            }
        }

class GetGmailMessagesByThread(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Retrieves Gmail messages filtered by thread ID, sender, and other criteria.
        """
        message_id = kwargs.get('message_id')
        thread_id = kwargs.get('thread_id')
        sender_email = kwargs.get('sender_email')
        content_keywords = kwargs.get('content_keywords', [])
        has_attachments = kwargs.get('has_attachments')
        sent_after = kwargs.get('sent_after')
        sent_before = kwargs.get('sent_before')

        gmail_messages = data.get('gmail_messages', [])

        # If message_id is provided, return specific message
        if message_id:
            for message in gmail_messages:
                if message.get('message_id') == message_id:
                    return json.dumps(message, indent=2)
            return json.dumps({"error": f"Message with ID '{message_id}' not found."})

        # Filter messages by criteria
        results = []
        for message in gmail_messages:
            # Apply filters
            if thread_id:
                if message.get('thread_id') != thread_id:
                    continue

            if sender_email:
                if message.get('sender_email') != sender_email:
                    continue

            if content_keywords:
                content = message.get('body_text_stripped', '').lower()
                if not any(keyword.lower() in content for keyword in content_keywords):
                    continue

            if has_attachments is not None:
                attachments = message.get('attachments_asset_ids', [])
                if has_attachments and not attachments:
                    continue
                if not has_attachments and attachments:
                    continue

            # Apply date filters
            if sent_after:
                sent_ts = message.get('sent_ts', '')
                if sent_ts < sent_after:
                    continue

            if sent_before:
                sent_ts = message.get('sent_ts', '')
                if sent_ts > sent_before:
                    continue

            results.append(message)

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_gmail_messages_by_thread",
                "description": "Retrieves Gmail messages filtered by thread ID, sender email, content keywords, attachment status, and date ranges for comprehensive message management.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "message_id": {"type": "string", "description": "The ID of a specific message to retrieve."},
                        "thread_id": {"type": "string", "description": "Filter messages by thread ID."},
                        "sender_email": {"type": "string", "description": "Filter messages by sender email address."},
                        "content_keywords": {"type": "array", "items": {"type": "string"}, "description": "Filter messages by keywords in the content."},
                        "has_attachments": {"type": "boolean", "description": "Filter messages by attachment presence (true for messages with attachments, false for without)."},
                        "sent_after": {"type": "string", "description": "Filter messages sent after this ISO timestamp."},
                        "sent_before": {"type": "string", "description": "Filter messages sent before this ISO timestamp."}
                    }
                }
            }
        }

class GetReleaseDiffSummary(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Retrieves release diff information and change summaries between releases.
        """
        diff_id = kwargs.get('diff_id')
        release_id = kwargs.get('release_id')
        component_filter = kwargs.get('component_filter')
        change_type = kwargs.get('change_type')
        include_changelog = kwargs.get('include_changelog', True)

        release_diffs = data.get('release_diffs', [])
        releases = data.get('releases', [])

        # If diff_id is provided, return specific diff
        if diff_id:
            diff_info = None
            for diff in release_diffs:
                if diff.get('diff_id') == diff_id:
                    diff_info = diff
                    break

            if not diff_info:
                return json.dumps({"error": f"Release diff with ID '{diff_id}' not found."})

            # Enrich with release information
            release_info = None
            for release in releases:
                if release.get('release_id') == diff_info.get('release_id'):
                    release_info = release
                    break

            summary = {
                "diff_info": diff_info,
                "release_info": release_info,
                "change_summary": {
                    "frames_added": len(diff_info.get('frames_added', [])),
                    "frames_updated": len(diff_info.get('frames_updated', [])),
                    "frames_removed": len(diff_info.get('frames_removed', [])),
                    "component_versions": len(diff_info.get('component_version_bumps', []))
                }
            }

            return json.dumps(summary, indent=2)

        # Filter diffs by criteria
        results = []
        for diff in release_diffs:
            # Apply filters
            if release_id:
                if diff.get('release_id') != release_id:
                    continue

            if component_filter:
                components = diff.get('component_version_bumps', [])
                if not any(component_filter.lower() in comp.lower() for comp in components):
                    continue

            if change_type:
                if change_type == 'added' and not diff.get('frames_added', []):
                    continue
                elif change_type == 'updated' and not diff.get('frames_updated', []):
                    continue
                elif change_type == 'removed' and not diff.get('frames_removed', []):
                    continue

            # Enrich with change summary
            diff_copy = diff.copy()
            diff_copy['change_summary'] = {
                "frames_added": len(diff.get('frames_added', [])),
                "frames_updated": len(diff.get('frames_updated', [])),
                "frames_removed": len(diff.get('frames_removed', [])),
                "component_versions": len(diff.get('component_version_bumps', []))
            }

            if not include_changelog:
                diff_copy.pop('changelog_highlights', None)

            results.append(diff_copy)

        summary = {
            "total_diffs": len(results),
            "aggregate_changes": {
                "total_frames_added": sum(len(d.get('frames_added', [])) for d in results),
                "total_frames_updated": sum(len(d.get('frames_updated', [])) for d in results),
                "total_frames_removed": sum(len(d.get('frames_removed', [])) for d in results),
                "total_component_bumps": sum(len(d.get('component_version_bumps', [])) for d in results)
            },
            "diffs": results
        }

        return json.dumps(summary, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_release_diff_summary",
                "description": "Retrieves release diff information and change summaries between releases including frame changes, component updates, and changelog highlights.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "diff_id": {"type": "string", "description": "The ID of a specific release diff to retrieve."},
                        "release_id": {"type": "string", "description": "Filter diffs by associated release ID."},
                        "component_filter": {"type": "string", "description": "Filter diffs by component name pattern (e.g., 'Button' to find button-related changes)."},
                        "change_type": {"type": "string", "description": "Filter diffs by change type ('added', 'updated', or 'removed')."},
                        "include_changelog": {"type": "boolean", "description": "Include changelog highlights in the results (default: true)."}
                    }
                }
            }
        }

class UpdateAuditReportStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Updates audit report status and manages audit completion workflow.
        """
        audit_id = kwargs.get('audit_id')
        new_status = kwargs.get('new_status')
        report_asset_id = kwargs.get('report_asset_id')
        completion_notes = kwargs.get('completion_notes', '')

        if not all([audit_id, new_status]):
            return json.dumps({"error": "audit_id and new_status are required."})

        # Validate status values
        valid_statuses = ['RUNNING', 'COMPLETED', 'FAILED', 'CANCELLED']
        if new_status not in valid_statuses:
            return json.dumps({"error": f"Invalid status. Must be one of: {', '.join(valid_statuses)}"})

        audits = data.get('audits', [])

        # Find the audit
        audit_found = False
        for audit in audits:
            if audit.get('audit_id') == audit_id:
                audit_found = True
                old_status = audit.get('status')

                # Update audit status
                audit['status'] = new_status
                audit['last_updated'] = datetime.now().isoformat()

                # Handle status-specific logic
                if new_status == 'COMPLETED':
                    audit['completed_at'] = datetime.now().isoformat()
                    if report_asset_id:
                        audit['report_asset_id_nullable'] = report_asset_id

                elif new_status == 'FAILED':
                    audit['failed_at'] = datetime.now().isoformat()
                    if completion_notes:
                        audit['failure_reason'] = completion_notes

                # Log the status change
                if 'status_history' not in audit:
                    audit['status_history'] = []
                audit['status_history'].append({
                    "from_status": old_status,
                    "to_status": new_status,
                    "changed_at": datetime.now().isoformat(),
                    "notes": completion_notes
                })

                break

        if not audit_found:
            return json.dumps({"error": f"Audit with ID '{audit_id}' not found."})

        return json.dumps({
            "success": True,
            "audit_id": audit_id,
            "old_status": old_status,
            "new_status": new_status,
            "updated_at": datetime.now().isoformat()
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_audit_report_status",
                "description": "Updates audit report status and manages audit completion workflow including report asset associations.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string", "description": "The ID of the audit to update."},
                        "new_status": {"type": "string", "description": "The new status for the audit. Must be one of: RUNNING, COMPLETED, FAILED, CANCELLED."},
                        "report_asset_id": {"type": "string", "description": "Optional asset ID for the generated report."},
                        "completion_notes": {"type": "string", "description": "Optional notes about the completion or failure."}
                    },
                    "required": ["audit_id", "new_status"]
                }
            }
        }

class UpdateGmailThreadPriority(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Updates Gmail thread priority and manages thread workflow urgency.
        """
        thread_id = kwargs.get('thread_id')
        new_priority = kwargs.get('new_priority')
        urgency_reason = kwargs.get('urgency_reason', '')
        escalate_to = kwargs.get('escalate_to', [])

        if not all([thread_id, new_priority]):
            return json.dumps({"error": "thread_id and new_priority are required."})

        # Validate priority values
        valid_priorities = ['LOW', 'NORMAL', 'HIGH', 'URGENT', 'CRITICAL']
        if new_priority not in valid_priorities:
            return json.dumps({"error": f"Invalid priority. Must be one of: {', '.join(valid_priorities)}"})

        gmail_threads = data.get('gmail_threads', [])

        # Find the thread
        thread_found = False
        for thread in gmail_threads:
            if thread.get('thread_id') == thread_id:
                thread_found = True
                old_priority = thread.get('priority', 'NORMAL')

                # Update thread priority
                thread['priority'] = new_priority
                thread['updated_ts'] = datetime.now().isoformat()

                # Handle high priority logic
                if new_priority in ['HIGH', 'URGENT', 'CRITICAL']:
                    thread['escalated_at'] = datetime.now().isoformat()
                    if urgency_reason:
                        thread['urgency_reason'] = urgency_reason
                    if escalate_to:
                        # Add escalation recipients to existing recipients
                        current_recipients = thread.get('recipients', [])
                        for recipient in escalate_to:
                            if recipient not in current_recipients:
                                current_recipients.append(recipient)
                        thread['recipients'] = current_recipients

                # Log the priority change
                if 'priority_history' not in thread:
                    thread['priority_history'] = []
                thread['priority_history'].append({
                    "from_priority": old_priority,
                    "to_priority": new_priority,
                    "changed_at": datetime.now().isoformat(),
                    "reason": urgency_reason
                })

                break

        if not thread_found:
            return json.dumps({"error": f"Gmail thread with ID '{thread_id}' not found."})

        return json.dumps({
            "success": True,
            "thread_id": thread_id,
            "old_priority": old_priority,
            "new_priority": new_priority,
            "updated_at": datetime.now().isoformat()
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_gmail_thread_priority",
                "description": "Updates Gmail thread priority and manages thread workflow urgency including escalation to additional recipients.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "thread_id": {"type": "string", "description": "The ID of the Gmail thread to update."},
                        "new_priority": {"type": "string", "description": "The new priority level. Must be one of: LOW, NORMAL, HIGH, URGENT, CRITICAL."},
                        "urgency_reason": {"type": "string", "description": "Optional reason for the priority change."},
                        "escalate_to": {"type": "array", "items": {"type": "string"}, "description": "Optional list of additional recipients to escalate to for high priority threads."}
                    },
                    "required": ["thread_id", "new_priority"]
                }
            }
        }
# New tool 1: Update Audit Status
class UpdateAuditStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Updates the status of an audit and manages audit workflow state.
        """
        audit_id = kwargs.get('audit_id')
        new_status = kwargs.get('new_status')
        notes = kwargs.get('notes', '')

        if not audit_id or not new_status:
            return json.dumps({"error": "audit_id and new_status are required"})

        audits = data.get('audits', [])
        for audit in audits:
            if audit.get('audit_id') == audit_id:
                old_status = audit.get('status')
                audit['status'] = new_status
                audit['last_updated'] = datetime.now().isoformat()

                # Add to audit history if not exists
                if 'history' not in audit:
                    audit['history'] = []
                audit['history'].append({
                    "timestamp": datetime.now().isoformat(),
                    "status": new_status,
                    "notes": notes
                })

                return json.dumps({
                    "success": True,
                    "audit_id": audit_id,
                    "old_status": old_status,
                    "new_status": new_status,
                    "updated_at": datetime.now().isoformat()
                })

        return json.dumps({"error": f"Audit with ID {audit_id} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_audit_status",
                "description": "Updates the status of an audit and manages audit workflow state transitions.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {
                            "type": "string",
                            "description": "The ID of the audit to update"
                        },
                        "new_status": {
                            "type": "string",
                            "description": "New status for the audit (e.g., 'IN_PROGRESS', 'COMPLETED', 'FAILED')"
                        },
                        "notes": {
                            "type": "string",
                            "description": "Optional notes about the status change"
                        }
                    },
                    "required": ["audit_id", "new_status"]
                }
            }
        }

# New tool 2: Update Fix Item Priority
class UpdateFixItemPriority(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Updates the priority of a fix item in a fix plan.
        """
        fix_item_id = kwargs.get('fix_item_id')
        new_priority = kwargs.get('new_priority')
        reason = kwargs.get('reason', '')

        if not fix_item_id or new_priority is None:
            return json.dumps({"error": "fix_item_id and new_priority are required"})

        fix_items = data.get('fix_items', [])
        for item in fix_items:
            if item.get('fix_item_id') == fix_item_id:
                old_priority = item.get('priority')
                item['priority'] = new_priority
                item['last_updated'] = datetime.now().isoformat()

                # Add to history if not exists
                if 'history' not in item:
                    item['history'] = []
                item['history'].append({
                    "timestamp": datetime.now().isoformat(),
                    "field": "priority",
                    "old_value": old_priority,
                    "new_value": new_priority,
                    "reason": reason
                })

                return json.dumps({
                    "success": True,
                    "fix_item_id": fix_item_id,
                    "old_priority": old_priority,
                    "new_priority": new_priority,
                    "updated_at": datetime.now().isoformat()
                })

        return json.dumps({"error": f"Fix item with ID {fix_item_id} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_fix_item_priority",
                "description": "Updates the priority of a fix item in a fix plan.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "fix_item_id": {
                            "type": "string",
                            "description": "The ID of the fix item to update"
                        },
                        "new_priority": {
                            "type": "integer",
                            "description": "New priority level (1=highest, 5=lowest)"
                        },
                        "reason": {
                            "type": "string",
                            "description": "Optional reason for the priority change"
                        }
                    },
                    "required": ["fix_item_id", "new_priority"]
                }
            }
        }

# New tool 3: Get Audit Summary
class GetAuditSummary(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Retrieves a summary of audit findings and metrics.
        """
        audit_id = kwargs.get('audit_id')
        status = kwargs.get('status')
        audit_type = kwargs.get('type')

        audits = data.get('audits', [])
        findings_ds = data.get('audit_findings_ds', [])
        findings_a11y = data.get('audit_findings_a11y', [])

        results = []
        for audit in audits:
            if (audit_id and audit.get('audit_id') != audit_id) or \
               (status and audit.get('status') != status) or \
               (audit_type and audit.get('type') != audit_type):
                continue

            audit_id = audit['audit_id']
            ds_findings = [f for f in findings_ds if f.get('audit_id') == audit_id]
            a11y_findings = [f for f in findings_a11y if f.get('audit_id') == audit_id]

            summary = {
                "audit_id": audit_id,
                "name": audit.get('name'),
                "status": audit.get('status'),
                "type": audit.get('type'),
                "total_findings": len(ds_findings) + len(a11y_findings),
                "ds_findings": {
                    "total": len(ds_findings),
                    "by_severity": {}
                },
                "a11y_findings": {
                    "total": len(a11y_findings),
                    "by_violation_type": {}
                },
                "started_at": audit.get('started_at'),
                "completed_at": audit.get('completed_at')
            }

            # Count by severity for design system findings
            for finding in ds_findings:
                severity = finding.get('severity', 'UNKNOWN')
                summary["ds_findings"]["by_severity"][severity] = \
                    summary["ds_findings"]["by_severity"].get(severity, 0) + 1

            # Count by violation type for accessibility findings
            for finding in a11y_findings:
                v_type = finding.get('violation_type', 'UNKNOWN')
                summary["a11y_findings"]["by_violation_type"][v_type] = \
                    summary["a11y_findings"]["by_violation_type"].get(v_type, 0) + 1

            results.append(summary)

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_audit_summary",
                "description": "Retrieves a summary of audit findings and metrics.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {
                            "type": "string",
                            "description": "Filter by specific audit ID"
                        },
                        "status": {
                            "type": "string",
                            "description": "Filter by audit status (e.g., 'IN_PROGRESS', 'COMPLETED')"
                        },
                        "type": {
                            "type": "string",
                            "description": "Filter by audit type (e.g., 'DESIGN_SYSTEM', 'ACCESSIBILITY')"
                        }
                    }
                }
            }
        }

# New tool 4: Get Fix Plan Items
class GetFixPlanById(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Retrieves a specific fix plan by its ID with detailed information.
        """
        plan_id = kwargs.get('plan_id')
        include_items = kwargs.get('include_items', True)

        if not plan_id:
            return json.dumps({"error": "plan_id is required"})

        fix_plans = data.get('fix_plans', [])
        fix_items = data.get('fix_items', [])

        # Find the requested fix plan
        plan = next((p for p in fix_plans if p.get('plan_id') == plan_id), None)
        if not plan:
            return json.dumps({"error": f"Fix plan with ID '{plan_id}' not found"})

        result = dict(plan)  # Create a copy of the plan

        # Include related items if requested
        if include_items:
            result['items'] = [
                item for item in fix_items
                if item.get('plan_id') == plan_id
            ]

        # Add additional metadata
        result['item_count'] = len(result.get('items', []))
        result['open_item_count'] = len([i for i in result.get('items', [])
                                       if i.get('status') != 'RESOLVED'])

        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_fix_plan_by_id",
                "description": "Retrieves a specific fix plan by its ID with detailed information.",
                "parameters": {
                    "type": "object",
                    "required": ["plan_id"],
                    "properties": {
                        "plan_id": {
                            "type": "string",
                            "description": "The ID of the fix plan to retrieve"
                        },
                        "include_items": {
                            "type": "boolean",
                            "default": True,
                            "description": "Whether to include the fix items in the response"
                        }
                    }
                }
            }
        }

class GetFixPlanItems(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Retrieves fix items for one or more fix plans with filtering options.
        """
        plan_ids = kwargs.get('plan_ids', [])
        status_filter = kwargs.get('status')
        severity_filter = kwargs.get('severity')
        include_resolved = kwargs.get('include_resolved', False)
        limit = kwargs.get('limit', 50)

        if not plan_ids and 'plan_id' in kwargs:
            plan_ids = [kwargs['plan_id']]

        if not plan_ids:
            return json.dumps({"error": "At least one plan_id is required"})

        fix_plans = data.get('fix_plans', [])
        fix_items = data.get('fix_items', [])

        result = []
        for plan_id in plan_ids:
            plan = next((p for p in fix_plans if p.get('plan_id') == plan_id), None)
            if not plan:
                continue

            plan_items = [
                item for item in fix_items
                if item.get('plan_id') == plan_id and
                   (include_resolved or item.get('status') != 'RESOLVED')
            ]

            if status_filter:
                plan_items = [item for item in plan_items if item.get('status') == status_filter]
            if severity_filter:
                plan_items = [item for item in plan_items if item.get('severity') == severity_filter]

            if plan_items:
                result.append({
                    'plan_id': plan_id,
                    'plan_name': plan.get('name', ''),
                    'status': plan.get('status', ''),
                    'items': plan_items[:limit]
                })

        return json.dumps({
            'total_plans': len(result),
            'total_items': sum(len(plan['items']) for plan in result),
            'plans': result
        }, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "get_fix_plan_items",
                "description": "Retrieves fix items for one or more fix plans with filtering options.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of fix plan IDs to retrieve items for"
                        },
                        "plan_id": {
                            "type": "string",
                            "description": "Single fix plan ID (alternative to plan_ids)"
                        },
                        "status": {
                            "type": "string",
                            "description": "Filter items by status (e.g., 'OPEN', 'IN_PROGRESS', 'RESOLVED')"
                        },
                        "severity": {
                            "type": "string",
                            "description": "Filter items by severity (e.g., 'LOW', 'MEDIUM', 'HIGH', 'CRITICAL')"
                        },
                        "include_resolved": {
                            "type": "boolean",
                            "default": False,
                            "description": "Include resolved items in results"
                        },
                        "limit": {
                            "type": "integer",
                            "default": 50,
                            "description": "Maximum number of items to return per plan"
                        }
                    },
                    "anyOf": [
                        {"required": ["plan_ids"]},
                        {"required": ["plan_id"]}
                    ]
                }
            }
        }

class GetAuditsByStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Retrieves audits filtered by status, type, and other criteria.
        """
        audit_id = kwargs.get('audit_id')
        status = kwargs.get('status')
        audit_type = kwargs.get('audit_type')
        artifact_id = kwargs.get('artifact_id')
        created_after = kwargs.get('created_after')
        created_before = kwargs.get('created_before')

        audits = data.get('audits', [])

        # If audit_id is provided, return specific audit
        if audit_id:
            for audit in audits:
                if audit.get('audit_id') == audit_id:
                    return json.dumps(audit, indent=2)
            return json.dumps({"error": f"Audit with ID '{audit_id}' not found."})

        # Filter audits by criteria
        results = []
        for audit in audits:
            # Apply filters
            if status:
                if audit.get('status') != status:
                    continue

            if audit_type:
                if audit.get('audit_type') != audit_type:
                    continue

            if artifact_id:
                if audit.get('artifact_id') != artifact_id:
                    continue

            # Apply date filters
            if created_after:
                audit_created = audit.get('created_ts', '')
                if audit_created < created_after:
                    continue

            if created_before:
                audit_created = audit.get('created_ts', '')
                if audit_created > created_before:
                    continue

            results.append(audit)

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_audits_by_status",
                "description": "Retrieves audits filtered by status, type, artifact association, and date ranges for comprehensive audit management.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string", "description": "The ID of a specific audit to retrieve."},
                        "status": {"type": "string", "description": "Filter audits by status (e.g., 'RUNNING', 'COMPLETED', 'FAILED')."},
                        "audit_type": {"type": "string", "description": "Filter audits by type (e.g., 'COMBINED_DS_A11Y', 'A11Y', 'DS')."},
                        "artifact_id": {"type": "string", "description": "Filter audits by associated artifact ID."},
                        "created_after": {"type": "string", "description": "Filter audits created after this ISO timestamp."},
                        "created_before": {"type": "string", "description": "Filter audits created before this ISO timestamp."}
                    }
                }
            }
        }

class GetReviewApprovalsSummary(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Retrieves review approvals with filtering and summary capabilities.
        """
        approval_id = kwargs.get('approval_id')
        cycle_id = kwargs.get('cycle_id')
        approver_id = kwargs.get('approver_id')
        approval_status = kwargs.get('approval_status')
        approved_after = kwargs.get('approved_after')
        approved_before = kwargs.get('approved_before')

        review_approvals = data.get('review_approvals', [])
        review_cycles = data.get('review_cycles', [])

        # If approval_id is provided, return specific approval
        if approval_id:
            for approval in review_approvals:
                if approval.get('approval_id') == approval_id:
                    # Enrich with cycle information
                    approval_copy = approval.copy()
                    cycle_id_ref = approval.get('cycle_id')
                    if cycle_id_ref:
                        for cycle in review_cycles:
                            if cycle.get('cycle_id') == cycle_id_ref:
                                approval_copy['review_cycle'] = cycle
                                break
                    return json.dumps(approval_copy, indent=2)
            return json.dumps({"error": f"Approval with ID '{approval_id}' not found."})

        # Filter approvals by criteria
        results = []
        for approval in review_approvals:
            # Apply filters
            if cycle_id:
                if approval.get('cycle_id') != cycle_id:
                    continue

            if approver_id:
                if approval.get('approver_id') != approver_id:
                    continue

            if approval_status:
                if approval.get('status') != approval_status:
                    continue

            # Apply date filters
            if approved_after:
                approval_date = approval.get('approval_date', '')
                if approval_date < approved_after:
                    continue

            if approved_before:
                approval_date = approval.get('approval_date', '')
                if approval_date > approved_before:
                    continue

            # Enrich with cycle information
            approval_copy = approval.copy()
            cycle_id_ref = approval.get('cycle_id')
            if cycle_id_ref:
                for cycle in review_cycles:
                    if cycle.get('cycle_id') == cycle_id_ref:
                        approval_copy['review_cycle'] = cycle
                        break

            results.append(approval_copy)

        # Create summary
        summary = {
            "total_approvals": len(results),
            "by_status": {},
            "by_approver": {},
            "approvals": results
        }

        # Group by status and approver
        for approval in results:
            status = approval.get('status', 'UNKNOWN')
            if status not in summary["by_status"]:
                summary["by_status"][status] = 0
            summary["by_status"][status] += 1

            approver = approval.get('approver_id', 'unknown')
            if approver not in summary["by_approver"]:
                summary["by_approver"][approver] = 0
            summary["by_approver"][approver] += 1

        return json.dumps(summary, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_review_approvals_summary",
                "description": "Retrieves review approvals with filtering and summary capabilities including status distribution and approver breakdown.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "approval_id": {"type": "string", "description": "The ID of a specific approval to retrieve."},
                        "cycle_id": {"type": "string", "description": "Filter approvals by review cycle ID."},
                        "approver_id": {"type": "string", "description": "Filter approvals by approver ID."},
                        "approval_status": {"type": "string", "description": "Filter approvals by status (e.g., 'APPROVED', 'REJECTED')."},
                        "approved_after": {"type": "string", "description": "Filter approvals made after this ISO timestamp."},
                        "approved_before": {"type": "string", "description": "Filter approvals made before this ISO timestamp."}
                    }
                }
            }
        }

class UpdateReleaseVersion(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Updates release version information and manages release lifecycle.
        """
        release_id = kwargs.get('release_id')
        version_id = kwargs.get('version_id')
        release_name = kwargs.get('release_name')
        owner_email = kwargs.get('owner_email')
        thread_id = kwargs.get('thread_id')

        if not all([release_id, version_id]):
            return json.dumps({"error": "release_id and version_id are required."})

        releases = data.get('releases', [])

        # Find the release
        release_found = False
        for release in releases:
            if release.get('release_id') == release_id:
                release_found = True
                old_version = release.get('version_id')

                # Update release information
                release['version_id'] = version_id
                release['last_updated'] = datetime.now().isoformat()

                # Update optional fields if provided
                if release_name:
                    release['release_name'] = release_name
                if owner_email:
                    release['owner_email'] = owner_email
                if thread_id:
                    release['thread_id_nullable'] = thread_id

                # Log the version change
                if 'version_history' not in release:
                    release['version_history'] = []
                release['version_history'].append({
                    "from_version": old_version,
                    "to_version": version_id,
                    "changed_at": datetime.now().isoformat()
                })

                break

        if not release_found:
            return json.dumps({"error": f"Release with ID '{release_id}' not found."})

        return json.dumps({
            "success": True,
            "release_id": release_id,
            "old_version": old_version,
            "new_version": version_id,
            "updated_at": datetime.now().isoformat()
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_release_version",
                "description": "Updates release version information and manages release lifecycle with optional metadata updates.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "release_id": {"type": "string", "description": "The ID of the release to update."},
                        "version_id": {"type": "string", "description": "The new version ID for the release."},
                        "release_name": {"type": "string", "description": "Optional new release name."},
                        "owner_email": {"type": "string", "description": "Optional new owner email."},
                        "thread_id": {"type": "string", "description": "Optional thread ID for release coordination."}
                    },
                    "required": ["release_id", "version_id"]
                }
            }
        }

class AddTerminalLogEntry(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Adds new terminal log entries and manages log level filtering.
        """
        log_message = kwargs.get('log_message')
        log_level = kwargs.get('log_level', 'INFO')
        component = kwargs.get('component')
        user_email = kwargs.get('user_email')

        if not log_message:
            return json.dumps({"error": "log_message is required."})

        # Validate log level
        valid_levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
        if log_level not in valid_levels:
            return json.dumps({"error": f"Invalid log level. Must be one of: {', '.join(valid_levels)}"})

        terminal_logs = data.get('terminal_logs', [])

        # Create new log entry
        new_log = {
            "log_ts": datetime.now().isoformat(),
            "message": f"{log_level}: {log_message}"
        }

        # Add optional metadata
        if component:
            new_log["component"] = component
        if user_email:
            new_log["user_email"] = user_email

        # Add to logs
        terminal_logs.append(new_log)

        return json.dumps({
            "success": True,
            "log_entry": new_log,
            "total_logs": len(terminal_logs)
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_terminal_log_entry",
                "description": "Adds new terminal log entries and manages log level filtering with optional metadata.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "log_message": {"type": "string", "description": "The log message content to add."},
                        "log_level": {"type": "string", "description": "The log level (DEBUG, INFO, WARNING, ERROR, CRITICAL). Default: INFO."},
                        "component": {"type": "string", "description": "Optional component name for the log entry."},
                        "user_email": {"type": "string", "description": "Optional user email associated with the log entry."}
                    },
                    "required": ["log_message"]
                }
            }
        }

class GetReleasesByOwner(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Retrieves releases filtered by owner and other criteria.
        """
        owner_email = kwargs.get('owner_email')
        release_id = kwargs.get('release_id')
        version_tag = kwargs.get('version_tag')
        created_after = kwargs.get('created_after')
        created_before = kwargs.get('created_before')

        if not owner_email:
            return json.dumps({"error": "owner_email is required."})

        releases = data.get('releases', [])

        # Filter releases by criteria
        results = []
        for release in releases:
            # Primary filter - owner email
            if release.get('owner_email') != owner_email:
                continue

            # Apply optional filters
            if release_id:
                if release.get('release_id') != release_id:
                    continue

            if version_tag:
                if version_tag not in release.get('version_tag', ''):
                    continue

            # Apply date filters
            if created_after:
                release_created = release.get('created_ts', '')
                if release_created < created_after:
                    continue

            if created_before:
                release_created = release.get('created_ts', '')
                if release_created > created_before:
                    continue

            results.append(release)

        # Create summary
        summary = {
            "owner_email": owner_email,
            "total_releases": len(results),
            "version_tags": list(set(r.get('version_tag', '') for r in results)),
            "releases": results
        }

        return json.dumps(summary, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_releases_by_owner",
                "description": "Retrieves releases filtered by owner email with optional filtering by release ID, version tag, and date ranges.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner_email": {"type": "string", "description": "The owner email to filter releases by."},
                        "release_id": {"type": "string", "description": "Optional specific release ID to retrieve."},
                        "version_tag": {"type": "string", "description": "Optional version tag pattern to filter by."},
                        "created_after": {"type": "string", "description": "Filter releases created after this ISO timestamp."},
                        "created_before": {"type": "string", "description": "Filter releases created before this ISO timestamp."}
                    },
                    "required": ["owner_email"]
                }
            }
        }

class GetFilteredLogEntries(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Retrieves terminal logs with filtering and summary capabilities.
        """
        log_level = kwargs.get('log_level')
        message_pattern = kwargs.get('message_pattern')
        after_timestamp = kwargs.get('after_timestamp')
        before_timestamp = kwargs.get('before_timestamp')
        component = kwargs.get('component')

        terminal_logs = data.get('terminal_logs', [])

        # Filter logs by criteria
        results = []
        for log in terminal_logs:
            # Apply log level filter
            if log_level:
                log_message = log.get('message', '')
                if not log_message.startswith(f"{log_level}:"):
                    continue

            # Apply message pattern filter
            if message_pattern:
                if message_pattern.lower() not in log.get('message', '').lower():
                    continue

            # Apply component filter
            if component:
                if log.get('component') != component:
                    continue

            # Apply timestamp filters
            if after_timestamp:
                log_time = log.get('log_ts', '')
                if log_time < after_timestamp:
                    continue

            if before_timestamp:
                log_time = log.get('log_ts', '')
                if log_time > before_timestamp:
                    continue

            results.append(log)

        # Create summary by log level
        level_counts = {}
        for log in results:
            message = log.get('message', '')
            level = message.split(':')[0] if ':' in message else 'UNKNOWN'
            level_counts[level] = level_counts.get(level, 0) + 1

        summary = {
            "total_logs": len(results),
            "level_breakdown": level_counts,
            "logs": results
        }

        return json.dumps(summary, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_filtered_log_entries",
                "description": "Retrieves terminal logs with filtering and summary capabilities including log level breakdown.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "log_level": {"type": "string", "description": "Filter logs by level (DEBUG, INFO, WARNING, ERROR, CRITICAL)."},
                        "message_pattern": {"type": "string", "description": "Filter logs containing this message pattern."},
                        "after_timestamp": {"type": "string", "description": "Filter logs after this ISO timestamp."},
                        "before_timestamp": {"type": "string", "description": "Filter logs before this ISO timestamp."},
                        "component": {"type": "string", "description": "Filter logs by component name."}
                    }
                }
            }
        }
# New Tool 1: Update Audit Status
class UpdateAuditStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Updates the status of an audit.
        """
        audit_id = kwargs.get('audit_id')
        new_status = kwargs.get('new_status')
        updated_by = kwargs.get('updated_by')
        notes = kwargs.get('notes', '')

        if not all([audit_id, new_status, updated_by]):
            return json.dumps({"error": "audit_id, new_status, and updated_by are required"})

        # Validate status values
        valid_statuses = ['DRAFT', 'IN_PROGRESS', 'PENDING_REVIEW', 'COMPLETED', 'ARCHIVED']
        if new_status not in valid_statuses:
            return json.dumps({"error": f"Invalid status. Must be one of: {', '.join(valid_statuses)}"})

        # Find and update the audit
        for audit in data.get('audits', []):
            if audit.get('audit_id') == audit_id:
                audit['status'] = new_status
                audit['last_updated'] = datetime.now().isoformat()
                audit['updated_by'] = updated_by
                if notes:
                    audit['notes'] = notes
                return json.dumps({"status": "success", "audit_id": audit_id, "new_status": new_status})

        return json.dumps({"error": f"Audit with ID {audit_id} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_audit_status",
                "description": "Updates the status of an audit.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string", "description": "The ID of the audit to update."},
                        "new_status": {"type": "string", "description": "The new status for the audit."},
                        "updated_by": {"type": "string", "description": "Email of the user updating the status."},
                        "notes": {"type": "string", "description": "Optional notes about the status update."}
                    },
                    "required": ["audit_id", "new_status", "updated_by"]
                }
            }
        }

# New Tool 2: Get Audit Summary
class GetAuditSummary(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Retrieves a summary of audit findings.
        """
        audit_id = kwargs.get('audit_id')

        if not audit_id:
            return json.dumps({"error": "audit_id is required"})

        # Find the audit
        for audit in data.get('audits', []):
            if audit.get('audit_id') == audit_id:
                # Count findings by severity
                findings = [f for f in data.get('audit_findings', []) if f.get('audit_id') == audit_id]
                severity_counts = {}
                for finding in findings:
                    severity = finding.get('severity', 'UNKNOWN')
                    severity_counts[severity] = severity_counts.get(severity, 0) + 1

                return json.dumps({
                    "audit_id": audit_id,
                    "total_findings": len(findings),
                    "severity_counts": severity_counts,
                    "status": audit.get('status'),
                    "last_updated": audit.get('last_updated')
                })

        return json.dumps({"error": f"Audit with ID {audit_id} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_audit_summary",
                "description": "Retrieves a summary of audit findings.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string", "description": "The ID of the audit to summarize."}
                    },
                    "required": ["audit_id"]
                }
            }
        }

# New Tool 3: Update Fix Item Priority
class UpdateFixItemPriority(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Updates the priority of a fix item.
        """
        item_id = kwargs.get('item_id')
        new_priority = kwargs.get('new_priority')
        updated_by = kwargs.get('updated_by')

        if not all([item_id, new_priority, updated_by]):
            return json.dumps({"error": "item_id, new_priority, and updated_by are required"})

        # Validate priority values
        valid_priorities = ['LOW', 'MEDIUM', 'HIGH', 'CRITICAL']
        if new_priority not in valid_priorities:
            return json.dumps({"error": f"Invalid priority. Must be one of: {', '.join(valid_priorities)}"})

        # Find and update the fix item
        for item in data.get('fix_items', []):
            if item.get('item_id') == item_id:
                item['priority'] = new_priority
                item['last_updated'] = datetime.now().isoformat()
                item['updated_by'] = updated_by
                return json.dumps({"status": "success", "item_id": item_id, "new_priority": new_priority})

        return json.dumps({"error": f"Fix item with ID {item_id} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_fix_item_priority",
                "description": "Updates the priority of a fix item.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "item_id": {"type": "string", "description": "The ID of the fix item to update."},
                        "new_priority": {"type": "string", "description": "The new priority level."},
                        "updated_by": {"type": "string", "description": "Email of the user updating the priority."},
                        "notes": {"type": "string", "description": "Optional notes about the priority change."}
                    },
                    "required": ["item_id", "new_priority", "updated_by"]
                }
            }
        }





class UpdateAuditFindingSeverity(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Updates the severity level of an audit finding.
        """
        finding_id = kwargs.get("finding_id")
        new_severity = kwargs.get("new_severity")

        if not all([finding_id, new_severity]):
            return json.dumps({"error": "finding_id and new_severity are required."})

        updated_by = kwargs.get("updated_by")
        notes = kwargs.get("notes", "")
        updated_ts = kwargs.get("updated_ts", "2024-08-23T15:00:00Z")

        return json.dumps({
            "status": "SUCCESS",
            "finding_id": finding_id,
            "previous_severity": "MEDIUM",
            "new_severity": new_severity,
            "updated_by": updated_by,
            "notes": notes,
            "updated_ts": updated_ts
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_audit_finding_severity",
                "description": "Updates the severity level of an audit finding (DS or A11y).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "finding_id": {"type": "string", "description": "The ID of the audit finding to update."},
                        "new_severity": {"type": "string", "description": "The new severity level (LOW, MEDIUM, HIGH, CRITICAL)."},
                        "updated_by": {"type": "string", "description": "Email of the user updating the severity."},
                        "notes": {"type": "string", "description": "Optional notes about the severity change."},
                        "updated_ts": {"type": "string", "description": "Timestamp of the update."}
                    },
                    "required": ["finding_id", "new_severity"]
                }
            }
        }


class UpdateAuditType(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Updates the audit type and associated metadata.
        """
        audit_id = kwargs.get("audit_id")
        new_audit_type = kwargs.get("new_audit_type")

        if not all([audit_id, new_audit_type]):
            return json.dumps({"error": "audit_id and new_audit_type are required."})

        updated_by = kwargs.get("updated_by")
        status = kwargs.get("status", "RUNNING")
        notes = kwargs.get("notes", "")
        updated_ts = kwargs.get("updated_ts", "2024-08-23T15:00:00Z")

        return json.dumps({
            "status": "SUCCESS",
            "audit_id": audit_id,
            "previous_audit_type": "A11Y",
            "new_audit_type": new_audit_type,
            "status": status,
            "updated_by": updated_by,
            "notes": notes,
            "updated_ts": updated_ts
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_audit_type",
                "description": "Updates the audit type and associated metadata.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string", "description": "The ID of the audit to update."},
                        "new_audit_type": {"type": "string", "description": "The new audit type (A11Y, DS_MAPPING, COMBINED_DS_A11Y)."},
                        "updated_by": {"type": "string", "description": "Email of the user updating the audit type."},
                        "status": {"type": "string", "description": "Optional status update (RUNNING, COMPLETED, FAILED)."},
                        "notes": {"type": "string", "description": "Optional notes about the audit type change."},
                        "updated_ts": {"type": "string", "description": "Timestamp of the update."}
                    },
                    "required": ["audit_id", "new_audit_type"]
                }
            }
        }


class GetAuditFindingsByType(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Retrieves audit findings filtered by type and other criteria.
        """
        finding_type = kwargs.get("finding_type")
        violation_type = kwargs.get("violation_type")
        severity = kwargs.get("severity")
        audit_id = kwargs.get("audit_id")
        limit = kwargs.get("limit", 10)

        audit_findings_ds = data.get("audit_findings_ds", [])
        audit_findings_a11y = data.get("audit_findings_a11y", [])

        results = []

        # Process DS findings
        if not violation_type:  # Only check DS findings if no violation_type specified
            for finding in audit_findings_ds:
                if finding_type and finding.get("finding_type") != finding_type:
                    continue
                if severity and finding.get("severity") != severity:
                    continue
                if audit_id and finding.get("audit_id") != audit_id:
                    continue

                results.append({
                    "source": "DS",
                    "finding": finding
                })

        # Process A11y findings
        if not finding_type:  # Only check A11y findings if no finding_type specified
            for finding in audit_findings_a11y:
                if violation_type and finding.get("violation_type") != violation_type:
                    continue
                if severity and finding.get("severity") != severity:
                    continue
                if audit_id and finding.get("audit_id") != audit_id:
                    continue

                results.append({
                    "source": "A11Y",
                    "finding": finding
                })

        # Apply limit
        results = results[:limit]

        return json.dumps({
            "total_found": len(results),
            "findings": results
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_audit_findings_by_type",
                "description": "Retrieves audit findings filtered by type, violation type, severity and other criteria.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "finding_type": {"type": "string", "description": "DS finding type filter (UNMAPPED, AMBIGUOUS, SUBSTITUTE_RECOMMENDED)."},
                        "violation_type": {"type": "string", "description": "A11y violation type filter (TOUCH_TARGET, CONTRAST, TEXT_SIZING, RTL)."},
                        "severity": {"type": "string", "description": "Severity level filter (LOW, MEDIUM, HIGH, CRITICAL)."},
                        "audit_id": {"type": "string", "description": "Filter by specific audit ID."},
                        "limit": {"type": "integer", "description": "Maximum number of results to return (default 10)."}
                    },
                    "required": []
                }
            }
        }


class GetAuditReportSummary(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Retrieves comprehensive audit report summary with findings breakdown.
        """
        audit_id = kwargs.get("audit_id")

        if not audit_id:
            return json.dumps({"error": "audit_id is required."})

        audits = data.get("audits", [])
        audit_findings_ds = data.get("audit_findings_ds", [])
        audit_findings_a11y = data.get("audit_findings_a11y", [])

        # Find the audit
        audit_info = None
        for audit in audits:
            if audit.get("audit_id") == audit_id:
                audit_info = audit
                break

        if not audit_info:
            return json.dumps({"error": f"Audit with ID {audit_id} not found."})

        # Get findings for this audit
        ds_findings = [f for f in audit_findings_ds if f.get("audit_id") == audit_id]
        a11y_findings = [f for f in audit_findings_a11y if f.get("audit_id") == audit_id]

        # Count findings by severity
        severity_counts = {"LOW": 0, "MEDIUM": 0, "HIGH": 0, "CRITICAL": 0}

        for finding in ds_findings + a11y_findings:
            severity = finding.get("severity", "MEDIUM")
            if severity in severity_counts:
                severity_counts[severity] += 1

        include_details = kwargs.get("include_details", False)

        summary = {
            "audit_info": audit_info,
            "ds_findings_count": len(ds_findings),
            "a11y_findings_count": len(a11y_findings),
            "total_findings": len(ds_findings) + len(a11y_findings),
            "severity_breakdown": severity_counts
        }

        if include_details:
            summary["ds_findings"] = ds_findings
            summary["a11y_findings"] = a11y_findings

        return json.dumps(summary, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_audit_report_summary",
                "description": "Retrieves comprehensive audit report summary with findings breakdown.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string", "description": "The ID of the audit to generate summary for."},
                        "include_details": {"type": "boolean", "description": "Include detailed finding information (default false)."}
                    },
                    "required": ["audit_id"]
                }
            }
        }


class UpdateAuditFindingStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Updates the status of an audit finding.
        """
        finding_id = kwargs.get('finding_id')
        new_status = kwargs.get('new_status')
        notes = kwargs.get('notes', '')
        updated_by = kwargs.get('updated_by')

        if not all([finding_id, new_status]):
            return json.dumps({"error": "finding_id and new_status are required."})

        # Valid statuses for audit findings
        valid_statuses = ['OPEN', 'IN_PROGRESS', 'RESOLVED', 'DEFERRED', 'VERIFIED']
        if new_status not in valid_statuses:
            return json.dumps({"error": f"Invalid status. Must be one of: {', '.join(valid_statuses)}"})

        # Check both design system and accessibility findings
        finding_found = False
        old_status = None
        finding_type = None

        for dataset_name in ['audit_findings_ds', 'audit_findings_a11y']:
            findings = data.get(dataset_name, [])
            for finding in findings:
                if finding.get('finding_id') == finding_id:
                    finding_found = True
                    old_status = finding.get('status', 'OPEN')
                    finding_type = dataset_name

                    # Update the finding
                    finding['status'] = new_status
                    finding['last_updated'] = datetime.now().isoformat()

                    if updated_by:
                        finding['updated_by'] = updated_by
                    if notes:
                        finding['resolution_notes'] = notes

                    # Add status history
                    if 'status_history' not in finding:
                        finding['status_history'] = []
                    finding['status_history'].append({
                        "from_status": old_status,
                        "to_status": new_status,
                        "changed_by": updated_by,
                        "changed_at": datetime.now().isoformat(),
                        "notes": notes
                    })

                    break
            if finding_found:
                break

        if not finding_found:
            return json.dumps({"error": f"Audit finding with ID '{finding_id}' not found."})

        return json.dumps({
            "success": True,
            "finding_id": finding_id,
            "finding_type": finding_type,
            "old_status": old_status,
            "new_status": new_status,
            "updated_at": datetime.now().isoformat()
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_audit_finding_status",
                "description": "Updates the status of an audit finding (design system or accessibility).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "finding_id": {"type": "string", "description": "The ID of the audit finding to update."},
                        "new_status": {"type": "string", "description": "The new status (OPEN, IN_PROGRESS, RESOLVED, DEFERRED, VERIFIED)."},
                        "notes": {"type": "string", "description": "Optional notes about the status change."},
                        "updated_by": {"type": "string", "description": "Optional email of person updating the finding."}
                    },
                    "required": ["finding_id", "new_status"]
                }
            }
        }


class UpdateAuditProgress(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Updates audit progress and completion percentage.
        """
        audit_id = kwargs.get('audit_id')
        progress_percentage = kwargs.get('progress_percentage')
        notes = kwargs.get('notes', '')
        updated_by = kwargs.get('updated_by')

        if not all([audit_id, progress_percentage is not None]):
            return json.dumps({"error": "audit_id and progress_percentage are required."})

        if not (0 <= progress_percentage <= 100):
            return json.dumps({"error": "progress_percentage must be between 0 and 100."})

        audits = data.get('audits', [])
        audit_found = False

        for audit in audits:
            if audit.get('audit_id') == audit_id:
                audit_found = True
                old_progress = audit.get('progress_percentage', 0)

                # Update audit progress
                audit['progress_percentage'] = progress_percentage
                audit['last_updated'] = datetime.now().isoformat()

                if updated_by:
                    audit['updated_by'] = updated_by
                if notes:
                    audit['progress_notes'] = notes

                # Auto-update status based on progress
                if progress_percentage == 100 and audit.get('status') == 'RUNNING':
                    audit['status'] = 'COMPLETED'
                    audit['completed_at'] = datetime.now().isoformat()
                elif progress_percentage > 0 and audit.get('status') not in ['RUNNING', 'COMPLETED']:
                    audit['status'] = 'RUNNING'

                # Add progress history
                if 'progress_history' not in audit:
                    audit['progress_history'] = []
                audit['progress_history'].append({
                    "from_progress": old_progress,
                    "to_progress": progress_percentage,
                    "changed_by": updated_by,
                    "changed_at": datetime.now().isoformat(),
                    "notes": notes
                })

                break

        if not audit_found:
            return json.dumps({"error": f"Audit with ID '{audit_id}' not found."})

        return json.dumps({
            "success": True,
            "audit_id": audit_id,
            "old_progress": old_progress,
            "new_progress": progress_percentage,
            "updated_at": datetime.now().isoformat()
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_audit_progress",
                "description": "Updates audit progress percentage and automatically manages status transitions.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string", "description": "The ID of the audit to update."},
                        "progress_percentage": {"type": "number", "description": "Progress percentage (0-100)."},
                        "notes": {"type": "string", "description": "Optional notes about the progress update."},
                        "updated_by": {"type": "string", "description": "Optional email of person updating the audit."}
                    },
                    "required": ["audit_id", "progress_percentage"]
                }
            }
        }


class GetAuditFindingDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Retrieves detailed information about audit findings with optional filtering.
        """
        audit_id = kwargs.get('audit_id')
        finding_id = kwargs.get('finding_id')
        include_resolved = kwargs.get('include_resolved', False)

        if not audit_id:
            return json.dumps({"error": "audit_id is required."})

        # Get findings from both datasets
        ds_findings = data.get('audit_findings_ds', [])
        a11y_findings = data.get('audit_findings_a11y', [])

        # Filter by audit_id
        ds_results = [f for f in ds_findings if f.get('audit_id') == audit_id]
        a11y_results = [f for f in a11y_findings if f.get('audit_id') == audit_id]

        # Filter by specific finding_id if provided
        if finding_id:
            ds_results = [f for f in ds_results if f.get('finding_id') == finding_id]
            a11y_results = [f for f in a11y_results if f.get('finding_id') == finding_id]

        # Filter resolved findings if not requested
        if not include_resolved:
            ds_results = [f for f in ds_results if f.get('status', 'OPEN') not in ['RESOLVED', 'VERIFIED']]
            a11y_results = [f for f in a11y_results if f.get('status', 'OPEN') not in ['RESOLVED', 'VERIFIED']]

        # Combine and enrich results
        all_findings = []

        for finding in ds_results:
            enriched = finding.copy()
            enriched['finding_category'] = 'design_system'
            all_findings.append(enriched)

        for finding in a11y_results:
            enriched = finding.copy()
            enriched['finding_category'] = 'accessibility'
            all_findings.append(enriched)

        # Sort by severity and creation order
        severity_order = {'CRITICAL': 0, 'HIGH': 1, 'MEDIUM': 2, 'LOW': 3}
        all_findings.sort(key=lambda x: (
            severity_order.get(x.get('severity', 'MEDIUM'), 2),
            x.get('finding_id', '')
        ))

        return json.dumps({
            "audit_id": audit_id,
            "total_findings": len(all_findings),
            "design_system_findings": len(ds_results),
            "accessibility_findings": len(a11y_results),
            "findings": all_findings
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_audit_finding_details",
                "description": "Retrieves detailed audit finding information with filtering options.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string", "description": "The ID of the audit to get findings for."},
                        "finding_id": {"type": "string", "description": "Optional specific finding ID to retrieve."},
                        "include_resolved": {"type": "boolean", "description": "Include resolved/verified findings (default false)."}
                    },
                    "required": ["audit_id"]
                }
            }
        }
class UpdateFixItemStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Updates the status of a fix item and manages the fix plan lifecycle.
        """
        fix_item_id = kwargs.get('fix_item_id')
        new_status = kwargs.get('new_status')
        assignee_id = kwargs.get('assignee_id')
        implementation_notes = kwargs.get('implementation_notes', '')
        completion_date = kwargs.get('completion_date')

        if not all([fix_item_id, new_status]):
            return json.dumps({"error": "fix_item_id and new_status are required."})

        # Validate status values
        valid_statuses = ['PENDING', 'IN_PROGRESS', 'APPLIED', 'DEFERRED', 'VERIFIED']
        if new_status not in valid_statuses:
            return json.dumps({"error": f"Invalid status. Must be one of: {', '.join(valid_statuses)}"})

        fix_items = data.get('fix_items', [])
        fix_plans = data.get('fix_plans', [])

        # Find the fix item
        item_found = False
        for item in fix_items:
            if item.get('item_id') == fix_item_id:
                item_found = True
                old_status = item.get('status')

                # Update the item status
                item['status'] = new_status
                item['last_updated'] = datetime.now().isoformat()

                # Handle status-specific logic
                if new_status == 'IN_PROGRESS' and assignee_id:
                    item['assignee_id'] = assignee_id
                    item['started_at'] = datetime.now().isoformat()

                elif new_status == 'APPLIED':
                    item['completion_date'] = completion_date or datetime.now().isoformat()
                    if implementation_notes:
                        item['implementation_notes'] = implementation_notes

                elif new_status == 'DEFERRED':
                    item['deferred_at'] = datetime.now().isoformat()
                    if implementation_notes:
                        item['deferral_reason'] = implementation_notes

                elif new_status == 'VERIFIED':
                    item['verified_at'] = datetime.now().isoformat()
                    if implementation_notes:
                        item['verification_notes'] = implementation_notes

                # Update fix plan progress
                plan_id = item.get('plan_id')
                if plan_id:
                    for plan in fix_plans:
                        if plan.get('plan_id') == plan_id:
                            # Recalculate completion percentage
                            plan_items = [i for i in fix_items if i.get('plan_id') == plan_id]
                            completed_items = [i for i in plan_items if i.get('status') in ['APPLIED', 'VERIFIED']]
                            completion_percentage = (len(completed_items) / len(plan_items)) * 100 if plan_items else 0

                            plan['completion_percentage'] = round(completion_percentage, 2)
                            plan['last_updated'] = datetime.now().isoformat()

                            # Update plan status if all items are completed
                            if completion_percentage == 100:
                                plan['status'] = 'COMPLETED'
                                plan['completed_at'] = datetime.now().isoformat()
                            elif completion_percentage > 0:
                                plan['status'] = 'IN_PROGRESS'

                            break

                # Log the status change
                if 'status_history' not in item:
                    item['status_history'] = []
                item['status_history'].append({
                    "from_status": old_status,
                    "to_status": new_status,
                    "changed_by": assignee_id,
                    "changed_at": datetime.now().isoformat(),
                    "notes": implementation_notes
                })

                break

        if not item_found:
            return json.dumps({"error": f"Fix item with ID '{fix_item_id}' not found."})

        return json.dumps({
            "success": True,
            "fix_item_id": fix_item_id,
            "old_status": old_status,
            "new_status": new_status,
            "updated_at": datetime.now().isoformat()
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_fix_item_status",
                "description": "Updates the status of a fix item and manages the fix plan lifecycle, including assignment, implementation, and verification.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "fix_item_id": {"type": "string", "description": "The ID of the fix item to update."},
                        "new_status": {"type": "string", "description": "The new status for the fix item. Must be one of: PENDING, IN_PROGRESS, APPLIED, DEFERRED, VERIFIED."},
                        "assignee_id": {"type": "string", "description": "The ID of the person assigned to work on the fix item."},
                        "implementation_notes": {"type": "string", "description": "Optional notes about the implementation, deferral reason, or verification."},
                        "completion_date": {"type": "string", "description": "Optional completion date in ISO format. If not provided, current timestamp will be used."}
                    },
                    "required": ["fix_item_id", "new_status"]
                }
            }
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
    GetFixPlanById()
]
