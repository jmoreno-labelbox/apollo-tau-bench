# Copyright Sierra

tasks = [
    {
        "annotator": 0,
        "user_id": "res_01",
        "instruction": "Effective 2025-07-01, promote Emma Rodriguez (E10003) to 'Senior Front-end Engineer' (POS3006) at level L.4, which includes a 5% salary increase. To support her new role, transfer Michael Park (E10002) to her department (DEPT1005), making Amelia his new manager. Log a performance review for Amelia with the summary 'Promotion to Senior Engineer.' For verification, retrieve the updated records for both employees.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "GetCompensationByEmployeeId",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10003",
                    "updates": {
                        "position_id": "POS3006",
                        "level_id": "L.4",
                        "role_description": "Senior Front-end Engineer"
                    }
                },
            },
            {
                "name": "GetNewCompensationId",
                "arguments": {
                {}
                },
            },
            {
                "name": "SetCompensation",
                "arguments": {
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10003",
                        "base_salary": 152250,
                        "bonus_target_pct": 15,
                        "equity_grant": 15000,
                        "currency": "USD",
                        "effective_date": "2025-07-01"
                    }
                },
            },
            {
                "name": "GetNewReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreatePerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "Promotion to Senior Engineer"
                    }
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10003",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": [
                            "PR5003",
                            "PR5010",
                            "PR10000"
                        ]
                    }
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10002",
                    "updates": {
                        "department_id": "DEPT1005",
                        "manager_id": "E10003"
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10002"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10003\",\n                    \"position_id\": \"POS3006\",\n                    \"level_id\": \"L.4\",\n                    \"compensation_id\": \"COMP10000\",\n                    \"performance_review_ids\": [\"PR5003\", \"PR5010\", \"PR10000\"]\n                },\n                {\n                    \"employee_id\": \"E10002\",\n                    \"department_id\": \"DEPT1005\",\n                    \"manager_id\": \"E10003\"\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_02",
        "instruction": "Process the transfer of Michael Park (E10002) to the 'Boston Office', effective 2025-07-24. His new manager will be Isabella Chen (E10001). As part of this transfer, also enroll him IND the 'Legal Insurance' plan (BEN9999). A performance review note (ID PR5013) must be logged with the summary 'Relocation to Boston; enrolled in Legal Insurance.' to document these changes. For verification, retrieve his updated employee record.",
        "actions": [
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10002",
                    "updates": {
                        "work_location": "Boston Office",
                        "manager_id": "E10001"
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10002"
                },
            },
            {
                "name": "SetEmployeeBenefits",
                "arguments": {
                    "employee_id": "E10002",
                    "benefit_plan_ids": [
                        "BEN4001",
                        "BEN4002",
                        "BEN9999"
                    ]
                },
            },
            {
                "name": "CreatePerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR5013",
                        "employee_id": "E10002",
                        "period_start": "2025-07-24",
                        "period_end": "2025-07-24",
                        "rating": null,
                        "summary": "Relocation to Boston; enrolled in Legal Insurance."
                    }
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10002",
                    "updates": {
                        "performance_review_ids": [
                            "PR5002",
                            "PR5013"
                        ]
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10002"
                }
            }
        ],
        "outputs": [
                "\n            {\n                \"employee_id\": \"E10002\",\n                \"first_name\": \"Daniel\",\n                \"last_name\": \"Kim\",\n                \"preferred_name\": \"Dan\",\n                \"date_of_birth\": \"1982-09-04\",\n                \"gender\": \"Male\",\n                \"ethnicity_code\": \"A\",\n                \"nationality\": \"USA\",\n                \"marital_status\": \"Single\",\n                \"hire_date\": \"2015-03-17\",\n                \"termination_date\": null,\n                \"status\": \"Active\",\n                \"position_id\": \"POS3004\",\n                \"department_id\": \"DEPT1002\",\n                \"level_id\": \"L.5\",\n                \"manager_id\": \"E10001\",\n                \"work_location\": \"Boston Office\",\n                \"work_email\": \"michael.park@example.com\",\n                \"work_phone\": \"+1-212-555-0144\",\n                \"compensation_id\": \"COMP2002\",\n                \"benefit_plan_ids\": [\n                    \"BEN4001\",\n                    \"BEN4002\",\n                    \"BEN9999\"\n                ],\n                \"performance_review_ids\": [\n                    \"PR5002\",\n                    \"PR5013\"\n                ],\n                \"skills\": [\n                    \"Sales Strategy\",\n                    \"CRM\",\n                    \"Negotiation\"\n                ],\n                \"role_description\": \"Regional VP of Sales for the Eastern territory.\",\n                \"notes\": \"High performer—President's Club 2023.\"\n            }\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_03",
        "instruction": "You need to onboard a new Marketing Intern, Jane Doe, into the Marketing department (DEPT1005), effective 2025-06-24. Her salary will be \u20ac45,000. For her benefits, she'll get a new 'Intern Medical' plan, so set up that plan first: it's plan ID BEN10000, from Blue Shield, with 80% employer coverage and a \u20ac50 monthly employee cost. Once she's IND the system, you'll also need to raise the Marketing department's budget by \u20ac50,000 for her role. After that's taken care of, please pull up Jane's new employee record for verification.",
        "actions": [
            {
                "name": "CreateBenefitPlan",
                "arguments": {
                    "benefit_plan": {
                        "benefit_plan_id": "BEN10000",
                        "name": "Intern Medical",
                        "provider": "Blue Shield",
                        "employer_coverage_pct": 80,
                        "employee_cost_monthly": 50
                    }
                },
            },
            {
                "name": "GetNewEmployeeId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateNewEmployee",
                "arguments": {
                    "employee": {
                        "employee_id": "E10000",
                        "first_name": "Jane",
                        "last_name": "Doe",
                        "status": "Active",
                        "hire_date": "2025-06-24",
                        "department_id": "DEPT1005",
                        "work_email": null,
                        "compensation_id": null,
                        "benefit_plan_ids": [
                            "BEN10000"
                        ],
                        "performance_review_ids": [],
                        "role_description": "Marketing Intern"
                    }
                },
            },
            {
                "name": "GetNewCompensationId",
                "arguments": {
                {}
                },
            },
            {
                "name": "SetCompensation",
                "arguments": {
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10000",
                        "base_salary": 45000,
                        "currency": "EUR",
                        "effective_date": "2025-06-24"
                    }
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10000",
                    "updates": {
                        "compensation_id": "COMP10000"
                    }
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1005"
                },
            },
            {
                "name": "UpdateDepartmentRecord",
                "arguments": {
                    "department_id": "DEPT1005",
                    "updates": {
                        "budget": 1650000
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10000"
                }
            }
        ],
        "outputs": [
                "\n            {\n                \"employee_id\": \"E10000\",\n                \"first_name\": \"Jane\",\n                \"last_name\": \"Doe\",\n                \"preferred_name\": null,\n                \"date_of_birth\": null,\n                \"gender\": null,\n                \"ethnicity_code\": null,\n                \"nationality\": null,\n                \"marital_status\": null,\n                \"hire_date\": \"2025-06-24\",\n                \"termination_date\": null,\n                \"status\": \"Active\",\n                \"position_id\": null,\n                \"department_id\": \"DEPT1005\",\n                \"level_id\": null,\n                \"manager_id\": null,\n                \"work_location\": null,\n                \"work_email\": null,\n                \"work_phone\": null,\n                \"compensation_id\": \"COMP10000\",\n                \"benefit_plan_ids\": [\n                    \"BEN10000\"\n                ],\n                \"performance_review_ids\": [],\n                \"skills\": [],\n                \"role_description\": \"Marketing Intern\",\n                \"notes\": null\n            }\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_04",
        "instruction": "Process the termination of Olivia Martinez (E10005), effective 2025-07-01. Follow all off-boarding procedures, including clearing her benefits, zeroing out her final compensation, and logging a performance review with the summary 'Termination.' To backfill her role, transfer William Liu (E10006) to her previous position (POS3010). For verification, retrieve the updated records for both employees.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10005"
                },
            },
            {
                "name": "TerminateEmployee",
                "arguments": {
                    "employee_id": "E10005",
                    "termination_date": "2025-07-01"
                },
            },
            {
                "name": "SetEmployeeBenefits",
                "arguments": {
                    "employee_id": "E10005",
                    "benefit_plan_ids": []
                },
            },
            {
                "name": "SetCompensation",
                "arguments": {
                    "compensation": {
                        "compensation_id": "COMP_FINAL_E10005",
                        "employee_id": "E10005",
                        "base_salary": 0,
                        "bonus_target_pct": 0,
                        "equity_grant": 0,
                        "effective_date": "2025-07-01"
                    }
                },
            },
            {
                "name": "GetNewReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreatePerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10005",
                        "summary": "Termination"
                    }
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10005",
                    "updates": {
                        "compensation_id": "COMP_FINAL_E10005",
                        "performance_review_ids": [
                            "PR10000"
                        ]
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10006"
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10006",
                    "updates": {
                        "position_id": "POS3010"
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10005"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10006"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10005\",\n                    \"status\": \"Terminated\",\n                    \"compensation_id\": \"COMP_FINAL_E10005\",\n                    \"performance_review_ids\": [\"PR10000\"]\n                },\n                {\n                    \"employee_id\": \"E10006\",\n                    \"position_id\": \"POS3010\"\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_05",
        "instruction": "Process and approve a vacation for Arjun Patel (E10004) from 2025-08-15 to 2025-08-30. Appoint Michael Park (E10002) as acting team lead, which includes a temporary 10% salary increase, effective 2025-08-15. Log a performance review for Daniel with the summary 'Acting team lead assignment and vacation coverage.' To fund the salary increase, transfer $5,000 from the Sales department (DEPT1002) to Engineering (DEPT1001). For verification, retrieve the updated records for both employees and the Engineering department.",
        "actions": [
            {
                "name": "GetNewLeaveId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateLeaveRecord",
                "arguments": {
                    "leave": {
                        "leave_id": "LV10000",
                        "employee_id": "E10004",
                        "leave_type": "Vacation",
                        "start_date": "2025-08-15",
                        "end_date": "2025-08-30",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "UpdateLeaveStatus",
                "arguments": {
                    "leave_id": "LV10000",
                    "status": "Approved"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10002"
                },
            },
            {
                "name": "GetCompensationByEmployeeId",
                "arguments": {
                    "employee_id": "E10002"
                },
            },
            {
                "name": "GetNewCompensationId",
                "arguments": {
                {}
                },
            },
            {
                "name": "SetCompensation",
                "arguments": {
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10002",
                        "base_salary": 231000,
                        "bonus_target_pct": 25,
                        "equity_grant": 40000,
                        "currency": "USD",
                        "effective_date": "2025-08-15"
                    }
                },
            },
            {
                "name": "GetNewReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreatePerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10002",
                        "summary": "Acting team lead assignment and vacation coverage"
                    }
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10002",
                    "updates": {
                        "role_description": "Acting Team Lead",
                        "compensation_id": "COMP10000",
                        "performance_review_ids": [
                            "PR5002",
                            "PR10000"
                        ]
                    }
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1002"
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1001"
                },
            },
            {
                "name": "UpdateDepartmentRecord",
                "arguments": {
                    "department_id": "DEPT1002",
                    "updates": {
                        "budget": 4995000
                    }
                },
            },
            {
                "name": "UpdateDepartmentRecord",
                "arguments": {
                    "department_id": "DEPT1001",
                    "updates": {
                        "budget": 7005000
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10004"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10002"
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1001"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10004\"\n                },\n                {\n                    \"employee_id\": \"E10002\",\n                    \"role_description\": \"Acting Team Lead\",\n                    \"compensation_id\": \"COMP10000\",\n                    \"performance_review_ids\": [\"PR5002\", \"PR10000\"]\n                },\n                {\n                    \"department_id\": \"DEPT1001\",\n                    \"name\": \"Engineering\",\n                    \"budget\": 7005000\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_06",
        "instruction": "Effective 2025-08-01, increase the monthly employee cost for the Medical-PPO plan (BEN4001) to $170. Concurrently, promote Isabella Chen (E10001) to 'Lead Engineer' (POS3002) at level L.A, which includes a 10% salary increase, and log a performance review with the summary 'Promotion to Lead Engineer.' Enroll Adrian Thompson (E99999) IND the updated Medical-PPO plan. To fund the promotion, transfer $50,000 from the HR department's budget (DEPT1003) to the Engineering department's (DEPT1001). For verification, retrieve the updated employee records for both Andrian and Sophia, and the updated Engineering department record.",
        "actions": [
            {
                "name": "UpdateBenefitPlan",
                "arguments": {
                    "benefit_plan_id": "BEN4001",
                    "updates": {
                        "employee_cost_monthly": 170
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E99999"
                },
            },
            {
                "name": "SetEmployeeBenefits",
                "arguments": {
                    "employee_id": "E99999",
                    "benefit_plan_ids": [
                        "BEN9999",
                        "BEN4001"
                    ]
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10001"
                },
            },
            {
                "name": "GetCompensationByEmployeeId",
                "arguments": {
                    "employee_id": "E10001"
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10001",
                    "updates": {
                        "position_id": "POS3002",
                        "level_id": "L.A"
                    }
                },
            },
            {
                "name": "GetNewCompensationId",
                "arguments": {
                {}
                },
            },
            {
                "name": "SetCompensation",
                "arguments": {
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10001",
                        "base_salary": 357500,
                        "bonus_target_pct": 30,
                        "equity_grant": 75000,
                        "currency": "USD",
                        "effective_date": "2025-08-01"
                    }
                },
            },
            {
                "name": "GetNewReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreatePerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10001",
                        "summary": "Promotion to Lead Engineer"
                    }
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10001",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": [
                            "PR5001",
                            "PR10000"
                        ]
                    }
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1003"
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1001"
                },
            },
            {
                "name": "UpdateDepartmentRecord",
                "arguments": {
                    "department_id": "DEPT1003",
                    "updates": {
                        "budget": 750000
                    }
                },
            },
            {
                "name": "UpdateDepartmentRecord",
                "arguments": {
                    "department_id": "DEPT1001",
                    "updates": {
                        "budget": 7050000
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E99999"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10001"
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1001"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E99999\",\n                    \"benefit_plan_ids\": [\"BEN9999\", \"BEN4001\"]\n                },\n                {\n                    \"employee_id\": \"E10001\",\n                    \"position_id\": \"POS3002\",\n                    \"level_id\": \"L.A\",\n                    \"compensation_id\": \"COMP10000\",\n                    \"performance_review_ids\": [\"PR5001\", \"PR10000\"]\n                },\n                {\n                    \"department_id\": \"DEPT1001\",\n                    \"name\": \"Engineering\",\n                    \"budget\": 7050000\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_07",
        "instruction": "Effective 2025-06-24, onboard a new HR Business Partner, Sarah Johnson, into the HR department (DEPT1003). Her compensation is a $110,000 salary, and she should be enrolled in benefits (BEN4001, BEN4002). Her manager will be Emma Rodriguez (E10003). Log a performance review for Mary with the summary 'New hire onboarding.' To fund the new role, transfer $120,000 from the Sales budget (DEPT1002) to HR. For verification, retrieve the updated records for Sarah Johnson and the HR department.",
        "actions": [
            {
                "name": "GetNewEmployeeId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateNewEmployee",
                "arguments": {
                    "employee": {
                        "employee_id": "E10000",
                        "first_name": "Mary",
                        "last_name": "Smith",
                        "status": "Active",
                        "hire_date": "2025-06-24",
                        "department_id": "DEPT1003",
                        "manager_id": "E10003",
                        "benefit_plan_ids": [
                            "BEN4001",
                            "BEN4002"
                        ],
                        "role_description": "HR Business Partner"
                    }
                },
            },
            {
                "name": "GetNewCompensationId",
                "arguments": {
                {}
                },
            },
            {
                "name": "SetCompensation",
                "arguments": {
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10000",
                        "base_salary": 110000,
                        "currency": "USD",
                        "effective_date": "2025-06-24"
                    }
                },
            },
            {
                "name": "GetNewReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreatePerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10000",
                        "summary": "New hire onboarding"
                    }
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10000",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": [
                            "PR10000"
                        ]
                    }
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1002"
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1003"
                },
            },
            {
                "name": "UpdateDepartmentRecord",
                "arguments": {
                    "department_id": "DEPT1002",
                    "updates": {
                        "budget": 4880000
                    }
                },
            },
            {
                "name": "UpdateDepartmentRecord",
                "arguments": {
                    "department_id": "DEPT1003",
                    "updates": {
                        "budget": 920000
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10000"
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1003"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10000\",\n                    \"first_name\": \"Mary\",\n                    \"last_name\": \"Smith\",\n                    \"compensation_id\": \"COMP10000\",\n                    \"performance_review_ids\": [\"PR10000\"]\n                },\n                {\n                    \"department_id\": \"DEPT1003\",\n                    \"name\": \"Human Resources\",\n                    \"budget\": 920000\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_08",
        "instruction": "Effective 2025-06-24, promote Arjun Patel (E10004) to 'Senior Engineer' (POS3006) at level L.3, which includes a 10% salary increase. To backfill his role, transfer Michael Park (E10002) to Rahul's previous department (DEPT1001) and manager (E10003). Log a performance review for Rahul with the summary 'Promotion to Senior Engineer'. To fund the promotion, transfer $50,000 from the Sales department's budget (DEPT1002) to Engineering (DEPT1001). For verification, retrieve the updated records for both employees and the Engineering department.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10004"
                },
            },
            {
                "name": "GetCompensationByEmployeeId",
                "arguments": {
                    "employee_id": "E10004"
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10004",
                    "updates": {
                        "position_id": "POS3006",
                        "level_id": "L.3",
                        "role_description": "Senior Engineer"
                    }
                },
            },
            {
                "name": "GetNewCompensationId",
                "arguments": {
                {}
                },
            },
            {
                "name": "SetCompensation",
                "arguments": {
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10004",
                        "base_salary": 129800,
                        "bonus_target_pct": 10,
                        "equity_grant": 8000,
                        "currency": "USD",
                        "effective_date": "2025-06-24"
                    }
                },
            },
            {
                "name": "GetNewReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreatePerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10004",
                        "summary": "Promotion to Senior Engineer"
                    }
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10004",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": [
                            "PR5004",
                            "PR5009",
                            "PR10000"
                        ]
                    }
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10002",
                    "updates": {
                        "department_id": "DEPT1001",
                        "manager_id": "E10003"
                    }
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1002"
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1001"
                },
            },
            {
                "name": "UpdateDepartmentRecord",
                "arguments": {
                    "department_id": "DEPT1002",
                    "updates": {
                        "budget": 4950000
                    }
                },
            },
            {
                "name": "UpdateDepartmentRecord",
                "arguments": {
                    "department_id": "DEPT1001",
                    "updates": {
                        "budget": 7050000
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10004"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10002"
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1001"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10004\",\n                    \"position_id\": \"POS3006\",\n                    \"level_id\": \"L.3\",\n                    \"compensation_id\": \"COMP10000\",\n                    \"performance_review_ids\": [\"PR5004\", \"PR5009\", \"PR10000\"]\n                },\n                {\n                    \"employee_id\": \"E10002\",\n                    \"department_id\": \"DEPT1001\",\n                    \"manager_id\": \"E10003\"\n                },\n                {\n                    \"department_id\": \"DEPT1001\",\n                    \"name\": \"Engineering\",\n                    \"budget\": 7050000\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_09",
        "instruction": "Effective 2025-08-01, increase the monthly employee cost for the Medical-PPO plan (BEN4001) to $170. Concurrently, promote Isabella Chen (E10001) to 'Lead Engineer' (POS3002) at level L.A, which includes a 10% salary increase, and log a performance review with the summary 'Promotion to Lead Engineer.' Enroll Adrian Thompson (E99999) IND the updated Medical-PPO plan. To fund the promotion, transfer $50,000 from the HR department's budget (DEPT1003) to the Engineering department's (DEPT1001). For verification, retrieve the updated employee records for both Andrian and Sophia, and the updated Engineering department record.",
        "actions": [
            {
                "name": "UpdateBenefitPlan",
                "arguments": {
                    "benefit_plan_id": "BEN4001",
                    "updates": {
                        "employee_cost_monthly": 170
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E99999"
                },
            },
            {
                "name": "SetEmployeeBenefits",
                "arguments": {
                    "employee_id": "E99999",
                    "benefit_plan_ids": [
                        "BEN9999",
                        "BEN4001"
                    ]
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10001"
                },
            },
            {
                "name": "GetCompensationByEmployeeId",
                "arguments": {
                    "employee_id": "E10001"
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10001",
                    "updates": {
                        "position_id": "POS3002",
                        "level_id": "L.A"
                    }
                },
            },
            {
                "name": "GetNewCompensationId",
                "arguments": {
                {}
                },
            },
            {
                "name": "SetCompensation",
                "arguments": {
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10001",
                        "base_salary": 357500,
                        "bonus_target_pct": 30,
                        "equity_grant": 75000,
                        "currency": "USD",
                        "effective_date": "2025-08-01"
                    }
                },
            },
            {
                "name": "GetNewReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreatePerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10001",
                        "summary": "Promotion to Lead Engineer"
                    }
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10001",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": [
                            "PR5001",
                            "PR10000"
                        ]
                    }
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1003"
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1001"
                },
            },
            {
                "name": "UpdateDepartmentRecord",
                "arguments": {
                    "department_id": "DEPT1003",
                    "updates": {
                        "budget": 750000
                    }
                },
            },
            {
                "name": "UpdateDepartmentRecord",
                "arguments": {
                    "department_id": "DEPT1001",
                    "updates": {
                        "budget": 7050000
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E99999"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10001"
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1001"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E99999\",\n                    \"benefit_plan_ids\": [\"BEN9999\", \"BEN4001\"]\n                },\n                {\n                    \"employee_id\": \"E10001\",\n                    \"position_id\": \"POS3002\",\n                    \"level_id\": \"L.A\",\n                    \"compensation_id\": \"COMP10000\",\n                    \"performance_review_ids\": [\"PR5001\", \"PR10000\"]\n                },\n                {\n                    \"department_id\": \"DEPT1001\",\n                    \"name\": \"Engineering\",\n                    \"budget\": 7050000\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_10",
        "instruction": "Effective 2025-07-15, process the termination of Olivia Martinez (E10005). Follow all off-boarding procedures, including clearing her benefits, zeroing out her final compensation, and logging a performance review with the summary 'Termination.' To backfill her role, transfer William Liu (E10006) to her previous position (POS3010). For verification, retrieve the updated record for William Liu.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10005"
                },
            },
            {
                "name": "TerminateEmployee",
                "arguments": {
                    "employee_id": "E10005",
                    "termination_date": "2025-07-15"
                },
            },
            {
                "name": "SetEmployeeBenefits",
                "arguments": {
                    "employee_id": "E10005",
                    "benefit_plan_ids": []
                },
            },
            {
                "name": "SetCompensation",
                "arguments": {
                    "compensation": {
                        "compensation_id": "COMP_FINAL_E10005",
                        "employee_id": "E10005",
                        "base_salary": 0,
                        "bonus_target_pct": 0,
                        "equity_grant": 0,
                        "effective_date": "2025-07-15"
                    }
                },
            },
            {
                "name": "GetNewReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreatePerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10005",
                        "summary": "Termination"
                    }
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10005",
                    "updates": {
                        "compensation_id": "COMP_FINAL_E10005",
                        "performance_review_ids": [
                            "PR10000"
                        ]
                    }
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10006",
                    "updates": {
                        "position_id": "POS3010"
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10006"
                }
            }
        ],
        "outputs": [
                "\n            {\n                \"employee_id\": \"E10006\",\n                \"first_name\": \"Marcus\",\n                \"last_name\": \"Chen\",\n                \"position_id\": \"POS3010\"\n            }\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_11",
        "instruction": "Effective 2025-07-01, restructure the Sales department (DEPT1002). Promote Michael Park (E10002) to 'Regional VP' (POS3004) with a 15% salary increase and log a performance review with the summary 'Promotion to Regional VP.' To support him, transfer Arjun Patel (E10004) to the Sales department, making Daniel his new manager. Increase the Sales department budget by $200,000. For verification, retrieve the updated records for both employees and the Sales department.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10002"
                },
            },
            {
                "name": "GetCompensationByEmployeeId",
                "arguments": {
                    "employee_id": "E10002"
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10002",
                    "updates": {
                        "position_id": "POS3004",
                        "role_description": "Regional VP"
                    }
                },
            },
            {
                "name": "GetNewCompensationId",
                "arguments": {
                {}
                },
            },
            {
                "name": "SetCompensation",
                "arguments": {
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10002",
                        "base_salary": 241500,
                        "bonus_target_pct": 25,
                        "equity_grant": 40000,
                        "currency": "USD",
                        "effective_date": "2025-07-01"
                    }
                },
            },
            {
                "name": "GetNewReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreatePerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10002",
                        "summary": "Promotion to Regional VP"
                    }
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10002",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": [
                            "PR5002",
                            "PR10000"
                        ]
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10004"
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10004",
                    "updates": {
                        "department_id": "DEPT1002",
                        "manager_id": "E10002"
                    }
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1002"
                },
            },
            {
                "name": "UpdateDepartmentRecord",
                "arguments": {
                    "department_id": "DEPT1002",
                    "updates": {
                        "budget": 5200000
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10002"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10004"
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1002"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10002\",\n                    \"position_id\": \"POS3004\",\n                    \"role_description\": \"Regional VP\",\n                    \"compensation_id\": \"COMP10000\",\n                    \"performance_review_ids\": [\"PR5002\", \"PR10000\"]\n                },\n                {\n                    \"employee_id\": \"E10004\",\n                    \"department_id\": \"DEPT1002\",\n                    \"manager_id\": \"E10002\"\n                },\n                {\n                    \"department_id\": \"DEPT1002\",\n                    \"name\": \"Sales\",\n                    \"budget\": 5200000\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_12",
        "instruction": "Effective 2025-08-01, promote Emma Rodriguez (E10003) to 'Senior Engineer' (POS3005) at level L.4 IND the Engineering department (DEPT1001), which includes a 10% salary increase. To support the team, transfer Michael Park (E10002) to the Engineering department, making Amelia his new manager. Log a performance review for Amelia with the summary 'Promotion to Senior Engineer.' To fund the promotion, transfer $75,000 from the Sales department's budget (DEPT1002) to Engineering. For verification, retrieve the updated records for both employees and both departments.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "GetCompensationByEmployeeId",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10003",
                    "updates": {
                        "department_id": "DEPT1001",
                        "position_id": "POS3005",
                        "level_id": "L.4",
                        "role_description": "Senior Engineer"
                    }
                },
            },
            {
                "name": "GetNewCompensationId",
                "arguments": {
                {}
                },
            },
            {
                "name": "SetCompensation",
                "arguments": {
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10003",
                        "base_salary": 159500,
                        "bonus_target_pct": 15,
                        "equity_grant": 15000,
                        "currency": "USD",
                        "effective_date": "2025-08-01"
                    }
                },
            },
            {
                "name": "GetNewReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreatePerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "Promotion to Senior Engineer"
                    }
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10003",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": [
                            "PR5003",
                            "PR5010",
                            "PR10000"
                        ]
                    }
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10002",
                    "updates": {
                        "department_id": "DEPT1001",
                        "manager_id": "E10003"
                    }
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1002"
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1001"
                },
            },
            {
                "name": "UpdateDepartmentRecord",
                "arguments": {
                    "department_id": "DEPT1002",
                    "updates": {
                        "budget": 4925000
                    }
                },
            },
            {
                "name": "UpdateDepartmentRecord",
                "arguments": {
                    "department_id": "DEPT1001",
                    "updates": {
                        "budget": 7075000
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10002"
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1001"
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1002"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10003\",\n                    \"department_id\": \"DEPT1001\",\n                    \"position_id\": \"POS3005\",\n                    \"level_id\": \"L.4\",\n                    \"compensation_id\": \"COMP10000\",\n                    \"performance_review_ids\": [\"PR5003\", \"PR5010\", \"PR10000\"]\n                },\n                {\n                    \"employee_id\": \"E10002\",\n                    \"department_id\": \"DEPT1001\",\n                    \"manager_id\": \"E10003\"\n                },\n                {\n                    \"department_id\": \"DEPT1001\",\n                    \"name\": \"Engineering\",\n                    \"budget\": 7075000\n                },\n                {\n                    \"department_id\": \"DEPT1002\",\n                    \"name\": \"Sales\",\n                    \"budget\": 4925000\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_13",
        "instruction": "Effective 2025-07-01, increase the Sales department's (DEPT1002) budget by $250,000. Use this to promote Michael Park (E10002) to 'Senior Sales Executive' (POS3005) at level L.5, which includes a 10% salary increase. To provide support, transfer Arjun Patel (E10004) to the Sales department, making Daniel his new manager. Log a performance review for Daniel with the summary 'Promotion to Senior Sales Executive.' For verification, retrieve the updated records for both employees and the Sales department.",
        "actions": [
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1002"
                },
            },
            {
                "name": "UpdateDepartmentRecord",
                "arguments": {
                    "department_id": "DEPT1002",
                    "updates": {
                        "budget": 5250000
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10002"
                },
            },
            {
                "name": "GetCompensationByEmployeeId",
                "arguments": {
                    "employee_id": "E10002"
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10002",
                    "updates": {
                        "position_id": "POS3005",
                        "level_id": "L.5",
                        "role_description": "Senior Sales Executive"
                    }
                },
            },
            {
                "name": "GetNewCompensationId",
                "arguments": {
                {}
                },
            },
            {
                "name": "SetCompensation",
                "arguments": {
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10002",
                        "base_salary": 231000,
                        "bonus_target_pct": 25,
                        "equity_grant": 40000,
                        "currency": "USD",
                        "effective_date": "2025-07-01"
                    }
                },
            },
            {
                "name": "GetNewReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreatePerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10002",
                        "summary": "Promotion to Senior Sales Executive"
                    }
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10002",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": [
                            "PR5002",
                            "PR10000"
                        ]
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10004"
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10004",
                    "updates": {
                        "department_id": "DEPT1002",
                        "manager_id": "E10002"
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10002"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10004"
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1002"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10002\",\n                    \"position_id\": \"POS3005\",\n                    \"level_id\": \"L.5\",\n                    \"compensation_id\": \"COMP10000\",\n                    \"performance_review_ids\": [\"PR5002\", \"PR10000\"]\n                },\n                {\n                    \"employee_id\": \"E10004\",\n                    \"department_id\": \"DEPT1002\",\n                    \"manager_id\": \"E10002\"\n                },\n                {\n                    \"department_id\": \"DEPT1002\",\n                    \"name\": \"Sales\",\n                    \"budget\": 5250000\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_14",
        "instruction": "Effective 2025-10-01, process and approve a parental leave for Isabella Chen (E10001) until 2026-02-01. Appoint Emma Rodriguez (E10003) as acting CTO (POS4001) at level L.5 to cover the leave, which includes a temporary 8% salary increase. Log a performance review for Amelia with the summary 'Acting CTO assignment.' To fund this, transfer $50,000 from the Sales department's budget (DEPT1002) to Engineering (DEPT1001). For verification, retrieve the updated records for both employees and the Engineering department.",
        "actions": [
            {
                "name": "GetNewLeaveId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateLeaveRecord",
                "arguments": {
                    "leave": {
                        "leave_id": "LV10000",
                        "employee_id": "E10001",
                        "leave_type": "Parental",
                        "start_date": "2025-10-01",
                        "end_date": "2026-02-01",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "UpdateLeaveStatus",
                "arguments": {
                    "leave_id": "LV10000",
                    "status": "Approved"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "GetCompensationByEmployeeId",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10003",
                    "updates": {
                        "position_id": "POS4001",
                        "level_id": "L.5",
                        "role_description": "Acting CTO"
                    }
                },
            },
            {
                "name": "GetNewCompensationId",
                "arguments": {
                {}
                },
            },
            {
                "name": "SetCompensation",
                "arguments": {
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10003",
                        "base_salary": 156600,
                        "bonus_target_pct": 15,
                        "equity_grant": 15000,
                        "currency": "USD",
                        "effective_date": "2025-10-01"
                    }
                },
            },
            {
                "name": "GetNewReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreatePerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "Acting CTO assignment"
                    }
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10003",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": [
                            "PR5003",
                            "PR5010",
                            "PR10000"
                        ]
                    }
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1002"
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1001"
                },
            },
            {
                "name": "UpdateDepartmentRecord",
                "arguments": {
                    "department_id": "DEPT1002",
                    "updates": {
                        "budget": 4950000
                    }
                },
            },
            {
                "name": "UpdateDepartmentRecord",
                "arguments": {
                    "department_id": "DEPT1001",
                    "updates": {
                        "budget": 7050000
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10001"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1001"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10001\"\n                },\n                {\n                    \"employee_id\": \"E10003\",\n                    \"position_id\": \"POS4001\",\n                    \"level_id\": \"L.5\",\n                    \"role_description\": \"Acting CTO\",\n                    \"compensation_id\": \"COMP10000\",\n                    \"performance_review_ids\": [\"PR5003\", \"PR5010\", \"PR10000\"]\n                },\n                {\n                    \"department_id\": \"DEPT1001\",\n                    \"name\": \"Engineering\",\n                    \"budget\": 7050000\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_15",
        "instruction": "Onboard a new hire, Sofia Hernandez, as a 'Junior Marketing Analyst' (POS3010) IND the Marketing department (DEPT1005), effective 2025-06-24. Her salary is \u20ac68,000 with a 5% bonus. Log a 'New hire onboarding' review for her. As part of the onboarding, update her manager William Liu's (E10006) role description to 'Senior Product Manager & Team Lead'. To fund the new role, increase the Marketing budget by \u20ac100,000. For verification, retrieve the updated records for both employees and the Marketing department.",
        "actions": [
            {
                "name": "GetNewEmployeeId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateNewEmployee",
                "arguments": {
                    "employee": {
                        "employee_id": "E10000",
                        "first_name": "Maria",
                        "last_name": "Lopez",
                        "status": "Active",
                        "hire_date": "2025-06-24",
                        "position_id": "POS3010",
                        "department_id": "DEPT1005",
                        "manager_id": "E10006",
                        "role_description": "Junior Marketing Analyst"
                    }
                },
            },
            {
                "name": "GetNewCompensationId",
                "arguments": {
                {}
                },
            },
            {
                "name": "SetCompensation",
                "arguments": {
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10000",
                        "base_salary": 68000,
                        "bonus_target_pct": 5,
                        "currency": "EUR",
                        "effective_date": "2025-06-24"
                    }
                },
            },
            {
                "name": "GetNewReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreatePerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10000",
                        "summary": "New hire onboarding"
                    }
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10000",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": [
                            "PR10000"
                        ]
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10006"
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10006",
                    "updates": {
                        "role_description": "Senior Product Manager & Team Lead"
                    }
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1005"
                },
            },
            {
                "name": "UpdateDepartmentRecord",
                "arguments": {
                    "department_id": "DEPT1005",
                    "updates": {
                        "budget": 1700000
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10000"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10006"
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1005"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10000\",\n                    \"first_name\": \"Maria\",\n                    \"last_name\": \"Lopez\",\n                    \"compensation_id\": \"COMP10000\",\n                    \"performance_review_ids\": [\"PR10000\"]\n                },\n                {\n                    \"employee_id\": \"E10006\",\n                    \"role_description\": \"Senior Product Manager & Team Lead\"\n                },\n                {\n                    \"department_id\": \"DEPT1005\",\n                    \"name\": \"Marketing\",\n                    \"budget\": 1700000\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_16",
        "instruction": "Arjun Patel's (E10004) recent vacation (leave ID LV6002) has concluded. Update the status of this leave record to 'Taken' to reflect that it's completed. As he has now returned, process his pending promotion to 'Senior Backend Engineer' (POS3009) at level L.3, effective 2025-07-27. This includes a 12% salary increase. Log a performance review with the summary 'Promotion to Senior Engineer.' To fund the raise, transfer $20,000 from the HR budget (DEPT1003) to Engineering (DEPT1001). For verification, retrieve his updated employee record, leave history, and the Engineering department record.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10004"
                },
            },
            {
                "name": "GetCompensationByEmployeeId",
                "arguments": {
                    "employee_id": "E10004"
                },
            },
            {
                "name": "UpdateLeaveStatus",
                "arguments": {
                    "leave_id": "LV6002",
                    "status": "Taken"
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10004",
                    "updates": {
                        "position_id": "POS3009",
                        "level_id": "L.3",
                        "role_description": "Senior Backend Engineer"
                    }
                },
            },
            {
                "name": "GetNewCompensationId",
                "arguments": {
                {}
                },
            },
            {
                "name": "SetCompensation",
                "arguments": {
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10004",
                        "base_salary": 132160,
                        "bonus_target_pct": 10,
                        "equity_grant": 8000,
                        "currency": "USD",
                        "effective_date": "2025-07-27"
                    }
                },
            },
            {
                "name": "GetNewReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreatePerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10004",
                        "summary": "Promotion to Senior Engineer"
                    }
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10004",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": [
                            "PR5004",
                            "PR5009",
                            "PR10000"
                        ]
                    }
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1003"
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1001"
                },
            },
            {
                "name": "UpdateDepartmentRecord",
                "arguments": {
                    "department_id": "DEPT1003",
                    "updates": {
                        "budget": 780000
                    }
                },
            },
            {
                "name": "UpdateDepartmentRecord",
                "arguments": {
                    "department_id": "DEPT1001",
                    "updates": {
                        "budget": 7020000
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10004"
                },
            },
            {
                "name": "ListEmployeeLeaves",
                "arguments": {
                    "employee_id": "E10004"
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1001"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10004\",\n                    \"position_id\": \"POS3009\",\n                    \"level_id\": \"L.3\",\n                    \"compensation_id\": \"COMP10000\",\n                    \"performance_review_ids\": [\"PR5004\", \"PR5009\", \"PR10000\"]\n                },\n                [\n                    {\n                        \"leave_id\": \"LV6002\",\n                        \"status\": \"Taken\"\n                    }\n                ],\n                {\n                    \"department_id\": \"DEPT1001\",\n                    \"name\": \"Engineering\",\n                    \"budget\": 7020000\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_17",
        "instruction": "Standardize the records for Arjun Patel (E10004), effective 2025-07-01, by updating his work location to 'Remote \u2013 Mumbai'. As part of this, promote his manager, Emma Rodriguez (E10003), to 'Lead Engineer' (POS3005) with a 5% salary increase. Log a performance review for Amelia with the summary 'Promotion to Lead Engineer.' For verification, retrieve the updated records for both employees.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10004"
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10004",
                    "updates": {
                        "work_location": "Remote – Mumbai"
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "GetCompensationByEmployeeId",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10003",
                    "updates": {
                        "position_id": "POS3005",
                        "role_description": "Lead Engineer"
                    }
                },
            },
            {
                "name": "GetNewCompensationId",
                "arguments": {
                {}
                },
            },
            {
                "name": "SetCompensation",
                "arguments": {
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10003",
                        "base_salary": 152250,
                        "bonus_target_pct": 15,
                        "equity_grant": 15000,
                        "currency": "USD",
                        "effective_date": "2025-07-01"
                    }
                },
            },
            {
                "name": "GetNewReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreatePerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "Promotion to Lead Engineer"
                    }
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10003",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": [
                            "PR5003",
                            "PR5010",
                            "PR10000"
                        ]
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10004"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10003"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10004\",\n                    \"work_location\": \"Remote – Mumbai\"\n                },\n                {\n                    \"employee_id\": \"E10003\",\n                    \"position_id\": \"POS3005\",\n                    \"role_description\": \"Lead Engineer\",\n                    \"compensation_id\": \"COMP10000\",\n                    \"performance_review_ids\": [\"PR5003\", \"PR5010\", \"PR10000\"]\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_18",
        "instruction": "Effective 2025-07-24, transfer Michael Park (E10002) to the Marketing department (DEPT1005). As part of this move, enroll him IND the 'Commuter Stipend - EU' plan (BEN4005). Log a performance review with the summary 'Transfer and benefit update.' For verification, retrieve his updated employee record.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10002"
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10002",
                    "updates": {
                        "department_id": "DEPT1005"
                    }
                },
            },
            {
                "name": "SetEmployeeBenefits",
                "arguments": {
                    "employee_id": "E10002",
                    "benefit_plan_ids": [
                        "BEN4001",
                        "BEN4002",
                        "BEN4005"
                    ]
                },
            },
            {
                "name": "GetNewReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreatePerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10002",
                        "summary": "Transfer and benefit update"
                    }
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10002",
                    "updates": {
                        "performance_review_ids": [
                            "PR5002",
                            "PR10000"
                        ]
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10002"
                }
            }
        ],
        "outputs": [
                "\n            {\n                \"employee_id\": \"E10002\",\n                \"department_id\": \"DEPT1005\",\n                \"benefit_plan_ids\": [\"BEN4001\", \"BEN4002\", \"BEN4005\"],\n                \"performance_review_ids\": [\"PR5002\", \"PR10000\"]\n            }\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_19",
        "instruction": "Effective 2025-06-24, process a leadership change. Promote Isabella Chen (E10001) to CEO (POS4000) with a new $400,000 base salary, 35% bonus, and 90,000 equity grant. Appoint Emma Rodriguez (E10003) as the new head of the Engineering department (DEPT1001). Log a performance review for Sophia with the summary 'Promotion to CEO.' For verification, retrieve the updated records for both employees and the Engineering department.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10001"
                },
            },
            {
                "name": "GetCompensationByEmployeeId",
                "arguments": {
                    "employee_id": "E10001"
                },
            },
            {
                "name": "GetNewCompensationId",
                "arguments": {
                {}
                },
            },
            {
                "name": "SetCompensation",
                "arguments": {
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10001",
                        "base_salary": 400000,
                        "bonus_target_pct": 35,
                        "equity_grant": 90000,
                        "currency": "USD",
                        "effective_date": "2025-06-24"
                    }
                },
            },
            {
                "name": "GetNewReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreatePerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10001",
                        "summary": "Promotion to CEO"
                    }
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10001",
                    "updates": {
                        "position_id": "POS4000",
                        "role_description": "Chief Executive Officer",
                        "compensation_id": "COMP10000",
                        "performance_review_ids": [
                            "PR5001",
                            "PR10000"
                        ]
                    }
                },
            },
            {
                "name": "UpdateDepartmentRecord",
                "arguments": {
                    "department_id": "DEPT1001",
                    "updates": {
                        "head_id": "E10003"
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10001"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1001"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10001\",\n                    \"position_id\": \"POS4000\",\n                    \"role_description\": \"Chief Executive Officer\",\n                    \"compensation_id\": \"COMP10000\",\n                    \"performance_review_ids\": [\"PR5001\", \"PR10000\"]\n                },\n                {\n                    \"employee_id\": \"E10003\"\n                },\n                {\n                    \"department_id\": \"DEPT1001\",\n                    \"name\": \"Engineering\",\n                    \"head_id\": \"E10003\"\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_20",
        "instruction": "Process a departmental reorganization, effective 2025-06-24. The Finance department (DEPT1004) is being merged into the Human Resources department (DEPT1003). Transfer all active employees from Finance to HR. William Liu (E10006) will be the new head of the combined HR department. Zero out the old Finance budget and set the new HR budget to $2,000,000. Log a performance review for Marcus to document the transition. For verification, provide an updated roster of all active employees IND the HR department.",
        "actions": [
            {
                "name": "FindEmployees",
                "arguments": {
                    "filters": {
                        "department_id": "DEPT1004",
                        "status": "Active"
                    }
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10005",
                    "updates": {
                        "department_id": "DEPT1003",
                        "manager_id": "E10006"
                    }
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10006",
                    "updates": {
                        "department_id": "DEPT1003"
                    }
                },
            },
            {
                "name": "UpdateDepartmentRecord",
                "arguments": {
                    "department_id": "DEPT1004",
                    "updates": {
                        "budget": 0,
                        "head_id": null
                    }
                },
            },
            {
                "name": "UpdateDepartmentRecord",
                "arguments": {
                    "department_id": "DEPT1003",
                    "updates": {
                        "budget": 2000000,
                        "head_id": "E10006"
                    }
                },
            },
            {
                "name": "GetNewReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreatePerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10006",
                        "period_start": "2025-06-24",
                        "period_end": "2025-06-24",
                        "rating": null,
                        "summary": null
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10006"
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10006",
                    "updates": {
                        "performance_review_ids": [
                            "PR5011",
                            "PR10000"
                        ]
                    }
                },
            },
            {
                "name": "FindEmployees",
                "arguments": {
                    "filters": {
                        "department_id": "DEPT1003",
                        "status": "Active"
                    }
                }
            }
        ],
        "outputs": [
                "\n            {\n                \"count\": 2,\n                \"results\": [\n                    {\n                        \"employee_id\": \"E10005\",\n                        \"first_name\": \"Elena\",\n                        \"last_name\": \"Rodriguez\",\n                        \"preferred_name\": \"Elena\",\n                        \"date_of_birth\": \"1995-01-30\",\n                        \"gender\": \"Female\",\n                        \"ethnicity_code\": \"H\",\n                        \"nationality\": \"ESP\",\n                        \"marital_status\": \"Single\",\n                        \"hire_date\": \"2024-09-01\",\n                        \"termination_date\": null,\n                        \"status\": \"Active\",\n                        \"position_id\": \"POS3010\",\n                        \"department_id\": \"DEPT1003\",\n                        \"level_id\": \"L.1\",\n                        \"manager_id\": \"E10006\",\n                        \"work_location\": \"Barcelona Office\",\n                        \"work_email\": \"olivia.martinez@example.com\",\n                        \"work_phone\": \"+34-91-555-0200\",\n                        \"compensation_id\": \"COMP2005\",\n                        \"benefit_plan_ids\": [\n                            \"BEN4001\",\n                            \"BEN4005\"\n                        ],\n                        \"performance_review_ids\": [],\n                        \"skills\": [\n                            \"Financial Modeling\",\n                            \"SQL\",\n                            \"Excel\"\n                        ],\n                        \"role_description\": \"Junior Financial Analyst supporting quarterly forecasts.\",\n                        \"notes\": \"Recent graduate—ESADE Business School.\"\n                    },\n                    {\n                        \"employee_id\": \"E10006\",\n                        \"first_name\": \"Marcus\",\n                        \"last_name\": \"Chen\",\n                        \"preferred_name\": \"Marcus\",\n                        \"date_of_birth\": \"1991-08-12\",\n                        \"gender\": \"Male\",\n                        \"ethnicity_code\": \"A\",\n                        \"nationality\": \"CAN\",\n                        \"marital_status\": \"Married\",\n                        \"hire_date\": \"2023-11-15\",\n                        \"termination_date\": null,\n                        \"status\": \"Active\",\n                        \"position_id\": \"POS3008\",\n                        \"department_id\": \"DEPT1003\",\n                        \"level_id\": \"L.4\",\n                        \"manager_id\": \"E10012\",\n                        \"work_location\": \"Barcelona Office\",\n                        \"work_email\": \"william.liu@example.com\",\n                        \"work_phone\": \"+1-604-555-0166\",\n                        \"compensation_id\": \"COMP2006\",\n                        \"benefit_plan_ids\": [\n                            \"BEN4001\",\n                            \"BEN4002\",\n                            \"BEN4003\"\n                        ],\n                        \"performance_review_ids\": [\n                            \"PR5011\",\n                            \"PR10000\"\n                        ],\n                        \"skills\": [\n                            \"Product Strategy\",\n                            \"User Research\",\n                            \"Data Analytics\"\n                        ],\n                        \"role_description\": \"Senior Product Manager leading the analytics platform initiatives.\",\n                        \"notes\": \"Previously led successful product launches at major tech companies.\"\n                    }\n                ]\n            }\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_21",
        "instruction": "Effective 2025-06-24, process an equity refresh for Michael Park (E10002), increasing his equity grant by $15,000 and updating his role description to 'Senior Sales Executive'. Log a performance review with the summary 'Equity refresh and title change.' To fund this, increase the Sales department (DEPT1002) budget by $15,000. As part of the same process, append the note 'Q3 compensation audit complete.' to the HR department's (DEPT1003) description. For verification, retrieve the updated records for Michael Park and both departments.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10002"
                },
            },
            {
                "name": "GetCompensationByEmployeeId",
                "arguments": {
                    "employee_id": "E10002"
                },
            },
            {
                "name": "GetNewCompensationId",
                "arguments": {
                {}
                },
            },
            {
                "name": "SetCompensation",
                "arguments": {
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10002",
                        "equity_grant": 55000,
                        "base_salary": 210000,
                        "bonus_target_pct": 25,
                        "currency": "USD",
                        "effective_date": "2025-06-24"
                    }
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10002",
                    "updates": {
                        "role_description": "Senior Sales Executive"
                    }
                },
            },
            {
                "name": "GetNewReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreatePerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10002",
                        "summary": "Equity refresh and title change"
                    }
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10002",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": [
                            "PR5002",
                            "PR10000"
                        ]
                    }
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1002"
                },
            },
            {
                "name": "UpdateDepartmentRecord",
                "arguments": {
                    "department_id": "DEPT1002",
                    "updates": {
                        "budget": 5015000
                    }
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1003"
                },
            },
            {
                "name": "UpdateDepartmentRecord",
                "arguments": {
                    "department_id": "DEPT1003",
                    "updates": {
                        "description": "Manages recruitment, retention, and employee well-being. Q3 compensation audit complete."
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10002"
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1002"
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1003"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10002\",\n                    \"role_description\": \"Senior Sales Executive\",\n                    \"compensation_id\": \"COMP10000\",\n                    \"performance_review_ids\": [\"PR5002\", \"PR10000\"]\n                },\n                {\n                    \"department_id\": \"DEPT1002\",\n                    \"name\": \"Sales\",\n                    \"budget\": 5015000\n                },\n                {\n                    \"department_id\": \"DEPT1003\",\n                    \"name\": \"Human Resources\",\n                    \"description\": \"Manages recruitment, retention, and employee well-being. Q3 compensation audit complete.\"\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_22",
        "instruction": "The company is launching a new Employee Assistance Program (EAP). Create the new benefit plan IND the system using ID BEN10002, with 'ComPsych' as the provider and 100% employer coverage. Once the plan exists, you need to enroll every currently active employee. To verify the rollout, provide the updated employee record for Isabella Chen (E10001).",
        "actions": [
            {
                "name": "CreateBenefitPlan",
                "arguments": {
                    "benefit_plan": {
                        "benefit_plan_id": "BEN10002",
                        "name": "Employee Assistance Program",
                        "provider": "ComPsych",
                        "employer_coverage_pct": 100
                    }
                },
            },
            {
                "name": "FindEmployees",
                "arguments": {
                    "filters": {
                        "status": "Active"
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10001"
                },
            },
            {
                "name": "SetEmployeeBenefits",
                "arguments": {
                    "employee_id": "E10001",
                    "benefit_plan_ids": [
                        "BEN4001",
                        "BEN4002",
                        "BEN4003",
                        "BEN10002"
                    ]
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10002"
                },
            },
            {
                "name": "SetEmployeeBenefits",
                "arguments": {
                    "employee_id": "E10002",
                    "benefit_plan_ids": [
                        "BEN4001",
                        "BEN4002",
                        "BEN10002"
                    ]
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "SetEmployeeBenefits",
                "arguments": {
                    "employee_id": "E10003",
                    "benefit_plan_ids": [
                        "BEN4001",
                        "BEN4003",
                        "BEN4004",
                        "BEN10002"
                    ]
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10004"
                },
            },
            {
                "name": "SetEmployeeBenefits",
                "arguments": {
                    "employee_id": "E10004",
                    "benefit_plan_ids": [
                        "BEN4001",
                        "BEN4003",
                        "BEN10002"
                    ]
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10005"
                },
            },
            {
                "name": "SetEmployeeBenefits",
                "arguments": {
                    "employee_id": "E10005",
                    "benefit_plan_ids": [
                        "BEN4001",
                        "BEN4005",
                        "BEN10002"
                    ]
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10006"
                },
            },
            {
                "name": "SetEmployeeBenefits",
                "arguments": {
                    "employee_id": "E10006",
                    "benefit_plan_ids": [
                        "BEN4001",
                        "BEN4002",
                        "BEN4003",
                        "BEN10002"
                    ]
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10001"
                }
            }
        ],
        "outputs": [
                "\n            {\n                \"employee_id\": \"E10001\",\n                \"first_name\": \"Sophia\",\n                \"last_name\": \"Nguyen\",\n                \"preferred_name\": \"Sophia\",\n                \"date_of_birth\": \"1978-02-16\",\n                \"gender\": \"Female\",\n                \"ethnicity_code\": \"W\",\n                \"nationality\": \"USA\",\n                \"marital_status\": \"Married\",\n                \"hire_date\": \"2010-08-02\",\n                \"termination_date\": null,\n                \"status\": \"Active\",\n                \"position_id\": \"POS3001\",\n                \"department_id\": \"DEPT1001\",\n                \"level_id\": \"L.C\",\n                \"manager_id\": null,\n                \"work_location\": \"Seattle HQ\",\n                \"work_email\": \"isabella.chen@example.com\",\n                \"work_phone\": \"+1-415-555-0100\",\n                \"compensation_id\": \"COMP2001\",\n                \"benefit_plan_ids\": [\n                    \"BEN4001\",\n                    \"BEN4002\",\n                    \"BEN4003\",\n                    \"BEN10002\"\n                ],\n                \"performance_review_ids\": [\n                    \"PR5001\",\n                    \"PR5009\"\n                ],\n                \"skills\": [\n                    \"Leadership\",\n                    \"Cloud Architecture\",\n                    \"Python\"\n                ],\n                \"role_description\": \"Chief Technology Officer overseeing all engineering functions.\",\n                \"notes\": \"Founder-level equity grant.\"\n            }\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_23",
        "instruction": "Process a paid sabbatical for Emma Rodriguez (E10003) from 2026-01-01 to 2026-07-01, and it should be logged and immediately approved. Per policy, an employee's bonus is set to 0% during a sabbatical, so you need to create a new compensation record reflecting this change, effective on the leave start date. Pull up her new compensation record.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "GetCompensationByEmployeeId",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "GetNewLeaveId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateLeaveRecord",
                "arguments": {
                    "leave": {
                        "leave_id": "LV10000",
                        "employee_id": "E10003",
                        "leave_type": "Sabbatical",
                        "start_date": "2026-01-01",
                        "end_date": "2026-07-01",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "UpdateLeaveStatus",
                "arguments": {
                    "leave_id": "LV10000",
                    "status": "Approved"
                },
            },
            {
                "name": "GetNewCompensationId",
                "arguments": {
                {}
                },
            },
            {
                "name": "SetCompensation",
                "arguments": {
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10003",
                        "base_salary": 145000,
                        "currency": "USD",
                        "bonus_target_pct": 0,
                        "equity_grant": 15000,
                        "effective_date": "2026-01-01"
                    }
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10003",
                    "updates": {
                        "compensation_id": "COMP10000"
                    }
                },
            },
            {
                "name": "GetCompensationByEmployeeId",
                "arguments": {
                    "employee_id": "E10003"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"compensation_id\": \"COMP10000\",\n                    \"employee_id\": \"E10003\",\n                    \"base_salary\": 145000,\n                    \"currency\": \"USD\",\n                    \"bonus_target_pct\": 0,\n                    \"equity_grant\": 15000,\n                    \"effective_date\": \"2026-01-01\"\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_24",
        "instruction": "Rehire Olivia Martinez (E10005) as Senior Accountant (POS3013) IND the finance department on 2025-09-01 with a \u20ac85,000 salary. Update her status to 'Active', set her benefits to Medical-PPO (BEN4001) & Dental (BEN4002), and log a rehiring review with the summary 'Re-hire processing.'. As her manager, William Liu (E10006), will now oversee re-hires, update his role description to 'Senior Product Manager, Team Lead'. For verification, retrieve both updated employee records.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10005"
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10005",
                    "updates": {
                        "status": "Active",
                        "hire_date": "2025-09-01",
                        "termination_date": null,
                        "position_id": "POS3013",
                        "role_description": "Senior Accountant"
                    }
                },
            },
            {
                "name": "SetEmployeeBenefits",
                "arguments": {
                    "employee_id": "E10005",
                    "benefit_plan_ids": [
                        "BEN4001",
                        "BEN4002"
                    ]
                },
            },
            {
                "name": "GetNewCompensationId",
                "arguments": {
                {}
                },
            },
            {
                "name": "SetCompensation",
                "arguments": {
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10005",
                        "base_salary": 85000,
                        "currency": "EUR",
                        "effective_date": "2025-09-01"
                    }
                },
            },
            {
                "name": "GetNewReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreatePerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10005",
                        "summary": "Re-hire processing."
                    }
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10005",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": [
                            "PR10000"
                        ]
                    }
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10006",
                    "updates": {
                        "role_description": "Senior Product Manager, Team Lead"
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10005"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10006"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10005\",\n                    \"status\": \"Active\",\n                    \"hire_date\": \"2025-09-01\",\n                    \"position_id\": \"POS3013\",\n                    \"compensation_id\": \"COMP10000\",\n                    \"performance_review_ids\": [\"PR10000\"]\n                },\n                {\n                    \"employee_id\": \"E10006\",\n                    \"role_description\": \"Senior Product Manager, Team Lead\"\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_25",
        "instruction": "Due to budget cuts effective 2025-06-24, reduce the Marketing (DEPT1005) budget by \u20ac300,000 and prepend 'HIRING FREEZE: H2 2025.' to its description. As part of this, transfer William Liu (E10006) to the Finance department (DEPT1004) and promote him to 'Senior Financial Analyst' (POS3010), which includes a 5% salary increase. Log a performance review with the summary 'Transfer and promotion due to restructuring.' For verification, retrieve the updated records for Marcus and the Marketing department.",
        "actions": [
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1005"
                },
            },
            {
                "name": "UpdateDepartmentRecord",
                "arguments": {
                    "department_id": "DEPT1005",
                    "updates": {
                        "budget": 1300000,
                        "description": "HIRING FREEZE: H2 2025. Drives brand awareness and demand generation."
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10006"
                },
            },
            {
                "name": "GetCompensationByEmployeeId",
                "arguments": {
                    "employee_id": "E10006"
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10006",
                    "updates": {
                        "department_id": "DEPT1004",
                        "position_id": "POS3010",
                        "role_description": "Senior Financial Analyst"
                    }
                },
            },
            {
                "name": "GetNewCompensationId",
                "arguments": {
                {}
                },
            },
            {
                "name": "SetCompensation",
                "arguments": {
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10006",
                        "base_salary": 63000,
                        "bonus_target_pct": 5,
                        "equity_grant": 5000,
                        "currency": "EUR",
                        "effective_date": "2025-06-24"
                    }
                },
            },
            {
                "name": "GetNewReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreatePerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10006",
                        "summary": "Transfer and promotion due to restructuring"
                    }
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10006",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": [
                            "PR5011",
                            "PR10000"
                        ]
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10006"
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1005"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10006\",\n                    \"department_id\": \"DEPT1004\",\n                    \"position_id\": \"POS3010\",\n                    \"role_description\": \"Senior Financial Analyst\",\n                    \"compensation_id\": \"COMP10000\",\n                    \"performance_review_ids\": [\"PR5011\", \"PR10000\"]\n                },\n                {\n                    \"department_id\": \"DEPT1005\",\n                    \"name\": \"Marketing\",\n                    \"budget\": 1300000,\n                    \"description\": \"HIRING FREEZE: H2 2025. Drives brand awareness and demand generation.\"\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_26",
        "instruction": "Effective 2025-06-30, process the termination of Adrian Thompson (E99999). Follow all off-boarding procedures, including clearing his benefits, zeroing out his final compensation, and logging a performance review with the summary 'Termination.' To backfill his duties, update Michael Park's (E10002) role description to 'Interim Team Lead.' For verification, retrieve the updated records for both employees.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E99999"
                },
            },
            {
                "name": "TerminateEmployee",
                "arguments": {
                    "employee_id": "E99999",
                    "termination_date": "2025-06-30"
                },
            },
            {
                "name": "SetEmployeeBenefits",
                "arguments": {
                    "employee_id": "E99999",
                    "benefit_plan_ids": []
                },
            },
            {
                "name": "SetCompensation",
                "arguments": {
                    "compensation": {
                        "compensation_id": "COMP_FINAL_E99999",
                        "employee_id": "E99999",
                        "base_salary": 0,
                        "bonus_target_pct": 0,
                        "equity_grant": 0,
                        "effective_date": "2025-06-30"
                    }
                },
            },
            {
                "name": "GetNewReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreatePerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E99999",
                        "summary": "Termination"
                    }
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E99999",
                    "updates": {
                        "compensation_id": "COMP_FINAL_E99999",
                        "performance_review_ids": [
                            "PR10000"
                        ]
                    }
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10002",
                    "updates": {
                        "role_description": "Interim Team Lead"
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E99999"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10002"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E99999\",\n                    \"status\": \"Terminated\",\n                    \"compensation_id\": \"COMP_FINAL_E99999\",\n                    \"performance_review_ids\": [\"PR10000\"]\n                },\n                {\n                    \"employee_id\": \"E10002\",\n                    \"role_description\": \"Interim Team Lead\"\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_27",
        "instruction": "We're rolling out the existing Legal Insurance plan (BEN9999) to all active, USA-national employees. Enroll all eligible employees IND this plan. As a separate administrative update, also increase the monthly employee cost of the Dental plan (BEN4002) to $25. To verify, provide an updated list of all active USA-national employees.",
        "actions": [
            {
                "name": "UpdateBenefitPlan",
                "arguments": {
                    "benefit_plan_id": "BEN4002",
                    "updates": {
                        "employee_cost_monthly": 25
                    }
                },
            },
            {
                "name": "FindEmployees",
                "arguments": {
                    "filters": {
                        "nationality": "USA",
                        "status": "Active"
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10001"
                },
            },
            {
                "name": "SetEmployeeBenefits",
                "arguments": {
                    "employee_id": "E10001",
                    "benefit_plan_ids": [
                        "BEN4001",
                        "BEN4002",
                        "BEN4003",
                        "BEN9999"
                    ]
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10002"
                },
            },
            {
                "name": "SetEmployeeBenefits",
                "arguments": {
                    "employee_id": "E10002",
                    "benefit_plan_ids": [
                        "BEN4001",
                        "BEN4002",
                        "BEN9999"
                    ]
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "SetEmployeeBenefits",
                "arguments": {
                    "employee_id": "E10003",
                    "benefit_plan_ids": [
                        "BEN4001",
                        "BEN4003",
                        "BEN4004",
                        "BEN9999"
                    ]
                },
            },
            {
                "name": "FindEmployees",
                "arguments": {
                    "filters": {
                        "nationality": "USA",
                        "status": "Active"
                    }
                }
            }
        ],
        "outputs": [
                "\n            {\n                \"count\": 3,\n                \"results\": [\n                    {\n                        \"employee_id\": \"E10001\",\n                        \"first_name\": \"Sophia\",\n                        \"last_name\": \"Nguyen\",\n                        \"preferred_name\": \"Sophia\",\n                        \"date_of_birth\": \"1978-02-16\",\n                        \"gender\": \"Female\",\n                        \"ethnicity_code\": \"W\",\n                        \"nationality\": \"USA\",\n                        \"marital_status\": \"Married\",\n                        \"hire_date\": \"2010-08-02\",\n                        \"termination_date\": null,\n                        \"status\": \"Active\",\n                        \"position_id\": \"POS3001\",\n                        \"department_id\": \"DEPT1001\",\n                        \"level_id\": \"L.C\",\n                        \"manager_id\": null,\n                        \"work_location\": \"Seattle HQ\",\n                        \"work_email\": \"isabella.chen@example.com\",\n                        \"work_phone\": \"+1-415-555-0100\",\n                        \"compensation_id\": \"COMP2001\",\n                        \"benefit_plan_ids\": [\n                            \"BEN4001\",\n                            \"BEN4002\",\n                            \"BEN4003\",\n                            \"BEN9999\"\n                        ],\n                        \"performance_review_ids\": [\n                            \"PR5001\",\n                            \"PR5009\"\n                        ],\n                        \"skills\": [\n                            \"Leadership\",\n                            \"Cloud Architecture\",\n                            \"Python\"\n                        ],\n                        \"role_description\": \"Chief Technology Officer overseeing all engineering functions.\",\n                        \"notes\": \"Founder-level equity grant.\"\n                    },\n                    {\n                        \"employee_id\": \"E10002\",\n                        \"first_name\": \"Daniel\",\n                        \"last_name\": \"Kim\",\n                        \"preferred_name\": \"Dan\",\n                        \"date_of_birth\": \"1982-09-04\",\n                        \"gender\": \"Male\",\n                        \"ethnicity_code\": \"A\",\n                        \"nationality\": \"USA\",\n                        \"marital_status\": \"Single\",\n                        \"hire_date\": \"2015-03-17\",\n                        \"termination_date\": null,\n                        \"status\": \"Active\",\n                        \"position_id\": \"POS3004\",\n                        \"department_id\": \"DEPT1002\",\n                        \"level_id\": \"L.5\",\n                        \"manager_id\": \"E10012\",\n                        \"work_location\": \"Boston Office\",\n                        \"work_email\": \"michael.park@example.com\",\n                        \"work_phone\": \"+1-212-555-0144\",\n                        \"compensation_id\": \"COMP2002\",\n                        \"benefit_plan_ids\": [\n                            \"BEN4001\",\n                            \"BEN4002\",\n                            \"BEN9999\"\n                        ],\n                        \"performance_review_ids\": [\n                            \"PR5002\"\n                        ],\n                        \"skills\": [\n                            \"Sales Strategy\",\n                            \"CRM\",\n                            \"Negotiation\"\n                        ],\n                        \"role_description\": \"Regional VP of Sales for the Eastern territory.\",\n                        \"notes\": \"High performer—President's Club 2023.\"\n                    },\n                    {\n                        \"employee_id\": \"E10003\",\n                        \"first_name\": \"Amelia\",\n                        \"last_name\": \"Garcia\",\n                        \"preferred_name\": \"Amy\",\n                        \"date_of_birth\": \"1990-11-22\",\n                        \"gender\": \"Female\",\n                        \"ethnicity_code\": \"H\",\n                        \"nationality\": \"USA\",\n                        \"marital_status\": \"Partnered\",\n                        \"hire_date\": \"2019-06-10\",\n                        \"termination_date\": null,\n                        \"status\": \"Active\",\n                        \"position_id\": \"POS3006\",\n                        \"department_id\": \"DEPT1005\",\n                        \"level_id\": \"L.3\",\n                        \"manager_id\": \"E10001\",\n                        \"work_location\": \"Remote – Dallas, TX\",\n                        \"work_email\": \"emma.rodriguez@example.com\",\n                        \"work_phone\": \"+1-737-555-0188\",\n                        \"compensation_id\": \"COMP2003\",\n                        \"benefit_plan_ids\": [\n                            \"BEN4001\",\n                            \"BEN4003\",\n                            \"BEN4004\",\n                            \"BEN9999\"\n                        ],\n                        \"performance_review_ids\": [\n                            \"PR5003\",\n                            \"PR5010\"\n                        ],\n                        \"skills\": [\n                            \"TypeScript\",\n                            \"React\",\n                            \"Accessibility\"\n                        ],\n                        \"role_description\": \"Senior Front-end Engineer on the web platform team.\",\n                        \"notes\": \"On parental leave 2024-11-01 → 2025-02-01.\"\n                    }\n                ]\n            }\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_28",
        "instruction": "Create a new 'Tech Allowance' benefit plan with ID BEN10003 and provider 'HR Ops'. Enroll all active staff IND the Engineering department (DEPT1001). Concurrently, promote the department head, Isabella Chen (E10001), to 'Principal Engineer' (POS4001) at level L.D, which includes a 5% salary increase, effective 2025-07-24. Log a performance review for her with the summary 'Promotion and benefit rollout oversight.' For verification, retrieve the updated records for Sophia and the Engineering department.",
        "actions": [
            {
                "name": "CreateBenefitPlan",
                "arguments": {
                    "benefit_plan": {
                        "benefit_plan_id": "BEN10003",
                        "name": "Tech Allowance",
                        "provider": "HR Ops"
                    }
                },
            },
            {
                "name": "FindEmployees",
                "arguments": {
                    "filters": {
                        "department_id": "DEPT1001",
                        "status": "Active"
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10001"
                },
            },
            {
                "name": "SetEmployeeBenefits",
                "arguments": {
                    "employee_id": "E10001",
                    "benefit_plan_ids": [
                        "BEN4001",
                        "BEN4002",
                        "BEN4003",
                        "BEN10003"
                    ]
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10004"
                },
            },
            {
                "name": "SetEmployeeBenefits",
                "arguments": {
                    "employee_id": "E10004",
                    "benefit_plan_ids": [
                        "BEN4001",
                        "BEN4003",
                        "BEN10003"
                    ]
                },
            },
            {
                "name": "GetCompensationByEmployeeId",
                "arguments": {
                    "employee_id": "E10001"
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10001",
                    "updates": {
                        "position_id": "POS4001",
                        "level_id": "L.D",
                        "role_description": "Principal Engineer"
                    }
                },
            },
            {
                "name": "GetNewCompensationId",
                "arguments": {
                {}
                },
            },
            {
                "name": "SetCompensation",
                "arguments": {
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10001",
                        "base_salary": 341250,
                        "bonus_target_pct": 30,
                        "equity_grant": 75000,
                        "currency": "USD",
                        "effective_date": "2025-07-24"
                    }
                },
            },
            {
                "name": "GetNewReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreatePerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10001",
                        "summary": "Promotion and benefit rollout oversight"
                    }
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10001",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": [
                            "PR5001",
                            "PR10000"
                        ]
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10001"
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1001"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10001\",\n                    \"position_id\": \"POS4001\",\n                    \"level_id\": \"L.D\",\n                    \"role_description\": \"Principal Engineer\",\n                    \"compensation_id\": \"COMP10000\",\n                    \"performance_review_ids\": [\"PR5001\", \"PR10000\"]\n                },\n                {\n                    \"department_id\": \"DEPT1001\",\n                    \"name\": \"Engineering\"\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_29",
        "instruction": "Create a new 'Diversity Scholarship' benefit plan with ID BEN10004, provider 'HR D&I', and an annual amount of $2,000. Once created, enroll all active employees with an ethnicity code of either 'H' or 'B'. For each enrolled employee, append the following to their record's notes field: 'Enrolled IND Diversity Scholarship 2025.'. For verification, provide a list of the updated records for all employees who were enrolled.",
        "actions": [
            {
                "name": "CreateBenefitPlan",
                "arguments": {
                    "benefit_plan": {
                        "benefit_plan_id": "BEN10004",
                        "name": "Diversity Scholarship",
                        "provider": "HR D&I",
                        "annual_amount": 2000
                    }
                },
            },
            {
                "name": "FindEmployees",
                "arguments": {
                    "filters": {
                        "status": "Active",
                        "ethnicity_code": "H"
                    }
                },
            },
            {
                "name": "FindEmployees",
                "arguments": {
                    "filters": {
                        "status": "Active",
                        "ethnicity_code": "B"
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "SetEmployeeBenefits",
                "arguments": {
                    "employee_id": "E10003",
                    "benefit_plan_ids": [
                        "BEN4001",
                        "BEN4003",
                        "BEN4004",
                        "BEN10004"
                    ]
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10003",
                    "updates": {
                        "notes": "On parental leave 2024-11-01 → 2025-02-01. Enrolled IND Diversity Scholarship 2025."
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10005"
                },
            },
            {
                "name": "SetEmployeeBenefits",
                "arguments": {
                    "employee_id": "E10005",
                    "benefit_plan_ids": [
                        "BEN4001",
                        "BEN4005",
                        "BEN10004"
                    ]
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10005",
                    "updates": {
                        "notes": "Recent graduate—ESADE Business School. Enrolled IND Diversity Scholarship 2025."
                    }
                },
            },
            {
                "name": "FindEmployees",
                "arguments": {
                    "filters": {
                        "status": "Active",
                        "ethnicity_code": "H"
                    }
                }
            }
        ],
        "outputs": [
                "\n            {\n                \"count\": 2,\n                \"results\": [\n                    {\n                        \"employee_id\": \"E10003\",\n                        \"first_name\": \"Amelia\",\n                        \"last_name\": \"Garcia\",\n                        \"preferred_name\": \"Amy\",\n                        \"date_of_birth\": \"1990-11-22\",\n                        \"gender\": \"Female\",\n                        \"ethnicity_code\": \"H\",\n                        \"nationality\": \"USA\",\n                        \"marital_status\": \"Partnered\",\n                        \"hire_date\": \"2019-06-10\",\n                        \"termination_date\": null,\n                        \"status\": \"Active\",\n                        \"position_id\": \"POS3006\",\n                        \"department_id\": \"DEPT1005\",\n                        \"level_id\": \"L.3\",\n                        \"manager_id\": \"E10001\",\n                        \"work_location\": \"Remote – Dallas, TX\",\n                        \"work_email\": \"emma.rodriguez@example.com\",\n                        \"work_phone\": \"+1-737-555-0188\",\n                        \"compensation_id\": \"COMP2003\",\n                        \"benefit_plan_ids\": [\n                            \"BEN4001\",\n                            \"BEN4003\",\n                            \"BEN4004\",\n                            \"BEN10004\"\n                        ],\n                        \"performance_review_ids\": [\n                            \"PR5003\",\n                            \"PR5010\"\n                        ],\n                        \"skills\": [\n                            \"TypeScript\",\n                            \"React\",\n                            \"Accessibility\"\n                        ],\n                        \"role_description\": \"Senior Front-end Engineer on the web platform team.\",\n                        \"notes\": \"On parental leave 2024-11-01 → 2025-02-01. Enrolled IND Diversity Scholarship 2025.\"\n                    },\n                    {\n                        \"employee_id\": \"E10005\",\n                        \"first_name\": \"Elena\",\n                        \"last_name\": \"Rodriguez\",\n                        \"preferred_name\": \"Elena\",\n                        \"date_of_birth\": \"1995-01-30\",\n                        \"gender\": \"Female\",\n                        \"ethnicity_code\": \"H\",\n                        \"nationality\": \"ESP\",\n                        \"marital_status\": \"Single\",\n                        \"hire_date\": \"2024-09-01\",\n                        \"termination_date\": null,\n                        \"status\": \"Active\",\n                        \"position_id\": \"POS3010\",\n                        \"department_id\": \"DEPT1004\",\n                        \"level_id\": \"L.1\",\n                        \"manager_id\": \"E10011\",\n                        \"work_location\": \"Barcelona Office\",\n                        \"work_email\": \"olivia.martinez@example.com\",\n                        \"work_phone\": \"+34-91-555-0200\",\n                        \"compensation_id\": \"COMP2005\",\n                        \"benefit_plan_ids\": [\n                            \"BEN4001\",\n                            \"BEN4005\",\n                            \"BEN10004\"\n                        ],\n                        \"performance_review_ids\": [],\n                        \"skills\": [\n                            \"Financial Modeling\",\n                            \"SQL\",\n                            \"Excel\"\n                        ],\n                        \"role_description\": \"Junior Financial Analyst supporting quarterly forecasts.\",\n                        \"notes\": \"Recent graduate—ESADE Business School. Enrolled IND Diversity Scholarship 2025.\"\n                    }\n                ]\n            }\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_30",
        "instruction": "Effective 2025-07-01, promote Arjun Patel (E10004) to 'Lead Backend Engineer' (POS3009) at level L.3, which includes an 8% salary increase. To backfill his role, transfer Michael Park (E10002) to Rahul's previous department (DEPT1001) and manager (E10003). Log a performance review for Rahul with the summary 'Promotion to Lead Engineer.' Also, update the description of the Engineering department (DEPT1001) to 'Core product and platform engineering.' For verification, retrieve the updated records for Arjun Patel and the Engineering department.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10004"
                },
            },
            {
                "name": "GetCompensationByEmployeeId",
                "arguments": {
                    "employee_id": "E10004"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10002"
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10004",
                    "updates": {
                        "position_id": "POS3009",
                        "level_id": "L.3",
                        "role_description": "Lead Backend Engineer"
                    }
                },
            },
            {
                "name": "GetNewCompensationId",
                "arguments": {
                {}
                },
            },
            {
                "name": "SetCompensation",
                "arguments": {
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10004",
                        "base_salary": 127440,
                        "bonus_target_pct": 10,
                        "equity_grant": 8000,
                        "currency": "USD",
                        "effective_date": "2025-07-01"
                    }
                },
            },
            {
                "name": "GetNewReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreatePerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10004",
                        "summary": "Promotion to Lead Engineer"
                    }
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10004",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": [
                            "PR5004",
                            "PR5009",
                            "PR10000"
                        ]
                    }
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10002",
                    "updates": {
                        "department_id": "DEPT1001",
                        "manager_id": "E10003"
                    }
                },
            },
            {
                "name": "UpdateDepartmentRecord",
                "arguments": {
                    "department_id": "DEPT1001",
                    "updates": {
                        "description": "Core product and platform engineering."
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10004"
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1001"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10004\",\n                    \"position_id\": \"POS3009\",\n                    \"level_id\": \"L.3\",\n                    \"compensation_id\": \"COMP10000\",\n                    \"performance_review_ids\": [\"PR5004\", \"PR5009\", \"PR10000\"]\n                },\n                {\n                    \"department_id\": \"DEPT1001\",\n                    \"name\": \"Engineering\",\n                    \"description\": \"Core product and platform engineering.\"\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_31",
        "instruction": "Onboard a new Engineering Intern, Liam Chen, effective 2025-07-01, into the Engineering department (DEPT1001) with a $35,000 salary. His manager will be Emma Rodriguez (E10003). Log a performance review for Liam with the summary 'New hire onboarding.' To fund the new role, transfer $50,000 from the Sales department (DEPT1002) to Engineering. For verification, retrieve the updated records for Liam Chen and the Engineering department.",
        "actions": [
            {
                "name": "GetNewEmployeeId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateNewEmployee",
                "arguments": {
                    "employee": {
                        "employee_id": "E10000",
                        "first_name": "Liam",
                        "last_name": "Chen",
                        "status": "Active",
                        "hire_date": "2025-07-01",
                        "department_id": "DEPT1001",
                        "manager_id": "E10003",
                        "role_description": "Engineering Intern"
                    }
                },
            },
            {
                "name": "GetNewCompensationId",
                "arguments": {
                {}
                },
            },
            {
                "name": "SetCompensation",
                "arguments": {
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10000",
                        "base_salary": 35000,
                        "currency": "USD",
                        "effective_date": "2025-07-01"
                    }
                },
            },
            {
                "name": "GetNewReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreatePerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10000",
                        "summary": "New hire onboarding"
                    }
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10000",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": [
                            "PR10000"
                        ]
                    }
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1002"
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1001"
                },
            },
            {
                "name": "UpdateDepartmentRecord",
                "arguments": {
                    "department_id": "DEPT1002",
                    "updates": {
                        "budget": 4950000
                    }
                },
            },
            {
                "name": "UpdateDepartmentRecord",
                "arguments": {
                    "department_id": "DEPT1001",
                    "updates": {
                        "budget": 7050000
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10000"
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1001"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10000\",\n                    \"first_name\": \"Liam\",\n                    \"last_name\": \"Chen\",\n                    \"department_id\": \"DEPT1001\",\n                    \"manager_id\": \"E10003\",\n                    \"compensation_id\": \"COMP10000\",\n                    \"performance_review_ids\": [\"PR10000\"]\n                },\n                {\n                    \"department_id\": \"DEPT1001\",\n                    \"name\": \"Engineering\",\n                    \"budget\": 7050000\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_32",
        "instruction": "Finalize Isabella Chen's (E10001) parental leave (LV7001) by updating its status to 'Approved'. Appoint Emma Rodriguez (E10003) as acting manager. As part of this temporary role, process a 5% salary increase for Amelia, effective on the leave start date of 2025-07-01. Log a performance review for Amelia with the summary 'Acting manager assignment.' For verification, retrieve both updated employee records.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10001"
                },
            },
            {
                "name": "UpdateLeaveStatus",
                "arguments": {
                    "leave_id": "LV7001",
                    "status": "Approved"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "GetCompensationByEmployeeId",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10003",
                    "updates": {
                        "role_description": "Acting Manager"
                    }
                },
            },
            {
                "name": "GetNewCompensationId",
                "arguments": {
                {}
                },
            },
            {
                "name": "SetCompensation",
                "arguments": {
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10003",
                        "base_salary": 152250,
                        "bonus_target_pct": 15,
                        "equity_grant": 15000,
                        "currency": "USD",
                        "effective_date": "2025-07-01"
                    }
                },
            },
            {
                "name": "GetNewReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreatePerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "Acting manager assignment"
                    }
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10003",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": [
                            "PR5003",
                            "PR5010",
                            "PR10000"
                        ]
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10001"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10003"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10001\"\n                },\n                {\n                    \"employee_id\": \"E10003\",\n                    \"role_description\": \"Acting Manager\",\n                    \"compensation_id\": \"COMP10000\",\n                    \"performance_review_ids\": [\"PR5003\", \"PR5010\", \"PR10000\"]\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_33",
        "instruction": "As part of a personnel file audit, log a review for Isabella Chen (E10001) with the summary 'Q3 2025 personnel file audit completed.' Concurrently, transfer Michael Park (E10002) to her department (DEPT1001) and make Sophia his new manager. As part of his transfer, process a 5% salary increase for him, effective 2025-07-01. For verification, retrieve both updated employee records.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10001"
                },
            },
            {
                "name": "GetNewReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreatePerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10001",
                        "summary": "Q3 2025 personnel file audit completed."
                    }
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10001",
                    "updates": {
                        "performance_review_ids": [
                            "PR5001",
                            "PR10000"
                        ]
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10002"
                },
            },
            {
                "name": "GetCompensationByEmployeeId",
                "arguments": {
                    "employee_id": "E10002"
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10002",
                    "updates": {
                        "department_id": "DEPT1001",
                        "manager_id": "E10001"
                    }
                },
            },
            {
                "name": "GetNewCompensationId",
                "arguments": {
                {}
                },
            },
            {
                "name": "SetCompensation",
                "arguments": {
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10002",
                        "base_salary": 220500,
                        "bonus_target_pct": 25,
                        "equity_grant": 40000,
                        "currency": "USD",
                        "effective_date": "2025-07-01"
                    }
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10002",
                    "updates": {
                        "compensation_id": "COMP10000"
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10001"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10002"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10001\",\n                    \"performance_review_ids\": [\"PR5001\", \"PR10000\"]\n                },\n                {\n                    \"employee_id\": \"E10002\",\n                    \"department_id\": \"DEPT1001\",\n                    \"manager_id\": \"E10001\",\n                    \"compensation_id\": \"COMP10000\"\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_34",
        "instruction": "We're launching a new Employee Stock Purchase Plan (ESPP). Create the benefit plan with ID BEN10005, provider 'Fidelity', and 0% employer coverage. Per the policy, you need to auto-enroll all active employees who are at level L.4 or higher (L.4, L.5, and L.C). Once they are all enrolled, please pull up the employee record for Isabella Chen (E10001) to verify the change.",
        "actions": [
            {
                "name": "CreateBenefitPlan",
                "arguments": {
                    "benefit_plan": {
                        "benefit_plan_id": "BEN10005",
                        "name": "Employee Stock Purchase Plan",
                        "provider": "Fidelity",
                        "employer_coverage_pct": 0
                    }
                },
            },
            {
                "name": "FindEmployees",
                "arguments": {
                    "filters": {
                        "level_id": "L.4",
                        "status": "Active"
                    }
                },
            },
            {
                "name": "FindEmployees",
                "arguments": {
                    "filters": {
                        "level_id": "L.5",
                        "status": "Active"
                    }
                },
            },
            {
                "name": "FindEmployees",
                "arguments": {
                    "filters": {
                        "level_id": "L.C",
                        "status": "Active"
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10001"
                },
            },
            {
                "name": "SetEmployeeBenefits",
                "arguments": {
                    "employee_id": "E10001",
                    "benefit_plan_ids": [
                        "BEN4001",
                        "BEN4002",
                        "BEN4003",
                        "BEN10005"
                    ]
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10002"
                },
            },
            {
                "name": "SetEmployeeBenefits",
                "arguments": {
                    "employee_id": "E10002",
                    "benefit_plan_ids": [
                        "BEN4001",
                        "BEN4002",
                        "BEN10005"
                    ]
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10006"
                },
            },
            {
                "name": "SetEmployeeBenefits",
                "arguments": {
                    "employee_id": "E10006",
                    "benefit_plan_ids": [
                        "BEN4001",
                        "BEN4002",
                        "BEN4003",
                        "BEN10005"
                    ]
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10001"
                }
            }
        ],
        "outputs": [
                "\n            {\n                \"employee_id\": \"E10001\",\n                \"first_name\": \"Sophia\",\n                \"last_name\": \"Nguyen\",\n                \"preferred_name\": \"Sophia\",\n                \"date_of_birth\": \"1978-02-16\",\n                \"gender\": \"Female\",\n                \"ethnicity_code\": \"W\",\n                \"nationality\": \"USA\",\n                \"marital_status\": \"Married\",\n                \"hire_date\": \"2010-08-02\",\n                \"termination_date\": null,\n                \"status\": \"Active\",\n                \"position_id\": \"POS3001\",\n                \"department_id\": \"DEPT1001\",\n                \"level_id\": \"L.C\",\n                \"manager_id\": null,\n                \"work_location\": \"Seattle HQ\",\n                \"work_email\": \"isabella.chen@example.com\",\n                \"work_phone\": \"+1-415-555-0100\",\n                \"compensation_id\": \"COMP2001\",\n                \"benefit_plan_ids\": [\n                    \"BEN4001\",\n                    \"BEN4002\",\n                    \"BEN4003\",\n                    \"BEN10005\"\n                ],\n                \"performance_review_ids\": [\n                    \"PR5001\",\n                    \"PR5009\"\n                ],\n                \"skills\": [\n                    \"Leadership\",\n                    \"Cloud Architecture\",\n                    \"Python\"\n                ],\n                \"role_description\": \"Chief Technology Officer overseeing all engineering functions.\",\n                \"notes\": \"Founder-level equity grant.\"\n            }\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_35",
        "instruction": "Effective 2025-07-24, process a benefits and compensation update for Olivia Martinez (E10005). Discontinue her 'Commuter Stipend - EU' (BEN4005) and enroll her IND two replacement plans: Dental (BEN4002) and Legal Insurance (BEN9999). As part of this update, also process a 5% salary increase. Log a single performance review with the summary 'Benefit and compensation update.' To fund the salary increase, increase the Finance department's (DEPT1004) budget by the exact amount of her raise. For verification, retrieve her updated employee record and the updated Finance department record.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10005"
                },
            },
            {
                "name": "GetCompensationByEmployeeId",
                "arguments": {
                    "employee_id": "E10005"
                },
            },
            {
                "name": "SetEmployeeBenefits",
                "arguments": {
                    "employee_id": "E10005",
                    "benefit_plan_ids": [
                        "BEN4001",
                        "BEN4002",
                        "BEN9999"
                    ]
                },
            },
            {
                "name": "GetNewCompensationId",
                "arguments": {
                {}
                },
            },
            {
                "name": "SetCompensation",
                "arguments": {
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10005",
                        "base_salary": 75600,
                        "bonus_target_pct": 5,
                        "equity_grant": 2000,
                        "currency": "EUR",
                        "effective_date": "2025-07-24"
                    }
                },
            },
            {
                "name": "GetNewReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreatePerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10005",
                        "summary": "Benefit and compensation update"
                    }
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10005",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": [
                            "PR10000"
                        ]
                    }
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1004"
                },
            },
            {
                "name": "UpdateDepartmentRecord",
                "arguments": {
                    "department_id": "DEPT1004",
                    "updates": {
                        "budget": 1203600
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10005"
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1004"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10005\",\n                    \"benefit_plan_ids\": [\"BEN4001\", \"BEN4002\", \"BEN9999\"],\n                    \"compensation_id\": \"COMP10000\",\n                    \"performance_review_ids\": [\"PR10000\"]\n                },\n                {\n                    \"department_id\": \"DEPT1004\",\n                    \"name\": \"Finance\",\n                    \"budget\": 1203600\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_36",
        "instruction": "Effective 2025-07-01, process a 3% cost-of-living adjustment (COLA) for Olivia Martinez (E10005) by creating a new compensation record. Concurrently, promote the Finance department head, William Liu (E10006), to 'Senior Director' (POS4003). Log a single performance review for Marcus with the summary 'Promotion to Senior Director.' Increase the Finance department budget by $50,000 to cover these changes. For verification, retrieve the updated records for both employees and the Finance department.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10005"
                },
            },
            {
                "name": "GetCompensationByEmployeeId",
                "arguments": {
                    "employee_id": "E10005"
                },
            },
            {
                "name": "GetNewCompensationId",
                "arguments": {
                {}
                },
            },
            {
                "name": "SetCompensation",
                "arguments": {
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10005",
                        "base_salary": 74160,
                        "bonus_target_pct": 5,
                        "equity_grant": 2000,
                        "currency": "EUR",
                        "effective_date": "2025-07-01"
                    }
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10005",
                    "updates": {
                        "compensation_id": "COMP10000"
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10006"
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10006",
                    "updates": {
                        "position_id": "POS4003",
                        "role_description": "Senior Director"
                    }
                },
            },
            {
                "name": "GetNewReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreatePerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10006",
                        "summary": "Promotion to Senior Director"
                    }
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10006",
                    "updates": {
                        "performance_review_ids": [
                            "PR5011",
                            "PR10000"
                        ]
                    }
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1004"
                },
            },
            {
                "name": "UpdateDepartmentRecord",
                "arguments": {
                    "department_id": "DEPT1004",
                    "updates": {
                        "budget": 1250000
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10005"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10006"
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1004"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10005\",\n                    \"compensation_id\": \"COMP10000\"\n                },\n                {\n                    \"employee_id\": \"E10006\",\n                    \"position_id\": \"POS4003\",\n                    \"role_description\": \"Senior Director\",\n                    \"performance_review_ids\": [\"PR5011\", \"PR10000\"]\n                },\n                {\n                    \"department_id\": \"DEPT1004\",\n                    \"name\": \"Finance\",\n                    \"budget\": 1250000\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_37",
        "instruction": "We're adding a new 'Mental-Health Support' benefit. Create the new plan with ID BEN10006, provider 'Lyra Health', 100 sessions per year, and 100% employer coverage. This benefit should be rolled out to all active employees with USA nationality. To verify the rollout is complete, pull up the updated employee record for Michael Park (E10002).",
        "actions": [
            {
                "name": "CreateBenefitPlan",
                "arguments": {
                    "benefit_plan": {
                        "benefit_plan_id": "BEN10006",
                        "name": "Mental-Health Support",
                        "provider": "Lyra Health",
                        "sessions_per_year": 100,
                        "employer_coverage_pct": 100
                    }
                },
            },
            {
                "name": "FindEmployees",
                "arguments": {
                    "filters": {
                        "nationality": "USA",
                        "status": "Active"
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10001"
                },
            },
            {
                "name": "SetEmployeeBenefits",
                "arguments": {
                    "employee_id": "E10001",
                    "benefit_plan_ids": [
                        "BEN4001",
                        "BEN4002",
                        "BEN4003",
                        "BEN10006"
                    ]
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10002"
                },
            },
            {
                "name": "SetEmployeeBenefits",
                "arguments": {
                    "employee_id": "E10002",
                    "benefit_plan_ids": [
                        "BEN4001",
                        "BEN4002",
                        "BEN10006"
                    ]
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "SetEmployeeBenefits",
                "arguments": {
                    "employee_id": "E10003",
                    "benefit_plan_ids": [
                        "BEN4001",
                        "BEN4003",
                        "BEN4004",
                        "BEN10006"
                    ]
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10002"
                }
            }
        ],
        "outputs": [
                "\n            {\n                \"employee_id\": \"E10002\",\n                \"first_name\": \"Daniel\",\n                \"last_name\": \"Kim\",\n                \"preferred_name\": \"Dan\",\n                \"date_of_birth\": \"1982-09-04\",\n                \"gender\": \"Male\",\n                \"ethnicity_code\": \"A\",\n                \"nationality\": \"USA\",\n                \"marital_status\": \"Single\",\n                \"hire_date\": \"2015-03-17\",\n                \"termination_date\": null,\n                \"status\": \"Active\",\n                \"position_id\": \"POS3004\",\n                \"department_id\": \"DEPT1002\",\n                \"level_id\": \"L.5\",\n                \"manager_id\": \"E10012\",\n                \"work_location\": \"Boston Office\",\n                \"work_email\": \"michael.park@example.com\",\n                \"work_phone\": \"+1-212-555-0144\",\n                \"compensation_id\": \"COMP2002\",\n                \"benefit_plan_ids\": [\n                    \"BEN4001\",\n                    \"BEN4002\",\n                    \"BEN10006\"\n                ],\n                \"performance_review_ids\": [\n                    \"PR5002\"\n                ],\n                \"skills\": [\n                    \"Sales Strategy\",\n                    \"CRM\",\n                    \"Negotiation\"\n                ],\n                \"role_description\": \"Regional VP of Sales for the Eastern territory.\",\n                \"notes\": \"High performer—President's Club 2023.\"\n            }\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_38",
        "instruction": "Effective 2025-07-24, promote Emma Rodriguez (E10003) to a 'Senior Engineer' role (POS3005) at level L.4 and update her role description to 'Senior Engineer'. This promotion includes an 8% salary increase. To backfill her previous role, transfer Arjun Patel (E10004) to her old position (POS3006). Log a performance review for Amelia with the summary 'Promotion to Senior Engineer.' To fund the promotion, transfer $20,000 from the Sales department's budget (DEPT1002) to Engineering (DEPT1001). For verification, retrieve the updated records for both employees and the Engineering department.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "GetCompensationByEmployeeId",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10003",
                    "updates": {
                        "position_id": "POS3005",
                        "level_id": "L.4",
                        "role_description": "Senior Engineer"
                    }
                },
            },
            {
                "name": "GetNewCompensationId",
                "arguments": {
                {}
                },
            },
            {
                "name": "SetCompensation",
                "arguments": {
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10003",
                        "base_salary": 156600,
                        "bonus_target_pct": 15,
                        "equity_grant": 15000,
                        "currency": "USD",
                        "effective_date": "2025-07-24"
                    }
                },
            },
            {
                "name": "GetNewReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreatePerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "Promotion to Senior Engineer"
                    }
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10003",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": [
                            "PR5003",
                            "PR5010",
                            "PR10000"
                        ]
                    }
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10004",
                    "updates": {
                        "position_id": "POS3006"
                    }
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1002"
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1001"
                },
            },
            {
                "name": "UpdateDepartmentRecord",
                "arguments": {
                    "department_id": "DEPT1002",
                    "updates": {
                        "budget": 4980000
                    }
                },
            },
            {
                "name": "UpdateDepartmentRecord",
                "arguments": {
                    "department_id": "DEPT1001",
                    "updates": {
                        "budget": 7020000
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10004"
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1001"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10003\",\n                    \"position_id\": \"POS3005\",\n                    \"level_id\": \"L.4\",\n                    \"compensation_id\": \"COMP10000\",\n                    \"performance_review_ids\": [\"PR5003\", \"PR5010\", \"PR10000\"]\n                },\n                {\n                    \"employee_id\": \"E10004\",\n                    \"position_id\": \"POS3006\"\n                },\n                {\n                    \"department_id\": \"DEPT1001\",\n                    \"name\": \"Engineering\",\n                    \"budget\": 7020000\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_39",
        "instruction": "As a performance reward for Isabella Chen (E10001), whose most recent rating was 'Exceeds', increase her bonus target by 10 percentage points, effective 2025-07-01. Log a performance review with the summary 'Exceeds Performance Bonus.' To support her, transfer Arjun Patel (E10004) to her team as a direct report. To fund the bonus, transfer $10,000 from the HR department's budget (DEPT1003) to Engineering (DEPT1001). For verification, retrieve the updated records for both employees and the Engineering department.",
        "actions": [
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10001"
                },
            },
            {
                "name": "GetPerformanceReviewsByEmployeeId",
                "arguments": {
                    "employee_id": "E10001"
                },
            },
            {
                "name": "GetCompensationByEmployeeId",
                "arguments": {
                    "employee_id": "E10001"
                },
            },
            {
                "name": "GetNewCompensationId",
                "arguments": {
                {}
                },
            },
            {
                "name": "SetCompensation",
                "arguments": {
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E10001",
                        "base_salary": 325000,
                        "bonus_target_pct": 40,
                        "equity_grant": 75000,
                        "currency": "USD",
                        "effective_date": "2025-07-01"
                    }
                },
            },
            {
                "name": "GetNewReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreatePerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10001",
                        "summary": "Exceeds Performance Bonus"
                    }
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10001",
                    "updates": {
                        "compensation_id": "COMP10000",
                        "performance_review_ids": [
                            "PR5001",
                            "PR10000"
                        ]
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10004"
                },
            },
            {
                "name": "UpdateEmployeeRecord",
                "arguments": {
                    "employee_id": "E10004",
                    "updates": {
                        "manager_id": "E10001"
                    }
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1003"
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1001"
                },
            },
            {
                "name": "UpdateDepartmentRecord",
                "arguments": {
                    "department_id": "DEPT1003",
                    "updates": {
                        "budget": 790000
                    }
                },
            },
            {
                "name": "UpdateDepartmentRecord",
                "arguments": {
                    "department_id": "DEPT1001",
                    "updates": {
                        "budget": 7010000
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10001"
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10004"
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1001"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10001\",\n                    \"compensation_id\": \"COMP10000\",\n                    \"performance_review_ids\": [\"PR5001\", \"PR10000\"]\n                },\n                {\n                    \"employee_id\": \"E10004\",\n                    \"manager_id\": \"E10001\"\n                },\n                {\n                    \"department_id\": \"DEPT1001\",\n                    \"name\": \"Engineering\",\n                    \"budget\": 7010000\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_40",
        "instruction": "Create a new 'Remote-Work Stipend' benefit plan with ID BEN10007, provider 'HR Ops', and an annual amount of $1,500. Next, enroll all active employees whose work location is either 'Remote \u2013\u00a0Austin,\u00a0TX' or 'Remote \u2013\u00a0Bangalore'. To fund this, increase the budget of each remote employee's respective department by $1,500. For verification, provide an updated list of all departments.",
        "actions": [
            {
                "name": "CreateBenefitPlan",
                "arguments": {
                    "benefit_plan": {
                        "benefit_plan_id": "BEN10007",
                        "name": "Remote-Work Stipend",
                        "provider": "HR Ops",
                        "annual_amount": 1500
                    }
                },
            },
            {
                "name": "FindEmployees",
                "arguments": {
                    "filters": {
                        "work_location": "Remote – Austin, TX",
                        "status": "Active"
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "SetEmployeeBenefits",
                "arguments": {
                    "employee_id": "E10003",
                    "benefit_plan_ids": [
                        "BEN4001",
                        "BEN4003",
                        "BEN4004",
                        "BEN10007"
                    ]
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1005"
                },
            },
            {
                "name": "UpdateDepartmentRecord",
                "arguments": {
                    "department_id": "DEPT1005",
                    "updates": {
                        "budget": 1601500
                    }
                },
            },
            {
                "name": "FindEmployees",
                "arguments": {
                    "filters": {
                        "work_location": "Remote – Bangalore",
                        "status": "Active"
                    }
                },
            },
            {
                "name": "GetEmployeeById",
                "arguments": {
                    "employee_id": "E10004"
                },
            },
            {
                "name": "SetEmployeeBenefits",
                "arguments": {
                    "employee_id": "E10004",
                    "benefit_plan_ids": [
                        "BEN4001",
                        "BEN4003",
                        "BEN10007"
                    ]
                },
            },
            {
                "name": "GetDepartmentById",
                "arguments": {
                    "department_id": "DEPT1001"
                },
            },
            {
                "name": "UpdateDepartmentRecord",
                "arguments": {
                    "department_id": "DEPT1001",
                    "updates": {
                        "budget": 7001500
                    }
                },
            },
            {
                "name": "ListDepartments",
                "arguments": {
                {}
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"department_id\": \"DEPT1001\",\n                    \"name\": \"Engineering\",\n                    \"head_id\": \"E10001\",\n                    \"location\": \"Seattle HQ\",\n                    \"budget\": 7001500,\n                    \"description\": \"Responsible for all product development and technical operations.\"\n                },\n                {\n                    \"department_id\": \"DEPT1002\",\n                    \"name\": \"Sales\",\n                    \"head_id\": \"E10012\",\n                    \"location\": \"Boston Office\",\n                    \"budget\": 5000000,\n                    \"description\": \"Owns revenue generation and customer relationships.\"\n                },\n                {\n                    \"department_id\": \"DEPT1003\",\n                    \"name\": \"Human Resources\",\n                    \"head_id\": \"E10009\",\n                    \"location\": \"Seattle HQ\",\n                    \"budget\": 800000,\n                    \"description\": \"Manages recruitment, retention, and employee well-being.\"\n                },\n                {\n                    \"department_id\": \"DEPT1004\",\n                    \"name\": \"Finance\",\n                    \"head_id\": \"E10011\",\n                    \"location\": \"Barcelona Office\",\n                    \"budget\": 1200000,\n                    \"description\": \"Oversees accounting, compliance, and financial planning.\"\n                },\n                {\n                    \"department_id\": \"DEPT1005\",\n                    \"name\": \"Marketing\",\n                    \"head_id\": \"E10013\",\n                    \"location\": \"Manchester Office\",\n                    \"budget\": 1601500,\n                    \"description\": \"Drives brand awareness and demand generation.\"\n                }\n            ]\n            "
        ]
    }
]
