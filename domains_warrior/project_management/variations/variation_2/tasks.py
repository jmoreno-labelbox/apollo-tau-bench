from domains.dto import Action, Task

TASKS = [
    Task(
        annotator="0",
        user_id="cross_team_coordination",
        instruction="""You are the program coordinator. team_mobile_01 needs to
        start sprint_003 but has dependencies on the Web team. Check the
        velocities for team_mobile_01 and team_dev_01 from the last 3 sprints.
        Find high priority tasks in the backlog and check if task_007
        dependencies are resolved. Update the priority to critical if blocked
        and create a high-priority coordination task "Cross-team sync meeting"
        with 3 story points assigned to emp_pm_03 for sprint_003, move task_007
        and task_018 to sprint_003. Check emp_dev_03's workload, and report both
        teams' velocities and the total story points planned for sprint_003.""",
        actions=[
            Action(
                name="get_team_velocity",
                kwargs={"team_id": "team_mobile_01", "last_n_sprints": 3},
            ),
            Action(
                name="get_team_velocity",
                kwargs={"team_id": "team_dev_01", "last_n_sprints": 3},
            ),
            Action(name="get_backlog_tasks", kwargs={"priority": "high"}),
            Action(name="search_tasks", kwargs={"task_id": "task_007"}),
            Action(name="get_task_details", kwargs={"task_id": "task_007"}),
            Action(name="search_tasks", kwargs={"task_id": "task_003"}),
            Action(
                name="update_task_priority",
                kwargs={
                    "task_id": "task_007",
                    "new_priority": "critical",
                },
            ),
            Action(
                name="create_task",
                kwargs={
                    "title": "Cross-team sync meeting",
                    "assignee_id": "emp_pm_03",
                    "priority": "high",
                    "story_points": 3,
                    "sprint_id": "sprint_003",
                },
            ),
            Action(
                name="bulk_move_tasks_to_sprint",
                kwargs={
                    "task_ids": ["task_007", "task_018"],
                    "target_sprint_id": "sprint_003",
                },
            ),
            Action(
                name="get_employee_workload",
                kwargs={"employee_id": "emp_dev_03", "sprint_id": "sprint_003"},
            ),
            Action(
                name="calculate_team_capacity",
                kwargs={"team_id": "team_mobile_01", "sprint_id": "sprint_003"},
            ),
            Action(name="get_sprint_details", kwargs={"sprint_id": "sprint_003"}),
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
        instruction="""You are the scrum master closing sprint_001 for
        team_analytics_01. Check time logging compliance to identify
        non-compliant tasks, log 4 hours for the first non-compliant task found
        to the assigned employee, complete any remaining in-progress or todo tasks by
        updating them to done, update sprint status to completed (if it isn't
        completed already), create a retrospective with items: "Data pipeline
        setup was smooth", and "Estimates need to be more precise". Tell me the
        final velocity and non-compliant count.""",
        actions=[
            Action(name="generate_sprint_report", kwargs={"sprint_id": "sprint_001"}),
            Action(
                name="check_time_logging_compliance", kwargs={"sprint_id": "sprint_001"}
            ),
            Action(
                name="get_task_details",
                kwargs={
                    "task_id": "task_001",
                },
            ),
            Action(
                name="log_time_on_task",
                kwargs={
                    "task_id": "task_001",
                    "hours_logged": 4,
                    "employee_id": "emp_dev_05",
                },
            ),
            Action(
                name="search_tasks",
                kwargs={
                    "sprint_id": "sprint_001",
                }
            ),
            Action(
                name="update_task_status",
                kwargs={
                    "task_id": "task_006",
                    "new_status": "done"
                },
            ),
            Action(
                name="update_sprint_status",
                kwargs={"sprint_id": "sprint_001", "new_status": "completed"},
            ),
            Action(
                name="create_sprint_retrospective",
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
            Action(name="get_sprint_details", kwargs={"sprint_id": "sprint_001"}),
        ],
        outputs=['"velocity": 31', '"non_compliant_count": 5', '"status": "completed"'],
    ),
    Task(
        annotator="0",
        user_id="sprint_crisis_manager",
        instruction="""You are the development manager responsible for
        sprint_002. The sprint is at risk. Escalate blocked task_005 to emp_head_eng. Create a
        critical task "Emergency API hotfix" with description "Fix critical
        production API bug affecting customers" for emp_dev_21 with 5 story
        points in sprint_002. Reassign task_010 to emp_dev_15. Log 6 hours on
        task_003 for emp_dev_21 with notes "API endpoint debugging and fixes".
        Mark all dependencies and blocking tasks for task_004 as done. Resolve
        all blocking tasks for task_004 with resolution "<task_id> completed".
        Then, update task_004 to in_progress. Report the number of blocked tasks.""",
        actions=[
            Action(
                name="escalate_task",
                kwargs={
                    "task_id": "task_005",
                    "escalate_to": "emp_head_eng",
                },
            ),
            Action(
                name="create_task",
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
                name="reassign_task",
                kwargs={
                    "task_id": "task_010",
                    "new_assignee_id": "emp_dev_15",
                },
            ),
            Action(
                name="log_time_on_task",
                kwargs={
                    "task_id": "task_003",
                    "hours_logged": 6,
                    "employee_id": "emp_dev_21",
                    "notes": "API endpoint debugging and fixes",
                },
            ),
            Action(
                name="search_tasks",
                kwargs={"task_id": "task_004"}
            ),
            Action(
                name="update_task_status",
                kwargs={"task_id": "task_003", "new_status": "done"},
            ),
            Action(
                name="resolve_blocked_task",
                kwargs={
                    "task_id": "task_004",
                    "resolution": "task_003 completed",
                    "unblock_dependencies": True,
                },
            ),
            Action(
                name="update_task_status",
                kwargs={"task_id": "task_004", "new_status": "in_progress"},
            ),
            Action(name="generate_sprint_report", kwargs={"sprint_id": "sprint_002"}),
        ],
        outputs=[
            '"blocked_tasks": 2',
        ],
    ),
    Task(
        annotator="0",
        user_id="dependency_resolution_manager",
        instruction="""You are the technical lead. Task_004 is blocked.
        Check its details and dependencies, verify if task_003 is
        complete. If it is not complete, then complete it with 4 hours logged to
        the assigned employee. Next, resolve task_004 blockage setting 'task_003 done' as resolution and
        unblock dependencies as true. Update task_004 status to 'in_progress'. Check task_015, which depends
        on task_004, and update its priority to high since it's blocking
        multiple tasks. Reassign it to emp_dev_20, and calculate sprint burndown. Finally, tell me the number of
        tasks blocked and emp_dev_20's final workload rating.""",
        actions=[
            Action(name="get_task_details", kwargs={"task_id": "task_004"}),
            Action(name="search_tasks", kwargs={"task_id": "task_003"}),
            Action(
                name="get_task_details",
                kwargs={
                    "task_id": "task_003",
                },
            ),
            Action(
                name="log_time_on_task",
                kwargs={
                    "task_id": "task_003",
                    "hours_logged": 4,
                    "employee_id": "emp_dev_21",
                },
            ),
            Action(
                name="update_task_status",
                kwargs={"task_id": "task_003", "new_status": "done"},
            ),
            Action(
                name="resolve_blocked_task",
                kwargs={"task_id": "task_004", "resolution": "task_003 done", "unblock_dependencies": True},
            ),
            Action(
                name="update_task_status",
                kwargs={"task_id": "task_004", "new_status": "in_progress"},
            ),
            Action(name="get_task_details", kwargs={"task_id": "task_015"}),
            Action(
                name="update_task_priority",
                kwargs={
                    "task_id": "task_015",
                    "new_priority": "high",
                },
            ),
            Action(
                name="reassign_task",
                kwargs={
                    "task_id": "task_015",
                    "new_assignee_id": "emp_dev_20",
                },
            ),
            Action(
                name="search_tasks",
                kwargs={"status": "blocked", "sprint_id": "sprint_002"},
            ),
            Action(
                name="get_employee_workload",
                kwargs={"employee_id": "emp_dev_20", "sprint_id": "sprint_002"},
            ),
            Action(
                name="calculate_sprint_burndown", kwargs={"sprint_id": "sprint_002"}
            ),
        ],
        outputs=['"workload_rating": "normal"', '"blocked_tasks": 2'],
    ),
    Task(
        annotator="0",
        user_id="tech_debt_manager",
        instruction="""You are the Technical Architect responsible for managing
        technical debt. Update task_006 priority to critical. Assign task_006 to
        sprint_002. Update task_011 priority to medium. Create task "Database
        indexing optimization" with description "Optimize database indexes for
        performance improvement" with 5 story points for emp_arch_01, critical
        priority in sprint_002. Create dependency between task_019 and task_006.
        Log 4 hours on task_006 with notes "Initial performance profiling
        completed". Reassign task_019 to emp_devops_04. Check time logging
        compliance for sprint_002. Log 3 hours on task_004 with notes "Sprint
        compliance update". Calculate team capacity for team_dev_01 in
        sprint_002. Report the team utilization and non-compliant count.""",
        actions=[
            Action(
                name="update_task_priority",
                kwargs={
                    "task_id": "task_006",
                    "new_priority": "critical",
                },
            ),
            Action(
                name="assign_task_to_sprint",
                kwargs={"task_id": "task_006", "sprint_id": "sprint_002"},
            ),
            Action(
                name="update_task_priority",
                kwargs={
                    "task_id": "task_011",
                    "new_priority": "medium",
                },
            ),
            Action(
                name="create_task",
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
                name="create_task_dependency",
                kwargs={"task_id": "task_019", "depends_on_task_id": "task_006"},
            ),
            Action(
                name="log_time_on_task",
                kwargs={
                    "task_id": "task_006",
                    "hours_logged": 4,
                    "employee_id": "emp_dev_07",
                    "notes": "Initial performance profiling completed",
                },
            ),
            Action(
                name="reassign_task",
                kwargs={
                    "task_id": "task_019",
                    "new_assignee_id": "emp_devops_04",
                },
            ),
            Action(
                name="check_time_logging_compliance", kwargs={"sprint_id": "sprint_002"}
            ),
            Action(
                name="log_time_on_task",
                kwargs={
                    "task_id": "task_004",
                    "hours_logged": 3,
                    "employee_id": "emp_dev_20",
                    "notes": "Sprint compliance update",
                },
            ),
            Action(
                name="calculate_team_capacity",
                kwargs={"team_id": "team_dev_01", "sprint_id": "sprint_002"},
            ),
        ],
        outputs=['"team_utilization": 26.2', '"non_compliant_count": 3'],
    ),
    Task(
        annotator="0",
        user_id="enforce_time_tracking",
        instruction="""You are the PMO lead. Check time logging compliance for
        sprint_002. For all non-compliant tasks, examine their details and take
        appropriate action: log 4 hours of time for every task to the respective
        assignees, and output the number of active story points assigned to employee
        emp_dev_21 along with the total number of non-compliant tasks found.""",
        actions=[
            Action(
                name="check_time_logging_compliance", kwargs={"sprint_id": "sprint_002"}
            ),
            Action(
                name="log_time_on_task",
                kwargs={
                    "task_id": "task_003",
                    "hours_logged": 4,
                    "employee_id": "emp_dev_21",
                },
            ),
            Action(
                name="log_time_on_task",
                kwargs={
                    "task_id": "task_012",
                    "hours_logged": 4,
                    "employee_id": "emp_sec_dev_02",
                },
            ),
            Action(
                name="log_time_on_task",
                kwargs={
                    "task_id": "task_008",
                    "hours_logged": 4,
                    "employee_id": "emp_test_05",
                },
            ),
            Action(
                name="log_time_on_task",
                kwargs={
                    "task_id": "task_019",
                    "hours_logged": 4,
                    "employee_id": "emp_devops_02",
                },
            ),
            Action(
                name="get_employee_workload",
                kwargs={"employee_id": "emp_dev_21", "sprint_id": "sprint_002"},
            ),
        ],
        outputs=['"non_compliant_count": 4', '"total_active_story_points": 8'],
    ),
    Task(
        annotator="0",
        user_id="resource_optimization_lead",
        instruction="""
        You are the resource optimization coordinator. Get team_dev_01's velocity for last 3 sprints. Move
        task_018 to sprint_003. Assign task_011 to sprint_003. Log 6 hours on task_003 with 'Finalizing the API
        implementation' as note and complete it. Clone task_016 as "Mobile optimization" for emp_dev_15. Output team_dev_01's
        average velocity.""",
        actions=[
            Action(
                name="get_team_velocity",
                kwargs={"team_id": "team_dev_01", "last_n_sprints": 3},
            ),
            Action(
                name="bulk_move_tasks_to_sprint",
                kwargs={
                    "task_ids": ["task_018"],
                    "target_sprint_id": "sprint_003",
                },
            ),
            Action(
                name="assign_task_to_sprint",
                kwargs={"task_id": "task_011", "sprint_id": "sprint_003"},
            ),
            Action(name="get_task_details", kwargs={"task_id": "task_003"}),
            Action(
                name="log_time_on_task",
                kwargs={
                    "task_id": "task_003",
                    "hours_logged": 6,
                    "employee_id": "emp_dev_21",
                    "notes": "Finalizing the API implementation",
                },
            ),
            Action(
                name="update_task_status",
                kwargs={"task_id": "task_003", "new_status": "done"},
            ),
            Action(
                name="clone_task",
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
        instruction="""You are the scrum master for the Web Development Team
        (team_dev_01). Create a new sprint for your team titled "Sprint 6 - Web
        Team" starting March 29th, 2024 and ending April 11th, 2024. Check team
        velocity from last sprints, calculate capacity, pull critical-priority tasks
        from backlog, resolve their dependencies with resolution "Emergency
        override", assign them to the sprint, and activate the sprint. Report
        the sprint's planned story points.""",
        actions=[
            Action(
                name="get_team_velocity",
                kwargs={"team_id": "team_dev_01", "last_n_sprints": 3},
            ),
            Action(name="calculate_team_capacity", kwargs={"team_id": "team_dev_01"}),
            Action(
                name="create_sprint",
                kwargs={
                    "sprint_id": "sprint_006",
                    "sprint_name": "Sprint 6 - Web Team",
                    "start_date": "2024-03-29",
                    "end_date": "2024-04-11",
                    "team_id": "team_dev_01",
                },
            ),
            Action(name="get_backlog_tasks", kwargs={"priority": "critical"}),
            Action(name="search_tasks", kwargs={"task_id": "task_014"}),
            Action(
                name="resolve_blocked_task",
                kwargs={
                    "task_id": "task_014",
                    "resolution": "Emergency override",
                    "unblock_dependencies": True,
                },
            ),
            Action(
                name="bulk_move_tasks_to_sprint",
                kwargs={
                    "task_ids": ["task_014"],
                    "target_sprint_id": "sprint_006",
                },
            ),
            Action(
                name="update_sprint_status",
                kwargs={"sprint_id": "sprint_006", "new_status": "active"},
            ),
            Action(name="get_sprint_details", kwargs={"sprint_id": "sprint_006"}),
        ],
        outputs=['"sprint_total_points": 13'],
    ),
    Task(
        annotator="0",
        user_id="manage_task_dependencies",
        instruction="""You are the tech lead. task_004 is blocked by task_003.
        Check task 003 status, if not done, verify the status of any
        dependencies, log time twice (8 hours and 6 hours respectively) to show
        progress on task_003, complete task_003, then unblock task_004 with the
        resolution 'Dependency satisfied'. Move task_004 to in_progress and tell
        me its new status.""",
        actions=[
            Action(name="search_tasks", kwargs={"task_id": "task_004"}),
            Action(name="search_tasks", kwargs={"task_id": "task_003"}),
            Action(name="get_task_details", kwargs={"task_id": "task_003"}),
            Action(name="get_task_history", kwargs={"task_id": "task_003"}),
            Action(name="search_tasks", kwargs={"task_id": "task_001"}),
            Action(name="search_tasks", kwargs={"task_id": "task_002"}),
            Action(
                name="log_time_on_task",
                kwargs={
                    "task_id": "task_003",
                    "hours_logged": 8,
                    "employee_id": "emp_dev_21",
                },
            ),
            Action(
                name="log_time_on_task",
                kwargs={
                    "task_id": "task_003",
                    "hours_logged": 6,
                    "employee_id": "emp_dev_21",
                },
            ),
            Action(
                name="update_task_status",
                kwargs={"task_id": "task_003", "new_status": "done"},
            ),
            Action(
                name="resolve_blocked_task",
                kwargs={
                    "task_id": "task_004",
                    "resolution": "Dependency satisfied",
                    "unblock_dependencies": True,
                },
            ),
            Action(
                name="update_task_status",
                kwargs={"task_id": "task_004", "new_status": "in_progress"},
            ),
            Action(name="search_tasks", kwargs={"task_id": "task_004"}),
        ],
        outputs=['"status": "in_progress"'],
    ),
    Task(
        annotator="0",
        user_id="emergency_security_incident_coordinator",
        instruction="""You are the Chief Security Officer handling a critical
        security breach. Use bulk move to transfer task_014 to
        sprint_002 (active). Clone task_005 as "Emergency security review -
        Finance" (task_071) for emp_sec_dev_02 and "Emergency security review -
        Banking" (task_072)
        for emp_sec_test_01. Resolve task_015 with resolution "Security
        emergency override - UI work deprioritized" using unblock dependencies.
        Move task_012 from sprint_002 to sprint_003. Create "Penetration test -
        Security Expert 1" (task_073) with description "Emergency penetration testing" for
        emp_sec_dev_01 with 4 critical story points in sprint_002. Create
        "Penetration test - Security Expert 2" (task_074) with description "Emergency
        penetration testing" for emp_sec_dev_02 with 4 critical story points in
        sprint_002. Output if the workflow was executed successfully.""",
        actions=[
            Action(
                name="bulk_move_tasks_to_sprint",
                kwargs={
                    "task_ids": ["task_014"],
                    "target_sprint_id": "sprint_002",
                },
            ),
            Action(
                name="clone_task",
                kwargs={
                    "source_task_id": "task_005",
                    "new_title": "Emergency security review - Finance",
                    "new_task_id": "task_071",
                    "new_assignee_id": "emp_sec_dev_02",
                },
            ),
            Action(
                name="clone_task",
                kwargs={
                    "source_task_id": "task_005",
                    "new_title": "Emergency security review - Banking",
                    "new_task_id": "task_072",
                    "new_assignee_id": "emp_sec_test_01",
                },
            ),
            Action(
                name="resolve_blocked_task",
                kwargs={
                    "task_id": "task_015",
                    "resolution": "Security emergency override - UI work deprioritized",
                    "unblock_dependencies": True,
                },
            ),
            Action(
                name="bulk_move_tasks_to_sprint",
                kwargs={"task_ids": ["task_012"], "target_sprint_id": "sprint_003"},
            ),
            Action(
                name="create_task",
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
                name="create_task",
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
        instruction="""You are the Resource Management Director. Calculate
        team_dev_01 capacity for sprint_002. Reassign task_004 from emp_dev_05
        to emp_test_05. Create "Resource Optimization Review" task with
        description "Review team resource allocation" with 4 story points for
        emp_dev_20 with high priority. Check time logging compliance for
        sprint_002. Log 4 hours on task_003 for emp_dev_21 with notes
        "Compliance update - resource optimization". Clone task_016 as "Load
        balancing implementation" for emp_dev_05 in sprint_002. Report the team utilization
        percentage and non-compliant task count.""",
        actions=[
            Action(
                name="calculate_team_capacity",
                kwargs={"team_id": "team_dev_01", "sprint_id": "sprint_002"},
            ),
            Action(
                name="reassign_task",
                kwargs={
                    "task_id": "task_004",
                    "new_assignee_id": "emp_test_05",
                },
            ),
            Action(
                name="create_task",
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
                name="check_time_logging_compliance", kwargs={"sprint_id": "sprint_002"}
            ),
            Action(
                name="log_time_on_task",
                kwargs={
                    "task_id": "task_003",
                    "hours_logged": 4,
                    "employee_id": "emp_dev_21",
                    "notes": "Compliance update - resource optimization",
                },
            ),
            Action(
                name="clone_task",
                kwargs={
                    "source_task_id": "task_016",
                    "new_title": "Load balancing implementation",
                    "new_assignee_id": "emp_dev_05",
                    "sprint_id": "sprint_002"
                },
            ),
            Action(
                name="calculate_team_capacity",
                kwargs={"team_id": "team_dev_01", "sprint_id": "sprint_002"},
            ),
            Action(
                name="check_time_logging_compliance", kwargs={"sprint_id": "sprint_002"}
            ),
        ],
        outputs=['"team_utilization": 37.5', '"non_compliant_count": 3'],
    ),
    Task(
        annotator="0",
        user_id="sprint_recovery_lead",
        instruction="""You are the sprint recovery specialist for team_dev_01.
        Escalate task_015 to emp_head_eng for sprint recovery. Update task_003
        to done with 8 hours logged by the assigned employee. Log 4 hours for
        task_004 (emp_dev_20) and task_012 (emp_sec_dev_02) for time compliance.
        Move task_004 to in_progress. Output the completion percentage.""",
        actions=[
            Action(
                name="check_blocked_tasks_for_escalation",
                kwargs={"sprint_id": "sprint_002"},
            ),
            Action(
                name="escalate_task",
                kwargs={
                    "task_id": "task_015",
                    "escalate_to": "emp_head_eng",
                },
            ),
            Action(name="get_task_details", kwargs={"task_id": "task_003"}),
            Action(
                name="log_time_on_task",
                kwargs={
                    "task_id": "task_003",
                    "hours_logged": 8,
                    "employee_id": "emp_dev_21",
                },
            ),
            Action(
                name="update_task_status",
                kwargs={"task_id": "task_003", "new_status": "done"},
            ),
            Action(
                name="log_time_on_task",
                kwargs={
                    "task_id": "task_004",
                    "hours_logged": 4,
                    "employee_id": "emp_dev_20",
                },
            ),
            Action(
                name="log_time_on_task",
                kwargs={
                    "task_id": "task_012",
                    "hours_logged": 4,
                    "employee_id": "emp_sec_dev_02",
                },
            ),
            Action(
                name="update_task_status",
                kwargs={"task_id": "task_004", "new_status": "in_progress"},
            ),
            Action(
                name="calculate_sprint_burndown", kwargs={"sprint_id": "sprint_002"}
            ),
        ],
        outputs=['"completion_percentage": 9.4'],
    ),
    Task(
        annotator="0",
        user_id="skills_gap_analyzer",
        instruction="""You are the resource planning specialist analyzing skill
        gaps. Create retrospective for
        sprint_002 with: What went well: "Data pipeline implementation was
        smooth", "Good knowledge transfer between team members", "Stakeholder
        communication was effective". What needs improvement: "Need better
        testing data for analytics", "Sprint planning took too long", "Some user
        stories were too vague". Action items: "Create test data generation
        scripts", "Time-box sprint planning to 2 hours", "Include acceptance
        criteria in all user stories". Update task_020 priority to high. Create
        task "ML skill development workshop" with description "Workshop to
        improve team's machine learning skills" with 4 story points for
        emp_data_02, medium priority. Create dependency where task_011 depends
        on task_008, make sure to block task_011. Clone task_006 as "Advanced performance optimization" for
        emp_dev_08. Get emp_data_01 workload for sprint_002. Output emp_data_01's final workload rating,
        and whether retrospective was successfully created.""",
        actions=[
            Action(
                name="create_sprint_retrospective",
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
                name="update_task_priority",
                kwargs={
                    "task_id": "task_020",
                    "new_priority": "high",
                },
            ),
            Action(
                name="create_task",
                kwargs={
                    "title": "ML skill development workshop",
                    "description": "Workshop to improve team's machine learning skills",
                    "assignee_id": "emp_data_02",
                    "priority": "medium",
                    "story_points": 4,
                },
            ),
            Action(
                name="create_task_dependency",
                kwargs={"task_id": "task_011", "depends_on_task_id": "task_008", "block_task": True},
            ),
            Action(
                name="clone_task",
                kwargs={
                    "source_task_id": "task_006",
                    "new_title": "Advanced performance optimization",
                    "new_assignee_id": "emp_dev_08",
                },
            ),
            Action(
                name="get_employee_workload",
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
        instruction="""You are the Agile Coach automating sprint closure for
        team_dev_01. Check time logging compliance for sprint_005. Log 10
        hours on task_013 for emp_dev_08 and 8 hours on task_017 for
        emp_devops_04 with notes "Sprint closure compliance". Update task_006 priority to critical. Get team
        velocity for team_dev_01 over last 2 sprints. Update task_011
        priority to critical. Create dependency where task_008 depends on
        task_012. Update task_003 status to done. Update sprint_005 status to
        completed. Create retrospective with what_went_well: "Data pipeline
        implementation was smooth", "Good knowledge transfer between team
        members", "Stakeholder communication was effective";
        what_needs_improvement: "Need better testing data for analytics",
        "Sprint planning took too long", "Some user stories were too vague";
        action_items: "Create test data generation scripts", "Time-box sprint
        planning to 2 hours", "Include acceptance criteria in all user stories".
        Reassign task_006 and task_11 to emp_analyst_03. Output average velocity for team_dev_01""",
        actions=[
            Action(
                name="check_time_logging_compliance", kwargs={"sprint_id": "sprint_005"}
            ),
            Action(
                name="log_time_on_task",
                kwargs={
                    "task_id": "task_013",
                    "hours_logged": 10,
                    "employee_id": "emp_dev_08",
                    "notes": "Sprint closure compliance",
                },
            ),
            Action(
                name="log_time_on_task",
                kwargs={
                    "task_id": "task_017",
                    "hours_logged": 8,
                    "employee_id": "emp_devops_04",
                    "notes": "Sprint closure compliance",
                },
            ),
            Action(
                name="update_task_priority",
                kwargs={
                    "task_id": "task_006",
                    "new_priority": "critical",
                },
            ),
            Action(
                name="update_task_priority",
                kwargs={
                    "task_id": "task_011",
                    "new_priority": "critical",
                },
            ),
            Action(
                name="create_task_dependency",
                kwargs={"task_id": "task_008", "depends_on_task_id": "task_012"},
            ),
            Action(
                name="update_task_status",
                kwargs={"task_id": "task_003", "new_status": "done"},
            ),
            Action(
                name="update_sprint_status",
                kwargs={"sprint_id": "sprint_005", "new_status": "completed"},
            ),
            Action(
                name="create_sprint_retrospective",
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
                name="reassign_task",
                kwargs={
                    "task_id": "task_006",
                    "new_assignee_id": "emp_analyst_03",
                },
            ),
            Action(
                name="reassign_task",
                kwargs={
                    "task_id": "task_011",
                    "new_assignee_id": "emp_analyst_03",
                },
            ),
            Action(
                name="get_team_velocity",
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
        instruction="""You are the agile coach facilitating retrospective for
        sprint_001. Get team_analytics_01 velocity trend for last 3 sprints. Get task_002 history.
        Clone task_002 as task_026 ("Database schema v2 design") for
        emp_arch_01. Create dependency where cloned task depends on task_014.
        Create sprint (sprint_006) "Analytics Sprint 2" from 2024-04-15 to
        2024-04-28 for team_analytics_01 with goal "Implement data pipeline v2
        with lessons learned". Move cloned task and task_014 to new sprint.
        Calculate team capacity for new sprint. Report velocity trend, task_002
        history count, and new sprint capacity points.""",
        actions=[
            Action(
                name="get_team_velocity",
                kwargs={"team_id": "team_analytics_01", "last_n_sprints": 3},
            ),
            Action(name="get_task_history", kwargs={"task_id": "task_002"}),
            Action(
                name="clone_task",
                kwargs={
                    "source_task_id": "task_002",
                    "new_task_id": "task_026",
                    "new_title": "Database schema v2 design",
                    "new_assignee_id": "emp_arch_01",
                },
            ),
            Action(
                name="create_task_dependency",
                kwargs={"task_id": "task_026", "depends_on_task_id": "task_014"},
            ),
            Action(
                name="create_sprint",
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
                name="bulk_move_tasks_to_sprint",
                kwargs={
                    "task_ids": ["task_026", "task_014"],
                    "target_sprint_id": "sprint_006",
                },
            ),
            Action(
                name="calculate_team_capacity",
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
        instruction="""You are the Skills Development Coordinator. Assign
        task_014 to sprint_002. Create task "ML knowledge transfer session" with
        description "Transfer ML expertise for data migration project" with 3
        story points for emp_data_02 with medium priority. Update task_006
        priority to critical. Create dependency where task_014 depends on
        task_002. Log 2 hours on task_014 for emp_data_01 with notes "ML
        algorithm research and planning". Check time logging compliance for
        sprint_002. Create task "Time tracking training session" with
        description "Train team on proper time tracking procedures" with 2 story
        points for emp_pm_04 with high priority. Get final workload for
        emp_data_01 in sprint_002 and report their workload rating and the total
        active story points.""",
        actions=[
            Action(
                name="assign_task_to_sprint",
                kwargs={"task_id": "task_014", "sprint_id": "sprint_002"},
            ),
            Action(
                name="create_task",
                kwargs={
                    "title": "ML knowledge transfer session",
                    "description": "Transfer ML expertise for data migration project",
                    "assignee_id": "emp_data_02",
                    "priority": "medium",
                    "story_points": 3,
                },
            ),
            Action(
                name="update_task_priority",
                kwargs={
                    "task_id": "task_006",
                    "new_priority": "critical",
                },
            ),
            Action(
                name="create_task_dependency",
                kwargs={"task_id": "task_014", "depends_on_task_id": "task_002"},
            ),
            Action(
                name="log_time_on_task",
                kwargs={
                    "task_id": "task_014",
                    "hours_logged": 2,
                    "employee_id": "emp_data_01",
                    "notes": "ML algorithm research and planning",
                },
            ),
            Action(
                name="check_time_logging_compliance", kwargs={"sprint_id": "sprint_002"}
            ),
            Action(
                name="create_task",
                kwargs={
                    "title": "Time tracking training session",
                    "description": "Train team on proper time tracking procedures",
                    "assignee_id": "emp_pm_04",
                    "priority": "high",
                    "story_points": 2,
                },
            ),
            Action(
                name="get_employee_workload",
                kwargs={"employee_id": "emp_data_01", "sprint_id": "sprint_002"},
            ),
        ],
        outputs=['"workload_rating": "normal"', '"total_active_story_points": 13'],
    ),
    Task(
        annotator="0",
        user_id="resource_conflict_resolver",
        instruction="""You are the Resource Allocation Director handling a
        critical skill shortage crisis. Create a critical task (task_022) "ML model
        optimization - Phase 1" with description "Optimize machine learning
        models for AI platform" with 8 story points for emp_data_01. Reassign
        task_014 to emp_data_02. Update task_014 priority to medium. Get
        team_analytics_01 velocity for last 3 sprints. Clone task_006 as task_023 ("AI data analysis
        pipeline") for emp_data_01. Log 4 hours on the ML optimization task with
        notes "Initial ML architecture design and planning". Create task
        (task_029) "Cross-team ML knowledge transfer" with description "Facilitate ML
        knowledge sharing across teams" with 3 story points for emp_pm_04
        priority high. Escalate task_005 to emp_head_eng. Get final workload for
        emp_data_01. Tell me the workload rating and the average velocity.""",
        actions=[
            Action(
                name="create_task",
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
                name="reassign_task",
                kwargs={
                    "task_id": "task_014",
                    "new_assignee_id": "emp_data_02",
                },
            ),
            Action(
                name="update_task_priority",
                kwargs={
                    "task_id": "task_014",
                    "new_priority": "medium",
                },
            ),
            Action(
                name="get_team_velocity",
                kwargs={"team_id": "team_analytics_01", "last_n_sprints": 3},
            ),
            Action(
                name="clone_task",
                kwargs={
                    "source_task_id": "task_006",
                    "new_task_id": "task_023",
                    "new_title": "AI data analysis pipeline",
                    "new_assignee_id": "emp_data_01",
                },
            ),
            Action(
                name="search_tasks",
                kwargs={"assignee_id": "emp_data_01", "priority": "critical"},
            ),
            Action(
                name="log_time_on_task",
                kwargs={
                    "task_id": "task_022",
                    "hours_logged": 4,
                    "employee_id": "emp_data_01",
                    "notes": "Initial ML architecture design and planning",
                },
            ),
            Action(
                name="create_task",
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
                name="escalate_task",
                kwargs={
                    "task_id": "task_005",
                    "escalate_to": "emp_head_eng",
                },
            ),
            Action(name="get_employee_workload", kwargs={"employee_id": "emp_data_01"}),
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
        instruction="""You are the Priority Rebalancing Specialist tasked with
        optimizing work distribution across priority levels. Your employee ID is
        emp_pmo_director. Check emp_sec_dev_01's workload to get their priority
        breakdown. If their critical priority points exceed 10, get their
        critical tasks in sprint_002. Check emp_dev_07 and emp_dev_08's
        workloads for priority breakdowns. If task_011 is assigned to someone
        with more than 3 low priority points, reassign it to emp_sec_test_01.
        Update task_011's priority to high. Check emp_qa_02's workload priority
        breakdown. If their medium priority points are less than 5, reassign
        task_010 to emp_qa_02. Create a new task "Priority distribution
        analysis" with description "Analyze and optimize team priority
        distribution" with 4 story points for emp_pm_04 with critical priority.
        Check blocked tasks for escalation in sprint_002. If any tasks have been
        blocked for "365+" days, escalate the first one to emp_cto. Log 3 hours
        on task_005 for emp_sec_dev_01 with notes "Security framework
        implementation". Calculate team capacity for team_security_01. Output
        the critical priority points from emp_sec_dev_01's priority_breakdown.""",
        actions=[
            Action(
                name="get_employee_workload",
                kwargs={"employee_id": "emp_sec_dev_01", "sprint_id": "sprint_002"},
            ),
            Action(
                name="search_tasks",
                kwargs={
                    "assignee_id": "emp_sec_dev_01",
                    "priority": "critical",
                    "sprint_id": "sprint_002",
                },
            ),
            Action(name="get_employee_workload", kwargs={"employee_id": "emp_dev_07"}),
            Action(name="get_employee_workload", kwargs={"employee_id": "emp_dev_08"}),
            Action(name="search_tasks", kwargs={"task_id": "task_011"}),
            Action(name="get_employee_workload", kwargs={"employee_id": "emp_qa_02"}),
            Action(
                name="reassign_task",
                kwargs={
                    "task_id": "task_011",
                    "new_assignee_id": "emp_sec_test_01",
                },
            ),
            Action(
                name="update_task_priority",
                kwargs={
                    "task_id": "task_011",
                    "new_priority": "high",
                },
            ),
            Action(name="get_employee_workload", kwargs={"employee_id": "emp_qa_02"}),
            Action(
                name="reassign_task",
                kwargs={
                    "task_id": "task_010",
                    "new_assignee_id": "emp_qa_02",
                },
            ),
            Action(
                name="create_task",
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
                name="check_blocked_tasks_for_escalation",
                kwargs={"sprint_id": "sprint_002"},
            ),
            Action(
                name="escalate_task",
                kwargs={
                    "task_id": "task_015",
                    "escalate_to": "emp_cto",
                },
            ),
            Action(
                name="log_time_on_task",
                kwargs={
                    "task_id": "task_005",
                    "hours_logged": 3,
                    "employee_id": "emp_sec_dev_01",
                    "notes": "Security framework implementation",
                },
            ),
            Action(
                name="calculate_team_capacity",
                kwargs={"team_id": "team_security_01", "sprint_id": "sprint_002"},
            ),
            Action(name="generate_sprint_report", kwargs={"sprint_id": "sprint_002"}),
            Action(
                name="get_employee_workload",
                kwargs={"employee_id": "emp_sec_dev_01", "sprint_id": "sprint_002"},
            ),
        ],
        outputs=['"critical": 13'],
    ),
    Task(
        annotator="0",
        user_id="predictive_blocker_prevention",
        instruction="""You are the process improvement specialist analyzing
        historical patterns. Get task history for task_005. Check blocked tasks
        needing escalation across all sprints. Get details for task_015 and
        create "Procurement process automation" task_030 with description "Automate
        procurement to prevent blocking" with 5 story points for emp_pm_04,
        critical priority. Create a dependency where task_019 depends on
        task_009 (set block task as true). Log 3 hours on task_009 with notes "Adding automated
        compliance checks". Get backlog tasks with max 5 story points. Clone
        task_016 as task_027 ("Security checklist automation") for emp_sec_test_01. Update
        its priority to high. Check time logging compliance for sprint_002. Bulk
        move tasks ["task_006", "task_011", "task_016"] to sprint_003. Get
        task_017 history. Create "Backup verification automation" task (task_028) with
        description "Automated backup verification" with 4 story points for
        emp_devops_04, high priority. Make task_019 depend on the new task.
        Calculate sprint_002 burndown. Report task_005 history count, bulk move
        success count, and completion percentage.""",
        actions=[
            Action(name="get_task_history", kwargs={"task_id": "task_005"}),
            Action(
                name="check_blocked_tasks_for_escalation",
                kwargs={"check_all_sprints": True},
            ),
            Action(name="get_task_details", kwargs={"task_id": "task_015"}),
            Action(
                name="create_task",
                kwargs={
                    "title": "Procurement process automation",
                    "new_task_id": "task_030",
                    "description": "Automate procurement to prevent blocking",
                    "assignee_id": "emp_pm_04",
                    "priority": "critical",
                    "story_points": 5,
                },
            ),
            Action(name="generate_sprint_report", kwargs={"sprint_id": "sprint_002"}),
            Action(
                name="create_task_dependency",
                kwargs={"task_id": "task_019", "depends_on_task_id": "task_009", "block_task": True},
            ),
            Action(
                name="log_time_on_task",
                kwargs={
                    "task_id": "task_009",
                    "hours_logged": 3,
                    "employee_id": "emp_devops_02",
                    "notes": "Adding automated compliance checks",
                },
            ),
            Action(name="get_backlog_tasks", kwargs={"max_story_points": 5}),
            Action(
                name="clone_task",
                kwargs={
                    "source_task_id": "task_016",
                    "new_task_id": "task_027",
                    "new_title": "Security checklist automation",
                    "new_assignee_id": "emp_sec_test_01",
                },
            ),
            Action(
                name="update_task_priority",
                kwargs={
                    "task_id": "task_027",
                    "new_priority": "high",
                },
            ),
            Action(
                name="check_time_logging_compliance", kwargs={"sprint_id": "sprint_002"}
            ),
            Action(
                name="bulk_move_tasks_to_sprint",
                kwargs={
                    "task_ids": ["task_006", "task_011", "task_016"],
                    "target_sprint_id": "sprint_003",
                },
            ),
            Action(name="get_task_history", kwargs={"task_id": "task_017"}),
            Action(
                name="create_task",
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
                name="create_task_dependency",
                kwargs={"task_id": "task_019", "depends_on_task_id": "task_028"},
            ),
            Action(
                name="calculate_sprint_burndown", kwargs={"sprint_id": "sprint_002"}
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
        instruction="""You are the Agile transformation lead analyzing
        team_dev_01's velocity decline. Get team velocity for the last
        sprint. Clone task_012 as task_034 ("User permissions system -
        Simplified") for emp_sec_dev_02. Bulk move task_004 to
        sprint_003. Escalate task_015 to emp_head_eng. Create task_032 "Velocity
        improvement workshop" with description "Workshop to address velocity
        decline" with 3 story points for emp_pm_03, high priority. Clone
        task_009 as task_030 ("Automated velocity tracking dashboard") for emp_devops_02.
        Create dependency where the cloned task depends on task_019. Resolve
        task_015 with resolution "Framework decision made - React selected".
        Report the velocity trend, number of tasks moved to next sprint, and
        whether a blocked task was resolved.""",
        actions=[
            Action(
                name="get_team_velocity",
                kwargs={"team_id": "team_dev_01", "last_n_sprints": 1},
            ),
            Action(
                name="clone_task",
                kwargs={
                    "source_task_id": "task_012",
                    "new_task_id": "task_034",
                    "new_title": "User permissions system - Simplified",
                    "new_assignee_id": "emp_sec_dev_02",
                },
            ),
            Action(
                name="bulk_move_tasks_to_sprint",
                kwargs={
                    "task_ids": ["task_004"],
                    "target_sprint_id": "sprint_003",
                },
            ),
            Action(
                name="escalate_task",
                kwargs={
                    "task_id": "task_015",
                    "escalate_to": "emp_head_eng",
                },
            ),
            Action(
                name="create_task",
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
                name="clone_task",
                kwargs={
                    "source_task_id": "task_009",
                    "new_task_id": "task_030",
                    "new_title": "Automated velocity tracking dashboard",
                    "new_assignee_id": "emp_devops_02",
                },
            ),
            Action(
                name="create_task_dependency",
                kwargs={"task_id": "task_030", "depends_on_task_id": "task_019"},
            ),
            Action(
                name="resolve_blocked_task",
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
        instruction="""
        You are the Performance Analytics Lead investigating declining team
        productivity. Your employee ID is emp_head_analytics. Find the assignee
        with the lowest completed_points to total_points ratio in the sprint
        'sprint_001'. Get that employee's current workload across all tasks. If
        their total_active_story_points is less than 10, reassign task_020 to
        them. Get team velocity (last 3 sprints) for team_analytics_01 to check
        individual_velocities trend. Create a critical task "Velocity
        improvement workshop" with description "Workshop to address declining
        team velocity" with 5 story points for emp_pm_03. Search for all tasks
        assigned to emp_analyst_03. If they have fewer than 2 tasks, clone
        task_011 as "Performance benchmarking suite" for emp_analyst_03. Check
        task_009 history to see how many times it was modified. Create a dependency where task_019 depends on task_017.
        Log 4 hours on task_013 for emp_dev_08 with notes "Email service
        optimization completed". Update task_006 priority to critical. If any
        risks in sprint_002 include "High number of blocked tasks", resolve
        task_015 with resolution "Emergency allocation of QA resources" using
        unblock_dependencies=true. Report the lowest completed points value from
        team performance and the first velocity value from the individual
        velocities.
        """,
        actions=[
            Action(name="generate_sprint_report", kwargs={"sprint_id": "sprint_001"}),
            Action(name="get_employee_workload", kwargs={"employee_id": "emp_dev_07"}),
            Action(
                name="reassign_task",
                kwargs={
                    "task_id": "task_020",
                    "new_assignee_id": "emp_dev_07",
                },
            ),
            Action(
                name="get_team_velocity",
                kwargs={"team_id": "team_analytics_01", "last_n_sprints": 3},
            ),
            Action(
                name="create_task",
                kwargs={
                    "title": "Velocity improvement workshop",
                    "description": "Workshop to address declining team velocity",
                    "assignee_id": "emp_pm_03",
                    "priority": "critical",
                    "story_points": 5,
                },
            ),
            Action(name="search_tasks", kwargs={"assignee_id": "emp_analyst_03"}),
            Action(
                name="clone_task",
                kwargs={
                    "source_task_id": "task_011",
                    "new_title": "Performance benchmarking suite",
                    "new_assignee_id": "emp_analyst_03",
                },
            ),
            Action(name="get_task_history", kwargs={"task_id": "task_009"}),
            Action(
                name="create_task_dependency",
                kwargs={"task_id": "task_019", "depends_on_task_id": "task_017"},
            ),
            Action(
                name="log_time_on_task",
                kwargs={
                    "task_id": "task_013",
                    "hours_logged": 4,
                    "employee_id": "emp_dev_08",
                    "notes": "Email service optimization completed",
                },
            ),
            Action(
                name="update_task_priority",
                kwargs={
                    "task_id": "task_006",
                    "new_priority": "critical",
                },
            ),
            Action(name="generate_sprint_report", kwargs={"sprint_id": "sprint_002"}),
            Action(
                name="resolve_blocked_task",
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
        instruction="""You are the continuous improvement manager implementing
        sprint_001's retrospective action items. Get task_013 history. Clone it
        as "Email service v2 - Modular design" for emp_dev_08. Get
        team_analytics_01 velocity for 2 sprints. Create "Retrospective action
        items tracker" with description "Track and measure impact of
        retrospective action items" with 4 story points for emp_analyst_02, high
        priority. Check time logging compliance for all tasks. Log 2 hours on
        task_006 by emp_dev_07 with notes "Retrospective compliance improvement". Log 2 hours
        on task_011 by emp_qa_02 with notes "Retrospective compliance improvement". Update
        task_006 to high priority. Create dependency where task_019 depends on
        task_006. Get medium priority backlog tasks. Clone task_010 as
        "Automated retrospective insights" for emp_pm_04. Calculate team_qa_01
        capacity. Create "QA capacity expansion planning" with description "Plan
        QA team expansion based on retrospective feedback" with 6 story points
        for emp_qa_02, critical priority. Move task_014 to sprint_002. Reassign
        task_006 to emp_analyst_03. Tell me the velocity, moved count, and
        success status.""",
        actions=[
            Action(name="get_task_history", kwargs={"task_id": "task_013"}),
            Action(
                name="clone_task",
                kwargs={
                    "source_task_id": "task_013",
                    "new_title": "Email service v2 - Modular design",
                    "new_assignee_id": "emp_dev_08",
                },
            ),
            Action(
                name="get_team_velocity",
                kwargs={"team_id": "team_analytics_01", "last_n_sprints": 2},
            ),
            Action(
                name="create_task",
                kwargs={
                    "title": "Retrospective action items tracker",
                    "description": "Track and measure impact of retrospective action items",
                    "assignee_id": "emp_analyst_02",
                    "priority": "high",
                    "story_points": 4,
                },
            ),
            Action(name="check_time_logging_compliance", kwargs={"check_all": True}),
            Action(
                name="log_time_on_task",
                kwargs={
                    "task_id": "task_006",
                    "hours_logged": 2,
                    "employee_id": "emp_dev_07",
                    "notes": "Retrospective compliance improvement",
                },
            ),
            Action(
                name="log_time_on_task",
                kwargs={
                    "task_id": "task_011",
                    "hours_logged": 2,
                    "employee_id": "emp_qa_02",
                    "notes": "Retrospective compliance improvement",
                },
            ),
            Action(
                name="update_task_priority",
                kwargs={
                    "task_id": "task_006",
                    "new_priority": "high",
                },
            ),
            Action(
                name="create_task_dependency",
                kwargs={"task_id": "task_019", "depends_on_task_id": "task_006"},
            ),
            Action(name="get_backlog_tasks", kwargs={"priority": "medium"}),
            Action(
                name="clone_task",
                kwargs={
                    "source_task_id": "task_010",
                    "new_title": "Automated retrospective insights",
                    "new_assignee_id": "emp_pm_04",
                },
            ),
            Action(name="calculate_team_capacity", kwargs={"team_id": "team_qa_01"}),
            Action(
                name="create_task",
                kwargs={
                    "title": "QA capacity expansion planning",
                    "description": "Plan QA team expansion based on retrospective feedback",
                    "assignee_id": "emp_qa_02",
                    "priority": "critical",
                    "story_points": 6,
                },
            ),
            Action(
                name="bulk_move_tasks_to_sprint",
                kwargs={
                    "task_ids": ["task_014"],
                    "target_sprint_id": "sprint_002",
                },
            ),
            Action(
                name="reassign_task",
                kwargs={
                    "task_id": "task_006",
                    "new_assignee_id": "emp_analyst_03",
                },
            ),
            Action(name="generate_sprint_report", kwargs={"sprint_id": "sprint_001"}),
        ],
        outputs=['"velocity": 28', '"moved_count": 1', '"success": true'],
    ),
    Task(
        annotator="0",
        user_id="capacity_rebalancer",
        instruction="""You are the resource optimization director. Calculate
        capacity for team_qa_01 and sprint_002. Update task_008 priority to critical. Log 6
        hours on task_008 for emp_test_05 with notes "Accelerating test
        coverage to unblock dependencies". Check blocked tasks for escalation in
        sprint_002. Create "Dependency resolution war room" task_041 with
        description "Coordinate resolution of dependency blockers" with 4 story
        points for emp_pm_03 with critical priority. Clone task_002 as task_042
        ("Dependency mapping documentation") for emp_arch_01 in sprint_002. Reassign task_008 to
        emp_sec_test_01. Get sprint_002 details. Bulk move task_020 and task_011
        to sprint_003. Resolve task_015 with resolution "Capacity freed up
        through rebalancing" (set unblock dependencies as false). Log 2 hours on task_010 for emp_dev_21 with notes
        "Documentation time allocation". Tell me the QA team utilization, number
        of tasks needing escalation, and sprint planned story points.""",
        actions=[
            Action(
                name="calculate_team_capacity",
                kwargs={"team_id": "team_qa_01", "sprint_id": "sprint_002"},
            ),
            Action(
                name="update_task_priority",
                kwargs={
                    "task_id": "task_008",
                    "new_priority": "critical",
                },
            ),
            Action(
                name="log_time_on_task",
                kwargs={
                    "task_id": "task_008",
                    "hours_logged": 6,
                    "employee_id": "emp_test_05",
                    "notes": "Accelerating test coverage to unblock dependencies",
                },
            ),
            Action(
                name="check_blocked_tasks_for_escalation",
                kwargs={"sprint_id": "sprint_002"},
            ),
            Action(
                name="create_task",
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
                name="clone_task",
                kwargs={
                    "source_task_id": "task_002",
                    "new_task_id": "task_042",
                    "new_title": "Dependency mapping documentation",
                    "sprint_id": "sprint_002",
                    "new_assignee_id": "emp_arch_01",
                },
            ),
            Action(
                name="reassign_task",
                kwargs={
                    "task_id": "task_008",
                    "new_assignee_id": "emp_sec_test_01",
                },
            ),
            Action(name="get_sprint_details", kwargs={"sprint_id": "sprint_002"}),
            Action(
                name="bulk_move_tasks_to_sprint",
                kwargs={
                    "task_ids": ["task_020", "task_011"],
                    "target_sprint_id": "sprint_003",
                },
            ),
            Action(
                name="search_tasks",
                kwargs={"task_id": "task_015"}
            ),
            Action(
                name="update_task_status",
                kwargs={"task_id": "task_004", "new_status": "done"},
            ),
            Action(
                name="update_task_status",
                kwargs={"task_id": "task_012", "new_status": "done"},
            ),
            Action(
                name="resolve_blocked_task",
                kwargs={
                    "task_id": "task_015",
                    "resolution": "Capacity freed up through rebalancing",
                    "unblock_dependencies": False,
                },
            ),
            Action(
                name="log_time_on_task",
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
        instruction="""You are the PMO process analyst studying escalation
        patterns. Get details for task_005. Create task "Security license
        procurement checklist" with description "Prevent license blockers" with
        3 story points for emp_pm_04 with high priority. Check blocked tasks for
        escalation across all sprints. Get details for task_015. Create
        "Fast-track approval process" with description "Streamline approvals"
        with 5 story points for emp_pm_03 with critical priority. Get details
        for task_001, task_005, and task_014. Clone task_001 as "Escalation
        prevention playbook" for emp_pm_04. Get workload for emp_pm_03 and
        emp_pm_04. Create "Monthly escalation review meeting" with description
        "Review escalations" with 2 story points and medium priority for
        emp_pm_03. Resolve task_015 with resolution "Escalation analysis
        triggered expedited resolution". Check time logging compliance for
        sprint_002. Create medium-priority "Automated time tracking reminders"
        task with description "Time logging reminders" with 2 story points for
        emp_devops_02. Create a sprint report for sprint_002 and output the total tasks""",
        actions=[
            Action(name="get_task_details", kwargs={"task_id": "task_005"}),
            Action(
                name="create_task",
                kwargs={
                    "title": "Security license procurement checklist",
                    "description": "Prevent license blockers",
                    "assignee_id": "emp_pm_04",
                    "priority": "high",
                    "story_points": 3,
                },
            ),
            Action(
                name="check_blocked_tasks_for_escalation",
                kwargs={"check_all_sprints": True},
            ),
            Action(name="get_task_details", kwargs={"task_id": "task_015"}),
            Action(
                name="create_task",
                kwargs={
                    "title": "Fast-track approval process",
                    "description": "Streamline approvals",
                    "assignee_id": "emp_pm_03",
                    "priority": "critical",
                    "story_points": 5,
                },
            ),
            Action(name="get_task_details", kwargs={"task_id": "task_001"}),
            Action(name="get_task_details", kwargs={"task_id": "task_005"}),
            Action(name="get_task_details", kwargs={"task_id": "task_014"}),
            Action(
                name="clone_task",
                kwargs={
                    "source_task_id": "task_001",
                    "new_title": "Escalation prevention playbook",
                    "new_assignee_id": "emp_pm_04",
                },
            ),
            Action(name="get_employee_workload", kwargs={"employee_id": "emp_pm_03"}),
            Action(name="get_employee_workload", kwargs={"employee_id": "emp_pm_04"}),
            Action(
                name="create_task",
                kwargs={
                    "title": "Monthly escalation review meeting",
                    "description": "Review escalations",
                    "assignee_id": "emp_pm_03",
                    "priority": "medium",
                    "story_points": 2,
                },
            ),
            Action(
                name="resolve_blocked_task",
                kwargs={
                    "task_id": "task_015",
                    "resolution": "Escalation analysis triggered expedited resolution",
                    "unblock_dependencies": True,
                },
            ),
            Action(
                name="check_time_logging_compliance", kwargs={"sprint_id": "sprint_002"}
            ),
            Action(
                name="create_task",
                kwargs={
                    "title": "Automated time tracking reminders",
                    "description": "Time logging reminders",
                    "assignee_id": "emp_devops_02",
                    "priority": "medium",
                    "story_points": 2,
                },
            ),
            Action(name="generate_sprint_report", kwargs={"sprint_id": "sprint_002"}),
        ],
        outputs=['"total_tasks": 8'],
    ),
    Task(
        annotator="0",
        user_id="estimation_accuracy_optimizer",
        instruction="""You are the estimation accuracy specialist analyzing time
        logging patterns. Get task details for task_001, task_002, and task_009.
        Update task_009 priority to high. Log 3 hours on task_009 for
        emp_devops_02 with notes "Retroactive compliance - minimum threshold".
        Clone task_003 as task_050 ("API endpoint for user profile - Pair
        Programming Session") for emp_dev_08. Get details for task_020 and
        task_008. Log 4 hours on task_008 for emp_test_05 with notes "Ensuring
        dependency has sufficient progress". Create "Story point calibration
        workshop" task_051 with description "Workshop to improve estimation
        accuracy based on historical data" with 3 story points for emp_pm_04
        with high priority. Get emp_dev_08 workload. Move tasks task_006 and
        task_011 to sprint_003. Reassign task_006 to emp_dev_08. Create
        retrospective for sprint_001 with what_went_well: ["Time tracking
        improved", "Story point accuracy increasing", "Bench resources utilized
        effectively"], what_needs_improvement: ["Setup tasks consistently
        underestimated", "Integration test dependencies unclear", "Need better
        estimation guidelines"], action_items: ["Implement 2x multiplier for
        setup tasks", "Create dependency visualization", "Run estimation
        workshop"]. Calculate team_dev_01 capacity for sprint_002. Tell me the
        time logged from task_001, hours logged for compliance, and
        retrospective success.""",
        actions=[
            Action(name="get_task_details", kwargs={"task_id": "task_001"}),
            Action(name="get_task_details", kwargs={"task_id": "task_002"}),
            Action(name="get_task_details", kwargs={"task_id": "task_009"}),
            Action(
                name="update_task_priority",
                kwargs={
                    "task_id": "task_009",
                    "new_priority": "high",
                },
            ),
            Action(
                name="log_time_on_task",
                kwargs={
                    "task_id": "task_009",
                    "hours_logged": 3,
                    "employee_id": "emp_devops_02",
                    "notes": "Retroactive compliance - minimum threshold",
                },
            ),
            Action(
                name="clone_task",
                kwargs={
                    "source_task_id": "task_003",
                    "new_task_id": "task_050",
                    "new_title": "API endpoint for user profile - Pair Programming Session",
                    "new_assignee_id": "emp_dev_08",
                },
            ),
            Action(name="get_task_details", kwargs={"task_id": "task_020"}),
            Action(name="get_task_details", kwargs={"task_id": "task_008"}),
            Action(
                name="log_time_on_task",
                kwargs={
                    "task_id": "task_008",
                    "hours_logged": 4,
                    "employee_id": "emp_test_05",
                    "notes": "Ensuring dependency has sufficient progress",
                },
            ),
            Action(
                name="create_task",
                kwargs={
                    "title": "Story point calibration workshop",
                    "new_task_id": "task_051",
                    "description": "Workshop to improve estimation accuracy based on historical data",
                    "assignee_id": "emp_pm_04",
                    "priority": "high",
                    "story_points": 3,
                },
            ),
            Action(name="get_employee_workload", kwargs={"employee_id": "emp_dev_08"}),
            Action(
                name="bulk_move_tasks_to_sprint",
                kwargs={
                    "task_ids": ["task_006", "task_011"],
                    "target_sprint_id": "sprint_003",
                },
            ),
            Action(
                name="reassign_task",
                kwargs={
                    "task_id": "task_006",
                    "new_assignee_id": "emp_dev_08",
                },
            ),
            Action(
                name="create_sprint_retrospective",
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
                name="calculate_team_capacity",
                kwargs={"team_id": "team_dev_01", "sprint_id": "sprint_002"},
            ),
        ],
        outputs=['"time_logged": 32', '"hours": 3', '"success": true'],
    ),
    Task(
        annotator="0",
        user_id="qa_process_coordinator",
        instruction="""You are the QA process coordinator. Update task_011
        priority to high for load testing urgency. Log 6 hours for task_003 for
        API finalization. Create coordination task "Load testing environment
        setup" with 4 story points for emp_qa_02, priority high. Reassign
        task_020 to emp_qa_02 for workload balancing. Clone task_020 as
        "Security integration tests" for emp_sec_test_01. Report emp_qa_02 final
        workload_rating and total_active_story_points.""",
        actions=[
            Action(
                name="update_task_priority",
                kwargs={
                    "task_id": "task_011",
                    "new_priority": "high",
                },
            ),
            Action(name="get_task_details", kwargs={"task_id": "task_003"}),
            Action(
                name="log_time_on_task",
                kwargs={
                    "task_id": "task_003",
                    "hours_logged": 6,
                    "employee_id": "emp_dev_21",
                    "notes": "API finalization",
                },
            ),
            Action(
                name="create_task",
                kwargs={
                    "title": "Load testing environment setup",
                    "assignee_id": "emp_qa_02",
                    "priority": "high",
                    "story_points": 4,
                },
            ),
            Action(
                name="reassign_task",
                kwargs={
                    "task_id": "task_020",
                    "new_assignee_id": "emp_qa_02",
                },
            ),
            Action(
                name="clone_task",
                kwargs={
                    "source_task_id": "task_020",
                    "new_title": "Security integration tests",
                    "new_assignee_id": "emp_sec_test_01",
                },
            ),
            Action(name="get_employee_workload", kwargs={"employee_id": "emp_qa_02"}),
        ],
        outputs=['"workload_rating": "normal"', '"total_active_story_points": 17'],
    ),
    Task(
        annotator="0",
        user_id="sprint_planning_coordinator",
        instruction="""You are the sprint planning coordinator for
        team_mobile_01. Get the team's velocity history for the last 3 sprints and calculate capacity
        for sprint_003. Assign task_007 and task_018 to sprint_003. Activate sprint_003 and output the
        sprint's total points, team capacity, and average velocity.""",
        actions=[
            Action(
                name="get_team_velocity",
                kwargs={"team_id": "team_mobile_01", "last_n_sprints": 3},
            ),
            Action(
                name="calculate_team_capacity", kwargs={"team_id": "team_mobile_01"}
            ),
            Action(
                name="bulk_move_tasks_to_sprint",
                kwargs={
                    "task_ids": ["task_007", "task_018"],
                    "target_sprint_id": "sprint_003",
                },
            ),
            Action(
                name="update_sprint_status",
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
        instruction="""You are the sprint optimization specialist for
        sprint_002. Reassign task_004 from emp_dev_20 to emp_dev_15 for load
        balancing. Create a "Sprint Recovery Plan" task (task_050) in sprint_002 with 3
        story points for emp_pm_04 with critical priority. Update task_016
        priority to critical. Reassign task_016 to emp_dev_08 and assign it to
        sprint_002. Log 2 hours on task_019 for monitoring sprint health. Update
        task_004's priority to critical. Output the completion percentage.""",
        actions=[
            Action(
                name="reassign_task",
                kwargs={
                    "task_id": "task_004",
                    "new_assignee_id": "emp_dev_15",
                },
            ),
            Action(
                name="create_task",
                kwargs={
                    "title": "Sprint Recovery Plan",
                    "new_task_id": "task_050",
                    "assignee_id": "emp_pm_04",
                    "priority": "critical",
                    "story_points": 3,
                    "sprint_id": "sprint_002",
                },
            ),
            Action(name="get_task_details", kwargs={"task_id": "task_016"}),
            Action(
                name="update_task_priority",
                kwargs={
                    "task_id": "task_016",
                    "new_priority": "critical",
                },
            ),
            Action(
                name="reassign_task",
                kwargs={
                    "task_id": "task_016",
                    "new_assignee_id": "emp_dev_08",
                },
            ),
            Action(
                name="assign_task_to_sprint",
                kwargs={"task_id": "task_016", "sprint_id": "sprint_002"},
            ),
            Action(name="get_task_details", kwargs={"task_id": "task_019"}),
            Action(
                name="log_time_on_task",
                kwargs={
                    "task_id": "task_019",
                    "hours_logged": 2,
                    "employee_id": "emp_devops_02",
                    "notes": "Monitoring sprint health",
                },
            ),
            Action(name="get_task_details", kwargs={"task_id": "task_004"}),
            Action(
                name="update_task_priority",
                kwargs={
                    "task_id": "task_004",
                    "new_priority": "critical",
                },
            ),
            Action(name="generate_sprint_report", kwargs={"sprint_id": "sprint_002"}),
        ],
        outputs=['"completion_percentage": 0.0'],
    ),
    Task(
        annotator="0",
        user_id="analytics_performance_manager",
        instruction="""You are the analytics team lead. Calculate
        team_analytics_01 velocity trends for the last sprint. Reassign
        task_010 to emp_analyst_03 to balance load. Create a knowledge sharing,
        medium-priority task "SQL optimization workshop" with 3 story points for emp_analyst_02.
        Check time compliance for sprint_001. Log 2 hours on task_006.
        Update task_011 priority to high for load testing needs. Output the team
        average velocity and total non-compliant tasks.""",
        actions=[
            Action(
                name="get_team_velocity",
                kwargs={"team_id": "team_analytics_01", "last_n_sprints": 1},
            ),
            Action(
                name="reassign_task",
                kwargs={
                    "task_id": "task_010",
                    "new_assignee_id": "emp_analyst_03",
                },
            ),
            Action(
                name="create_task",
                kwargs={
                    "title": "SQL optimization workshop",
                    "assignee_id": "emp_analyst_02",
                    "priority": "medium",
                    "story_points": 3,
                },
            ),
            Action(
                name="check_time_logging_compliance", kwargs={"sprint_id": "sprint_001"}
            ),
            Action(name="get_task_details", kwargs={"task_id": "task_006"}),
            Action(
                name="log_time_on_task",
                kwargs={
                    "task_id": "task_006",
                    "hours_logged": 2,
                    "employee_id": "emp_dev_07",
                },
            ),
            Action(
                name="update_task_priority",
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
        instruction="""You are the PMO risk manager responsible for identifying
        and mitigating sprint risks. Reassign task_010 to emp_analyst_03 for
        workload balancing. Create a "Workload Balancing Review" task in
        sprint_002 with 4 story points for emp_pm_04 with high priority. Check
        blocked tasks needing escalation in sprint_002. If there are blocked
        tasks, assign the first task to emp_head_eng. Update task_005's priority
        to critical for security audit critical path. Log 3 hours on task_012
        with 'RBAC implementation progress' as note and emp_sec_dev_02 as employee ID. Clone task_011 as "Performance Testing
        Suite" for emp_qa_02. Calculate final team capacity (use team_dev_01) and report the
        number of escalations created and final team utilization
        percentage.""",
        actions=[
            Action(
                name="reassign_task",
                kwargs={
                    "task_id": "task_010",
                    "new_assignee_id": "emp_analyst_03",
                },
            ),
            Action(
                name="create_task",
                kwargs={
                    "title": "Workload Balancing Review",
                    "assignee_id": "emp_pm_04",
                    "priority": "high",
                    "story_points": 4,
                    "sprint_id": "sprint_002",
                },
            ),
            Action(
                name="check_blocked_tasks_for_escalation",
                kwargs={"sprint_id": "sprint_002"},
            ),
            Action(
                name="escalate_task",
                kwargs={
                    "task_id": "task_015",
                    "escalate_to": "emp_head_eng",
                },
            ),
            Action(
                name="update_task_priority",
                kwargs={
                    "task_id": "task_005",
                    "new_priority": "critical",
                },
            ),
            Action(
                name="log_time_on_task",
                kwargs={
                    "task_id": "task_012",
                    "hours_logged": 3,
                    "employee_id": "emp_sec_dev_02",
                    "notes": "RBAC implementation progress",
                },
            ),
            Action(
                name="clone_task",
                kwargs={
                    "source_task_id": "task_011",
                    "new_title": "Performance Testing Suite",
                    "new_assignee_id": "emp_qa_02",
                },
            ),
            Action(
                name="calculate_team_capacity",
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
        instruction="""You are the resource optimization lead. Create an
        infrastructure task "Cloud migration planning" with 8 story points for
        emp_devops_04 as critical priority. Update task_014's priority to
        critical for data migration urgency and assign it to sprint_002. Check
        blocked tasks needing escalation in sprint_002. If any found, escalate
        the first one to emp_head_eng. Output the team utilization for
        team_devops_01 and blocked task count.""",
        actions=[
            Action(
                name="create_task",
                kwargs={
                    "title": "Cloud migration planning",
                    "assignee_id": "emp_devops_04",
                    "priority": "critical",
                    "story_points": 8,
                    "sprint_id": "sprint_002",
                },
            ),
            Action(name="search_tasks", kwargs={"task_id": "task_014"}),
            Action(
                name="update_task_priority",
                kwargs={
                    "task_id": "task_014",
                    "new_priority": "critical",
                },
            ),
            Action(
                name="assign_task_to_sprint",
                kwargs={"task_id": "task_014", "sprint_id": "sprint_002"},
            ),
            Action(
                name="check_blocked_tasks_for_escalation",
                kwargs={"sprint_id": "sprint_002"},
            ),
            Action(
                name="escalate_task",
                kwargs={
                    "task_id": "task_015",
                    "escalate_to": "emp_head_eng",
                },
            ),
            Action(
                name="calculate_sprint_burndown", kwargs={"sprint_id": "sprint_002"}
            ),
            Action(
                name="calculate_team_capacity",
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
        instruction="""You are the security incident response coordinator. A
        critical security vulnerability has been discovered in proj_banking_01.
        Create a critical task "Emergency security patch - Banking" with
        description "Critical vulnerability patching for banking integration"
        with 8 story points for emp_sec_dev_01 in sprint_002. Update task_011
        priority to critical. Resolve blocked task_005 with resolution
        "Emergency override for critical vulnerability". Log 4 hours on task_005
        with notes "Emergency security audit". Reassign task_012 to emp_dev_07.
        Create critical task "Penetration testing - Banking hotfix" with
        description "Security testing for banking patch" with 5 story points for
        emp_sec_test_01. Check blocked tasks needing escalation in sprint_002.
        Escalate task_015 to emp_head_eng. Create "Sprint Risk Mitigation"
        critical-priority task with description "Address sprint risks" with 3 story
        points for emp_pm_04. Output the completion percentage, total blocked
        tasks, and whether new escalations were created.""",
        actions=[
            Action(
                name="create_task",
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
                name="update_task_priority",
                kwargs={
                    "task_id": "task_011",
                    "new_priority": "critical",
                },
            ),
            Action(
                name="resolve_blocked_task",
                kwargs={
                    "task_id": "task_005",
                    "resolution": "Emergency override for critical vulnerability",
                    "unblock_dependencies": True,
                },
            ),
            Action(
                name="log_time_on_task",
                kwargs={
                    "task_id": "task_005",
                    "hours_logged": 4,
                    "employee_id": "emp_sec_dev_01",
                    "notes": "Emergency security audit",
                },
            ),
            Action(
                name="reassign_task",
                kwargs={
                    "task_id": "task_012",
                    "new_assignee_id": "emp_dev_07",
                },
            ),
            Action(
                name="create_task",
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
                name="check_blocked_tasks_for_escalation",
                kwargs={"sprint_id": "sprint_002"},
            ),
            Action(
                name="escalate_task",
                kwargs={
                    "task_id": "task_015",
                    "escalate_to": "emp_head_eng",
                },
            ),
            Action(
                name="create_task",
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
                name="calculate_sprint_burndown", kwargs={"sprint_id": "sprint_002"}
            ),
            Action(name="generate_sprint_report", kwargs={"sprint_id": "sprint_002"}),
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
        instruction="""You are the QA lead enforcing time logging. Check time
        logging compliance for sprint_002. Log 3 hours for task_004. Create a
        reminder task "Time logging compliance review" with 2 story points for
        emp_qa_02 and a normal priority. Check blocked tasks for escalation.
        Escalate task_015 to emp_head_qa if it needs escalation. Tell me the
        final compliance count and whether a new escalation was created.""",
        actions=[
            Action(
                name="check_time_logging_compliance", kwargs={"sprint_id": "sprint_002"}
            ),
            Action(name="search_tasks", kwargs={"task_id": "task_004"}),
            Action(
                name="log_time_on_task",
                kwargs={
                    "task_id": "task_004",
                    "hours_logged": 3,
                    "employee_id": "emp_dev_20",
                },
            ),
            Action(
                name="create_task",
                kwargs={
                    "title": "Time logging compliance review",
                    "assignee_id": "emp_qa_02",
                    "priority": "medium",
                    "story_points": 2,
                },
            ),
            Action(
                name="check_blocked_tasks_for_escalation",
                kwargs={"sprint_id": "sprint_002"},
            ),
            Action(
                name="escalate_task",
                kwargs={
                    "task_id": "task_015",
                    "escalate_to": "emp_head_qa",
                },
            ),
            Action(
                name="check_time_logging_compliance", kwargs={"sprint_id": "sprint_002"}
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
        instruction="""You are the scrum master for team_dev_01. Calculate the
        team's average velocity from the last 3 sprints, check sprint_002's
        burndown progress, identify any blocked tasks that haven't been
        escalated yet, escalate the first one found to emp_head_eng, and report
        the sprint completion percentage.""",
        actions=[
            Action(
                name="get_team_velocity",
                kwargs={"team_id": "team_dev_01", "last_n_sprints": 3},
            ),
            Action(
                name="calculate_sprint_burndown", kwargs={"sprint_id": "sprint_002"}
            ),
            Action(
                name="check_blocked_tasks_for_escalation",
                kwargs={"sprint_id": "sprint_002"},
            ),
            Action(
                name="escalate_task",
                kwargs={
                    "task_id": "task_015",
                    "escalate_to": "emp_head_eng",
                },
            ),
            Action(
                name="calculate_sprint_burndown", kwargs={"sprint_id": "sprint_002"}
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
        instruction="""You are the DevOps platform optimization lead. Create a
        critical task "Container orchestration optimization" with description
        "Optimize container orchestration" with 6 story points for
        emp_devops_04. Update task_006 priority to critical. Reassign task_006
        to emp_devops_04. Create dependency where task_019 depends on task_006.
        Log 5 hours on task_006 with notes "Performance bottleneck analysis
        completed". Update task_019 priority to high. Create task "Kubernetes
        cluster scaling automation" with description "Implement auto-scaling"
        with 8 story points for emp_devops_04, priority critical. Escalate
        task_005 to emp_head_eng. Calculate team_devops_01 capacity for
        sprint_002. Output the team utilization.""",
        actions=[
            Action(
                name="create_task",
                kwargs={
                    "title": "Container orchestration optimization",
                    "description": "Optimize container orchestration",
                    "assignee_id": "emp_devops_04",
                    "priority": "critical",
                    "story_points": 6,
                },
            ),
            Action(
                name="update_task_priority",
                kwargs={
                    "task_id": "task_006",
                    "new_priority": "critical",
                },
            ),
            Action(
                name="reassign_task",
                kwargs={
                    "task_id": "task_006",
                    "new_assignee_id": "emp_devops_04",
                },
            ),
            Action(
                name="create_task_dependency",
                kwargs={"task_id": "task_019", "depends_on_task_id": "task_006"},
            ),
            Action(
                name="log_time_on_task",
                kwargs={
                    "task_id": "task_006",
                    "hours_logged": 5,
                    "employee_id": "emp_devops_04",
                    "notes": "Performance bottleneck analysis completed",
                },
            ),
            Action(
                name="update_task_priority",
                kwargs={
                    "task_id": "task_019",
                    "new_priority": "high",
                },
            ),
            Action(
                name="create_task",
                kwargs={
                    "title": "Kubernetes cluster scaling automation",
                    "description": "Implement auto-scaling",
                    "assignee_id": "emp_devops_04",
                    "priority": "critical",
                    "story_points": 8,
                },
            ),
            Action(
                name="escalate_task",
                kwargs={
                    "task_id": "task_005",
                    "escalate_to": "emp_head_eng",
                },
            ),
            Action(
                name="calculate_team_capacity",
                kwargs={"team_id": "team_devops_01", "sprint_id": "sprint_002"},
            ),
        ],
        outputs=['"team_utilization": 7.5'],
    ),
    Task(
        annotator="0",
        user_id="resolve_sprint_blocks",
        instruction="""You are the project manager. Check Sprint 2 (sprint_002)
        for tasks that have been blocked for more than 2 days and need
        escalation. Note the tasks_needing_escalation count from this check.
        Escalate any tasks that aren't already escalated to emp_head_eng
        (Engineering department head), update priority to critical if needed,
        and reassign to emp_dev_20. For task_015, also resolve the blocking
        issue with resolution "Resolved by sprint lead" and move it to
        in_progress status. Tell me the number of tasks the need to be
        escalated.""",
        actions=[
            Action(
                name="check_blocked_tasks_for_escalation",
                kwargs={"sprint_id": "sprint_002"},
            ),
            Action(
                name="escalate_task",
                kwargs={"task_id": "task_015", "escalate_to": "emp_head_eng"},
            ),
            Action(
                name="update_task_priority",
                kwargs={
                    "task_id": "task_015",
                    "new_priority": "critical",
                },
            ),
            Action(
                name="reassign_task",
                kwargs={
                    "task_id": "task_015",
                    "new_assignee_id": "emp_dev_20",
                },
            ),
            Action(
                name="get_task_details",
                kwargs={
                    "task_id": "task_015",
                },
            ),
            Action(
                name="update_task_status",
                kwargs={"task_id": "task_004", "new_status": "done"},
            ),
            Action(
                name="update_task_status",
                kwargs={"task_id": "task_012", "new_status": "done"},
            ),
            Action(
                name="resolve_blocked_task",
                kwargs={
                    "task_id": "task_015",
                    "resolution": "Resolved by sprint lead",
                    "unblock_dependencies": True
                },
            ),
            Action(
                name="update_task_status",
                kwargs={"task_id": "task_015", "new_status": "in_progress"},
            ),
            Action(name="generate_sprint_report", kwargs={"sprint_id": "sprint_002"}),
        ],
        outputs=['"tasks_needing_escalation": 1'],
    ),
    Task(
        annotator="0",
        user_id="complete_sprint_cycle",
        instruction="""You are the scrum master analyzing the sprint_001 for
        team_analytics_01. Find the number of noncompliant time logging tasks,
        calculate the team's velocity trend for the last 3 sprints, and report the burndown completion
        progress and capacity hours. Mark sprint_001 as reviewed.""",
        actions=[
            Action(name="get_sprint_details", kwargs={"sprint_id": "sprint_001"}),
            Action(
                name="calculate_sprint_burndown", kwargs={"sprint_id": "sprint_001"}
            ),
            Action(name="generate_sprint_report", kwargs={"sprint_id": "sprint_001"}),
            Action(
                name="check_time_logging_compliance", kwargs={"sprint_id": "sprint_001"}
            ),
            Action(
                name="get_team_velocity",
                kwargs={"team_id": "team_analytics_01", "last_n_sprints": 3},
            ),
            Action(
                name="calculate_team_capacity",
                kwargs={"team_id": "team_analytics_01", "sprint_id": "sprint_001"},
            ),
            Action(
                name="mark_sprint_as_reviewed",
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
        instruction="""You are a QA bottleneck resolution specialist. Calculate
        team_qa_01's current capacity. Update task_011 priority to high.
        Reassign task_011 to emp_test_05. Create task "Automated test framework
        setup" with description "Set up comprehensive automated testing
        framework" with 6 story points for emp_sec_test_01 with high priority.
        Create dependency where task_020 depends on task_008. Log 5 hours on
        task_008 with notes "Test framework implementation progress". Resolve
        task_015 and unblock dependencies with resolution "Additional QA resources allocated". Check time
        logging compliance. Log 4 hours on task_004 with notes "QA compliance
        time logging" and using 'emp_dev_20' as employee ID. Create "QA process
        optimization" task with description
        "Optimize QA processes to eliminate bottlenecks" with 4 story points for
        emp_qa_02 with critical priority in sprint_002. Calculate final capacity
        for team_qa_01 in sprint_002. Output the final team utilization
        percentage and the non-compliant task count before fixes.""",
        actions=[
            Action(name="calculate_team_capacity", kwargs={"team_id": "team_qa_01"}),
            Action(
                name="update_task_priority",
                kwargs={
                    "task_id": "task_011",
                    "new_priority": "high",
                },
            ),
            Action(
                name="reassign_task",
                kwargs={
                    "task_id": "task_011",
                    "new_assignee_id": "emp_test_05",
                },
            ),
            Action(
                name="create_task",
                kwargs={
                    "title": "Automated test framework setup",
                    "description": "Set up comprehensive automated testing framework",
                    "assignee_id": "emp_sec_test_01",
                    "priority": "high",
                    "story_points": 6,
                },
            ),
            Action(
                name="create_task_dependency",
                kwargs={"task_id": "task_020", "depends_on_task_id": "task_008"},
            ),
            Action(
                name="log_time_on_task",
                kwargs={
                    "task_id": "task_008",
                    "hours_logged": 5,
                    "employee_id": "emp_test_05",
                    "notes": "Test framework implementation progress",
                },
            ),
            Action(
                name="resolve_blocked_task",
                kwargs={
                    "task_id": "task_015",
                    "resolution": "Additional QA resources allocated",
                    "unblock_dependencies": True,
                },
            ),
            Action(name="check_time_logging_compliance", kwargs={"check_all": True}),
            Action(
                name="log_time_on_task",
                kwargs={
                    "task_id": "task_004",
                    "hours_logged": 4,
                    "employee_id": "emp_dev_20",
                    "notes": "QA compliance time logging",
                },
            ),
            Action(
                name="create_task",
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
                name="calculate_team_capacity",
                kwargs={"team_id": "team_qa_01", "sprint_id": "sprint_002"},
            ),
            Action(name="generate_sprint_report", kwargs={"sprint_id": "sprint_002"}),
        ],
        outputs=['"team_utilization": 10.0', '"non_compliant_count": 8'],
    ),
    Task(
        annotator="0",
        user_id="conflict_resolution_specialist",
        instruction="""
        You are the PMO director handling resource conflicts. Check employee
        emp_arch_01's workload across all projects. Create a coordination task
        called "Architecture split allocation review" with 5 story points for
        emp_pm_03 in sprint_002 with critical priority. Reassign task_010 from
        emp_dev_21 to emp_arch_01 to balance workload. Update task_010 priority
        to low. Calculate and output final team 'team_dev_01' utilization and
        the task_010 logged hours.""",
       actions=[
            Action(name="get_employee_workload", kwargs={"employee_id": "emp_arch_01"}),
            Action(
                name="create_task",
                kwargs={
                    "title": "Architecture split allocation review",
                    "assignee_id": "emp_pm_03",
                    "priority": "critical",
                    "story_points": 5,
                    "sprint_id": "sprint_002",
                },
            ),
            Action(name="search_tasks", kwargs={"task_id": "task_010"}),
            Action(
                name="reassign_task",
                kwargs={
                    "task_id": "task_010",
                    "new_assignee_id": "emp_arch_01",
                },
            ),
            Action(
                name="update_task_priority",
                kwargs={
                    "task_id": "task_010",
                    "new_priority": "low",
                },
            ),
            Action(
                name="calculate_team_capacity",
                kwargs={"team_id": "team_dev_01", "sprint_id": "sprint_002"},
            ),
            Action(name="generate_sprint_report", kwargs={"sprint_id": "sprint_002"}),
        ],
        outputs=[
            '"team_utilization": 22.5',
            '"time_logged": 0',
        ],
    ),
    Task(
        annotator="0",
        user_id="sprint_health_monitor",
        instruction="""You are the scrum master monitoring sprint health.
        Calculate burndown for sprint_002. Check time logging compliance to
        identify issues. Log 4 hours for task_004 . Search for blocked tasks in
        the sprint and update task_015's status to todo to unblock it. Calculate
        final team capacity for team_dev_01 and report the completion percentage
        and team utilization.""",
        actions=[
            Action(
                name="calculate_sprint_burndown", kwargs={"sprint_id": "sprint_002"}
            ),
            Action(
                name="check_time_logging_compliance", kwargs={"sprint_id": "sprint_002"}
            ),
            Action(name="search_tasks", kwargs={"task_id": "task_004"}),
            Action(
                name="get_task_details",
                kwargs={
                    "task_id": "task_004",
                },
            ),
            Action(
                name="log_time_on_task",
                kwargs={
                    "task_id": "task_004",
                    "hours_logged": 4,
                    "employee_id": "emp_dev_20",
                },
            ),
            Action(
                name="search_tasks",
                kwargs={"status": "blocked", "sprint_id": "sprint_002"},
            ),
            Action(
                name="update_task_status",
                kwargs={"task_id": "task_015", "new_status": "todo"},
            ),
            Action(
                name="calculate_team_capacity",
                kwargs={"team_id": "team_dev_01", "sprint_id": "sprint_002"},
            ),
            Action(
                name="calculate_sprint_burndown", kwargs={"sprint_id": "sprint_002"}
            ),
        ],
        outputs=[
            '"completion_percentage": 0.0',
            '"team_utilization": 26.2',
            '"non_compliant_count": 4',
        ],
    )
]
