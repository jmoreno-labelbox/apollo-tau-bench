
tasks = [
    {
        "annotator": 0,
        "user_id": "resolve_resource_overallocation",
        "instruction": "\n        As a resource manager, you need to address the situation where your developer Olivia Anderson is over-allocated at 120% capacity. Examine her present assignments, pinpoint the project with lower priority, and decrease its allocation to achieve a 100% utilization rate. Present the final weekly hours and percentage of employee utilization.\n        ",
        "actions": [
            {
                "name": "SearchEmployees",
                "arguments": {
                    "name": "Olivia Anderson"
                },
            },
            {
                "name": "GetEmployeeAllocations",
                "arguments": {
                    "employee_id": "emp_dev_05"
                },
            },
            {
                "name": "GetProjectDetails",
                "arguments": {
                    "project_id": "proj_web_01"
                },
            },
            {
                "name": "GetProjectDetails",
                "arguments": {
                    "project_id": "proj_api_02"
                },
            },
            {
                "name": "CompareProjectPriorities",
                "arguments": {
                    "project_id_1": "proj_web_01",
                    "project_id_2": "proj_api_02"
                },
            },
            {
                "name": "UpdateAllocation",
                "arguments": {
                    "allocation_id": "alloc_web_01",
                    "hours_per_week": 17
                },
            },
            {
                "name": "CalculateEmployeeUtilization",
                "arguments": {
                    "employee_id": "emp_dev_05"
                },
            },
            {
                "name": "UpdateUtilizationLog",
                "arguments": {
                    "employee_id": "emp_dev_05",
                    "new_utilization": 100
                }
            }
        ],
        "outputs": [
                "\"total_hours\": 40",
                "\"utilization_percentage\": 100"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "handle_urgent_resource_request",
        "instruction": "The Engineering department has sent you an urgent request for a \"Kubernetes Expert\" to work on the 'Cloud Migration' project. Search for employees within the Engineering department who possess this skill, and if more than one is found, opt for the employee with the least utilization. Determine this employee's available hours and assign them to the 'Cloud Migration' project. Ensure the allocation begins on 2024-03-01 and ends on 2024-12-31. Update the department's capacity and provide the employee ID along with the hours allocated to the 'Cloud Migration' project.",
        "actions": [
            {
                "name": "SearchProjects",
                "arguments": {
                    "name": "Cloud Migration"
                },
            },
            {
                "name": "SearchEmployees",
                "arguments": {
                    "skills": [
                        "Kubernetes"
                    ],
                    "department": "Engineering"
                },
            },
            {
                "name": "CalculateEmployeeAvailability",
                "arguments": {
                    "employee_id": "emp_devops_04"
                },
            },
            {
                "name": "CreateAllocation",
                "arguments": {
                    "employee_id": "emp_devops_04",
                    "project_id": "proj_cloud_01",
                    "hours_per_week": 16,
                    "role": "Kubernetes Expert",
                    "start_date": "2024-03-01",
                    "end_date": "2024-12-31",
                    "status": "active"
                },
            },
            {
                "name": "UpdateUtilizationLog",
                "arguments": {
                    "employee_id": "emp_devops_04",
                    "new_utilization": 100
                },
            },
            {
                "name": "UpdateDepartmentCapacity",
                "arguments": {
                    "department": "Engineering",
                    "employee_id": "emp_devops_04",
                    "hours_allocated": 16
                }
            }
        ],
        "outputs": [
                "\"employee_id\": \"emp_devops_04\", \"hours_allocated\": 16\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "cross_department_resource_sharing",
        "instruction": "\n        As the operations director, you are tasked to assist the Engineering team in their need for a UX designer from the Design department for the 'Product Redesign' project. Look for UX designers whose utilization in the 'Design' department is below 80%. Assign 20 hours of the employee with the least utilization from your findings to the 'Product Redesign' project. The allocation should commence on \"2024-02-15\" and conclude on \"2024-07-31\". Keep in mind that this allocation involves multiple departments, and record the allocated hours.\n        ",
        "actions": [
            {
                "name": "SearchProjects",
                "arguments": {
                    "name": "Product Redesign"
                },
            },
            {
                "name": "SearchEmployees",
                "arguments": {
                    "department": "Design",
                    "role": "UX Designer",
                    "utilization_below": 80
                },
            },
            {
                "name": "CalculateEmployeeAvailability",
                "arguments": {
                    "employee_id": "emp_ux_03"
                },
            },
            {
                "name": "CreateAllocation",
                "arguments": {
                    "employee_id": "emp_ux_03",
                    "project_id": "proj_redesign_01",
                    "hours_per_week": 20,
                    "role": "UX Designer",
                    "start_date": "2024-02-15",
                    "end_date": "2024-07-31",
                    "status": "active",
                    "cross_department": true
                },
            },
            {
                "name": "UpdateUtilizationLog",
                "arguments": {
                    "employee_id": "emp_ux_03",
                    "new_utilization": 50
                },
            },
            {
                "name": "UpdateDepartmentCapacity",
                "arguments": {
                    "department": "Design",
                    "employee_id": "emp_ux_03",
                    "hours_allocated": 20,
                    "cross_department_project": "proj_redesign_01"
                }
            }
        ],
        "outputs": [
                "\"hours_allocated\": 20"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "rebalance_team_workload",
        "instruction": "As the resource planning manager, your role is to address the uneven utilization within the Analytics Team. Evaluate each team member's workload, pinpoint those who are overutilized and those who are underutilized, then adjust the assignments by reallocating 10 hours from the member with the heaviest workload to the one with the lightest. Set up the revised allocation for the Analytics Reporting project (proj_reporting_01) to begin on 2024-01-15 and end on 2024-06-30.",
        "actions": [
            {
                "name": "GetTeamDetails",
                "arguments": {
                    "team_name": "Analytics Team"
                },
            },
            {
                "name": "GetEmployeeAllocations",
                "arguments": {
                    "employee_id": "emp_analyst_01"
                },
            },
            {
                "name": "GetEmployeeAllocations",
                "arguments": {
                    "employee_id": "emp_analyst_02"
                },
            },
            {
                "name": "GetEmployeeAllocations",
                "arguments": {
                    "employee_id": "emp_analyst_03"
                },
            },
            {
                "name": "UpdateAllocation",
                "arguments": {
                    "allocation_id": "alloc_report_01",
                    "hours_per_week": 20
                },
            },
            {
                "name": "CreateAllocation",
                "arguments": {
                    "employee_id": "emp_analyst_03",
                    "project_id": "proj_reporting_01",
                    "hours_per_week": 10,
                    "role": "Junior Analyst",
                    "start_date": "2024-01-15",
                    "end_date": "2024-06-30",
                    "status": "active"
                },
            },
            {
                "name": "UpdateUtilizationLog",
                "arguments": {
                    "employee_id": "emp_analyst_01",
                    "new_utilization": 70
                },
            },
            {
                "name": "UpdateUtilizationLog",
                "arguments": {
                    "employee_id": "emp_analyst_03",
                    "new_utilization": 85
                },
            },
            {
                "name": "SummarizeWorkloadRebalance",
                "arguments": {
                    "hours_transferred": 10,
                    "from_employee": "emp_analyst_01",
                    "to_employee": "emp_analyst_03"
                }
            }
        ],
        "outputs": [
                "\"rebalanced\": true",
                "\"hours_transferred\": 10"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "emergency_project_staffing",
        "instruction": "\n        As an emergency response manager, a crucial 'Security Patch' project requires urgent staffing.\n        Locate developers with secret-level security clearance who can commit available hours to cover all necessary\n        project hours. Focus on assigning employees with lower utilization to contribute hours to the project.\n        All assignments should commence on 2024-03-15 and conclude on 2024-04-30. Present the employees assigned to the\n        'Security Patch' in this operation and the total hours.\n        ",
        "actions": [
            {
                "name": "SearchProjects",
                "arguments": {
                    "name": "Security Patch"
                },
            },
            {
                "name": "GetProjectAllocations",
                "arguments": {
                    "project_id": "proj_security_patch"
                },
            },
            {
                "name": "SearchEmployees",
                "arguments": {
                    "clearance": "secret",
                    "role_contains": "Developer"
                },
            },
            {
                "name": "CalculateEmployeeAvailability",
                "arguments": {
                    "employee_id": "emp_sec_dev_02"
                },
            },
            {
                "name": "CalculateEmployeeAvailability",
                "arguments": {
                    "employee_id": "emp_sec_dev_03"
                },
            },
            {
                "name": "CalculateEmployeeAvailability",
                "arguments": {
                    "employee_id": "emp_sec_dev_XX"
                },
            },
            {
                "name": "CreateAllocation",
                "arguments": {
                    "employee_id": "emp_sec_dev_03",
                    "project_id": "proj_security_patch",
                    "hours_per_week": 40,
                    "role": "Security Developer",
                    "start_date": "2024-03-15",
                    "end_date": "2024-04-30",
                    "status": "active"
                },
            },
            {
                "name": "CreateAllocation",
                "arguments": {
                    "employee_id": "emp_sec_dev_XX",
                    "project_id": "proj_security_patch",
                    "hours_per_week": 40,
                    "role": "Security Developer",
                    "start_date": "2024-03-15",
                    "end_date": "2024-04-30",
                    "status": "active"
                },
            },
            {
                "name": "UpdateEmployeesUtilization",
                "arguments": {
                    "employee_ids": [
                        "emp_sec_dev_03",
                        "emp_sec_dev_XX"
                    ]
                }
            }
        ],
        "outputs": [
                "\"employees_allocated\": [\"emp_sec_dev_03\", \"emp_sec_dev_XX\"]",
                "\"total_allocated_hours\": 80"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "mass_reallocation_after_cancellation",
        "instruction": "\n        As the crisis manager, the 'proj_client_01' project has been terminated. Label this project as 'cancelled' and\n        transfer all developers from the cancelled project to 'proj_enterprise_01',\n        allocating any remaining employees to 'proj_mobile_01'. Ensure that the utilization rates for\n        all moved employees remain constant. Display the employees transferred by destination project.\n        ",
        "actions": [
            {
                "name": "GetProjectAllocations",
                "arguments": {
                    "project_id": "proj_client_01"
                },
            },
            {
                "name": "UpdateProjectStatus",
                "arguments": {
                    "project_id": "proj_client_01",
                    "status": "cancelled"
                },
            },
            {
                "name": "GetEmployeeDetails",
                "arguments": {
                    "employee_id": "emp_dev_20"
                },
            },
            {
                "name": "GetEmployeeDetails",
                "arguments": {
                    "employee_id": "emp_dev_21"
                },
            },
            {
                "name": "GetEmployeeDetails",
                "arguments": {
                    "employee_id": "emp_test_05"
                },
            },
            {
                "name": "CreateAllocation",
                "arguments": {
                    "employee_id": "emp_dev_20",
                    "project_id": "proj_enterprise_01",
                    "hours_per_week": 40,
                    "role": "Frontend Developer",
                    "status": "active"
                },
            },
            {
                "name": "CreateAllocation",
                "arguments": {
                    "employee_id": "emp_dev_21",
                    "project_id": "proj_enterprise_01",
                    "hours_per_week": 40,
                    "role": "Backend Developer",
                    "status": "active"
                },
            },
            {
                "name": "CreateAllocation",
                "arguments": {
                    "employee_id": "emp_test_05",
                    "project_id": "proj_mobile_01",
                    "hours_per_week": 40,
                    "role": "Test Engineer",
                    "status": "active"
                },
            },
            {
                "name": "DeleteAllocation",
                "arguments": {
                    "allocation_id": "alloc_client_01"
                },
            },
            {
                "name": "DeleteAllocation",
                "arguments": {
                    "allocation_id": "alloc_client_02"
                },
            },
            {
                "name": "DeleteAllocation",
                "arguments": {
                    "allocation_id": "alloc_client_03"
                }
            }
        ],
        "outputs": [
                "\"proj_mobile_01_allocation\": [\"emp_dev_20\", \"emp_dev_21\"]",
                "\"proj_mobile_01_allocation\": [\"emp_test_05\"]"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "manage_bench_resources",
        "instruction": "\n        As the resource manager, you are tasked with closing projects due to finish this week.\n        Identify employees with active allocations that end on 2024-06-01 or earlier. Gather each employee's details,\n        and assign them to a bench assignment starting on 2024-06-01 with immediate availability.\n        Update each employee's status and utilization accordingly. Indicate whether a bench assignment was created.\n        ",
        "actions": [
            {
                "name": "SearchAllocations",
                "arguments": {
                    "end_date_before": "2024-06-01",
                    "status": "active"
                },
            },
            {
                "name": "GetEmployeeDetails",
                "arguments": {
                    "employee_id": "emp_dev_05"
                },
            },
            {
                "name": "CreateBenchAssignment",
                "arguments": {
                    "employee_id": "emp_dev_05",
                    "start_date": "2024-06-01",
                    "skills": [
                        "JavaScript",
                        "Python",
                        "React"
                    ],
                    "availability": "immediate"
                },
            },
            {
                "name": "UpdateEmployeeStatus",
                "arguments": {
                    "employee_id": "emp_dev_05",
                    "status": "bench",
                    "available_from": "2024-06-01"
                },
            },
            {
                "name": "UpdateUtilizationLog",
                "arguments": {
                    "employee_id": "emp_dev_05",
                    "new_utilization": 0
                }
            }
        ],
        "outputs": [
                "\"bench_assignment\": \"created\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "rotate_team_resources",
        "instruction": "\n        As the Team Lead, your team (team_analytics_01) has been working on the same project for an extended period and needs\n        rotation for skill growth. Locate team members who have been on projects for over 550 days,\n        and arrange rotation schedules (date=2024-04-01) for these individuals to the project 'proj_beta_02'. Ensure\n        the rotation hours align with the employees' utilization in their prior project, and set skill\n        development rotation to true while marking holiday coverage as false. Display the\n        employees who were given rotation schedules.\n        ",
        "actions": [
            {
                "name": "GetTeamDetails",
                "arguments": {
                    "team_id": "team_analytics_01"
                },
            },
            {
                "name": "GetEmployeeAllocations",
                "arguments": {
                    "employee_id": "emp_analyst_01"
                },
            },
            {
                "name": "CheckAllocationDuration",
                "arguments": {
                    "employee_id": "emp_analyst_01",
                    "project_id": "proj_reporting_01"
                },
            },
            {
                "name": "CheckAllocationDuration",
                "arguments": {
                    "employee_id": "emp_analyst_01",
                    "project_id": "proj_insights_01"
                },
            },
            {
                "name": "GetEmployeeAllocations",
                "arguments": {
                    "employee_id": "emp_analyst_02"
                },
            },
            {
                "name": "CheckAllocationDuration",
                "arguments": {
                    "employee_id": "emp_analyst_02",
                    "project_id": "proj_reporting_01"
                },
            },
            {
                "name": "CheckAllocationDuration",
                "arguments": {
                    "employee_id": "emp_analyst_02",
                    "project_id": "proj_insights_01"
                },
            },
            {
                "name": "GetEmployeeAllocations",
                "arguments": {
                    "employee_id": "emp_analyst_03"
                },
            },
            {
                "name": "CheckAllocationDuration",
                "arguments": {
                    "employee_id": "emp_analyst_03",
                    "project_id": "proj_gamma_03"
                },
            },
            {
                "name": "CreateRotationSchedule",
                "arguments": {
                    "employee_id": "emp_analyst_01",
                    "from_project": "proj_reporting_01",
                    "to_project": "proj_beta_02",
                    "rotation_date": "2024-04-01",
                    "hours_to_rotate": 30,
                    "skill_development_rotation": "true",
                    "holiday_coverage": "false"
                },
            },
            {
                "name": "CreateRotationSchedule",
                "arguments": {
                    "employee_id": "emp_analyst_02",
                    "from_project": "proj_reporting_01",
                    "to_project": "proj_beta_02",
                    "rotation_date": "2024-04-01",
                    "hours_to_rotate": 10,
                    "skill_development_rotation": "true",
                    "holiday_coverage": "false"
                }
            }
        ],
        "outputs": [
                "\"rotation_employees\": [\"emp_analyst_01\", \"emp_analyst_02\"]"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "optimize_resource_utilization",
        "instruction": "\n        As the resource manager, focus on optimizing the utilization of resources across various projects. Identify senior resources\n        whose utilization is below 90% and allocate all available hours following this guideline: developers should\n        be assigned to the project 'proj_security_patch' and other employees to the project 'proj_web_03'.\n        Present the allocated employees based on their destination project.\n        ",
        "actions": [
            {
                "name": "SearchEmployees",
                "arguments": {
                    "role_contains": "Senior",
                    "utilization_below": 90
                },
            },
            {
                "name": "CalculateEmployeeAvailability",
                "arguments": {
                    "employee_id": "emp_dev_03"
                },
            },
            {
                "name": "CalculateEmployeeAvailability",
                "arguments": {
                    "employee_id": "emp_data_01"
                },
            },
            {
                "name": "CalculateEmployeeAvailability",
                "arguments": {
                    "employee_id": "emp_eng_20"
                },
            },
            {
                "name": "CreateAllocation",
                "arguments": {
                    "employee_id": "emp_dev_03",
                    "project_id": "proj_security_patch",
                    "hours_per_week": 10,
                    "role": "Senior Developer",
                    "status": "active"
                },
            },
            {
                "name": "CreateAllocation",
                "arguments": {
                    "employee_id": "emp_eng_20",
                    "project_id": "proj_security_patch",
                    "hours_per_week": 8,
                    "role": "Senior Developer",
                    "status": "active"
                },
            },
            {
                "name": "CreateAllocation",
                "arguments": {
                    "employee_id": "emp_data_01",
                    "project_id": "proj_web_03",
                    "hours_per_week": 8,
                    "role": "Senior Data Analyst",
                    "status": "active"
                },
            },
            {
                "name": "UpdateUtilizationLog",
                "arguments": {
                    "employee_id": "emp_data_01",
                    "new_utilization": 100
                },
            },
            {
                "name": "UpdateUtilizationLog",
                "arguments": {
                    "employee_id": "emp_dev_03",
                    "new_utilization": 100
                },
            },
            {
                "name": "UpdateUtilizationLog",
                "arguments": {
                    "employee_id": "emp_eng_20",
                    "new_utilization": 100
                }
            }
        ],
        "outputs": [
                "\"proj_web_03_allocations\": [\"emp_data_01\"]",
                "\"proj_security_patch_allocations\": [\"emp_dev_03\", \"emp_eng_20\"]"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "redistribute_department_workload",
        "instruction": "\n        In your role as department head, address the uneven workload distribution within the QA department where some employees are overworked\n        (utilization above 90%) while others are underutilized (utilization of 70% or below). Review both overloaded and\n        underutilized employees within the QA department. For\n        those overloaded, adjust their allocations by reducing hours to reach 90% utilization. For underutilized employees, provide additional\n        hours necessary to reach 90% utilization, targeting the project 'proj_client_01'. Compute and display the overall department\n        utilization and the adjusted hours for each employee.\n        ",
        "actions": [
            {
                "name": "SearchEmployees",
                "arguments": {
                    "department": "QA",
                    "utilization_above": 90
                },
            },
            {
                "name": "GetEmployeeAllocations",
                "arguments": {
                    "employee_id": "emp_test_05"
                },
            },
            {
                "name": "UpdateAllocation",
                "arguments": {
                    "allocation_id": "alloc_client_03",
                    "hours_per_week": 36
                },
            },
            {
                "name": "SearchEmployees",
                "arguments": {
                    "department": "QA",
                    "utilization_below": 70
                },
            },
            {
                "name": "GetEmployeeAllocations",
                "arguments": {
                    "employee_id": "emp_sec_test_01"
                },
            },
            {
                "name": "GetEmployeeAllocations",
                "arguments": {
                    "employee_id": "emp_qa_02"
                },
            },
            {
                "name": "CreateAllocation",
                "arguments": {
                    "employee_id": "emp_sec_test_01",
                    "project_id": "proj_client_01",
                    "hours_per_week": 8,
                    "role": "Security Tester",
                    "status": "active"
                },
            },
            {
                "name": "CreateAllocation",
                "arguments": {
                    "employee_id": "emp_qa_02",
                    "project_id": "proj_client_01",
                    "hours_per_week": 12,
                    "role": "QA Engineer",
                    "status": "active"
                },
            },
            {
                "name": "CalculateDepartmentUtilization",
                "arguments": {
                    "department": "QA"
                },
            },
            {
                "name": "UpdateEmployeesUtilization",
                "arguments": {
                    "employee_ids": [
                        "emp_test_05",
                        "emp_qa_02",
                        "emp_sec_test_01"
                    ]
                }
            }
        ],
        "outputs": [
                "\"emp_test_05\": -4",
                "\"emp_qa_02\": 12",
                "\"emp_sec_test_01\": 8",
                "\"department_utilization\": 90"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "execute_multi_project_resource_optimization",
        "instruction": "\n        As a portfolio director, your task involves optimizing resource allocation for 2 key projects\n        (Enterprise Platform and Platform Modernization).\n        For both projects, acquire details of all\n        employees assigned, then adjust the allocations according to each employee's maximum capacity.\n        Employees participating in both projects should be excluded. Output the new utilization percentage by employee.\n        ",
        "actions": [
            {
                "name": "SearchProjects",
                "arguments": {
                    "name": "Enterprise Platform"
                },
            },
            {
                "name": "SearchProjects",
                "arguments": {
                    "name": "Platform Modernization"
                },
            },
            {
                "name": "GetProjectAllocations",
                "arguments": {
                    "project_id": "proj_enterprise_01"
                },
            },
            {
                "name": "GetProjectAllocations",
                "arguments": {
                    "project_id": "proj_platform_02"
                },
            },
            {
                "name": "GetEmployeeDetails",
                "arguments": {
                    "employee_id": "emp_devops_02"
                },
            },
            {
                "name": "UpdateAllocation",
                "arguments": {
                    "allocation_id": "alloc_devops_01",
                    "hours_per_week": 40
                },
            },
            {
                "name": "GetEmployeeDetails",
                "arguments": {
                    "employee_id": "emp_data_02"
                },
            },
            {
                "name": "UpdateAllocation",
                "arguments": {
                    "allocation_id": "alloc_data_02",
                    "hours_per_week": 40
                },
            },
            {
                "name": "GetEmployeeDetails",
                "arguments": {
                    "employee_id": "emp_devops_04"
                },
            },
            {
                "name": "UpdateAllocation",
                "arguments": {
                    "allocation_id": "alloc_devops_02",
                    "hours_per_week": 40
                },
            },
            {
                "name": "UpdateEmployeesUtilization",
                "arguments": {
                    "employee_ids": [
                        "emp_devops_02",
                        "emp_devops_04",
                        "emp_data_02"
                    ]
                }
            }
        ],
        "outputs": [
                "\"emp_devops_02\": 100",
                "\"emp_devops_04\": 100",
                "\"emp_data_02\": 100"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "emergency_resource_allocation",
        "instruction": "\n        As a project manager, your critical project 'Mobile App Launch' requires an additional developer with\n        JavaScript skills who can assist with React development (minimum proficiency 4 for both skills).\n        You need someone with at least 20 available hours weekly. If no employees with these skills have 20 hours\n        available, select the employee with these skills with the least utilization and allocate all available hours to the\n        project. Ensure to update the employee utilization percentage to 100%.\n        The allocation must utilize a start_date of 2024-01-15 and an end_date of 2024-06-30. Output the allocation ID and the allocated\n        hours\n\n        ",
        "actions": [
            {
                "name": "SearchProjects",
                "arguments": {
                    "name": "Mobile App Launch"
                },
            },
            {
                "name": "GetProjectDetails",
                "arguments": {
                    "project_id": "proj_mobile_01"
                },
            },
            {
                "name": "SearchEmployees",
                "arguments": {
                    "skills": [
                        "JavaScript",
                        "React"
                    ],
                    "min_proficiency": 4,
                    "min_skill_matches": 2,
                    "min_available_hours": 20
                },
            },
            {
                "name": "SearchEmployees",
                "arguments": {
                    "skills": [
                        "JavaScript",
                        "React"
                    ],
                    "min_proficiency": 4,
                    "min_skill_matches": 2
                },
            },
            {
                "name": "CalculateEmployeeAvailability",
                "arguments": {
                    "employee_id": "emp_eng_20"
                },
            },
            {
                "name": "CreateAllocation",
                "arguments": {
                    "allocation_id": "alloc_mobile_04",
                    "employee_id": "emp_eng_20",
                    "project_id": "proj_mobile_01",
                    "hours_per_week": 8,
                    "role": "Senior Developer",
                    "start_date": "2024-01-15",
                    "end_date": "2024-06-30",
                    "status": "active"
                },
            },
            {
                "name": "UpdateUtilizationLog",
                "arguments": {
                    "employee_id": "emp_eng_20",
                    "new_utilization": 100
                }
            }
        ],
        "outputs": [
                "\"allocation_id\": \"alloc_mobile_04\"",
                "\"hours_per_week\": 8",
                "\"status\": \"active\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "skill_based_team_expansion",
        "instruction": "\n        Assume the role of the HR director. The 'Customer Insights' project is in need of additional staff. Identify a non-junior\n        employee with a utilization rate of 70% or below to work on Python-related tasks, and a junior employee possessing SQL skills whose\n        utilization is at 60% or less. In the event of having several\n        candidates, opt for the one with the lowest utilization percentage; if there's a tie, select the first individual\n        listed in the search results. Assign to the project the lesser value between 30 and the available hours of the selected\n        employees. The duration of the allocation should align with the project's timeframe. Provide the\n        hours assigned per employee ID. Report the newly assigned team members, the total allocated hours within\n        the workflow, and the project's cumulative hours.\n        ",
        "actions": [
            {
                "name": "SearchProjects",
                "arguments": {
                    "name": "Customer Insights"
                },
            },
            {
                "name": "GetProjectDetails",
                "arguments": {
                    "project_id": "proj_insights_01"
                },
            },
            {
                "name": "GetProjectAllocations",
                "arguments": {
                    "project_id": "proj_insights_01"
                },
            },
            {
                "name": "SearchEmployees",
                "arguments": {
                    "skills": [
                        "Python"
                    ],
                    "utilization_below": 70,
                    "role_disregard": "Junior"
                },
            },
            {
                "name": "SearchEmployees",
                "arguments": {
                    "skills": [
                        "SQL"
                    ],
                    "utilization_below": 60,
                    "role_contains": "Junior"
                },
            },
            {
                "name": "CalculateEmployeeAvailability",
                "arguments": {
                    "employee_id": "emp_analyst_03"
                },
            },
            {
                "name": "CalculateEmployeeAvailability",
                "arguments": {
                    "employee_id": "emp_sec_dev_03"
                },
            },
            {
                "name": "CreateAllocation",
                "arguments": {
                    "allocation_id": "alloc_insights_04",
                    "employee_id": "emp_analyst_03",
                    "project_id": "proj_insights_01",
                    "hours_per_week": 16,
                    "role": "Junior Analyst",
                    "start_date": "2024-02-01",
                    "end_date": "2024-08-31",
                    "status": "active"
                },
            },
            {
                "name": "CreateAllocation",
                "arguments": {
                    "allocation_id": "alloc_insights_05",
                    "employee_id": "emp_sec_dev_03",
                    "project_id": "proj_insights_01",
                    "hours_per_week": 30,
                    "role": "Security Developer",
                    "start_date": "2024-02-01",
                    "end_date": "2024-08-31",
                    "status": "active"
                },
            },
            {
                "name": "UpdateUtilizationLog",
                "arguments": {
                    "employee_id": "emp_analyst_03",
                    "new_utilization": 100
                },
            },
            {
                "name": "UpdateUtilizationLog",
                "arguments": {
                    "employee_id": "emp_sec_dev_03",
                    "new_utilization": 75
                }
            }
        ],
        "outputs": [
                "\"new_team_members\": [\"emp_analyst_03\", \"emp_sec_dev_03\"]",
                "\"additional_hours\": 46",
                "\"total_hours\": 76"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "fill_multiple_skill_gaps",
        "instruction": "\n        The 'AI Platform' project necessitates Machine Learning engineers with a proficiency level of 4 or above. Seek out available\n        employees to satisfy this requirement. Determine the availability\n        of employees from the search results. If no employees fitting the criteria are located, or the summed\n        available hours combined with the project\u2019s allocated hours fall short of the necessary project hours,\n        initiate an urgent resource request (id=req_ai_ml_01) for external recruitment to cover the shortfall in hours required for\n        the project. Indicate if a skill gap was detected, along with the request ID and the requested hours.\n        ",
        "actions": [
            {
                "name": "SearchProjects",
                "arguments": {
                    "name": "AI Platform"
                },
            },
            {
                "name": "GetProjectDetails",
                "arguments": {
                    "project_id": "proj_ai_01"
                },
            },
            {
                "name": "SearchEmployees",
                "arguments": {
                    "skills": [
                        "Machine Learning"
                    ],
                    "min_proficiency": 4
                },
            },
            {
                "name": "CreateResourceRequest",
                "arguments": {
                    "request_id": "req_ai_ml_01",
                    "project_id": "proj_ai_01",
                    "skill_required": "Machine Learning",
                    "hours_needed": 88,
                    "urgency": "urgent",
                    "department": "Engineering"
                }
            }
        ],
        "outputs": [
                "\"skill_gap_identified\": true",
                "\"request_id\": \"req_ai_ml_01\"",
                "\"hours_needed\": 88"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "consolidate_project_teams",
        "instruction": "\n        As the integration director, your role is to manage the merging of three projects: Alpha Module, Beta\n        Module, and Gamma Module. Locate these projects and utilize Alpha Module as the overarching project. Reassign all team members from the merged projects into the unified project. If the transferred employees are not already part of the Alpha Module, establish new allocations; otherwise, simply modify the existing allocations. Retain the original start/end dates for current allocations, while adopting the unified project's start/end dates for new allocations. Eliminate the allocations\n        from the merged projects, and designate these as cancelled. Adjust the unified project's required hours to reflect the cumulative required hours of all three projects. Form a team named \"Alpha Unified Team\" incorporating the employees from the new unified project and provide a consolidation summary including the team size, total allocation hours, and the unified project ID.\n        ",
        "actions": [
            {
                "name": "SearchProjects",
                "arguments": {
                    "name": "Alpha Module"
                },
            },
            {
                "name": "SearchProjects",
                "arguments": {
                    "name": "Beta Module"
                },
            },
            {
                "name": "SearchProjects",
                "arguments": {
                    "name": "Gamma Module"
                },
            },
            {
                "name": "GetProjectDetails",
                "arguments": {
                    "project_id": "proj_alpha_01"
                },
            },
            {
                "name": "GetProjectDetails",
                "arguments": {
                    "project_id": "proj_beta_02"
                },
            },
            {
                "name": "GetProjectDetails",
                "arguments": {
                    "project_id": "proj_gamma_03"
                },
            },
            {
                "name": "GetProjectAllocations",
                "arguments": {
                    "project_id": "proj_alpha_01"
                },
            },
            {
                "name": "GetProjectAllocations",
                "arguments": {
                    "project_id": "proj_beta_02"
                },
            },
            {
                "name": "GetProjectAllocations",
                "arguments": {
                    "project_id": "proj_gamma_03"
                },
            },
            {
                "name": "UpdateAllocation",
                "arguments": {
                    "allocation_id": "alloc_alpha_01",
                    "hours_per_week": 60
                },
            },
            {
                "name": "DeleteAllocation",
                "arguments": {
                    "allocation_id": "alloc_beta_01"
                },
            },
            {
                "name": "DeleteAllocation",
                "arguments": {
                    "allocation_id": "alloc_gamma_01"
                },
            },
            {
                "name": "CreateAllocation",
                "arguments": {
                    "allocation_id": "alloc_alpha_03",
                    "employee_id": "emp_qa_02",
                    "project_id": "proj_alpha_01",
                    "hours_per_week": 24,
                    "role": "QA Engineer",
                    "start_date": "2024-01-01",
                    "end_date": "2024-06-30",
                    "status": "active"
                },
            },
            {
                "name": "DeleteAllocation",
                "arguments": {
                    "allocation_id": "alloc_analyst_03"
                },
            },
            {
                "name": "CreateAllocation",
                "arguments": {
                    "allocation_id": "alloc_alpha_04",
                    "employee_id": "emp_analyst_03",
                    "project_id": "proj_alpha_01",
                    "hours_per_week": 24,
                    "role": "Junior Analyst",
                    "start_date": "2024-01-01",
                    "end_date": "2024-06-30",
                    "status": "active"
                },
            },
            {
                "name": "CreateTeam",
                "arguments": {
                    "team_id": "team_alpha_unified",
                    "team_name": "Alpha Unified Team",
                    "project_id": "proj_alpha_01",
                    "team_members": [
                        "emp_dev_15",
                        "emp_qa_02",
                        "emp_analyst_03"
                    ]
                },
            },
            {
                "name": "UpdateProjectStatus",
                "arguments": {
                    "project_id": "proj_beta_02",
                    "status": "cancelled"
                },
            },
            {
                "name": "UpdateProjectStatus",
                "arguments": {
                    "project_id": "proj_gamma_03",
                    "status": "cancelled"
                },
            },
            {
                "name": "UpdateProjectRequiredHours",
                "arguments": {
                    "project_id": "proj_alpha_01",
                    "required_hours": "180"
                }
            }
        ],
        "outputs": [
                "\"consolidated_to\": \"proj_alpha_01\"",
                "\"total_hours\": 108",
                "\"team_size\": 3"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "handle_clearance_requirement_change",
        "instruction": "\n        As the security compliance manager, your task is to address the new requirement for the 'Banking Integration' project, which now mandates secret clearance for all team members due to updated regulatory rules. Examine current allocations, pinpoint employees without the necessary clearance, and seek replacements who possess secret clearance, holding the same job roles and availability as the employees being replaced, ensuring all replaced employees' allocated hours are covered. Finally, compile the list of employees removed and added to the project, and provide the compliance status validation.\n        The allocations should have a start_date of 2024-01-01 and an end_date of 2024-08-31.\n        ",
        "actions": [
            {
                "name": "SearchProjects",
                "arguments": {
                    "name": "Banking Integration"
                },
            },
            {
                "name": "GetProjectAllocations",
                "arguments": {
                    "project_id": "proj_banking_01"
                },
            },
            {
                "name": "GetEmployeeDetails",
                "arguments": {
                    "employee_id": "emp_sec_dev_01"
                },
            },
            {
                "name": "SearchEmployees",
                "arguments": {
                    "clearance": "secret",
                    "role_contains": "Security Developer",
                    "min_available_hours": 40
                },
            },
            {
                "name": "CalculateEmployeeAvailability",
                "arguments": {
                    "employee_id": "emp_sec_dev_XX"
                },
            },
            {
                "name": "CreateResourceConflict",
                "arguments": {
                    "employee_id": "emp_sec_dev_01",
                    "competing_projects": [
                        "proj_banking_01"
                    ],
                    "conflict_type": "clearance_violation"
                },
            },
            {
                "name": "DeleteAllocation",
                "arguments": {
                    "allocation_id": "alloc_bank_01"
                },
            },
            {
                "name": "CreateAllocation",
                "arguments": {
                    "employee_id": "emp_sec_dev_XX",
                    "project_id": "proj_banking_01",
                    "hours_per_week": 40,
                    "role": "Security Developer",
                    "start_date": "2024-01-01",
                    "end_date": "2024-08-31",
                    "status": "active"
                },
            },
            {
                "name": "UpdateEmployeesUtilization",
                "arguments": {
                    "employee_ids": [
                        "emp_sec_dev_XX",
                        "emp_sec_dev_01"
                    ]
                },
            },
            {
                "name": "ValidateComplianceStatus",
                "arguments": {
                    "project_id": "proj_banking_01",
                    "required_clearance": "secret"
                }
            }
        ],
        "outputs": [
                "\"employees_removed\": \"emp_sec_dev_01\"",
                "\"employees_added\": \"emp_sec_dev_XX\"",
                "\"compliance_achieved\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "manage_skill_shortage_cascade",
        "instruction": "\n        As the talent director, handle the critical skill shortage resulting from the resignation of three senior Machine Learning engineers\n        from the 'AI Platform' project. Dedicate 92 hours to this project. Initially, assign all available hours from employees possessing 'Machine Learning' skills.\n        If these hours do not reach the required 92, look for employees with Python skills, proficiency of 4 or higher, and an 85% utilization rate or below.\n        Prioritize lower utilization percentages, and in the event of a tie, select the first employee listed in search results.\n        Endeavor to allocate all available hours per priority until reaching a total of 92.\n        Form the 'AI Emergency Response Team' with the new staff arrangement for the project and place an immediate resource request for external hiring requiring 70 hours, with the skill 'Machine Learning' in the 'Engineering' department.\n        Present the project hours allocated by employees.\n        ",
        "actions": [
            {
                "name": "SearchProjects",
                "arguments": {
                    "name": "AI Platform"
                },
            },
            {
                "name": "GetProjectAllocations",
                "arguments": {
                    "project_id": "proj_ai_01"
                },
            },
            {
                "name": "SearchEmployees",
                "arguments": {
                    "skills": [
                        "Machine Learning"
                    ]
                },
            },
            {
                "name": "CalculateEmployeeAvailability",
                "arguments": {
                    "employee_id": "emp_data_01"
                },
            },
            {
                "name": "UpdateAllocation",
                "arguments": {
                    "allocation_id": "alloc_data_01",
                    "hours_per_week": 40
                },
            },
            {
                "name": "UpdateUtilizationLog",
                "arguments": {
                    "employee_id": "emp_data_01",
                    "new_utilization": 100
                },
            },
            {
                "name": "SearchEmployees",
                "arguments": {
                    "skills": [
                        "Python"
                    ],
                    "min_proficiency": 4,
                    "utilization_below": 85
                },
            },
            {
                "name": "CalculateEmployeeAvailability",
                "arguments": {
                    "employee_id": "emp_sec_dev_XX"
                },
            },
            {
                "name": "CreateAllocation",
                "arguments": {
                    "employee_id": "emp_sec_dev_XX",
                    "project_id": "proj_ai_01",
                    "hours_per_week": 40,
                    "role": "Security Developer",
                    "status": "active"
                },
            },
            {
                "name": "CalculateEmployeeAvailability",
                "arguments": {
                    "employee_id": "emp_data_02"
                },
            },
            {
                "name": "CreateAllocation",
                "arguments": {
                    "employee_id": "emp_data_02",
                    "project_id": "proj_ai_01",
                    "hours_per_week": 12,
                    "role": "Data Engineer",
                    "status": "active"
                },
            },
            {
                "name": "CreateResourceRequest",
                "arguments": {
                    "project_id": "proj_ai_01",
                    "skill_required": "Machine Learning",
                    "hours_needed": 70,
                    "urgency": "urgent",
                    "department": "Engineering"
                },
            },
            {
                "name": "CreateTeam",
                "arguments": {
                    "team_name": "AI Emergency Response Team",
                    "project_id": "proj_ai_01",
                    "team_members": [
                        "emp_data_02",
                        "emp_sec_dev_XX",
                        "emp_data_01"
                    ]
                },
            },
            {
                "name": "UpdateEmployeesUtilization",
                "arguments": {
                    "employee_ids": [
                        "emp_data_02",
                        "emp_sec_dev_XX",
                        "emp_data_01"
                    ]
                }
            }
        ],
        "outputs": [
                "\"emp_data_01\": 40",
                "\"emp_sec_dev_XX\": 40",
                "\"emp_data_02\": 12"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "optimize_resource_allocation_efficiency",
        "instruction": "\n        As the asset optimization specialist, address the resource\n        allocation issues in the 'Enterprise Platform' project, where senior architects are performing junior-level tasks. Evaluate the current allocations and, for each senior\n        employee, find a junior employee to substitute them. Follow this example for locating junior\n        employees: for every senior in the project, identify an employee with 'Junior' in their job role and\n        possessing at least 2 of the 3 skills listed in the senior employee's details. Moreover, use the senior employee's\n        allocated hours as 'min_available_hours' in the employee search. Once a suitable junior employee meeting the conditions is identified, transfer the senior employee's hours to the junior employee and remove the allocation for the senior employee.\n        If there are multiple junior employee options, select the first\n        employee in the search results. Calculate the project's optimization metrics and report the efficiency improvement.\n        ",
        "actions": [
            {
                "name": "SearchProjects",
                "arguments": {
                    "name": "Enterprise Platform"
                },
            },
            {
                "name": "GetProjectDetails",
                "arguments": {
                    "project_id": "proj_enterprise_01"
                },
            },
            {
                "name": "GetProjectAllocations",
                "arguments": {
                    "project_id": "proj_enterprise_01"
                },
            },
            {
                "name": "GetEmployeeDetails",
                "arguments": {
                    "employee_id": "emp_arch_01"
                },
            },
            {
                "name": "SearchEmployees",
                "arguments": {
                    "skills": [
                        "System Design",
                        "Cloud Architecture",
                        "Microservices"
                    ],
                    "min_skill_matches": 2,
                    "role_contains": "Junior",
                    "min_available_hours": 20
                },
            },
            {
                "name": "CalculateEmployeeAvailability",
                "arguments": {
                    "employee_id": "emp_jr_arch_01"
                },
            },
            {
                "name": "DeleteAllocation",
                "arguments": {
                    "allocation_id": "alloc_arch_01"
                },
            },
            {
                "name": "CreateAllocation",
                "arguments": {
                    "employee_id": "emp_jr_arch_01",
                    "project_id": "proj_enterprise_01",
                    "hours_per_week": 20,
                    "role": "Junior Architect",
                    "status": "active"
                },
            },
            {
                "name": "UpdateEmployeesUtilization",
                "arguments": {
                    "employee_ids": [
                        "emp_jr_arch_01",
                        "emp_arch_01"
                    ]
                },
            },
            {
                "name": "CalculateOptimizationMetrics",
                "arguments": {
                    "projects": [
                        "proj_enterprise_01"
                    ],
                    "metric_type": "efficiency_gain"
                }
            }
        ],
        "outputs": [
                "\"efficiency_gain\": 28"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "handle_department_merger",
        "instruction": "\n        As the lead for restructuring, the task is to merge the Analytics and QA departments into the new 'Quality Analytics'\n        department. Appoint the Analytics head to oversee this newly formed department, eliminating the prior departments.\n        Ensure to update the team and employee registry reflecting the merger. Provide the total capacity and allocated hours for the new department.\n        ",
        "actions": [
            {
                "name": "GetDepartmentTeams",
                "arguments": {
                    "department": "Analytics"
                },
            },
            {
                "name": "GetDepartmentTeams",
                "arguments": {
                    "department": "QA"
                },
            },
            {
                "name": "SearchEmployees",
                "arguments": {
                    "department": "Analytics"
                },
            },
            {
                "name": "SearchEmployees",
                "arguments": {
                    "department": "QA"
                },
            },
            {
                "name": "GetDepartmentTeams",
                "arguments": {
                    "department": "Analytics"
                },
            },
            {
                "name": "GetDepartmentDetails",
                "arguments": {
                    "name": "Analytics"
                },
            },
            {
                "name": "CreateDepartment",
                "arguments": {
                    "name": "Quality Analytics",
                    "head_id": "emp_head_analytics"
                },
            },
            {
                "name": "UpdateTeamsDepartment",
                "arguments": {
                    "team_id": "team_analytics_01",
                    "department": "Quality Analytics"
                },
            },
            {
                "name": "UpdateTeamsDepartment",
                "arguments": {
                    "team_id": "team_qa_01",
                    "department": "Quality Analytics"
                },
            },
            {
                "name": "UpdateTeamsDepartment",
                "arguments": {
                    "team_id": "team_qa_02",
                    "department": "Quality Analytics"
                },
            },
            {
                "name": "UpdateEmployeesDepartment",
                "arguments": {
                    "employee_id": "emp_data_01",
                    "department": "Quality Analytics"
                },
            },
            {
                "name": "UpdateEmployeesDepartment",
                "arguments": {
                    "employee_id": "emp_data_02",
                    "department": "Quality Analytics"
                },
            },
            {
                "name": "UpdateEmployeesDepartment",
                "arguments": {
                    "employee_id": "emp_analyst_01",
                    "department": "Quality Analytics"
                },
            },
            {
                "name": "UpdateEmployeesDepartment",
                "arguments": {
                    "employee_id": "emp_analyst_02",
                    "department": "Quality Analytics"
                },
            },
            {
                "name": "UpdateEmployeesDepartment",
                "arguments": {
                    "employee_id": "emp_analyst_03",
                    "department": "Quality Analytics"
                },
            },
            {
                "name": "UpdateEmployeesDepartment",
                "arguments": {
                    "employee_id": "emp_sec_test_01",
                    "department": "Quality Analytics"
                },
            },
            {
                "name": "UpdateEmployeesDepartment",
                "arguments": {
                    "employee_id": "emp_qa_02",
                    "department": "Quality Analytics"
                },
            },
            {
                "name": "UpdateEmployeesDepartment",
                "arguments": {
                    "employee_id": "emp_test_05",
                    "department": "Quality Analytics"
                },
            },
            {
                "name": "DeleteDepartment",
                "arguments": {
                    "name": "Analytics"
                },
            },
            {
                "name": "DeleteDepartment",
                "arguments": {
                    "name": "QA"
                },
            },
            {
                "name": "UpdateDepartmentsUtilization",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetDepartmentDetails",
                "arguments": {
                    "name": "Quality Analytics"
                }
            }
        ],
        "outputs": [
                "\"total_capacity\": 320",
                "\"allocated_hours\": 244"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "implement_skills_development_rotation",
        "instruction": "\n        As the manager overseeing skills development, coordinate a rotation program where junior developers dedicate 25% of their time\n        (10 hours/week) to advanced projects for enhancing skills. Identify junior developers engaged in projects who demonstrate high potential\n        (proficiency 3+), decrease their present allocations by 10 hours, and assign those 10 hours to the 'Enterprise Platform'\n        senior-led project. Set allocation timelines beginning 'start_date' 2024-04-01, concluding 'end_date' 2024-06-30. Establish the rotation\n        commencement date as 2024-04-01, ensuring the holiday coverage is set to false and skill development rotation to true.\n        Present the count of developers involved in rotation and the cumulative skills development hours.\n        ",
        "actions": [
            {
                "name": "SearchEmployees",
                "arguments": {
                    "role_contains": "Junior",
                    "min_proficiency": 3
                },
            },
            {
                "name": "GetEmployeeAllocations",
                "arguments": {
                    "employee_id": "emp_analyst_03"
                },
            },
            {
                "name": "GetEmployeeAllocations",
                "arguments": {
                    "employee_id": "emp_jr_arch_01"
                },
            },
            {
                "name": "GetEmployeeDetails",
                "arguments": {
                    "employee_id": "emp_analyst_03"
                },
            },
            {
                "name": "SearchProjects",
                "arguments": {
                    "name": "Enterprise Platform"
                },
            },
            {
                "name": "GetProjectDetails",
                "arguments": {
                    "project_id": "proj_enterprise_01"
                },
            },
            {
                "name": "UpdateAllocation",
                "arguments": {
                    "allocation_id": "alloc_analyst_03",
                    "hours_per_week": 14
                },
            },
            {
                "name": "CreateAllocation",
                "arguments": {
                    "employee_id": "emp_analyst_03",
                    "project_id": "proj_enterprise_01",
                    "hours_per_week": 10,
                    "role": "Junior Analyst",
                    "start_date": "2024-04-01",
                    "end_date": "2024-06-30",
                    "status": "active"
                },
            },
            {
                "name": "CreateRotationSchedule",
                "arguments": {
                    "employee_id": "emp_analyst_03",
                    "from_project": "proj_gamma_03",
                    "to_project": "proj_enterprise_01",
                    "rotation_date": "2024-04-01",
                    "hours_to_rotate": 10,
                    "skill_development_rotation": "true",
                    "holiday_coverage": "false"
                }
            }
        ],
        "outputs": [
                "\"developers_in_rotation\": 1",
                "\"skill_development_hours\": 10"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "manage_project_phase_transition",
        "instruction": "\n        As the program manager, oversee the transition of the 'Mobile App Launch' project from development to the testing phase\n        on April 1st. Reduce developer allocations to a total of 20 hours per week, and increase QA resources to 10 hours per week by\n        identifying QA staff with utilization under 80%. Give priority to employees with less utilization. The new allocations\n        should start on 2024-04-01 and end on 2024-06-30. Provide the outcomes for project development hours and QA hours.\n        ",
        "actions": [
            {
                "name": "SearchProjects",
                "arguments": {
                    "name": "Mobile App Launch"
                },
            },
            {
                "name": "GetProjectDetails",
                "arguments": {
                    "project_id": "proj_mobile_01"
                },
            },
            {
                "name": "GetProjectAllocations",
                "arguments": {
                    "project_id": "proj_mobile_01"
                },
            },
            {
                "name": "UpdateAllocation",
                "arguments": {
                    "allocation_id": "alloc_mobile_03",
                    "hours_per_week": 20
                },
            },
            {
                "name": "SearchEmployees",
                "arguments": {
                    "department": "QA",
                    "utilization_below": 80
                },
            },
            {
                "name": "CalculateEmployeeAvailability",
                "arguments": {
                    "employee_id": "emp_qa_02"
                },
            },
            {
                "name": "CalculateEmployeeAvailability",
                "arguments": {
                    "employee_id": "emp_sec_test_01"
                },
            },
            {
                "name": "CreateAllocation",
                "arguments": {
                    "employee_id": "emp_qa_02",
                    "project_id": "proj_mobile_01",
                    "hours_per_week": 10,
                    "role": "QA Engineer",
                    "start_date": "2024-04-01",
                    "end_date": "2024-06-30",
                    "status": "active"
                },
            },
            {
                "name": "UpdateEmployeesUtilization",
                "arguments": {
                    "employee_ids": [
                        "emp_qa_02",
                        "emp_dev_03"
                    ]
                },
            },
            {
                "name": "SummarizeProjectPhaseMetrics",
                "arguments": {
                    "project_id": "proj_mobile_01"
                }
            }
        ],
        "outputs": [
                "\"dev_hours\": 20",
                "\"qa_hours\": 10"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "implement_rotation_schedules_across_projects",
        "instruction": "\n        As an operations manager, devise skill development rotation schedules for the employees of the\n        projects: 'Banking Integration' and 'Customer Portal'. Ensure a rotation schedule is established for each employee of the\n        'Customer Portal' to rotate into 'Banking Integration'. Repeat the process for employees\n        from 'Banking Integration' to the 'Customer Portal'. Set the rotation date as \"2024-12-23\",\n        ensure 20 rotation hours, and configure the 'holiday_coverage' parameter to false, with skill\n        development rotation marked as true. List the employees involved in the rotation.\n        ",
        "actions": [
            {
                "name": "SearchProjects",
                "arguments": {
                    "name": "Banking Integration"
                },
            },
            {
                "name": "SearchProjects",
                "arguments": {
                    "name": "Customer Portal"
                },
            },
            {
                "name": "GetProjectAllocations",
                "arguments": {
                    "project_id": "proj_banking_01"
                },
            },
            {
                "name": "GetProjectAllocations",
                "arguments": {
                    "project_id": "proj_web_03"
                },
            },
            {
                "name": "CreateRotationSchedule",
                "arguments": {
                    "employee_id": "emp_sec_dev_01",
                    "from_project": "proj_banking_01",
                    "to_project": "proj_web_03",
                    "rotation_date": "2024-12-23",
                    "hours_to_rotate": 20,
                    "skill_development_rotation": "true",
                    "holiday_coverage": "false"
                },
            },
            {
                "name": "CreateRotationSchedule",
                "arguments": {
                    "employee_id": "emp_eng_20",
                    "from_project": "proj_web_03",
                    "to_project": "proj_banking_01",
                    "rotation_date": "2024-12-23",
                    "hours_to_rotate": 20,
                    "skill_development_rotation": "true",
                    "holiday_coverage": "false"
                }
            }
        ],
        "outputs": [
                "\"employees_in_rotation\": [\"emp_sec_dev_01\", \"emp_eng_20\"]"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "balance_remote_onsite_allocation",
        "instruction": "\n        As the hybrid work coordinator, it is your responsibility to manage the 'Enterprise Platform' project, which requires an onsite presence of 40%.\n        Gather details for each employee involved in the project to compute the total hours dedicated by those who are able to work onsite.\n        If the current total hours are insufficient to meet the 40% requirement, locate a team member from the Engineering department eligible for onsite work, prioritizing those with lower capacity\n        and possessing the 'Mathematics' skill. Reallocate the available hours for the employee to meet the necessary onsite percentage.\n        Ensure that the allocations commence from start_date 2024-02-01 and conclude on end_date 2024-12-31. Provide the sum of onsite hours,\n        incorporating both prior and adjusted allocations.\n        ",
        "actions": [
            {
                "name": "SearchProjects",
                "arguments": {
                    "name": "Enterprise Platform"
                },
            },
            {
                "name": "GetProjectDetails",
                "arguments": {
                    "project_id": "proj_enterprise_01"
                },
            },
            {
                "name": "GetProjectAllocations",
                "arguments": {
                    "project_id": "proj_enterprise_01"
                },
            },
            {
                "name": "GetEmployeeDetails",
                "arguments": {
                    "employee_id": "emp_devops_02"
                },
            },
            {
                "name": "GetEmployeeDetails",
                "arguments": {
                    "employee_id": "emp_arch_01"
                },
            },
            {
                "name": "SearchEmployees",
                "arguments": {
                    "department": "Engineering",
                    "skills": [
                        "Mathematics"
                    ]
                },
            },
            {
                "name": "CreateAllocation",
                "arguments": {
                    "employee_id": "emp_dev_08",
                    "project_id": "proj_enterprise_01",
                    "hours_per_week": 8,
                    "role": "Backend Developer",
                    "start_date": "2024-02-01",
                    "end_date": "2024-12-31",
                    "status": "active"
                }
            }
        ],
        "outputs": [
                "\"onsite_hours\": 64"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "optimize_docker_expertise",
        "instruction": "\n        In your capacity as the DevOps manager, you need to address the urgent requirement for Docker expertise (proficiency 5) in the 'Platform Modernization' project.\n        Identify employees with a Docker skill level of 5, confirm they are utilized at less than 80%, and assign 10 hours/week\n        to the project. Return the resulting utilization percentage of the employee who has been allocated. Plan this allocation with\n        start_date 2024-03-01 and end_date 2024-10-31.\n        ",
        "actions": [
            {
                "name": "SearchProjects",
                "arguments": {
                    "name": "Platform Modernization"
                },
            },
            {
                "name": "SearchEmployees",
                "arguments": {
                    "skills": [
                        "Docker"
                    ],
                    "min_proficiency": 5,
                    "utilization_below": 80
                },
            },
            {
                "name": "GetEmployeeAllocations",
                "arguments": {
                    "employee_id": "emp_devops_04"
                },
            },
            {
                "name": "CalculateEmployeeAvailability",
                "arguments": {
                    "employee_id": "emp_devops_04"
                },
            },
            {
                "name": "CreateAllocation",
                "arguments": {
                    "employee_id": "emp_devops_04",
                    "project_id": "proj_platform_02",
                    "hours_per_week": 10,
                    "role": "DevOps Engineer",
                    "start_date": "2024-03-01",
                    "end_date": "2024-10-31",
                    "status": "active"
                },
            },
            {
                "name": "CalculateEmployeeUtilization",
                "arguments": {
                    "employee_id": "emp_devops_04"
                }
            }
        ],
        "outputs": [
                "85"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "create_security_taskforce",
        "instruction": "\n        As the CISO, you need to establish a security task force for the 'Security Patch' project. Identify 2 developers and 1\n        tester with the necessary security clearance, assess their availability, and form a team named 'Security Task Force'.\n        Assign 10 hours of work for each member to this project. Give priority to employees with a utilization rate of 0%.\n        Report how many resources have been successfully allocated to the project.\n        ",
        "actions": [
            {
                "name": "SearchProjects",
                "arguments": {
                    "name": "Security Patch"
                },
            },
            {
                "name": "GetProjectAllocations",
                "arguments": {
                    "project_id": "proj_security_patch"
                },
            },
            {
                "name": "SearchEmployees",
                "arguments": {
                    "clearance": "secret",
                    "role_contains": "Developer"
                },
            },
            {
                "name": "SearchEmployees",
                "arguments": {
                    "clearance": "secret",
                    "role_contains": "Tester"
                },
            },
            {
                "name": "CalculateEmployeeAvailability",
                "arguments": {
                    "employee_id": "emp_sec_dev_03"
                },
            },
            {
                "name": "CalculateEmployeeAvailability",
                "arguments": {
                    "employee_id": "emp_sec_dev_XX"
                },
            },
            {
                "name": "CalculateEmployeeAvailability",
                "arguments": {
                    "employee_id": "emp_sec_test_01"
                },
            },
            {
                "name": "CreateTeam",
                "arguments": {
                    "team_name": "Security Task Force",
                    "project_id": "proj_security_patch",
                    "team_members": [
                        "emp_sec_dev_03",
                        "emp_sec_dev_XX",
                        "emp_sec_test_01"
                    ]
                },
            },
            {
                "name": "CreateAllocation",
                "arguments": {
                    "employee_id": "emp_sec_test_01",
                    "project_id": "proj_security_patch",
                    "hours_per_week": 10,
                    "role": "Security Tester",
                    "status": "active"
                },
            },
            {
                "name": "CreateAllocation",
                "arguments": {
                    "employee_id": "emp_sec_dev_XX",
                    "project_id": "proj_security_patch",
                    "hours_per_week": 10,
                    "role": "Security Developer",
                    "status": "active"
                },
            },
            {
                "name": "CreateAllocation",
                "arguments": {
                    "employee_id": "emp_sec_dev_03",
                    "project_id": "proj_security_patch",
                    "hours_per_week": 10,
                    "role": "Security Developer",
                    "status": "active"
                },
            },
            {
                "name": "ValidateComplianceStatus",
                "arguments": {
                    "project_id": "proj_security_patch",
                    "required_clearance": "secret"
                }
            }
        ],
        "outputs": [
                "3"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "create_project_and_team_analytics",
        "instruction": "\n        As a tech lead, you should initiate a new project titled \"Analytics Project\". In conjunction with this project, form a team called 'Analytics Team' comprised of employees from the Analytics department.\n        Ensure the team has a cumulative availability of at least 24 hours. Give preference to employees skilled in 'Python' and 'SQL', avoiding Junior-level staff.\n        Team members you select should maintain current utilization below 90. Assign each team member 8 hours to contribute to the project. Conclude by confirming if the\n        project and team creation was successful, and list the employees added to the team in the results.\n        ",
        "actions": [
            {
                "name": "CreateProject",
                "arguments": {
                    "department": "Analytics",
                    "project_id": "proj_analytics_01",
                    "project_name": "Analytics Project",
                    "required_hours_per_week": 24
                },
            },
            {
                "name": "SearchEmployees",
                "arguments": {
                    "department": "Analytics",
                    "utilization_below": 90,
                    "role_disregard": "Junior"
                },
            },
            {
                "name": "CalculateEmployeeUtilization",
                "arguments": {
                    "employee_id": "emp_data_01"
                },
            },
            {
                "name": "CalculateEmployeeUtilization",
                "arguments": {
                    "employee_id": "emp_data_02"
                },
            },
            {
                "name": "CalculateEmployeeUtilization",
                "arguments": {
                    "employee_id": "emp_analyst_02"
                },
            },
            {
                "name": "CreateAllocation",
                "arguments": {
                    "employee_id": "emp_data_01",
                    "project_id": "proj_analytics_01",
                    "hours_per_week": 8,
                    "role": "Senior Data Analyst",
                    "status": "active"
                },
            },
            {
                "name": "CreateAllocation",
                "arguments": {
                    "employee_id": "emp_data_02",
                    "project_id": "proj_analytics_01",
                    "hours_per_week": 8,
                    "role": "Data Engineer",
                    "status": "active"
                },
            },
            {
                "name": "CreateAllocation",
                "arguments": {
                    "employee_id": "emp_analyst_02",
                    "project_id": "proj_analytics_01",
                    "hours_per_week": 8,
                    "role": "Data Analyst",
                    "status": "active"
                },
            },
            {
                "name": "CreateTeam",
                "arguments": {
                    "team_name": "Analytics Team",
                    "project_id": "proj_analytics_01",
                    "team_members": [
                        "emp_data_01",
                        "emp_data_02",
                        "emp_analyst_02"
                    ]
                }
            }
        ],
        "outputs": [
                "\"project_created\": \"Analytics Project\"",
                "\"team_created\": \"Analytics Team\"",
                "\"employees_added\": \"emp_data_01\", \"emp_data_02\", \"emp_analyst_02\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "integrate_contract_resources",
        "instruction": "\n        You are the staffing manager. The 'Web Platform Update' project is in need of additional frontend developers.\n        Locate employees with a proficiency in React at level 4 or higher and with a utilization rate of 70% or below to allocate them to the project.\n        Initiate a resource request with standard urgency for the 'Engineering' department\n        and calculate how many hours are still required. Provide the remaining hours needed.\n        ",
        "actions": [
            {
                "name": "SearchProjects",
                "arguments": {
                    "name": "Web Platform Update"
                },
            },
            {
                "name": "GetProjectDetails",
                "arguments": {
                    "project_id": "proj_web_02"
                },
            },
            {
                "name": "SearchEmployees",
                "arguments": {
                    "skills": [
                        "React"
                    ],
                    "min_proficiency": 4,
                    "utilization_below": 70
                },
            },
            {
                "name": "CreateResourceRequest",
                "arguments": {
                    "project_id": "proj_web_02",
                    "skill_required": "React",
                    "hours_needed": 60,
                    "urgency": "normal",
                    "department": "Engineering"
                }
            }
        ],
        "outputs": [
                "60"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "optimize_architect_time",
        "instruction": "\n        As the Engineering Director, oversee Senior Architect Daniel Mitchell, who is engaged in two projects.\n        Assess the priority of each project, and remove him from the one with lower priority. Subsequently, establish\n        an allocation for a junior staff member who possesses at least two shared skills with him.\n        Ensure that the junior employee's full 40 available hours are utilized in the allocation.\n        Lastly, present the efficiency improvement percentage resulting from this change.\n        ",
        "actions": [
            {
                "name": "SearchEmployees",
                "arguments": {
                    "name": "Michael Roberts"
                },
            },
            {
                "name": "GetEmployeeAllocations",
                "arguments": {
                    "employee_id": "emp_arch_01"
                },
            },
            {
                "name": "CompareProjectPriorities",
                "arguments": {
                    "project_id_1": "proj_enterprise_01",
                    "project_id_2": "proj_platform_02"
                },
            },
            {
                "name": "SearchEmployees",
                "arguments": {
                    "skills": [
                        "System Design",
                        "Cloud Architecture",
                        "Microservices"
                    ],
                    "min_available_hours": 40,
                    "min_skill_matches": 2,
                    "role_contains": "Junior"
                },
            },
            {
                "name": "GetEmployeeAllocations",
                "arguments": {
                    "employee_id": "emp_jr_arch_01"
                },
            },
            {
                "name": "CalculateEmployeeAvailability",
                "arguments": {
                    "employee_id": "emp_jr_arch_01"
                },
            },
            {
                "name": "DeleteAllocation",
                "arguments": {
                    "allocation_id": "alloc_arch_02"
                },
            },
            {
                "name": "CreateAllocation",
                "arguments": {
                    "employee_id": "emp_jr_arch_01",
                    "project_id": "proj_platform_02",
                    "hours_per_week": 40,
                    "role": "Junior Architect",
                    "department": "Engineering"
                },
            },
            {
                "name": "UpdateEmployeesUtilization",
                "arguments": {
                    "employee_ids": [
                        "emp_jr_arch_01",
                        "emp_arch_01"
                    ]
                },
            },
            {
                "name": "CalculateOptimizationMetrics",
                "arguments": {
                    "projects": [
                        "proj_enterprise_01",
                        "proj_platform_02"
                    ],
                    "metric_type": "efficiency_gain"
                }
            }
        ],
        "outputs": [
                "25"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "manage_budget_overrun",
        "instruction": "\n        As the project controller, deal with the situation where the 'Customer Portal' project nears its budget limits. Examine current\n        resource allocations, identify junior resources with proficiency levels of 3 or higher, who have utilization rates not exceeding 80%. Determine\n        the availability of\n        the identified employees and assign their available hours to meet the project's required hours. In your allocation,\n        give priority to those with lower utilization rates. Provide a report showing the final utilization percentages of the junior employees allocated, based on their employee IDs.\n        Ensure that the new allocations commence on 2024-03-01 and conclude on 2024-10-31.\n        ",
        "actions": [
            {
                "name": "SearchProjects",
                "arguments": {
                    "name": "Customer Portal"
                },
            },
            {
                "name": "GetProjectAllocations",
                "arguments": {
                    "project_id": "proj_web_03"
                },
            },
            {
                "name": "GetProjectDetails",
                "arguments": {
                    "project_id": "proj_web_03"
                },
            },
            {
                "name": "SearchEmployees",
                "arguments": {
                    "role_contains": "Junior",
                    "min_proficiency": 3,
                    "utilization_below": 80
                },
            },
            {
                "name": "CalculateEmployeeAvailability",
                "arguments": {
                    "employee_id": "emp_jr_arch_01"
                },
            },
            {
                "name": "CalculateEmployeeAvailability",
                "arguments": {
                    "employee_id": "emp_analyst_03"
                },
            },
            {
                "name": "CreateAllocation",
                "arguments": {
                    "employee_id": "emp_analyst_03",
                    "project_id": "proj_web_03",
                    "hours_per_week": 8,
                    "role": "Junior Analyst",
                    "start_date": "2024-03-01",
                    "end_date": "2024-10-31",
                    "status": "active"
                },
            },
            {
                "name": "CreateAllocation",
                "arguments": {
                    "employee_id": "emp_jr_arch_01",
                    "project_id": "proj_web_03",
                    "hours_per_week": 40,
                    "role": "Junior Architect",
                    "start_date": "2024-03-01",
                    "end_date": "2024-10-31",
                    "status": "active"
                },
            },
            {
                "name": "UpdateEmployeesUtilization",
                "arguments": {
                    "employee_ids": [
                        "emp_analyst_03",
                        "emp_jr_arch_01"
                    ]
                }
            }
        ],
        "outputs": [
                "\"emp_jr_arch_01\": 100",
                "\"emp_analyst_03\": 80"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "expand_analytics_team",
        "instruction": "\n        As the analytics manager, handle the requirement to increase the 'Customer Insights' project's commitment from 30 to 60 hours per week.\n        Select two employees proficient in Python, whose utilization falls within [49%, 61%], and assign each 15 hours to the project.\n        Develop allocations that start on 2024-02-01 and end on 2024-08-31, and make sure to select the first two employees listed in the result.\n        Report the total number of project hours following the expansion. Be aware that the project requires 80 hours per week,\n        but for the moment, focus on adding 30 hours to the project commitment.\n        ",
        "actions": [
            {
                "name": "SearchProjects",
                "arguments": {
                    "name": "Customer Insights"
                },
            },
            {
                "name": "GetProjectAllocations",
                "arguments": {
                    "project_id": "proj_insights_01"
                },
            },
            {
                "name": "SearchEmployees",
                "arguments": {
                    "skills": [
                        "Python"
                    ],
                    "utilization_below": 61,
                    "utilization_above": 49
                },
            },
            {
                "name": "CalculateEmployeeAvailability",
                "arguments": {
                    "employee_id": "emp_qa_02"
                },
            },
            {
                "name": "CreateAllocation",
                "arguments": {
                    "employee_id": "emp_qa_02",
                    "project_id": "proj_insights_01",
                    "hours_per_week": 15,
                    "role": "QA Engineer",
                    "start_date": "2024-02-01",
                    "end_date": "2024-08-31",
                    "status": "active",
                    "cross_department": true
                },
            },
            {
                "name": "CalculateEmployeeAvailability",
                "arguments": {
                    "employee_id": "emp_analyst_03"
                },
            },
            {
                "name": "CreateAllocation",
                "arguments": {
                    "employee_id": "emp_analyst_03",
                    "project_id": "proj_insights_01",
                    "hours_per_week": 15,
                    "role": "Junior Analyst",
                    "start_date": "2024-02-01",
                    "end_date": "2024-08-31",
                    "status": "active"
                },
            },
            {
                "name": "SummarizeTeamExpansion",
                "arguments": {
                    "project_id": "proj_insights_01",
                    "new_team_members": [
                        "emp_qa_02",
                        "emp_analyst_03"
                    ],
                    "additional_hours": 30,
                    "existing_hours": 30
                }
            }
        ],
        "outputs": [
                "60"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "consolidate_web_projects",
        "instruction": "\n        As a portfolio director, you are overseeing three web projects: Web Portal Redesign, Web Platform Update, and Customer\n        Portal, which have intersecting objectives. Examine their allocations, priorities, and resources. Combine them\n        into the project with the highest priority and adjust the project statuses accordingly. In conclusion, outline the projects' consolidation, designate the highest priority project as the 'consolidate to' and categorize the other two projects as the 'consolidated projects.' Present the 'consolidate to' project, team size, and total hours.\n        ",
        "actions": [
            {
                "name": "SearchProjects",
                "arguments": {
                    "name": "Web Portal Redesign"
                },
            },
            {
                "name": "SearchProjects",
                "arguments": {
                    "name": "Web Platform Update"
                },
            },
            {
                "name": "SearchProjects",
                "arguments": {
                    "name": "Customer Portal"
                },
            },
            {
                "name": "GetProjectDetails",
                "arguments": {
                    "project_id": "proj_web_01"
                },
            },
            {
                "name": "GetProjectDetails",
                "arguments": {
                    "project_id": "proj_web_02"
                },
            },
            {
                "name": "GetProjectDetails",
                "arguments": {
                    "project_id": "proj_web_03"
                },
            },
            {
                "name": "CompareProjectPriorities",
                "arguments": {
                    "project_id_1": "proj_web_01",
                    "project_id_2": "proj_web_02"
                },
            },
            {
                "name": "CompareProjectPriorities",
                "arguments": {
                    "project_id_1": "proj_web_03",
                    "project_id_2": "proj_web_01"
                },
            },
            {
                "name": "GetProjectAllocations",
                "arguments": {
                    "project_id": "proj_web_03"
                },
            },
            {
                "name": "GetProjectAllocations",
                "arguments": {
                    "project_id": "proj_web_02"
                },
            },
            {
                "name": "GetProjectAllocations",
                "arguments": {
                    "project_id": "proj_web_01"
                },
            },
            {
                "name": "CreateAllocation",
                "arguments": {
                    "employee_id": "emp_dev_05",
                    "project_id": "proj_web_03",
                    "hours_per_week": 25,
                    "role": "Full Stack Developer",
                    "status": "active"
                },
            },
            {
                "name": "DeleteAllocation",
                "arguments": {
                    "allocation_id": "alloc_web_01"
                },
            },
            {
                "name": "UpdateProjectStatus",
                "arguments": {
                    "project_id": "proj_web_01",
                    "status": "cancelled"
                },
            },
            {
                "name": "UpdateProjectStatus",
                "arguments": {
                    "project_id": "proj_web_02",
                    "status": "cancelled"
                },
            },
            {
                "name": "SummarizeProjectConsolidation",
                "arguments": {
                    "consolidated_to": "proj_web_03",
                    "total_hours": 57,
                    "team_size": 2,
                    "consolidated_projects": [
                        "proj_web_01",
                        "proj_web_02"
                    ]
                }
            }
        ],
        "outputs": [
                "\"consolidated_to\": \"proj_web_03\"",
                "\"total_hours\": 57",
                "\"team_size\": 2"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "transition_to_testing_phase",
        "instruction": "\n        You are the transition manager tasked with overseeing the 'Mobile App Launch' project as it shifts from the development phase to the testing phase.\n        Determine the current development/QA hours distribution, cut developer allocations by 50%, identify 2 QA employees\n        with 75% utilization or less and assign them 12 hours each for the project. Establish allocations\n        starting from 2024-01-15 and concluding on 2024-06-30. Provide a report on the revised development and QA hours.\n        ",
        "actions": [
            {
                "name": "SearchProjects",
                "arguments": {
                    "name": "Mobile App Launch"
                },
            },
            {
                "name": "GetProjectAllocations",
                "arguments": {
                    "project_id": "proj_mobile_01"
                },
            },
            {
                "name": "GetEmployeeDetails",
                "arguments": {
                    "employee_id": "emp_dev_03"
                },
            },
            {
                "name": "UpdateAllocation",
                "arguments": {
                    "allocation_id": "alloc_mobile_03",
                    "hours_per_week": 15
                },
            },
            {
                "name": "SearchEmployees",
                "arguments": {
                    "department": "QA",
                    "utilization_below": 75
                },
            },
            {
                "name": "CalculateEmployeeAvailability",
                "arguments": {
                    "employee_id": "emp_qa_02"
                },
            },
            {
                "name": "CalculateEmployeeAvailability",
                "arguments": {
                    "employee_id": "emp_sec_test_01"
                },
            },
            {
                "name": "CreateAllocation",
                "arguments": {
                    "employee_id": "emp_qa_02",
                    "project_id": "proj_mobile_01",
                    "hours_per_week": 12,
                    "role": "QA Engineer",
                    "start_date": "2024-01-15",
                    "end_date": "2024-06-30",
                    "status": "active"
                },
            },
            {
                "name": "CreateAllocation",
                "arguments": {
                    "employee_id": "emp_sec_test_01",
                    "project_id": "proj_mobile_01",
                    "hours_per_week": 12,
                    "role": "Security Tester",
                    "start_date": "2024-01-15",
                    "end_date": "2024-06-30",
                    "status": "active"
                },
            },
            {
                "name": "UpdateEmployeesUtilization",
                "arguments": {
                    "employee_ids": [
                        "emp_qa_02",
                        "emp_sec_test_01",
                        "emp_dev_03"
                    ]
                },
            },
            {
                "name": "SummarizeProjectPhaseMetrics",
                "arguments": {
                    "project_id": "proj_mobile_01"
                }
            }
        ],
        "outputs": [
                "\"dev_hours\": 15",
                "\"qa_hours\": 24"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "fill_ml_expertise_gap",
        "instruction": "\n        You are tasked with directing skills development. There exists a significant Machine Learning expertise gap in the 'AI Platform' project. Seek out new employees\n        (excluding those already assigned) possessing Machine Learning abilities at any proficiency level and incorporate them into the project. If no employees\n        are identified in the initial search, look for individuals with Python skills (proficiency >= 4) and utilization at 90% or lower as potential alternatives. Select\n        the first two employees from the secondary search results, and allocate them to the project. Calculate their allocation hours by subtracting\n        the product of maximum hours per week and utilization percentage from the maximum weekly hours available.\n        Initiate an urgent resource request to obtain the hours necessary to meet the project's total required hours,\n        factoring in the project's final allocation status, specifically for employees with 'Machine Learning' expertise in the 'Engineering'\n        department. Provide the output of the hours needed to meet the project's total required hours.\n        ",
        "actions": [
            {
                "name": "SearchProjects",
                "arguments": {
                    "name": "AI Platform"
                },
            },
            {
                "name": "GetProjectDetails",
                "arguments": {
                    "project_id": "proj_ai_01"
                },
            },
            {
                "name": "GetProjectAllocations",
                "arguments": {
                    "project_id": "proj_ai_01"
                },
            },
            {
                "name": "SearchEmployees",
                "arguments": {
                    "skills": [
                        "Machine Learning"
                    ],
                    "disregard_employee_ids": [
                        "emp_data_01"
                    ]
                },
            },
            {
                "name": "SearchEmployees",
                "arguments": {
                    "skills": [
                        "Python"
                    ],
                    "min_proficiency": 4,
                    "utilization_below": 90,
                    "disregard_employee_ids": [
                        "emp_data_01"
                    ]
                },
            },
            {
                "name": "CreateAllocation",
                "arguments": {
                    "employee_id": "emp_data_02",
                    "project_id": "proj_ai_01",
                    "hours_per_week": 14,
                    "role": "Data Engineer",
                    "status": "active"
                },
            },
            {
                "name": "CreateAllocation",
                "arguments": {
                    "employee_id": "emp_dev_07",
                    "project_id": "proj_ai_01",
                    "hours_per_week": 12,
                    "role": "Backend Developer",
                    "status": "active"
                },
            },
            {
                "name": "GetProjectDetails",
                "arguments": {
                    "project_id": "proj_ai_01"
                },
            },
            {
                "name": "CreateResourceRequest",
                "arguments": {
                    "project_id": "proj_ai_01",
                    "skill_required": "Machine Learning",
                    "hours_needed": 62,
                    "urgency": "urgent",
                    "department": "Engineering"
                }
            }
        ],
        "outputs": [
                "\"hours_needed\": 62"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "balance_onsite_remote",
        "instruction": "\n        Your role is as a work coordinator. The 'Enterprise Platform' project requires an increase in onsite presence. Examine current project allocations,\n        identify one new employee capable of working onsite to contribute 30 hours to the project. Select the first employee listed in the search results. Develop an allocation\n        with a start date of 2024-02-01 and an end date of 2024-12-31. Provide the name of the employee selected.\n        ",
        "actions": [
            {
                "name": "SearchProjects",
                "arguments": {
                    "name": "Enterprise Platform"
                },
            },
            {
                "name": "GetProjectAllocations",
                "arguments": {
                    "project_id": "proj_enterprise_01"
                },
            },
            {
                "name": "GetProjectDetails",
                "arguments": {
                    "project_id": "proj_enterprise_01"
                },
            },
            {
                "name": "SearchEmployees",
                "arguments": {
                    "disregard_employee_ids": [
                        "emp_devops_02",
                        "emp_arch_01"
                    ],
                    "min_available_hours": 30
                },
            },
            {
                "name": "CalculateEmployeeAvailability",
                "arguments": {
                    "employee_id": "emp_ux_03"
                },
            },
            {
                "name": "CreateAllocation",
                "arguments": {
                    "employee_id": "emp_ux_03",
                    "project_id": "proj_enterprise_01",
                    "hours_per_week": 30,
                    "role": "UX Designer",
                    "start_date": "2024-02-01",
                    "end_date": "2024-12-31",
                    "status": "active"
                },
            },
            {
                "name": "UpdateUtilizationLog",
                "arguments": {
                    "employee_id": "emp_ux_03",
                    "new_utilization": 75
                }
            }
        ],
        "outputs": [
                "\"employee_name\": \"Grace Wang\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "rebalance_overloaded_teams",
        "instruction": "\n        As the workload manager, address the imbalanced workload of the Analytics team members, with some at 95% utilization and others at 60%. Review all team member allocations, pinpoint the most overloaded and the least utilized employee. From the overloaded employee's allocations, select the task with fewer hours and remove it. Subsequently, assign the project from the discarded allocation to the most underutilized employee, maintaining the original start and end dates. Conclude by revising employees' utilizations and display the change in hours for each employee by their ID.\n        ",
        "actions": [
            {
                "name": "GetTeamDetails",
                "arguments": {
                    "team_name": "Analytics Team"
                },
            },
            {
                "name": "GetEmployeeAllocations",
                "arguments": {
                    "employee_id": "emp_analyst_01"
                },
            },
            {
                "name": "GetEmployeeAllocations",
                "arguments": {
                    "employee_id": "emp_analyst_02"
                },
            },
            {
                "name": "GetEmployeeAllocations",
                "arguments": {
                    "employee_id": "emp_analyst_03"
                },
            },
            {
                "name": "DeleteAllocation",
                "arguments": {
                    "allocation_id": "alloc_insights_02"
                },
            },
            {
                "name": "CreateAllocation",
                "arguments": {
                    "employee_id": "emp_analyst_03",
                    "project_id": "proj_insights_01",
                    "hours_per_week": 8,
                    "role": "Junior Analyst",
                    "start_date": "2024-02-01",
                    "end_date": "2024-08-31",
                    "status": "active"
                },
            },
            {
                "name": "UpdateUtilizationLog",
                "arguments": {
                    "employee_id": "emp_analyst_01",
                    "new_utilization": 75
                },
            },
            {
                "name": "UpdateUtilizationLog",
                "arguments": {
                    "employee_id": "emp_analyst_03",
                    "new_utilization": 80
                }
            }
        ],
        "outputs": [
                "\"emp_analyst_03\": 8",
                "\"emp_analyst_01\": -8"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "handle_enterprise_cancellation",
        "instruction": "\n        As the crisis manager, manage the abrupt cancellation of the 'Enterprise Platform' project. Identify all employees presently allocated to this project and assign each 20 hours to the project AI Platform (ID proj_ai_01). Prior to creating these new assignments, remove the allocations from the cancelled project. Ensure the 'Enterprise Platform' project is duly marked as cancelled. Finally, report the number of resources reassigned. The new allocations should have a start date of 2024-08-01 and an end date of 2024-12-31.\n        ",
        "actions": [
            {
                "name": "SearchProjects",
                "arguments": {
                    "name": "Enterprise Platform"
                },
            },
            {
                "name": "GetProjectAllocations",
                "arguments": {
                    "project_id": "proj_enterprise_01"
                },
            },
            {
                "name": "UpdateProjectStatus",
                "arguments": {
                    "project_id": "proj_enterprise_01",
                    "status": "cancelled"
                },
            },
            {
                "name": "DeleteAllocation",
                "arguments": {
                    "allocation_id": "alloc_arch_01"
                },
            },
            {
                "name": "DeleteAllocation",
                "arguments": {
                    "allocation_id": "alloc_devops_01"
                },
            },
            {
                "name": "CreateAllocation",
                "arguments": {
                    "employee_id": "emp_arch_01",
                    "project_id": "proj_ai_01",
                    "hours_per_week": 20,
                    "role": "Senior Architect",
                    "start_date": "2024-08-01",
                    "end_date": "2024-12-31",
                    "status": "active"
                },
            },
            {
                "name": "CreateAllocation",
                "arguments": {
                    "employee_id": "emp_devops_02",
                    "project_id": "proj_ai_01",
                    "hours_per_week": 20,
                    "role": "DevOps Engineer",
                    "start_date": "2024-08-01",
                    "end_date": "2024-12-31",
                    "status": "active"
                }
            }
        ],
        "outputs": [
                "\"relocated_resources_quantity\": 2"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "ensure_banking_compliance",
        "instruction": "\n        As the compliance officer, handle the new regulation requirement mandating secret clearance for ALL banking project\n        staff. Assess the 'Banking Integration' project to confirm compliance. If non-compliant, revoke every allocation\n        involving employees lacking secret clearance. Additionally, introduce a resource conflict marked as\n        'clearance_violation'. Report if the project stands as non-compliant.\n        ",
        "actions": [
            {
                "name": "SearchProjects",
                "arguments": {
                    "name": "Banking Integration"
                },
            },
            {
                "name": "ValidateComplianceStatus",
                "arguments": {
                    "project_id": "proj_banking_01",
                    "required_clearance": "secret"
                },
            },
            {
                "name": "GetProjectAllocations",
                "arguments": {
                    "project_id": "proj_banking_01"
                },
            },
            {
                "name": "GetEmployeeDetails",
                "arguments": {
                    "employee_id": "emp_sec_dev_01"
                },
            },
            {
                "name": "CreateResourceConflict",
                "arguments": {
                    "employee_id": "emp_sec_dev_01",
                    "competing_projects": [
                        "proj_banking_01"
                    ],
                    "conflict_type": "clearance_violation"
                },
            },
            {
                "name": "DeleteAllocation",
                "arguments": {
                    "allocation_id": "alloc_bank_01"
                },
            },
            {
                "name": "UpdateEmployeesUtilization",
                "arguments": {
                    "employee_ids": [
                        "emp_sec_dev_01"
                    ]
                }
            }
        ],
        "outputs": [
                "\"non_compliant\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "optimize_portfolio_efficiency",
        "instruction": "\n        Coordinate efforts to enhance portfolio efficiency. Examine whether any of these projects are given critical\n        priority and lack resources: Mobile App Launch, AI Platform, Cloud Migration, Platform Modernization, and Banking\n        Integration. For projects fitting this description, evaluate the availability of employees already committed to each and\n        adjust their allocations to 40 hours. Disregard projects that have no employees assigned.\n        Ultimately, provide the list of modified projects along with the total additional hours allotted to each.\n        ",
        "actions": [
            {
                "name": "SearchProjects",
                "arguments": {
                    "name": "Mobile App Launch"
                },
            },
            {
                "name": "SearchProjects",
                "arguments": {
                    "name": "AI Platform"
                },
            },
            {
                "name": "SearchProjects",
                "arguments": {
                    "name": "Cloud Migration"
                },
            },
            {
                "name": "SearchProjects",
                "arguments": {
                    "name": "Platform Modernization"
                },
            },
            {
                "name": "SearchProjects",
                "arguments": {
                    "name": "Banking Integration"
                },
            },
            {
                "name": "GetProjectAllocations",
                "arguments": {
                    "project_id": "proj_mobile_01"
                },
            },
            {
                "name": "CalculateEmployeeAvailability",
                "arguments": {
                    "employee_id": "emp_dev_03"
                },
            },
            {
                "name": "UpdateAllocation",
                "arguments": {
                    "allocation_id": "alloc_mobile_03",
                    "hours_per_week": 40
                },
            },
            {
                "name": "GetProjectAllocations",
                "arguments": {
                    "project_id": "proj_ai_01"
                },
            },
            {
                "name": "CalculateEmployeeAvailability",
                "arguments": {
                    "employee_id": "emp_data_01"
                },
            },
            {
                "name": "UpdateAllocation",
                "arguments": {
                    "allocation_id": "alloc_data_01",
                    "hours_per_week": 40
                },
            },
            {
                "name": "GetProjectAllocations",
                "arguments": {
                    "project_id": "proj_cloud_01"
                }
            }
        ],
        "outputs": [
                "\"proj_mobile_01\": 10",
                "\"proj_ai_01\": 8"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "handle_security_breach",
        "instruction": "\n        As an incident response manager, a security breach necessitates swift attention. Search for two employees\n        possessing secret clearance to contribute to the 'Security Patch' project. Give precedence to employees skilled in 'Penetration\n        Testing'. Determine the availability of the selected employees and allocate their resulting availability to the\n        project. Form a team consisting of all project staff named 'Emergency Security Response Team'.\n        ",
        "actions": [
            {
                "name": "SearchEmployees",
                "arguments": {
                    "clearance": "secret",
                    "skills": "Penetration Testing"
                },
            },
            {
                "name": "CalculateEmployeeAvailability",
                "arguments": {
                    "employee_id": "emp_sec_dev_03"
                },
            },
            {
                "name": "CalculateEmployeeAvailability",
                "arguments": {
                    "employee_id": "emp_sec_dev_02"
                },
            },
            {
                "name": "SearchProjects",
                "arguments": {
                    "name": "Security Patch"
                },
            },
            {
                "name": "GetProjectAllocations",
                "arguments": {
                    "project_id": "proj_security_patch"
                },
            },
            {
                "name": "CreateAllocation",
                "arguments": {
                    "employee_id": "emp_sec_dev_02",
                    "project_id": "proj_security_patch",
                    "hours_per_week": 10,
                    "role": "Security Developer"
                },
            },
            {
                "name": "CreateAllocation",
                "arguments": {
                    "employee_id": "emp_sec_dev_03",
                    "project_id": "proj_security_patch",
                    "hours_per_week": 40,
                    "role": "Security Developer"
                },
            },
            {
                "name": "CreateTeam",
                "arguments": {
                    "team_name": "Emergency Security Response Team",
                    "project_id": "proj_security_patch",
                    "team_members": [
                        "emp_sec_dev_03",
                        "emp_sec_dev_02"
                    ]
                },
            },
            {
                "name": "UpdateEmployeesUtilization",
                "arguments": {
                    "employee_ids": [
                        "emp_sec_dev_03",
                        "emp_sec_dev_02"
                    ]
                }
            }
        ],
        "outputs": [
                "\"new_team_members\": [\"emp_sec_dev_03\", \"emp_sec_dev_02\"]"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "activate_bench_resources",
        "instruction": "\n        As the lead for resource optimization, you have multiple employees concluding their projects.\n        Examine the allocations with an end date before 2024-07-20. Obtain all employees from the results, calculate their\n        availabilities, and allocate all their available hours to the\n        Compliance Audit System project. Provide the relocated hours per each employee.\n        Note: The allocation search exclusively covers projects that concluded before 2024-07-20. Thus, employee\n        availability could be greater than the total allocation hours observed, because availability is calculated over\n        the entire timeline, whereas the allocation search is confined to a specified period.\n        ",
        "actions": [
            {
                "name": "SearchAllocations",
                "arguments": {
                    "end_date_before": "2024-07-20",
                    "status": "active"
                },
            },
            {
                "name": "CalculateEmployeeAvailability",
                "arguments": {
                    "employee_id": "emp_dev_05"
                },
            },
            {
                "name": "CalculateEmployeeAvailability",
                "arguments": {
                    "employee_id": "emp_sec_test_01"
                },
            },
            {
                "name": "CalculateEmployeeAvailability",
                "arguments": {
                    "employee_id": "emp_analyst_01"
                },
            },
            {
                "name": "CalculateEmployeeAvailability",
                "arguments": {
                    "employee_id": "emp_analyst_02"
                },
            },
            {
                "name": "CalculateEmployeeAvailability",
                "arguments": {
                    "employee_id": "emp_dev_15"
                },
            },
            {
                "name": "CalculateEmployeeAvailability",
                "arguments": {
                    "employee_id": "emp_dev_03"
                },
            },
            {
                "name": "SearchProjects",
                "arguments": {
                    "name": "Compliance Audit System"
                },
            },
            {
                "name": "CreateAllocation",
                "arguments": {
                    "employee_id": "emp_sec_test_01",
                    "project_id": "proj_audit_01",
                    "hours_per_week": 12,
                    "role": "Security Tester"
                },
            },
            {
                "name": "CreateAllocation",
                "arguments": {
                    "employee_id": "emp_analyst_01",
                    "project_id": "proj_audit_01",
                    "hours_per_week": 2,
                    "role": "Business Analyst"
                },
            },
            {
                "name": "CreateAllocation",
                "arguments": {
                    "employee_id": "emp_analyst_02",
                    "project_id": "proj_audit_01",
                    "hours_per_week": 8,
                    "role": "Data Analyst"
                },
            },
            {
                "name": "CreateAllocation",
                "arguments": {
                    "employee_id": "emp_dev_03",
                    "project_id": "proj_audit_01",
                    "hours_per_week": 10,
                    "role": "React Native Developer"
                },
            },
            {
                "name": "UpdateEmployeesUtilization",
                "arguments": {
                    "employee_ids": [
                        "emp_dev_03",
                        "emp_analyst_02",
                        "emp_analyst_01",
                        "emp_sec_test_01"
                    ]
                }
            }
        ],
        "outputs": [
                "\"emp_dev_03\": 10",
                "\"emp_analyst_02\": 8",
                "\"emp_analyst_01\": 2",
                "\"emp_sec_test_01\": 12"
        ]
    }
]
