
from tau_bench.types import Action, Task

TASKS = [
    Task(
        annotator="0",
        user_id="user_1",
        instruction=(
            "Handle the role of a review cycle SLA management expert in charge of managing review cycle escalation and integrated audit workflow processes. Your assignment is to oversee review cycle SLA management alongside audit status oversight and ensure accurate escalation tracking. Concentrate on the transition of review cycle statuses from NEEDS_REVIEW to ESCALATED, including audit status monitoring and thorough logging. Engage with review teams via suitable communication methods to guarantee all SLA breaches and audit workflows are correctly aligned. Required constants: cycle_id=cycle_001, artifact_id=art_001, new_status=ESCALATED, audit_id=audit_001, audit_status=IN_PROGRESS, updated_by=emma.creative@company.com, thread_id=thread_001, priority_level=HIGH, urgency_reason=SLA breach requires immediate escalation, escalate_to=emma.creative@company.com, log_level=WARNING, component=review_sla, after_timestamp=2024-08-20T15:00:00Z, message_pattern=escalation, log_message=Review cycle SLA escalation completed with audit integration, category=review_sla_config"
        ),
        actions=[
            Action(name="GetReviewApprovalsSummary", kwargs={"cycle_id": "cycle_001"}),
            Action(name="UpdateReviewCycleStatus", kwargs={"cycle_id": "cycle_001", "new_status": "ESCALATED", "reviewer_email": "emma.creative@company.com", "completion_notes": "SLA breach requires immediate escalation"}),
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_001"}),
            Action(name="UpdateAuditStatus", kwargs={"audit_id": "audit_001", "new_status": "IN_PROGRESS", "updated_by": "emma.creative@company.com"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "SLA breach requires immediate escalation"}),
            Action(name="AddTerminalLogEntry", kwargs={"log_message": "Review cycle SLA escalation completed with audit integration", "log_level": "WARNING", "component": "review_sla", "user_email": "emma.creative@company.com"}),
            Action(name="GetFilteredLogEntries", kwargs={"log_level": "WARNING", "component": "review_sla", "after_timestamp": "2024-08-20T15:00:00Z", "message_pattern": "escalation"}),
            Action(name="GetSystemConfigByCategory", kwargs={"category": "review_sla_config"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_2",
        instruction=(
            "Coordinate the tasks of an audit report management specialist tasked with managing the comprehensive audit lifecycle for design system components and ensuring accessibility compliance. Your core duty involves handling audit_001 for artifact art_001 (Homepage Hero Section), which necessitates detailed status tracking from COMPLETED to final report creation. The workflow synchronizes with audit_002 for the accessibility evaluation of art_008 admin panel components, requiring status synchronization. The audit management process focuses on increasing thread_001 priority to HIGH for design review coordination under the supervision of emma.creative@company.com, with URGENT priority escalation for detailed design review tracking, and escalation_reason 'Critical audit findings require immediate design team attention and stakeholder review'. Priority management demands elaborate Gmail thread coordination and extensive audit status documentation. Your coordination efforts should assure smooth audit report creation through effective status management, decisive priority escalation for design review threads, and detailed tracking of audit findings for stakeholder reporting. Key parameters: audit_id=audit_001, new_status=COMPLETED, report_asset_id=asset_001, completion_notes=Design system audit completed with recommendations, thread_001_priority=HIGH, thread_002_priority=NORMAL, thread_001_urgency=Critical audit findings require immediate design team attention, thread_002_urgency=Secondary audit review completed, escalate_to=emma.creative@company.com,jake.design@company.com, audit_type=COMBINED_DS_A11Y, created_after=2024-08-20T15:00:00Z, audit_date_filter=2024-08-18T00:00:00Z, thread_ids=thread_001,thread_002, artifact_ids=art_001,art_008"
        ),
        actions=[
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_001"}),
            Action(name="UpdateAuditReportStatus", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed with recommendations"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical audit findings require immediate design team attention", "escalate_to": ["emma.creative@company.com", "jake.design@company.com"]}),
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_002"}),
            Action(name="UpdateAuditReportStatus", kwargs={"audit_id": "audit_002", "new_status": "COMPLETED", "report_asset_id": "asset_007"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Secondary audit review completed"}),
            Action(name="GetAuditsByStatus", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"})
        ],
        outputs=[]
    ),
    
    Task(
        annotator="0",
        user_id="user_3",
        instruction=(
            "You are tasked with handling the management of audit reports, specifically focusing on the audit lifecycle for design system components and ensuring their compliance with accessibility standards. Your main duty is to oversee audit_001 for artifact art_001 (Homepage Hero Section), which necessitates meticulous status monitoring from COMPLETED up to the final report creation. The procedure incorporates audit_002 to review the accessibility of art_008 admin panel components, demanding coordinated status management. The audit oversight workflow emphasizes prioritizing thread_001 to a HIGH priority for design review involving the oversight of emma.creative@company.com, marking an URGENT priority level for an exhaustive design examination, with the escalation_reason 'Critical audit findings require immediate design team attention and stakeholder review'. Effective priority management calls for extensive coordination of Gmail threads and meticulous audit status documentation. Your coordination activities should facilitate smooth audit report generation through proficient status management, effective escalation of design review threads, and detailed tracking of audit findings for stakeholder communication. Key parameters: audit_id=audit_001, new_status=COMPLETED, report_asset_id=asset_001, completion_notes=Design system audit completed with recommendations, thread_001_priority=HIGH, thread_002_priority=NORMAL, thread_001_urgency=Critical audit findings require immediate design team attention, thread_002_urgency=Secondary audit review completed, escalate_to=emma.creative@company.com,jake.design@company.com, audit_type=COMBINED_DS_A11Y, created_after=2024-08-20T15:00:00Z, audit_date_filter=2024-08-18T00:00:00Z, thread_ids=thread_001,thread_002, artifact_ids=art_001,art_008"
        ),
        actions=[
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_001"}),
            Action(name="UpdateAuditReportStatus", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed with recommendations"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical audit findings require immediate design team attention", "escalate_to": ["emma.creative@company.com", "jake.design@company.com"]}),
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_002"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Secondary audit review completed"}),
            Action(name="GetAuditsByStatus", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"}),
            Action(name="AddTerminalLogEntry", kwargs={"log_message": "Audit management workflow completed for audit_001 and audit_002 with critical findings escalation", "log_level": "INFO", "component": "audit_management", "user_email": "emma.creative@company.com"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_4",
        instruction=(
            "Your role is to oversee the coordination of audit findings and manage fix items within admin panel accessibility projects. Your primary duty is to facilitate the accessibility audits for audit_002, audit_004, and audit_005, where detailed analysis of findings and updating the status of fix items need to be processed systematically. This involves managing the lifecycle of fix items, ensuring they progress through appropriate statuses. The workflow in accessibility compliance emphasizes verifying touch targets like item_001 to achieve VERIFIED status, coordinating the application and timestamp of font size adjustments for item_004, and managing contrast violation fixes for item_002 under the IN_PROGRESS status. Effective implementation of fixes necessitates systematic status coordination and compliance validation. Your coordination work should guarantee thorough audit findings analysis, proper management of fix item lifecycles, and successful tracking of accessibility compliance for reporting to stakeholders and completion of workflows."
        ),
        actions=[
            Action(name="GetAuditFindingsSummary", kwargs={"audit_id": "audit_002"}),
            Action(name="GetAuditFindingsSummary", kwargs={"audit_id": "audit_004"}),
            Action(name="GetAuditFindingsSummary", kwargs={"audit_id": "audit_005"}),
            Action(name="UpdateFixItemStatus", kwargs={"fix_item_id": "item_001", "new_status": "VERIFIED"}),
            Action(name="UpdateFixItemStatus", kwargs={"fix_item_id": "item_004", "new_status": "APPLIED", "completion_date": "2024-08-25T15:30:00Z"}),
            Action(name="UpdateFixItemStatus", kwargs={"fix_item_id": "item_002", "new_status": "IN_PROGRESS"}),
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_007"}),
            Action(name="GetFixPlanItems", kwargs={"plan_id": "plan_001"})
        ],
        outputs=[]
    ),
    
    Task(
        annotator="0",
        user_id="user_5",
        instruction=(
            "As a specialist in managing review cycle SLA, you are tasked with handling the coordination of review cycle escalation and integration of audit workflows. Your responsibility is to oversee the coordination of review cycle SLA with audit status management and ensure accurate escalation tracking. Concentrate on overseeing review cycle status changes from NEEDS_REVIEW to ESCALATED, which includes coordinating audit statuses and maintaining comprehensive logging. Work with review teams through appropriate channels to ensure synchronization of all SLA breaches and audit workflows. Required constants: cycle_id=cycle_001, artifact_id=art_001, new_status=ESCALATED, audit_id=audit_001, audit_status=IN_PROGRESS, updated_by=emma.creative@company.com, thread_id=thread_001, priority_level=HIGH, urgency_reason=SLA breach requires immediate escalation, escalate_to=emma.creative@company.com, log_level=WARNING, component=review_sla, after_timestamp=2024-08-20T15:00:00Z, message_pattern=escalation, log_message=Review cycle SLA escalation completed with audit integration, asset_id=asset_001, category=sla_config"
        ),
        actions=[
            Action(name="GetReviewApprovalsSummary", kwargs={"cycle_id": "cycle_001"}),
            Action(name="UpdateReviewCycleStatus", kwargs={"cycle_id": "cycle_001", "new_status": "ESCALATED", "reviewer_email": "emma.creative@company.com", "completion_notes": "SLA breach requires immediate escalation"}),
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_001"}),
            Action(name="UpdateAuditStatus", kwargs={"audit_id": "audit_001", "new_status": "IN_PROGRESS", "updated_by": "emma.creative@company.com"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "SLA breach requires immediate escalation"}),
            Action(name="AddTerminalLogEntry", kwargs={"log_message": "Review cycle SLA escalation completed with audit integration", "log_level": "WARNING", "component": "review_sla", "user_email": "emma.creative@company.com"}),
            Action(name="GetFilteredLogEntries", kwargs={"log_level": "WARNING", "component": "review_sla", "after_timestamp": "2024-08-20T15:00:00Z", "message_pattern": "escalation"}),
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_001"}),
            Action(name="GetSystemConfigByCategory", kwargs={"category": "sla_config"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_6",
        instruction=(
            "Handling the role of a Figma comment resolution specialist, you are in charge of coordinating accessibility feedback and managing workflows for admin panel header components. Your main responsibility includes coordinating accessibility feedback for art_008 admin panel header where unresolved comments with resolved_status False must be identified and managed for resolution. This workflow also involves asset_007 admin header export integration, requiring status verification and coordination alignment. The workflow for accessibility improvement focuses on comment_006 accessibility enhancement coordination under the oversight of jake.design@company.com, emphasizing HIGH priority accessibility improvements, and tracking comprehensive ARIA labels and keyboard navigation support implementation. The resolution of feedback involves status coordination and detailed documentation of implementation. Your coordination efforts should ensure smooth communication of accessibility audits through thread_004, effective coordination of the comment lifecycle, and thorough tracking of accessibility compliance for stakeholder reporting and successful workflow completion. You can use resolution_notes Accessibility improvements in progress - adding ARIA labels and keyboard navigation support, thread_priority=HIGH, urgency_reason=Accessibility improvements require immediate attention, escalate_to=jake.design@company.com"
        ),
        actions=[
            Action(name="GetFigmaCommentsByArtifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_007"}),
            Action(name="UpdateFigmaCommentStatus", kwargs={"comment_id": "comment_006", "new_status": "IN_PROGRESS", "resolution_notes": "Accessibility improvements in progress - adding ARIA labels and keyboard navigation support", "assignee_email": "jake.design@company.com", "priority_level": "HIGH"}),
            Action(name="GetGmailThreadsByLabels", kwargs={"thread_id": "thread_004"}),
            Action(name="GetFigmaCommentsByArtifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="AddTerminalLogEntry", kwargs={"log_message": "Accessibility comment resolution workflow completed for art_008 admin panel header", "log_level": "INFO", "component": "accessibility_resolution", "user_email": "jake.design@company.com"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_004", "new_priority": "HIGH", "urgency_reason": "Accessibility improvements require immediate attention", "escalate_to": ["jake.design@company.com"]})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_7",
        instruction=(
            "You are tasked as an audit report management expert in charge of handling the comprehensive audit lifecycle for design system components and ensuring accessibility compliance. Your main duty includes overseeing audit_001 for artifact art_001 (Homepage Hero Section), which demands complete status tracking from COMPLETED to the creation of the final report. This workflow ties into audit_002, focusing on the accessibility review of art_008 admin panel components and necessitating status coordination. The audit management is reliant on elevated priority for thread_001 to HIGH for design review coordination under emma.creative@company.com guidance, URGENT priority escalation for thorough design review tracking, and escalation_reason 'Critical audit findings require immediate design team attention and stakeholder review'. Proper management of priorities is essential and involves detailed Gmail thread coordination and precise audit status documentation. Your efforts should guarantee proficient audit report generation via accurate status management, effective priority escalation in design review threads, thorough tracking of audit findings for stakeholder reporting, and successful audit lifecycle conclusion with correct report asset alignment. Key parameters: audit_id=audit_001, new_status=COMPLETED, report_asset_id=asset_001, completion_notes=Design system audit completed with recommendations, thread_001_priority=HIGH, thread_002_priority=NORMAL, thread_001_urgency=Critical audit findings require immediate design team attention, thread_002_urgency=Secondary audit review completed, escalate_to=emma.creative@company.com,jake.design@company.com, audit_type=COMBINED_DS_A11Y, created_after=2024-08-20T15:00:00Z, audit_date_filter=2024-08-18T00:00:00Z, thread_ids=thread_001,thread_002, artifact_ids=art_001,art_008, asset_id=asset_001, category=audit_thresholds"
        ),
        actions=[
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_001"}),
            Action(name="UpdateAuditReportStatus", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed with recommendations"}),
            Action(name="GetAuditsByStatus", kwargs={"status": "COMPLETED", "audit_type": "COMBINED_DS_A11Y"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical audit findings require immediate design team attention", "escalate_to": ["emma.creative@company.com", "jake.design@company.com"]}),
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_002"}),
            Action(name="GetAuditsByStatus", kwargs={"artifact_id": "art_001", "created_after": "2024-08-20T15:00:00Z"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Secondary audit review completed"}),
            Action(name="GetAuditsByStatus", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"}),
            Action(name="GetSystemConfigByCategory", kwargs={"category": "audit_thresholds"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_8",
        instruction=(
            "You are designated as a design system component audit expert charged with coordinating thorough audits and managing thread priorities for component workflows. Your chief responsibility encompasses coordination of audit_002 involving design system components that necessitate complete status tracking and thread priority management for component review processes. This process is integrated with approval verification and thread escalation for preparing the design system release. The coordination workflow for the design system focuses on rigorous audit tracking under emma.creative@company.com supervision, managing HIGH priority for thread_001 in design system coordination, and detailed approval verification throughout design system workflows. Your coordination actions should guarantee smooth design system audit handling, with thorough status tracking, effective thread priority management for component reviews, and detailed approval verification for workflows, ensuring proper design team coordination and tracking of release preparation. Key parameters: audit_002_id=audit_002, audit_002_status=COMPLETED, art_008_id=art_008, audit_type=A11Y, thread_001_id=thread_001, thread_008_id=thread_008, thread_001_priority=HIGH, thread_008_priority=NORMAL, thread_001_urgency=Design system component review requires immediate coordination, thread_008_urgency=Design system follow-up coordination completed, completion_notes=Design system component audit completed successfully, approval_002_id=approval_002, cycle_002_id=cycle_002, escalate_to=emma.creative@company.com,design.system@company.com, release_owner=emma.creative@company.com, release_start_date=2024-08-20T13:00:00Z, category=design_system_config"
        ),
        actions=[
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_002"}),
            Action(name="UpdateAuditReportStatus", kwargs={"audit_id": "audit_002", "new_status": "COMPLETED", "completion_notes": "Design system component audit completed successfully"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Design system component review requires immediate coordination", "escalate_to": ["emma.creative@company.com", "design.system@company.com"]}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_008", "new_priority": "NORMAL", "urgency_reason": "Design system follow-up coordination completed"}),
            Action(name="GetReviewApprovalsSummary", kwargs={"approval_id": "approval_002", "cycle_id": "cycle_002"}),
            Action(name="GetAuditsByStatus", kwargs={"artifact_id": "art_008", "audit_type": "A11Y"}),
            Action(name="GetReleasesByOwner", kwargs={"owner_email": "emma.creative@company.com", "created_after": "2024-08-20T13:00:00Z"}),
            Action(name="GetSystemConfigByCategory", kwargs={"category": "design_system_config"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_9",
        instruction=(
            "As a mid-stage audit coordination specialist, you are tasked with overseeing comprehensive audit workflows and the analysis/system integration of findings. Your role involves managing mid-stage audit coordination, handling finding analysis management, and system integration procedures for enterprise audit management. Concentrate on controlling the analysis of audit finding details, progress coordination, status management, and asset integration workflows while ensuring comprehensive mid-stage audit coordination. Work alongside audit teams through suitable channels to guarantee that all audit coordination and system integration processes are accurately orchestrated. Required constants: audit_id=audit_002, include_resolved=True, finding_id=finding_a11y_002, progress_percentage=55, progress_notes=Mid-stage audit coordination advancing with comprehensive analysis, updated_by=jake.design@company.com, new_finding_status=IN_PROGRESS, finding_notes=Mid-stage audit finding progressing with comprehensive coordination, asset_id=asset_002, category=email_templates, thread_id=thread_002, owner_email=jake.design@company.com, created_after=2024-08-18T11:30:00Z, log_level=WARNING, component=mid_stage_audit_coordination"
        ),
        actions=[
            Action(name="UpdateAuditProgress", kwargs={"audit_id": "audit_002", "progress_percentage": 55, "notes": "Mid-stage audit coordination advancing with comprehensive analysis", "updated_by": "jake.design@company.com"}),
            Action(name="GetAuditFindingDetails", kwargs={"audit_id": "audit_002", "include_resolved": True}),
            Action(name="UpdateAuditFindingStatus", kwargs={"finding_id": "finding_a11y_002", "new_status": "IN_PROGRESS", "notes": "Mid-stage audit finding progressing with comprehensive coordination", "updated_by": "jake.design@company.com"}),
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_002"}),
            Action(name="GetSystemConfigByCategory", kwargs={"category": "email_templates"}),
            Action(name="GetGmailThreadsByLabels", kwargs={"thread_id": "thread_002"}),
            Action(name="GetReleasesByOwner", kwargs={"owner_email": "jake.design@company.com", "created_after": "2024-08-18T11:30:00Z"}),
            Action(name="GetTerminalLogsSummary", kwargs={"log_level": "WARNING", "component": "mid_stage_audit_coordination"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_10",
        instruction=(
            "As a specialist in audit report management, you are responsible for orchestrating the end-to-end audit lifecycle of design system components. Your aim is to complete the audit report for the Homepage Hero Section (art_001) while ensuring all associated components are properly documented. Key tasks include: - Changing the status of audit_001 to COMPLETED with the final report asset_001 - Guaranteeing the tracking of audit_002 for admin panel components (art_008) with status IN_PROGRESS - Overseeing communication threads for design review and stakeholder updates - Recording all audit findings and status updates Required constants: audit_001_status=COMPLETED, audit_002_status=IN_PROGRESS, report_asset_id=asset_001, completion_notes=Design system audit completed with recommendations, thread_001_priority=HIGH, thread_002_priority=NORMAL, thread_001_urgency=Critical audit findings require immediate design team attention, thread_002_urgency=Secondary audit review completed, escalate_to=emma.creative@company.com,jake.design@company.com, audit_type=COMBINED_DS_A11Y, created_after=2024-08-20T15:00:00Z, audit_date_filter=2024-08-18T00:00:00Z, thread_ids=thread_001,thread_002, artifact_ids=art_001,art_008, asset_id=asset_001, log_message=audit_001_completion_workflow, log_level=INFO, component=audit_management, user_email=emma.creative@company.com"
        ),
        actions=[
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_001"}),
            Action(name="UpdateAuditReportStatus", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed with recommendations"}),
            Action(name="GetAuditsByStatus", kwargs={"status": "COMPLETED", "audit_type": "COMBINED_DS_A11Y"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical audit findings require immediate design team attention", "escalate_to": ["emma.creative@company.com", "jake.design@company.com"]}),
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_002"}),
            Action(name="GetAuditsByStatus", kwargs={"artifact_id": "art_001", "created_after": "2024-08-20T15:00:00Z"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Secondary audit review completed"}),
            Action(name="GetAuditsByStatus", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"}),
            Action(name="GetSystemConfigByCategory", kwargs={"category": "audit_config"}),
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_001"}),
            Action(name="AddTerminalLogEntry", kwargs={"log_message": "Audit management workflow completed with comprehensive tracking and report generation", "log_level": "INFO", "component": "audit_management", "user_email": "emma.creative@company.com"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_11",
        instruction=(
            "You serve as an audit report management specialist tasked with handling the full audit lifecycle for design system components and accessibility compliance. Your principal duty is to coordinate audit_001 for artifact art_001 (Homepage Hero Section), necessitating thorough status tracking from COMPLETED to the final report production. The workflow incorporates audit_002 for the accessibility review of art_008 admin panel components. You are required to coordinate thread priorities across various stakeholders, focusing on thread_001 for critical design review tasks. The system is expected to document all status changes and priority escalations thoroughly. Key parameters: audit_id=audit_001, new_status=COMPLETED, report_asset_id=asset_001, completion_notes=Design system audit completed with recommendations, thread_001_priority=HIGH, thread_002_priority=NORMAL, thread_001_urgency=Critical audit findings require immediate design team attention and stakeholder review, thread_002_urgency=Secondary audit review completed, escalate_to=emma.creative@company.com,jake.design@company.com, audit_type=COMBINED_DS_A11Y, created_after=2024-08-20T15:00:00Z, audit_date_filter=2024-08-18T00:00:00Z, thread_ids=thread_001,thread_002, artifact_ids=art_001,art_008, asset_id=asset_001, audit_002_status=COMPLETED, updated_by=emma.creative@company.com,"
        ),
        actions=[
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_001"}),
            Action(name="UpdateAuditReportStatus", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed with recommendations"}),
            Action(name="GetAuditsByStatus", kwargs={"status": "COMPLETED", "audit_type": "COMBINED_DS_A11Y"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical audit findings require immediate design team attention and stakeholder review", "escalate_to": ["emma.creative@company.com", "jake.design@company.com"]}),
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_002"}),
            Action(name="GetAuditsByStatus", kwargs={"artifact_id": "art_001", "created_after": "2024-08-20T15:00:00Z"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Secondary audit review completed"}),
            Action(name="GetAuditsByStatus", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"}),
            Action(name="GetSystemConfigByCategory", kwargs={"category": "audit_config"}),
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_001"}),
            Action(name="UpdateAuditStatus", kwargs={"audit_id": "audit_002", "new_status": "COMPLETED", "updated_by": "emma.creative@company.com"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_12",
        instruction=(
            "Your role as a Figma comment resolution specialist involves managing accessibility feedback coordination and workflow for admin panel header components. Your main obligation is to oversee accessibility feedback coordination for art_008 admin panel header, where unresolved comments marked as resolved_status False need to be identified and coordinated for resolution. Additionally, the workflow necessitates asset_007 admin header export integration, with an emphasis on status verification and coordination alignment. The accessibility enhancement workflow focuses on coordinating comment_006 accessibility improvement efforts, requiring oversight by team member jake.design@company.com, prioritizing HIGH priority accessibility upgrades, and tracking the implementation of comprehensive ARIA labels and keyboard navigation support. Coordination is needed for managing progress status and drafting detailed implementation documentation. Ensure that your coordination efforts facilitate seamless communication through thread_004 for accessibility audits, efficiently manage the comment lifecycle, and comprehensively track accessibility compliance for stakeholder reporting and successful workflow completion. Utilize resolution_notes Accessibility improvements in progress - adding ARIA labels and keyboard navigation support"
        ),
        actions=[
            Action(name="GetFigmaCommentsByArtifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_007"}),
            Action(name="UpdateFigmaCommentStatus", kwargs={"comment_id": "comment_006", "new_status": "IN_PROGRESS", "resolution_notes": "Accessibility improvements in progress - adding ARIA labels and keyboard navigation support", "assignee_email": "jake.design@company.com", "priority_level": "HIGH"}),
            Action(name="GetGmailThreadsByLabels", kwargs={"thread_id": "thread_004"}),
            Action(name="GetFigmaCommentsByArtifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="AddTerminalLogEntry", kwargs={"log_message": "Figma comment resolution workflow completed for accessibility improvements", "log_level": "INFO", "component": "figma_comment_resolution", "user_email": "jake.design@company.com"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_13",
        instruction=(
            "Your role as a Figma comment resolution specialist involves handling accessibility feedback coordination and managing workflows for admin panel header components. Your main duty is to coordinate accessibility feedback for art_008 admin panel header, where you must identify and manage unresolved comments marked with resolved_status False. The workflow also includes handling the export integration of asset_007 admin header by verifying status and ensuring coordination alignment. The focus of the accessibility enhancement workflow is on coordinating comment_006 accessibility improvements with oversight by team member jake.design@company.com, prioritizing HIGH priority improvements, and tracking the implementation of comprehensive ARIA labels and keyboard navigation support. Feedback resolution requires coordinating progress status and documenting detailed implementations. Your coordination should facilitate smooth accessibility audit communication via thread_004, efficiently manage the comment lifecycle, and track comprehensive accessibility compliance for stakeholder reports and proper workflow completion. You can utilize resolution_notes Accessibility improvements in progress - adding ARIA labels and keyboard navigation support."
        ),
        actions=[
            Action(name="GetFigmaCommentsByArtifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_007"}),
            Action(name="UpdateFigmaCommentStatus", kwargs={"comment_id": "comment_006", "new_status": "IN_PROGRESS", "resolution_notes": "Accessibility improvements in progress - adding ARIA labels and keyboard navigation support", "assignee_email": "jake.design@company.com", "priority_level": "HIGH"}),
            Action(name="GetGmailThreadsByLabels", kwargs={"thread_id": "thread_004"}),
            Action(name="GetFigmaCommentsByArtifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="GetSystemConfigByCategory", kwargs={"category": "accessibility_config"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_14",
        instruction=(
            "Your role as a Figma comment resolution specialist involves managing accessibility feedback coordination and workflows across admin panel header components. Your main task is to handle accessibility feedback coordination for art_008 admin panel header, identifying and coordinating the resolution of unresolved comments identified by resolved_status False. Additionally, the workflow involves managing the export integration of asset_007 admin header, which requires status verification and coordination alignment. The accessibility improvement process focuses on coordinating enhancements for comment_006, involving team member oversight by jake.design@company.com, addressing HIGH priority improvements, and tracking the implementation of comprehensive ARIA labels and keyboard navigation support. Resolving feedback necessitates coordinating progress status and detailed documentation of implementations. Your efforts should ensure seamless accessibility audit communication through thread_004, effective management of comment lifecycle coordination, and exhaustive tracking of accessibility compliance for stakeholder reporting and successful workflow completion. Utilize resolution_notes Accessibility improvements in progress - adding ARIA labels and keyboard navigation support. Use these specific constants: audit_id=audit_008, owner_email=jake.design@company.com, created_after=2024-08-19T12:00:00Z, log_message=Accessibility comment resolution workflow completed for art_008 admin panel header, component=accessibility_resolution."
        ),
        actions=[
            Action(name="GetFigmaCommentsByArtifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_007"}),
            Action(name="UpdateFigmaCommentStatus", kwargs={"comment_id": "comment_006", "new_status": "IN_PROGRESS", "resolution_notes": "Accessibility improvements in progress - adding ARIA labels and keyboard navigation support", "assignee_email": "jake.design@company.com", "priority_level": "HIGH"}),
            Action(name="GetGmailThreadsByLabels", kwargs={"thread_id": "thread_004"}),
            Action(name="GetFigmaCommentsByArtifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="AddTerminalLogEntry", kwargs={"log_message": "Accessibility comment resolution workflow completed for art_008 admin panel header", "log_level": "INFO", "component": "accessibility_resolution", "user_email": "jake.design@company.com"}),
            Action(name="GetAuditSummary", kwargs={"audit_id": "audit_008"})

        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_15",
        instruction=(
            "You are a release diff analysis specialist tasked with handling the tracking of release differences and managing integrated comment resolution workflows. Your role involves managing coordination of release diffs with figma comment resolution and ensuring accurate version tracking. Emphasize managing release version updates with comprehensive coordination of comment statuses and verifying asset exports. Collaborate with development teams through designated channels to make sure all release diffs and comment workflows are synchronized properly. Required constants: release_id=release_001, version_id=v1.4.0, release_name=Design System v1.4.0 - Diff Analysis Updates, owner_email=emma.creative@company.com, comment_id=comment_001, new_status=RESOLVED, assignee_email=emma.creative@company.com, priority_level=NORMAL, resolution_notes=Release diff analysis completed with comprehensive comment resolution, artifact_id=art_001, asset_id=asset_001, export_status=COMPLETED, dlp_scan_status=CLEAN, created_after=2024-08-20T15:00:00Z, thread_id=thread_001, export_notes=Release diff analysis asset export completed"
        ),
        actions=[
            Action(name="GetReleaseDiffSummary", kwargs={"release_id": "release_001"}),
            Action(name="UpdateReleaseVersion", kwargs={"release_id": "release_001", "version_id": "v1.4.0", "release_name": "Design System v1.4.0 - Diff Analysis Updates", "owner_email": "emma.creative@company.com", "thread_id": "thread_001"}),
            Action(name="GetFigmaCommentsByArtifact", kwargs={"artifact_id": "art_001", "resolved_status": False}),
            Action(name="UpdateFigmaCommentStatus", kwargs={"comment_id": "comment_001", "new_status": "RESOLVED", "resolution_notes": "Release diff analysis completed with comprehensive comment resolution", "assignee_email": "emma.creative@company.com", "priority_level": "NORMAL"}),
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_001"}),
            Action(name="UpdateAssetExportStatus", kwargs={"asset_id": "asset_001", "new_status": "COMPLETED", "notes": "Release diff analysis asset export completed", "dlp_scan_status": "CLEAN"}),
            Action(name="GetReleasesByOwner", kwargs={"owner_email": "emma.creative@company.com", "created_after": "2024-08-20T15:00:00Z"}),
            Action(name="AddTerminalLogEntry", kwargs={"log_message": "Release diff analysis workflow completed - version v1.4.0 updated with comment resolution", "log_level": "INFO", "component": "release_diff_analysis", "user_email": "emma.creative@company.com"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_16",
        instruction=(
            "You are a review management coordination specialist in charge of organizing comprehensive review workflows and updating audit statuses. Your assignment is to manage coordination of review cycles, track artifacts, and oversee audit status management for design system components. Concentrate on handling review approvals, verifying active artifacts, conducting system configuration checks, and coordinating audit status with appropriate workflow management. Work with UX teams through designated channels to ensure all review management processes are accurately tracked and updated. Required constants: cycle_id=cycle_001, status=ACTIVE, category=gmail_labels, asset_id=asset_006, thread_id=thread_007, owner_email=jake.design@company.com, created_after=2024-08-20T16:30:00Z, audit_id=audit_007, new_status=IN_PROGRESS, updated_by=jake.design@company.com, notes=Review management coordination completed with audit workflow, log_level=INFO, component=review_management"
        ),
        actions=[
            Action(name="GetReviewApprovalsSummary", kwargs={"cycle_id": "cycle_001"}),
            Action(name="GetFigmaArtifactsByStatus", kwargs={"status": "ACTIVE"}),
            Action(name="GetSystemConfigByCategory", kwargs={"category": "gmail_labels"}),
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_006"}),
            Action(name="GetGmailThreadsByLabels", kwargs={"thread_id": "thread_007"}),
            Action(name="GetReleasesByOwner", kwargs={"owner_email": "jake.design@company.com", "created_after": "2024-08-20T16:30:00Z"}),
            Action(name="UpdateAuditStatus", kwargs={"audit_id": "audit_007", "new_status": "IN_PROGRESS", "updated_by": "jake.design@company.com", "notes": "Review management coordination completed with audit workflow"})
        ],
        outputs=[]
    ),
    
    Task(
        annotator="0",
        user_id="user_17",
        instruction=(
            "You function as an audit report management specialist managing the entire audit lifecycle for design system components and accessibility compliance. Your key task consists of overseeing audit_001 for artifact art_001 (Homepage Hero Section) requiring detailed status tracking from COMPLETED through to report generation. This process integrates audit_002 for the accessibility review of art_008 admin panel components necessitating status coordination. The audit management procedure highlights thread_001 priority elevation to HIGH for design review coordination with oversight from emma.creative@company.com, urgent priority escalation for tracking the comprehensive design review, and the escalation_reason 'Critical audit findings require immediate design team attention'. Managing priority requires thorough Gmail thread coordination and detailed documentation of audit statuses. Your coordination should secure flawless audit report production through accurate status handling, effective priority escalation for design review threads, and detailed tracking of audit findings for stakeholder reports. Key parameters include: audit_id=audit_001, new_status=COMPLETED, report_asset_id=asset_001, completion_notes=Design system audit completed with recommendations, thread_001_priority=HIGH, thread_002_priority=NORMAL, thread_001_urgency=Critical audit findings require immediate design team attention, thread_002_urgency=Secondary audit review completed, escalate_to=emma.creative@company.com,jake.design@company.com, audit_type=COMBINED_DS_A11Y, created_after=2024-08-20T15:00:00Z, audit_date_filter=2024-08-18T00:00:00Z, thread_ids=thread_001,thread_002, artifact_ids=art_001,art_008, fix_item_id=item_001, completion_date=2024-08-27T15:00:00Z"
        ),
        actions=[
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_001"}),
            Action(name="UpdateAuditReportStatus", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed with recommendations"}),
            Action(name="GetAuditsByStatus", kwargs={"status": "COMPLETED", "audit_type": "COMBINED_DS_A11Y"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical audit findings require immediate design team attention", "escalate_to": ["emma.creative@company.com", "jake.design@company.com"]}),
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_002"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Secondary audit review completed"}),
            Action(name="GetAuditsByStatus", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"}),
            Action(name="UpdateFixItemStatus", kwargs={"fix_item_id": "item_001", "new_status": "VERIFIED", "completion_date": "2024-08-27T15:00:00Z"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_18",
        instruction=(
            "You serve as an audit report management specialist completing the audit lifecycle for design system components. Adjust audit_001 and audit_002 statuses to COMPLETED and standardize thread priorities to NORMAL/LOW. Key parameters: audit_001:status=COMPLETED,report_asset=asset_001,notes=Design system audit completed and finalized; audit_002:status=COMPLETED,report_asset=asset_007; thread_001:priority=NORMAL,escalate_to=emma.creative@company.com,jake.design@company.com,reason=Audit review completed; thread_002:priority=LOW,reason=Audit follow-up completed"
        ),
        actions=[
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_001"}),
            Action(name="UpdateAuditReportStatus", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed and finalized"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_001", "new_priority": "NORMAL", "urgency_reason": "Audit review completed", "escalate_to": ["emma.creative@company.com", "jake.design@company.com"]}),
            Action(name="UpdateAuditReportStatus", kwargs={"audit_id": "audit_002", "new_status": "COMPLETED", "report_asset_id": "asset_007"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_002", "new_priority": "LOW", "urgency_reason": "Audit follow-up completed"}),
            Action(name="AddTerminalLogEntry", kwargs={"log_message": "Audit finalization completed for audit_001 and audit_002", "log_level": "INFO", "component": "audit_workflow", "user_email": "emma.creative@company.com"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_19",
        instruction=(
            "You are an audit report management specialist tasked with overseeing the complete lifecycle of audits for design system components and ensuring compliance with accessibility standards. Your main duty is to oversee audit_001 for artifact art_001 (Homepage Hero Section), which necessitates thorough tracking from COMPLETED through to final report generation. The process incorporates audit_002 for assessing the accessibility of art_008 admin panel components, demanding status coordination. Central to the audit management process is thread_001, which needs to be escalated to a HIGH priority for the design review coordination under the supervision of emma.creative@company.com. It requires URGENT priority escalation for detailed design review monitoring, with the escalation_reason being 'Critical audit findings require immediate design team attention and stakeholder review'. Managing priority involves detailed coordination via Gmail threads and meticulous documentation of audit statuses. Your efforts in coordination should facilitate the smooth generation of audit reports by accurately managing statuses, escalating design review threads appropriately, tracking audit findings thoroughly for stakeholder reports, and completing the audit lifecycle with correct report asset association. Essential parameters: audit_id=audit_001, new_status=COMPLETED, report_asset_id=asset_001, completion_notes=Design system audit completed with recommendations, thread_001_priority=HIGH, thread_002_priority=NORMAL, thread_001_urgency=Critical audit findings require immediate design team attention, thread_002_urgency=Secondary audit review completed, escalate_to=emma.creative@company.com,jake.design@company.com, audit_type=COMBINED_DS_A11Y, created_after=2024-08-20T15:00:00Z, audit_date_filter=2024-08-18T00:00:00Z, thread_ids=thread_001,thread_002, artifact_ids=art_001,art_008"
        ),
        actions=[
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_001"}),
            Action(name="UpdateAuditReportStatus", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed with recommendations"}),
            Action(name="GetAuditsByStatus", kwargs={"status": "COMPLETED", "audit_type": "COMBINED_DS_A11Y"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical audit findings require immediate design team attention", "escalate_to": ["emma.creative@company.com", "jake.design@company.com"]}),
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_002"}),
            Action(name="GetAuditsByStatus", kwargs={"artifact_id": "art_001", "created_after": "2024-08-20T15:00:00Z"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Secondary audit review completed"}),
            Action(name="GetAuditsByStatus", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_20",
        instruction=(
            "You are an email workflow manager tasked with managing the design review process for the Homepage Hero Section through effective stakeholder communication and approval workflows. It is your responsibility to ensure that the Homepage Hero Section review transitions successfully to an approved status with all necessary coordination among stakeholders. This review process involves thread_001, which necessitates updates, management of labels, and extended communication with stakeholders. The review workflow also includes validating findings from audit_001 and Figma artifacts for art_001, alongside updating the review cycle status to denote approval. The objective is to ensure a seamless move towards production readiness with appropriate documentation and stakeholder notifications. Every action should uphold the integrity of the design review process while ensuring transparent communication among all teams involved in the production handoff. Required constants: audit_id=audit_001, new_status=COMPLETED, updated_by=email_workflow_manager_001, notes=Homepage hero section design review completed and approved, thread_id=thread_001, new_labels=approved,figma-integrated, remove_labels=urgent, recipients=jake.design@company.com,chris.engineer@company.com,anna.brand@company.com,design-team@company.com, cycle_id=cycle_001, approver_id=email_workflow_manager_001, approval_comments=Homepage hero section approved after comprehensive review - updating review cycle status and coordinating with email workflow"
        ),
        actions=[
            Action(name="GetGmailThreadsByLabels", kwargs={"thread_id": "thread_001"}),
            Action(name="GetFigmaArtifactsByStatus", kwargs={"artifact_id": "art_001"}),
            Action(name="GetAuditFindingsSummary", kwargs={"audit_id": "audit_001"}),
            Action(name="UpdateGmailThreadLabels", kwargs={"thread_id": "thread_001", "new_labels": ["approved", "figma-integrated"], "remove_labels": ["urgent"], "update_recipients": ["jake.design@company.com", "chris.engineer@company.com", "anna.brand@company.com", "design-team@company.com"]}),
            Action(name="UpdateReviewCycleStatus", kwargs={"cycle_id": "cycle_001", "new_status": "APPROVED", "approver_id": "email_workflow_manager_001", "comments": "Homepage hero section approved after comprehensive review - updating review cycle status and coordinating with email workflow"}),
            Action(name="UpdateAuditStatus", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "notes": "Homepage hero section design review completed and approved", "updated_by": "email_workflow_manager_001"}),
            Action(name="GetGmailThreadsByLabels", kwargs={"thread_id": "thread_001"}),
            Action(name="GetFigmaArtifactsByStatus", kwargs={"artifact_id": "art_001"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_21",
        instruction=(
            "You are an accessibility compliance specialist tasked with overseeing audit findings coordination and managing fix items within admin panel accessibility initiatives. Your main duty is to coordinate accessibility audits for audit_002, audit_004, and audit_005, requiring comprehensive analysis of findings and updates on the status of fix items through systematic processing. The workflow includes managing the lifecycle of fix items by following appropriate status progression. The workflow for accessibility compliance focuses on verifying item_001 touch target with a VERIFIED status, ensuring item_004 font size compliance with an APPLIED status and coordinating a completion timestamp, and addressing item_002 contrast violations under an IN_PROGRESS status. Implementing fixes requires systematic coordination of status and compliance verification. Your coordination should guarantee thorough analysis of audit findings, appropriate management of fix item lifecycles, and successful tracking of accessibility compliance for reporting to stakeholders and completing the workflow."
        ),
        actions=[
            Action(name="GetAuditFindingsSummary", kwargs={"audit_id": "audit_002"}),
            Action(name="GetAuditFindingsSummary", kwargs={"audit_id": "audit_004"}),
            Action(name="GetAuditFindingsSummary", kwargs={"audit_id": "audit_005"}),
            Action(name="UpdateFixItemStatus", kwargs={"fix_item_id": "item_001", "new_status": "VERIFIED"}),
            Action(name="UpdateFixItemStatus", kwargs={"fix_item_id": "item_004", "new_status": "APPLIED", "completion_date": "2024-08-25T15:30:00Z"}),
            Action(name="UpdateFixItemStatus", kwargs={"fix_item_id": "item_002", "new_status": "IN_PROGRESS"}),
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_007"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_22",
        instruction=(
            "You are responsible as a Figma comment resolution specialist for coordinating accessibility feedback and managing workflows across admin panel header components. Your central responsibility involves coordinating accessibility feedback for art_008 admin panel header where unresolved comments marked with resolved_status False need to be identified and resolved. The workflow also necessitates coordination and status verification for asset_007 admin header export integration. Focusing on accessibility improvements, the workflow includes coordination for comment_006, which involves oversight by the team member jake.design@company.com, targeting HIGH priority accessibility enhancements, and tracking the implementation of comprehensive ARIA labels and keyboard navigation support. Resolving feedback requires coordinating progress status and documenting implementations in detail. Your coordination efforts must ensure efficient communication of accessibility audits through thread_004, effective management of comment lifecycles, and thorough tracking of accessibility compliance for stakeholder reporting and successful completion of the workflow."
        ),
        actions=[
            Action(name="GetFigmaCommentsByArtifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_007"}),
            Action(name="UpdateFigmaCommentStatus", kwargs={"comment_id": "comment_006", "new_status": "IN_PROGRESS", "resolution_notes": "Accessibility improvements in progress - adding ARIA labels and keyboard navigation support", "assignee_email": "jake.design@company.com", "priority_level": "HIGH"}),
            Action(name="GetGmailThreadsByLabels", kwargs={"thread_id": "thread_004"}),
            Action(name="GetFigmaCommentsByArtifact", kwargs={"artifact_id": "art_008", "resolved_status": False})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_23",
        instruction=(
            "Handle the end-to-end process of audit lifecycle management for design system components and ensure accessibility compliance. You are in charge of managing audit_001 for artifact art_001 (Homepage Hero Section), which requires thorough tracking of its status from COMPLETED to the generation of the final report. The workflow also involves coordinating with audit_002 for the accessibility review of art_008 admin panel components, needing status-specific management. Central to this audit management is the thread_001 that demands priority escalation to HIGH for coordinating design reviews under emma.creative@company.com’s supervision, with URGENT priority escalation due to the 'Critical audit findings' necessitating immediate attention from the design team and stakeholders. Managing priorities entails comprehensive Gmail thread operations and meticulous documentation of audit statuses. Your coordination must ensure the smooth production of audit reports by managing statuses properly, effectively handling priority escalations for design review threads, documenting audit findings thoroughly for stakeholder reporting, and successfully completing the audit lifecycle with correct report asset links. Key parameters: audit_id=audit_001, new_status=COMPLETED, report_asset_id=asset_001, completion_notes=Design system audit completed with recommendations, thread_001_priority=HIGH, thread_002_priority=NORMAL, thread_001_urgency=Critical audit findings require immediate design team attention, thread_002_urgency=Secondary audit review completed, escalate_to=emma.creative@company.com,jake.design@company.com, audit_type=COMBINED_DS_A11Y, created_after=2024-08-20T15:00:00Z, audit_date_filter=2024-08-18T00:00:00Z, thread_ids=thread_001,thread_002, artifact_ids=art_001,art_008, log_message=Audit management workflow completed with comprehensive report generation and status tracking, log_level=INFO, component=audit_lifecycle, user_email=emma.creative@company.com"
        ),
        actions=[
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_001"}),
            Action(name="UpdateAuditReportStatus", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed with recommendations"}),
            Action(name="GetAuditsByStatus", kwargs={"status": "COMPLETED", "audit_type": "COMBINED_DS_A11Y"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical audit findings require immediate design team attention", "escalate_to": ["emma.creative@company.com", "jake.design@company.com"]}),
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_002"}),
            Action(name="UpdateAuditReportStatus", kwargs={"audit_id": "audit_002", "new_status": "COMPLETED", "report_asset_id": "asset_007"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Secondary audit review completed"}),
            Action(name="GetAuditsByStatus", kwargs={"status": "COMPLETED", "created_after": "2024-08-20T15:00:00Z"}),
            Action(name="GetAuditsByStatus", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"}),
            Action(name="AddTerminalLogEntry", kwargs={"log_message": "Audit management workflow completed with comprehensive report generation and status tracking", "log_level": "INFO", "component": "audit_lifecycle", "user_email": "emma.creative@company.com"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_24",
        instruction=(
            "Oversee the resolution of Figma comments related to accessibility feedback and manage workflows across the admin panel header components. You need to coordinate accessibility feedback for art_008 admin panel header, identifying and resolving comments marked with resolved_status False. Additionally, make sure to verify and align the status concerning the export integration of asset_007 admin header. This accessibility improvement process hinges on managing comment_006 for accessibility enhancements, which involves oversight by the team member jake.design@company.com, prioritizing HIGH importance on accessibility improvements, and tracking the implementation of comprehensive ARIA labels and keyboard navigation support. Ensure progress status coordination and detailed implementation documentation for feedback resolution. Your efforts should facilitate smooth communication of accessibility audits through thread_004, streamline comment lifecycle management, and maintain thorough tracking of accessibility compliance for stakeholder reports and successful workflow completion. Use resolution_notes=Accessibility improvements in progress - adding ARIA labels and keyboard navigation support,notes=Admin header accessibility export completed with ARIA labels"
        ),
        actions=[
            Action(name="GetFigmaCommentsByArtifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_007"}),
            Action(name="UpdateFigmaCommentStatus", kwargs={"comment_id": "comment_006", "new_status": "IN_PROGRESS", "resolution_notes": "Accessibility improvements in progress - adding ARIA labels and keyboard navigation support", "assignee_email": "jake.design@company.com", "priority_level": "HIGH"}),
            Action(name="GetGmailThreadsByLabels", kwargs={"thread_id": "thread_004"}),
            Action(name="GetFigmaCommentsByArtifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="UpdateAssetExportStatus", kwargs={"asset_id": "asset_007", "new_status": "COMPLETED", "notes": "Admin header accessibility export completed with ARIA labels", "dlp_scan_status": "CLEAN"}),
            Action(name="GetTerminalLogsSummary", kwargs={"log_level": "INFO", "component": "accessibility_coordination"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_25",
        instruction=(
            "As a specialist in audit report management, your role involves handling the complete audit lifecycle for design system components and ensuring accessibility compliance. Your main duty includes overseeing audit_001 for artifact art_001 (Homepage Hero Section), which necessitates thorough tracking of status changes from COMPLETED to the generation of the final report. The process is linked with audit_002 for the accessibility review of art_008 admin panel components, requiring you to coordinate their statuses. The audit management workflow focuses on the escalation of thread_001 to HIGH priority for design review coordination, which involves oversight by emma.creative@company.com, upgrading to URGENT priority for comprehensive design review tracking, and addressing the escalation_reason 'Critical audit findings require immediate design team attention and stakeholder review'. Priority management entails comprehensive coordination of Gmail threads and meticulous documentation of audit statuses. Your coordination efforts should guarantee the smooth generation of audit reports through proper status management, effective design review thread priority escalation, and detailed tracking of audit findings for report to stakeholders. Key parameters include: audit_id=audit_001, new_status=COMPLETED, report_asset_id=asset_001, completion_notes=Design system audit completed with recommendations, thread_001_priority=HIGH, thread_002_priority=NORMAL, thread_001_urgency=Critical audit findings require immediate design team attention, thread_002_urgency=Secondary audit review completed, escalate_to=emma.creative@company.com,jake.design@company.com, audit_type=COMBINED_DS_A11Y, created_after=2024-08-20T15:00:00Z, audit_date_filter=2024-08-18T00:00:00Z, thread_ids=thread_001,thread_002, artifact_ids=art_001,art_008, audit_summary_id=audit_001"
        ),
        actions=[
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_001"}),
            Action(name="UpdateAuditReportStatus", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed with recommendations"}),
            Action(name="GetAuditsByStatus", kwargs={"status": "COMPLETED", "audit_type": "COMBINED_DS_A11Y"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical audit findings require immediate design team attention", "escalate_to": ["emma.creative@company.com", "jake.design@company.com"]}),
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_002"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Secondary audit review completed"}),
            Action(name="GetAuditsByStatus", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"}),
            Action(name="GetAuditSummary", kwargs={"audit_id": "audit_001"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_26",
        instruction=(
            "As a Figma comment resolution specialist, you are in charge of managing accessibility feedback and workflow coordination for admin panel header components. Your primary duty involves managing accessibility feedback for art_008 admin panel header, where unresolved comments with resolved_status False require identification and coordination for resolution. The workflow also demands integration and verification of statuses for asset_007 admin header export. The process of improving accessibility revolves around the coordination of comment_006 accessibility enhancements, with oversight by team member jake.design@company.com, prioritizing HIGH accessibility improvements, and ensuring comprehensive tracking of ARIA labels and keyboard navigation support implementation. Resolving feedback necessitates progress status management and detailed documentation of implementation steps. Your coordination should facilitate seamless communication of accessibility audits via thread_004, efficient handling of the comment lifecycle, and extensive tracking of accessibility compliance for stakeholder reporting and the successful conclusion of the workflow. Utilize resolution_notes Accessibility improvements in progress - adding ARIA labels and keyboard navigation support. Required constants include: plan_id=plan_005, resolution_notes=Accessibility improvements in progress - adding ARIA labels and keyboard navigation support, new_status=IN_PROGRESS"
        ),
        actions=[
            Action(name="GetFigmaCommentsByArtifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_007"}),
            Action(name="UpdateFigmaCommentStatus", kwargs={"comment_id": "comment_006", "new_status": "IN_PROGRESS", "resolution_notes": "Accessibility improvements in progress - adding ARIA labels and keyboard navigation support", "assignee_email": "jake.design@company.com", "priority_level": "HIGH"}),
            Action(name="GetGmailThreadsByLabels", kwargs={"thread_id": "thread_004"}),
            Action(name="GetFigmaCommentsByArtifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="UpdateFixPlanStatus", kwargs={"plan_id": "plan_005", "new_status": "IN_PROGRESS"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_27",
        instruction=(
            "As a Figma comment resolution specialist, you are responsible for managing accessibility feedback coordination and overseeing workflows related to the admin panel header components. Your main duty is to coordinate feedback on accessibility for art_008 admin panel header by identifying and managing unresolved comments with a resolved_status of False. Additionally, the task involves handling asset_007 admin header export integration requiring status checks and coordination adjustments. Significant focus is placed on comment_006 for accessibility improvement under the oversight of jake.design@company.com. This involves implementing HIGH priority accessibility enhancements and tracking the integration of comprehensive ARIA labels along with keyboard navigation support. Your role involves ensuring the coordination of feedback progress statuses and the preparation of detailed implementation documentation. Ensure streamlined accessibility audit communication is maintained through thread_004, oversee an effective comment lifecycle, and manage accessibility compliance tracking to provide accurate stakeholder reporting and achieve workflow completion. You can use resolution_notes Accessibility improvements in progress - adding ARIA labels and keyboard navigation support."
        ),
        actions=[
            Action(name="GetFigmaCommentsByArtifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_007"}),
            Action(name="UpdateFigmaCommentStatus", kwargs={"comment_id": "comment_006", "new_status": "IN_PROGRESS", "resolution_notes": "Accessibility improvements in progress - adding ARIA labels and keyboard navigation support", "assignee_email": "jake.design@company.com", "priority_level": "HIGH"}),
            Action(name="GetGmailThreadsByLabels", kwargs={"thread_id": "thread_004"}),
            Action(name="GetFigmaCommentsByArtifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="AddTerminalLogEntry", kwargs={"log_message": "Accessibility comment resolution workflow completed for art_008 admin panel header", "log_level": "INFO", "component": "accessibility_resolution", "user_email": "jake.design@company.com"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_28",
        instruction=(
            "In your role as an audit report management specialist, your duties include coordinating the finalization of several audits, specifically, audit_001 for the Homepage Hero Section (art_001) and audit_002 for the admin panel components (art_008). Your tasks cover verifying and updating audit statuses, producing final reports, liaising with design and accessibility teams, managing stakeholder communications, and maintaining thorough documentation. For audit_001, ensure the status reflects COMPLETED with report_asset_id=asset_001 and relevant completion notes appended. For audit_002, confirm the status and link it with report_asset_id=asset_007. Oversee thread priorities, giving thread_001 a HIGH priority due to critical findings necessitating immediate design team intervention and setting thread_002 to NORMAL priority for routine review completion. Critical parameters include: - Audit details: * audit_001: COMPLETED status with report_asset_id=asset_001 (COMBINED_DS_A11Y type) * audit_002: COMPLETED status with report_asset_id=asset_007 (A11Y type) * completion_notes=Design system audit completed with recommendations - Thread management: * thread_001: HIGH priority (Critical audit findings require immediate design team attention) * thread_002: NORMAL priority (Secondary audit review completed) * escalate_to=emma.creative@company.com,jake.design@company.com - Date filters: * created_after=2024-08-20T15:00:00Z: Filter audits created after this timestamp * audit_date_filter=2024-08-18T00:00:00Z: Filter audit data for this specific date - References: * thread_ids=thread_001,thread_002 * artifact_ids=art_001,art_008"
        ),
        actions=[
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_001"}),
            Action(name="UpdateAuditReportStatus", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed with recommendations"}),
            Action(name="GetAuditsByStatus", kwargs={"status": "COMPLETED", "audit_type": "COMBINED_DS_A11Y"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical audit findings require immediate design team attention", "escalate_to": ["emma.creative@company.com", "jake.design@company.com"]}),
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_002"}),
            Action(name="UpdateAuditReportStatus", kwargs={"audit_id": "audit_002", "new_status": "COMPLETED", "report_asset_id": "asset_007"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Secondary audit review completed"}),
            Action(name="GetAuditsByStatus", kwargs={"status": "COMPLETED", "created_after": "2024-08-20T15:00:00Z"}),
            Action(name="GetAuditsByStatus", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"}),
            Action(name="AddTerminalLogEntry", kwargs={"log_message": "Audit report management workflow completed for audit_001 and audit_002 with comprehensive status tracking and priority escalation", "log_level": "INFO", "component": "audit_management", "user_email": "emma.creative@company.com"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_29",
        instruction=(
            "As an accessibility compliance specialist, you are in charge of handling audit findings and managing the lifecycle of fix items within admin panel accessibility initiatives. Your role involves conducting a thorough analysis of audit findings, overseeing the lifecycle of fix items, and tracking compliance with accessibility standards. Make it a priority to verify compliance with touch target standards, monitor font size compliance, and identify contrast issues while keeping status updates and documentation precise. Engage with both design and development teams through designated channels to guarantee that all accessibility issues are fully addressed and validated. Utilize the following constants: audit_ids=audit_002,audit_004,audit_005, fix_item_ids=item_001,item_002,item_004, statuses=VERIFIED,APPLIED,IN_PROGRESS, completion_date=2024-08-25T15:30:00Z, comment_id=comment_009, assignee_email=emma.creative@company.com"
        ),
        actions=[
            Action(name="GetAuditFindingsSummary", kwargs={"audit_id": "audit_002"}),
            Action(name="GetAuditFindingsSummary", kwargs={"audit_id": "audit_004"}),
            Action(name="GetAuditFindingsSummary", kwargs={"audit_id": "audit_005"}),
            Action(name="UpdateFixItemStatus", kwargs={"fix_item_id": "item_001", "new_status": "VERIFIED"}),
            Action(name="UpdateFixItemStatus", kwargs={"fix_item_id": "item_004", "new_status": "APPLIED", "completion_date": "2024-08-25T15:30:00Z"}),
            Action(name="UpdateFixItemStatus", kwargs={"fix_item_id": "item_002", "new_status": "IN_PROGRESS"}),
            Action(name="UpdateFigmaCommentStatus", kwargs={"comment_id": "comment_009", "new_status": "RESOLVED", "assignee_email": "emma.creative@company.com"}),
            Action(name="GetAuditSummary", kwargs={"audit_id": "audit_002"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_30",
        instruction=(
            "You serve as a Figma comment resolution specialist, tasked with the coordination of accessibility feedback and management of workflows for admin panel header components. Your main task is the coordination of accessibility feedback for art_008 admin panel header, focusing on identifying and coordinating the resolution of unresolved comments with resolved_status False. Your role also includes managing the export integration of asset_007 admin header, verifying its status and ensuring alignment in coordination. The focus is on the coordination of accessibility enhancements for comment_006, involving supervision from team member jake.design@company.com, prioritizing HIGH priority accessibility improvements, and ensuring the tracking of ARIA label implementations and keyboard navigation support. Progress status coordination and comprehensive implementation documentation are essential for feedback resolution. Your efforts in coordination should guarantee seamless communication for the accessibility audit through thread_004, efficient management of the comment lifecycle, and complete tracking of accessibility compliance for stakeholder reports, leading to successful completion of workflows. Utilize resolution_notes Accessibility improvements in progress - adding ARIA labels and keyboard navigation supportRequired constants: plan_id=plan_005,resolution_notes=Accessibility improvements in progress - adding ARIA labels and keyboard navigation support,new_status=IN_PROGRESS"
        ),
        actions=[
            Action(name="GetFigmaCommentsByArtifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_007"}),
            Action(name="UpdateFigmaCommentStatus", kwargs={"comment_id": "comment_006", "new_status": "IN_PROGRESS", "resolution_notes": "Accessibility improvements in progress - adding ARIA labels and keyboard navigation support", "assignee_email": "jake.design@company.com", "priority_level": "HIGH"}),
            Action(name="GetGmailThreadsByLabels", kwargs={"thread_id": "thread_004"}),
            Action(name="GetFigmaCommentsByArtifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="UpdateFixPlanStatus", kwargs={"plan_id": "plan_005", "new_status": "IN_PROGRESS"}),
            Action(name="AddTerminalLogEntry", kwargs={"log_message": "Figma comment resolution workflow completed for accessibility improvements with fix plan coordination", "log_level": "INFO", "component": "figma_comment_resolution", "user_email": "jake.design@company.com"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_31",
        instruction=(
            "As a specialist in audit report management, you are tasked with overseeing the entire audit lifecycle for design system elements and ensuring they comply with accessibility standards. Your main role includes handling audit_001 for artifact art_001 (Homepage Hero Section), which necessitates comprehensive tracking from COMPLETED to the creation of the final report. The process is linked with audit_002 for the accessibility review of admin panel components art_008, requiring status synchronization. The audit management focus is on escalating thread_001's priority to HIGH for coordinating design review under the supervision of emma.creative@company.com, moving URGENT priority level for in-depth design review tracking, alongside escalation_reason 'Critical audit findings require immediate design team attention and stakeholder review'. Priority management includes thorough coordination via Gmail threads and detailed documentation of the audit status. Your efforts in coordination should guarantee smooth report generation by managing statuses effectively, escalating priority levels for design review threads, and ensuring a detailed record of audit findings for stakeholder presentations. Moreover, you'll obtain asset export summaries to ensure proper documentation and coordination of assets throughout the audit management process. Key parameters: audit_id=audit_001, new_status=COMPLETED, report_asset_id=asset_001, completion_notes=Design system audit completed with recommendations, thread_001_priority=HIGH, thread_002_priority=NORMAL, thread_001_urgency=Critical audit findings require immediate design team attention, thread_002_urgency=Secondary audit review completed, escalate_to=emma.creative@company.com,jake.design@company.com, audit_type=COMBINED_DS_A11Y, created_after=2024-08-20T15:00:00Z, audit_date_filter=2024-08-18T00:00:00Z, thread_ids=thread_001,thread_002, artifact_ids=art_001,art_008"
        ),
        actions=[
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_001"}),
            Action(name="UpdateAuditReportStatus", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed with recommendations"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical audit findings require immediate design team attention", "escalate_to": ["emma.creative@company.com", "jake.design@company.com"]}),
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_002"}),
            Action(name="UpdateAuditReportStatus", kwargs={"audit_id": "audit_002", "new_status": "COMPLETED", "report_asset_id": "asset_007"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Secondary audit review completed"}),
            Action(name="GetAuditsByStatus", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"}),
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_001"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_32",
        instruction=(
            "In the role of a data collection specialist, your duty is to aggregate comprehensive data from various sources to aid in audit and design system coordination. Your goal is to collect and correlate information from Figma artifacts, audit records, asset exports, email communications, and system configurations. The data collection should involve current ACTIVE Figma artifacts, a complete audit summary for audit_003, an export summary for asset_003, all email exchanges from thread_003, releases by emily.ux@company.com since August 22nd, 2024, and the present design system aliases configuration. Once all data is collected, record the completion of this process by logging an INFO level message to the data_collection component log. Required data points: audit_id=audit_003,thread_id=thread_003,owner_email=emily.ux@company.com,log_message=Data collection workflow completed with comprehensive coordination,created_after=2024-08-22T17:00:00Z,category=design_system_aliases"
        ),
        actions=[
            Action(name="GetFigmaArtifactsByStatus", kwargs={"status": "ACTIVE"}),
            Action(name="GetAuditSummary", kwargs={"audit_id": "audit_003"}),
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_003"}),
            Action(name="GetGmailThreadsByLabels", kwargs={"thread_id": "thread_003"}),
            Action(name="GetReleasesByOwner", kwargs={"owner_email": "emily.ux@company.com", "created_after": "2024-08-22T17:00:00Z"}),
            Action(name="GetSystemConfigByCategory", kwargs={"category": "design_system_aliases"}),
            Action(name="AddTerminalLogEntry", kwargs={"log_message": "Data collection workflow completed with comprehensive coordination", "log_level": "INFO", "component": "data_collection", "user_email": "emily.ux@company.com"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_33",
        instruction=(
            "As an audit report management expert, your duties involve handling the complete audit process for design system components and ensuring accessibility compliance is met. Your main task is overseeing audit_001 for artifact art_001 (Homepage Hero Section), which necessitates thorough monitoring from COMPLETED status to final report generation. This workflow connects with audit_002 for accessibility review of art_008 admin panel components, requiring status management. The audit workflow prioritizes thread_001, escalating it to HIGH priority for coordination of design reviews under the supervision of emma.creative@company.com, raising URGENT priority for comprehensive design review tracking, with the reason being 'Critical audit findings require immediate design team attention and stakeholder review'. Priority handling involves detailed Gmail thread coordination and complete documentation of audit statuses. Your efforts should guarantee efficient audit report creation through precise status handling, effective priority elevation for design review threads, detailed tracking of audit findings for stakeholder updates, and the successful conclusion of the audit process with accurate report asset associations. Key parameters include: audit_id=audit_001, new_status=COMPLETED, report_asset_id=asset_001, completion_notes=Design system audit completed with recommendations, thread_001_priority=HIGH, thread_002_priority=NORMAL, thread_001_urgency=Critical audit findings require immediate design team attention, thread_002_urgency=Secondary audit review completed, escalate_to=emma.creative@company.com,jake.design@company.com, audit_type=COMBINED_DS_A11Y, created_after=2024-08-20T15:00:00Z, audit_date_filter=2024-08-18T00:00:00Z, thread_ids=thread_001,thread_002, artifact_ids=art_001,art_008, asset_id=asset_001, log_message=Audit management workflow completed - audit_001 report generated with comprehensive status tracking, log_level=INFO, component=audit_management, user_email=emma.creative@company.com"
        ),
        actions=[
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_001"}),
            Action(name="UpdateAuditReportStatus", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed with recommendations"}),
            Action(name="GetAuditsByStatus", kwargs={"status": "COMPLETED", "audit_type": "COMBINED_DS_A11Y"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical audit findings require immediate design team attention", "escalate_to": ["emma.creative@company.com", "jake.design@company.com"]}),
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_002"}),
            Action(name="GetAuditsByStatus", kwargs={"artifact_id": "art_001", "created_after": "2024-08-20T15:00:00Z"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Secondary audit review completed"}),
            Action(name="GetAuditsByStatus", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"}),
            Action(name="AddTerminalLogEntry", kwargs={"log_message": "Audit management workflow completed - audit_001 report generated with comprehensive status tracking", "log_level": "INFO", "component": "audit_management", "user_email": "emma.creative@company.com"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_34",
        instruction=(
            "As an asset management specialist, you are tasked with managing comprehensive asset management and fix item status processes. Coordinate asset exports, system configuration, and fix item status workflows to align with design system compliance requirements. Place emphasis on managing exports, analyzing system configurations, incorporating audit details, and updating fix item statuses through precise coordination. Interact with development teams via suitable channels to ensure the proper facilitation of all asset management and fix item operations. Required constants are as follows: asset_id=asset_005, category=design_system_aliases, audit_id=audit_006, thread_id=thread_006, owner_email=emma.creative@company.com, created_after=2024-08-21T14:00:00Z, log_level=INFO, component=asset_management, fix_item_id=item_003, new_status=APPLIED, updated_by=emma.creative@company.com, notes=Asset management coordination completed with design system compliance, log_message=Asset management workflow completed with fix item status coordination, terminal_component=asset_management, user_email=emma.creative@company.com"
        ),
        actions=[
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_005"}),
            Action(name="GetSystemConfigByCategory", kwargs={"category": "design_system_aliases"}),
            Action(name="GetAuditSummary", kwargs={"audit_id": "audit_006"}),
            Action(name="GetGmailThreadsByLabels", kwargs={"thread_id": "thread_006"}),
            Action(name="GetReleasesByOwner", kwargs={"owner_email": "emma.creative@company.com", "created_after": "2024-08-21T14:00:00Z"}),
            Action(name="GetTerminalLogsSummary", kwargs={"log_level": "INFO", "component": "asset_management"}),
            Action(name="UpdateFixItemStatus", kwargs={"fix_item_id": "item_003", "new_status": "APPLIED", "updated_by": "emma.creative@company.com", "notes": "Asset management coordination completed with design system compliance"}),
            Action(name="AddTerminalLogEntry", kwargs={"log_message": "Asset management workflow completed with fix item status coordination", "log_level": "INFO", "component": "asset_management", "user_email": "emma.creative@company.com"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_35",
        instruction=(
            "You hold the role of a Figma comment resolution specialist in charge of managing accessibility feedback coordination and overseeing workflow processes concerning admin panel header components. Required constants: artifact_id=art_008, asset_id=asset_007, comment_id=comment_006, assignee_email=jake.design@company.com, priority_level=HIGH, resolution_notes=ARIA_AND_NAV_IMPROVEMENTS_IN_PROGRESS, export_notes=ADMIN_HEADER_EXPORT_COMPLETED, dlp_scan_status=CLEAN, log_message=FIGMA_COMMENT_RESOLUTION_COMPLETED, log_level=INFO, component=figma_comment_resolution, thread_id=thread_004"
        ),
        actions=[
            Action(name="GetFigmaCommentsByArtifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_007"}),
            Action(name="UpdateFigmaCommentStatus", kwargs={"comment_id": "comment_006", "new_status": "IN_PROGRESS", "resolution_notes": "ARIA_AND_NAV_IMPROVEMENTS_IN_PROGRESS", "assignee_email": "jake.design@company.com", "priority_level": "HIGH"}),
            Action(name="GetGmailThreadsByLabels", kwargs={"thread_id": "thread_004"}),
            Action(name="UpdateAssetExportStatus", kwargs={"asset_id": "asset_007", "new_status": "COMPLETED", "notes": "ADMIN_HEADER_EXPORT_COMPLETED", "dlp_scan_status": "CLEAN"}),
            Action(name="AddTerminalLogEntry", kwargs={"log_message": "FIGMA_COMMENT_RESOLUTION_COMPLETED", "log_level": "INFO", "component": "figma_comment_resolution", "user_email": "jake.design@company.com"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_36",
        instruction=(
            "You are tasked with being an audit findings severity management specialist responsible for overseeing audit finding severity updates and the integration of fix plan workflows. Your responsibility includes handling the escalation of audit finding severity with coordination for fix plan status and ensuring effective priority management. Emphasize managing audit finding severity updates for CRITICAL violations, incorporating fix plan delivery coordination and thorough tracking of fix items. Collaborate with development teams through suitable channels to ensure synchronization of all audit findings and fix workflows. Required constants: finding_id=finding_a11y_001, new_severity=CRITICAL, updated_by=chris.engineer@company.com, plan_id=plan_001, delivery_method=TICKETS, owner_email=chris.engineer@company.com, item_id=item_001, fix_item_id=item_001, new_priority=HIGH, priority_reason=Critical audit finding requires immediate fix attention, audit_id=audit_002, violation_type=TOUCH_TARGET, severity=CRITICAL, log_message=Audit findings severity management and fix plan coordination completed"
        ),
        actions=[
            Action(name="UpdateAuditFindingSeverity", kwargs={"finding_id": "finding_a11y_001", "new_severity": "CRITICAL", "updated_by": "chris.engineer@company.com"}),
            Action(name="GetAuditFindingsByType", kwargs={"violation_type": "TOUCH_TARGET", "severity": "CRITICAL"}),
            Action(name="GetFixPlanItems", kwargs={"plan_id": "plan_001"}),
            Action(name="UpdateFixPlanStatus", kwargs={"plan_id": "plan_001", "new_status": "IN_PROGRESS", "delivery_method": "TICKETS", "owner_email": "chris.engineer@company.com"}),
            Action(name="UpdateFixItemPriority", kwargs={"item_id": "item_001", "new_priority": "HIGH", "priority_reason": "Critical audit finding requires immediate fix attention", "updated_by": "chris.engineer@company.com"}),
            Action(name="UpdateFixItemStatus", kwargs={"fix_item_id": "item_001", "new_status": "IN_PROGRESS", "updated_by": "chris.engineer@company.com"}),
            Action(name="AddTerminalLogEntry", kwargs={"log_message": "Audit findings severity management and fix plan coordination completed", "log_level": "INFO", "component": "audit_severity", "user_email": "chris.engineer@company.com"}),
            Action(name="GetAuditSummary", kwargs={"audit_id": "audit_002"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_37",
        instruction=(
            "You are a release diff analysis specialist tasked with handling the examination of variations between design system releases. Your assignment involves scrutinizing release_012 to spot modifications in design system components, overseeing related Figma artifacts, and refreshing the fix plan with your findings. Focus should be placed on pinpointing breaking changes, addressing design system updates, and determining accessibility enhancements within the release. Deliverables should encompass a thorough diff summary, the status of impacted Figma artifacts, and an updated fix plan with distinct action points. Necessary constants: release_id=release_012, status=ACTIVE, asset_id=asset_014, thread_id=thread_014, owner_email=chris.engineer@company.com, created_after=2024-08-23T16:15:00Z, log_level=WARNING, component=release_diff_analysis, plan_id=plan_008, new_plan_status=DELIVERED, delivery_method=COMMENTS, plan_notes=Release diff analysis completed with comprehensive management, analysis_scope=design_system_components, impact_level=high, priority=P1"
        ),
        actions=[
            Action(name="GetReleaseDiffSummary", kwargs={"release_id": "release_012"}),
            Action(name="GetFigmaArtifactsByStatus", kwargs={"status": "ACTIVE"}),
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_014"}),
            Action(name="GetGmailThreadsByLabels", kwargs={"thread_id": "thread_014"}),
            Action(name="GetReleasesByOwner", kwargs={"owner_email": "chris.engineer@company.com", "created_after": "2024-08-23T16:15:00Z"}),
            Action(name="GetTerminalLogsSummary", kwargs={"log_level": "WARNING", "component": "release_diff_analysis"}),
            Action(name="GetReleaseSummary", kwargs={"release_id": "release_012"}),
            Action(name="UpdateFixPlanStatus", kwargs={"plan_id": "plan_008", "new_status": "DELIVERED", "delivery_method": "COMMENTS", "owner_email": "chris.engineer@company.com", "notes": "Release diff analysis completed with comprehensive management"})
        ],
        outputs=[]
    ),
    
    Task(
        annotator="0",
        user_id="user_38",
        instruction=(
            "You are a specialist in resolving Figma comments, charged with handling accessibility feedback coordination and managing workflow across admin panel header components. Your main task is to oversee accessibility feedback coordination for art_008 admin panel header where unresolved comments, with resolved_status marked as False, need identification and resolution coordination. The workflow also demands status verification and coordination alignment for asset_007 admin header export integration. Central to your workflow is coordinating accessibility enhancement for comment_006, involving oversight from the team member jake.design@company.com, focusing on HIGH priority accessibility improvements, and tracking the implementation of detailed ARIA labels and keyboard navigation support. Your coordination responsibilities include managing progress status and meticulously documenting implementations. Your efforts should guarantee smooth communication during the accessibility audit through thread_004, efficient coordination of comment lifecycle, and robust tracking of accessibility compliance for stakeholder reporting and successful workflow execution. You can utilize resolution_notes Accessibility improvements in progress - adding ARIA labels and keyboard navigation support"
        ),
        actions=[
            Action(name="GetFigmaCommentsByArtifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_007"}),
            Action(name="UpdateFigmaCommentStatus", kwargs={"comment_id": "comment_006", "new_status": "IN_PROGRESS", "resolution_notes": "Accessibility improvements in progress - adding ARIA labels and keyboard navigation support", "assignee_email": "jake.design@company.com", "priority_level": "HIGH"}),
            Action(name="GetGmailThreadsByLabels", kwargs={"thread_id": "thread_004"}),
            Action(name="GetFigmaCommentsByArtifact", kwargs={"artifact_id": "art_008", "resolved_status": False})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_39",
        instruction=(
            "As a Figma comment resolution specialist, you are tasked with accessibility feedback coordination and workflow management across admin panel header components. Your main duty entails coordinating accessibility feedback for art_008 admin panel header, identifying and managing resolution for comments marked with resolved_status False. The process also includes ensuring the integration of asset_007 admin header export is verified and coordinated properly. The focus of accessibility enhancement is on comment_006 and involves jake.design@company.com managing team oversight, prioritizing HIGH priority accessibility upgrades, and meticulously tracking the implementation of ARIA labels and keyboard navigation. Your feedback resolution duties should involve coordinating progress status and detailing the implementation documentation. Ensure seamless communication during accessibility audits via thread_004, managing the comment lifecycle effectively, and tracking compliance for stakeholder reporting to complete the workflow successfully. You may utilize resolution_notes Accessibility improvements in progress - adding ARIA labels and keyboard navigation support, asset_export_status=COMPLETED, dlp_scan_status=CLEAN, export_notes=Admin header accessibility export completed with ARIA labels."
        ),
        actions=[
            Action(name="GetFigmaCommentsByArtifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_007"}),
            Action(name="UpdateFigmaCommentStatus", kwargs={"comment_id": "comment_006", "new_status": "IN_PROGRESS", "resolution_notes": "Accessibility improvements in progress - adding ARIA labels and keyboard navigation support", "assignee_email": "jake.design@company.com", "priority_level": "HIGH"}),
            Action(name="GetGmailThreadsByLabels", kwargs={"thread_id": "thread_004"}),
            Action(name="GetFigmaCommentsByArtifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="AddTerminalLogEntry", kwargs={"log_message": "Accessibility comment resolution workflow completed for art_008 admin panel header", "log_level": "INFO", "component": "accessibility_resolution", "user_email": "jake.design@company.com"}),
            Action(name="UpdateAssetExportStatus", kwargs={"asset_id": "asset_007", "new_status": "COMPLETED", "notes": "Admin header accessibility export completed with ARIA labels", "dlp_scan_status": "CLEAN"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_40",
        instruction=(
            "You hold the role of an accessibility compliance specialist in charge of coordinating audit findings and managing fix items within admin panel accessibility projects. Your key task involves coordinating accessibility audits for audit_002, audit_004, and audit_005, handling comprehensive findings analysis and updating fix item statuses systematically. Properly managing the fix item progression is essential in the workflow. Focusing on accessibility compliance, you will verify item_001 touch targets to achieve VERIFIED status, ensure item_004 font size compliance is in APPLIED status with coordination of completion timestamps, and manage item_002 contrast violation remediation in its IN_PROGRESS state. Implementing fixes demands systematic status coordination and verification of compliance. Your role ensures thorough analysis of audit findings, appropriate lifecycle management of fix items, and effective tracking of compliance for stakeholder reports to conclude the workflow successfully."
        ),
        actions=[
            Action(name="GetAuditFindingsSummary", kwargs={"audit_id": "audit_002"}),
            Action(name="GetAuditFindingsSummary", kwargs={"audit_id": "audit_004"}),
            Action(name="GetAuditFindingsSummary", kwargs={"audit_id": "audit_005"}),
            Action(name="UpdateFixItemStatus", kwargs={"fix_item_id": "item_001", "new_status": "VERIFIED"}),
            Action(name="UpdateFixItemStatus", kwargs={"fix_item_id": "item_004", "new_status": "APPLIED", "completion_date": "2024-08-25T15:30:00Z"}),
            Action(name="UpdateFixItemStatus", kwargs={"fix_item_id": "item_002", "new_status": "IN_PROGRESS"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_41",
        instruction=(
            "Handle the entire audit lifecycle for design system components and accessibility compliance as an audit report management specialist. Your main duty includes overseeing audit_001 for artifact art_001 (Homepage Hero Section) which demands thorough status tracking from COMPLETED to the generation of the final report. The process is integrated with audit_002 for the accessibility evaluation of art_008 admin panel components requiring coordinated status management. The audit management workflow focuses on elevating thread_001 priority to HIGH for design review coordination under emma.creative@company.com supervision, with URGENT escalation for complete design review monitoring, and an escalation_reason 'Critical audit findings require immediate design team attention and stakeholder review'. The priority handling involves detailed Gmail thread coordination and precise audit status documentation. Ensure seamless audit report production via proper status handling, efficient priority escalation for design review threads, and thorough tracking of audit findings for stakeholder reporting. Key parameters: audit_id=audit_001, new_status=COMPLETED, report_asset_id=asset_001, completion_notes=Design system audit completed with recommendations, thread_001_priority=HIGH, thread_002_priority=NORMAL, thread_001_urgency=Critical audit findings require immediate design team attention, thread_002_urgency=Secondary audit review completed, escalate_to=emma.creative@company.com,jake.design@company.com, audit_type=COMBINED_DS_A11Y, created_after=2024-08-20T15:00:00Z, audit_date_filter=2024-08-18T00:00:00Z, thread_ids=thread_001,thread_002, artifact_ids=art_001,art_008"
        ),
        actions=[
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_001"}),
            Action(name="UpdateAuditReportStatus", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed with recommendations"}),
            Action(name="GetAuditsByStatus", kwargs={"status": "COMPLETED", "audit_type": "COMBINED_DS_A11Y"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical audit findings require immediate design team attention", "escalate_to": ["emma.creative@company.com", "jake.design@company.com"]}),
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_002"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Secondary audit review completed"}),
            Action(name="GetAuditsByStatus", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"}),
            Action(name="AddTerminalLogEntry", kwargs={"log_message": "Audit management workflow completed for audit_001 and audit_002 with critical findings escalation", "log_level": "INFO", "component": "audit_management", "user_email": "emma.creative@company.com"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_42",
        instruction=(
            "Coordinate the complete audit process for design system components and accessibility compliance as an audit report management specialist. Oversee audit_001 for artifact art_001 (Homepage Hero Section), requiring full status monitoring from COMPLETED to final report preparation. The workflow aligns with audit_002 for accessibility scrutiny of art_008 admin panel components needing status synchronization. The audit management framework emphasizes escalating thread_001 priority to HIGH for design review coordination under emma.creative@company.com guidance, featuring URGENT priority advancement for exhaustive design review tracking, and an escalation_reason 'Critical audit findings require immediate design team attention and stakeholder review'. Managing priority involves extensive Gmail thread coordination and detailed audit status reporting. Your coordination should facilitate smooth audit report synthesis via accurate status management, efficient design review thread priority escalation, comprehensive audit findings tracking for stakeholder communication, and the successful conclusion of the audit process with suitable report asset correlations. Key parameters: audit_id=audit_001, new_status=COMPLETED, report_asset_id=asset_001, completion_notes=Design system audit completed with recommendations, thread_001_priority=HIGH, thread_002_priority=NORMAL, thread_001_urgency=Critical audit findings require immediate design team attention, thread_002_urgency=Secondary audit review completed, escalate_to=emma.creative@company.com,jake.design@company.com, audit_type=COMBINED_DS_A11Y, created_after=2024-08-20T15:00:00Z, audit_date_filter=2024-08-18T00:00:00Z, thread_ids=thread_001,thread_002, artifact_ids=art_001,art_008, category=audit_lifecycle_config"
        ),
        actions=[
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_001"}),
            Action(name="UpdateAuditReportStatus", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed with recommendations"}),
            Action(name="GetAuditsByStatus", kwargs={"status": "COMPLETED", "audit_type": "COMBINED_DS_A11Y"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical audit findings require immediate design team attention", "escalate_to": ["emma.creative@company.com", "jake.design@company.com"]}),
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_002"}),
            Action(name="UpdateAuditReportStatus", kwargs={"audit_id": "audit_002", "new_status": "COMPLETED", "report_asset_id": "asset_007"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Secondary audit review completed"}),
            Action(name="GetAuditsByStatus", kwargs={"status": "COMPLETED", "created_after": "2024-08-20T15:00:00Z"}),
            Action(name="GetAuditsByStatus", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"}),
            Action(name="GetSystemConfigByCategory", kwargs={"category": "audit_lifecycle_config"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_43",
        instruction=(
            "As an audit report management specialist, your task involves overseeing the entire audit lifecycle for design system components and ensuring accessibility compliance. Your main duty is to manage audit_001 pertaining to artifact art_001 (Homepage Hero Section), which necessitates thorough status monitoring from COMPLETED to the creation of the final report. This process connects with audit_002 for the accessibility review of art_008 admin panel elements, demanding status coordination. The core of the audit management workflow is shifting thread_001 to HIGH priority to facilitate design review coordination under emma.creative@company.com's supervision, with URGENT priority level escalation for meticulous design review tracking, and the escalation_reason being 'Critical audit findings require immediate design team attention and stakeholder review'. You must effectively manage priorities, requiring extensive Gmail thread coordination and meticulous documentation of audit statuses. Your orchestration should guarantee smooth generation of the audit report through adept status handling, potent priority escalation for design review threads, meticulous tracking of audit findings for stakeholder reporting, and triumphant completion of the audit lifecycle with correct report asset associations. Key parameters: audit_id=audit_001, new_status=COMPLETED, report_asset_id=asset_001, completion_notes=Design system audit completed with recommendations, thread_001_priority=HIGH, thread_002_priority=NORMAL, thread_001_urgency=Critical audit findings require immediate design team attention, thread_002_urgency=Secondary audit review completed, escalate_to=emma.creative@company.com,jake.design@company.com, audit_type=COMBINED_DS_A11Y, created_after=2024-08-20T15:00:00Z, audit_date_filter=2024-08-18T00:00:00Z, thread_ids=thread_001,thread_002, artifact_ids=art_001,art_008, asset_id=asset_001"
        ),
        actions=[
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_001"}),
            Action(name="UpdateAuditReportStatus", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed with recommendations"}),
            Action(name="GetAuditsByStatus", kwargs={"status": "COMPLETED", "audit_type": "COMBINED_DS_A11Y"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical audit findings require immediate design team attention", "escalate_to": ["emma.creative@company.com", "jake.design@company.com"]}),
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_002"}),
            Action(name="GetAuditsByStatus", kwargs={"artifact_id": "art_001", "created_after": "2024-08-20T15:00:00Z"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Secondary audit review completed"}),
            Action(name="GetAuditsByStatus", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"}),
            Action(name="GetSystemConfigByCategory", kwargs={"category": "audit_config"}),
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_001"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_44",
        instruction=(
            "As an audit report management specialist, you are tasked with supervising the complete audit lifecycle for design system components and achieving accessibility compliance. Your foremost responsibility is managing audit_001 related to artifact art_001 (Homepage Hero Section), which demands detailed status tracking from COMPLETED to final report production. This sequence integrates with audit_002 for the accessibility evaluation of art_008 admin panel components needing status coordination. At the heart of the audit management workflow is the escalation of thread_001 to HIGH priority for design review coordination under emma.creative@company.com's oversight, with an URGENT priority level escalation for all-encompassing design review tracking, and the escalation_reason stated as 'Critical audit findings require immediate design team attention and stakeholder review'. The management of priorities necessitates exhaustive Gmail thread coordination as well as detailed audit status documentation. Your organizational abilities should ensure the effortless generation of audit reports through effective status management, strong priority escalation for design review threads, diligent tracking of audit findings for stakeholder reporting, and successful closure of the audit lifecycle with apt report asset integrations. Key parameters: audit_id=audit_001, new_status=COMPLETED, report_asset_id=asset_001, completion_notes=Design system audit completed with recommendations, thread_001_priority=HIGH, thread_002_priority=NORMAL, thread_001_urgency=Critical audit findings require immediate design team attention, thread_002_urgency=Secondary audit review completed, escalate_to=emma.creative@company.com,jake.design@company.com, audit_type=COMBINED_DS_A11Y, created_after=2024-08-20T15:00:00Z, audit_date_filter=2024-08-18T00:00:00Z, thread_ids=thread_001,thread_002, artifact_ids=art_001,art_008, audit_002_status=COMPLETED, updated_by=emma.creative@company.com"
        ),
        actions=[
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_001"}),
            Action(name="UpdateAuditReportStatus", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed with recommendations"}),
            Action(name="GetAuditsByStatus", kwargs={"status": "COMPLETED", "audit_type": "COMBINED_DS_A11Y"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical audit findings require immediate design team attention", "escalate_to": ["emma.creative@company.com", "jake.design@company.com"]}),
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_002"}),
            Action(name="GetAuditsByStatus", kwargs={"artifact_id": "art_001", "created_after": "2024-08-20T15:00:00Z"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Secondary audit review completed"}),
            Action(name="GetAuditsByStatus", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"}),
            Action(name="GetSystemConfigByCategory", kwargs={"category": "audit_config"}),
            Action(name="UpdateAuditStatus", kwargs={"audit_id": "audit_002", "new_status": "COMPLETED", "updated_by": "emma.creative@company.com"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_45",
        instruction=(
            "You hold the position of a review management coordination specialist charged with managing extensive review processes and audit status updates. Your role involves orchestrating review cycle coordination, artifact monitoring, and handling the management of audit statuses for components of the design system. Prioritize managing review approvals, verifying active artifacts, conducting system configuration checks, and coordinating audit statuses with proper workflow oversight. Collaborate with UX teams via suitable channels to guarantee all review management procedures are accurately tracked and updated. Required constants: cycle_id=cycle_001, status=ACTIVE, category=gmail_labels, asset_id=asset_006, thread_id=thread_007, owner_email=jake.design@company.com, created_after=2024-08-20T16:30:00Z, audit_id=audit_007, new_status=IN_PROGRESS, updated_by=jake.design@company.com, notes=Review management coordination completed with audit workflow, log_level=INFO, component=review_management"
        ),
        actions=[
            Action(name="GetReviewApprovalsSummary", kwargs={"cycle_id": "cycle_001"}),
            Action(name="GetFigmaArtifactsByStatus", kwargs={"status": "ACTIVE"}),
            Action(name="GetSystemConfigByCategory", kwargs={"category": "gmail_labels"}),
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_006"}),
            Action(name="GetGmailThreadsByLabels", kwargs={"thread_id": "thread_007"}),
            Action(name="GetReleasesByOwner", kwargs={"owner_email": "jake.design@company.com", "created_after": "2024-08-20T16:30:00Z"}),
            Action(name="UpdateAuditStatus", kwargs={"audit_id": "audit_007", "new_status": "IN_PROGRESS", "updated_by": "jake.design@company.com", "notes": "Review management coordination completed with audit workflow"}),
            Action(name="GetAuditSummary", kwargs={"audit_id": "audit_007"})
        ],
        outputs=[]
    ),
    
    Task(
        annotator="0",
        user_id="user_46",
        instruction=(
            "You are tasked as a review cycle SLA management specialist with the responsibility of overseeing review cycle escalation and the management of integrated audit workflows. Your duty involves orchestrating review cycle SLA coordination alongside audit status management, ensuring efficient escalation tracking. Prioritize managing the transitions of review cycle statuses from NEEDS_REVIEW to ESCALATED, inclusive of audit status coordination and comprehensive logging. Engage with review teams via appropriate channels to ensure all SLA breaches and audit workflows are seamlessly synchronized. Required constants: cycle_id=cycle_001, artifact_id=art_001, new_status=ESCALATED, audit_id=audit_001, audit_status=IN_PROGRESS, updated_by=emma.creative@company.com, thread_id=thread_001, priority_level=HIGH, urgency_reason=SLA breach requires immediate escalation, escalate_to=emma.creative@company.com, log_level=WARNING, component=review_sla, after_timestamp=2024-08-20T15:00:00Z, message_pattern=escalation, log_message=Review cycle SLA escalation completed with audit integration, asset_id=asset_001, export_status=COMPLETED, export_notes=SLA escalation asset export completed, dlp_scan_status=CLEAN"
        ),
        actions=[
            Action(name="GetReviewApprovalsSummary", kwargs={"cycle_id": "cycle_001"}),
            Action(name="UpdateReviewCycleStatus", kwargs={"cycle_id": "cycle_001", "new_status": "ESCALATED", "reviewer_email": "emma.creative@company.com", "completion_notes": "SLA breach requires immediate escalation"}),
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_001"}),
            Action(name="UpdateAuditStatus", kwargs={"audit_id": "audit_001", "new_status": "IN_PROGRESS", "updated_by": "emma.creative@company.com"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "SLA breach requires immediate escalation"}),
            Action(name="AddTerminalLogEntry", kwargs={"log_message": "Review cycle SLA escalation completed with audit integration", "log_level": "WARNING", "component": "review_sla", "user_email": "emma.creative@company.com"}),
            Action(name="GetFilteredLogEntries", kwargs={"log_level": "WARNING", "component": "review_sla", "after_timestamp": "2024-08-20T15:00:00Z", "message_pattern": "escalation"}),
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_001"}),
            Action(name="UpdateAssetExportStatus", kwargs={"asset_id": "asset_001", "new_status": "COMPLETED", "notes": "SLA escalation asset export completed", "dlp_scan_status": "CLEAN"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_47",
        instruction=(
            "You are an initial audit setup management specialist responsible for handling comprehensive audit initialization workflows and tracking discovery/progress processes. Your duties include managing initial audit setup coordination, handling finding discovery, initializing progress, and coordinating system processes for enterprise audit setup management. Focus on handling audit finding details discovery, tracking initial progress, initializing status, and coordinating release workflows within a comprehensive initial audit setup. Work with audit setup teams through appropriate channels to ensure all initial audit setup and discovery workflows are orchestrated correctly. Furthermore, you will retrieve comprehensive audit summaries to ensure proper oversight and coordination during the audit initialization process. Required constants: audit_id=audit_001, finding_id=finding_ds_001, include_resolved=False, progress_percentage=15, progress_notes=Initial audit setup commenced with comprehensive discovery, updated_by=emma.creative@company.com, new_finding_status=OPEN, finding_notes=Initial audit finding discovered and opened for comprehensive analysis, release_id=release_001, category=design_system_aliases, thread_id=thread_001, owner_email=emma.creative@company.com, created_after=2024-08-20T10:00:00Z, log_level=INFO, component=initial_audit_setup"
        ),
        actions=[
            Action(name="GetAuditFindingDetails", kwargs={"audit_id": "audit_001", "finding_id": "finding_ds_001", "include_resolved": False}),
            Action(name="UpdateAuditProgress", kwargs={"audit_id": "audit_001", "progress_percentage": 15, "notes": "Initial audit setup commenced with comprehensive discovery", "updated_by": "emma.creative@company.com"}),
            Action(name="UpdateAuditFindingStatus", kwargs={"finding_id": "finding_ds_001", "new_status": "OPEN", "notes": "Initial audit finding discovered and opened for comprehensive analysis", "updated_by": "emma.creative@company.com"}),
            Action(name="GetReleaseSummary", kwargs={"release_id": "release_001"}),
            Action(name="GetSystemConfigByCategory", kwargs={"category": "design_system_aliases"}),
            Action(name="GetGmailThreadsByLabels", kwargs={"thread_id": "thread_001"}),
            Action(name="GetReleasesByOwner", kwargs={"owner_email": "emma.creative@company.com", "created_after": "2024-08-20T10:00:00Z"}),
            Action(name="GetTerminalLogsSummary", kwargs={"log_level": "INFO", "component": "initial_audit_setup"}),
            Action(name="GetAuditSummary", kwargs={"audit_id": "audit_001"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_48",
        instruction=(
            "You are a design system component audit specialist tasked with handling comprehensive design system audits and managing thread priorities for component workflows. Your main responsibility entails audit_002 coordination for design system components that require comprehensive status tracking and thread priority management for component review coordination. The workflow integrates approval verification and thread escalation for preparing the design system release. The design system coordination workflow is centered on thorough audit tracking with oversight by emma.creative@company.com, managing HIGH priority for thread_001 in design system coordination, and performing detailed approval verification across design system workflows. Your coordination efforts should ensure seamless design system audit handling through comprehensive status tracking, effective thread priority management for component reviews, and detailed approval verification for design system workflows alongside proper coordination with the design team and release preparation tracking. Key parameters: audit_002_id=audit_002, audit_002_status=COMPLETED, art_008_id=art_008, audit_type=A11Y, thread_001_id=thread_001, thread_008_id=thread_008, thread_001_priority=HIGH, thread_008_priority=NORMAL, thread_001_urgency=Design system component review requires immediate coordination, thread_008_urgency=Design system follow-up coordination completed, completion_notes=Design system component audit completed successfully, approval_002_id=approval_002, cycle_002_id=cycle_002, escalate_to=emma.creative@company.com,design.system@company.com, release_owner=emma.creative@company.com, release_start_date=2024-08-20T13:00:00Z"
        ),
        actions=[
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_002"}),
            Action(name="UpdateAuditReportStatus", kwargs={"audit_id": "audit_002", "new_status": "COMPLETED", "completion_notes": "Design system component audit completed successfully"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Design system component review requires immediate coordination", "escalate_to": ["emma.creative@company.com", "design.system@company.com"]}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_008", "new_priority": "NORMAL", "urgency_reason": "Design system follow-up coordination completed"}),
            Action(name="GetReviewApprovalsSummary", kwargs={"approval_id": "approval_002", "cycle_id": "cycle_002"}),
            Action(name="GetAuditsByStatus", kwargs={"artifact_id": "art_008", "audit_type": "A11Y"}),
            Action(name="GetReleasesByOwner", kwargs={"owner_email": "emma.creative@company.com", "created_after": "2024-08-20T13:00:00Z"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_49",
        instruction=(
            "You are a Figma comment resolution expert tasked with handling accessibility feedback coordination and managing workflows across admin panel header components. Your main duty includes coordinating accessibility feedback for art_008 admin panel header, where unresolved comments tagged with resolved_status False need to be identified and resolved. The workflow also incorporates the export integration of asset_007 admin header, necessitating status verification and alignment in coordination. The accessibility enhancement workflow focuses on the coordination of comment_006 accessibility improvements involving oversight by jake.design@company.com, prioritizing HIGH priority accessibility upgrades, and tracking the implementation of comprehensive ARIA labels and keyboard navigation support. Resolving feedback entails coordinating progress status and documenting detailed implementations. Your coordination efforts should guarantee smooth accessibility audit communication through thread_004, efficient comment lifecycle management, and extensive tracking of accessibility compliance for stakeholder reporting and successful workflow finalization. Parameters: log_message=Figma comment resolution workflow completed for comment_006 accessibility improvements,note=Admin header accessibility export completed with ARIA labels"
        ),
        actions=[
            Action(name="GetFigmaCommentsByArtifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_007"}),
            Action(name="UpdateFigmaCommentStatus", kwargs={"comment_id": "comment_006", "new_status": "IN_PROGRESS", "resolution_notes": "Accessibility improvements in progress - adding ARIA labels and keyboard navigation support", "assignee_email": "jake.design@company.com", "priority_level": "HIGH"}),
            Action(name="GetGmailThreadsByLabels", kwargs={"thread_id": "thread_004"}),
            Action(name="GetFigmaCommentsByArtifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="UpdateAssetExportStatus", kwargs={"asset_id": "asset_007", "new_status": "COMPLETED", "notes": "Admin header accessibility export completed with ARIA labels", "dlp_scan_status": "CLEAN"}),
            Action(name="AddTerminalLogEntry", kwargs={"log_message": "Figma comment resolution workflow completed for comment_006 accessibility improvements", "log_level": "INFO", "component": "figma_comment_resolution", "user_email": "jake.design@company.com"}),
            Action(name="GetAuditsByStatus", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_50",
        instruction=(
            "You are tasked as an email workflow manager to orchestrate the Homepage Hero Section design review process through stakeholder communication and approval workflows. Your main focus is on thread_001, which currently has design-review and urgent labels but requires shifting to approved and figma-integrated status for production readiness. The coordination with stakeholders needs to expand to include jake.design@company.com, chris.engineer@company.com, anna.brand@company.com, and design-team@company.com, along with detailed handoff documentation noting the conclusion of the design review and recipient list expansion for production coordination. The review workflow includes audit_001 findings and art_001 figma artifacts for status verification; cycle_001 review cycle necessitates an APPROVED status transition with authorization from email_workflow_manager_001 and comprehensive approval comments regarding the completion of the homepage hero section and email workflow coordination. Your workflow coordination should ensure a smooth transition from an urgent review status to an approved production-ready status with appropriate label management, expanded stakeholder communication, and a completed integrated email workflow and design review process. Place a comment stating Homepage hero section approved after a comprehensive review - updating review cycle status and aligning with email workflow. Additionally, modify the audit status to COMPLETED with detailed notes about the design review completion. Required constants: audit_id=audit_001, new_status=COMPLETED, updated_by=email_workflow_manager_001, notes=Homepage hero section design review completed and approved, asset_id=asset_001"
        ),
        actions=[
            Action(name="GetGmailThreadsByLabels", kwargs={"thread_id": "thread_001"}),
            Action(name="GetFigmaArtifactsByStatus", kwargs={"artifact_id": "art_001"}),
            Action(name="GetAuditFindingsSummary", kwargs={"audit_id": "audit_001"}),
            Action(name="UpdateGmailThreadLabels", kwargs={"thread_id": "thread_001", "new_labels": ["approved", "figma-integrated"], "remove_labels": ["urgent"], "update_recipients": ["jake.design@company.com", "chris.engineer@company.com", "anna.brand@company.com", "design-team@company.com"]}),
            Action(name="UpdateReviewCycleStatus", kwargs={"cycle_id": "cycle_001", "new_status": "APPROVED", "approver_id": "email_workflow_manager_001", "comments": "Homepage hero section approved after comprehensive review - updating review cycle status and coordinating with email workflow"}),
            Action(name="UpdateAuditStatus", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "notes": "Homepage hero section design review completed and approved", "updated_by": "email_workflow_manager_001"}),
            Action(name="GetGmailThreadsByLabels", kwargs={"thread_id": "thread_001"}),
            Action(name="GetFigmaArtifactsByStatus", kwargs={"artifact_id": "art_001"}),
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_001"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_51",
        instruction=(
            "You are a review cycle SLA management specialist tasked with handling review cycle escalation and integrated audit workflow organization. Your job is to supervise review cycle SLA handling with audit status management and guarantee accurate escalation monitoring. Emphasize overseeing review cycle status changes from NEEDS_REVIEW to ESCALATED, including audit status organization and thorough documentation. Collaborate with review teams via suitable channels to confirm all SLA violations and audit workflows are correctly harmonized. Required constants: cycle_id=cycle_001, artifact_id=art_001, new_status=ESCALATED, audit_id=audit_001, audit_status=IN_PROGRESS, updated_by=emma.creative@company.com, thread_id=thread_001, priority_level=HIGH, urgency_reason=SLA breach requires immediate escalation, escalate_to=emma.creative@company.com, log_level=WARNING, component=review_sla, after_timestamp=2024-08-20T15:00:00Z, message_pattern=escalation, log_message=Review cycle SLA escalation completed with audit integration, asset_id=asset_001"
        ),
        actions=[
            Action(name="GetReviewApprovalsSummary", kwargs={"cycle_id": "cycle_001"}),
            Action(name="UpdateReviewCycleStatus", kwargs={"cycle_id": "cycle_001", "new_status": "ESCALATED", "reviewer_email": "emma.creative@company.com", "completion_notes": "SLA breach requires immediate escalation"}),
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_001"}),
            Action(name="UpdateAuditStatus", kwargs={"audit_id": "audit_001", "new_status": "IN_PROGRESS", "updated_by": "emma.creative@company.com"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "SLA breach requires immediate escalation"}),
            Action(name="AddTerminalLogEntry", kwargs={"log_message": "Review cycle SLA escalation completed with audit integration", "log_level": "WARNING", "component": "review_sla", "user_email": "emma.creative@company.com"}),
            Action(name="GetFilteredLogEntries", kwargs={"log_level": "WARNING", "component": "review_sla", "after_timestamp": "2024-08-20T15:00:00Z", "message_pattern": "escalation"}),
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_001"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_52",
        instruction=(
            "You are a Figma comment resolution specialist in charge of accessibility feedback handling and workflow management over admin panel header components. Your main responsibility entails accessibility feedback coordination for art_008 admin panel header where unresolved comments with resolved_status False need identification and resolution organization. The workflow also requires asset_007 admin header export integration needing status verification and collaboration alignment. The accessibility enhancement workflow focuses on comment_006 accessibility improvement coordination involving jake.design@company.com team member oversight, HIGH priority accessibility modifications, and extensive ARIA labels and keyboard navigation support implementation monitoring. The feedback resolution necessitates progress status collaboration and thorough implementation documentation. Your coordination efforts should assure smooth accessibility audit communication through thread_004, efficient comment lifecycle handling, and comprehensive accessibility compliance monitoring for stakeholder reporting and successful workflow completion. You can use resolution_notes Accessibility improvements in progress - adding ARIA labels and keyboard navigation support"
        ),
        actions=[
            Action(name="GetFigmaCommentsByArtifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_007"}),
            Action(name="UpdateFigmaCommentStatus", kwargs={"comment_id": "comment_006", "new_status": "IN_PROGRESS", "resolution_notes": "Accessibility improvements in progress - adding ARIA labels and keyboard navigation support", "assignee_email": "jake.design@company.com", "priority_level": "HIGH"}),
            Action(name="GetGmailThreadsByLabels", kwargs={"thread_id": "thread_004"}),
            Action(name="GetFigmaCommentsByArtifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="AddTerminalLogEntry", kwargs={"log_message": "Figma comment resolution workflow completed for accessibility improvements", "log_level": "INFO", "component": "figma_comment_resolution", "user_email": "jake.design@company.com"}),
            Action(name="UpdateAssetExportStatus", kwargs={"asset_id": "asset_007", "new_status": "COMPLETED", "notes": "Admin header accessibility export completed with ARIA labels", "dlp_scan_status": "CLEAN"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_53",
        instruction=(
            "You are tasked with audit report management, overseeing the complete audit process for design system components in terms of accessibility compliance. Your main duty is to handle audit_001 for the artifact art_001 (Homepage Hero Section), which necessitates thorough tracking of the status from COMPLETED to generating the final report. This procedure connects with audit_002 for an accessibility review of the art_008 admin panel components, requiring coordination of the status. The audit management process prioritizes thread_001, elevating its importance to HIGH for design review coordination that includes oversight by emma.creative@company.com, URGENT priority elevation for tracking the comprehensive design review, and the escalation_reason is articulated as 'Critical audit findings require immediate design team attention and stakeholder review'. Managing priority necessitates detailed Gmail thread coordination along with complete audit status documentation. Your coordination should ensure smooth generation of audit reports through appropriate status handling, efficient priority escalation for design review threads, thorough audit findings tracking for stakeholder reporting, and the successful conclusion of the audit lifecycle with correct report asset links. Essential parameters: audit_id=audit_001, new_status=COMPLETED, report_asset_id=asset_001, completion_notes=Design system audit completed with recommendations, thread_001_priority=HIGH, thread_002_priority=NORMAL, thread_001_urgency=Critical audit findings require immediate design team attention, thread_002_urgency=Secondary audit review completed, escalate_to=emma.creative@company.com,jake.design@company.com, audit_type=COMBINED_DS_A11Y, created_after=2024-08-20T15:00:00Z, audit_date_filter=2024-08-18T00:00:00Z, thread_ids=thread_001,thread_002, artifact_ids=art_001,art_008, asset_id=asset_001, log_message=Audit management workflow completed with comprehensive tracking and report generation, log_level=INFO, component=audit_management, user_email=emma.creative@company.com"
        ),
        actions=[
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_001"}),
            Action(name="UpdateAuditReportStatus", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed with recommendations"}),
            Action(name="GetAuditsByStatus", kwargs={"status": "COMPLETED", "audit_type": "COMBINED_DS_A11Y"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical audit findings require immediate design team attention", "escalate_to": ["emma.creative@company.com", "jake.design@company.com"]}),
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_002"}),
            Action(name="GetAuditsByStatus", kwargs={"artifact_id": "art_001", "created_after": "2024-08-20T15:00:00Z"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Secondary audit review completed"}),
            Action(name="GetAuditsByStatus", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"}),
            Action(name="GetSystemConfigByCategory", kwargs={"category": "audit_config"}),
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_001"}),
            Action(name="GetFigmaArtifactsByStatus", kwargs={"artifact_id": "art_001", "status": "APPROVED"}),
            Action(name="AddTerminalLogEntry", kwargs={"log_message": "Audit management workflow completed with comprehensive tracking and report generation", "log_level": "INFO", "component": "audit_management", "user_email": "emma.creative@company.com"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_54",
        instruction=(
            "You are in charge of the accessibility audit, responsible for bringing the audit process to a conclusion. Your assignment is to ensure that the status of audit_001 is updated to reflect the resolution of design system findings accurately. You need to align a button component with Button-Primary-v1.2 to assure accessibility compliance. Once the audit is finished, you should change the review cycle cycle_001 status to APPROVED to signify the audit's conclusion. As part of your duties, confirm the export status of asset_001 to verify that all components are documented appropriately. Essential parameters for your updates should include: audit_id=audit_001, new_status=COMPLETED, notes='Button component mapped to Button-Primary-v1.2 for accessibility compliance', updated_by=alice.designer@company.com, cycle_id=cycle_001, status_notes='Audit completed with component mapping updates', asset_id=asset_001"
        ),
        actions=[
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_001"}),
            Action(name="UpdateAuditStatus", kwargs={
                "audit_id": "audit_001",
                "new_status": "COMPLETED",
                "notes": "Button component mapped to Button-Primary-v1.2 for accessibility compliance",
                "updated_by": "alice.designer@company.com"
            }),
            Action(name="GetReviewApprovalsSummary", kwargs={"cycle_id": "cycle_001"}),
            Action(name="UpdateReviewCycleStatus", kwargs={
                "cycle_id": "cycle_001",
                "new_status": "APPROVED",
                "status_notes": "Audit completed with component mapping updates",
                "updated_by": "alice.designer@company.com"
            }),
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_001"}),
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_001"}),
            Action(name="GetReviewApprovalsSummary", kwargs={"cycle_id": "cycle_001"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_55",
        instruction=(
            "You are a Figma comment resolution specialist tasked with ensuring accessibility feedback coordination and workflow management concerning admin panel header components. Your main duty is to handle accessibility feedback coordination for art_008 admin panel header, focusing on locating unresolved comments with resolved_status False and coordinating their resolution. The workflow also includes managing asset_007 admin header export integration, necessitating status verification and coordination alignment. A central aspect of the accessibility improvement process is coordinating comment_006 accessibility enhancements, overseeing team member jake.design@company.com, addressing HIGH priority accessibility improvements, and tracking the execution of comprehensive ARIA labels and keyboard accessibility support. The progression of feedback resolution demands coordination of progress status and the meticulous documentation of implementations. Your coordination efforts should guarantee fluid communication in accessibility audits via thread_004, effective coordination of comment lifecycles, and thorough tracking of accessibility compliance in reports for stakeholders, leading to successful workflow completion. Utilize resolution_notes Accessibility improvements in progress - adding ARIA labels and keyboard navigation support"
        ),
        actions=[
            Action(name="GetFigmaCommentsByArtifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_007"}),
            Action(name="UpdateFigmaCommentStatus", kwargs={"comment_id": "comment_006", "new_status": "IN_PROGRESS", "resolution_notes": "Accessibility improvements in progress - adding ARIA labels and keyboard navigation support", "assignee_email": "jake.design@company.com", "priority_level": "HIGH"}),
            Action(name="GetGmailThreadsByLabels", kwargs={"thread_id": "thread_004"}),
            Action(name="GetFigmaCommentsByArtifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="AddTerminalLogEntry", kwargs={"log_message": "Figma comment resolution workflow completed for accessibility improvements", "log_level": "INFO", "component": "figma_comment_resolution", "user_email": "jake.design@company.com"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_004", "new_priority": "HIGH", "urgency_reason": "Accessibility feedback coordination requires immediate attention", "escalate_to": ["jake.design@company.com"]})
        ],
        outputs=[]
    ),    

    Task(
        annotator="0",
        user_id="user_56",
        instruction=(
            "You are an audit report management specialist liable for orchestrating the complete audit lifecycle concerning design system components and accessibility compliance. Your key duty is to oversee audit_001 for artifact art_001 (Homepage Hero Section), requiring meticulous status tracking from COMPLETED to the generation of final reports. This workflow converges with audit_002 for an accessibility review of art_008 admin panel components, necessitating status coordination. Core to the audit management process is the escalation of thread_001 to HIGH priority for design review coordination under the guidance of emma.creative@company.com, as well as escalating URGENT priority levels for thorough design review tracking, all due to the escalation_reason 'Critical audit findings require immediate design team attention and stakeholder review'. Managing priorities requires proficient coordination of Gmail threads and well-documented audit status. Your coordination should enable seamless audit report generation through efficient status management, critical priority escalation of design review threads, meticulous tracking of audit findings for stakeholder reports, and conclusively completing the audit lifecycle with proper report asset linkage. Key parameters include: audit_id=audit_001, new_status=COMPLETED, report_asset_id=asset_001, completion_notes=Design system audit completed with recommendations, thread_001_priority=HIGH, thread_002_priority=NORMAL, thread_001_urgency=Critical audit findings require immediate design team attention, thread_002_urgency=Secondary audit review completed, escalate_to=emma.creative@company.com,jake.design@company.com, audit_type=COMBINED_DS_A11Y, created_after=2024-08-20T15:00:00Z, audit_date_filter=2024-08-18T00:00:00Z, thread_ids=thread_001,thread_002, artifact_ids=art_001,art_008, asset_id=asset_001, log_message=Audit management workflow completed with comprehensive tracking and report generation, log_level=INFO, component=audit_management, user_email=emma.creative@company.com"
        ),
        actions=[
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_001"}),
            Action(name="UpdateAuditReportStatus", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed with recommendations"}),
            Action(name="GetAuditsByStatus", kwargs={"status": "COMPLETED", "audit_type": "COMBINED_DS_A11Y"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical audit findings require immediate design team attention", "escalate_to": ["emma.creative@company.com", "jake.design@company.com"]}),
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_002"}),
            Action(name="GetAuditsByStatus", kwargs={"artifact_id": "art_001", "created_after": "2024-08-20T15:00:00Z"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Secondary audit review completed"}),
            Action(name="GetAuditsByStatus", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"}),
            Action(name="GetSystemConfigByCategory", kwargs={"category": "audit_config"}),
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_001"}),
            Action(name="GetFigmaCommentsByArtifact", kwargs={"artifact_id": "art_001", "resolved_status": True}),
            Action(name="AddTerminalLogEntry", kwargs={"log_message": "Audit management workflow completed with comprehensive tracking and report generation", "log_level": "INFO", "component": "audit_management", "user_email": "emma.creative@company.com"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_57",
        instruction=(
            "As a specialist in audit report management, you are tasked with overseeing the complete audit process for design system components and ensuring accessibility compliance. Your main duty is to handle audit_001 for artifact art_001 (Homepage Hero Section). This involves meticulous tracking from the point of being COMPLETED to the final report generation. Your workflow combines with audit_002, focusing on the accessibility review of art_008 admin panel components, which requires precise status coordination. The center of this audit management workflow is the priority elevation of thread_001 to HIGH priority for design review oversight, managed by emma.creative@company.com. It also involves raising the urgency level to URGENT for an exhaustive design review tracking due to the escalation_reason 'Critical audit findings require immediate design team attention and stakeholder review'. It is crucial to coordinate Gmail threads and maintain detailed documentation of audit statuses. Ensure seamless generation of the audit report by managing status transitions effectively, elevating priorities for design review threads, tracking audit findings comprehensively for stakeholder reporting, and efficiently concluding the audit lifecycle with proper report asset links. Important parameters: audit_id=audit_001, new_status=COMPLETED, report_asset_id=asset_001, completion_notes=Design system audit completed with recommendations, thread_001_priority=HIGH, thread_002_priority=NORMAL, thread_001_urgency=Critical audit findings require immediate design team attention, thread_002_urgency=Secondary audit review completed, escalate_to=emma.creative@company.com,jake.design@company.com, audit_type=COMBINED_DS_A11Y, created_after=2024-08-20T15:00:00Z, audit_date_filter=2024-08-18T00:00:00Z, thread_ids=thread_001,thread_002, artifact_ids=art_001,art_008"
        ),
        actions=[
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_001"}),
            Action(name="UpdateAuditReportStatus", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed with recommendations"}),
            Action(name="GetAuditsByStatus", kwargs={"status": "COMPLETED", "audit_type": "COMBINED_DS_A11Y"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical audit findings require immediate design team attention", "escalate_to": ["emma.creative@company.com", "jake.design@company.com"]}),
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_002"}),
            Action(name="UpdateAuditReportStatus", kwargs={"audit_id": "audit_002", "new_status": "COMPLETED", "report_asset_id": "asset_007"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Secondary audit review completed"}),
            Action(name="GetAuditsByStatus", kwargs={"status": "COMPLETED", "created_after": "2024-08-20T15:00:00Z"}),
            Action(name="GetAuditsByStatus", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_58",
        instruction=(
            "You are tasked with resolving Figma comments as part of the accessibility enhancement initiatives for the admin panel header. Your role involves organizing the response to accessibility feedback and ensuring all associated assets and communications are thoroughly accounted for. Concentrate on advancing the accessibility improvement process, which includes resolving comments and keeping asset export statuses updated. Work closely with the UX team using the designated communication channels to guarantee the fulfillment of all accessibility standards. Constant parameters include: artifact_id=art_008, asset_id=asset_007, comment_id=comment_006, assignee_email=jake.design@company.com, priority_level=HIGH, thread_ids=thread_004,thread_005, resolution_notes=Accessibility improvements in progress - adding ARIA labels and keyboard navigation support, export_notes=Admin header accessibility export completed with ARIA labels, dlp_scan_status=CLEAN, new_status=IN_PROGRESS, export_status=COMPLETED"
        ),
        actions=[
            Action(name="GetFigmaCommentsByArtifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_007"}),
            Action(name="UpdateFigmaCommentStatus", kwargs={"comment_id": "comment_006", "new_status": "IN_PROGRESS", "resolution_notes": "Accessibility improvements in progress - adding ARIA labels and keyboard navigation support", "assignee_email": "jake.design@company.com", "priority_level": "HIGH"}),
            Action(name="GetGmailThreadsByLabels", kwargs={"thread_id": "thread_004"}),
            Action(name="GetGmailThreadsByLabels", kwargs={"thread_id": "thread_005"}),  # Additional action
            Action(name="GetFigmaCommentsByArtifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="UpdateAssetExportStatus", kwargs={"asset_id": "asset_007", "new_status": "COMPLETED", "notes": "Admin header accessibility export completed with ARIA labels", "dlp_scan_status": "CLEAN"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_59",
        instruction=(
            "Handle the role of a mobile component audit integration specialist tasked with managing comprehensive mobile audit workflows and release management for mobile application components. Your main role involves audit_002 management for mobile components necessitating extensive status tracking and thread_002 CRITICAL priority escalation for coordinating mobile dashboard releases. The workflow is integrated with approval checking for mobile workflows and thorough audit tracking for mobile application readiness. The mobile integration workflow emphasizes comprehensive audit coordination under the supervision of jake.design@company.com, managing thread_007 HIGH priority for mobile app release coordination, escalation_reason \"Mobile application release requires immediate audit integration and cross-team coordination\", along with detailed approval tracking for mobile component workflows focused on release preparation. Your coordination must ensure smooth mobile audit integration through thorough status management, effective priority escalation for mobile release threads, and detailed approval verification for mobile workflows with correct UX team coordination and release readiness monitoring. Key parameters: audit_002_id=audit_002, audit_002_status=COMPLETED, thread_002_id=thread_002, thread_007_id=thread_007, additional_thread_id=thread_005, thread_002_priority=CRITICAL, thread_007_priority=HIGH, thread_002_urgency=Mobile application release requires immediate coordination, thread_007_urgency=Mobile app release coordination support required, additional_thread_priority=NORMAL, additional_thread_urgency=Mobile component design review required, completion_notes=Mobile component audit completed with accessibility integration, approval_002_id=approval_002, cycle_002_id=cycle_002, audit_type=A11Y, created_after_date=2024-08-19T12:00:00Z, escalate_to=jake.design@company.com,mobile.team@company.com"
        ),
        actions=[
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_002"}),
            Action(name="UpdateAuditReportStatus", kwargs={"audit_id": "audit_002", "new_status": "COMPLETED", "completion_notes": "Mobile component audit completed with accessibility integration"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_002", "new_priority": "CRITICAL", "urgency_reason": "Mobile application release requires immediate coordination", "escalate_to": ["jake.design@company.com", "mobile.team@company.com"]}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_005", "new_priority": "NORMAL", "urgency_reason": "Mobile component design review required"}),  # Additional action
            Action(name="GetReviewApprovalsSummary", kwargs={"approval_id": "approval_002", "cycle_id": "cycle_002"}),
            Action(name="GetAuditsByStatus", kwargs={"created_after": "2024-08-19T12:00:00Z", "audit_type": "A11Y"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_007", "new_priority": "HIGH", "urgency_reason": "Mobile app release coordination support required"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_60",
        instruction=(
            "Manage the responsibilities as a mobile component audit integration specialist overseeing comprehensive mobile audit workflows and release management for mobile application components. Your core duty involves the management of audit_002 for mobile components requiring comprehensive status tracking and thread_002 CRITICAL priority escalation for coordinating mobile dashboard releases. The workflow incorporates approval verification for mobile workflows and detailed audit tracking for mobile application readiness. The mobile integration workflow is centered on comprehensive audit coordination with oversight from jake.design@company.com, handling thread_007 HIGH priority management for mobile app release coordination, escalation_reason \"Mobile application release requires immediate audit integration and cross-team coordination\", additionally ensuring detailed approval tracking for mobile component workflows with an emphasis on release preparation. Your coordination should achieve seamless mobile audit integration through comprehensive status management, efficient priority escalation for mobile release threads, and detailed approval verification for mobile workflows with necessary UX team coordination and tracking of release readiness. Key parameters: audit_002_id=audit_002, audit_002_status=COMPLETED, thread_002_id=thread_002, thread_007_id=thread_007, thread_002_priority=CRITICAL, thread_007_priority=HIGH, thread_002_urgency=Mobile application release requires immediate coordination, thread_007_urgency=Mobile app release coordination support required, completion_notes=Mobile component audit completed with accessibility integration, approval_002_id=approval_002, cycle_002_id=cycle_002, audit_type=A11Y, additional_audit_id=audit_003, created_after_date=2024-08-19T12:00:00Z, escalate_to=jake.design@company.com,mobile.team@company.com"
        ),
        actions=[
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_002"}),
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_003"}),  # Additional action
            Action(name="UpdateAuditReportStatus", kwargs={"audit_id": "audit_002", "new_status": "COMPLETED", "completion_notes": "Mobile component audit completed with accessibility integration"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_002", "new_priority": "CRITICAL", "urgency_reason": "Mobile application release requires immediate coordination", "escalate_to": ["jake.design@company.com", "mobile.team@company.com"]}),
            Action(name="GetReviewApprovalsSummary", kwargs={"approval_id": "approval_002", "cycle_id": "cycle_002"}),
            Action(name="GetAuditsByStatus", kwargs={"created_after": "2024-08-19T12:00:00Z", "audit_type": "A11Y"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_007", "new_priority": "HIGH", "urgency_reason": "Mobile app release coordination support required"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_61",
        instruction=(
            "Handle the role of a Figma comment resolution specialist, focusing on the coordination of accessibility feedback and workflow management for admin panel header components. Your main task is to manage accessibility feedback for the art_008 admin panel header, identifying and coordinating resolution for unresolved comments marked with resolved_status False. The workflow also encompasses the export integration of asset_007 admin header, requiring status verification and alignment coordination. The accessibility improvement initiative centers on coordinating enhancements to comment_006, overseen by team member jake.design@company.com, prioritizing HIGH urgency accessibility upgrades, and tracking the implementation of comprehensive ARIA labels and keyboard navigation support. Progress status must be coordinated for feedback resolution, along with detailed documentation of implementations. Your coordination efforts should guarantee smooth communication of accessibility audits via thread_004, proficient comment lifecycle management, and thorough tracking of accessibility compliance for stakeholder reporting and the successful conclusion of workflows. Utilize resolution_notes 'Accessibility improvements in progress - adding ARIA labels and keyboard navigation support.'"
        ),
        actions=[
            Action(name="GetFigmaCommentsByArtifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_007"}),
            Action(name="UpdateFigmaCommentStatus", kwargs={"comment_id": "comment_006", "new_status": "IN_PROGRESS", "resolution_notes": "Accessibility improvements in progress - adding ARIA labels and keyboard navigation support", "assignee_email": "jake.design@company.com", "priority_level": "HIGH"}),
            Action(name="GetGmailThreadsByLabels", kwargs={"thread_id": "thread_004"}),
            Action(name="GetFigmaCommentsByArtifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="AddTerminalLogEntry", kwargs={"log_message": "Figma comment resolution workflow completed for accessibility improvements", "log_level": "INFO", "component": "figma_comment_resolution", "user_email": "jake.design@company.com"}),
            Action(name="GetSystemConfigByCategory", kwargs={"category": "accessibility_config"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_62",
        instruction=(
            "Coordinate the duties of a Figma comment resolution specialist, tasked with managing accessibility feedback and the workflow for components of the admin panel header. Your principal duty involves coordinating accessibility feedback for the art_008 admin panel header, which involves identifying unresolved comments with resolved_status False and coordinating their resolution. Additionally, the workflow includes the export integration of asset_007 admin header, requiring alignment of status verification and coordination. Accessibility improvement efforts focus on the coordination of enhancements to comment_006, directed by team member jake.design@company.com, with a focus on HIGH priority accessibility improvements and the tracking of comprehensive ARIA labels and keyboard navigation support implementation. The feedback resolution process requires you to coordinate progress status and document implementations meticulously. Ensure seamless communication for accessibility audits through thread_004, effective management of the comment lifecycle, and comprehensive tracking of accessibility compliance for stakeholder reports and successful workflow completion."
        ),
        actions=[
            Action(name="GetFigmaCommentsByArtifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_007"}),
            Action(name="UpdateFigmaCommentStatus", kwargs={"comment_id": "comment_006", "new_status": "IN_PROGRESS", "resolution_notes": "Accessibility improvements in progress - adding ARIA labels and keyboard navigation support", "assignee_email": "jake.design@company.com", "priority_level": "HIGH"}),
            Action(name="GetGmailThreadsByLabels", kwargs={"thread_id": "thread_004"}),
            Action(name="GetFigmaCommentsByArtifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="UpdateAssetExportStatus", kwargs={"asset_id": "asset_007", "new_status": "COMPLETED", "notes": "Admin header accessibility export completed with ARIA labels", "dlp_scan_status": "CLEAN"}),
            Action(name="AddTerminalLogEntry", kwargs={"log_message": "Figma comment resolution workflow completed for comment_006 accessibility improvements", "log_level": "INFO", "component": "figma_comment_resolution", "user_email": "jake.design@company.com"}),
            Action(name="GetAuditsByStatus", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_63",
        instruction=(
            "Your role as a Figma comment resolution specialist involves managing accessibility feedback and workflow processes across admin panel header components. Key duties include managing accessibility feedback specifically for art_008's admin panel header, where unresolved comments marked with resolved_status False need identification and coordinated resolution. This process also encompasses the integration of asset_007's admin header export, requiring verification of status and alignment in coordination. The primary focus is on improving accessibility workflows through comment_006, including oversight from team member jake.design@company.com, prioritizing HIGH-level accessibility improvements, and tracking the implementation of comprehensive ARIA labels and keyboard navigation support. Effectively managing feedback resolution requires coordinating progress statuses and documenting implementation details. Your efforts must ensure fluid communication during accessibility audits via thread_004, efficient comment lifecycle management, and thorough tracking of accessibility compliance for stakeholder reporting, culminating in the successful completion of the workflow. Apply resolution_notes Accessibility improvements in progress - adding ARIA labels and keyboard navigation support or similar. When export is COMPLETED, use note Admin header accessibility export completed with ARIA labels."
        ),
        actions=[
            Action(name="GetFigmaCommentsByArtifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_007"}),
            Action(name="UpdateFigmaCommentStatus", kwargs={"comment_id": "comment_006", "new_status": "IN_PROGRESS", "resolution_notes": "Accessibility improvements in progress - adding ARIA labels and keyboard navigation support", "assignee_email": "jake.design@company.com", "priority_level": "HIGH"}),
            Action(name="GetGmailThreadsByLabels", kwargs={"thread_id": "thread_004"}),
            Action(name="GetFigmaCommentsByArtifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="UpdateAssetExportStatus", kwargs={"asset_id": "asset_007", "new_status": "COMPLETED", "notes": "Admin header accessibility export completed with ARIA labels", "dlp_scan_status": "CLEAN"}),
            Action(name="GetFigmaArtifactsByStatus", kwargs={"artifact_id": "art_008"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_64",
        instruction=(
            "As a design system component audit specialist, your task is to facilitate in-depth audits of the design system and manage thread priorities within component workflows. Your main focus is overseeing audit_002 for design system components that require detailed status tracking and priority management of threads for component review coordination. This workflow interfaces with approval checks and thread escalation needed for preparing design system releases. The coordination workflow for the design system is centered around exhaustive audit tracking with oversight from emma.creative@company.com, along with high-priority thread_001 management for design system coordination, and thorough approval checks across the workflows. Your efforts must guarantee smooth audit coordination of the design system through meticulous status tracking, effective management of thread priorities for component reviews, and thorough approval verification, all aligned with proper synchronization among the design team and monitoring release preparations. Essential parameters include: audit_002_id=audit_002, audit_002_status=COMPLETED, art_008_id=art_008, audit_type=A11Y, thread_001_id=thread_001, thread_008_id=thread_008, thread_001_priority=HIGH, thread_008_priority=NORMAL, thread_001_urgency=Design system component review requires immediate coordination, thread_008_urgency=Design system follow-up coordination completed, completion_notes=Design system component audit completed successfully, approval_002_id=approval_002, cycle_002_id=cycle_002, escalate_to=emma.creative@company.com,design.system@company.com, release_owner=emma.creative@company.com, release_start_date=2024-08-20T13:00:00Z, log_message=Design system component audit workflow completed with comprehensive tracking, log_level=INFO, component=design_system_audit, user_email=emma.creative@company.com"
        ),
        actions=[
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_002"}),
            Action(name="UpdateAuditReportStatus", kwargs={"audit_id": "audit_002", "new_status": "COMPLETED", "completion_notes": "Design system component audit completed successfully"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Design system component review requires immediate coordination", "escalate_to": ["emma.creative@company.com", "design.system@company.com"]}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_008", "new_priority": "NORMAL", "urgency_reason": "Design system follow-up coordination completed"}),
            Action(name="GetReviewApprovalsSummary", kwargs={"approval_id": "approval_002", "cycle_id": "cycle_002"}),
            Action(name="GetAuditsByStatus", kwargs={"artifact_id": "art_008", "audit_type": "A11Y"}),
            Action(name="GetReleasesByOwner", kwargs={"owner_email": "emma.creative@company.com", "created_after": "2024-08-20T13:00:00Z"}),
            Action(name="AddTerminalLogEntry", kwargs={"log_message": "Design system component audit workflow completed with comprehensive tracking", "log_level": "INFO", "component": "design_system_audit", "user_email": "emma.creative@company.com"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_65",
        instruction=(
            "Handle mobile audit findings severity control as a specialist managing update processes and integrated fix plan workflows. Your role involves handling severity escalations in audit findings alongside fix plan status coordination and ensuring correct priority management. Dedicate attention to managing severity updates for CRITICAL violations, including orchestrating fix plan deliveries and thorough fix item tracking. Engage with development teams via designated channels to ensure synchronization of all audit findings and fix workflows. Moreover, retrieve audit summaries to guarantee comprehensive oversight and continuity throughout the severity management workflow. Required constants: finding_id=finding_a11y_001, new_severity=CRITICAL, updated_by=chris.engineer@company.com, plan_id=plan_001, delivery_method=TICKETS, owner_email=chris.engineer@company.com, item_id=item_001, fix_item_id=item_001, new_priority=HIGH, priority_reason=Critical finding requires immediate fix attention, audit_id=audit_002, violation_type=COLOR_CONTRAST, severity=CRITICAL, log_message=Audit findings severity management and fix plan coordination completed, log_level=INFO, log_component=audit_severity, comment_id=comment_006, comment_status=RESOLVED"
        ),
        actions=[
            Action(name="UpdateAuditFindingSeverity", kwargs={"finding_id": "finding_a11y_001", "new_severity": "CRITICAL", "updated_by": "chris.engineer@company.com"}),
            Action(name="GetAuditFindingsByType", kwargs={"violation_type": "COLOR_CONTRAST", "severity": "CRITICAL"}),
            Action(name="GetFixPlanItems", kwargs={"plan_id": "plan_001"}),
            Action(name="UpdateFixPlanStatus", kwargs={"plan_id": "plan_001", "new_status": "IN_PROGRESS", "delivery_method": "TICKETS", "owner_email": "chris.engineer@company.com"}),
            Action(name="UpdateFixItemPriority", kwargs={"item_id": "item_001", "new_priority": "HIGH", "priority_reason": "Critical finding requires immediate fix attention", "updated_by": "chris.engineer@company.com"}),
            Action(name="UpdateFixItemStatus", kwargs={"fix_item_id": "item_001", "new_status": "IN_PROGRESS", "updated_by": "chris.engineer@company.com"}),
            Action(name="AddTerminalLogEntry", kwargs={"log_message": "Audit findings severity management and fix plan coordination completed", "log_level": "INFO", "component": "audit_severity", "user_email": "chris.engineer@company.com"}),
            Action(name="GetAuditSummary", kwargs={"audit_id": "audit_002"}),
            Action(name="UpdateFigmaCommentStatus", kwargs={"comment_id": "comment_006", "new_status": "RESOLVED", "resolved_by": "chris.engineer@company.com"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_66",
        instruction=(
            "Coordinate efforts as an accessibility compliance specialist in audit findings management and fix item organization across initiatives focused on admin panel accessibility. Your main task involves the facilitation of accessibility audits on audit_002, audit_004, and audit_005, necessitating detailed analysis of findings and status updates on fix items through a systematic approach. The process encompasses managing the lifecycle of fix items following designated progression protocols. This compliance operation emphasizes the verification of item_001 touch targets leading to VERIFIED status, oversight of item_004 font size compliance attaining APPLIED status with coordinated completion timestamps, and overseeing item_002 contrast correction under IN_PROGRESS status. Undertake systematic coordination to assure status checks and compliance verification, thereby achieving comprehensive audit findings analysis, efficient fix item lifecycle management, and successful accessibility compliance oversight for stakeholder reporting and workflow finalization."
        ),
        actions=[
            Action(name="GetAuditFindingsSummary", kwargs={"audit_id": "audit_002"}),
            Action(name="GetAuditFindingsSummary", kwargs={"audit_id": "audit_004"}),
            Action(name="GetAuditFindingsSummary", kwargs={"audit_id": "audit_005"}),
            Action(name="UpdateFixItemStatus", kwargs={"fix_item_id": "item_001", "new_status": "VERIFIED"}),
            Action(name="UpdateFixItemStatus", kwargs={"fix_item_id": "item_004", "new_status": "APPLIED", "completion_date": "2024-08-25T15:30:00Z"}),
            Action(name="UpdateFixItemStatus", kwargs={"fix_item_id": "item_002", "new_status": "IN_PROGRESS"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_67",
        instruction=(
            "Handle the role of a comprehensive release management coordinator tasked with managing the entire release process, including system configuration management and Gmail communication for design system components. Your primary duty includes managing the status of release_003 and coordinating asset_003 export, which involves detailed status tracking, verifying asset export summaries, handling system configuration, and coordinating Gmail threads for communication about the release. This process includes cross-team collaboration, ensuring system configuration verification, and appropriate release lifecycle management with stakeholder communication. The improved release coordination process focuses on achieving PUBLISHED status for release_003, providing detailed release notes, coordinating the export status of asset_003 to achieve COMPLETED status with DLP scan verification, verifying export summaries for documentation compliance, managing system configuration for release standards, and handling thread_003 with NORMAL priority for release documentation coordination. Your efforts should guarantee comprehensive management of the release lifecycle, including system integration, accurate asset export status and summary management, verification of system configuration for release standards, managing Gmail threads for documentation coordination, and tracking successful release deployment to report to stakeholders and complete the workflow. Required constants: release_id=release_003, new_status=PUBLISHED, release_notes=Design system components release with accessibility improvements, updated_by=emma.creative@company.com, asset_id=asset_003, export_status=COMPLETED, export_notes=Design system asset export completed with accessibility compliance, dlp_scan_status=CLEAN, owner_email=emma.creative@company.com, created_after=2024-08-20T15:00:00Z, category=release_documentation_config, thread_id=thread_003, thread_priority=NORMAL, urgency_reason=Release documentation and compliance verification completed"
        ),
        actions=[
            Action(name="UpdateReleaseStatus", kwargs={"release_id": "release_003", "new_status": "PUBLISHED", "release_notes": "Design system components release with accessibility improvements", "updated_by": "emma.creative@company.com"}),
            Action(name="UpdateAssetExportStatus", kwargs={"asset_id": "asset_003", "new_status": "COMPLETED", "notes": "Design system asset export completed with accessibility compliance", "dlp_scan_status": "CLEAN"}),
            Action(name="GetReleasesByOwner", kwargs={"owner_email": "emma.creative@company.com", "created_after": "2024-08-20T15:00:00Z"}),
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_003"}),
            Action(name="GetSystemConfigByCategory", kwargs={"category": "release_documentation_config"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_003", "new_priority": "NORMAL", "urgency_reason": "Release documentation and compliance verification completed"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_68",
        instruction=(
            "Manage the role of a design system component audit specialist, ensuring comprehensive audits and managing thread priority for component workflows. Your main task is to coordinate audit_002 for design system components, which demands thorough status tracking and thread priority handling for component review coordination. This process works alongside approval verification and thread escalation in preparation for the release of the design system. The coordination process for the design system emphasizes thorough audit tracking under emma.creative@company.com’s supervision, HIGH priority management of thread_001 for coordination, and meticulous approval verification across the workflows. Your coordination should ensure smooth design system audit handling by ensuring comprehensive status tracking, effective thread priority management for component reviews, and meticulous approval verification within the workflows, collaborating correctly with the design team and tracking release preparation. Key parameters: audit_002_id=audit_002, audit_002_status=COMPLETED, art_008_id=art_008, audit_type=A11Y, thread_001_id=thread_001, thread_008_id=thread_008, thread_001_priority=HIGH, thread_008_priority=NORMAL, thread_001_urgency=Design system component review requires immediate coordination, thread_008_urgency=Design system follow-up coordination completed, completion_notes=Design system component audit completed successfully, approval_002_id=approval_002, cycle_002_id=cycle_002, escalate_to=emma.creative@company.com,design.system@company.com, release_owner=emma.creative@company.com, release_start_date=2024-08-20T13:00:00Z"
        ),
        actions=[
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_002"}),
            Action(name="UpdateAuditReportStatus", kwargs={"audit_id": "audit_002", "new_status": "COMPLETED", "completion_notes": "Design system component audit completed successfully"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Design system component review requires immediate coordination", "escalate_to": ["emma.creative@company.com", "design.system@company.com"]}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_008", "new_priority": "NORMAL", "urgency_reason": "Design system follow-up coordination completed"}),
            Action(name="GetReviewApprovalsSummary", kwargs={"approval_id": "approval_002", "cycle_id": "cycle_002"}),
            Action(name="GetAuditsByStatus", kwargs={"artifact_id": "art_008", "audit_type": "A11Y"}),
            Action(name="GetReleasesByOwner", kwargs={"owner_email": "emma.creative@company.com", "created_after": "2024-08-20T13:00:00Z"}),
            Action(name="GetAuditFindingsSummary", kwargs={"audit_id": "audit_002", "include_resolved": True}),
            Action(name="GetSystemConfigByCategory", kwargs={"category": "design_system_audit_config"}),
            Action(name="UpdateAuditType", kwargs={"audit_id": "audit_002", "new_audit_type": "COMBINED_DS_A11Y", "updated_by": "emma.creative@company.com"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_69",
        instruction=(
            "You are a design system component audit specialist tasked with handling comprehensive design system audits and managing thread priorities for component workflows. Your central responsibility includes audit_002 coordination for design system components, necessitating comprehensive status tracking and thread priority management for component review coordination. The workflow is integrated with approval verification and includes thread escalation in preparation for design system releases. The design system coordination workflow emphasizes comprehensive audit tracking under the guidance of emma.creative@company.com, prioritizing high thread management for design system coordination and thorough approval verification across workflows. Your coordination activities should guarantee smooth audit coordination for design systems via comprehensive status tracking, adept thread priority management for component evaluations, and meticulous approval verification within design system workflows with appropriate team coordination and release preparation tracking. Key parameters: audit_002_id=audit_002, audit_002_status=COMPLETED, art_008_id=art_008, audit_type=A11Y, thread_001_id=thread_001, thread_008_id=thread_008, thread_001_priority=HIGH, thread_008_priority=NORMAL, thread_001_urgency=Design system component review requires immediate coordination, thread_008_urgency=Design system follow-up coordination completed, completion_notes=Design system component audit completed successfully, approval_002_id=approval_002, cycle_002_id=cycle_002, escalate_to=emma.creative@company.com,design.system@company.com, release_owner=emma.creative@company.com, release_start_date=2024-08-20T13:00:00Z"
        ),
        actions=[
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_002"}),
            Action(name="UpdateAuditReportStatus", kwargs={"audit_id": "audit_002", "new_status": "COMPLETED", "completion_notes": "Design system component audit completed successfully"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Design system component review requires immediate coordination", "escalate_to": ["emma.creative@company.com", "design.system@company.com"]}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_008", "new_priority": "NORMAL", "urgency_reason": "Design system follow-up coordination completed"}),
            Action(name="GetReviewApprovalsSummary", kwargs={"approval_id": "approval_002", "cycle_id": "cycle_002"}),
            Action(name="GetAuditsByStatus", kwargs={"artifact_id": "art_008", "audit_type": "A11Y"}),
            Action(name="GetReleasesByOwner", kwargs={"owner_email": "emma.creative@company.com", "created_after": "2024-08-20T13:00:00Z"}),
            Action(name="GetAuditFindingsSummary", kwargs={"audit_id": "audit_002", "include_resolved": True})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_70",
        instruction=(
            "You are an audit report management specialist tasked with overseeing the complete audit lifecycle for design system components and accessibility compliance. Your main duty involves managing audit_001 for artifact art_001 (Homepage Hero Section), requiring exhaustive status tracking from COMPLETED through to final report creation. The workflow is synchronized with audit_002 for an accessibility review of art_008 admin panel components, needing coordinated status management. The focus of the audit management workflow is on escalating thread_001 priority to HIGH for design review coordination, under the supervision of emma.creative@company.com, with an URGENT priority level escalation for thorough design review tracking, alongside the escalation_reason 'Critical audit findings require immediate design team attention and stakeholder review'. The priority management mandates extensive Gmail thread coordination and detailed audit status documentation. Your coordination must ensure seamless audit report production through proper status management, effective priority escalation for design review threads, and extensive audit findings tracking for stakeholder communication. Key parameters: audit_id=audit_001, new_status=COMPLETED, report_asset_id=asset_001, completion_notes=Design system audit completed with recommendations, thread_001_priority=HIGH, thread_002_priority=NORMAL, thread_001_urgency=Critical audit findings require immediate design team attention, thread_002_urgency=Secondary audit review completed, escalate_to=emma.creative@company.com,jake.design@company.com, audit_type=COMBINED_DS_A11Y, created_after=2024-08-20T15:00:00Z, audit_date_filter=2024-08-18T00:00:00Z, thread_ids=thread_001,thread_002, artifact_ids=art_001,art_008"
        ),
        actions=[
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_001"}),
            Action(name="UpdateAuditReportStatus", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed with recommendations"}),
            Action(name="GetAuditsByStatus", kwargs={"status": "COMPLETED", "audit_type": "COMBINED_DS_A11Y"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical audit findings require immediate design team attention", "escalate_to": ["emma.creative@company.com", "jake.design@company.com"]}),
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_002"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Secondary audit review completed"}),
            Action(name="GetAuditsByStatus", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"}),
            Action(name="AddTerminalLogEntry", kwargs={"log_message": "Audit management workflow completed for audit_001 and audit_002 with critical findings escalation", "log_level": "INFO", "component": "audit_management", "user_email": "emma.creative@company.com"}),
            Action(name="GetReleasesByOwner", kwargs={"owner_email": "emma.creative@company.com", "created_after": "2024-08-20T15:00:00Z"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_71",
        instruction=(
            "As a mobile component audit integration specialist, you are tasked with handling comprehensive mobile audit workflows and managing releases for mobile application components. Your main job includes audit_002 management for mobile components needing detailed status monitoring and thread_002 CRITICAL priority escalation for coordinating mobile dashboard releases. The workflow integrates approval verification for mobile processes and thorough audit tracking for mobile application readiness. The mobile integration process concentrates on full audit coordination with oversight by jake.design@company.com, thread_007 HIGH priority handling for mobile app release coordination, with an escalation_reason \"Mobile application release requires immediate audit integration and cross-team coordination,\" and meticulous approval monitoring for mobile component workflows focusing on release preparation. Your coordination efforts should facilitate seamless mobile audit integration by maintaining detailed status coordination, implementing effective priority escalation for mobile release threads, and verifying approvals for mobile workflows with appropriate UX team collaboration and release readiness tracking. Key parameters: audit_002_id=audit_002, audit_002_status=COMPLETED, thread_002_id=thread_002, thread_007_id=thread_007, thread_002_priority=CRITICAL, thread_007_priority=HIGH, thread_002_urgency=Mobile application release requires immediate coordination, thread_007_urgency=Mobile app release coordination support required, completion_notes=Mobile component audit completed with accessibility integration, approval_002_id=approval_002, cycle_002_id=cycle_002, audit_type=A11Y, created_after_date=2024-08-19T12:00:00Z, escalate_to=jake.design@company.com,mobile.team@company.com"
        ),
        actions=[
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_002"}),
            Action(name="UpdateAuditReportStatus", kwargs={"audit_id": "audit_002", "new_status": "COMPLETED", "completion_notes": "Mobile component audit completed with accessibility integration"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_002", "new_priority": "CRITICAL", "urgency_reason": "Mobile application release requires immediate coordination", "escalate_to": ["jake.design@company.com", "mobile.team@company.com"]}),
            Action(name="GetReviewApprovalsSummary", kwargs={"approval_id": "approval_002", "cycle_id": "cycle_002"}),
            Action(name="GetAuditsByStatus", kwargs={"created_after": "2024-08-19T12:00:00Z", "audit_type": "A11Y"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_007", "new_priority": "HIGH", "urgency_reason": "Mobile app release coordination support required"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_72",
        instruction=(
            "As an audit report management specialist, you are responsible for orchestrating the entire audit lifecycle for design system components and ensuring accessibility compliance. Your main duty involves managing audit_001 for artifact art_001 (Homepage Hero Section) which demands thorough status tracking from COMPLETED to the final report creation. The process also incorporates audit_002 for an accessibility review of art_008 admin panel components needing status coordination. The audit management workflow focuses on escalating thread_001 to HIGH priority for design review coordination under the supervision of emma.creative@company.com, with URGENT priority level escalation for detailed design review tracking, and an escalation_reason 'Critical audit findings require immediate design team attention and stakeholder review'. The priority management entails organizing comprehensive Gmail thread coordination and meticulous documentation of audit statuses. Your coordination efforts should allow for smooth audit report generation through accurate status management, competent priority escalation for design review threads, extensive tracking of audit findings for stakeholder reports, and the successful completion of the audit lifecycle with correct report asset associations. Key parameters: audit_id=audit_001, new_status=COMPLETED, report_asset_id=asset_001, completion_notes=Design system audit completed with recommendations, thread_001_priority=HIGH, thread_002_priority=NORMAL, thread_001_urgency=Critical audit findings require immediate design team attention, thread_002_urgency=Secondary audit review completed, escalate_to=emma.creative@company.com,jake.design@company.com, audit_type=COMBINED_DS_A11Y, created_after=2024-08-20T15:00:00Z, audit_date_filter=2024-08-18T00:00:00Z, thread_ids=thread_001,thread_002, artifact_ids=art_001,art_008"
        ),
        actions=[
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_001"}),
            Action(name="UpdateAuditReportStatus", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed with recommendations"}),
            Action(name="GetAuditsByStatus", kwargs={"status": "COMPLETED", "audit_type": "COMBINED_DS_A11Y"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical audit findings require immediate design team attention", "escalate_to": ["emma.creative@company.com", "jake.design@company.com"]}),
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_002"}),
            Action(name="GetAuditsByStatus", kwargs={"artifact_id": "art_001", "created_after": "2024-08-20T15:00:00Z"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Secondary audit review completed"}),
            Action(name="GetAuditsByStatus", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"}),
            Action(name="AddTerminalLogEntry", kwargs={"log_message": "Audit management workflow completed for audit_001 and audit_002 with comprehensive status tracking", "log_level": "INFO", "component": "audit_management", "user_email": "emma.creative@company.com"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_73",
        instruction=(
            "Manage the audit report lifecycle for design system components and accessibility compliance as an audit report management specialist. Your key task is handling audit_001 for artifact art_001 (Homepage Hero Section), ensuring comprehensive status updates from COMPLETED to the generation of the final report. This process is linked with audit_002 for accessibility review of art_008 admin panel components, necessitating status harmonization. The audit management workflow focuses on escalating thread_001 priority to HIGH for design review oversight with emma.creative@company.com, escalated to URGENT for thorough design review tracking, and an escalation_reason being 'Critical audit findings require immediate design team attention and stakeholder review'. Priority management demands organized Gmail thread coordination and meticulous audit status documentation. Your coordination should guarantee efficient audit report generation via accurate status control, targeted priority escalation for design review threads, comprehensive tracking of audit findings for stakeholder reports, and the successful closure of the audit lifecycle with correctly associated report assets. Essential details: audit_id=audit_001, new_status=COMPLETED, report_asset_id=asset_001, completion_notes=Design system audit completed with recommendations, thread_001_priority=HIGH, thread_002_priority=NORMAL, thread_001_urgency=Critical audit findings require immediate design team attention, thread_002_urgency=Secondary audit review completed, escalate_to=emma.creative@company.com,jake.design@company.com, audit_type=COMBINED_DS_A11Y, created_after=2024-08-20T15:00:00Z, audit_date_filter=2024-08-18T00:00:00Z, thread_ids=thread_001,thread_002, artifact_ids=art_001,art_008"
        ),
        actions=[
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_001"}),
            Action(name="UpdateAuditReportStatus", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed with recommendations"}),
            Action(name="GetAuditsByStatus", kwargs={"status": "COMPLETED", "audit_type": "COMBINED_DS_A11Y"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical audit findings require immediate design team attention", "escalate_to": ["emma.creative@company.com", "jake.design@company.com"]}),
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_002"}),
            Action(name="GetAuditsByStatus", kwargs={"artifact_id": "art_001", "created_after": "2024-08-20T15:00:00Z"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Secondary audit review completed"}),
            Action(name="GetAuditsByStatus", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"}),
            Action(name="GetSystemConfigByCategory", kwargs={"category": "audit_config"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_74",
        instruction=(
            "Oversee the coordination of multi-audit status management and comprehensive compliance reporting as an audit compliance specialist. Your main task is managing audit_005 for artifact art_007 (Dashboard Components) to ensure a status change from COMPLETED to ultimate compliance verification, along with generating a complete audit report. This task involves coordinating audit_006, a design system mapping audit, requiring status synchronization and thread_005 communication escalation. Focus on audit status management for audit_005 under a COMBINED_DS_A11Y audit type while verifying audit_006 DS_MAPPING audit completion and managing thread_005 priority escalation to NORMAL under mike.dev@company.com oversight for comprehensive compliance tracking. Your efforts should enable seamless multi-audit compliance reporting through meticulous audit status verification, proficient compliance documentation management, and thorough audit type coordination for stakeholder compliance reports. Required constants: primary_audit_id=audit_005, secondary_audit_id=audit_006, artifact_id=art_007, thread_id=thread_005, assignee_email=mike.dev@company.com, priority_level=NORMAL, audit_type=COMBINED_DS_A11Y, secondary_audit_type=DS_MAPPING, report_asset_id=asset_006, status=COMPLETED, escalation_reason=Multi-audit compliance verification requires development team coordination, created_after=2024-08-22T11:00:00Z, completion_notes=Multi-audit compliance verification completed, log_message=Multi-audit compliance reporting workflow completed for audit_005 and audit_006, log_level=INFO, component=compliance_reporting, user_email=mike.dev@company.com"
        ),
        actions=[
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_005", "status": "COMPLETED"}),
            Action(name="UpdateAuditReportStatus", kwargs={"audit_id": "audit_005", "new_status": "COMPLETED", "report_asset_id": "asset_006", "completion_notes": "Multi-audit compliance verification completed"}),
            Action(name="GetAuditsByStatus", kwargs={"audit_type": "COMBINED_DS_A11Y", "artifact_id": "art_007"}),
            Action(name="GetAuditSummary", kwargs={"audit_id": "audit_005"}),
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_006", "audit_type": "DS_MAPPING"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_005", "new_priority": "NORMAL", "urgency_reason": "Multi-audit compliance verification requires development team coordination", "escalate_to": ["mike.dev@company.com"]}),
            Action(name="GetAuditReportSummary", kwargs={"audit_id": "audit_006", "audit_type": "DS_MAPPING"}),
            Action(name="AddTerminalLogEntry", kwargs={"log_message": "Multi-audit compliance reporting workflow completed for audit_005 and audit_006", "log_level": "INFO", "component": "compliance_reporting", "user_email": "mike.dev@company.com"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_75",
        instruction=(
            "As a fix plan delivery coordinator, your role involves managing extensive fix plan delivery workflows and overseeing the coordination of release versions. Your responsibility is to handle the delivery process of fix plans while ensuring effective release version management and verifying asset exports. Concentrate on overseeing the fix plan delivery process transitioning from DRAFTED to DELIVERED status, paying attention to release version updates and export arrangements. Work with development teams via suitable communication channels to guarantee proper tracking of all fix deliverables. Required constants: plan_id=plan_002, new_status=DELIVERED, delivery_method=TICKETS, owner_email=emma.creative@company.com, release_id=release_001, version_id=v1.4.0, release_name=Design System v1.4.0 - Fix Implementation Updates, thread_id=thread_006, asset_id=asset_001, export_status=COMPLETED, export_notes=Fix plan delivery assets exported successfully, dlp_scan_status=CLEAN, created_after=2024-08-22T18:00:00Z, log_message=Fix plan delivery coordination completed for plan_002 with release version v1.4.0, log_level=INFO, component=fix_delivery, user_email=emma.creative@company.com"
        ),
        actions=[
            Action(name="GetFixPlanItems", kwargs={"plan_id": "plan_002"}),
            Action(name="UpdateFixPlanStatus", kwargs={"plan_id": "plan_002", "new_status": "DELIVERED", "delivery_method": "TICKETS", "owner_email": "emma.creative@company.com"}),
            Action(name="GetReleasesByOwner", kwargs={"owner_email": "emma.creative@company.com", "created_after": "2024-08-22T18:00:00Z"}),
            Action(name="UpdateReleaseVersion", kwargs={"release_id": "release_001", "version_id": "v1.4.0", "release_name": "Design System v1.4.0 - Fix Implementation Updates", "owner_email": "emma.creative@company.com", "thread_id": "thread_006"}),
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_001"}),
            Action(name="UpdateAssetExportStatus", kwargs={"asset_id": "asset_001", "new_status": "COMPLETED", "notes": "Fix plan delivery assets exported successfully", "dlp_scan_status": "CLEAN"}),
            Action(name="AddTerminalLogEntry", kwargs={"log_message": "Fix plan delivery coordination completed for plan_002 with release version v1.4.0", "log_level": "INFO", "component": "fix_delivery", "user_email": "emma.creative@company.com"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_76",
        instruction=(
            "As a specialist in review cycle SLA management, you are tasked with coordinating review cycle escalations and managing integrated audit workflows. Your duty is to oversee the coordination of review cycle SLAs alongside audit status management, ensuring that escalations are tracked correctly. Concentrate on managing the transition of review cycle statuses from NEEDS_REVIEW to ESCALATED, while coordinating audit statuses and maintaining thorough logging. Collaborate with review teams through suitable channels to ensure SLAs and audit workflows are synchronized effectively. Required constants: cycle_id=cycle_001, artifact_id=art_001, new_status=ESCALATED, audit_id=audit_001, audit_status=IN_PROGRESS, updated_by=emma.creative@company.com, thread_id=thread_001, priority_level=HIGH, urgency_reason=SLA breach requires immediate escalation, escalate_to=emma.creative@company.com, log_level=WARNING, component=review_sla, after_timestamp=2024-08-20T15:00:00Z, message_pattern=escalation, log_message=Review cycle SLA escalation completed with audit integration"
        ),
        actions=[
            Action(name="GetReviewApprovalsSummary", kwargs={"cycle_id": "cycle_001"}),
            Action(name="UpdateReviewCycleStatus", kwargs={"cycle_id": "cycle_001", "new_status": "ESCALATED", "reviewer_email": "emma.creative@company.com", "completion_notes": "SLA breach requires immediate escalation"}),
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_001"}),
            Action(name="UpdateAuditStatus", kwargs={"audit_id": "audit_001", "new_status": "IN_PROGRESS", "updated_by": "emma.creative@company.com"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "SLA breach requires immediate escalation"}),
            Action(name="AddTerminalLogEntry", kwargs={"log_message": "Review cycle SLA escalation completed with audit integration", "log_level": "WARNING", "component": "review_sla", "user_email": "emma.creative@company.com"}),
            Action(name="GetFilteredLogEntries", kwargs={"log_level": "WARNING", "component": "review_sla", "after_timestamp": "2024-08-20T15:00:00Z", "message_pattern": "escalation"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_77",
        instruction=(
            "As a specialist in managing audit reports, your responsibility is to handle the entire audit process for design system components and ensure they meet accessibility standards. Your role includes overseeing the completion of audits and maintaining accurate status tracking for these components. Concentrate on advancing the audit workflow from IN_PROGRESS to COMPLETED status, which includes generating reports and communicating with stakeholders. Required constants: audit_id=audit_001, new_status=COMPLETED, report_asset_id=asset_001, completion_notes=Design system audit completed with recommendations, thread_001_priority=HIGH, thread_002_priority=NORMAL, thread_001_urgency=Critical audit findings require immediate design team attention, escalate_to=emma.creative@company.com,jake.design@company.com, audit_type=COMBINED_DS_A11Y, created_after=2024-08-20T15:00:00Z, audit_date_filter=2024-08-18T00:00:00Z, thread_ids=thread_001,thread_002, artifact_ids=art_001,art_008"
        ),
        actions=[
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_001"}),
            Action(name="UpdateAuditReportStatus", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed with recommendations"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical audit findings require immediate design team attention", "escalate_to": ["emma.creative@company.com", "jake.design@company.com"]}),
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_002"}),
            Action(name="UpdateAuditReportStatus", kwargs={"audit_id": "audit_002", "new_status": "COMPLETED", "report_asset_id": "asset_007"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Secondary audit review completed"}),
            Action(name="GetAuditsByStatus", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"}),
            Action(name="AddTerminalLogEntry", kwargs={"log_message": "Audit report management workflow completed for audit_001 and audit_002 with comprehensive status tracking", "log_level": "INFO", "component": "audit_management", "user_email": "emma.creative@company.com"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_78",
        instruction=(
            "As a mobile component audit integration expert, your task is to coordinate extensive mobile audit workflows and manage the release processes for mobile app components. Your main duty is the management of audit_002, which demands thorough status tracking and escalation of thread_002 with CRITICAL priority to coordinate the mobile dashboard release. This workflow incorporates approval checks for mobile workflows and keeps track of the comprehensive audit for mobile app readiness. The integration workflow for mobiles focuses on in-depth audit coordination under the supervision of jake.design@company.com, handling thread_007 with HIGH priority for mobile app release coordination, and meticulous tracking of approvals for mobile component workflows with an emphasis on preparing for release. Your coordination should assure smooth mobile audit integration by managing status comprehensively, effectively escalating priorities for mobile release threads, and precisely verifying approvals for mobile workflows, all while coordinating with the UX team and tracking release readiness. Required constants: audit_id=audit_002, thread_002_id=thread_002, thread_007_id=thread_007, thread_002_priority=CRITICAL, thread_007_priority=HIGH, thread_002_urgency=Mobile application release requires immediate coordination, thread_007_urgency=Mobile app release coordination support required, completion_notes=Mobile component audit completed with accessibility integration, approval_002_id=approval_002, cycle_002_id=cycle_002, audit_type=A11Y, created_after_date=2024-08-19T12:00:00Z, escalate_to=jake.design@company.com,mobile.team@company.com, owner_email=jake.design@company.com"
        ),
        actions=[
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_002"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_002", "new_priority": "CRITICAL", "urgency_reason": "Mobile application release requires immediate coordination", "escalate_to": ["jake.design@company.com", "mobile.team@company.com"]}),
            Action(name="GetReviewApprovalsSummary", kwargs={"approval_id": "approval_002", "cycle_id": "cycle_002"}),
            Action(name="GetAuditsByStatus", kwargs={"created_after": "2024-08-19T12:00:00Z", "audit_type": "A11Y"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_007", "new_priority": "HIGH", "urgency_reason": "Mobile app release coordination support required"}),
            Action(name="GetReleasesByOwner", kwargs={"owner_email": "jake.design@company.com", "created_after": "2024-08-19T12:00:00Z"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_79",
        instruction=(
            "Serve as a Figma comment and fix item resolution expert dedicated to overseeing accessibility feedback and the tracking of related fix items. Your role involves handling accessibility enhancements, monitoring comment resolutions, managing fix items, and ensuring effective team communication. Concentrate on updating comment statuses, monitoring the progress of fix items, delegating tasks, and verifying the export of assets. Required constants: artifact_id=art_008, asset_id=asset_007, comment_ids=comment_006,comment_009, fix_item_id=item_016, new_status=IN_PROGRESS, assignee_id=dev_team@company.com, thread_id=thread_004, priority_level=HIGH, comment_assignee_1=jake.design@company.com, comment_assignee_2=emma.creative@company.com, resolution_notes=Accessibility improvements in progress - adding ARIA labels and keyboard navigation support, implementation_notes=Starting work on accessibility improvements for admin panel header"
        ),
        actions=[
            Action(name="GetFigmaCommentsByArtifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_007"}),
            Action(name="UpdateFigmaCommentStatus", kwargs={"comment_id": "comment_006", "new_status": "IN_PROGRESS", "resolution_notes": "Accessibility improvements in progress - adding ARIA labels and keyboard navigation support", "assignee_email": "jake.design@company.com", "priority_level": "HIGH"}),
            Action(name="GetGmailThreadsByLabels", kwargs={"thread_id": "thread_004"}),
            Action(name="UpdateFixItemStatus", kwargs={"fix_item_id": "item_016", "new_status": "IN_PROGRESS", "assignee_id": "dev_team@company.com", "implementation_notes": "Starting work on accessibility improvements for admin panel header"}),
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_007"}),
            Action(name="UpdateFigmaCommentStatus", kwargs={"comment_id": "comment_009", "new_status": "RESOLVED", "assignee_email": "emma.creative@company.com"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_80",
        instruction=(
            "Act as a thorough release management coordinator charged with orchestrating comprehensive release workflows including audit integration and Gmail communication oversight for design system components. Your responsibilities include overseeing release status updates, managing asset export, verifying system configuration, ensuring audit compliance, and managing Gmail threads for design system releases. Concentrate on guaranteeing full release lifecycle management with audit integration, asset export status oversight, system configuration management, and coordinating Gmail communications regarding release workflows. Collaborate with design and development teams via suitable channels to make sure all release workflows are executed, documented, and communicated with stakeholder updates. Required constants: release_id=release_003, new_status=PUBLISHED, release_notes=Design system components release with accessibility improvements, updated_by=emma.creative@company.com, asset_id=asset_003, export_status=COMPLETED, export_notes=Design system asset export completed with accessibility compliance, dlp_scan_status=CLEAN, owner_email=emma.creative@company.com, created_after=2024-08-20T15:00:00Z, category=release_management_config, log_message=Release management workflow completed with system configuration, log_level=INFO, component=release_management, audit_id=audit_002, thread_id=thread_002, thread_priority=NORMAL, urgency_reason=Release configuration updates completed successfully"
        ),
        actions=[
            Action(name="UpdateReleaseStatus", kwargs={"release_id": "release_003", "new_status": "PUBLISHED", "release_notes": "Design system components release with accessibility improvements", "updated_by": "emma.creative@company.com"}),
            Action(name="UpdateAssetExportStatus", kwargs={"asset_id": "asset_003", "new_status": "COMPLETED", "notes": "Design system asset export completed with accessibility compliance", "dlp_scan_status": "CLEAN"}),
            Action(name="GetReleasesByOwner", kwargs={"owner_email": "emma.creative@company.com", "created_after": "2024-08-20T15:00:00Z"}),
            Action(name="GetSystemConfigByCategory", kwargs={"category": "release_management_config"}),
            Action(name="GetAuditSummary", kwargs={"audit_id": "audit_002"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Release configuration updates completed successfully"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_81",
        instruction=(
            "As a design system component audit specialist, you are tasked with orchestrating comprehensive audits and overseeing thread priority management within component workflows. Your central duty involves the coordination of audit_002 related to design system components needing detailed status tracking and priority management of threads for component review coordination. This workflow integrates with approval verification and thread escalation to prepare for design system release. The focus is on thorough audit tracking, supervised by emma.creative@company.com, handling thread_001 with HIGH priority management for design system coordination, and ensuring detailed approval verification across the workflows. Your efforts should ensure smooth coordination of audits through rigorous status tracking, effective management of thread priorities during component reviews, and detailed approval verification within design system workflows, aligned with proper coordination with the design team and timely release preparations. Key parameters: audit_002_id=audit_002, audit_002_status=COMPLETED, art_008_id=art_008, audit_type=A11Y, thread_001_id=thread_001, thread_008_id=thread_008, thread_001_priority=HIGH, thread_008_priority=NORMAL, thread_001_urgency=Design system component review requires immediate coordination, thread_008_urgency=Design system follow-up coordination completed, completion_notes=Design system component audit completed successfully, approval_002_id=approval_002, cycle_002_id=cycle_002, escalate_to=emma.creative@company.com,design.system@company.com, release_owner=emma.creative@company.com, release_start_date=2024-08-20T13:00:00Z"
        ),
        actions=[
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_002"}),
            Action(name="UpdateAuditReportStatus", kwargs={"audit_id": "audit_002", "new_status": "COMPLETED", "completion_notes": "Design system component audit completed successfully"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Design system component review requires immediate coordination", "escalate_to": ["emma.creative@company.com", "design.system@company.com"]}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_008", "new_priority": "NORMAL", "urgency_reason": "Design system follow-up coordination completed"}),
            Action(name="GetReviewApprovalsSummary", kwargs={"approval_id": "approval_002", "cycle_id": "cycle_002"}),
            Action(name="GetAuditsByStatus", kwargs={"artifact_id": "art_008", "audit_type": "A11Y"}),
            Action(name="GetReleasesByOwner", kwargs={"owner_email": "emma.creative@company.com", "created_after": "2024-08-20T13:00:00Z"}),
            Action(name="GetAuditFindingsSummary", kwargs={"audit_id": "audit_002", "include_resolved": True}),
            Action(name="GetSystemConfigByCategory", kwargs={"category": "design_system_audit_config"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_82",
        instruction=(
            "You are tasked as an audit report management specialist, responsible for overseeing the entire audit lifecycle for design system components and ensuring accessibility compliance. Your key responsibility is managing audit_001 for artifact art_001 (Homepage Hero Section), which involves exhaustive status tracking from COMPLETED to the generation of the final report. This workflow connects with audit_002 for reviewing the accessibility of admin panel components in art_008, requiring status coordination. Focusing on thread_001, the workflow demands priority escalation to HIGH for coordinating design reviews, overseen by emma.creative@company.com, and escalating the URGENT priority level for comprehensive design review monitoring, all due to the reason 'Critical audit findings require immediate design team attention and stakeholder review'. Priority management insists on effective Gmail thread coordination and meticulous documentation of audit statuses. Your tasks should guarantee the efficient generation of audit reports through accurate status management, successful priority escalation during design review threads, detailed tracking of audit findings for stakeholder reports, and a successful audit lifecycle completion, with correct report asset associations. Key parameters: audit_id=audit_001, new_status=COMPLETED, report_asset_id=asset_001, completion_notes=Design system audit completed with recommendations, thread_001_priority=HIGH, thread_002_priority=NORMAL, thread_001_urgency=Critical audit findings require immediate design team attention, thread_002_urgency=Secondary audit review completed, escalate_to=emma.creative@company.com,jake.design@company.com, audit_type=COMBINED_DS_A11Y, created_after=2024-08-20T15:00:00Z, audit_date_filter=2024-08-18T00:00:00Z, thread_ids=thread_001,thread_002, artifact_ids=art_001,art_008, asset_id=asset_001"
        ),
        actions=[
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_001"}),
            Action(name="UpdateAuditReportStatus", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed with recommendations"}),
            Action(name="GetAuditsByStatus", kwargs={"status": "COMPLETED", "audit_type": "COMBINED_DS_A11Y"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical audit findings require immediate design team attention", "escalate_to": ["emma.creative@company.com", "jake.design@company.com"]}),
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_002"}),
            Action(name="UpdateAuditReportStatus", kwargs={"audit_id": "audit_002", "new_status": "COMPLETED", "report_asset_id": "asset_007"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Secondary audit review completed"}),
            Action(name="GetAuditsByStatus", kwargs={"status": "COMPLETED", "created_after": "2024-08-20T15:00:00Z"}),
            Action(name="GetAuditsByStatus", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"}),
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_001"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_83",
        instruction=(
            "You are a Figma comment and communication specialist tasked with overseeing accessibility feedback and associated email communications. It is your duty to handle accessibility enhancements, monitor comment resolution, manage email thread priorities, and maintain effective communication across teams. Emphasize managing comment status updates, setting suitable email priorities, assigning responsibilities, and confirming asset exports. Required constants: artifact_id=art_008, asset_id=asset_007, comment_ids=comment_006,comment_009, thread_id=thread_004, thread_priority=HIGH, urgency_reason=Accessibility compliance deadline approaching, escalate_to=accessibility-team@company.com,design-leads@company.com, resolution_notes=Accessibility improvements in progress - adding ARIA labels and keyboard navigation support"
        ),
        actions=[
            Action(name="GetFigmaCommentsByArtifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_007"}),
            Action(name="UpdateFigmaCommentStatus", kwargs={"comment_id": "comment_006", "new_status": "IN_PROGRESS", "resolution_notes": "Accessibility improvements in progress - adding ARIA labels and keyboard navigation support", "assignee_email": "jake.design@company.com", "priority_level": "HIGH"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_004", "new_priority": "HIGH", "urgency_reason": "Accessibility compliance deadline approaching", "escalate_to": ["accessibility-team@company.com", "design-leads@company.com"]}),
            Action(name="GetGmailThreadsByLabels", kwargs={"thread_id": "thread_004"}),
            Action(name="UpdateFigmaCommentStatus", kwargs={"comment_id": "comment_009", "new_status": "RESOLVED", "assignee_email": "emma.creative@company.com"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_84",
        instruction=(
            "As an information gathering specialist, you are responsible for orchestrating comprehensive information collection and Gmail message status update workflows. It is your role to compile system information from various sources and synchronize Gmail message status with proper coordination. Prioritize collecting audit data, release details, asset exports, and terminal logs in coordination with Gmail message status. Collaborate with communication teams through the appropriate channels to ensure all information gathering and message status workflows are efficiently managed. Required constants: audit_id=audit_004, release_id=release_002, asset_id=asset_004, owner_email=jake.design@company.com, created_after=2024-08-19T12:30:00Z, log_level=INFO, component=information_gathering, message_id=msg_002, new_status=READ, updated_by=jake.design@company.com, plan_id=plan_002"
        ),
        actions=[
            Action(name="GetAuditSummary", kwargs={"audit_id": "audit_004"}),
            Action(name="GetReleaseSummary", kwargs={"release_id": "release_002"}),
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_004"}),
            Action(name="GetReleasesByOwner", kwargs={"owner_email": "jake.design@company.com", "created_after": "2024-08-19T12:30:00Z"}),
            Action(name="GetTerminalLogsSummary", kwargs={"log_level": "INFO", "component": "information_gathering"}),
            Action(name="GetFixPlanItems", kwargs={"plan_id": "plan_002"}),
            Action(name="UpdateGmailMessageStatus", kwargs={"message_id": "msg_002", "new_status": "READ", "updated_by": "jake.design@company.com"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_85",
        instruction=(
            "You act as an asset management specialist tasked with handling extensive asset management along with fixing item status processes. Your role includes overseeing asset exports, configuring systems, and coordinating fix item status for adherence to the design system. Concentrate on overseeing asset exports, analyzing system configurations, reviewing audits, and updating fix item statuses with proper coordination. Communicate with development teams via suitable channels to ensure all asset management and fix item processes are smoothly coordinated. Required constants: asset_id=asset_005, category=design_system_aliases, audit_id=audit_006, thread_id=thread_006, owner_email=emma.creative@company.com, created_after=2024-08-21T14:00:00Z, log_level=INFO, component=asset_management, fix_item_id=item_003, new_status=APPLIED, updated_by=emma.creative@company.com, notes=Asset management coordination completed with design system compliance"
        ),
        actions=[
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_005"}),
            Action(name="GetSystemConfigByCategory", kwargs={"category": "design_system_aliases"}),
            Action(name="GetAuditSummary", kwargs={"audit_id": "audit_006"}),
            Action(name="GetGmailThreadsByLabels", kwargs={"thread_id": "thread_006"}),
            Action(name="GetReleasesByOwner", kwargs={"owner_email": "emma.creative@company.com", "created_after": "2024-08-21T14:00:00Z"}),
            Action(name="GetTerminalLogsSummary", kwargs={"log_level": "INFO", "component": "asset_management"}),
            Action(name="UpdateFixItemStatus", kwargs={"fix_item_id": "item_003", "new_status": "APPLIED", "updated_by": "emma.creative@company.com", "notes": "Asset management coordination completed with design system compliance"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_86",
        instruction=(
            "You serve as a release diff analysis specialist charged with managing release difference tracking and running integrated comment resolution processes. Your duty includes coordinating release diff processes with figma comment resolution while ensuring accurate version tracking. Prioritize handling release version updates with thorough comment status coordination and verifying asset exports. Liaise with development teams through effective channels to guarantee all release diffs and comment workflows are consistently synchronized. Required constants: release_id=release_001, version_id=v1.4.0, release_name=Design System v1.4.0 - Diff Analysis Updates, owner_email=emma.creative@company.com, comment_id=comment_001, new_status=RESOLVED, assignee_email=emma.creative@company.com, priority_level=NORMAL, resolution_notes=Release diff analysis completed with comprehensive comment resolution, artifact_id=art_001, asset_id=asset_001, export_status=COMPLETED, dlp_scan_status=CLEAN, created_after=2024-08-20T15:00:00Z, thread_id=thread_001, export_notes=Release diff analysis asset export completed"
        ),
        actions=[
            Action(name="GetReleaseDiffSummary", kwargs={"release_id": "release_001"}),
            Action(name="UpdateReleaseVersion", kwargs={"release_id": "release_001", "version_id": "v1.4.0", "release_name": "Design System v1.4.0 - Diff Analysis Updates", "owner_email": "emma.creative@company.com", "thread_id": "thread_001"}),
            Action(name="GetFigmaCommentsByArtifact", kwargs={"artifact_id": "art_001", "resolved_status": False}),
            Action(name="UpdateFigmaCommentStatus", kwargs={"comment_id": "comment_001", "new_status": "RESOLVED", "resolution_notes": "Release diff analysis completed with comprehensive comment resolution", "assignee_email": "emma.creative@company.com", "priority_level": "NORMAL"}),
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_001"}),
            Action(name="UpdateAssetExportStatus", kwargs={"asset_id": "asset_001", "new_status": "COMPLETED", "notes": "Release diff analysis asset export completed", "dlp_scan_status": "CLEAN"}),
            Action(name="GetReleasesByOwner", kwargs={"owner_email": "emma.creative@company.com", "created_after": "2024-08-20T15:00:00Z"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_87",
        instruction=(
            "You are tasked with the responsibility of overseeing accessibility improvements for the admin panel header components. Your goal is to ensure every piece of accessibility feedback is thoroughly addressed and monitored to completion. This involves working with the UX team on the implementation of ARIA labels as well as keyboard navigation enhancements, checking on the export status of accessibility improvements, and sustaining open communication channels. All actions should be meticulously documented for compliance and tracking requirements. Key parameters: artifact_id=art_008, asset_id=asset_007, comment_id=comment_006, assignee_email=jake.design@company.com, priority_level=HIGH, resolution_notes=Accessibility improvements in progress - adding ARIA labels and keyboard navigation support, export_notes=Admin header accessibility export completed with ARIA labels, dlp_scan_status=CLEAN, thread_id=thread_004"
        ),
        actions=[
            Action(name="GetFigmaCommentsByArtifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_007"}),
            Action(name="UpdateFigmaCommentStatus", kwargs={"comment_id": "comment_006", "new_status": "IN_PROGRESS", "resolution_notes": "Accessibility improvements in progress - adding ARIA labels and keyboard navigation support", "assignee_email": "jake.design@company.com", "priority_level": "HIGH"}),
            Action(name="GetGmailThreadsByLabels", kwargs={"thread_id": "thread_004"}),
            Action(name="GetFigmaCommentsByArtifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="UpdateAssetExportStatus", kwargs={"asset_id": "asset_007", "new_status": "COMPLETED", "notes": "Admin header accessibility export completed with ARIA labels", "dlp_scan_status": "CLEAN"}),
            Action(name="GetFigmaArtifactsByStatus", kwargs={"artifact_id": "art_008"}),
            Action(name="AddTerminalLogEntry", kwargs={"log_message": "Figma comment resolution workflow completed for art_008 admin panel header with accessibility improvements and export status updates", "log_level": "INFO", "component": "comment_resolution", "user_email": "jake.design@company.com"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_88",
        instruction=(
            "You serve as a specialist in mobile audit findings severity management, responsible for orchestrating audit finding severity updates and integrated fix plan workflows. You are to handle the escalation of audit finding severity while coordinating fix plan statuses and ensuring effective priority management. Concentrate on updating the severity of audit findings for CRITICAL violations, including orchestrating fix plan delivery and detailed tracking of fix items. Work in collaboration with development teams through the right channels to guarantee all audit findings and fix workflows are well-aligned. Additionally, you should gather audit summaries to provide broad oversight and coordination throughout the severity management procedure. Required constants: finding_id=finding_a11y_001, new_severity=CRITICAL, updated_by=chris.engineer@company.com, plan_id=plan_001, delivery_method=TICKETS, owner_email=chris.engineer@company.com, item_id=item_001, fix_item_id=item_001, new_priority=HIGH, priority_reason=Critical finding requires immediate fix attention, audit_id=audit_002, violation_type=COLOR_CONTRAST, severity=CRITICAL, log_message=Audit findings severity management and fix plan coordination completed, log_level=INFO, log_component=audit_severity, comment_id=comment_006, comment_status=RESOLVED"
        ),
        actions=[
            Action(name="UpdateAuditFindingSeverity", kwargs={"finding_id": "finding_a11y_001", "new_severity": "CRITICAL", "updated_by": "chris.engineer@company.com"}),
            Action(name="GetAuditFindingsByType", kwargs={"violation_type": "COLOR_CONTRAST", "severity": "CRITICAL"}),
            Action(name="GetFixPlanItems", kwargs={"plan_id": "plan_001"}),
            Action(name="UpdateFixPlanStatus", kwargs={"plan_id": "plan_001", "new_status": "IN_PROGRESS", "delivery_method": "TICKETS", "owner_email": "chris.engineer@company.com"}),
            Action(name="UpdateFixItemPriority", kwargs={"item_id": "item_001", "new_priority": "HIGH", "priority_reason": "Critical finding requires immediate fix attention", "updated_by": "chris.engineer@company.com"}),
            Action(name="UpdateFixItemStatus", kwargs={"fix_item_id": "item_001", "new_status": "IN_PROGRESS", "updated_by": "chris.engineer@company.com"}),
            Action(name="AddTerminalLogEntry", kwargs={"log_message": "Audit findings severity management and fix plan coordination completed", "log_level": "INFO", "component": "audit_severity", "user_email": "chris.engineer@company.com"}),
            Action(name="GetAuditSummary", kwargs={"audit_id": "audit_002"}),
            Action(name="UpdateFigmaCommentStatus", kwargs={"comment_id": "comment_006", "new_status": "RESOLVED", "resolved_by": "chris.engineer@company.com"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_89",
        instruction=(
            "Handle the role of a multi-platform release management specialist responsible for coordinating comprehensive release orchestration and dual status update workflows. Your task involves managing multi-platform release coordination, audit findings analysis, asset export verification, and dual status updates for enterprise release orchestration. Concentrate on managing release summary coordination, tracking audit findings, verifying asset exports, conducting system configuration analysis, and dual status update workflows with multi-platform coordination. Coordinate with release orchestration teams via appropriate channels to ensure all multi-platform release management and dual status update workflows are properly coordinated. Required constants: release_id=release_010, audit_id=audit_012, violation_type=FOCUS_INDICATOR, severity=HIGH, asset_id=asset_018, owner_email=emma.creative@company.com, created_after=2024-08-23T16:30:00Z, thread_id=thread_013, log_level=INFO, component=multi_platform_release, category=notification_settings, plan_id=plan_011, new_plan_status=DELIVERED, delivery_method=TICKETS, plan_notes=Multi-platform release coordination completed with comprehensive orchestration, new_asset_status=COMPLETED, dlp_scan_status=CLEAN, notes=Multi-platform release management coordination completed with comprehensive tracking"
        ),
        actions=[
            Action(name="GetReleaseSummary", kwargs={"release_id": "release_010"}),
            Action(name="GetAuditFindingsByType", kwargs={"violation_type": "FOCUS_INDICATOR", "severity": "HIGH"}),
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_018"}),
            Action(name="GetReleasesByOwner", kwargs={"owner_email": "emma.creative@company.com", "created_after": "2024-08-23T16:30:00Z"}),
            Action(name="GetGmailThreadsByLabels", kwargs={"thread_id": "thread_013"}),
            Action(name="GetTerminalLogsSummary", kwargs={"log_level": "INFO", "component": "multi_platform_release"}),
            Action(name="GetSystemConfigByCategory", kwargs={"category": "notification_settings"}),
            Action(name="UpdateFixPlanStatus", kwargs={"plan_id": "plan_011", "new_status": "DELIVERED", "delivery_method": "TICKETS", "owner_email": "emma.creative@company.com", "notes": "Multi-platform release coordination completed with comprehensive orchestration"}),
            Action(name="UpdateAssetExportStatus", kwargs={"asset_id": "asset_018", "new_status": "COMPLETED", "notes": "Multi-platform release management coordination completed with comprehensive tracking", "dlp_scan_status": "CLEAN"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_90",
        instruction=(
            "Take charge as a design system integration specialist responsible for coordinating comprehensive design system workflows and dual audit/asset update processes. Your task is to manage design system integration coordination, figma artifact tracking, audit summary analysis, and dual update processes for enterprise design system management. Direct your focus on managing figma artifact coordination, analyzing design system configuration, tracking audit summaries, coordinating releases, and dual update workflows ensuring comprehensive design system integration. Coordinate with design system teams through appropriate channels to ensure all integration and dual update workflows are properly orchestrated. Required constants: status=ACTIVE, category=design_system_aliases, audit_id=audit_010, thread_id=thread_012, owner_email=emma.creative@company.com, created_after=2024-08-23T15:30:00Z, log_level=INFO, component=design_system_integration, asset_id=asset_016, new_audit_status=COMPLETED, audit_notes=Design system integration coordination completed with comprehensive tracking, new_asset_status=COMPLETED, asset_notes=Design system asset coordination completed with integration tracking, dlp_scan_status=CLEAN"
        ),
        actions=[
            Action(name="GetFigmaArtifactsByStatus", kwargs={"status": "ACTIVE"}),
            Action(name="GetSystemConfigByCategory", kwargs={"category": "design_system_aliases"}),
            Action(name="GetAuditSummary", kwargs={"audit_id": "audit_010"}),
            Action(name="GetGmailThreadsByLabels", kwargs={"thread_id": "thread_012"}),
            Action(name="GetReleasesByOwner", kwargs={"owner_email": "emma.creative@company.com", "created_after": "2024-08-23T15:30:00Z"}),
            Action(name="GetTerminalLogsSummary", kwargs={"log_level": "INFO", "component": "design_system_integration"}),
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_016"}),
            Action(name="UpdateAuditStatus", kwargs={"audit_id": "audit_010", "new_status": "COMPLETED", "notes": "Design system integration coordination completed with comprehensive tracking", "updated_by": "emma.creative@company.com"}),
            Action(name="UpdateAssetExportStatus", kwargs={"asset_id": "asset_016", "new_status": "COMPLETED", "notes": "Design system asset coordination completed with integration tracking", "dlp_scan_status": "CLEAN"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_91",
        instruction=(
            "Handle the audit report management as a specialist by overseeing the entire audit lifecycle for design system components with a focus on accessibility compliance. Your main task is to manage audit_001 for artifact art_001 (Homepage Hero Section), requiring thorough status monitoring from COMPLETED to final report issuance. This workflow is linked with audit_002 for the accessibility review of art_008 admin panel components, needing status coordination. Ensure audit management workflow prioritizes thread_001, escalating its priority to HIGH for design review coordination under the oversight of emma.creative@company.com. URGENT priority level escalation is necessary for detailed design review tracking with the escalation_reason 'Critical audit findings require immediate design team attention and stakeholder review'. Priority management involves detailed coordination of Gmail threads and meticulous documentation of audit statuses. Your efforts should lead to seamless audit report production through efficient status management, priority escalation for design review threads, comprehensive audit findings tracking for stakeholder reporting, and the successful completion of the audit lifecycle with correct report asset associations. Important parameters include: audit_id=audit_001, new_status=COMPLETED, report_asset_id=asset_001, completion_notes=Design system audit completed with recommendations, thread_001_priority=HIGH, thread_002_priority=NORMAL, thread_001_urgency=Critical audit findings require immediate design team attention, thread_002_urgency=Secondary audit review completed, escalate_to=emma.creative@company.com,jake.design@company.com, audit_type=COMBINED_DS_A11Y, created_after=2024-08-20T15:00:00Z, audit_date_filter=2024-08-18T00:00:00Z, thread_ids=thread_001,thread_002, artifact_ids=art_001,art_008, log_message=Audit management workflow completed with comprehensive status tracking and report generation, log_level=INFO, component=audit_management, user_email=emma.creative@company.com"
        ),
        actions=[
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_001"}),
            Action(name="UpdateAuditReportStatus", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed with recommendations"}),
            Action(name="GetAuditsByStatus", kwargs={"status": "COMPLETED", "audit_type": "COMBINED_DS_A11Y"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical audit findings require immediate design team attention", "escalate_to": ["emma.creative@company.com", "jake.design@company.com"]}),
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_002"}),
            Action(name="GetAuditsByStatus", kwargs={"artifact_id": "art_001", "created_after": "2024-08-20T15:00:00Z"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Secondary audit review completed"}),
            Action(name="GetAuditsByStatus", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"}),
            Action(name="GetSystemConfigByCategory", kwargs={"category": "audit_config"}),
            Action(name="AddTerminalLogEntry", kwargs={"log_message": "Audit management workflow completed with comprehensive status tracking and report generation", "log_level": "INFO", "component": "audit_management", "user_email": "emma.creative@company.com"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_92",
        instruction=(
            "Coordinate the comprehensive audits of design system components, managing thread priorities for component workflows as a specialist. Your primary duty is to manage audit_002 for design system components, which requires extensive status monitoring and thread priority handling for component review synchronization. This process incorporates approval verification and thread escalation to prepare for design system release. Manage the design system coordination by concentrating on audit tracking with oversight from emma.creative@company.com, managing thread_001 with HIGH priority for design system coordination, and carrying out thorough approval verification across the design system workflows. Your coordination should ensure faultless design system audit synchronization through meticulous status monitoring, effective management of thread priorities for component reviews, and detailed approval verification for system workflows, along with proper design team coordination and release preparation tracking. Key parameters are: audit_002_id=audit_002, audit_002_status=COMPLETED, art_008_id=art_008, audit_type=A11Y, thread_001_id=thread_001, thread_008_id=thread_008, thread_001_priority=HIGH, thread_008_priority=NORMAL, thread_001_urgency=Design system component review requires immediate coordination, thread_008_urgency=Design system follow-up coordination completed, completion_notes=Design system component audit completed successfully, approval_002_id=approval_002, cycle_002_id=cycle_002, escalate_to=emma.creative@company.com,design.system@company.com, release_owner=emma.creative@company.com, release_start_date=2024-08-20T13:00:00Z"
        ),
        actions=[
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_002"}),
            Action(name="UpdateAuditReportStatus", kwargs={"audit_id": "audit_002", "new_status": "COMPLETED", "completion_notes": "Design system component audit completed successfully"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Design system component review requires immediate coordination", "escalate_to": ["emma.creative@company.com", "design.system@company.com"]}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_008", "new_priority": "NORMAL", "urgency_reason": "Design system follow-up coordination completed"}),
            Action(name="GetReviewApprovalsSummary", kwargs={"approval_id": "approval_002", "cycle_id": "cycle_002"}),
            Action(name="GetAuditsByStatus", kwargs={"artifact_id": "art_008", "audit_type": "A11Y"}),
            Action(name="GetReleasesByOwner", kwargs={"owner_email": "emma.creative@company.com", "created_after": "2024-08-20T13:00:00Z"}),
            Action(name="GetAuditFindingsSummary", kwargs={"audit_id": "audit_002", "include_resolved": True}),
            Action(name="AddTerminalLogEntry", kwargs={"log_message": "Design system component audit workflow completed - audit_002 with thread priority management", "log_level": "INFO", "component": "design_system_audit", "user_email": "emma.creative@company.com"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_93",
        instruction=(
            "You are a design system compliance analysis specialist tasked with overseeing comprehensive workflows and audit update processes in design systems. Your responsibility includes handling design system compliance coordination, scrutinizing audit findings, tracking releases, and managing audit update processes for enterprise design system management. Emphasize managing audit findings coordination, analyzing release summaries, tracking system configurations, and executing audit update workflows while ensuring comprehensive compliance with the design system. Collaborate with design system compliance teams using appropriate communication channels to ensure all analysis and audit update workflows for the design system are correctly orchestrated. Required constants: violation_type=DESIGN_SYSTEM, severity=HIGH, release_id=release_008, category=design_system_aliases, thread_id=thread_011, owner_email=emma.creative@company.com, created_after=2024-08-23T13:00:00Z, log_level=INFO, component=design_system_compliance, audit_id=audit_008, new_audit_status=COMPLETED, audit_notes=Design system compliance analysis completed with comprehensive tracking, updated_by=emma.creative@company.com"
        ),
        actions=[
            Action(name="GetAuditFindingsByType", kwargs={"violation_type": "DESIGN_SYSTEM", "severity": "HIGH"}),
            Action(name="GetReleaseSummary", kwargs={"release_id": "release_008"}),
            Action(name="GetSystemConfigByCategory", kwargs={"category": "design_system_aliases"}),
            Action(name="GetGmailThreadsByLabels", kwargs={"thread_id": "thread_011"}),
            Action(name="GetReleasesByOwner", kwargs={"owner_email": "emma.creative@company.com", "created_after": "2024-08-23T13:00:00Z"}),
            Action(name="GetTerminalLogsSummary", kwargs={"log_level": "INFO", "component": "design_system_compliance"}),
            Action(name="GetAuditSummary", kwargs={"audit_id": "audit_008"}),
            Action(name="UpdateAuditStatus", kwargs={"audit_id": "audit_008", "new_status": "COMPLETED", "notes": "Design system compliance analysis completed with comprehensive tracking", "updated_by": "emma.creative@company.com"})
        ],
        outputs=[]
    ),
    Task(
        annotator="variant_4",
        user_id="user_94",
        instruction=(
            "You are an audit report coordination specialist entrusted with conducting comprehensive analysis and managing the workflows for audit report analysis and fix plan status. You need to oversee audit report coordination, analyze fix plans, and provide status updates regarding fix plans in audit management workflows. Concentrate on coordinating audit reports, analyzing fix plan items, tracking releases, and updating the status of fix plans with effective workflow management. Work in tandem with audit teams using appropriate channels to ensure all workflows related to audit reports and fix plans are efficiently managed. Required constants: audit_id=audit_008, plan_id=plan_006, release_id=release_001, owner_email=emma.creative@company.com, created_after=2024-08-22T16:45:00Z, thread_id=thread_014, log_level=INFO, component=audit_report_coordination, new_status=DELIVERED, delivery_method=TICKETS, notes=Audit report coordination completed with fix plan workflow"
        ),
        actions=[
            Action(name="GetAuditReportSummary", kwargs={"audit_id": "audit_008"}),
            Action(name="GetFixPlanItems", kwargs={"plan_id": "plan_006"}),
            Action(name="GetReleaseDiffSummary", kwargs={"release_id": "release_001"}),
            Action(name="GetReleasesByOwner", kwargs={"owner_email": "emma.creative@company.com", "created_after": "2024-08-22T16:45:00Z"}),
            Action(name="GetGmailThreadsByLabels", kwargs={"thread_id": "thread_014"}),
            Action(name="GetTerminalLogsSummary", kwargs={"log_level": "INFO", "component": "audit_report_coordination"}),
            Action(name="UpdateFixPlanStatus", kwargs={"plan_id": "plan_006", "new_status": "DELIVERED", "delivery_method": "TICKETS", "owner_email": "emma.creative@company.com", "notes": "Audit report coordination completed with fix plan workflow"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_95",
        instruction=(
            "As an audit report management specialist, you are tasked with handling the comprehensive audit lifecycle coordination for design system components and ensuring accessibility compliance. Your main duty is managing audit_001 for artifact art_001 (Homepage Hero Section), necessitating thorough status progression tracking from COMPLETED to final report creation. This workflow is linked with audit_002 for accessibility review of art_008 admin panel components, demanding status alignment. The audit management workflow is centered on elevating thread_001 to HIGH priority for design review coordination, overseen by emma.creative@company.com, as well as escalating to URGENT priority level for detailed design review tracking due to escalation_reason 'Critical audit findings require immediate design team attention and stakeholder review'. Proper management of Gmail threads and precise documentation of audit statuses are crucial. Your efforts should result in smooth audit report production through efficient status management, priority escalation for design review threads, and detailed tracking of audit findings for stakeholder reporting. Key parameters: audit_id=audit_001, new_status=COMPLETED, report_asset_id=asset_001, completion_notes=Design system audit completed with recommendations, thread_001_priority=HIGH, thread_002_priority=NORMAL, thread_001_urgency=Critical audit findings require immediate design team attention, thread_002_urgency=Secondary audit review completed, escalate_to=emma.creative@company.com,jake.design@company.com, audit_type=COMBINED_DS_A11Y, created_after=2024-08-20T15:00:00Z, audit_date_filter=2024-08-18T00:00:00Z, thread_ids=thread_001,thread_002, artifact_ids=art_001,art_008, asset_id=asset_001"
        ),
        actions=[
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_001"}),
            Action(name="UpdateAuditReportStatus", kwargs={"audit_id": "audit_001", "new_status": "COMPLETED", "report_asset_id": "asset_001", "completion_notes": "Design system audit completed with recommendations"}),
            Action(name="GetAuditsByStatus", kwargs={"status": "COMPLETED", "audit_type": "COMBINED_DS_A11Y"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical audit findings require immediate design team attention", "escalate_to": ["emma.creative@company.com", "jake.design@company.com"]}),
            Action(name="GetAuditsByStatus", kwargs={"audit_id": "audit_002"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_002", "new_priority": "NORMAL", "urgency_reason": "Secondary audit review completed"}),
            Action(name="GetAuditsByStatus", kwargs={"audit_type": "A11Y", "artifact_id": "art_008"}),
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_001"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_96",
        instruction=(
            "As a specialist in resolving Figma comments, your task involves managing accessibility improvements for the admin panel header. Ensure all accessibility feedback resolutions and associated assets and communications are effectively tracked. Focus on the workflow for accessibility enhancements, including comment resolution and updates on asset export status. Work closely with the UX team using the appropriate communication channels to meet all accessibility requirements. Required constants: artifact_id=art_008, asset_id=asset_007, comment_id=comment_006, assignee_email=jake.design@company.com, priority_level=HIGH, thread_ids=thread_004,thread_005, resolution_notes=Accessibility improvements in progress - adding ARIA labels and keyboard navigation support, export_notes=Admin header accessibility export completed with ARIA labels, dlp_scan_status=CLEAN, new_status=IN_PROGRESS, export_status=COMPLETED"
        ),
        actions=[
            Action(name="GetFigmaCommentsByArtifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_007"}),
            Action(name="UpdateFigmaCommentStatus", kwargs={"comment_id": "comment_006", "new_status": "IN_PROGRESS", "resolution_notes": "Accessibility improvements in progress - adding ARIA labels and keyboard navigation support", "assignee_email": "jake.design@company.com", "priority_level": "HIGH"}),
            Action(name="GetGmailThreadsByLabels", kwargs={"thread_id": "thread_004"}),
            Action(name="GetGmailThreadsByLabels", kwargs={"thread_id": "thread_005"}),
            Action(name="GetFigmaCommentsByArtifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="UpdateAssetExportStatus", kwargs={"asset_id": "asset_007", "new_status": "COMPLETED", "notes": "Admin header accessibility export completed with ARIA labels", "dlp_scan_status": "CLEAN"}),
            Action(name="AddTerminalLogEntry", kwargs={"log_message": "comment_resolution:comment_006:IN_PROGRESS:asset_007:COMPLETED", "log_level": "INFO", "component": "figma_comment_resolution", "user_email": "jake.design@company.com"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_97",
        instruction=(
            "As a release management coordinator, manage the complete release workflows and asset export status for design system components. You are tasked with handling release_003 status management and asset_003 export coordination, which requires detailed status tracking and integration within the release workflow management. The task involves cross-team coordination and effective release lifecycle management. The focus of the release coordination workflow is on achieving PUBLISHED status for release_003 with comprehensive release notes documentation, coordinating asset_003 export status to COMPLETE, ensuring a DLP scan verification, and assigning the release oversight to emma.creative@company.com. The management requires systematic status coordination and compliance verification. Your efforts should ensure comprehensive management of the release lifecycle, proper asset export coordination, and successful deployment tracking for stakeholder reporting and workflow completion. Required constants: release_id=release_003, new_status=PUBLISHED, release_notes=Design system components release with accessibility improvements, updated_by=emma.creative@company.com, asset_id=asset_003, export_status=COMPLETED, export_notes=Design system asset export completed with accessibility compliance, dlp_scan_status=CLEAN, owner_email=emma.creative@company.com, created_after=2024-08-20T15:00:00Z, log_message=Release management workflow completed - release_003 published with asset_003 export completion, log_level=INFO, component=release_management, user_email=emma.creative@company.com, audit_id=audit_001, thread_id=thread_001, thread_priority=HIGH, urgency_reason=Critical release deployment requires immediate stakeholder coordination, escalate_to=emma.creative@company.com,release.team@company.com"
        ),
        actions=[
            Action(name="UpdateReleaseStatus", kwargs={"release_id": "release_003", "new_status": "PUBLISHED", "release_notes": "Design system components release with accessibility improvements", "updated_by": "emma.creative@company.com"}),
            Action(name="UpdateAssetExportStatus", kwargs={"asset_id": "asset_003", "new_status": "COMPLETED", "notes": "Design system asset export completed with accessibility compliance", "dlp_scan_status": "CLEAN"}),
            Action(name="GetReleasesByOwner", kwargs={"owner_email": "emma.creative@company.com", "created_after": "2024-08-20T15:00:00Z"}),
            Action(name="AddTerminalLogEntry", kwargs={"log_message": "Release management workflow completed - release_003 published with asset_003 export completion", "log_level": "INFO", "component": "release_management", "user_email": "emma.creative@company.com"}),
            Action(name="GetAuditSummary", kwargs={"audit_id": "audit_001"}),
            Action(name="UpdateGmailThreadPriority", kwargs={"thread_id": "thread_001", "new_priority": "HIGH", "urgency_reason": "Critical release deployment requires immediate stakeholder coordination", "escalate_to": ["emma.creative@company.com", "release.team@company.com"]})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="user_98",
        instruction=(
            "As a specialist in Figma comment resolution, oversee the coordination of accessibility feedback and workflow management for admin panel header components. Your primary role involves managing accessibility feedback for art_008 admin panel header, identifying comments with resolved_status False and coordinating their resolution. The workflow also includes overseeing asset_007 admin header export integration by verifying status and aligning coordination. The improvement workflow concentrates on managing comment_006 accessibility enhancement involving oversight by team member jake.design@company.com, prioritizing HIGH level accessibility improvements, and tracking the implementation of ARIA labels and keyboard navigation support. Feedback resolution necessitates progress status coordination and thorough implementation documentation. Your coordination should provide seamless accessibility audit communication via thread_004, effective comment lifecycle management, and comprehensive compliance tracking for stakeholders, ensuring successful workflow completion. Use resolution_notes=Accessibility improvements in progress - adding ARIA labels and keyboard navigation support, notes=Admin header accessibility export completed with ARIA labels"
        ),
        actions=[
            Action(name="GetFigmaCommentsByArtifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_007"}),
            Action(name="UpdateFigmaCommentStatus", kwargs={"comment_id": "comment_006", "new_status": "IN_PROGRESS", "resolution_notes": "Accessibility improvements in progress - adding ARIA labels and keyboard navigation support", "assignee_email": "jake.design@company.com", "priority_level": "HIGH"}),
            Action(name="GetGmailThreadsByLabels", kwargs={"thread_id": "thread_004"}),
            Action(name="GetFigmaCommentsByArtifact", kwargs={"artifact_id": "art_008", "resolved_status": False}),
            Action(name="UpdateAssetExportStatus", kwargs={"asset_id": "asset_007", "new_status": "COMPLETED", "notes": "Admin header accessibility export completed with ARIA labels", "dlp_scan_status": "CLEAN"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_99",
        instruction=(
            "You function as an asset management expert entrusted with overseeing comprehensive asset management and fix item status workflows. Handle asset exports, system configuration, and fix item status coordination to meet design system standards. Prioritize managing asset exports, analyzing system configurations, auditing information, and updating fix item statuses with meticulous coordination. Engage with development teams via suitable channels to ensure seamless coordination of all asset management and fix item workflows. Furthermore, maintain detailed terminal logging throughout the asset management procedure to guarantee accurate tracking and an audit trail for workflow coordination. Required constants: asset_id=asset_005, category=design_system_aliases, audit_id=audit_006, thread_id=thread_006, owner_email=emma.creative@company.com, created_after=2024-08-21T14:00:00Z, log_level=INFO, component=asset_management, fix_item_id=item_003, new_status=APPLIED, updated_by=emma.creative@company.com, notes=Asset management coordination completed with design system compliance"
        ),
        actions=[
            Action(name="GetAssetExportSummary", kwargs={"asset_id": "asset_005"}),
            Action(name="GetSystemConfigByCategory", kwargs={"category": "design_system_aliases"}),
            Action(name="GetAuditSummary", kwargs={"audit_id": "audit_006"}),
            Action(name="GetGmailThreadsByLabels", kwargs={"thread_id": "thread_006"}),
            Action(name="GetReleasesByOwner", kwargs={"owner_email": "emma.creative@company.com", "created_after": "2024-08-21T14:00:00Z"}),
            Action(name="GetTerminalLogsSummary", kwargs={"log_level": "INFO", "component": "asset_management"}),
            Action(name="UpdateFixItemStatus", kwargs={"fix_item_id": "item_003", "new_status": "APPLIED", "updated_by": "emma.creative@company.com", "notes": "Asset management coordination completed with design system compliance"}),
            Action(name="AddTerminalLogEntry", kwargs={"log_message": "Asset management coordination completed with design system compliance", "log_level": "INFO", "component": "asset_management", "user_email": "emma.creative@company.com"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="user_100",
        instruction=(
            "You serve as an audit findings severity management expert tasked with handling audit finding severity updates along with integrated fix plan workflows. Your responsibility includes managing audit finding severity escalation and coordinating fix plan status while ensuring efficient priority management. Emphasize managing audit finding severity updates for CRITICAL violations, coordinating fix plan deliveries, and conducting comprehensive tracking of fix items. Collaborate with development teams via appropriate channels to ensure audit findings and fix workflows are effectively synchronized. Additionally, gather audit summaries to maintain thorough oversight and coordination throughout the severity management process. Required constants: finding_id=finding_a11y_001, new_severity=CRITICAL, updated_by=chris.engineer@company.com, plan_id=plan_001, delivery_method=TICKETS, owner_email=chris.engineer@company.com, item_id=item_001, fix_item_id=item_001, new_priority=HIGH, priority_reason=Critical audit finding requires immediate fix attention, audit_id=audit_002, violation_type=TOUCH_TARGET, severity=CRITICAL, log_message=Audit findings severity management and fix plan coordination completed"
        ),
        actions=[
            Action(name="UpdateAuditFindingSeverity", kwargs={"finding_id": "finding_a11y_001", "new_severity": "CRITICAL", "updated_by": "chris.engineer@company.com"}),
            Action(name="GetAuditFindingsByType", kwargs={"violation_type": "TOUCH_TARGET", "severity": "CRITICAL"}),
            Action(name="GetFixPlanItems", kwargs={"plan_id": "plan_001"}),
            Action(name="UpdateFixPlanStatus", kwargs={"plan_id": "plan_001", "new_status": "IN_PROGRESS", "delivery_method": "TICKETS", "owner_email": "chris.engineer@company.com"}),
            Action(name="UpdateFixItemPriority", kwargs={"item_id": "item_001", "new_priority": "HIGH", "priority_reason": "Critical audit finding requires immediate fix attention", "updated_by": "chris.engineer@company.com"}),
            Action(name="UpdateFixItemStatus", kwargs={"fix_item_id": "item_001", "new_status": "IN_PROGRESS", "updated_by": "chris.engineer@company.com"}),
            Action(name="AddTerminalLogEntry", kwargs={"log_message": "Audit findings severity management and fix plan coordination completed", "log_level": "INFO", "component": "audit_severity", "user_email": "chris.engineer@company.com"}),
            Action(name="GetAuditSummary", kwargs={"audit_id": "audit_002"})
        ],
        outputs=[]
    ),
]
