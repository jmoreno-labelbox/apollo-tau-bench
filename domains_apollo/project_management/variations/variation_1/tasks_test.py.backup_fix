from tau_bench.types import Action, Task

TASKS = [
    Task(
        annotator="0",
        user_id="resolve_resource_overallocation",
        instruction="""
        As a resource manager, you need to address the situation where your developer Olivia Anderson is over-allocated at 120% capacity. Examine her present assignments, pinpoint the project with lower priority, and decrease its allocation to achieve a 100% utilization rate. Present the final weekly hours and percentage of employee utilization.
        """,
        actions=[
            Action(name="SearchEmployees", kwargs={"name": "Olivia Anderson"}),
            Action(
                name="GetEmployeeAllocations", kwargs={"employee_id": "emp_dev_05"}
            ),
            Action(name="GetProjectDetails", kwargs={"project_id": "proj_web_01"}),
            Action(name="GetProjectDetails", kwargs={"project_id": "proj_api_02"}),
            Action(
                name="CompareProjectPriorities",
                kwargs={"project_id_1": "proj_web_01", "project_id_2": "proj_api_02"},
            ),
            Action(
                name="UpdateAllocation",
                kwargs={"allocation_id": "alloc_web_01", "hours_per_week": 17},
            ),
            Action(
                name="CalculateEmployeeUtilization",
                kwargs={"employee_id": "emp_dev_05"},
            ),
            Action(
                name="UpdateUtilizationLog",
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
        instruction="""The Engineering department has sent you an urgent request for a "Kubernetes Expert" to work on the 'Cloud Migration' project. Search for employees within the Engineering department who possess this skill, and if more than one is found, opt for the employee with the least utilization. Determine this employee's available hours and assign them to the 'Cloud Migration' project. Ensure the allocation begins on 2024-03-01 and ends on 2024-12-31. Update the department's capacity and provide the employee ID along with the hours allocated to the 'Cloud Migration' project.""",
        actions=[
            Action(name="SearchProjects", kwargs={"name": "Cloud Migration"}),
            Action(
                name="SearchEmployees",
                kwargs={"skills": ["Kubernetes"], "department": "Engineering"},
            ),
            Action(
                name="CalculateEmployeeAvailability",
                kwargs={"employee_id": "emp_devops_04"},
            ),
            Action(
                name="CreateAllocation",
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
                name="UpdateUtilizationLog",
                kwargs={
                    "employee_id": "emp_devops_04",
                    "new_utilization": 100,
                },
            ),
            Action(
                name="UpdateDepartmentCapacity",
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
        As the operations director, you are tasked to assist the Engineering team in their need for a UX designer from the Design department for the 'Product Redesign' project. Look for UX designers whose utilization in the 'Design' department is below 80%. Assign 20 hours of the employee with the least utilization from your findings to the 'Product Redesign' project. The allocation should commence on "2024-02-15" and conclude on "2024-07-31". Keep in mind that this allocation involves multiple departments, and record the allocated hours.
        """,
        actions=[
            Action(name="SearchProjects", kwargs={"name": "Product Redesign"}),
            Action(
                name="SearchEmployees",
                kwargs={"department": "Design", "role": "UX Designer", "utilization_below": 80},
            ),
            Action(
                name="CalculateEmployeeAvailability",
                kwargs={"employee_id": "emp_ux_03"},
            ),
            Action(
                name="CreateAllocation",
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
                name="UpdateUtilizationLog",
                kwargs={
                    "employee_id": "emp_ux_03",
                    "new_utilization": 50,
                },
            ),
            Action(
                name="UpdateDepartmentCapacity",
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
        instruction="""As the resource planning manager, your role is to address the uneven utilization within the Analytics Team. Evaluate each team member's workload, pinpoint those who are overutilized and those who are underutilized, then adjust the assignments by reallocating 10 hours from the member with the heaviest workload to the one with the lightest. Set up the revised allocation for the Analytics Reporting project (proj_reporting_01) to begin on 2024-01-15 and end on 2024-06-30.""",
        actions=[
            Action(name="GetTeamDetails", kwargs={"team_name": "Analytics Team"}),
            Action(
                name="GetEmployeeAllocations",
                kwargs={"employee_id": "emp_analyst_01"},
            ),
            Action(
                name="GetEmployeeAllocations",
                kwargs={"employee_id": "emp_analyst_02"},
            ),
            Action(
                name="GetEmployeeAllocations",
                kwargs={"employee_id": "emp_analyst_03"},
            ),
            Action(
                name="UpdateAllocation",
                kwargs={"allocation_id": "alloc_report_01", "hours_per_week": 20},
            ),
            Action(
                name="CreateAllocation",
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
                name="UpdateUtilizationLog",
                kwargs={
                    "employee_id": "emp_analyst_01",
                    "new_utilization": 70,
                },
            ),
            Action(
                name="UpdateUtilizationLog",
                kwargs={
                    "employee_id": "emp_analyst_03",
                    "new_utilization": 85,
                },
            ),
            Action(
                name="SummarizeWorkloadRebalance",
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
        As an emergency response manager, a crucial 'Security Patch' project requires urgent staffing.
        Locate developers with secret-level security clearance who can commit available hours to cover all necessary
        project hours. Focus on assigning employees with lower utilization to contribute hours to the project.
        All assignments should commence on 2024-03-15 and conclude on 2024-04-30. Present the employees assigned to the
        'Security Patch' in this operation and the total hours.
        """,
        actions=[
            Action(name="SearchProjects", kwargs={"name": "Security Patch"}),
            Action(name="GetProjectAllocations", kwargs={"project_id": "proj_security_patch"}),
            Action(
                name="SearchEmployees",
                kwargs={"clearance": "secret", "role_contains": "Developer"},
            ),
            Action(
                name="CalculateEmployeeAvailability",
                kwargs={"employee_id": "emp_sec_dev_02"},
            ),
            Action(
                name="CalculateEmployeeAvailability",
                kwargs={"employee_id": "emp_sec_dev_03"},
            ),
            Action(
                name="CalculateEmployeeAvailability",
                kwargs={"employee_id": "emp_sec_dev_XX"},
            ),
            Action(
                name="CreateAllocation",
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
                name="CreateAllocation",
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
            Action(name="UpdateEmployeesUtilization", kwargs={"employee_ids": ["emp_sec_dev_03", "emp_sec_dev_XX"]}),
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
        As the crisis manager, the 'proj_client_01' project has been terminated. Label this project as 'cancelled' and
        transfer all developers from the cancelled project to 'proj_enterprise_01',
        allocating any remaining employees to 'proj_mobile_01'. Ensure that the utilization rates for
        all moved employees remain constant. Display the employees transferred by destination project.
        """,
        actions=[
            Action(
                name="GetProjectAllocations", kwargs={"project_id": "proj_client_01"}
            ),
            Action(
                name="UpdateProjectStatus",
                kwargs={"project_id": "proj_client_01", "status": "cancelled"},
            ),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "emp_dev_20"}),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "emp_dev_21"}),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "emp_test_05"}),
            Action(
                name="CreateAllocation",
                kwargs={
                    "employee_id": "emp_dev_20",
                    "project_id": "proj_enterprise_01",
                    "hours_per_week": 40,
                    "role": "Frontend Developer",
                    "status": "active",
                },
            ),
            Action(
                name="CreateAllocation",
                kwargs={
                    "employee_id": "emp_dev_21",
                    "project_id": "proj_enterprise_01",
                    "hours_per_week": 40,
                    "role": "Backend Developer",
                    "status": "active",
                },
            ),
            Action(
                name="CreateAllocation",
                kwargs={
                    "employee_id": "emp_test_05",
                    "project_id": "proj_mobile_01",
                    "hours_per_week": 40,
                    "role": "Test Engineer",
                    "status": "active",
                },
            ),
            Action(
                name="DeleteAllocation", kwargs={"allocation_id": "alloc_client_01"}
            ),
            Action(
                name="DeleteAllocation", kwargs={"allocation_id": "alloc_client_02"}
            ),
            Action(
                name="DeleteAllocation", kwargs={"allocation_id": "alloc_client_03"}
            ),
        ],
        outputs=['"proj_mobile_01_allocation": ["emp_dev_20", "emp_dev_21"]', '"proj_mobile_01_allocation": ["emp_test_05"]'],
    ),
    Task(
        annotator="0",
        user_id="manage_bench_resources",
        instruction="""
        As the resource manager, you are tasked with closing projects due to finish this week.
        Identify employees with active allocations that end on 2024-06-01 or earlier. Gather each employee's details,
        and assign them to a bench assignment starting on 2024-06-01 with immediate availability.
        Update each employee's status and utilization accordingly. Indicate whether a bench assignment was created.
        """,
        actions=[
            Action(
                name="SearchAllocations",
                kwargs={"end_date_before": "2024-06-01", "status": "active"},
            ),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "emp_dev_05"}),
            Action(
                name="CreateBenchAssignment",
                kwargs={
                    "employee_id": "emp_dev_05",
                    "start_date": "2024-06-01",
                    "skills": ["JavaScript", "Python", "React"],
                    "availability": "immediate",
                },
            ),
            Action(
                name="UpdateEmployeeStatus",
                kwargs={
                    "employee_id": "emp_dev_05",
                    "status": "bench",
                    "available_from": "2024-06-01",
                },
            ),
            Action(
                name="UpdateUtilizationLog",
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
        As the Team Lead, your team (team_analytics_01) has been working on the same project for an extended period and needs
        rotation for skill growth. Locate team members who have been on projects for over 550 days,
        and arrange rotation schedules (date=2024-04-01) for these individuals to the project 'proj_beta_02'. Ensure
        the rotation hours align with the employees' utilization in their prior project, and set skill
        development rotation to true while marking holiday coverage as false. Display the
        employees who were given rotation schedules.
        """,
        actions=[
            Action(name="GetTeamDetails", kwargs={"team_id": "team_analytics_01"}),
            Action(
                name="GetEmployeeAllocations",
                kwargs={"employee_id": "emp_analyst_01"},
            ),
            Action(
                name="CheckAllocationDuration",
                kwargs={
                    "employee_id": "emp_analyst_01",
                    "project_id": "proj_reporting_01",
                },
            ),
            Action(
                name="CheckAllocationDuration",
                kwargs={
                    "employee_id": "emp_analyst_01",
                    "project_id": "proj_insights_01",
                },
            ),
            Action(
                name="GetEmployeeAllocations",
                kwargs={"employee_id": "emp_analyst_02"},
            ),
            Action(
                name="CheckAllocationDuration",
                kwargs={
                    "employee_id": "emp_analyst_02",
                    "project_id": "proj_reporting_01",
                },
            ),
            Action(
                name="CheckAllocationDuration",
                kwargs={
                    "employee_id": "emp_analyst_02",
                    "project_id": "proj_insights_01",
                },
            ),
            Action(
                name="GetEmployeeAllocations",
                kwargs={"employee_id": "emp_analyst_03"},
            ),
            Action(
                name="CheckAllocationDuration",
                kwargs={
                    "employee_id": "emp_analyst_03",
                    "project_id": "proj_gamma_03",
                },
            ),
            Action(
                name="CreateRotationSchedule",
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
                name="CreateRotationSchedule",
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
        As the resource manager, focus on optimizing the utilization of resources across various projects. Identify senior resources
        whose utilization is below 90% and allocate all available hours following this guideline: developers should
        be assigned to the project 'proj_security_patch' and other employees to the project 'proj_web_03'.
        Present the allocated employees based on their destination project.
        """,
        actions=[
            Action(
                name="SearchEmployees",
                kwargs={"role_contains": "Senior", "utilization_below": 90},
            ),
            Action(
                name="CalculateEmployeeAvailability", kwargs={"employee_id": "emp_dev_03"}
            ),
            Action(name="CalculateEmployeeAvailability", kwargs={"employee_id": "emp_data_01"}),
            Action(name="CalculateEmployeeAvailability", kwargs={"employee_id": "emp_eng_20"}),
            Action(
                name="CreateAllocation",
                kwargs={
                    "employee_id": "emp_dev_03",
                    "project_id": "proj_security_patch",
                    "hours_per_week": 10,
                    "role": "Senior Developer",
                    "status": "active",
                },
            ),
            Action(
                name="CreateAllocation",
                kwargs={
                    "employee_id": "emp_eng_20",
                    "project_id": "proj_security_patch",
                    "hours_per_week": 8,
                    "role":  "Senior Developer",
                    "status": "active",
                },
            ),
            Action(
                name="CreateAllocation",
                kwargs={
                    "employee_id": "emp_data_01",
                    "project_id": "proj_web_03",
                    "hours_per_week": 8,
                    "role": "Senior Data Analyst",
                    "status": "active",
                },
            ),
            Action(
                name="UpdateUtilizationLog",
                kwargs={
                    "employee_id": "emp_data_01",
                    "new_utilization": 100,
                },
            ),
            Action(
                name="UpdateUtilizationLog",
                kwargs={
                    "employee_id": "emp_dev_03",
                    "new_utilization": 100,
                },
            ),
            Action(
                name="UpdateUtilizationLog",
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
        In your role as department head, address the uneven workload distribution within the QA department where some employees are overworked
        (utilization above 90%) while others are underutilized (utilization of 70% or below). Review both overloaded and
        underutilized employees within the QA department. For
        those overloaded, adjust their allocations by reducing hours to reach 90% utilization. For underutilized employees, provide additional
        hours necessary to reach 90% utilization, targeting the project 'proj_client_01'. Compute and display the overall department
        utilization and the adjusted hours for each employee.
        """,
        actions=[
            Action(
                name="SearchEmployees",
                kwargs={"department": "QA", "utilization_above": 90},
            ),
            Action(
                name="GetEmployeeAllocations",
                kwargs={"employee_id": "emp_test_05"},
            ),
            Action(
                name="UpdateAllocation",
                kwargs={"allocation_id": "alloc_client_03", "hours_per_week": 36},
            ),
            Action(
                name="SearchEmployees",
                kwargs={"department": "QA", "utilization_below": 70},
            ),
            Action(
                name="GetEmployeeAllocations",
                kwargs={"employee_id": "emp_sec_test_01"},
            ),
            Action(
                name="GetEmployeeAllocations",
                kwargs={"employee_id": "emp_qa_02"},
            ),
            Action(
                name="CreateAllocation",
                kwargs={
                    "employee_id": "emp_sec_test_01",
                    "project_id": "proj_client_01",
                    "hours_per_week": 8,
                    "role": "Security Tester",
                    "status": "active",
                },
            ),
            Action(
                name="CreateAllocation",
                kwargs={
                    "employee_id": "emp_qa_02",
                    "project_id": "proj_client_01",
                    "hours_per_week": 12,
                    "role": "QA Engineer",
                    "status": "active",
                },
            ),
            Action(
                name="CalculateDepartmentUtilization", kwargs={"department": "QA"}
            ),
            Action(
                name="UpdateEmployeesUtilization",
                kwargs={"employee_ids": ["emp_test_05", "emp_qa_02", "emp_sec_test_01"]},
            ),
        ],
        outputs=['"emp_test_05": -4', '"emp_qa_02": 12','"emp_sec_test_01": 8', '"department_utilization": 90'],
    ),
    Task(
        annotator="0",
        user_id="execute_multi_project_resource_optimization",
        instruction="""
        As a portfolio director, your task involves optimizing resource allocation for 2 key projects
        (Enterprise Platform and Platform Modernization).
        For both projects, acquire details of all
        employees assigned, then adjust the allocations according to each employee's maximum capacity.
        Employees participating in both projects should be excluded. Output the new utilization percentage by employee.
        """,
        actions=[
            Action(name="SearchProjects", kwargs={"name": "Enterprise Platform"}),
            Action(name="SearchProjects", kwargs={"name": "Platform Modernization"}),
            Action(
                name="GetProjectAllocations",
                kwargs={"project_id": "proj_enterprise_01"},
            ),
            Action(
                name="GetProjectAllocations",
                kwargs={"project_id": "proj_platform_02"},
            ),
            Action(
                name="GetEmployeeDetails", kwargs={"employee_id": "emp_devops_02"}
            ),
            Action(
                name="UpdateAllocation",
                kwargs={"allocation_id": "alloc_devops_01", "hours_per_week": 40},
            ),
            Action(
                name="GetEmployeeDetails", kwargs={"employee_id": "emp_data_02"}
            ),
            Action(
                name="UpdateAllocation",
                kwargs={"allocation_id":  "alloc_data_02", "hours_per_week": 40},
            ),
            Action(
                name="GetEmployeeDetails", kwargs={"employee_id":  "emp_devops_04"}
            ),
            Action(
                name="UpdateAllocation",
                kwargs={"allocation_id":  "alloc_devops_02", "hours_per_week": 40},
            ),
            Action(
                name="UpdateEmployeesUtilization",
                kwargs={"employee_ids": ["emp_devops_02", "emp_devops_04", "emp_data_02"]},
            ),
        ],
        outputs=['"emp_devops_02": 100', '"emp_devops_04": 100', '"emp_data_02": 100'],
    ),
    Task(
        annotator="0",
        user_id="emergency_resource_allocation",
        instruction="""
        As a project manager, your critical project 'Mobile App Launch' requires an additional developer with
        JavaScript skills who can assist with React development (minimum proficiency 4 for both skills).
        You need someone with at least 20 available hours weekly. If no employees with these skills have 20 hours
        available, select the employee with these skills with the least utilization and allocate all available hours to the
        project. Ensure to update the employee utilization percentage to 100%.
        The allocation must utilize a start_date of 2024-01-15 and an end_date of 2024-06-30. Output the allocation ID and the allocated
        hours

        """,
        actions=[
            Action(name="SearchProjects", kwargs={"name": "Mobile App Launch"}),
            Action(name="GetProjectDetails", kwargs={"project_id": "proj_mobile_01"}),
            Action(
                name="SearchEmployees",
                kwargs={
                    "skills": ["JavaScript", "React"],
                    "min_proficiency": 4,
                    "min_skill_matches": 2,
                    "min_available_hours": 20,
                },
            ),
            Action(
                name="SearchEmployees",
                kwargs={
                    "skills": ["JavaScript", "React"],
                    "min_proficiency": 4,
                    "min_skill_matches": 2,
                },
            ),
            Action(
                name="CalculateEmployeeAvailability",
                kwargs={"employee_id":  "emp_eng_20"},
            ),
            Action(
                name="CreateAllocation",
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
                name="UpdateUtilizationLog",
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
        Assume the role of the HR director. The 'Customer Insights' project is in need of additional staff. Identify a non-junior
        employee with a utilization rate of 70% or below to work on Python-related tasks, and a junior employee possessing SQL skills whose
        utilization is at 60% or less. In the event of having several
        candidates, opt for the one with the lowest utilization percentage; if there's a tie, select the first individual
        listed in the search results. Assign to the project the lesser value between 30 and the available hours of the selected
        employees. The duration of the allocation should align with the project's timeframe. Provide the
        hours assigned per employee ID. Report the newly assigned team members, the total allocated hours within
        the workflow, and the project's cumulative hours.
        """,
        actions=[
            Action(name="SearchProjects", kwargs={"name": "Customer Insights"}),
            Action(
                name="GetProjectDetails", kwargs={"project_id": "proj_insights_01"}
            ),
            Action(
                name="GetProjectAllocations",
                kwargs={"project_id": "proj_insights_01"},
            ),
            Action(
                name="SearchEmployees",
                kwargs={"skills": ["Python"], "utilization_below": 70, "role_disregard": "Junior"},
            ),
            Action(
                name="SearchEmployees",
                kwargs={"skills": ["SQL"], "utilization_below": 60, "role_contains": "Junior"},
            ),
            Action(
                name="CalculateEmployeeAvailability",
                kwargs={"employee_id": "emp_analyst_03"},
            ),
            Action(
                name="CalculateEmployeeAvailability",
                kwargs={"employee_id":  "emp_sec_dev_03"},
            ),
            Action(
                name="CreateAllocation",
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
                name="CreateAllocation",
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
                name="UpdateUtilizationLog",
                kwargs={
                    "employee_id": "emp_analyst_03",
                    "new_utilization": 100,
                },
            ),
            Action(
                name="UpdateUtilizationLog",
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
        The 'AI Platform' project necessitates Machine Learning engineers with a proficiency level of 4 or above. Seek out available
        employees to satisfy this requirement. Determine the availability
        of employees from the search results. If no employees fitting the criteria are located, or the summed
        available hours combined with the project’s allocated hours fall short of the necessary project hours,
        initiate an urgent resource request (id=req_ai_ml_01) for external recruitment to cover the shortfall in hours required for
        the project. Indicate if a skill gap was detected, along with the request ID and the requested hours.
        """,
        actions=[
            Action(name="SearchProjects", kwargs={"name": "AI Platform"}),
            Action(name="GetProjectDetails", kwargs={"project_id": "proj_ai_01"}),
            Action(
                name="SearchEmployees",
                kwargs={"skills": ["Machine Learning"], "min_proficiency": 4},
            ),
            Action(
                name="CreateResourceRequest",
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
        As the integration director, your role is to manage the merging of three projects: Alpha Module, Beta
        Module, and Gamma Module. Locate these projects and utilize Alpha Module as the overarching project. Reassign all team members from the merged projects into the unified project. If the transferred employees are not already part of the Alpha Module, establish new allocations; otherwise, simply modify the existing allocations. Retain the original start/end dates for current allocations, while adopting the unified project's start/end dates for new allocations. Eliminate the allocations
        from the merged projects, and designate these as cancelled. Adjust the unified project's required hours to reflect the cumulative required hours of all three projects. Form a team named "Alpha Unified Team" incorporating the employees from the new unified project and provide a consolidation summary including the team size, total allocation hours, and the unified project ID.
        """,
        actions=[
            Action(name="SearchProjects", kwargs={"name": "Alpha Module"}),
            Action(name="SearchProjects", kwargs={"name": "Beta Module"}),
            Action(name="SearchProjects", kwargs={"name": "Gamma Module"}),
            Action(name="GetProjectDetails", kwargs={"project_id": "proj_alpha_01"}),
            Action(name="GetProjectDetails", kwargs={"project_id": "proj_beta_02"}),
            Action(name="GetProjectDetails", kwargs={"project_id": "proj_gamma_03"}),
            Action(
                name="GetProjectAllocations", kwargs={"project_id": "proj_alpha_01"}
            ),
            Action(
                name="GetProjectAllocations", kwargs={"project_id": "proj_beta_02"}
            ),
            Action(
                name="GetProjectAllocations", kwargs={"project_id": "proj_gamma_03"}
            ),
            Action(
                name="UpdateAllocation",
                kwargs={"allocation_id": "alloc_alpha_01", "hours_per_week": 60},
            ),
            Action(name="DeleteAllocation", kwargs={"allocation_id": "alloc_beta_01"}),
            Action(
                name="DeleteAllocation", kwargs={"allocation_id": "alloc_gamma_01"}
            ),
            Action(
                name="CreateAllocation",
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
                name="DeleteAllocation", kwargs={"allocation_id": "alloc_analyst_03"}
            ),
            Action(
                name="CreateAllocation",
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
                name="CreateTeam",
                kwargs={
                    "team_id": "team_alpha_unified",
                    "team_name": "Alpha Unified Team",
                    "project_id": "proj_alpha_01",
                    "team_members": ["emp_dev_15", "emp_qa_02", "emp_analyst_03"],
                },
            ),
            Action(
                name="UpdateProjectStatus",
                kwargs={"project_id": "proj_beta_02", "status": "cancelled"},
            ),
            Action(
                name="UpdateProjectStatus",
                kwargs={"project_id": "proj_gamma_03", "status": "cancelled"},
            ),
            Action(
                name="UpdateProjectRequiredHours",
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
        As the security compliance manager, your task is to address the new requirement for the 'Banking Integration' project, which now mandates secret clearance for all team members due to updated regulatory rules. Examine current allocations, pinpoint employees without the necessary clearance, and seek replacements who possess secret clearance, holding the same job roles and availability as the employees being replaced, ensuring all replaced employees' allocated hours are covered. Finally, compile the list of employees removed and added to the project, and provide the compliance status validation.
        The allocations should have a start_date of 2024-01-01 and an end_date of 2024-08-31.
        """,
        actions=[
            Action(name="SearchProjects", kwargs={"name": "Banking Integration"}),
            Action(
                name="GetProjectAllocations", kwargs={"project_id": "proj_banking_01"}
            ),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "emp_sec_dev_01"}),
            Action(
                name="SearchEmployees",
                kwargs={
                    "clearance": "secret",
                    "role_contains": "Security Developer",
                    "min_available_hours": 40,
                },
            ),
            Action(
                name="CalculateEmployeeAvailability",
                kwargs={"employee_id": "emp_sec_dev_XX"},
            ),
            Action(
                name="CreateResourceConflict",
                kwargs={
                    "employee_id": "emp_sec_dev_01",
                    "competing_projects": ["proj_banking_01"],
                    "conflict_type": "clearance_violation",
                },
            ),
            Action(name="DeleteAllocation", kwargs={"allocation_id": "alloc_bank_01"}),
            Action(
                name="CreateAllocation",
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
                name="UpdateEmployeesUtilization",
                kwargs={"employee_ids": ["emp_sec_dev_XX", "emp_sec_dev_01"]},
            ),
            Action(
                name="ValidateComplianceStatus",
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
        As the talent director, handle the critical skill shortage resulting from the resignation of three senior Machine Learning engineers
        from the 'AI Platform' project. Dedicate 92 hours to this project. Initially, assign all available hours from employees possessing 'Machine Learning' skills.
        If these hours do not reach the required 92, look for employees with Python skills, proficiency of 4 or higher, and an 85% utilization rate or below.
        Prioritize lower utilization percentages, and in the event of a tie, select the first employee listed in search results.
        Endeavor to allocate all available hours per priority until reaching a total of 92.
        Form the 'AI Emergency Response Team' with the new staff arrangement for the project and place an immediate resource request for external hiring requiring 70 hours, with the skill 'Machine Learning' in the 'Engineering' department.
        Present the project hours allocated by employees.
        """,
        actions=[
            Action(name="SearchProjects", kwargs={"name": "AI Platform"}),
            Action(name="GetProjectAllocations", kwargs={"project_id": "proj_ai_01"}),
            Action(name="SearchEmployees", kwargs={"skills": ["Machine Learning"]}),
            Action(name="CalculateEmployeeAvailability", kwargs={"employee_id": "emp_data_01"}),
            Action(name="UpdateAllocation", kwargs={"allocation_id":  "alloc_data_01", "hours_per_week": 40}),
            Action(name="UpdateUtilizationLog", kwargs={"employee_id":  "emp_data_01", "new_utilization": 100}),
            Action(
                name="SearchEmployees",
                kwargs={
                    "skills": ["Python"],
                    "min_proficiency": 4,
                    "utilization_below": 85,
                },
            ),
            Action(name="CalculateEmployeeAvailability", kwargs={"employee_id":  "emp_sec_dev_XX"}),
            Action(
                name="CreateAllocation",
                kwargs={
                    "employee_id": "emp_sec_dev_XX",
                    "project_id": "proj_ai_01",
                    "hours_per_week": 40,
                    "role":  "Security Developer",
                    "status": "active",
                },
            ),
            Action(name="CalculateEmployeeAvailability", kwargs={"employee_id": "emp_data_02"}),
            Action(
                name="CreateAllocation",
                kwargs={
                    "employee_id": "emp_data_02",
                    "project_id": "proj_ai_01",
                    "hours_per_week": 12,
                    "role":  "Data Engineer",
                    "status": "active",
                },
            ),
            Action(
                name="CreateResourceRequest",
                kwargs={
                    "project_id": "proj_ai_01",
                    "skill_required": "Machine Learning",
                    "hours_needed": 70,
                    "urgency": "urgent",
                    "department": "Engineering",
                },
            ),
            Action(
                name="CreateTeam",
                kwargs={
                    "team_name": "AI Emergency Response Team",
                    "project_id": "proj_ai_01",
                    "team_members": ["emp_data_02", "emp_sec_dev_XX", "emp_data_01"],
                },
            ),
            Action(
                name="UpdateEmployeesUtilization",
                kwargs={"employee_ids": ["emp_data_02", "emp_sec_dev_XX", "emp_data_01"]}
            ),
        ],
        outputs=['"emp_data_01": 40', '"emp_sec_dev_XX": 40', '"emp_data_02": 12'],
    ),
    Task(
        annotator="0",
        user_id="optimize_resource_allocation_efficiency",
        instruction="""
        As the asset optimization specialist, address the resource
        allocation issues in the 'Enterprise Platform' project, where senior architects are performing junior-level tasks. Evaluate the current allocations and, for each senior
        employee, find a junior employee to substitute them. Follow this example for locating junior
        employees: for every senior in the project, identify an employee with 'Junior' in their job role and
        possessing at least 2 of the 3 skills listed in the senior employee's details. Moreover, use the senior employee's
        allocated hours as 'min_available_hours' in the employee search. Once a suitable junior employee meeting the conditions is identified, transfer the senior employee's hours to the junior employee and remove the allocation for the senior employee.
        If there are multiple junior employee options, select the first
        employee in the search results. Calculate the project's optimization metrics and report the efficiency improvement.
        """,
        actions=[
            Action(name="SearchProjects", kwargs={"name": "Enterprise Platform"}),
            Action(
                name="GetProjectDetails", kwargs={"project_id": "proj_enterprise_01"}
            ),
            Action(
                name="GetProjectAllocations",
                kwargs={"project_id": "proj_enterprise_01"},
            ),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "emp_arch_01"}),
            Action(
                name="SearchEmployees",
                kwargs={
                    "skills": ["System Design", "Cloud Architecture", "Microservices"],
                    "min_skill_matches": 2,
                    "role_contains": "Junior",
                    "min_available_hours": 20,
                },
            ),
            Action(
                name="CalculateEmployeeAvailability",
                kwargs={"employee_id": "emp_jr_arch_01"},
            ),
            Action(
                name="DeleteAllocation",
                kwargs={"allocation_id": "alloc_arch_01"},
            ),
            Action(
                name="CreateAllocation",
                kwargs={
                    "employee_id": "emp_jr_arch_01",
                    "project_id": "proj_enterprise_01",
                    "hours_per_week": 20,
                    "role":  "Junior Architect",
                    "status": "active",
                },
            ),
            Action(
                name="UpdateEmployeesUtilization",
                kwargs={"employee_ids": ["emp_jr_arch_01", "emp_arch_01"]},
            ),
            Action(
                name="CalculateOptimizationMetrics",
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
        As the lead for restructuring, the task is to merge the Analytics and QA departments into the new 'Quality Analytics'
        department. Appoint the Analytics head to oversee this newly formed department, eliminating the prior departments.
        Ensure to update the team and employee registry reflecting the merger. Provide the total capacity and allocated hours for the new department.
        """,
        actions=[
            Action(name="GetDepartmentTeams", kwargs={"department": "Analytics"}),
            Action(name="GetDepartmentTeams", kwargs={"department": "QA"}),
            Action(name="SearchEmployees", kwargs={"department": "Analytics"}),
            Action(name="SearchEmployees", kwargs={"department": "QA"}),
            Action(name="GetDepartmentTeams", kwargs={"department": "Analytics"}),
            Action(name="GetDepartmentDetails", kwargs={"name": "Analytics"}),
            Action(
                name="CreateDepartment",
                kwargs={
                    "name": "Quality Analytics",
                    "head_id": "emp_head_analytics"}
            ),
            Action(
                name="UpdateTeamsDepartment",
                kwargs={"team_id": "team_analytics_01", "department": "Quality Analytics"}
            ),
            Action(
                name="UpdateTeamsDepartment",
                kwargs={"team_id": "team_qa_01", "department": "Quality Analytics"}
            ),
            Action(
                name="UpdateTeamsDepartment",
                kwargs={"team_id": "team_qa_02", "department": "Quality Analytics"}
            ),
            Action(
                name="UpdateEmployeesDepartment",
                kwargs={"employee_id": "emp_data_01", "department": "Quality Analytics"}
            ),
            Action(
                name="UpdateEmployeesDepartment",
                kwargs={"employee_id": "emp_data_02", "department": "Quality Analytics"}
            ),
            Action(
                name="UpdateEmployeesDepartment",
                kwargs={"employee_id": "emp_analyst_01", "department": "Quality Analytics"}
            ),
            Action(
                name="UpdateEmployeesDepartment",
                kwargs={"employee_id": "emp_analyst_02", "department": "Quality Analytics"}
            ),
            Action(
                name="UpdateEmployeesDepartment",
                kwargs={"employee_id": "emp_analyst_03", "department": "Quality Analytics"}
            ),
            Action(
                name="UpdateEmployeesDepartment",
                kwargs={"employee_id": "emp_sec_test_01", "department": "Quality Analytics"}
            ),
            Action(
                name="UpdateEmployeesDepartment",
                kwargs={"employee_id": "emp_qa_02", "department": "Quality Analytics"}
            ),
            Action(
                name="UpdateEmployeesDepartment",
                kwargs={"employee_id": "emp_test_05", "department": "Quality Analytics"}
            ),
            Action(name="DeleteDepartment", kwargs={"name": "Analytics"}),
            Action(name="DeleteDepartment", kwargs={"name": "QA"}),
            Action(name="UpdateDepartmentsUtilization", kwargs={}),
            Action(name="GetDepartmentDetails", kwargs={"name": "Quality Analytics"}),
        ],
        outputs=['"total_capacity": 320', '"allocated_hours": 244'],
    ),
    Task(
        annotator="0",
        user_id="implement_skills_development_rotation",
        instruction="""
        As the manager overseeing skills development, coordinate a rotation program where junior developers dedicate 25% of their time
        (10 hours/week) to advanced projects for enhancing skills. Identify junior developers engaged in projects who demonstrate high potential
        (proficiency 3+), decrease their present allocations by 10 hours, and assign those 10 hours to the 'Enterprise Platform'
        senior-led project. Set allocation timelines beginning 'start_date' 2024-04-01, concluding 'end_date' 2024-06-30. Establish the rotation
        commencement date as 2024-04-01, ensuring the holiday coverage is set to false and skill development rotation to true.
        Present the count of developers involved in rotation and the cumulative skills development hours.
        """,
        actions=[
            Action(
                name="SearchEmployees",
                kwargs={"role_contains": "Junior", "min_proficiency": 3},
            ),
            Action(
                name="GetEmployeeAllocations",
                kwargs={"employee_id": "emp_analyst_03"},
            ),
            Action(
                name="GetEmployeeAllocations",
                kwargs={"employee_id": "emp_jr_arch_01"},
            ),
            Action(
                name="GetEmployeeDetails", kwargs={"employee_id": "emp_analyst_03"}
            ),
            Action(name="SearchProjects", kwargs={"name": "Enterprise Platform"}),
            Action(
                name="GetProjectDetails", kwargs={"project_id": "proj_enterprise_01"}
            ),
            Action(
                name="UpdateAllocation",
                kwargs={"allocation_id": "alloc_analyst_03", "hours_per_week": 14},
            ),
            Action(
                name="CreateAllocation",
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
                name="CreateRotationSchedule",
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
        As the program manager, oversee the transition of the 'Mobile App Launch' project from development to the testing phase
        on April 1st. Reduce developer allocations to a total of 20 hours per week, and increase QA resources to 10 hours per week by
        identifying QA staff with utilization under 80%. Give priority to employees with less utilization. The new allocations
        should start on 2024-04-01 and end on 2024-06-30. Provide the outcomes for project development hours and QA hours.
        """,
        actions=[
            Action(name="SearchProjects", kwargs={"name": "Mobile App Launch"}),
            Action(name="GetProjectDetails", kwargs={"project_id": "proj_mobile_01"}),
            Action(
                name="GetProjectAllocations", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(
                name="UpdateAllocation",
                kwargs={
                    "allocation_id": "alloc_mobile_03",
                    "hours_per_week": 20,
                },
            ),
            Action(
                name="SearchEmployees",
                kwargs={"department": "QA", "utilization_below": 80},
            ),
            Action(
                name="CalculateEmployeeAvailability",
                kwargs={"employee_id": "emp_qa_02"},
            ),
            Action(
                name="CalculateEmployeeAvailability",
                kwargs={"employee_id": "emp_sec_test_01"},
            ),
            Action(
                name="CreateAllocation",
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
                name="UpdateEmployeesUtilization",
                kwargs={
                    "employee_ids": ["emp_qa_02", "emp_dev_03"],
                },
            ),
            Action(
                name="SummarizeProjectPhaseMetrics",
                kwargs={"project_id": "proj_mobile_01"},
            ),
        ],
        outputs=['"dev_hours": 20', '"qa_hours": 10'],
    ),
    Task(
        annotator="0",
        user_id="implement_rotation_schedules_across_projects",
        instruction="""
        As an operations manager, devise skill development rotation schedules for the employees of the
        projects: 'Banking Integration' and 'Customer Portal'. Ensure a rotation schedule is established for each employee of the
        'Customer Portal' to rotate into 'Banking Integration'. Repeat the process for employees
        from 'Banking Integration' to the 'Customer Portal'. Set the rotation date as "2024-12-23",
        ensure 20 rotation hours, and configure the 'holiday_coverage' parameter to false, with skill
        development rotation marked as true. List the employees involved in the rotation.
        """,
        actions=[
            Action(name="SearchProjects", kwargs={"name": "Banking Integration"}),
            Action(name="SearchProjects", kwargs={"name": "Customer Portal"}),
            Action(
                name="GetProjectAllocations", kwargs={"project_id": "proj_banking_01"}
            ),
            Action(
                name="GetProjectAllocations", kwargs={"project_id": "proj_web_03"}
            ),
            Action(
                name="CreateRotationSchedule",
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
                name="CreateRotationSchedule",
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
        As the hybrid work coordinator, it is your responsibility to manage the 'Enterprise Platform' project, which requires an onsite presence of 40%.
        Gather details for each employee involved in the project to compute the total hours dedicated by those who are able to work onsite.
        If the current total hours are insufficient to meet the 40% requirement, locate a team member from the Engineering department eligible for onsite work, prioritizing those with lower capacity
        and possessing the 'Mathematics' skill. Reallocate the available hours for the employee to meet the necessary onsite percentage.
        Ensure that the allocations commence from start_date 2024-02-01 and conclude on end_date 2024-12-31. Provide the sum of onsite hours,
        incorporating both prior and adjusted allocations.
        """,
        actions=[
            Action(name="SearchProjects", kwargs={"name": "Enterprise Platform"}),
            Action(
                name="GetProjectDetails", kwargs={"project_id": "proj_enterprise_01"}
            ),
            Action(
                name="GetProjectAllocations",
                kwargs={"project_id": "proj_enterprise_01"},
            ),
            Action(
                name="GetEmployeeDetails", kwargs={"employee_id": "emp_devops_02"}
            ),
            Action(
                name="GetEmployeeDetails", kwargs={"employee_id": "emp_arch_01"}
            ),
            Action(
                name="SearchEmployees",
                kwargs={"department": "Engineering", "skills": ["Mathematics"]},
            ),
            Action(
                name="CreateAllocation",
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
        In your capacity as the DevOps manager, you need to address the urgent requirement for Docker expertise (proficiency 5) in the 'Platform Modernization' project.
        Identify employees with a Docker skill level of 5, confirm they are utilized at less than 80%, and assign 10 hours/week
        to the project. Return the resulting utilization percentage of the employee who has been allocated. Plan this allocation with
        start_date 2024-03-01 and end_date 2024-10-31.
        """,
        actions=[
            Action(name="SearchProjects", kwargs={"name": "Platform Modernization"}),
            Action(
                name="SearchEmployees",
                kwargs={
                    "skills": ["Docker"],
                    "min_proficiency": 5,
                    "utilization_below": 80,
                },
            ),
            Action(
                name="GetEmployeeAllocations", kwargs={"employee_id": "emp_devops_04"}
            ),
            Action(
                name="CalculateEmployeeAvailability",
                kwargs={"employee_id": "emp_devops_04"},
            ),
            Action(
                name="CreateAllocation",
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
                name="CalculateEmployeeUtilization",
                kwargs={"employee_id": "emp_devops_04"},
            ),
        ],
        outputs=["85"],
    ),
    Task(
        annotator="0",
        user_id="create_security_taskforce",
        instruction="""
        As the CISO, you need to establish a security task force for the 'Security Patch' project. Identify 2 developers and 1
        tester with the necessary security clearance, assess their availability, and form a team named 'Security Task Force'.
        Assign 10 hours of work for each member to this project. Give priority to employees with a utilization rate of 0%.
        Report how many resources have been successfully allocated to the project.
        """,
        actions=[
            Action(name="SearchProjects", kwargs={"name": "Security Patch"}),
            Action(name="GetProjectAllocations", kwargs={"project_id": "proj_security_patch"}),
            Action(
                name="SearchEmployees",
                kwargs={"clearance": "secret", "role_contains": "Developer"},
            ),
            Action(
                name="SearchEmployees",
                kwargs={"clearance": "secret", "role_contains": "Tester"},
            ),
            Action(
                name="CalculateEmployeeAvailability",
                kwargs={"employee_id": "emp_sec_dev_03"},
            ),
            Action(
                name="CalculateEmployeeAvailability",
                kwargs={"employee_id": "emp_sec_dev_XX"},
            ),
            Action(
                name="CalculateEmployeeAvailability",
                kwargs={"employee_id": "emp_sec_test_01"},
            ),
            Action(
                name="CreateTeam",
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
                name="CreateAllocation",
                kwargs={
                    "employee_id": "emp_sec_test_01",
                    "project_id": "proj_security_patch",
                    "hours_per_week": 10,
                    "role": "Security Tester",
                    "status": "active",
                },
            ),
            Action(
                name="CreateAllocation",
                kwargs={
                    "employee_id": "emp_sec_dev_XX",
                    "project_id": "proj_security_patch",
                    "hours_per_week": 10,
                    "role": "Security Developer",
                    "status": "active",
                },
            ),
            Action(
                name="CreateAllocation",
                kwargs={
                    "employee_id": "emp_sec_dev_03",
                    "project_id": "proj_security_patch",
                    "hours_per_week": 10,
                    "role": "Security Developer",
                    "status": "active",
                },
            ),
            Action(
                name="ValidateComplianceStatus",
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
        As a tech lead, you should initiate a new project titled "Analytics Project". In conjunction with this project, form a team called 'Analytics Team' comprised of employees from the Analytics department.
        Ensure the team has a cumulative availability of at least 24 hours. Give preference to employees skilled in 'Python' and 'SQL', avoiding Junior-level staff.
        Team members you select should maintain current utilization below 90. Assign each team member 8 hours to contribute to the project. Conclude by confirming if the
        project and team creation was successful, and list the employees added to the team in the results.
        """,
        actions=[
            Action(
                name="CreateProject",
                kwargs={
                    "department": "Analytics",
                    "project_id": "proj_analytics_01",
                    "project_name": "Analytics Project",
                    "required_hours_per_week": 24
                }),
            Action(
                name="SearchEmployees",
                kwargs={"department": "Analytics", "utilization_below": 90, "role_disregard": "Junior"}
            ),
            Action(name="CalculateEmployeeUtilization", kwargs={"employee_id": "emp_data_01"}),
            Action(name="CalculateEmployeeUtilization", kwargs={"employee_id": "emp_data_02"}),
            Action(name="CalculateEmployeeUtilization", kwargs={"employee_id": "emp_analyst_02"}),
            Action(
                name="CreateAllocation",
                kwargs={
                    "employee_id": "emp_data_01",
                    "project_id": "proj_analytics_01",
                    "hours_per_week": 8,
                    "role": "Senior Data Analyst",
                    "status": "active",
                },
            ),
            Action(
                name="CreateAllocation",
                kwargs={
                    "employee_id": "emp_data_02",
                    "project_id": "proj_analytics_01",
                    "hours_per_week": 8,
                    "role": "Data Engineer",
                    "status": "active",
                },
            ),
            Action(
                name="CreateAllocation",
                kwargs={
                    "employee_id": "emp_analyst_02",
                    "project_id": "proj_analytics_01",
                    "hours_per_week": 8,
                    "role": "Data Analyst",
                    "status": "active",
                },
            ),
            Action(
                name="CreateTeam",
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
        You are the staffing manager. The 'Web Platform Update' project is in need of additional frontend developers.
        Locate employees with a proficiency in React at level 4 or higher and with a utilization rate of 70% or below to allocate them to the project.
        Initiate a resource request with standard urgency for the 'Engineering' department
        and calculate how many hours are still required. Provide the remaining hours needed.
        """,
        actions=[
            Action(name="SearchProjects", kwargs={"name": "Web Platform Update"}),
            Action(name="GetProjectDetails", kwargs={"project_id": "proj_web_02"}),
            Action(
                name="SearchEmployees",
                kwargs={
                    "skills": ["React"],
                    "min_proficiency": 4,
                    "utilization_below": 70,
                },
            ),
            Action(
                name="CreateResourceRequest",
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
        As the Engineering Director, oversee Senior Architect Daniel Mitchell, who is engaged in two projects.
        Assess the priority of each project, and remove him from the one with lower priority. Subsequently, establish
        an allocation for a junior staff member who possesses at least two shared skills with him.
        Ensure that the junior employee's full 40 available hours are utilized in the allocation.
        Lastly, present the efficiency improvement percentage resulting from this change.
        """,
        actions=[
            Action(name="SearchEmployees", kwargs={"name": "Michael Roberts"}),
            Action(
                name="GetEmployeeAllocations", kwargs={"employee_id": "emp_arch_01"}
            ),
            Action(
                name="CompareProjectPriorities",
                kwargs={
                    "project_id_1": "proj_enterprise_01",
                    "project_id_2": "proj_platform_02",
                },
            ),
            Action(
                name="SearchEmployees",
                kwargs={
                    "skills": ["System Design", "Cloud Architecture", "Microservices"],
                    "min_available_hours": 40,
                    "min_skill_matches": 2,
                    "role_contains": "Junior",
                },
            ),
            Action(
                name="GetEmployeeAllocations", kwargs={"employee_id": "emp_jr_arch_01"}
            ),
            Action(
                name="CalculateEmployeeAvailability", kwargs={"employee_id": "emp_jr_arch_01"}
            ),
            Action(
                name="DeleteAllocation",
                kwargs={"allocation_id": "alloc_arch_02"}
            ),
            Action(
                name="CreateAllocation",
                kwargs={
                    "employee_id": "emp_jr_arch_01",
                    "project_id": "proj_platform_02",
                    "hours_per_week": 40,
                    "role": "Junior Architect",
                    "department": "Engineering",
                }
            ),
            Action(
                name="UpdateEmployeesUtilization",
                kwargs={"employee_ids": ["emp_jr_arch_01", "emp_arch_01"]}
            ),
            Action(
                name="CalculateOptimizationMetrics",
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
        As the project controller, deal with the situation where the 'Customer Portal' project nears its budget limits. Examine current
        resource allocations, identify junior resources with proficiency levels of 3 or higher, who have utilization rates not exceeding 80%. Determine
        the availability of
        the identified employees and assign their available hours to meet the project's required hours. In your allocation,
        give priority to those with lower utilization rates. Provide a report showing the final utilization percentages of the junior employees allocated, based on their employee IDs.
        Ensure that the new allocations commence on 2024-03-01 and conclude on 2024-10-31.
        """,
        actions=[
            Action(name="SearchProjects", kwargs={"name": "Customer Portal"}),
            Action(
                name="GetProjectAllocations", kwargs={"project_id": "proj_web_03"}
            ),
            Action(
                name="GetProjectDetails", kwargs={"project_id": "proj_web_03"}
            ),
            Action(
                name="SearchEmployees",
                kwargs={
                    "role_contains": "Junior",
                    "min_proficiency": 3,
                    "utilization_below": 80,
                },
            ),
            Action(
                name="CalculateEmployeeAvailability",
                kwargs={"employee_id": "emp_jr_arch_01"},
            ),
            Action(
                name="CalculateEmployeeAvailability",
                kwargs={"employee_id": "emp_analyst_03"},
            ),
            Action(
                name="CreateAllocation",
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
                name="CreateAllocation",
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
                name="UpdateEmployeesUtilization",
                kwargs={"employee_ids": ["emp_analyst_03", "emp_jr_arch_01"]},
            ),
        ],
        outputs=['"emp_jr_arch_01": 100', '"emp_analyst_03": 80'],
    ),
    Task(
        annotator="0",
        user_id="expand_analytics_team",
        instruction="""
        As the analytics manager, handle the requirement to increase the 'Customer Insights' project's commitment from 30 to 60 hours per week.
        Select two employees proficient in Python, whose utilization falls within [49%, 61%], and assign each 15 hours to the project.
        Develop allocations that start on 2024-02-01 and end on 2024-08-31, and make sure to select the first two employees listed in the result.
        Report the total number of project hours following the expansion. Be aware that the project requires 80 hours per week,
        but for the moment, focus on adding 30 hours to the project commitment.
        """,
        actions=[
            Action(name="SearchProjects", kwargs={"name": "Customer Insights"}),
            Action(
                name="GetProjectAllocations",
                kwargs={"project_id": "proj_insights_01"},
            ),
            Action(
                name="SearchEmployees",
                kwargs={"skills": ["Python"], "utilization_below": 61, "utilization_above": 49},
            ),
            Action(
                name="CalculateEmployeeAvailability",
                kwargs={"employee_id": "emp_qa_02"},
            ),
            Action(
                name="CreateAllocation",
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
                name="CalculateEmployeeAvailability",
                kwargs={"employee_id": "emp_analyst_03"},
            ),
            Action(
                name="CreateAllocation",
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
                name="SummarizeTeamExpansion",
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
        As a portfolio director, you are overseeing three web projects: Web Portal Redesign, Web Platform Update, and Customer
        Portal, which have intersecting objectives. Examine their allocations, priorities, and resources. Combine them
        into the project with the highest priority and adjust the project statuses accordingly. In conclusion, outline the projects' consolidation, designate the highest priority project as the 'consolidate to' and categorize the other two projects as the 'consolidated projects.' Present the 'consolidate to' project, team size, and total hours.
        """,
        actions=[
            Action(name="SearchProjects", kwargs={"name": "Web Portal Redesign"}),
            Action(name="SearchProjects", kwargs={"name": "Web Platform Update"}),
            Action(name="SearchProjects", kwargs={"name": "Customer Portal"}),
            Action(name="GetProjectDetails", kwargs={"project_id": "proj_web_01"}),
            Action(name="GetProjectDetails", kwargs={"project_id": "proj_web_02"}),
            Action(name="GetProjectDetails", kwargs={"project_id": "proj_web_03"}),
            Action(
                name="CompareProjectPriorities",
                kwargs={"project_id_1": "proj_web_01", "project_id_2": "proj_web_02"},
            ),
            Action(
                name="CompareProjectPriorities",
                kwargs={"project_id_1": "proj_web_03", "project_id_2": "proj_web_01"},
            ),
            Action(
                name="GetProjectAllocations", kwargs={"project_id": "proj_web_03"}
            ),
            Action(
                name="GetProjectAllocations", kwargs={"project_id": "proj_web_02"}
            ),
            Action(
                name="GetProjectAllocations", kwargs={"project_id": "proj_web_01"}
            ),
            Action(
                name="CreateAllocation",
                kwargs={
                    "employee_id": "emp_dev_05",
                    "project_id": "proj_web_03",
                    "hours_per_week": 25,
                    "role": "Full Stack Developer",
                    "status": "active",
                },
            ),
            Action(
                name="DeleteAllocation",
                kwargs={"allocation_id": "alloc_web_01"},
            ),
            Action(
                name="UpdateProjectStatus",
                kwargs={"project_id": "proj_web_01", "status": "cancelled"},
            ),
            Action(
                name="UpdateProjectStatus",
                kwargs={"project_id": "proj_web_02", "status": "cancelled"},
            ),
            Action(
                name="SummarizeProjectConsolidation",
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
        You are the transition manager tasked with overseeing the 'Mobile App Launch' project as it shifts from the development phase to the testing phase.
        Determine the current development/QA hours distribution, cut developer allocations by 50%, identify 2 QA employees
        with 75% utilization or less and assign them 12 hours each for the project. Establish allocations
        starting from 2024-01-15 and concluding on 2024-06-30. Provide a report on the revised development and QA hours.
        """,
        actions=[
            Action(name="SearchProjects", kwargs={"name": "Mobile App Launch"}),
            Action(
                name="GetProjectAllocations", kwargs={"project_id": "proj_mobile_01"}
            ),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "emp_dev_03"}),
            Action(
                name="UpdateAllocation",
                kwargs={
                    "allocation_id": "alloc_mobile_03",
                    "hours_per_week": 15,
                },
            ),
            Action(
                name="SearchEmployees",
                kwargs={"department": "QA", "utilization_below": 75},
            ),
            Action(
                name="CalculateEmployeeAvailability",
                kwargs={"employee_id": "emp_qa_02"},
            ),
            Action(
                name="CalculateEmployeeAvailability",
                kwargs={"employee_id": "emp_sec_test_01"},
            ),
            Action(
                name="CreateAllocation",
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
                name="CreateAllocation",
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
                name="UpdateEmployeesUtilization",
                kwargs={
                    "employee_ids": ["emp_qa_02", "emp_sec_test_01", "emp_dev_03"],
                },
            ),
            Action(
                name="SummarizeProjectPhaseMetrics",
                kwargs={"project_id": "proj_mobile_01"},
            ),
        ],
        outputs=['"dev_hours": 15', '"qa_hours": 24'],
    ),
    Task(
        annotator="0",
        user_id="fill_ml_expertise_gap",
        instruction="""
        You are tasked with directing skills development. There exists a significant Machine Learning expertise gap in the 'AI Platform' project. Seek out new employees
        (excluding those already assigned) possessing Machine Learning abilities at any proficiency level and incorporate them into the project. If no employees
        are identified in the initial search, look for individuals with Python skills (proficiency >= 4) and utilization at 90% or lower as potential alternatives. Select
        the first two employees from the secondary search results, and allocate them to the project. Calculate their allocation hours by subtracting
        the product of maximum hours per week and utilization percentage from the maximum weekly hours available.
        Initiate an urgent resource request to obtain the hours necessary to meet the project's total required hours,
        factoring in the project's final allocation status, specifically for employees with 'Machine Learning' expertise in the 'Engineering'
        department. Provide the output of the hours needed to meet the project's total required hours.
        """,
        actions=[
            Action(name="SearchProjects", kwargs={"name": "AI Platform"}),
            Action(name="GetProjectDetails", kwargs={"project_id": "proj_ai_01"}),
            Action(name="GetProjectAllocations", kwargs={"project_id": "proj_ai_01"}),
            Action(
                name="SearchEmployees",
                kwargs={"skills": ["Machine Learning"], "disregard_employee_ids": ["emp_data_01"]}
            ),
            Action(
                name="SearchEmployees",
                kwargs={
                    "skills": ["Python"],
                    "min_proficiency": 4,
                    "utilization_below": 90,
                    "disregard_employee_ids": ["emp_data_01"]
                },
            ),
            Action(
                name="CreateAllocation",
                kwargs={
                    "employee_id": "emp_data_02",
                    "project_id": "proj_ai_01",
                    "hours_per_week": 14,
                    "role": "Data Engineer",
                    "status": "active",
                },
            ),
            Action(
                name="CreateAllocation",
                kwargs={
                    "employee_id": "emp_dev_07",
                    "project_id": "proj_ai_01",
                    "hours_per_week": 12,
                    "role": "Backend Developer",
                    "status": "active",
                },
            ),
            Action(name="GetProjectDetails", kwargs={"project_id": "proj_ai_01"}),
            Action(
                name="CreateResourceRequest",
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
        Your role is as a work coordinator. The 'Enterprise Platform' project requires an increase in onsite presence. Examine current project allocations,
        identify one new employee capable of working onsite to contribute 30 hours to the project. Select the first employee listed in the search results. Develop an allocation
        with a start date of 2024-02-01 and an end date of 2024-12-31. Provide the name of the employee selected.
        """,
        actions=[
            Action(name="SearchProjects", kwargs={"name": "Enterprise Platform"}),
            Action(
                name="GetProjectAllocations",
                kwargs={"project_id": "proj_enterprise_01"},
            ),
            Action(
                name="GetProjectDetails",
                kwargs={"project_id": "proj_enterprise_01"},
            ),
            Action(
                name="SearchEmployees",
                kwargs={
                    "disregard_employee_ids": ["emp_devops_02",  "emp_arch_01"],
                    "min_available_hours": 30
                },
            ),
            Action(
                name="CalculateEmployeeAvailability",
                kwargs={"employee_id": "emp_ux_03"},
            ),
            Action(
                name="CreateAllocation",
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
                name="UpdateUtilizationLog",
                kwargs={
                    "employee_id":  "emp_ux_03",
                    "new_utilization": 75,
                },
            ),
        ],
        outputs=['"employee_name": "Grace Wang"'],
    ),
    Task(
        annotator="0",
        user_id="rebalance_overloaded_teams",
        instruction="""
        As the workload manager, address the imbalanced workload of the Analytics team members, with some at 95% utilization and others at 60%. Review all team member allocations, pinpoint the most overloaded and the least utilized employee. From the overloaded employee's allocations, select the task with fewer hours and remove it. Subsequently, assign the project from the discarded allocation to the most underutilized employee, maintaining the original start and end dates. Conclude by revising employees' utilizations and display the change in hours for each employee by their ID.
        """,
        actions=[
            Action(name="GetTeamDetails", kwargs={"team_name": "Analytics Team"}),
            Action(
                name="GetEmployeeAllocations",
                kwargs={"employee_id": "emp_analyst_01"},
            ),
            Action(
                name="GetEmployeeAllocations",
                kwargs={"employee_id": "emp_analyst_02"},
            ),
            Action(
                name="GetEmployeeAllocations",
                kwargs={"employee_id": "emp_analyst_03"},
            ),
            Action(
                name="DeleteAllocation",
                kwargs={"allocation_id": "alloc_insights_02"},
            ),
            Action(
                name="CreateAllocation",
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
                name="UpdateUtilizationLog",
                kwargs={
                    "employee_id": "emp_analyst_01",
                    "new_utilization": 75,
                },
            ),
            Action(
                name="UpdateUtilizationLog",
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
        As the crisis manager, manage the abrupt cancellation of the 'Enterprise Platform' project. Identify all employees presently allocated to this project and assign each 20 hours to the project AI Platform (ID proj_ai_01). Prior to creating these new assignments, remove the allocations from the cancelled project. Ensure the 'Enterprise Platform' project is duly marked as cancelled. Finally, report the number of resources reassigned. The new allocations should have a start date of 2024-08-01 and an end date of 2024-12-31.
        """,
        actions=[
            Action(name="SearchProjects", kwargs={"name": "Enterprise Platform"}),
            Action(
                name="GetProjectAllocations",
                kwargs={"project_id": "proj_enterprise_01"},
            ),
            Action(
                name="UpdateProjectStatus",
                kwargs={"project_id": "proj_enterprise_01", "status": "cancelled"},
            ),
            Action(
                name="DeleteAllocation",
                kwargs={"allocation_id": "alloc_arch_01"},
            ),
            Action(
                name="DeleteAllocation", kwargs={"allocation_id": "alloc_devops_01"}
            ),
            Action(
                name="CreateAllocation",
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
                name="CreateAllocation",
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
        As the compliance officer, handle the new regulation requirement mandating secret clearance for ALL banking project
        staff. Assess the 'Banking Integration' project to confirm compliance. If non-compliant, revoke every allocation
        involving employees lacking secret clearance. Additionally, introduce a resource conflict marked as
        'clearance_violation'. Report if the project stands as non-compliant.
        """,
        actions=[
            Action(name="SearchProjects", kwargs={"name": "Banking Integration"}),
            Action(
                name="ValidateComplianceStatus",
                kwargs={
                    "project_id": "proj_banking_01",
                    "required_clearance": "secret",
                },
            ),
            Action(
                name="GetProjectAllocations", kwargs={"project_id": "proj_banking_01"}
            ),
            Action(
                name="GetEmployeeDetails", kwargs={"employee_id": "emp_sec_dev_01"}
            ),
            Action(
                name="CreateResourceConflict",
                kwargs={
                    "employee_id": "emp_sec_dev_01",
                    "competing_projects": ["proj_banking_01"],
                    "conflict_type": "clearance_violation",
                },
            ),
            Action(
                name="DeleteAllocation",
                kwargs={"allocation_id": "alloc_bank_01"},
            ),
            Action(
                name="UpdateEmployeesUtilization",
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
        Coordinate efforts to enhance portfolio efficiency. Examine whether any of these projects are given critical
        priority and lack resources: Mobile App Launch, AI Platform, Cloud Migration, Platform Modernization, and Banking
        Integration. For projects fitting this description, evaluate the availability of employees already committed to each and
        adjust their allocations to 40 hours. Disregard projects that have no employees assigned.
        Ultimately, provide the list of modified projects along with the total additional hours allotted to each.
        """,
        actions=[
            Action(name="SearchProjects", kwargs={"name": "Mobile App Launch"}),
            Action(name="SearchProjects", kwargs={"name": "AI Platform"}),
            Action(name="SearchProjects", kwargs={"name": "Cloud Migration"}),
            Action(name="SearchProjects", kwargs={"name": "Platform Modernization"}),
            Action(name="SearchProjects", kwargs={"name": "Banking Integration"}),
            Action(name="GetProjectAllocations", kwargs={"project_id": "proj_mobile_01"}),
            Action(name="CalculateEmployeeAvailability", kwargs={"employee_id": "emp_dev_03"}),
            Action(name="UpdateAllocation", kwargs={"allocation_id": "alloc_mobile_03", "hours_per_week": 40}),
            Action(name="GetProjectAllocations", kwargs={"project_id": "proj_ai_01"}),
            Action(name="CalculateEmployeeAvailability", kwargs={"employee_id": "emp_data_01"}),
            Action(name="UpdateAllocation", kwargs={"allocation_id": "alloc_data_01", "hours_per_week": 40}),
            Action(name="GetProjectAllocations", kwargs={"project_id": "proj_cloud_01"}),
        ],
        outputs=['"proj_mobile_01": 10', '"proj_ai_01": 8'],
    ),
    Task(
        annotator="0",
        user_id="handle_security_breach",
        instruction="""
        As an incident response manager, a security breach necessitates swift attention. Search for two employees
        possessing secret clearance to contribute to the 'Security Patch' project. Give precedence to employees skilled in 'Penetration
        Testing'. Determine the availability of the selected employees and allocate their resulting availability to the
        project. Form a team consisting of all project staff named 'Emergency Security Response Team'.
        """,
        actions=[
            Action(
                name="SearchEmployees",
                kwargs={"clearance": "secret", "skills": "Penetration Testing"},
            ),
            Action(
                name="CalculateEmployeeAvailability", kwargs={"employee_id": "emp_sec_dev_03"}
            ),
            Action(
                name="CalculateEmployeeAvailability", kwargs={"employee_id": "emp_sec_dev_02"}
            ),
            Action(
                name="SearchProjects", kwargs={"name": "Security Patch"}
            ),
            Action(
                name="GetProjectAllocations", kwargs={"project_id": "proj_security_patch"}
            ),
            Action(
                name="CreateAllocation",
                kwargs={
                    "employee_id": "emp_sec_dev_02",
                    "project_id": "proj_security_patch",
                    "hours_per_week": 10,
                    "role": "Security Developer",
                },
            ),
            Action(
                name="CreateAllocation",
                kwargs={
                    "employee_id": "emp_sec_dev_03",
                    "project_id": "proj_security_patch",
                    "hours_per_week": 40,
                    "role": "Security Developer",
                },
            ),
            Action(
                name="CreateTeam",
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
                name="UpdateEmployeesUtilization",
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
        As the lead for resource optimization, you have multiple employees concluding their projects.
        Examine the allocations with an end date before 2024-07-20. Obtain all employees from the results, calculate their
        availabilities, and allocate all their available hours to the
        Compliance Audit System project. Provide the relocated hours per each employee.
        Note: The allocation search exclusively covers projects that concluded before 2024-07-20. Thus, employee
        availability could be greater than the total allocation hours observed, because availability is calculated over
        the entire timeline, whereas the allocation search is confined to a specified period.
        """,
        actions=[
            Action(
                name="SearchAllocations",
                kwargs={"end_date_before": "2024-07-20", "status": "active"},
            ),
            Action(name="CalculateEmployeeAvailability", kwargs={"employee_id": "emp_dev_05"}),
            Action(name="CalculateEmployeeAvailability", kwargs={"employee_id": "emp_sec_test_01"}),
            Action(name="CalculateEmployeeAvailability", kwargs={"employee_id": "emp_analyst_01"}),
            Action(name="CalculateEmployeeAvailability", kwargs={"employee_id": "emp_analyst_02"}),
            Action(name="CalculateEmployeeAvailability", kwargs={"employee_id": "emp_dev_15"}),
            Action(name="CalculateEmployeeAvailability", kwargs={"employee_id": "emp_dev_03"}),
            Action(name="SearchProjects", kwargs={"name": "Compliance Audit System"}),
            Action(
                name="CreateAllocation",
                kwargs={
                    "employee_id": "emp_sec_test_01",
                    "project_id": "proj_audit_01",
                    "hours_per_week": 12,
                    "role": "Security Tester",
                },
            ),
            Action(
                name="CreateAllocation",
                kwargs={
                    "employee_id": "emp_analyst_01",
                    "project_id": "proj_audit_01",
                    "hours_per_week": 2,
                    "role": "Business Analyst",
                },
            ),
            Action(
                name="CreateAllocation",
                kwargs={
                    "employee_id": "emp_analyst_02",
                    "project_id": "proj_audit_01",
                    "hours_per_week": 8,
                    "role": "Data Analyst",
                },
            ),
            Action(
                name="CreateAllocation",
                kwargs={
                    "employee_id": "emp_dev_03",
                    "project_id": "proj_audit_01",
                    "hours_per_week": 10,
                    "role": "React Native Developer",
                },
            ),
            Action(
                name="UpdateEmployeesUtilization",
                kwargs={
                    "employee_ids": ["emp_dev_03", "emp_analyst_02", "emp_analyst_01", "emp_sec_test_01"],
                },
            ),
        ],
        outputs=['"emp_dev_03": 10', '"emp_analyst_02": 8', '"emp_analyst_01": 2', '"emp_sec_test_01": 12'],
    ),
]
