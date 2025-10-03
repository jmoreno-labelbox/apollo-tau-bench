from domains.dto import Action, Task

TASKS = [
    Task(
        annotator="0",
        user_id="compliance_auditor_review",
        instruction="As a compliance auditor, your task is to examine change management processes for the Mobile App Launch project. Locate all change requests in proj_mobile_01 (ensure include impact is true), then ensure compliance for change request cr_001 by verifying: has_business_justification, has_impact_assessment,"
                    " proper_approval_sequence, baseline_exists, and critical_path_risk_assessed. Also, check for conflicts"
                    " with cr_003, if there is any conflicts, save them for both change requests. Finally, determine the"
                    " total budget impact and if rule violations were found.",
        actions=[
            Action(
                name="SearchChangeRequests",
                kwargs={"project_id": "proj_mobile_01", "include_impact": True},
            ),
            Action(
                name="ValidateChangeCompliance",
                kwargs={
                    "cr_id": "cr_001",
                    "compliance_checklist": [
                        "has_business_justification",
                        "has_impact_assessment",
                        "proper_approval_sequence",
                        "baseline_exists",
                        "critical_path_risk_assessed",
                    ],
                },
            ),
            Action(name="CheckChangeConflicts", kwargs={"cr_id": "cr_001", "compare_to_cr_id": "cr_003"}),
            Action(
                name="SaveChangeRequestsConflicts",
                kwargs={
                    "cr_id": "cr_001",
                    "conflicting_cr_id": "cr_003",
                    "type": "deliverable_conflict",
                    "conflicting_deliverables": ["del_001"],
                    "severity": "critical",
                    "rule_violation": "Multiple change requests affecting the same deliverable must be consolidated",
                    "action_required": "Merge with existing CR or wait for completion",
                    "recommendation": "Cannot proceed - consolidate with conflicting CRs"
                }
            ),
            Action(
                name="SaveChangeRequestsConflicts",
                kwargs={
                    "cr_id": "cr_003",
                    "conflicting_cr_id": "cr_001",
                    "type": "deliverable_conflict",
                    "conflicting_deliverables": ["del_001"],
                    "severity": "critical",
                    "rule_violation": "Multiple change requests affecting the same deliverable must be consolidated",
                    "action_required": "Merge with existing CR or wait for completion",
                    "recommendation": "Cannot proceed - consolidate with conflicting CRs"
                }
            ),
            Action(
                name="CalculateCumulativeImpact",
                kwargs={"project_id": "proj_mobile_01", "include_pending": True},
            ),
        ],
        outputs=['"total_budget_impact": 110000', '"has_rule_violations": True'],
    ),
    Task(
        annotator="0",
        user_id="project_manager_baseline_review",
        instruction="You are a project manager reviewing the AI Platform project status. First, compare the current project scope against the baseline for proj_ai_01. Then schedule a quarterly change review meeting for March 25, 2024 at 14:00:00Z with participants Daniel Li (sh_003) and Amanda Johnson (emp_pm_04), scheduled by yourself (emp_pm_04). Link change request cr_002 to milestone ms_003 with impact type schedule. Search for change requests for proj_ai_01 with status in_review without including impact details. Validate change compliance for cr_002, checking for has_business_justification and baseline_exists. Finally, report the variance percentage from baseline and whether a rebaseline is recommended.",
        actions=[
            Action(
                name="CompareAgainstBaseline", kwargs={"project_id": "proj_ai_01"}
            ),
            Action(
                name="ScheduleChangeReview",
                kwargs={
                    "project_id": "proj_ai_01",
                    "review_date": "2024-03-25T14:00:00Z",
                    "review_type": "quarterly",
                    "participants": ["sh_003", "emp_pm_04"],
                    "scheduled_by": "emp_pm_04",
                },
            ),
            Action(
                name="LinkChangeToMilestone",
                kwargs={
                    "cr_id": "cr_002",
                    "milestone_id": "ms_003",
                    "impact_type": "schedule",
                },
            ),
            Action(
                name="SearchChangeRequests",
                kwargs={
                    "project_id": "proj_ai_01",
                    "status": "in_review",
                    "include_impact": False,
                },
            ),
            Action(
                name="ValidateChangeCompliance",
                kwargs={
                    "cr_id": "cr_002",
                    "compliance_checklist": [
                        "has_business_justification",
                        "baseline_exists",
                    ],
                },
            ),
        ],
        outputs=[
            '"variance_percentage": 0.0',
            '"recommendation": "Within acceptable variance"',
        ],
    ),
    Task(
        annotator="0",
        user_id="process_improvement_lead",
        instruction="""
        You are the process improvement lead standardizing change procedures. Create a new change template called
        'Security Enhancement Standard' as template type 'standard_enhancement' with standard fields for change_type
        'requirement_change' and priority 'high', typical duration of 6 weeks, typical resources of 3, requiring
        approvals from project_manager and security_lead, with medium risk threshold, created by yourself (sh_005).
        Then bulk update the status of the change request cr_002 from its current status to cancelled by
        Daniel Li (sh_003). Archive changes for project proj_mobile_01 before date 2024-03-01T00:00:00Z,
        archived by yourself (sh_005). Finally, generate a summary change report for project proj_mobile_01 without
        including details, and report the number of updated and pending artifacts.
        """,
        actions=[
            Action(
                name="CreateChangeTemplate",
                kwargs={
                    "template_name": "Security Enhancement Standard",
                    "template_type": "standard_enhancement",
                    "standard_fields": {
                        "change_type": "requirement_change",
                        "priority": "high",
                        "typical_duration_weeks": 6,
                        "typical_resources": 3,
                    },
                    "required_approvals": ["project_manager", "security_lead"],
                    "risk_threshold": "medium",
                    "created_by": "sh_005",
                },
            ),
            Action(
                name="BulkUpdateChangeStatus",
                kwargs={
                    "cr_ids": ["cr_002"],
                    "new_status": "cancelled",
                    "updated_by": "sh_003",
                },
            ),
            Action(
                name="ArchiveChanges",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "archive_before_date": "2024-03-01T00:00:00Z",
                    "archived_by": "sh_005",
                },
            ),
            Action(
                name="GenerateChangeReport",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "report_type": "summary",
                    "include_details": False,
                },
            ),
        ],
        outputs=['"artifacts_updated": 2','"artifacts_pending": 3 '],
    ),
    Task(
        annotator="0",
        user_id="baseline_manager_approval",
        instruction="""
        You are the baseline manager establishing a new scope baseline for the AI Platform project. Create a scope
        baseline (use bl_d90b8c50 for baseline ID) for proj_ai_01 named 'AI Platform Q2 2024 Baseline' with scope items for 'Advanced ML algorithms'
        (item_id: scope_011, category: feature) and 'Real-time inference engine' (item_id: scope_012, category: feature),
        deliverables including 'Model optimization framework' (deliverable_id: del_006, description: 'Framework for
        optimizing ML model performance') with 480 estimated hours and 'Inference API' (deliverable_id: del_007,
        description: 'High-performance inference API') with 320 estimated hours, acceptance criteria for 99% uptime
        (availability) and sub-100ms response time (latency), and success metrics for 95% model accuracy and 10000
        requests/second throughput, created by Daniel Mitchell (emp_arch_01). After creating the baseline, use the
        returned baseline_id to approve this baseline with approval by Daniel Li (sh_003) with notes 'Q2 baseline
        approved for AI platform expansion'. Generate an audit trail for change request cr_002 excluding approvals and
        artifacts. Compare against baseline version 1.1 for project proj_ai_01. Report the baseline version and
        total estimated effort hours.""",
        actions=[
            Action(
                name="CreateScopeBaseline",
                kwargs={
                    "project_id": "proj_ai_01",
                    "baseline_id": "bl_d90b8c50",
                    "baseline_name": "AI Platform Q2 2024 Baseline",
                    "scope_items": [
                        {
                            "item_id": "scope_011",
                            "description": "Advanced ML algorithms",
                            "category": "feature",
                        },
                        {
                            "item_id": "scope_012",
                            "description": "Real-time inference engine",
                            "category": "feature",
                        },
                    ],
                    "deliverables": [
                        {
                            "deliverable_id": "del_006",
                            "name": "Model optimization framework",
                            "description": "Framework for optimizing ML model performance",
                            "estimated_hours": 480,
                        },
                        {
                            "deliverable_id": "del_007",
                            "name": "Inference API",
                            "description": "High-performance inference API",
                            "estimated_hours": 320,
                        },
                    ],
                    "acceptance_criteria": {
                        "availability": "99% uptime",
                        "latency": "Sub-100ms response time",
                    },
                    "success_metrics": {
                        "accuracy": "95% model accuracy",
                        "throughput": "10000 requests/second",
                    },
                    "created_by": "emp_arch_01",
                },
            ),
            Action(
                name="ApproveBaselineUpdate",
                kwargs={
                    "baseline_id": "bl_d90b8c50",
                    "approved_by": "sh_003",
                    "approval_notes": "Q2 baseline approved for AI platform expansion",
                },
            ),
            Action(
                name="GenerateAuditTrail",
                kwargs={
                    "cr_id": "cr_002",
                    "include_approvals": False,
                    "include_artifacts": False,
                },
            ),
            Action(
                name="CompareAgainstBaseline",
                kwargs={"project_id": "proj_ai_01", "baseline_version": "1.1"},
            ),
        ],
        outputs=['"version": "1.1"', '"estimated_effort_hours": 800'],
    ),
    Task(
        annotator="0",
        user_id="change_compliance_auditor",
        instruction="You are reviewing change management compliance for project proj_mobile_01. First, search for all change requests for this project with status 'pending_approval' (set include impact as true). Then check for conflicts with cr_003. Validate compliance for cr_001 using these specific checks: baseline_exists, has_business_justification, and has_impact_assessment. Calculate the cumulative impact for the project including pending changes. Link cr_003 to ms_002 with schedule impact type. Generate a compliance report for the project. From your findings, report: 1) The total number of change requests for the project (from the compliance report), and 2) The total cumulative budget impact (from the cumulative impact calculation).",
        actions=[
            Action(
                name="SearchChangeRequests",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "status": "pending_approval",
                    "include_impact": True,
                },
            ),
            Action(name="CheckChangeConflicts", kwargs={"cr_id": "cr_003"}),
            Action(
                name="ValidateChangeCompliance",
                kwargs={
                    "cr_id": "cr_001",
                    "compliance_checklist": [
                        "baseline_exists",
                        "has_business_justification",
                        "has_impact_assessment",
                    ],
                },
            ),
            Action(
                name="CalculateCumulativeImpact",
                kwargs={"project_id": "proj_mobile_01", "include_pending": True},
            ),
            Action(
                name="LinkChangeToMilestone",
                kwargs={
                    "cr_id": "cr_003",
                    "milestone_id": "ms_002",
                    "impact_type": "schedule",
                },
            ),
            Action(
                name="GenerateChangeReport",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "report_type": "compliance",
                },
            ),
        ],
        outputs=['"total_change_requests": 2', '"total_budget_impact": 110000'],
    ),
    Task(
        annotator="0",
        user_id="change_control_coordinator",
        instruction="You are a change control board coordinator preparing for quarterly reviews. Search for all change requests in project proj_ai_01 regardless of status (set include impact as true). Validate compliance for cr_002 checking for has_business_justification, has_impact_assessment, and baseline_exists. Check if cr_002 has any conflicts. Schedule a change review for proj_ai_01 on 2024-03-28T10:00:00Z as a quarterly review with participants emp_pm_04 and sh_003, scheduled by sh_003. Calculate cumulative impact for proj_ai_01 excluding pending changes. Generate a summary change report for the project. From your findings, report: 1) The total number of change requests found for the project (from the summary report), and 2) The timeline impact in weeks from the cumulative impact calculation.",
        actions=[
            Action(
                name="SearchChangeRequests",
                kwargs={"project_id": "proj_ai_01", "include_impact": True},
            ),
            Action(
                name="ValidateChangeCompliance",
                kwargs={
                    "cr_id": "cr_002",
                    "compliance_checklist": [
                        "has_business_justification",
                        "has_impact_assessment",
                        "baseline_exists",
                    ],
                },
            ),
            Action(name="CheckChangeConflicts", kwargs={"cr_id": "cr_002"}),
            Action(
                name="ScheduleChangeReview",
                kwargs={
                    "project_id": "proj_ai_01",
                    "review_date": "2024-03-28T10:00:00Z",
                    "review_type": "quarterly",
                    "participants": ["emp_pm_04", "sh_003"],
                    "scheduled_by": "sh_003",
                },
            ),
            Action(
                name="CalculateCumulativeImpact",
                kwargs={"project_id": "proj_ai_01", "include_pending": False},
            ),
            Action(
                name="GenerateChangeReport",
                kwargs={
                    "project_id": "proj_ai_01",
                    "report_type": "summary",
                    "include_details": False,
                },
            ),
        ],
        outputs=['"total_change_requests": 1', '"timeline_impact_weeks": 0'],
    ),
    Task(
        annotator="0",
        user_id="risk_compliance_officer",
        instruction="You are a risk compliance officer reviewing change requests. Search for all change requests in proj_mobile_01 (set include impact as true). Check conflicts for cr_003. If cr_003 has any conflicts or affects the critical path (check the impact assessment from search results), create a risk assessment. As the risk manager (sh_005), assess the risks for cr_003 using these specific assessments: technical risk as medium, schedule risk as medium, resource risk as medium, quality risk as low, and stakeholder risk as low. For a multi-language support change, identify these specific risks: 'Multi-language UI complexity', 'Translation quality concerns', and 'Extended testing requirements'. Include these mitigation strategies: 'Professional translation services', 'Phased language rollout', and 'Native speaker review process'. For contingency planning, set quality_issues plan as 'Delay individual language releases' and the rollback procedure as 'Disable specific language if issues found'. Link cr_003 to ms_001 with schedule impact. From the risk assessment results, report the overall risk level and from the conflict check results, report whether it has rule violations.",
        actions=[
            Action(
                name="SearchChangeRequests",
                kwargs={"project_id": "proj_mobile_01", "include_impact": True},
            ),
            Action(name="CheckChangeConflicts", kwargs={"cr_id": "cr_003"}),
            Action(
                name="CreateRiskAssessment",
                kwargs={
                    "cr_id": "cr_003",
                    "assessed_by": "sh_005",
                    "risk_categories": {
                        "technical": "medium",
                        "schedule": "medium",
                        "resource": "medium",
                        "quality": "low",
                        "stakeholder": "low",
                    },
                    "identified_risks": [
                        "Multi-language UI complexity",
                        "Translation quality concerns",
                        "Extended testing requirements",
                    ],
                    "mitigation_strategies": [
                        "Professional translation services",
                        "Phased language rollout",
                        "Native speaker review process",
                    ],
                    "contingency_plans": {
                        "quality_issues": "Delay individual language releases"
                    },
                    "rollback_procedure": "Disable specific language if issues found",
                },
            ),
            Action(
                name="LinkChangeToMilestone",
                kwargs={
                    "cr_id": "cr_003",
                    "milestone_id": "ms_001",
                    "impact_type": "schedule",
                },
            ),
        ],
        outputs=['"overall_risk_level": "medium"', '"has_rule_violations": true'],
    ),
    Task(
        annotator="0",
        user_id="workflow_automation_specialist",
        instruction="""
        You are automating approval workflows for pending changes. Search for change requests in proj_ai_01 with status
        'in_review', set change impact as false in the search. If you find cr_002 in the results, first, make sure a
        workflow exists for cr_002. Then record an
        approval decision for cr_002 with approver_id sh_002, decision 'approve', and include the comment 'Scope
        reduction aligns with timeline constraints'. Also, update the change request status to 'approved' for cr_002 performed by
        sh_002. After the approval is recorded, track artifact updates for cr_002
        for the 'project_schedule' artifact type, using description 'Removed advanced analytics from Phase 2 timeline',
        version_before '1.5', version_after '1.6', updated_by 'emp_pm_04', and update ID 'up_c4838f8f'. Report
        the update ID if no errors was generated in the workflow.""",
        actions=[
            Action(
                name="SearchChangeRequests",
                kwargs={
                    "project_id": "proj_ai_01",
                    "status": "in_review",
                    "include_impact": False,
                },
            ),
            Action(
                name="CheckWorkflowExistsForChangeRequest",
                kwargs={"cr_id": "cr_002"},
            ),
            Action(
                name="RecordApprovalDecision",
                kwargs={
                    "cr_id": "cr_002",
                    "approver_id": "sh_002",
                    "decision": "approve",
                    "comments": "Scope reduction aligns with timeline constraints",
                    "conditions": [],
                },
            ),
            Action(
                name="UpdateChangeRequestStatus",
                kwargs={
                    "cr_id": "cr_002",
                    "performed_by": "sh_002",
                    "new_status": "approved",
                },
            ),
            Action(
                name="TrackArtifactUpdates",
                kwargs={
                    "update_id": "up_c4838f8f",
                    "cr_id": "cr_002",
                    "artifact_type": "project_schedule",
                    "update_description": "Removed advanced analytics from Phase 2 timeline",
                    "version_before": "1.5",
                    "version_after": "1.6",
                    "updated_by": "emp_pm_04",
                },
            ),
        ],
        outputs=['"update_id": "up_c4838f8f"'],
    ),
    Task(
        annotator="0",
        user_id="technical_assessment_coordinator",
        instruction="You are coordinating technical assessments for pending changes. Search for change requests in proj_ai_01 that have status 'in_review' (set include impact as false). For any found, if cr_002 is among them, perform an impact assessment for it with the following parameters: assessed_by should be emp_data_01, timeline_impact_weeks should be -3 (negative because this is a scope reduction), budget_impact should be -75000 (cost savings from reduced scope), resource_requirements should be an empty array, and technical_dependencies should be an empty array. After the assessment, check for any conflicts with cr_002. Calculate the cumulative impact for proj_ai_01 including all pending changes. Generate a detailed change report for the project including all details. From your results, report: 1) The budget_impact_percentage from cr_002's impact assessment, and 2) The number of conflicts_found from the conflict check.",
        actions=[
            Action(
                name="SearchChangeRequests",
                kwargs={
                    "project_id": "proj_ai_01",
                    "status": "in_review",
                    "include_impact": False,
                },
            ),
            Action(
                name="PerformImpactAssessment",
                kwargs={
                    "cr_id": "cr_002",
                    "assessed_by": "emp_data_01",
                    "timeline_impact_weeks": -3,
                    "budget_impact": -75000,
                    "resource_requirements": [],
                    "technical_dependencies": [],
                },
            ),
            Action(name="CheckChangeConflicts", kwargs={"cr_id": "cr_002"}),
            Action(
                name="CalculateCumulativeImpact",
                kwargs={"project_id": "proj_ai_01", "include_pending": True},
            ),
            Action(
                name="GenerateChangeReport",
                kwargs={
                    "project_id": "proj_ai_01",
                    "report_type": "detailed",
                    "include_details": True,
                },
            ),
        ],
        outputs=['"budget_impact_percentage": -2.3', '"conflicts_found": 0'],
    ),
    Task(
        annotator="0",
        user_id="approval_process_administrator",
        instruction="""
        You are administering approval processes for in-progress changes. Search for all change requests (set include impact as false) in
        proj_mobile_01. For cr_001, attempt to create an expedited approval workflow. Generate an audit trail for cr_001
        including approvals and artifacts. Record an approval decision for cr_003 by approver sh_003 with decision
        'approve', comments 'Resources available for multi-language support', and no conditions. Finally, generate
        a compliance report (set include details as false) for proj_mobile_01. Report: 1) The total number of change requests for the project
        (from the compliance report), and 2) The number of overdue implementations (from the compliance report).
        """,
        actions=[
            Action(
                name="SearchChangeRequests",
                kwargs={"project_id": "proj_mobile_01", "include_impact": False},
            ),
            Action(
                name="CreateApprovalWorkflow",
                kwargs={"cr_id": "cr_001", "workflow_type": "expedited"},
            ),
            Action(
                name="GenerateAuditTrail",
                kwargs={
                    "cr_id": "cr_001",
                    "include_approvals": True,
                    "include_artifacts": True,
                },
            ),
            Action(
                name="RecordApprovalDecision",
                kwargs={
                    "cr_id": "cr_003",
                    "approver_id": "sh_003",
                    "decision": "approve",
                    "comments": "Resources available for multi-language support",
                    "conditions": [],
                },
            ),
            Action(
                name="GenerateChangeReport",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "report_type": "compliance",
                    "include_details": False,
                },
            ),
        ],
        outputs=['"total_change_requests": 2', '"overdue_implementations": 1'],
    ),
    Task(
        annotator="0",
        user_id="project_approval_manager",
        instruction="""
        You are managing project approvals. Search for change requests in proj_ai_01 with status in_review (set include impact as false). If you find
        cr_002, validate its compliance checking for baseline_exists and has_business_justification. If cr_002 is found
        and compliant, record an approval decision for cr_002 by sh_002 with decision 'approve', comment 'Descoping
        analytics aligns with delivery timeline', and no conditions. Then update cr_002 status to approved performed by
        sh_002. Calculate cumulative impact for proj_ai_01 including pending changes. Generate a summary change report
        for the project. From the cumulative impact calculation, report the total_budget_impact value. From the summary
        report's approval_metrics, report the approval_rate value.
        """,
        actions=[
            Action(
                name="SearchChangeRequests",
                kwargs={
                    "project_id": "proj_ai_01",
                    "status": "in_review",
                    "include_impact": False,
                },
            ),
            Action(
                name="ValidateChangeCompliance",
                kwargs={
                    "cr_id": "cr_002",
                    "compliance_checklist": [
                        "baseline_exists",
                        "has_business_justification",
                    ],
                },
            ),
            Action(
                name="RecordApprovalDecision",
                kwargs={
                    "cr_id": "cr_002",
                    "approver_id": "sh_002",
                    "decision": "approve",
                    "comments": "Descoping analytics aligns with delivery timeline",
                    "conditions": [],
                },
            ),
            Action(
                name="UpdateChangeRequestStatus",
                kwargs={
                    "cr_id": "cr_002",
                    "new_status": "approved",
                    "performed_by": "sh_002",
                },
            ),
            Action(
                name="CalculateCumulativeImpact",
                kwargs={"project_id": "proj_ai_01", "include_pending": True},
            ),
            Action(
                name="GenerateChangeReport",
                kwargs={
                    "project_id": "proj_ai_01",
                    "report_type": "summary",
                    "include_details": False,
                },
            ),
        ],
        outputs=['"total_budget_impact": 0', '"approval_rate": 100'],
    ),
    Task(
        annotator="0",
        user_id="change_process_validator",
        instruction="""
        You are a change process validator examining project proj_mobile_01. Search for all change requests with status
        pending_approval in this project (set include impact as true). Check if cr_003 has any conflicts with other
        changes. Validate the compliance
        of cr_003 specifically checking for has_business_justification, has_impact_assessment, baseline_exists, and
        no_deliverable_conflicts. Link change request cr_003 to milestone ms_001 with impact type schedule. Calculate
        the cumulative impact for proj_mobile_01 including pending changes. From your findings, report: 1) The number
        of conflicts found for cr_003 (from the conflict check),
        and 2) The total budget impact (from the cumulative impact calculation).
        """,
        actions=[
            Action(
                name="SearchChangeRequests",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "status": "pending_approval",
                    "include_impact": True,
                },
            ),
            Action(name="CheckChangeConflicts", kwargs={"cr_id": "cr_003"}),
            Action(
                name="ValidateChangeCompliance",
                kwargs={
                    "cr_id": "cr_003",
                    "compliance_checklist": [
                        "has_business_justification",
                        "has_impact_assessment",
                        "baseline_exists",
                        "no_deliverable_conflicts",
                    ],
                },
            ),
            Action(
                name="LinkChangeToMilestone",
                kwargs={
                    "cr_id": "cr_003",
                    "milestone_id": "ms_001",
                    "impact_type": "schedule",
                },
            ),
            Action(
                name="CalculateCumulativeImpact",
                kwargs={"project_id": "proj_mobile_01", "include_pending": True},
            ),
        ],
        outputs=['"conflicts_found": 1', '"total_budget_impact": 110000'],
    ),
    Task(
        annotator="0",
        user_id="pmo_approval_authority",
        instruction="""
        You are a PMO director (sh_003) responsible for approving changes. Search for change requests in proj_mobile_01
        that have status pending_approval (set include impact as true). For cr_003, validate its compliance using these specific checks: baseline_exists,
        has_business_justification, has_impact_assessment, and proper_approval_sequence. If the compliance status is compliant,
        record your approval decision for cr_003 with the decision to 'approve' and the comment 'Multi-language support aligns with market
        expansion strategy'. After recording approval, update the change request status to 'approved'.
        Report the final status of cr_003 after your updates.
        """,
        actions=[
            Action(
                name="SearchChangeRequests",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "status": "pending_approval",
                    "include_impact": True,
                },
            ),
            Action(
                name="ValidateChangeCompliance",
                kwargs={
                    "cr_id": "cr_003",
                    "compliance_checklist": [
                        "baseline_exists",
                        "has_business_justification",
                        "has_impact_assessment",
                        "proper_approval_sequence",
                    ],
                },
            ),
            Action(
                name="RecordApprovalDecision",
                kwargs={
                    "cr_id": "cr_003",
                    "approver_id": "sh_003",
                    "decision": "approve",
                    "comments": "Multi-language support aligns with market expansion strategy",
                    "conditions": [],
                },
            ),
            Action(
                name="UpdateChangeRequestStatus",
                kwargs={
                    "cr_id": "cr_003",
                    "new_status": "approved",
                    "performed_by": "sh_003",
                },
            ),
        ],
        outputs=['"status": "approved"'],
    ),
    Task(
        annotator="0",
        user_id="change_pipeline_analyst",
        instruction="""
        You are analyzing the change pipeline for project proj_ai_01. First search for all change requests in proj_ai_01
        regardless of status (set include impact as true). Then search specifically for change requests with status in_review (set include impact as false). For cr_002, perform an
        impact assessment as emp_data_01 with timeline impact of -3 weeks (negative because it's a scope reduction),
        budget impact of -75000, no resource requirements, and no technical dependencies. Validate compliance for cr_002
        checking has_business_justification and has_impact_assessment. Create a standard approval workflow for cr_002.
        Calculate the cumulative impact for proj_ai_01 excluding pending changes. Generate a compliance report.
        Report: 1) the total number of change requests found in your initial search (all statuses), and
        2) the timeline_impact_weeks from the cumulative impact calculation.
        """,
        actions=[
            Action(
                name="SearchChangeRequests",
                kwargs={"project_id": "proj_ai_01", "include_impact": True},
            ),
            Action(
                name="SearchChangeRequests",
                kwargs={
                    "project_id": "proj_ai_01",
                    "status": "in_review",
                    "include_impact": False,
                },
            ),
            Action(
                name="PerformImpactAssessment",
                kwargs={
                    "cr_id": "cr_002",
                    "assessed_by": "emp_data_01",
                    "timeline_impact_weeks": -3,
                    "budget_impact": -75000,
                    "resource_requirements": [],
                    "technical_dependencies": [],
                },
            ),
            Action(
                name="ValidateChangeCompliance",
                kwargs={
                    "cr_id": "cr_002",
                    "compliance_checklist": [
                        "has_business_justification",
                        "has_impact_assessment",
                    ],
                },
            ),
            Action(
                name="CreateApprovalWorkflow",
                kwargs={"cr_id": "cr_002", "workflow_type": "standard"},
            ),
            Action(
                name="CalculateCumulativeImpact",
                kwargs={"project_id": "proj_ai_01", "include_pending": False},
            ),
            Action(
                name="GenerateChangeReport",
                kwargs={
                    "project_id": "proj_ai_01",
                    "report_type": "compliance",
                    "include_details": False,
                },
            ),
        ],
        outputs=['"total_change_requests": 1', '"timeline_impact_weeks": 0'],
    ),
    Task(
        annotator="0",
        user_id="implementation_tracking_coordinator",
        instruction="You are tracking implementation progress for approved changes. Search for all change requests in proj_mobile_01 with status approved (set 'include_impact' as true). For the first approved change request found, validate compliance checking artifacts_updated. If cr_001 is approved, track artifact updates for it: First update the budget artifact with description 'Updated budget to reflect biometric authentication requirements' from version 1.2 to version 1.3 by emp_pm_03. Then track another update for the resource_plan artifact with description 'Updated resource allocation for authentication module' from version 1.3 to version 1.4 by emp_pm_03. Calculate cumulative impact for proj_mobile_01 excluding pending changes. Generate a detailed change report. From the artifact update responses, report how many artifacts are still pending updates after your updates, and from the cumulative impact calculation, report the total budget impact.",
        actions=[
            Action(
                name="SearchChangeRequests",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "status": "approved",
                    "include_impact": True,
                },
            ),
            Action(
                name="ValidateChangeCompliance",
                kwargs={
                    "cr_id": "cr_001",
                    "compliance_checklist": ["artifacts_updated"],
                },
            ),
            Action(
                name="TrackArtifactUpdates",
                kwargs={
                    "cr_id": "cr_001",
                    "artifact_type": "budget",
                    "update_description": "Updated budget to reflect biometric authentication requirements",
                    "version_before": "1.2",
                    "version_after": "1.3",
                    "updated_by": "emp_pm_03",
                },
            ),
            Action(
                name="TrackArtifactUpdates",
                kwargs={
                    "cr_id": "cr_001",
                    "artifact_type": "resource_plan",
                    "update_description": "Updated resource allocation for authentication module",
                    "version_before": "1.3",
                    "version_after": "1.4",
                    "updated_by": "emp_pm_03",
                },
            ),
            Action(
                name="CalculateCumulativeImpact",
                kwargs={"project_id": "proj_mobile_01", "include_pending": False},
            ),
            Action(
                name="GenerateChangeReport",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "report_type": "detailed",
                    "include_details": True,
                },
            ),
        ],
        outputs=[
            '"remaining_artifacts": ["scope_statement"]',
            '"total_budget_impact": 45000',
        ],
    ),
    Task(
        annotator="0",
        user_id="baseline_administrator",
        instruction="""
        You are establishing a new baseline for project proj_ai_01 after scope changes. First, search for change
        requests in this project with status 'in_review' (set 'include_impact' as false). Then compare the current
        project against baseline version 1.0.
        Create a new scope baseline (use bl_b9f5c8a2 for baseline ID and emp_pm_04 for 'created_by')
        for the project with the name 'AI Platform Reduced
        Scope Q2 2024', including the scope items and deliverables specified in the parameters. For the acceptance
        criteria used in the scope baseline, include the following exact values: accuracy must be "95% model accuracy",
        and latency must be "Sub-150ms response time". For the success metrics, include ('accuracy' = '90% model accuracy',
        'throughput': '500 requests/second'). After creating the baseline, you'll need to approve it. Use
        the baseline_id from the creation response to approve the baseline as sh_003 with approval notes 'Approved after
        scope reduction per CR-002'. Finally, generate a compliance report for the project (don't include details).
        The scope items and deliverables to be included in the new baseline are as follows. Scope items:
        (1) scope_101 - Core ML algorithms (category: feature), and (2) scope_102 - Basic inference API (category: feature).
        Deliverables: (1) del_101 - ML Training Pipeline: Simplified ML training pipeline, estimated at 480 hours; and
        (2) del_102 - Inference API: Basic inference API without analytics, estimated at 240 hours.
        Use these exact values when creating the scope baseline. From the baseline creation
        response, report: 1) The version of the baseline created, and 2) The total estimated effort hours from the metrics.
        """,
        actions=[
            Action(
                name="SearchChangeRequests",
                kwargs={
                    "project_id": "proj_ai_01",
                    "status": "in_review",
                    "include_impact": False,
                },
            ),
            Action(
                name="CompareAgainstBaseline",
                kwargs={"project_id": "proj_ai_01", "baseline_version": "1.0"},
            ),
            Action(
                name="CreateScopeBaseline",
                kwargs={
                    "baseline_id": "bl_b9f5c8a2",
                    "project_id": "proj_ai_01",
                    "baseline_name": "AI Platform Reduced Scope Q2 2024",
                    "scope_items": [
                        {
                            "item_id": "scope_101",
                            "description": "Core ML algorithms",
                            "category": "feature",
                        },
                        {
                            "item_id": "scope_102",
                            "description": "Basic inference API",
                            "category": "feature",
                        },
                    ],
                    "deliverables": [
                        {
                            "deliverable_id": "del_101",
                            "name": "ML Training Pipeline",
                            "description": "Simplified ML training pipeline",
                            "estimated_hours": 480,
                        },
                        {
                            "deliverable_id": "del_102",
                            "name": "Inference API",
                            "description": "Basic inference API without analytics",
                            "estimated_hours": 240,
                        },
                    ],
                    "acceptance_criteria": {
                        "accuracy": "95% model accuracy",
                        "latency": "Sub-150ms response time",
                    },
                    "success_metrics": {
                        "accuracy": "90% model accuracy",
                        "throughput": "500 requests/second",
                    },
                    "created_by": "emp_pm_04",
                },
            ),
            Action(
                name="ApproveBaselineUpdate",
                kwargs={
                    "baseline_id": "bl_b9f5c8a2",
                    "approved_by": "sh_003",
                    "approval_notes": "Approved after scope reduction per CR-002",
                },
            ),
            Action(
                name="GenerateChangeReport",
                kwargs={
                    "project_id": "proj_ai_01",
                    "report_type": "compliance",
                    "include_details": False,
                },
            ),
        ],
        outputs=['"version": "1.1"', '"estimated_effort_hours": 720'],
    ),
    Task(
        annotator="0",
        user_id="baseline_variance_analyst",
        instruction="""
        You are analyzing baseline variance for project proj_mobile_01. Search for all approved change requests in
        this project (set include impact as true). Compare the current project state against baseline version 1.0. Check for conflicts with cr_001.
        Calculate the cumulative impact including pending changes. If the variance percentage from the baseline
        is above 30%, schedule
        a change review for 2024-03-30T14:00:00Z with participants sh_002, sh_003, and emp_pm_03, scheduled by sh_003.
        The review type should be quarterly. From the baseline comparison
        results, report the variance percentage.
        """,
        actions=[
            Action(
                name="SearchChangeRequests",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "status": "approved",
                    "include_impact": True,
                },
            ),
            Action(
                name="CompareAgainstBaseline",
                kwargs={"project_id": "proj_mobile_01", "baseline_version": "1.0"},
            ),
            Action(name="CheckChangeConflicts", kwargs={"cr_id": "cr_001"}),
            Action(
                name="CalculateCumulativeImpact",
                kwargs={"project_id": "proj_mobile_01", "include_pending": True},
            ),
            Action(
                name="ScheduleChangeReview",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "review_date": "2024-03-30T14:00:00Z",
                    "review_type": "quarterly",
                    "participants": ["sh_002", "sh_003", "emp_pm_03"],
                    "scheduled_by": "sh_003",
                },
            ),
        ],
        outputs=[
            '"variance_percentage": 33.3',
        ],
    ),
    Task(
        annotator="0",
        user_id="emergency_review_coordinator",
        instruction="You are coordinating emergency reviews for critical changes. Search for all change requests in proj_mobile_01 (set include impact as true). Check if cr_003 has any conflicts. Validate compliance for cr_003 checking specifically for critical_path_risk_assessed. If there are rule violations, create a risk assessment for cr_003 with assessed_by sh_005, using these risk levels: technical risk high, schedule risk high, resource risk medium, quality risk low, and stakeholder risk medium. Include these identified risks: 'Integration complexity with multiple languages', 'Testing resource constraints', and 'Deployment synchronization challenges'. Add these mitigation strategies: 'Phased language rollout', 'Automated testing framework', and 'Feature flags for controlled release'. For contingency plans, include: integration_failure plan as 'Rollback to single language' and resource_shortage plan as 'Prioritize core languages first'. Set the rollback_procedure as 'Disable language features via configuration'. After the risk assessment (if needed), schedule an adhoc change review for proj_mobile_01 on 2024-03-26T09:00:00Z with participants sh_001, sh_003, sh_005, and emp_pm_03, scheduled by sh_003. Report: 1) The overall risk level from the risk assessment (if created), and 2) The number of urgent items from the scheduled review.",
        actions=[
            Action(
                name="SearchChangeRequests",
                kwargs={"project_id": "proj_mobile_01", "include_impact": True},
            ),
            Action(name="CheckChangeConflicts", kwargs={"cr_id": "cr_003"}),
            Action(
                name="ValidateChangeCompliance",
                kwargs={
                    "cr_id": "cr_003",
                    "compliance_checklist": ["critical_path_risk_assessed"],
                },
            ),
            Action(
                name="CreateRiskAssessment",
                kwargs={
                    "cr_id": "cr_003",
                    "assessed_by": "sh_005",
                    "risk_categories": {
                        "technical": "high",
                        "schedule": "high",
                        "resource": "medium",
                        "quality": "low",
                        "stakeholder": "medium",
                    },
                    "identified_risks": [
                        "Integration complexity with multiple languages",
                        "Testing resource constraints",
                        "Deployment synchronization challenges",
                    ],
                    "mitigation_strategies": [
                        "Phased language rollout",
                        "Automated testing framework",
                        "Feature flags for controlled release",
                    ],
                    "contingency_plans": {
                        "integration_failure": "Rollback to single language",
                        "resource_shortage": "Prioritize core languages first",
                    },
                    "rollback_procedure": "Disable language features via configuration",
                },
            ),
            Action(
                name="ScheduleChangeReview",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "review_date": "2024-03-26T09:00:00Z",
                    "review_type": "adhoc",
                    "participants": ["sh_001", "sh_003", "sh_005", "emp_pm_03"],
                    "scheduled_by": "sh_003",
                },
            ),
        ],
        outputs=['"overall_risk_level": "medium"', '"urgent_items": 0'],
    ),
    Task(
        annotator="0",
        user_id="change_compliance_officer",
        instruction="""
        You are a compliance officer reviewing change management practices for project proj_mobile_01. Search for all
        change requests in proj_mobile_01 (set include impact as true). Validate compliance for cr_001 checking for artifacts_updated and
        within_budget_threshold. Calculate cumulative impact including
        pending changes. If the total budget impact from the cumulative impact calculation exceeds 100000, escalate
        cr_003 to executive level and escalated_by as sh_005. Generate a compliance report for proj_mobile_01 with
        details. Report the non_compliant_items from the compliance report.
        """,
        actions=[
            Action(
                name="SearchChangeRequests",
                kwargs={"project_id": "proj_mobile_01", "include_impact": True},
            ),
            Action(
                name="ValidateChangeCompliance",
                kwargs={
                    "cr_id": "cr_001",
                    "compliance_checklist": [
                        "artifacts_updated",
                        "within_budget_threshold",
                    ],
                },
            ),
            Action(
                name="CalculateCumulativeImpact",
                kwargs={"project_id": "proj_mobile_01", "include_pending": True},
            ),
            Action(
                name="EscalateChangeRequest",
                kwargs={
                    "cr_id": "cr_003",
                    "escalate_to_level": "executive",
                    "escalated_by": "sh_005",
                },
            ),
            Action(
                name="GenerateChangeReport",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "report_type": "compliance",
                    "include_details": True,
                },
            ),
        ],
        outputs=[
            '"non_compliant_items": ["cr_001"]',
        ],
    ),
    Task(
        annotator="0",
        user_id="critical_path_risk_manager",
        instruction="You are a risk manager reviewing critical path changes. Search for change requests in proj_mobile_01 with status pending_approval (set include impact as true). Validate compliance for cr_003 checking specifically for critical_path_risk_assessed and affects_critical_path. If the validation shows that cr_003 affects the critical path and lacks a risk assessment, create a risk assessment with the following details: assessor sh_005, risk categories (technical: medium, schedule: high, resource: medium, quality: low, stakeholder: low), identified risks ('Translation quality control', 'UI layout complexity', 'Testing timeline pressure'), mitigation strategies ('Professional translation review', 'Responsive design framework', 'Parallel testing streams'), contingency plan for schedule_overrun ('Reduce initial language set'), and rollback procedure ('Feature flag per language'). After handling the risk assessment, link cr_003 to ms_002 with schedule impact type. Generate a summary report for the project. From the risk assessment created, report the overall_risk_level and monitoring_frequency values.",
        actions=[
            Action(
                name="SearchChangeRequests",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "status": "pending_approval",
                    "include_impact": True,
                },
            ),
            Action(
                name="ValidateChangeCompliance",
                kwargs={
                    "cr_id": "cr_003",
                    "compliance_checklist": [
                        "critical_path_risk_assessed",
                        "affects_critical_path",
                    ],
                },
            ),
            Action(
                name="CreateRiskAssessment",
                kwargs={
                    "cr_id": "cr_003",
                    "assessed_by": "sh_005",
                    "risk_categories": {
                        "technical": "medium",
                        "schedule": "high",
                        "resource": "medium",
                        "quality": "low",
                        "stakeholder": "low",
                    },
                    "identified_risks": [
                        "Translation quality control",
                        "UI layout complexity",
                        "Testing timeline pressure",
                    ],
                    "mitigation_strategies": [
                        "Professional translation review",
                        "Responsive design framework",
                        "Parallel testing streams",
                    ],
                    "contingency_plans": {
                        "schedule_overrun": "Reduce initial language set"
                    },
                    "rollback_procedure": "Feature flag per language",
                },
            ),
            Action(
                name="LinkChangeToMilestone",
                kwargs={
                    "cr_id": "cr_003",
                    "milestone_id": "ms_002",
                    "impact_type": "schedule",
                },
            ),
            Action(
                name="GenerateChangeReport",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "report_type": "summary",
                    "include_details": False,
                },
            ),
        ],
        outputs=['"overall_risk_level": "medium"', '"monitoring_frequency": "weekly"'],
    ),
    Task(
        annotator="0",
        user_id="milestone_impact_coordinator",
        instruction="""
        You are coordinating milestone impacts for project proj_ai_01. Search for all change requests in this project (set include impact as false).
        For cr_002, check if it has any conflicts with other changes. Perform an impact assessment for cr_002 with
        assessed_by as emp_pm_04, timeline impact of -3 weeks, budget impact of -75000, and an empty list for resource requirements and technical dependencies.
        Since cr_002 is a scope reduction (based on its change_type), link it to ms_003 with impact type 'scope'. Then
        calculate the cumulative impact for proj_ai_01 including pending changes. Generate a detailed report for the
        project with full details. From your analysis, report: 1) The number of conflicts found for cr_002, and 2) The
        cumulative timeline impact in weeks from the cumulative impact calculation.""",
        actions=[
            Action(
                name="SearchChangeRequests",
                kwargs={"project_id": "proj_ai_01", "include_impact": False},
            ),
            Action(name="CheckChangeConflicts", kwargs={"cr_id": "cr_002"}),
            Action(
                name="PerformImpactAssessment",
                kwargs={
                    "cr_id": "cr_002",
                    "assessed_by": "emp_pm_04",
                    "timeline_impact_weeks": -3,
                    "budget_impact": -75000,
                    "resource_requirements": [],
                    "technical_dependencies": [],
                },
            ),
            Action(
                name="LinkChangeToMilestone",
                kwargs={
                    "cr_id": "cr_002",
                    "milestone_id": "ms_003",
                    "impact_type": "scope",
                },
            ),
            Action(
                name="CalculateCumulativeImpact",
                kwargs={"project_id": "proj_ai_01", "include_pending": True},
            ),
            Action(
                name="GenerateChangeReport",
                kwargs={
                    "project_id": "proj_ai_01",
                    "report_type": "detailed",
                    "include_details": True,
                },
            ),
        ],
        outputs=['"conflicts_found": 0', '"timeline_impact_weeks": -3'],
    ),
    Task(
        annotator="0",
        user_id="baseline_approval_authority",
        instruction="""
        You are a baseline approval authority for project proj_enterprise_01. Search for all change requests in this
        project (set include impact as true). Compare the project against its current baseline (version 1.0). Create a new scope baseline
        for the project named 'Enterprise Platform Phase 2 Baseline' with the
        following specifications: scope items including 'Microservices architecture' (architecture category),
        'API gateway implementation' (infrastructure category), 'Service mesh deployment' (infrastructure category),
        and 'Security layer' (security category); deliverables including 'Enterprise Architecture'
        (Complete microservices architecture, 960 hours) and 'Security Framework' (Zero trust security implementation,
        480 hours); acceptance criteria for 99.9% uptime availability and zero trust architecture security; success
        metrics for sub-second response times performance and support for 10000 concurrent users scalability; created
        by emp_arch_01. After creating the baseline, approve the newly created baseline as sh_003 with approval notes
        'Phase 2 baseline approved with security enhancements'.
        Use the following specific identifiers when creating the new scope baseline: set the baseline_id to bl_7f3d9e2a;
        define scope items with IDs scope_301, scope_302, scope_303, and scope_304 for "Microservices architecture",
        "API gateway implementation", "Service mesh deployment", and "Security layer" respectively; and use deliverable
        IDs del_301 and del_302 for "Enterprise Architecture" and "Security Framework". These identifiers are predefined
        and must be used exactly as provided to ensure consistency in evaluation.
        Generate a compliance report for the project (set include details as false). From the
        approved baseline, report: the total change requests.
        """,
        actions=[
            Action(
                name="SearchChangeRequests",
                kwargs={"project_id": "proj_enterprise_01", "include_impact": True},
            ),
            Action(
                name="CompareAgainstBaseline",
                kwargs={"project_id": "proj_enterprise_01", "baseline_version": "1.0"},
            ),
            Action(
                name="CreateScopeBaseline",
                kwargs={
                    "baseline_id": "bl_7f3d9e2a",
                    "project_id": "proj_enterprise_01",
                    "baseline_name": "Enterprise Platform Phase 2 Baseline",
                    "scope_items": [
                        {
                            "item_id": "scope_301",
                            "description": "Microservices architecture",
                            "category": "architecture",
                        },
                        {
                            "item_id": "scope_302",
                            "description": "API gateway implementation",
                            "category": "infrastructure",
                        },
                        {
                            "item_id": "scope_303",
                            "description": "Service mesh deployment",
                            "category": "infrastructure",
                        },
                        {
                            "item_id": "scope_304",
                            "description": "Security layer",
                            "category": "security",
                        },
                    ],
                    "deliverables": [
                        {
                            "deliverable_id": "del_301",
                            "name": "Enterprise Architecture",
                            "description": "Complete microservices architecture",
                            "estimated_hours": 960,
                        },
                        {
                            "deliverable_id": "del_302",
                            "name": "Security Framework",
                            "description": "Zero trust security implementation",
                            "estimated_hours": 480,
                        },
                    ],
                    "acceptance_criteria": {
                        "availability": "99.9% uptime",
                        "security": "Zero trust architecture",
                    },
                    "success_metrics": {
                        "performance": "Sub-second response times",
                        "scalability": "Support 10000 concurrent users",
                    },
                    "created_by": "emp_arch_01",
                },
            ),
            Action(
                name="ApproveBaselineUpdate",
                kwargs={
                    "baseline_id": "bl_7f3d9e2a",
                    "approved_by": "sh_003",
                    "approval_notes": "Phase 2 baseline approved with security enhancements",
                },
            ),
            Action(
                name="GenerateChangeReport",
                kwargs={
                    "project_id": "proj_enterprise_01",
                    "report_type": "compliance",
                    "include_details": False,
                },
            ),
        ],
        outputs=['"total_change_requests": 1'],
    ),
    Task(
        annotator="0",
        user_id="conflict_resolution_specialist",
        instruction="Acting as a conflict resolution specialist, you are tasked with examining project proj_mobile_01. Locate any conflicts within this project (ensure include impact is set to true). Should you identify a conflict involving a key deliverable, combine the conflicting change requests with the highest priority change request as the main one, using "
                    " as the primary change request, and merged by sh_003."
                    " Finally, generate a detailed report for the project. Considering all workflow, output if it was found conflicts"
                    " in the project, indicate the quantity of conflicts, the change requests involved and the conflict solution.",
        actions=[
            Action(
                name="SearchChangeRequests",
                kwargs={"project_id": "proj_mobile_01", "include_impact": True},
            ),
            Action(name="CheckChangeConflicts", kwargs={"cr_id": "cr_001"}),
            Action(
                name="MergeChangeRequests",
                kwargs={
                    "primary_cr_id": "cr_001",
                    "secondary_cr_ids": ["cr_003"],
                    "merged_by": "sh_003",
                },
            ),
            Action(
                name="GenerateChangeReport",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "report_type": "detailed",
                    "include_details": True,
                },
            ),
        ],
        outputs=[
            '"conflicts_found": 1', '"change_requests_involved: ["cr_001", "cr_003"]', '"action": merge change requests',
        ],
    ),
    Task(
        annotator="0",
        user_id="change_conflict_analyst",
        instruction="""
        You are analyzing change conflicts for project proj_enterprise_01. Search for all change requests in this
        project (set include impact as true). Check for conflicts with cr_004. Since cr_004 has been rejected,
        search for any change requests with
        status 'rejected' in proj_enterprise_01 (set include impact as false). Validate compliance for cr_004 checking specifically for
        cooling_period_observed and baseline_exists. Archive changes for proj_enterprise_01 that were created
        before 2024-03-01T00:00:00Z,
        with sh_003 as the archiver. Generate a summary report for the project. From your analysis, report
        the number of conflicts found for cr_004.
        """,
        actions=[
            Action(
                name="SearchChangeRequests",
                kwargs={"project_id": "proj_enterprise_01", "include_impact": True},
            ),
            Action(name="CheckChangeConflicts", kwargs={"cr_id": "cr_004"}),
            Action(
                name="SearchChangeRequests",
                kwargs={
                    "project_id": "proj_enterprise_01",
                    "status": "rejected",
                    "include_impact": False,
                },
            ),
            Action(
                name="ValidateChangeCompliance",
                kwargs={
                    "cr_id": "cr_004",
                    "compliance_checklist": [
                        "cooling_period_observed",
                        "baseline_exists",
                    ],
                },
            ),
            Action(
                name="ArchiveChanges",
                kwargs={
                    "project_id": "proj_enterprise_01",
                    "archive_before_date": "2024-03-01T00:00:00Z",
                    "archived_by": "sh_003",
                },
            ),
            Action(
                name="GenerateChangeReport",
                kwargs={
                    "project_id": "proj_enterprise_01",
                    "report_type": "summary",
                    "include_details": False,
                },
            ),
        ],
        outputs=['"conflicts_found": 0'],
    ),
    Task(
        annotator="0",
        user_id="scope_change_coordinator",
        instruction="""
        You are coordinating a scope addition for project proj_web_01. First, search for any existing change requests
        for this project (set include impact as true). Then create a new change request with these exact details: title
        'Add real-time chat support
        feature', description 'Implement live chat functionality for customer support integration', requester emp_ux_03,
        type scope_addition, priority high, affecting deliverable del_005, business justification 'Customer feedback
        shows 82% want live chat support. Will improve user engagement and reduce support tickets.' After creating the
        change request, use the returned cr_id (which should be cr_f8a3b7d9) for all subsequent actions. Check for conflicts using
        the cr_id. Validate compliance checking only
        baseline_exists and has_business_justification. Create a standard workflow. Record approval by sh_002 with
        decision 'approve' and comment 'Aligns with customer experience goals' (use app_0001 as approval ID). Finally, generate a summary report
        and report the total number of change requests for the project.
        """,
        actions=[
            Action(
                name="SearchChangeRequests",
                kwargs={"project_id": "proj_web_01", "include_impact": True},
            ),
            Action(
                name="CreateChangeRequest",
                kwargs={
                    "cr_id": "cr_f8a3b7d9",
                    "title": "Add real-time chat support feature",
                    "description": "Implement live chat functionality for customer support integration",
                    "requester_id": "emp_ux_03",
                    "project_id": "proj_web_01",
                    "change_type": "scope_addition",
                    "priority": "high",
                    "affected_deliverables": ["del_005"],
                    "business_justification": "Customer feedback shows 82% want live chat support. Will improve user engagement and reduce support tickets.",
                },
            ),
            Action(name="CheckChangeConflicts", kwargs={"cr_id": "cr_f8a3b7d9"}),
            Action(
                name="ValidateChangeCompliance",
                kwargs={
                    "cr_id": "cr_f8a3b7d9",
                    "compliance_checklist": [
                        "baseline_exists",
                        "has_business_justification",
                    ],
                },
            ),
            Action(
                name="CreateApprovalWorkflow",
                kwargs={"cr_id": "cr_f8a3b7d9", "workflow_type": "standard"},
            ),
            Action(
                name="RecordApprovalDecision",
                kwargs={
                    "approval_id": "app_0001",
                    "cr_id": "cr_f8a3b7d9",
                    "approver_id": "sh_002",
                    "decision": "approve",
                    "comments": "Aligns with customer experience goals",
                    "conditions": [],
                },
            ),
            Action(
                name="GenerateChangeReport",
                kwargs={
                    "project_id": "proj_web_01",
                    "report_type": "summary",
                    "include_details": False,
                },
            ),
        ],
        outputs=['"total_change_requests": 1'],
    ),
    Task(
        annotator="0",
        user_id="strategic_change_evaluator",
        instruction="""
        You are evaluating strategic changes for project proj_ai_01. Search for change requests in this project with status
        'in_review' (set include impact as false). For cr_002, check if it has any conflicts. Perform an impact assessment with sh_004 as the assessor,
        timeline impact of -3 weeks, budget impact of -75000, empty resource requirements and technical dependencies.
        Escalate cr_002 to executive level by sh_004. Then update the status to
        'pending_approval' performed by sh_004. Generate a detailed report for the project. From your analysis,
        report the new priority level after escalation.
        """,
        actions=[
            Action(
                name="SearchChangeRequests",
                kwargs={
                    "project_id": "proj_ai_01",
                    "status": "in_review",
                    "include_impact": False,
                },
            ),
            Action(name="CheckChangeConflicts", kwargs={"cr_id": "cr_002"}),
            Action(
                name="PerformImpactAssessment",
                kwargs={
                    "cr_id": "cr_002",
                    "assessed_by": "sh_004",
                    "timeline_impact_weeks": -3,
                    "budget_impact": -75000,
                    "resource_requirements": [],
                    "technical_dependencies": [],
                },
            ),
            Action(
                name="EscalateChangeRequest",
                kwargs={
                    "cr_id": "cr_002",
                    "escalate_to_level": "executive",
                    "escalated_by": "sh_004",
                },
            ),
            Action(
                name="UpdateChangeRequestStatus",
                kwargs={
                    "cr_id": "cr_002",
                    "new_status": "pending_approval",
                    "performed_by": "sh_004",
                },
            ),
            Action(
                name="GenerateChangeReport",
                kwargs={
                    "project_id": "proj_ai_01",
                    "report_type": "detailed",
                    "include_details": True,
                },
            ),
        ],
        outputs=['"new_priority": "critical"'],
    ),
    Task(
        annotator="0",
        user_id="compliance_escalation_officer",
        instruction="You are a compliance officer reviewing critical changes in project proj_mobile_01. Search for all change requests in this project (set include impact as true). Check conflicts for cr_003. Validate compliance for cr_003 checking for no_deliverable_conflicts, critical_path_risk_assessed, and has_rule_violations. Since rule violations exist, escalate cr_003 to critical level escalated by sh_005. After escalation, create a risk assessment for cr_003 by sh_005 with risk categories: technical as high, schedule as critical, resource as high, quality as medium, and stakeholder as medium. For identified risks include: 'Deliverable conflict delays', 'Critical path disruption', and 'Resource allocation conflicts'. For mitigation strategies include: 'Merge conflicting changes', 'Fast-track critical activities', and 'Bring in additional resources'. For contingency plans, set timeline_slip as 'Reduce feature set' and resource_shortage as 'Outsource non-critical tasks'. Set rollback procedure as 'Revert to single language support'. Schedule an adhoc review for proj_mobile_01 on 2024-03-23T08:00:00Z with participants sh_001, sh_003, sh_005 scheduled by sh_005. Report whether the escalation workflow was updated and the overall risk level from the risk assessment.",
        actions=[
            Action(
                name="SearchChangeRequests",
                kwargs={"project_id": "proj_mobile_01", "include_impact": True},
            ),
            Action(name="CheckChangeConflicts", kwargs={"cr_id": "cr_003"}),
            Action(
                name="ValidateChangeCompliance",
                kwargs={
                    "cr_id": "cr_003",
                    "compliance_checklist": [
                        "no_deliverable_conflicts",
                        "critical_path_risk_assessed",
                        "has_rule_violations",
                    ],
                },
            ),
            Action(
                name="EscalateChangeRequest",
                kwargs={
                    "cr_id": "cr_003",
                    "escalate_to_level": "critical",
                    "escalated_by": "sh_005",
                },
            ),
            Action(
                name="CreateRiskAssessment",
                kwargs={
                    "cr_id": "cr_003",
                    "assessed_by": "sh_005",
                    "risk_categories": {
                        "technical": "high",
                        "schedule": "critical",
                        "resource": "high",
                        "quality": "medium",
                        "stakeholder": "medium",
                    },
                    "identified_risks": [
                        "Deliverable conflict delays",
                        "Critical path disruption",
                        "Resource allocation conflicts",
                    ],
                    "mitigation_strategies": [
                        "Merge conflicting changes",
                        "Fast-track critical activities",
                        "Bring in additional resources",
                    ],
                    "contingency_plans": {
                        "timeline_slip": "Reduce feature set",
                        "resource_shortage": "Outsource non-critical tasks",
                    },
                    "rollback_procedure": "Revert to single language support",
                },
            ),
            Action(
                name="ScheduleChangeReview",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "review_date": "2024-03-23T08:00:00Z",
                    "review_type": "adhoc",
                    "participants": ["sh_001", "sh_003", "sh_005"],
                    "scheduled_by": "sh_005",
                },
            ),
        ],
        outputs=['"workflow_updated": true', '"overall_risk_level": "high"'],
    ),
    Task(
        annotator="0",
        user_id="change_status_manager",
        instruction="""
        You are managing the change pipeline for project proj_mobile_01. Search for all change requests in this project (set include impact as true).
        Validate its compliance checking for
        has_business_justification, has_impact_assessment, and proper_approval_sequence. Since cr_003 is still
        pending, record an approval decision for it by sh_003 approving with comment 'Language support critical
        for market expansion'. Update the status of cr_003 to approved. Track an artifact update for cr_003 updating
        the budget artifact with description 'Budget adjusted for translation services' from version 2.2 to version
        2.3 by emp_finance_01. Calculate cumulative impact for the project including pending changes. Output the
        total budget impact for project proj_mobile_01.
        """,
        actions=[
            Action(
                name="SearchChangeRequests",
                kwargs={"project_id": "proj_mobile_01", "include_impact": True},
            ),
            Action(
                name="ValidateChangeCompliance",
                kwargs={
                    "cr_id": "cr_003",
                    "compliance_checklist": [
                        "has_business_justification",
                        "has_impact_assessment",
                        "proper_approval_sequence",
                    ],
                },
            ),
            Action(
                name="RecordApprovalDecision",
                kwargs={
                    "cr_id": "cr_003",
                    "approver_id": "sh_003",
                    "decision": "approve",
                    "comments": "Language support critical for market expansion",
                    "conditions": [],
                },
            ),
            Action(
                name="UpdateChangeRequestStatus",
                kwargs={
                    "cr_id": "cr_003",
                    "new_status": "approved",
                    "performed_by": "sh_003",
                },
            ),
            Action(
                name="TrackArtifactUpdates",
                kwargs={
                    "cr_id": "cr_003",
                    "artifact_type": "budget",
                    "update_description": "Budget adjusted for translation services",
                    "version_before": "2.2",
                    "version_after": "2.3",
                    "updated_by": "emp_finance_01",
                },
            ),
            Action(
                name="CalculateCumulativeImpact",
                kwargs={"project_id": "proj_mobile_01", "include_pending": True},
            ),
        ],
        outputs=['"total_budget_impact": 110000'],
    ),
    Task(
        annotator="0",
        user_id="ai_platform_change_reviewer",
        instruction="""
        You are reviewing scope changes for project proj_ai_01. Search for change requests in this project with status
        in_review (set include impact as true). For cr_002, perform an impact assessment by emp_data_01 with timeline impact of
        -2 weeks and budget
        impact of -50000 (negative values since this is a scope reduction). Check for any conflicts with cr_002.
        Validate compliance for cr_002 using these specific checks: baseline_exists, has_business_justification, and
        has_impact_assessment. Create a standard approval workflow for cr_002. Record approval decision by sh_002
        with decision 'approve' and comments 'Scope reduction helps meet deadline'.
        Update cr_002 status to 'approved' performed by sh_002. Link cr_002 to milestone ms_003 with impact type
        'scope'. Calculate the cumulative impact for proj_ai_01 with include_pending set to false. Generate a summary
        report for the project. From the cumulative impact calculation results, report the timeline_impact_weeks value.
        """,
        actions=[
            Action(
                name="SearchChangeRequests",
                kwargs={
                    "project_id": "proj_ai_01",
                    "status": "in_review",
                    "include_impact": True,
                },
            ),
            Action(
                name="PerformImpactAssessment",
                kwargs={
                    "cr_id": "cr_002",
                    "assessed_by": "emp_data_01",
                    "timeline_impact_weeks": -2,
                    "budget_impact": -50000,
                    "resource_requirements": [],
                    "technical_dependencies": [],
                },
            ),
            Action(name="CheckChangeConflicts", kwargs={"cr_id": "cr_002"}),
            Action(
                name="ValidateChangeCompliance",
                kwargs={
                    "cr_id": "cr_002",
                    "compliance_checklist": [
                        "baseline_exists",
                        "has_business_justification",
                        "has_impact_assessment",
                    ],
                },
            ),
            Action(
                name="CreateApprovalWorkflow",
                kwargs={"cr_id": "cr_002", "workflow_type": "standard"},
            ),
            Action(
                name="RecordApprovalDecision",
                kwargs={
                    "cr_id": "cr_002",
                    "approver_id": "sh_002",
                    "decision": "approve",
                    "comments": "Scope reduction helps meet deadline",
                    "conditions": [],
                },
            ),
            Action(
                name="UpdateChangeRequestStatus",
                kwargs={
                    "cr_id": "cr_002",
                    "new_status": "approved",
                    "performed_by": "sh_002",
                },
            ),
            Action(
                name="LinkChangeToMilestone",
                kwargs={
                    "cr_id": "cr_002",
                    "milestone_id": "ms_003",
                    "impact_type": "scope",
                },
            ),
            Action(
                name="CalculateCumulativeImpact",
                kwargs={"project_id": "proj_ai_01", "include_pending": False},
            ),
            Action(
                name="GenerateChangeReport",
                kwargs={
                    "project_id": "proj_ai_01",
                    "report_type": "summary",
                    "include_details": False,
                },
            ),
        ],
        outputs=['"timeline_impact_weeks": -2'],
    ),
    Task(
        annotator="0",
        user_id="change_consolidation_coordinator",
        instruction="""
        You are consolidating related changes. Search for all change requests in proj_ai_01 (set include impact as true). Check conflicts for
        cr_002. Update cr_002 status to draft performed by emp_pm_04. Update cr_004 status to draft performed by
        emp_arch_01. Check conflicts for cr_004. Calculate cumulative
        impact for proj_ai_01 excluding pending changes. Generate a summary report and report the total number of
        change requests from the summary report.
        """,
        actions=[
            Action(
                name="SearchChangeRequests",
                kwargs={"project_id": "proj_ai_01", "include_impact": True},
            ),
            Action(name="CheckChangeConflicts", kwargs={"cr_id": "cr_002"}),
            Action(
                name="UpdateChangeRequestStatus",
                kwargs={
                    "cr_id": "cr_002",
                    "new_status": "draft",
                    "performed_by": "emp_pm_04",
                },
            ),
            Action(
                name="UpdateChangeRequestStatus",
                kwargs={
                    "cr_id": "cr_004",
                    "new_status": "draft",
                    "performed_by": "emp_arch_01",
                },
            ),
            Action(name="CheckChangeConflicts", kwargs={"cr_id": "cr_004"}),
            Action(
                name="CalculateCumulativeImpact",
                kwargs={"project_id": "proj_ai_01", "include_pending": False},
            ),
            Action(
                name="GenerateChangeReport",
                kwargs={
                    "project_id": "proj_ai_01",
                    "report_type": "summary",
                    "include_details": False,
                },
            ),
        ],
        outputs=['"total_change_requests": 1'],
    ),
    Task(
        annotator="0",
        user_id="archive_administrator",
        instruction="""
        You are performing quarterly archive cleanup for project proj_enterprise_01. Search for all change requests
        in proj_enterprise_01 (set include impact as false). Then specifically search for rejected changes in
        proj_enterprise_01 (set include impact as false). Validate compliance
        for cr_004 checking cooling_period_observed. If the validation shows no cooling period violations, proceed to
        archive changes for proj_enterprise_01 before date 2024-03-15T00:00:00Z archived by emp_arch_01. After archiving,
        search again for all changes in proj_enterprise_01 to verify the archive operation (set include impact as false). Create a change template
        named 'Database Migration Standard' as template type standard_enhancement with standard fields change_type
        requirement_change and priority critical, requiring approvals from project_manager and technical_lead, created
        by emp_arch_01. Generate a compliance report for the project. Report the archived count from the archive
        operation and the success status from the template creation.
        """,
        actions=[
            Action(
                name="SearchChangeRequests",
                kwargs={"project_id": "proj_enterprise_01", "include_impact": False},
            ),
            Action(
                name="SearchChangeRequests",
                kwargs={
                    "project_id": "proj_enterprise_01",
                    "status": "rejected",
                    "include_impact": False,
                },
            ),
            Action(
                name="ValidateChangeCompliance",
                kwargs={
                    "cr_id": "cr_004",
                    "compliance_checklist": ["cooling_period_observed"],
                },
            ),
            Action(
                name="ArchiveChanges",
                kwargs={
                    "project_id": "proj_enterprise_01",
                    "archive_before_date": "2024-03-15T00:00:00Z",
                    "archived_by": "emp_arch_01",
                },
            ),
            Action(
                name="SearchChangeRequests",
                kwargs={"project_id": "proj_enterprise_01", "include_impact": False},
            ),
            Action(
                name="CreateChangeTemplate",
                kwargs={
                    "template_name": "Database Migration Standard",
                    "template_type": "standard_enhancement",
                    "standard_fields": {
                        "change_type": "requirement_change",
                        "priority": "critical",
                    },
                    "required_approvals": ["project_manager", "technical_lead"],
                    "created_by": "emp_arch_01",
                },
            ),
            Action(
                name="GenerateChangeReport",
                kwargs={
                    "project_id": "proj_enterprise_01",
                    "report_type": "compliance",
                    "include_details": False,
                },
            ),
        ],
        outputs=['"archived_count": 1', '"success": true'],
    ),
    Task(
        annotator="0",
        user_id="emergency_compliance_auditor",
        instruction="""
        You are auditing emergency change compliance across projects. Search for all change requests in proj_mobile_01 (set 'include_impact' as true).
        Validate compliance for cr_003 using these checks: emergency_deadlines_met, has_business_justification,
        and retroactive_status. If cr_003 has emergency approval requirements, generate an audit trail for it
        including approvals. Then search for change requests in proj_ai_01 (set include impact as false). Validate compliance for cr_002 checking if
        baseline exists. Create an approval workflow for it with standard type. Calculate cumulative impact
        for proj_mobile_01 including pending changes. Generate a compliance report for proj_mobile_01. From your
        findings, report the total budget impact from the cumulative impact calculation.""",
        actions=[
            Action(
                name="SearchChangeRequests",
                kwargs={"project_id": "proj_mobile_01", "include_impact": True},
            ),
            Action(
                name="ValidateChangeCompliance",
                kwargs={
                    "cr_id": "cr_003",
                    "compliance_checklist": [
                        "emergency_deadlines_met",
                        "has_business_justification",
                        "retroactive_status",
                    ],
                },
            ),
            Action(
                name="SearchChangeRequests",
                kwargs={"project_id": "proj_ai_01", "include_impact": False},
            ),
            Action(
                name="ValidateChangeCompliance",
                kwargs={
                    "cr_id": "cr_002",
                    "compliance_checklist": [
                        "baseline_exists",
                    ],
                },
            ),
            Action(
                name="CreateApprovalWorkflow",
                kwargs={"cr_id": "cr_002", "workflow_type": "standard"},
            ),
            Action(
                name="CalculateCumulativeImpact",
                kwargs={"project_id": "proj_mobile_01", "include_pending": True},
            ),
            Action(
                name="GenerateChangeReport",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "report_type": "compliance",
                    "include_details": False,
                },
            ),
        ],
        outputs=['"total_budget_impact": 110000'],
    ),
    Task(
        annotator="0",
        user_id="template_standardization_officer",
        instruction="""
        You are standardizing change processes. Search for all change requests in proj_ai_01 (set include impact as false). Search for changes
        with status 'rejected' across all projects (set include impact as false). Validate compliance for cr_004 checking for cooling_period_observed.
        If you find rejected changes, create a change template with template_name 'Critical Infrastructure Change',
        template_type 'requirement_update', with standard_fields containing change_type 'requirement_change', priority
        'critical', typical_duration_weeks 8, and typical_resources 4. Set required_approvals to include project_manager,
        technical_lead, and pmo_director, with risk_threshold 'high', created_by 'sh_003'. Then create another template
         with template_name 'Emergency Security Fix', template_type 'emergency_fix', typical_duration_weeks" 1,
         with standard_fields containing
         change_type 'requirement_change', priority 'critical', and requires_emergency_approval true. Set
         required_approvals to include security_lead and executive_sponsor, with risk_threshold 'critical', created_by
        'sh_005'. Generate a summary report for proj_enterprise_01. Report the usage_count from any created template
         and the total_change_requests from the summary report.""",
        actions=[
            Action(
                name="SearchChangeRequests",
                kwargs={"project_id": "proj_ai_01", "include_impact": False},
            ),
            Action(
                name="SearchChangeRequests",
                kwargs={"status": "rejected", "include_impact": False},
            ),
            Action(
                name="ValidateChangeCompliance",
                kwargs={
                    "cr_id": "cr_004",
                    "compliance_checklist": ["cooling_period_observed"],
                },
            ),
            Action(
                name="CreateChangeTemplate",
                kwargs={
                    "template_name": "Critical Infrastructure Change",
                    "template_type": "requirement_update",
                    "standard_fields": {
                        "change_type": "requirement_change",
                        "priority": "critical",
                        "typical_duration_weeks": 8,
                        "typical_resources": 4,
                    },
                    "required_approvals": [
                        "project_manager",
                        "technical_lead",
                        "pmo_director",
                    ],
                    "risk_threshold": "high",
                    "created_by": "sh_003",
                },
            ),
            Action(
                name="CreateChangeTemplate",
                kwargs={
                    "template_name": "Emergency Security Fix",
                    "template_type": "emergency_fix",
                    "standard_fields": {
                        "change_type": "requirement_change",
                        "priority": "critical",
                        "requires_emergency_approval": True,
                        "typical_duration_weeks": 1,
                    },
                    "required_approvals": ["security_lead", "executive_sponsor"],
                    "risk_threshold": "critical",
                    "created_by": "sh_005",
                },
            ),
            Action(
                name="GenerateChangeReport",
                kwargs={
                    "project_id": "proj_enterprise_01",
                    "report_type": "summary",
                    "include_details": False,
                },
            ),
        ],
        outputs=['"usage_count": 0', '"total_change_requests": 1'],
    ),
    Task(
        annotator="0",
        user_id="resubmission_coordinator",
        instruction="""
        You are managing resubmissions for project proj_enterprise_01. Search for all change requests in this project (set include impact as true).
        Check the details of cr_004. Validate compliance for cr_004 checking cooling_period_observed. Looking at
        cr_004's details, create a new change request (use 'cr_a1b2c3d4' for ID) with title 'Implement document store for unstructured data'
        and description 'Add MongoDB as supplementary database for unstructured data only, keeping PostgreSQL for
        structured data', requested by emp_arch_01, change type requirement_change, priority high, affecting
        deliverable del_007, with justification 'Hybrid approach addresses scalability concerns while minimizing risk.
        Previous rejection feedback incorporated - no migration required.' After creating the change request, use the
        returned cr_id to perform impact assessment by emp_arch_01 with 4 weeks timeline impact and $65000 budget
        impact. Schedule a change review for proj_enterprise_01 on 2024-04-15T14:00:00Z with participants sh_003,
        sh_004, and emp_arch_01, scheduled by sh_003 and review type as 'quarterly'. Generate a summary report and tell me the total number of
        change requests.
        """,
        actions=[
            Action(
                name="SearchChangeRequests",
                kwargs={"project_id": "proj_enterprise_01", "include_impact": True},
            ),
            Action(
                name="ValidateChangeCompliance",
                kwargs={
                    "cr_id": "cr_004",
                    "compliance_checklist": ["cooling_period_observed"],
                },
            ),
            Action(
                name="CreateChangeRequest",
                kwargs={
                    "cr_id": "cr_a1b2c3d4",
                    "title": "Implement document store for unstructured data",
                    "description": "Add MongoDB as supplementary database for unstructured data only, keeping PostgreSQL for structured data",
                    "requester_id": "emp_arch_01",
                    "project_id": "proj_enterprise_01",
                    "change_type": "requirement_change",
                    "priority": "high",
                    "affected_deliverables": ["del_007"],
                    "business_justification": "Hybrid approach addresses scalability concerns while minimizing risk. Previous rejection feedback incorporated - no migration required.",
                },
            ),
            Action(
                name="PerformImpactAssessment",
                kwargs={
                    "cr_id": "cr_a1b2c3d4",
                    "assessed_by": "emp_arch_01",
                    "timeline_impact_weeks": 4,
                    "budget_impact": 65000,
                    "resource_requirements": [],
                    "technical_dependencies": [],
                },
            ),
            Action(
                name="ScheduleChangeReview",
                kwargs={
                    "project_id": "proj_enterprise_01",
                    "review_date": "2024-04-15T14:00:00Z",
                    "review_type": "quarterly",
                    "participants": ["sh_003", "sh_004", "emp_arch_01"],
                    "scheduled_by": "sh_003",
                },
            ),
            Action(
                name="GenerateChangeReport",
                kwargs={
                    "project_id": "proj_enterprise_01",
                    "report_type": "summary",
                    "include_details": False,
                },
            ),
        ],
        outputs=['"total_change_requests": 2'],
    ),
    Task(
        annotator="0",
        user_id="project_cleanup_coordinator",
        instruction="""
        You are performing quarterly status cleanup. Search for all change requests in proj_mobile_01 (set include impact as false). Check conflicts
        for cr_003. Since cr_003 has deliverable conflicts with cr_001, validate compliance for both cr_001 and cr_003
        checking no_deliverable_conflicts. Due to the conflicts, bulk update the status of cr_003 to cancelled updated
        by sh_002. Then search for approved changes in proj_mobile_01 (set include impact as false). Attempt to bulk update cr_001 and cr_005 to
        in_implementation status updated by emp_pm_03. Generate a
        detailed report with full details. Report the budget impact of cr_003 in the generated report.
        """,
        actions=[
            Action(
                name="SearchChangeRequests",
                kwargs={"project_id": "proj_mobile_01", "include_impact": False},
            ),
            Action(name="CheckChangeConflicts", kwargs={"cr_id": "cr_003"}),
            Action(
                name="ValidateChangeCompliance",
                kwargs={
                    "cr_id": "cr_001",
                    "compliance_checklist": ["no_deliverable_conflicts"],
                },
            ),
            Action(
                name="ValidateChangeCompliance",
                kwargs={
                    "cr_id": "cr_003",
                    "compliance_checklist": ["no_deliverable_conflicts"],
                },
            ),
            Action(
                name="BulkUpdateChangeStatus",
                kwargs={
                    "cr_ids": ["cr_003"],
                    "new_status": "cancelled",
                    "updated_by": "sh_002",
                },
            ),
            Action(
                name="SearchChangeRequests",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "status": "approved",
                    "include_impact": False,
                },
            ),
            Action(
                name="BulkUpdateChangeStatus",
                kwargs={
                    "cr_ids": ["cr_001", "cr_005"],
                    "new_status": "in_implementation",
                    "updated_by": "emp_pm_03",
                },
            ),
            Action(
                name="GenerateChangeReport",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "report_type": "detailed",
                    "include_details": True,
                },
            ),
        ],
        outputs=['"budget_impact": 65000'],
    ),
    Task(
        annotator="0",
        user_id="change_cleanup_coordinator",
        instruction="""
        You are performing quarterly cleanup for project proj_mobile_01. First search for all change requests in this
        project (set include impact as false). Generate an audit trail for cr_001 including both approvals and artifacts.
        Since cr_001 is approved
        and has been implemented, bulk update the status of cr_001 from approved to completed updated by sh_003.
        Create a new change template named 'Mobile Feature Addition' as template type standard_enhancement with
        standard fields change_type scope_addition, priority medium, typical_duration_weeks 3, and typical_resources 2,
        requiring approvals from project_manager and technical_lead, risk threshold medium, created by sh_003.
        Calculate ROI for cr_001 with expected benefits of cost_savings_monthly 8000 and productivity_gain_percentage 15 over
        12 months. Generate a summary report for the project (set 'include_details' as false.
        Output the ROI percentage from the ROI calculation.
        """,
        actions=[
            Action(
                name="SearchChangeRequests",
                kwargs={"project_id": "proj_mobile_01", "include_impact": False},
            ),
            Action(
                name="GenerateAuditTrail",
                kwargs={
                    "cr_id": "cr_001",
                    "include_approvals": True,
                    "include_artifacts": True,
                },
            ),
            Action(
                name="BulkUpdateChangeStatus",
                kwargs={
                    "cr_ids": ["cr_001"],
                    "new_status": "completed",
                    "updated_by": "sh_003",
                },
            ),
            Action(
                name="CreateChangeTemplate",
                kwargs={
                    "template_name": "Mobile Feature Addition",
                    "template_type": "standard_enhancement",
                    "standard_fields": {
                        "change_type": "scope_addition",
                        "priority": "medium",
                        "typical_duration_weeks": 3,
                        "typical_resources": 2,
                    },
                    "required_approvals": ["project_manager", "technical_lead"],
                    "risk_threshold": "medium",
                    "created_by": "sh_003",
                },
            ),
            Action(
                name="CalculateChangeRoi",
                kwargs={
                    "cr_id": "cr_001",
                    "expected_benefits": {
                        "cost_savings_monthly": 8000,
                        "productivity_gain_percentage": 15,
                    },
                    "benefit_timeframe_months": 12,
                },
            ),
            Action(
                name="GenerateChangeReport",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "report_type": "summary",
                    "include_details": False,
                },
            ),
        ],
        outputs=['"roi_percentage": 877.8'],
    ),
    Task(
        annotator="0",
        user_id="change_roi_analyst",
        instruction="""
        You are analyzing ROI for pending changes in project proj_mobile_01. Search for change requests with status
        pending_approval in this project (set include impact as true). Perform an impact
        assessment for cr_003 by emp_analyst_01 with timeline impact of 3 weeks, budget impact of 65000, and resource
        requirements for emp_dev_20 at 15 hours per week for 4 weeks. Calculate the ROI for cr_003 with expected benefits
        of 25000 in revenue_increase_monthly for 12 months. If ROI is positive, link cr_003 to milestone ms_002 with
        impact type scope. If ROI exceeds 200%, record approval decision for cr_003 by sh_002 with decision approve
        and comment 'High ROI justifies multi-language investment'. Generate a detailed report for the project. Output
        the ROI percentage and payback period in months from the ROI calculation results.
        """,
        actions=[
            Action(
                name="SearchChangeRequests",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "status": "pending_approval",
                    "include_impact": True,
                },
            ),
            Action(
                name="PerformImpactAssessment",
                kwargs={
                    "cr_id": "cr_003",
                    "assessed_by": "emp_analyst_01",
                    "timeline_impact_weeks": 3,
                    "budget_impact": 65000,
                    "resource_requirements": [
                        {
                            "employee_id": "emp_dev_20",
                            "hours_per_week": 15,
                            "duration_weeks": 4,
                        }
                    ],
                    "technical_dependencies": [],
                },
            ),
            Action(
                name="CalculateChangeRoi",
                kwargs={
                    "cr_id": "cr_003",
                    "expected_benefits": {"revenue_increase_monthly": 25000},
                    "benefit_timeframe_months": 12,
                },
            ),
            Action(
                name="LinkChangeToMilestone",
                kwargs={
                    "cr_id": "cr_003",
                    "milestone_id": "ms_002",
                    "impact_type": "scope",
                },
            ),
            Action(
                name="RecordApprovalDecision",
                kwargs={
                    "cr_id": "cr_003",
                    "approver_id": "sh_002",
                    "decision": "approve",
                    "comments": "High ROI justifies multi-language investment",
                    "conditions": [],
                },
            ),
            Action(
                name="GenerateChangeReport",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "report_type": "detailed",
                    "include_details": True,
                },
            ),
        ],
        outputs=['"roi_percentage": 305.4', '"payback_period_months": 3.0'],
    ),
    Task(
        annotator="0",
        user_id="conflict_resolution_manager",
        instruction="""
        You are resolving conflicts for project proj_mobile_01. Search for all change requests in this project (set include impact as true).
        Check conflicts for cr_001. Then check conflicts for cr_003. If both CRs affect the same deliverable(s), they
        violate Rule 3 (multiple change requests affecting the same deliverable must be consolidated). If such a
        violation exists, merge cr_003 into cr_001 as the primary change merged by sh_003. After merging (if applicable),
        escalate cr_001 to executive level escalated by sh_003. Calculate cumulative impact for the project excluding
        pending changes. Generate a compliance report and report the number of deliverable conflicts found in the
        compliance summary.
        """,
        actions=[
            Action(
                name="SearchChangeRequests",
                kwargs={"project_id": "proj_mobile_01", "include_impact": True},
            ),
            Action(name="CheckChangeConflicts", kwargs={"cr_id": "cr_001"}),
            Action(name="CheckChangeConflicts", kwargs={"cr_id": "cr_003"}),
            Action(
                name="MergeChangeRequests",
                kwargs={
                    "primary_cr_id": "cr_001",
                    "secondary_cr_ids": ["cr_003"],
                    "merged_by": "sh_003",
                },
            ),
            Action(
                name="EscalateChangeRequest",
                kwargs={
                    "cr_id": "cr_001",
                    "escalate_to_level": "executive",
                    "escalated_by": "sh_003",
                },
            ),
            Action(
                name="CalculateCumulativeImpact",
                kwargs={"project_id": "proj_mobile_01", "include_pending": False},
            ),
            Action(
                name="GenerateChangeReport",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "report_type": "compliance",
                    "include_details": False,
                },
            ),
        ],
        outputs=['"deliverable_conflicts": 0'],
    ),
    Task(
        annotator="0",
        user_id="audit_compliance_officer",
        instruction="""
        You are conducting an audit review of approved changes in project proj_mobile_01. Search for change requests
        with status approved in this project (set include_impact as true). For cr_001, validate compliance checking proper_approval_sequence,
        artifacts_updated, and emergency_deadlines_met. Generate an audit trail for cr_001 including both approvals
        and artifacts. Then check if cr_003 has any conflicts. Generate an audit trail for cr_003 including approvals.
        Schedule a change review for proj_mobile_01 on
        2024-04-05T10:00:00Z with participants sh_002, sh_003, and sh_004 scheduled by sh_003 to discuss audit findings (set review type as 'quarterly').
        Generate a compliance report for the project. From the audit trail for cr_001, report the total number of events.
        Also report the compliance status from the validation check for cr_001.
        """,
        actions=[
            Action(
                name="SearchChangeRequests",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "status": "approved",
                    "include_impact": True,
                },
            ),
            Action(
                name="ValidateChangeCompliance",
                kwargs={
                    "cr_id": "cr_001",
                    "compliance_checklist": [
                        "proper_approval_sequence",
                        "artifacts_updated",
                        "emergency_deadlines_met",
                    ],
                },
            ),
            Action(
                name="GenerateAuditTrail",
                kwargs={
                    "cr_id": "cr_001",
                    "include_approvals": True,
                    "include_artifacts": True,
                },
            ),
            Action(name="CheckChangeConflicts", kwargs={"cr_id": "cr_003"}),
            Action(
                name="GenerateAuditTrail",
                kwargs={
                    "cr_id": "cr_003",
                    "include_approvals": True,
                    "include_artifacts": False,
                },
            ),
            Action(
                name="ScheduleChangeReview",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "review_date": "2024-04-05T10:00:00Z",
                    "review_type": "quarterly",
                    "participants": ["sh_002", "sh_003", "sh_004"],
                    "scheduled_by": "sh_003",
                },
            ),
            Action(
                name="GenerateChangeReport",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "report_type": "compliance",
                    "include_details": False,
                },
            ),
        ],
        outputs=['"total_events": 10', '"compliance_status": "non_compliant"'],
    ),
    Task(
        annotator="0",
        user_id="emergency_approval_coordinator",
        instruction="""
        You are handling an emergency change and its retroactive approval. Search for change requests in proj_ai_01 with status
        in_review (set 'include_impact' as false).
        For cr_002, validate compliance checking has_impact_assessment and critical_path_risk_assessed. Process cr_002 as
        an emergency change (use elog_6f8a3c21 for ID) authorized by sh_003 with emergency type bypass_approval and the justification 'Critical client
        deadline - scope reduction must be implemented immediately to meet Q2 deliverable'.
        After processing the emergency change, use the emergency log ID from the response to record retroactive approval
        by sh_001 with approval decision approve. Then update cr_002 status to in_implementation
        performed by sh_003. Generate an audit trail for cr_002 excluding approvals and excluding artifacts and
        output the current total events in the summary.
        """,
        actions=[
            Action(
                name="SearchChangeRequests",
                kwargs={
                    "project_id": "proj_ai_01",
                    "status": "in_review",
                    "include_impact": False,
                },
            ),
            Action(
                name="ValidateChangeCompliance",
                kwargs={
                    "cr_id": "cr_002",
                    "compliance_checklist": [
                        "has_impact_assessment",
                        "critical_path_risk_assessed",
                    ],
                },
            ),
            Action(
                name="ProcessEmergencyChange",
                kwargs={
                    "log_id": "elog_6f8a3c21",
                    "cr_id": "cr_002",
                    "authorized_by": "sh_003",
                    "emergency_type": "bypass_approval",
                    "justification": "Critical client deadline - scope reduction must be implemented immediately to meet Q2 deliverable",
                },
            ),
            Action(
                name="RecordRetroactiveApproval",
                kwargs={
                    "emergency_log_id": "elog_6f8a3c21",
                    "approver_id": "sh_001",
                    "approval_decision": "approve",
                },
            ),
            Action(
                name="UpdateChangeRequestStatus",
                kwargs={
                    "cr_id": "cr_002",
                    "new_status": "in_implementation",
                    "performed_by": "sh_003",
                },
            ),
            Action(
                name="GenerateAuditTrail",
                kwargs={
                    "cr_id": "cr_002",
                    "include_approvals": False,
                    "include_artifacts": False,
                },
            ),
        ],
        outputs=['"total_events": 3'],
    ),
]
