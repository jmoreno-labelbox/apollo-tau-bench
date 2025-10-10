from domains.dto import Action, Task

TASKS = [
    Task(
        annotator="0",
        user_id="resolve_resource_overallocation",
        instruction="""
        You are a resource manager. Your developer Emma Wilson is allocated at 120% capacity. Review her current
        allocations, identify the lower priority project, and reduce that allocation to bring her to 100%. Output
        the final employee utilization in hours per week and percentage.
        """,
        actions=[
            Action(name="search_employees", kwargs={"name": "Emma Wilson"}),
            Action(
                name="get_employee_allocations", kwargs={"employee_id": "emp_dev_05"}
            ),
            Action(name="get_project_details", kwargs={"project_id": "proj_web_01"}),
            Action(name="get_project_details", kwargs={"project_id": "proj_api_02"}),
            Action(
                name="compare_project_priorities",
                kwargs={"project_id_1": "proj_web_01", "project_id_2": "proj_api_02"},
            ),
            Action(
                name="update_allocation",
                kwargs={"allocation_id": "alloc_web_01", "hours_per_week": 17},
            ),
            Action(
                name="calculate_employee_utilization",
                kwargs={"employee_id": "emp_dev_05"},
            ),
            Action(
                name="update_utilization_log",
                kwargs={
                    "employee_id": "emp_dev_05",
                    "new_utilization": 100,
                },
            ),
        ],
        outputs=['"total_hours": 40', '"utilization_percentage": 100'],
    ),
    Task(
        annotator="0",
        user_id="handle_urgent_resource_request",
        instruction="""You received an urgent request from the Engineering
        department for the role "Kubernetes Expert" for 'Cloud Migration' project. Find
        available employees with this skill in the Engineering department, if
        multiple employees have this skill, chose the one with the lowest
        utilization. Get the available hours of this employee and allocate it in
        the project 'Cloud Migration'. The allocation should have the start_date
        2024-03-01 and end_date 2024-12-31. Update the department capacity and
        output the employee ID and hours allocated to the project 'Cloud
        Migration'.""",
        actions=[
            Action(name="search_projects", kwargs={"name": "Cloud Migration"}),
            Action(
                name="search_employees",
                kwargs={"skills": ["Kubernetes"], "department": "Engineering"},
            ),
            Action(
                name="calculate_employee_availability",
                kwargs={"employee_id": "emp_devops_04"},
            ),
            Action(
                name="create_allocation",
                kwargs={
                    "employee_id": "emp_devops_04",
                    "project_id": "proj_cloud_01",
                    "hours_per_week": 16,
                    "role": "Kubernetes Expert",
                    "start_date": "2024-03-01",
                    "end_date": "2024-12-31",
                    "status": "active",
                },
            ),
            Action(
                name="update_utilization_log",
                kwargs={
                    "employee_id": "emp_devops_04",
                    "new_utilization": 100,
                },
            ),
            Action(
                name="update_department_capacity",
                kwargs={
                    "department": "Engineering",
                    "employee_id": "emp_devops_04",
                    "hours_allocated": 16,
                },
            ),
        ],
        outputs=['"employee_id": "emp_devops_04", "hours_allocated": 16"'],
    ),
    Task(
        annotator="0",
        user_id="cross_department_resource_sharing",
        instruction="""
        You are the operations director. Engineering needs a UX designer from Design department for 'Product Redesign'
        project. Search for UX designers across 'Design' department with utilization lower than 80%. Allocate 20 hours
        of the employee with the lowest utilization among the search results to the 'Product Redesign' project. The
        allocation start date should be "2024-02-15" and the end date should be "2024-07-31". Remember that this is a
        cross department allocation, output the hours allocated.
        """,
        actions=[
            Action(name="search_projects", kwargs={"name": "Product Redesign"}),
            Action(
                name="search_employees",
                kwargs={"department": "Design", "role": "UX Designer", "utilization_below": 80},
            ),
            Action(
                name="calculate_employee_availability",
                kwargs={"employee_id": "emp_ux_03"},
            ),
            Action(
                name="create_allocation",
                kwargs={
                    "employee_id": "emp_ux_03",
                    "project_id": "proj_redesign_01",
                    "hours_per_week": 20,
                    "role": "UX Designer",
                    "start_date": "2024-02-15",
                    "end_date": "2024-07-31",
                    "status": "active",
                    "cross_department": True,
                },
            ),
            Action(
                name="update_utilization_log",
                kwargs={
                    "employee_id": "emp_ux_03",
                    "new_utilization": 50,
                },
            ),
            Action(
                name="update_department_capacity",
                kwargs={
                    "department": "Design",
                    "employee_id": "emp_ux_03",
                    "hours_allocated": 20,
                    "cross_department_project": "proj_redesign_01",
                },
            ),
        ],
        outputs=['"hours_allocated": 20'],
    ),
    Task(
        annotator="0",
        user_id="rebalance_team_workload",
        instruction="""You are the resource planning manager. The Analytics Team has uneven utilization. Check each member's allocations, identify overutilized and underutilized members, then redistribute work by moving 10 hours from the busiest to the least busy member. Create the new allocation for the Analytics Reporting project (proj_reporting_01) with start_date 2024-01-15 and end_date 2024-06-30.""",
        actions=[
            Action(name="get_team_details", kwargs={"team_name": "Analytics Team"}),
            Action(
                name="get_employee_allocations",
                kwargs={"employee_id": "emp_analyst_01"},
            ),
            Action(
                name="get_employee_allocations",
                kwargs={"employee_id": "emp_analyst_02"},
            ),
            Action(
                name="get_employee_allocations",
                kwargs={"employee_id": "emp_analyst_03"},
            ),
            Action(
                name="update_allocation",
                kwargs={"allocation_id": "alloc_report_01", "hours_per_week": 20},
            ),
            Action(
                name="create_allocation",
                kwargs={
                    "employee_id": "emp_analyst_03",
                    "project_id": "proj_reporting_01",
                    "hours_per_week": 10,
                    "role": "Junior Analyst",
                    "start_date": "2024-01-15",
                    "end_date": "2024-06-30",
                    "status": "active",
                },
            ),
            Action(
                name="update_utilization_log",
                kwargs={
                    "employee_id": "emp_analyst_01",
                    "new_utilization": 70,
                },
            ),
            Action(
                name="update_utilization_log",
                kwargs={
                    "employee_id": "emp_analyst_03",
                    "new_utilization": 85,
                },
            ),
            Action(
                name="summarize_workload_rebalance",
                kwargs={
                    "hours_transferred": 10,
                    "from_employee": "emp_analyst_01",
                    "to_employee": "emp_analyst_03",
                },
            ),
        ],
        outputs=['"rebalanced": true', '"hours_transferred": 10'],
    ),
    Task(
        annotator="0",
        user_id="emergency_project_staffing",
        instruction="""
        You are an emergency response manager. A critical 'Security Patch' project needs immediate staffing.
        Find developers with security clearance (secret level) who have available hours to fulfill all required hours
        for the project. Prioritize employees with lower utilization to allocate hours to the project.
        All allocations should have start_date 2024-03-15 and end_date 2024-04-30. Output the employees allocated to the
        'Security Patch' in this workflow and the the total of hours.
        """,
        actions=[
            Action(name="search_projects", kwargs={"name": "Security Patch"}),
            Action(name="get_project_allocations", kwargs={"project_id": "proj_security_patch"}),
            Action(
                name="search_employees",
                kwargs={"clearance": "secret", "role_contains": "Developer"},
            ),
            Action(
                name="calculate_employee_availability",
                kwargs={"employee_id": "emp_sec_dev_02"},
            ),
            Action(
                name="calculate_employee_availability",
                kwargs={"employee_id": "emp_sec_dev_03"},
            ),
            Action(
                name="calculate_employee_availability",
                kwargs={"employee_id": "emp_sec_dev_XX"},
            ),
            Action(
                name="create_allocation",
                kwargs={
                    "employee_id": "emp_sec_dev_03",
                    "project_id": "proj_security_patch",
                    "hours_per_week": 40,
                    "role": "Security Developer",
                    "start_date": "2024-03-15",
                    "end_date": "2024-04-30",
                    "status": "active",
                },
            ),
            Action(
                name="create_allocation",
                kwargs={
                    "employee_id": "emp_sec_dev_XX",
                    "project_id": "proj_security_patch",
                    "hours_per_week": 40,
                    "role": "Security Developer",
                    "start_date": "2024-03-15",
                    "end_date": "2024-04-30",
                    "status": "active",
                },
            ),
            Action(name="update_employees_utilization", kwargs={"employee_ids": ["emp_sec_dev_03", "emp_sec_dev_XX"]}),
        ],
        outputs=[
            '"employees_allocated": ["emp_sec_dev_03", "emp_sec_dev_XX"]',
            '"total_allocated_hours": 80'
        ],
    ),
    Task(
        annotator="0",
        user_id="mass_reallocation_after_cancellation",
        instruction="""
        You are the crisis manager. The 'proj_client_01' project was cancelled. Mark this project as 'cancelled' and
        relocate all developers of the cancelled project to the project 'proj_enterprise_01',
        and the remaining employees to the project 'proj_mobile_01'. Make sure to keep the same utilization for
        all employees relocated. Output the employees relocated by destination project.
        """,
        actions=[
            Action(
                name="get_project_allocations", kwargs={"project_id": "proj_client_01"}
            ),
            Action(
                name="update_project_status",
                kwargs={"project_id": "proj_client_01", "status": "cancelled"},
            ),
            Action(name="get_employee_details", kwargs={"employee_id": "emp_dev_20"}),
            Action(name="get_employee_details", kwargs={"employee_id": "emp_dev_21"}),
            Action(name="get_employee_details", kwargs={"employee_id": "emp_test_05"}),
            Action(
                name="create_allocation",
                kwargs={
                    "employee_id": "emp_dev_20",
                    "project_id": "proj_enterprise_01",
                    "hours_per_week": 40,
                    "role": "Frontend Developer",
                    "status": "active",
                },
            ),
            Action(
                name="create_allocation",
                kwargs={
                    "employee_id": "emp_dev_21",
                    "project_id": "proj_enterprise_01",
                    "hours_per_week": 40,
                    "role": "Backend Developer",
                    "status": "active",
                },
            ),
            Action(
                name="create_allocation",
                kwargs={
                    "employee_id": "emp_test_05",
                    "project_id": "proj_mobile_01",
                    "hours_per_week": 40,
                    "role": "Test Engineer",
                    "status": "active",
                },
            ),
            Action(
                name="delete_allocation", kwargs={"allocation_id": "alloc_client_01"}
            ),
            Action(
                name="delete_allocation", kwargs={"allocation_id": "alloc_client_02"}
            ),
            Action(
                name="delete_allocation", kwargs={"allocation_id": "alloc_client_03"}
            ),
        ],
        outputs=['"proj_mobile_01_allocation": ["emp_dev_20", "emp_dev_21"]', '"proj_mobile_01_allocation": ["emp_test_05"]'],
    ),
    Task(
        annotator="0",
        user_id="manage_bench_resources",
        instruction="""
        You are the resource manager and you are closing projects that are finishing this week.
        Find employees with active allocations ending in 2024-06-01 or sooner. Get the employee details for each employee found,
        create a bench assignment for each employee, with 2024-06-01 as start date, and immediate availability.
        Update the status and utilization for each employee. Output if a bench assignment was created.
        """,
        actions=[
            Action(
                name="search_allocations",
                kwargs={"end_date_before": "2024-06-01", "status": "active"},
            ),
            Action(name="get_employee_details", kwargs={"employee_id": "emp_dev_05"}),
            Action(
                name="create_bench_assignment",
                kwargs={
                    "employee_id": "emp_dev_05",
                    "start_date": "2024-06-01",
                    "skills": ["JavaScript", "Python", "React"],
                    "availability": "immediate",
                },
            ),
            Action(
                name="update_employee_status",
                kwargs={
                    "employee_id": "emp_dev_05",
                    "status": "bench",
                    "available_from": "2024-06-01",
                },
            ),
            Action(
                name="update_utilization_log",
                kwargs={
                    "employee_id": "emp_dev_05",
                    "new_utilization": 0,
                },
            ),
        ],
        outputs=['"bench_assignment": "created"'],
    ),
    Task(
        annotator="0",
        user_id="rotate_team_resources",
        instruction="""
        You are the Team Lead. Your team (team_analytics_01) has been on the same project for a long time and needs
        rotation for skill development. Find team members who have been working on projects for more than 550 days,
        create a rotation schedules (date=2024-04-01) for these cases to the project 'proj_beta_02'. Make sure
        the amount of hours to rotate matches the employee utilization in the previous project, and to set skill
        development rotation as true and holiday coverage as false. Output the
        employees who received rotation schedules.
        """,
        actions=[
            Action(name="get_team_details", kwargs={"team_id": "team_analytics_01"}),
            Action(
                name="get_employee_allocations",
                kwargs={"employee_id": "emp_analyst_01"},
            ),
            Action(
                name="check_allocation_duration",
                kwargs={
                    "employee_id": "emp_analyst_01",
                    "project_id": "proj_reporting_01",
                },
            ),
            Action(
                name="check_allocation_duration",
                kwargs={
                    "employee_id": "emp_analyst_01",
                    "project_id": "proj_insights_01",
                },
            ),
            Action(
                name="get_employee_allocations",
                kwargs={"employee_id": "emp_analyst_02"},
            ),
            Action(
                name="check_allocation_duration",
                kwargs={
                    "employee_id": "emp_analyst_02",
                    "project_id": "proj_reporting_01",
                },
            ),
            Action(
                name="check_allocation_duration",
                kwargs={
                    "employee_id": "emp_analyst_02",
                    "project_id": "proj_insights_01",
                },
            ),
            Action(
                name="get_employee_allocations",
                kwargs={"employee_id": "emp_analyst_03"},
            ),
            Action(
                name="check_allocation_duration",
                kwargs={
                    "employee_id": "emp_analyst_03",
                    "project_id": "proj_gamma_03",
                },
            ),
            Action(
                name="create_rotation_schedule",
                kwargs={
                    "employee_id": "emp_analyst_01",
                    "from_project": "proj_reporting_01",
                    "to_project": "proj_beta_02",
                    "rotation_date": "2024-04-01",
                    "hours_to_rotate": 30,
                    "skill_development_rotation": "true",
                    "holiday_coverage": "false",
                },
            ),
            Action(
                name="create_rotation_schedule",
                kwargs={
                    "employee_id": "emp_analyst_02",
                    "from_project": "proj_reporting_01",
                    "to_project": "proj_beta_02",
                    "rotation_date": "2024-04-01",
                    "hours_to_rotate": 10,
                    "skill_development_rotation": "true",
                    "holiday_coverage": "false",
                },
            ),
        ],
        outputs=['"rotation_employees": ["emp_analyst_01", "emp_analyst_02"]'],
    ),
    Task(
        annotator="0",
        user_id="optimize_resource_utilization",
        instruction="""
        You are the resource manager. You need to optimize resource utilization across projects. Find senior resources
        who have utilization below 90%, allocate all available hours from then following the rule: developers should
        be allocated to the project 'proj_security_patch' and the remaining employees to the project 'proj_web_03'.
        Output the employees allocated by destination project.
        """,
        actions=[
            Action(
                name="search_employees",
                kwargs={"role_contains": "Senior", "utilization_below": 90},
            ),
            Action(
                name="calculate_employee_availability", kwargs={"employee_id": "emp_dev_03"}
            ),
            Action(name="calculate_employee_availability", kwargs={"employee_id": "emp_data_01"}),
            Action(name="calculate_employee_availability", kwargs={"employee_id": "emp_eng_20"}),
            Action(
                name="create_allocation",
                kwargs={
                    "employee_id": "emp_dev_03",
                    "project_id": "proj_security_patch",
                    "hours_per_week": 10,
                    "role": "Senior Developer",
                    "status": "active",
                },
            ),
            Action(
                name="create_allocation",
                kwargs={
                    "employee_id": "emp_eng_20",
                    "project_id": "proj_security_patch",
                    "hours_per_week": 8,
                    "role":  "Senior Developer",
                    "status": "active",
                },
            ),
            Action(
                name="create_allocation",
                kwargs={
                    "employee_id": "emp_data_01",
                    "project_id": "proj_web_03",
                    "hours_per_week": 8,
                    "role": "Senior Data Analyst",
                    "status": "active",
                },
            ),
            Action(
                name="update_utilization_log",
                kwargs={
                    "employee_id": "emp_data_01",
                    "new_utilization": 100,
                },
            ),
            Action(
                name="update_utilization_log",
                kwargs={
                    "employee_id": "emp_dev_03",
                    "new_utilization": 100,
                },
            ),
            Action(
                name="update_utilization_log",
                kwargs={
                    "employee_id": "emp_eng_20",
                    "new_utilization": 100,
                },
            ),
        ],
        outputs=[
            '"proj_web_03_allocations": ["emp_data_01"]',
            '"proj_security_patch_allocations": ["emp_dev_03", "emp_eng_20"]'
        ],
    ),
    Task(
        annotator="0",
        user_id="redistribute_department_workload",
        instruction="""
        You are the department head. Your QA department has uneven workload distribution with some employees overloaded
        (utilization above 90%) and others underutilized (utilization of 70% or below). Analyze overloaded and
        underutilized in the QA department. For
        overloaded employees update their allocations by removing the amount
        of hours necessary for the employee achieve 90% utilization. For underutilized employees, allocate the amount
        of hours necessary to achieve 90% utilization to the project 'proj_client_01'. Calculate and output the department
        utilization and the increased or decreased hours per employee.
        """,
        actions=[
            Action(
                name="search_employees",
                kwargs={"department": "QA", "utilization_above": 90},
            ),
            Action(
                name="get_employee_allocations",
                kwargs={"employee_id": "emp_test_05"},
            ),
            Action(
                name="update_allocation",
                kwargs={"allocation_id": "alloc_client_03", "hours_per_week": 36},
            ),
            Action(
                name="search_employees",
                kwargs={"department": "QA", "utilization_below": 70},
            ),
            Action(
                name="get_employee_allocations",
                kwargs={"employee_id": "emp_sec_test_01"},
            ),
            Action(
                name="get_employee_allocations",
                kwargs={"employee_id": "emp_qa_02"},
            ),
            Action(
                name="create_allocation",
                kwargs={
                    "employee_id": "emp_sec_test_01",
                    "project_id": "proj_client_01",
                    "hours_per_week": 8,
                    "role": "Security Tester",
                    "status": "active",
                },
            ),
            Action(
                name="create_allocation",
                kwargs={
                    "employee_id": "emp_qa_02",
                    "project_id": "proj_client_01",
                    "hours_per_week": 12,
                    "role": "QA Engineer",
                    "status": "active",
                },
            ),
            Action(
                name="calculate_department_utilization", kwargs={"department": "QA"}
            ),
            Action(
                name="update_employees_utilization",
                kwargs={"employee_ids": ["emp_test_05", "emp_qa_02", "emp_sec_test_01"]},
            ),
        ],
        outputs=['"emp_test_05": -4', '"emp_qa_02": 12','"emp_sec_test_01": 8', '"department_utilization": 90'],
    ),
    Task(
        annotator="0",
        user_id="execute_multi_project_resource_optimization",
        instruction="""
        You are the portfolio director. You need to optimize resource allocation across 2 major projects
        (Enterprise Platform and Platform Modernization).
        For both projects, get details for all
        employees allocated, then update the allocations considering the maximum capacity of each employee.
        You should disregard employees who participate in both projects. Output the new utilization percentage by employee.
        """,
        actions=[
            Action(name="search_projects", kwargs={"name": "Enterprise Platform"}),
            Action(name="search_projects", kwargs={"name": "Platform Modernization"}),
            Action(
                name="get_project_allocations",
                kwargs={"project_id": "proj_enterprise_01"},
            ),
            Action(
                name="get_project_allocations",
                kwargs={"project_id": "proj_platform_02"},
            ),
            Action(
                name="get_employee_details", kwargs={"employee_id": "emp_devops_02"}
            ),
            Action(
                name="update_allocation",
                kwargs={"allocation_id": "alloc_devops_01", "hours_per_week": 40},
            ),
            Action(
                name="get_employee_details", kwargs={"employee_id": "emp_data_02"}
            ),
            Action(
                name="update_allocation",
                kwargs={"allocation_id":  "alloc_data_02", "hours_per_week": 40},
            ),
            Action(
                name="get_employee_details", kwargs={"employee_id":  "emp_devops_04"}
            ),
            Action(
                name="update_allocation",
                kwargs={"allocation_id":  "alloc_devops_02", "hours_per_week": 40},
            ),
            Action(
                name="update_employees_utilization",
                kwargs={"employee_ids": ["emp_devops_02", "emp_devops_04", "emp_data_02"]},
            ),
        ],
        outputs=['"emp_devops_02": 100', '"emp_devops_04": 100', '"emp_data_02": 100'],
    ),
    Task(
        annotator="0",
        user_id="emergency_resource_allocation",
        instruction="""
        You are a project manager. Your critical project 'Mobile App Launch' needs an additional developer with
        JavaScript skills who can contribute to React development (minimum proficiency 4 for both skills).
        You need someone with at least 20 hours per week available. If none employee with these skills have 20 hours
        available, choose the employee with these skills with less utilization and allocate all available hours to the
        project. Make sure to update the employee utilization percentage to 100%.
        The allocation must have start_date 2024-01-15 and end_date 2024-06-30. Output the allocation ID and the allocated
        hours

        """,
        actions=[
            Action(name="search_projects", kwargs={"name": "Mobile App Launch"}),
            Action(name="get_project_details", kwargs={"project_id": "proj_mobile_01"}),
            Action(
                name="search_employees",
                kwargs={
                    "skills": ["JavaScript", "React"],
                    "min_proficiency": 4,
                    "min_skill_matches": 2,
                    "min_available_hours": 20,
                },
            ),
            Action(
                name="search_employees",
                kwargs={
                    "skills": ["JavaScript", "React"],
                    "min_proficiency": 4,
                    "min_skill_matches": 2,
                },
            ),
            Action(
                name="calculate_employee_availability",
                kwargs={"employee_id":  "emp_eng_20"},
            ),
            Action(
                name="create_allocation",
                kwargs={
                    "allocation_id": "alloc_mobile_04",
                    "employee_id": "emp_eng_20",
                    "project_id": "proj_mobile_01",
                    "hours_per_week": 8,
                    "role":  "Senior Developer",
                    "start_date": "2024-01-15",
                    "end_date": "2024-06-30",
                    "status": "active",
                },
            ),
            Action(
                name="update_utilization_log",
                kwargs={
                    "employee_id": "emp_eng_20",
                    "new_utilization": 100,
                },
            ),
        ],
        outputs=[
            '"allocation_id": "alloc_mobile_04"',
            '"hours_per_week": 8',
            '"status": "active"',
        ],
    ),
    Task(
        annotator="0",
        user_id="skill_based_team_expansion",
        instruction="""
        You are the HR director. The 'Customer Insights' project currently needs new staff. Find a non-junior
        employee with utilization at 70% or below to work on Python features and a junior employee with SQL skills who have
        utilization at 60% or below. In case of multiple
        candidates, choose the one with the lower utilization percentage, in case of tie, choose the first employee
        to appear in the search results. Allocate the minimum between 30 and the available hours of the chosen
        employees to the project. The allocation period should be the same as the project period. Output the
        allocated hours per employee ID. Output the new employees added to the project, the total allocated hours in
        the workflow and the project total hours.
        """,
        actions=[
            Action(name="search_projects", kwargs={"name": "Customer Insights"}),
            Action(
                name="get_project_details", kwargs={"project_id": "proj_insights_01"}
            ),
            Action(
                name="get_project_allocations",
                kwargs={"project_id": "proj_insights_01"},
            ),
            Action(
                name="search_employees",
                kwargs={"skills": ["Python"], "utilization_below": 70, "role_disregard": "Junior"},
            ),
            Action(
                name="search_employees",
                kwargs={"skills": ["SQL"], "utilization_below": 60, "role_contains": "Junior"},
            ),
            Action(
                name="calculate_employee_availability",
                kwargs={"employee_id": "emp_analyst_03"},
            ),
            Action(
                name="calculate_employee_availability",
                kwargs={"employee_id":  "emp_sec_dev_03"},
            ),
            Action(
                name="create_allocation",
                kwargs={
                    "allocation_id": "alloc_insights_04",
                    "employee_id": "emp_analyst_03",
                    "project_id": "proj_insights_01",
                    "hours_per_week": 16,
                    "role": "Junior Analyst",
                    "start_date": "2024-02-01",
                    "end_date": "2024-08-31",
                    "status": "active",
                },
            ),
            Action(
                name="create_allocation",
                kwargs={
                    "allocation_id": "alloc_insights_05",
                    "employee_id": "emp_sec_dev_03",
                    "project_id": "proj_insights_01",
                    "hours_per_week": 30,
                    "role": "Security Developer",
                    "start_date": "2024-02-01",
                    "end_date": "2024-08-31",
                    "status": "active",
                },
            ),
            Action(
                name="update_utilization_log",
                kwargs={
                    "employee_id": "emp_analyst_03",
                    "new_utilization": 100,
                },
            ),
            Action(
                name="update_utilization_log",
                kwargs={
                    "employee_id": "emp_sec_dev_03",
                    "new_utilization": 75,
                },
            ),
        ],
        outputs=[
            '"new_team_members": ["emp_analyst_03", "emp_sec_dev_03"]',
            '"additional_hours": 46',
            '"total_hours": 76',
        ],
    ),
    Task(
        annotator="0",
        user_id="fill_multiple_skill_gaps",
        instruction="""
        Your 'AI Platform' project needs Machine Learning engineers with proficiency level 4 or higher. Search for available
        employees to fulfill this demand. Calculate availability
        of the employees in the search result. If none employee with the specified aspects were found, or the total
        available hours calculated plus the project allocated hours is less than the project required hours,
        create an urgent resource request (id=req_ai_ml_01) for external hiring with the amount of hours necessary to
        fulfill the project required hours. Output if a skill gap was identified, the request ID and the request hours.
        """,
        actions=[
            Action(name="search_projects", kwargs={"name": "AI Platform"}),
            Action(name="get_project_details", kwargs={"project_id": "proj_ai_01"}),
            Action(
                name="search_employees",
                kwargs={"skills": ["Machine Learning"], "min_proficiency": 4},
            ),
            Action(
                name="create_resource_request",
                kwargs={
                    "request_id": "req_ai_ml_01",
                    "project_id": "proj_ai_01",
                    "skill_required": "Machine Learning",
                    "hours_needed": 88,
                    "urgency": "urgent",
                    "department": "Engineering",
                },
            ),
        ],
        outputs=[
            '"skill_gap_identified": true',
            '"request_id": "req_ai_ml_01"',
            '"hours_needed": 88',
        ],
    ),
    Task(
        annotator="0",
        user_id="consolidate_project_teams",
        instruction="""
        You are the integration director. Three projects (Alpha Module, Beta
        Module, and Gamma Module) are being consolidated. Find these projects,
        use Alpha Module as the unified project, transfer all team members from
        the consolidated projects to the unified project. Create new allocations
        if the relocated employees are not currently in the Alpha Module
        project, otherwise, just update the allocation. Keep the original
        start/end dates for existing allocations, but use the unified projects's
        start/end dates for new allocations. Delete the allocations
        from consolidated projects, and mark this projects as cancelled. Update
        the unified project required hours to the required hours summation of
        all three projects. Create a team called "Alpha Unified Team" with the
        employees of the new unified project and output a consolidation summary
        with the team size, total allocation hours and the unified project ID.
        """,
        actions=[
            Action(name="search_projects", kwargs={"name": "Alpha Module"}),
            Action(name="search_projects", kwargs={"name": "Beta Module"}),
            Action(name="search_projects", kwargs={"name": "Gamma Module"}),
            Action(name="get_project_details", kwargs={"project_id": "proj_alpha_01"}),
            Action(name="get_project_details", kwargs={"project_id": "proj_beta_02"}),
            Action(name="get_project_details", kwargs={"project_id": "proj_gamma_03"}),
            Action(
                name="get_project_allocations", kwargs={"project_id": "proj_alpha_01"}
            ),
            Action(
                name="get_project_allocations", kwargs={"project_id": "proj_beta_02"}
            ),
            Action(
                name="get_project_allocations", kwargs={"project_id": "proj_gamma_03"}
            ),
            Action(
                name="update_allocation",
                kwargs={"allocation_id": "alloc_alpha_01", "hours_per_week": 60},
            ),
            Action(name="delete_allocation", kwargs={"allocation_id": "alloc_beta_01"}),
            Action(
                name="delete_allocation", kwargs={"allocation_id": "alloc_gamma_01"}
            ),
            Action(
                name="create_allocation",
                kwargs={
                    "allocation_id": "alloc_alpha_03",
                    "employee_id": "emp_qa_02",
                    "project_id": "proj_alpha_01",
                    "hours_per_week": 24,
                    "role":  "QA Engineer",
                    "start_date": "2024-01-01",
                    "end_date": "2024-06-30",
                    "status": "active",
                },
            ),
            Action(
                name="delete_allocation", kwargs={"allocation_id": "alloc_analyst_03"}
            ),
            Action(
                name="create_allocation",
                kwargs={
                    "allocation_id": "alloc_alpha_04",
                    "employee_id":  "emp_analyst_03",
                    "project_id": "proj_alpha_01",
                    "hours_per_week": 24,
                    "role":  "Junior Analyst",
                    "start_date": "2024-01-01",
                    "end_date": "2024-06-30",
                    "status": "active",
                },
            ),
            Action(
                name="create_team",
                kwargs={
                    "team_id": "team_alpha_unified",
                    "team_name": "Alpha Unified Team",
                    "project_id": "proj_alpha_01",
                    "team_members": ["emp_dev_15", "emp_qa_02", "emp_analyst_03"],
                },
            ),
            Action(
                name="update_project_status",
                kwargs={"project_id": "proj_beta_02", "status": "cancelled"},
            ),
            Action(
                name="update_project_status",
                kwargs={"project_id": "proj_gamma_03", "status": "cancelled"},
            ),
            Action(
                name="update_project_required_hours",
                kwargs={"project_id": "proj_alpha_01", "required_hours": "180"},
            ),
        ],
        outputs=[
            '"consolidated_to": "proj_alpha_01"',
            '"total_hours": 108',
            '"team_size": 3',
        ],
    ),
    Task(
        annotator="0",
        user_id="handle_clearance_requirement_change",
        instruction="""
        You are the security compliance manager. The 'Banking Integration' project now requires all team members to have
        secret clearance due to new regulatory requirements. Review current allocations, identify employees without
        proper clearance, find replacements with secret clearance who have the same job role as the replaced employees,
        and availability to get all replaced employees allocated hours.
        Finally output the employees removed and added to the project, also, output the compliance status validation.
        The allocations must have start_date 2024-01-01 and end_date 2024-08-31.
        """,
        actions=[
            Action(name="search_projects", kwargs={"name": "Banking Integration"}),
            Action(
                name="get_project_allocations", kwargs={"project_id": "proj_banking_01"}
            ),
            Action(name="get_employee_details", kwargs={"employee_id": "emp_sec_dev_01"}),
            Action(
                name="search_employees",
                kwargs={
                    "clearance": "secret",
                    "role_contains": "Security Developer",
                    "min_available_hours": 40,
                },
            ),
            Action(
                name="calculate_employee_availability",
                kwargs={"employee_id": "emp_sec_dev_XX"},
            ),
            Action(
                name="create_resource_conflict",
                kwargs={
                    "employee_id": "emp_sec_dev_01",
                    "competing_projects": ["proj_banking_01"],
                    "conflict_type": "clearance_violation",
                },
            ),
            Action(name="delete_allocation", kwargs={"allocation_id": "alloc_bank_01"}),
            Action(
                name="create_allocation",
                kwargs={
                    "employee_id": "emp_sec_dev_XX",
                    "project_id": "proj_banking_01",
                    "hours_per_week": 40,
                    "role": "Security Developer",
                    "start_date": "2024-01-01",
                    "end_date": "2024-08-31",
                    "status": "active",
                },
            ),
            Action(
                name="update_employees_utilization",
                kwargs={"employee_ids": ["emp_sec_dev_XX", "emp_sec_dev_01"]},
            ),
            Action(
                name="validate_compliance_status",
                kwargs={
                    "project_id": "proj_banking_01",
                    "required_clearance": "secret",
                },
            ),
        ],
        outputs=[
            '"employees_removed": "emp_sec_dev_01"',
            '"employees_added": "emp_sec_dev_XX"',
            '"compliance_achieved": true'
        ],
    ),
    Task(
        annotator="0",
        user_id="manage_skill_shortage_cascade",
        instruction="""
        You are the talent director. Three senior Machine Learning engineers
        just resigned from the 'AI Platform' project, creating a critical skill
        shortage. You should allocate 92 hours to this project. First allocate
        all available hours from employees who have 'Machine Learning' skills.
        If this allocation did not complete the 92 hours required, search for
        employees with Python skills and proficiency 4 or above who have 85%
        utilization or lower. Prioritize employees with lower utilization
        percentage, in case of tie, chose the first employee in the search
        result list. You should try to allocate all available hours from the
        employees following the priority until the total allocation achieves 92.
        Create a team called 'AI Emergency Response Team' with the new staff
        configuration for the project. Create an urgent resource request for
        external hiring needing 70 hours, with the skill 'Machine Learning' and
        'Engineering' department. Output the project allocated hours by
        employees.
        """,
        actions=[
            Action(name="search_projects", kwargs={"name": "AI Platform"}),
            Action(name="get_project_allocations", kwargs={"project_id": "proj_ai_01"}),
            Action(name="search_employees", kwargs={"skills": ["Machine Learning"]}),
            Action(name="calculate_employee_availability", kwargs={"employee_id": "emp_data_01"}),
            Action(name="update_allocation", kwargs={"allocation_id":  "alloc_data_01", "hours_per_week": 40}),
            Action(name="update_utilization_log", kwargs={"employee_id":  "emp_data_01", "new_utilization": 100}),
            Action(
                name="search_employees",
                kwargs={
                    "skills": ["Python"],
                    "min_proficiency": 4,
                    "utilization_below": 85,
                },
            ),
            Action(name="calculate_employee_availability", kwargs={"employee_id":  "emp_sec_dev_XX"}),
            Action(
                name="create_allocation",
                kwargs={
                    "employee_id": "emp_sec_dev_XX",
                    "project_id": "proj_ai_01",
                    "hours_per_week": 40,
                    "role":  "Security Developer",
                    "status": "active",
                },
            ),
            Action(name="calculate_employee_availability", kwargs={"employee_id": "emp_data_02"}),
            Action(
                name="create_allocation",
                kwargs={
                    "employee_id": "emp_data_02",
                    "project_id": "proj_ai_01",
                    "hours_per_week": 12,
                    "role":  "Data Engineer",
                    "status": "active",
                },
            ),
            Action(
                name="create_resource_request",
                kwargs={
                    "project_id": "proj_ai_01",
                    "skill_required": "Machine Learning",
                    "hours_needed": 70,
                    "urgency": "urgent",
                    "department": "Engineering",
                },
            ),
            Action(
                name="create_team",
                kwargs={
                    "team_name": "AI Emergency Response Team",
                    "project_id": "proj_ai_01",
                    "team_members": ["emp_data_02", "emp_sec_dev_XX", "emp_data_01"],
                },
            ),
            Action(
                name="update_employees_utilization",
                kwargs={"employee_ids": ["emp_data_02", "emp_sec_dev_XX", "emp_data_01"]}
            ),
        ],
        outputs=['"emp_data_01": 40', '"emp_sec_dev_XX": 40', '"emp_data_02": 12'],
    ),
    Task(
        annotator="0",
        user_id="optimize_resource_allocation_efficiency",
        instruction="""
        You are the responsible for asset optimization. The 'Enterprise Platform' project has issues with resource
        allocation with senior architects doing junior-level work. Analyze the current allocations, for each senior
        employee, search a junior employee for replacement. Here's an example on what you should do to search junior
        employees: for each senior in the project, search for a employee who contains 'Junior' in the job role and
        have at least 2 of the three skills that appears in the senior employee details, also, use the senior employee
        allocated hours as the parameter 'min_available_hours' in the employees search. If a junior employee who satisfies
        the specifications is found, allocated the senior employee hours to the junior employee and delete the senior employee allocation.
        In case of multiple junior employee alternatives, choose the first
        employee that appears in the search result. Calculate the projects' optimization metrics and output the efficiency gain.
        """,
        actions=[
            Action(name="search_projects", kwargs={"name": "Enterprise Platform"}),
            Action(
                name="get_project_details", kwargs={"project_id": "proj_enterprise_01"}
            ),
            Action(
                name="get_project_allocations",
                kwargs={"project_id": "proj_enterprise_01"},
            ),
            Action(name="get_employee_details", kwargs={"employee_id": "emp_arch_01"}),
            Action(
                name="search_employees",
                kwargs={
                    "skills": ["System Design", "Cloud Architecture", "Microservices"],
                    "min_skill_matches": 2,
                    "role_contains": "Junior",
                    "min_available_hours": 20,
                },
            ),
            Action(
                name="calculate_employee_availability",
                kwargs={"employee_id": "emp_jr_arch_01"},
            ),
            Action(
                name="delete_allocation",
                kwargs={"allocation_id": "alloc_arch_01"},
            ),
            Action(
                name="create_allocation",
                kwargs={
                    "employee_id": "emp_jr_arch_01",
                    "project_id": "proj_enterprise_01",
                    "hours_per_week": 20,
                    "role":  "Junior Architect",
                    "status": "active",
                },
            ),
            Action(
                name="update_employees_utilization",
                kwargs={"employee_ids": ["emp_jr_arch_01", "emp_arch_01"]},
            ),
            Action(
                name="calculate_optimization_metrics",
                kwargs={
                    "projects": ["proj_enterprise_01"],
                    "metric_type": "efficiency_gain",
                },
            ),
        ],
        outputs=['"efficiency_gain": 28'],
    ),
    Task(
        annotator="0",
        user_id="handle_department_merger",
        instruction="""
        You are the restructuring lead. Analytics and QA departments are merging into a new 'Quality Analytics'
        department. While creating the new department, use the Analytics head
        to be the head of this new department, and delete the old departments. Update the register of teams and
        employees with the merge. Output the new department total capacity and allocated hours.
        """,
        actions=[
            Action(name="get_department_teams", kwargs={"department": "Analytics"}),
            Action(name="get_department_teams", kwargs={"department": "QA"}),
            Action(name="search_employees", kwargs={"department": "Analytics"}),
            Action(name="search_employees", kwargs={"department": "QA"}),
            Action(name="get_department_teams", kwargs={"department": "Analytics"}),
            Action(name="get_department_details", kwargs={"name": "Analytics"}),
            Action(
                name="create_department",
                kwargs={
                    "name": "Quality Analytics",
                    "head_id": "emp_head_analytics"}
            ),
            Action(
                name="update_teams_department",
                kwargs={"team_id": "team_analytics_01", "department": "Quality Analytics"}
            ),
            Action(
                name="update_teams_department",
                kwargs={"team_id": "team_qa_01", "department": "Quality Analytics"}
            ),
            Action(
                name="update_teams_department",
                kwargs={"team_id": "team_qa_02", "department": "Quality Analytics"}
            ),
            Action(
                name="update_employees_department",
                kwargs={"employee_id": "emp_data_01", "department": "Quality Analytics"}
            ),
            Action(
                name="update_employees_department",
                kwargs={"employee_id": "emp_data_02", "department": "Quality Analytics"}
            ),
            Action(
                name="update_employees_department",
                kwargs={"employee_id": "emp_analyst_01", "department": "Quality Analytics"}
            ),
            Action(
                name="update_employees_department",
                kwargs={"employee_id": "emp_analyst_02", "department": "Quality Analytics"}
            ),
            Action(
                name="update_employees_department",
                kwargs={"employee_id": "emp_analyst_03", "department": "Quality Analytics"}
            ),
            Action(
                name="update_employees_department",
                kwargs={"employee_id": "emp_sec_test_01", "department": "Quality Analytics"}
            ),
            Action(
                name="update_employees_department",
                kwargs={"employee_id": "emp_qa_02", "department": "Quality Analytics"}
            ),
            Action(
                name="update_employees_department",
                kwargs={"employee_id": "emp_test_05", "department": "Quality Analytics"}
            ),
            Action(name="delete_department", kwargs={"name": "Analytics"}),
            Action(name="delete_department", kwargs={"name": "QA"}),
            Action(name="update_departments_utilization", kwargs={}),
            Action(name="get_department_details", kwargs={"name": "Quality Analytics"}),
        ],
        outputs=['"total_capacity": 320', '"allocated_hours": 244'],
    ),
    Task(
        annotator="0",
        user_id="implement_skills_development_rotation",
        instruction="""
        You are the skills development manager. Implement a rotation program where junior developers spend 25% time
        (10 hours/week) on advanced projects for skill development. Identify junior developers who are currently working on projects,
        with high potential (proficiency 3+), reduce their current allocations by 10 hours, and relocate the 10 hours to the 'Enterprise Platform'
        senior-led project. The allocations must have 'start_date' 2024-04-01, and 'end_date' 2024-06-30. The rotation
        date should be 2024-04-01, you should set the rotation schedule holiday coverage as false and skill development rotation as true.
        Output the number of developers in rotation and the total skills development hours.
        """,
        actions=[
            Action(
                name="search_employees",
                kwargs={"role_contains": "Junior", "min_proficiency": 3},
            ),
            Action(
                name="get_employee_allocations",
                kwargs={"employee_id": "emp_analyst_03"},
            ),
            Action(
                name="get_employee_allocations",
                kwargs={"employee_id": "emp_jr_arch_01"},
            ),
            Action(
                name="get_employee_details", kwargs={"employee_id": "emp_analyst_03"}
            ),
            Action(name="search_projects", kwargs={"name": "Enterprise Platform"}),
            Action(
                name="get_project_details", kwargs={"project_id": "proj_enterprise_01"}
            ),
            Action(
                name="update_allocation",
                kwargs={"allocation_id": "alloc_analyst_03", "hours_per_week": 14},
            ),
            Action(
                name="create_allocation",
                kwargs={
                    "employee_id": "emp_analyst_03",
                    "project_id": "proj_enterprise_01",
                    "hours_per_week": 10,
                    "role": "Junior Analyst",
                    "start_date": "2024-04-01",
                    "end_date": "2024-06-30",
                    "status": "active",
                },
            ),
            Action(
                name="create_rotation_schedule",
                kwargs={
                    "employee_id": "emp_analyst_03",
                    "from_project": "proj_gamma_03",
                    "to_project": "proj_enterprise_01",
                    "rotation_date": "2024-04-01",
                    "hours_to_rotate": 10,
                    "skill_development_rotation": "true",
                    "holiday_coverage": "false",
                },
            ),
        ],
        outputs=['"developers_in_rotation": 1', '"skill_development_hours": 10'],
    ),
    Task(
        annotator="0",
        user_id="manage_project_phase_transition",
        instruction="""
        You are the program manager. The 'Mobile App Launch' project is transitioning from development to testing phase
        on April 1st. Decrease developer allocations to 20 hours/week total, ramp up QA resources to 10 hours/week by
        finding QA staff with less than 80% utilization. Prioritize employees with lower utilization. The new allocations
        should have 'start_date' 2024-04-01 and 'end_date' "2024-06-30. Output the projects development hours and QA hours.
        """,
        actions=[
            Action(name="search_projects", kwargs={"name": "Mobile App Launch"}),
            Action(name="get_project_details", kwargs={"project_id": "proj_mobile_01"}),
            Action(
                name="get_project_allocations", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="update_allocation",
                kwargs={
                    "allocation_id": "alloc_mobile_03",
                    "hours_per_week": 20,
                },
            ),
            Action(
                name="search_employees",
                kwargs={"department": "QA", "utilization_below": 80},
            ),
            Action(
                name="calculate_employee_availability",
                kwargs={"employee_id": "emp_qa_02"},
            ),
            Action(
                name="calculate_employee_availability",
                kwargs={"employee_id": "emp_sec_test_01"},
            ),
            Action(
                name="create_allocation",
                kwargs={
                    "employee_id": "emp_qa_02",
                    "project_id": "proj_mobile_01",
                    "hours_per_week": 10,
                    "role": "QA Engineer",
                    "start_date": "2024-04-01",
                    "end_date": "2024-06-30",
                    "status": "active",
                },
            ),
            Action(
                name="update_employees_utilization",
                kwargs={
                    "employee_ids": ["emp_qa_02", "emp_dev_03"],
                },
            ),
            Action(
                name="summarize_project_phase_metrics",
                kwargs={"project_id": "proj_mobile_01"},
            ),
        ],
        outputs=['"dev_hours": 20', '"qa_hours": 10'],
    ),
    Task(
        annotator="0",
        user_id="implement_rotation_schedules_across_projects",
        instruction="""
        You are an operations manager. Create skill development rotation schedules between the employees from the
        projects: 'Banking Integration' and 'Customer Portal'. You should create a rotation schedule to the project
        'Banking Integration' for each employee of the project 'Customer Portal'. You should do the same with employees
        from the project 'Banking Integration' to the project 'Customer Portal'. The rotation date is "2024-12-23",
        the rotation hours should be 20, and you should set the 'holiday_coverage' parameter as false and skill
        development rotation as true. Output the employees in rotation.
        """,
        actions=[
            Action(name="search_projects", kwargs={"name": "Banking Integration"}),
            Action(name="search_projects", kwargs={"name": "Customer Portal"}),
            Action(
                name="get_project_allocations", kwargs={"project_id": "proj_banking_01"}
            ),
            Action(
                name="get_project_allocations", kwargs={"project_id": "proj_web_03"}
            ),
            Action(
                name="create_rotation_schedule",
                kwargs={
                    "employee_id": "emp_sec_dev_01",
                    "from_project": "proj_banking_01",
                    "to_project": "proj_web_03",
                    "rotation_date": "2024-12-23",
                    "hours_to_rotate": 20,
                    "skill_development_rotation": "true",
                    "holiday_coverage": "false",
                },
            ),
            Action(
                name="create_rotation_schedule",
                kwargs={
                    "employee_id": "emp_eng_20",
                    "from_project": "proj_web_03",
                    "to_project": "proj_banking_01",
                    "rotation_date": "2024-12-23",
                    "hours_to_rotate": 20,
                    "skill_development_rotation": "true",
                    "holiday_coverage": "false",
                },
            ),
        ],
        outputs=['"employees_in_rotation": ["emp_sec_dev_01", "emp_eng_20"]'],
    ),
    Task(
        annotator="0",
        user_id="balance_remote_onsite_allocation",
        instruction="""
        You are the hybrid work coordinator. The 'Enterprise Platform' project requires 40% onsite presence.
        Get the details for each employee in the project to calculate the total of hours allocated in the project by
        employees that can work onsite. If the currently total of hours doesn't match the required 40%,
        identify a team member who can work onsite from Engineering department, prioritize employees with lower capacity
        and have 'Mathematics' skill. Relocate the employee available hours to achieve the required onsite percentage.
        The allocations should have start_date 2024-02-01 and end_date 2024-12-31. Output the total onsite hours
        including old and new allocations.
        """,
        actions=[
            Action(name="search_projects", kwargs={"name": "Enterprise Platform"}),
            Action(
                name="get_project_details", kwargs={"project_id": "proj_enterprise_01"}
            ),
            Action(
                name="get_project_allocations",
                kwargs={"project_id": "proj_enterprise_01"},
            ),
            Action(
                name="get_employee_details", kwargs={"employee_id": "emp_devops_02"}
            ),
            Action(
                name="get_employee_details", kwargs={"employee_id": "emp_arch_01"}
            ),
            Action(
                name="search_employees",
                kwargs={"department": "Engineering", "skills": ["Mathematics"]},
            ),
            Action(
                name="create_allocation",
                kwargs={
                    "employee_id": "emp_dev_08",
                    "project_id": "proj_enterprise_01",
                    "hours_per_week": 8,
                    "role": "Backend Developer",
                    "start_date": "2024-02-01",
                    "end_date": "2024-12-31",
                    "status": "active",
                },
            ),
        ],
        outputs=['"onsite_hours": 64'],
    ),
    Task(
        annotator="0",
        user_id="optimize_docker_expertise",
        instruction="""
        You are the DevOps manager. The 'Platform Modernization' project urgently needs Docker expertise (proficiency 5).
        Find employees with Docker skill level 5, verify they have less than 80% utilization, and allocate 10 hours/week
        to the project. Return the final utilization percentage of the allocated employee. Consider the allocation
        with start_date 2024-03-01 and end_date 2024-10-31.""",
        actions=[
            Action(name="search_projects", kwargs={"name": "Platform Modernization"}),
            Action(
                name="search_employees",
                kwargs={
                    "skills": ["Docker"],
                    "min_proficiency": 5,
                    "utilization_below": 80,
                },
            ),
            Action(
                name="get_employee_allocations", kwargs={"employee_id": "emp_devops_04"}
            ),
            Action(
                name="calculate_employee_availability",
                kwargs={"employee_id": "emp_devops_04"},
            ),
            Action(
                name="create_allocation",
                kwargs={
                    "employee_id": "emp_devops_04",
                    "project_id": "proj_platform_02",
                    "hours_per_week": 10,
                    "role": "DevOps Engineer",
                    "start_date": "2024-03-01",
                    "end_date": "2024-10-31",
                    "status": "active",
                },
            ),
            Action(
                name="calculate_employee_utilization",
                kwargs={"employee_id": "emp_devops_04"},
            ),
        ],
        outputs=["85"],
    ),
    Task(
        annotator="0",
        user_id="create_security_taskforce",
        instruction="""
        You are the CISO. Create a security task force for the 'Security Patch' project. Find 2 developers and 1
        tester with security clearance, calculate their availability, and create a team called 'Security Task Force',
        allocate 10 hours of each to the project. Prioritize employees with utilization at 0%.
        Output the quantity cleared resources are now on the project.
        """,
        actions=[
            Action(name="search_projects", kwargs={"name": "Security Patch"}),
            Action(name="get_project_allocations", kwargs={"project_id": "proj_security_patch"}),
            Action(
                name="search_employees",
                kwargs={"clearance": "secret", "role_contains": "Developer"},
            ),
            Action(
                name="search_employees",
                kwargs={"clearance": "secret", "role_contains": "Tester"},
            ),
            Action(
                name="calculate_employee_availability",
                kwargs={"employee_id": "emp_sec_dev_03"},
            ),
            Action(
                name="calculate_employee_availability",
                kwargs={"employee_id": "emp_sec_dev_XX"},
            ),
            Action(
                name="calculate_employee_availability",
                kwargs={"employee_id": "emp_sec_test_01"},
            ),
            Action(
                name="create_team",
                kwargs={
                    "team_name": "Security Task Force",
                    "project_id": "proj_security_patch",
                    "team_members": [
                        "emp_sec_dev_03",
                        "emp_sec_dev_XX",
                        "emp_sec_test_01",
                    ],
                },
            ),
            Action(
                name="create_allocation",
                kwargs={
                    "employee_id": "emp_sec_test_01",
                    "project_id": "proj_security_patch",
                    "hours_per_week": 10,
                    "role": "Security Tester",
                    "status": "active",
                },
            ),
            Action(
                name="create_allocation",
                kwargs={
                    "employee_id": "emp_sec_dev_XX",
                    "project_id": "proj_security_patch",
                    "hours_per_week": 10,
                    "role": "Security Developer",
                    "status": "active",
                },
            ),
            Action(
                name="create_allocation",
                kwargs={
                    "employee_id": "emp_sec_dev_03",
                    "project_id": "proj_security_patch",
                    "hours_per_week": 10,
                    "role": "Security Developer",
                    "status": "active",
                },
            ),
            Action(
                name="validate_compliance_status",
                kwargs={
                    "project_id": "proj_security_patch",
                    "required_clearance": "secret",
                },
            ),
        ],
        outputs=["3"],
    ),
    Task(
        annotator="0",
        user_id="create_project_and_team_analytics",
        instruction="""
        You are a tech lead. First, you should create a new project called "Analytics Project". For this project, you
        must create a team called 'Analytics Team' with employees from the department
        Analytics. The team should have at least 24 hours available across employees.
        Prioritize employees with the skills: 'Python' and 'SQL', and disregard Junior employees.
        The employees added to the team should have current utilization below 90. Allocate 8 hours of each team member
        to the project. At the end, output if the
        project and team was created with success, and include the employees added to the team in the output.
        """,
        actions=[
            Action(
                name="create_project",
                kwargs={
                    "department": "Analytics",
                    "project_id": "proj_analytics_01",
                    "project_name": "Analytics Project",
                    "required_hours_per_week": 24
                }),
            Action(
                name="search_employees",
                kwargs={"department": "Analytics", "utilization_below": 90, "role_disregard": "Junior"}
            ),
            Action(name="calculate_employee_utilization", kwargs={"employee_id": "emp_data_01"}),
            Action(name="calculate_employee_utilization", kwargs={"employee_id": "emp_data_02"}),
            Action(name="calculate_employee_utilization", kwargs={"employee_id": "emp_analyst_02"}),
            Action(
                name="create_allocation",
                kwargs={
                    "employee_id": "emp_data_01",
                    "project_id": "proj_analytics_01",
                    "hours_per_week": 8,
                    "role": "Senior Data Analyst",
                    "status": "active",
                },
            ),
            Action(
                name="create_allocation",
                kwargs={
                    "employee_id": "emp_data_02",
                    "project_id": "proj_analytics_01",
                    "hours_per_week": 8,
                    "role": "Data Engineer",
                    "status": "active",
                },
            ),
            Action(
                name="create_allocation",
                kwargs={
                    "employee_id": "emp_analyst_02",
                    "project_id": "proj_analytics_01",
                    "hours_per_week": 8,
                    "role": "Data Analyst",
                    "status": "active",
                },
            ),
            Action(
                name="create_team",
                kwargs={
                    "team_name": "Analytics Team",
                    "project_id": "proj_analytics_01",
                    "team_members": ["emp_data_01", "emp_data_02", "emp_analyst_02"],
                },
            ),
        ],
        outputs=[
            '"project_created": "Analytics Project"',
            '"team_created": "Analytics Team"',
            '"employees_added": "emp_data_01", "emp_data_02", "emp_analyst_02"'
        ],
    ),
    Task(
        annotator="0",
        user_id="integrate_contract_resources",
        instruction="""
        You are the staffing manager. The 'Web Platform Update' project needs additional frontend developers.
        Search for employees with React skill (proficiency 4+) and 70% or less utilization to be allocated to the project.
        Create a resource request with normal urgency for the 'Engineering' department
        and report how many hours are still needed. Output how many hours are still needed.
        """,
        actions=[
            Action(name="search_projects", kwargs={"name": "Web Platform Update"}),
            Action(name="get_project_details", kwargs={"project_id": "proj_web_02"}),
            Action(
                name="search_employees",
                kwargs={
                    "skills": ["React"],
                    "min_proficiency": 4,
                    "utilization_below": 70,
                },
            ),
            Action(
                name="create_resource_request",
                kwargs={
                    "project_id": "proj_web_02",
                    "skill_required": "React",
                    "hours_needed": 60,
                    "urgency": "normal",
                    "department": "Engineering",
                },
            ),
        ],
        outputs=["60"],
    ),
    Task(
        annotator="0",
        user_id="optimize_architect_time",
        instruction="""
        You are the Engineering Director. Senior Architect Michael Roberts is assigned to two projects.
        Compare the priority of both projects, and delete the allocation of the lower-priority project. Then, create
        an allocation for a junior employee who shares at least two skills with him.
        Make sure to use all available 40 hours from the junior employee in the allocation.
        Finally, report the percentage of efficiency gain as a result of this reassignment.
        """,
        actions=[
            Action(name="search_employees", kwargs={"name": "Michael Roberts"}),
            Action(
                name="get_employee_allocations", kwargs={"employee_id": "emp_arch_01"}
            ),
            Action(
                name="compare_project_priorities",
                kwargs={
                    "project_id_1": "proj_enterprise_01",
                    "project_id_2": "proj_platform_02",
                },
            ),
            Action(
                name="search_employees",
                kwargs={
                    "skills": ["System Design", "Cloud Architecture", "Microservices"],
                    "min_available_hours": 40,
                    "min_skill_matches": 2,
                    "role_contains": "Junior",
                },
            ),
            Action(
                name="get_employee_allocations", kwargs={"employee_id": "emp_jr_arch_01"}
            ),
            Action(
                name="calculate_employee_availability", kwargs={"employee_id": "emp_jr_arch_01"}
            ),
            Action(
                name="delete_allocation",
                kwargs={"allocation_id": "alloc_arch_02"}
            ),
            Action(
                name="create_allocation",
                kwargs={
                    "employee_id": "emp_jr_arch_01",
                    "project_id": "proj_platform_02",
                    "hours_per_week": 40,
                    "role": "Junior Architect",
                    "department": "Engineering",
                }
            ),
            Action(
                name="update_employees_utilization",
                kwargs={"employee_ids": ["emp_jr_arch_01", "emp_arch_01"]}
            ),
            Action(
                name="calculate_optimization_metrics",
                kwargs={
                    "projects": ["proj_enterprise_01", "proj_platform_02"],
                    "metric_type": "efficiency_gain",
                },
            ),
        ],
        outputs=["25"],
    ),
    Task(
        annotator="0",
        user_id="manage_budget_overrun",
        instruction="""
        You are the project controller. The 'Customer Portal' project is approaching budget limits. Review current
        allocations, find junior resources with proficiency 3+ and utilization at 80% or below. Calculate
        availability of
        the employees found and allocate their available hours to achieve the project's required hours. In the allocation,
        prioritize employees with lower utilization. Report the junior employees allocated final utilization percentage by employee ID.
        The new allocations should have start_date 2024-03-01 and end_date 2024-10-31.
        """,
        actions=[
            Action(name="search_projects", kwargs={"name": "Customer Portal"}),
            Action(
                name="get_project_allocations", kwargs={"project_id": "proj_web_03"}
            ),
            Action(
                name="get_project_details", kwargs={"project_id": "proj_web_03"}
            ),
            Action(
                name="search_employees",
                kwargs={
                    "role_contains": "Junior",
                    "min_proficiency": 3,
                    "utilization_below": 80,
                },
            ),
            Action(
                name="calculate_employee_availability",
                kwargs={"employee_id": "emp_jr_arch_01"},
            ),
            Action(
                name="calculate_employee_availability",
                kwargs={"employee_id": "emp_analyst_03"},
            ),
            Action(
                name="create_allocation",
                kwargs={
                    "employee_id": "emp_analyst_03",
                    "project_id": "proj_web_03",
                    "hours_per_week": 8,
                    "role": "Junior Analyst",
                    "start_date": "2024-03-01",
                    "end_date": "2024-10-31",
                    "status": "active",
                },
            ),
            Action(
                name="create_allocation",
                kwargs={
                    "employee_id": "emp_jr_arch_01",
                    "project_id": "proj_web_03",
                    "hours_per_week": 40,
                    "role": "Junior Architect",
                    "start_date": "2024-03-01",
                    "end_date": "2024-10-31",
                    "status": "active",
                },
            ),
            Action(
                name="update_employees_utilization",
                kwargs={"employee_ids": ["emp_analyst_03", "emp_jr_arch_01"]},
            ),
        ],
        outputs=['"emp_jr_arch_01": 100', '"emp_analyst_03": 80'],
    ),
    Task(
        annotator="0",
        user_id="expand_analytics_team",
        instruction="""
        You are the analytics manager. The 'Customer Insights' project needs to expand from 30 to 60 hours/week.
        Find two employees with Python expertise with utilization between [49%, 61%], allocate 15 hours each to the project.
        Create allocations with start_date 2024-02-01 and end_date 2024-08-31, also, choose the first two employees that
        appear in the result. Report the total project hours after expansion. Note that the project requires 80 hours/week,
        but for now, you are trying to allocate 30 hours in the project.
        """,
        actions=[
            Action(name="search_projects", kwargs={"name": "Customer Insights"}),
            Action(
                name="get_project_allocations",
                kwargs={"project_id": "proj_insights_01"},
            ),
            Action(
                name="search_employees",
                kwargs={"skills": ["Python"], "utilization_below": 61, "utilization_above": 49},
            ),
            Action(
                name="calculate_employee_availability",
                kwargs={"employee_id": "emp_qa_02"},
            ),
            Action(
                name="create_allocation",
                kwargs={
                    "employee_id": "emp_qa_02",
                    "project_id": "proj_insights_01",
                    "hours_per_week": 15,
                    "role": "QA Engineer",
                    "start_date": "2024-02-01",
                    "end_date": "2024-08-31",
                    "status": "active",
                    "cross_department": True,
                },
            ),
            Action(
                name="calculate_employee_availability",
                kwargs={"employee_id": "emp_analyst_03"},
            ),
            Action(
                name="create_allocation",
                kwargs={
                    "employee_id": "emp_analyst_03",
                    "project_id": "proj_insights_01",
                    "hours_per_week": 15,
                    "role": "Junior Analyst",
                    "start_date": "2024-02-01",
                    "end_date": "2024-08-31",
                    "status": "active",
                },
            ),
            Action(
                name="summarize_team_expansion",
                kwargs={
                    "project_id": "proj_insights_01",
                    "new_team_members": ["emp_qa_02", "emp_analyst_03"],
                    "additional_hours": 30,
                    "existing_hours": 30,
                },
            ),
        ],
        outputs=["60"],
    ),
    Task(
        annotator="0",
        user_id="consolidate_web_projects",
        instruction="""
        You are a portfolio director. Three web projects (Web Portal Redesign, Web Platform Update, and Customer
        Portal) have overlapping objectives. Analyze their allocations, priorities, and resources. Consolidate them
        into the highest priority project and update project statuses. Finally, summarize projects consolidation, set the
        highest priority project as the 'consolidate to' and the other two projects as the 'consolidated projects. Output
        'consolidate to' project, the team size and the total hours.
        """,
        actions=[
            Action(name="search_projects", kwargs={"name": "Web Portal Redesign"}),
            Action(name="search_projects", kwargs={"name": "Web Platform Update"}),
            Action(name="search_projects", kwargs={"name": "Customer Portal"}),
            Action(name="get_project_details", kwargs={"project_id": "proj_web_01"}),
            Action(name="get_project_details", kwargs={"project_id": "proj_web_02"}),
            Action(name="get_project_details", kwargs={"project_id": "proj_web_03"}),
            Action(
                name="compare_project_priorities",
                kwargs={"project_id_1": "proj_web_01", "project_id_2": "proj_web_02"},
            ),
            Action(
                name="compare_project_priorities",
                kwargs={"project_id_1": "proj_web_03", "project_id_2": "proj_web_01"},
            ),
            Action(
                name="get_project_allocations", kwargs={"project_id": "proj_web_03"}
            ),
            Action(
                name="get_project_allocations", kwargs={"project_id": "proj_web_02"}
            ),
            Action(
                name="get_project_allocations", kwargs={"project_id": "proj_web_01"}
            ),
            Action(
                name="create_allocation",
                kwargs={
                    "employee_id": "emp_dev_05",
                    "project_id": "proj_web_03",
                    "hours_per_week": 25,
                    "role": "Full Stack Developer",
                    "status": "active",
                },
            ),
            Action(
                name="delete_allocation",
                kwargs={"allocation_id": "alloc_web_01"},
            ),
            Action(
                name="update_project_status",
                kwargs={"project_id": "proj_web_01", "status": "cancelled"},
            ),
            Action(
                name="update_project_status",
                kwargs={"project_id": "proj_web_02", "status": "cancelled"},
            ),
            Action(
                name="summarize_project_consolidation",
                kwargs={
                    "consolidated_to": "proj_web_03",
                    "total_hours": 57,
                    "team_size": 2,
                    "consolidated_projects": ["proj_web_01", "proj_web_02"],
                },
            ),
        ],
        outputs=[
            '"consolidated_to": "proj_web_03"',
            '"total_hours": 57',
            '"team_size": 2',
        ],
    ),
    Task(
        annotator="0",
        user_id="transition_to_testing_phase",
        instruction="""
        You are the  transition manager. The 'Mobile App Launch' project is moving from the development to testing phase.
        Calculate the current dev/QA hours split, reduce developer allocations by 50%, find 2 QA employees
        with 75% utilization or less and allocate 12 hours each to the project. Create allocations
        with start_date 2024-01-15 and end_date 2024-06-30. Report the new dev and QA hours.
        """,
        actions=[
            Action(name="search_projects", kwargs={"name": "Mobile App Launch"}),
            Action(
                name="get_project_allocations", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(name="get_employee_details", kwargs={"employee_id": "emp_dev_03"}),
            Action(
                name="update_allocation",
                kwargs={
                    "allocation_id": "alloc_mobile_03",
                    "hours_per_week": 15,
                },
            ),
            Action(
                name="search_employees",
                kwargs={"department": "QA", "utilization_below": 75},
            ),
            Action(
                name="calculate_employee_availability",
                kwargs={"employee_id": "emp_qa_02"},
            ),
            Action(
                name="calculate_employee_availability",
                kwargs={"employee_id": "emp_sec_test_01"},
            ),
            Action(
                name="create_allocation",
                kwargs={
                    "employee_id": "emp_qa_02",
                    "project_id": "proj_mobile_01",
                    "hours_per_week": 12,
                    "role": "QA Engineer",
                    "start_date": "2024-01-15",
                    "end_date": "2024-06-30",
                    "status": "active",
                },
            ),
            Action(
                name="create_allocation",
                kwargs={
                    "employee_id": "emp_sec_test_01",
                    "project_id": "proj_mobile_01",
                    "hours_per_week": 12,
                    "role": "Security Tester",
                    "start_date": "2024-01-15",
                    "end_date": "2024-06-30",
                    "status": "active",
                },
            ),
            Action(
                name="update_employees_utilization",
                kwargs={
                    "employee_ids": ["emp_qa_02", "emp_sec_test_01", "emp_dev_03"],
                },
            ),
            Action(
                name="summarize_project_phase_metrics",
                kwargs={"project_id": "proj_mobile_01"},
            ),
        ],
        outputs=['"dev_hours": 15', '"qa_hours": 24'],
    ),
    Task(
        annotator="0",
        user_id="fill_ml_expertise_gap",
        instruction="""
        You are a skills director. The 'AI Platform' project has a critical Machine Learning skill gap. Search for new employees
        (excluding already-allocated employees) with ML skills at any proficiency and add them to the project. If none
        employee were found in the first search, search for employees with Python expertise (proficiency >= 4) and
        utilization at 90% or less as alternatives. Get the first two employees that appeared in the second search, and allocate
        them in the project. The allocation hours should be the employees available hours, you can calculate it by subtracting the
        maximum hours per week by the product between maximum hours per week and utilization percentage.
        Generate a urgent resource request to cover the amount of hours needed to fulfill the project required hours,
        considering project final allocation status, for employees with expertize in 'Machine Learning' from the 'Engineering'
        department. Output the hours needed to achieve the project's required hours.
        """,
        actions=[
            Action(name="search_projects", kwargs={"name": "AI Platform"}),
            Action(name="get_project_details", kwargs={"project_id": "proj_ai_01"}),
            Action(name="get_project_allocations", kwargs={"project_id": "proj_ai_01"}),
            Action(
                name="search_employees",
                kwargs={"skills": ["Machine Learning"], "disregard_employee_ids": ["emp_data_01"]}
            ),
            Action(
                name="search_employees",
                kwargs={
                    "skills": ["Python"],
                    "min_proficiency": 4,
                    "utilization_below": 90,
                    "disregard_employee_ids": ["emp_data_01"]
                },
            ),
            Action(
                name="create_allocation",
                kwargs={
                    "employee_id": "emp_data_02",
                    "project_id": "proj_ai_01",
                    "hours_per_week": 14,
                    "role": "Data Engineer",
                    "status": "active",
                },
            ),
            Action(
                name="create_allocation",
                kwargs={
                    "employee_id": "emp_dev_07",
                    "project_id": "proj_ai_01",
                    "hours_per_week": 12,
                    "role": "Backend Developer",
                    "status": "active",
                },
            ),
            Action(name="get_project_details", kwargs={"project_id": "proj_ai_01"}),
            Action(
                name="create_resource_request",
                kwargs={
                    "project_id": "proj_ai_01",
                    "skill_required": "Machine Learning",
                    "hours_needed": 62,
                    "urgency": "urgent",
                    "department": "Engineering",
                },
            ),
        ],
        outputs=['"hours_needed": 62'],
    ),
    Task(
        annotator="0",
        user_id="balance_onsite_remote",
        instruction="""
        You are a work coordinator. The 'Enterprise Platform' needs more onsite presence. Analyze current project allocations,
        find one new employee who can work on site to allocate 30 hours to the project. Choose the first employee that appears
        in the search results. Create an allocation with start_date 2024-02-01 and end_date 2024-12-31. Output the chosen
        employees' name.
        """,
        actions=[
            Action(name="search_projects", kwargs={"name": "Enterprise Platform"}),
            Action(
                name="get_project_allocations",
                kwargs={"project_id": "proj_enterprise_01"},
            ),
            Action(
                name="get_project_details",
                kwargs={"project_id": "proj_enterprise_01"},
            ),
            Action(
                name="search_employees",
                kwargs={
                    "disregard_employee_ids": ["emp_devops_02",  "emp_arch_01"],
                    "min_available_hours": 30
                },
            ),
            Action(
                name="calculate_employee_availability",
                kwargs={"employee_id": "emp_ux_03"},
            ),
            Action(
                name="create_allocation",
                kwargs={
                    "employee_id": "emp_ux_03",
                    "project_id": "proj_enterprise_01",
                    "hours_per_week": 30,
                    "role": "UX Designer",
                    "start_date": "2024-02-01",
                    "end_date": "2024-12-31",
                    "status": "active",
                },
            ),
            Action(
                name="update_utilization_log",
                kwargs={
                    "employee_id":  "emp_ux_03",
                    "new_utilization": 75,
                },
            ),
        ],
        outputs=['"employee_name": "Lisa Chang"'],
    ),
    Task(
        annotator="0",
        user_id="rebalance_overloaded_teams",
        instruction="""
        You are the workload manager. Analytics team members are severely imbalanced - some at 95% utilization,
        others at 60%. Analyze all team member allocations, identify the most overloaded employee, and the most
        underutilized employee. Analysing overloaded employee allocations, choose the allocation with less hours and
        delete it. Then create an allocation for the most underutilized employee for the project specified in the allocation
        excluded in the previous step. Also, use the same same start and end date as the excluded allocation.
        Finally, update employees' utilization and output the increase/decrease of hours by employee ID.
        """,
        actions=[
            Action(name="get_team_details", kwargs={"team_name": "Analytics Team"}),
            Action(
                name="get_employee_allocations",
                kwargs={"employee_id": "emp_analyst_01"},
            ),
            Action(
                name="get_employee_allocations",
                kwargs={"employee_id": "emp_analyst_02"},
            ),
            Action(
                name="get_employee_allocations",
                kwargs={"employee_id": "emp_analyst_03"},
            ),
            Action(
                name="delete_allocation",
                kwargs={"allocation_id": "alloc_insights_02"},
            ),
            Action(
                name="create_allocation",
                kwargs={
                    "employee_id": "emp_analyst_03",
                    "project_id": "proj_insights_01",
                    "hours_per_week": 8,
                    "role": "Junior Analyst",
                    "start_date": "2024-02-01",
                    "end_date": "2024-08-31",
                    "status": "active",
                },
            ),
            Action(
                name="update_utilization_log",
                kwargs={
                    "employee_id": "emp_analyst_01",
                    "new_utilization": 75,
                },
            ),
            Action(
                name="update_utilization_log",
                kwargs={
                    "employee_id": "emp_analyst_03",
                    "new_utilization": 80,
                },
            ),
        ],
        outputs=['"emp_analyst_03": 8', '"emp_analyst_01": -8'],
    ),
    Task(
        annotator="0",
        user_id="handle_enterprise_cancellation",
        instruction="""
        You are the crisis manager. The 'Enterprise Platform' project was suddenly cancelled.
        Find all employees who are currently allocated to this project, and allocate 20 hours of each in the
        project AI Platform (use the ID proj_ai_01). Before creating the new allocations,
        delete the allocations from the cancelled project. Make sure the project 'Enterprise Platform' is marked as cancelled.
        Finally, output the quantity of resources relocated.
        The new allocations should use start_date 2024-08-01 and end_date 2024-12-31.
        """,
        actions=[
            Action(name="search_projects", kwargs={"name": "Enterprise Platform"}),
            Action(
                name="get_project_allocations",
                kwargs={"project_id": "proj_enterprise_01"},
            ),
            Action(
                name="update_project_status",
                kwargs={"project_id": "proj_enterprise_01", "status": "cancelled"},
            ),
            Action(
                name="delete_allocation",
                kwargs={"allocation_id": "alloc_arch_01"},
            ),
            Action(
                name="delete_allocation", kwargs={"allocation_id": "alloc_devops_01"}
            ),
            Action(
                name="create_allocation",
                kwargs={
                    "employee_id": "emp_arch_01",
                    "project_id": "proj_ai_01",
                    "hours_per_week": 20,
                    "role": "Senior Architect",
                    "start_date": "2024-08-01",
                    "end_date": "2024-12-31",
                    "status": "active",
                },
            ),
            Action(
                name="create_allocation",
                kwargs={
                    "employee_id": "emp_devops_02",
                    "project_id": "proj_ai_01",
                    "hours_per_week": 20,
                    "role": "DevOps Engineer",
                    "start_date": "2024-08-01",
                    "end_date": "2024-12-31",
                    "status": "active",
                },
            ),
        ],
        outputs=[
            '"relocated_resources_quantity": 2'
        ],
    ),
    Task(
        annotator="0",
        user_id="ensure_banking_compliance",
        instruction="""
        You are the compliance officer. New regulations require ALL banking project staff to have secret clearance.
        Audit the 'Banking Integration' project, if the project is non-compliant, remove all allocations in the project
        which have employees without secret clearance. In that case, also create a resource conflict with 'clearance_violation'
        type. Output if the project is non-compliant.
        """,
        actions=[
            Action(name="search_projects", kwargs={"name": "Banking Integration"}),
            Action(
                name="validate_compliance_status",
                kwargs={
                    "project_id": "proj_banking_01",
                    "required_clearance": "secret",
                },
            ),
            Action(
                name="get_project_allocations", kwargs={"project_id": "proj_banking_01"}
            ),
            Action(
                name="get_employee_details", kwargs={"employee_id": "emp_sec_dev_01"}
            ),
            Action(
                name="create_resource_conflict",
                kwargs={
                    "employee_id": "emp_sec_dev_01",
                    "competing_projects": ["proj_banking_01"],
                    "conflict_type": "clearance_violation",
                },
            ),
            Action(
                name="delete_allocation",
                kwargs={"allocation_id": "alloc_bank_01"},
            ),
            Action(
                name="update_employees_utilization",
                kwargs={
                    "employee_ids": ["emp_sec_dev_01"],
                },
            ),
        ],
        outputs=['"non_compliant": true'],
    ),
    Task(
        annotator="0",
        user_id="optimize_portfolio_efficiency",
        instruction="""
        You are in charge of portfolio optimization. Verify if any of the following projects have critical priority and
        need resources: Mobile App Launch, AI Platform, Cloud Migration,
        Platform Modernization, and Banking Integration. For the projects that matches this criteria, calculate
        availability for each employees currently allocated in each project and update their allocations to 40 hours.
        If the project doesn't have employees allocated, ignore it. Finally, output the projects modified with the
        total of hours added in each project.
        """,
        actions=[
            Action(name="search_projects", kwargs={"name": "Mobile App Launch"}),
            Action(name="search_projects", kwargs={"name": "AI Platform"}),
            Action(name="search_projects", kwargs={"name": "Cloud Migration"}),
            Action(name="search_projects", kwargs={"name": "Platform Modernization"}),
            Action(name="search_projects", kwargs={"name": "Banking Integration"}),
            Action(name="get_project_allocations", kwargs={"project_id": "proj_mobile_01"}),
            Action(name="calculate_employee_availability", kwargs={"employee_id": "emp_dev_03"}),
            Action(name="update_allocation", kwargs={"allocation_id": "alloc_mobile_03", "hours_per_week": 40}),
            Action(name="get_project_allocations", kwargs={"project_id": "proj_ai_01"}),
            Action(name="calculate_employee_availability", kwargs={"employee_id": "emp_data_01"}),
            Action(name="update_allocation", kwargs={"allocation_id": "alloc_data_01", "hours_per_week": 40}),
            Action(name="get_project_allocations", kwargs={"project_id": "proj_cloud_01"}),
        ],
        outputs=['"proj_mobile_01": 10', '"proj_ai_01": 8'],
    ),
    Task(
        annotator="0",
        user_id="handle_security_breach",
        instruction="""
        You are an incident response manager. A security breach requires immediate action. Search for two employees
        with secret clearance to work on the project 'Security Patch'. Prioritize employees with the skill 'Penetration
        Testing'. Calculate the availability for the chosen employees and allocate the resulted availability to the
        project. Create a team with all project employees called 'Emergency Security Response Team'.
        """,
        actions=[
            Action(
                name="search_employees",
                kwargs={"clearance": "secret", "skills": "Penetration Testing"},
            ),
            Action(
                name="calculate_employee_availability", kwargs={"employee_id": "emp_sec_dev_03"}
            ),
            Action(
                name="calculate_employee_availability", kwargs={"employee_id": "emp_sec_dev_02"}
            ),
            Action(
                name="search_projects", kwargs={"name": "Security Patch"}
            ),
            Action(
                name="get_project_allocations", kwargs={"project_id": "proj_security_patch"}
            ),
            Action(
                name="create_allocation",
                kwargs={
                    "employee_id": "emp_sec_dev_02",
                    "project_id": "proj_security_patch",
                    "hours_per_week": 10,
                    "role": "Security Developer",
                },
            ),
            Action(
                name="create_allocation",
                kwargs={
                    "employee_id": "emp_sec_dev_03",
                    "project_id": "proj_security_patch",
                    "hours_per_week": 40,
                    "role": "Security Developer",
                },
            ),
            Action(
                name="create_team",
                kwargs={
                    "team_name": "Emergency Security Response Team",
                    "project_id": "proj_security_patch",
                    "team_members": [
                        "emp_sec_dev_03",
                        "emp_sec_dev_02",
                    ],
                },
            ),
            Action(
                name="update_employees_utilization",
                kwargs={"employee_ids": ["emp_sec_dev_03", "emp_sec_dev_02"]},
            ),
        ],
        outputs=[
            '"new_team_members": ["emp_sec_dev_03", "emp_sec_dev_02"]'
        ],
    ),
    Task(
        annotator="0",
        user_id="activate_bench_resources",
        instruction="""
        You are the lead for resource optimization. Multiple employees are finishing projects.
        Search the allocations with end date before 2024-07-20. Get all the employees in the result, calculated their
        availabilities and allocate all available hours of them in the project
        Compliance Audit System. Output the relocated hours by employee.
        Note: The allocation search only includes projects that ended before 2024-07-20. As a result, employee
        availability may appear higher than the total allocation hours shown, since availability is calculated over
        the entire time horizon, while the allocation search is limited to a specific period.
        """,
        actions=[
            Action(
                name="search_allocations",
                kwargs={"end_date_before": "2024-07-20", "status": "active"},
            ),
            Action(name="calculate_employee_availability", kwargs={"employee_id": "emp_dev_05"}),
            Action(name="calculate_employee_availability", kwargs={"employee_id": "emp_sec_test_01"}),
            Action(name="calculate_employee_availability", kwargs={"employee_id": "emp_analyst_01"}),
            Action(name="calculate_employee_availability", kwargs={"employee_id": "emp_analyst_02"}),
            Action(name="calculate_employee_availability", kwargs={"employee_id": "emp_dev_15"}),
            Action(name="calculate_employee_availability", kwargs={"employee_id": "emp_dev_03"}),
            Action(name="search_projects", kwargs={"name": "Compliance Audit System"}),
            Action(
                name="create_allocation",
                kwargs={
                    "employee_id": "emp_sec_test_01",
                    "project_id": "proj_audit_01",
                    "hours_per_week": 12,
                    "role": "Security Tester",
                },
            ),
            Action(
                name="create_allocation",
                kwargs={
                    "employee_id": "emp_analyst_01",
                    "project_id": "proj_audit_01",
                    "hours_per_week": 2,
                    "role": "Business Analyst",
                },
            ),
            Action(
                name="create_allocation",
                kwargs={
                    "employee_id": "emp_analyst_02",
                    "project_id": "proj_audit_01",
                    "hours_per_week": 8,
                    "role": "Data Analyst",
                },
            ),
            Action(
                name="create_allocation",
                kwargs={
                    "employee_id": "emp_dev_03",
                    "project_id": "proj_audit_01",
                    "hours_per_week": 10,
                    "role": "React Native Developer",
                },
            ),
            Action(
                name="update_employees_utilization",
                kwargs={
                    "employee_ids": ["emp_dev_03", "emp_analyst_02", "emp_analyst_01", "emp_sec_test_01"],
                },
            ),
        ],
        outputs=['"emp_dev_03": 10', '"emp_analyst_02": 8', '"emp_analyst_01": 2', '"emp_sec_test_01": 12'],
    ),
]
