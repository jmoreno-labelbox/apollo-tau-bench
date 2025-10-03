# Copyright Sierra

tasks = [
    {
        "annotator": 0,
        "user_id": "res_01",
        "instruction": "Starting on 2026-05-22, handle the promotion of Emma Rodriguez (E10003) to 'Lead Compliance Officer' (POS4002) at level L.4, which ensures an 8% salary increase. To facilitate her new responsibilities, coordinate the reassignment of Michael Park (E10002) as her direct report. Log a performance evaluation for Amelia under the summary 'Promotion to Lead Compliance Officer.' Retrieve the updated employee information for both to verify.",
        "actions": [
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10003",
                    "updates": {
                        "position_id": "POS4002",
                        "level_id": "L.4",
                        "role_description": "Lead Compliance Officer"
                    }
                },
            },
            {
                "name": "GetUnusedCompensationId",
                "arguments": {
                {}
                },
            },
            {
                "name": "IncreaseEmployeeCompensation",
                "arguments": {
                    "employee_id": "E10003",
                    "compensation_id": "COMP10000",
                    "effective_date": "2026-05-22",
                    "salary_increase_pct": 8
                },
            },
            {
                "name": "GetUnusedReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "Promotion to Lead Compliance Officer"
                    }
                },
            },
            {
                "name": "UpdateEmployee",
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
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10002",
                    "updates": {
                        "manager_id": "E10003"
                    }
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10002"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10003\",\n                    \"position_id\": \"POS4002\",\n                    \"level_id\": \"L.4\",\n                    \"role_description\": \"Lead Compliance Officer\",\n                    \"compensation_id\": \"COMP10000\",\n                    \"performance_review_ids\": [\"PR5003\", \"PR5010\", \"PR10000\"]\n                },\n                {\n                    \"employee_id\": \"E10002\",\n                    \"manager_id\": \"E10003\"\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_02",
        "instruction": "Beginning on 2026-05-25, carry out an equity refresh for Emma Rodriguez (E10003), providing her with an additional $20,000 IND equity. Since this advances her to a new equity tier, alter her role description to 'Principal Engineer', upload her signed 'Equity Grant Agreement' document, and register a performance evaluation with the summary 'Equity refresh and tier promotion.' To acknowledge her manager, Isabella Chen (E10001), for 'Mentorship excellence,' issue a one-time bonus of $1,000. Obtain both updated employee records for confirmation.",
        "actions": [
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "GetCompensation",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "GetUnusedCompensationId",
                "arguments": {
                {}
                },
            },
            {
                "name": "IncreaseEmployeeCompensation",
                "arguments": {
                    "employee_id": "E10003",
                    "compensation_id": "COMP10000",
                    "effective_date": "2026-05-25",
                    "equity_increase_amount": 20000
                },
            },
            {
                "name": "GetUnusedReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "Equity refresh and tier promotion."
                    }
                },
            },
            {
                "name": "GetUnusedDocumentId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddEmployeeDocument",
                "arguments": {
                    "document": {
                        "doc_id": "DOC10000",
                        "employee_id": "E10003",
                        "title": "Equity Grant Agreement",
                        "date": "2026-05-25"
                    }
                },
            },
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10003",
                    "updates": {
                        "role_description": "Principal Engineer",
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
                "name": "GetUnusedBonusId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddBonusPayment",
                "arguments": {
                    "bonus": {
                        "bonus_id": "BON10000",
                        "employee_id": "E10001",
                        "amount": 1000,
                        "reason": "Mentorship excellence."
                    }
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10001"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10003\",\n                    \"role_description\": \"Principal Engineer\",\n                    \"compensation_id\": \"COMP10000\",\n                    \"performance_review_ids\": [\"PR5003\", \"PR5010\", \"PR10000\"]\n                },\n                {\n                    \"employee_id\": \"E10001\"\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_03",
        "instruction": "Handle and authorize a 12-week parental leave for Isabella Chen (E10001) from 2025-08-01 to 2025-10-23. Allocate Emma Rodriguez (E10003) as acting CTO for this period, granting a temporary 5% salary increase. Record a performance assessment for Amelia with the summary 'Acting CTO during S. Nguyen's leave.' To finance these modifications, relocate $50,000 from the Sales department's budget (DEPT1002) to the Engineering department's (DEPT1001). For validation, obtain the updated records for both employees and the Engineering department.",
        "actions": [
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10001"
                },
            },
            {
                "name": "GetUnusedLeaveId",
                "arguments": {
                {}
                },
            },
            {
                "name": "RequestLeave",
                "arguments": {
                    "leave": {
                        "leave_id": "LV10000",
                        "employee_id": "E10001",
                        "leave_type": "Parental Leave",
                        "start_date": "2025-08-01",
                        "end_date": "2025-10-23",
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
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "GetCompensation",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10003",
                    "updates": {
                        "role_description": "Acting CTO"
                    }
                },
            },
            {
                "name": "GetUnusedCompensationId",
                "arguments": {
                {}
                },
            },
            {
                "name": "IncreaseEmployeeCompensation",
                "arguments": {
                    "employee_id": "E10003",
                    "compensation_id": "COMP10000",
                    "salary_increase_pct": 5,
                    "effective_date": "2025-08-01"
                },
            },
            {
                "name": "GetUnusedReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "Acting CTO during S. Nguyen's leave."
                    }
                },
            },
            {
                "name": "UpdateEmployee",
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
                "name": "GetDepartment",
                "arguments": {
                    "department_id": "DEPT1002"
                },
            },
            {
                "name": "GetDepartment",
                "arguments": {
                    "department_id": "DEPT1001"
                },
            },
            {
                "name": "UpdateDepartment",
                "arguments": {
                    "department_id": "DEPT1002",
                    "updates": {
                        "budget": 4950000
                    }
                },
            },
            {
                "name": "UpdateDepartment",
                "arguments": {
                    "department_id": "DEPT1001",
                    "updates": {
                        "budget": 7050000
                    }
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10001"
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "GetDepartment",
                "arguments": {
                    "department_id": "DEPT1001"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10001\"\n                },\n                {\n                    \"employee_id\": \"E10003\",\n                    \"role_description\": \"Acting CTO\",\n                    \"compensation_id\": \"COMP10000\",\n                    \"performance_review_ids\": [\"PR5003\", \"PR5010\", \"PR10000\"]\n                },\n                {\n                    \"department_id\": \"DEPT1001\",\n                    \"name\": \"Engineering\",\n                    \"budget\": 7050000\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_04",
        "instruction": "Coordinate the termination of Olivia Martinez (E10005), effective 2025-07-01. Adhere to all off-boarding protocols, including resolving her benefits, adjusting her final compensation to zero, and documenting a performance review with the summary 'Termination.' To fill her position, reassign William Liu (E10006) to her former role (POS3010) and modify his role description to 'Senior Financial Analyst.' For validation, acquire both updated employee records.",
        "actions": [
            {
                "name": "GetEmployee",
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
                "name": "GetUnusedCompensationId",
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
                        "base_salary": 0,
                        "bonus_target_pct": 0,
                        "equity_grant": 0,
                        "effective_date": "2025-07-01"
                    }
                },
            },
            {
                "name": "GetUnusedReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10005",
                        "summary": "Termination"
                    }
                },
            },
            {
                "name": "UpdateEmployee",
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
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10006"
                },
            },
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10006",
                    "updates": {
                        "position_id": "POS3010",
                        "role_description": "Senior Financial Analyst"
                    }
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10005"
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10006"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10005\",\n                    \"status\": \"Terminated\",\n                    \"compensation_id\": \"COMP10000\",\n                    \"performance_review_ids\": [\"PR10000\"]\n                },\n                {\n                    \"employee_id\": \"E10006\",\n                    \"position_id\": \"POS3010\",\n                    \"role_description\": \"Senior Financial Analyst\"\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_05",
        "instruction": "Starting from 2025-09-01, handle the promotion of Emma Rodriguez (E10003) to the position of Staff Engineer (POS3005) at level L.4, which involves a 10% increase IND her base salary. Record a performance review with the note 'Promotion to Staff Engineer.' To fill her previous role, transfer Michael Park (E10002) to her former position (POS3006). For confirmation, obtain the updated records for both employees.",
        "actions": [
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "GetCompensation",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10003",
                    "updates": {
                        "position_id": "POS3005",
                        "level_id": "L.4",
                        "role_description": "Staff Engineer"
                    }
                },
            },
            {
                "name": "GetUnusedCompensationId",
                "arguments": {
                {}
                },
            },
            {
                "name": "IncreaseEmployeeCompensation",
                "arguments": {
                    "employee_id": "E10003",
                    "compensation_id": "COMP10000",
                    "salary_increase_pct": 10,
                    "effective_date": "2025-09-01"
                },
            },
            {
                "name": "GetUnusedReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "Promotion to Staff Engineer"
                    }
                },
            },
            {
                "name": "UpdateEmployee",
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
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10002",
                    "updates": {
                        "position_id": "POS3006"
                    }
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10002"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10003\",\n                    \"position_id\": \"POS3005\",\n                    \"level_id\": \"L.4\",\n                    \"role_description\": \"Staff Engineer\",\n                    \"compensation_id\": \"COMP10000\",\n                    \"performance_review_ids\": [\"PR5003\", \"PR5010\", \"PR10000\"]\n                },\n                {\n                    \"employee_id\": \"E10002\",\n                    \"position_id\": \"POS3006\"\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_06",
        "instruction": "Commencing on 2025-08-01, adjust the monthly employee cost for the Medical-PPO plan (BEN4001) to $170. Simultaneously, coordinate the promotion of Isabella Chen (E10001) to 'Lead Engineer' (POS3002) at level L.A, which includes a 10% salary hike. Enroll Adrian Thompson (E99999) IND the revised Medical-PPO plan. Document a performance review for Sophia with the summary 'Promotion to Lead Engineer.' To support the promotion, allocate $50,000 from the HR department's budget (DEPT1003) to the Engineering department's (DEPT1001). For validation, retrieve the updated employee records for both Andrian and Sophia, as well as the updated record for the Engineering department.",
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
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E99999"
                },
            },
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E99999",
                    "updates": {
                        "benefit_plan_ids": [
                            "BEN9999",
                            "BEN4001"
                        ]
                    }
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10001"
                },
            },
            {
                "name": "GetCompensation",
                "arguments": {
                    "employee_id": "E10001"
                },
            },
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10001",
                    "updates": {
                        "position_id": "POS3002",
                        "level_id": "L.A"
                    }
                },
            },
            {
                "name": "GetUnusedCompensationId",
                "arguments": {
                {}
                },
            },
            {
                "name": "IncreaseEmployeeCompensation",
                "arguments": {
                    "employee_id": "E10001",
                    "compensation_id": "COMP10000",
                    "salary_increase_pct": 10,
                    "effective_date": "2025-08-01"
                },
            },
            {
                "name": "GetUnusedReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10001",
                        "summary": "Promotion to Lead Engineer"
                    }
                },
            },
            {
                "name": "UpdateEmployee",
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
                "name": "GetDepartment",
                "arguments": {
                    "department_id": "DEPT1003"
                },
            },
            {
                "name": "GetDepartment",
                "arguments": {
                    "department_id": "DEPT1001"
                },
            },
            {
                "name": "UpdateDepartment",
                "arguments": {
                    "department_id": "DEPT1003",
                    "updates": {
                        "budget": 750000
                    }
                },
            },
            {
                "name": "UpdateDepartment",
                "arguments": {
                    "department_id": "DEPT1001",
                    "updates": {
                        "budget": 7050000
                    }
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E99999"
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10001"
                },
            },
            {
                "name": "GetDepartment",
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
        "instruction": "Starting on 2025-06-24, integrate a new HR Business Partner, Sarah Johnson, into the HR department (DEPT1003). Her salary will be $110,000, and she must be enrolled in the benefits (BEN4001, BEN4002). Her supervisor will be Emma Rodriguez (E10003). Record a performance evaluation for Mary with the summary 'New hire onboarding.' To finance the new position, allocate $120,000 from the Sales department's budget (DEPT1002) to HR. For validation, obtain the revised records for Sarah Johnson and the HR department.",
        "actions": [
            {
                "name": "GetUnusedEmployeeId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateEmployee",
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
                "name": "GetUnusedCompensationId",
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
                "name": "GetUnusedReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10000",
                        "summary": "New hire onboarding"
                    }
                },
            },
            {
                "name": "UpdateEmployee",
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
                "name": "GetDepartment",
                "arguments": {
                    "department_id": "DEPT1002"
                },
            },
            {
                "name": "GetDepartment",
                "arguments": {
                    "department_id": "DEPT1003"
                },
            },
            {
                "name": "UpdateDepartment",
                "arguments": {
                    "department_id": "DEPT1002",
                    "updates": {
                        "budget": 4880000
                    }
                },
            },
            {
                "name": "UpdateDepartment",
                "arguments": {
                    "department_id": "DEPT1003",
                    "updates": {
                        "budget": 920000
                    }
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10000"
                },
            },
            {
                "name": "GetDepartment",
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
        "instruction": "As of 2025-10-15, coordinate an internal relocation and promotion for Emma Rodriguez (E10003) to 'Senior Software Engineer' (POS3009) at level L.3 IND the Engineering department (DEPT1001), with a salary increase of 10%. To replace her previous position, move Arjun Patel (E10004) to her former role (POS3006). Document a performance review for Amelia with the summary 'Promotion and transfer to Engineering.' For confirmation, access the updated employee record for Amelia.",
        "actions": [
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "GetCompensation",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10003",
                    "updates": {
                        "department_id": "DEPT1001",
                        "position_id": "POS3009",
                        "level_id": "L.3",
                        "role_description": "Senior Software Engineer"
                    }
                },
            },
            {
                "name": "GetUnusedCompensationId",
                "arguments": {
                {}
                },
            },
            {
                "name": "IncreaseEmployeeCompensation",
                "arguments": {
                    "employee_id": "E10003",
                    "compensation_id": "COMP10000",
                    "salary_increase_pct": 10,
                    "effective_date": "2025-10-15"
                },
            },
            {
                "name": "GetUnusedReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "Promotion and transfer to Engineering"
                    }
                },
            },
            {
                "name": "UpdateEmployee",
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
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10004",
                    "updates": {
                        "position_id": "POS3006"
                    }
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10003"
                }
            }
        ],
        "outputs": [
                "\n            {\n                \"employee_id\": \"E10003\",\n                \"department_id\": \"DEPT1001\",\n                \"position_id\": \"POS3009\",\n                \"level_id\": \"L.3\",\n                \"compensation_id\": \"COMP10000\",\n                \"performance_review_ids\": [\"PR5003\", \"PR5010\", \"PR10000\"]\n            }\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_09",
        "instruction": "Establish a new 'Vision Plan' (BEN4006) utilizing provider 'VSP' with a monthly fee of $15. Enroll all currently active employees IND the Marketing department (DEPT1005). Transfer Michael Park (E10002) to the Marketing department as part of this and enroll him as well. Record a performance review for Emma Rodriguez (E10003), including the summary 'Benefit rollout and new team member.' For verification purposes, obtain the updated records for Amelia, Daniel, and the Marketing department.",
        "actions": [
            {
                "name": "AddBenefitPlan",
                "arguments": {
                    "benefit_plan": {
                        "benefit_plan_id": "BEN4006",
                        "name": "Vision Plan",
                        "provider": "VSP",
                        "employee_cost_monthly": 15
                    }
                },
            },
            {
                "name": "SearchEmployees",
                "arguments": {
                    "filters": {
                        "department_id": "DEPT1005",
                        "status": "Active"
                    }
                },
            },
            {
                "name": "GetEmployee",
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
                        "BEN4006"
                    ]
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10002"
                },
            },
            {
                "name": "UpdateEmployee",
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
                        "BEN4006"
                    ]
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "GetUnusedReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "Benefit rollout and new team member."
                    }
                },
            },
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10003",
                    "updates": {
                        "performance_review_ids": [
                            "PR5003",
                            "PR5010",
                            "PR10000"
                        ]
                    }
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10002"
                },
            },
            {
                "name": "GetDepartment",
                "arguments": {
                    "department_id": "DEPT1005"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10003\",\n                    \"benefit_plan_ids\": [\"BEN4001\", \"BEN4003\", \"BEN4004\", \"BEN4006\"],\n                    \"performance_review_ids\": [\"PR5003\", \"PR5010\", \"PR10000\"]\n                },\n                {\n                    \"employee_id\": \"E10002\",\n                    \"department_id\": \"DEPT1005\",\n                    \"benefit_plan_ids\": [\"BEN4001\", \"BEN4002\", \"BEN4006\"]\n                },\n                {\n                    \"department_id\": \"DEPT1005\",\n                    \"name\": \"Marketing\"\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_10",
        "instruction": "Approve and handle a one-month unpaid sabbatical for Emma Rodriguez (E10003) from 2025-11-01 to 2025-11-30. Designate Arjun Patel (E10004) as acting team lead and grant him a one-time bonus of $2,500 for 'Acting team lead coverage.' Record a performance review for Amelia with the note 'Unpaid sabbatical approved.' To cover the bonus, raise the Engineering department's (DEPT1001) budget by $2,500. For verification, procure the updated employee records for both Amelia and Rahul, along with the modified Engineering department record.",
        "actions": [
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "GetUnusedLeaveId",
                "arguments": {
                {}
                },
            },
            {
                "name": "RequestLeave",
                "arguments": {
                    "leave": {
                        "leave_id": "LV10000",
                        "employee_id": "E10003",
                        "leave_type": "Sabbatical",
                        "start_date": "2025-11-01",
                        "end_date": "2025-11-30",
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
                "name": "GetUnusedReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "Unpaid sabbatical approved"
                    }
                },
            },
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10003",
                    "updates": {
                        "performance_review_ids": [
                            "PR5003",
                            "PR5010",
                            "PR10000"
                        ]
                    }
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10004"
                },
            },
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10004",
                    "updates": {
                        "role_description": "Acting Team Lead"
                    }
                },
            },
            {
                "name": "GetUnusedBonusId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddBonusPayment",
                "arguments": {
                    "bonus": {
                        "bonus_id": "BON10000",
                        "employee_id": "E10004",
                        "amount": 2500,
                        "reason": "Acting team lead coverage."
                    }
                },
            },
            {
                "name": "GetDepartment",
                "arguments": {
                    "department_id": "DEPT1001"
                },
            },
            {
                "name": "UpdateDepartment",
                "arguments": {
                    "department_id": "DEPT1001",
                    "updates": {
                        "budget": 7002500
                    }
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10004"
                },
            },
            {
                "name": "GetDepartment",
                "arguments": {
                    "department_id": "DEPT1001"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10003\",\n                    \"performance_review_ids\": [\"PR5003\", \"PR5010\", \"PR10000\"]\n                },\n                {\n                    \"employee_id\": \"E10004\",\n                    \"role_description\": \"Acting Team Lead\"\n                },\n                {\n                    \"department_id\": \"DEPT1001\",\n                    \"name\": \"Engineering\",\n                    \"budget\": 7002500\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_11",
        "instruction": "Handle a 30-day Performance Improvement Plan (PIP) initiation for Michael Park (E10002), starting on 2025-11-01, with the summary '30-day Performance Improvement Plan initiated.' and a 'Needs Improvement' rating. As part of the PIP, reassign him to the Marketing department (DEPT1005), upload his signed 'PIP Agreement' document, and generate a new compensation record to adjust his bonus target to 0%. To facilitate this, allocate $10,000 from the Sales department's budget (DEPT1002) to Marketing. For verification purposes, obtain the updated records for Michael Park and the Marketing department.",
        "actions": [
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10002"
                },
            },
            {
                "name": "GetCompensation",
                "arguments": {
                    "employee_id": "E10002"
                },
            },
            {
                "name": "GetUnusedReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10002",
                        "period_start": "2025-11-01",
                        "period_end": "2025-11-30",
                        "rating": "Needs Improvement",
                        "summary": "30-day Performance Improvement Plan initiated."
                    }
                },
            },
            {
                "name": "GetUnusedDocumentId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddEmployeeDocument",
                "arguments": {
                    "document": {
                        "doc_id": "DOC10000",
                        "employee_id": "E10002",
                        "title": "PIP Agreement",
                        "date": "2025-11-01"
                    }
                },
            },
            {
                "name": "GetUnusedCompensationId",
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
                        "bonus_target_pct": 0,
                        "base_salary": 210000,
                        "equity_grant": 40000,
                        "currency": "USD",
                        "effective_date": "2025-11-01"
                    }
                },
            },
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10002",
                    "updates": {
                        "department_id": "DEPT1005",
                        "compensation_id": "COMP10000",
                        "performance_review_ids": [
                            "PR5002",
                            "PR10000"
                        ]
                    }
                },
            },
            {
                "name": "GetDepartment",
                "arguments": {
                    "department_id": "DEPT1002"
                },
            },
            {
                "name": "GetDepartment",
                "arguments": {
                    "department_id": "DEPT1005"
                },
            },
            {
                "name": "UpdateDepartment",
                "arguments": {
                    "department_id": "DEPT1002",
                    "updates": {
                        "budget": 4990000
                    }
                },
            },
            {
                "name": "UpdateDepartment",
                "arguments": {
                    "department_id": "DEPT1005",
                    "updates": {
                        "budget": 1610000
                    }
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10002"
                },
            },
            {
                "name": "GetDepartment",
                "arguments": {
                    "department_id": "DEPT1005"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10002\",\n                    \"department_id\": \"DEPT1005\",\n                    \"compensation_id\": \"COMP10000\",\n                    \"performance_review_ids\": [\"PR5002\", \"PR10000\"]\n                },\n                {\n                    \"department_id\": \"DEPT1005\",\n                    \"name\": \"Marketing\",\n                    \"budget\": 1610000\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_12",
        "instruction": "Authorize the request for Isabella Chen (E10001) to commence remote work from 'Remote \u2013 Seattle', effective 2025-07-24. Update her work location and upload her signed 'Remote Work Agreement', following which confirm the upload. As part of this team restructuring, adjust Michael Park's (E10002) reporting line to have him report directly to Sophia. Record a performance review for Sophia with the summary 'Remote work transition.' For verification, obtain the updated employee records for both.",
        "actions": [
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10001"
                },
            },
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10001",
                    "updates": {
                        "work_location": "Remote – Seattle"
                    }
                },
            },
            {
                "name": "GetUnusedDocumentId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddEmployeeDocument",
                "arguments": {
                    "document": {
                        "doc_id": "DOC10000",
                        "employee_id": "E10001",
                        "title": "Remote Work Agreement",
                        "date": "2025-07-24"
                    }
                },
            },
            {
                "name": "ListEmployeeDocuments",
                "arguments": {
                    "employee_id": "E10001"
                },
            },
            {
                "name": "GetUnusedReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10001",
                        "summary": "Remote work transition"
                    }
                },
            },
            {
                "name": "UpdateEmployee",
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
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10002",
                    "updates": {
                        "manager_id": "E10001"
                    }
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10001"
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10002"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10001\",\n                    \"work_location\": \"Remote – Seattle\",\n                    \"performance_review_ids\": [\"PR5001\", \"PR10000\"]\n                },\n                {\n                    \"employee_id\": \"E10002\",\n                    \"manager_id\": \"E10001\"\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_13",
        "instruction": "Handle the extension of Isabella Chen's (E10001) parental leave (LV7001) to 2026-02-15 and modify her status to 'On Leave'. Designate Emma Rodriguez (E10003) to act as interim CTO, which includes granting a temporary 5% salary increase starting on the leave commencement date. Log a performance evaluation for Amelia with the summary 'Acting CTO coverage.' For confirmation, access the updated employee record for Amelia.",
        "actions": [
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10001"
                },
            },
            {
                "name": "ListEmployeeLeaves",
                "arguments": {
                    "employee_id": "E10001"
                },
            },
            {
                "name": "UpdateLeaveRecord",
                "arguments": {
                    "leave_id": "LV7001",
                    "updates": {
                        "end_date": "2026-02-15"
                    }
                },
            },
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10001",
                    "updates": {
                        "status": "On Leave"
                    }
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "GetCompensation",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10003",
                    "updates": {
                        "role_description": "Acting CTO"
                    }
                },
            },
            {
                "name": "GetUnusedCompensationId",
                "arguments": {
                {}
                },
            },
            {
                "name": "IncreaseEmployeeCompensation",
                "arguments": {
                    "employee_id": "E10003",
                    "compensation_id": "COMP10000",
                    "salary_increase_pct": 5,
                    "effective_date": "2025-07-01"
                },
            },
            {
                "name": "GetUnusedReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "Acting CTO coverage."
                    }
                },
            },
            {
                "name": "UpdateEmployee",
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
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10003"
                }
            }
        ],
        "outputs": [
                "\n            {\n                \"employee_id\": \"E10003\",\n                \"role_description\": \"Acting CTO\",\n                \"compensation_id\": \"COMP10000\",\n                \"performance_review_ids\": [\"PR5003\", \"PR5010\", \"PR10000\"]\n            }\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_14",
        "instruction": "Coordinate the promotion of Michael Park (E10002) to Senior Analyst (POS3012) at level L.2, effective 2025-12-01, with a 7% increase IND base salary. Record a new performance review with an 'Exceeds' rating and the summary 'Promoted to Senior Analyst (L.2).' To acknowledge his manager, William Liu (E10006), for this successful promotion, allocate him a one-time bonus of \u20ac1,000 for 'Team development.' For confirmation, access both updated employee records.",
        "actions": [
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10002"
                },
            },
            {
                "name": "GetCompensation",
                "arguments": {
                    "employee_id": "E10002"
                },
            },
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10002",
                    "updates": {
                        "level_id": "L.2",
                        "position_id": "POS3012",
                        "role_description": "Senior Analyst"
                    }
                },
            },
            {
                "name": "GetUnusedCompensationId",
                "arguments": {
                {}
                },
            },
            {
                "name": "IncreaseEmployeeCompensation",
                "arguments": {
                    "employee_id": "E10002",
                    "compensation_id": "COMP10000",
                    "salary_increase_pct": 7,
                    "effective_date": "2025-12-01"
                },
            },
            {
                "name": "GetUnusedReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10002",
                        "rating": "Exceeds",
                        "summary": "Promoted to Senior Analyst (L.2)."
                    }
                },
            },
            {
                "name": "UpdateEmployee",
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
                "name": "GetUnusedBonusId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddBonusPayment",
                "arguments": {
                    "bonus": {
                        "bonus_id": "BON10000",
                        "employee_id": "E10006",
                        "amount": 1000,
                        "currency": "EUR",
                        "reason": "Team development"
                    }
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10002"
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10006"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10002\",\n                    \"position_id\": \"POS3012\",\n                    \"level_id\": \"L.2\",\n                    \"compensation_id\": \"COMP10000\",\n                    \"performance_review_ids\": [\"PR5002\", \"PR10000\"]\n                },\n                {\n                    \"employee_id\": \"E10006\"\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_15",
        "instruction": "Starting 2025-12-01, handle the removal of the 'Vision Plan' (BEN4006) from Isabella Chen's (E10001) benefits and ensure a 'Benefit Change Form' is uploaded to her file. To acknowledge her manager, Emma Rodriguez (E10003), for overseeing this transition, coordinate a one-time bonus of $500 for 'Administrative excellence.' Record a performance review for Sophia with the summary 'Benefit change processed.' Adjust the Engineering department's (DEPT1001) budget by $500 to accommodate the bonus. For verification purposes, obtain both the updated employee records and the Engineering department's revised record.",
        "actions": [
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10001"
                },
            },
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10001",
                    "updates": {
                        "benefit_plan_ids": [
                            "BEN4001",
                            "BEN4002",
                            "BEN4003"
                        ]
                    }
                },
            },
            {
                "name": "GetUnusedDocumentId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddEmployeeDocument",
                "arguments": {
                    "document": {
                        "doc_id": "DOC10000",
                        "employee_id": "E10001",
                        "title": "Benefit Change Form",
                        "date": "2025-12-01"
                    }
                },
            },
            {
                "name": "GetUnusedReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10001",
                        "summary": "Benefit change processed"
                    }
                },
            },
            {
                "name": "UpdateEmployee",
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
                "name": "GetUnusedBonusId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddBonusPayment",
                "arguments": {
                    "bonus": {
                        "bonus_id": "BON10000",
                        "employee_id": "E10003",
                        "amount": 500,
                        "reason": "Administrative excellence."
                    }
                },
            },
            {
                "name": "GetDepartment",
                "arguments": {
                    "department_id": "DEPT1001"
                },
            },
            {
                "name": "UpdateDepartment",
                "arguments": {
                    "department_id": "DEPT1001",
                    "updates": {
                        "budget": 7000500
                    }
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10001"
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "GetDepartment",
                "arguments": {
                    "department_id": "DEPT1001"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10001\",\n                    \"benefit_plan_ids\": [\"BEN4001\", \"BEN4002\", \"BEN4003\"],\n                    \"performance_review_ids\": [\"PR5001\", \"PR10000\"]\n                },\n                {\n                    \"employee_id\": \"E10003\"\n                },\n                {\n                    \"department_id\": \"DEPT1001\",\n                    \"name\": \"Engineering\",\n                    \"budget\": 7000500\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_16",
        "instruction": "Coordinate and sanction a 5-day bereavement leave for Michael Park (E10002) from 2025-12-10 to 2025-12-14. Assign Arjun Patel (E10004) as the acting manager during Daniel's absence, which involves a temporary 5% salary increment. Register a performance review for Rahul with the summary 'Acting manager coverage.' For verification, acquire the updated employee records for both Daniel and Rahul.",
        "actions": [
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10002"
                },
            },
            {
                "name": "GetUnusedLeaveId",
                "arguments": {
                {}
                },
            },
            {
                "name": "RequestLeave",
                "arguments": {
                    "leave": {
                        "leave_id": "LV10000",
                        "employee_id": "E10002",
                        "leave_type": "Bereavement Leave",
                        "start_date": "2025-12-10",
                        "end_date": "2025-12-14",
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
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10002",
                    "updates": {
                        "manager_id": "E10004"
                    }
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10004"
                },
            },
            {
                "name": "GetCompensation",
                "arguments": {
                    "employee_id": "E10004"
                },
            },
            {
                "name": "GetUnusedCompensationId",
                "arguments": {
                {}
                },
            },
            {
                "name": "IncreaseEmployeeCompensation",
                "arguments": {
                    "employee_id": "E10004",
                    "compensation_id": "COMP10000",
                    "salary_increase_pct": 5,
                    "effective_date": "2025-12-10"
                },
            },
            {
                "name": "GetUnusedReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10004",
                        "summary": "Acting manager coverage"
                    }
                },
            },
            {
                "name": "UpdateEmployee",
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
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10002"
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10004"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10002\",\n                    \"manager_id\": \"E10004\"\n                },\n                {\n                    \"employee_id\": \"E10004\",\n                    \"compensation_id\": \"COMP10000\",\n                    \"performance_review_ids\": [\"PR5004\", \"PR5009\", \"PR10000\"]\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_17",
        "instruction": "Starting on 2026-01-01, handle a 3% cost-of-living salary increment for Emma Rodriguez (E10003) and record a performance review with the summary 'COLA applied.' Additionally, within the same audit, allocate a one-time bonus of $2,000 to Michael Park (E10002) for 'cross-functional collaboration.' Allocate $15,000 from the HR department's budget (DEPT1003) to the Sales department's (DEPT1002) to facilitate these adjustments. To ensure accuracy, gather the updated employee records for both and the revised Sales department record.",
        "actions": [
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "GetCompensation",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "GetUnusedCompensationId",
                "arguments": {
                {}
                },
            },
            {
                "name": "IncreaseEmployeeCompensation",
                "arguments": {
                    "employee_id": "E10003",
                    "compensation_id": "COMP10000",
                    "salary_increase_pct": 3,
                    "effective_date": "2026-01-01"
                },
            },
            {
                "name": "GetUnusedReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "COLA applied."
                    }
                },
            },
            {
                "name": "UpdateEmployee",
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
                "name": "GetUnusedBonusId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddBonusPayment",
                "arguments": {
                    "bonus": {
                        "bonus_id": "BON10000",
                        "employee_id": "E10002",
                        "amount": 2000,
                        "reason": "cross-functional collaboration"
                    }
                },
            },
            {
                "name": "GetDepartment",
                "arguments": {
                    "department_id": "DEPT1003"
                },
            },
            {
                "name": "GetDepartment",
                "arguments": {
                    "department_id": "DEPT1002"
                },
            },
            {
                "name": "UpdateDepartment",
                "arguments": {
                    "department_id": "DEPT1003",
                    "updates": {
                        "budget": 785000
                    }
                },
            },
            {
                "name": "UpdateDepartment",
                "arguments": {
                    "department_id": "DEPT1002",
                    "updates": {
                        "budget": 5015000
                    }
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10002"
                },
            },
            {
                "name": "GetDepartment",
                "arguments": {
                    "department_id": "DEPT1002"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10003\",\n                    \"compensation_id\": \"COMP10000\",\n                    \"performance_review_ids\": [\"PR5003\", \"PR5010\", \"PR10000\"]\n                },\n                {\n                    \"employee_id\": \"E10002\"\n                },\n                {\n                    \"department_id\": \"DEPT1002\",\n                    \"name\": \"Sales\",\n                    \"budget\": 5015000\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_18",
        "instruction": "Authorize Michael Park's (E10002) request to work remotely from 'Remote \u2013 Dallas', effective starting 2025-07-24. Update his work location information and upload his signed 'Remote Work Agreement'. As a component of the remote work package, coordinate a 5% salary increment for him. Record a performance review noting 'Remote work and compensation updated.' For accuracy verification, obtain his updated employee record.",
        "actions": [
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10002"
                },
            },
            {
                "name": "GetCompensation",
                "arguments": {
                    "employee_id": "E10002"
                },
            },
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10002",
                    "updates": {
                        "work_location": "Remote – Dallas"
                    }
                },
            },
            {
                "name": "GetUnusedDocumentId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddEmployeeDocument",
                "arguments": {
                    "document": {
                        "doc_id": "DOC10000",
                        "employee_id": "E10002",
                        "title": "Remote Work Agreement",
                        "date": "2025-07-24"
                    }
                },
            },
            {
                "name": "GetUnusedCompensationId",
                "arguments": {
                {}
                },
            },
            {
                "name": "IncreaseEmployeeCompensation",
                "arguments": {
                    "employee_id": "E10002",
                    "compensation_id": "COMP10000",
                    "salary_increase_pct": 5,
                    "effective_date": "2025-07-24"
                },
            },
            {
                "name": "GetUnusedReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10002",
                        "summary": "Remote work and compensation updated."
                    }
                },
            },
            {
                "name": "UpdateEmployee",
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
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10002"
                }
            }
        ],
        "outputs": [
                "\n            {\n                \"employee_id\": \"E10002\",\n                \"work_location\": \"Remote – Dallas\",\n                \"compensation_id\": \"COMP10000\",\n                \"performance_review_ids\": [\"PR5002\", \"PR10000\"]\n            }\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_19",
        "instruction": "Register Emma Rodriguez (E10003) and Michael Park (E10002) IND the 'Legal Insurance' plan (BEN9999), commencing on 2025-07-24. Record a performance review once for their supervisor, Isabella Chen (E10001), with the commentary 'Benefit enrollment processed for team.' For verification, access the updated employee records for all three.",
        "actions": [
            {
                "name": "GetEmployee",
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
                "name": "GetEmployee",
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
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10001"
                },
            },
            {
                "name": "GetUnusedReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10001",
                        "summary": "Benefit enrollment processed for team."
                    }
                },
            },
            {
                "name": "UpdateEmployee",
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
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10002"
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10001"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10003\",\n                    \"benefit_plan_ids\": [\"BEN4001\", \"BEN4003\", \"BEN4004\", \"BEN9999\"]\n                },\n                {\n                    \"employee_id\": \"E10002\",\n                    \"benefit_plan_ids\": [\"BEN4001\", \"BEN4002\", \"BEN9999\"]\n                },\n                {\n                    \"employee_id\": \"E10001\",\n                    \"performance_review_ids\": [\"PR5001\", \"PR10000\"]\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_20",
        "instruction": "Starting 2026-01-01, handle a compensation adjustment for Isabella Chen (E10001), creating a new entry to set her bonus target at 25%. Record a performance review with the summary 'Bonus target adjusted.' To acknowledge her superior, grant a one-time bonus of $5,000 to Emma Rodriguez (E10003) for 'Leadership excellence.' For verification, access the updated employee records for both.",
        "actions": [
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10001"
                },
            },
            {
                "name": "GetCompensation",
                "arguments": {
                    "employee_id": "E10001"
                },
            },
            {
                "name": "GetUnusedCompensationId",
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
                        "bonus_target_pct": 25,
                        "base_salary": 325000,
                        "equity_grant": 75000,
                        "currency": "USD",
                        "effective_date": "2026-01-01"
                    }
                },
            },
            {
                "name": "GetUnusedReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10001",
                        "summary": "Bonus target adjusted"
                    }
                },
            },
            {
                "name": "UpdateEmployee",
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
                "name": "GetUnusedBonusId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddBonusPayment",
                "arguments": {
                    "bonus": {
                        "bonus_id": "BON10000",
                        "employee_id": "E10003",
                        "amount": 5000,
                        "reason": "Leadership excellence."
                    }
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10001"
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10003"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10001\",\n                    \"compensation_id\": \"COMP10000\",\n                    \"performance_review_ids\": [\"PR5001\", \"\"PR10000\"]\n                },\n                {\n                    \"employee_id\": \"E10003\"\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_21",
        "instruction": "Handle the early return of Sophia Nguyen (E10001) from parental leave (LV7001) on 2025-08-31 by updating her leave record to 'Taken' and changing her status to 'Active'. For successful team management during her leave, coordinate a 5% salary raise for her manager, Amelia Garcia (E10003), and log a performance review with the summary 'Team management bonus.' For confirmation, access Amelia's updated employee record.",
        "actions": [
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10001"
                },
            },
            {
                "name": "UpdateLeaveRecord",
                "arguments": {
                    "leave_id": "LV7001",
                    "updates": {
                        "end_date": "2025-08-31",
                        "status": "Taken"
                    }
                },
            },
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10001",
                    "updates": {
                        "status": "Active"
                    }
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "GetCompensation",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "GetUnusedCompensationId",
                "arguments": {
                {}
                },
            },
            {
                "name": "IncreaseEmployeeCompensation",
                "arguments": {
                    "employee_id": "E10003",
                    "compensation_id": "COMP10000",
                    "salary_increase_pct": 5,
                    "effective_date": "2025-08-31"
                },
            },
            {
                "name": "GetUnusedReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "Team management bonus."
                    }
                },
            },
            {
                "name": "UpdateEmployee",
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
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10003"
                }
            }
        ],
        "outputs": [
                "\n            {\n                \"employee_id\": \"E10003\",\n                \"compensation_id\": \"COMP10000\",\n                \"performance_review_ids\": [\"PR5003\", \"PR5010\", \"PR10000\"]\n            }\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_22",
        "instruction": "Carry out an equity refresh grant for Michael Park (E10002) to take effect on 2026-01-15. Increase his equity grant by $10,000. To document this, log a performance review note with the summary 'Equity refresh of $10,000 granted.' For verification, retrieve his most recent updated compensation record.",
        "actions": [
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10002"
                },
            },
            {
                "name": "GetCompensation",
                "arguments": {
                    "employee_id": "E10002"
                },
            },
            {
                "name": "GetUnusedCompensationId",
                "arguments": {
                {}
                },
            },
            {
                "name": "IncreaseEmployeeCompensation",
                "arguments": {
                    "employee_id": "E10002",
                    "compensation_id": "COMP10000",
                    "effective_date": "2026-01-15",
                    "equity_increase_amount": 10000
                },
            },
            {
                "name": "GetUnusedReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10002",
                        "summary": "Equity refresh of $10,000 granted."
                    }
                },
            },
            {
                "name": "UpdateEmployee",
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
                "name": "GetCompensation",
                "arguments": {
                    "employee_id": "E10002"
                }
            }
        ],
        "outputs": [
                "\n            {\n                \"compensation_id\": \"COMP10000\",\n                \"employee_id\": \"E10002\",\n                \"base_salary\": 210000,\n                \"currency\": \"USD\",\n                \"bonus_target_pct\": 25,\n                \"equity_grant\": 50000,\n                \"effective_date\": \"2026-01-15\"\n            }\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_23",
        "instruction": "Starting on 2026-01-01, handle the processing and approval of a 6-month sabbatical for Emma Rodriguez (E10003). IND accordance with policy, generate a new compensation record to adjust her bonus target to 0% during this period. Assign Michael Park (E10002) as acting manager by modifying his role description. Record a performance review for Amelia with the note 'Sabbatical leave.' To finance this temporary arrangement, allocate $15,000 from the Sales department's budget (DEPT1002) to the Engineering department's account (DEPT1001). Confirm by retrieving both refined employee records and the updated Engineering department record.",
        "actions": [
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "GetCompensation",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "GetUnusedLeaveId",
                "arguments": {
                {}
                },
            },
            {
                "name": "RequestLeave",
                "arguments": {
                    "leave": {
                        "leave_id": "LV10000",
                        "employee_id": "E10003",
                        "leave_type": "Sabbatical",
                        "start_date": "2026-01-01",
                        "end_date": "2026-06-30",
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
                "name": "GetUnusedCompensationId",
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
                        "bonus_target_pct": 0,
                        "base_salary": 145000,
                        "equity_grant": 15000,
                        "currency": "USD",
                        "effective_date": "2026-01-01"
                    }
                },
            },
            {
                "name": "GetUnusedReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "Sabbatical leave"
                    }
                },
            },
            {
                "name": "UpdateEmployee",
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
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10002",
                    "updates": {
                        "role_description": "Acting Manager"
                    }
                },
            },
            {
                "name": "GetDepartment",
                "arguments": {
                    "department_id": "DEPT1002"
                },
            },
            {
                "name": "GetDepartment",
                "arguments": {
                    "department_id": "DEPT1001"
                },
            },
            {
                "name": "UpdateDepartment",
                "arguments": {
                    "department_id": "DEPT1002",
                    "updates": {
                        "budget": 4985000
                    }
                },
            },
            {
                "name": "UpdateDepartment",
                "arguments": {
                    "department_id": "DEPT1001",
                    "updates": {
                        "budget": 7015000
                    }
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10002"
                },
            },
            {
                "name": "GetDepartment",
                "arguments": {
                    "department_id": "DEPT1001"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10003\",\n                    \"compensation_id\": \"COMP10000\",\n                    \"performance_review_ids\": [\"PR5003\", \"PR5010\", \"PR10000\"]\n                },\n                {\n                    \"employee_id\": \"E10002\",\n                    \"role_description\": \"Acting Manager\"\n                },\n                {\n                    \"department_id\": \"DEPT1001\",\n                    \"name\": \"Engineering\",\n                    \"budget\": 7015000\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_24",
        "instruction": "Coordinate a data audit on previous leave for Emma Rodriguez (E10003) and Arjun Patel (E10004), effective as of 2025-07-01. Specifically for Amelia, since her parental leave (LV6001) is finalized but still labeled 'Scheduled', update this to 'Taken'. Next, implement a 5% salary increase for her and record a performance review with the summary 'Completed leave and performance cycle.' For Rahul, provide a one-time bonus of $1,500 citing 'Data audit completion bonus.' as his vacation (LV6002) is already marked as 'Taken' correctly. To support these initiatives, shift $10,000 from the Sales department's budget (DEPT1002) to the Marketing department's account (DEPT1005). Ensure by retrieving the revised employee records for both individuals and the updated department record for Marketing.",
        "actions": [
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "GetCompensation",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "UpdateLeaveRecord",
                "arguments": {
                    "leave_id": "LV6001",
                    "updates": {
                        "status": "Taken"
                    }
                },
            },
            {
                "name": "GetUnusedCompensationId",
                "arguments": {
                {}
                },
            },
            {
                "name": "IncreaseEmployeeCompensation",
                "arguments": {
                    "employee_id": "E10003",
                    "compensation_id": "COMP10000",
                    "salary_increase_pct": 5,
                    "effective_date": "2025-07-01"
                },
            },
            {
                "name": "GetUnusedReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "Completed leave and performance cycle."
                    }
                },
            },
            {
                "name": "UpdateEmployee",
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
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10004"
                },
            },
            {
                "name": "GetUnusedBonusId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddBonusPayment",
                "arguments": {
                    "bonus": {
                        "bonus_id": "BON10000",
                        "employee_id": "E10004",
                        "amount": 1500,
                        "reason": "Data audit completion bonus."
                    }
                },
            },
            {
                "name": "GetDepartment",
                "arguments": {
                    "department_id": "DEPT1002"
                },
            },
            {
                "name": "GetDepartment",
                "arguments": {
                    "department_id": "DEPT1005"
                },
            },
            {
                "name": "UpdateDepartment",
                "arguments": {
                    "department_id": "DEPT1002",
                    "updates": {
                        "budget": 4990000
                    }
                },
            },
            {
                "name": "UpdateDepartment",
                "arguments": {
                    "department_id": "DEPT1005",
                    "updates": {
                        "budget": 1610000
                    }
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10004"
                },
            },
            {
                "name": "GetDepartment",
                "arguments": {
                    "department_id": "DEPT1005"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10003\",\n                    \"compensation_id\": \"COMP10000\",\n                    \"performance_review_ids\": [\"PR5003\", \"PR5010\", \"PR10000\"]\n                },\n                {\n                    \"employee_id\": \"E10004\"\n                },\n                {\n                    \"department_id\": \"DEPT1005\",\n                    \"name\": \"Marketing\",\n                    \"budget\": 1610000\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_25",
        "instruction": "Initiate a promotion for Arjun Patel (E10004) to Senior Front-end Engineer (POS3006), which corresponds to a level L.3 position, effective 2026-04-01. This promotion entails a 15% increase IND base salary, resulting IND a new compensation record. Record a performance review with the summary 'Promoted to Senior Front-end Engineer (L.3).' to note the change. To confirm, access his updated employee record.",
        "actions": [
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10004"
                },
            },
            {
                "name": "GetCompensation",
                "arguments": {
                    "employee_id": "E10004"
                },
            },
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10004",
                    "updates": {
                        "level_id": "L.3",
                        "position_id": "POS3006"
                    }
                },
            },
            {
                "name": "GetUnusedCompensationId",
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
                        "base_salary": 135700,
                        "currency": "USD",
                        "equity_grant": 8000,
                        "effective_date": "2026-04-01"
                    }
                },
            },
            {
                "name": "GetUnusedReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10004",
                        "period_start": "2026-04-01",
                        "period_end": "2026-04-01",
                        "rating": null,
                        "summary": "Promoted to Senior Front-end Engineer (L.3)."
                    }
                },
            },
            {
                "name": "UpdateEmployee",
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
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10004"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10004\",\n                    \"first_name\": \"Rahul\",\n                    \"last_name\": \"Singh\",\n                    \"preferred_name\": \"Rahul\",\n                    \"date_of_birth\": \"1988-05-02\",\n                    \"gender\": \"Male\",\n                    \"ethnicity_code\": \"A\",\n                    \"nationality\": \"IND\",\n                    \"marital_status\": \"Married\",\n                    \"hire_date\": \"2022-02-14\",\n                    \"termination_date\": null,\n                    \"status\": \"Active\",\n                    \"position_id\": \"POS3006\",\n                    \"department_id\": \"DEPT1001\",\n                    \"level_id\": \"L.3\",\n                    \"manager_id\": \"E10003\",\n                    \"work_location\": \"Remote – Mumbai\",\n                    \"work_email\": \"arjun.patel@example.com\",\n                    \"work_phone\": \"+91-80-5550-1122\",\n                    \"compensation_id\": \"COMP10000\",\n                    \"benefit_plan_ids\": [\n                        \"BEN4001\",\n                        \"BEN4003\"\n                    ],\n                    \"performance_review_ids\": [\n                        \"PR5004\",\n                        \"PR5009\",\n                        \"PR10000\"\n                    ],\n                    \"skills\": [\n                        \"Go\",\n                        \"Kubernetes\",\n                        \"CI/CD\"\n                    ],\n                    \"role_description\": \"Backend Engineer focusing on micro-services.\",\n                    \"notes\": \"Visa sponsored (H-1B).\"\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_26",
        "instruction": "Coordinate a compensation audit for Michael Park (E10002), effective 2025-07-15. Confirm if his base salary is under $140,000 (target: $145,000) or if his bonus target falls below 15% (target: 17%). Document the audit by logging a performance review. For verification purposes, obtain his complete list of performance reviews.",
        "actions": [
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10002"
                },
            },
            {
                "name": "GetCompensation",
                "arguments": {
                    "employee_id": "E10002"
                },
            },
            {
                "name": "ConditionalCompensationCheckAndUpdate",
                "arguments": {
                    "employee_id": "E10002",
                    "compensation_id": "COMP2002",
                    "effective_date": "2025-07-15",
                    "salary_threshold": 140000,
                    "target_salary": 145000,
                    "bonus_threshold": 15,
                    "target_bonus": 17
                },
            },
            {
                "name": "GetUnusedReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10002",
                        "period_start": "2025-07-15",
                        "period_end": "2025-07-15",
                        "rating": null,
                        "summary": null
                    }
                },
            },
            {
                "name": "UpdateEmployee",
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
                "name": "ListPerformanceReviews",
                "arguments": {
                    "employee_id": "E10002"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"review_id\": \"PR5002\",\n                    \"employee_id\": \"E10002\",\n                    \"period_start\": \"2024-01-01\",\n                    \"period_end\": \"2024-03-31\",\n                    \"rating\": \"Meets\",\n                    \"manager_id\": \"E10012\",\n                    \"summary\": \"On track to hit Q2 quota.\"\n                },\n                {\n                    \"review_id\": \"PR10000\",\n                    \"employee_id\": \"E10002\",\n                    \"period_start\": \"2025-07-15\",\n                    \"period_end\": \"2025-07-15\",\n                    \"rating\": null,\n                    \"summary\": null\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_27",
        "instruction": "Handle and approve a 6-week medical leave for Arjun Patel (E10004) covering the period from 2025-08-01 to 2025-09-12, and upload his 'Medical Certificate' dated 2025-07-24. Assign Michael Park (E10002) as the acting project lead during Singh's absence and log a review for him with the summary 'Acting project lead during R. Singh's leave.' To allocate funds, transfer $15,000 from the Engineering department's budget (DEPT1001) to the Sales department's (DEPT1002). For verification purposes, retrieve the updated records for both departments.",
        "actions": [
            {
                "name": "GetUnusedLeaveId",
                "arguments": {
                {}
                },
            },
            {
                "name": "RequestLeave",
                "arguments": {
                    "leave": {
                        "leave_id": "LV10000",
                        "employee_id": "E10004",
                        "leave_type": "Medical Leave",
                        "start_date": "2025-08-01",
                        "end_date": "2025-09-12",
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
                "name": "GetUnusedDocumentId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddEmployeeDocument",
                "arguments": {
                    "document": {
                        "doc_id": "DOC10000",
                        "employee_id": "E10004",
                        "doc_type": "Medical Certificate",
                        "title": "Medical Certificate",
                        "date": "2025-07-24"
                    }
                },
            },
            {
                "name": "ListEmployeeDocuments",
                "arguments": {
                    "employee_id": "E10004"
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10002"
                },
            },
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10002",
                    "updates": {
                        "role_description": "Acting project lead"
                    }
                },
            },
            {
                "name": "GetUnusedReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10002",
                        "period_start": "2025-08-01",
                        "period_end": "2025-09-12",
                        "rating": null,
                        "summary": "Acting project lead during R. Singh's leave."
                    }
                },
            },
            {
                "name": "UpdateEmployee",
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
                "name": "GetDepartment",
                "arguments": {
                    "department_id": "DEPT1001"
                },
            },
            {
                "name": "GetDepartment",
                "arguments": {
                    "department_id": "DEPT1002"
                },
            },
            {
                "name": "UpdateDepartment",
                "arguments": {
                    "department_id": "DEPT1001",
                    "updates": {
                        "budget": 6985000
                    }
                },
            },
            {
                "name": "UpdateDepartment",
                "arguments": {
                    "department_id": "DEPT1002",
                    "updates": {
                        "budget": 5015000
                    }
                },
            },
            {
                "name": "GetDepartment",
                "arguments": {
                    "department_id": "DEPT1001"
                },
            },
            {
                "name": "GetDepartment",
                "arguments": {
                    "department_id": "DEPT1002"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"department_id\": \"DEPT1001\",\n                    \"name\": \"Engineering\",\n                    \"head_id\": \"E10001\",\n                    \"location\": \"Seattle HQ\",\n                    \"budget\": 6985000,\n                    \"description\": \"Responsible for all product development and technical operations.\"\n                },\n                {\n                    \"department_id\": \"DEPT1002\",\n                    \"name\": \"Sales\",\n                    \"head_id\": \"E10012\",\n                    \"location\": \"Boston Office\",\n                    \"budget\": 5015000,\n                    \"description\": \"Owns revenue generation and customer relationships.\"\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_28",
        "instruction": "As of 2025-09-01, coordinate an internal transfer for Elena Rodriguez (E10005) to the Marketing department (DEPT1005) with her new supervisor, Marcus Chen (E10006). This transfer involves a salary raise to \u20ac78,000. Log a performance review with the summary 'Internal transfer and salary adjustment.' To provide funding, increase the Marketing budget by \u20ac10,000. For verification, obtain her updated employee record and the Marketing department record.",
        "actions": [
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10005"
                },
            },
            {
                "name": "GetCompensation",
                "arguments": {
                    "employee_id": "E10005"
                },
            },
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10005",
                    "updates": {
                        "department_id": "DEPT1005",
                        "manager_id": "E10006"
                    }
                },
            },
            {
                "name": "GetUnusedCompensationId",
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
                        "base_salary": 78000,
                        "bonus_target_pct": 5,
                        "equity_grant": 2000,
                        "currency": "EUR",
                        "effective_date": "2025-09-01"
                    }
                },
            },
            {
                "name": "GetUnusedReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10005",
                        "summary": "Internal transfer and salary adjustment"
                    }
                },
            },
            {
                "name": "UpdateEmployee",
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
                "name": "GetDepartment",
                "arguments": {
                    "department_id": "DEPT1005"
                },
            },
            {
                "name": "UpdateDepartment",
                "arguments": {
                    "department_id": "DEPT1005",
                    "updates": {
                        "budget": 1610000
                    }
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10005"
                },
            },
            {
                "name": "GetDepartment",
                "arguments": {
                    "department_id": "DEPT1005"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10005\",\n                    \"department_id\": \"DEPT1005\",\n                    \"manager_id\": \"E10006\",\n                    \"compensation_id\": \"COMP10000\",\n                    \"performance_review_ids\": [\"PR10000\"]\n                },\n                {\n                    \"department_id\": \"DEPT1005\",\n                    \"name\": \"Marketing\",\n                    \"budget\": 1610000\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_29",
        "instruction": "Handle a 60-day Performance Improvement Plan (PIP) for Rahul Singh (E10004), commencing 2025-10-01, with the summary 'PIP Initiated.' and a 'Needs Improvement' rating. Upload his signed 'PIP Agreement' document. As per policy, create a fresh compensation record to adjust his bonus target to 0%. To support the PIP process, transfer $10,000 from the Sales department's budget (DEPT1002) to Engineering (DEPT1001). For verification, retrieve the updated records for Rahul and the Engineering department.",
        "actions": [
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10004"
                },
            },
            {
                "name": "GetCompensation",
                "arguments": {
                    "employee_id": "E10004"
                },
            },
            {
                "name": "GetUnusedReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10004",
                        "period_start": "2025-10-01",
                        "period_end": "2025-11-30",
                        "rating": "Needs Improvement",
                        "summary": "PIP Initiated."
                    }
                },
            },
            {
                "name": "GetUnusedDocumentId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddEmployeeDocument",
                "arguments": {
                    "document": {
                        "doc_id": "DOC10000",
                        "employee_id": "E10004",
                        "title": "PIP Agreement",
                        "date": "2025-10-01"
                    }
                },
            },
            {
                "name": "GetUnusedCompensationId",
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
                        "bonus_target_pct": 0,
                        "base_salary": 118000,
                        "equity_grant": 8000,
                        "currency": "USD",
                        "effective_date": "2025-10-01"
                    }
                },
            },
            {
                "name": "UpdateEmployee",
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
                "name": "GetDepartment",
                "arguments": {
                    "department_id": "DEPT1002"
                },
            },
            {
                "name": "GetDepartment",
                "arguments": {
                    "department_id": "DEPT1001"
                },
            },
            {
                "name": "UpdateDepartment",
                "arguments": {
                    "department_id": "DEPT1002",
                    "updates": {
                        "budget": 4990000
                    }
                },
            },
            {
                "name": "UpdateDepartment",
                "arguments": {
                    "department_id": "DEPT1001",
                    "updates": {
                        "budget": 7010000
                    }
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10004"
                },
            },
            {
                "name": "GetDepartment",
                "arguments": {
                    "department_id": "DEPT1001"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10004\",\n                    \"compensation_id\": \"COMP10000\",\n                    \"performance_review_ids\": [\"PR5004\", \"PR5009\", \"PR10000\"]\n                },\n                {\n                    \"department_id\": \"DEPT1001\",\n                    \"name\": \"Engineering\",\n                    \"budget\": 7010000\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_30",
        "instruction": "Coordinate a benefit audit for William Liu (E10006), effective 2025-07-24. Enroll him IND the Legal Insurance plan (BEN9999) and ensure he is enrolled in the 401(k) plan (BEN4003). Update his role description to 'Senior Product Manager, Finance Liaison'. Record a performance review with the summary 'Benefit audit completed.' As a reward for the successful audit, issue a one-time bonus of $1,000 to his manager, Isabella Chen (E10001), for 'Managerial oversight.' To fund this, increase the Engineering department's (DEPT1001) budget by $1,000. For verification, retrieve the updated employee records for both Marcus and Sophia, and the updated Engineering department record.",
        "actions": [
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10006"
                },
            },
            {
                "name": "AddEmployeeBenefitsConditionally",
                "arguments": {
                    "employee_id": "E10006",
                    "benefit_plan_ids": [
                        "BEN4003",
                        "BEN9999"
                    ]
                },
            },
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10006",
                    "updates": {
                        "role_description": "Senior Product Manager, Finance Liaison"
                    }
                },
            },
            {
                "name": "GetUnusedReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10006",
                        "summary": "Benefit audit completed."
                    }
                },
            },
            {
                "name": "UpdateEmployee",
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
                "name": "GetUnusedBonusId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddBonusPayment",
                "arguments": {
                    "bonus": {
                        "bonus_id": "BON10000",
                        "employee_id": "E10001",
                        "amount": 1000,
                        "reason": "Managerial oversight."
                    }
                },
            },
            {
                "name": "GetDepartment",
                "arguments": {
                    "department_id": "DEPT1001"
                },
            },
            {
                "name": "UpdateDepartment",
                "arguments": {
                    "department_id": "DEPT1001",
                    "updates": {
                        "budget": 7001000
                    }
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10006"
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10001"
                },
            },
            {
                "name": "GetDepartment",
                "arguments": {
                    "department_id": "DEPT1001"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10006\",\n                    \"role_description\": \"Senior Product Manager, Finance Liaison\",\n                    \"performance_review_ids\": [\"PR5011\", \"PR10000\"]\n                },\n                {\n                    \"employee_id\": \"E10001\"\n                },\n                {\n                    \"department_id\": \"DEPT1001\",\n                    \"name\": \"Engineering\",\n                    \"budget\": 7001000\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_31",
        "instruction": "Handle the voluntary departure of Elena Rodriguez (E10005), taking effect on 2025-12-15. As part of her exit compensation, she should receive a pro-rated performance bonus (ID BON1001) of \u20ac2,500 with the reason 'Pro-rated bonus.'. Update her benefits: terminate all current plans but ensure her enrollment in the vested Legal Insurance plan (BEN9999). Record a final performance review (ID PR5024) with a 'Meets' rating and the summary 'Voluntary termination.' to document the situation. For verification purposes, access her updated employee record.",
        "actions": [
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10005"
                },
            },
            {
                "name": "TerminateEmployee",
                "arguments": {
                    "employee_id": "E10005",
                    "termination_date": "2025-12-15"
                },
            },
            {
                "name": "AddBonusPayment",
                "arguments": {
                    "bonus": {
                        "bonus_id": "BON1001",
                        "employee_id": "E10005",
                        "amount": 2500,
                        "currency": "EUR",
                        "payment_date": "2025-12-15",
                        "reason": "Pro-rated bonus."
                    }
                },
            },
            {
                "name": "SetEmployeeBenefits",
                "arguments": {
                    "employee_id": "E10005",
                    "benefit_plan_ids": [
                        "BEN9999"
                    ]
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR5024",
                        "employee_id": "E10005",
                        "period_start": "2025-12-15",
                        "period_end": "2025-12-15",
                        "rating": "Meets",
                        "summary": "Voluntary termination."
                    }
                },
            },
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10005",
                    "updates": {
                        "performance_review_ids": [
                            "PR5024"
                        ]
                    }
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10005"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10005\",\n                    \"first_name\": \"Elena\",\n                    \"last_name\": \"Rodriguez\",\n                    \"preferred_name\": \"Elena\",\n                    \"date_of_birth\": \"1995-01-30\",\n                    \"gender\": \"Female\",\n                    \"ethnicity_code\": \"H\",\n                    \"nationality\": \"ESP\",\n                    \"marital_status\": \"Single\",\n                    \"hire_date\": \"2024-09-01\",\n                    \"termination_date\": \"2025-12-15\",\n                    \"status\": \"Terminated\",\n                    \"position_id\": \"POS3010\",\n                    \"department_id\": \"DEPT1004\",\n                    \"level_id\": \"L.1\",\n                    \"manager_id\": \"E10011\",\n                    \"work_location\": \"Barcelona Office\",\n                    \"work_email\": \"olivia.martinez@example.com\",\n                    \"work_phone\": \"+34-91-555-0200\",\n                    \"compensation_id\": \"COMP2005\",\n                    \"benefit_plan_ids\": [\n                      \"BEN9999\"\n                    ],\n                    \"performance_review_ids\": [\n                     \"PR5024\"\n                    ],\n                    \"skills\": [\n                        \"Financial Modeling\",\n                        \"SQL\",\n                        \"Excel\"\n                    ],\n                    \"role_description\": \"Junior Financial Analyst supporting quarterly forecasts.\",\n                    \"notes\": \"Recent graduate—ESADE Business School.\"\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_32",
        "instruction": "Initiate the onboarding of a new Senior Backend Engineer, Sarah Johnson, with a start date of 2025-08-15, for the Engineering department (DEPT1001). Her compensation package includes a $145,000 salary, 15% bonus, and $25,000 equity grant. Upon joining, Sarah will take on the role of manager for Rahul Singh (E10004). Record a performance review for Rahul with the summary 'Manager updated.' To finance the new position, allocate $175,000 from the Sales budget (DEPT1002) to Engineering. For verification, obtain the updated records for both the employees and the Engineering department.",
        "actions": [
            {
                "name": "GetUnusedEmployeeId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateEmployee",
                "arguments": {
                    "employee": {
                        "employee_id": "E10000",
                        "first_name": "Sarah",
                        "last_name": "Johnson",
                        "status": "Active",
                        "hire_date": "2025-08-15",
                        "department_id": "DEPT1001",
                        "role_description": "Senior Backend Engineer"
                    }
                },
            },
            {
                "name": "GetUnusedCompensationId",
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
                        "base_salary": 145000,
                        "bonus_target_pct": 15,
                        "equity_grant": 25000,
                        "currency": "USD",
                        "effective_date": "2025-08-15"
                    }
                },
            },
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10000",
                    "updates": {
                        "compensation_id": "COMP10000"
                    }
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10004"
                },
            },
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10004",
                    "updates": {
                        "manager_id": "E10000"
                    }
                },
            },
            {
                "name": "GetUnusedReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10004",
                        "summary": "Manager updated"
                    }
                },
            },
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10004",
                    "updates": {
                        "performance_review_ids": [
                            "PR5004",
                            "PR5009",
                            "PR10000"
                        ]
                    }
                },
            },
            {
                "name": "GetDepartment",
                "arguments": {
                    "department_id": "DEPT1002"
                },
            },
            {
                "name": "GetDepartment",
                "arguments": {
                    "department_id": "DEPT1001"
                },
            },
            {
                "name": "UpdateDepartment",
                "arguments": {
                    "department_id": "DEPT1002",
                    "updates": {
                        "budget": 4825000
                    }
                },
            },
            {
                "name": "UpdateDepartment",
                "arguments": {
                    "department_id": "DEPT1001",
                    "updates": {
                        "budget": 7175000
                    }
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10000"
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10004"
                },
            },
            {
                "name": "GetDepartment",
                "arguments": {
                    "department_id": "DEPT1001"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10000\",\n                    \"first_name\": \"Sarah\",\n                    \"last_name\": \"Johnson\",\n                    \"compensation_id\": \"COMP10000\"\n                },\n                {\n                    \"employee_id\": \"E10004\",\n                    \"manager_id\": \"E10000\",\n                    \"performance_review_ids\": [\"PR5004\", \"PR5009\", \"PR10000\"]\n                },\n                {\n                    \"department_id\": \"DEPT1001\",\n                    \"name\": \"Engineering\",\n                    \"budget\": 7175000\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_33",
        "instruction": "Announce the launch of a new initiative, 'Project Titan,' starting from 2025-11-01. Firstly, promote Amelia Garcia (E10003) to the position 'Lead Engineer, Project Titan' (POS4001), classified as level L.5. This role adjustment encompasses a 12% salary hike and an added $30,000 equity grant. Document this by generating a fresh compensation record and recording a performance review with the note 'Promotion to Lead Engineer, Project Titan.' Subsequently, reassign Rahul Singh (E10004) to fill Amelia's former role (POS3006) within the Marketing department (DEPT1005). Reallocate funds by reducing the Marketing department's budget by $250,000 and bolstering the Engineering department's (DEPT1001) budget equivalent to this reduction. IND addition, prefix 'HIRING FREEZE: Q4 2025.' to the Marketing department's description. For confirmation, retrieve the revised employee records for both Amelia Garcia and Rahul Singh, alongside the updated department record for Engineering.",
        "actions": [
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "GetCompensation",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10003",
                    "updates": {
                        "position_id": "POS4001",
                        "level_id": "L.5",
                        "role_description": "Lead Engineer, Project Titan"
                    }
                },
            },
            {
                "name": "GetUnusedCompensationId",
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
                        "base_salary": 162400,
                        "equity_grant": 45000,
                        "currency": "USD",
                        "bonus_target_pct": 15,
                        "effective_date": "2025-11-01"
                    }
                },
            },
            {
                "name": "GetUnusedReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "Promotion to Lead Engineer, Project Titan."
                    }
                },
            },
            {
                "name": "UpdateEmployee",
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
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10004"
                },
            },
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10004",
                    "updates": {
                        "position_id": "POS3006",
                        "department_id": "DEPT1005"
                    }
                },
            },
            {
                "name": "GetDepartment",
                "arguments": {
                    "department_id": "DEPT1005"
                },
            },
            {
                "name": "GetDepartment",
                "arguments": {
                    "department_id": "DEPT1001"
                },
            },
            {
                "name": "UpdateDepartment",
                "arguments": {
                    "department_id": "DEPT1005",
                    "updates": {
                        "budget": 1350000,
                        "description": "HIRING FREEZE: Q4 2025. Drives brand awareness and demand generation."
                    }
                },
            },
            {
                "name": "UpdateDepartment",
                "arguments": {
                    "department_id": "DEPT1001",
                    "updates": {
                        "budget": 7250000
                    }
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10004"
                },
            },
            {
                "name": "GetDepartment",
                "arguments": {
                    "department_id": "DEPT1001"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10003\",\n                    \"position_id\": \"POS4001\",\n                    \"level_id\": \"L.5\",\n                    \"compensation_id\": \"COMP10000\",\n                    \"performance_review_ids\": [\"PR5003\", \"PR5010\", \"PR10000\"]\n                },\n                {\n                    \"employee_id\": \"E10004\",\n                    \"position_id\": \"POS3006\",\n                    \"department_id\": \"DEPT1005\"\n                },\n                {\n                    \"department_id\": \"DEPT1001\",\n                    \"name\": \"Engineering\",\n                    \"budget\": 7250000\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_34",
        "instruction": "Prolong Amelia Garcia's (E10003) parental leave (LV6001) through 2025-03-01 and upload her 'Medical Certificate' dated 2025-07-01. Record a review for her with the note 'Parental leave extended.' To acknowledge Michael Park (E10002) for taking over her responsibilities, designate him as 'Acting Team Lead' by updating his role description and award him a one-time bonus of $1,500 for 'Leave coverage bonus.' For validation, retrieve both updated employee records.",
        "actions": [
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "UpdateLeaveRecord",
                "arguments": {
                    "leave_id": "LV6001",
                    "updates": {
                        "end_date": "2025-03-01"
                    }
                },
            },
            {
                "name": "GetUnusedDocumentId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddEmployeeDocument",
                "arguments": {
                    "document": {
                        "doc_id": "DOC10000",
                        "employee_id": "E10003",
                        "title": "Medical Certificate",
                        "date": "2025-07-01"
                    }
                },
            },
            {
                "name": "GetUnusedReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "summary": "Parental leave extended."
                    }
                },
            },
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10003",
                    "updates": {
                        "performance_review_ids": [
                            "PR5003",
                            "PR5010",
                            "PR10000"
                        ]
                    }
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10002"
                },
            },
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10002",
                    "updates": {
                        "role_description": "Acting Team Lead"
                    }
                },
            },
            {
                "name": "GetUnusedBonusId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddBonusPayment",
                "arguments": {
                    "bonus": {
                        "bonus_id": "BON10000",
                        "employee_id": "E10002",
                        "amount": 1500,
                        "reason": "Leave coverage bonus"
                    }
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10002"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10003\",\n                    \"performance_review_ids\": [\"PR5003\", \"PR5010\", \"PR10000\"]\n                },\n                {\n                    \"employee_id\": \"E10002\",\n                    \"role_description\": \"Acting Team Lead\"\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_35",
        "instruction": "Starting from 2025-10-15, handle the promotion of William Liu (E10006) to Director (level L.5) with a revised base salary of \u20ac85,000 and a bonus target of 18%. With this transition, assign him as the new head of the Finance department (DEPT1004). To facilitate this, transfer \u20ac150,000 from the budget of the Marketing department (DEPT1005) to Finance. Lastly, enter a single performance review for Marcus with the summary 'Promotion to Director and Head of Finance.' To confirm, fetch the updated records for William Liu and the two affected departments.",
        "actions": [
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10006"
                },
            },
            {
                "name": "GetCompensation",
                "arguments": {
                    "employee_id": "E10006"
                },
            },
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10006",
                    "updates": {
                        "level_id": "L.5",
                        "role_description": "Director",
                        "position_id": null
                    }
                },
            },
            {
                "name": "GetUnusedCompensationId",
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
                        "base_salary": 85000,
                        "bonus_target_pct": 18,
                        "equity_grant": 5000,
                        "currency": "EUR",
                        "effective_date": "2025-10-15"
                    }
                },
            },
            {
                "name": "GetUnusedReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10006",
                        "summary": "Promotion to Director and Head of Finance"
                    }
                },
            },
            {
                "name": "UpdateEmployee",
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
                "name": "GetDepartment",
                "arguments": {
                    "department_id": "DEPT1005"
                },
            },
            {
                "name": "GetDepartment",
                "arguments": {
                    "department_id": "DEPT1004"
                },
            },
            {
                "name": "UpdateDepartment",
                "arguments": {
                    "department_id": "DEPT1005",
                    "updates": {
                        "budget": 1450000
                    }
                },
            },
            {
                "name": "UpdateDepartment",
                "arguments": {
                    "department_id": "DEPT1004",
                    "updates": {
                        "budget": 1350000,
                        "head_id": "E10006"
                    }
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10006"
                },
            },
            {
                "name": "GetDepartment",
                "arguments": {
                    "department_id": "DEPT1005"
                },
            },
            {
                "name": "GetDepartment",
                "arguments": {
                    "department_id": "DEPT1004"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10006\",\n                    \"level_id\": \"L.5\",\n                    \"role_description\": \"Director\",\n                    \"compensation_id\": \"COMP10000\",\n                    \"performance_review_ids\": [\"PR5011\", \"PR10000\"]\n                },\n                {\n                    \"department_id\": \"DEPT1005\",\n                    \"name\": \"Marketing\",\n                    \"budget\": 1450000\n                },\n                {\n                    \"department_id\": \"DEPT1004\",\n                    \"name\": \"Finance\",\n                    \"head_id\": \"E10006\",\n                    \"budget\": 1350000\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_36",
        "instruction": "Starting from 2025-09-01, handle the re-hire of former employee, Adrian Thompson (E99999), as a 'Senior Backend Engineer' (POS3009) at level L.3 within the Engineering department (DEPT1001). His updated compensation comprises a base salary of $130,000 and a bonus target of 15%; assign his benefits to the standard package (BEN4001, BEN4002, BEN4003) and upload his 'Re-hire Packet' document. Upon commencement, Andrian will take on the role of manager for Michael Park (E10002). As a result, advance Daniel to 'Senior Analyst' (POS3012), adjust his salary with a 5% increase, and record a performance review with the summary 'Promotion to Senior Analyst'. To finance these changes, shift $150,000 from the Sales department budget (DEPT1002) to that of the Engineering department's (DEPT1001). For confirmation, acquire the updated employee records for both Andrian and Daniel, alongside the revised department record for Engineering.",
        "actions": [
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E99999",
                    "updates": {
                        "status": "Active",
                        "hire_date": "2025-09-01",
                        "termination_date": null,
                        "position_id": "POS3009",
                        "department_id": "DEPT1001",
                        "level_id": "L.3",
                        "role_description": "Senior Backend Engineer"
                    }
                },
            },
            {
                "name": "GetUnusedCompensationId",
                "arguments": {
                {}
                },
            },
            {
                "name": "SetCompensation",
                "arguments": {
                    "compensation": {
                        "compensation_id": "COMP10000",
                        "employee_id": "E99999",
                        "base_salary": 130000,
                        "bonus_target_pct": 15,
                        "currency": "USD",
                        "effective_date": "2025-09-01"
                    }
                },
            },
            {
                "name": "SetEmployeeBenefits",
                "arguments": {
                    "employee_id": "E99999",
                    "benefit_plan_ids": [
                        "BEN4001",
                        "BEN4002",
                        "BEN4003"
                    ]
                },
            },
            {
                "name": "GetUnusedDocumentId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddEmployeeDocument",
                "arguments": {
                    "document": {
                        "doc_id": "DOC10000",
                        "employee_id": "E99999",
                        "title": "Re-hire Packet"
                    }
                },
            },
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E99999",
                    "updates": {
                        "compensation_id": "COMP10000"
                    }
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10002"
                },
            },
            {
                "name": "GetCompensation",
                "arguments": {
                    "employee_id": "E10002"
                },
            },
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10002",
                    "updates": {
                        "manager_id": "E99999",
                        "position_id": "POS3012"
                    }
                },
            },
            {
                "name": "IncreaseEmployeeCompensation",
                "arguments": {
                    "employee_id": "E10002",
                    "compensation_id": "COMP2002",
                    "salary_increase_pct": 5,
                    "effective_date": "2025-09-01"
                },
            },
            {
                "name": "GetUnusedReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10002",
                        "summary": "Promotion to Senior Analyst"
                    }
                },
            },
            {
                "name": "UpdateEmployee",
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
                "name": "GetDepartment",
                "arguments": {
                    "department_id": "DEPT1002"
                },
            },
            {
                "name": "GetDepartment",
                "arguments": {
                    "department_id": "DEPT1001"
                },
            },
            {
                "name": "UpdateDepartment",
                "arguments": {
                    "department_id": "DEPT1002",
                    "updates": {
                        "budget": 4850000
                    }
                },
            },
            {
                "name": "UpdateDepartment",
                "arguments": {
                    "department_id": "DEPT1001",
                    "updates": {
                        "budget": 7150000
                    }
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E99999"
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10002"
                },
            },
            {
                "name": "GetDepartment",
                "arguments": {
                    "department_id": "DEPT1001"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E99999\",\n                    \"status\": \"Active\",\n                    \"position_id\": \"POS3009\",\n                    \"level_id\": \"L.3\",\n                    \"compensation_id\": \"COMP10000\"\n                },\n                {\n                    \"employee_id\": \"E10002\",\n                    \"manager_id\": \"E99999\",\n                    \"position_id\": \"POS3012\",\n                    \"performance_review_ids\": [\"PR5002\", \"PR10000\"]\n                },\n                {\n                    \"department_id\": \"DEPT1001\",\n                    \"name\": \"Engineering\",\n                    \"budget\": 7150000\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_37",
        "instruction": "Authorize the request for Rahul Singh (E10004) to continue his work permanently from his present remote location in Bangalore, starting 2025-12-01. Modify his work location to reflect the standardized entry 'Remote - Mumbai' and upload his 'Remote Work Agreement' document. Additionally, record a performance review note with the summary 'Permanent remote work approved.' to log the adjustment. To verify, obtain his updated employee record.",
        "actions": [
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10004"
                },
            },
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10004",
                    "updates": {
                        "work_location": "Remote - Bangalore"
                    }
                },
            },
            {
                "name": "GetUnusedDocumentId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddEmployeeDocument",
                "arguments": {
                    "document": {
                        "doc_id": "DOC10000",
                        "employee_id": "E10004",
                        "doc_type": "Remote Work Agreement",
                        "title": "Remote Work Agreement",
                        "date": "2025-12-01"
                    }
                },
            },
            {
                "name": "GetUnusedReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10004",
                        "period_start": "2025-12-01",
                        "period_end": "2025-12-01",
                        "rating": null,
                        "summary": "Permanent remote work approved."
                    }
                },
            },
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10004",
                    "updates": {
                        "performance_review_ids": [
                            "PR5004",
                            "PR5009",
                            "PR10000"
                        ]
                    }
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10004"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10004\",\n                    \"first_name\": \"Rahul\",\n                    \"last_name\": \"Singh\",\n                    \"preferred_name\": \"Rahul\",\n                    \"date_of_birth\": \"1988-05-02\",\n                    \"gender\": \"Male\",\n                    \"ethnicity_code\": \"A\",\n                    \"nationality\": \"IND\",\n                    \"marital_status\": \"Married\",\n                    \"hire_date\": \"2022-02-14\",\n                    \"termination_date\": null,\n                    \"status\": \"Active\",\n                    \"position_id\": \"POS3007\",\n                    \"department_id\": \"DEPT1001\",\n                    \"level_id\": \"L.2\",\n                    \"manager_id\": \"E10003\",\n                    \"work_location\": \"Remote - Mumbai\",\n                    \"work_email\": \"arjun.patel@example.com\",\n                    \"work_phone\": \"+91-80-5550-1122\",\n                    \"compensation_id\": \"COMP2004\",\n                    \"benefit_plan_ids\": [\n                        \"BEN4001\",\n                        \"BEN4003\"\n                    ],\n                    \"performance_review_ids\": [\n                        \"PR5004\",\n                        \"PR5009\",\n                        \"PR10000\"\n                    ],\n                    \"skills\": [\n                        \"Go\",\n                        \"Kubernetes\",\n                        \"CI/CD\"\n                    ],\n                    \"role_description\": \"Backend Engineer focusing on micro-services.\",\n                    \"notes\": \"Visa sponsored (H-1B).\"\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_38",
        "instruction": "Handle the annual performance evaluation for Amelia Garcia (E10003), effective 2025-07-24. Her performance rating is 'Exceeds', making her eligible for a one-time performance bonus of $8,500 with the reason 'Annual performance bonus.' and an 8% merit-based salary raise. Record these changes by creating a new performance review with the summary 'Annual review completed.'. For verification, obtain her updated employee record.",
        "actions": [
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "GetCompensation",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "GetUnusedReviewId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR10000",
                        "employee_id": "E10003",
                        "period_start": "2024-07-24",
                        "period_end": "2025-07-24",
                        "rating": "Exceeds",
                        "summary": "Annual review completed."
                    }
                },
            },
            {
                "name": "GetUnusedBonusId",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddBonusPayment",
                "arguments": {
                    "bonus": {
                        "bonus_id": "BON10000",
                        "employee_id": "E10003",
                        "amount": 8500,
                        "currency": "USD",
                        "payment_date": "2025-07-24",
                        "reason": "Annual performance bonus."
                    }
                },
            },
            {
                "name": "IncreaseEmployeeCompensation",
                "arguments": {
                    "employee_id": "E10003",
                    "salary_increase_pct": 8,
                    "compensation_id": "COMP2003",
                    "effective_date": "2025-07-24"
                },
            },
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10003",
                    "updates": {
                        "performance_review_ids": [
                            "PR5003",
                            "PR5010",
                            "PR10000"
                        ]
                    }
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10003"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10003\",\n                    \"first_name\": \"Amelia\",\n                    \"last_name\": \"Garcia\",\n                    \"preferred_name\": \"Amy\",\n                    \"date_of_birth\": \"1990-11-22\",\n                    \"gender\": \"Female\",\n                    \"ethnicity_code\": \"H\",\n                    \"nationality\": \"USA\",\n                    \"marital_status\": \"Partnered\",\n                    \"hire_date\": \"2019-06-10\",\n                    \"termination_date\": null,\n                    \"status\": \"Active\",\n                    \"position_id\": \"POS3006\",\n                    \"department_id\": \"DEPT1005\",\n                    \"level_id\": \"L.3\",\n                    \"manager_id\": \"E10001\",\n                    \"work_location\": \"Remote – Dallas, TX\",\n                    \"work_email\": \"emma.rodriguez@example.com\",\n                    \"work_phone\": \"+1-737-555-0188\",\n                    \"compensation_id\": \"COMP2003\",\n                    \"benefit_plan_ids\": [\n                        \"BEN4001\",\n                        \"BEN4003\",\n                        \"BEN4004\"\n                    ],\n                    \"performance_review_ids\": [\n                        \"PR5003\",\n                        \"PR5010\",\n                        \"PR10000\"\n                    ],\n                    \"skills\": [\n                        \"TypeScript\",\n                        \"React\",\n                        \"Accessibility\"\n                    ],\n                    \"role_description\": \"Senior Front-end Engineer on the web platform team.\",\n                    \"notes\": \"On parental leave 2024-11-01 → 2025-02-01.\"\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_39",
        "instruction": "Handle an emergency family leave for Marcus Chen (E10006). This leave spans 2 weeks, beginning retroactively from 2025-07-20 and concluding on 2025-08-03. Document and authorize the request using leave ID LV8006. Since the leave is presently active, adjust his employment status to 'On Leave'. Attach the 'Emergency Leave Request' form (doc ID E10006-001) under the title 'Emergency Leave Form'. Record a review note (ID PR5032) with the summary 'Emergency leave processed.' for documentation. To verify, access his updated employee record.",
        "actions": [
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10006"
                },
            },
            {
                "name": "RequestLeave",
                "arguments": {
                    "leave": {
                        "leave_id": "LV8006",
                        "employee_id": "E10006",
                        "leave_type": "Emergency Family Leave",
                        "start_date": "2025-07-20",
                        "end_date": "2025-08-03",
                        "status": "Pending"
                    }
                },
            },
            {
                "name": "UpdateLeaveStatus",
                "arguments": {
                    "leave_id": "LV8006",
                    "status": "Approved"
                },
            },
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10006",
                    "updates": {
                        "status": "On Leave"
                    }
                },
            },
            {
                "name": "AddEmployeeDocument",
                "arguments": {
                    "document": {
                        "doc_id": "E10006-001",
                        "employee_id": "E10006",
                        "doc_type": "Emergency Leave",
                        "title": "Emergency Leave Form"
                    }
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR5032",
                        "employee_id": "E10006",
                        "period_start": "2025-07-20",
                        "period_end": "2025-08-03",
                        "rating": null,
                        "summary": "Emergency leave processed."
                    }
                },
            },
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10006",
                    "updates": {
                        "performance_review_ids": [
                            "PR5011",
                            "PR5032"
                        ]
                    }
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10006"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"employee_id\": \"E10006\",\n                    \"first_name\": \"Marcus\",\n                    \"last_name\": \"Chen\",\n                    \"preferred_name\": \"Marcus\",\n                    \"date_of_birth\": \"1991-08-12\",\n                    \"gender\": \"Male\",\n                    \"ethnicity_code\": \"A\",\n                    \"nationality\": \"CAN\",\n                    \"marital_status\": \"Married\",\n                    \"hire_date\": \"2023-11-15\",\n                    \"termination_date\": null,\n                    \"status\": \"On Leave\",\n                    \"position_id\": \"POS3008\",\n                    \"department_id\": \"DEPT1004\",\n                    \"level_id\": \"L.4\",\n                    \"manager_id\": \"E10012\",\n                    \"work_location\": \"Barcelona Office\",\n                    \"work_email\": \"william.liu@example.com\",\n                    \"work_phone\": \"+1-604-555-0166\",\n                    \"compensation_id\": \"COMP2006\",\n                    \"benefit_plan_ids\": [\n                        \"BEN4001\",\n                        \"BEN4002\",\n                        \"BEN4003\"\n                    ],\n                    \"performance_review_ids\": [\n                        \"PR5011\",\n                        \"PR5032\"\n                    ],\n                    \"skills\": [\n                        \"Product Strategy\",\n                        \"User Research\",\n                        \"Data Analytics\"\n                    ],\n                    \"role_description\": \"Senior Product Manager leading the analytics platform initiatives.\",\n                    \"notes\": \"Previously led successful product launches at major tech companies.\"\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_40",
        "instruction": "Coordinate a compensation audit for Daniel Kim (E10002), starting 2025-12-01. The audit compares his salary against a $150,000 minimum (target: $152,000) and his bonus target against a 20% minimum (target: 20%). The audit also incorporates an unconditional equity grant increase of $5,000. Establish a new compensation record with ID COMP5008. Record a review note (ID PR5033) with the summary 'Compensation audit completed.' to document the audit's outcomes. For verification, obtain his latest compensation record.",
        "actions": [
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10002"
                },
            },
            {
                "name": "ConditionalCompensationCheckAndUpdate",
                "arguments": {
                    "employee_id": "E10002",
                    "compensation_id": "COMP5008",
                    "effective_date": "2025-12-01",
                    "salary_threshold": 150000,
                    "target_salary": 152000,
                    "bonus_threshold": 20,
                    "target_bonus": 20,
                    "equity_increase_amount": 5000
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR5033",
                        "employee_id": "E10002",
                        "period_start": "2025-12-01",
                        "period_end": "2025-12-01",
                        "rating": null,
                        "summary": "Compensation audit completed."
                    }
                },
            },
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10002",
                    "updates": {
                        "performance_review_ids": [
                            "PR5002",
                            "PR5033"
                        ]
                    }
                },
            },
            {
                "name": "GetCompensation",
                "arguments": {
                    "employee_id": "E10002"
                }
            }
        ],
        "outputs": [
                "\n            [\n                {\n                    \"compensation_id\": \"COMP5008\",\n                    \"employee_id\": \"E10002\",\n                    \"base_salary\": 210000,\n                    \"currency\": \"USD\",\n                    \"bonus_target_pct\": 25,\n                    \"equity_grant\": 45000,\n                    \"effective_date\": \"2025-12-01\"\n                }\n            ]\n            "
        ]
    }
]
