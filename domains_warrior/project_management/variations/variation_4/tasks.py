from domains.dto import Action, Task

TASKS = [
    Task(
        annotator="0",
        user_id="project_recovery_coordinator",
        instruction="""
        You are a project recovery coordinator for the Mobile App Launch project (proj_mobile_01). The Phase 1 Gate
        Review milestone (ms_002) is approaching but appears to be delayed. First check the project timeline to
        understand the current situation. Then validate if milestone ms_002 is ready to proceed.
        Check the float status for all project milestones. Since
        ms_002 shows negative float, analyze schedule compression options targeting a 10-day reduction using the
        crashing method. Based on the compression analysis results, create a recovery plan that includes adding
        2 senior developers (emp_dev_15 and emp_eng_10) to critical tasks for 3 impact days, and implementing
        weekend work for 2 impact days. Mark the recovery as high feasibility with daily progress tracking as
        risk mitigation. Finally, update the ms_002 target date to April 12th to reflect the recovery plan.
        Output the total impact days achieved and the cost-benefit ratio from the compression analysis.
        """,
        actions=[
            Action(
                name="get_project_timeline",
                kwargs={"project_id": "proj_mobile_01", "include_dependencies": True},
            ),
            Action(
                name="validate_milestone_readiness", kwargs={"milestone_id": "ms_002"}
            ),
            Action(
                name="check_milestone_float", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="analyze_schedule_compression",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "target_reduction": 10,
                    "compression_type": "crashing",
                },
            ),
            Action(
                name="create_recovery_plan",
                kwargs={
                    "milestone_id": "ms_002",
                    "recovery_actions": [
                        {
                            "type": "crashing",
                            "description": "Add 2 senior developers to critical tasks",
                            "impact_days": 3,
                        },
                        {
                            "type": "crashing",
                            "description": "Implementing weekend work",
                            "impact_days": 2,
                        },
                    ],
                    "additional_resources": ["emp_dev_15", "emp_eng_10"],
                    "risk_mitigation": ["Daily progress tracking"],
                    "feasibility": "high",
                },
            ),
            Action(
                name="update_milestone_dates",
                kwargs={
                    "milestone_id": "ms_002",
                    "new_target_date": "2024-04-12T00:00:00Z",
                },
            ),
        ],
        outputs=["5", "500"],
    ),
    Task(
        annotator="0",
        user_id="schedule_compliance_manager",
        instruction="You are a schedule compliance manager reviewing the Mobile App Launch project. First, get the project timeline for proj_mobile_01 including dependencies. Then check milestone float status to identify schedule risks. The Phase 1 Gate Review (ms_002) needs additional security compliance validation. Add an external dependency for 'Security Audit Services' from SecureTest Systems, expected delivery April 15th, with critical priority and 7 contingency days. The dependency is not yet confirmed. Use Security Team as contact name with email audit@securetest.com, and set notice period to 30 days. Next, analyze schedule compression for a 14-day reduction using fast tracking method. Since the project has consumed some buffer already, update the phase gate buffer consumption by 3 days for milestone ms_002 due to 'Gate review preparation delays'. Create a quarterly schedule baseline named 'Q2 2024 Security Compliance Baseline' with notes stating 'Baseline after security audit dependency integration'. Finally, check the variance against the new baseline. Report the achieved reduction days, total buffer consumed percentage, and number of milestone snapshots in the baseline.",
        actions=[
            Action(
                name="get_project_timeline",
                kwargs={"project_id": "proj_mobile_01", "include_dependencies": True},
            ),
            Action(
                name="check_milestone_float", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="add_external_dependency",
                kwargs={
                    "milestone_id": "ms_002",
                    "dependency_name": "Security Audit Services",
                    "provider": "SecureTest Systems",
                    "expected_delivery_date": "2024-04-15T00:00:00Z",
                    "criticality": "critical",
                    "confirmed": False,
                    "contact_info": {
                        "name": "Security Team",
                        "email": "audit@securetest.com",
                    },
                    "contingency_days": 7,
                    "notice_days": 30,
                },
            ),
            Action(
                name="analyze_schedule_compression",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "target_reduction": 14,
                    "compression_type": "fast_tracking",
                },
            ),
            Action(
                name="update_buffer_consumption",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "buffer_type": "phase_gate",
                    "days_consumed": 3,
                    "milestone_id": "ms_002",
                },
            ),
            Action(
                name="create_schedule_baseline",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "baseline_name": "Q2 2024 Security Compliance Baseline",
                    "baseline_type": "quarterly",
                    "notes": "Baseline after security audit dependency integration",
                },
            ),
            Action(
                name="get_schedule_variance", kwargs={"project_id": "proj_mobile_01"}
            ),
        ],
        outputs=[
            '"achieved_reduction": 13',
            '"consumption_percentage": 20.0',
            '"milestone_count": 2',
        ],
    ),
    Task(
        annotator="0",
        user_id="milestone_compliance_officer",
        instruction="You are a milestone compliance officer for the Mobile App Launch project. Start by getting the timeline for proj_mobile_01 with dependencies included. Then check the variance against the baseline to understand schedule performance. Since the Authentication Module (ms_001) is complete, archive it. Next, create a milestone from template using the 'Standard Product Launch' template (template_001) for a new 'Beta Testing Phase' milestone with target date June 1st, 2024, assigned to emp_qa_02. Update the external dependency status for the delivered Network Infrastructure (ext_003) marking it as 'delivered' with actual delivery April 15th. Since buffer consumption is increasing, check the current milestone float status. Finally, analyze schedule compression for 12 days using fast tracking to recover schedule. Report the number of float days and whether fast tracking is feasible.",
        actions=[
            Action(
                name="get_project_timeline",
                kwargs={"project_id": "proj_mobile_01", "include_dependencies": True},
            ),
            Action(
                name="get_schedule_variance", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="archive_milestone",
                kwargs={"milestone_id": "ms_001"},
            ),
            Action(
                name="create_milestone_from_template",
                kwargs={
                    "template_id": "template_001",
                    "project_id": "proj_mobile_01",
                    "milestone_name": "Beta Testing Phase",
                    "target_date": "2024-06-01T00:00:00Z",
                    "owner_id": "emp_qa_02",
                },
            ),
            Action(
                name="update_external_dependency_status",
                kwargs={
                    "dependency_id": "ext_003",
                    "new_status": "delivered",
                    "actual_delivery_date": "2024-04-15T00:00:00Z",
                },
            ),
            Action(
                name="check_milestone_float", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="analyze_schedule_compression",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "target_reduction": 12,
                    "compression_type": "fast_tracking",
                },
            ),
        ],
        outputs=['"float_days": -2', '"feasible": true'],
    ),
    Task(
        annotator="0",
        user_id="qa_lead_phase_completion",
        instruction="You are a QA lead finalizing the Phase 1 Gate Review for the Mobile App Launch project. First, get the details of milestone ms_002 to understand current status. Then check if ms_002 is ready to proceed by validating its readiness. The team has completed all deliverables, so update ms_002 status to 'completed' with 100% progress and 'green' health, listing all completed deliverables: 'Core features complete', 'Security audit passed', and 'Performance benchmarks met'. Add status notes about successful security review completion. After updating, get the project timeline to see the impact. Since phase 1 is complete, update the dates for the ML Model Training milestone (ms_003) to start May 10th. Check milestone float after the date change. Finally, calculate the critical path for proj_ai_01 to understand schedule impacts. Report the milestone health change, number of completed milestones in mobile project, and total float days for ms_003.",
        actions=[
            Action(name="get_milestone_details", kwargs={"milestone_id": "ms_002"}),
            Action(
                name="validate_milestone_readiness", kwargs={"milestone_id": "ms_002"}
            ),
            Action(
                name="update_milestone_status",
                kwargs={
                    "milestone_id": "ms_002",
                    "new_status": "completed",
                    "progress_percentage": 100,
                    "health": "green",
                    "status_notes": "Successful security review completion",
                    "deliverables_completed": [
                        "Core features complete",
                        "Security audit passed",
                        "Performance benchmarks met",
                    ],
                },
            ),
            Action(
                name="get_project_timeline",
                kwargs={"project_id": "proj_mobile_01", "include_dependencies": False},
            ),
            Action(
                name="update_milestone_dates",
                kwargs={
                    "milestone_id": "ms_003",
                    "new_start_date": "2024-05-10T00:00:00Z",
                },
            ),
            Action(name="check_milestone_float", kwargs={"project_id": "proj_ai_01"}),
            Action(name="calculate_critical_path", kwargs={"project_id": "proj_ai_01"}),
        ],
        outputs=[
            '"health_change": "yellow -> green"',
            '"completed": 2',
            '"float_days": 0',
        ],
    ),
    Task(
        annotator="0",
        user_id="milestone_rebaseline_coordinator",
        instruction="""
        You are coordinating milestone recovery for the Mobile App Launch
        project (proj_mobile_01). First, check the schedule variance against the
        baseline. Validate the Phase 1 Gate Review (ms_002) readiness. Create a
        recovery plan for ms_002 with crashing actions: add 2 senior developers
        for 3 days and authorize weekend work for 2 days, using employees emp_dev_15
        and emp_eng_10 as additional resources. Mark the recovery as high feasibility
        with daily progress tracking as risk mitigation. After creating the recovery
        plan, analyze schedule compression for the project targeting 10 days reduction
        using crashing method. Update the phase gate buffer consumption by 3 days for
        ms_002 due to gate review preparation delays. Report the number of
        readiness issues found, total impact days from the recovery plan, and
        the cost-benefit ratio from compression analysis.
        """,
        actions=[
            Action(
                name="get_schedule_variance", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="validate_milestone_readiness", kwargs={"milestone_id": "ms_002"}
            ),
            Action(
                name="create_recovery_plan",
                kwargs={
                    "milestone_id": "ms_002",
                    "recovery_actions": [
                        {
                            "type": "crashing",
                            "description": "Add 2 senior developers for 3 days",
                            "impact_days": 3,
                        },
                        {
                            "type": "crashing",
                            "description": "Authorize weekend work for 2 days",
                            "impact_days": 2,
                        },
                    ],
                    "additional_resources": ["emp_dev_15", "emp_eng_10"],
                    "risk_mitigation": ["Daily progress tracking"],
                    "feasibility": "high",
                },
            ),
            Action(
                name="analyze_schedule_compression",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "target_reduction": 10,
                    "compression_type": "crashing",
                },
            ),
            Action(
                name="update_buffer_consumption",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "buffer_type": "phase_gate",
                    "days_consumed": 3,
                    "milestone_id": "ms_002",
                },
            ),
        ],
        outputs=["1", "5", "500"],
    ),
    Task(
        annotator="0",
        user_id="ai_project_dependency_manager",
        instruction="""
        You are managing dependencies for the AI Platform project (proj_ai_01).
        First check the milestone details for the ML Model Training Complete
        milestone (ms_003). Then get the project timeline to see all milestones.
        Create a milestone with the ID "ms_XXX", from template_004 for the
        proj_ai_01, with the name 'AI Infrastructure', with
        '2024-06-25T00:00:00Z' as target date and emp_data_01 as owner. Create a
        milestone dependency where ms_XXX must complete before ms_003 can start,
        with a 7-day lag and make it mandatory. Include notes that
        authentication is required for secure model access. After creating the
        dependency, calculate the critical path for the AI project. Check the
        milestone float status to see the impact. Finally, validate the
        readiness of ms_003 to see if the new dependency affects it. Report the
        project ID from the dependency creation result and the float days for
        ms_003.
        """,
        actions=[
            Action(name="get_milestone_details", kwargs={"milestone_id": "ms_003"}),
            Action(
                name="get_project_timeline",
                kwargs={"project_id": "proj_ai_01", "include_dependencies": False},
            ),
            Action(
                name="create_milestone_from_template",
                kwargs={
                    "milestone_id": "ms_XXX",
                    "template_id": "template_004",
                    "project_id": "proj_ai_01",
                    "milestone_name": "AI Infrastructure",
                    "target_date": "2024-06-25T00:00:00Z",
                    "owner_id": "emp_data_01",
                },
            ),
            Action(
                name="create_milestone_dependency",
                kwargs={
                    "predecessor_id": "ms_XXX",
                    "successor_id": "ms_003",
                    "dependency_type": "finish_to_start",
                    "lag_days": 7,
                    "is_mandatory": True,
                    "notes": "authentication is required for secure model access",
                },
            ),
            Action(name="calculate_critical_path", kwargs={"project_id": "proj_ai_01"}),
            Action(name="check_milestone_float", kwargs={"project_id": "proj_ai_01"}),
            Action(
                name="validate_milestone_readiness", kwargs={"milestone_id": "ms_003"}
            ),
        ],
        outputs=[
            '"project_id": "proj_ai_01"',
            '"float_days": 5',
        ],
    ),
    Task(
        annotator="0",
        user_id="mobile_project_critical_path_optimizer",
        instruction="""
        You are optimizing the critical path for the Mobile App Launch project (proj_mobile_01). First get the milestone
        details for ms_002 (Phase 1 Gate Review). Then calculate the critical path for the project. Check the milestone
        float to see which milestones have the least slack. If ms_002 has negative float, update its dates by extending
        the target date by 5 days to April 20th due to critical path pressure. Create a dependency between ms_001 and
        ms_002 if not already existing, with 2-day lag, making it mandatory and set type as 'finish_to_start'.
        After these changes, recalculate the
        critical path. Finally, validate the readiness of ms_002. Report the float days for ms_002 from the initial
        float check, the critical milestones count from the final critical path calculation, and the is_ready status
        from the validation.
        """,
        actions=[
            Action(name="get_milestone_details", kwargs={"milestone_id": "ms_002"}),
            Action(
                name="calculate_critical_path", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="check_milestone_float", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="update_milestone_dates",
                kwargs={
                    "milestone_id": "ms_002",
                    "new_target_date": "2024-04-20T00:00:00Z",
                },
            ),
            Action(
                name="create_milestone_dependency",
                kwargs={
                    "predecessor_id": "ms_001",
                    "successor_id": "ms_002",
                    "dependency_type": "finish_to_start",
                    "lag_days": 2,
                    "is_mandatory": True,
                },
            ),
            Action(
                name="calculate_critical_path", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="validate_milestone_readiness", kwargs={"milestone_id": "ms_002"}
            ),
        ],
        outputs=[
            '"float_days": -2',
            '"critical_milestones_count": 1',
            '"is_ready": false',
        ],
    ),
    Task(
        annotator="0",
        user_id="mobile_project_path_coordinator",
        instruction="You are coordinating the critical path for the Mobile App Launch project (proj_mobile_01). First calculate the critical path for the project. Check milestone float to identify schedule risks. Then get the milestone details for ms_001 (Authentication Module). Since ms_001 is complete, update its status to completed with 100% progress and green health, with status notes 'All authentication features implemented successfully', listing the completed deliverables: OAuth2 integration, User session management, and Security documentation. After updating, recalculate the critical path to see changes. Finally, create a gate review for ms_002 with review date April 10, 2024, marking all criteria as pass except 'No critical security issues' as fail, with reviewers emp_arch_01, emp_sec_dev_01, and emp_pm_03. Add review notes 'Minor security issues need resolution within 5 days'. Report the critical milestones count from the first calculation, the health change from the status update, and the overall decision from the gate review.",
        actions=[
            Action(
                name="calculate_critical_path", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="check_milestone_float", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(name="get_milestone_details", kwargs={"milestone_id": "ms_001"}),
            Action(
                name="update_milestone_status",
                kwargs={
                    "milestone_id": "ms_001",
                    "new_status": "completed",
                    "progress_percentage": 100,
                    "health": "green",
                    "status_notes": "All authentication features implemented successfully",
                    "deliverables_completed": [
                        "OAuth2 integration",
                        "User session management",
                        "Security documentation",
                    ],
                },
            ),
            Action(
                name="calculate_critical_path", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="create_gate_review",
                kwargs={
                    "milestone_id": "ms_002",
                    "review_date": "2024-04-10T00:00:00Z",
                    "criteria_results": {
                        "Code coverage > 80%": "pass",
                        "No critical security issues": "fail",
                        "Performance meets SLA": "pass",
                        "Architecture review approved": "pass",
                    },
                    "reviewers": ["emp_arch_01", "emp_sec_dev_01", "emp_pm_03"],
                    "review_notes": "Minor security issues need resolution within 5 days",
                },
            ),
        ],
        outputs=[
            '"critical_milestones_count": 1',
            '"health_change": "green -> green"',
            '"overall_decision": "fail"',
        ],
    ),
    Task(
        annotator="0",
        user_id="ai_platform_baseline_coordinator",
        instruction="You are establishing a new baseline for the AI Platform project (proj_ai_01). First get the project timeline to see current milestones. Check the schedule variance to understand if a baseline exists. Since the project only has an initial baseline, create a new quarterly baseline called 'Q2 2024 AI Platform Baseline' with baseline type quarterly, including notes about ML model progress. Then get the schedule variance again to compare against the new baseline. Check milestone float to assess schedule health. Finally, analyze schedule compression for 20 days using fast tracking to understand schedule flexibility. Report the total milestones from the timeline, the milestone count from the baseline creation, and the achieved reduction from compression analysis.",
        actions=[
            Action(
                name="get_project_timeline",
                kwargs={"project_id": "proj_ai_01", "include_dependencies": True},
            ),
            Action(name="get_schedule_variance", kwargs={"project_id": "proj_ai_01"}),
            Action(
                name="create_schedule_baseline",
                kwargs={
                    "project_id": "proj_ai_01",
                    "baseline_name": "Q2 2024 AI Platform Baseline",
                    "baseline_type": "quarterly",
                    "notes": "ML model progress",
                },
            ),
            Action(name="get_schedule_variance", kwargs={"project_id": "proj_ai_01"}),
            Action(name="check_milestone_float", kwargs={"project_id": "proj_ai_01"}),
            Action(
                name="analyze_schedule_compression",
                kwargs={
                    "project_id": "proj_ai_01",
                    "target_reduction": 20,
                    "compression_type": "fast_tracking",
                },
            ),
        ],
        outputs=[
            '"total_milestones": 1',
            '"milestone_count": 1',
            '"achieved_reduction": 18',
        ],
    ),
    Task(
        annotator="0",
        user_id="ai_platform_schedule_adjuster",
        instruction="You are adjusting the schedule for the AI Platform project (proj_ai_01). First get the milestone details for ms_003 (ML Model Training). Check the current milestone float status for the project. Since GPU infrastructure availability has improved, update ms_003 dates by moving the start date to April 25, 2024 and target date to June 20, 2024. After the date change, check milestone float again to see the impact. Analyze schedule compression for 12 days using crashing to identify further optimization opportunities. Finally, update the project buffer consumption by 5 days for ms_003 due to the schedule acceleration. Report the float days for ms_003 before the date change, the number of impacted milestones from the date update, and the consumption percentage from the buffer update.",
        actions=[
            Action(name="get_milestone_details", kwargs={"milestone_id": "ms_003"}),
            Action(name="check_milestone_float", kwargs={"project_id": "proj_ai_01"}),
            Action(
                name="update_milestone_dates",
                kwargs={
                    "milestone_id": "ms_003",
                    "new_start_date": "2024-04-25T00:00:00Z",
                    "new_target_date": "2024-06-20T00:00:00Z",
                },
            ),
            Action(name="check_milestone_float", kwargs={"project_id": "proj_ai_01"}),
            Action(
                name="analyze_schedule_compression",
                kwargs={
                    "project_id": "proj_ai_01",
                    "target_reduction": 12,
                    "compression_type": "crashing",
                },
            ),
            Action(
                name="update_buffer_consumption",
                kwargs={
                    "project_id": "proj_ai_01",
                    "buffer_type": "project",
                    "days_consumed": 5,
                    "milestone_id": "ms_003",
                },
            ),
        ],
        outputs=[
            '"float_days": 5',
            '"impacted_count": 0',
            '"consumption_percentage": 11.1',
        ],
    ),
    Task(
        annotator="0",
        user_id="mobile_gate_review_coordinator",
        instruction="You are coordinating gate reviews for the Mobile App Launch project (proj_mobile_01). First validate the readiness of ms_002 (Phase 1 Gate Review). Get the milestone dependencies to understand prerequisites. Check if there are any delayed milestones in the project. Create a gate review for ms_002 with review date April 10, 2024, where Code coverage > 80% passes, Performance meets SLA passes, Architecture review approved passes, but No critical security issues fails. Use reviewers emp_arch_01, emp_sec_dev_01, and emp_pm_03 with conditional pass decision. Include action items: Fix SQL injection vulnerability and Update security documentation. Note that minor security issues need resolution within 5 days. After the review, get milestone details for ms_002 to see the status. Finally, if there were readiness issues, create a recovery plan with crashing actions: security fixes for 2 impact days and documentation updates for 1 impact day, using emp_sec_dev_02 as additional resource with high feasibility and include security code review and automated vulnerability scanning as risk mitigation. Tell me the readiness score, the decision from the gate review, and the days recovered from the recovery plan.",
        actions=[
            Action(
                name="validate_milestone_readiness", kwargs={"milestone_id": "ms_002"}
            ),
            Action(
                name="get_milestone_dependencies", kwargs={"milestone_id": "ms_002"}
            ),
            Action(
                name="get_delayed_milestones",
                kwargs={"project_id": "proj_mobile_01", "include_recovery_plans": True},
            ),
            Action(
                name="create_gate_review",
                kwargs={
                    "milestone_id": "ms_002",
                    "review_date": "2024-04-10T00:00:00Z",
                    "criteria_results": {
                        "Code coverage > 80%": "pass",
                        "No critical security issues": "fail",
                        "Performance meets SLA": "pass",
                        "Architecture review approved": "pass",
                    },
                    "reviewers": ["emp_arch_01", "emp_sec_dev_01", "emp_pm_03"],
                    "action_items": [
                        "Fix SQL injection vulnerability",
                        "Update security documentation",
                    ],
                    "review_notes": "Minor security issues need resolution within 5 days",
                    "conditional_pass": True,
                },
            ),
            Action(name="get_milestone_details", kwargs={"milestone_id": "ms_002"}),
            Action(
                name="create_recovery_plan",
                kwargs={
                    "milestone_id": "ms_002",
                    "recovery_actions": [
                        {
                            "type": "crashing",
                            "description": "security fixes",
                            "impact_days": 2,
                        },
                        {
                            "type": "crashing",
                            "description": "documentation updates",
                            "impact_days": 1,
                        },
                    ],
                    "additional_resources": ["emp_sec_dev_02"],
                    "risk_mitigation": [
                        "security code review",
                        "automated vulnerability scanning",
                    ],
                    "feasibility": "high",
                },
            ),
        ],
        outputs=[
            '"readiness_score": 75',
            '"decision": "conditional_pass"',
            '"days_recovered": 3',
        ],
    ),
    Task(
        annotator="0",
        user_id="ai_platform_vendor_coordinator",
        instruction="""
        You are managing external dependencies for the AI Platform project (proj_ai_01). First get the milestone
        details for ms_003 (ML Model Training). Check the project timeline to understand the schedule. Add an external
        dependency for Cloud GPU Infrastructure from AWS with expected delivery April 20, 2024, marking it as critical
        with 5 contingency days and requiring 30 days notice (use 'ext_26845ca5' as dependency ID.
        Set it as unconfirmed with contact info: GPU Support Team at gpu-support@aws.com. After adding the dependency,
        validate milestone readiness for ms_003 to see the impact. Update the external dependency status to confirmed
        once AWS confirms availability. Finally, check milestone float to assess schedule risk. Report the milestone
        type from the initial details, the dependency ID created, and whether ms_003 is ready after adding the
        dependency.
        """,
        actions=[
            Action(name="get_milestone_details", kwargs={"milestone_id": "ms_003"}),
            Action(
                name="get_project_timeline",
                kwargs={"project_id": "proj_ai_01", "include_dependencies": False},
            ),
            Action(
                name="add_external_dependency",
                kwargs={
                    "dependency_id": "ext_26845ca5",
                    "milestone_id": "ms_003",
                    "dependency_name": "Cloud GPU Infrastructure",
                    "provider": "AWS",
                    "expected_delivery_date": "2024-04-20T00:00:00Z",
                    "criticality": "critical",
                    "confirmed": False,
                    "contact_info": {
                        "name": "GPU Support Team",
                        "email": "gpu-support@aws.com",
                    },
                    "contingency_days": 5,
                    "notice_days": 30,
                },
            ),
            Action(
                name="validate_milestone_readiness", kwargs={"milestone_id": "ms_003"}
            ),
            Action(
                name="update_external_dependency_status",
                kwargs={"dependency_id": "ext_26845ca5", "new_status": "confirmed"},
            ),
            Action(name="check_milestone_float", kwargs={"project_id": "proj_ai_01"}),
        ],
        outputs=[
            '"milestone_type": "phase_gate"',
            '"dependency_id": "ext_',
            '"is_ready": false',
        ],
    ),
    Task(
        annotator="0",
        user_id="mobile_project_recovery_specialist",
        instruction="You are a recovery specialist for the Mobile App Launch project (proj_mobile_01). First check milestone float to identify schedule pressures. Get delayed milestones with recovery plans included to see existing issues. Analyze schedule compression for 14 days using fast tracking to understand options. Since ms_002 (Phase 1 Gate Review) is showing negative float, validate its readiness. Create a recovery plan for ms_002 with mixed actions: fast tracking UI/UX work for 4 impact days, crashing backend development for 3 impact days, and resource addition of senior architect for 2 impact days. Use emp_arch_01 and emp_dev_15 as additional resources with risk mitigation including hourly progress updates and dedicated war room. Set feasibility as medium. After creating the plan, update the phase gate buffer consumption by 2 days for ms_002 citing recovery plan implementation. Report the number of delayed milestones initially found, whether the recovery was created within 48 hours, and the total buffer consumed percentage.",
        actions=[
            Action(
                name="check_milestone_float", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="get_delayed_milestones",
                kwargs={"project_id": "proj_mobile_01", "include_recovery_plans": True},
            ),
            Action(
                name="analyze_schedule_compression",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "target_reduction": 14,
                    "compression_type": "fast_tracking",
                },
            ),
            Action(
                name="validate_milestone_readiness", kwargs={"milestone_id": "ms_002"}
            ),
            Action(
                name="create_recovery_plan",
                kwargs={
                    "milestone_id": "ms_002",
                    "recovery_actions": [
                        {
                            "type": "fast_tracking",
                            "description": "fast tracking UI/UX work",
                            "impact_days": 4,
                        },
                        {
                            "type": "crashing",
                            "description": "crashing backend development",
                            "impact_days": 3,
                        },
                        {
                            "type": "resource_addition",
                            "description": "resource addition of senior architect",
                            "impact_days": 2,
                        },
                    ],
                    "additional_resources": ["emp_arch_01", "emp_dev_15"],
                    "risk_mitigation": [
                        "hourly progress updates",
                        "dedicated war room",
                    ],
                    "feasibility": "medium",
                },
            ),
            Action(
                name="update_buffer_consumption",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "buffer_type": "phase_gate",
                    "days_consumed": 2,
                    "milestone_id": "ms_002",
                },
            ),
        ],
        outputs=[
            '"delayed_count": 1',
            '"created_within_48hrs": false',
            '"consumption_percentage": 16.7',
        ],
    ),
    Task(
        annotator="0",
        user_id="mobile_compression_strategy_analyst",
        instruction="""
        You are analyzing compression strategies for the Mobile App Launch project (proj_mobile_01). First check
        milestone float to identify schedule pressures. Get the project timeline to understand the current schedule.
        Analyze schedule compression for 12 days using crashing to evaluate the cost approach. Then analyze compression
        for the same 12 days using fast tracking to compare risk vs cost. Update ms_002 dates by moving the target
        date earlier by 7 days to April 8, 2024. After the date change, check milestone float again to see the
        impact. Finally, validate the readiness of ms_002 after the schedule changes. Report the number of milestones
        with negative float initially, the achieved reduction from crashing analysis, and the readiness score after
        schedule changes.
        """,
        actions=[
            Action(
                name="check_milestone_float", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="get_project_timeline",
                kwargs={"project_id": "proj_mobile_01", "include_dependencies": True},
            ),
            Action(
                name="analyze_schedule_compression",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "target_reduction": 12,
                    "compression_type": "crashing",
                },
            ),
            Action(
                name="analyze_schedule_compression",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "target_reduction": 12,
                    "compression_type": "fast_tracking",
                },
            ),
            Action(
                name="update_milestone_dates",
                kwargs={
                    "milestone_id": "ms_002",
                    "new_target_date": "2024-04-08T00:00:00Z",
                },
            ),
            Action(
                name="check_milestone_float", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="validate_milestone_readiness", kwargs={"milestone_id": "ms_002"}
            ),
        ],
        outputs=[
            '"negative_float": 1',
            '"achieved_reduction": 8',
            '"readiness_score": 75',
        ],
    ),
    Task(
        annotator="0",
        user_id="mobile_buffer_management_coordinator",
        instruction="You are managing buffer consumption for the Mobile App Launch project (proj_mobile_01). First get the schedule variance to understand baseline performance. Check milestone float to identify which milestones are consuming float. Since ms_001 authentication work required extra testing, update the project buffer consumption by 3 days for ms_001 citing additional security testing requirements. Then update the phase gate buffer by 2 days for ms_002 due to gate review preparation complexity. Check if any delayed milestones exist in the project. If there are delayed milestones, also update the integration buffer by 1 day for ms_002 citing interface testing delays. After all buffer updates, analyze schedule compression for 10 days using crashing to understand recovery options. Finally, check milestone float again to see the updated float status. Report the variance percentage for any delayed milestone from schedule variance, the risk review required status from the final buffer update, and the affected milestones count from compression analysis.",
        actions=[
            Action(
                name="get_schedule_variance", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="check_milestone_float", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="update_buffer_consumption",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "buffer_type": "project",
                    "days_consumed": 3,
                    "milestone_id": "ms_001",
                },
            ),
            Action(
                name="update_buffer_consumption",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "buffer_type": "phase_gate",
                    "days_consumed": 2,
                    "milestone_id": "ms_002",
                },
            ),
            Action(
                name="get_delayed_milestones",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "include_recovery_plans": False,
                },
            ),
            Action(
                name="update_buffer_consumption",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "buffer_type": "integration",
                    "days_consumed": 1,
                    "milestone_id": "ms_002",
                },
            ),
            Action(
                name="analyze_schedule_compression",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "target_reduction": 10,
                    "compression_type": "crashing",
                },
            ),
            Action(
                name="check_milestone_float", kwargs={"project_id": "proj_mobile_01"}
            ),
        ],
        outputs=[
            '"variance_percentage": 0.0',
            '"risk_review_required": false',
            '"affected_milestones": 2',
        ],
    ),
    Task(
        annotator="0",
        user_id="ai_platform_float_optimization_specialist",
        instruction="""
        You are optimizing float management for the AI Platform project (proj_ai_01). First check milestone float
        to understand the current schedule health. Get the project timeline to see milestone details. If ms_003 has
        comfortable float (5 days or more), analyze schedule compression for 10 days using crashing to identify
        opportunities. Based on the float analysis, if there are no milestones with negative float, create a new
        milestone from template_004 (Infrastructure Migration) called 'AI Infrastructure Scaling' with target date
        July 30, 2024, assigned to emp_devops_02. After creating the milestone, check milestone float again to see
        the impact. If the new milestone has more than 10 days float, update buffer consumption by 4 days for project
        buffer citing proactive schedule optimization. Finally, get delayed milestones to confirm no new delays were
        introduced. Report the initial comfortable float count, the float status of the new milestone created, and
        the total delayed milestones at the end.
        """,
        actions=[
            Action(name="check_milestone_float", kwargs={"project_id": "proj_ai_01"}),
            Action(
                name="get_project_timeline",
                kwargs={"project_id": "proj_ai_01", "include_dependencies": False},
            ),
            Action(
                name="analyze_schedule_compression",
                kwargs={
                    "project_id": "proj_ai_01",
                    "target_reduction": 10,
                    "compression_type": "crashing",
                },
            ),
            Action(
                name="create_milestone_from_template",
                kwargs={
                    "template_id": "template_004",
                    "project_id": "proj_ai_01",
                    "milestone_name": "AI Infrastructure Scaling",
                    "target_date": "2024-07-30T00:00:00Z",
                    "owner_id": "emp_devops_02",
                },
            ),
            Action(name="check_milestone_float", kwargs={"project_id": "proj_ai_01"}),
            Action(
                name="update_buffer_consumption",
                kwargs={
                    "project_id": "proj_ai_01",
                    "buffer_type": "project",
                    "days_consumed": 4,
                },
            ),
            Action(
                name="get_delayed_milestones",
                kwargs={"project_id": "proj_ai_01", "include_recovery_plans": False},
            ),
        ],
        outputs=[
            '"comfortable_float": 0',
            '"float_status": "comfortable"',
            '"delayed_count": 0',
        ],
    ),
    Task(
        annotator="0",
        user_id="mobile_resource_conflict_resolver",
        instruction="""
        You are resolving resource conflicts for the Mobile App Launch project (proj_mobile_01). First check milestone
        float to identify critical paths. Get the project timeline to understand resource needs. Apply resource
        leveling with constraints: Senior Developer limited to 2 and React Native Developer limited to 1, using
        critical path priority method. Based on the leveling results, update
        the milestone dates for any shifted milestone by adding 5 days to ms_002's target date to April 20, 2024,
        citing resource conflict resolution. After any date changes, analyze schedule compression for 8 days using
        fast tracking to recover time. Check milestone float again after all changes. Finally,
        create a recovery plan for ms_002 with resource addition: bring in contractor
        for 4 impact days and overtime authorization for 3 impact days, using emp_dev_15 as additional resource with
        medium feasibility. Include risk mitigation strategies in the recovery plan. Report the number of conflicts
        found from leveling, whether approval is required for the extension, and the risk multiplier from compression
        analysis.
        """,
        actions=[
            Action(
                name="check_milestone_float", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="get_project_timeline",
                kwargs={"project_id": "proj_mobile_01", "include_dependencies": True},
            ),
            Action(
                name="apply_resource_leveling",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "resource_constraints": {
                        "Senior Developer": 2,
                        "React Native Developer": 1,
                    },
                    "priority_method": "critical_path",
                },
            ),
            Action(
                name="update_milestone_dates",
                kwargs={
                    "milestone_id": "ms_002",
                    "new_target_date": "2024-04-20T00:00:00Z",
                },
            ),
            Action(
                name="analyze_schedule_compression",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "target_reduction": 8,
                    "compression_type": "fast_tracking",
                },
            ),
            Action(
                name="check_milestone_float", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="create_recovery_plan",
                kwargs={
                    "milestone_id": "ms_002",
                    "recovery_actions": [
                        {
                            "type": "resource_addition",
                            "description": "Bring in contractor",
                            "impact_days": 4,
                        },
                        {
                            "type": "crashing",
                            "description": "Overtime authorization",
                            "impact_days": 3,
                        },
                    ],
                    "additional_resources": ["emp_dev_15"],
                    "risk_mitigation": ["Risk mitigation strategies"],
                    "feasibility": "medium",
                },
            ),
        ],
        outputs=[
            '"conflicts_found": 0',
            '"requires_approval": false',
            '"risk_multiplier": 2.0',
        ],
    ),
    Task(
        annotator="0",
        user_id="mobile_timeline_comprehensive_analyst",
        instruction="""
        You are analyzing the comprehensive timeline for the Mobile App Launch project (proj_mobile_01). First get the
        project timeline with dependencies to understand the full schedule structure. Check the schedule variance to
        see performance against baseline. Get the project timeline again without dependencies for a cleaner view.
        Based on the timeline analysis, validate milestone readiness for ms_001. If ms_001 is ready, update its
        status to completed with 100% progress and green health, noting 'Milestone completed successfully', listing
        completed deliverables: OAuth2 integration, User session management, and Security documentation. After
        the status update, get delayed milestones to see if any schedule issues exist. Create a gate review for milestone
        ms_002 on April 10 2024 with reviewers emp_arch_01 and emp_pm_03. The criteria results were 'Code coverage
        > 80%' pass, 'No critical security issues' pass, 'Performance meets SLA' fail,
        and 'Architecture review approved' pass. Add the note 'Performance issues need resolution'. Finally, check
        milestone float to assess the overall schedule health. Report the number of completed milestones from
        the initial timeline metrics, the health change from the status update, and the zero float count from
        the final float check.
        """,
        actions=[
            Action(
                name="get_project_timeline",
                kwargs={"project_id": "proj_mobile_01", "include_dependencies": True},
            ),
            Action(
                name="get_schedule_variance", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="get_project_timeline",
                kwargs={"project_id": "proj_mobile_01", "include_dependencies": False},
            ),
            Action(
                name="validate_milestone_readiness", kwargs={"milestone_id": "ms_001"}
            ),
            Action(
                name="update_milestone_status",
                kwargs={
                    "milestone_id": "ms_001",
                    "new_status": "completed",
                    "progress_percentage": 100,
                    "health": "green",
                    "status_notes": "Milestone completed successfully",
                    "deliverables_completed": [
                        "OAuth2 integration",
                        "User session management",
                        "Security documentation",
                    ],
                },
            ),
            Action(
                name="get_delayed_milestones",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "include_recovery_plans": False,
                },
            ),
            Action(
                name="create_gate_review",
                kwargs={
                    "milestone_id": "ms_002",
                    "review_date": "2024-04-10T00:00:00Z",
                    "criteria_results": {
                        "Code coverage > 80%": "pass",
                        "No critical security issues": "pass",
                        "Performance meets SLA": "fail",
                        "Architecture review approved": "pass",
                    },
                    "reviewers": ["emp_arch_01", "emp_pm_03"],
                    "review_notes": "Performance issues need resolution",
                },
            ),
            Action(
                name="check_milestone_float", kwargs={"project_id": "proj_mobile_01"}
            ),
        ],
        outputs=[
            '"completed": 1',
            '"health_change": "green -> green"',
            '"zero_float": 1',
        ],
    ),
    Task(
        annotator="0",
        user_id="ai_platform_vendor_delivery_manager",
        instruction="""
        You are managing external vendor deliveries for the AI Platform project (proj_ai_01). First get milestone
        details for ms_003 to understand its requirements. Check if there are any external dependencies by getting
        the project timeline. Update the status of external dependency ext_001 (Cloud GPU Infrastructure) to delayed.
        After marking it delayed, validate the readiness of ms_003 to see the impact. Due to the delay, add a new
        external dependency (use ext_002_ms_003 as dependency ID) for Alternative GPU Provider from Google Cloud with
        expected delivery April 25, 2024,
        marking it as high criticality with 3 contingency days and 15 days notice period. Contact should be Cloud
        Support at support@gcp.com. After adding the backup dependency, update the original dependency ext_001 status
        to cancelled. Check milestone float to assess schedule impact. Finally, update the newly created external
        dependency (use the dependency_id from the add_external_dependency output) to confirmed status. Report the
        milestone health from initial details, the readiness status after first delay, and the criticality of the
        new dependency added.
        """,
        actions=[
            Action(name="get_milestone_details", kwargs={"milestone_id": "ms_003"}),
            Action(
                name="get_project_timeline",
                kwargs={"project_id": "proj_ai_01", "include_dependencies": True},
            ),
            Action(
                name="update_external_dependency_status",
                kwargs={"dependency_id": "ext_001", "new_status": "delayed"},
            ),
            Action(
                name="validate_milestone_readiness", kwargs={"milestone_id": "ms_003"}
            ),
            Action(
                name="add_external_dependency",
                kwargs={
                    "milestone_id": "ms_003",
                    "dependency_id": "ext_002_ms_003",
                    "dependency_name": "Alternative GPU Provider",
                    "provider": "Google Cloud",
                    "expected_delivery_date": "2024-04-25T00:00:00Z",
                    "criticality": "high",
                    "confirmed": False,
                    "contact_info": {
                        "name": "Cloud Support",
                        "email": "support@gcp.com",
                    },
                    "contingency_days": 3,
                    "notice_days": 15,
                },
            ),
            Action(
                name="update_external_dependency_status",
                kwargs={"dependency_id": "ext_001", "new_status": "cancelled"},
            ),
            Action(name="check_milestone_float", kwargs={"project_id": "proj_ai_01"}),
            Action(
                name="update_external_dependency_status",
                kwargs={"dependency_id": "ext_002_ms_003", "new_status": "confirmed"},
            ),
        ],
        outputs=['"health": "green"', '"is_ready": false', '"criticality": "high"'],
    ),
    Task(
        annotator="0",
        user_id="enterprise_milestone_template_coordinator",
        instruction="""
        You are coordinating milestone creation for the Enterprise Platform project (proj_enterprise_01). First get
        the project timeline to see existing milestones (exclude dependencies). Check milestone float to identify schedule
        gaps. Create a milestone (use ms_XXY as ID) from template_007 (Architecture Review Gate) called 'Enterprise Architecture Deep
        Dive' with target date May 25, 2024, assigned to emp_arch_01. After creating this milestone,
        also create another milestone (use ms_XYZ as ID) from template_005 (Data Privacy Compliance) called 'GDPR Compliance Review' with
        target date June 10, 2024, assigned to emp_analyst_01. Get milestone details for the first created milestone
        to verify its properties. Check milestone float again to see the impact of new milestones. Report the milestone type
        of ms_XXY, and the critical path count and total milestones from the final float check.
        """,
        actions=[
            Action(
                name="get_project_timeline",
                kwargs={
                    "project_id": "proj_enterprise_01",
                    "include_dependencies": False,
                },
            ),
            Action(
                name="check_milestone_float",
                kwargs={"project_id": "proj_enterprise_01"},
            ),
            Action(
                name="create_milestone_from_template",
                kwargs={
                    "milestone_id": "ms_XXY",
                    "template_id": "template_007",
                    "project_id": "proj_enterprise_01",
                    "milestone_name": "Enterprise Architecture Deep Dive",
                    "target_date": "2024-05-25T00:00:00Z",
                    "owner_id": "emp_arch_01",
                },
            ),
            Action(
                name="create_milestone_from_template",
                kwargs={
                    "milestone_id": "ms_XYZ",
                    "template_id": "template_005",
                    "project_id": "proj_enterprise_01",
                    "milestone_name": "GDPR Compliance Review",
                    "target_date": "2024-06-10T00:00:00Z",
                    "owner_id": "emp_analyst_01",
                },
            ),
            Action(
                name="get_milestone_details",
                kwargs={"milestone_id": "ms_XXY"},
            ),
            Action(
                name="check_milestone_float",
                kwargs={"project_id": "proj_enterprise_01"},
            ),
        ],
        outputs=[
            '"milestone_type": "phase_gate"',
            '"total_milestones": 2',
            '"critical_path_count": 1',
        ],
    ),
    Task(
        annotator="0",
        user_id="mobile_project_cleanup_coordinator",
        instruction="""
        You are performing milestone cleanup for the Mobile App Launch project (proj_mobile_01). First get the
        project timeline to see all milestones. Check milestone details for ms_001 (Authentication Module) to verify
        its status. Since ms_001 is complete, archive it. After archiving, get the project timeline again to confirm
        it's removed from active milestones. Check if there are any delayed milestones that need attention. Create a
        new milestone from template_006 (MVP Release) called 'Mobile App Beta Release' with target date May 15, 2024,
        assigned to emp_pm_03 to replace the archived milestone. After creating the new milestone, check milestone
        float to assess schedule health. Finally, analyze schedule
        compression for 7 days using crashing. Report the actual completion date of the archived milestone, the
        total milestones after archiving, and whether the new milestone is a critical path candidate.
        """,
        actions=[
            Action(
                name="get_project_timeline",
                kwargs={"project_id": "proj_mobile_01", "include_dependencies": False},
            ),
            Action(name="get_milestone_details", kwargs={"milestone_id": "ms_001"}),
            Action(
                name="archive_milestone",
                kwargs={"milestone_id": "ms_001"},
            ),
            Action(
                name="get_project_timeline",
                kwargs={"project_id": "proj_mobile_01", "include_dependencies": False},
            ),
            Action(
                name="get_delayed_milestones",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "include_recovery_plans": False,
                },
            ),
            Action(
                name="create_milestone_from_template",
                kwargs={
                    "template_id": "template_006",
                    "project_id": "proj_mobile_01",
                    "milestone_name": "Mobile App Beta Release",
                    "target_date": "2024-05-15T00:00:00Z",
                    "owner_id": "emp_pm_03",
                },
            ),
            Action(
                name="check_milestone_float", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="analyze_schedule_compression",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "target_reduction": 7,
                    "compression_type": "crashing",
                },
            ),
        ],
        outputs=[
            '"actual_completion_date": "2024-03-28T00:00:00Z"',
            '"total_milestones": 1',
            '"is_critical_path": true',
        ],
    ),
    Task(
        annotator="0",
        user_id="mobile_delay_mitigation_coordinator",
        instruction="""
        You are coordinating delay mitigation for the Mobile App Launch project (proj_mobile_01). First get delayed
        milestones with recovery plans included to understand current issues. Check the schedule variance to see how
        far off baseline we are. If there are any delayed milestones, validate the readiness of the most critical one
        (ms_002). Based on the delays found, analyze schedule
        compression for 15 days using crashing. Create a gate
        review for ms_002 with review date April 8, 2024, set 'pass' to 'Expedite progress' as criteria results,
        also set the review notes as 'To expedite progress', and set the
        reviewers emp_arch_01 and emp_pm_03. After the review, update the project buffer consumption by 5 days for
        ms_002 citing delay recovery efforts. Finally, get delayed milestones again without recovery plans to see
        the current status. Report the initial critical delays count, whether ms_002 has a recovery plan, and the
        final delayed count.
        """,
        actions=[
            Action(
                name="get_delayed_milestones",
                kwargs={"project_id": "proj_mobile_01", "include_recovery_plans": True},
            ),
            Action(
                name="get_schedule_variance", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="validate_milestone_readiness", kwargs={"milestone_id": "ms_002"}
            ),
            Action(
                name="analyze_schedule_compression",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "target_reduction": 15,
                    "compression_type": "crashing",
                },
            ),
            Action(
                name="create_gate_review",
                kwargs={
                    "milestone_id": "ms_002",
                    "review_date": "2024-04-08T00:00:00Z",
                    "reviewers": ["emp_arch_01", "emp_pm_03"],
                    "review_notes": "To expedite progress",
                    "criteria_results": {
                        "Expedite progress": "pass"
                    }
                },
            ),
            Action(
                name="update_buffer_consumption",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "buffer_type": "project",
                    "days_consumed": 5,
                    "milestone_id": "ms_002",
                },
            ),
            Action(
                name="get_delayed_milestones",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "include_recovery_plans": False,
                },
            ),
        ],
        outputs=[
            '"critical_delays": 1',
            '"has_recovery_plan": true',
            '"delayed_count": 1',
        ],
    ),
    Task(
        annotator="0",
        user_id="mobile_readiness_assurance_manager",
        instruction="""
        You are ensuring milestone readiness for the Mobile App Launch project (proj_mobile_01). First validate the
        readiness of ms_002 (Phase 1 Gate Review). Get milestone details for ms_002 to understand its requirements.
        Based on the readiness validation, if the readiness score is 75 or below, check milestone dependencies to identify
        blocking predecessors. Update ms_001 status to completed with 100% progress
        and green health, noting all deliverables completed: OAuth2 integration, User session management, and Security
        documentation. After status updates, validate ms_002 readiness again to see improvements. If external
        dependencies are an issue, add an external dependency for Security Audit Services from SecureTest Systems with
        expected delivery April 10, 2024, marking it as high criticality with 3 contingency days, confirmed as true,
        with contact info for Security Team at audit@securetest.com, and 30 notice days. Finally, if the readiness
        score is still below 100, create a gate review for ms_002 scheduled for April 10, 2024, with all criteria
        passing (Code coverage > 80%, No critical security issues, Performance meets SLA, Architecture review
        approved) and reviewers emp_arch_01 and emp_pm_03, noting 'All criteria met for phase gate'. Output the
        initial readiness score and whether ms_002 is ready after all interventions.
        """,
        actions=[
            Action(
                name="validate_milestone_readiness", kwargs={"milestone_id": "ms_002"}
            ),
            Action(name="get_milestone_details", kwargs={"milestone_id": "ms_002"}),
            Action(
                name="get_milestone_dependencies", kwargs={"milestone_id": "ms_002"}
            ),
            Action(
                name="update_milestone_status",
                kwargs={
                    "milestone_id": "ms_001",
                    "new_status": "completed",
                    "progress_percentage": 100,
                    "health": "green",
                    "status_notes": "All deliverables completed",
                    "deliverables_completed": [
                        "OAuth2 integration",
                        "User session management",
                        "Security documentation",
                    ],
                },
            ),
            Action(
                name="validate_milestone_readiness", kwargs={"milestone_id": "ms_002"}
            ),
            Action(
                name="add_external_dependency",
                kwargs={
                    "milestone_id": "ms_002",
                    "dependency_name": "Security Audit Services",
                    "provider": "SecureTest Systems",
                    "expected_delivery_date": "2024-04-10T00:00:00Z",
                    "criticality": "high",
                    "confirmed": True,
                    "contact_info": {
                        "name": "Security Team",
                        "email": "audit@securetest.com",
                    },
                    "contingency_days": 3,
                    "notice_days": 30,
                },
            ),
            Action(
                name="create_gate_review",
                kwargs={
                    "milestone_id": "ms_002",
                    "review_date": "2024-04-10T00:00:00Z",
                    "criteria_results": {
                        "Code coverage > 80%": "pass",
                        "No critical security issues": "pass",
                        "Performance meets SLA": "pass",
                        "Architecture review approved": "pass",
                    },
                    "reviewers": ["emp_arch_01", "emp_pm_03"],
                    "review_notes": "All criteria met for phase gate",
                },
            ),
        ],
        outputs=['"readiness_score": 75', '"is_ready": false'],
    ),
    Task(
        annotator="0",
        user_id="mobile_variance_control_specialist",
        instruction="""
        You are controlling schedule variance for the Mobile App Launch project (proj_mobile_01). First get the
        schedule variance to assess current performance. Check milestone float to identify critical and non-critical
        milestones. Based on the variance analysis, create a new quarterly baseline (use bs_XXX as baseline ID and 2024-04-01T00:00:00Z as creation date)
        called 'Mobile Q2 2024 Adjusted Baseline' with notes about minor variance corrections. After creating the
        baseline, get schedule variance again against the new baseline. Update ms_001
        dates by moving the target date 3 days later to April 3, 2024 citing minor adjustment for variance control.
        Then update the project buffer consumption by 2 days for ms_001 due to the adjustment. Finally, validate
        milestone readiness for ms_002 to ensure dependencies are not affected. Report the number of on-track milestones
        from initial variance, the baseline creation success status, and the readiness score for ms_002.
        """,
        actions=[
            Action(
                name="get_schedule_variance", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="check_milestone_float", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="create_schedule_baseline",
                kwargs={
                    "baseline_id": "bs_XXX",
                    "create_date": "2024-04-01T00:00:00Z",
                    "project_id": "proj_mobile_01",
                    "baseline_name": "Mobile Q2 2024 Adjusted Baseline",
                    "baseline_type": "quarterly",
                    "notes": "minor variance corrections",
                },
            ),
            Action(
                name="get_schedule_variance", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="update_milestone_dates",
                kwargs={
                    "milestone_id": "ms_001",
                    "new_target_date": "2024-04-03T00:00:00Z",
                },
            ),
            Action(
                name="update_buffer_consumption",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "buffer_type": "project",
                    "days_consumed": 2,
                    "milestone_id": "ms_001",
                },
            ),
            Action(
                name="validate_milestone_readiness", kwargs={"milestone_id": "ms_002"}
            ),
        ],
        outputs=[
            '"on_track_milestones": 1',
            '"success": true',
            '"readiness_score": 75',
        ],
    ),
    Task(
        annotator="0",
        user_id="mobile_recovery_approval_manager",
        instruction="You are managing recovery plan approvals for the Mobile App Launch project (proj_mobile_01). First get delayed milestones with recovery plans included to identify pending approvals. Check the milestone details for ms_002 to understand its current status. Since recovery_001 is pending approval for ms_002, review its details by checking milestone float for the project. Approve recovery plan recovery_001 as sh_003 (PMO Director) with decision to approve, including approval notes about critical recovery needed for gate review delays. After approval, update milestone dates for ms_002 to April 10, 2024 based on the recovery plan, citing approved recovery plan implementation. Then update the phase gate buffer consumption by 2 days for ms_002 due to recovery activities. Finally, validate milestone readiness for ms_002 to ensure it's back on track. Report whether ms_002 has a recovery plan from the delayed milestones check, the decision made on the recovery plan, and the buffer consumption percentage after the update.",
        actions=[
            Action(
                name="get_delayed_milestones",
                kwargs={"project_id": "proj_mobile_01", "include_recovery_plans": True},
            ),
            Action(name="get_milestone_details", kwargs={"milestone_id": "ms_002"}),
            Action(
                name="check_milestone_float", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="approve_recovery_plan",
                kwargs={
                    "plan_id": "recovery_001",
                    "decision": "approve",
                    "approver_id": "sh_003",
                    "approval_notes": "Critical recovery needed for gate review delays",
                },
            ),
            Action(
                name="update_milestone_dates",
                kwargs={
                    "milestone_id": "ms_002",
                    "new_target_date": "2024-04-10T00:00:00Z",
                },
            ),
            Action(
                name="update_buffer_consumption",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "buffer_type": "phase_gate",
                    "days_consumed": 2,
                    "milestone_id": "ms_002",
                },
            ),
            Action(
                name="validate_milestone_readiness", kwargs={"milestone_id": "ms_002"}
            ),
        ],
        outputs=[
            '"has_recovery_plan": true',
            '"decision": "approve"',
            '"consumption_percentage": 16.7',
        ],
    ),
    Task(
        annotator="0",
        user_id="mobile_milestone_health_auditor",
        instruction="You are auditing milestone health for the Mobile App Launch project (proj_mobile_01). First get milestone details for ms_001 to check its current state. Then get details for ms_002 to compare progress. Check the schedule variance for the project to understand baseline performance. If ms_002 has health status yellow or red based on the details, create a gate review for ms_002 with review date April 5, 2024, marking Code coverage > 80% as pass, Performance meets SLA as pass, but No critical security issues as fail, and Architecture review approved as pass. Use reviewers emp_arch_01 and emp_pm_03. Include review notes about security issues identified during the health audit. After the review, if ms_002 progress is less than 70%, update its status to in_progress with 65% progress and yellow health, noting slow progress due to technical challenges. Then analyze schedule compression for 7 days using crashing. Finally, if ms_001 status is completed from the initial check, archive it. Report the health status of ms_002 from initial details, the overall decision from any gate review created, and the feasibility of compression.",
        actions=[
            Action(name="get_milestone_details", kwargs={"milestone_id": "ms_001"}),
            Action(name="get_milestone_details", kwargs={"milestone_id": "ms_002"}),
            Action(
                name="get_schedule_variance", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="create_gate_review",
                kwargs={
                    "milestone_id": "ms_002",
                    "review_date": "2024-04-05T00:00:00Z",
                    "criteria_results": {
                        "Code coverage > 80%": "pass",
                        "No critical security issues": "fail",
                        "Performance meets SLA": "pass",
                        "Architecture review approved": "pass",
                    },
                    "reviewers": ["emp_arch_01", "emp_pm_03"],
                    "review_notes": "Security issues identified during health audit",
                },
            ),
            Action(
                name="update_milestone_status",
                kwargs={
                    "milestone_id": "ms_002",
                    "new_status": "in_progress",
                    "progress_percentage": 65,
                    "health": "yellow",
                    "status_notes": "Slow progress due to technical challenges",
                },
            ),
            Action(
                name="analyze_schedule_compression",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "target_reduction": 7,
                    "compression_type": "crashing",
                },
            ),
            Action(
                name="archive_milestone",
                kwargs={
                    "milestone_id": "ms_001",
                },
            ),
        ],
        outputs=[
            '"health": "yellow"',
            '"overall_decision": "fail"',
            '"feasible": true',
        ],
    ),
    Task(
        annotator="0",
        user_id="enterprise_milestone_creation_specialist",
        instruction="""
        You are creating strategic milestones for the Enterprise Platform project (proj_enterprise_01). First get the
        project timeline to understand current milestones. Check milestone float to identify schedule gaps. Create a
        new major milestone (use 'ms_ABC' as ID) called 'Enterprise Security Architecture Review' with target
        date May 15, 2024, start date April 15, 2024, description
        'Comprehensive security architecture validation for enterprise platform', deliverables including Security
        architecture document, Threat model analysis, and Compliance checklist. Set owner as emp_arch_01 with gate
        criteria: Security vulnerabilities addressed, Architecture patterns approved, and Performance impact assessed.
        Output the the created milestone buffer consumption and health.
        """,
        actions=[
            Action(
                name="get_project_timeline",
                kwargs={
                    "project_id": "proj_enterprise_01",
                    "include_dependencies": False,
                },
            ),
            Action(
                name="check_milestone_float",
                kwargs={"project_id": "proj_enterprise_01"},
            ),
            Action(
                name="create_milestone",
                kwargs={
                    "milestone_id": "ms_ABC",
                    "project_id": "proj_enterprise_01",
                    "milestone_name": "Enterprise Security Architecture Review",
                    "milestone_type": "major",
                    "target_date": "2024-05-15T00:00:00Z",
                    "start_date": "2024-04-15T00:00:00Z",
                    "description": "Comprehensive security architecture validation for enterprise platform",
                    "deliverables": [
                        "Security architecture document",
                        "Threat model analysis",
                        "Compliance checklist",
                    ],
                    "owner_id": "emp_arch_01",
                    "gate_criteria": [
                        "Security vulnerabilities addressed",
                        "Architecture patterns approved",
                        "Performance impact assessed",
                    ],
                },
            ),
        ],
        outputs=['"health": "green"', '"buffer_consumed": 0'],
    ),
    Task(
        annotator="0",
        user_id="mobile_milestone_progress_manager",
        instruction="""You are managing milestone progress for the Mobile App
        Launch project (proj_mobile_01). First get milestone details for ms_002
        (Phase 1 Gate Review) to check current status. Validate its readiness to
        understand completion requirements. Since the team has made significant
        progress, update ms_002 status to in_progress with 85% completion and
        yellow health, listing completed deliverables: Core features complete
        and Performance benchmarks met. Add status notes about pending security
        review. After the status update, check milestone float to see if the
        progress affects schedule pressure. Get delayed milestones to see if
        ms_002 is still considered delayed. If ms_002 still shows as delayed,
        create a gate review for it with review date April 12, 2024, marking
        Code coverage > 80% as pass, No critical security issues as fail,
        Performance meets SLA as pass, and Architecture review approved as pass,
        with reviewers emp_arch_01 and emp_pm_03. Add review notes that security
        issues were identified and remediation is in progress. Finally, if a
        gate review was created, update ms_002 status again to 90% progress with
        status notes about gate review scheduled. Output the initial progress
        percentage, and the health change from the first update.""",
        actions=[
            Action(name="get_milestone_details", kwargs={"milestone_id": "ms_002"}),
            Action(
                name="validate_milestone_readiness", kwargs={"milestone_id": "ms_002"}
            ),
            Action(
                name="update_milestone_status",
                kwargs={
                    "milestone_id": "ms_002",
                    "new_status": "in_progress",
                    "progress_percentage": 85,
                    "health": "yellow",
                    "status_notes": "Pending security review",
                    "deliverables_completed": [
                        "Core features complete",
                        "Performance benchmarks met",
                    ],
                },
            ),
            Action(
                name="check_milestone_float", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="get_delayed_milestones",
                kwargs={
                    "project_id": "proj_mobile_01",
                },
            ),
            Action(
                name="create_gate_review",
                kwargs={
                    "milestone_id": "ms_002",
                    "review_date": "2024-04-12T00:00:00Z",
                    "criteria_results": {
                        "Code coverage > 80%": "pass",
                        "No critical security issues": "fail",
                        "Performance meets SLA": "pass",
                        "Architecture review approved": "pass",
                    },
                    "reviewers": ["emp_arch_01", "emp_pm_03"],
                    "review_notes": "Security issues identified, remediation in progress",
                },
            ),
            Action(
                name="update_milestone_status",
                kwargs={
                    "milestone_id": "ms_002",
                    "new_status": "in_progress",
                    "progress_percentage": 90,
                    "status_notes": "Gate review scheduled",
                },
            ),
        ],
        outputs=[
            '"progress_percentage": 65',
            '"health_change": "yellow -> yellow"',
        ],
    ),
    Task(
        annotator="0",
        user_id="cross_project_dependency_coordinator",
        instruction="""
        You are coordinating dependencies across projects. First get the milestone details for ms_003 (ML Model
        Training) in the AI Platform project. Check milestone float for proj_ai_01 to understand schedule flexibility.
        Get milestone dependencies for ms_003 to see existing relationships. Since ML training requires completed
        authentication, create a dependency where ms_001 (Authentication Module) from Mobile project must complete
        before ms_003 with a 10-day lag, making it mandatory with notes about security requirements for ML access.
        Check milestone float again to identify any new critical paths. Analyze schedule compression
        for 15 days using crashing and output the reduction days count.
        """,
        actions=[
            Action(name="get_milestone_details", kwargs={"milestone_id": "ms_003"}),
            Action(name="check_milestone_float", kwargs={"project_id": "proj_ai_01"}),
            Action(
                name="get_milestone_dependencies", kwargs={"milestone_id": "ms_003"}
            ),
            Action(
                name="create_milestone_dependency",
                kwargs={
                    "predecessor_id": "ms_001",
                    "successor_id": "ms_003",
                    "dependency_type": "finish_to_start",
                    "lag_days": 10,
                    "is_mandatory": True,
                    "notes": "Security requirements for ML access",
                    "zero_lag": False,
                },
            ),
            Action(name="check_milestone_float", kwargs={"project_id": "proj_ai_01"}),
            Action(
                name="analyze_schedule_compression",
                kwargs={
                    "project_id": "proj_ai_01",
                    "target_reduction": 15,
                    "compression_type": "crashing",
                },
            ),
        ],
        outputs=[
            '"reduction_days": 12',
        ],
    ),
    Task(
        annotator="0",
        user_id="mobile_critical_path_manager",
        instruction="""
        You are managing the critical path for the Mobile App Launch project (proj_mobile_01). First calculate the
        critical path to establish baseline. Get milestone details for ms_002 to understand its role. If ms_002
        is on the critical path, create an external dependency for Security Audit Certification from SecureTest
        Systems with expected delivery April 5, 2024, marking it as high criticality with 3 contingency days. Set
        confirmed as False and use 30 days notice period. For contact info, use Audit Team with email
        audit@securetest.com. After adding the dependency, calculate the critical path again to see the impact.
        Based on the new critical path, if total duration exceeds 20 days, analyze schedule compression for 15
        days using crashing. Check milestone float after these changes. If ms_001 still has zero float, update its
        dates by moving the start date earlier to February 25, 2024 to create schedule buffer. Finally, calculate
        the critical path one more time to verify the optimization. Report the initial critical tasks count, the
        total duration after adding dependency, and the final critical milestones count after all optimizations.
        """,
        actions=[
            Action(
                name="calculate_critical_path", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(name="get_milestone_details", kwargs={"milestone_id": "ms_002"}),
            Action(
                name="add_external_dependency",
                kwargs={
                    "milestone_id": "ms_002",
                    "dependency_name": "Security Audit Certification",
                    "provider": "SecureTest Systems",
                    "expected_delivery_date": "2024-04-05T00:00:00Z",
                    "criticality": "high",
                    "confirmed": False,
                    "contact_info": {
                        "name": "Audit Team",
                        "email": "audit@securetest.com",
                    },
                    "contingency_days": 3,
                    "notice_days": 30,
                },
            ),
            Action(
                name="calculate_critical_path", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="analyze_schedule_compression",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "target_reduction": 15,
                    "compression_type": "crashing",
                },
            ),
            Action(
                name="check_milestone_float", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="update_milestone_dates",
                kwargs={
                    "milestone_id": "ms_001",
                    "new_start_date": "2024-02-25T00:00:00Z",
                },
            ),
            Action(
                name="calculate_critical_path", kwargs={"project_id": "proj_mobile_01"}
            ),
        ],
        outputs=[
            '"critical_tasks": ["ms_001"]',
            '"total_duration_days": 30',
            '"critical_milestones_count": 1',
        ],
    ),
    Task(
        annotator="0",
        user_id="mobile_baseline_version_controller",
        instruction="""
        You are managing baseline versions for the Mobile App Launch project (proj_mobile_01). First get the schedule
        variance to check current baseline performance. Check milestone float to identify any major variances. Create a
        new schedule baseline called 'Mobile Q2 2024
        Recovery Baseline' with quarterly type and notes about addressing schedule delays (set create date as 2024-04-15T00:00:00Z).
        Include PMO approval since
        this would be the second quarterly baseline. After creating the baseline, get schedule variance again to
        verify it's using the new baseline. Analyze schedule compression for 10 days using crashing to plan recovery.
        Output the number of delayed milestones.
        """,
        actions=[
            Action(
                name="get_schedule_variance", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="check_milestone_float", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="create_schedule_baseline",
                kwargs={
                    "create_date": "2024-04-15T00:00:00Z",
                    "project_id": "proj_mobile_01",
                    "baseline_name": "Mobile Q2 2024 Recovery Baseline",
                    "baseline_type": "quarterly",
                    "notes": "Addressing schedule delays",
                    "pmo_approval": True,
                },
            ),
            Action(
                name="get_schedule_variance", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="analyze_schedule_compression",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "target_reduction": 10,
                    "compression_type": "crashing",
                },
            ),
        ],
        outputs=[
            '"delayed_milestones": 0',
        ],
    ),
    Task(
        annotator="0",
        user_id="ai_platform_schedule_accelerator",
        instruction="You are accelerating the schedule for the AI Platform project (proj_ai_01). First get milestone details for ms_003 (ML Model Training). Check the current schedule variance to understand baseline performance. Since cloud resources became available early, update ms_003 dates by moving both start and target dates earlier: new start April 20, 2024 and new target June 15, 2024, citing 'Early cloud resource availability'. After the date change, calculate the critical path to see schedule impacts. Check milestone float to verify the acceleration didn't create negative float. If ms_003 now has negative float, create an external dependency for 'GPU Cluster Allocation' from DataCenter Corp with expected delivery April 15, 2024, marking it as critical with 3 contingency days, confirmed status true, contact info with name 'DC Operations' and email 'ops@datacenter.com', and 14 notice days. Then validate milestone readiness for ms_003. Finally, update the project buffer consumption by 7 days due to the accelerated schedule, referencing milestone ms_003. Report the number of impacted milestones from the date change, whether critical path update is required, and the remaining buffer after consumption.",
        actions=[
            Action(name="get_milestone_details", kwargs={"milestone_id": "ms_003"}),
            Action(name="get_schedule_variance", kwargs={"project_id": "proj_ai_01"}),
            Action(
                name="update_milestone_dates",
                kwargs={
                    "milestone_id": "ms_003",
                    "new_start_date": "2024-04-20T00:00:00Z",
                    "new_target_date": "2024-06-15T00:00:00Z",
                },
            ),
            Action(name="calculate_critical_path", kwargs={"project_id": "proj_ai_01"}),
            Action(name="check_milestone_float", kwargs={"project_id": "proj_ai_01"}),
            Action(
                name="add_external_dependency",
                kwargs={
                    "milestone_id": "ms_003",
                    "dependency_name": "GPU Cluster Allocation",
                    "provider": "DataCenter Corp",
                    "expected_delivery_date": "2024-04-15T00:00:00Z",
                    "criticality": "critical",
                    "confirmed": True,
                    "contact_info": {
                        "name": "DC Operations",
                        "email": "ops@datacenter.com",
                    },
                    "contingency_days": 3,
                    "notice_days": 14,
                },
            ),
            Action(
                name="validate_milestone_readiness", kwargs={"milestone_id": "ms_003"}
            ),
            Action(
                name="update_buffer_consumption",
                kwargs={
                    "project_id": "proj_ai_01",
                    "buffer_type": "project",
                    "days_consumed": 7,
                    "milestone_id": "ms_003",
                },
            ),
        ],
        outputs=[
            '"impacted_count": 0',
            '"critical_path_update_required": false',
            '"remaining_buffer": 38',
        ],
    ),
    Task(
        annotator="0",
        user_id="ai_platform_gate_escalation_manager",
        instruction="You are managing gate reviews for the AI Platform project (proj_ai_01). First get milestone details for ms_003 (ML Model Training) to check its gate criteria. Validate the readiness of ms_003 before the review. Create a gate review for ms_003 with review date June 20, 2024, where Model accuracy > 95% passes, Training data validated passes, but Bias testing complete fails. Use reviewers emp_data_01, sh_004, and emp_analyst_01. Include action items: Complete bias testing with diverse datasets and Document bias mitigation strategies. After the review, check milestone details again to see health status changes. Since this is a failed review, update the milestone dates by extending target date by 14 days to July 14, 2024 citing gate review remediation period. Then create another gate review for the new date July 5, 2024 where all criteria pass this time. Finally, check milestone float after all changes. Report the gate criteria count from initial details, the decision from the first gate review, and whether the second review resulted in escalation.",
        actions=[
            Action(name="get_milestone_details", kwargs={"milestone_id": "ms_003"}),
            Action(
                name="validate_milestone_readiness", kwargs={"milestone_id": "ms_003"}
            ),
            Action(
                name="create_gate_review",
                kwargs={
                    "milestone_id": "ms_003",
                    "review_date": "2024-06-20T00:00:00Z",
                    "criteria_results": {
                        "Model accuracy > 95%": "pass",
                        "Training data validated": "pass",
                        "Bias testing complete": "fail",
                    },
                    "reviewers": ["emp_data_01", "sh_004", "emp_analyst_01"],
                    "action_items": [
                        "Complete bias testing with diverse datasets",
                        "Document bias mitigation strategies",
                    ],
                },
            ),
            Action(name="get_milestone_details", kwargs={"milestone_id": "ms_003"}),
            Action(
                name="update_milestone_dates",
                kwargs={
                    "milestone_id": "ms_003",
                    "new_target_date": "2024-07-14T00:00:00Z",
                },
            ),
            Action(
                name="create_gate_review",
                kwargs={
                    "milestone_id": "ms_003",
                    "review_date": "2024-07-05T00:00:00Z",
                    "criteria_results": {
                        "Model accuracy > 95%": "pass",
                        "Training data validated": "pass",
                        "Bias testing complete": "pass",
                    },
                    "reviewers": ["emp_data_01", "sh_004", "emp_analyst_01"],
                },
            ),
            Action(name="check_milestone_float", kwargs={"project_id": "proj_ai_01"}),
        ],
        outputs=[
            '"gate_criteria": [',
            '"overall_decision": "fail"',
            '"escalated": false',
        ],
    ),
    Task(
        annotator="0",
        user_id="mobile_vendor_dependency_coordinator",
        instruction="""
        You are coordinating external vendor dependencies for the Mobile App Launch project (proj_mobile_01).
        First get milestone details for ms_002 (Phase 1 Gate Review). Check the project timeline to understand
        schedule constraints. Add an external dependency (use 'ext_f9444b49' as dependency ID),
        for Payment Gateway Integration from Stripe with expected
        delivery April 5, 2024, marking it as high criticality with 3 contingency days. Set it as unconfirmed initially
         with contact info: Integration Team at integrations@stripe.com, requiring 14 days notice. After adding the
         dependency, validate milestone readiness for ms_002 to see the impact of the unconfirmed dependency. Update
         the external dependency status to delivered with actual delivery date April 3, 2024. Then validate milestone
         readiness again to see the improvement. Finally, update its status to
         in_progress with 75% completion and yellow health, noting Payment gateway integration delivered early.
         Report the dependency ID created, whether ms_002 was ready before delivery confirmation, and the health
         status after the update.
         """,
        actions=[
            Action(name="get_milestone_details", kwargs={"milestone_id": "ms_002"}),
            Action(
                name="get_project_timeline",
                kwargs={"project_id": "proj_mobile_01", "include_dependencies": False},
            ),
            Action(
                name="add_external_dependency",
                kwargs={
                    "dependency_id": "ext_f9444b49",
                    "milestone_id": "ms_002",
                    "dependency_name": "Payment Gateway Integration",
                    "provider": "Stripe",
                    "expected_delivery_date": "2024-04-05T00:00:00Z",
                    "criticality": "high",
                    "confirmed": False,
                    "contact_info": {
                        "name": "Integration Team",
                        "email": "integrations@stripe.com",
                    },
                    "contingency_days": 3,
                    "notice_days": 14,
                },
            ),
            Action(
                name="validate_milestone_readiness", kwargs={"milestone_id": "ms_002"}
            ),
            Action(
                name="update_external_dependency_status",
                kwargs={
                    "dependency_id": "ext_f9444b49",
                    "new_status": "delivered",
                    "actual_delivery_date": "2024-04-03T00:00:00Z",
                },
            ),
            Action(
                name="validate_milestone_readiness", kwargs={"milestone_id": "ms_002"}
            ),
            Action(
                name="update_milestone_status",
                kwargs={
                    "milestone_id": "ms_002",
                    "new_status": "in_progress",
                    "progress_percentage": 75,
                    "health": "yellow",
                    "status_notes": "Payment gateway integration delivered early",
                },
            ),
        ],
        outputs=['"dependency_id": "ext_', '"is_ready": false', '"health": "yellow"'],
    ),
    Task(
        annotator="0",
        user_id="ai_platform_external_risk_manager",
        instruction="""
        You are managing external risks for the AI Platform project (proj_ai_01). First get milestone details for ms_003
        (ML Model Training). Check for existing external dependencies on this milestone. Add a new external dependency (use 'ext_16299417' as dependency ID)
        for GPU Cluster Expansion from DataCenter Corp, expected May 15, 2024, marking it as high criticality with 7
        contingency days and 45 notice days. The contact is Infrastructure Team at infra@datacenter.com, phone 555-0123.
        After adding, validate milestone readiness for ms_003 to see the impact. Since external dependencies create risk,
        create a recovery plan for ms_003 with mixed strategies: scope reduction by deferring advanced features (6 impact days),
        fast tracking model validation (4 impact days), and crashing by using cloud GPU bursting (5 impact days).
        Include emp_data_01 and emp_data_02 as additional resources with risk mitigation including vendor escalation
        procedures and backup cloud providers. Set feasibility as low due to external constraints. After the recovery plan,
        update the external dependency status to delayed (use the dependency_id from the add_external_dependency output).
        Finally, check delayed milestones to see overall project impact. Report the milestone health from initial details,
        the total impact days from recovery plan, and whether ms_003 appears in delayed milestones.
        """,
        actions=[
            Action(name="get_milestone_details", kwargs={"milestone_id": "ms_003"}),
            Action(
                name="add_external_dependency",
                kwargs={
                    "dependency_id": "ext_16299417",
                    "milestone_id": "ms_003",
                    "dependency_name": "GPU Cluster Expansion",
                    "provider": "DataCenter Corp",
                    "expected_delivery_date": "2024-05-15T00:00:00Z",
                    "criticality": "high",
                    "confirmed": False,
                    "contact_info": {
                        "name": "Infrastructure Team",
                        "email": "infra@datacenter.com",
                        "phone": "555-0123",
                    },
                    "contingency_days": 7,
                    "notice_days": 45,
                },
            ),
            Action(
                name="validate_milestone_readiness", kwargs={"milestone_id": "ms_003"}
            ),
            Action(
                name="create_recovery_plan",
                kwargs={
                    "milestone_id": "ms_003",
                    "recovery_actions": [
                        {
                            "type": "scope_reduction",
                            "description": "deferring advanced features",
                            "impact_days": 6,
                        },
                        {
                            "type": "fast_tracking",
                            "description": "fast tracking model validation",
                            "impact_days": 4,
                        },
                        {
                            "type": "crashing",
                            "description": "using cloud GPU bursting",
                            "impact_days": 5,
                        },
                    ],
                    "additional_resources": ["emp_data_01", "emp_data_02"],
                    "risk_mitigation": [
                        "vendor escalation procedures",
                        "backup cloud providers",
                    ],
                    "feasibility": "low",
                },
            ),
            Action(
                name="update_external_dependency_status",
                kwargs={"dependency_id": "ext_16299417", "new_status": "delayed"},
            ),
            Action(
                name="get_delayed_milestones",
                kwargs={"project_id": "proj_ai_01", "include_recovery_plans": True},
            ),
        ],
        outputs=['"health": "green"', '"total_impact_days": 15', '"delayed_count": 0'],
    ),
    Task(
        annotator="0",
        user_id="mobile_incremental_compression_analyst",
        instruction="""
        You are analyzing incremental compression options for the Mobile App Launch project (proj_mobile_01).
        First get the schedule variance to understand baseline performance. Check milestone float to identify
        compression candidates. Analyze schedule compression for 5 days using crashing to test minimal compression.
        Analyze compression again for 10 days using crashing. Then analyze
        compression for 10 days using fast tracking to compare approaches. Based on the analyses, if fast tracking
        achieves at least 8 days reduction, create a gate review for milestone ms_002 on April 12, 2024, with
        reviewers emp_arch_01 and emp_pm_03. For criteria results, marked as "pass" the following: code coverage > 80%,
        no critical security issues, performance meets SLA, and architecture review approved.
        Also add the note: 'Fast track implementation approved based on compression analysis'. Update
        project buffer by 4 days citing optimal
        compression point identified. Finally, validate milestone readiness for ms_002 after all changes. You want
        to find out the cost from 5-day crashing, whether fast tracking is feasible for 10 days, and the readiness
        score after changes.
        """,
        actions=[
            Action(
                name="get_schedule_variance", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="check_milestone_float", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="analyze_schedule_compression",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "target_reduction": 5,
                    "compression_type": "crashing",
                },
            ),
            Action(
                name="analyze_schedule_compression",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "target_reduction": 10,
                    "compression_type": "crashing",
                },
            ),
            Action(
                name="analyze_schedule_compression",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "target_reduction": 10,
                    "compression_type": "fast_tracking",
                },
            ),
            Action(
                name="create_gate_review",
                kwargs={
                    "milestone_id": "ms_002",
                    "review_date": "2024-04-12T00:00:00Z",
                    "criteria_results": {
                        "Code coverage > 80%": "pass",
                        "No critical security issues": "pass",
                        "Performance meets SLA": "pass",
                        "Architecture review approved": "pass",
                    },
                    "reviewers": ["emp_arch_01", "emp_pm_03"],
                    "review_notes": "Fast track implementation approved based on compression analysis",
                },
            ),
            Action(
                name="update_buffer_consumption",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "buffer_type": "project",
                    "days_consumed": 4,
                    "milestone_id": "ms_002",
                },
            ),
            Action(
                name="validate_milestone_readiness", kwargs={"milestone_id": "ms_002"}
            ),
        ],
        outputs=['"total_cost": 2500', '"feasible": true', '"readiness_score": 75'],
    ),
    Task(
        annotator="0",
        user_id="ai_platform_buffer_risk_manager",
        instruction="""
        You are managing buffer risks for the AI Platform project (proj_ai_01). First get the schedule variance to
        check baseline performance. Check milestone float to identify schedule pressures. Since ML model training
        is complex, update the project buffer consumption by 8 days for ms_003 citing machine learning model
        complexity exceeding estimates. Then analyze schedule compression for 15 days using crashing to understand
        cost implications. Based on the buffer update, also
        update the integration buffer by 3 days for ms_003 citing model integration complexity, but include change
        request ID CR-2024-AI-001 since this is for scope addition. After buffer updates, validate milestone readiness
        for ms_003. Finally, create a recovery plan for ms_003 with crashing: accelerated training for 5 impact
        days and parallel validation for 4 impact days, using emp_data_01 and emp_data_02 as additional resources
        with high feasibility and 24/7 training monitoring and automated validation pipelines as risk mitigation.
        Give me the initial variance percentage for ms_003, whether risk review was triggered after first buffer
        update, and the total days recovered from the recovery plan.
        """,
        actions=[
            Action(name="get_schedule_variance", kwargs={"project_id": "proj_ai_01"}),
            Action(name="check_milestone_float", kwargs={"project_id": "proj_ai_01"}),
            Action(
                name="update_buffer_consumption",
                kwargs={
                    "project_id": "proj_ai_01",
                    "buffer_type": "project",
                    "days_consumed": 8,
                    "milestone_id": "ms_003",
                },
            ),
            Action(
                name="analyze_schedule_compression",
                kwargs={
                    "project_id": "proj_ai_01",
                    "target_reduction": 15,
                    "compression_type": "crashing",
                },
            ),
            Action(
                name="update_buffer_consumption",
                kwargs={
                    "project_id": "proj_ai_01",
                    "buffer_type": "integration",
                    "days_consumed": 3,
                    "milestone_id": "ms_003",
                    "change_request_id": "CR-2024-AI-001",
                },
            ),
            Action(
                name="validate_milestone_readiness", kwargs={"milestone_id": "ms_003"}
            ),
            Action(
                name="create_recovery_plan",
                kwargs={
                    "milestone_id": "ms_003",
                    "recovery_actions": [
                        {
                            "type": "crashing",
                            "description": "Accelerated training",
                            "impact_days": 5,
                        },
                        {
                            "type": "crashing",
                            "description": "Parallel validation",
                            "impact_days": 4,
                        },
                    ],
                    "additional_resources": ["emp_data_01", "emp_data_02"],
                    "risk_mitigation": [
                        "24/7 training monitoring",
                        "Automated validation pipelines",
                    ],
                    "feasibility": "high",
                },
            ),
        ],
        outputs=[
            '"variance_percentage": 0.0',
            '"risk_review_required": false',
            '"days_recovered": 9',
        ],
    ),
    Task(
        annotator="0",
        user_id="ai_dependency_gap_analyst",
        instruction="""
        You are analyzing dependency gaps for the AI Platform project (proj_ai_01). First get milestone dependencies
        for ms_003 (ML Model Training) to check its prerequisites. Get the project timeline to see all milestones and
        their relationships. Since ML model training requires infrastructure, add an external dependency (use ext_35c30d1d as dependency ID) for GPU
        Cluster Setup from DataCenter Corp with expected delivery May 1, 2024, marking it as critical with 7
        contingency days and 45 notice days. Check milestone float to see if the new dependency
        affects the schedule. Validate milestone readiness for ms_003 to confirm the external dependency impact.
        Finally, if ms_003 is not ready due to the external dependency, update the external dependency status to
        confirmed to resolve the readiness issue. The dependency_id from the add_external_dependency action output
        should be used for the update. Find the initial number of predecessors for ms_003, the criticality level of
        the external dependency added, and whether ms_003 has positive float.
        """,
        actions=[
            Action(
                name="get_milestone_dependencies", kwargs={"milestone_id": "ms_003"}
            ),
            Action(
                name="get_project_timeline",
                kwargs={"project_id": "proj_ai_01", "include_dependencies": True},
            ),
            Action(
                name="add_external_dependency",
                kwargs={
                    "milestone_id": "ms_003",
                    "dependency_id": "ext_35c30d1d",
                    "dependency_name": "GPU Cluster Setup",
                    "provider": "DataCenter Corp",
                    "expected_delivery_date": "2024-05-01T00:00:00Z",
                    "criticality": "critical",
                    "confirmed": False,
                    "contingency_days": 7,
                    "notice_days": 45,
                },
            ),
            Action(name="check_milestone_float", kwargs={"project_id": "proj_ai_01"}),
            Action(
                name="validate_milestone_readiness", kwargs={"milestone_id": "ms_003"}
            ),
            Action(
                name="update_external_dependency_status",
                kwargs={
                    "dependency_id": "ext_35c30d1d",
                    "new_status": "confirmed",
                },
            ),
        ],
        outputs=['"predecessors": []', '"criticality": "critical"', '"float_days": 5'],
    ),
    Task(
        annotator="0",
        user_id="mobile_float_risk_monitor",
        instruction="""
        You are monitoring float risks for the Mobile App Launch project
        (proj_mobile_01). First check milestone float to establish baseline risk
        levels. Get delayed milestones including recovery plans to understand current issues. If there
        are milestones with negative float, validate readiness for the milestone
        with the most negative float (ms_002). Based on float analysis, if more
        than half the milestones have zero or negative float, update buffer
        consumption by 5 days for integration buffer citing critical path
        pressure across multiple milestones. Check milestone float again after
        buffer update. Create an external dependency for ms_002: Testing
        Environment from Cloud Provider expected April 5, 2024, marked as high
        criticality with 3 contingency days, unconfirmed status, with Cloud
        Support contact (name: Cloud Support, email: support@cloudprovider.com)
        and 14 notice days. Finally, analyze schedule compression for 15 days
        using crashing to evaluate emergency options. Let me know the initial
        zero float count, the risk level for the milestone with most negative
        float, and whether the critical path count increased after buffer
        consumption.""",
        actions=[
            Action(
                name="check_milestone_float", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="get_delayed_milestones",
                kwargs={"project_id": "proj_mobile_01", "include_recovery_plans": True},
            ),
            Action(
                name="validate_milestone_readiness", kwargs={"milestone_id": "ms_002"}
            ),
            Action(
                name="update_buffer_consumption",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "buffer_type": "integration",
                    "days_consumed": 5,
                    "milestone_id": "ms_002",
                },
            ),
            Action(
                name="check_milestone_float", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="add_external_dependency",
                kwargs={
                    "milestone_id": "ms_002",
                    "dependency_name": "Testing Environment",
                    "provider": "Cloud Provider",
                    "expected_delivery_date": "2024-04-05T00:00:00Z",
                    "criticality": "high",
                    "confirmed": False,
                    "contact_info": {
                        "name": "Cloud Support",
                        "email": "support@cloudprovider.com",
                    },
                    "contingency_days": 3,
                    "notice_days": 14,
                },
            ),
            Action(
                name="analyze_schedule_compression",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "target_reduction": 15,
                    "compression_type": "crashing",
                },
            ),
        ],
        outputs=[
            '"zero_float": 1',
            '"risk_level": "critical"',
            '"critical_path_count": 2',
        ],
    ),
    Task(
        annotator="0",
        user_id="enterprise_resource_optimization_analyst",
        instruction="""
        You are optimizing resource allocation for the Enterprise Platform project (proj_enterprise_01). First get the
        project timeline to understand resource requirements. Create a milestone (use 'ms_524727c0' as milestone ID)
        from template_007 (Architecture Review
        Gate) called 'Enterprise Security Architecture Review' with target date August 15, 2024, assigned to emp_arch_01.
        Apply resource leveling with constraints: Senior Architect limited to 1 and Security Developer limited to 2,
        using business value priority method. If milestones were shifted during leveling, check milestone float to
        assess the impact. Based on the leveling results,
        update the project buffer consumption by 3 days for milestone ms_524727c0 citing resource optimization tradeoffs
        from leveling. Then create a schedule baseline called 'Enterprise Resource Optimized Baseline' with quarterly
        type and 'Baseline after resource leveling impacts' as notes. Finally, get the schedule variance to compare against the new
        baseline. Tell me the number of milestones shifted from leveling, the extension percentage, and the milestone
        count in the new baseline.""",
        actions=[
            Action(
                name="get_project_timeline",
                kwargs={
                    "project_id": "proj_enterprise_01",
                    "include_dependencies": False,
                },
            ),
            Action(
                name="create_milestone_from_template",
                kwargs={
                    "milestone_id": "ms_524727c0",
                    "template_id": "template_007",
                    "project_id": "proj_enterprise_01",
                    "milestone_name": "Enterprise Security Architecture Review",
                    "target_date": "2024-08-15T00:00:00Z",
                    "owner_id": "emp_arch_01",
                },
            ),
            Action(
                name="apply_resource_leveling",
                kwargs={
                    "project_id": "proj_enterprise_01",
                    "resource_constraints": {
                        "Senior Architect": 1,
                        "Security Developer": 2,
                    },
                    "priority_method": "business_value",
                },
            ),
            Action(
                name="check_milestone_float",
                kwargs={"project_id": "proj_enterprise_01"},
            ),
            Action(
                name="update_buffer_consumption",
                kwargs={
                    "project_id": "proj_enterprise_01",
                    "buffer_type": "project",
                    "days_consumed": 3,
                    "milestone_id": "ms_524727c0",
                },
            ),
            Action(
                name="create_schedule_baseline",
                kwargs={
                    "project_id": "proj_enterprise_01",
                    "baseline_name": "Enterprise Resource Optimized Baseline",
                    "baseline_type": "quarterly",
                    "notes": "Baseline after resource leveling impacts",
                },
            ),
            Action(
                name="get_schedule_variance",
                kwargs={"project_id": "proj_enterprise_01"},
            ),
        ],
        outputs=[
            '"milestones_shifted": 1',
            '"extension_percentage": 3.9',
            '"milestone_count": 1',
        ],
    ),
]
