
from domains.dto import Task, Action

TASKS = [
    Task(
        annotator="0",
        user_id="user_1",
        instruction=(
            "You are a review cycle SLA management specialist responsible for coordinating review cycle escalation and integrated audit workflow management. "
            "Your task is to manage review cycle SLA coordination with audit status management and ensure proper escalation tracking. "
            "Focus on managing review cycle status transitions from NEEDS_REVIEW to ESCALATED, including audit status coordination and comprehensive logging. "
            "Coordinate with review teams through appropriate channels to ensure all SLA breaches and audit workflows are properly synchronized. "
            "Required constants: "
            "cycle_id=cycle_001, artifact_id=art_001, new_status=ESCALATED, "
            "audit_id=audit_001, audit_status=IN_PROGRESS, updated_by=sarah.designer@company.com, "
            "thread_id=thread_001, priority_level=HIGH, urgency_reason=SLA breach requires immediate escalation, "
            "escalate_to=sarah.designer@company.com, "
            "log_level=WARNING, component=review_sla, after_timestamp=2024-08-20T15:00:00Z, "
            "message_pattern=escalation, log_message=Review cycle SLA escalation completed with audit integration, "
            "category=review_sla_config"
        ),
        actions=[
            Action(name="get_review_approvals_summary", kwargs={"cycle_id": "cycle_001"}),
            Action(name="update_review_cycle_status", kwargs={"cycle_id": "cycle_001", "new_status": "ESCALATED", "reviewer_email": "sarah.designer@company.com", "completion_notes": "SLA breach requires immediate escalation"}),
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_001"}),
            Action(name="update_audit_status", kwargs={"audit_id": "audit_001", "new_status": "IN_PROGRESS", "updated_by": "sarah.designer@company.com"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "SLA breach requires immediate escalation"}),
            Action(name="add_terminal_log_entry", kwargs={"log_message": "Review cycle SLA escalation completed with audit integration", "log_level": "WARNING", "component": "review_sla", "user_email": "sarah.designer@company.com"}),
            Action(name="get_filtered_log_entries", kwargs={"log_level": "WARNING", "component": "review_sla", "after_timestamp": "2024-08-20T15:00:00Z", "message_pattern": "escalation"}),
            Action(name="get_system_config_by_category", kwargs={"category": "review_sla_config"})
        ],
        outputs=[
            "Review cycle SLA management completed for cycle_001: review cycle approvals verified for SLA coordination, review cycle status updated to ESCALATED with Sarah Designer oversight and SLA breach escalation notes, audit_001 status verified for coordination workflow, audit status updated to IN_PROGRESS with Sarah Designer assignment, Gmail thread priority escalated to HIGH with SLA breach urgency and stakeholder escalation, comprehensive SLA escalation logging added with WARNING level review_sla component tracking, filtered escalation logs retrieved for WARNING level pattern matching since August 20th, and review SLA configuration retrieved for system coordination settings."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_2",
        instruction=(
            "You are an audit report management specialist responsible for coordinating the end-to-end audit lifecycle for design system components and accessibility compliance. "
            "Your primary responsibility involves managing audit_001 for artifact art_001 (Homepage Hero Section) which requires comprehensive status tracking from COMPLETED to final report generation. The workflow integrates with audit_002 for accessibility review of art_008 admin panel components requiring status coordination. "
            "The audit management workflow centers on thread_001 priority escalation to HIGH priority for design review coordination involving sarah.designer@company.com oversight, URGENT priority level escalation for comprehensive design review tracking, and escalation_reason 'Critical audit findings require immediate design team attention and stakeholder review'. The priority management requires comprehensive Gmail thread coordination and detailed audit status documentation. "
            "Your coordination efforts should ensure seamless audit report generation through proper status management, effective priority escalation for design review threads, and comprehensive audit findings tracking for stakeholder reporting. "
            "Key parameters: audit_id=audit_001, new_status=COMPLETED, report_asset_id=asset_001, completion_notes=Design system audit completed with recommendations, "
            "thread_001_priority=HIGH, thread_002_priority=NORMAL, thread_001_urgency=Critical audit findings require immediate design team attention, thread_002_urgency=Secondary audit review completed, "
            "escalate_to=sarah.designer@company.com,mike.ux@company.com, audit_type=COMBINED_DS_A11Y, created_after=2024-08-20T15:00:00Z, audit_date_filter=2024-08-18T00:00:00Z, "
            "thread_ids=thread_001,thread_002, artifact_ids=art_001,art_008"
        ),
        actions=[
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_001"}),
            Action(name="update_audit_report_status", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed with recommendations"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical audit findings require immediate design team attention", "escalate_to": ["sarah.designer@company.com", "mike.ux@company.com"]}),
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_002"}),
            Action(name="update_audit_report_status", kwargs={"audit_id": "audit_002", "new_status": "COMPLETED", "report_asset_id": "asset_007"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Secondary audit review completed"}),
            Action(name="get_audits_by_status", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"})
        ],
        outputs=[
            "Audit management workflow completed: audit_001 status updated to COMPLETED with report asset_001 association and completion notes, thread_001 priority escalated to HIGH with critical findings urgency and stakeholder escalation to design team, audit_002 status updated to COMPLETED with report asset_007, and comprehensive audit verification completed for A11Y audit type."
        ]
    ),
    
    Task(
        annotator="0",
        user_id="user_3",
        instruction=(
            "You are an audit report management specialist responsible for coordinating the end-to-end audit lifecycle for design system components and accessibility compliance. "
            "Your primary responsibility involves managing audit_001 for artifact art_001 (Homepage Hero Section) which requires comprehensive status tracking from COMPLETED to final report generation. The workflow integrates with audit_002 for accessibility review of art_008 admin panel components requiring status coordination. "
            "The audit management workflow centers on thread_001 priority escalation to HIGH priority for design review coordination involving sarah.designer@company.com oversight, URGENT priority level escalation for comprehensive design review tracking, and escalation_reason 'Critical audit findings require immediate design team attention and stakeholder review'. The priority management requires comprehensive Gmail thread coordination and detailed audit status documentation. "
            "Your coordination efforts should ensure seamless audit report generation through proper status management, effective priority escalation for design review threads, and comprehensive audit findings tracking for stakeholder reporting. "
            "Key parameters: audit_id=audit_001, new_status=COMPLETED, report_asset_id=asset_001, completion_notes=Design system audit completed with recommendations, "
            "thread_001_priority=HIGH, thread_002_priority=NORMAL, thread_001_urgency=Critical audit findings require immediate design team attention, thread_002_urgency=Secondary audit review completed, "
            "escalate_to=sarah.designer@company.com,mike.ux@company.com, audit_type=COMBINED_DS_A11Y, created_after=2024-08-20T15:00:00Z, audit_date_filter=2024-08-18T00:00:00Z, "
            "thread_ids=thread_001,thread_002, artifact_ids=art_001,art_008"
        ),
        actions=[
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_001"}),
            Action(name="update_audit_report_status", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed with recommendations"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical audit findings require immediate design team attention", "escalate_to": ["sarah.designer@company.com", "mike.ux@company.com"]}),
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_002"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Secondary audit review completed"}),
            Action(name="get_audits_by_status", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"}),
            Action(name="add_terminal_log_entry", kwargs={"log_message": "Audit management workflow completed for audit_001 and audit_002 with critical findings escalation", "log_level": "INFO", "component": "audit_management", "user_email": "sarah.designer@company.com"})
        ],
        outputs=[
            "Audit management workflow completed: audit_001 status updated to COMPLETED with report asset_001 association and completion notes, thread_001 priority escalated to HIGH with critical findings urgency and stakeholder escalation to design team, comprehensive audit verification completed for A11Y audit type, and terminal log entry added for audit management workflow tracking."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_4",
        instruction=(
            "You are an accessibility compliance specialist responsible for audit findings coordination and fix item management across admin panel accessibility initiatives. "
            "Your primary responsibility involves accessibility audit coordination for audit_002, audit_004, and audit_005 where comprehensive findings analysis and fix item status updates require systematic processing. The workflow involves fix item lifecycle management following proper status progression. "
            "The accessibility compliance workflow centers on item_001 touch target verification with VERIFIED status achievement, item_004 font size compliance with APPLIED status and completion timestamp coordination, and item_002 contrast violation remediation with IN_PROGRESS status management. The fix implementation requires systematic status coordination and compliance verification. "
            "Your coordination efforts should ensure comprehensive audit findings analysis, proper fix item lifecycle management, and successful accessibility compliance tracking for stakeholder reporting and workflow completion."
        ),
        actions=[
            Action(name="get_audit_findings_summary", kwargs={"audit_id": "audit_002"}),
            Action(name="get_audit_findings_summary", kwargs={"audit_id": "audit_004"}),
            Action(name="get_audit_findings_summary", kwargs={"audit_id": "audit_005"}),
            Action(name="update_fix_item_status", kwargs={"fix_item_id": "item_001", "new_status": "VERIFIED"}),
            Action(name="update_fix_item_status", kwargs={"fix_item_id": "item_004", "new_status": "APPLIED", "completion_date": "2024-08-25T15:30:00Z"}),
            Action(name="update_fix_item_status", kwargs={"fix_item_id": "item_002", "new_status": "IN_PROGRESS"}),
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_007"}),
            Action(name="get_fix_plan_items", kwargs={"plan_id": "plan_001"})
        ],
        outputs=[
            "Accessibility compliance workflow completed: audit findings analyzed for audit_002, audit_004, and audit_005, item_001 updated to VERIFIED status, item_004 updated to APPLIED status with completion date 2024-08-25T15:30:00Z, item_002 updated to IN_PROGRESS status for continued accessibility improvements, asset export summary verified for asset_007 accessibility compliance coordination, and fix plan items retrieved for plan_001 comprehensive accessibility workflow coordination."
        ]
    ),
    
    Task(
        annotator="0",
        user_id="user_5",
        instruction=(
            "You are a review cycle SLA management specialist responsible for coordinating review cycle escalation and integrated audit workflow management. "
            "Your task is to manage review cycle SLA coordination with audit status management and ensure proper escalation tracking. "
            "Focus on managing review cycle status transitions from NEEDS_REVIEW to ESCALATED, including audit status coordination and comprehensive logging. "
            "Coordinate with review teams through appropriate channels to ensure all SLA breaches and audit workflows are properly synchronized. "
            "Required constants: "
            "cycle_id=cycle_001, artifact_id=art_001, new_status=ESCALATED, "
            "audit_id=audit_001, audit_status=IN_PROGRESS, updated_by=sarah.designer@company.com, "
            "thread_id=thread_001, priority_level=HIGH, urgency_reason=SLA breach requires immediate escalation, "
            "escalate_to=sarah.designer@company.com, "
            "log_level=WARNING, component=review_sla, after_timestamp=2024-08-20T15:00:00Z, "
            "message_pattern=escalation, log_message=Review cycle SLA escalation completed with audit integration, "
            "asset_id=asset_001, category=sla_config"
        ),
        actions=[
            Action(name="get_review_approvals_summary", kwargs={"cycle_id": "cycle_001"}),
            Action(name="update_review_cycle_status", kwargs={"cycle_id": "cycle_001", "new_status": "ESCALATED", "reviewer_email": "sarah.designer@company.com", "completion_notes": "SLA breach requires immediate escalation"}),
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_001"}),
            Action(name="update_audit_status", kwargs={"audit_id": "audit_001", "new_status": "IN_PROGRESS", "updated_by": "sarah.designer@company.com"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "SLA breach requires immediate escalation"}),
            Action(name="add_terminal_log_entry", kwargs={"log_message": "Review cycle SLA escalation completed with audit integration", "log_level": "WARNING", "component": "review_sla", "user_email": "sarah.designer@company.com"}),
            Action(name="get_filtered_log_entries", kwargs={"log_level": "WARNING", "component": "review_sla", "after_timestamp": "2024-08-20T15:00:00Z", "message_pattern": "escalation"}),
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_001"}),
            Action(name="get_system_config_by_category", kwargs={"category": "sla_config"})
        ],
        outputs=[
            "Review cycle SLA management completed for cycle_001: review cycle approvals verified for SLA coordination, review cycle status updated to ESCALATED with Sarah Designer oversight and SLA breach escalation notes, audit_001 status verified for coordination workflow, audit status updated to IN_PROGRESS with Sarah Designer assignment, Gmail thread priority escalated to HIGH with SLA breach urgency and stakeholder escalation, comprehensive SLA escalation logging added with WARNING level review_sla component tracking, filtered escalation logs retrieved for WARNING level pattern matching since August 20th, asset export summary retrieved for asset_001 coordination tracking, and SLA configuration retrieved for system coordination settings."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_6",
        instruction=(
            "You are a Figma comment resolution specialist responsible for accessibility feedback coordination and workflow management across admin panel header components. "
            "Your primary responsibility involves accessibility feedback coordination for art_008 admin panel header where unresolved comments with resolved_status False require identification and resolution coordination. The workflow also involves asset_007 admin header export integration requiring status verification and coordination alignment. "
            "The accessibility improvement workflow centers on comment_006 accessibility enhancement coordination involving mike.ux@company.com team member oversight, HIGH priority accessibility improvements, and comprehensive ARIA labels and keyboard navigation support implementation tracking. The feedback resolution requires progress status coordination and detailed implementation documentation. "
            "Your coordination efforts should ensure seamless accessibility audit communication through thread_004, effective comment lifecycle coordination, and comprehensive accessibility compliance tracking for stakeholder reporting and successful workflow completion."
            "You can use resolution_notes Accessibility improvements in progress - adding ARIA labels and keyboard navigation support, "
            "thread_priority=HIGH, urgency_reason=Accessibility improvements require immediate attention, escalate_to=mike.ux@company.com"
        ),
        actions=[
            Action(name="get_figma_comments_by_artifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_007"}),
            Action(name="update_figma_comment_status", kwargs={"comment_id": "comment_006", "new_status": "IN_PROGRESS", "resolution_notes": "Accessibility improvements in progress - adding ARIA labels and keyboard navigation support", "assignee_email": "mike.ux@company.com", "priority_level": "HIGH"}),
            Action(name="get_gmail_threads_by_labels", kwargs={"thread_id": "thread_004"}),
            Action(name="get_figma_comments_by_artifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="add_terminal_log_entry", kwargs={"log_message": "Accessibility comment resolution workflow completed for art_008 admin panel header", "log_level": "INFO", "component": "accessibility_resolution", "user_email": "mike.ux@company.com"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_004", "new_priority": "HIGH", "urgency_reason": "Accessibility improvements require immediate attention", "escalate_to": ["mike.ux@company.com"]})
        ],
        outputs=[
            "Comment resolution workflow completed. comment status updated, assignee assigned to Mike UX with HIGH priority level, resolution notes added about accessibility improvements, asset export status verified for admin header asset_007, Gmail thread communication status verified for thread_004 accessibility audit coordination, terminal log entry added for accessibility comment resolution workflow tracking, and thread_004 priority escalated to HIGH for accessibility improvements requiring immediate attention with Mike UX escalation."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_7",
        instruction=(
            "You are an audit report management specialist responsible for coordinating the end-to-end audit lifecycle for design system components and accessibility compliance. "
            "Your primary responsibility involves managing audit_001 for artifact art_001 (Homepage Hero Section) which requires comprehensive status tracking from COMPLETED to final report generation. The workflow integrates with audit_002 for accessibility review of art_008 admin panel components requiring status coordination. "
            "The audit management workflow centers on thread_001 priority escalation to HIGH priority for design review coordination involving sarah.designer@company.com oversight, URGENT priority level escalation for comprehensive design review tracking, and escalation_reason 'Critical audit findings require immediate design team attention and stakeholder review'. The priority management requires comprehensive Gmail thread coordination and detailed audit status documentation. "
            "Your coordination efforts should ensure seamless audit report generation through proper status management, effective priority escalation for design review threads, comprehensive audit findings tracking for stakeholder reporting, and successful audit lifecycle completion with proper report asset associations. "
            "Key parameters: audit_id=audit_001, new_status=COMPLETED, report_asset_id=asset_001, completion_notes=Design system audit completed with recommendations, "
            "thread_001_priority=HIGH, thread_002_priority=NORMAL, thread_001_urgency=Critical audit findings require immediate design team attention, thread_002_urgency=Secondary audit review completed, "
            "escalate_to=sarah.designer@company.com,mike.ux@company.com, audit_type=COMBINED_DS_A11Y, created_after=2024-08-20T15:00:00Z, audit_date_filter=2024-08-18T00:00:00Z, "
            "thread_ids=thread_001,thread_002, artifact_ids=art_001,art_008, "
            "asset_id=asset_001, category=audit_thresholds"
        ),
        actions=[
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_001"}),
            Action(name="update_audit_report_status", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed with recommendations"}),
            Action(name="get_audits_by_status", kwargs={"status": "COMPLETED", "audit_type": "COMBINED_DS_A11Y"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical audit findings require immediate design team attention", "escalate_to": ["sarah.designer@company.com", "mike.ux@company.com"]}),
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_002"}),
            Action(name="get_audits_by_status", kwargs={"artifact_id": "art_001", "created_after": "2024-08-20T15:00:00Z"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Secondary audit review completed"}),
            Action(name="get_audits_by_status", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"}),
            Action(name="get_system_config_by_category", kwargs={"category": "audit_thresholds"})
        ],
        outputs=[
            "Audit management workflow completed: audit_001 status updated to COMPLETED with report asset_001 association and completion notes, thread_001 priority escalated to HIGH with critical findings urgency and stakeholder escalation to design team, secondary thread_002 priority normalized, comprehensive audit status verification completed across all COMBINED_DS_A11Y and A11Y audit types for stakeholder reporting, and system configuration retrieved for audit_thresholds category to ensure proper audit compliance settings."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_8",
        instruction=(
            "You are a design system component audit specialist responsible for coordinating comprehensive design system audits and thread priority management for component workflows. "
            "Your primary responsibility involves audit_002 coordination for design system components requiring comprehensive status tracking and thread priority management for component review coordination. The workflow integrates with approval verification and thread escalation for design system release preparation. "
            "The design system coordination workflow centers on comprehensive audit tracking with sarah.designer@company.com oversight, thread_001 HIGH priority management for design system coordination, and detailed approval verification across design system workflows. "
            "Your coordination efforts should ensure seamless design system audit coordination through comprehensive status tracking, effective thread priority management for component reviews, and detailed approval verification for design system workflows with proper design team coordination and release preparation tracking. "
            "Key parameters: "
            "audit_002_id=audit_002, audit_002_status=COMPLETED, "
            "art_008_id=art_008, audit_type=A11Y, "
            "thread_001_id=thread_001, thread_008_id=thread_008, "
            "thread_001_priority=HIGH, thread_008_priority=NORMAL, "
            "thread_001_urgency=Design system component review requires immediate coordination, "
            "thread_008_urgency=Design system follow-up coordination completed, "
            "completion_notes=Design system component audit completed successfully, "
            "approval_002_id=approval_002, cycle_002_id=cycle_002, "
            "escalate_to=sarah.designer@company.com,design.system@company.com, "
            "release_owner=sarah.designer@company.com, release_start_date=2024-08-20T13:00:00Z, "
            "category=design_system_config"
        ),
        actions=[
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_002"}),
            Action(name="update_audit_report_status", kwargs={"audit_id": "audit_002", "new_status": "COMPLETED", "completion_notes": "Design system component audit completed successfully"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Design system component review requires immediate coordination", "escalate_to": ["sarah.designer@company.com", "design.system@company.com"]}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_008", "new_priority": "NORMAL", "urgency_reason": "Design system follow-up coordination completed"}),
            Action(name="get_review_approvals_summary", kwargs={"approval_id": "approval_002", "cycle_id": "cycle_002"}),
            Action(name="get_audits_by_status", kwargs={"artifact_id": "art_008", "audit_type": "A11Y"}),
            Action(name="get_releases_by_owner", kwargs={"owner_email": "sarah.designer@company.com", "created_after": "2024-08-20T13:00:00Z"}),
            Action(name="get_system_config_by_category", kwargs={"category": "design_system_config"})
        ],
        outputs=[
            "audit_002_verified:audit_002",
            "audit_status_updated:COMPLETED",
            "thread_001_updated:HIGH",
            "thread_008_updated:NORMAL",
            "approval_verified:approval_002",
            "art_audit_verified:art_008",
            "releases_retrieved:sarah.designer@company.com",
            "system_config_retrieved:design_system_config"
        ]
    ),

    Task(
        annotator="0",
        user_id="user_9",
        instruction=(
            "You are a mid-stage audit coordination specialist responsible for comprehensive audit workflows and finding analysis/system integration. "
            "Your task is to manage mid-stage audit coordination, finding analysis management, and system integration processes for enterprise audit management. "
            "Focus on managing audit finding details analysis, progress coordination, status management, and asset integration workflows with comprehensive mid-stage audit coordination. "
            "Coordinate with audit teams through appropriate channels to ensure all audit coordination and system integration workflows are properly orchestrated."
            "Required constants: "
            "audit_id=audit_002, include_resolved=True, finding_id=finding_a11y_002, "
            "progress_percentage=55, progress_notes=Mid-stage audit coordination advancing with comprehensive analysis, "
            "updated_by=mike.ux@company.com, new_finding_status=IN_PROGRESS, "
            "finding_notes=Mid-stage audit finding progressing with comprehensive coordination, "
            "asset_id=asset_002, category=email_templates, thread_id=thread_002, "
            "owner_email=mike.ux@company.com, created_after=2024-08-18T11:30:00Z, "
            "log_level=WARNING, component=mid_stage_audit_coordination"
        ),
        actions=[
            Action(name="update_audit_progress", kwargs={"audit_id": "audit_002", "progress_percentage": 55, "notes": "Mid-stage audit coordination advancing with comprehensive analysis", "updated_by": "mike.ux@company.com"}),
            Action(name="get_audit_finding_details", kwargs={"audit_id": "audit_002", "include_resolved": True}),
            Action(name="update_audit_finding_status", kwargs={"finding_id": "finding_a11y_002", "new_status": "IN_PROGRESS", "notes": "Mid-stage audit finding progressing with comprehensive coordination", "updated_by": "mike.ux@company.com"}),
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_002"}),
            Action(name="get_system_config_by_category", kwargs={"category": "email_templates"}),
            Action(name="get_gmail_threads_by_labels", kwargs={"thread_id": "thread_002"}),
            Action(name="get_releases_by_owner", kwargs={"owner_email": "mike.ux@company.com", "created_after": "2024-08-18T11:30:00Z"}),
            Action(name="get_terminal_logs_summary", kwargs={"log_level": "WARNING", "component": "mid_stage_audit_coordination"})
        ],
        outputs=[
            "Mid-stage audit coordination with finding analysis and system integration completed: audit_002 progress updated to 55% with mid-stage coordination analysis notes by Mike UX, audit finding details retrieved for audit_002 with resolved findings included for comprehensive mid-stage analysis, accessibility finding_a11y_002 status updated to IN_PROGRESS with mid-stage coordination notes by Mike UX, asset_002 export summary verified for asset coordination, email_templates config retrieved for system coordination, Gmail thread_002 verified for communication coordination, Mike UX releases retrieved for release coordination since August 18th, and terminal logs summary retrieved for WARNING level mid_stage_audit_coordination component."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_10",
        instruction=(
            "You are an audit report management specialist responsible for coordinating the end-to-end audit lifecycle for design system components. "
            "Your goal is to finalize the audit report for the Homepage Hero Section (art_001) and ensure all related components are properly tracked. "
            "Key objectives: "
            "- Update audit_001 status to COMPLETED with the final report asset_001 "
            "- Ensure audit_002 for admin panel components (art_008) is properly tracked with status IN_PROGRESS "
            "- Manage communication threads for design review and stakeholder updates "
            "- Document all audit findings and status changes "
            "Required constants: "
            "audit_001_status=COMPLETED, audit_002_status=IN_PROGRESS, "
            "report_asset_id=asset_001, completion_notes=Design system audit completed with recommendations, "
            "thread_001_priority=HIGH, thread_002_priority=NORMAL, "
            "thread_001_urgency=Critical audit findings require immediate design team attention, "
            "thread_002_urgency=Secondary audit review completed, "
            "escalate_to=sarah.designer@company.com,mike.ux@company.com, "
            "audit_type=COMBINED_DS_A11Y, created_after=2024-08-20T15:00:00Z, "
            "audit_date_filter=2024-08-18T00:00:00Z, thread_ids=thread_001,thread_002, "
            "artifact_ids=art_001,art_008, asset_id=asset_001, "
            "log_message=audit_001_completion_workflow, log_level=INFO, "
            "component=audit_management, user_email=sarah.designer@company.com"
        ),
        actions=[
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_001"}),
            Action(name="update_audit_report_status", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed with recommendations"}),
            Action(name="get_audits_by_status", kwargs={"status": "COMPLETED", "audit_type": "COMBINED_DS_A11Y"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical audit findings require immediate design team attention", "escalate_to": ["sarah.designer@company.com", "mike.ux@company.com"]}),
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_002"}),
            Action(name="get_audits_by_status", kwargs={"artifact_id": "art_001", "created_after": "2024-08-20T15:00:00Z"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Secondary audit review completed"}),
            Action(name="get_audits_by_status", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"}),
            Action(name="get_system_config_by_category", kwargs={"category": "audit_config"}),
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_001"}),
            Action(name="add_terminal_log_entry", kwargs={"log_message": "Audit management workflow completed with comprehensive tracking and report generation", "log_level": "INFO", "component": "audit_management", "user_email": "sarah.designer@company.com"})
        ],
        outputs=[
            "Audit management workflow completed: audit_001 status updated to COMPLETED with report asset_001 association and completion notes, thread_001 priority escalated to HIGH with critical findings urgency and stakeholder escalation to design team, secondary thread_002 priority normalized, comprehensive audit status verification completed across all COMBINED_DS_A11Y and A11Y audit types for stakeholder reporting, audit configuration retrieved for system coordination settings, asset export summary retrieved for asset_001 coordination and compliance tracking, and terminal log entry added documenting audit management workflow completion with comprehensive tracking."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_11",
        instruction=(
            "You are an audit report management specialist responsible for coordinating the end-to-end audit lifecycle for design system components and accessibility compliance. "
            "Your primary responsibility involves managing audit_001 for artifact art_001 (Homepage Hero Section) which requires comprehensive status tracking from COMPLETED to final report generation. The workflow integrates with audit_002 for accessibility review of art_008 admin panel components. "
            "The audit management workflow requires coordinating thread priorities across multiple stakeholders, with thread_001 requiring elevated attention for critical design review items. The system must maintain comprehensive documentation of all status changes and priority escalations. "
            "Key parameters: audit_id=audit_001, new_status=COMPLETED, report_asset_id=asset_001, completion_notes=Design system audit completed with recommendations, "
            "thread_001_priority=HIGH, thread_002_priority=NORMAL, thread_001_urgency=Critical audit findings require immediate design team attention and stakeholder review, thread_002_urgency=Secondary audit review completed, "
            "escalate_to=sarah.designer@company.com,mike.ux@company.com, audit_type=COMBINED_DS_A11Y, created_after=2024-08-20T15:00:00Z, audit_date_filter=2024-08-18T00:00:00Z, "
            "thread_ids=thread_001,thread_002, artifact_ids=art_001,art_008, "
            "asset_id=asset_001, audit_002_status=COMPLETED, updated_by=sarah.designer@company.com,"
        ),
        actions=[
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_001"}),
            Action(name="update_audit_report_status", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed with recommendations"}),
            Action(name="get_audits_by_status", kwargs={"status": "COMPLETED", "audit_type": "COMBINED_DS_A11Y"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical audit findings require immediate design team attention and stakeholder review", "escalate_to": ["sarah.designer@company.com", "mike.ux@company.com"]}),
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_002"}),
            Action(name="get_audits_by_status", kwargs={"artifact_id": "art_001", "created_after": "2024-08-20T15:00:00Z"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Secondary audit review completed"}),
            Action(name="get_audits_by_status", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"}),
            Action(name="get_system_config_by_category", kwargs={"category": "audit_config"}),
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_001"}),
            Action(name="update_audit_status", kwargs={"audit_id": "audit_002", "new_status": "COMPLETED", "updated_by": "sarah.designer@company.com"})
        ],
        outputs=[
            "Audit management workflow completed: audit_001 status updated to COMPLETED with report asset_001 association and completion notes, thread_001 priority escalated to HIGH with critical findings urgency and stakeholder escalation to design team, secondary thread_002 priority normalized, comprehensive audit status verification completed across all COMBINED_DS_A11Y and A11Y audit types for stakeholder reporting, audit configuration retrieved for system coordination settings, asset export summary retrieved for asset_001 coordination and compliance tracking, and audit_002 status updated to COMPLETED with sarah.designer@company.com coordination for comprehensive audit lifecycle management."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_12",
        instruction=(
            "You are a Figma comment resolution specialist responsible for accessibility feedback coordination and workflow management across admin panel header components. "
            "Your primary responsibility involves accessibility feedback coordination for art_008 admin panel header where unresolved comments with resolved_status False require identification and resolution coordination. The workflow also involves asset_007 admin header export integration requiring status verification and coordination alignment. "
            "The accessibility improvement workflow centers on comment_006 accessibility enhancement coordination involving mike.ux@company.com team member oversight, HIGH priority accessibility improvements, and comprehensive ARIA labels and keyboard navigation support implementation tracking. The feedback resolution requires progress status coordination and detailed implementation documentation. "
            "Your coordination efforts should ensure seamless accessibility audit communication through thread_004, effective comment lifecycle coordination, and comprehensive accessibility compliance tracking for stakeholder reporting and successful workflow completion."
            "You can use resolution_notes Accessibility improvements in progress - adding ARIA labels and keyboard navigation support"
        ),
        actions=[
            Action(name="get_figma_comments_by_artifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_007"}),
            Action(name="update_figma_comment_status", kwargs={"comment_id": "comment_006", "new_status": "IN_PROGRESS", "resolution_notes": "Accessibility improvements in progress - adding ARIA labels and keyboard navigation support", "assignee_email": "mike.ux@company.com", "priority_level": "HIGH"}),
            Action(name="get_gmail_threads_by_labels", kwargs={"thread_id": "thread_004"}),
            Action(name="get_figma_comments_by_artifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="add_terminal_log_entry", kwargs={"log_message": "Figma comment resolution workflow completed for accessibility improvements", "log_level": "INFO", "component": "figma_comment_resolution", "user_email": "mike.ux@company.com"})
        ],
        outputs=[
            "Comment resolution workflow completed. comment status updated, assignee assigned to Mike UX with HIGH priority level, resolution notes added about accessibility improvements, asset export status verified for admin header asset_007, Gmail thread communication status verified for thread_004 accessibility audit coordination, and terminal log entry added for comment resolution workflow tracking."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_13",
        instruction=(
            "You are a Figma comment resolution specialist responsible for accessibility feedback coordination and workflow management across admin panel header components. "
            "Your primary responsibility involves accessibility feedback coordination for art_008 admin panel header where unresolved comments with resolved_status False require identification and resolution coordination. The workflow also involves asset_007 admin header export integration requiring status verification and coordination alignment. "
            "The accessibility improvement workflow centers on comment_006 accessibility enhancement coordination involving mike.ux@company.com team member oversight, HIGH priority accessibility improvements, and comprehensive ARIA labels and keyboard navigation support implementation tracking. The feedback resolution requires progress status coordination and detailed implementation documentation. "
            "Your coordination efforts should ensure seamless accessibility audit communication through thread_004, effective comment lifecycle coordination, and comprehensive accessibility compliance tracking for stakeholder reporting and successful workflow completion."
            "You can use resolution_notes Accessibility improvements in progress - adding ARIA labels and keyboard navigation support"
        ),
        actions=[
            Action(name="get_figma_comments_by_artifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_007"}),
            Action(name="update_figma_comment_status", kwargs={"comment_id": "comment_006", "new_status": "IN_PROGRESS", "resolution_notes": "Accessibility improvements in progress - adding ARIA labels and keyboard navigation support", "assignee_email": "mike.ux@company.com", "priority_level": "HIGH"}),
            Action(name="get_gmail_threads_by_labels", kwargs={"thread_id": "thread_004"}),
            Action(name="get_figma_comments_by_artifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="get_system_config_by_category", kwargs={"category": "accessibility_config"})
        ],
        outputs=[
            "Comment resolution workflow completed. comment status updated, assignee assigned to Mike UX with HIGH priority level, resolution notes added about accessibility improvements, asset export status verified for admin header asset_007, Gmail thread communication status verified for thread_004 accessibility audit coordination, and system configuration retrieved for accessibility_config category."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_14",
        instruction=(
            "You are a Figma comment resolution specialist responsible for accessibility feedback coordination and workflow management across admin panel header components. "
            "Your primary responsibility involves accessibility feedback coordination for art_008 admin panel header where unresolved comments with resolved_status False require identification and resolution coordination. The workflow also involves asset_007 admin header export integration requiring status verification and coordination alignment. "
            "The accessibility improvement workflow centers on comment_006 accessibility enhancement coordination involving mike.ux@company.com team member oversight, HIGH priority accessibility improvements, and comprehensive ARIA labels and keyboard navigation support implementation tracking. The feedback resolution requires progress status coordination and detailed implementation documentation. "
            "Your coordination efforts should ensure seamless accessibility audit communication through thread_004, effective comment lifecycle coordination, and comprehensive accessibility compliance tracking for stakeholder reporting and successful workflow completion."
            "You can use resolution_notes Accessibility improvements in progress - adding ARIA labels and keyboard navigation support"
            "Use these specific constants: "
            "audit_id=audit_008, "
            "owner_email=mike.ux@company.com, "
            "created_after=2024-08-19T12:00:00Z, "
            "log_message=Accessibility comment resolution workflow completed for art_008 admin panel header, "
            "component=accessibility_resolution"
        ),
        actions=[
            Action(name="get_figma_comments_by_artifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_007"}),
            Action(name="update_figma_comment_status", kwargs={"comment_id": "comment_006", "new_status": "IN_PROGRESS", "resolution_notes": "Accessibility improvements in progress - adding ARIA labels and keyboard navigation support", "assignee_email": "mike.ux@company.com", "priority_level": "HIGH"}),
            Action(name="get_gmail_threads_by_labels", kwargs={"thread_id": "thread_004"}),
            Action(name="get_figma_comments_by_artifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="add_terminal_log_entry", kwargs={"log_message": "Accessibility comment resolution workflow completed for art_008 admin panel header", "log_level": "INFO", "component": "accessibility_resolution", "user_email": "mike.ux@company.com"}),
            Action(name="get_audit_summary", kwargs={"audit_id": "audit_008"})

        ],
        outputs=[
            "Comment resolution workflow completed. comment status updated, assignee assigned to Mike UX with HIGH priority level, resolution notes added about accessibility improvements, asset export status verified for admin header asset_007, Gmail thread communication status verified for thread_004 accessibility audit coordination, terminal log entry added for accessibility comment resolution workflow tracking, and audit_008 summary verified for accessibility audit coordination."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_15",
        instruction=(
            "You are a release diff analysis specialist responsible for coordinating release difference tracking and integrated comment resolution workflows. "
            "Your task is to manage release diff coordination with figma comment resolution and ensure proper version tracking. "
            "Focus on managing release version updates with comprehensive comment status coordination and asset export verification. "
            "Coordinate with development teams through appropriate channels to ensure all release diffs and comment workflows are properly synchronized. "
            "Required constants: "
            "release_id=release_001, version_id=v1.4.0, release_name=Design System v1.4.0 - Diff Analysis Updates, "
            "owner_email=sarah.designer@company.com, comment_id=comment_001, new_status=RESOLVED, "
            "assignee_email=sarah.designer@company.com, priority_level=NORMAL, "
            "resolution_notes=Release diff analysis completed with comprehensive comment resolution, "
            "artifact_id=art_001, asset_id=asset_001, export_status=COMPLETED, "
            "dlp_scan_status=CLEAN, created_after=2024-08-20T15:00:00Z, "
            "thread_id=thread_001, export_notes=Release diff analysis asset export completed"
        ),
        actions=[
            Action(name="get_release_diff_summary", kwargs={"release_id": "release_001"}),
            Action(name="update_release_version", kwargs={"release_id": "release_001", "version_id": "v1.4.0", "release_name": "Design System v1.4.0 - Diff Analysis Updates", "owner_email": "sarah.designer@company.com", "thread_id": "thread_001"}),
            Action(name="get_figma_comments_by_artifact", kwargs={"artifact_id": "art_001", "resolved_status": False}),
            Action(name="update_figma_comment_status", kwargs={"comment_id": "comment_001", "new_status": "RESOLVED", "resolution_notes": "Release diff analysis completed with comprehensive comment resolution", "assignee_email": "sarah.designer@company.com", "priority_level": "NORMAL"}),
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_001"}),
            Action(name="update_asset_export_status", kwargs={"asset_id": "asset_001", "new_status": "COMPLETED", "notes": "Release diff analysis asset export completed", "dlp_scan_status": "CLEAN"}),
            Action(name="get_releases_by_owner", kwargs={"owner_email": "sarah.designer@company.com", "created_after": "2024-08-20T15:00:00Z"}),
            Action(name="add_terminal_log_entry", kwargs={"log_message": "Release diff analysis workflow completed - version v1.4.0 updated with comment resolution", "log_level": "INFO", "component": "release_diff_analysis", "user_email": "sarah.designer@company.com"})
        ],
        outputs=[
            "Release diff analysis completed for release_001: release diff summary verified for comprehensive analysis workflow, release version updated to v1.4.0 with diff analysis updates and Sarah Designer ownership, unresolved figma comments retrieved for art_001 artifact coordination, comment_001 status updated to RESOLVED with comprehensive resolution notes and Sarah Designer assignment at NORMAL priority, asset export summary verified for asset_001 coordination, export status updated to COMPLETED with diff analysis notes and CLEAN DLP scan, Sarah Designer releases verified for coordination since August 20th, and terminal log entry added documenting release diff analysis workflow completion."
        ]
    ),
    Task(
        annotator="0",
        user_id="user_16",
        instruction=(
            "You are a review management coordination specialist responsible for orchestrating comprehensive review workflows and audit status updates. "
            "Your task is to manage review cycle coordination, artifact tracking, and audit status management for design system components. "
            "Focus on managing review approvals, active artifact verification, system configuration checks, and audit status coordination with proper workflow management. "
            "Coordinate with UX teams through appropriate channels to ensure all review management processes are properly tracked and updated. "
            "Required constants: "
            "cycle_id=cycle_001, status=ACTIVE, category=gmail_labels, asset_id=asset_006, "
            "thread_id=thread_007, owner_email=mike.ux@company.com, created_after=2024-08-20T16:30:00Z, "
            "audit_id=audit_007, new_status=IN_PROGRESS, updated_by=mike.ux@company.com, "
            "notes=Review management coordination completed with audit workflow, log_level=INFO, component=review_management"
        ),
        actions=[
            Action(name="get_review_approvals_summary", kwargs={"cycle_id": "cycle_001"}),
            Action(name="get_figma_artifacts_by_status", kwargs={"status": "ACTIVE"}),
            Action(name="get_system_config_by_category", kwargs={"category": "gmail_labels"}),
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_006"}),
            Action(name="get_gmail_threads_by_labels", kwargs={"thread_id": "thread_007"}),
            Action(name="get_releases_by_owner", kwargs={"owner_email": "mike.ux@company.com", "created_after": "2024-08-20T16:30:00Z"}),
            Action(name="update_audit_status", kwargs={"audit_id": "audit_007", "new_status": "IN_PROGRESS", "updated_by": "mike.ux@company.com", "notes": "Review management coordination completed with audit workflow"})
        ],
        outputs=[
            "review_approvals_retrieved:cycle_001",
            "figma_artifacts_retrieved:ACTIVE",
            "system_config_retrieved:gmail_labels",
            "asset_export_verified:asset_006",
            "gmail_thread_retrieved:thread_007",
            "releases_retrieved:mike.ux@company.com:2024-08-20T16:30:00Z",
            "audit_status_updated:audit_007:IN_PROGRESS:mike.ux@company.com"
        ]
    ),
    
    Task(
        annotator="0",
        user_id="user_17",
        instruction=(
            "You are an audit report management specialist responsible for coordinating the end-to-end audit lifecycle for design system components and accessibility compliance. "
            "Your primary responsibility involves managing audit_001 for artifact art_001 (Homepage Hero Section) which requires comprehensive status tracking from COMPLETED to final report generation. The workflow integrates with audit_002 for accessibility review of art_008 admin panel components requiring status coordination. "
            "The audit management workflow centers on thread_001 priority escalation to HIGH priority for design review coordination involving sarah.designer@company.com oversight, URGENT priority level escalation for comprehensive design review tracking, and escalation_reason 'Critical audit findings require immediate design team attention'. The priority management requires comprehensive Gmail thread coordination and detailed audit status documentation. "
            "Your coordination efforts should ensure seamless audit report generation through proper status management, effective priority escalation for design review threads, and comprehensive audit findings tracking for stakeholder reporting. "
            "Key parameters: audit_id=audit_001, new_status=COMPLETED, report_asset_id=asset_001, completion_notes=Design system audit completed with recommendations, "
            "thread_001_priority=HIGH, thread_002_priority=NORMAL, thread_001_urgency=Critical audit findings require immediate design team attention, thread_002_urgency=Secondary audit review completed, "
            "escalate_to=sarah.designer@company.com,mike.ux@company.com, audit_type=COMBINED_DS_A11Y, created_after=2024-08-20T15:00:00Z, audit_date_filter=2024-08-18T00:00:00Z, "
            "thread_ids=thread_001,thread_002, artifact_ids=art_001,art_008, fix_item_id=item_001, completion_date=2024-08-27T15:00:00Z"
        ),
        actions=[
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_001"}),
            Action(name="update_audit_report_status", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed with recommendations"}),
            Action(name="get_audits_by_status", kwargs={"status": "COMPLETED", "audit_type": "COMBINED_DS_A11Y"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical audit findings require immediate design team attention", "escalate_to": ["sarah.designer@company.com", "mike.ux@company.com"]}),
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_002"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Secondary audit review completed"}),
            Action(name="get_audits_by_status", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"}),
            Action(name="update_fix_item_status", kwargs={"fix_item_id": "item_001", "new_status": "VERIFIED", "completion_date": "2024-08-27T15:00:00Z"})
        ],
        outputs=[
            "Audit management workflow completed: audit_001 status updated to COMPLETED with report asset_001 association and completion notes, thread_001 priority escalated to HIGH with critical findings urgency and stakeholder escalation to design team, comprehensive audit verification completed for A11Y audit type, and fix item_001 updated to VERIFIED status for audit remediation tracking."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_18",
        instruction=(
            "You are an audit report management specialist finalizing the audit lifecycle for design system components. "
            "Update audit_001 and audit_002 to COMPLETED status and normalize thread priorities to NORMAL/LOW. "
            "Key parameters: "
            "audit_001:status=COMPLETED,report_asset=asset_001,notes=Design system audit completed and finalized; "
            "audit_002:status=COMPLETED,report_asset=asset_007; "
            "thread_001:priority=NORMAL,escalate_to=sarah.designer@company.com,mike.ux@company.com,reason=Audit review completed; "
            "thread_002:priority=LOW,reason=Audit follow-up completed"
        ),
        actions=[
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_001"}),
            Action(name="update_audit_report_status", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed and finalized"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_001", "new_priority": "NORMAL", "urgency_reason": "Audit review completed", "escalate_to": ["sarah.designer@company.com", "mike.ux@company.com"]}),
            Action(name="update_audit_report_status", kwargs={"audit_id": "audit_002", "new_status": "COMPLETED", "report_asset_id": "asset_007"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_002", "new_priority": "LOW", "urgency_reason": "Audit follow-up completed"}),
            Action(name="add_terminal_log_entry", kwargs={"log_message": "Audit finalization completed for audit_001 and audit_002", "log_level": "INFO", "component": "audit_workflow", "user_email": "sarah.designer@company.com"})
        ],
        outputs=[
            "audit_001:status=COMPLETED,report_asset=asset_001",
            "audit_002:status=COMPLETED,report_asset=asset_007",
            "thread_001:priority=NORMAL,escalated_to=sarah.designer@company.com,mike.ux@company.com",
            "thread_002:priority=LOW,reason=Audit follow-up completed",
            "log:entry=Audit finalization completed for audit_001 and audit_002"
        ]
    ),
    Task(
        annotator="0",
        user_id="user_19",
        instruction=(
            "You are an audit report management specialist responsible for coordinating the end-to-end audit lifecycle for design system components and accessibility compliance. "
            "Your primary responsibility involves managing audit_001 for artifact art_001 (Homepage Hero Section) which requires comprehensive status tracking from COMPLETED to final report generation. The workflow integrates with audit_002 for accessibility review of art_008 admin panel components requiring status coordination. "
            "The audit management workflow centers on thread_001 priority escalation to HIGH priority for design review coordination involving sarah.designer@company.com oversight, URGENT priority level escalation for comprehensive design review tracking, and escalation_reason 'Critical audit findings require immediate design team attention and stakeholder review'. The priority management requires comprehensive Gmail thread coordination and detailed audit status documentation. "
            "Your coordination efforts should ensure seamless audit report generation through proper status management, effective priority escalation for design review threads, comprehensive audit findings tracking for stakeholder reporting, and successful audit lifecycle completion with proper report asset associations. "
            "Key parameters: audit_id=audit_001, new_status=COMPLETED, report_asset_id=asset_001, completion_notes=Design system audit completed with recommendations, "
            "thread_001_priority=HIGH, thread_002_priority=NORMAL, thread_001_urgency=Critical audit findings require immediate design team attention, thread_002_urgency=Secondary audit review completed, "
            "escalate_to=sarah.designer@company.com,mike.ux@company.com, audit_type=COMBINED_DS_A11Y, created_after=2024-08-20T15:00:00Z, audit_date_filter=2024-08-18T00:00:00Z, "
            "thread_ids=thread_001,thread_002, artifact_ids=art_001,art_008"
        ),
        actions=[
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_001"}),
            Action(name="update_audit_report_status", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed with recommendations"}),
            Action(name="get_audits_by_status", kwargs={"status": "COMPLETED", "audit_type": "COMBINED_DS_A11Y"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical audit findings require immediate design team attention", "escalate_to": ["sarah.designer@company.com", "mike.ux@company.com"]}),
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_002"}),
            Action(name="get_audits_by_status", kwargs={"artifact_id": "art_001", "created_after": "2024-08-20T15:00:00Z"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Secondary audit review completed"}),
            Action(name="get_audits_by_status", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"})
        ],
        outputs=[
            "Audit management workflow completed: audit_001 status updated to COMPLETED with report asset_001 association and completion notes, thread_001 priority escalated to HIGH with critical findings urgency and stakeholder escalation to design team, secondary thread_002 priority normalized, and comprehensive audit status verification completed across all COMBINED_DS_A11Y and A11Y audit types for stakeholder reporting."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_20",
        instruction=(
            "You are an email workflow manager responsible for coordinating the Homepage Hero Section design review process across stakeholder communication and approval workflows. "
            "Your task is to ensure the Homepage Hero Section review is properly transitioned to approved status with all necessary stakeholder coordination. The review involves thread_001, which requires status updates, label management, and expanded stakeholder communication. "
            "The review workflow includes verification of audit_001 findings and art_001 Figma artifacts, along with updating the review cycle status to reflect approval. The goal is to ensure a smooth transition to production readiness with proper documentation and stakeholder notification. "
            "All actions should maintain the integrity of the design review process while ensuring clear communication across all teams involved in the production handoff."
            "Required constants: "
            "audit_id=audit_001, new_status=COMPLETED, updated_by=email_workflow_manager_001, notes=Homepage hero section design review completed and approved, "
            "thread_id=thread_001, new_labels=approved,figma-integrated, remove_labels=urgent, "
            "recipients=mike.ux@company.com,alex.dev@company.com,lisa.marketing@company.com,design-team@company.com, "
            "cycle_id=cycle_001, approver_id=email_workflow_manager_001, "
            "approval_comments=Homepage hero section approved after comprehensive review - updating review cycle status and coordinating with email workflow"
        ),
        actions=[
            Action(name="get_gmail_threads_by_labels", kwargs={"thread_id": "thread_001"}),
            Action(name="get_figma_artifacts_by_status", kwargs={"artifact_id": "art_001"}),
            Action(name="get_audit_findings_summary", kwargs={"audit_id": "audit_001"}),
            Action(name="update_gmail_thread_labels", kwargs={"thread_id": "thread_001", "new_labels": ["approved", "figma-integrated"], "remove_labels": ["urgent"], "update_recipients": ["mike.ux@company.com", "alex.dev@company.com", "lisa.marketing@company.com", "design-team@company.com"]}),
            Action(name="update_review_cycle_status", kwargs={"cycle_id": "cycle_001", "new_status": "APPROVED", "approver_id": "email_workflow_manager_001", "comments": "Homepage hero section approved after comprehensive review - updating review cycle status and coordinating with email workflow"}),
            Action(name="update_audit_status", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "notes": "Homepage hero section design review completed and approved", "updated_by": "email_workflow_manager_001"}),
            Action(name="get_gmail_threads_by_labels", kwargs={"thread_id": "thread_001"}),
            Action(name="get_figma_artifacts_by_status", kwargs={"artifact_id": "art_001"})
        ],
        outputs=[
            "Email workflow management completed for thread_001: Gmail thread labels updated from urgent to approved/figma-integrated, recipients expanded to include design-team@company.com, review cycle cycle_001 status updated to APPROVED, audit_001 status updated to COMPLETED with review notes, and coordination completed between email workflow and design review processes for seamless production handoff."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_21",
        instruction=(
            "You are an accessibility compliance specialist responsible for audit findings coordination and fix item management across admin panel accessibility initiatives. "
            "Your primary responsibility involves accessibility audit coordination for audit_002, audit_004, and audit_005 where comprehensive findings analysis and fix item status updates require systematic processing. The workflow involves fix item lifecycle management following proper status progression. "
            "The accessibility compliance workflow centers on item_001 touch target verification with VERIFIED status achievement, item_004 font size compliance with APPLIED status and completion timestamp coordination, and item_002 contrast violation remediation with IN_PROGRESS status management. The fix implementation requires systematic status coordination and compliance verification. "
            "Your coordination efforts should ensure comprehensive audit findings analysis, proper fix item lifecycle management, and successful accessibility compliance tracking for stakeholder reporting and workflow completion."
        ),
        actions=[
            Action(name="get_audit_findings_summary", kwargs={"audit_id": "audit_002"}),
            Action(name="get_audit_findings_summary", kwargs={"audit_id": "audit_004"}),
            Action(name="get_audit_findings_summary", kwargs={"audit_id": "audit_005"}),
            Action(name="update_fix_item_status", kwargs={"fix_item_id": "item_001", "new_status": "VERIFIED"}),
            Action(name="update_fix_item_status", kwargs={"fix_item_id": "item_004", "new_status": "APPLIED", "completion_date": "2024-08-25T15:30:00Z"}),
            Action(name="update_fix_item_status", kwargs={"fix_item_id": "item_002", "new_status": "IN_PROGRESS"}),
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_007"})
        ],
        outputs=[
            "Accessibility compliance workflow completed: audit findings analyzed for audit_002, audit_004, and audit_005, item_001 updated to VERIFIED status, item_004 updated to APPLIED status with completion date 2024-08-25T15:30:00Z, item_002 updated to IN_PROGRESS status for continued accessibility improvements, and asset export summary verified for asset_007 accessibility compliance coordination."
        ]
    ),
    Task(
        annotator="0",
        user_id="user_22",
        instruction=(
            "You are a Figma comment resolution specialist responsible for accessibility feedback coordination and workflow management across admin panel header components. "
            "Your primary responsibility involves accessibility feedback coordination for art_008 admin panel header where unresolved comments with resolved_status False require identification and resolution coordination. The workflow also involves asset_007 admin header export integration requiring status verification and coordination alignment. "
            "The accessibility improvement workflow centers on comment_006 accessibility enhancement coordination involving mike.ux@company.com team member oversight, HIGH priority accessibility improvements, and comprehensive ARIA labels and keyboard navigation support implementation tracking. The feedback resolution requires progress status coordination and detailed implementation documentation. "
            "Your coordination efforts should ensure seamless accessibility audit communication through thread_004, effective comment lifecycle coordination, and comprehensive accessibility compliance tracking for stakeholder reporting and successful workflow completion."
        ),
        actions=[
            Action(name="get_figma_comments_by_artifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_007"}),
            Action(name="update_figma_comment_status", kwargs={"comment_id": "comment_006", "new_status": "IN_PROGRESS", "resolution_notes": "Accessibility improvements in progress - adding ARIA labels and keyboard navigation support", "assignee_email": "mike.ux@company.com", "priority_level": "HIGH"}),
            Action(name="get_gmail_threads_by_labels", kwargs={"thread_id": "thread_004"}),
            Action(name="get_figma_comments_by_artifact", kwargs={"artifact_id": "art_008", "resolved_status": False})
        ],
        outputs=[
            "Comment resolution workflow completed for comment_006: comment status updated to IN_PROGRESS, assignee assigned to Mike UX with HIGH priority level, resolution notes added about accessibility improvements, asset export status verified for admin header asset_007, and Gmail thread communication status verified for thread_004 accessibility audit coordination."
        ]
    ),
    Task(
        annotator="0",
        user_id="user_23",
        instruction=(
            "You are an audit report management specialist responsible for coordinating the end-to-end audit lifecycle for design system components and accessibility compliance. "
            "Your primary responsibility involves managing audit_001 for artifact art_001 (Homepage Hero Section) which requires comprehensive status tracking from COMPLETED to final report generation. The workflow integrates with audit_002 for accessibility review of art_008 admin panel components requiring status coordination. "
            "The audit management workflow centers on thread_001 priority escalation to HIGH priority for design review coordination involving sarah.designer@company.com oversight, URGENT priority level escalation for comprehensive design review tracking, and escalation_reason 'Critical audit findings require immediate design team attention and stakeholder review'. The priority management requires comprehensive Gmail thread coordination and detailed audit status documentation. "
            "Your coordination efforts should ensure seamless audit report generation through proper status management, effective priority escalation for design review threads, comprehensive audit findings tracking for stakeholder reporting, and successful audit lifecycle completion with proper report asset associations. "
            "Key parameters: audit_id=audit_001, new_status=COMPLETED, report_asset_id=asset_001, completion_notes=Design system audit completed with recommendations, "
            "thread_001_priority=HIGH, thread_002_priority=NORMAL, thread_001_urgency=Critical audit findings require immediate design team attention, thread_002_urgency=Secondary audit review completed, "
            "escalate_to=sarah.designer@company.com,mike.ux@company.com, audit_type=COMBINED_DS_A11Y, created_after=2024-08-20T15:00:00Z, audit_date_filter=2024-08-18T00:00:00Z, "
            "thread_ids=thread_001,thread_002, artifact_ids=art_001,art_008, "
            "log_message=Audit management workflow completed with comprehensive report generation and status tracking, "
            "log_level=INFO, component=audit_lifecycle, user_email=sarah.designer@company.com"
        ),
        actions=[
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_001"}),
            Action(name="update_audit_report_status", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed with recommendations"}),
            Action(name="get_audits_by_status", kwargs={"status": "COMPLETED", "audit_type": "COMBINED_DS_A11Y"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical audit findings require immediate design team attention", "escalate_to": ["sarah.designer@company.com", "mike.ux@company.com"]}),
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_002"}),
            Action(name="update_audit_report_status", kwargs={"audit_id": "audit_002", "new_status": "COMPLETED", "report_asset_id": "asset_007"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Secondary audit review completed"}),
            Action(name="get_audits_by_status", kwargs={"status": "COMPLETED", "created_after": "2024-08-20T15:00:00Z"}),
            Action(name="get_audits_by_status", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"}),
            Action(name="add_terminal_log_entry", kwargs={"log_message": "Audit management workflow completed with comprehensive report generation and status tracking", "log_level": "INFO", "component": "audit_lifecycle", "user_email": "sarah.designer@company.com"})
        ],
        outputs=[
            "Audit management workflow completed: audit_001 status updated to COMPLETED with report asset_001 association and completion notes, thread_001 priority escalated to HIGH with critical findings urgency and stakeholder escalation to design team, audit_002 status updated to COMPLETED with report asset_007, secondary thread_002 priority normalized, comprehensive audit status verification completed across all COMBINED_DS_A11Y and A11Y audit types for stakeholder reporting, and terminal log entry added documenting audit management workflow completion with comprehensive report generation and status tracking."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_24",
        instruction=(
            "You are a Figma comment resolution specialist responsible for accessibility feedback coordination and workflow management across admin panel header components. "
            "Your primary responsibility involves accessibility feedback coordination for art_008 admin panel header where unresolved comments with resolved_status False require identification and resolution coordination. The workflow also involves asset_007 admin header export integration requiring status verification and coordination alignment. "
            "The accessibility improvement workflow centers on comment_006 accessibility enhancement coordination involving mike.ux@company.com team member oversight, HIGH priority accessibility improvements, and comprehensive ARIA labels and keyboard navigation support implementation tracking. The feedback resolution requires progress status coordination and detailed implementation documentation. "
            "Your coordination efforts should ensure seamless accessibility audit communication through thread_004, effective comment lifecycle coordination, and comprehensive accessibility compliance tracking for stakeholder reporting and successful workflow completion."
            "Use resolution_notes=Accessibility improvements in progress - adding ARIA labels and keyboard navigation support"
            ",notes=Admin header accessibility export completed with ARIA labels"
        ),
        actions=[
            Action(name="get_figma_comments_by_artifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_007"}),
            Action(name="update_figma_comment_status", kwargs={"comment_id": "comment_006", "new_status": "IN_PROGRESS", "resolution_notes": "Accessibility improvements in progress - adding ARIA labels and keyboard navigation support", "assignee_email": "mike.ux@company.com", "priority_level": "HIGH"}),
            Action(name="get_gmail_threads_by_labels", kwargs={"thread_id": "thread_004"}),
            Action(name="get_figma_comments_by_artifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="update_asset_export_status", kwargs={"asset_id": "asset_007", "new_status": "COMPLETED", "notes": "Admin header accessibility export completed with ARIA labels", "dlp_scan_status": "CLEAN"}),
            Action(name="get_terminal_logs_summary", kwargs={"log_level": "INFO", "component": "accessibility_coordination"})
        ],
        outputs=[
            "Comment resolution workflow completed for comment_006: comment status updated to IN_PROGRESS, assignee assigned to Mike UX with HIGH priority level, resolution notes added about accessibility improvements, asset export status verified for admin header asset_007, Gmail thread communication status verified for thread_004 accessibility audit coordination, asset export updated to COMPLETED with accessibility enhancements, and terminal logs summary retrieved for accessibility coordination component tracking."
        ]
    ),
    Task(
        annotator="0",
        user_id="user_25",
        instruction=(
            "You are an audit report management specialist responsible for coordinating the end-to-end audit lifecycle for design system components and accessibility compliance. "
            "Your primary responsibility involves managing audit_001 for artifact art_001 (Homepage Hero Section) which requires comprehensive status tracking from COMPLETED to final report generation. The workflow integrates with audit_002 for accessibility review of art_008 admin panel components requiring status coordination. "
            "The audit management workflow centers on thread_001 priority escalation to HIGH priority for design review coordination involving sarah.designer@company.com oversight, URGENT priority level escalation for comprehensive design review tracking, and escalation_reason 'Critical audit findings require immediate design team attention and stakeholder review'. The priority management requires comprehensive Gmail thread coordination and detailed audit status documentation. "
            "Your coordination efforts should ensure seamless audit report generation through proper status management, effective priority escalation for design review threads, and comprehensive audit findings tracking for stakeholder reporting. "
            "Key parameters: audit_id=audit_001, new_status=COMPLETED, report_asset_id=asset_001, completion_notes=Design system audit completed with recommendations, "
            "thread_001_priority=HIGH, thread_002_priority=NORMAL, thread_001_urgency=Critical audit findings require immediate design team attention, thread_002_urgency=Secondary audit review completed, "
            "escalate_to=sarah.designer@company.com,mike.ux@company.com, audit_type=COMBINED_DS_A11Y, created_after=2024-08-20T15:00:00Z, audit_date_filter=2024-08-18T00:00:00Z, "
            "thread_ids=thread_001,thread_002, artifact_ids=art_001,art_008, "
            "audit_summary_id=audit_001"
        ),
        actions=[
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_001"}),
            Action(name="update_audit_report_status", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed with recommendations"}),
            Action(name="get_audits_by_status", kwargs={"status": "COMPLETED", "audit_type": "COMBINED_DS_A11Y"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical audit findings require immediate design team attention", "escalate_to": ["sarah.designer@company.com", "mike.ux@company.com"]}),
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_002"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Secondary audit review completed"}),
            Action(name="get_audits_by_status", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"}),
            Action(name="get_audit_summary", kwargs={"audit_id": "audit_001"})
        ],
        outputs=[
            "Audit management workflow completed: audit_001 status updated to COMPLETED with report asset_001 association and completion notes, thread_001 priority escalated to HIGH with critical findings urgency and stakeholder escalation to design team, comprehensive audit verification completed for A11Y audit type, and comprehensive audit_001 summary retrieved for report documentation and compliance verification."
        ]
    ),
    Task(
        annotator="0",
        user_id="user_26",
        instruction=(
            "You are a Figma comment resolution specialist responsible for accessibility feedback coordination and workflow management across admin panel header components. "
            "Your primary responsibility involves accessibility feedback coordination for art_008 admin panel header where unresolved comments with resolved_status False require identification and resolution coordination. The workflow also involves asset_007 admin header export integration requiring status verification and coordination alignment. "
            "The accessibility improvement workflow centers on comment_006 accessibility enhancement coordination involving mike.ux@company.com team member oversight, HIGH priority accessibility improvements, and comprehensive ARIA labels and keyboard navigation support implementation tracking. The feedback resolution requires progress status coordination and detailed implementation documentation. "
            "Your coordination efforts should ensure seamless accessibility audit communication through thread_004, effective comment lifecycle coordination, and comprehensive accessibility compliance tracking for stakeholder reporting and successful workflow completion."
            "You can use resolution_notes Accessibility improvements in progress - adding ARIA labels and keyboard navigation support"
            "Required constants: plan_id=plan_005,resolution_notes=Accessibility improvements in progress - adding ARIA labels and keyboard navigation support,new_status=IN_PROGRESS"
        ),
        actions=[
            Action(name="get_figma_comments_by_artifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_007"}),
            Action(name="update_figma_comment_status", kwargs={"comment_id": "comment_006", "new_status": "IN_PROGRESS", "resolution_notes": "Accessibility improvements in progress - adding ARIA labels and keyboard navigation support", "assignee_email": "mike.ux@company.com", "priority_level": "HIGH"}),
            Action(name="get_gmail_threads_by_labels", kwargs={"thread_id": "thread_004"}),
            Action(name="get_figma_comments_by_artifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="update_fix_plan_status", kwargs={"plan_id": "plan_005", "new_status": "IN_PROGRESS"})
        ],
        outputs=[
            "Comment resolution workflow completed. comment status updated, assignee assigned to Mike UX with HIGH priority level, resolution notes added about accessibility improvements, asset export status verified for admin header asset_007, Gmail thread communication status verified for thread_004 accessibility audit coordination, and fix plan plan_005 updated to IN_PROGRESS status."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_27",
        instruction=(
            "You are a Figma comment resolution specialist responsible for accessibility feedback coordination and workflow management across admin panel header components. "
            "Your primary responsibility involves accessibility feedback coordination for art_008 admin panel header where unresolved comments with resolved_status False require identification and resolution coordination. The workflow also involves asset_007 admin header export integration requiring status verification and coordination alignment. "
            "The accessibility improvement workflow centers on comment_006 accessibility enhancement coordination involving mike.ux@company.com team member oversight, HIGH priority accessibility improvements, and comprehensive ARIA labels and keyboard navigation support implementation tracking. The feedback resolution requires progress status coordination and detailed implementation documentation. "
            "Your coordination efforts should ensure seamless accessibility audit communication through thread_004, effective comment lifecycle coordination, and comprehensive accessibility compliance tracking for stakeholder reporting and successful workflow completion."
            "You can use resolution_notes Accessibility improvements in progress - adding ARIA labels and keyboard navigation support"
        ),
        actions=[
            Action(name="get_figma_comments_by_artifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_007"}),
            Action(name="update_figma_comment_status", kwargs={"comment_id": "comment_006", "new_status": "IN_PROGRESS", "resolution_notes": "Accessibility improvements in progress - adding ARIA labels and keyboard navigation support", "assignee_email": "mike.ux@company.com", "priority_level": "HIGH"}),
            Action(name="get_gmail_threads_by_labels", kwargs={"thread_id": "thread_004"}),
            Action(name="get_figma_comments_by_artifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="add_terminal_log_entry", kwargs={"log_message": "Accessibility comment resolution workflow completed for art_008 admin panel header", "log_level": "INFO", "component": "accessibility_resolution", "user_email": "mike.ux@company.com"})
        ],
        outputs=[
            "Comment resolution workflow completed. comment status updated, assignee assigned to Mike UX with HIGH priority level, resolution notes added about accessibility improvements, asset export status verified for admin header asset_007, Gmail thread communication status verified for thread_004 accessibility audit coordination, and terminal log entry added for accessibility comment resolution workflow tracking."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_28",
        instruction=(
            "You are an audit report management specialist responsible for coordinating the completion of multiple audits, specifically audit_001 for the Homepage Hero Section (art_001) and audit_002 for the admin panel components (art_008). Your responsibilities include verifying and updating audit statuses, generating final reports, coordinating with design and accessibility teams, managing stakeholder communications, and maintaining comprehensive documentation. "
            "For audit_001, ensure the status is updated to COMPLETED with report_asset_id=asset_001 and appropriate completion notes. For audit_002, verify the status and associate it with report_asset_id=asset_007. "
            "Manage thread priorities with thread_001 set to HIGH priority for critical findings requiring immediate design team attention, and thread_002 set to NORMAL priority for secondary review completion. "
            "Key parameters: "
            "- Audit details: "
            "  * audit_001: COMPLETED status with report_asset_id=asset_001 (COMBINED_DS_A11Y type) "
            "  * audit_002: COMPLETED status with report_asset_id=asset_007 (A11Y type) "
            "  * completion_notes=Design system audit completed with recommendations "
            "- Thread management: "
            "  * thread_001: HIGH priority (Critical audit findings require immediate design team attention) "
            "  * thread_002: NORMAL priority (Secondary audit review completed) "
            "  * escalate_to=sarah.designer@company.com,mike.ux@company.com "
            "- Date filters: "
            "  * created_after=2024-08-20T15:00:00Z: Filter audits created after this timestamp "
            "  * audit_date_filter=2024-08-18T00:00:00Z: Filter audit data for this specific date "
            "- References: "
            "  * thread_ids=thread_001,thread_002 "
            "  * artifact_ids=art_001,art_008"
        ),
        actions=[
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_001"}),
            Action(name="update_audit_report_status", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed with recommendations"}),
            Action(name="get_audits_by_status", kwargs={"status": "COMPLETED", "audit_type": "COMBINED_DS_A11Y"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical audit findings require immediate design team attention", "escalate_to": ["sarah.designer@company.com", "mike.ux@company.com"]}),
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_002"}),
            Action(name="update_audit_report_status", kwargs={"audit_id": "audit_002", "new_status": "COMPLETED", "report_asset_id": "asset_007"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Secondary audit review completed"}),
            Action(name="get_audits_by_status", kwargs={"status": "COMPLETED", "created_after": "2024-08-20T15:00:00Z"}),
            Action(name="get_audits_by_status", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"}),
            Action(name="add_terminal_log_entry", kwargs={"log_message": "Audit report management workflow completed for audit_001 and audit_002 with comprehensive status tracking and priority escalation", "log_level": "INFO", "component": "audit_management", "user_email": "sarah.designer@company.com"})
        ],
        outputs=[
            "Audit management workflow completed: audit_001 status updated to COMPLETED with report asset_001 association and completion notes, thread_001 priority escalated to HIGH with critical findings urgency and stakeholder escalation to design team, audit_002 status updated to COMPLETED with report asset_007, secondary thread_002 priority normalized, comprehensive audit status verification completed across all COMBINED_DS_A11Y and A11Y audit types for stakeholder reporting, and terminal log entry added for audit report management workflow tracking."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_29",
        instruction=(
            "You are an accessibility compliance specialist responsible for coordinating audit findings and managing fix items across admin panel accessibility initiatives. "
            "Your task is to ensure comprehensive audit findings analysis, proper fix item lifecycle management, and successful accessibility compliance tracking. "
            "Focus on verifying touch target compliance, font size standards, and contrast violations while maintaining accurate status updates and documentation. "
            "Coordinate with design and development teams through appropriate channels to ensure all accessibility issues are properly addressed and verified. "
            "Required constants: "
            "audit_ids=audit_002,audit_004,audit_005, fix_item_ids=item_001,item_002,item_004, "
            "statuses=VERIFIED,APPLIED,IN_PROGRESS, completion_date=2024-08-25T15:30:00Z, "
            "comment_id=comment_009, assignee_email=sarah.designer@company.com"
        ),
        actions=[
            Action(name="get_audit_findings_summary", kwargs={"audit_id": "audit_002"}),
            Action(name="get_audit_findings_summary", kwargs={"audit_id": "audit_004"}),
            Action(name="get_audit_findings_summary", kwargs={"audit_id": "audit_005"}),
            Action(name="update_fix_item_status", kwargs={"fix_item_id": "item_001", "new_status": "VERIFIED"}),
            Action(name="update_fix_item_status", kwargs={"fix_item_id": "item_004", "new_status": "APPLIED", "completion_date": "2024-08-25T15:30:00Z"}),
            Action(name="update_fix_item_status", kwargs={"fix_item_id": "item_002", "new_status": "IN_PROGRESS"}),
            Action(name="update_figma_comment_status", kwargs={"comment_id": "comment_009", "new_status": "RESOLVED", "assignee_email": "sarah.designer@company.com"}),
            Action(name="get_audit_summary", kwargs={"audit_id": "audit_002"})
        ],
        outputs=[
            "audit_findings_retrieved:audit_002,audit_004,audit_005",
            "fix_item_updated:item_001:VERIFIED",
            "fix_item_updated:item_004:APPLIED:2024-08-25T15:30:00Z",
            "fix_item_updated:item_002:IN_PROGRESS",
            "figma_comment_updated:comment_009:RESOLVED:sarah.designer@company.com",
            "audit_summary_retrieved:audit_002"
        ]
    ),

    Task(
        annotator="0",
        user_id="user_30",
        instruction=(
            "You are a Figma comment resolution specialist responsible for accessibility feedback coordination and workflow management across admin panel header components. "
            "Your primary responsibility involves accessibility feedback coordination for art_008 admin panel header where unresolved comments with resolved_status False require identification and resolution coordination. The workflow also involves asset_007 admin header export integration requiring status verification and coordination alignment. "
            "The accessibility improvement workflow centers on comment_006 accessibility enhancement coordination involving mike.ux@company.com team member oversight, HIGH priority accessibility improvements, and comprehensive ARIA labels and keyboard navigation support implementation tracking. The feedback resolution requires progress status coordination and detailed implementation documentation. "
            "Your coordination efforts should ensure seamless accessibility audit communication through thread_004, effective comment lifecycle coordination, and comprehensive accessibility compliance tracking for stakeholder reporting and successful workflow completion."
            "You can use resolution_notes Accessibility improvements in progress - adding ARIA labels and keyboard navigation support"
            "Required constants: plan_id=plan_005,resolution_notes=Accessibility improvements in progress - adding ARIA labels and keyboard navigation support,new_status=IN_PROGRESS"
        ),
        actions=[
            Action(name="get_figma_comments_by_artifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_007"}),
            Action(name="update_figma_comment_status", kwargs={"comment_id": "comment_006", "new_status": "IN_PROGRESS", "resolution_notes": "Accessibility improvements in progress - adding ARIA labels and keyboard navigation support", "assignee_email": "mike.ux@company.com", "priority_level": "HIGH"}),
            Action(name="get_gmail_threads_by_labels", kwargs={"thread_id": "thread_004"}),
            Action(name="get_figma_comments_by_artifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="update_fix_plan_status", kwargs={"plan_id": "plan_005", "new_status": "IN_PROGRESS"}),
            Action(name="add_terminal_log_entry", kwargs={"log_message": "Figma comment resolution workflow completed for accessibility improvements with fix plan coordination", "log_level": "INFO", "component": "figma_comment_resolution", "user_email": "mike.ux@company.com"})
        ],
        outputs=[
            "Comment resolution workflow completed. comment status updated, assignee assigned to Mike UX with HIGH priority level, resolution notes added about accessibility improvements, asset export status verified for admin header asset_007, Gmail thread communication status verified for thread_004 accessibility audit coordination, fix plan plan_005 updated to IN_PROGRESS status, and comprehensive terminal logging completed for accessibility workflow tracking."
        ]
    ),
    Task(
        annotator="0",
        user_id="user_31",
        instruction=(
            "You are an audit report management specialist responsible for coordinating the end-to-end audit lifecycle for design system components and accessibility compliance. "
            "Your primary responsibility involves managing audit_001 for artifact art_001 (Homepage Hero Section) which requires comprehensive status tracking from COMPLETED to final report generation. The workflow integrates with audit_002 for accessibility review of art_008 admin panel components requiring status coordination. "
            "The audit management workflow centers on thread_001 priority escalation to HIGH priority for design review coordination involving sarah.designer@company.com oversight, URGENT priority level escalation for comprehensive design review tracking, and escalation_reason 'Critical audit findings require immediate design team attention and stakeholder review'. The priority management requires comprehensive Gmail thread coordination and detailed audit status documentation. "
            "Your coordination efforts should ensure seamless audit report generation through proper status management, effective priority escalation for design review threads, and comprehensive audit findings tracking for stakeholder reporting. "
            "Additionally, you'll retrieve asset export summaries to ensure proper documentation and asset coordination throughout the audit management process. "
            "Key parameters: audit_id=audit_001, new_status=COMPLETED, report_asset_id=asset_001, completion_notes=Design system audit completed with recommendations, "
            "thread_001_priority=HIGH, thread_002_priority=NORMAL, thread_001_urgency=Critical audit findings require immediate design team attention, thread_002_urgency=Secondary audit review completed, "
            "escalate_to=sarah.designer@company.com,mike.ux@company.com, audit_type=COMBINED_DS_A11Y, created_after=2024-08-20T15:00:00Z, audit_date_filter=2024-08-18T00:00:00Z, "
            "thread_ids=thread_001,thread_002, artifact_ids=art_001,art_008"
        ),
        actions=[
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_001"}),
            Action(name="update_audit_report_status", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed with recommendations"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical audit findings require immediate design team attention", "escalate_to": ["sarah.designer@company.com", "mike.ux@company.com"]}),
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_002"}),
            Action(name="update_audit_report_status", kwargs={"audit_id": "audit_002", "new_status": "COMPLETED", "report_asset_id": "asset_007"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Secondary audit review completed"}),
            Action(name="get_audits_by_status", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"}),
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_001"})
        ],
        outputs=[
            "Audit management workflow completed: audit_001 status updated to COMPLETED with report asset_001 association and completion notes, thread_001 priority escalated to HIGH with critical findings urgency and stakeholder escalation to design team, audit_002 status updated to COMPLETED with report asset_007, comprehensive audit verification completed for A11Y audit type, and asset_001 export summary retrieved for audit documentation coordination."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_32",
        instruction=(
            "As a data collection specialist, you are responsible for gathering comprehensive system data from multiple sources to support audit and design system coordination. "
            "Your objective is to collect and correlate data from Figma artifacts, audit records, asset exports, email communications, and system configurations. "
            "The data collection must include current ACTIVE Figma artifacts, the complete audit summary for audit_003, export summary for asset_003, "
            "all email communications from thread_003, releases by emily.ux@company.com since August 22nd, 2024, and the current design system aliases configuration. "
            "After collecting all data, log the completion of this workflow with an INFO level message to the data_collection component log."
            "Required data points: audit_id=audit_003,thread_id=thread_003,owner_email=emily.ux@company.com,log_message=Data collection workflow completed with comprehensive coordination,"
            "created_after=2024-08-22T17:00:00Z,category=design_system_aliases"
        ),
        actions=[
            Action(name="get_figma_artifacts_by_status", kwargs={"status": "ACTIVE"}),
            Action(name="get_audit_summary", kwargs={"audit_id": "audit_003"}),
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_003"}),
            Action(name="get_gmail_threads_by_labels", kwargs={"thread_id": "thread_003"}),
            Action(name="get_releases_by_owner", kwargs={"owner_email": "emily.ux@company.com", "created_after": "2024-08-22T17:00:00Z"}),
            Action(name="get_system_config_by_category", kwargs={"category": "design_system_aliases"}),
            Action(name="add_terminal_log_entry", kwargs={"log_message": "Data collection workflow completed with comprehensive coordination", "log_level": "INFO", "component": "data_collection", "user_email": "emily.ux@company.com"})
        ],
        outputs=[
            "Data collection with terminal logging completed: ACTIVE figma artifacts retrieved for comprehensive data coordination, audit_003 summary verified for audit data tracking, asset_003 export summary retrieved for asset coordination, Gmail thread_003 verified for communication tracking, Emily UX releases retrieved for release coordination since August 22nd, design_system_aliases config retrieved for system coordination, and comprehensive data collection workflow logging updated with INFO level coordination."
        ]
    ),
    Task(
        annotator="0",
        user_id="user_33",
        instruction=(
            "You are an audit report management specialist responsible for coordinating the end-to-end audit lifecycle for design system components and accessibility compliance. "
            "Your primary responsibility involves managing audit_001 for artifact art_001 (Homepage Hero Section) which requires comprehensive status tracking from COMPLETED to final report generation. The workflow integrates with audit_002 for accessibility review of art_008 admin panel components requiring status coordination. "
            "The audit management workflow centers on thread_001 priority escalation to HIGH priority for design review coordination involving sarah.designer@company.com oversight, URGENT priority level escalation for comprehensive design review tracking, and escalation_reason 'Critical audit findings require immediate design team attention and stakeholder review'. The priority management requires comprehensive Gmail thread coordination and detailed audit status documentation. "
            "Your coordination efforts should ensure seamless audit report generation through proper status management, effective priority escalation for design review threads, comprehensive audit findings tracking for stakeholder reporting, and successful audit lifecycle completion with proper report asset associations. "
            "Key parameters: audit_id=audit_001, new_status=COMPLETED, report_asset_id=asset_001, completion_notes=Design system audit completed with recommendations, "
            "thread_001_priority=HIGH, thread_002_priority=NORMAL, thread_001_urgency=Critical audit findings require immediate design team attention, thread_002_urgency=Secondary audit review completed, "
            "escalate_to=sarah.designer@company.com,mike.ux@company.com, audit_type=COMBINED_DS_A11Y, created_after=2024-08-20T15:00:00Z, audit_date_filter=2024-08-18T00:00:00Z, "
            "thread_ids=thread_001,thread_002, artifact_ids=art_001,art_008, "
            "asset_id=asset_001, "
            "log_message=Audit management workflow completed - audit_001 report generated with comprehensive status tracking, "
            "log_level=INFO, component=audit_management, user_email=sarah.designer@company.com"
        ),
        actions=[
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_001"}),
            Action(name="update_audit_report_status", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed with recommendations"}),
            Action(name="get_audits_by_status", kwargs={"status": "COMPLETED", "audit_type": "COMBINED_DS_A11Y"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical audit findings require immediate design team attention", "escalate_to": ["sarah.designer@company.com", "mike.ux@company.com"]}),
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_002"}),
            Action(name="get_audits_by_status", kwargs={"artifact_id": "art_001", "created_after": "2024-08-20T15:00:00Z"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Secondary audit review completed"}),
            Action(name="get_audits_by_status", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"}),
            Action(name="add_terminal_log_entry", kwargs={"log_message": "Audit management workflow completed - audit_001 report generated with comprehensive status tracking", "log_level": "INFO", "component": "audit_management", "user_email": "sarah.designer@company.com"})
        ],
        outputs=[
            "Audit management workflow completed: audit_001 status updated to COMPLETED with report asset_001 association and completion notes, thread_001 priority escalated to HIGH with critical findings urgency and stakeholder escalation to design team, secondary thread_002 priority normalized, comprehensive audit status verification completed across all COMBINED_DS_A11Y and A11Y audit types for stakeholder reporting, and terminal log entry added documenting audit management workflow completion with comprehensive status tracking."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_34",
        instruction=(
            "You are an asset management specialist responsible for coordinating comprehensive asset management and fix item status workflows. "
            "Your task is to manage asset exports, system configuration, and fix item status coordination for design system compliance. "
            "Focus on managing asset exports, system configuration analysis, audit information, and fix item status updates with proper coordination. "
            "Coordinate with development teams through appropriate channels to ensure all asset management and fix item workflows are properly coordinated. "
            "Required constants: "
            "asset_id=asset_005, category=design_system_aliases, audit_id=audit_006, "
            "thread_id=thread_006, owner_email=sarah.designer@company.com, created_after=2024-08-21T14:00:00Z, "
            "log_level=INFO, component=asset_management, fix_item_id=item_003, "
            "new_status=APPLIED, updated_by=sarah.designer@company.com, notes=Asset management coordination completed with design system compliance, "
            "log_message=Asset management workflow completed with fix item status coordination, "
            "terminal_component=asset_management, user_email=sarah.designer@company.com"
        ),
        actions=[
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_005"}),
            Action(name="get_system_config_by_category", kwargs={"category": "design_system_aliases"}),
            Action(name="get_audit_summary", kwargs={"audit_id": "audit_006"}),
            Action(name="get_gmail_threads_by_labels", kwargs={"thread_id": "thread_006"}),
            Action(name="get_releases_by_owner", kwargs={"owner_email": "sarah.designer@company.com", "created_after": "2024-08-21T14:00:00Z"}),
            Action(name="get_terminal_logs_summary", kwargs={"log_level": "INFO", "component": "asset_management"}),
            Action(name="update_fix_item_status", kwargs={"fix_item_id": "item_003", "new_status": "APPLIED", "updated_by": "sarah.designer@company.com", "notes": "Asset management coordination completed with design system compliance"}),
            Action(name="add_terminal_log_entry", kwargs={"log_message": "Asset management workflow completed with fix item status coordination", "log_level": "INFO", "component": "asset_management", "user_email": "sarah.designer@company.com"})
        ],
        outputs=[
            "Asset management with fix item status update completed: asset_005 export summary retrieved for asset management coordination, design_system_aliases config retrieved for system coordination, audit_006 summary verified for audit tracking, Gmail thread_006 verified for communication coordination, Sarah Designer releases retrieved for release coordination since August 21st, terminal logs summary retrieved for INFO level asset_management component, fix item_003 status updated to APPLIED with asset management coordination notes by Sarah Designer, and terminal log entry added documenting asset management workflow completion."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_35",
        instruction=(
            "You are a Figma comment resolution specialist responsible for accessibility feedback coordination and workflow management across admin panel header components. "
            "Required constants: "
            "artifact_id=art_008, asset_id=asset_007, comment_id=comment_006, "
            "assignee_email=mike.ux@company.com, priority_level=HIGH, "
            "resolution_notes=ARIA_AND_NAV_IMPROVEMENTS_IN_PROGRESS, "
            "export_notes=ADMIN_HEADER_EXPORT_COMPLETED, "
            "dlp_scan_status=CLEAN, "
            "log_message=FIGMA_COMMENT_RESOLUTION_COMPLETED, "
            "log_level=INFO, component=figma_comment_resolution, "
            "thread_id=thread_004"
        ),
        actions=[
            Action(name="get_figma_comments_by_artifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_007"}),
            Action(name="update_figma_comment_status", kwargs={"comment_id": "comment_006", "new_status": "IN_PROGRESS", "resolution_notes": "ARIA_AND_NAV_IMPROVEMENTS_IN_PROGRESS", "assignee_email": "mike.ux@company.com", "priority_level": "HIGH"}),
            Action(name="get_gmail_threads_by_labels", kwargs={"thread_id": "thread_004"}),
            Action(name="update_asset_export_status", kwargs={"asset_id": "asset_007", "new_status": "COMPLETED", "notes": "ADMIN_HEADER_EXPORT_COMPLETED", "dlp_scan_status": "CLEAN"}),
            Action(name="add_terminal_log_entry", kwargs={"log_message": "FIGMA_COMMENT_RESOLUTION_COMPLETED", "log_level": "INFO", "component": "figma_comment_resolution", "user_email": "mike.ux@company.com"})
        ],
        outputs=[
            "Comment resolution workflow completed for comment_006: comment status updated to IN_PROGRESS, assignee assigned to Mike UX with HIGH priority level, resolution notes added about accessibility improvements, asset export status verified for admin header asset_007, Gmail thread communication status verified for thread_004 accessibility audit coordination, asset export updated to COMPLETED with accessibility enhancements, and terminal log entry added for comment resolution workflow completion tracking."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_36",
        instruction=(
            "You are an audit findings severity management specialist responsible for coordinating audit finding severity updates and integrated fix plan workflows. "
            "Your task is to manage audit finding severity escalation with fix plan status coordination and ensure proper priority management. "
            "Focus on managing audit finding severity updates for CRITICAL violations, including fix plan delivery coordination and comprehensive fix item tracking. "
            "Coordinate with development teams through appropriate channels to ensure all audit findings and fix workflows are properly synchronized. "
            "Required constants: "
            "finding_id=finding_a11y_001, new_severity=CRITICAL, updated_by=alex.dev@company.com, "
            "plan_id=plan_001, delivery_method=TICKETS, owner_email=alex.dev@company.com, "
            "item_id=item_001, fix_item_id=item_001, new_priority=HIGH, "
            "priority_reason=Critical audit finding requires immediate fix attention, "
            "audit_id=audit_002, violation_type=TOUCH_TARGET, severity=CRITICAL, "
            "log_message=Audit findings severity management and fix plan coordination completed"
        ),
        actions=[
            Action(name="update_audit_finding_severity", kwargs={"finding_id": "finding_a11y_001", "new_severity": "CRITICAL", "updated_by": "alex.dev@company.com"}),
            Action(name="get_audit_findings_by_type", kwargs={"violation_type": "TOUCH_TARGET", "severity": "CRITICAL"}),
            Action(name="get_fix_plan_items", kwargs={"plan_id": "plan_001"}),
            Action(name="update_fix_plan_status", kwargs={"plan_id": "plan_001", "new_status": "IN_PROGRESS", "delivery_method": "TICKETS", "owner_email": "alex.dev@company.com"}),
            Action(name="update_fix_item_priority", kwargs={"item_id": "item_001", "new_priority": "HIGH", "priority_reason": "Critical audit finding requires immediate fix attention", "updated_by": "alex.dev@company.com"}),
            Action(name="update_fix_item_status", kwargs={"fix_item_id": "item_001", "new_status": "IN_PROGRESS", "updated_by": "alex.dev@company.com"}),
            Action(name="add_terminal_log_entry", kwargs={"log_message": "Audit findings severity management and fix plan coordination completed", "log_level": "INFO", "component": "audit_severity", "user_email": "alex.dev@company.com"}),
            Action(name="get_audit_summary", kwargs={"audit_id": "audit_002"})
        ],
        outputs=[
            "Audit findings severity management completed: finding_a11y_001 severity escalated to CRITICAL with Alex Dev oversight, CRITICAL severity TOUCH_TARGET violations analyzed for comprehensive coordination, fix plan items retrieved for plan_001 coordination workflow, fix plan status updated to IN_PROGRESS with TICKETS delivery method and Alex Dev ownership, fix item_001 priority escalated to HIGH with critical finding attention and Alex Dev assignment, fix item status updated to IN_PROGRESS for active coordination, comprehensive audit severity management workflow logging completed, and comprehensive audit summary retrieved for audit_002 compliance verification and severity management documentation."
        ]
    ),
    Task(
        annotator="0",
        user_id="user_37",
        instruction=(
            "You are a release diff analysis specialist responsible for coordinating the analysis of differences between design system releases. "
            "The task requires analyzing release_012 to identify changes in design system components, tracking associated Figma artifacts, and updating the fix plan with the analysis results. "
            "The analysis should focus on identifying breaking changes, design system updates, and accessibility improvements in the release. "
            "The output should include a comprehensive diff summary, status of affected Figma artifacts, and an updated fix plan with clear action items. "
            "Required constants: "
            "release_id=release_012, status=ACTIVE, asset_id=asset_014, "
            "thread_id=thread_014, owner_email=alex.dev@company.com, created_after=2024-08-23T16:15:00Z, "
            "log_level=WARNING, component=release_diff_analysis, plan_id=plan_008, "
            "new_plan_status=DELIVERED, delivery_method=COMMENTS, plan_notes=Release diff analysis completed with comprehensive management, "
            "analysis_scope=design_system_components, impact_level=high, priority=P1"
        ),
        actions=[
            Action(name="get_release_diff_summary", kwargs={"release_id": "release_012"}),
            Action(name="get_figma_artifacts_by_status", kwargs={"status": "ACTIVE"}),
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_014"}),
            Action(name="get_gmail_threads_by_labels", kwargs={"thread_id": "thread_014"}),
            Action(name="get_releases_by_owner", kwargs={"owner_email": "alex.dev@company.com", "created_after": "2024-08-23T16:15:00Z"}),
            Action(name="get_terminal_logs_summary", kwargs={"log_level": "WARNING", "component": "release_diff_analysis"}),
            Action(name="get_release_summary", kwargs={"release_id": "release_012"}),
            Action(name="update_fix_plan_status", kwargs={"plan_id": "plan_008", "new_status": "DELIVERED", "delivery_method": "COMMENTS", "owner_email": "alex.dev@company.com", "notes": "Release diff analysis completed with comprehensive management"})
        ],
        outputs=[
            "Release diff analysis with plan update completed: release_012 diff summary retrieved for diff coordination, ACTIVE figma artifacts retrieved for comprehensive coordination, asset_014 export summary verified for asset coordination, Gmail thread_014 verified for communication coordination, Alex Dev releases retrieved for release coordination since August 23rd, terminal logs summary retrieved for WARNING level release_diff_analysis component, release_012 summary verified for release coordination, and fix plan_008 status updated to DELIVERED with COMMENTS delivery method and comprehensive management notes."
        ]
    ),
    
    Task(
        annotator="0",
        user_id="user_38",
        instruction=(
            "You are a Figma comment resolution specialist responsible for accessibility feedback coordination and workflow management across admin panel header components. "
            "Your primary responsibility involves accessibility feedback coordination for art_008 admin panel header where unresolved comments with resolved_status False require identification and resolution coordination. The workflow also involves asset_007 admin header export integration requiring status verification and coordination alignment. "
            "The accessibility improvement workflow centers on comment_006 accessibility enhancement coordination involving mike.ux@company.com team member oversight, HIGH priority accessibility improvements, and comprehensive ARIA labels and keyboard navigation support implementation tracking. The feedback resolution requires progress status coordination and detailed implementation documentation. "
            "Your coordination efforts should ensure seamless accessibility audit communication through thread_004, effective comment lifecycle coordination, and comprehensive accessibility compliance tracking for stakeholder reporting and successful workflow completion."
            "You can use resolution_notes Accessibility improvements in progress - adding ARIA labels and keyboard navigation support"
        ),
        actions=[
            Action(name="get_figma_comments_by_artifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_007"}),
            Action(name="update_figma_comment_status", kwargs={"comment_id": "comment_006", "new_status": "IN_PROGRESS", "resolution_notes": "Accessibility improvements in progress - adding ARIA labels and keyboard navigation support", "assignee_email": "mike.ux@company.com", "priority_level": "HIGH"}),
            Action(name="get_gmail_threads_by_labels", kwargs={"thread_id": "thread_004"}),
            Action(name="get_figma_comments_by_artifact", kwargs={"artifact_id": "art_008", "resolved_status": False})
        ],
        outputs=[
            "Comment resolution workflow completed. comment status updated, assignee assigned to Mike UX with HIGH priority level, resolution notes added about accessibility improvements, asset export status verified for admin header asset_007, and Gmail thread communication status verified for thread_004 accessibility audit coordination."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_39",
        instruction=(
            "You are a Figma comment resolution specialist responsible for accessibility feedback coordination and workflow management across admin panel header components. "
            "Your primary responsibility involves accessibility feedback coordination for art_008 admin panel header where unresolved comments with resolved_status False require identification and resolution coordination. The workflow also involves asset_007 admin header export integration requiring status verification and coordination alignment. "
            "The accessibility improvement workflow centers on comment_006 accessibility enhancement coordination involving mike.ux@company.com team member oversight, HIGH priority accessibility improvements, and comprehensive ARIA labels and keyboard navigation support implementation tracking. The feedback resolution requires progress status coordination and detailed implementation documentation. "
            "Your coordination efforts should ensure seamless accessibility audit communication through thread_004, effective comment lifecycle coordination, and comprehensive accessibility compliance tracking for stakeholder reporting and successful workflow completion."
            "You can use resolution_notes Accessibility improvements in progress - adding ARIA labels and keyboard navigation support, "
            "asset_export_status=COMPLETED, dlp_scan_status=CLEAN, export_notes=Admin header accessibility export completed with ARIA labels"
        ),
        actions=[
            Action(name="get_figma_comments_by_artifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_007"}),
            Action(name="update_figma_comment_status", kwargs={"comment_id": "comment_006", "new_status": "IN_PROGRESS", "resolution_notes": "Accessibility improvements in progress - adding ARIA labels and keyboard navigation support", "assignee_email": "mike.ux@company.com", "priority_level": "HIGH"}),
            Action(name="get_gmail_threads_by_labels", kwargs={"thread_id": "thread_004"}),
            Action(name="get_figma_comments_by_artifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="add_terminal_log_entry", kwargs={"log_message": "Accessibility comment resolution workflow completed for art_008 admin panel header", "log_level": "INFO", "component": "accessibility_resolution", "user_email": "mike.ux@company.com"}),
            Action(name="update_asset_export_status", kwargs={"asset_id": "asset_007", "new_status": "COMPLETED", "notes": "Admin header accessibility export completed with ARIA labels", "dlp_scan_status": "CLEAN"})
        ],
        outputs=[
            "Comment resolution workflow completed. comment status updated, assignee assigned to Mike UX with HIGH priority level, resolution notes added about accessibility improvements, asset export status verified for admin header asset_007, Gmail thread communication status verified for thread_004 accessibility audit coordination, terminal log entry added for accessibility comment resolution workflow tracking, and asset export status updated to COMPLETED with accessibility enhancements and DLP scan verification."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_40",
        instruction=(
            "You are an accessibility compliance specialist responsible for audit findings coordination and fix item management across admin panel accessibility initiatives. "
            "Your primary responsibility involves accessibility audit coordination for audit_002, audit_004, and audit_005 where comprehensive findings analysis and fix item status updates require systematic processing. The workflow involves fix item lifecycle management following proper status progression. "
            "The accessibility compliance workflow centers on item_001 touch target verification with VERIFIED status achievement, item_004 font size compliance with APPLIED status and completion timestamp coordination, and item_002 contrast violation remediation with IN_PROGRESS status management. The fix implementation requires systematic status coordination and compliance verification. "
            "Your coordination efforts should ensure comprehensive audit findings analysis, proper fix item lifecycle management, and successful accessibility compliance tracking for stakeholder reporting and workflow completion."
        ),
        actions=[
            Action(name="get_audit_findings_summary", kwargs={"audit_id": "audit_002"}),
            Action(name="get_audit_findings_summary", kwargs={"audit_id": "audit_004"}),
            Action(name="get_audit_findings_summary", kwargs={"audit_id": "audit_005"}),
            Action(name="update_fix_item_status", kwargs={"fix_item_id": "item_001", "new_status": "VERIFIED"}),
            Action(name="update_fix_item_status", kwargs={"fix_item_id": "item_004", "new_status": "APPLIED", "completion_date": "2024-08-25T15:30:00Z"}),
            Action(name="update_fix_item_status", kwargs={"fix_item_id": "item_002", "new_status": "IN_PROGRESS"})
        ],
        outputs=[
            "Accessibility compliance workflow completed: audit findings analyzed for audit_002, audit_004, and audit_005, item_001 updated to VERIFIED status, item_004 updated to APPLIED status with completion date 2024-08-25T15:30:00Z, and item_002 updated to IN_PROGRESS status for continued accessibility improvements."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_41",
        instruction=(
            "You are an audit report management specialist responsible for coordinating the end-to-end audit lifecycle for design system components and accessibility compliance. "
            "Your primary responsibility involves managing audit_001 for artifact art_001 (Homepage Hero Section) which requires comprehensive status tracking from COMPLETED to final report generation. The workflow integrates with audit_002 for accessibility review of art_008 admin panel components requiring status coordination. "
            "The audit management workflow centers on thread_001 priority escalation to HIGH priority for design review coordination involving sarah.designer@company.com oversight, URGENT priority level escalation for comprehensive design review tracking, and escalation_reason 'Critical audit findings require immediate design team attention and stakeholder review'. The priority management requires comprehensive Gmail thread coordination and detailed audit status documentation. "
            "Your coordination efforts should ensure seamless audit report generation through proper status management, effective priority escalation for design review threads, and comprehensive audit findings tracking for stakeholder reporting. "
            "Key parameters: audit_id=audit_001, new_status=COMPLETED, report_asset_id=asset_001, completion_notes=Design system audit completed with recommendations, "
            "thread_001_priority=HIGH, thread_002_priority=NORMAL, thread_001_urgency=Critical audit findings require immediate design team attention, thread_002_urgency=Secondary audit review completed, "
            "escalate_to=sarah.designer@company.com,mike.ux@company.com, audit_type=COMBINED_DS_A11Y, created_after=2024-08-20T15:00:00Z, audit_date_filter=2024-08-18T00:00:00Z, "
            "thread_ids=thread_001,thread_002, artifact_ids=art_001,art_008"
        ),
        actions=[
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_001"}),
            Action(name="update_audit_report_status", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed with recommendations"}),
            Action(name="get_audits_by_status", kwargs={"status": "COMPLETED", "audit_type": "COMBINED_DS_A11Y"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical audit findings require immediate design team attention", "escalate_to": ["sarah.designer@company.com", "mike.ux@company.com"]}),
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_002"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Secondary audit review completed"}),
            Action(name="get_audits_by_status", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"}),
            Action(name="add_terminal_log_entry", kwargs={"log_message": "Audit management workflow completed for audit_001 and audit_002 with critical findings escalation", "log_level": "INFO", "component": "audit_management", "user_email": "sarah.designer@company.com"})
        ],
        outputs=[
            "Audit management workflow completed: audit_001 status updated to COMPLETED with report asset_001 association and completion notes, thread_001 priority escalated to HIGH with critical findings urgency and stakeholder escalation to design team, comprehensive audit verification completed for A11Y audit type, and terminal log entry added for audit management workflow tracking."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_42",
        instruction=(
            "You are an audit report management specialist responsible for coordinating the end-to-end audit lifecycle for design system components and accessibility compliance. "
            "Your primary responsibility involves managing audit_001 for artifact art_001 (Homepage Hero Section) which requires comprehensive status tracking from COMPLETED to final report generation. The workflow integrates with audit_002 for accessibility review of art_008 admin panel components requiring status coordination. "
            "The audit management workflow centers on thread_001 priority escalation to HIGH priority for design review coordination involving sarah.designer@company.com oversight, URGENT priority level escalation for comprehensive design review tracking, and escalation_reason 'Critical audit findings require immediate design team attention and stakeholder review'. The priority management requires comprehensive Gmail thread coordination and detailed audit status documentation. "
            "Your coordination efforts should ensure seamless audit report generation through proper status management, effective priority escalation for design review threads, comprehensive audit findings tracking for stakeholder reporting, and successful audit lifecycle completion with proper report asset associations. "
            "Key parameters: audit_id=audit_001, new_status=COMPLETED, report_asset_id=asset_001, completion_notes=Design system audit completed with recommendations, "
            "thread_001_priority=HIGH, thread_002_priority=NORMAL, thread_001_urgency=Critical audit findings require immediate design team attention, thread_002_urgency=Secondary audit review completed, "
            "escalate_to=sarah.designer@company.com,mike.ux@company.com, audit_type=COMBINED_DS_A11Y, created_after=2024-08-20T15:00:00Z, audit_date_filter=2024-08-18T00:00:00Z, "
            "thread_ids=thread_001,thread_002, artifact_ids=art_001,art_008, "
            "category=audit_lifecycle_config"
        ),
        actions=[
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_001"}),
            Action(name="update_audit_report_status", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed with recommendations"}),
            Action(name="get_audits_by_status", kwargs={"status": "COMPLETED", "audit_type": "COMBINED_DS_A11Y"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical audit findings require immediate design team attention", "escalate_to": ["sarah.designer@company.com", "mike.ux@company.com"]}),
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_002"}),
            Action(name="update_audit_report_status", kwargs={"audit_id": "audit_002", "new_status": "COMPLETED", "report_asset_id": "asset_007"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Secondary audit review completed"}),
            Action(name="get_audits_by_status", kwargs={"status": "COMPLETED", "created_after": "2024-08-20T15:00:00Z"}),
            Action(name="get_audits_by_status", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"}),
            Action(name="get_system_config_by_category", kwargs={"category": "audit_lifecycle_config"})
        ],
        outputs=[
            "Audit management workflow completed: audit_001 status updated to COMPLETED with report asset_001 association and completion notes, thread_001 priority escalated to HIGH with critical findings urgency and stakeholder escalation to design team, audit_002 status updated to COMPLETED with report asset_007, secondary thread_002 priority normalized, comprehensive audit status verification completed across all COMBINED_DS_A11Y and A11Y audit types for stakeholder reporting, and audit lifecycle configuration retrieved for system coordination settings."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_43",
        instruction=(
            "You are an audit report management specialist responsible for coordinating the end-to-end audit lifecycle for design system components and accessibility compliance. "
            "Your primary responsibility involves managing audit_001 for artifact art_001 (Homepage Hero Section) which requires comprehensive status tracking from COMPLETED to final report generation. The workflow integrates with audit_002 for accessibility review of art_008 admin panel components requiring status coordination. "
            "The audit management workflow centers on thread_001 priority escalation to HIGH priority for design review coordination involving sarah.designer@company.com oversight, URGENT priority level escalation for comprehensive design review tracking, and escalation_reason 'Critical audit findings require immediate design team attention and stakeholder review'. The priority management requires comprehensive Gmail thread coordination and detailed audit status documentation. "
            "Your coordination efforts should ensure seamless audit report generation through proper status management, effective priority escalation for design review threads, comprehensive audit findings tracking for stakeholder reporting, and successful audit lifecycle completion with proper report asset associations. "
            "Key parameters: audit_id=audit_001, new_status=COMPLETED, report_asset_id=asset_001, completion_notes=Design system audit completed with recommendations, "
            "thread_001_priority=HIGH, thread_002_priority=NORMAL, thread_001_urgency=Critical audit findings require immediate design team attention, thread_002_urgency=Secondary audit review completed, "
            "escalate_to=sarah.designer@company.com,mike.ux@company.com, audit_type=COMBINED_DS_A11Y, created_after=2024-08-20T15:00:00Z, audit_date_filter=2024-08-18T00:00:00Z, "
            "thread_ids=thread_001,thread_002, artifact_ids=art_001,art_008, "
            "asset_id=asset_001"
        ),
        actions=[
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_001"}),
            Action(name="update_audit_report_status", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed with recommendations"}),
            Action(name="get_audits_by_status", kwargs={"status": "COMPLETED", "audit_type": "COMBINED_DS_A11Y"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical audit findings require immediate design team attention", "escalate_to": ["sarah.designer@company.com", "mike.ux@company.com"]}),
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_002"}),
            Action(name="get_audits_by_status", kwargs={"artifact_id": "art_001", "created_after": "2024-08-20T15:00:00Z"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Secondary audit review completed"}),
            Action(name="get_audits_by_status", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"}),
            Action(name="get_system_config_by_category", kwargs={"category": "audit_config"}),
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_001"})
        ],
        outputs=[
            "Audit management workflow completed: audit_001 status updated to COMPLETED with report asset_001 association and completion notes, thread_001 priority escalated to HIGH with critical findings urgency and stakeholder escalation to design team, secondary thread_002 priority normalized, comprehensive audit status verification completed across all COMBINED_DS_A11Y and A11Y audit types for stakeholder reporting, audit configuration retrieved for system coordination settings, and asset export summary retrieved for asset_001 coordination and compliance tracking."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_44",
        instruction=(
            "You are an audit report management specialist responsible for coordinating the end-to-end audit lifecycle for design system components and accessibility compliance. "
            "Your primary responsibility involves managing audit_001 for artifact art_001 (Homepage Hero Section) which requires comprehensive status tracking from COMPLETED to final report generation. The workflow integrates with audit_002 for accessibility review of art_008 admin panel components requiring status coordination. "
            "The audit management workflow centers on thread_001 priority escalation to HIGH priority for design review coordination involving sarah.designer@company.com oversight, URGENT priority level escalation for comprehensive design review tracking, and escalation_reason 'Critical audit findings require immediate design team attention and stakeholder review'. The priority management requires comprehensive Gmail thread coordination and detailed audit status documentation. "
            "Your coordination efforts should ensure seamless audit report generation through proper status management, effective priority escalation for design review threads, comprehensive audit findings tracking for stakeholder reporting, and successful audit lifecycle completion with proper report asset associations. "
            "Key parameters: audit_id=audit_001, new_status=COMPLETED, report_asset_id=asset_001, completion_notes=Design system audit completed with recommendations, "
            "thread_001_priority=HIGH, thread_002_priority=NORMAL, thread_001_urgency=Critical audit findings require immediate design team attention, thread_002_urgency=Secondary audit review completed, "
            "escalate_to=sarah.designer@company.com,mike.ux@company.com, audit_type=COMBINED_DS_A11Y, created_after=2024-08-20T15:00:00Z, audit_date_filter=2024-08-18T00:00:00Z, "
            "thread_ids=thread_001,thread_002, artifact_ids=art_001,art_008, "
            "audit_002_status=COMPLETED, updated_by=sarah.designer@company.com"
        ),
        actions=[
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_001"}),
            Action(name="update_audit_report_status", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed with recommendations"}),
            Action(name="get_audits_by_status", kwargs={"status": "COMPLETED", "audit_type": "COMBINED_DS_A11Y"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical audit findings require immediate design team attention", "escalate_to": ["sarah.designer@company.com", "mike.ux@company.com"]}),
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_002"}),
            Action(name="get_audits_by_status", kwargs={"artifact_id": "art_001", "created_after": "2024-08-20T15:00:00Z"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Secondary audit review completed"}),
            Action(name="get_audits_by_status", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"}),
            Action(name="get_system_config_by_category", kwargs={"category": "audit_config"}),
            Action(name="update_audit_status", kwargs={"audit_id": "audit_002", "new_status": "COMPLETED", "updated_by": "sarah.designer@company.com"})
        ],
        outputs=[
            "Audit management workflow completed: audit_001 status updated to COMPLETED with report asset_001 association and completion notes, thread_001 priority escalated to HIGH with critical findings urgency and stakeholder escalation to design team, secondary thread_002 priority normalized, comprehensive audit status verification completed across all COMBINED_DS_A11Y and A11Y audit types for stakeholder reporting, audit configuration retrieved for system coordination settings, and audit_002 status updated to COMPLETED with sarah.designer@company.com coordination for comprehensive audit lifecycle management."
        ]
    ),
    Task(
        annotator="0",
        user_id="user_45",
        instruction=(
            "You are a review management coordination specialist responsible for orchestrating comprehensive review workflows and audit status updates. "
            "Your task is to manage review cycle coordination, artifact tracking, and audit status management for design system components. "
            "Focus on managing review approvals, active artifact verification, system configuration checks, and audit status coordination with proper workflow management. "
            "Coordinate with UX teams through appropriate channels to ensure all review management processes are properly tracked and updated. "
            "Required constants: "
            "cycle_id=cycle_001, status=ACTIVE, category=gmail_labels, asset_id=asset_006, "
            "thread_id=thread_007, owner_email=mike.ux@company.com, created_after=2024-08-20T16:30:00Z, "
            "audit_id=audit_007, new_status=IN_PROGRESS, updated_by=mike.ux@company.com, "
            "notes=Review management coordination completed with audit workflow, log_level=INFO, component=review_management"
        ),
        actions=[
            Action(name="get_review_approvals_summary", kwargs={"cycle_id": "cycle_001"}),
            Action(name="get_figma_artifacts_by_status", kwargs={"status": "ACTIVE"}),
            Action(name="get_system_config_by_category", kwargs={"category": "gmail_labels"}),
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_006"}),
            Action(name="get_gmail_threads_by_labels", kwargs={"thread_id": "thread_007"}),
            Action(name="get_releases_by_owner", kwargs={"owner_email": "mike.ux@company.com", "created_after": "2024-08-20T16:30:00Z"}),
            Action(name="update_audit_status", kwargs={"audit_id": "audit_007", "new_status": "IN_PROGRESS", "updated_by": "mike.ux@company.com", "notes": "Review management coordination completed with audit workflow"}),
            Action(name="get_audit_summary", kwargs={"audit_id": "audit_007"})
        ],
        outputs=[
            "review_approvals_retrieved:cycle_001",
            "figma_artifacts_retrieved:ACTIVE",
            "system_config_retrieved:gmail_labels",
            "asset_export_verified:asset_006",
            "gmail_thread_retrieved:thread_007",
            "releases_retrieved:mike.ux@company.com:2024-08-20T16:30:00Z",
            "audit_status_updated:audit_007:IN_PROGRESS:mike.ux@company.com",
            "audit_summary_retrieved:audit_007"
        ]
    ),
    
    Task(
        annotator="0",
        user_id="user_46",
        instruction=(
            "You are a review cycle SLA management specialist responsible for coordinating review cycle escalation and integrated audit workflow management. "
            "Your task is to manage review cycle SLA coordination with audit status management and ensure proper escalation tracking. "
            "Focus on managing review cycle status transitions from NEEDS_REVIEW to ESCALATED, including audit status coordination and comprehensive logging. "
            "Coordinate with review teams through appropriate channels to ensure all SLA breaches and audit workflows are properly synchronized. "
            "Required constants: "
            "cycle_id=cycle_001, artifact_id=art_001, new_status=ESCALATED, "
            "audit_id=audit_001, audit_status=IN_PROGRESS, updated_by=sarah.designer@company.com, "
            "thread_id=thread_001, priority_level=HIGH, urgency_reason=SLA breach requires immediate escalation, "
            "escalate_to=sarah.designer@company.com, "
            "log_level=WARNING, component=review_sla, after_timestamp=2024-08-20T15:00:00Z, "
            "message_pattern=escalation, log_message=Review cycle SLA escalation completed with audit integration, "
            "asset_id=asset_001, export_status=COMPLETED, export_notes=SLA escalation asset export completed, dlp_scan_status=CLEAN"
        ),
        actions=[
            Action(name="get_review_approvals_summary", kwargs={"cycle_id": "cycle_001"}),
            Action(name="update_review_cycle_status", kwargs={"cycle_id": "cycle_001", "new_status": "ESCALATED", "reviewer_email": "sarah.designer@company.com", "completion_notes": "SLA breach requires immediate escalation"}),
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_001"}),
            Action(name="update_audit_status", kwargs={"audit_id": "audit_001", "new_status": "IN_PROGRESS", "updated_by": "sarah.designer@company.com"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "SLA breach requires immediate escalation"}),
            Action(name="add_terminal_log_entry", kwargs={"log_message": "Review cycle SLA escalation completed with audit integration", "log_level": "WARNING", "component": "review_sla", "user_email": "sarah.designer@company.com"}),
            Action(name="get_filtered_log_entries", kwargs={"log_level": "WARNING", "component": "review_sla", "after_timestamp": "2024-08-20T15:00:00Z", "message_pattern": "escalation"}),
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_001"}),
            Action(name="update_asset_export_status", kwargs={"asset_id": "asset_001", "new_status": "COMPLETED", "notes": "SLA escalation asset export completed", "dlp_scan_status": "CLEAN"})
        ],
        outputs=[
            "Review cycle SLA management completed for cycle_001: review cycle approvals verified for SLA coordination, review cycle status updated to ESCALATED with Sarah Designer oversight and SLA breach escalation notes, audit_001 status verified for coordination workflow, audit status updated to IN_PROGRESS with Sarah Designer assignment, Gmail thread priority escalated to HIGH with SLA breach urgency and stakeholder escalation, comprehensive SLA escalation logging added with WARNING level review_sla component tracking, filtered escalation logs retrieved for WARNING level pattern matching since August 20th, asset export summary retrieved for asset_001 coordination tracking, and asset export status updated to COMPLETED with SLA escalation export completion and DLP scan verification."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_47",
        instruction=(
            "You are an initial audit setup management specialist responsible for coordinating comprehensive audit initialization workflows and finding discovery/progress tracking processes. "
            "Your task is to manage initial audit setup coordination, finding discovery management, progress initialization, and system coordination processes for enterprise audit setup management. "
            "Focus on managing audit finding details discovery, initial progress tracking, status initialization, and release coordination workflows with comprehensive initial audit setup. "
            "Coordinate with audit setup teams through appropriate channels to ensure all initial audit setup and discovery workflows are properly orchestrated. "
            "Additionally, you'll retrieve comprehensive audit summaries to ensure proper oversight and coordination throughout the audit initialization process. "
            "Required constants: "
            "audit_id=audit_001, finding_id=finding_ds_001, include_resolved=False, "
            "progress_percentage=15, progress_notes=Initial audit setup commenced with comprehensive discovery, "
            "updated_by=sarah.designer@company.com, new_finding_status=OPEN, "
            "finding_notes=Initial audit finding discovered and opened for comprehensive analysis, "
            "release_id=release_001, category=design_system_aliases, thread_id=thread_001, "
            "owner_email=sarah.designer@company.com, created_after=2024-08-20T10:00:00Z, "
            "log_level=INFO, component=initial_audit_setup"
        ),
        actions=[
            Action(name="get_audit_finding_details", kwargs={"audit_id": "audit_001", "finding_id": "finding_ds_001", "include_resolved": False}),
            Action(name="update_audit_progress", kwargs={"audit_id": "audit_001", "progress_percentage": 15, "notes": "Initial audit setup commenced with comprehensive discovery", "updated_by": "sarah.designer@company.com"}),
            Action(name="update_audit_finding_status", kwargs={"finding_id": "finding_ds_001", "new_status": "OPEN", "notes": "Initial audit finding discovered and opened for comprehensive analysis", "updated_by": "sarah.designer@company.com"}),
            Action(name="get_release_summary", kwargs={"release_id": "release_001"}),
            Action(name="get_system_config_by_category", kwargs={"category": "design_system_aliases"}),
            Action(name="get_gmail_threads_by_labels", kwargs={"thread_id": "thread_001"}),
            Action(name="get_releases_by_owner", kwargs={"owner_email": "sarah.designer@company.com", "created_after": "2024-08-20T10:00:00Z"}),
            Action(name="get_terminal_logs_summary", kwargs={"log_level": "INFO", "component": "initial_audit_setup"}),
            Action(name="get_audit_summary", kwargs={"audit_id": "audit_001"})
        ],
        outputs=[
            "Initial audit setup management with finding discovery and progress tracking completed: audit_001 finding details retrieved with finding_ds_001 specifics and unresolved findings focus for initial discovery, audit progress updated to 15% with initial setup discovery notes by Sarah Designer, design system finding_ds_001 status updated to OPEN with initial discovery analysis notes by Sarah Designer, release_001 summary verified for release coordination, design_system_aliases config retrieved for system coordination, Gmail thread_001 verified for communication coordination, Sarah Designer releases retrieved for release coordination since August 20th, terminal logs summary retrieved for INFO level initial_audit_setup component, and audit_001 comprehensive summary retrieved for oversight and coordination."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_48",
        instruction=(
            "You are a design system component audit specialist responsible for coordinating comprehensive design system audits and thread priority management for component workflows. "
            "Your primary responsibility involves audit_002 coordination for design system components requiring comprehensive status tracking and thread priority management for component review coordination. The workflow integrates with approval verification and thread escalation for design system release preparation. "
            "The design system coordination workflow centers on comprehensive audit tracking with sarah.designer@company.com oversight, thread_001 HIGH priority management for design system coordination, and detailed approval verification across design system workflows. "
            "Your coordination efforts should ensure seamless design system audit coordination through comprehensive status tracking, effective thread priority management for component reviews, and detailed approval verification for design system workflows with proper design team coordination and release preparation tracking. "
            "Key parameters: "
            "audit_002_id=audit_002, audit_002_status=COMPLETED, "
            "art_008_id=art_008, audit_type=A11Y, "
            "thread_001_id=thread_001, thread_008_id=thread_008, "
            "thread_001_priority=HIGH, thread_008_priority=NORMAL, "
            "thread_001_urgency=Design system component review requires immediate coordination, "
            "thread_008_urgency=Design system follow-up coordination completed, "
            "completion_notes=Design system component audit completed successfully, "
            "approval_002_id=approval_002, cycle_002_id=cycle_002, "
            "escalate_to=sarah.designer@company.com,design.system@company.com, "
            "release_owner=sarah.designer@company.com, release_start_date=2024-08-20T13:00:00Z"
        ),
        actions=[
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_002"}),
            Action(name="update_audit_report_status", kwargs={"audit_id": "audit_002", "new_status": "COMPLETED", "completion_notes": "Design system component audit completed successfully"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Design system component review requires immediate coordination", "escalate_to": ["sarah.designer@company.com", "design.system@company.com"]}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_008", "new_priority": "NORMAL", "urgency_reason": "Design system follow-up coordination completed"}),
            Action(name="get_review_approvals_summary", kwargs={"approval_id": "approval_002", "cycle_id": "cycle_002"}),
            Action(name="get_audits_by_status", kwargs={"artifact_id": "art_008", "audit_type": "A11Y"}),
            Action(name="get_releases_by_owner", kwargs={"owner_email": "sarah.designer@company.com", "created_after": "2024-08-20T13:00:00Z"})
        ],
        outputs=[
            "audit_002_verified:audit_002",
            "audit_status_updated:COMPLETED",
            "thread_001_updated:HIGH",
            "thread_008_updated:NORMAL",
            "approval_verified:approval_002",
            "art_audit_verified:art_008",
            "releases_retrieved:sarah.designer@company.com"
        ]
    ),
    Task(
        annotator="0",
        user_id="user_49",
        instruction=(
            "You are a Figma comment resolution specialist responsible for accessibility feedback coordination and workflow management across admin panel header components. "
            "Your primary responsibility involves accessibility feedback coordination for art_008 admin panel header where unresolved comments with resolved_status False require identification and resolution coordination. The workflow also involves asset_007 admin header export integration requiring status verification and coordination alignment. "
            "The accessibility improvement workflow centers on comment_006 accessibility enhancement coordination involving mike.ux@company.com team member oversight, HIGH priority accessibility improvements, and comprehensive ARIA labels and keyboard navigation support implementation tracking. The feedback resolution requires progress status coordination and detailed implementation documentation. "
            "Your coordination efforts should ensure seamless accessibility audit communication through thread_004, effective comment lifecycle coordination, and comprehensive accessibility compliance tracking for stakeholder reporting and successful workflow completion."
            "Parameters: log_message=Figma comment resolution workflow completed for comment_006 accessibility improvements,"
            "note=Admin header accessibility export completed with ARIA labels"
        ),
        actions=[
            Action(name="get_figma_comments_by_artifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_007"}),
            Action(name="update_figma_comment_status", kwargs={"comment_id": "comment_006", "new_status": "IN_PROGRESS", "resolution_notes": "Accessibility improvements in progress - adding ARIA labels and keyboard navigation support", "assignee_email": "mike.ux@company.com", "priority_level": "HIGH"}),
            Action(name="get_gmail_threads_by_labels", kwargs={"thread_id": "thread_004"}),
            Action(name="get_figma_comments_by_artifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="update_asset_export_status", kwargs={"asset_id": "asset_007", "new_status": "COMPLETED", "notes": "Admin header accessibility export completed with ARIA labels", "dlp_scan_status": "CLEAN"}),
            Action(name="add_terminal_log_entry", kwargs={"log_message": "Figma comment resolution workflow completed for comment_006 accessibility improvements", "log_level": "INFO", "component": "figma_comment_resolution", "user_email": "mike.ux@company.com"}),
            Action(name="get_audits_by_status", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"})
        ],
        outputs=[
            "Comment resolution workflow completed for comment_006: comment status updated to IN_PROGRESS, assignee assigned to Mike UX with HIGH priority level, resolution notes added about accessibility improvements, asset export status verified for admin header asset_007, Gmail thread communication status verified for thread_004 accessibility audit coordination, asset export updated to COMPLETED with accessibility enhancements, accessibility audit status retrieved for A11Y audit type, and terminal log entry added for comment resolution workflow completion tracking."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_50",
        instruction=(
            "You are an email workflow manager responsible for coordinating the Homepage Hero Section design review process across stakeholder communication and approval workflows. "
            "Your primary focus involves thread_001 which currently has design-review and urgent labels but requires transition to approved and figma-integrated status for production readiness. The stakeholder coordination needs expansion to include mike.ux@company.com, alex.dev@company.com, lisa.marketing@company.com, and design-team@company.com with comprehensive handoff documentation noting design review completion and recipient list expansion for production coordination. "
            "The review workflow involves audit_001 findings and art_001 figma artifacts for status verification; cycle_001 review cycle requiring APPROVED status transition with email_workflow_manager_001 authorization and comprehensive approval comments about homepage hero section completion and email workflow coordination. "
            "Your workflow coordination should ensure seamless transition from urgent review status to approved production-ready status with proper label management, expanded stakeholder communication, and integrated email workflow and design review process completion. "
            "Make a comment as Homepage hero section approved after comprehensive review - updating review cycle status and coordinating with email workflow. "
            "Additionally, update the audit status to COMPLETED with comprehensive notes about the design review completion. "
            "Required constants: "
            "audit_id=audit_001, new_status=COMPLETED, updated_by=email_workflow_manager_001, notes=Homepage hero section design review completed and approved, "
            "asset_id=asset_001"
        ),
        actions=[
            Action(name="get_gmail_threads_by_labels", kwargs={"thread_id": "thread_001"}),
            Action(name="get_figma_artifacts_by_status", kwargs={"artifact_id": "art_001"}),
            Action(name="get_audit_findings_summary", kwargs={"audit_id": "audit_001"}),
            Action(name="update_gmail_thread_labels", kwargs={"thread_id": "thread_001", "new_labels": ["approved", "figma-integrated"], "remove_labels": ["urgent"], "update_recipients": ["mike.ux@company.com", "alex.dev@company.com", "lisa.marketing@company.com", "design-team@company.com"]}),
            Action(name="update_review_cycle_status", kwargs={"cycle_id": "cycle_001", "new_status": "APPROVED", "approver_id": "email_workflow_manager_001", "comments": "Homepage hero section approved after comprehensive review - updating review cycle status and coordinating with email workflow"}),
            Action(name="update_audit_status", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "notes": "Homepage hero section design review completed and approved", "updated_by": "email_workflow_manager_001"}),
            Action(name="get_gmail_threads_by_labels", kwargs={"thread_id": "thread_001"}),
            Action(name="get_figma_artifacts_by_status", kwargs={"artifact_id": "art_001"}),
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_001"})
        ],
        outputs=[
            "Email workflow management completed for thread_001: Gmail thread labels updated from urgent to approved/figma-integrated, recipients expanded to include design-team@company.com, review cycle cycle_001 status updated to APPROVED, audit_001 status updated to COMPLETED with review notes, coordination completed between email workflow and design review processes for seamless production handoff, and asset export summary retrieved for asset_001 documentation and production readiness verification."
        ]
    ),
    Task(
        annotator="0",
        user_id="user_51",
        instruction=(
            "You are a review cycle SLA management specialist responsible for coordinating review cycle escalation and integrated audit workflow management. "
            "Your task is to manage review cycle SLA coordination with audit status management and ensure proper escalation tracking. "
            "Focus on managing review cycle status transitions from NEEDS_REVIEW to ESCALATED, including audit status coordination and comprehensive logging. "
            "Coordinate with review teams through appropriate channels to ensure all SLA breaches and audit workflows are properly synchronized. "
            "Required constants: "
            "cycle_id=cycle_001, artifact_id=art_001, new_status=ESCALATED, "
            "audit_id=audit_001, audit_status=IN_PROGRESS, updated_by=sarah.designer@company.com, "
            "thread_id=thread_001, priority_level=HIGH, urgency_reason=SLA breach requires immediate escalation, "
            "escalate_to=sarah.designer@company.com, "
            "log_level=WARNING, component=review_sla, after_timestamp=2024-08-20T15:00:00Z, "
            "message_pattern=escalation, log_message=Review cycle SLA escalation completed with audit integration, "
            "asset_id=asset_001"
        ),
        actions=[
            Action(name="get_review_approvals_summary", kwargs={"cycle_id": "cycle_001"}),
            Action(name="update_review_cycle_status", kwargs={"cycle_id": "cycle_001", "new_status": "ESCALATED", "reviewer_email": "sarah.designer@company.com", "completion_notes": "SLA breach requires immediate escalation"}),
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_001"}),
            Action(name="update_audit_status", kwargs={"audit_id": "audit_001", "new_status": "IN_PROGRESS", "updated_by": "sarah.designer@company.com"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "SLA breach requires immediate escalation"}),
            Action(name="add_terminal_log_entry", kwargs={"log_message": "Review cycle SLA escalation completed with audit integration", "log_level": "WARNING", "component": "review_sla", "user_email": "sarah.designer@company.com"}),
            Action(name="get_filtered_log_entries", kwargs={"log_level": "WARNING", "component": "review_sla", "after_timestamp": "2024-08-20T15:00:00Z", "message_pattern": "escalation"}),
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_001"})
        ],
        outputs=[
            "Review cycle SLA management completed for cycle_001: review cycle approvals verified for SLA coordination, review cycle status updated to ESCALATED with Sarah Designer oversight and SLA breach escalation notes, audit_001 status verified for coordination workflow, audit status updated to IN_PROGRESS with Sarah Designer assignment, Gmail thread priority escalated to HIGH with SLA breach urgency and stakeholder escalation, comprehensive SLA escalation logging added with WARNING level review_sla component tracking, filtered escalation logs retrieved for WARNING level pattern matching since August 20th, and asset export summary retrieved for asset_001 coordination tracking."
        ]
    ),
    Task(
        annotator="0",
        user_id="user_52",
        instruction=(
            "You are a Figma comment resolution specialist responsible for accessibility feedback coordination and workflow management across admin panel header components. "
            "Your primary responsibility involves accessibility feedback coordination for art_008 admin panel header where unresolved comments with resolved_status False require identification and resolution coordination. The workflow also involves asset_007 admin header export integration requiring status verification and coordination alignment. "
            "The accessibility improvement workflow centers on comment_006 accessibility enhancement coordination involving mike.ux@company.com team member oversight, HIGH priority accessibility improvements, and comprehensive ARIA labels and keyboard navigation support implementation tracking. The feedback resolution requires progress status coordination and detailed implementation documentation. "
            "Your coordination efforts should ensure seamless accessibility audit communication through thread_004, effective comment lifecycle coordination, and comprehensive accessibility compliance tracking for stakeholder reporting and successful workflow completion."
            "You can use resolution_notes Accessibility improvements in progress - adding ARIA labels and keyboard navigation support"
        ),
        actions=[
            Action(name="get_figma_comments_by_artifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_007"}),
            Action(name="update_figma_comment_status", kwargs={"comment_id": "comment_006", "new_status": "IN_PROGRESS", "resolution_notes": "Accessibility improvements in progress - adding ARIA labels and keyboard navigation support", "assignee_email": "mike.ux@company.com", "priority_level": "HIGH"}),
            Action(name="get_gmail_threads_by_labels", kwargs={"thread_id": "thread_004"}),
            Action(name="get_figma_comments_by_artifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="add_terminal_log_entry", kwargs={"log_message": "Figma comment resolution workflow completed for accessibility improvements", "log_level": "INFO", "component": "figma_comment_resolution", "user_email": "mike.ux@company.com"}),
            Action(name="update_asset_export_status", kwargs={"asset_id": "asset_007", "new_status": "COMPLETED", "notes": "Admin header accessibility export completed with ARIA labels", "dlp_scan_status": "CLEAN"})
        ],
        outputs=[
            "Comment resolution workflow completed. comment status updated, assignee assigned to Mike UX with HIGH priority level, resolution notes added about accessibility improvements, asset export status verified for admin header asset_007, Gmail thread communication status verified for thread_004 accessibility audit coordination, terminal log entry added for comment resolution workflow tracking, and asset export status updated to COMPLETED with accessibility enhancements."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_53",
        instruction=(
            "You are an audit report management specialist responsible for coordinating the end-to-end audit lifecycle for design system components and accessibility compliance. "
            "Your primary responsibility involves managing audit_001 for artifact art_001 (Homepage Hero Section) which requires comprehensive status tracking from COMPLETED to final report generation. The workflow integrates with audit_002 for accessibility review of art_008 admin panel components requiring status coordination. "
            "The audit management workflow centers on thread_001 priority escalation to HIGH priority for design review coordination involving sarah.designer@company.com oversight, URGENT priority level escalation for comprehensive design review tracking, and escalation_reason 'Critical audit findings require immediate design team attention and stakeholder review'. The priority management requires comprehensive Gmail thread coordination and detailed audit status documentation. "
            "Your coordination efforts should ensure seamless audit report generation through proper status management, effective priority escalation for design review threads, comprehensive audit findings tracking for stakeholder reporting, and successful audit lifecycle completion with proper report asset associations. "
            "Key parameters: audit_id=audit_001, new_status=COMPLETED, report_asset_id=asset_001, completion_notes=Design system audit completed with recommendations, "
            "thread_001_priority=HIGH, thread_002_priority=NORMAL, thread_001_urgency=Critical audit findings require immediate design team attention, thread_002_urgency=Secondary audit review completed, "
            "escalate_to=sarah.designer@company.com,mike.ux@company.com, audit_type=COMBINED_DS_A11Y, created_after=2024-08-20T15:00:00Z, audit_date_filter=2024-08-18T00:00:00Z, "
            "thread_ids=thread_001,thread_002, artifact_ids=art_001,art_008, "
            "asset_id=asset_001, "
            "log_message=Audit management workflow completed with comprehensive tracking and report generation, "
            "log_level=INFO, component=audit_management, user_email=sarah.designer@company.com"
        ),
        actions=[
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_001"}),
            Action(name="update_audit_report_status", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed with recommendations"}),
            Action(name="get_audits_by_status", kwargs={"status": "COMPLETED", "audit_type": "COMBINED_DS_A11Y"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical audit findings require immediate design team attention", "escalate_to": ["sarah.designer@company.com", "mike.ux@company.com"]}),
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_002"}),
            Action(name="get_audits_by_status", kwargs={"artifact_id": "art_001", "created_after": "2024-08-20T15:00:00Z"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Secondary audit review completed"}),
            Action(name="get_audits_by_status", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"}),
            Action(name="get_system_config_by_category", kwargs={"category": "audit_config"}),
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_001"}),
            Action(name="get_figma_artifacts_by_status", kwargs={"artifact_id": "art_001", "status": "APPROVED"}),
            Action(name="add_terminal_log_entry", kwargs={"log_message": "Audit management workflow completed with comprehensive tracking and report generation", "log_level": "INFO", "component": "audit_management", "user_email": "sarah.designer@company.com"})
        ],
        outputs=[
            "Audit management workflow completed: audit_001 status updated to COMPLETED with report asset_001 association and completion notes, thread_001 priority escalated to HIGH with critical findings urgency and stakeholder escalation to design team, secondary thread_002 priority normalized, comprehensive audit status verification completed across all COMBINED_DS_A11Y and A11Y audit types for stakeholder reporting, audit configuration retrieved for system coordination settings, asset export summary retrieved for asset_001 coordination and compliance tracking, Figma artifacts verified for art_001 with APPROVED status ensuring design system integration, and terminal log entry added documenting audit management workflow completion with comprehensive tracking."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_54",
        instruction=(
            "You are an accessibility audit specialist responsible for finalizing the audit process. Your task is to update the status of audit_001 to reflect the resolution of design system findings. "
            "You need to map a button component to Button-Primary-v1.2 for accessibility compliance. "
            "After completing the audit, you should update the review cycle cycle_001 to APPROVED to indicate the completion of the audit. "
            "As part of your responsibilities, you must verify the asset_001 export status to ensure all components are properly documented. "
            "Make sure to include these required parameters in your updates: "
            "audit_id=audit_001, new_status=COMPLETED, notes='Button component mapped to Button-Primary-v1.2 for accessibility compliance', "
            "updated_by=alice.designer@company.com, cycle_id=cycle_001, status_notes='Audit completed with component mapping updates', "
            "asset_id=asset_001"
        ),
        actions=[
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_001"}),
            Action(name="update_audit_status", kwargs={
                "audit_id": "audit_001",
                "new_status": "COMPLETED",
                "notes": "Button component mapped to Button-Primary-v1.2 for accessibility compliance",
                "updated_by": "alice.designer@company.com"
            }),
            Action(name="get_review_approvals_summary", kwargs={"cycle_id": "cycle_001"}),
            Action(name="update_review_cycle_status", kwargs={
                "cycle_id": "cycle_001",
                "new_status": "APPROVED",
                "status_notes": "Audit completed with component mapping updates",
                "updated_by": "alice.designer@company.com"
            }),
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_001"}),
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_001"}),
            Action(name="get_review_approvals_summary", kwargs={"cycle_id": "cycle_001"})
        ],
        outputs=[
            "Audit audit_001 status updated to COMPLETED with resolution notes",
            "Review cycle cycle_001 status updated to APPROVED with audit completion notes",
            "Asset export summary retrieved for asset_001"
        ]
    ),
    Task(
        annotator="0",
        user_id="user_55",
        instruction=(
            "You are a Figma comment resolution specialist responsible for accessibility feedback coordination and workflow management across admin panel header components. "
            "Your primary responsibility involves accessibility feedback coordination for art_008 admin panel header where unresolved comments with resolved_status False require identification and resolution coordination. The workflow also involves asset_007 admin header export integration requiring status verification and coordination alignment. "
            "The accessibility improvement workflow centers on comment_006 accessibility enhancement coordination involving mike.ux@company.com team member oversight, HIGH priority accessibility improvements, and comprehensive ARIA labels and keyboard navigation support implementation tracking. The feedback resolution requires progress status coordination and detailed implementation documentation. "
            "Your coordination efforts should ensure seamless accessibility audit communication through thread_004, effective comment lifecycle coordination, and comprehensive accessibility compliance tracking for stakeholder reporting and successful workflow completion."
            "You can use resolution_notes Accessibility improvements in progress - adding ARIA labels and keyboard navigation support"
        ),
        actions=[
            Action(name="get_figma_comments_by_artifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_007"}),
            Action(name="update_figma_comment_status", kwargs={"comment_id": "comment_006", "new_status": "IN_PROGRESS", "resolution_notes": "Accessibility improvements in progress - adding ARIA labels and keyboard navigation support", "assignee_email": "mike.ux@company.com", "priority_level": "HIGH"}),
            Action(name="get_gmail_threads_by_labels", kwargs={"thread_id": "thread_004"}),
            Action(name="get_figma_comments_by_artifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="add_terminal_log_entry", kwargs={"log_message": "Figma comment resolution workflow completed for accessibility improvements", "log_level": "INFO", "component": "figma_comment_resolution", "user_email": "mike.ux@company.com"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_004", "new_priority": "HIGH", "urgency_reason": "Accessibility feedback coordination requires immediate attention", "escalate_to": ["mike.ux@company.com"]})
        ],
        outputs=[
            "Comment resolution workflow completed. comment status updated, assignee assigned to Mike UX with HIGH priority level, resolution notes added about accessibility improvements, asset export status verified for admin header asset_007, Gmail thread communication status verified for thread_004 accessibility audit coordination, terminal log entry added for comment resolution workflow tracking, and Gmail thread priority updated to HIGH for accessibility feedback coordination."
        ]
    ),    

    Task(
        annotator="0",
        user_id="user_56",
        instruction=(
            "You are an audit report management specialist responsible for coordinating the end-to-end audit lifecycle for design system components and accessibility compliance. "
            "Your primary responsibility involves managing audit_001 for artifact art_001 (Homepage Hero Section) which requires comprehensive status tracking from COMPLETED to final report generation. The workflow integrates with audit_002 for accessibility review of art_008 admin panel components requiring status coordination. "
            "The audit management workflow centers on thread_001 priority escalation to HIGH priority for design review coordination involving sarah.designer@company.com oversight, URGENT priority level escalation for comprehensive design review tracking, and escalation_reason 'Critical audit findings require immediate design team attention and stakeholder review'. The priority management requires comprehensive Gmail thread coordination and detailed audit status documentation. "
            "Your coordination efforts should ensure seamless audit report generation through proper status management, effective priority escalation for design review threads, comprehensive audit findings tracking for stakeholder reporting, and successful audit lifecycle completion with proper report asset associations. "
            "Key parameters: audit_id=audit_001, new_status=COMPLETED, report_asset_id=asset_001, completion_notes=Design system audit completed with recommendations, "
            "thread_001_priority=HIGH, thread_002_priority=NORMAL, thread_001_urgency=Critical audit findings require immediate design team attention, thread_002_urgency=Secondary audit review completed, "
            "escalate_to=sarah.designer@company.com,mike.ux@company.com, audit_type=COMBINED_DS_A11Y, created_after=2024-08-20T15:00:00Z, audit_date_filter=2024-08-18T00:00:00Z, "
            "thread_ids=thread_001,thread_002, artifact_ids=art_001,art_008, "
            "asset_id=asset_001, "
            "log_message=Audit management workflow completed with comprehensive tracking and report generation, "
            "log_level=INFO, component=audit_management, user_email=sarah.designer@company.com"
        ),
        actions=[
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_001"}),
            Action(name="update_audit_report_status", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed with recommendations"}),
            Action(name="get_audits_by_status", kwargs={"status": "COMPLETED", "audit_type": "COMBINED_DS_A11Y"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical audit findings require immediate design team attention", "escalate_to": ["sarah.designer@company.com", "mike.ux@company.com"]}),
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_002"}),
            Action(name="get_audits_by_status", kwargs={"artifact_id": "art_001", "created_after": "2024-08-20T15:00:00Z"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Secondary audit review completed"}),
            Action(name="get_audits_by_status", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"}),
            Action(name="get_system_config_by_category", kwargs={"category": "audit_config"}),
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_001"}),
            Action(name="get_figma_comments_by_artifact", kwargs={"artifact_id": "art_001", "resolved_status": True}),
            Action(name="add_terminal_log_entry", kwargs={"log_message": "Audit management workflow completed with comprehensive tracking and report generation", "log_level": "INFO", "component": "audit_management", "user_email": "sarah.designer@company.com"})
        ],
        outputs=[
            "Audit management workflow completed: audit_001 status updated to COMPLETED with report asset_001 association and completion notes, thread_001 priority escalated to HIGH with critical findings urgency and stakeholder escalation to design team, secondary thread_002 priority normalized, comprehensive audit status verification completed across all COMBINED_DS_A11Y and A11Y audit types for stakeholder reporting, audit configuration retrieved for system coordination settings, asset export summary retrieved for asset_001 coordination and compliance tracking, Figma comments verified for art_001 with resolved status ensuring design system feedback integration, and terminal log entry added documenting audit management workflow completion with comprehensive tracking."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_57",
        instruction=(
            "You are an audit report management specialist responsible for coordinating the end-to-end audit lifecycle for design system components and accessibility compliance. "
            "Your primary responsibility involves managing audit_001 for artifact art_001 (Homepage Hero Section) which requires comprehensive status tracking from COMPLETED to final report generation. The workflow integrates with audit_002 for accessibility review of art_008 admin panel components requiring status coordination. "
            "The audit management workflow centers on thread_001 priority escalation to HIGH priority for design review coordination involving sarah.designer@company.com oversight, URGENT priority level escalation for comprehensive design review tracking, and escalation_reason 'Critical audit findings require immediate design team attention and stakeholder review'. The priority management requires comprehensive Gmail thread coordination and detailed audit status documentation. "
            "Your coordination efforts should ensure seamless audit report generation through proper status management, effective priority escalation for design review threads, comprehensive audit findings tracking for stakeholder reporting, and successful audit lifecycle completion with proper report asset associations. "
            "Key parameters: audit_id=audit_001, new_status=COMPLETED, report_asset_id=asset_001, completion_notes=Design system audit completed with recommendations, "
            "thread_001_priority=HIGH, thread_002_priority=NORMAL, thread_001_urgency=Critical audit findings require immediate design team attention, thread_002_urgency=Secondary audit review completed, "
            "escalate_to=sarah.designer@company.com,mike.ux@company.com, audit_type=COMBINED_DS_A11Y, created_after=2024-08-20T15:00:00Z, audit_date_filter=2024-08-18T00:00:00Z, "
            "thread_ids=thread_001,thread_002, artifact_ids=art_001,art_008"
        ),
        actions=[
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_001"}),
            Action(name="update_audit_report_status", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed with recommendations"}),
            Action(name="get_audits_by_status", kwargs={"status": "COMPLETED", "audit_type": "COMBINED_DS_A11Y"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical audit findings require immediate design team attention", "escalate_to": ["sarah.designer@company.com", "mike.ux@company.com"]}),
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_002"}),
            Action(name="update_audit_report_status", kwargs={"audit_id": "audit_002", "new_status": "COMPLETED", "report_asset_id": "asset_007"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Secondary audit review completed"}),
            Action(name="get_audits_by_status", kwargs={"status": "COMPLETED", "created_after": "2024-08-20T15:00:00Z"}),
            Action(name="get_audits_by_status", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"})
        ],
        outputs=[
            "Audit management workflow completed: audit_001 status updated to COMPLETED with report asset_001 association and completion notes, thread_001 priority escalated to HIGH with critical findings urgency and stakeholder escalation to design team, audit_002 status updated to COMPLETED with report asset_007, secondary thread_002 priority normalized, and comprehensive audit status verification completed across all COMBINED_DS_A11Y and A11Y audit types for stakeholder reporting."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_58",
        instruction=(
            "You are a Figma comment resolution specialist managing accessibility improvements for the admin panel header. "
            "Your task is to coordinate the resolution of accessibility feedback and ensure all related assets and communications are properly tracked. "
            "Focus on managing the accessibility enhancement workflow, including comment resolution and asset export status updates. "
            "Coordinate with the UX team through the appropriate communication channels to ensure all accessibility requirements are met. "
            "Required constants: "
            "artifact_id=art_008, asset_id=asset_007, comment_id=comment_006, "
            "assignee_email=mike.ux@company.com, priority_level=HIGH, "
            "thread_ids=thread_004,thread_005, "
            "resolution_notes=Accessibility improvements in progress - adding ARIA labels and keyboard navigation support, "
            "export_notes=Admin header accessibility export completed with ARIA labels, "
            "dlp_scan_status=CLEAN, "
            "new_status=IN_PROGRESS, export_status=COMPLETED"
        ),
        actions=[
            Action(name="get_figma_comments_by_artifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_007"}),
            Action(name="update_figma_comment_status", kwargs={"comment_id": "comment_006", "new_status": "IN_PROGRESS", "resolution_notes": "Accessibility improvements in progress - adding ARIA labels and keyboard navigation support", "assignee_email": "mike.ux@company.com", "priority_level": "HIGH"}),
            Action(name="get_gmail_threads_by_labels", kwargs={"thread_id": "thread_004"}),
            Action(name="get_gmail_threads_by_labels", kwargs={"thread_id": "thread_005"}),  # Additional action
            Action(name="get_figma_comments_by_artifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="update_asset_export_status", kwargs={"asset_id": "asset_007", "new_status": "COMPLETED", "notes": "Admin header accessibility export completed with ARIA labels", "dlp_scan_status": "CLEAN"})
        ],
        outputs=[
            "Comment resolution workflow completed for comment_006: comment status updated to IN_PROGRESS, assignee assigned to Mike UX with HIGH priority level, resolution notes added about accessibility improvements, asset export status verified for admin header asset_007, Gmail thread communication status verified for thread_004 and thread_005 accessibility audit coordination, and asset export updated to COMPLETED with accessibility enhancements."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_59",
        instruction=(
            "You are a mobile component audit integration specialist responsible for coordinating comprehensive mobile audit workflows and release management for mobile application components. "
            "Your primary responsibility involves audit_002 management for mobile components requiring comprehensive status tracking and thread_002 CRITICAL priority escalation for mobile dashboard release coordination. The workflow integrates with approval verification for mobile workflows and comprehensive audit tracking for mobile application readiness. "
            "The mobile integration workflow centers on comprehensive audit coordination with mike.ux@company.com oversight, thread_007 HIGH priority management for mobile app release coordination, escalation_reason \"Mobile application release requires immediate audit integration and cross-team coordination\", and detailed approval tracking for mobile component workflows with release preparation focus. "
            "Your coordination efforts should ensure seamless mobile audit integration through comprehensive status coordination, effective priority escalation for mobile release threads, and detailed approval verification for mobile workflows with proper UX team coordination and release readiness tracking. "
            "Key parameters: "
            "audit_002_id=audit_002, audit_002_status=COMPLETED, "
            "thread_002_id=thread_002, thread_007_id=thread_007, "
            "additional_thread_id=thread_005, "
            "thread_002_priority=CRITICAL, thread_007_priority=HIGH, "
            "thread_002_urgency=Mobile application release requires immediate coordination, "
            "thread_007_urgency=Mobile app release coordination support required, "
            "additional_thread_priority=NORMAL, "
            "additional_thread_urgency=Mobile component design review required, "
            "completion_notes=Mobile component audit completed with accessibility integration, "
            "approval_002_id=approval_002, cycle_002_id=cycle_002, "
            "audit_type=A11Y, "
            "created_after_date=2024-08-19T12:00:00Z, "
            "escalate_to=mike.ux@company.com,mobile.team@company.com"
        ),
        actions=[
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_002"}),
            Action(name="update_audit_report_status", kwargs={"audit_id": "audit_002", "new_status": "COMPLETED", "completion_notes": "Mobile component audit completed with accessibility integration"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_002", "new_priority": "CRITICAL", "urgency_reason": "Mobile application release requires immediate coordination", "escalate_to": ["mike.ux@company.com", "mobile.team@company.com"]}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_005", "new_priority": "NORMAL", "urgency_reason": "Mobile component design review required"}),  # Additional action
            Action(name="get_review_approvals_summary", kwargs={"approval_id": "approval_002", "cycle_id": "cycle_002"}),
            Action(name="get_audits_by_status", kwargs={"created_after": "2024-08-19T12:00:00Z", "audit_type": "A11Y"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_007", "new_priority": "HIGH", "urgency_reason": "Mobile app release coordination support required"})
        ],
        outputs=[
            "audit_002 status=COMPLETED, thread_002 priority=CRITICAL, thread_005 priority=NORMAL, thread_007 priority=HIGH, approval_002 cycle=cycle_002, A11Y audits since 2024-08-19 verified"
        ]
    ),

    Task(
        annotator="0",
        user_id="user_60",
        instruction=(
            "You are a mobile component audit integration specialist responsible for coordinating comprehensive mobile audit workflows and release management for mobile application components. "
            "Your primary responsibility involves audit_002 management for mobile components requiring comprehensive status tracking and thread_002 CRITICAL priority escalation for mobile dashboard release coordination. The workflow integrates with approval verification for mobile workflows and comprehensive audit tracking for mobile application readiness. "
            "The mobile integration workflow centers on comprehensive audit coordination with mike.ux@company.com oversight, thread_007 HIGH priority management for mobile app release coordination, escalation_reason \"Mobile application release requires immediate audit integration and cross-team coordination\", and detailed approval tracking for mobile component workflows with release preparation focus. "
            "Your coordination efforts should ensure seamless mobile audit integration through comprehensive status coordination, effective priority escalation for mobile release threads, and detailed approval verification for mobile workflows with proper UX team coordination and release readiness tracking. "
            "Key parameters: "
            "audit_002_id=audit_002, audit_002_status=COMPLETED, "
            "thread_002_id=thread_002, thread_007_id=thread_007, "
            "thread_002_priority=CRITICAL, thread_007_priority=HIGH, "
            "thread_002_urgency=Mobile application release requires immediate coordination, "
            "thread_007_urgency=Mobile app release coordination support required, "
            "completion_notes=Mobile component audit completed with accessibility integration, "
            "approval_002_id=approval_002, cycle_002_id=cycle_002, "
            "audit_type=A11Y, "
            "additional_audit_id=audit_003, "
            "created_after_date=2024-08-19T12:00:00Z, "
            "escalate_to=mike.ux@company.com,mobile.team@company.com"
        ),
        actions=[
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_002"}),
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_003"}),  # Additional action
            Action(name="update_audit_report_status", kwargs={"audit_id": "audit_002", "new_status": "COMPLETED", "completion_notes": "Mobile component audit completed with accessibility integration"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_002", "new_priority": "CRITICAL", "urgency_reason": "Mobile application release requires immediate coordination", "escalate_to": ["mike.ux@company.com", "mobile.team@company.com"]}),
            Action(name="get_review_approvals_summary", kwargs={"approval_id": "approval_002", "cycle_id": "cycle_002"}),
            Action(name="get_audits_by_status", kwargs={"created_after": "2024-08-19T12:00:00Z", "audit_type": "A11Y"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_007", "new_priority": "HIGH", "urgency_reason": "Mobile app release coordination support required"})
        ],
        outputs=[
            "Mobile component audit integration completed: audit_002 status verified for mobile component tracking, additional audit_003 status checked for comprehensive coverage, audit_002 status updated to COMPLETED with mobile accessibility integration notes, thread_002 priority escalated to CRITICAL for mobile release with UX team and mobile team escalation, approval_002 verification completed for cycle_002 mobile workflow coordination, comprehensive A11Y audit verification completed for mobile components since dashboard creation, and thread_007 priority elevated to HIGH for mobile app release coordination support."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_61",
        instruction=(
            "You are a Figma comment resolution specialist responsible for accessibility feedback coordination and workflow management across admin panel header components. "
            "Your primary responsibility involves accessibility feedback coordination for art_008 admin panel header where unresolved comments with resolved_status False require identification and resolution coordination. The workflow also involves asset_007 admin header export integration requiring status verification and coordination alignment. "
            "The accessibility improvement workflow centers on comment_006 accessibility enhancement coordination involving mike.ux@company.com team member oversight, HIGH priority accessibility improvements, and comprehensive ARIA labels and keyboard navigation support implementation tracking. The feedback resolution requires progress status coordination and detailed implementation documentation. "
            "Your coordination efforts should ensure seamless accessibility audit communication through thread_004, effective comment lifecycle coordination, and comprehensive accessibility compliance tracking for stakeholder reporting and successful workflow completion."
            "You can use resolution_notes Accessibility improvements in progress - adding ARIA labels and keyboard navigation support"
        ),
        actions=[
            Action(name="get_figma_comments_by_artifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_007"}),
            Action(name="update_figma_comment_status", kwargs={"comment_id": "comment_006", "new_status": "IN_PROGRESS", "resolution_notes": "Accessibility improvements in progress - adding ARIA labels and keyboard navigation support", "assignee_email": "mike.ux@company.com", "priority_level": "HIGH"}),
            Action(name="get_gmail_threads_by_labels", kwargs={"thread_id": "thread_004"}),
            Action(name="get_figma_comments_by_artifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="add_terminal_log_entry", kwargs={"log_message": "Figma comment resolution workflow completed for accessibility improvements", "log_level": "INFO", "component": "figma_comment_resolution", "user_email": "mike.ux@company.com"}),
            Action(name="get_system_config_by_category", kwargs={"category": "accessibility_config"})
        ],
        outputs=[
            "Comment resolution workflow completed. comment status updated, assignee assigned to Mike UX with HIGH priority level, resolution notes added about accessibility improvements, asset export status verified for admin header asset_007, Gmail thread communication status verified for thread_004 accessibility audit coordination, terminal log entry added for comment resolution workflow tracking, and system configuration retrieved for accessibility_config category."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_62",
        instruction=(
            "You are a Figma comment resolution specialist responsible for accessibility feedback coordination and workflow management across admin panel header components. "
            "Your primary responsibility involves accessibility feedback coordination for art_008 admin panel header where unresolved comments with resolved_status False require identification and resolution coordination. The workflow also involves asset_007 admin header export integration requiring status verification and coordination alignment. "
            "The accessibility improvement workflow centers on comment_006 accessibility enhancement coordination involving mike.ux@company.com team member oversight, HIGH priority accessibility improvements, and comprehensive ARIA labels and keyboard navigation support implementation tracking. The feedback resolution requires progress status coordination and detailed implementation documentation. "
            "Your coordination efforts should ensure seamless accessibility audit communication through thread_004, effective comment lifecycle coordination, and comprehensive accessibility compliance tracking for stakeholder reporting and successful workflow completion."
        ),
        actions=[
            Action(name="get_figma_comments_by_artifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_007"}),
            Action(name="update_figma_comment_status", kwargs={"comment_id": "comment_006", "new_status": "IN_PROGRESS", "resolution_notes": "Accessibility improvements in progress - adding ARIA labels and keyboard navigation support", "assignee_email": "mike.ux@company.com", "priority_level": "HIGH"}),
            Action(name="get_gmail_threads_by_labels", kwargs={"thread_id": "thread_004"}),
            Action(name="get_figma_comments_by_artifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="update_asset_export_status", kwargs={"asset_id": "asset_007", "new_status": "COMPLETED", "notes": "Admin header accessibility export completed with ARIA labels", "dlp_scan_status": "CLEAN"}),
            Action(name="add_terminal_log_entry", kwargs={"log_message": "Figma comment resolution workflow completed for comment_006 accessibility improvements", "log_level": "INFO", "component": "figma_comment_resolution", "user_email": "mike.ux@company.com"}),
            Action(name="get_audits_by_status", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"})
        ],
        outputs=[
            "Comment resolution workflow completed for comment_006: comment status updated to IN_PROGRESS, assignee assigned to Mike UX with HIGH priority level, resolution notes added about accessibility improvements, asset export status verified for admin header asset_007, Gmail thread communication status verified for thread_004 accessibility audit coordination, asset export updated to COMPLETED with accessibility enhancements, accessibility audit status retrieved for A11Y audit type, and terminal log entry added for comment resolution workflow completion tracking."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_63",
        instruction=(
            "You are a Figma comment resolution specialist responsible for accessibility feedback coordination and workflow management across admin panel header components. "
            "Your primary responsibility involves accessibility feedback coordination for art_008 admin panel header where unresolved comments with resolved_status False require identification and resolution coordination. The workflow also involves asset_007 admin header export integration requiring status verification and coordination alignment. "
            "The accessibility improvement workflow centers on comment_006 accessibility enhancement coordination involving mike.ux@company.com team member oversight, HIGH priority accessibility improvements, and comprehensive ARIA labels and keyboard navigation support implementation tracking. The feedback resolution requires progress status coordination and detailed implementation documentation. "
            "Your coordination efforts should ensure seamless accessibility audit communication through thread_004, effective comment lifecycle coordination, and comprehensive accessibility compliance tracking for stakeholder reporting and successful workflow completion."
            "Use resolution_notes Accessibility improvements in progress - adding ARIA labels and keyboard navigation support or similar"
            "Use note Admin header accessibility export completed with ARIA labels when export is COMPLETED"
        ),
        actions=[
            Action(name="get_figma_comments_by_artifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_007"}),
            Action(name="update_figma_comment_status", kwargs={"comment_id": "comment_006", "new_status": "IN_PROGRESS", "resolution_notes": "Accessibility improvements in progress - adding ARIA labels and keyboard navigation support", "assignee_email": "mike.ux@company.com", "priority_level": "HIGH"}),
            Action(name="get_gmail_threads_by_labels", kwargs={"thread_id": "thread_004"}),
            Action(name="get_figma_comments_by_artifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="update_asset_export_status", kwargs={"asset_id": "asset_007", "new_status": "COMPLETED", "notes": "Admin header accessibility export completed with ARIA labels", "dlp_scan_status": "CLEAN"}),
            Action(name="get_figma_artifacts_by_status", kwargs={"artifact_id": "art_008"})
        ],
        outputs=[
            "Comment resolution workflow completed for comment_006: comment status updated to IN_PROGRESS, assignee assigned to Mike UX with HIGH priority level, resolution notes added about accessibility improvements, asset export status verified for admin header asset_007, Gmail thread communication status verified for thread_004 accessibility audit coordination, asset export updated to COMPLETED with accessibility enhancements, and artifact status verified for comprehensive tracking."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_64",
        instruction=(
            "You are a design system component audit specialist responsible for coordinating comprehensive design system audits and thread priority management for component workflows. "
            "Your primary responsibility involves audit_002 coordination for design system components requiring comprehensive status tracking and thread priority management for component review coordination. The workflow integrates with approval verification and thread escalation for design system release preparation. "
            "The design system coordination workflow centers on comprehensive audit tracking with sarah.designer@company.com oversight, thread_001 HIGH priority management for design system coordination, and detailed approval verification across design system workflows. "
            "Your coordination efforts should ensure seamless design system audit coordination through comprehensive status tracking, effective thread priority management for component reviews, and detailed approval verification for design system workflows with proper design team coordination and release preparation tracking. "
            "Key parameters: "
            "audit_002_id=audit_002, audit_002_status=COMPLETED, "
            "art_008_id=art_008, audit_type=A11Y, "
            "thread_001_id=thread_001, thread_008_id=thread_008, "
            "thread_001_priority=HIGH, thread_008_priority=NORMAL, "
            "thread_001_urgency=Design system component review requires immediate coordination, "
            "thread_008_urgency=Design system follow-up coordination completed, "
            "completion_notes=Design system component audit completed successfully, "
            "approval_002_id=approval_002, cycle_002_id=cycle_002, "
            "escalate_to=sarah.designer@company.com,design.system@company.com, "
            "release_owner=sarah.designer@company.com, release_start_date=2024-08-20T13:00:00Z, "
            "log_message=Design system component audit workflow completed with comprehensive tracking, "
            "log_level=INFO, component=design_system_audit, user_email=sarah.designer@company.com"
        ),
        actions=[
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_002"}),
            Action(name="update_audit_report_status", kwargs={"audit_id": "audit_002", "new_status": "COMPLETED", "completion_notes": "Design system component audit completed successfully"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Design system component review requires immediate coordination", "escalate_to": ["sarah.designer@company.com", "design.system@company.com"]}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_008", "new_priority": "NORMAL", "urgency_reason": "Design system follow-up coordination completed"}),
            Action(name="get_review_approvals_summary", kwargs={"approval_id": "approval_002", "cycle_id": "cycle_002"}),
            Action(name="get_audits_by_status", kwargs={"artifact_id": "art_008", "audit_type": "A11Y"}),
            Action(name="get_releases_by_owner", kwargs={"owner_email": "sarah.designer@company.com", "created_after": "2024-08-20T13:00:00Z"}),
            Action(name="add_terminal_log_entry", kwargs={"log_message": "Design system component audit workflow completed with comprehensive tracking", "log_level": "INFO", "component": "design_system_audit", "user_email": "sarah.designer@company.com"})
        ],
        outputs=[
            "audit_002_verified:audit_002",
            "audit_status_updated:COMPLETED",
            "thread_001_updated:HIGH",
            "thread_008_updated:NORMAL",
            "approval_verified:approval_002",
            "art_audit_verified:art_008",
            "releases_retrieved:sarah.designer@company.com",
            "terminal_log_added:design_system_audit_workflow_completed"
        ]
    ),

    Task(
        annotator="0",
        user_id="user_65",
        instruction=(
            "You are a mobile audit findings severity management specialist responsible for coordinating audit finding severity updates and integrated fix plan workflows. "
            "Your task is to manage audit finding severity escalation with fix plan status coordination and ensure proper priority management. "
            "Focus on managing audit finding severity updates for CRITICAL violations, including fix plan delivery coordination and comprehensive fix item tracking. "
            "Coordinate with development teams through appropriate channels to ensure all audit findings and fix workflows are properly synchronized. "
            "Additionally, you'll retrieve audit summaries to ensure comprehensive oversight and coordination throughout the severity management process. "
            "Required constants: "
            "finding_id=finding_a11y_001, new_severity=CRITICAL, updated_by=alex.dev@company.com, "
            "plan_id=plan_001, delivery_method=TICKETS, owner_email=alex.dev@company.com, "
            "item_id=item_001, fix_item_id=item_001, new_priority=HIGH, "
            "priority_reason=Critical finding requires immediate fix attention, "
            "audit_id=audit_002, violation_type=COLOR_CONTRAST, severity=CRITICAL, "
            "log_message=Audit findings severity management and fix plan coordination completed, "
            "log_level=INFO, log_component=audit_severity, "
            "comment_id=comment_006, comment_status=RESOLVED"
        ),
        actions=[
            Action(name="update_audit_finding_severity", kwargs={"finding_id": "finding_a11y_001", "new_severity": "CRITICAL", "updated_by": "alex.dev@company.com"}),
            Action(name="get_audit_findings_by_type", kwargs={"violation_type": "COLOR_CONTRAST", "severity": "CRITICAL"}),
            Action(name="get_fix_plan_items", kwargs={"plan_id": "plan_001"}),
            Action(name="update_fix_plan_status", kwargs={"plan_id": "plan_001", "new_status": "IN_PROGRESS", "delivery_method": "TICKETS", "owner_email": "alex.dev@company.com"}),
            Action(name="update_fix_item_priority", kwargs={"item_id": "item_001", "new_priority": "HIGH", "priority_reason": "Critical finding requires immediate fix attention", "updated_by": "alex.dev@company.com"}),
            Action(name="update_fix_item_status", kwargs={"fix_item_id": "item_001", "new_status": "IN_PROGRESS", "updated_by": "alex.dev@company.com"}),
            Action(name="add_terminal_log_entry", kwargs={"log_message": "Audit findings severity management and fix plan coordination completed", "log_level": "INFO", "component": "audit_severity", "user_email": "alex.dev@company.com"}),
            Action(name="get_audit_summary", kwargs={"audit_id": "audit_002"}),
            Action(name="update_figma_comment_status", kwargs={"comment_id": "comment_006", "new_status": "RESOLVED", "resolved_by": "alex.dev@company.com"})
        ],
        outputs=[
            "Audit findings severity management completed: finding_a11y_001 severity escalated to CRITICAL, CRITICAL severity COLOR_CONTRAST violations analyzed, fix plan items retrieved for plan_001, fix plan status updated to IN_PROGRESS with TICKETS delivery method, fix item_001 priority escalated to HIGH with critical finding attention, fix item status updated to IN_PROGRESS, comprehensive audit severity management workflow logging completed, audit_002 summary retrieved, and Figma comment comment_006 marked as RESOLVED."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_66",
        instruction=(
            "You are an accessibility compliance specialist responsible for audit findings coordination and fix item management across admin panel accessibility initiatives. "
            "Your primary responsibility involves accessibility audit coordination for audit_002, audit_004, and audit_005 where comprehensive findings analysis and fix item status updates require systematic processing. The workflow involves fix item lifecycle management following proper status progression. "
            "The accessibility compliance workflow centers on item_001 touch target verification with VERIFIED status achievement, item_004 font size compliance with APPLIED status and completion timestamp coordination, and item_002 contrast violation remediation with IN_PROGRESS status management. The fix implementation requires systematic status coordination and compliance verification. "
            "Your coordination efforts should ensure comprehensive audit findings analysis, proper fix item lifecycle management, and successful accessibility compliance tracking for stakeholder reporting and workflow completion."
        ),
        actions=[
            Action(name="get_audit_findings_summary", kwargs={"audit_id": "audit_002"}),
            Action(name="get_audit_findings_summary", kwargs={"audit_id": "audit_004"}),
            Action(name="get_audit_findings_summary", kwargs={"audit_id": "audit_005"}),
            Action(name="update_fix_item_status", kwargs={"fix_item_id": "item_001", "new_status": "VERIFIED"}),
            Action(name="update_fix_item_status", kwargs={"fix_item_id": "item_004", "new_status": "APPLIED", "completion_date": "2024-08-25T15:30:00Z"}),
            Action(name="update_fix_item_status", kwargs={"fix_item_id": "item_002", "new_status": "IN_PROGRESS"})
        ],
        outputs=[
            "Accessibility compliance workflow completed: audit findings analyzed for audit_002, audit_004, and audit_005, item_001 updated to VERIFIED status, item_004 updated to APPLIED status with completion date 2024-08-25T15:30:00Z, and item_002 updated to IN_PROGRESS status for continued accessibility improvements."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_67",
        instruction=(
            "You are a comprehensive release management coordinator responsible for coordinating end-to-end release workflows with system configuration management and Gmail communication coordination for design system components. "
            "Your primary responsibility involves release_003 status management and asset_003 export coordination requiring comprehensive status tracking, asset export summary verification, system configuration management, and Gmail thread coordination for release communication. The workflow integrates cross-team coordination, system configuration verification, and proper release lifecycle management with stakeholder communication. "
            "The enhanced release coordination workflow centers on release_003 PUBLISHED status achievement with comprehensive release notes documentation, asset_003 export status coordination with COMPLETED status and DLP scan verification, asset_003 export summary verification for documentation compliance, system configuration management for release standards, and thread_003 NORMAL priority management for release documentation coordination. "
            "Your coordination efforts should ensure comprehensive release lifecycle management with system integration, proper asset export status and summary coordination, system configuration verification for release standards, Gmail thread management for documentation coordination, and successful release deployment tracking for stakeholder reporting and workflow completion. "
            "Required constants: "
            "release_id=release_003, new_status=PUBLISHED, "
            "release_notes=Design system components release with accessibility improvements, "
            "updated_by=sarah.designer@company.com, asset_id=asset_003, export_status=COMPLETED, "
            "export_notes=Design system asset export completed with accessibility compliance, "
            "dlp_scan_status=CLEAN, owner_email=sarah.designer@company.com, "
            "created_after=2024-08-20T15:00:00Z, "
            "category=release_documentation_config, thread_id=thread_003, thread_priority=NORMAL, "
            "urgency_reason=Release documentation and compliance verification completed"
        ),
        actions=[
            Action(name="update_release_status", kwargs={"release_id": "release_003", "new_status": "PUBLISHED", "release_notes": "Design system components release with accessibility improvements", "updated_by": "sarah.designer@company.com"}),
            Action(name="update_asset_export_status", kwargs={"asset_id": "asset_003", "new_status": "COMPLETED", "notes": "Design system asset export completed with accessibility compliance", "dlp_scan_status": "CLEAN"}),
            Action(name="get_releases_by_owner", kwargs={"owner_email": "sarah.designer@company.com", "created_after": "2024-08-20T15:00:00Z"}),
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_003"}),
            Action(name="get_system_config_by_category", kwargs={"category": "release_documentation_config"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_003", "new_priority": "NORMAL", "urgency_reason": "Release documentation and compliance verification completed"})
        ],
        outputs=[
            "Enhanced release management workflow completed: release_003 status updated to PUBLISHED with design system release notes and sarah.designer@company.com assignment, asset_003 export status updated to COMPLETED with DLP scan verification and accessibility compliance, releases retrieved for sarah.designer@company.com owner tracking, comprehensive asset_003 export summary retrieved for release documentation and compliance verification, system configuration retrieved for release documentation standards and deployment compliance, and thread_003 priority updated to NORMAL for release documentation coordination completion."
        ]
    ),
    Task(
        annotator="0",
        user_id="user_68",
        instruction=(
            "You are a design system component audit specialist responsible for coordinating comprehensive design system audits and thread priority management for component workflows. "
            "Your primary responsibility involves audit_002 coordination for design system components requiring comprehensive status tracking and thread priority management for component review coordination. The workflow integrates with approval verification and thread escalation for design system release preparation. "
            "The design system coordination workflow centers on comprehensive audit tracking with sarah.designer@company.com oversight, thread_001 HIGH priority management for design system coordination, and detailed approval verification across design system workflows. "
            "Your coordination efforts should ensure seamless design system audit coordination through comprehensive status tracking, effective thread priority management for component reviews, and detailed approval verification for design system workflows with proper design team coordination and release preparation tracking. "
            "Key parameters: "
            "audit_002_id=audit_002, audit_002_status=COMPLETED, "
            "art_008_id=art_008, audit_type=A11Y, "
            "thread_001_id=thread_001, thread_008_id=thread_008, "
            "thread_001_priority=HIGH, thread_008_priority=NORMAL, "
            "thread_001_urgency=Design system component review requires immediate coordination, "
            "thread_008_urgency=Design system follow-up coordination completed, "
            "completion_notes=Design system component audit completed successfully, "
            "approval_002_id=approval_002, cycle_002_id=cycle_002, "
            "escalate_to=sarah.designer@company.com,design.system@company.com, "
            "release_owner=sarah.designer@company.com, release_start_date=2024-08-20T13:00:00Z"
        ),
        actions=[
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_002"}),
            Action(name="update_audit_report_status", kwargs={"audit_id": "audit_002", "new_status": "COMPLETED", "completion_notes": "Design system component audit completed successfully"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Design system component review requires immediate coordination", "escalate_to": ["sarah.designer@company.com", "design.system@company.com"]}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_008", "new_priority": "NORMAL", "urgency_reason": "Design system follow-up coordination completed"}),
            Action(name="get_review_approvals_summary", kwargs={"approval_id": "approval_002", "cycle_id": "cycle_002"}),
            Action(name="get_audits_by_status", kwargs={"artifact_id": "art_008", "audit_type": "A11Y"}),
            Action(name="get_releases_by_owner", kwargs={"owner_email": "sarah.designer@company.com", "created_after": "2024-08-20T13:00:00Z"}),
            Action(name="get_audit_findings_summary", kwargs={"audit_id": "audit_002", "include_resolved": True}),
            Action(name="get_system_config_by_category", kwargs={"category": "design_system_audit_config"}),
            Action(name="update_audit_type", kwargs={"audit_id": "audit_002", "new_audit_type": "COMBINED_DS_A11Y", "updated_by": "sarah.designer@company.com"})
        ],
        outputs=[
            "audit_002_verified:audit_002",
            "audit_status_updated:COMPLETED",
            "thread_001_updated:HIGH",
            "thread_008_updated:NORMAL",
            "approval_summary_retrieved:approval_002",
            "audit_artifacts_retrieved:art_008",
            "releases_retrieved:sarah.designer@company.com",
            "audit_findings_retrieved:audit_002",
            "system_config_retrieved:design_system_audit_config",
            "audit_type_updated:COMBINED_DS_A11Y"
        ]
    ),

    Task(
        annotator="0",
        user_id="user_69",
        instruction=(
            "You are a design system component audit specialist responsible for coordinating comprehensive design system audits and thread priority management for component workflows. "
            "Your primary responsibility involves audit_002 coordination for design system components requiring comprehensive status tracking and thread priority management for component review coordination. The workflow integrates with approval verification and thread escalation for design system release preparation. "
            "The design system coordination workflow centers on comprehensive audit tracking with sarah.designer@company.com oversight, thread_001 HIGH priority management for design system coordination, and detailed approval verification across design system workflows. "
            "Your coordination efforts should ensure seamless design system audit coordination through comprehensive status tracking, effective thread priority management for component reviews, and detailed approval verification for design system workflows with proper design team coordination and release preparation tracking. "
            "Key parameters: "
            "audit_002_id=audit_002, audit_002_status=COMPLETED, "
            "art_008_id=art_008, audit_type=A11Y, "
            "thread_001_id=thread_001, thread_008_id=thread_008, "
            "thread_001_priority=HIGH, thread_008_priority=NORMAL, "
            "thread_001_urgency=Design system component review requires immediate coordination, "
            "thread_008_urgency=Design system follow-up coordination completed, "
            "completion_notes=Design system component audit completed successfully, "
            "approval_002_id=approval_002, cycle_002_id=cycle_002, "
            "escalate_to=sarah.designer@company.com,design.system@company.com, "
            "release_owner=sarah.designer@company.com, release_start_date=2024-08-20T13:00:00Z"
        ),
        actions=[
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_002"}),
            Action(name="update_audit_report_status", kwargs={"audit_id": "audit_002", "new_status": "COMPLETED", "completion_notes": "Design system component audit completed successfully"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Design system component review requires immediate coordination", "escalate_to": ["sarah.designer@company.com", "design.system@company.com"]}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_008", "new_priority": "NORMAL", "urgency_reason": "Design system follow-up coordination completed"}),
            Action(name="get_review_approvals_summary", kwargs={"approval_id": "approval_002", "cycle_id": "cycle_002"}),
            Action(name="get_audits_by_status", kwargs={"artifact_id": "art_008", "audit_type": "A11Y"}),
            Action(name="get_releases_by_owner", kwargs={"owner_email": "sarah.designer@company.com", "created_after": "2024-08-20T13:00:00Z"}),
            Action(name="get_audit_findings_summary", kwargs={"audit_id": "audit_002", "include_resolved": True})
        ],
        outputs=[
            "audit_002_verified:audit_002",
            "audit_status_updated:COMPLETED",
            "thread_001_updated:HIGH",
            "thread_008_updated:NORMAL",
            "approval_summary_retrieved:approval_002",
            "audit_artifacts_retrieved:art_008",
            "releases_retrieved:sarah.designer@company.com",
            "audit_findings_retrieved:audit_002"
        ]
    ),

    Task(
        annotator="0",
        user_id="user_70",
        instruction=(
            "You are an audit report management specialist responsible for coordinating the end-to-end audit lifecycle for design system components and accessibility compliance. "
            "Your primary responsibility involves managing audit_001 for artifact art_001 (Homepage Hero Section) which requires comprehensive status tracking from COMPLETED to final report generation. The workflow integrates with audit_002 for accessibility review of art_008 admin panel components requiring status coordination. "
            "The audit management workflow centers on thread_001 priority escalation to HIGH priority for design review coordination involving sarah.designer@company.com oversight, URGENT priority level escalation for comprehensive design review tracking, and escalation_reason 'Critical audit findings require immediate design team attention and stakeholder review'. The priority management requires comprehensive Gmail thread coordination and detailed audit status documentation. "
            "Your coordination efforts should ensure seamless audit report generation through proper status management, effective priority escalation for design review threads, and comprehensive audit findings tracking for stakeholder reporting. "
            "Key parameters: audit_id=audit_001, new_status=COMPLETED, report_asset_id=asset_001, completion_notes=Design system audit completed with recommendations, "
            "thread_001_priority=HIGH, thread_002_priority=NORMAL, thread_001_urgency=Critical audit findings require immediate design team attention, thread_002_urgency=Secondary audit review completed, "
            "escalate_to=sarah.designer@company.com,mike.ux@company.com, audit_type=COMBINED_DS_A11Y, created_after=2024-08-20T15:00:00Z, audit_date_filter=2024-08-18T00:00:00Z, "
            "thread_ids=thread_001,thread_002, artifact_ids=art_001,art_008"
        ),
        actions=[
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_001"}),
            Action(name="update_audit_report_status", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed with recommendations"}),
            Action(name="get_audits_by_status", kwargs={"status": "COMPLETED", "audit_type": "COMBINED_DS_A11Y"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical audit findings require immediate design team attention", "escalate_to": ["sarah.designer@company.com", "mike.ux@company.com"]}),
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_002"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Secondary audit review completed"}),
            Action(name="get_audits_by_status", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"}),
            Action(name="add_terminal_log_entry", kwargs={"log_message": "Audit management workflow completed for audit_001 and audit_002 with critical findings escalation", "log_level": "INFO", "component": "audit_management", "user_email": "sarah.designer@company.com"}),
            Action(name="get_releases_by_owner", kwargs={"owner_email": "sarah.designer@company.com", "created_after": "2024-08-20T15:00:00Z"})
        ],
        outputs=[
            "Audit management workflow completed: audit_001 status updated to COMPLETED with report asset_001 association and completion notes, thread_001 priority escalated to HIGH with critical findings urgency and stakeholder escalation to design team, comprehensive audit verification completed for A11Y audit type, releases retrieved for sarah.designer@company.com owner after 2024-08-20T15:00:00Z, and terminal log entry added for audit management workflow tracking."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_71",
        instruction=(
            "You are a mobile component audit integration specialist responsible for coordinating comprehensive mobile audit workflows and release management for mobile application components. "
            "Your primary responsibility involves audit_002 management for mobile components requiring comprehensive status tracking and thread_002 CRITICAL priority escalation for mobile dashboard release coordination. The workflow integrates with approval verification for mobile workflows and comprehensive audit tracking for mobile application readiness. "
            "The mobile integration workflow centers on comprehensive audit coordination with mike.ux@company.com oversight, thread_007 HIGH priority management for mobile app release coordination, escalation_reason \"Mobile application release requires immediate audit integration and cross-team coordination\", and detailed approval tracking for mobile component workflows with release preparation focus. "
            "Your coordination efforts should ensure seamless mobile audit integration through comprehensive status coordination, effective priority escalation for mobile release threads, and detailed approval verification for mobile workflows with proper UX team coordination and release readiness tracking. "
            "Key parameters: "
            "audit_002_id=audit_002, audit_002_status=COMPLETED, "
            "thread_002_id=thread_002, thread_007_id=thread_007, "
            "thread_002_priority=CRITICAL, thread_007_priority=HIGH, "
            "thread_002_urgency=Mobile application release requires immediate coordination, "
            "thread_007_urgency=Mobile app release coordination support required, "
            "completion_notes=Mobile component audit completed with accessibility integration, "
            "approval_002_id=approval_002, cycle_002_id=cycle_002, "
            "audit_type=A11Y, "
            "created_after_date=2024-08-19T12:00:00Z, "
            "escalate_to=mike.ux@company.com,mobile.team@company.com"
        ),
        actions=[
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_002"}),
            Action(name="update_audit_report_status", kwargs={"audit_id": "audit_002", "new_status": "COMPLETED", "completion_notes": "Mobile component audit completed with accessibility integration"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_002", "new_priority": "CRITICAL", "urgency_reason": "Mobile application release requires immediate coordination", "escalate_to": ["mike.ux@company.com", "mobile.team@company.com"]}),
            Action(name="get_review_approvals_summary", kwargs={"approval_id": "approval_002", "cycle_id": "cycle_002"}),
            Action(name="get_audits_by_status", kwargs={"created_after": "2024-08-19T12:00:00Z", "audit_type": "A11Y"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_007", "new_priority": "HIGH", "urgency_reason": "Mobile app release coordination support required"})
        ],
        outputs=[
            "Mobile component audit integration completed: audit_002 status verified for mobile component tracking, audit_002 status updated to COMPLETED with mobile accessibility integration notes, thread_002 priority escalated to CRITICAL for mobile release with UX team and mobile team escalation, approval_002 verification completed for cycle_002 mobile workflow coordination, comprehensive A11Y audit verification completed for mobile components since dashboard creation, and thread_007 priority elevated to HIGH for mobile app release coordination support."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_72",
        instruction=(
            "You are an audit report management specialist responsible for coordinating the end-to-end audit lifecycle for design system components and accessibility compliance. "
            "Your primary responsibility involves managing audit_001 for artifact art_001 (Homepage Hero Section) which requires comprehensive status tracking from COMPLETED to final report generation. The workflow integrates with audit_002 for accessibility review of art_008 admin panel components requiring status coordination. "
            "The audit management workflow centers on thread_001 priority escalation to HIGH priority for design review coordination involving sarah.designer@company.com oversight, URGENT priority level escalation for comprehensive design review tracking, and escalation_reason 'Critical audit findings require immediate design team attention and stakeholder review'. The priority management requires comprehensive Gmail thread coordination and detailed audit status documentation. "
            "Your coordination efforts should ensure seamless audit report generation through proper status management, effective priority escalation for design review threads, comprehensive audit findings tracking for stakeholder reporting, and successful audit lifecycle completion with proper report asset associations. "
            "Key parameters: audit_id=audit_001, new_status=COMPLETED, report_asset_id=asset_001, completion_notes=Design system audit completed with recommendations, "
            "thread_001_priority=HIGH, thread_002_priority=NORMAL, thread_001_urgency=Critical audit findings require immediate design team attention, thread_002_urgency=Secondary audit review completed, "
            "escalate_to=sarah.designer@company.com,mike.ux@company.com, audit_type=COMBINED_DS_A11Y, created_after=2024-08-20T15:00:00Z, audit_date_filter=2024-08-18T00:00:00Z, "
            "thread_ids=thread_001,thread_002, artifact_ids=art_001,art_008"
        ),
        actions=[
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_001"}),
            Action(name="update_audit_report_status", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed with recommendations"}),
            Action(name="get_audits_by_status", kwargs={"status": "COMPLETED", "audit_type": "COMBINED_DS_A11Y"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical audit findings require immediate design team attention", "escalate_to": ["sarah.designer@company.com", "mike.ux@company.com"]}),
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_002"}),
            Action(name="get_audits_by_status", kwargs={"artifact_id": "art_001", "created_after": "2024-08-20T15:00:00Z"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Secondary audit review completed"}),
            Action(name="get_audits_by_status", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"}),
            Action(name="add_terminal_log_entry", kwargs={"log_message": "Audit management workflow completed for audit_001 and audit_002 with comprehensive status tracking", "log_level": "INFO", "component": "audit_management", "user_email": "sarah.designer@company.com"})
        ],
        outputs=[
            "Audit management workflow completed: audit_001 status updated to COMPLETED with report asset_001 association and completion notes, thread_001 priority escalated to HIGH with critical findings urgency and stakeholder escalation to design team, secondary thread_002 priority normalized, comprehensive audit status verification completed across all COMBINED_DS_A11Y and A11Y audit types for stakeholder reporting, and terminal log entry added for audit management workflow tracking."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_73",
        instruction=(
            "You are an audit report management specialist responsible for coordinating the end-to-end audit lifecycle for design system components and accessibility compliance. "
            "Your primary responsibility involves managing audit_001 for artifact art_001 (Homepage Hero Section) which requires comprehensive status tracking from COMPLETED to final report generation. The workflow integrates with audit_002 for accessibility review of art_008 admin panel components requiring status coordination. "
            "The audit management workflow centers on thread_001 priority escalation to HIGH priority for design review coordination involving sarah.designer@company.com oversight, URGENT priority level escalation for comprehensive design review tracking, and escalation_reason 'Critical audit findings require immediate design team attention and stakeholder review'. The priority management requires comprehensive Gmail thread coordination and detailed audit status documentation. "
            "Your coordination efforts should ensure seamless audit report generation through proper status management, effective priority escalation for design review threads, comprehensive audit findings tracking for stakeholder reporting, and successful audit lifecycle completion with proper report asset associations. "
            "Key parameters: audit_id=audit_001, new_status=COMPLETED, report_asset_id=asset_001, completion_notes=Design system audit completed with recommendations, "
            "thread_001_priority=HIGH, thread_002_priority=NORMAL, thread_001_urgency=Critical audit findings require immediate design team attention, thread_002_urgency=Secondary audit review completed, "
            "escalate_to=sarah.designer@company.com,mike.ux@company.com, audit_type=COMBINED_DS_A11Y, created_after=2024-08-20T15:00:00Z, audit_date_filter=2024-08-18T00:00:00Z, "
            "thread_ids=thread_001,thread_002, artifact_ids=art_001,art_008"
        ),
        actions=[
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_001"}),
            Action(name="update_audit_report_status", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed with recommendations"}),
            Action(name="get_audits_by_status", kwargs={"status": "COMPLETED", "audit_type": "COMBINED_DS_A11Y"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical audit findings require immediate design team attention", "escalate_to": ["sarah.designer@company.com", "mike.ux@company.com"]}),
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_002"}),
            Action(name="get_audits_by_status", kwargs={"artifact_id": "art_001", "created_after": "2024-08-20T15:00:00Z"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Secondary audit review completed"}),
            Action(name="get_audits_by_status", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"}),
            Action(name="get_system_config_by_category", kwargs={"category": "audit_config"})
        ],
        outputs=[
            "Audit management workflow completed: audit_001 status updated to COMPLETED with report asset_001 association and completion notes, thread_001 priority escalated to HIGH with critical findings urgency and stakeholder escalation to design team, secondary thread_002 priority normalized, comprehensive audit status verification completed across all COMBINED_DS_A11Y and A11Y audit types for stakeholder reporting, and system configuration retrieved for audit_config category."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_74",
        instruction=(
            "You are an audit compliance specialist responsible for coordinating multi-audit status management and comprehensive compliance reporting workflow. "
            "Your primary responsibility involves managing audit_005 for artifact art_007 (Dashboard Components) requiring status transition from COMPLETED to final compliance verification with comprehensive audit report generation. The workflow integrates audit_006 design system mapping audit requiring status coordination and thread_005 communication escalation. "
            "The compliance reporting workflow centers on audit status management for audit_005 with COMBINED_DS_A11Y audit type coordination, managing audit_006 DS_MAPPING audit completion verification, and coordinating thread_005 priority escalation to NORMAL priority with mike.dev@company.com oversight for comprehensive compliance tracking. "
            "Your coordination efforts should ensure seamless multi-audit compliance reporting through proper audit status verification, effective compliance documentation management, and comprehensive audit type coordination for stakeholder compliance reporting. "
            "Required constants: primary_audit_id=audit_005, secondary_audit_id=audit_006, artifact_id=art_007, "
            "thread_id=thread_005, assignee_email=mike.dev@company.com, priority_level=NORMAL, "
            "audit_type=COMBINED_DS_A11Y, secondary_audit_type=DS_MAPPING, report_asset_id=asset_006, "
            "status=COMPLETED, escalation_reason=Multi-audit compliance verification requires development team coordination, "
            "created_after=2024-08-22T11:00:00Z, completion_notes=Multi-audit compliance verification completed, "
            "log_message=Multi-audit compliance reporting workflow completed for audit_005 and audit_006, "
            "log_level=INFO, component=compliance_reporting, "
            "user_email=mike.dev@company.com"
        ),
        actions=[
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_005", "status": "COMPLETED"}),
            Action(name="update_audit_report_status", kwargs={"audit_id": "audit_005", "new_status": "COMPLETED", "report_asset_id": "asset_006", "completion_notes": "Multi-audit compliance verification completed"}),
            Action(name="get_audits_by_status", kwargs={"audit_type": "COMBINED_DS_A11Y", "artifact_id": "art_007"}),
            Action(name="get_audit_summary", kwargs={"audit_id": "audit_005"}),
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_006", "audit_type": "DS_MAPPING"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_005", "new_priority": "NORMAL", "urgency_reason": "Multi-audit compliance verification requires development team coordination", "escalate_to": ["mike.dev@company.com"]}),
            Action(name="get_audit_report_summary", kwargs={"audit_id": "audit_006", "audit_type": "DS_MAPPING"}),
            Action(name="add_terminal_log_entry", kwargs={"log_message": "Multi-audit compliance reporting workflow completed for audit_005 and audit_006", "log_level": "INFO", "component": "compliance_reporting", "user_email": "mike.dev@company.com"})
        ],
        outputs=[
            "Multi-audit compliance reporting completed: audit_005 status verified as COMPLETED for art_007 dashboard components with comprehensive compliance verification, audit report status updated with asset_006 association and completion notes, COMBINED_DS_A11Y audit type verified for comprehensive compliance tracking, audit_005 summary generated for compliance documentation, audit_006 DS_MAPPING audit verification completed for design system compliance, thread_005 priority escalated to NORMAL with development team coordination and mike.dev@company.com stakeholder notification, DS_MAPPING audit report summary generated for compliance verification, and comprehensive compliance reporting workflow logging completed."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_75",
        instruction=(
            "You are a fix plan delivery coordinator responsible for managing comprehensive fix plan delivery workflows and release version coordination. "
            "Your task is to coordinate the delivery of fix plans and ensure proper release version management with asset export verification. "
            "Focus on managing the fix plan delivery workflow from DRAFTED to DELIVERED status, including release version updates and export coordination. "
            "Coordinate with development teams through appropriate communication channels to ensure all fix deliverables are properly tracked. "
            "Required constants: "
            "plan_id=plan_002, new_status=DELIVERED, delivery_method=TICKETS, "
            "owner_email=sarah.designer@company.com, release_id=release_001, version_id=v1.4.0, "
            "release_name=Design System v1.4.0 - Fix Implementation Updates, thread_id=thread_006, "
            "asset_id=asset_001, export_status=COMPLETED, export_notes=Fix plan delivery assets exported successfully, "
            "dlp_scan_status=CLEAN, created_after=2024-08-22T18:00:00Z, "
            "log_message=Fix plan delivery coordination completed for plan_002 with release version v1.4.0, "
            "log_level=INFO, component=fix_delivery, user_email=sarah.designer@company.com"
        ),
        actions=[
            Action(name="get_fix_plan_items", kwargs={"plan_id": "plan_002"}),
            Action(name="update_fix_plan_status", kwargs={"plan_id": "plan_002", "new_status": "DELIVERED", "delivery_method": "TICKETS", "owner_email": "sarah.designer@company.com"}),
            Action(name="get_releases_by_owner", kwargs={"owner_email": "sarah.designer@company.com", "created_after": "2024-08-22T18:00:00Z"}),
            Action(name="update_release_version", kwargs={"release_id": "release_001", "version_id": "v1.4.0", "release_name": "Design System v1.4.0 - Fix Implementation Updates", "owner_email": "sarah.designer@company.com", "thread_id": "thread_006"}),
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_001"}),
            Action(name="update_asset_export_status", kwargs={"asset_id": "asset_001", "new_status": "COMPLETED", "notes": "Fix plan delivery assets exported successfully", "dlp_scan_status": "CLEAN"}),
            Action(name="add_terminal_log_entry", kwargs={"log_message": "Fix plan delivery coordination completed for plan_002 with release version v1.4.0", "log_level": "INFO", "component": "fix_delivery", "user_email": "sarah.designer@company.com"})
        ],
        outputs=[
            "Fix plan delivery coordination completed for plan_002: fix plan status updated from DRAFTED to DELIVERED with TICKETS delivery method, Sarah Designer releases verified for fix coordination since August 22nd, release version updated to v1.4.0 with fix implementation updates and thread_006 coordination, asset export summary verified for asset_001, export status updated to COMPLETED with successful delivery notes and CLEAN DLP scan, and comprehensive fix delivery workflow logging completed."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_76",
        instruction=(
            "You are a review cycle SLA management specialist responsible for coordinating review cycle escalation and integrated audit workflow management. "
            "Your task is to manage review cycle SLA coordination with audit status management and ensure proper escalation tracking. "
            "Focus on managing review cycle status transitions from NEEDS_REVIEW to ESCALATED, including audit status coordination and comprehensive logging. "
            "Coordinate with review teams through appropriate channels to ensure all SLA breaches and audit workflows are properly synchronized. "
            "Required constants: "
            "cycle_id=cycle_001, artifact_id=art_001, new_status=ESCALATED, "
            "audit_id=audit_001, audit_status=IN_PROGRESS, updated_by=sarah.designer@company.com, "
            "thread_id=thread_001, priority_level=HIGH, urgency_reason=SLA breach requires immediate escalation, "
            "escalate_to=sarah.designer@company.com, "
            "log_level=WARNING, component=review_sla, after_timestamp=2024-08-20T15:00:00Z, "
            "message_pattern=escalation, log_message=Review cycle SLA escalation completed with audit integration"
        ),
        actions=[
            Action(name="get_review_approvals_summary", kwargs={"cycle_id": "cycle_001"}),
            Action(name="update_review_cycle_status", kwargs={"cycle_id": "cycle_001", "new_status": "ESCALATED", "reviewer_email": "sarah.designer@company.com", "completion_notes": "SLA breach requires immediate escalation"}),
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_001"}),
            Action(name="update_audit_status", kwargs={"audit_id": "audit_001", "new_status": "IN_PROGRESS", "updated_by": "sarah.designer@company.com"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "SLA breach requires immediate escalation"}),
            Action(name="add_terminal_log_entry", kwargs={"log_message": "Review cycle SLA escalation completed with audit integration", "log_level": "WARNING", "component": "review_sla", "user_email": "sarah.designer@company.com"}),
            Action(name="get_filtered_log_entries", kwargs={"log_level": "WARNING", "component": "review_sla", "after_timestamp": "2024-08-20T15:00:00Z", "message_pattern": "escalation"})
        ],
        outputs=[
            "Review cycle SLA management completed for cycle_001: review cycle approvals verified for SLA coordination, review cycle status updated to ESCALATED with Sarah Designer oversight and SLA breach escalation notes, audit_001 status verified for coordination workflow, audit status updated to IN_PROGRESS with Sarah Designer assignment, Gmail thread priority escalated to HIGH with SLA breach urgency and stakeholder escalation, comprehensive SLA escalation logging added with WARNING level review_sla component tracking, and filtered escalation logs retrieved for WARNING level pattern matching since August 20th."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_77",
        instruction=(
            "You are an audit report management specialist responsible for coordinating the end-to-end audit lifecycle for design system components and accessibility compliance. "
            "Your task is to manage the audit completion process and ensure proper status tracking for design system components. "
            "Focus on coordinating the audit workflow from IN_PROGRESS to COMPLETED status, including report generation and stakeholder communication. "
            "Required constants: "
            "audit_id=audit_001, new_status=COMPLETED, report_asset_id=asset_001, "
            "completion_notes=Design system audit completed with recommendations, "
            "thread_001_priority=HIGH, thread_002_priority=NORMAL, "
            "thread_001_urgency=Critical audit findings require immediate design team attention, "
            "escalate_to=sarah.designer@company.com,mike.ux@company.com, "
            "audit_type=COMBINED_DS_A11Y, created_after=2024-08-20T15:00:00Z, "
            "audit_date_filter=2024-08-18T00:00:00Z, thread_ids=thread_001,thread_002, "
            "artifact_ids=art_001,art_008"
        ),
        actions=[
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_001"}),
            Action(name="update_audit_report_status", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed with recommendations"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical audit findings require immediate design team attention", "escalate_to": ["sarah.designer@company.com", "mike.ux@company.com"]}),
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_002"}),
            Action(name="update_audit_report_status", kwargs={"audit_id": "audit_002", "new_status": "COMPLETED", "report_asset_id": "asset_007"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Secondary audit review completed"}),
            Action(name="get_audits_by_status", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"}),
            Action(name="add_terminal_log_entry", kwargs={"log_message": "Audit report management workflow completed for audit_001 and audit_002 with comprehensive status tracking", "log_level": "INFO", "component": "audit_management", "user_email": "sarah.designer@company.com"})
        ],
        outputs=[
            "Audit management workflow completed: audit_001 status updated to COMPLETED with report asset_001 association and completion notes, thread_001 priority escalated to HIGH with critical findings urgency and stakeholder escalation to design team, audit_002 status updated to COMPLETED with report asset_007, comprehensive audit verification completed for A11Y audit type, and terminal log entry added for audit report management workflow tracking."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_78",
        instruction=(
            "You are a mobile component audit integration specialist responsible for coordinating comprehensive mobile audit workflows and release management for mobile application components. "
            "Your primary responsibility involves audit_002 management for mobile components requiring comprehensive status tracking and thread_002 CRITICAL priority escalation for mobile dashboard release coordination. The workflow integrates with approval verification for mobile workflows and comprehensive audit tracking for mobile application readiness. "
            "The mobile integration workflow centers on comprehensive audit coordination with mike.ux@company.com oversight, thread_007 HIGH priority management for mobile app release coordination, and detailed approval tracking for mobile component workflows with release preparation focus. "
            "Your coordination efforts should ensure seamless mobile audit integration through comprehensive status coordination, effective priority escalation for mobile release threads, and detailed approval verification for mobile workflows with proper UX team coordination and release readiness tracking. "
            "Required constants: "
            "audit_id=audit_002, "
            "thread_002_id=thread_002, thread_007_id=thread_007, "
            "thread_002_priority=CRITICAL, thread_007_priority=HIGH, "
            "thread_002_urgency=Mobile application release requires immediate coordination, "
            "thread_007_urgency=Mobile app release coordination support required, "
            "completion_notes=Mobile component audit completed with accessibility integration, "
            "approval_002_id=approval_002, cycle_002_id=cycle_002, "
            "audit_type=A11Y, "
            "created_after_date=2024-08-19T12:00:00Z, "
            "escalate_to=mike.ux@company.com,mobile.team@company.com, "
            "owner_email=mike.ux@company.com"
        ),
        actions=[
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_002"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_002", "new_priority": "CRITICAL", "urgency_reason": "Mobile application release requires immediate coordination", "escalate_to": ["mike.ux@company.com", "mobile.team@company.com"]}),
            Action(name="get_review_approvals_summary", kwargs={"approval_id": "approval_002", "cycle_id": "cycle_002"}),
            Action(name="get_audits_by_status", kwargs={"created_after": "2024-08-19T12:00:00Z", "audit_type": "A11Y"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_007", "new_priority": "HIGH", "urgency_reason": "Mobile app release coordination support required"}),
            Action(name="get_releases_by_owner", kwargs={"owner_email": "mike.ux@company.com", "created_after": "2024-08-19T12:00:00Z"})
        ],
        outputs=[
            "Mobile component audit integration completed: audit_002 status verified for mobile component tracking, thread_002 priority escalated to CRITICAL for mobile release with UX team and mobile team escalation, approval_002 verification completed for cycle_002 mobile workflow coordination, comprehensive A11Y audit verification completed for mobile components since dashboard creation, thread_007 priority elevated to HIGH for mobile app release coordination support, and releases by Mike UX retrieved for mobile audit coordination release tracking since dashboard creation."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_79",
        instruction=(
            "You are a Figma comment and fix item resolution specialist responsible for managing accessibility feedback and tracking related fix items. "
            "Your task is to coordinate accessibility improvements, track comment resolution, manage fix items, and ensure proper communication across teams. "
            "Focus on managing comment status updates, tracking fix item progress, assigning tasks, and verifying asset exports. "
            "Required constants: "
            "artifact_id=art_008, asset_id=asset_007, comment_ids=comment_006,comment_009, "
            "fix_item_id=item_016, new_status=IN_PROGRESS, assignee_id=dev_team@company.com, "
            "thread_id=thread_004, priority_level=HIGH, "
            "comment_assignee_1=mike.ux@company.com, comment_assignee_2=sarah.designer@company.com, "
            "resolution_notes=Accessibility improvements in progress - adding ARIA labels and keyboard navigation support, "
            "implementation_notes=Starting work on accessibility improvements for admin panel header"
        ),
        actions=[
            Action(name="get_figma_comments_by_artifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_007"}),
            Action(name="update_figma_comment_status", kwargs={"comment_id": "comment_006", "new_status": "IN_PROGRESS", "resolution_notes": "Accessibility improvements in progress - adding ARIA labels and keyboard navigation support", "assignee_email": "mike.ux@company.com", "priority_level": "HIGH"}),
            Action(name="get_gmail_threads_by_labels", kwargs={"thread_id": "thread_004"}),
            Action(name="update_fix_item_status", kwargs={"fix_item_id": "item_016", "new_status": "IN_PROGRESS", "assignee_id": "dev_team@company.com", "implementation_notes": "Starting work on accessibility improvements for admin panel header"}),
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_007"}),
            Action(name="update_figma_comment_status", kwargs={"comment_id": "comment_009", "new_status": "RESOLVED", "assignee_email": "sarah.designer@company.com"})
        ],
        outputs=[
            "figma_comments_retrieved:art_008:unresolved",
            "asset_export_verified:asset_007",
            "comment_status_updated:comment_006:IN_PROGRESS:mike.ux@company.com:HIGH",
            "gmail_thread_retrieved:thread_004",
            "fix_item_updated:item_016:IN_PROGRESS:dev_team@company.com",
            "asset_export_summary_retrieved:asset_007",
            "comment_status_updated:comment_009:RESOLVED:sarah.designer@company.com"
        ]
    ),

    Task(
        annotator="0",
        user_id="user_80",
        instruction=(
            "You are a comprehensive release management coordinator responsible for coordinating end-to-end release workflows with audit integration and Gmail communication management for design system components. "
            "Your task is to manage release status updates, asset export coordination, system configuration verification, audit compliance verification, and Gmail thread management for design system releases. "
            "Focus on ensuring proper release lifecycle management with audit integration, asset export status tracking, system configuration management, and Gmail communication coordination for release workflows. "
            "Coordinate with design and development teams through appropriate channels to ensure all release workflows are properly executed, documented, and communicated with stakeholder updates. "
            "Required constants: "
            "release_id=release_003, new_status=PUBLISHED, release_notes=Design system components release with accessibility improvements, "
            "updated_by=sarah.designer@company.com, asset_id=asset_003, export_status=COMPLETED, "
            "export_notes=Design system asset export completed with accessibility compliance, dlp_scan_status=CLEAN, "
            "owner_email=sarah.designer@company.com, created_after=2024-08-20T15:00:00Z, category=release_management_config, "
            "log_message=Release management workflow completed with system configuration, log_level=INFO, component=release_management, "
            "audit_id=audit_002, thread_id=thread_002, thread_priority=NORMAL, "
            "urgency_reason=Release configuration updates completed successfully"
        ),
        actions=[
            Action(name="update_release_status", kwargs={"release_id": "release_003", "new_status": "PUBLISHED", "release_notes": "Design system components release with accessibility improvements", "updated_by": "sarah.designer@company.com"}),
            Action(name="update_asset_export_status", kwargs={"asset_id": "asset_003", "new_status": "COMPLETED", "notes": "Design system asset export completed with accessibility compliance", "dlp_scan_status": "CLEAN"}),
            Action(name="get_releases_by_owner", kwargs={"owner_email": "sarah.designer@company.com", "created_after": "2024-08-20T15:00:00Z"}),
            Action(name="get_system_config_by_category", kwargs={"category": "release_management_config"}),
            Action(name="get_audit_summary", kwargs={"audit_id": "audit_002"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Release configuration updates completed successfully"})
        ],
        outputs=[
            "Enhanced release management workflow completed: release_003 status updated to PUBLISHED with design system release notes and sarah.designer@company.com assignment, asset_003 export status updated to COMPLETED with DLP scan verification and accessibility compliance, releases retrieved for sarah.designer@company.com owner tracking, system configuration retrieved for release management settings and deployment standards, comprehensive audit_002 summary retrieved for release compliance verification, and thread_002 priority updated to NORMAL for release configuration completion coordination."
        ]
    ),
    Task(
        annotator="0",
        user_id="user_81",
        instruction=(
            "You are a design system component audit specialist responsible for coordinating comprehensive design system audits and thread priority management for component workflows. "
            "Your primary responsibility involves audit_002 coordination for design system components requiring comprehensive status tracking and thread priority management for component review coordination. The workflow integrates with approval verification and thread escalation for design system release preparation. "
            "The design system coordination workflow centers on comprehensive audit tracking with sarah.designer@company.com oversight, thread_001 HIGH priority management for design system coordination, and detailed approval verification across design system workflows. "
            "Your coordination efforts should ensure seamless design system audit coordination through comprehensive status tracking, effective thread priority management for component reviews, and detailed approval verification for design system workflows with proper design team coordination and release preparation tracking. "
            "Key parameters: "
            "audit_002_id=audit_002, audit_002_status=COMPLETED, "
            "art_008_id=art_008, audit_type=A11Y, "
            "thread_001_id=thread_001, thread_008_id=thread_008, "
            "thread_001_priority=HIGH, thread_008_priority=NORMAL, "
            "thread_001_urgency=Design system component review requires immediate coordination, "
            "thread_008_urgency=Design system follow-up coordination completed, "
            "completion_notes=Design system component audit completed successfully, "
            "approval_002_id=approval_002, cycle_002_id=cycle_002, "
            "escalate_to=sarah.designer@company.com,design.system@company.com, "
            "release_owner=sarah.designer@company.com, release_start_date=2024-08-20T13:00:00Z"
        ),
        actions=[
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_002"}),
            Action(name="update_audit_report_status", kwargs={"audit_id": "audit_002", "new_status": "COMPLETED", "completion_notes": "Design system component audit completed successfully"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Design system component review requires immediate coordination", "escalate_to": ["sarah.designer@company.com", "design.system@company.com"]}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_008", "new_priority": "NORMAL", "urgency_reason": "Design system follow-up coordination completed"}),
            Action(name="get_review_approvals_summary", kwargs={"approval_id": "approval_002", "cycle_id": "cycle_002"}),
            Action(name="get_audits_by_status", kwargs={"artifact_id": "art_008", "audit_type": "A11Y"}),
            Action(name="get_releases_by_owner", kwargs={"owner_email": "sarah.designer@company.com", "created_after": "2024-08-20T13:00:00Z"}),
            Action(name="get_audit_findings_summary", kwargs={"audit_id": "audit_002", "include_resolved": True}),
            Action(name="get_system_config_by_category", kwargs={"category": "design_system_audit_config"})
        ],
        outputs=[
            "audit_002_verified:audit_002",
            "audit_status_updated:COMPLETED",
            "thread_001_updated:HIGH",
            "thread_008_updated:NORMAL",
            "approval_summary_retrieved:approval_002",
            "audit_artifacts_retrieved:art_008",
            "releases_retrieved:sarah.designer@company.com",
            "audit_findings_retrieved:audit_002",
            "system_config_retrieved:design_system_audit_config"
        ]
    ),

    Task(
        annotator="0",
        user_id="user_82",
        instruction=(
            "You are an audit report management specialist responsible for coordinating the end-to-end audit lifecycle for design system components and accessibility compliance. "
            "Your primary responsibility involves managing audit_001 for artifact art_001 (Homepage Hero Section) which requires comprehensive status tracking from COMPLETED to final report generation. The workflow integrates with audit_002 for accessibility review of art_008 admin panel components requiring status coordination. "
            "The audit management workflow centers on thread_001 priority escalation to HIGH priority for design review coordination involving sarah.designer@company.com oversight, URGENT priority level escalation for comprehensive design review tracking, and escalation_reason 'Critical audit findings require immediate design team attention and stakeholder review'. The priority management requires comprehensive Gmail thread coordination and detailed audit status documentation. "
            "Your coordination efforts should ensure seamless audit report generation through proper status management, effective priority escalation for design review threads, comprehensive audit findings tracking for stakeholder reporting, and successful audit lifecycle completion with proper report asset associations. "
            "Key parameters: audit_id=audit_001, new_status=COMPLETED, report_asset_id=asset_001, completion_notes=Design system audit completed with recommendations, "
            "thread_001_priority=HIGH, thread_002_priority=NORMAL, thread_001_urgency=Critical audit findings require immediate design team attention, thread_002_urgency=Secondary audit review completed, "
            "escalate_to=sarah.designer@company.com,mike.ux@company.com, audit_type=COMBINED_DS_A11Y, created_after=2024-08-20T15:00:00Z, audit_date_filter=2024-08-18T00:00:00Z, "
            "thread_ids=thread_001,thread_002, artifact_ids=art_001,art_008, "
            "asset_id=asset_001"
        ),
        actions=[
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_001"}),
            Action(name="update_audit_report_status", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed with recommendations"}),
            Action(name="get_audits_by_status", kwargs={"status": "COMPLETED", "audit_type": "COMBINED_DS_A11Y"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical audit findings require immediate design team attention", "escalate_to": ["sarah.designer@company.com", "mike.ux@company.com"]}),
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_002"}),
            Action(name="update_audit_report_status", kwargs={"audit_id": "audit_002", "new_status": "COMPLETED", "report_asset_id": "asset_007"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Secondary audit review completed"}),
            Action(name="get_audits_by_status", kwargs={"status": "COMPLETED", "created_after": "2024-08-20T15:00:00Z"}),
            Action(name="get_audits_by_status", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"}),
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_001"})
        ],
        outputs=[
            "Audit management workflow completed: audit_001 status updated to COMPLETED with report asset_001 association and completion notes, thread_001 priority escalated to HIGH with critical findings urgency and stakeholder escalation to design team, audit_002 status updated to COMPLETED with report asset_007, secondary thread_002 priority normalized, comprehensive audit status verification completed across all COMBINED_DS_A11Y and A11Y audit types for stakeholder reporting, and asset export summary retrieved for asset_001 coordination and compliance tracking."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_83",
        instruction=(
            "You are a Figma comment and communication specialist responsible for managing accessibility feedback and related email communications. "
            "Your task is to coordinate accessibility improvements, track comment resolution, manage email thread priorities, and ensure proper communication across teams. "
            "Focus on managing comment status updates, setting appropriate email priorities, assigning tasks, and verifying asset exports. "
            "Required constants: "
            "artifact_id=art_008, asset_id=asset_007, comment_ids=comment_006,comment_009, "
            "thread_id=thread_004, thread_priority=HIGH, urgency_reason=Accessibility compliance deadline approaching, "
            "escalate_to=accessibility-team@company.com,design-leads@company.com, "
            "resolution_notes=Accessibility improvements in progress - adding ARIA labels and keyboard navigation support"
        ),
        actions=[
            Action(name="get_figma_comments_by_artifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_007"}),
            Action(name="update_figma_comment_status", kwargs={"comment_id": "comment_006", "new_status": "IN_PROGRESS", "resolution_notes": "Accessibility improvements in progress - adding ARIA labels and keyboard navigation support", "assignee_email": "mike.ux@company.com", "priority_level": "HIGH"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_004", "new_priority": "HIGH", "urgency_reason": "Accessibility compliance deadline approaching", "escalate_to": ["accessibility-team@company.com", "design-leads@company.com"]}),
            Action(name="get_gmail_threads_by_labels", kwargs={"thread_id": "thread_004"}),
            Action(name="update_figma_comment_status", kwargs={"comment_id": "comment_009", "new_status": "RESOLVED", "assignee_email": "sarah.designer@company.com"})
        ],
        outputs=[
            "figma_comments_retrieved:art_008:unresolved",
            "asset_export_verified:asset_007",
            "comment_status_updated:comment_006:IN_PROGRESS:mike.ux@company.com:HIGH",
            "thread_priority_updated:thread_004:HIGH:accessibility-team@company.com,design-leads@company.com",
            "gmail_thread_retrieved:thread_004",
            "comment_status_updated:comment_009:RESOLVED:sarah.designer@company.com"
        ]
    ),
    Task(
        annotator="0",
        user_id="user_84",
        instruction=(
            "You are an information gathering specialist responsible for coordinating comprehensive information collection and Gmail message status update workflows. "
            "Your task is to gather system information from multiple sources and update Gmail message status with proper coordination. "
            "Focus on collecting audit data, release information, asset exports, and terminal logs with Gmail message status coordination. "
            "Coordinate with communication teams through appropriate channels to ensure all information gathering and message status workflows are properly managed. "
            "Required constants: "
            "audit_id=audit_004, release_id=release_002, asset_id=asset_004, "
            "owner_email=mike.ux@company.com, created_after=2024-08-19T12:30:00Z, "
            "log_level=INFO, component=information_gathering, message_id=msg_002, "
            "new_status=READ, updated_by=mike.ux@company.com, plan_id=plan_002"
        ),
        actions=[
            Action(name="get_audit_summary", kwargs={"audit_id": "audit_004"}),
            Action(name="get_release_summary", kwargs={"release_id": "release_002"}),
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_004"}),
            Action(name="get_releases_by_owner", kwargs={"owner_email": "mike.ux@company.com", "created_after": "2024-08-19T12:30:00Z"}),
            Action(name="get_terminal_logs_summary", kwargs={"log_level": "INFO", "component": "information_gathering"}),
            Action(name="get_fix_plan_items", kwargs={"plan_id": "plan_002"}),
            Action(name="update_gmail_message_status", kwargs={"message_id": "msg_002", "new_status": "READ", "updated_by": "mike.ux@company.com"})
        ],
        outputs=[
            "Information gathering with Gmail message status update completed: audit_004 summary retrieved for audit information coordination, release_002 summary verified for release data tracking, asset_004 export summary retrieved for asset information, Mike UX releases verified for release coordination since August 19th, terminal logs summary retrieved for INFO level information_gathering component, fix plan items retrieved for plan_002 coordination, and Gmail message msg_002 status updated to READ by Mike UX."
        ]
    ),
    Task(
        annotator="0",
        user_id="user_85",
        instruction=(
            "You are an asset management specialist responsible for coordinating comprehensive asset management and fix item status workflows. "
            "Your task is to manage asset exports, system configuration, and fix item status coordination for design system compliance. "
            "Focus on managing asset exports, system configuration analysis, audit information, and fix item status updates with proper coordination. "
            "Coordinate with development teams through appropriate channels to ensure all asset management and fix item workflows are properly coordinated. "
            "Required constants: "
            "asset_id=asset_005, category=design_system_aliases, audit_id=audit_006, "
            "thread_id=thread_006, owner_email=sarah.designer@company.com, created_after=2024-08-21T14:00:00Z, "
            "log_level=INFO, component=asset_management, fix_item_id=item_003, "
            "new_status=APPLIED, updated_by=sarah.designer@company.com, notes=Asset management coordination completed with design system compliance"
        ),
        actions=[
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_005"}),
            Action(name="get_system_config_by_category", kwargs={"category": "design_system_aliases"}),
            Action(name="get_audit_summary", kwargs={"audit_id": "audit_006"}),
            Action(name="get_gmail_threads_by_labels", kwargs={"thread_id": "thread_006"}),
            Action(name="get_releases_by_owner", kwargs={"owner_email": "sarah.designer@company.com", "created_after": "2024-08-21T14:00:00Z"}),
            Action(name="get_terminal_logs_summary", kwargs={"log_level": "INFO", "component": "asset_management"}),
            Action(name="update_fix_item_status", kwargs={"fix_item_id": "item_003", "new_status": "APPLIED", "updated_by": "sarah.designer@company.com", "notes": "Asset management coordination completed with design system compliance"})
        ],
        outputs=[
            "Asset management with fix item status update completed: asset_005 export summary retrieved for asset management coordination, design_system_aliases config retrieved for system coordination, audit_006 summary verified for audit tracking, Gmail thread_006 verified for communication coordination, Sarah Designer releases retrieved for release coordination since August 21st, terminal logs summary retrieved for INFO level asset_management component, and fix item_003 status updated to APPLIED with asset management coordination notes by Sarah Designer."
        ]
    ),
    Task(
        annotator="0",
        user_id="user_86",
        instruction=(
            "You are a release diff analysis specialist responsible for coordinating release difference tracking and integrated comment resolution workflows. "
            "Your task is to manage release diff coordination with figma comment resolution and ensure proper version tracking. "
            "Focus on managing release version updates with comprehensive comment status coordination and asset export verification. "
            "Coordinate with development teams through appropriate channels to ensure all release diffs and comment workflows are properly synchronized. "
            "Required constants: "
            "release_id=release_001, version_id=v1.4.0, release_name=Design System v1.4.0 - Diff Analysis Updates, "
            "owner_email=sarah.designer@company.com, comment_id=comment_001, new_status=RESOLVED, "
            "assignee_email=sarah.designer@company.com, priority_level=NORMAL, "
            "resolution_notes=Release diff analysis completed with comprehensive comment resolution, "
            "artifact_id=art_001, asset_id=asset_001, export_status=COMPLETED, "
            "dlp_scan_status=CLEAN, created_after=2024-08-20T15:00:00Z, "
            "thread_id=thread_001, export_notes=Release diff analysis asset export completed"
        ),
        actions=[
            Action(name="get_release_diff_summary", kwargs={"release_id": "release_001"}),
            Action(name="update_release_version", kwargs={"release_id": "release_001", "version_id": "v1.4.0", "release_name": "Design System v1.4.0 - Diff Analysis Updates", "owner_email": "sarah.designer@company.com", "thread_id": "thread_001"}),
            Action(name="get_figma_comments_by_artifact", kwargs={"artifact_id": "art_001", "resolved_status": False}),
            Action(name="update_figma_comment_status", kwargs={"comment_id": "comment_001", "new_status": "RESOLVED", "resolution_notes": "Release diff analysis completed with comprehensive comment resolution", "assignee_email": "sarah.designer@company.com", "priority_level": "NORMAL"}),
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_001"}),
            Action(name="update_asset_export_status", kwargs={"asset_id": "asset_001", "new_status": "COMPLETED", "notes": "Release diff analysis asset export completed", "dlp_scan_status": "CLEAN"}),
            Action(name="get_releases_by_owner", kwargs={"owner_email": "sarah.designer@company.com", "created_after": "2024-08-20T15:00:00Z"})
        ],
        outputs=[
            "Release diff analysis completed for release_001: release diff summary verified for comprehensive analysis workflow, release version updated to v1.4.0 with diff analysis updates and Sarah Designer ownership, unresolved figma comments retrieved for art_001 artifact coordination, comment_001 status updated to RESOLVED with comprehensive resolution notes and Sarah Designer assignment at NORMAL priority, asset export summary verified for asset_001 coordination, export status updated to COMPLETED with diff analysis notes and CLEAN DLP scan, and Sarah Designer releases verified for coordination since August 20th."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_87",
        instruction=(
            "You are responsible for managing accessibility improvements for the admin panel header components. "
            "Your objective is to ensure all accessibility-related feedback is properly addressed and tracked through completion. "
            "This includes coordinating with the UX team on implementing ARIA labels and keyboard navigation enhancements, "
            "verifying the export status of accessibility improvements, and maintaining clear communication channels. "
            "All activities should be properly documented for compliance and tracking purposes. "
            "Key parameters: "
            "artifact_id=art_008, asset_id=asset_007, comment_id=comment_006, "
            "assignee_email=mike.ux@company.com, priority_level=HIGH, "
            "resolution_notes=Accessibility improvements in progress - adding ARIA labels and keyboard navigation support, "
            "export_notes=Admin header accessibility export completed with ARIA labels, "
            "dlp_scan_status=CLEAN, thread_id=thread_004"
        ),
        actions=[
            Action(name="get_figma_comments_by_artifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_007"}),
            Action(name="update_figma_comment_status", kwargs={"comment_id": "comment_006", "new_status": "IN_PROGRESS", "resolution_notes": "Accessibility improvements in progress - adding ARIA labels and keyboard navigation support", "assignee_email": "mike.ux@company.com", "priority_level": "HIGH"}),
            Action(name="get_gmail_threads_by_labels", kwargs={"thread_id": "thread_004"}),
            Action(name="get_figma_comments_by_artifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="update_asset_export_status", kwargs={"asset_id": "asset_007", "new_status": "COMPLETED", "notes": "Admin header accessibility export completed with ARIA labels", "dlp_scan_status": "CLEAN"}),
            Action(name="get_figma_artifacts_by_status", kwargs={"artifact_id": "art_008"}),
            Action(name="add_terminal_log_entry", kwargs={"log_message": "Figma comment resolution workflow completed for art_008 admin panel header with accessibility improvements and export status updates", "log_level": "INFO", "component": "comment_resolution", "user_email": "mike.ux@company.com"})
        ],
        outputs=[
            "comment_006_status:IN_PROGRESS",
            "comment_assignee:mike.ux@company.com",
            "comment_priority:HIGH",
            "asset_007_status:COMPLETED",
            "dlp_scan_status:CLEAN",
            "thread_004_verified:true",
            "art_008_verified:true",
            "terminal_log_added:true"
        ]
    ),
    Task(
        annotator="0",
        user_id="user_88",
        instruction=(
            "You are a mobile audit findings severity management specialist responsible for coordinating audit finding severity updates and integrated fix plan workflows. "
            "Your task is to manage audit finding severity escalation with fix plan status coordination and ensure proper priority management. "
            "Focus on managing audit finding severity updates for CRITICAL violations, including fix plan delivery coordination and comprehensive fix item tracking. "
            "Coordinate with development teams through appropriate channels to ensure all audit findings and fix workflows are properly synchronized. "
            "Additionally, you'll retrieve audit summaries to ensure comprehensive oversight and coordination throughout the severity management process. "
            "Required constants: "
            "finding_id=finding_a11y_001, new_severity=CRITICAL, updated_by=alex.dev@company.com, "
            "plan_id=plan_001, delivery_method=TICKETS, owner_email=alex.dev@company.com, "
            "item_id=item_001, fix_item_id=item_001, new_priority=HIGH, "
            "priority_reason=Critical finding requires immediate fix attention, "
            "audit_id=audit_002, violation_type=COLOR_CONTRAST, severity=CRITICAL, "
            "log_message=Audit findings severity management and fix plan coordination completed, "
            "log_level=INFO, log_component=audit_severity, "
            "comment_id=comment_006, comment_status=RESOLVED"
        ),
        actions=[
            Action(name="update_audit_finding_severity", kwargs={"finding_id": "finding_a11y_001", "new_severity": "CRITICAL", "updated_by": "alex.dev@company.com"}),
            Action(name="get_audit_findings_by_type", kwargs={"violation_type": "COLOR_CONTRAST", "severity": "CRITICAL"}),
            Action(name="get_fix_plan_items", kwargs={"plan_id": "plan_001"}),
            Action(name="update_fix_plan_status", kwargs={"plan_id": "plan_001", "new_status": "IN_PROGRESS", "delivery_method": "TICKETS", "owner_email": "alex.dev@company.com"}),
            Action(name="update_fix_item_priority", kwargs={"item_id": "item_001", "new_priority": "HIGH", "priority_reason": "Critical finding requires immediate fix attention", "updated_by": "alex.dev@company.com"}),
            Action(name="update_fix_item_status", kwargs={"fix_item_id": "item_001", "new_status": "IN_PROGRESS", "updated_by": "alex.dev@company.com"}),
            Action(name="add_terminal_log_entry", kwargs={"log_message": "Audit findings severity management and fix plan coordination completed", "log_level": "INFO", "component": "audit_severity", "user_email": "alex.dev@company.com"}),
            Action(name="get_audit_summary", kwargs={"audit_id": "audit_002"}),
            Action(name="update_figma_comment_status", kwargs={"comment_id": "comment_006", "new_status": "RESOLVED", "resolved_by": "alex.dev@company.com"})
        ],
        outputs=[
            "Audit findings severity management completed: finding_a11y_001 severity escalated to CRITICAL, CRITICAL severity COLOR_CONTRAST violations analyzed, fix plan items retrieved for plan_001, fix plan status updated to IN_PROGRESS with TICKETS delivery method, fix item_001 priority escalated to HIGH with critical finding attention, fix item status updated to IN_PROGRESS, comprehensive audit severity management workflow logging completed, audit_002 summary retrieved, and Figma comment comment_006 marked as RESOLVED."
        ]
    ),
    Task(
        annotator="0",
        user_id="user_89",
        instruction=(
            "You are a multi-platform release management specialist responsible for coordinating comprehensive release orchestration and dual status update workflows. "
            "Your task is to manage multi-platform release coordination, audit findings analysis, asset export verification, and dual status updates for enterprise release orchestration. "
            "Focus on managing release summary coordination, audit findings tracking, asset export verification, system configuration analysis, and dual status update workflows with multi-platform coordination. "
            "Coordinate with release orchestration teams through appropriate channels to ensure all multi-platform release management and dual status update workflows are properly coordinated. "
            "Required constants: "
            "release_id=release_010, audit_id=audit_012, violation_type=FOCUS_INDICATOR, severity=HIGH, "
            "asset_id=asset_018, owner_email=sarah.designer@company.com, created_after=2024-08-23T16:30:00Z, "
            "thread_id=thread_013, log_level=INFO, component=multi_platform_release, "
            "category=notification_settings, plan_id=plan_011, new_plan_status=DELIVERED, "
            "delivery_method=TICKETS, plan_notes=Multi-platform release coordination completed with comprehensive orchestration, "
            "new_asset_status=COMPLETED, dlp_scan_status=CLEAN, "
            "notes=Multi-platform release management coordination completed with comprehensive tracking"
        ),
        actions=[
            Action(name="get_release_summary", kwargs={"release_id": "release_010"}),
            Action(name="get_audit_findings_by_type", kwargs={"violation_type": "FOCUS_INDICATOR", "severity": "HIGH"}),
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_018"}),
            Action(name="get_releases_by_owner", kwargs={"owner_email": "sarah.designer@company.com", "created_after": "2024-08-23T16:30:00Z"}),
            Action(name="get_gmail_threads_by_labels", kwargs={"thread_id": "thread_013"}),
            Action(name="get_terminal_logs_summary", kwargs={"log_level": "INFO", "component": "multi_platform_release"}),
            Action(name="get_system_config_by_category", kwargs={"category": "notification_settings"}),
            Action(name="update_fix_plan_status", kwargs={"plan_id": "plan_011", "new_status": "DELIVERED", "delivery_method": "TICKETS", "owner_email": "sarah.designer@company.com", "notes": "Multi-platform release coordination completed with comprehensive orchestration"}),
            Action(name="update_asset_export_status", kwargs={"asset_id": "asset_018", "new_status": "COMPLETED", "notes": "Multi-platform release management coordination completed with comprehensive tracking", "dlp_scan_status": "CLEAN"})
        ],
        outputs=[
            "Multi-platform release management with dual status updates completed: release_010 summary retrieved for multi-platform coordination, HIGH severity FOCUS_INDICATOR violations analyzed for audit coordination, asset_018 export summary verified for asset tracking, Sarah Designer releases retrieved for release coordination since August 23rd, Gmail thread_013 verified for communication coordination, terminal logs summary retrieved for INFO level multi_platform_release component, notification_settings config retrieved for system coordination, fix plan_011 status updated to DELIVERED with TICKETS delivery method and comprehensive orchestration notes, and asset export status updated to COMPLETED with multi-platform coordination tracking and CLEAN DLP scan."
        ]
    ),
    Task(
        annotator="0",
        user_id="user_90",
        instruction=(
            "You are a design system integration specialist responsible for coordinating comprehensive design system workflows and dual audit/asset update processes. "
            "Your task is to manage design system integration coordination, figma artifact tracking, audit summary analysis, and dual update processes for enterprise design system management. "
            "Focus on managing figma artifact coordination, design system config analysis, audit summary tracking, release coordination, and dual update workflows with comprehensive design system integration. "
            "Coordinate with design system teams through appropriate channels to ensure all integration and dual update workflows are properly orchestrated. "
            "Required constants: "
            "status=ACTIVE, category=design_system_aliases, audit_id=audit_010, "
            "thread_id=thread_012, owner_email=sarah.designer@company.com, created_after=2024-08-23T15:30:00Z, "
            "log_level=INFO, component=design_system_integration, asset_id=asset_016, "
            "new_audit_status=COMPLETED, audit_notes=Design system integration coordination completed with comprehensive tracking, "
            "new_asset_status=COMPLETED, asset_notes=Design system asset coordination completed with integration tracking, "
            "dlp_scan_status=CLEAN"
        ),
        actions=[
            Action(name="get_figma_artifacts_by_status", kwargs={"status": "ACTIVE"}),
            Action(name="get_system_config_by_category", kwargs={"category": "design_system_aliases"}),
            Action(name="get_audit_summary", kwargs={"audit_id": "audit_010"}),
            Action(name="get_gmail_threads_by_labels", kwargs={"thread_id": "thread_012"}),
            Action(name="get_releases_by_owner", kwargs={"owner_email": "sarah.designer@company.com", "created_after": "2024-08-23T15:30:00Z"}),
            Action(name="get_terminal_logs_summary", kwargs={"log_level": "INFO", "component": "design_system_integration"}),
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_016"}),
            Action(name="update_audit_status", kwargs={"audit_id": "audit_010", "new_status": "COMPLETED", "notes": "Design system integration coordination completed with comprehensive tracking", "updated_by": "sarah.designer@company.com"}),
            Action(name="update_asset_export_status", kwargs={"asset_id": "asset_016", "new_status": "COMPLETED", "notes": "Design system asset coordination completed with integration tracking", "dlp_scan_status": "CLEAN"})
        ],
        outputs=[
            "Design system integration with audit and asset updates completed: ACTIVE figma artifacts retrieved for comprehensive design system coordination, design_system_aliases config retrieved for system coordination, audit_010 summary verified for audit tracking, Gmail thread_012 verified for communication coordination, Sarah Designer releases retrieved for release coordination since August 23rd, terminal logs summary retrieved for INFO level design_system_integration component, asset_016 export summary verified for asset coordination, audit status updated to COMPLETED with design system integration tracking by Sarah Designer, and asset export status updated to COMPLETED with integration tracking and CLEAN DLP scan."
        ]
    ),
    Task(
        annotator="0",
        user_id="user_91",
        instruction=(
            "You are an audit report management specialist responsible for coordinating the end-to-end audit lifecycle for design system components and accessibility compliance. "
            "Your primary responsibility involves managing audit_001 for artifact art_001 (Homepage Hero Section) which requires comprehensive status tracking from COMPLETED to final report generation. The workflow integrates with audit_002 for accessibility review of art_008 admin panel components requiring status coordination. "
            "The audit management workflow centers on thread_001 priority escalation to HIGH priority for design review coordination involving sarah.designer@company.com oversight, URGENT priority level escalation for comprehensive design review tracking, and escalation_reason 'Critical audit findings require immediate design team attention and stakeholder review'. The priority management requires comprehensive Gmail thread coordination and detailed audit status documentation. "
            "Your coordination efforts should ensure seamless audit report generation through proper status management, effective priority escalation for design review threads, comprehensive audit findings tracking for stakeholder reporting, and successful audit lifecycle completion with proper report asset associations. "
            "Key parameters: audit_id=audit_001, new_status=COMPLETED, report_asset_id=asset_001, completion_notes=Design system audit completed with recommendations, "
            "thread_001_priority=HIGH, thread_002_priority=NORMAL, thread_001_urgency=Critical audit findings require immediate design team attention, thread_002_urgency=Secondary audit review completed, "
            "escalate_to=sarah.designer@company.com,mike.ux@company.com, audit_type=COMBINED_DS_A11Y, created_after=2024-08-20T15:00:00Z, audit_date_filter=2024-08-18T00:00:00Z, "
            "thread_ids=thread_001,thread_002, artifact_ids=art_001,art_008, "
            "log_message=Audit management workflow completed with comprehensive status tracking and report generation, "
            "log_level=INFO, component=audit_management, user_email=sarah.designer@company.com"
        ),
        actions=[
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_001"}),
            Action(name="update_audit_report_status", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed with recommendations"}),
            Action(name="get_audits_by_status", kwargs={"status": "COMPLETED", "audit_type": "COMBINED_DS_A11Y"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical audit findings require immediate design team attention", "escalate_to": ["sarah.designer@company.com", "mike.ux@company.com"]}),
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_002"}),
            Action(name="get_audits_by_status", kwargs={"artifact_id": "art_001", "created_after": "2024-08-20T15:00:00Z"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Secondary audit review completed"}),
            Action(name="get_audits_by_status", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"}),
            Action(name="get_system_config_by_category", kwargs={"category": "audit_config"}),
            Action(name="add_terminal_log_entry", kwargs={"log_message": "Audit management workflow completed with comprehensive status tracking and report generation", "log_level": "INFO", "component": "audit_management", "user_email": "sarah.designer@company.com"})
        ],
        outputs=[
            "Audit management workflow completed: audit_001 status updated to COMPLETED with report asset_001 association and completion notes, thread_001 priority escalated to HIGH with critical findings urgency and stakeholder escalation to design team, secondary thread_002 priority normalized, comprehensive audit status verification completed across all COMBINED_DS_A11Y and A11Y audit types for stakeholder reporting, audit configuration retrieved for system coordination settings, and terminal log entry added documenting audit management workflow completion with comprehensive status tracking."
        ]
    ),
    Task(
        annotator="0",
        user_id="user_92",
        instruction=(
            "You are a design system component audit specialist responsible for coordinating comprehensive design system audits and thread priority management for component workflows. "
            "Your primary responsibility involves audit_002 coordination for design system components requiring comprehensive status tracking and thread priority management for component review coordination. The workflow integrates with approval verification and thread escalation for design system release preparation. "
            "The design system coordination workflow centers on comprehensive audit tracking with sarah.designer@company.com oversight, thread_001 HIGH priority management for design system coordination, and detailed approval verification across design system workflows. "
            "Your coordination efforts should ensure seamless design system audit coordination through comprehensive status tracking, effective thread priority management for component reviews, and detailed approval verification for design system workflows with proper design team coordination and release preparation tracking. "
            "Key parameters: "
            "audit_002_id=audit_002, audit_002_status=COMPLETED, "
            "art_008_id=art_008, audit_type=A11Y, "
            "thread_001_id=thread_001, thread_008_id=thread_008, "
            "thread_001_priority=HIGH, thread_008_priority=NORMAL, "
            "thread_001_urgency=Design system component review requires immediate coordination, "
            "thread_008_urgency=Design system follow-up coordination completed, "
            "completion_notes=Design system component audit completed successfully, "
            "approval_002_id=approval_002, cycle_002_id=cycle_002, "
            "escalate_to=sarah.designer@company.com,design.system@company.com, "
            "release_owner=sarah.designer@company.com, release_start_date=2024-08-20T13:00:00Z"
        ),
        actions=[
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_002"}),
            Action(name="update_audit_report_status", kwargs={"audit_id": "audit_002", "new_status": "COMPLETED", "completion_notes": "Design system component audit completed successfully"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Design system component review requires immediate coordination", "escalate_to": ["sarah.designer@company.com", "design.system@company.com"]}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_008", "new_priority": "NORMAL", "urgency_reason": "Design system follow-up coordination completed"}),
            Action(name="get_review_approvals_summary", kwargs={"approval_id": "approval_002", "cycle_id": "cycle_002"}),
            Action(name="get_audits_by_status", kwargs={"artifact_id": "art_008", "audit_type": "A11Y"}),
            Action(name="get_releases_by_owner", kwargs={"owner_email": "sarah.designer@company.com", "created_after": "2024-08-20T13:00:00Z"}),
            Action(name="get_audit_findings_summary", kwargs={"audit_id": "audit_002", "include_resolved": True}),
            Action(name="add_terminal_log_entry", kwargs={"log_message": "Design system component audit workflow completed - audit_002 with thread priority management", "log_level": "INFO", "component": "design_system_audit", "user_email": "sarah.designer@company.com"})
        ],
        outputs=[
            "audit_002_verified:audit_002",
            "audit_status_updated:COMPLETED",
            "thread_001_updated:HIGH",
            "thread_008_updated:NORMAL",
            "approval_summary_retrieved:approval_002",
            "audit_artifacts_retrieved:art_008",
            "releases_retrieved:sarah.designer@company.com",
            "audit_findings_retrieved:audit_002",
            "terminal_log_added:design_system_audit_workflow_completed"
        ]
    ),

    Task(
        annotator="0",
        user_id="user_93",
        instruction=(
            "You are a design system compliance analysis specialist responsible for coordinating comprehensive design system workflows and audit update processes. "
            "Your task is to manage design system compliance coordination, audit findings analysis, release tracking, and audit update processes for enterprise design system management. "
            "Focus on managing audit findings coordination, release summary analysis, system configuration tracking, and audit update workflows with comprehensive design system compliance. "
            "Coordinate with design system compliance teams through appropriate channels to ensure all design system analysis and audit update workflows are properly orchestrated. "
            "Required constants: "
            "violation_type=DESIGN_SYSTEM, severity=HIGH, release_id=release_008, "
            "category=design_system_aliases, thread_id=thread_011, owner_email=sarah.designer@company.com, "
            "created_after=2024-08-23T13:00:00Z, log_level=INFO, component=design_system_compliance, "
            "audit_id=audit_008, new_audit_status=COMPLETED, audit_notes=Design system compliance analysis completed with comprehensive tracking, "
            "updated_by=sarah.designer@company.com"
        ),
        actions=[
            Action(name="get_audit_findings_by_type", kwargs={"violation_type": "DESIGN_SYSTEM", "severity": "HIGH"}),
            Action(name="get_release_summary", kwargs={"release_id": "release_008"}),
            Action(name="get_system_config_by_category", kwargs={"category": "design_system_aliases"}),
            Action(name="get_gmail_threads_by_labels", kwargs={"thread_id": "thread_011"}),
            Action(name="get_releases_by_owner", kwargs={"owner_email": "sarah.designer@company.com", "created_after": "2024-08-23T13:00:00Z"}),
            Action(name="get_terminal_logs_summary", kwargs={"log_level": "INFO", "component": "design_system_compliance"}),
            Action(name="get_audit_summary", kwargs={"audit_id": "audit_008"}),
            Action(name="update_audit_status", kwargs={"audit_id": "audit_008", "new_status": "COMPLETED", "notes": "Design system compliance analysis completed with comprehensive tracking", "updated_by": "sarah.designer@company.com"})
        ],
        outputs=[
            "Design system compliance analysis with audit update completed: HIGH severity DESIGN_SYSTEM audit findings analyzed for compliance coordination, release_008 summary retrieved for release coordination, design_system_aliases config retrieved for system coordination, Gmail thread_011 verified for communication coordination, Sarah Designer releases retrieved for release coordination since August 23rd, terminal logs summary retrieved for INFO level design_system_compliance component, audit_008 summary verified for audit coordination, and audit status updated to COMPLETED with design system compliance tracking by Sarah Designer."
        ]
    ),
    Task(
        annotator="variant_4",
        user_id="user_94",
        instruction=(
            "You are an audit report coordination specialist responsible for coordinating comprehensive audit report analysis and fix plan status workflows. "
            "Your task is to manage audit report coordination, fix plan analysis, and fix plan status updates for audit management processes. "
            "Focus on managing audit report coordination, fix plan items analysis, release tracking, and fix plan status updates with proper workflow management. "
            "Coordinate with audit teams through appropriate channels to ensure all audit report and fix plan workflows are properly managed. "
            "Required constants: "
            "audit_id=audit_008, plan_id=plan_006, release_id=release_001, "
            "owner_email=sarah.designer@company.com, created_after=2024-08-22T16:45:00Z, "
            "thread_id=thread_014, log_level=INFO, component=audit_report_coordination, "
            "new_status=DELIVERED, delivery_method=TICKETS, notes=Audit report coordination completed with fix plan workflow"
        ),
        actions=[
            Action(name="get_audit_report_summary", kwargs={"audit_id": "audit_008"}),
            Action(name="get_fix_plan_items", kwargs={"plan_id": "plan_006"}),
            Action(name="get_release_diff_summary", kwargs={"release_id": "release_001"}),
            Action(name="get_releases_by_owner", kwargs={"owner_email": "sarah.designer@company.com", "created_after": "2024-08-22T16:45:00Z"}),
            Action(name="get_gmail_threads_by_labels", kwargs={"thread_id": "thread_014"}),
            Action(name="get_terminal_logs_summary", kwargs={"log_level": "INFO", "component": "audit_report_coordination"}),
            Action(name="update_fix_plan_status", kwargs={"plan_id": "plan_006", "new_status": "DELIVERED", "delivery_method": "TICKETS", "owner_email": "sarah.designer@company.com", "notes": "Audit report coordination completed with fix plan workflow"})
        ],
        outputs=[
            "Audit report coordination with fix plan status update completed: audit_008 report summary retrieved for audit coordination, fix plan items retrieved for plan_006 coordination, release_001 diff summary verified for release analysis, Sarah Designer releases retrieved for release coordination since August 22nd, Gmail thread_014 verified for communication coordination, terminal logs summary retrieved for INFO level audit_report_coordination component, and fix plan_006 status updated to DELIVERED with TICKETS delivery method and audit coordination notes by Sarah Designer."
        ]
    ),
    Task(
        annotator="0",
        user_id="user_95",
        instruction=(
            "You are an audit report management specialist responsible for coordinating the end-to-end audit lifecycle for design system components and accessibility compliance. "
            "Your primary responsibility involves managing audit_001 for artifact art_001 (Homepage Hero Section) which requires comprehensive status tracking from COMPLETED to final report generation. The workflow integrates with audit_002 for accessibility review of art_008 admin panel components requiring status coordination. "
            "The audit management workflow centers on thread_001 priority escalation to HIGH priority for design review coordination involving sarah.designer@company.com oversight, URGENT priority level escalation for comprehensive design review tracking, and escalation_reason 'Critical audit findings require immediate design team attention and stakeholder review'. The priority management requires comprehensive Gmail thread coordination and detailed audit status documentation. "
            "Your coordination efforts should ensure seamless audit report generation through proper status management, effective priority escalation for design review threads, and comprehensive audit findings tracking for stakeholder reporting. "
            "Key parameters: audit_id=audit_001, new_status=COMPLETED, report_asset_id=asset_001, completion_notes=Design system audit completed with recommendations, "
            "thread_001_priority=HIGH, thread_002_priority=NORMAL, thread_001_urgency=Critical audit findings require immediate design team attention, thread_002_urgency=Secondary audit review completed, "
            "escalate_to=sarah.designer@company.com,mike.ux@company.com, audit_type=COMBINED_DS_A11Y, created_after=2024-08-20T15:00:00Z, audit_date_filter=2024-08-18T00:00:00Z, "
            "thread_ids=thread_001,thread_002, artifact_ids=art_001,art_008, "
            "asset_id=asset_001"
        ),
        actions=[
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_001"}),
            Action(name="update_audit_report_status", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed with recommendations"}),
            Action(name="get_audits_by_status", kwargs={"status": "COMPLETED", "audit_type": "COMBINED_DS_A11Y"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical audit findings require immediate design team attention", "escalate_to": ["sarah.designer@company.com", "mike.ux@company.com"]}),
            Action(name="get_audits_by_status", kwargs={"audit_id": "audit_002"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Secondary audit review completed"}),
            Action(name="get_audits_by_status", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"}),
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_001"})
        ],
        outputs=[
            "Audit management workflow completed: audit_001 status updated to COMPLETED with report asset_001 association and completion notes, thread_001 priority escalated to HIGH with critical findings urgency and stakeholder escalation to design team, comprehensive audit verification completed for A11Y audit type, and asset export summary retrieved for asset_001 documentation and compliance tracking."
        ]
    ),
    Task(
        annotator="0",
        user_id="user_96",
        instruction=(
            "You are a Figma comment resolution specialist managing accessibility improvements for the admin panel header. "
            "Your task is to coordinate the resolution of accessibility feedback and ensure all related assets and communications are properly tracked. "
            "Focus on managing the accessibility enhancement workflow, including comment resolution and asset export status updates. "
            "Coordinate with the UX team through the appropriate communication channels to ensure all accessibility requirements are met. "
            "Required constants: "
            "artifact_id=art_008, asset_id=asset_007, comment_id=comment_006, "
            "assignee_email=mike.ux@company.com, priority_level=HIGH, "
            "thread_ids=thread_004,thread_005, "
            "resolution_notes=Accessibility improvements in progress - adding ARIA labels and keyboard navigation support, "
            "export_notes=Admin header accessibility export completed with ARIA labels, "
            "dlp_scan_status=CLEAN, "
            "new_status=IN_PROGRESS, export_status=COMPLETED"
        ),
        actions=[
            Action(name="get_figma_comments_by_artifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_007"}),
            Action(name="update_figma_comment_status", kwargs={"comment_id": "comment_006", "new_status": "IN_PROGRESS", "resolution_notes": "Accessibility improvements in progress - adding ARIA labels and keyboard navigation support", "assignee_email": "mike.ux@company.com", "priority_level": "HIGH"}),
            Action(name="get_gmail_threads_by_labels", kwargs={"thread_id": "thread_004"}),
            Action(name="get_gmail_threads_by_labels", kwargs={"thread_id": "thread_005"}),
            Action(name="get_figma_comments_by_artifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="update_asset_export_status", kwargs={"asset_id": "asset_007", "new_status": "COMPLETED", "notes": "Admin header accessibility export completed with ARIA labels", "dlp_scan_status": "CLEAN"}),
            Action(name="add_terminal_log_entry", kwargs={"log_message": "comment_resolution:comment_006:IN_PROGRESS:asset_007:COMPLETED", "log_level": "INFO", "component": "figma_comment_resolution", "user_email": "mike.ux@company.com"})
        ],
        outputs=[
            "comment_updated:comment_006:IN_PROGRESS:mike.ux@company.com",
            "thread_checked:thread_004:thread_005",
            "asset_updated:asset_007:COMPLETED",
            "log_added:figma_comment_resolution:INFO"
        ]
    ),
    Task(
        annotator="0",
        user_id="user_97",
        instruction=(
            "You are a release management coordinator responsible for coordinating comprehensive release workflows and asset export status management for design system components. "
            "Your primary responsibility involves release_003 status management and asset_003 export coordination requiring comprehensive status tracking and integration with release workflow management. The workflow involves cross-team coordination and proper release lifecycle management. "
            "The release coordination workflow centers on release_003 PUBLISHED status achievement with comprehensive release notes documentation, asset_003 export status coordination with COMPLETED status and DLP scan verification, and proper release owner assignment to sarah.designer@company.com for design system release oversight. The release management requires systematic status coordination and compliance verification. "
            "Your coordination efforts should ensure comprehensive release lifecycle management, proper asset export status coordination, and successful release deployment tracking for stakeholder reporting and workflow completion. "
            "Required constants: "
            "release_id=release_003, new_status=PUBLISHED, "
            "release_notes=Design system components release with accessibility improvements, "
            "updated_by=sarah.designer@company.com, asset_id=asset_003, export_status=COMPLETED, "
            "export_notes=Design system asset export completed with accessibility compliance, "
            "dlp_scan_status=CLEAN, owner_email=sarah.designer@company.com, "
            "created_after=2024-08-20T15:00:00Z, "
            "log_message=Release management workflow completed - release_003 published with asset_003 export completion, "
            "log_level=INFO, component=release_management, user_email=sarah.designer@company.com, "
            "audit_id=audit_001, thread_id=thread_001, thread_priority=HIGH, "
            "urgency_reason=Critical release deployment requires immediate stakeholder coordination, "
            "escalate_to=sarah.designer@company.com,release.team@company.com"
        ),
        actions=[
            Action(name="update_release_status", kwargs={"release_id": "release_003", "new_status": "PUBLISHED", "release_notes": "Design system components release with accessibility improvements", "updated_by": "sarah.designer@company.com"}),
            Action(name="update_asset_export_status", kwargs={"asset_id": "asset_003", "new_status": "COMPLETED", "notes": "Design system asset export completed with accessibility compliance", "dlp_scan_status": "CLEAN"}),
            Action(name="get_releases_by_owner", kwargs={"owner_email": "sarah.designer@company.com", "created_after": "2024-08-20T15:00:00Z"}),
            Action(name="add_terminal_log_entry", kwargs={"log_message": "Release management workflow completed - release_003 published with asset_003 export completion", "log_level": "INFO", "component": "release_management", "user_email": "sarah.designer@company.com"}),
            Action(name="get_audit_summary", kwargs={"audit_id": "audit_001"}),
            Action(name="update_gmail_thread_priority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical release deployment requires immediate stakeholder coordination", "escalate_to": ["sarah.designer@company.com", "release.team@company.com"]})
        ],
        outputs=[
            "Enhanced release management workflow completed: release_003 status updated to PUBLISHED with design system release notes and sarah.designer@company.com assignment, asset_003 export status updated to COMPLETED with DLP scan verification and accessibility compliance, releases retrieved for sarah.designer@company.com owner tracking, terminal log entry added documenting release workflow completion, comprehensive audit_001 summary retrieved for release compliance verification, and thread_001 priority escalated to HIGH for critical release deployment coordination with stakeholder escalation to release team."
        ]
    ),

    Task(
        annotator="0",
        user_id="user_98",
        instruction=(
            "You are a Figma comment resolution specialist responsible for accessibility feedback coordination and workflow management across admin panel header components. "
            "Your primary responsibility involves accessibility feedback coordination for art_008 admin panel header where unresolved comments with resolved_status False require identification and resolution coordination. The workflow also involves asset_007 admin header export integration requiring status verification and coordination alignment. "
            "The accessibility improvement workflow centers on comment_006 accessibility enhancement coordination involving mike.ux@company.com team member oversight, HIGH priority accessibility improvements, and comprehensive ARIA labels and keyboard navigation support implementation tracking. The feedback resolution requires progress status coordination and detailed implementation documentation. "
            "Your coordination efforts should ensure seamless accessibility audit communication through thread_004, effective comment lifecycle coordination, and comprehensive accessibility compliance tracking for stakeholder reporting and successful workflow completion."
            "Use resolution_notes=Accessibility improvements in progress - adding ARIA labels and keyboard navigation support"
            ",notes=Admin header accessibility export completed with ARIA labels"
        ),
        actions=[
            Action(name="get_figma_comments_by_artifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_007"}),
            Action(name="update_figma_comment_status", kwargs={"comment_id": "comment_006", "new_status": "IN_PROGRESS", "resolution_notes": "Accessibility improvements in progress - adding ARIA labels and keyboard navigation support", "assignee_email": "mike.ux@company.com", "priority_level": "HIGH"}),
            Action(name="get_gmail_threads_by_labels", kwargs={"thread_id": "thread_004"}),
            Action(name="get_figma_comments_by_artifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="update_asset_export_status", kwargs={"asset_id": "asset_007", "new_status": "COMPLETED", "notes": "Admin header accessibility export completed with ARIA labels", "dlp_scan_status": "CLEAN"})
        ],
        outputs=[
            "Comment resolution workflow completed for comment_006: comment status updated to IN_PROGRESS, assignee assigned to Mike UX with HIGH priority level, resolution notes added about accessibility improvements, asset export status verified for admin header asset_007, Gmail thread communication status verified for thread_004 accessibility audit coordination, and asset export updated to COMPLETED with accessibility enhancements."
        ]
    ),
    Task(
        annotator="0",
        user_id="user_99",
        instruction=(
            "You are an asset management specialist responsible for coordinating comprehensive asset management and fix item status workflows. "
            "Your task is to manage asset exports, system configuration, and fix item status coordination for design system compliance. "
            "Focus on managing asset exports, system configuration analysis, audit information, and fix item status updates with proper coordination. "
            "Coordinate with development teams through appropriate channels to ensure all asset management and fix item workflows are properly coordinated. "
            "Additionally, you'll maintain comprehensive terminal logging throughout the asset management process to ensure proper tracking and audit trail for the workflow coordination. "
            "Required constants: "
            "asset_id=asset_005, category=design_system_aliases, audit_id=audit_006, "
            "thread_id=thread_006, owner_email=sarah.designer@company.com, created_after=2024-08-21T14:00:00Z, "
            "log_level=INFO, component=asset_management, fix_item_id=item_003, "
            "new_status=APPLIED, updated_by=sarah.designer@company.com, notes=Asset management coordination completed with design system compliance"
        ),
        actions=[
            Action(name="get_asset_export_summary", kwargs={"asset_id": "asset_005"}),
            Action(name="get_system_config_by_category", kwargs={"category": "design_system_aliases"}),
            Action(name="get_audit_summary", kwargs={"audit_id": "audit_006"}),
            Action(name="get_gmail_threads_by_labels", kwargs={"thread_id": "thread_006"}),
            Action(name="get_releases_by_owner", kwargs={"owner_email": "sarah.designer@company.com", "created_after": "2024-08-21T14:00:00Z"}),
            Action(name="get_terminal_logs_summary", kwargs={"log_level": "INFO", "component": "asset_management"}),
            Action(name="update_fix_item_status", kwargs={"fix_item_id": "item_003", "new_status": "APPLIED", "updated_by": "sarah.designer@company.com", "notes": "Asset management coordination completed with design system compliance"}),
            Action(name="add_terminal_log_entry", kwargs={"log_message": "Asset management coordination completed with design system compliance", "log_level": "INFO", "component": "asset_management", "user_email": "sarah.designer@company.com"})
        ],
        outputs=[
            "Asset management with fix item status update completed: asset_005 export summary retrieved for asset management coordination, design_system_aliases config retrieved for system coordination, audit_006 summary verified for audit tracking, Gmail thread_006 verified for communication coordination, Sarah Designer releases retrieved for release coordination since August 21st, terminal logs summary retrieved for INFO level asset_management component, fix item_003 status updated to APPLIED with asset management coordination notes by Sarah Designer, and terminal log entry added for asset management workflow tracking."
        ]
    ),
    Task(
        annotator="0",
        user_id="user_100",
        instruction=(
            "You are an audit findings severity management specialist responsible for coordinating audit finding severity updates and integrated fix plan workflows. "
            "Your task is to manage audit finding severity escalation with fix plan status coordination and ensure proper priority management. "
            "Focus on managing audit finding severity updates for CRITICAL violations, including fix plan delivery coordination and comprehensive fix item tracking. "
            "Coordinate with development teams through appropriate channels to ensure all audit findings and fix workflows are properly synchronized. "
            "Additionally, you'll retrieve audit summaries to ensure comprehensive oversight and coordination throughout the severity management process. "
            "Required constants: "
            "finding_id=finding_a11y_001, new_severity=CRITICAL, updated_by=alex.dev@company.com, "
            "plan_id=plan_001, delivery_method=TICKETS, owner_email=alex.dev@company.com, "
            "item_id=item_001, fix_item_id=item_001, new_priority=HIGH, "
            "priority_reason=Critical audit finding requires immediate fix attention, "
            "audit_id=audit_002, violation_type=TOUCH_TARGET, severity=CRITICAL, "
            "log_message=Audit findings severity management and fix plan coordination completed"
        ),
        actions=[
            Action(name="update_audit_finding_severity", kwargs={"finding_id": "finding_a11y_001", "new_severity": "CRITICAL", "updated_by": "alex.dev@company.com"}),
            Action(name="get_audit_findings_by_type", kwargs={"violation_type": "TOUCH_TARGET", "severity": "CRITICAL"}),
            Action(name="get_fix_plan_items", kwargs={"plan_id": "plan_001"}),
            Action(name="update_fix_plan_status", kwargs={"plan_id": "plan_001", "new_status": "IN_PROGRESS", "delivery_method": "TICKETS", "owner_email": "alex.dev@company.com"}),
            Action(name="update_fix_item_priority", kwargs={"item_id": "item_001", "new_priority": "HIGH", "priority_reason": "Critical audit finding requires immediate fix attention", "updated_by": "alex.dev@company.com"}),
            Action(name="update_fix_item_status", kwargs={"fix_item_id": "item_001", "new_status": "IN_PROGRESS", "updated_by": "alex.dev@company.com"}),
            Action(name="add_terminal_log_entry", kwargs={"log_message": "Audit findings severity management and fix plan coordination completed", "log_level": "INFO", "component": "audit_severity", "user_email": "alex.dev@company.com"}),
            Action(name="get_audit_summary", kwargs={"audit_id": "audit_002"})
        ],
        outputs=[
            "Audit findings severity management completed: finding_a11y_001 severity escalated to CRITICAL with Alex Dev oversight, CRITICAL severity TOUCH_TARGET violations analyzed for comprehensive coordination, fix plan items retrieved for plan_001 coordination workflow, fix plan status updated to IN_PROGRESS with TICKETS delivery method and Alex Dev ownership, fix item_001 priority escalated to HIGH with critical finding attention and Alex Dev assignment, fix item status updated to IN_PROGRESS for active coordination, comprehensive audit severity management workflow logging completed, and audit_002 summary retrieved for comprehensive audit oversight and coordination."
        ]
    ),
]
