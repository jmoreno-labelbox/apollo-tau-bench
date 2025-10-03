from tau_bench.types import Action, Task

TASKS = [
    Task(
        annotator="0",
        user_id="cross_team_coordination",
        instruction="""As the program coordinator, handle task initiation for team_mobile_01's
        sprint_003, which depends on the Web team. Review the velocity stats
        from the last 3 sprints for team_mobile_01 and team_dev_01. Identify
        high priority tasks in the backlog, ensuring the resolution of
        task_007's dependencies. Escalate the priority to critical if blocked,
        and coordinate the setup of a high-priority task "Cross-team sync meeting"
        with 3 story points assigned to emp_pm_03 for sprint_003. Transition
        task_007 and task_018 into sprint_003. Assess emp_dev_03's workload,
        and compile a report on both teams' velocities along with the total
        story points planned for sprint_003.""",
        actions=[
            Action(
                name="GetTeamVelocity",
                kwargs={"team_id": "team_mobile_01", "last_n_sprints": 3},
            ),
            Action(
                name="GetTeamVelocity",
                kwargs={"team_id": "team_dev_01", "last_n_sprints": 3},
            ),
            Action(name="GetBacklogTasks", kwargs={"priority": "high"}),
            Action(name="SearchTasks", kwargs={"task_id": "task_007"}),
            Action(name="GetTaskDetails", kwargs={"task_id": "task_007"}),
            Action(name="SearchTasks", kwargs={"task_id": "task_003"}),
            Action(
                name="UpdateTaskPriority",
                kwargs={
                    "task_id": "task_007",
                    "new_priority": "critical",
                },
            ),
            Action(
                name="CreateTask",
                kwargs={
                    "title": "Cross-team sync meeting",
                    "assignee_id": "emp_pm_03",
                    "priority": "high",
                    "story_points": 3,
                    "sprint_id": "sprint_003",
                },
            ),
            Action(
                name="BulkMoveTasksToSprint",
                kwargs={
                    "task_ids": ["task_007", "task_018"],
                    "target_sprint_id": "sprint_003",
                },
            ),
            Action(
                name="GetEmployeeWorkload",
                kwargs={"employee_id": "emp_dev_03", "sprint_id": "sprint_003"},
            ),
            Action(
                name="CalculateTeamCapacity",
                kwargs={"team_id": "team_mobile_01", "sprint_id": "sprint_003"},
            ),
            Action(name="GetSprintDetails", kwargs={"sprint_id": "sprint_003"}),
        ],
        outputs=[
            '"average_velocity": 0',
            '"average_velocity": 18.0',
            '"planned_story_points": 19',
        ],
    ),
    Task(
        annotator="0",
        user_id="sprint_closure_process",
        instruction="""Act as the scrum master closing sprint_001 for
        team_analytics_01. Verify time logging compliance to detect
        non-compliant tasks, log 4 hours for the first identified
        non-compliant task to the responsible employee, finalize remaining
        in-progress or todo tasks by marking them done, update the sprint
        status to completed (unless it's already marked as such), and initiate
        a retrospective with topics: "Data pipeline setup was smooth", and
        "Estimates need to be more precise". Provide the final velocity
        and count of non-compliant tasks.""",
        actions=[
            Action(name="GenerateSprintReport", kwargs={"sprint_id": "sprint_001"}),
            Action(
                name="CheckTimeLoggingCompliance", kwargs={"sprint_id": "sprint_001"}
            ),
            Action(
                name="GetTaskDetails",
                kwargs={
                    "task_id": "task_001",
                },
            ),
            Action(
                name="LogTimeOnTask",
                kwargs={
                    "task_id": "task_001",
                    "hours_logged": 4,
                    "employee_id": "emp_dev_05",
                },
            ),
            Action(
                name="SearchTasks",
                kwargs={
                    "sprint_id": "sprint_001",
                }
            ),
            Action(
                name="UpdateTaskStatus",
                kwargs={
                    "task_id": "task_006",
                    "new_status": "done"
                },
            ),
            Action(
                name="UpdateSprintStatus",
                kwargs={"sprint_id": "sprint_001", "new_status": "completed"},
            ),
            Action(
                name="CreateSprintRetrospective",
                kwargs={
                    "sprint_id": "sprint_001",
                    "what_went_well": [
                        "Data pipeline setup was smooth",
                    ],
                    "what_needs_improvement": [
                        "Estimates need to be more precise",
                    ],
                },
            ),
            Action(name="GetSprintDetails", kwargs={"sprint_id": "sprint_001"}),
        ],
        outputs=['"velocity": 31', '"non_compliant_count": 5', '"status": "completed"'],
    ),
    Task(
        annotator="0",
        user_id="sprint_crisis_manager",
        instruction="""As the development manager in charge of
        sprint_002, address the risk status. Elevate blocked task_005 to emp_head_eng. Initiate a
        critical task titled "Emergency API hotfix" with the description "Fix critical
        production API bug affecting customers" for emp_dev_21, allocating 5 story
        points in sprint_002. Transfer task_010 to emp_dev_15. Register 6 hours on
        task_003 for emp_dev_21 with remarks "API endpoint debugging and fixes".
        Confirm all dependencies and blocking arrangements for task_004 are completed. Resolve
        any blocking issues for task_004 with the resolution note "<task_id> completed".
        Subsequently, modify task_004 status to in_progress. Inform about the total number of blocked tasks.""",
        actions=[
            Action(
                name="EscalateTask",
                kwargs={
                    "task_id": "task_005",
                    "escalate_to": "emp_head_eng",
                },
            ),
            Action(
                name="CreateTask",
                kwargs={
                    "title": "Emergency API hotfix",
                    "description": "Fix critical production API bug affecting customers",
                    "assignee_id": "emp_dev_21",
                    "priority": "critical",
                    "story_points": 5,
                    "sprint_id": "sprint_002",
                },
            ),
            Action(
                name="ReassignTask",
                kwargs={
                    "task_id": "task_010",
                    "new_assignee_id": "emp_dev_15",
                },
            ),
            Action(
                name="LogTimeOnTask",
                kwargs={
                    "task_id": "task_003",
                    "hours_logged": 6,
                    "employee_id": "emp_dev_21",
                    "notes": "API endpoint debugging and fixes",
                },
            ),
            Action(
                name="SearchTasks",
                kwargs={"task_id": "task_004"}
            ),
            Action(
                name="UpdateTaskStatus",
                kwargs={"task_id": "task_003", "new_status": "done"},
            ),
            Action(
                name="ResolveBlockedTask",
                kwargs={
                    "task_id": "task_004",
                    "resolution": "task_003 completed",
                    "unblock_dependencies": True,
                },
            ),
            Action(
                name="UpdateTaskStatus",
                kwargs={"task_id": "task_004", "new_status": "in_progress"},
            ),
            Action(name="GenerateSprintReport", kwargs={"sprint_id": "sprint_002"}),
        ],
        outputs=[
            '"blocked_tasks": 2',
        ],
    ),
    Task(
        annotator="0",
        user_id="dependency_resolution_manager",
        instruction="""As the technical lead, manage the blockage of Task_004.
        Inspect its details and dependencies, and confirm whether task_003 is
        finalized. If it remains incomplete, finish it by logging 4 hours for
        the assigned employee. Thereafter, resolve the obstruction for task_004 by setting 'task_003 done' as the resolution and
        set 'unblock dependencies' to true. Change the status of task_004 to 'in_progress'. Review task_015, which relies
        on task_004, and elevate its priority to high due to its impact on
        multiple tasks. Assign it to emp_dev_20, and compute the sprint burndown. Lastly, provide the count of
        tasks that are blocked and the final workload rating for emp_dev_20.""",
        actions=[
            Action(name="GetTaskDetails", kwargs={"task_id": "task_004"}),
            Action(name="SearchTasks", kwargs={"task_id": "task_003"}),
            Action(
                name="GetTaskDetails",
                kwargs={
                    "task_id": "task_003",
                },
            ),
            Action(
                name="LogTimeOnTask",
                kwargs={
                    "task_id": "task_003",
                    "hours_logged": 4,
                    "employee_id": "emp_dev_21",
                },
            ),
            Action(
                name="UpdateTaskStatus",
                kwargs={"task_id": "task_003", "new_status": "done"},
            ),
            Action(
                name="ResolveBlockedTask",
                kwargs={"task_id": "task_004", "resolution": "task_003 done", "unblock_dependencies": True},
            ),
            Action(
                name="UpdateTaskStatus",
                kwargs={"task_id": "task_004", "new_status": "in_progress"},
            ),
            Action(name="GetTaskDetails", kwargs={"task_id": "task_015"}),
            Action(
                name="UpdateTaskPriority",
                kwargs={
                    "task_id": "task_015",
                    "new_priority": "high",
                },
            ),
            Action(
                name="ReassignTask",
                kwargs={
                    "task_id": "task_015",
                    "new_assignee_id": "emp_dev_20",
                },
            ),
            Action(
                name="SearchTasks",
                kwargs={"status": "blocked", "sprint_id": "sprint_002"},
            ),
            Action(
                name="GetEmployeeWorkload",
                kwargs={"employee_id": "emp_dev_20", "sprint_id": "sprint_002"},
            ),
            Action(
                name="CalculateSprintBurndown", kwargs={"sprint_id": "sprint_002"}
            ),
        ],
        outputs=['"workload_rating": "normal"', '"blocked_tasks": 2'],
    ),
    Task(
        annotator="0",
        user_id="tech_debt_manager",
        instruction="""You oversee the role of Technical Architect tasked with managing technical debt. Elevate task_006 priority to critical. Allocate task_006 to sprint_002. Adjust task_011 priority to medium. Formulate task "Database indexing optimization" featuring description "Optimize database indexes for performance improvement" with 5 story points designated for emp_arch_01, critical priority in sprint_002. Establish a dependency between task_019 and task_006. Record 4 hours for task_006, including notes "Initial performance profiling completed". Reallocate task_019 to emp_devops_04. Verify time logging adherence for sprint_002. Record 3 hours on task_004, including notes "Sprint compliance update". Compute the team capacity for team_dev_01 within sprint_002. Present the team utilization and count of non-compliances.""",
        actions=[
            Action(
                name="UpdateTaskPriority",
                kwargs={
                    "task_id": "task_006",
                    "new_priority": "critical",
                },
            ),
            Action(
                name="AssignTaskToSprint",
                kwargs={"task_id": "task_006", "sprint_id": "sprint_002"},
            ),
            Action(
                name="UpdateTaskPriority",
                kwargs={
                    "task_id": "task_011",
                    "new_priority": "medium",
                },
            ),
            Action(
                name="CreateTask",
                kwargs={
                    "title": "Database indexing optimization",
                    "description": "Optimize database indexes for performance improvement",
                    "assignee_id": "emp_arch_01",
                    "priority": "critical",
                    "story_points": 5,
                    "sprint_id": "sprint_002",
                },
            ),
            Action(
                name="CreateTaskDependency",
                kwargs={"task_id": "task_019", "depends_on_task_id": "task_006"},
            ),
            Action(
                name="LogTimeOnTask",
                kwargs={
                    "task_id": "task_006",
                    "hours_logged": 4,
                    "employee_id": "emp_dev_07",
                    "notes": "Initial performance profiling completed",
                },
            ),
            Action(
                name="ReassignTask",
                kwargs={
                    "task_id": "task_019",
                    "new_assignee_id": "emp_devops_04",
                },
            ),
            Action(
                name="CheckTimeLoggingCompliance", kwargs={"sprint_id": "sprint_002"}
            ),
            Action(
                name="LogTimeOnTask",
                kwargs={
                    "task_id": "task_004",
                    "hours_logged": 3,
                    "employee_id": "emp_dev_20",
                    "notes": "Sprint compliance update",
                },
            ),
            Action(
                name="CalculateTeamCapacity",
                kwargs={"team_id": "team_dev_01", "sprint_id": "sprint_002"},
            ),
        ],
        outputs=['"team_utilization": 26.2', '"non_compliant_count": 3'],
    ),
    Task(
        annotator="0",
        user_id="enforce_time_tracking",
        instruction="""You act as the PMO lead. Verify time logging adherence for sprint_002. For all tasks not in compliance, investigate their specifics and apply necessary measures: log 4 hours of time for each task to the assigned personnel, and display the total story points currently assigned to employee emp_dev_21 as well as the overall count of non-compliant tasks identified.""",
        actions=[
            Action(
                name="CheckTimeLoggingCompliance", kwargs={"sprint_id": "sprint_002"}
            ),
            Action(
                name="LogTimeOnTask",
                kwargs={
                    "task_id": "task_003",
                    "hours_logged": 4,
                    "employee_id": "emp_dev_21",
                },
            ),
            Action(
                name="LogTimeOnTask",
                kwargs={
                    "task_id": "task_012",
                    "hours_logged": 4,
                    "employee_id": "emp_sec_dev_02",
                },
            ),
            Action(
                name="LogTimeOnTask",
                kwargs={
                    "task_id": "task_008",
                    "hours_logged": 4,
                    "employee_id": "emp_test_05",
                },
            ),
            Action(
                name="LogTimeOnTask",
                kwargs={
                    "task_id": "task_019",
                    "hours_logged": 4,
                    "employee_id": "emp_devops_02",
                },
            ),
            Action(
                name="GetEmployeeWorkload",
                kwargs={"employee_id": "emp_dev_21", "sprint_id": "sprint_002"},
            ),
        ],
        outputs=['"non_compliant_count": 4', '"total_active_story_points": 8'],
    ),
    Task(
        annotator="0",
        user_id="resource_optimization_lead",
        instruction="""
        As the resource optimization coordinator, determine team_dev_01's velocity for the last 3 sprints. Transfer
        task_018 to sprint_003 and allocate task_011 to sprint_003. Record 6 hours on task_003 with 'Finalizing the API
        implementation' as the note, then mark it as complete. Replicate task_016 as "Mobile optimization" for emp_dev_15. Calculate and provide team_dev_01's
        average velocity.""",
        actions=[
            Action(
                name="GetTeamVelocity",
                kwargs={"team_id": "team_dev_01", "last_n_sprints": 3},
            ),
            Action(
                name="BulkMoveTasksToSprint",
                kwargs={
                    "task_ids": ["task_018"],
                    "target_sprint_id": "sprint_003",
                },
            ),
            Action(
                name="AssignTaskToSprint",
                kwargs={"task_id": "task_011", "sprint_id": "sprint_003"},
            ),
            Action(name="GetTaskDetails", kwargs={"task_id": "task_003"}),
            Action(
                name="LogTimeOnTask",
                kwargs={
                    "task_id": "task_003",
                    "hours_logged": 6,
                    "employee_id": "emp_dev_21",
                    "notes": "Finalizing the API implementation",
                },
            ),
            Action(
                name="UpdateTaskStatus",
                kwargs={"task_id": "task_003", "new_status": "done"},
            ),
            Action(
                name="CloneTask",
                kwargs={
                    "source_task_id": "task_016",
                    "new_title": "Mobile optimization",
                    "new_assignee_id": "emp_dev_15",
                    "sprint_id": "sprint_003",
                },
            ),
        ],
        outputs=[
            '"average_velocity": 18.0',
        ],
    ),
    Task(
        annotator="0",
        user_id="plan_next_sprint",
        instruction="""As the scrum master for the Web Development Team
        (team_dev_01), set up a new sprint for the team called "Sprint 6 - Web
        Team" that begins on March 29th, 2024 and concludes on April 11th, 2024. Review team
        velocity from past sprints, determine capacity, extract high-priority tasks
        from the backlog, resolve their dependencies using "Emergency
        override", assign these tasks to the sprint, and commence the sprint. Document
        the planned story points for the sprint.""",
        actions=[
            Action(
                name="GetTeamVelocity",
                kwargs={"team_id": "team_dev_01", "last_n_sprints": 3},
            ),
            Action(name="CalculateTeamCapacity", kwargs={"team_id": "team_dev_01"}),
            Action(
                name="CreateSprint",
                kwargs={
                    "sprint_id": "sprint_006",
                    "sprint_name": "Sprint 6 - Web Team",
                    "start_date": "2024-03-29",
                    "end_date": "2024-04-11",
                    "team_id": "team_dev_01",
                },
            ),
            Action(name="GetBacklogTasks", kwargs={"priority": "critical"}),
            Action(name="SearchTasks", kwargs={"task_id": "task_014"}),
            Action(
                name="ResolveBlockedTask",
                kwargs={
                    "task_id": "task_014",
                    "resolution": "Emergency override",
                    "unblock_dependencies": True,
                },
            ),
            Action(
                name="BulkMoveTasksToSprint",
                kwargs={
                    "task_ids": ["task_014"],
                    "target_sprint_id": "sprint_006",
                },
            ),
            Action(
                name="UpdateSprintStatus",
                kwargs={"sprint_id": "sprint_006", "new_status": "active"},
            ),
            Action(name="GetSprintDetails", kwargs={"sprint_id": "sprint_006"}),
        ],
        outputs=['"sprint_total_points": 13'],
    ),
    Task(
        annotator="0",
        user_id="manage_task_dependencies",
        instruction="""As the tech lead, recognize that task_004 is dependent on task_003. Ascertain the status of task_003; if it is unfinished, check the status of any associated dependencies. Record time entries for task_003 to reflect progress (8 hours and 6 hours correspondingly), finalize task_003, and subsequently lift the block on task_004 by marking 'Dependency satisfied' as the resolution. Update task_004's status to in_progress and inform me of its current status.""",
        actions=[
            Action(name="SearchTasks", kwargs={"task_id": "task_004"}),
            Action(name="SearchTasks", kwargs={"task_id": "task_003"}),
            Action(name="GetTaskDetails", kwargs={"task_id": "task_003"}),
            Action(name="GetTaskHistory", kwargs={"task_id": "task_003"}),
            Action(name="SearchTasks", kwargs={"task_id": "task_001"}),
            Action(name="SearchTasks", kwargs={"task_id": "task_002"}),
            Action(
                name="LogTimeOnTask",
                kwargs={
                    "task_id": "task_003",
                    "hours_logged": 8,
                    "employee_id": "emp_dev_21",
                },
            ),
            Action(
                name="LogTimeOnTask",
                kwargs={
                    "task_id": "task_003",
                    "hours_logged": 6,
                    "employee_id": "emp_dev_21",
                },
            ),
            Action(
                name="UpdateTaskStatus",
                kwargs={"task_id": "task_003", "new_status": "done"},
            ),
            Action(
                name="ResolveBlockedTask",
                kwargs={
                    "task_id": "task_004",
                    "resolution": "Dependency satisfied",
                    "unblock_dependencies": True,
                },
            ),
            Action(
                name="UpdateTaskStatus",
                kwargs={"task_id": "task_004", "new_status": "in_progress"},
            ),
            Action(name="SearchTasks", kwargs={"task_id": "task_004"}),
        ],
        outputs=['"status": "in_progress"'],
    ),
    Task(
        annotator="0",
        user_id="emergency_security_incident_coordinator",
        instruction="""In your capacity as the Chief Security Officer, address a critical security incident. Employ the bulk move function to relocate task_014 to sprint_002 (active). Duplicate task_005 as "Emergency security review - Finance" (task_071) for emp_sec_dev_02 and as "Emergency security review - Banking" (task_072) for emp_sec_test_01. Close task_015 using the resolution "Security emergency override - UI work deprioritized" with unblock dependencies. Transfer task_012 from sprint_002 to sprint_003. Establish "Penetration test - Security Expert 1" (task_073) with the description "Emergency penetration testing" for emp_sec_dev_01, assigning 4 critical story points in sprint_002. Similarly, create "Penetration test - Security Expert 2" (task_074) with the same description "Emergency penetration testing" for emp_sec_dev_02, also with 4 critical story points in sprint_002. Confirm if the process was successfully executed.""",
        actions=[
            Action(
                name="BulkMoveTasksToSprint",
                kwargs={
                    "task_ids": ["task_014"],
                    "target_sprint_id": "sprint_002",
                },
            ),
            Action(
                name="CloneTask",
                kwargs={
                    "source_task_id": "task_005",
                    "new_title": "Emergency security review - Finance",
                    "new_task_id": "task_071",
                    "new_assignee_id": "emp_sec_dev_02",
                },
            ),
            Action(
                name="CloneTask",
                kwargs={
                    "source_task_id": "task_005",
                    "new_title": "Emergency security review - Banking",
                    "new_task_id": "task_072",
                    "new_assignee_id": "emp_sec_test_01",
                },
            ),
            Action(
                name="ResolveBlockedTask",
                kwargs={
                    "task_id": "task_015",
                    "resolution": "Security emergency override - UI work deprioritized",
                    "unblock_dependencies": True,
                },
            ),
            Action(
                name="BulkMoveTasksToSprint",
                kwargs={"task_ids": ["task_012"], "target_sprint_id": "sprint_003"},
            ),
            Action(
                name="CreateTask",
                kwargs={
                    "new_task_id": "task_073",
                    "title": "Penetration test - Security Expert 1",
                    "description": "Emergency penetration testing",
                    "assignee_id": "emp_sec_dev_01",
                    "priority": "critical",
                    "story_points": 4,
                    "sprint_id": "sprint_002",
                },
            ),
            Action(
                name="CreateTask",
                kwargs={
                    "new_task_id": "task_074",
                    "title": "Penetration test - Security Expert 2",
                    "description": "Emergency penetration testing",
                    "assignee_id": "emp_sec_dev_02",
                    "priority": "critical",
                    "story_points": 4,
                    "sprint_id": "sprint_002",
                },
            ),
        ],
        outputs=['"workflow_execution": "success"'],
    ),
    Task(
        annotator="0",
        user_id="resource_balance_optimizer",
        instruction="""As the Resource Management Director, assess the capacity of
        team_dev_01 for sprint_002. Transfer responsibility of task_004 from emp_dev_05
        to emp_test_05. Generate a "Resource Optimization Review" task with the
        description "Review team resource allocation" involving 4 story points for
        emp_dev_20, marked with high priority. Verify the adherence to time logging rules for
        sprint_002. Record 4 hours on task_003 for emp_dev_21, including notes
        "Compliance update - resource optimization". Duplicate task_016 renaming it as "Load
        balancing implementation" assigned to emp_dev_05 for sprint_002. Provide statistics on team utilization
        percentage and the count of non-compliant tasks.""",
        actions=[
            Action(
                name="CalculateTeamCapacity",
                kwargs={"team_id": "team_dev_01", "sprint_id": "sprint_002"},
            ),
            Action(
                name="ReassignTask",
                kwargs={
                    "task_id": "task_004",
                    "new_assignee_id": "emp_test_05",
                },
            ),
            Action(
                name="CreateTask",
                kwargs={
                    "title": "Resource Optimization Review",
                    "description": "Review team resource allocation",
                    "assignee_id": "emp_dev_20",
                    "priority": "high",
                    "story_points": 4,
                    "sprint_id": "sprint_002",
                },
            ),
            Action(
                name="CheckTimeLoggingCompliance", kwargs={"sprint_id": "sprint_002"}
            ),
            Action(
                name="LogTimeOnTask",
                kwargs={
                    "task_id": "task_003",
                    "hours_logged": 4,
                    "employee_id": "emp_dev_21",
                    "notes": "Compliance update - resource optimization",
                },
            ),
            Action(
                name="CloneTask",
                kwargs={
                    "source_task_id": "task_016",
                    "new_title": "Load balancing implementation",
                    "new_assignee_id": "emp_dev_05",
                    "sprint_id": "sprint_002"
                },
            ),
            Action(
                name="CalculateTeamCapacity",
                kwargs={"team_id": "team_dev_01", "sprint_id": "sprint_002"},
            ),
            Action(
                name="CheckTimeLoggingCompliance", kwargs={"sprint_id": "sprint_002"}
            ),
        ],
        outputs=['"team_utilization": 37.5', '"non_compliant_count": 3'],
    ),
    Task(
        annotator="0",
        user_id="sprint_recovery_lead",
        instruction="""Acting as the sprint recovery expert for team_dev_01,
        prioritize task_015, directing it to emp_head_eng for the purpose of sprint recovery. Mark task_003
        as completed with 8 hours documented by the designated staff. Record 4 hours for
        task_004 (emp_dev_20) and task_012 (emp_sec_dev_02) to maintain time compliance.
        Transition task_004 to in_progress status. Report the percentage of tasks completed.""",
        actions=[
            Action(
                name="CheckBlockedTasksForEscalation",
                kwargs={"sprint_id": "sprint_002"},
            ),
            Action(
                name="EscalateTask",
                kwargs={
                    "task_id": "task_015",
                    "escalate_to": "emp_head_eng",
                },
            ),
            Action(name="GetTaskDetails", kwargs={"task_id": "task_003"}),
            Action(
                name="LogTimeOnTask",
                kwargs={
                    "task_id": "task_003",
                    "hours_logged": 8,
                    "employee_id": "emp_dev_21",
                },
            ),
            Action(
                name="UpdateTaskStatus",
                kwargs={"task_id": "task_003", "new_status": "done"},
            ),
            Action(
                name="LogTimeOnTask",
                kwargs={
                    "task_id": "task_004",
                    "hours_logged": 4,
                    "employee_id": "emp_dev_20",
                },
            ),
            Action(
                name="LogTimeOnTask",
                kwargs={
                    "task_id": "task_012",
                    "hours_logged": 4,
                    "employee_id": "emp_sec_dev_02",
                },
            ),
            Action(
                name="UpdateTaskStatus",
                kwargs={"task_id": "task_004", "new_status": "in_progress"},
            ),
            Action(
                name="CalculateSprintBurndown", kwargs={"sprint_id": "sprint_002"}
            ),
        ],
        outputs=['"completion_percentage": 9.4'],
    ),
    Task(
        annotator="0",
        user_id="skills_gap_analyzer",
        instruction="""As the resource planning specialist examining skill gaps, generate a retrospective for sprint_002 including: What went well: "Data pipeline implementation was smooth", "Good knowledge transfer between team members", "Stakeholder communication was effective". Identify areas needing improvement: "Need better testing data for analytics", "Sprint planning took too long", "Some user stories were too vague". Designate action items: "Create test data generation scripts", "Time-box sprint planning to 2 hours", "Include acceptance criteria in all user stories". Change task_020 priority to high. Introduce task "ML skill development workshop" with description "Workshop to improve team's machine learning skills" allocating 4 story points for emp_data_02, with medium priority. Establish a dependency where task_011 depends on task_008, ensuring task_011 is blocked. Duplicate task_006 as "Advanced performance optimization" for emp_dev_08. Retrieve emp_data_01 workload for sprint_002. Provide emp_data_01's final workload rating, and confirm if the retrospective was successfully created.""",
        actions=[
            Action(
                name="CreateSprintRetrospective",
                kwargs={
                    "sprint_id": "sprint_002",
                    "what_went_well": [
                        "Data pipeline implementation was smooth",
                        "Good knowledge transfer between team members",
                        "Stakeholder communication was effective",
                    ],
                    "what_needs_improvement": [
                        "Need better testing data for analytics",
                        "Sprint planning took too long",
                        "Some user stories were too vague",
                    ],
                    "action_items": [
                        "Create test data generation scripts",
                        "Time-box sprint planning to 2 hours",
                        "Include acceptance criteria in all user stories",
                    ],
                },
            ),
            Action(
                name="UpdateTaskPriority",
                kwargs={
                    "task_id": "task_020",
                    "new_priority": "high",
                },
            ),
            Action(
                name="CreateTask",
                kwargs={
                    "title": "ML skill development workshop",
                    "description": "Workshop to improve team's machine learning skills",
                    "assignee_id": "emp_data_02",
                    "priority": "medium",
                    "story_points": 4,
                },
            ),
            Action(
                name="CreateTaskDependency",
                kwargs={"task_id": "task_011", "depends_on_task_id": "task_008", "block_task": True},
            ),
            Action(
                name="CloneTask",
                kwargs={
                    "source_task_id": "task_006",
                    "new_title": "Advanced performance optimization",
                    "new_assignee_id": "emp_dev_08",
                },
            ),
            Action(
                name="GetEmployeeWorkload",
                kwargs={"employee_id": "emp_data_01", "sprint_id": "sprint_002"},
            ),
        ],
        outputs=[
            '"workload_rating": "normal"',
            '"success": true',
        ],
    ),
    Task(
        annotator="0",
        user_id="sprint_closure_automation_lead",
        instruction="""Being the Agile Coach in charge of automating sprint closure for team_dev_01, ensure time logging compliance for sprint_005. Allocate 10 hours on task_013 for emp_dev_08 and 8 hours on task_017 for emp_devops_04 including notes "Sprint closure compliance". Adjust task_006 priority to critical. Determine team velocity for team_dev_01 over the last 2 sprints. Elevate task_011 priority to critical. Formulate a dependency where task_008 relies on task_012. Mark task_003 status as done. Transition sprint_005 status to completed. Compose a retrospective with what_went_well: "Data pipeline implementation was smooth", "Good knowledge transfer between team members", "Stakeholder communication was effective"; what_needs_improvement: "Need better testing data for analytics", "Sprint planning took too long", "Some user stories were too vague"; action_items: "Create test data generation scripts", "Time-box sprint planning to 2 hours", "Include acceptance criteria in all user stories". Reallocate task_006 and task_11 to emp_analyst_03. Present average velocity for team_dev_01""",
        actions=[
            Action(
                name="CheckTimeLoggingCompliance", kwargs={"sprint_id": "sprint_005"}
            ),
            Action(
                name="LogTimeOnTask",
                kwargs={
                    "task_id": "task_013",
                    "hours_logged": 10,
                    "employee_id": "emp_dev_08",
                    "notes": "Sprint closure compliance",
                },
            ),
            Action(
                name="LogTimeOnTask",
                kwargs={
                    "task_id": "task_017",
                    "hours_logged": 8,
                    "employee_id": "emp_devops_04",
                    "notes": "Sprint closure compliance",
                },
            ),
            Action(
                name="UpdateTaskPriority",
                kwargs={
                    "task_id": "task_006",
                    "new_priority": "critical",
                },
            ),
            Action(
                name="UpdateTaskPriority",
                kwargs={
                    "task_id": "task_011",
                    "new_priority": "critical",
                },
            ),
            Action(
                name="CreateTaskDependency",
                kwargs={"task_id": "task_008", "depends_on_task_id": "task_012"},
            ),
            Action(
                name="UpdateTaskStatus",
                kwargs={"task_id": "task_003", "new_status": "done"},
            ),
            Action(
                name="UpdateSprintStatus",
                kwargs={"sprint_id": "sprint_005", "new_status": "completed"},
            ),
            Action(
                name="CreateSprintRetrospective",
                kwargs={
                    "sprint_id": "sprint_005",
                    "what_went_well": [
                        "Data pipeline implementation was smooth",
                        "Good knowledge transfer between team members",
                        "Stakeholder communication was effective",
                    ],
                    "what_needs_improvement": [
                        "Need better testing data for analytics",
                        "Sprint planning took too long",
                        "Some user stories were too vague",
                    ],
                    "action_items": [
                        "Create test data generation scripts",
                        "Time-box sprint planning to 2 hours",
                        "Include acceptance criteria in all user stories",
                    ],
                },
            ),
            Action(
                name="ReassignTask",
                kwargs={
                    "task_id": "task_006",
                    "new_assignee_id": "emp_analyst_03",
                },
            ),
            Action(
                name="ReassignTask",
                kwargs={
                    "task_id": "task_011",
                    "new_assignee_id": "emp_analyst_03",
                },
            ),
            Action(
                name="GetTeamVelocity",
                kwargs={"team_id": "team_dev_01", "last_n_sprints": 2},
            ),
        ],
        outputs=[
            '"average_velocity": 0',
        ],
    ),
    Task(
        annotator="0",
        user_id="retrospective_facilitator",
        instruction="""As the agile coach overseeing retrospective for sprint_001, obtain the velocity trend of team_analytics_01 for the past 3 sprints. Retrieve the history of task_002. Duplicate task_002 to create task_026 ("Database schema v2 design") for emp_arch_01. Establish a dependency where the duplicated task relies on task_014. Initiate sprint (sprint_006) named "Analytics Sprint 2" running from 2024-04-15 to 2024-04-28 for team_analytics_01 with the objective "Implement data pipeline v2 with lessons learned". Relocate the duplicated task and task_014 to this new sprint. Determine the team capacity for the upcoming sprint. Submit a report on the velocity trend, the count of task_002 history, and capacity points for the new sprint.""",
        actions=[
            Action(
                name="GetTeamVelocity",
                kwargs={"team_id": "team_analytics_01", "last_n_sprints": 3},
            ),
            Action(name="GetTaskHistory", kwargs={"task_id": "task_002"}),
            Action(
                name="CloneTask",
                kwargs={
                    "source_task_id": "task_002",
                    "new_task_id": "task_026",
                    "new_title": "Database schema v2 design",
                    "new_assignee_id": "emp_arch_01",
                },
            ),
            Action(
                name="CreateTaskDependency",
                kwargs={"task_id": "task_026", "depends_on_task_id": "task_014"},
            ),
            Action(
                name="CreateSprint",
                kwargs={
                    "sprint_name": "Analytics Sprint 2",
                    "sprint_id": "sprint_006",
                    "start_date": "2024-04-15",
                    "end_date": "2024-04-28",
                    "sprint_goal": "Implement data pipeline v2 with lessons learned",
                    "team_id": "team_analytics_01",
                },
            ),
            Action(
                name="BulkMoveTasksToSprint",
                kwargs={
                    "task_ids": ["task_026", "task_014"],
                    "target_sprint_id": "sprint_006",
                },
            ),
            Action(
                name="CalculateTeamCapacity",
                kwargs={"team_id": "team_analytics_01", "sprint_id": "sprint_006"},
            ),
        ],
        outputs=[
            '"trend": "stable"',
            '"history_count": 1',
            '"total_capacity_points": 60',
        ],
    ),
    Task(
        annotator="0",
        user_id="skill_transfer_coordinator",
        instruction="""As the Skills Development Coordinator, allocate task_014 to sprint_002. Develop the task "ML knowledge transfer session" with the description "Transfer ML expertise for data migration project" which has 3 story points for emp_data_02 and is set at medium priority. Elevate the priority of task_006 to critical. Form a dependency where task_014 is contingent on task_002. Record 2 hours on task_014 for emp_data_01, including the notes "ML algorithm research and planning". Verify the compliance of time logging for sprint_002. Formulate task "Time tracking training session" with description "Train team on proper time tracking procedures" and assign 2 story points to emp_pm_04, designated with high priority. Compile the final workload for emp_data_01 in sprint_002 and deliver their workload rating and total active story points.""",
        actions=[
            Action(
                name="AssignTaskToSprint",
                kwargs={"task_id": "task_014", "sprint_id": "sprint_002"},
            ),
            Action(
                name="CreateTask",
                kwargs={
                    "title": "ML knowledge transfer session",
                    "description": "Transfer ML expertise for data migration project",
                    "assignee_id": "emp_data_02",
                    "priority": "medium",
                    "story_points": 3,
                },
            ),
            Action(
                name="UpdateTaskPriority",
                kwargs={
                    "task_id": "task_006",
                    "new_priority": "critical",
                },
            ),
            Action(
                name="CreateTaskDependency",
                kwargs={"task_id": "task_014", "depends_on_task_id": "task_002"},
            ),
            Action(
                name="LogTimeOnTask",
                kwargs={
                    "task_id": "task_014",
                    "hours_logged": 2,
                    "employee_id": "emp_data_01",
                    "notes": "ML algorithm research and planning",
                },
            ),
            Action(
                name="CheckTimeLoggingCompliance", kwargs={"sprint_id": "sprint_002"}
            ),
            Action(
                name="CreateTask",
                kwargs={
                    "title": "Time tracking training session",
                    "description": "Train team on proper time tracking procedures",
                    "assignee_id": "emp_pm_04",
                    "priority": "high",
                    "story_points": 2,
                },
            ),
            Action(
                name="GetEmployeeWorkload",
                kwargs={"employee_id": "emp_data_01", "sprint_id": "sprint_002"},
            ),
        ],
        outputs=['"workload_rating": "normal"', '"total_active_story_points": 13'],
    ),
    Task(
        annotator="0",
        user_id="resource_conflict_resolver",
        instruction="""You are designated as the Resource Allocation Director managing an urgent skill shortage scenario. Initiate a critical task (task_022) "ML model optimization - Phase 1" with description "Optimize machine learning models for AI platform" with 8 story points for emp_data_01. Transfer task_014 to emp_data_02. Modify task_014's priority to medium. Retrieve team_analytics_01 velocity for the past 3 sprints. Duplicate task_006 into task_023 ("AI data analysis pipeline") for emp_data_01. Document 4 hours on the ML optimization task with remarks "Initial ML architecture design and planning". Formulate task (task_029) "Cross-team ML knowledge transfer" with description "Facilitate ML knowledge sharing across teams" with 3 story points for emp_pm_04 with high priority. Elevate task_005 to emp_head_eng. Obtain final workload for emp_data_01. Provide the workload rating and the average velocity.""",
        actions=[
            Action(
                name="CreateTask",
                kwargs={
                    "new_task_id": "task_022",
                    "title": "ML model optimization - Phase 1",
                    "description": "Optimize machine learning models for AI platform",
                    "assignee_id": "emp_data_01",
                    "priority": "critical",
                    "story_points": 8,
                },
            ),
            Action(
                name="ReassignTask",
                kwargs={
                    "task_id": "task_014",
                    "new_assignee_id": "emp_data_02",
                },
            ),
            Action(
                name="UpdateTaskPriority",
                kwargs={
                    "task_id": "task_014",
                    "new_priority": "medium",
                },
            ),
            Action(
                name="GetTeamVelocity",
                kwargs={"team_id": "team_analytics_01", "last_n_sprints": 3},
            ),
            Action(
                name="CloneTask",
                kwargs={
                    "source_task_id": "task_006",
                    "new_task_id": "task_023",
                    "new_title": "AI data analysis pipeline",
                    "new_assignee_id": "emp_data_01",
                },
            ),
            Action(
                name="SearchTasks",
                kwargs={"assignee_id": "emp_data_01", "priority": "critical"},
            ),
            Action(
                name="LogTimeOnTask",
                kwargs={
                    "task_id": "task_022",
                    "hours_logged": 4,
                    "employee_id": "emp_data_01",
                    "notes": "Initial ML architecture design and planning",
                },
            ),
            Action(
                name="CreateTask",
                kwargs={
                    "new_task_id": "task_029",
                    "title": "Cross-team ML knowledge transfer",
                    "description": "Facilitate ML knowledge sharing across teams",
                    "assignee_id": "emp_pm_04",
                    "priority": "high",
                    "story_points": 3,
                },
            ),
            Action(
                name="EscalateTask",
                kwargs={
                    "task_id": "task_005",
                    "escalate_to": "emp_head_eng",
                },
            ),
            Action(name="GetEmployeeWorkload", kwargs={"employee_id": "emp_data_01"}),
        ],
        outputs=[
            '"workload_rating": "normal"',
            '"new_escalation_created": false',
            '"average_velocity": 28.0',
        ],
    ),
    Task(
        annotator="0",
        user_id="priority_rebalancing_specialist",
        instruction="""You have the role of Priority Rebalancing Specialist, focused on enhancing work allocation across priority classifications. Your employee ID is emp_pmo_director. Inspect emp_sec_dev_01's workload to determine their priority breakdown. Should their critical priority points surpass 10, retrieve their critical tasks in sprint_002. Review workloads of emp_dev_07 and emp_dev_08 for priority breakdowns. If task_011 is linked to someone exceeding 3 low priority points, transfer it to emp_sec_test_01. Alter task_011's priority to high. Examine emp_qa_02's workload for priority breakdowns. In case their medium priority points are fewer than 5, assign task_010 to emp_qa_02. Construct a task titled "Priority distribution analysis" with description "Analyze and optimize team priority distribution" with 4 story points for emp_pm_04, marked as critical priority. Assess blocked tasks for potential escalation in sprint_002. If any tasks have been obstructed for "365+" days, raise the first one to emp_cto. Record 3 hours on task_005 for emp_sec_dev_01 with annotations "Security framework implementation". Compute team capacity for team_security_01. Extract the critical priority points from emp_sec_dev_01's priority_breakdown.""",
        actions=[
            Action(
                name="GetEmployeeWorkload",
                kwargs={"employee_id": "emp_sec_dev_01", "sprint_id": "sprint_002"},
            ),
            Action(
                name="SearchTasks",
                kwargs={
                    "assignee_id": "emp_sec_dev_01",
                    "priority": "critical",
                    "sprint_id": "sprint_002",
                },
            ),
            Action(name="GetEmployeeWorkload", kwargs={"employee_id": "emp_dev_07"}),
            Action(name="GetEmployeeWorkload", kwargs={"employee_id": "emp_dev_08"}),
            Action(name="SearchTasks", kwargs={"task_id": "task_011"}),
            Action(name="GetEmployeeWorkload", kwargs={"employee_id": "emp_qa_02"}),
            Action(
                name="ReassignTask",
                kwargs={
                    "task_id": "task_011",
                    "new_assignee_id": "emp_sec_test_01",
                },
            ),
            Action(
                name="UpdateTaskPriority",
                kwargs={
                    "task_id": "task_011",
                    "new_priority": "high",
                },
            ),
            Action(name="GetEmployeeWorkload", kwargs={"employee_id": "emp_qa_02"}),
            Action(
                name="ReassignTask",
                kwargs={
                    "task_id": "task_010",
                    "new_assignee_id": "emp_qa_02",
                },
            ),
            Action(
                name="CreateTask",
                kwargs={
                    "title": "Priority distribution analysis",
                    "description": "Analyze and optimize team priority distribution",
                    "assignee_id": "emp_pm_04",
                    "priority": "critical",
                    "story_points": 4,
                    "sprint_id": "sprint_002",
                },
            ),
            Action(
                name="CheckBlockedTasksForEscalation",
                kwargs={"sprint_id": "sprint_002"},
            ),
            Action(
                name="EscalateTask",
                kwargs={
                    "task_id": "task_015",
                    "escalate_to": "emp_cto",
                },
            ),
            Action(
                name="LogTimeOnTask",
                kwargs={
                    "task_id": "task_005",
                    "hours_logged": 3,
                    "employee_id": "emp_sec_dev_01",
                    "notes": "Security framework implementation",
                },
            ),
            Action(
                name="CalculateTeamCapacity",
                kwargs={"team_id": "team_security_01", "sprint_id": "sprint_002"},
            ),
            Action(name="GenerateSprintReport", kwargs={"sprint_id": "sprint_002"}),
            Action(
                name="GetEmployeeWorkload",
                kwargs={"employee_id": "emp_sec_dev_01", "sprint_id": "sprint_002"},
            ),
        ],
        outputs=['"critical": 13'],
    ),
    Task(
        annotator="0",
        user_id="predictive_blocker_prevention",
        instruction="""As a process improvement specialist, you are analyzing historical patterns. Retrieve the task history for task_005. Identify tasks that are blocked and require escalation across all sprints. Gather details for task_015 and initiate "Procurement process automation" task_030 with the description "Automate procurement to prevent blocking" and allocate 5 story points for emp_pm_04, labeling it as critical priority. Establish a dependency whereby task_019 is contingent on task_009 (set block task to true). Record 3 hours on task_009 with notes "Adding automated compliance checks". Retrieve backlog tasks that have a maximum of 5 story points. Duplicate task_016 as task_027 ("Security checklist automation") for emp_sec_test_01 and modify its priority to high. Verify time logging compliance for sprint_002. Relocate tasks ["task_006", "task_011", "task_016"] to sprint_003 en masse. Retrieve the history of task_017. Initiate "Backup verification automation" task (task_028) with the description "Automated backup verification" and assign 4 story points for emp_devops_04, prioritizing it as high. Make task_019 contingent on the new task. Compute the burndown for sprint_002. Report the history count of task_005, the count of successfully moved tasks in bulk, and the percentage of completion.""",
        actions=[
            Action(name="GetTaskHistory", kwargs={"task_id": "task_005"}),
            Action(
                name="CheckBlockedTasksForEscalation",
                kwargs={"check_all_sprints": True},
            ),
            Action(name="GetTaskDetails", kwargs={"task_id": "task_015"}),
            Action(
                name="CreateTask",
                kwargs={
                    "title": "Procurement process automation",
                    "new_task_id": "task_030",
                    "description": "Automate procurement to prevent blocking",
                    "assignee_id": "emp_pm_04",
                    "priority": "critical",
                    "story_points": 5,
                },
            ),
            Action(name="GenerateSprintReport", kwargs={"sprint_id": "sprint_002"}),
            Action(
                name="CreateTaskDependency",
                kwargs={"task_id": "task_019", "depends_on_task_id": "task_009", "block_task": True},
            ),
            Action(
                name="LogTimeOnTask",
                kwargs={
                    "task_id": "task_009",
                    "hours_logged": 3,
                    "employee_id": "emp_devops_02",
                    "notes": "Adding automated compliance checks",
                },
            ),
            Action(name="GetBacklogTasks", kwargs={"max_story_points": 5}),
            Action(
                name="CloneTask",
                kwargs={
                    "source_task_id": "task_016",
                    "new_task_id": "task_027",
                    "new_title": "Security checklist automation",
                    "new_assignee_id": "emp_sec_test_01",
                },
            ),
            Action(
                name="UpdateTaskPriority",
                kwargs={
                    "task_id": "task_027",
                    "new_priority": "high",
                },
            ),
            Action(
                name="CheckTimeLoggingCompliance", kwargs={"sprint_id": "sprint_002"}
            ),
            Action(
                name="BulkMoveTasksToSprint",
                kwargs={
                    "task_ids": ["task_006", "task_011", "task_016"],
                    "target_sprint_id": "sprint_003",
                },
            ),
            Action(name="GetTaskHistory", kwargs={"task_id": "task_017"}),
            Action(
                name="CreateTask",
                kwargs={
                    "title": "Backup verification automation",
                    "new_task_id": "task_028",
                    "description": "Automated backup verification",
                    "assignee_id": "emp_devops_04",
                    "priority": "high",
                    "story_points": 4,
                },
            ),
            Action(
                name="CreateTaskDependency",
                kwargs={"task_id": "task_019", "depends_on_task_id": "task_028"},
            ),
            Action(
                name="CalculateSprintBurndown", kwargs={"sprint_id": "sprint_002"}
            ),
        ],
        outputs=[
            '"history_count": 3',
            '"moved_count": 3',
            '"completion_percentage": 0.0',
        ],
    ),
    Task(
        annotator="0",
        user_id="velocity_driven_sprint_recovery",
        instruction="""In your role as the Agile transformation lead, you're analyzing the velocity decline of team_dev_01. Retrieve the team's velocity from the last sprint. Duplicate task_012 as task_034 ("User permissions system - Simplified") for emp_sec_dev_02. Conduct a bulk move of task_004 to sprint_003. Escalate task_015 to emp_head_eng. Initiate task_032 "Velocity improvement workshop" with the description "Workshop to address velocity decline" allocating 3 story points for emp_pm_03, with a priority set to high. Duplicate task_009 as task_030 ("Automated velocity tracking dashboard") for emp_devops_02. Establish a dependency where the duplicated task is reliant on task_019. Resolve task_015 with the resolution "Framework decision made - React selected". Report the velocity trend, the number of tasks transferred to the next sprint, and confirm whether a blocked task was resolved.""",
        actions=[
            Action(
                name="GetTeamVelocity",
                kwargs={"team_id": "team_dev_01", "last_n_sprints": 1},
            ),
            Action(
                name="CloneTask",
                kwargs={
                    "source_task_id": "task_012",
                    "new_task_id": "task_034",
                    "new_title": "User permissions system - Simplified",
                    "new_assignee_id": "emp_sec_dev_02",
                },
            ),
            Action(
                name="BulkMoveTasksToSprint",
                kwargs={
                    "task_ids": ["task_004"],
                    "target_sprint_id": "sprint_003",
                },
            ),
            Action(
                name="EscalateTask",
                kwargs={
                    "task_id": "task_015",
                    "escalate_to": "emp_head_eng",
                },
            ),
            Action(
                name="CreateTask",
                kwargs={
                    "title": "Velocity improvement workshop",
                    "new_task_id": "task_032",
                    "description": "Workshop to address velocity decline",
                    "assignee_id": "emp_pm_03",
                    "priority": "high",
                    "story_points": 3,
                },
            ),
            Action(
                name="CloneTask",
                kwargs={
                    "source_task_id": "task_009",
                    "new_task_id": "task_030",
                    "new_title": "Automated velocity tracking dashboard",
                    "new_assignee_id": "emp_devops_02",
                },
            ),
            Action(
                name="CreateTaskDependency",
                kwargs={"task_id": "task_030", "depends_on_task_id": "task_019"},
            ),
            Action(
                name="ResolveBlockedTask",
                kwargs={
                    "task_id": "task_015",
                    "resolution": "Framework decision made - React selected",
                    "unblock_dependencies": True,
                },
            ),
        ],
        outputs=['"trend": "stable"', '"moved_count": 1', '"success": true'],
    ),
    Task(
        annotator="0",
        user_id="performance_analytics_lead",
        instruction="""As the Performance Analytics Lead investigating the decline in team productivity, your employee ID, emp_head_analytics, needs to be used to identify the assignee with the lowest ratio of completed_points to total_points in the sprint 'sprint_001'. Determine that employee's current task workload. Should their total_active_story_points register under 10, assign task_020 to them. For team_analytics_01, calculate team velocity across the last 3 sprints to review the trend of individual_velocities. Develop a critical task titled "Velocity improvement workshop" with a description "Workshop to address declining team velocity" comprising 5 story points for emp_pm_03. Search and list tasks allocated to emp_analyst_03; if fewer than 2 tasks are found, duplicate task_011 as "Performance benchmarking suite" for emp_analyst_03. Examine task_009's history to track modification frequency. Establish a dependency with task_019 relying on task_017. Allocate 4 hours for emp_dev_08 on task_013 with the annotation "Email service optimization completed". Elevate the priority of task_006 to critical status. If any threats in sprint_002 include "High number of blocked tasks," resolve task_015 with the resolution "Emergency allocation of QA resources" while applying unblock_dependencies=true. Record the lowest completed points from the team's performance and the initial velocity from individual velocities.""",
        actions=[
            Action(name="GenerateSprintReport", kwargs={"sprint_id": "sprint_001"}),
            Action(name="GetEmployeeWorkload", kwargs={"employee_id": "emp_dev_07"}),
            Action(
                name="ReassignTask",
                kwargs={
                    "task_id": "task_020",
                    "new_assignee_id": "emp_dev_07",
                },
            ),
            Action(
                name="GetTeamVelocity",
                kwargs={"team_id": "team_analytics_01", "last_n_sprints": 3},
            ),
            Action(
                name="CreateTask",
                kwargs={
                    "title": "Velocity improvement workshop",
                    "description": "Workshop to address declining team velocity",
                    "assignee_id": "emp_pm_03",
                    "priority": "critical",
                    "story_points": 5,
                },
            ),
            Action(name="SearchTasks", kwargs={"assignee_id": "emp_analyst_03"}),
            Action(
                name="CloneTask",
                kwargs={
                    "source_task_id": "task_011",
                    "new_title": "Performance benchmarking suite",
                    "new_assignee_id": "emp_analyst_03",
                },
            ),
            Action(name="GetTaskHistory", kwargs={"task_id": "task_009"}),
            Action(
                name="CreateTaskDependency",
                kwargs={"task_id": "task_019", "depends_on_task_id": "task_017"},
            ),
            Action(
                name="LogTimeOnTask",
                kwargs={
                    "task_id": "task_013",
                    "hours_logged": 4,
                    "employee_id": "emp_dev_08",
                    "notes": "Email service optimization completed",
                },
            ),
            Action(
                name="UpdateTaskPriority",
                kwargs={
                    "task_id": "task_006",
                    "new_priority": "critical",
                },
            ),
            Action(name="GenerateSprintReport", kwargs={"sprint_id": "sprint_002"}),
            Action(
                name="ResolveBlockedTask",
                kwargs={
                    "task_id": "task_015",
                    "resolution": "Emergency allocation of QA resources",
                    "unblock_dependencies": True,
                },
            ),
        ],
        outputs=['"completed_points": 0', '"individual_velocities": [28]'],
    ),
    Task(
        annotator="0",
        user_id="retrospective_action_implementer",
        instruction="""As the manager of continuous improvement responsible for implementing sprint_001's retrospective action items, you are to retrieve the history of task_013, then duplicate it as "Email service v2 - Modular design" for emp_dev_08. Procure the velocity for team_analytics_01 across 2 sprints. Initiate "Retrospective action items tracker" with the description "Track and measure impact of retrospective action items", assigning 4 story points to emp_analyst_02 with high priority. Verify time logging adherence for all tasks. Log 2 hours on task_006 by emp_dev_07, annotated "Retrospective compliance improvement," and similarly for task_011 by emp_qa_02. Upgrade task_006 to high priority status. Create a dependency with task_019 dependent on task_006. Identify backlog tasks of medium priority. Replicate task_010 as "Automated retrospective insights" for emp_pm_04. Calculate team_qa_01 capacity. Formulate "QA capacity expansion planning" with the description "Plan QA team expansion based on retrospective feedback", assigning 6 story points to emp_qa_02 with critical priority. Transition task_014 to sprint_002. Reallocate task_006 to emp_analyst_03. Communicate the velocity, count of moved tasks, and the status of success.""",
        actions=[
            Action(name="GetTaskHistory", kwargs={"task_id": "task_013"}),
            Action(
                name="CloneTask",
                kwargs={
                    "source_task_id": "task_013",
                    "new_title": "Email service v2 - Modular design",
                    "new_assignee_id": "emp_dev_08",
                },
            ),
            Action(
                name="GetTeamVelocity",
                kwargs={"team_id": "team_analytics_01", "last_n_sprints": 2},
            ),
            Action(
                name="CreateTask",
                kwargs={
                    "title": "Retrospective action items tracker",
                    "description": "Track and measure impact of retrospective action items",
                    "assignee_id": "emp_analyst_02",
                    "priority": "high",
                    "story_points": 4,
                },
            ),
            Action(name="CheckTimeLoggingCompliance", kwargs={"check_all": True}),
            Action(
                name="LogTimeOnTask",
                kwargs={
                    "task_id": "task_006",
                    "hours_logged": 2,
                    "employee_id": "emp_dev_07",
                    "notes": "Retrospective compliance improvement",
                },
            ),
            Action(
                name="LogTimeOnTask",
                kwargs={
                    "task_id": "task_011",
                    "hours_logged": 2,
                    "employee_id": "emp_qa_02",
                    "notes": "Retrospective compliance improvement",
                },
            ),
            Action(
                name="UpdateTaskPriority",
                kwargs={
                    "task_id": "task_006",
                    "new_priority": "high",
                },
            ),
            Action(
                name="CreateTaskDependency",
                kwargs={"task_id": "task_019", "depends_on_task_id": "task_006"},
            ),
            Action(name="GetBacklogTasks", kwargs={"priority": "medium"}),
            Action(
                name="CloneTask",
                kwargs={
                    "source_task_id": "task_010",
                    "new_title": "Automated retrospective insights",
                    "new_assignee_id": "emp_pm_04",
                },
            ),
            Action(name="CalculateTeamCapacity", kwargs={"team_id": "team_qa_01"}),
            Action(
                name="CreateTask",
                kwargs={
                    "title": "QA capacity expansion planning",
                    "description": "Plan QA team expansion based on retrospective feedback",
                    "assignee_id": "emp_qa_02",
                    "priority": "critical",
                    "story_points": 6,
                },
            ),
            Action(
                name="BulkMoveTasksToSprint",
                kwargs={
                    "task_ids": ["task_014"],
                    "target_sprint_id": "sprint_002",
                },
            ),
            Action(
                name="ReassignTask",
                kwargs={
                    "task_id": "task_006",
                    "new_assignee_id": "emp_analyst_03",
                },
            ),
            Action(name="GenerateSprintReport", kwargs={"sprint_id": "sprint_001"}),
        ],
        outputs=['"velocity": 28', '"moved_count": 1', '"success": true'],
    ),
    Task(
        annotator="0",
        user_id="capacity_rebalancer",
        instruction="""You are the resource optimization director. Compute capacity for team_qa_01 and sprint_002. Adjust task_008 priority to critical. Record 6 hours on task_008 for emp_test_05 with notes "Accelerating test coverage to unblock dependencies". Examine blocked tasks for escalation in sprint_002. Formulate "Dependency resolution war room" task_041 with description "Coordinate resolution of dependency blockers" allocated 4 story points for emp_pm_03 with critical priority. Replicate task_002 as task_042 ("Dependency mapping documentation") for emp_arch_01 in sprint_002. Delegate task_008 to emp_sec_test_01. Retrieve sprint_002 details. Mass relocate task_020 and task_011 to sprint_003. Conclude task_015 with resolution "Capacity freed up through rebalancing" (set unblock dependencies as false). Document 2 hours on task_010 for emp_dev_21 with notes "Documentation time allocation". Provide the QA team utilization, the number of tasks requiring escalation, and the sprint's planned story points.""",
        actions=[
            Action(
                name="CalculateTeamCapacity",
                kwargs={"team_id": "team_qa_01", "sprint_id": "sprint_002"},
            ),
            Action(
                name="UpdateTaskPriority",
                kwargs={
                    "task_id": "task_008",
                    "new_priority": "critical",
                },
            ),
            Action(
                name="LogTimeOnTask",
                kwargs={
                    "task_id": "task_008",
                    "hours_logged": 6,
                    "employee_id": "emp_test_05",
                    "notes": "Accelerating test coverage to unblock dependencies",
                },
            ),
            Action(
                name="CheckBlockedTasksForEscalation",
                kwargs={"sprint_id": "sprint_002"},
            ),
            Action(
                name="CreateTask",
                kwargs={
                    "title": "Dependency resolution war room",
                    "new_task_id": "task_041",
                    "description": "Coordinate resolution of dependency blockers",
                    "assignee_id": "emp_pm_03",
                    "priority": "critical",
                    "story_points": 4,
                    "sprint_id": "sprint_002",
                },
            ),
            Action(
                name="CloneTask",
                kwargs={
                    "source_task_id": "task_002",
                    "new_task_id": "task_042",
                    "new_title": "Dependency mapping documentation",
                    "sprint_id": "sprint_002",
                    "new_assignee_id": "emp_arch_01",
                },
            ),
            Action(
                name="ReassignTask",
                kwargs={
                    "task_id": "task_008",
                    "new_assignee_id": "emp_sec_test_01",
                },
            ),
            Action(name="GetSprintDetails", kwargs={"sprint_id": "sprint_002"}),
            Action(
                name="BulkMoveTasksToSprint",
                kwargs={
                    "task_ids": ["task_020", "task_011"],
                    "target_sprint_id": "sprint_003",
                },
            ),
            Action(
                name="SearchTasks",
                kwargs={"task_id": "task_015"}
            ),
            Action(
                name="UpdateTaskStatus",
                kwargs={"task_id": "task_004", "new_status": "done"},
            ),
            Action(
                name="UpdateTaskStatus",
                kwargs={"task_id": "task_012", "new_status": "done"},
            ),
            Action(
                name="ResolveBlockedTask",
                kwargs={
                    "task_id": "task_015",
                    "resolution": "Capacity freed up through rebalancing",
                    "unblock_dependencies": False,
                },
            ),
            Action(
                name="LogTimeOnTask",
                kwargs={
                    "task_id": "task_010",
                    "hours_logged": 2,
                    "employee_id": "emp_dev_21",
                    "notes": "Documentation time allocation",
                },
            ),
        ],
        outputs=[
            '"team_utilization": 0.0',
            '"tasks_needing_escalation": 1',
            '"planned_story_points": 45',
        ],
    ),
    Task(
        annotator="0",
        user_id="escalation_pattern_analyzer",
        instruction="""You are the PMO process analyst examining escalation patterns. Obtain details for task_005. Establish task "Security license procurement checklist" with description "Prevent license blockers" with 3 story points for emp_pm_04 with high priority. Assess blocked tasks for escalation across all sprints. Retrieve details for task_015. Develop "Fast-track approval process" with description "Streamline approvals" and 5 story points for emp_pm_03 with critical priority. Acquire details for task_001, task_005, and task_014. Duplicate task_001 as "Escalation prevention playbook" for emp_pm_04. Determine workload for emp_pm_03 and emp_pm_04. Organize "Monthly escalation review meeting" with description "Review escalations" containing 2 story points and medium priority for emp_pm_03. Resolve task_015 with resolution "Escalation analysis triggered expedited resolution". Verify time logging compliance for sprint_002. Initiate medium-priority "Automated time tracking reminders" task with description "Time logging reminders" with 2 story points for emp_devops_02. Compile a sprint report for sprint_002 and present the total tasks.""",
        actions=[
            Action(name="GetTaskDetails", kwargs={"task_id": "task_005"}),
            Action(
                name="CreateTask",
                kwargs={
                    "title": "Security license procurement checklist",
                    "description": "Prevent license blockers",
                    "assignee_id": "emp_pm_04",
                    "priority": "high",
                    "story_points": 3,
                },
            ),
            Action(
                name="CheckBlockedTasksForEscalation",
                kwargs={"check_all_sprints": True},
            ),
            Action(name="GetTaskDetails", kwargs={"task_id": "task_015"}),
            Action(
                name="CreateTask",
                kwargs={
                    "title": "Fast-track approval process",
                    "description": "Streamline approvals",
                    "assignee_id": "emp_pm_03",
                    "priority": "critical",
                    "story_points": 5,
                },
            ),
            Action(name="GetTaskDetails", kwargs={"task_id": "task_001"}),
            Action(name="GetTaskDetails", kwargs={"task_id": "task_005"}),
            Action(name="GetTaskDetails", kwargs={"task_id": "task_014"}),
            Action(
                name="CloneTask",
                kwargs={
                    "source_task_id": "task_001",
                    "new_title": "Escalation prevention playbook",
                    "new_assignee_id": "emp_pm_04",
                },
            ),
            Action(name="GetEmployeeWorkload", kwargs={"employee_id": "emp_pm_03"}),
            Action(name="GetEmployeeWorkload", kwargs={"employee_id": "emp_pm_04"}),
            Action(
                name="CreateTask",
                kwargs={
                    "title": "Monthly escalation review meeting",
                    "description": "Review escalations",
                    "assignee_id": "emp_pm_03",
                    "priority": "medium",
                    "story_points": 2,
                },
            ),
            Action(
                name="ResolveBlockedTask",
                kwargs={
                    "task_id": "task_015",
                    "resolution": "Escalation analysis triggered expedited resolution",
                    "unblock_dependencies": True,
                },
            ),
            Action(
                name="CheckTimeLoggingCompliance", kwargs={"sprint_id": "sprint_002"}
            ),
            Action(
                name="CreateTask",
                kwargs={
                    "title": "Automated time tracking reminders",
                    "description": "Time logging reminders",
                    "assignee_id": "emp_devops_02",
                    "priority": "medium",
                    "story_points": 2,
                },
            ),
            Action(name="GenerateSprintReport", kwargs={"sprint_id": "sprint_002"}),
        ],
        outputs=['"total_tasks": 8'],
    ),
    Task(
        annotator="0",
        user_id="estimation_accuracy_optimizer",
        instruction="""As the estimation accuracy specialist, your role is to analyze time logging patterns. Retrieve task details for task_001, task_002, and task_009. Adjust the priority of task_009 to high. Record 3 hours on task_009 for emp_devops_02, including notes "Retroactive compliance - minimum threshold". Duplicate task_003 as task_050 ("API endpoint for user profile - Pair Programming Session") for emp_dev_08. Obtain details for task_020 and task_008. Document 4 hours on task_008 for emp_test_05 with the note "Ensuring dependency has sufficient progress". Generate a new task called "Story point calibration workshop" task_051 with a description of "Workshop to improve estimation accuracy based on historical data" allocated with 3 story points for emp_pm_04 with a high priority. Gather the workload of emp_dev_08. Shift tasks task_006 and task_011 to sprint_003. Assign task_006 to emp_dev_08. Organize a retrospective for sprint_001 with what_went_well: ["Time tracking improved", "Story point accuracy increasing", "Bench resources utilized effectively"], what_needs_improvement: ["Setup tasks consistently underestimated", "Integration test dependencies unclear", "Need better estimation guidelines"], action_items: ["Implement 2x multiplier for setup tasks", "Create dependency visualization", "Run estimation workshop"]. Compute the capacity of team_dev_01 for sprint_002. Report the time logged from task_001, the hours logged for compliance, and the success of the retrospective.""",
        actions=[
            Action(name="GetTaskDetails", kwargs={"task_id": "task_001"}),
            Action(name="GetTaskDetails", kwargs={"task_id": "task_002"}),
            Action(name="GetTaskDetails", kwargs={"task_id": "task_009"}),
            Action(
                name="UpdateTaskPriority",
                kwargs={
                    "task_id": "task_009",
                    "new_priority": "high",
                },
            ),
            Action(
                name="LogTimeOnTask",
                kwargs={
                    "task_id": "task_009",
                    "hours_logged": 3,
                    "employee_id": "emp_devops_02",
                    "notes": "Retroactive compliance - minimum threshold",
                },
            ),
            Action(
                name="CloneTask",
                kwargs={
                    "source_task_id": "task_003",
                    "new_task_id": "task_050",
                    "new_title": "API endpoint for user profile - Pair Programming Session",
                    "new_assignee_id": "emp_dev_08",
                },
            ),
            Action(name="GetTaskDetails", kwargs={"task_id": "task_020"}),
            Action(name="GetTaskDetails", kwargs={"task_id": "task_008"}),
            Action(
                name="LogTimeOnTask",
                kwargs={
                    "task_id": "task_008",
                    "hours_logged": 4,
                    "employee_id": "emp_test_05",
                    "notes": "Ensuring dependency has sufficient progress",
                },
            ),
            Action(
                name="CreateTask",
                kwargs={
                    "title": "Story point calibration workshop",
                    "new_task_id": "task_051",
                    "description": "Workshop to improve estimation accuracy based on historical data",
                    "assignee_id": "emp_pm_04",
                    "priority": "high",
                    "story_points": 3,
                },
            ),
            Action(name="GetEmployeeWorkload", kwargs={"employee_id": "emp_dev_08"}),
            Action(
                name="BulkMoveTasksToSprint",
                kwargs={
                    "task_ids": ["task_006", "task_011"],
                    "target_sprint_id": "sprint_003",
                },
            ),
            Action(
                name="ReassignTask",
                kwargs={
                    "task_id": "task_006",
                    "new_assignee_id": "emp_dev_08",
                },
            ),
            Action(
                name="CreateSprintRetrospective",
                kwargs={
                    "sprint_id": "sprint_001",
                    "what_went_well": [
                        "Time tracking improved",
                        "Story point accuracy increasing",
                        "Bench resources utilized effectively",
                    ],
                    "what_needs_improvement": [
                        "Setup tasks consistently underestimated",
                        "Integration test dependencies unclear",
                        "Need better estimation guidelines",
                    ],
                    "action_items": [
                        "Implement 2x multiplier for setup tasks",
                        "Create dependency visualization",
                        "Run estimation workshop",
                    ],
                },
            ),
            Action(
                name="CalculateTeamCapacity",
                kwargs={"team_id": "team_dev_01", "sprint_id": "sprint_002"},
            ),
        ],
        outputs=['"time_logged": 32', '"hours": 3', '"success": true'],
    ),
    Task(
        annotator="0",
        user_id="qa_process_coordinator",
        instruction="""As the QA process coordinator, elevate task_011 priority to high due to the urgency of load testing. Allocate 6 hours for task_003 dedicated to API finalization. Establish a coordination task titled "Load testing environment setup" assigned 4 story points to emp_qa_02 with high priority. Transfer task_020 to emp_qa_02 to ensure workload balancing. Duplicate task_020 as "Security integration tests" for emp_sec_test_01. Provide a report on emp_qa_02's final workload_rating and the total_active_story_points.""",
        actions=[
            Action(
                name="UpdateTaskPriority",
                kwargs={
                    "task_id": "task_011",
                    "new_priority": "high",
                },
            ),
            Action(name="GetTaskDetails", kwargs={"task_id": "task_003"}),
            Action(
                name="LogTimeOnTask",
                kwargs={
                    "task_id": "task_003",
                    "hours_logged": 6,
                    "employee_id": "emp_dev_21",
                    "notes": "API finalization",
                },
            ),
            Action(
                name="CreateTask",
                kwargs={
                    "title": "Load testing environment setup",
                    "assignee_id": "emp_qa_02",
                    "priority": "high",
                    "story_points": 4,
                },
            ),
            Action(
                name="ReassignTask",
                kwargs={
                    "task_id": "task_020",
                    "new_assignee_id": "emp_qa_02",
                },
            ),
            Action(
                name="CloneTask",
                kwargs={
                    "source_task_id": "task_020",
                    "new_title": "Security integration tests",
                    "new_assignee_id": "emp_sec_test_01",
                },
            ),
            Action(name="GetEmployeeWorkload", kwargs={"employee_id": "emp_qa_02"}),
        ],
        outputs=['"workload_rating": "normal"', '"total_active_story_points": 17'],
    ),
    Task(
        annotator="0",
        user_id="sprint_planning_coordinator",
        instruction="""As the sprint planning coordinator for team_mobile_01, retrieve the team's velocity history from the past 3 sprints to determine the capacity for sprint_003. Allocate task_007 and task_018 to sprint_003. Initiate sprint_003 and deliver the total points, team capacity, and average velocity for the sprint.""",
        actions=[
            Action(
                name="GetTeamVelocity",
                kwargs={"team_id": "team_mobile_01", "last_n_sprints": 3},
            ),
            Action(
                name="CalculateTeamCapacity", kwargs={"team_id": "team_mobile_01"}
            ),
            Action(
                name="BulkMoveTasksToSprint",
                kwargs={
                    "task_ids": ["task_007", "task_018"],
                    "target_sprint_id": "sprint_003",
                },
            ),
            Action(
                name="UpdateSprintStatus",
                kwargs={"sprint_id": "sprint_003", "new_status": "active"},
            ),
        ],
        outputs=[
            '"planned_story_points": 16',
            '"total_capacity_points": 60',
            '"average_velocity": 0',
        ],
    ),
    Task(
        annotator="0",
        user_id="sprint_optimization_lead",
        instruction="""As the sprint optimization specialist for sprint_002, transfer task_004 from emp_dev_20 to emp_dev_15 to achieve load balancing. Generate a "Sprint Recovery Plan" task (task_050) within sprint_002, attributing 3 story points to emp_pm_04 with high criticality. Amend the priority of task_016 to critical. Redirect task_016 to emp_dev_08 and incorporate it into sprint_002. Record 2 hours on task_019 to assess sprint health. Elevate task_004's priority to critical. Provide the completion percentage.""",
        actions=[
            Action(
                name="ReassignTask",
                kwargs={
                    "task_id": "task_004",
                    "new_assignee_id": "emp_dev_15",
                },
            ),
            Action(
                name="CreateTask",
                kwargs={
                    "title": "Sprint Recovery Plan",
                    "new_task_id": "task_050",
                    "assignee_id": "emp_pm_04",
                    "priority": "critical",
                    "story_points": 3,
                    "sprint_id": "sprint_002",
                },
            ),
            Action(name="GetTaskDetails", kwargs={"task_id": "task_016"}),
            Action(
                name="UpdateTaskPriority",
                kwargs={
                    "task_id": "task_016",
                    "new_priority": "critical",
                },
            ),
            Action(
                name="ReassignTask",
                kwargs={
                    "task_id": "task_016",
                    "new_assignee_id": "emp_dev_08",
                },
            ),
            Action(
                name="AssignTaskToSprint",
                kwargs={"task_id": "task_016", "sprint_id": "sprint_002"},
            ),
            Action(name="GetTaskDetails", kwargs={"task_id": "task_019"}),
            Action(
                name="LogTimeOnTask",
                kwargs={
                    "task_id": "task_019",
                    "hours_logged": 2,
                    "employee_id": "emp_devops_02",
                    "notes": "Monitoring sprint health",
                },
            ),
            Action(name="GetTaskDetails", kwargs={"task_id": "task_004"}),
            Action(
                name="UpdateTaskPriority",
                kwargs={
                    "task_id": "task_004",
                    "new_priority": "critical",
                },
            ),
            Action(name="GenerateSprintReport", kwargs={"sprint_id": "sprint_002"}),
        ],
        outputs=['"completion_percentage": 0.0'],
    ),
    Task(
        annotator="0",
        user_id="analytics_performance_manager",
        instruction="""Serve as the analytics team leader. Determine team_analytics_01 velocity trends for the last sprint. Transfer task_010 to emp_analyst_03 to distribute workload evenly. Initiate a knowledge sharing, medium-priority task "SQL optimization workshop" with 3 story points for emp_analyst_02. Verify time compliance for sprint_001. Record 2 hours on task_006. Modify task_011 priority to high to accommodate load testing requirements. Report the team average velocity and total number of non-compliant tasks.""",
        actions=[
            Action(
                name="GetTeamVelocity",
                kwargs={"team_id": "team_analytics_01", "last_n_sprints": 1},
            ),
            Action(
                name="ReassignTask",
                kwargs={
                    "task_id": "task_010",
                    "new_assignee_id": "emp_analyst_03",
                },
            ),
            Action(
                name="CreateTask",
                kwargs={
                    "title": "SQL optimization workshop",
                    "assignee_id": "emp_analyst_02",
                    "priority": "medium",
                    "story_points": 3,
                },
            ),
            Action(
                name="CheckTimeLoggingCompliance", kwargs={"sprint_id": "sprint_001"}
            ),
            Action(name="GetTaskDetails", kwargs={"task_id": "task_006"}),
            Action(
                name="LogTimeOnTask",
                kwargs={
                    "task_id": "task_006",
                    "hours_logged": 2,
                    "employee_id": "emp_dev_07",
                },
            ),
            Action(
                name="UpdateTaskPriority",
                kwargs={
                    "task_id": "task_011",
                    "new_priority": "high",
                },
            ),
        ],
        outputs=[
            '"average_velocity": 28.0',
            '"non_compliant_count": 5',
        ],
    ),
    Task(
        annotator="0",
        user_id="sprint_risk_mitigator",
        instruction="""Act as the PMO risk manager tasked with identifying and alleviating sprint risks. Transfer task_010 to emp_analyst_03 to ensure workload balance. Establish a "Workload Balancing Review" task in sprint_002 with 4 story points assigned to emp_pm_04 as high priority. Inspect blocked tasks needing escalation in sprint_002. In case blocked tasks are detected, allocate the first task to emp_head_eng. Adjust task_005's priority to critical for the security audit critical path. Register 3 hours on task_012 with 'RBAC implementation progress' noted and emp_sec_dev_02 as the employee ID. Duplicate task_011 as "Performance Testing Suite" for emp_qa_02. Compute final team capacity (consider team_dev_01) and provide a report on the number of escalations created along with the final team utilization percentage.""",
        actions=[
            Action(
                name="ReassignTask",
                kwargs={
                    "task_id": "task_010",
                    "new_assignee_id": "emp_analyst_03",
                },
            ),
            Action(
                name="CreateTask",
                kwargs={
                    "title": "Workload Balancing Review",
                    "assignee_id": "emp_pm_04",
                    "priority": "high",
                    "story_points": 4,
                    "sprint_id": "sprint_002",
                },
            ),
            Action(
                name="CheckBlockedTasksForEscalation",
                kwargs={"sprint_id": "sprint_002"},
            ),
            Action(
                name="EscalateTask",
                kwargs={
                    "task_id": "task_015",
                    "escalate_to": "emp_head_eng",
                },
            ),
            Action(
                name="UpdateTaskPriority",
                kwargs={
                    "task_id": "task_005",
                    "new_priority": "critical",
                },
            ),
            Action(
                name="LogTimeOnTask",
                kwargs={
                    "task_id": "task_012",
                    "hours_logged": 3,
                    "employee_id": "emp_sec_dev_02",
                    "notes": "RBAC implementation progress",
                },
            ),
            Action(
                name="CloneTask",
                kwargs={
                    "source_task_id": "task_011",
                    "new_title": "Performance Testing Suite",
                    "new_assignee_id": "emp_qa_02",
                },
            ),
            Action(
                name="CalculateTeamCapacity",
                kwargs={"team_id": "team_dev_01", "sprint_id": "sprint_002"},
            ),
        ],
        outputs=[
            '"new_escalation_created": true',
            '"team_utilization": 22.5',
            '"tasks_needing_escalation": 1',
        ],
    ),
    Task(
        annotator="0",
        user_id="resource_allocation_optimizer",
        instruction="""You are the resource optimization lead. Handle an infrastructure task "Cloud migration planning" with 8 story points for emp_devops_04 as a critical priority. Modify task_014's priority to critical due to data migration urgency and assign it to sprint_002. Identify blocked tasks that require escalation in sprint_002. If any exist, escalate the first one to emp_head_eng. Provide the team utilization for team_devops_01 and the count of blocked tasks.""",
        actions=[
            Action(
                name="CreateTask",
                kwargs={
                    "title": "Cloud migration planning",
                    "assignee_id": "emp_devops_04",
                    "priority": "critical",
                    "story_points": 8,
                    "sprint_id": "sprint_002",
                },
            ),
            Action(name="SearchTasks", kwargs={"task_id": "task_014"}),
            Action(
                name="UpdateTaskPriority",
                kwargs={
                    "task_id": "task_014",
                    "new_priority": "critical",
                },
            ),
            Action(
                name="AssignTaskToSprint",
                kwargs={"task_id": "task_014", "sprint_id": "sprint_002"},
            ),
            Action(
                name="CheckBlockedTasksForEscalation",
                kwargs={"sprint_id": "sprint_002"},
            ),
            Action(
                name="EscalateTask",
                kwargs={
                    "task_id": "task_015",
                    "escalate_to": "emp_head_eng",
                },
            ),
            Action(
                name="CalculateSprintBurndown", kwargs={"sprint_id": "sprint_002"}
            ),
            Action(
                name="CalculateTeamCapacity",
                kwargs={"team_id": "team_devops_01", "sprint_id": "sprint_002"},
            ),
        ],
        outputs=[
            '"team_utilization": 27.5',
            '"blocked_tasks": 2',
            '"new_escalation_created": true',
        ],
    ),
    Task(
        annotator="0",
        user_id="security_incident_response",
        instruction="""You are the security incident response coordinator. A critical security vulnerability has been identified in proj_banking_01. Coordinate a critical task "Emergency security patch - Banking" with description "Critical vulnerability patching for banking integration" with 8 story points for emp_sec_dev_01 in sprint_002. Change task_011 priority to critical. Address blocked task_005 with resolution "Emergency override for critical vulnerability". Log 4 hours on task_005 with notes "Emergency security audit". Reallocate task_012 to emp_dev_07. Manage a critical task "Penetration testing - Banking hotfix" with description "Security testing for banking patch" with 5 story points for emp_sec_test_01. Detect blocked tasks needing escalation in sprint_002. Escalate task_015 to emp_head_eng. Initiate a "Sprint Risk Mitigation" critical-priority task with description "Address sprint risks" with 3 story points for emp_pm_04. Present the completion percentage, total blocked tasks, and indicate if new escalations were initiated.""",
        actions=[
            Action(
                name="CreateTask",
                kwargs={
                    "title": "Emergency security patch - Banking",
                    "description": "Critical vulnerability patching for banking integration",
                    "assignee_id": "emp_sec_dev_01",
                    "priority": "critical",
                    "story_points": 8,
                    "sprint_id": "sprint_002",
                },
            ),
            Action(
                name="UpdateTaskPriority",
                kwargs={
                    "task_id": "task_011",
                    "new_priority": "critical",
                },
            ),
            Action(
                name="ResolveBlockedTask",
                kwargs={
                    "task_id": "task_005",
                    "resolution": "Emergency override for critical vulnerability",
                    "unblock_dependencies": True,
                },
            ),
            Action(
                name="LogTimeOnTask",
                kwargs={
                    "task_id": "task_005",
                    "hours_logged": 4,
                    "employee_id": "emp_sec_dev_01",
                    "notes": "Emergency security audit",
                },
            ),
            Action(
                name="ReassignTask",
                kwargs={
                    "task_id": "task_012",
                    "new_assignee_id": "emp_dev_07",
                },
            ),
            Action(
                name="CreateTask",
                kwargs={
                    "title": "Penetration testing - Banking hotfix",
                    "description": "Security testing for banking patch",
                    "assignee_id": "emp_sec_test_01",
                    "priority": "critical",
                    "story_points": 5,
                    "sprint_id": "sprint_002",
                },
            ),
            Action(
                name="CheckBlockedTasksForEscalation",
                kwargs={"sprint_id": "sprint_002"},
            ),
            Action(
                name="EscalateTask",
                kwargs={
                    "task_id": "task_015",
                    "escalate_to": "emp_head_eng",
                },
            ),
            Action(
                name="CreateTask",
                kwargs={
                    "title": "Sprint Risk Mitigation",
                    "description": "Address sprint risks",
                    "assignee_id": "emp_pm_04",
                    "priority": "critical",
                    "story_points": 3,
                    "sprint_id": "sprint_002",
                },
            ),
            Action(
                name="CalculateSprintBurndown", kwargs={"sprint_id": "sprint_002"}
            ),
            Action(name="GenerateSprintReport", kwargs={"sprint_id": "sprint_002"}),
        ],
        outputs=[
            '"completion_percentage": 0.0',
            '"total_blocked_tasks": 1',
            '"new_escalation_created": true',
        ],
    ),
    Task(
        annotator="0",
        user_id="compliance_enforcer",
        instruction="""As the QA lead, your responsibility is to ensure time logging adherence. Verify compliance for sprint_002. Record 3 hours for task_004. Set up a reminder task "Time logging compliance review" with 2 story points assigned to emp_qa_02, maintaining normal priority status. Review any blocked tasks for potential escalation. If necessary, escalate task_015 to emp_head_qa. Provide me with the final count of compliance and indicate if a new escalation has been initiated.""",
        actions=[
            Action(
                name="CheckTimeLoggingCompliance", kwargs={"sprint_id": "sprint_002"}
            ),
            Action(name="SearchTasks", kwargs={"task_id": "task_004"}),
            Action(
                name="LogTimeOnTask",
                kwargs={
                    "task_id": "task_004",
                    "hours_logged": 3,
                    "employee_id": "emp_dev_20",
                },
            ),
            Action(
                name="CreateTask",
                kwargs={
                    "title": "Time logging compliance review",
                    "assignee_id": "emp_qa_02",
                    "priority": "medium",
                    "story_points": 2,
                },
            ),
            Action(
                name="CheckBlockedTasksForEscalation",
                kwargs={"sprint_id": "sprint_002"},
            ),
            Action(
                name="EscalateTask",
                kwargs={
                    "task_id": "task_015",
                    "escalate_to": "emp_head_qa",
                },
            ),
            Action(
                name="CheckTimeLoggingCompliance", kwargs={"sprint_id": "sprint_002"}
            ),
        ],
        outputs=[
            '"non_compliant_count": 4',
            '"new_escalation_created": true',
            '"tasks_needing_escalation": 1',
        ],
    ),
    Task(
        annotator="0",
        user_id="sprint_velocity_analysis",
        instruction="""Act as the scrum master for team_dev_01. Determine the team's average velocity over the past 3 sprints, evaluate the burndown progress of sprint_002, and pinpoint any blocked tasks remaining that have not yet been escalated. Elevate the first such task you find to emp_head_eng, and then convey the sprint completion rate.""",
        actions=[
            Action(
                name="GetTeamVelocity",
                kwargs={"team_id": "team_dev_01", "last_n_sprints": 3},
            ),
            Action(
                name="CalculateSprintBurndown", kwargs={"sprint_id": "sprint_002"}
            ),
            Action(
                name="CheckBlockedTasksForEscalation",
                kwargs={"sprint_id": "sprint_002"},
            ),
            Action(
                name="EscalateTask",
                kwargs={
                    "task_id": "task_015",
                    "escalate_to": "emp_head_eng",
                },
            ),
            Action(
                name="CalculateSprintBurndown", kwargs={"sprint_id": "sprint_002"}
            ),
        ],
        outputs=[
            '"average_velocity": 18.0',
            '"completion_percentage": 0.0',
            '"blocked_points": 21',
        ],
    ),
    Task(
        annotator="0",
        user_id="devops_platform_optimization",
        instruction="""As the lead for DevOps platform optimization, handle a
        critical task entitled "Container orchestration optimization" with the description
        "Optimize container orchestration" assigning 6 story points to
        emp_devops_04. Modify task_006 to a critical priority. Assign task_006
        to emp_devops_04. Establish a dependency such that task_019 relies on task_006.
        Record 5 hours on task_006 with commentary "Performance bottleneck analysis
        completed". Set task_019 to a high priority. Initiate task "Kubernetes
        cluster scaling automation" with the details "Implement auto-scaling"
        allotting 8 story points to emp_devops_04, marked as critical priority. Transfer
        task_005 to emp_head_eng. Compute the capacity of team_devops_01 for
        sprint_002. Convey the team's utilization metrics.""",
        actions=[
            Action(
                name="CreateTask",
                kwargs={
                    "title": "Container orchestration optimization",
                    "description": "Optimize container orchestration",
                    "assignee_id": "emp_devops_04",
                    "priority": "critical",
                    "story_points": 6,
                },
            ),
            Action(
                name="UpdateTaskPriority",
                kwargs={
                    "task_id": "task_006",
                    "new_priority": "critical",
                },
            ),
            Action(
                name="ReassignTask",
                kwargs={
                    "task_id": "task_006",
                    "new_assignee_id": "emp_devops_04",
                },
            ),
            Action(
                name="CreateTaskDependency",
                kwargs={"task_id": "task_019", "depends_on_task_id": "task_006"},
            ),
            Action(
                name="LogTimeOnTask",
                kwargs={
                    "task_id": "task_006",
                    "hours_logged": 5,
                    "employee_id": "emp_devops_04",
                    "notes": "Performance bottleneck analysis completed",
                },
            ),
            Action(
                name="UpdateTaskPriority",
                kwargs={
                    "task_id": "task_019",
                    "new_priority": "high",
                },
            ),
            Action(
                name="CreateTask",
                kwargs={
                    "title": "Kubernetes cluster scaling automation",
                    "description": "Implement auto-scaling",
                    "assignee_id": "emp_devops_04",
                    "priority": "critical",
                    "story_points": 8,
                },
            ),
            Action(
                name="EscalateTask",
                kwargs={
                    "task_id": "task_005",
                    "escalate_to": "emp_head_eng",
                },
            ),
            Action(
                name="CalculateTeamCapacity",
                kwargs={"team_id": "team_devops_01", "sprint_id": "sprint_002"},
            ),
        ],
        outputs=['"team_utilization": 7.5'],
    ),
    Task(
        annotator="0",
        user_id="resolve_sprint_blocks",
        instruction="""Act as the project manager. Review Sprint 2 (sprint_002)
        for tasks that have been obstructed for over 2 days and require
        escalation. Document the tasks_needing_escalation count from this review.
        Raise any unescorted tasks to emp_head_eng
        (Engineering department head), modify their priority to critical if necessary,
        and reallocate to emp_dev_20. For task_015, also address the blocking
        issue with the solution "Resolved by sprint lead" and transition it to
        in_progress status. Inform me of the count of tasks that require
        escalation.""",
        actions=[
            Action(
                name="CheckBlockedTasksForEscalation",
                kwargs={"sprint_id": "sprint_002"},
            ),
            Action(
                name="EscalateTask",
                kwargs={"task_id": "task_015", "escalate_to": "emp_head_eng"},
            ),
            Action(
                name="UpdateTaskPriority",
                kwargs={
                    "task_id": "task_015",
                    "new_priority": "critical",
                },
            ),
            Action(
                name="ReassignTask",
                kwargs={
                    "task_id": "task_015",
                    "new_assignee_id": "emp_dev_20",
                },
            ),
            Action(
                name="GetTaskDetails",
                kwargs={
                    "task_id": "task_015",
                },
            ),
            Action(
                name="UpdateTaskStatus",
                kwargs={"task_id": "task_004", "new_status": "done"},
            ),
            Action(
                name="UpdateTaskStatus",
                kwargs={"task_id": "task_012", "new_status": "done"},
            ),
            Action(
                name="ResolveBlockedTask",
                kwargs={
                    "task_id": "task_015",
                    "resolution": "Resolved by sprint lead",
                    "unblock_dependencies": True
                },
            ),
            Action(
                name="UpdateTaskStatus",
                kwargs={"task_id": "task_015", "new_status": "in_progress"},
            ),
            Action(name="GenerateSprintReport", kwargs={"sprint_id": "sprint_002"}),
        ],
        outputs=['"tasks_needing_escalation": 1'],
    ),
    Task(
        annotator="0",
        user_id="complete_sprint_cycle",
        instruction="""As the scrum master for sprint_001 with team_analytics_01, identify the number of tasks with noncompliant time logging, determine the velocity trend over the last three sprints, and provide a report on the burndown completion progress and available capacity hours. Ensure that sprint_001 is marked as reviewed.""",
        actions=[
            Action(name="GetSprintDetails", kwargs={"sprint_id": "sprint_001"}),
            Action(
                name="CalculateSprintBurndown", kwargs={"sprint_id": "sprint_001"}
            ),
            Action(name="GenerateSprintReport", kwargs={"sprint_id": "sprint_001"}),
            Action(
                name="CheckTimeLoggingCompliance", kwargs={"sprint_id": "sprint_001"}
            ),
            Action(
                name="GetTeamVelocity",
                kwargs={"team_id": "team_analytics_01", "last_n_sprints": 3},
            ),
            Action(
                name="CalculateTeamCapacity",
                kwargs={"team_id": "team_analytics_01", "sprint_id": "sprint_001"},
            ),
            Action(
                name="MarkSprintAsReviewed",
                kwargs={"sprint_id": "sprint_001"},
            )
        ],
        outputs=[
            '"non_compliant_count": 5',
            '"velocity": 28',
            '"completion_percentage": 90.3',
            '"total_capacity_hours": 180',
        ],
    ),
    Task(
        annotator="0",
        user_id="qa_bottleneck_resolver",
        instruction="""As a specialist in resolving QA bottlenecks, determine team_qa_01's current capacity. Change the priority of task_011 to high and assign it to emp_test_05. Initiate the task "Automated test framework setup" with the description "Set up comprehensive automated testing framework" and allocate 6 story points to emp_sec_test_01 with a high priority level. Create a dependency so that task_020 relies on task_008. Log 5 hours on task_008, noting "Test framework implementation progress". Finalize task_015 and clear any blocked dependencies, noting "Additional QA resources allocated" as the resolution. Review time logging compliance and log 4 hours on task_004, with notes "QA compliance time logging", referencing 'emp_dev_20' as the employee ID. Initiate the "QA process optimization" task with the description "Optimize QA processes to eliminate bottlenecks" and assign 4 story points to emp_qa_02 in sprint_002, marking it with critical priority. Recalculate the final capacity for team_qa_01 in sprint_002. Provide the final team utilization percentage and the number of non-compliant tasks identified before corrections.""",
        actions=[
            Action(name="CalculateTeamCapacity", kwargs={"team_id": "team_qa_01"}),
            Action(
                name="UpdateTaskPriority",
                kwargs={
                    "task_id": "task_011",
                    "new_priority": "high",
                },
            ),
            Action(
                name="ReassignTask",
                kwargs={
                    "task_id": "task_011",
                    "new_assignee_id": "emp_test_05",
                },
            ),
            Action(
                name="CreateTask",
                kwargs={
                    "title": "Automated test framework setup",
                    "description": "Set up comprehensive automated testing framework",
                    "assignee_id": "emp_sec_test_01",
                    "priority": "high",
                    "story_points": 6,
                },
            ),
            Action(
                name="CreateTaskDependency",
                kwargs={"task_id": "task_020", "depends_on_task_id": "task_008"},
            ),
            Action(
                name="LogTimeOnTask",
                kwargs={
                    "task_id": "task_008",
                    "hours_logged": 5,
                    "employee_id": "emp_test_05",
                    "notes": "Test framework implementation progress",
                },
            ),
            Action(
                name="ResolveBlockedTask",
                kwargs={
                    "task_id": "task_015",
                    "resolution": "Additional QA resources allocated",
                    "unblock_dependencies": True,
                },
            ),
            Action(name="CheckTimeLoggingCompliance", kwargs={"check_all": True}),
            Action(
                name="LogTimeOnTask",
                kwargs={
                    "task_id": "task_004",
                    "hours_logged": 4,
                    "employee_id": "emp_dev_20",
                    "notes": "QA compliance time logging",
                },
            ),
            Action(
                name="CreateTask",
                kwargs={
                    "title": "QA process optimization",
                    "description": "Optimize QA processes to eliminate bottlenecks",
                    "assignee_id": "emp_qa_02",
                    "priority": "critical",
                    "story_points": 4,
                    "sprint_id": "sprint_002",
                },
            ),
            Action(
                name="CalculateTeamCapacity",
                kwargs={"team_id": "team_qa_01", "sprint_id": "sprint_002"},
            ),
            Action(name="GenerateSprintReport", kwargs={"sprint_id": "sprint_002"}),
        ],
        outputs=['"team_utilization": 10.0', '"non_compliant_count": 8'],
    ),
    Task(
        annotator="0",
        user_id="conflict_resolution_specialist",
        instruction="""
        As the PMO director responsible for handling resource conflicts, inspect employee
        emp_arch_01's workload across every project. Initiate a coordination task
        titled "Architecture split allocation review" with 5 story points assigned to
        emp_pm_03 in sprint_002 with a critical priority level. Move task_010 from
        emp_dev_21 to emp_arch_01 to even out workload. Adjust the priority of task_010
        to low. Compute and present the final team 'team_dev_01' utilization as well as
        the logged hours for task_010.""",
       actions=[
            Action(name="GetEmployeeWorkload", kwargs={"employee_id": "emp_arch_01"}),
            Action(
                name="CreateTask",
                kwargs={
                    "title": "Architecture split allocation review",
                    "assignee_id": "emp_pm_03",
                    "priority": "critical",
                    "story_points": 5,
                    "sprint_id": "sprint_002",
                },
            ),
            Action(name="SearchTasks", kwargs={"task_id": "task_010"}),
            Action(
                name="ReassignTask",
                kwargs={
                    "task_id": "task_010",
                    "new_assignee_id": "emp_arch_01",
                },
            ),
            Action(
                name="UpdateTaskPriority",
                kwargs={
                    "task_id": "task_010",
                    "new_priority": "low",
                },
            ),
            Action(
                name="CalculateTeamCapacity",
                kwargs={"team_id": "team_dev_01", "sprint_id": "sprint_002"},
            ),
            Action(name="GenerateSprintReport", kwargs={"sprint_id": "sprint_002"}),
        ],
        outputs=[
            '"team_utilization": 22.5',
            '"time_logged": 0',
        ],
    ),
    Task(
        annotator="0",
        user_id="sprint_health_monitor",
        instruction="""As the scrum master accountable for monitoring sprint health,
        compute the burndown for sprint_002. Assess time logging adherence
        to pinpoint any issues. Record 4 hours against task_004. Locate blocked tasks
        within the sprint and change task_015's status to todo to remove the block.
        Determine the final team capacity for team_dev_01 and document the completion
        percentage along with the team's overall utilization.""",
        actions=[
            Action(
                name="CalculateSprintBurndown", kwargs={"sprint_id": "sprint_002"}
            ),
            Action(
                name="CheckTimeLoggingCompliance", kwargs={"sprint_id": "sprint_002"}
            ),
            Action(name="SearchTasks", kwargs={"task_id": "task_004"}),
            Action(
                name="GetTaskDetails",
                kwargs={
                    "task_id": "task_004",
                },
            ),
            Action(
                name="LogTimeOnTask",
                kwargs={
                    "task_id": "task_004",
                    "hours_logged": 4,
                    "employee_id": "emp_dev_20",
                },
            ),
            Action(
                name="SearchTasks",
                kwargs={"status": "blocked", "sprint_id": "sprint_002"},
            ),
            Action(
                name="UpdateTaskStatus",
                kwargs={"task_id": "task_015", "new_status": "todo"},
            ),
            Action(
                name="CalculateTeamCapacity",
                kwargs={"team_id": "team_dev_01", "sprint_id": "sprint_002"},
            ),
            Action(
                name="CalculateSprintBurndown", kwargs={"sprint_id": "sprint_002"}
            ),
        ],
        outputs=[
            '"completion_percentage": 0.0',
            '"team_utilization": 26.2',
            '"non_compliant_count": 4',
        ],
    )
]
