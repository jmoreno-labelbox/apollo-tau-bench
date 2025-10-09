from tau_bench.types import Action, Task

TASKS = [
    Task(
        annotator="0",
        user_id="project_recovery_coordinator",
        instruction="""
        As a project recovery coordinator for the Mobile App Launch project (proj_mobile_01), it is crucial to handle the approaching Phase 1 Gate Review milestone (ms_002), which seems to be delayed. Start by reviewing the project timeline to grasp the current status. Next, determine if the ms_002 milestone is prepared for progression. Examine the float status for all project milestones. Given that ms_002 is experiencing negative float, consider schedule compression strategies aiming for a 10-day reduction via the crashing method. Following the compression analysis, coordinate the development of a recovery plan that involves adding 2 senior developers (emp_dev_15 and emp_eng_10) to crucial tasks for 3 impact days and introducing weekend work for 2 impact days. Designate the recovery as having high feasibility with daily progress monitoring as a risk mitigation measure. Conclude by revising the ms_002 target date to April 12th in accordance with the recovery strategy. Present the total impact days realized and the cost-benefit ratio derived from the compression analysis.
        """,
        actions=[
            Action(
                name="GetProjectTimeline",
                kwargs={"project_id": "proj_mobile_01", "include_dependencies": True},
            ),
            Action(
                name="ValidateMilestoneReadiness", kwargs={"milestone_id": "ms_002"}
            ),
            Action(
                name="CheckMilestoneFloat", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="AnalyzeScheduleCompression",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "target_reduction": 10,
                    "compression_type": "crashing",
                },
            ),
            Action(
                name="CreateRecoveryPlan",
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
                name="UpdateMilestoneDates",
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
        instruction="As a schedule compliance manager, your role involves assessing the Mobile App Launch project timeline. Begin by obtaining the timeline for proj_mobile_01, inclusive of dependencies. Following this, examine the milestone float status to pinpoint schedule risks. Ensure that the Phase 1 Gate Review (ms_002) undergoes further security compliance validation. Integrate an external dependency for 'Security Audit Services' from CyberAudit Technologies, projected for delivery on April 15th, tagged with critical priority and 7 days of contingency. This dependency remains unconfirmed. Use the Audit Team as the contact with the email audit@cyberaudit.com, and establish a notification period of 30 days. Proceed with an analysis of schedule compression aiming for a 14-day reduction utilizing the fast tracking method. In light of the buffer consumption, update the phase gate buffer by 3 days for milestone ms_002 owing to 'Gate review preparation delays'. Draft a quarterly schedule baseline titled 'Q2 2024 Security Compliance Baseline' with annotations stating 'Baseline after security audit dependency integration'. Subsequently, evaluate the variance in relation to the updated baseline. Compile a report indicating the reduction days achieved, the percentage of total buffer consumed, and the count of milestone snapshots within the baseline.",
        actions=[
            Action(
                name="GetProjectTimeline",
                kwargs={"project_id": "proj_mobile_01", "include_dependencies": True},
            ),
            Action(
                name="CheckMilestoneFloat", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="AddExternalDependency",
                kwargs={
                    "milestone_id": "ms_002",
                    "dependency_name": "Security Audit Services",
                    "provider": "CyberAudit Technologies",
                    "expected_delivery_date": "2024-04-15T00:00:00Z",
                    "criticality": "critical",
                    "confirmed": False,
                    "contact_info": {
                        "name": "Audit Team",
                        "email": "audit@cyberaudit.com",
                    },
                    "contingency_days": 7,
                    "notice_days": 30,
                },
            ),
            Action(
                name="AnalyzeScheduleCompression",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "target_reduction": 14,
                    "compression_type": "fast_tracking",
                },
            ),
            Action(
                name="UpdateBufferConsumption",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "buffer_type": "phase_gate",
                    "days_consumed": 3,
                    "milestone_id": "ms_002",
                },
            ),
            Action(
                name="CreateScheduleBaseline",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "baseline_name": "Q2 2024 Security Compliance Baseline",
                    "baseline_type": "quarterly",
                    "notes": "Baseline after security audit dependency integration",
                },
            ),
            Action(
                name="GetScheduleVariance", kwargs={"project_id": "proj_mobile_01"}
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
        instruction="As a milestone compliance officer for the Mobile App Launch project, begin by obtaining the timeline for proj_mobile_01, including all dependencies. Next, assess the variance against the established baseline to evaluate schedule performance. With the Authentication Module (ms_001) completed, ensure it is archived. Proceed to establish a milestone from the 'Standard Product Launch' template (template_001) for a new 'Beta Testing Phase' milestone targeting June 1st, 2024, to be assigned to emp_qa_02. Update the external dependency status for the Network Infrastructure (ext_003), indicating it has been 'delivered' with an actual delivery date of April 15th. As there is an increase in buffer consumption, review the current milestone float status. Lastly, evaluate schedule compression possibilities for 12 days by employing fast tracking to recover the schedule. Report the count of float days and determine if fast tracking is viable.",
        actions=[
            Action(
                name="GetProjectTimeline",
                kwargs={"project_id": "proj_mobile_01", "include_dependencies": True},
            ),
            Action(
                name="GetScheduleVariance", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="ArchiveMilestone",
                kwargs={"milestone_id": "ms_001"},
            ),
            Action(
                name="CreateMilestoneFromTemplate",
                kwargs={
                    "template_id": "template_001",
                    "project_id": "proj_mobile_01",
                    "milestone_name": "Beta Testing Phase",
                    "target_date": "2024-06-01T00:00:00Z",
                    "owner_id": "emp_qa_02",
                },
            ),
            Action(
                name="UpdateExternalDependencyStatus",
                kwargs={
                    "dependency_id": "ext_003",
                    "new_status": "delivered",
                    "actual_delivery_date": "2024-04-15T00:00:00Z",
                },
            ),
            Action(
                name="CheckMilestoneFloat", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="AnalyzeScheduleCompression",
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
        instruction="In your role as a QA lead concluding the Phase 1 Gate Review for the Mobile App Launch project, start by retrieving the details of milestone ms_002 to ascertain the current status. Confirm if ms_002 is prepared to advance by validating its readiness. With all deliverables completed by the team, update ms_002 status to 'completed' with 100% progress and 'green' health, detailing all concluded deliverables: 'Core features complete', 'Security audit passed', and 'Performance benchmarks met'. Include notes regarding the successful completion of the security review. After making updates, acquire the project timeline to observe its impact. Since phase 1 is finalized, revise the dates for the ML Model Training milestone (ms_003) to commence on May 10th. Post date modification, verify the milestone float. Ultimately, compute the critical path for proj_ai_01 to comprehend schedule repercussions. Report on the change in milestone health, the number of completed milestones in the mobile project, and the total float days for ms_003.",
        actions=[
            Action(name="GetMilestoneDetails", kwargs={"milestone_id": "ms_002"}),
            Action(
                name="ValidateMilestoneReadiness", kwargs={"milestone_id": "ms_002"}
            ),
            Action(
                name="UpdateMilestoneStatus",
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
                name="GetProjectTimeline",
                kwargs={"project_id": "proj_mobile_01", "include_dependencies": False},
            ),
            Action(
                name="UpdateMilestoneDates",
                kwargs={
                    "milestone_id": "ms_003",
                    "new_start_date": "2024-05-10T00:00:00Z",
                },
            ),
            Action(name="CheckMilestoneFloat", kwargs={"project_id": "proj_ai_01"}),
            Action(name="CalculateCriticalPath", kwargs={"project_id": "proj_ai_01"}),
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
        You are responsible for managing milestone recovery for the Mobile App Launch
        project (proj_mobile_01). Start by examining the schedule variance compared to the
        baseline. Confirm the Phase 1 Gate Review (ms_002) preparedness. Develop a
        recovery plan for ms_002 with specific crashing actions: appoint 2 senior developers
        for 3 days and permit weekend work for 2 days, utilizing employees emp_dev_15
        and emp_eng_10 as added resources. Classify the recovery as highly feasible
        with daily progress tracking as a risk mitigation strategy. Once the recovery
        plan is in place, assess the feasibility of reducing the project timeline by
        10 days using the crashing method. Adjust the phase gate buffer consumption for
        ms_002 by 3 days owing to delays in gate review preparation. Report the
        number of identified readiness issues, total recovery plan impact days, and
        the cost-effectiveness ratio from the compression analysis.
        """,
        actions=[
            Action(
                name="GetScheduleVariance", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="ValidateMilestoneReadiness", kwargs={"milestone_id": "ms_002"}
            ),
            Action(
                name="CreateRecoveryPlan",
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
                name="AnalyzeScheduleCompression",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "target_reduction": 10,
                    "compression_type": "crashing",
                },
            ),
            Action(
                name="UpdateBufferConsumption",
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
        You are tasked with managing dependencies for the AI Platform project (proj_ai_01).
        Begin by verifying the milestone details for the ML Model Training Complete
        milestone (ms_003). Subsequently, retrieve the project timeline to review all milestones.
        Establish a milestone with the ID "ms_XXX", derived from template_004 for the
        proj_ai_01, titled 'AI Infrastructure', with
        '2024-06-25T00:00:00Z' as the target date and emp_data_01 as the owner. Formulate a
        milestone dependency ensuring ms_XXX finishes before ms_003 can initiate,
        with a 7-day delay and consider it mandatory. Attach notes specifying that
        authentication is necessary for secure model access. Upon establishing the
        dependency, compute the critical path for the AI project. Inspect the
        milestone float status to evaluate its impact. In conclusion, confirm the
        readiness of ms_003 to ascertain any effects from the new dependency. Report the
        project ID from the dependency creation outcome and the float days for
        ms_003.
        """,
        actions=[
            Action(name="GetMilestoneDetails", kwargs={"milestone_id": "ms_003"}),
            Action(
                name="GetProjectTimeline",
                kwargs={"project_id": "proj_ai_01", "include_dependencies": False},
            ),
            Action(
                name="CreateMilestoneFromTemplate",
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
                name="CreateMilestoneDependency",
                kwargs={
                    "predecessor_id": "ms_XXX",
                    "successor_id": "ms_003",
                    "dependency_type": "finish_to_start",
                    "lag_days": 7,
                    "is_mandatory": True,
                    "notes": "authentication is required for secure model access",
                },
            ),
            Action(name="CalculateCriticalPath", kwargs={"project_id": "proj_ai_01"}),
            Action(name="CheckMilestoneFloat", kwargs={"project_id": "proj_ai_01"}),
            Action(
                name="ValidateMilestoneReadiness", kwargs={"milestone_id": "ms_003"}
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
        Your task is to enhance the critical path for the Mobile App Launch project (proj_mobile_01). Start by obtaining the milestone
        details for ms_002 (Phase 1 Gate Review). Next, determine the critical path for the project. Examine the milestone
        float to identify milestones with minimal slack. Should ms_002 possess a negative float, adjust its dates by extending
        the target date by 5 days to April 20th due to critical path pressure. Establish a dependency between ms_001 and
        ms_002 if not yet present, incorporating a 2-day lag, and designate it as mandatory with a 'finish_to_start' type.
        Following these adjustments, recompute the
        critical path. Finally, confirm the readiness of ms_002. Document the float days for ms_002 from the initial
        float examination, the count of critical milestones from the final critical path computation, and the is_ready status
        from the validation.
        """,
        actions=[
            Action(name="GetMilestoneDetails", kwargs={"milestone_id": "ms_002"}),
            Action(
                name="CalculateCriticalPath", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="CheckMilestoneFloat", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="UpdateMilestoneDates",
                kwargs={
                    "milestone_id": "ms_002",
                    "new_target_date": "2024-04-20T00:00:00Z",
                },
            ),
            Action(
                name="CreateMilestoneDependency",
                kwargs={
                    "predecessor_id": "ms_001",
                    "successor_id": "ms_002",
                    "dependency_type": "finish_to_start",
                    "lag_days": 2,
                    "is_mandatory": True,
                },
            ),
            Action(
                name="CalculateCriticalPath", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="ValidateMilestoneReadiness", kwargs={"milestone_id": "ms_002"}
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
        instruction="Your role is to manage the critical path coordination for the Mobile App Launch project (proj_mobile_01). Begin by determining the critical path for the project. Inspect milestone float to flag any schedule risks. Then acquire the milestone details for ms_001 (Authentication Module). Since ms_001 is done, update its status to completed with 100% progress and green health, including status notes 'All authentication features implemented successfully', listing the finished deliverables: OAuth2 integration, User session management, and Security documentation. After making updates, recompute the critical path to observe any changes. Lastly, arrange a gate review for ms_002 with a review date set for April 10, 2024, marking all criteria as pass except 'No critical security issues' as fail, with reviewers emp_arch_01, emp_sec_dev_01, and emp_pm_03. Include review notes 'Minor security issues need resolution within 5 days'. Record the critical milestones count from the initial calculation, the health change from the status update, and the overall decision from the gate review.",
        actions=[
            Action(
                name="CalculateCriticalPath", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="CheckMilestoneFloat", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(name="GetMilestoneDetails", kwargs={"milestone_id": "ms_001"}),
            Action(
                name="UpdateMilestoneStatus",
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
                name="CalculateCriticalPath", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="CreateGateReview",
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
        instruction="You are setting up a new baseline for the AI Platform project (proj_ai_01). Initially, obtain the project timeline to view current milestones. Verify the schedule variance to determine if a baseline is present. As the project has merely an initial baseline, establish a new quarterly baseline labeled 'Q2 2024 AI Platform Baseline' with a quarterly baseline type, incorporating notes on ML model progress. Subsequently, retrieve the schedule variance once more to evaluate against the new baseline. Examine milestone float in order to gauge schedule health. Ultimately, perform an analysis of schedule compression for 20 days employing fast tracking to comprehend schedule flexibility. Compile a report detailing the total milestones from the timeline, the milestone count at the point of baseline creation, and the achieved reduction resulting from the compression analysis.",
        actions=[
            Action(
                name="GetProjectTimeline",
                kwargs={"project_id": "proj_ai_01", "include_dependencies": True},
            ),
            Action(name="GetScheduleVariance", kwargs={"project_id": "proj_ai_01"}),
            Action(
                name="CreateScheduleBaseline",
                kwargs={
                    "project_id": "proj_ai_01",
                    "baseline_name": "Q2 2024 AI Platform Baseline",
                    "baseline_type": "quarterly",
                    "notes": "ML model progress",
                },
            ),
            Action(name="GetScheduleVariance", kwargs={"project_id": "proj_ai_01"}),
            Action(name="CheckMilestoneFloat", kwargs={"project_id": "proj_ai_01"}),
            Action(
                name="AnalyzeScheduleCompression",
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
        instruction="You are modifying the schedule for the AI Platform project (proj_ai_01). To begin, retrieve the milestone details for ms_003 (ML Model Training). Verify the current status of the milestone float for the project. Due to improved GPU infrastructure availability, adjust the ms_003 dates by changing the start date to April 25, 2024, and target date to June 20, 2024. Following the date modification, reassess the milestone float to evaluate the impact. Conduct an analysis of schedule compression for 12 days using crashing to discover further optimization possibilities. Finally, revise the project buffer consumption by 5 days for ms_003 because of the schedule acceleration. Provide a report of the float days for ms_003 prior to the date adjustment, the quantity of impacted milestones due to the date update, and the consumption percentage from the buffer revision.",
        actions=[
            Action(name="GetMilestoneDetails", kwargs={"milestone_id": "ms_003"}),
            Action(name="CheckMilestoneFloat", kwargs={"project_id": "proj_ai_01"}),
            Action(
                name="UpdateMilestoneDates",
                kwargs={
                    "milestone_id": "ms_003",
                    "new_start_date": "2024-04-25T00:00:00Z",
                    "new_target_date": "2024-06-20T00:00:00Z",
                },
            ),
            Action(name="CheckMilestoneFloat", kwargs={"project_id": "proj_ai_01"}),
            Action(
                name="AnalyzeScheduleCompression",
                kwargs={
                    "project_id": "proj_ai_01",
                    "target_reduction": 12,
                    "compression_type": "crashing",
                },
            ),
            Action(
                name="UpdateBufferConsumption",
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
        instruction="You are supervising gate reviews for the Mobile App Launch project (proj_mobile_01). Initially verify the readiness of ms_002 (Phase 1 Gate Review). Retrieve the milestone dependencies to grasp prerequisites. Determine if any milestones in the project are delayed. Establish a gate review for ms_002 with review date April 10, 2024, ensuring Code coverage > 80% passes, Performance meets SLA passes, Architecture review approved passes, while No critical security issues fails. Engage reviewers emp_arch_01, emp_sec_dev_01, and emp_pm_03 with a conditional pass decision. Include action items: Fix SQL injection vulnerability and Update security documentation. Note that minor security issues require resolution within 5 days. Subsequent to the review, acquire milestone details for ms_002 to ascertain the status. Lastly, if there were readiness issues, formulate a recovery plan including crashing actions: security fixes for 2 impact days and documentation updates for 1 impact day, enlisting emp_sec_dev_02 as an additional resource with high feasibility and incorporate security code review and automated vulnerability scanning as risk mitigation. Communicate the readiness score, the decision from the gate review, and the days recuperated from the recovery plan.",
        actions=[
            Action(
                name="ValidateMilestoneReadiness", kwargs={"milestone_id": "ms_002"}
            ),
            Action(
                name="GetMilestoneDependencies", kwargs={"milestone_id": "ms_002"}
            ),
            Action(
                name="GetDelayedMilestones",
                kwargs={"project_id": "proj_mobile_01", "include_recovery_plans": True},
            ),
            Action(
                name="CreateGateReview",
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
            Action(name="GetMilestoneDetails", kwargs={"milestone_id": "ms_002"}),
            Action(
                name="CreateRecoveryPlan",
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
        You are overseeing external dependencies for the AI Platform project (proj_ai_01). Initially obtain the milestone
        details for ms_003 (ML Model Training). Examine the project timeline to comprehend the schedule. Incorporate an external
        dependency for Cloud GPU Infrastructure from CloudTech with expected delivery April 20, 2024, labeling it as critical
        with 5 contingency days and requiring 30 days notice (use 'ext_26845ca5' as dependency ID).
        Mark it as unconfirmed with contact info: GPU Support Team at gpu-support@cloudtech.com. After incorporating the dependency,
        verify milestone readiness for ms_003 to discern the impact. Update the external dependency status to confirmed
        once CloudTech affirms availability. Finally, evaluate milestone float to gauge schedule risk. Provide the milestone
        type from the initial details, the dependency ID created, and whether ms_003 stands ready after adding the
        dependency.
        """,
        actions=[
            Action(name="GetMilestoneDetails", kwargs={"milestone_id": "ms_003"}),
            Action(
                name="GetProjectTimeline",
                kwargs={"project_id": "proj_ai_01", "include_dependencies": False},
            ),
            Action(
                name="AddExternalDependency",
                kwargs={
                    "dependency_id": "ext_26845ca5",
                    "milestone_id": "ms_003",
                    "dependency_name": "Cloud GPU Infrastructure",
                    "provider": "CloudTech",
                    "expected_delivery_date": "2024-04-20T00:00:00Z",
                    "criticality": "critical",
                    "confirmed": False,
                    "contact_info": {
                        "name": "GPU Support Team",
                        "email": "gpu-support@cloudtech.com",
                    },
                    "contingency_days": 5,
                    "notice_days": 30,
                },
            ),
            Action(
                name="ValidateMilestoneReadiness", kwargs={"milestone_id": "ms_003"}
            ),
            Action(
                name="UpdateExternalDependencyStatus",
                kwargs={"dependency_id": "ext_26845ca5", "new_status": "confirmed"},
            ),
            Action(name="CheckMilestoneFloat", kwargs={"project_id": "proj_ai_01"}),
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
        instruction="As a recovery specialist for the Mobile App Launch project (proj_mobile_01), your first task is to handle milestone float to spot schedule pressures. Identify delayed milestones with included recovery plans to assess existing issues. Conduct an analysis of schedule compression over 14 days utilizing fast tracking to explore options. Given that ms_002 (Phase 1 Gate Review) has negative float, its readiness needs validation. Develop a recovery plan for ms_002 incorporating mixed actions: fast tracking UI/UX work for 4 impact days, crashing backend development for 3 impact days, and adding a senior architect for 2 impact days. Employ emp_arch_01 and emp_dev_15 as extra resources, with risk mitigation measures like hourly progress updates and a dedicated war room. Assess the feasibility as medium. Once the plan is created, adjust the phase gate buffer consumption by 2 days for ms_002, referencing the recovery plan execution. Document the number of delayed milestones initially identified, whether the recovery was devised within 48 hours, and the overall buffer consumed percentage.",
        actions=[
            Action(
                name="CheckMilestoneFloat", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="GetDelayedMilestones",
                kwargs={"project_id": "proj_mobile_01", "include_recovery_plans": True},
            ),
            Action(
                name="AnalyzeScheduleCompression",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "target_reduction": 14,
                    "compression_type": "fast_tracking",
                },
            ),
            Action(
                name="ValidateMilestoneReadiness", kwargs={"milestone_id": "ms_002"}
            ),
            Action(
                name="CreateRecoveryPlan",
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
                name="UpdateBufferConsumption",
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
        As an analyst for compression strategies within the Mobile App Launch project (proj_mobile_01), start by reviewing
        milestone float to pinpoint schedule pressures. Acquire the project timeline to understand the existing schedule.
        Evaluate schedule compression for 12 days by implementing crashing to examine the cost implications. Follow up
        with an evaluation of the same 12 days using fast tracking to juxtapose risk against cost. Revise ms_002 dates
        by moving the target date ahead by 7 days to April 8, 2024. Post date revision, reassess milestone float
        to observe the impact. Lastly, confirm the readiness of ms_002 subsequent to the schedule updates. Record the
        initial number of milestones with negative float, the reduction achieved from the crashing analysis, and the
        readiness score following the schedule adjustments.
        """,
        actions=[
            Action(
                name="CheckMilestoneFloat", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="GetProjectTimeline",
                kwargs={"project_id": "proj_mobile_01", "include_dependencies": True},
            ),
            Action(
                name="AnalyzeScheduleCompression",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "target_reduction": 12,
                    "compression_type": "crashing",
                },
            ),
            Action(
                name="AnalyzeScheduleCompression",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "target_reduction": 12,
                    "compression_type": "fast_tracking",
                },
            ),
            Action(
                name="UpdateMilestoneDates",
                kwargs={
                    "milestone_id": "ms_002",
                    "new_target_date": "2024-04-08T00:00:00Z",
                },
            ),
            Action(
                name="CheckMilestoneFloat", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="ValidateMilestoneReadiness", kwargs={"milestone_id": "ms_002"}
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
        instruction="You are overseeing buffer consumption for the Mobile App Launch project (proj_mobile_01). Initially, determine the schedule variance to assess baseline performance. Examine milestone float to pinpoint which milestones are utilizing float. With ms_001 authentication work needing extra testing, adjust the project buffer consumption by 3 days for ms_001, referencing additional security testing needs. Next, modify the phase gate buffer by 2 days for ms_002 due to complexities in gate review preparation. Verify the existence of any delayed milestones in the project. Should there be delayed milestones, further update the integration buffer by 1 day for ms_002, due to interface testing delays. After all alterations to buffers, assess schedule compression over 10 days by using crashing to identify recovery strategies. Finally, re-examine milestone float to evaluate the revised float status. Provide a report of the variance percentage for any delayed milestone from schedule variance, the necessity of risk review post buffer update, and the count of milestones affected from compression analysis.",
        actions=[
            Action(
                name="GetScheduleVariance", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="CheckMilestoneFloat", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="UpdateBufferConsumption",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "buffer_type": "project",
                    "days_consumed": 3,
                    "milestone_id": "ms_001",
                },
            ),
            Action(
                name="UpdateBufferConsumption",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "buffer_type": "phase_gate",
                    "days_consumed": 2,
                    "milestone_id": "ms_002",
                },
            ),
            Action(
                name="GetDelayedMilestones",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "include_recovery_plans": False,
                },
            ),
            Action(
                name="UpdateBufferConsumption",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "buffer_type": "integration",
                    "days_consumed": 1,
                    "milestone_id": "ms_002",
                },
            ),
            Action(
                name="AnalyzeScheduleCompression",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "target_reduction": 10,
                    "compression_type": "crashing",
                },
            ),
            Action(
                name="CheckMilestoneFloat", kwargs={"project_id": "proj_mobile_01"}
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
        You are streamlining float management for the AI Platform project (proj_ai_01). Begin by reviewing milestone float
        to comprehend the present schedule health. Acquire the project timeline to observe milestone specifics. If ms_003 possesses
        sufficient float (5 days or more), conduct schedule compression for 10 days utilizing crashing to discover opportunities.
        Based on the float examination, if no milestones exhibit negative float, establish a new milestone using template_004
        (Infrastructure Migration) titled 'AI Infrastructure Scaling' with a target date of July 30, 2024, assigned to
        emp_devops_02. Following the milestone creation, recheck milestone float to observe the effect. If the new
        milestone has in excess of 10 days float, adjust buffer consumption by 4 days for the project buffer citing
        proactive schedule optimization. Lastly, retrieve delayed milestones to verify no new delays have been introduced.
        Document the initial count of comfortable floats, the float condition of the newly created milestone, and
        the total delayed milestones at the conclusion.
        """,
        actions=[
            Action(name="CheckMilestoneFloat", kwargs={"project_id": "proj_ai_01"}),
            Action(
                name="GetProjectTimeline",
                kwargs={"project_id": "proj_ai_01", "include_dependencies": False},
            ),
            Action(
                name="AnalyzeScheduleCompression",
                kwargs={
                    "project_id": "proj_ai_01",
                    "target_reduction": 10,
                    "compression_type": "crashing",
                },
            ),
            Action(
                name="CreateMilestoneFromTemplate",
                kwargs={
                    "template_id": "template_004",
                    "project_id": "proj_ai_01",
                    "milestone_name": "AI Infrastructure Scaling",
                    "target_date": "2024-07-30T00:00:00Z",
                    "owner_id": "emp_devops_02",
                },
            ),
            Action(name="CheckMilestoneFloat", kwargs={"project_id": "proj_ai_01"}),
            Action(
                name="UpdateBufferConsumption",
                kwargs={
                    "project_id": "proj_ai_01",
                    "buffer_type": "project",
                    "days_consumed": 4,
                },
            ),
            Action(
                name="GetDelayedMilestones",
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
        Handle resource conflict resolution for the Mobile App Launch project (proj_mobile_01). Start by examining milestone
        float to determine the critical paths. Obtain the project timeline to comprehend resource requirements. Conduct resource
        leveling while adhering to constraints: Senior Developer is capped at 2 and React Native Developer at 1, employing
        the critical path priority strategy. As a result of the leveling, adjust
        milestone dates for any rescheduled milestone by adding 5 days to ms_002's targeted date to April 20, 2024,
        due to resource conflict settlement. Following any date modifications, perform a schedule compression analysis for 8 days utilizing
        fast tracking to make up for lost time. Re-check milestone float after completing all amendments. Finally,
        formulate a recovery plan for ms_002 by bringing on a contractor
        for 4 impact days and approving overtime for 3 impact days, engaging emp_dev_15 as additional resource with
        moderate feasibility. Incorporate risk mitigation strategies into the recovery plan. Report the number of conflicts
        identified from leveling, whether approval is necessary for the extension, and the risk multiplier from compression
        analysis.
        """,
        actions=[
            Action(
                name="CheckMilestoneFloat", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="GetProjectTimeline",
                kwargs={"project_id": "proj_mobile_01", "include_dependencies": True},
            ),
            Action(
                name="ApplyResourceLeveling",
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
                name="UpdateMilestoneDates",
                kwargs={
                    "milestone_id": "ms_002",
                    "new_target_date": "2024-04-20T00:00:00Z",
                },
            ),
            Action(
                name="AnalyzeScheduleCompression",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "target_reduction": 8,
                    "compression_type": "fast_tracking",
                },
            ),
            Action(
                name="CheckMilestoneFloat", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="CreateRecoveryPlan",
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
        Coordinate a comprehensive analysis of the timeline for the Mobile App Launch project (proj_mobile_01). Begin by retrieving the
        project timeline including dependencies to gain a thorough understanding of the schedule structure. Assess schedule variance to
        evaluate performance against the baseline. Access the project timeline once more without dependencies for a simplified view.
        Based on the timeline evaluation, confirm milestone ms_001's readiness. If ms_001 is deemed ready, update its
        status to complete with 100% progress and green health, with the note 'Milestone completed successfully', listing
        completed deliverables: OAuth2 integration, User session management, and Security documentation. Following
        the status update, identify any delayed milestones to recognize possible schedule issues. Prepare a gate review for milestone
        ms_002 on April 10 2024 with reviewers emp_arch_01 and emp_pm_03. The criteria results were 'Code coverage
        > 80%' pass, 'No critical security issues' pass, 'Performance meets SLA' fail,
        and 'Architecture review approved' pass. Add a note indicating 'Performance issues need resolution'. Finally, evaluate
        milestone float to determine overall schedule health. Report the number of completed milestones from
        the initial timeline metrics, the health alteration from the status update, and the zero float count from
        the final float evaluation.
        """,
        actions=[
            Action(
                name="GetProjectTimeline",
                kwargs={"project_id": "proj_mobile_01", "include_dependencies": True},
            ),
            Action(
                name="GetScheduleVariance", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="GetProjectTimeline",
                kwargs={"project_id": "proj_mobile_01", "include_dependencies": False},
            ),
            Action(
                name="ValidateMilestoneReadiness", kwargs={"milestone_id": "ms_001"}
            ),
            Action(
                name="UpdateMilestoneStatus",
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
                name="GetDelayedMilestones",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "include_recovery_plans": False,
                },
            ),
            Action(
                name="CreateGateReview",
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
                name="CheckMilestoneFloat", kwargs={"project_id": "proj_mobile_01"}
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
        Handle the management of external vendor deliveries for the AI Platform project (proj_ai_01). Begin by retrieving
        milestone details for ms_003 to comprehend its requirements. Verify if there are any external dependencies
        by consulting the project timeline. Record the status of external dependency ext_001 (Cloud GPU Infrastructure)
        as delayed. After marking it as delayed, examine the readiness of ms_003 to evaluate the impact. In response
        to the delay, introduce a new external dependency (use ext_002_ms_003 as dependency ID) for Alternative GPU
        Provider from Google Cloud with an anticipated delivery of April 25, 2024. Assign it high criticality with
        3 contingency days and a 15-day notice period. The point of contact should be Cloud Support at support@gcp.com.
        Following the addition of the backup dependency, change the original dependency ext_001 status to cancelled.
        Assess the milestone float to understand schedule impacts. Finally, update the status of the newly created
        external dependency (use the dependency_id from the add_external_dependency output) to confirmed. Report
        the initial milestone health details, the readiness status post delay, and the criticality of the new
        dependency added.
        """,
        actions=[
            Action(name="GetMilestoneDetails", kwargs={"milestone_id": "ms_003"}),
            Action(
                name="GetProjectTimeline",
                kwargs={"project_id": "proj_ai_01", "include_dependencies": True},
            ),
            Action(
                name="UpdateExternalDependencyStatus",
                kwargs={"dependency_id": "ext_001", "new_status": "delayed"},
            ),
            Action(
                name="ValidateMilestoneReadiness", kwargs={"milestone_id": "ms_003"}
            ),
            Action(
                name="AddExternalDependency",
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
                name="UpdateExternalDependencyStatus",
                kwargs={"dependency_id": "ext_001", "new_status": "cancelled"},
            ),
            Action(name="CheckMilestoneFloat", kwargs={"project_id": "proj_ai_01"}),
            Action(
                name="UpdateExternalDependencyStatus",
                kwargs={"dependency_id": "ext_002_ms_003", "new_status": "confirmed"},
            ),
        ],
        outputs=['"health": "green"', '"is_ready": false', '"criticality": "high"'],
    ),
    Task(
        annotator="0",
        user_id="enterprise_milestone_template_coordinator",
        instruction="""
        Coordinate the creation of milestones for the Enterprise Platform project (proj_enterprise_01). Start by obtaining
        the project timeline to review existing milestones (disregarding dependencies). Check milestone float to
        identify any scheduling gaps. Develop a milestone (use ms_XXY as ID) based on template_007 (Architecture Review Gate)
        named 'Enterprise Architecture Deep Dive' with a target date of May 25, 2024, assigned to emp_arch_01. Upon
        setting up this milestone, create another milestone (use ms_XYZ as ID) from template_005 (Data Privacy Compliance)
        labeled 'GDPR Compliance Review' with a planned date of June 10, 2024, assigned to emp_analyst_01. Obtain
        details for the initially created milestone to confirm its attributes. Reassess milestone float to understand
        the effect of the newly created milestones. Report the type of milestone for ms_XXY, along with the critical path
        count and the total milestones from the final float evaluation.
        """,
        actions=[
            Action(
                name="GetProjectTimeline",
                kwargs={
                    "project_id": "proj_enterprise_01",
                    "include_dependencies": False,
                },
            ),
            Action(
                name="CheckMilestoneFloat",
                kwargs={"project_id": "proj_enterprise_01"},
            ),
            Action(
                name="CreateMilestoneFromTemplate",
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
                name="CreateMilestoneFromTemplate",
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
                name="GetMilestoneDetails",
                kwargs={"milestone_id": "ms_XXY"},
            ),
            Action(
                name="CheckMilestoneFloat",
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
        As the milestone cleanup coordinator for the Mobile App Launch project (proj_mobile_01), handle the task of organizing project timelines. Initially, access the project timeline to view all milestones. Examine the details of ms_001 (Authentication Module) to confirm its completion status. Since ms_001 is finalized, archive this milestone. Post-archiving, fetch the project timeline again to ensure its removal from active milestones. Look for any delayed milestones requiring your attention. Generate a new milestone from template_006 (MVP Release), naming it 'Mobile App Beta Release', with a set completion date of May 15, 2024, and assign it to emp_pm_03 as a replacement for the archived milestone. Once the new milestone is created, check the milestone float to evaluate the schedule's health. Finally, conduct an analysis of schedule compression for a period of 7 days by employing crashing. Document the actual completion date of the milestone archived, the total milestones remaining after the archiving process, and assess whether the new milestone is a candidate for the critical path.
        """,
        actions=[
            Action(
                name="GetProjectTimeline",
                kwargs={"project_id": "proj_mobile_01", "include_dependencies": False},
            ),
            Action(name="GetMilestoneDetails", kwargs={"milestone_id": "ms_001"}),
            Action(
                name="ArchiveMilestone",
                kwargs={"milestone_id": "ms_001"},
            ),
            Action(
                name="GetProjectTimeline",
                kwargs={"project_id": "proj_mobile_01", "include_dependencies": False},
            ),
            Action(
                name="GetDelayedMilestones",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "include_recovery_plans": False,
                },
            ),
            Action(
                name="CreateMilestoneFromTemplate",
                kwargs={
                    "template_id": "template_006",
                    "project_id": "proj_mobile_01",
                    "milestone_name": "Mobile App Beta Release",
                    "target_date": "2024-05-15T00:00:00Z",
                    "owner_id": "emp_pm_03",
                },
            ),
            Action(
                name="CheckMilestoneFloat", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="AnalyzeScheduleCompression",
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
        Your role involves coordinating delay mitigation for the Mobile App Launch project (proj_mobile_01). Begin by retrieving delayed milestones that include recovery plans to gain insights into the existing issues. Review the schedule variance to determine the deviation from the baseline. If you encounter any delayed milestones, verify the readiness of the most pivotal one, ms_002. Depending on the discovered delays, use crashing to conduct a 15-day schedule compression analysis. Schedule a gate review for ms_002 with the review set on April 8, 2024; establish 'pass' to 'Expedite progress' as the criteria outcomes, also note the review comments as 'To expedite progress', and designate the reviewers as emp_arch_01 and emp_pm_03. Following the review, adjust the project buffer consumption for ms_002 by an additional 5 days, attributing this to delay recovery initiatives. Finally, retrieve the list of delayed milestones that lack recovery plans to verify the current status. Report the initial count of critical delays, whether ms_002 is equipped with a recovery plan, and the final count of delayed milestones.
        """,
        actions=[
            Action(
                name="GetDelayedMilestones",
                kwargs={"project_id": "proj_mobile_01", "include_recovery_plans": True},
            ),
            Action(
                name="GetScheduleVariance", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="ValidateMilestoneReadiness", kwargs={"milestone_id": "ms_002"}
            ),
            Action(
                name="AnalyzeScheduleCompression",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "target_reduction": 15,
                    "compression_type": "crashing",
                },
            ),
            Action(
                name="CreateGateReview",
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
                name="UpdateBufferConsumption",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "buffer_type": "project",
                    "days_consumed": 5,
                    "milestone_id": "ms_002",
                },
            ),
            Action(
                name="GetDelayedMilestones",
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
        Oversee milestone readiness for the Mobile App Launch project (proj_mobile_01). Initially, confirm the
        readiness of ms_002 (Phase 1 Gate Review). Obtain milestone details for ms_002 to comprehend its requirements.
        If the readiness score is 75 or lower after validation, examine milestone dependencies to pinpoint
        obstructing predecessors. Mark ms_001 as completed with 100% progress
        and green health, recording all deliverables such as OAuth2 integration, User session management, and Security
        documentation as completed. Following status updates, reassess ms_002 readiness to detect improvements. If external
        dependencies pose a challenge, include an external dependency for Security Audit Services with CyberAudit Technologies slated for
        completion by April 10, 2024, identified as high criticality with 3 contingency days, confirmed as true,
        along with contact information for Audit Team at audit@cyberaudit.com, and a 30-day notice period. Finally, if the readiness
        score remains under 100, arrange a gate review for ms_002 on April 10, 2024, ensuring all criteria
        are passed (Code coverage > 80%, No critical security issues, Performance meets SLA, Architecture review
        approved) with reviewers emp_arch_01 and emp_pm_03, noting 'All criteria met for phase gate'. Output the
        initial readiness score and the readiness status of ms_002 after all actions.
        """,
        actions=[
            Action(
                name="ValidateMilestoneReadiness", kwargs={"milestone_id": "ms_002"}
            ),
            Action(name="GetMilestoneDetails", kwargs={"milestone_id": "ms_002"}),
            Action(
                name="GetMilestoneDependencies", kwargs={"milestone_id": "ms_002"}
            ),
            Action(
                name="UpdateMilestoneStatus",
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
                name="ValidateMilestoneReadiness", kwargs={"milestone_id": "ms_002"}
            ),
            Action(
                name="AddExternalDependency",
                kwargs={
                    "milestone_id": "ms_002",
                    "dependency_name": "Security Audit Services",
                    "provider": "CyberAudit Technologies",
                    "expected_delivery_date": "2024-04-10T00:00:00Z",
                    "criticality": "high",
                    "confirmed": True,
                    "contact_info": {
                        "name": "Audit Team",
                        "email": "audit@cyberaudit.com",
                    },
                    "contingency_days": 3,
                    "notice_days": 30,
                },
            ),
            Action(
                name="CreateGateReview",
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
        Manage schedule variance for the Mobile App Launch project (proj_mobile_01). Begin by acquiring the
        schedule variance to evaluate current performance. Analyze milestone float to distinguish critical and non-critical
        milestones. Following the variance analysis, establish a new quarterly baseline (use bs_XXX as baseline ID and 2024-04-01T00:00:00Z as the creation date)
        titled 'Mobile Q2 2024 Adjusted Baseline' including notes on minor variance adjustments. After establishing the
        baseline, retrieve schedule variance once more against the revised baseline. Adjust ms_001
        dates by moving the target date 3 days forward to April 3, 2024 citing a minor amendment for variance control.
        Subsequently, decrease the project buffer consumption by 2 days for ms_001 due to the modification. Finally, verify
        milestone readiness for ms_002 to ensure dependencies remain unaffected. Report the number of on-track milestones
        from initial variance, the success status of the baseline creation, and the readiness score for ms_002.
        """,
        actions=[
            Action(
                name="GetScheduleVariance", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="CheckMilestoneFloat", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="CreateScheduleBaseline",
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
                name="GetScheduleVariance", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="UpdateMilestoneDates",
                kwargs={
                    "milestone_id": "ms_001",
                    "new_target_date": "2024-04-03T00:00:00Z",
                },
            ),
            Action(
                name="UpdateBufferConsumption",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "buffer_type": "project",
                    "days_consumed": 2,
                    "milestone_id": "ms_001",
                },
            ),
            Action(
                name="ValidateMilestoneReadiness", kwargs={"milestone_id": "ms_002"}
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
        instruction="You are overseeing recovery plan approvals for the Mobile App Launch project (proj_mobile_01). Begin by identifying delayed milestones that include recovery plans for pending approvals. Examine the milestone details for ms_002 to ascertain its current status. Since recovery_001 is awaiting approval for ms_002, assess its details by evaluating the milestone float for the project. As sh_003 (PMO Director), approve the recovery plan recovery_001 with a decision to endorse, adding approval notes about essential recovery needed for gate review delays. Following approval, adjust milestone dates for ms_002 to April 10, 2024 based on the recovery plan, referencing approved recovery plan implementation. Subsequently, amend the phase gate buffer consumption by 2 days for ms_002 due to recovery activities. Lastly, confirm the readiness of milestone ms_002 to ensure it's realigned with the schedule. Report if ms_002 has an associated recovery plan from the check of delayed milestones, the determination made regarding the recovery plan, and the buffer consumption percentage post-update.",
        actions=[
            Action(
                name="GetDelayedMilestones",
                kwargs={"project_id": "proj_mobile_01", "include_recovery_plans": True},
            ),
            Action(name="GetMilestoneDetails", kwargs={"milestone_id": "ms_002"}),
            Action(
                name="CheckMilestoneFloat", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="ApproveRecoveryPlan",
                kwargs={
                    "plan_id": "recovery_001",
                    "decision": "approve",
                    "approver_id": "sh_003",
                    "approval_notes": "Critical recovery needed for gate review delays",
                },
            ),
            Action(
                name="UpdateMilestoneDates",
                kwargs={
                    "milestone_id": "ms_002",
                    "new_target_date": "2024-04-10T00:00:00Z",
                },
            ),
            Action(
                name="UpdateBufferConsumption",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "buffer_type": "phase_gate",
                    "days_consumed": 2,
                    "milestone_id": "ms_002",
                },
            ),
            Action(
                name="ValidateMilestoneReadiness", kwargs={"milestone_id": "ms_002"}
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
        instruction="You are responsible for evaluating milestone health for the Mobile App Launch project (proj_mobile_01). Begin by acquiring milestone details for ms_001 to assess its current condition. Next, obtain details for ms_002 to contrast progress. Review the project schedule variance to understand baseline performance. If ms_002 exhibits a health status of yellow or red based on the details, organize a gate review for ms_002 with the review date of April 5, 2024, indicating Code coverage > 80% as a pass, Performance meets SLA as a pass, but No critical security issues as a fail, and Architecture review approved as a pass. Utilize reviewers emp_arch_01 and emp_pm_03. Incorporate review notes regarding security issues identified during the health audit. Post review, if ms_002 progress is below 70%, modify its status to in_progress with 65% progress and yellow health, noting impediments due to technical challenges. Then, investigate schedule compression for 7 days using crashing. Finally, if the initial check shows ms_001 status as completed, archive it. Report the health status of ms_002 from initial details, the comprehensive decision from any gate review instituted, and the feasibility of the compression.",
        actions=[
            Action(name="GetMilestoneDetails", kwargs={"milestone_id": "ms_001"}),
            Action(name="GetMilestoneDetails", kwargs={"milestone_id": "ms_002"}),
            Action(
                name="GetScheduleVariance", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="CreateGateReview",
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
                name="UpdateMilestoneStatus",
                kwargs={
                    "milestone_id": "ms_002",
                    "new_status": "in_progress",
                    "progress_percentage": 65,
                    "health": "yellow",
                    "status_notes": "Slow progress due to technical challenges",
                },
            ),
            Action(
                name="AnalyzeScheduleCompression",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "target_reduction": 7,
                    "compression_type": "crashing",
                },
            ),
            Action(
                name="ArchiveMilestone",
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
        Develop strategic milestones for the Enterprise Platform project (proj_enterprise_01). Begin by retrieving the
        project timeline to gain insight into existing milestones. Examine milestone float to pinpoint schedule gaps. Establish a
        new major milestone (use 'ms_ABC' as ID) titled 'Enterprise Security Architecture Review' with a target
        date May 15, 2024, and start date April 15, 2024, having the description
        'Comprehensive security architecture validation for enterprise platform'. Deliverables must include the Security
        architecture document, Threat model analysis, and Compliance checklist. Assign the owner as emp_arch_01 with gate
        criteria: Addressed security vulnerabilities, Approved architecture patterns, and Assessed performance impact.
        Output the created milestone buffer consumption and health.
        """,
        actions=[
            Action(
                name="GetProjectTimeline",
                kwargs={
                    "project_id": "proj_enterprise_01",
                    "include_dependencies": False,
                },
            ),
            Action(
                name="CheckMilestoneFloat",
                kwargs={"project_id": "proj_enterprise_01"},
            ),
            Action(
                name="CreateMilestone",
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
        instruction="""Oversee milestone progress for the Mobile App
        Launch project (proj_mobile_01). Initially, access milestone details for ms_002
        (Phase 1 Gate Review) to understand the current status. Confirm its readiness to
        ascertain completion needs. Given the team's significant advancement,
        update ms_002 status to in_progress with 85% completion and
        designate yellow health, identifying completed deliverables: Core features complete
        and Performance benchmarks met. Add notes on the status concerning the pending security
        review. Following the status update, inspect milestone float to determine if
        the progress influences schedule pressure. Retrieve delayed milestones to check if
        ms_002 remains delayed. If ms_002 continues to be delayed,
        schedule a gate review for it with a review date April 12, 2024, qualifying
        Code coverage > 80% as pass, No critical security issues as fail,
        Performance meets SLA as pass, and Architecture review approved as pass,
        with emp_arch_01 and emp_pm_03 as reviewers. Include review notes that security
        issues were detected and remedial actions are in progress. Ultimately, if a
        gate review was initiated, revise ms_002 status to indicate 90% progress with
        status notes reflecting the scheduled gate review. Provide the initial progress
        percentage and the health change from the first update.""",
        actions=[
            Action(name="GetMilestoneDetails", kwargs={"milestone_id": "ms_002"}),
            Action(
                name="ValidateMilestoneReadiness", kwargs={"milestone_id": "ms_002"}
            ),
            Action(
                name="UpdateMilestoneStatus",
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
                name="CheckMilestoneFloat", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="GetDelayedMilestones",
                kwargs={
                    "project_id": "proj_mobile_01",
                },
            ),
            Action(
                name="CreateGateReview",
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
                name="UpdateMilestoneStatus",
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
        You are overseeing the coordination of dependencies between projects. Initially, obtain the details of the milestone for ms_003 (ML Model
        Training) in the AI Platform project. Examine the milestone float for proj_ai_01 to assess the scheduling flexibility.
        Retrieve the dependencies of milestone ms_003 to understand the current relations. Since the ML training depends on
        completed authentication, establish a dependency such that ms_001 (Authentication Module) from the Mobile project must be finished
        prior to ms_003 with a 10-day lag, making it essential and include notes regarding security requirements for accessing ML.
        Reassess the milestone float to locate any newly critical paths. Evaluate schedule compression for 15 days using crashing and provide
        the count of days reduced.
        """,
        actions=[
            Action(name="GetMilestoneDetails", kwargs={"milestone_id": "ms_003"}),
            Action(name="CheckMilestoneFloat", kwargs={"project_id": "proj_ai_01"}),
            Action(
                name="GetMilestoneDependencies", kwargs={"milestone_id": "ms_003"}
            ),
            Action(
                name="CreateMilestoneDependency",
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
            Action(name="CheckMilestoneFloat", kwargs={"project_id": "proj_ai_01"}),
            Action(
                name="AnalyzeScheduleCompression",
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
        You are in charge of the critical path management for the Mobile App Launch project (proj_mobile_01). Begin by calculating the
        critical path to set a baseline. Acquire milestone details for ms_002 to comprehend its role. If ms_002 is
        part of the critical path, establish an external dependency for Security Audit Certification from SecureTest
        Systems with an anticipated delivery on April 5, 2024, assigning it high criticality with 3 contingent days. Set
        confirmation as False, utilizing a 30-day notice period. For contact details, employ Audit Team with the email
        audit@cyberaudit.com. After the dependency addition, recompute the critical path to assess its impact.
        Based on the new critical path, if the total duration surpasses 20 days, conduct schedule compression for 15
        days through crashing. Recheck the milestone float following these modifications. If ms_001 maintains zero float, adjust its
        schedule by advancing the start date to February 25, 2024, to create a schedule buffer. Finally, recompute
        the critical path once more to validate the optimization. Report the initial count of critical tasks, the
        total duration following the dependency addition, and the final count of critical milestones after all optimizations.
        """,
        actions=[
            Action(
                name="CalculateCriticalPath", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(name="GetMilestoneDetails", kwargs={"milestone_id": "ms_002"}),
            Action(
                name="AddExternalDependency",
                kwargs={
                    "milestone_id": "ms_002",
                    "dependency_name": "Security Audit Certification",
                    "provider": "CyberAudit Technologies",
                    "expected_delivery_date": "2024-04-05T00:00:00Z",
                    "criticality": "high",
                    "confirmed": False,
                    "contact_info": {
                        "name": "Audit Team",
                        "email": "audit@cyberaudit.com",
                    },
                    "contingency_days": 3,
                    "notice_days": 30,
                },
            ),
            Action(
                name="CalculateCriticalPath", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="AnalyzeScheduleCompression",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "target_reduction": 15,
                    "compression_type": "crashing",
                },
            ),
            Action(
                name="CheckMilestoneFloat", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="UpdateMilestoneDates",
                kwargs={
                    "milestone_id": "ms_001",
                    "new_start_date": "2024-02-25T00:00:00Z",
                },
            ),
            Action(
                name="CalculateCriticalPath", kwargs={"project_id": "proj_mobile_01"}
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
        Handle the baseline versions for the Mobile App Launch project (proj_mobile_01). Obtain the schedule
        variance initially to evaluate the current baseline performance. Review the milestone float to pinpoint any significant variances. Establish a
        new schedule baseline titled 'Mobile Q2 2024
        Recovery Baseline' with a quarterly type, including notes on addressing schedule delays (ensure the creation date is 2024-04-15T00:00:00Z).
        Include PMO approval since
        this represents the second quarterly baseline. After setting up the new baseline, acquire schedule variance once more to confirm it's aligned with the new baseline. Assess schedule compression for 10 days by crashing to strategize recovery.
        Present the count of delayed milestones.
        """,
        actions=[
            Action(
                name="GetScheduleVariance", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="CheckMilestoneFloat", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="CreateScheduleBaseline",
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
                name="GetScheduleVariance", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="AnalyzeScheduleCompression",
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
        instruction="Coordinate the schedule acceleration for the AI Platform project (proj_ai_01). Initially, gather information on milestone ms_003 (ML Model Training). Access the current schedule variance to assess baseline effectiveness. Given the early availability of cloud resources, adjust the dates for ms_003 by moving both the start and target dates earlier: the start is now April 20, 2024, with the target set for June 15, 2024, referencing 'Early cloud resource availability'. Following this update, compute the critical path to examine the schedule impacts. Evaluate the milestone float to ensure that acceleration has not introduced negative float. Should ms_003 now exhibit negative float, establish an external dependency on 'GPU Cluster Allocation' from DataCenter Corp with an anticipated delivery on April 15, 2024, noting it as critical with 3 contingency days; confirmed status true; contact information listing name 'DC Operations', email 'ops@datacenter.com', and 14 notice days. Subsequently, confirm the milestone readiness for ms_003. Conclude by adjusting the project buffer consumption by 7 days due to the accelerated timeline, linking it to milestone ms_003. Report on the number of affected milestones from the date adjustment, the necessity of a critical path update, and the buffer remaining after consumption.",
        actions=[
            Action(name="GetMilestoneDetails", kwargs={"milestone_id": "ms_003"}),
            Action(name="GetScheduleVariance", kwargs={"project_id": "proj_ai_01"}),
            Action(
                name="UpdateMilestoneDates",
                kwargs={
                    "milestone_id": "ms_003",
                    "new_start_date": "2024-04-20T00:00:00Z",
                    "new_target_date": "2024-06-15T00:00:00Z",
                },
            ),
            Action(name="CalculateCriticalPath", kwargs={"project_id": "proj_ai_01"}),
            Action(name="CheckMilestoneFloat", kwargs={"project_id": "proj_ai_01"}),
            Action(
                name="AddExternalDependency",
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
                name="ValidateMilestoneReadiness", kwargs={"milestone_id": "ms_003"}
            ),
            Action(
                name="UpdateBufferConsumption",
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
        instruction="You are overseeing gate reviews for the AI Platform project (proj_ai_01). Initially, obtain milestone details for ms_003 (ML Model Training) to verify its gate criteria. Confirm the preparedness of ms_003 prior to the review. Schedule a gate review for ms_003 with the review date set for June 20, 2024, where Model accuracy > 95% passes, Training data validated passes, but Bias testing complete fails. Employ reviewers emp_data_01, sh_004, and emp_analyst_01. Add action items: Complete bias testing with diverse datasets and Document bias mitigation strategies. Once the review concludes, reassess milestone details to observe any changes in health status. As this is a failed review, adjust the milestone dates by extending the target date by 14 days to July 14, 2024, citing the gate review remediation period. Subsequently, arrange another gate review for the new date July 5, 2024, where all criteria are met this time. Lastly, evaluate milestone float after all modifications. Provide the gate criteria count from the initial details, the outcome of the first gate review, and determine if the second review led to escalation.",
        actions=[
            Action(name="GetMilestoneDetails", kwargs={"milestone_id": "ms_003"}),
            Action(
                name="ValidateMilestoneReadiness", kwargs={"milestone_id": "ms_003"}
            ),
            Action(
                name="CreateGateReview",
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
            Action(name="GetMilestoneDetails", kwargs={"milestone_id": "ms_003"}),
            Action(
                name="UpdateMilestoneDates",
                kwargs={
                    "milestone_id": "ms_003",
                    "new_target_date": "2024-07-14T00:00:00Z",
                },
            ),
            Action(
                name="CreateGateReview",
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
            Action(name="CheckMilestoneFloat", kwargs={"project_id": "proj_ai_01"}),
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
        You are managing external vendor dependencies for the Mobile App Launch project (proj_mobile_01).
        Begin by obtaining milestone details for ms_002 (Phase 1 Gate Review). Examine the project timeline to grasp
        schedule constraints. Incorporate an external dependency (use 'ext_f9444b49' as dependency ID),
        for Payment Gateway Integration from Stripe expecting delivery by April 5, 2024, categorizing it as high criticality with 3 contingency days. Initially set it as unconfirmed
         with contact info: Integration Team at integrations@stripe.com, requiring 14 days notice. Following the addition of the
         dependency, check milestone readiness for ms_002 to determine the impact of the unconfirmed dependency. Modify
         the external dependency status to delivered with the actual delivery date of April 3, 2024. Then reassess milestone
         readiness to identify any improvement. Lastly, change its status to
         in_progress with 75% completion and yellow health, indicating Payment gateway integration was delivered early.
         Report the dependency ID created, determine whether ms_002 was ready before delivery confirmation, and note the health
         status after the update.
         """,
        actions=[
            Action(name="GetMilestoneDetails", kwargs={"milestone_id": "ms_002"}),
            Action(
                name="GetProjectTimeline",
                kwargs={"project_id": "proj_mobile_01", "include_dependencies": False},
            ),
            Action(
                name="AddExternalDependency",
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
                name="ValidateMilestoneReadiness", kwargs={"milestone_id": "ms_002"}
            ),
            Action(
                name="UpdateExternalDependencyStatus",
                kwargs={
                    "dependency_id": "ext_f9444b49",
                    "new_status": "delivered",
                    "actual_delivery_date": "2024-04-03T00:00:00Z",
                },
            ),
            Action(
                name="ValidateMilestoneReadiness", kwargs={"milestone_id": "ms_002"}
            ),
            Action(
                name="UpdateMilestoneStatus",
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
        Handle the management of external risks for the AI Platform project (proj_ai_01). Begin by retrieving milestone details for ms_003
        (ML Model Training). Inspect any existing external dependencies linked to this milestone. Introduce a new external dependency (apply 'ext_16299417' as dependency ID)
        for GPU Cluster Expansion from Infrastructure Corp, anticipated on May 15, 2024, tagging it with high criticality along with 7
        contingency days and 45 notice days. The contact point is the Infrastructure Team at infra@datacenter.com, phone 555-0123.
        Once added, confirm milestone readiness for ms_003 to evaluate the impact. Since external dependencies can pose risks,
        formulate a recovery plan for ms_003 utilizing a blend of strategies: scope reduction through postponing advanced features (6 impact days),
        fast-tracking model validation (4 impact days), and crashing by employing cloud GPU bursting (5 impact days).
        Incorporate emp_data_01 and emp_data_02 as additional resources with risk mitigation practices, including vendor escalation
        procedures and backup cloud provider plans. Due to external constraints, set feasibility as low. Upon completing the recovery plan,
        adjust the external dependency status to delayed (utilize the dependency_id from the add_external_dependency outcome).
        Lastly, inspect delayed milestones to determine the overall project impact. Report the milestone health from initial details,
        the total impact days from the recovery plan, and if ms_003 is featured in delayed milestones.
        """,
        actions=[
            Action(name="GetMilestoneDetails", kwargs={"milestone_id": "ms_003"}),
            Action(
                name="AddExternalDependency",
                kwargs={
                    "dependency_id": "ext_16299417",
                    "milestone_id": "ms_003",
                    "dependency_name": "GPU Cluster Expansion",
                    "provider": "Infrastructure Corp",
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
                name="ValidateMilestoneReadiness", kwargs={"milestone_id": "ms_003"}
            ),
            Action(
                name="CreateRecoveryPlan",
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
                name="UpdateExternalDependencyStatus",
                kwargs={"dependency_id": "ext_16299417", "new_status": "delayed"},
            ),
            Action(
                name="GetDelayedMilestones",
                kwargs={"project_id": "proj_ai_01", "include_recovery_plans": True},
            ),
        ],
        outputs=['"health": "green"', '"total_impact_days": 15', '"delayed_count": 0'],
    ),
    Task(
        annotator="0",
        user_id="mobile_incremental_compression_analyst",
        instruction="""
        Coordinate the analysis of incremental compression options for the Mobile App Launch project (proj_mobile_01).
        Start by obtaining the schedule variance to assess baseline performance. Examine milestone float to spot
        potential compression candidates. Execute a schedule compression analysis for 5 days using crashing to evaluate minimal compression.
        Repeat the analysis for 10 days utilizing crashing. Then, perform
        compression analysis for 10 days by applying fast tracking to contrast methods. From the analyses, if fast tracking
        achieves a reduction of at least 8 days, arrange a gate review for milestone ms_002 on April 12, 2024, with
        reviewers emp_arch_01 and emp_pm_03. For criteria results, record a "pass" for these: code coverage > 80%,
        absence of critical security issues, performance meeting SLA, and architecture review approval.
        Additionally, append the note: 'Fast track implementation approved based on compression analysis'. Modify
        the project buffer by 4 days, indicating the recognition of an optimal
        compression point. Finally, affirm milestone readiness for ms_002 following all modifications. You need
        to determine the cost incurred from 5-day crashing, the feasibility of a 10-day fast tracking, and the readiness
        score post-changes.
        """,
        actions=[
            Action(
                name="GetScheduleVariance", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="CheckMilestoneFloat", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="AnalyzeScheduleCompression",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "target_reduction": 5,
                    "compression_type": "crashing",
                },
            ),
            Action(
                name="AnalyzeScheduleCompression",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "target_reduction": 10,
                    "compression_type": "crashing",
                },
            ),
            Action(
                name="AnalyzeScheduleCompression",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "target_reduction": 10,
                    "compression_type": "fast_tracking",
                },
            ),
            Action(
                name="CreateGateReview",
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
                name="UpdateBufferConsumption",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "buffer_type": "project",
                    "days_consumed": 4,
                    "milestone_id": "ms_002",
                },
            ),
            Action(
                name="ValidateMilestoneReadiness", kwargs={"milestone_id": "ms_002"}
            ),
        ],
        outputs=['"total_cost": 2500', '"feasible": true', '"readiness_score": 75'],
    ),
    Task(
        annotator="0",
        user_id="ai_platform_buffer_risk_manager",
        instruction="""
        Oversee buffer risks for the AI Platform project (proj_ai_01). Begin by assessing the schedule variance to
        examine baseline performance. Evaluate milestone float to pinpoint schedule pressures. Due to the complexity
        of ML model training, adjust the project buffer consumption by 8 days for ms_003, citing the machine learning
        model complexity surpassing estimates. Next, scrutinize schedule compression for 15 days using crashing to 
        evaluate cost implications. In view of the buffer adjustment, modify the integration buffer by 3 days for 
        ms_003, citing model integration complexity, but ensure inclusion of change request ID CR-2024-AI-001 as
        this is for scope addition. Following the buffer adjustments, ascertain milestone readiness for ms_003.
        Ultimately, devise a recovery plan for ms_003 using crashing: expedited training for 5 impact days and
        simultaneous validation for 4 impact days, employing emp_data_01 and emp_data_02 as supplementary resources
        with high feasibility and implementing 24/7 training monitoring alongside automated validation pipelines for
        risk mitigation. Provide the initial variance percentage for ms_003, confirm if a risk review was initiated
        after the first buffer update, and specify the total days regained from the recovery plan.
        """,
        actions=[
            Action(name="GetScheduleVariance", kwargs={"project_id": "proj_ai_01"}),
            Action(name="CheckMilestoneFloat", kwargs={"project_id": "proj_ai_01"}),
            Action(
                name="UpdateBufferConsumption",
                kwargs={
                    "project_id": "proj_ai_01",
                    "buffer_type": "project",
                    "days_consumed": 8,
                    "milestone_id": "ms_003",
                },
            ),
            Action(
                name="AnalyzeScheduleCompression",
                kwargs={
                    "project_id": "proj_ai_01",
                    "target_reduction": 15,
                    "compression_type": "crashing",
                },
            ),
            Action(
                name="UpdateBufferConsumption",
                kwargs={
                    "project_id": "proj_ai_01",
                    "buffer_type": "integration",
                    "days_consumed": 3,
                    "milestone_id": "ms_003",
                    "change_request_id": "CR-2024-AI-001",
                },
            ),
            Action(
                name="ValidateMilestoneReadiness", kwargs={"milestone_id": "ms_003"}
            ),
            Action(
                name="CreateRecoveryPlan",
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
        Conduct an analysis of dependency gaps for the AI Platform project (proj_ai_01). Start by retrieving
        milestone dependencies for ms_003 (ML Model Training) to verify its prerequisites. Acquire the project timeline
        to review all milestones and their interconnections. Given that ML model training necessitates infrastructure,
        introduce an external dependency (use ext_35c30d1d as dependency ID) for GPU Cluster Setup from DataCenter
        Corp, expected by May 1, 2024, labeling it as critical with 7 contingency days and 45 notice days included.
        Inspect milestone float to determine if the newly added dependency impacts the schedule. Confirm milestone
        readiness for ms_003 to assess the effect of the external dependency. Finally, if ms_003 is deemed unready
        due to this external dependency, change the external dependency status to confirmed to address the readiness
        issue. The dependency_id from the add_external_dependency action output should be employed for the update.
        Establish the initial count of predecessors for ms_003, the critical level of the external dependency added,
        and determine whether ms_003 has a positive float.
        """,
        actions=[
            Action(
                name="GetMilestoneDependencies", kwargs={"milestone_id": "ms_003"}
            ),
            Action(
                name="GetProjectTimeline",
                kwargs={"project_id": "proj_ai_01", "include_dependencies": True},
            ),
            Action(
                name="AddExternalDependency",
                kwargs={
                    "milestone_id": "ms_003",
                    "dependency_id": "ext_35c30d1d",
                    "dependency_name": "GPU Cluster Setup",
                    "provider": "Infrastructure Corp",
                    "expected_delivery_date": "2024-05-01T00:00:00Z",
                    "criticality": "critical",
                    "confirmed": False,
                    "contingency_days": 7,
                    "notice_days": 45,
                },
            ),
            Action(name="CheckMilestoneFloat", kwargs={"project_id": "proj_ai_01"}),
            Action(
                name="ValidateMilestoneReadiness", kwargs={"milestone_id": "ms_003"}
            ),
            Action(
                name="UpdateExternalDependencyStatus",
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
        You are overseeing float risks concerning the Mobile App Launch project
        (proj_mobile_01). Initiate by checking the milestone float to determine baseline risk
        levels. Obtain delayed milestones including their recovery plans to grasp current issues. If there
        are milestones with negative float, confirm readiness for the milestone
        with the most negative float (ms_002). From the float analysis, should more
        than half the milestones possess zero or negative float, adjust buffer
        consumption by 5 days for the integration buffer due to critical path
        pressure across numerous milestones. Examine milestone float once more subsequent to
        buffer adjustment. Establish an external dependency for ms_002: Testing
        Environment from Cloud Provider anticipated on April 5, 2024, denoted as high
        criticality, inclusive of 3 contingency days, unconfirmed status, with Cloud
        Support contact (name: Cloud Support, email: support@cloudprovider.com)
        and 14 notice days. Conclusively, evaluate schedule compression for 15 days
        utilizing crashing to explore emergency alternatives. Inform me of the initial
        zero float count, the risk level for the milestone with the most negative
        float, and if the critical path count heightened after buffer
        consumption.""",
        actions=[
            Action(
                name="CheckMilestoneFloat", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="GetDelayedMilestones",
                kwargs={"project_id": "proj_mobile_01", "include_recovery_plans": True},
            ),
            Action(
                name="ValidateMilestoneReadiness", kwargs={"milestone_id": "ms_002"}
            ),
            Action(
                name="UpdateBufferConsumption",
                kwargs={
                    "project_id": "proj_mobile_01",
                    "buffer_type": "integration",
                    "days_consumed": 5,
                    "milestone_id": "ms_002",
                },
            ),
            Action(
                name="CheckMilestoneFloat", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="AddExternalDependency",
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
                name="AnalyzeScheduleCompression",
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
        You are enhancing resource allocation within the Enterprise Platform project (proj_enterprise_01). Begin by obtaining the
        project timeline to comprehend resource requirements. Develop a milestone (use 'ms_524727c0' as milestone ID)
        from template_007 (Architecture Review
        Gate) labeled 'Enterprise Security Architecture Review' with a target date of August 15, 2024, assigned to emp_arch_01.
        Implement resource leveling with constraints: Senior Architect restricted to 1 and Security Developer capped at 2,
        using the business value priority method. If milestones were adjusted during leveling, review milestone float to
        evaluate the impact. Following the leveling outcomes,
        amend the project buffer consumption by 3 days for milestone ms_524727c0 citing resource optimization trade-offs
        from leveling. Next, create a schedule baseline titled 'Enterprise Resource Optimized Baseline' with a quarterly
        type and 'Baseline after resource leveling impacts' as notes. Lastly, obtain the schedule variance to compare against the new
        baseline. Let me know the number of milestones affected by leveling, the extension percentage, and the milestone
        count in the new baseline.""",
        actions=[
            Action(
                name="GetProjectTimeline",
                kwargs={
                    "project_id": "proj_enterprise_01",
                    "include_dependencies": False,
                },
            ),
            Action(
                name="CreateMilestoneFromTemplate",
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
                name="ApplyResourceLeveling",
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
                name="CheckMilestoneFloat",
                kwargs={"project_id": "proj_enterprise_01"},
            ),
            Action(
                name="UpdateBufferConsumption",
                kwargs={
                    "project_id": "proj_enterprise_01",
                    "buffer_type": "project",
                    "days_consumed": 3,
                    "milestone_id": "ms_524727c0",
                },
            ),
            Action(
                name="CreateScheduleBaseline",
                kwargs={
                    "project_id": "proj_enterprise_01",
                    "baseline_name": "Enterprise Resource Optimized Baseline",
                    "baseline_type": "quarterly",
                    "notes": "Baseline after resource leveling impacts",
                },
            ),
            Action(
                name="GetScheduleVariance",
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
