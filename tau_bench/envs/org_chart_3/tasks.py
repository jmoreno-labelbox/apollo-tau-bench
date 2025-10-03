
tasks = [
    {
        "annotator": 0,
        "user_id": "res_01",
        "instruction": "Delete the Dental Plan (BEN4002) from Michael Park's benefits with immediate effect and document the change.",
        "actions": [
            {
                "name": "SearchEmployees",
                "arguments": {
                    "filters": {
                        "first_name": "Daniel",
                        "last_name": "Kim"
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
                "name": "SetEmployeeBenefits",
                "arguments": {
                    "employee_id": "E10002",
                    "benefit_plan_ids": [
                        "BEN4001"
                    ]
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
                "Dental Plan BEN4002 removed for Michael Park."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_02",
        "instruction": "Grant Isabella Chen a $8,000 spot bonus and confirm the payout record.",
        "actions": [
            {
                "name": "SearchEmployees",
                "arguments": {
                    "filters": {
                        "first_name": "Sophia",
                        "last_name": "Nguyen"
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
                "name": "AddBonusPayment",
                "arguments": {
                    "bonus": {
                        "bonus_id": "BON_SophiaNguyen_8000",
                        "employee_id": "E10001",
                        "amount": 8000,
                        "currency": "USD"
                    }
                },
            },
            {
                "name": "ListBonusPayments",
                "arguments": {
                    "employee_id": "E10001"
                }
            }
        ],
        "outputs": [
                "$8,000 spot bonus BON_SophiaNguyen_8000 recorded for Isabella Chen."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_03",
        "instruction": "Handle the update of Emma Rodriguez's (E10003) work location to 'Remote - Denver', starting 2025-07-24. Record a performance review note, PR5011, to document this modification. To verify, access her updated employee record.",
        "actions": [
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10003",
                    "updates": {
                        "work_location": "Remote - Denver"
                    }
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR5011",
                        "employee_id": "E10003",
                        "period_start": "2025-07-24",
                        "period_end": "2025-07-24",
                        "rating": null,
                        "summary": "Work location updated to Remote - Denver."
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
                            "PR5011"
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
                "\n            [\n                {\n                    \"employee_id\": \"E10003\",\n                    \"first_name\": \"Amelia\",\n                    \"last_name\": \"Garcia\",\n                    \"preferred_name\": \"Amy\",\n                    \"date_of_birth\": \"1990-11-22\",\n                    \"gender\": \"Female\",\n                    \"ethnicity_code\": \"H\",\n                    \"nationality\": \"USA\",\n                    \"marital_status\": \"Partnered\",\n                    \"hire_date\": \"2019-06-10\",\n                    \"termination_date\": null,\n                    \"status\": \"Active\",\n                    \"position_id\": \"POS3006\",\n                    \"department_id\": \"DEPT1005\",\n                    \"level_id\": \"L.3\",\n                    \"manager_id\": \"E10001\",\n                    \"work_location\": \"Remote - Denver\",\n                    \"work_email\": \"emma.rodriguez@example.com\",\n                    \"work_phone\": \"+1-737-555-0188\",\n                    \"compensation_id\": \"COMP2003\",\n                    \"benefit_plan_ids\": [\n                        \"BEN4001\",\n                        \"BEN4003\",\n                        \"BEN4004\"\n                    ],\n                    \"performance_review_ids\": [\n                        \"PR5003\",\n                        \"PR5010\",\n                        \"PR5011\"\n                    ],\n                    \"skills\": [\n                        \"TypeScript\",\n                        \"React\",\n                        \"Accessibility\"\n                    ],\n                    \"role_description\": \"Senior Front-end Engineer on the web platform team.\",\n                    \"notes\": \"On parental leave 2024-11-01 → 2025-02-01.\"\n                }\n            ]\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_04",
        "instruction": "Coordinate the logging and approval of a 10-day jury duty leave for Michael Park (E10002), spanning from 2026-06-05 to 2026-06-14. Access his complete list of leave records for confirmation.",
        "actions": [
            {
                "name": "RequestLeave",
                "arguments": {
                    "leave": {
                        "leave_id": "LV5001",
                        "employee_id": "E10002",
                        "leave_type": "Jury Duty",
                        "start_date": "2026-06-05",
                        "end_date": "2026-06-14",
                        "status": "Pending",
                        "notes": "10-day jury duty leave."
                    }
                },
            },
            {
                "name": "UpdateLeaveStatus",
                "arguments": {
                    "leave_id": "LV5001",
                    "status": "Approved"
                },
            },
            {
                "name": "ListLeaveRecords",
                "arguments": {
                    "employee_id": "E10002"
                }
            }
        ],
        "outputs": [
                "\n            {\n              \"count\": 1,\n              \"results\": [\n                {\n                  \"leave_id\": \"LV5001\",\n                  \"employee_id\": \"E10002\",\n                  \"leave_type\": \"Jury Duty\",\n                  \"start_date\": \"2026-06-05\",\n                  \"end_date\": \"2026-06-14\",\n                  \"status\": \"Approved\",\n                  \"notes\": \"10-day jury duty leave.\"\n                }\n              ]\n            }\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_05",
        "instruction": "Seek to advance Emma Rodriguez from Senior Engineer (L.3) to Staff Engineer (L.4), elevate her base salary by 10 %, and document the change.",
        "actions": [
            {
                "name": "SearchEmployees",
                "arguments": {
                    "filters": {
                        "first_name": "Amelia",
                        "last_name": "Garcia"
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
                        "level_id": "L.4"
                    }
                },
            },
            {
                "name": "IncreaseEmployeeCompensation",
                "arguments": {
                    "employee_id": "E10003",
                    "compensation_id": "COMP2003",
                    "effective_date": "2024-07-01",
                    "salary_increase_pct": 10
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
                "Emma Rodriguez promoted to L.4 with 10% salary increase."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_06",
        "instruction": "Authorize a $25,000 equity refresh for Isabella Chen effective 2025-09-01. Establish compensation record COMP2008 and performance review PR5015 to document the change.",
        "actions": [
            {
                "name": "SearchEmployees",
                "arguments": {
                    "filters": {
                        "first_name": "Sophia",
                        "last_name": "Nguyen"
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
                "name": "IncreaseEmployeeCompensation",
                "arguments": {
                    "employee_id": "E10001",
                    "compensation_id": "COMP2008",
                    "effective_date": "2025-09-01",
                    "equity_increase_amount": 25000
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR5015",
                        "employee_id": "E10001",
                        "period_start": "2025-09-01",
                        "period_end": "2025-09-01"
                    }
                },
            },
            {
                "name": "ListPerformanceReviews",
                "arguments": {
                    "employee_id": "E10001"
                }
            }
        ],
        "outputs": [
                "Isabella Chen equity refresh recorded IND compensation COMP2008 and review PR5015."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_07",
        "instruction": "Re-employ Michael Park (E10002) starting from 2025-10-01 IND the role of Financial Analyst (position POS3010) within Finance (DEPT1004) reporting to manager E10011. Establish a compensation record COMP2009 (base 120000 USD, bonus 10%) and document the occurrence with performance review PR5016.",
        "actions": [
            {
                "name": "SearchEmployees",
                "arguments": {
                    "filters": {
                        "first_name": "Daniel",
                        "last_name": "Kim"
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
                        "status": "Active",
                        "hire_date": "2025-10-01",
                        "termination_date": "",
                        "department_id": "DEPT1004",
                        "manager_id": "E10011",
                        "position_id": "POS3010"
                    }
                },
            },
            {
                "name": "SetCompensation",
                "arguments": {
                    "compensation": {
                        "compensation_id": "COMP2009",
                        "employee_id": "E10002",
                        "base_salary": 120000,
                        "currency": "USD",
                        "bonus_target_pct": 10,
                        "equity_grant": 0,
                        "effective_date": "2025-10-01"
                    }
                },
            },
            {
                "name": "SetEmployeeBenefits",
                "arguments": {
                    "employee_id": "E10002",
                    "benefit_plan_ids": [
                        "BEN4001",
                        "BEN4002"
                    ]
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR5016",
                        "employee_id": "E10002",
                        "period_start": "2025-10-01",
                        "period_end": "2025-10-01"
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
                "Michael Park rehired with compensation COMP2009; review PR5016 recorded."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_08",
        "instruction": "Move Emma Rodriguez (E10003) to the Engineering department (DEPT1001); Isabella Chen (E10001) will continue as manager. Record the transfer IND review PR5017.",
        "actions": [
            {
                "name": "SearchEmployees",
                "arguments": {
                    "filters": {
                        "first_name": "Amelia",
                        "last_name": "Garcia"
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
                "name": "GetDepartment",
                "arguments": {
                    "department_id": "DEPT1001"
                },
            },
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10003",
                    "updates": {
                        "department_id": "DEPT1001"
                    }
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR5017",
                        "employee_id": "E10003",
                        "period_start": "2025-10-15",
                        "period_end": "2025-10-15"
                    }
                },
            },
            {
                "name": "ListPerformanceReviews",
                "arguments": {
                    "employee_id": "E10003"
                }
            }
        ],
        "outputs": [
                "Emma Rodriguez transferred to DEPT1001; review PR5017 logged."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_09",
        "instruction": "Register Isabella Chen (E10001) for Vision Plan BEN4006 immediately. Establish benefit plan BEN4006 (name 'Vision Plan') and record performance review PR5018 to document the benefit modification.",
        "actions": [
            {
                "name": "SearchEmployees",
                "arguments": {
                    "filters": {
                        "first_name": "Sophia",
                        "last_name": "Nguyen"
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
                "name": "AddBenefitPlan",
                "arguments": {
                    "benefit_plan": {
                        "benefit_plan_id": "BEN4006",
                        "name": "Vision Plan"
                    }
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
                        "BEN4006"
                    ]
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR5018",
                        "employee_id": "E10001",
                        "period_start": "2025-07-28",
                        "period_end": "2025-07-28"
                    }
                },
            },
            {
                "name": "ListPerformanceReviews",
                "arguments": {
                    "employee_id": "E10001"
                }
            }
        ],
        "outputs": [
                "Vision Plan BEN4006 added for Isabella Chen; review PR5018 logged."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_10",
        "instruction": "Authorize a one-month unpaid leave for Emma Rodriguez commencing on 2025-11-01 and revise her status.",
        "actions": [
            {
                "name": "SearchEmployees",
                "arguments": {
                    "filters": {
                        "first_name": "Amelia",
                        "last_name": "Garcia"
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
                "name": "AddLeaveRecord",
                "arguments": {
                    "leave": {
                        "leave_id": "LV6102",
                        "employee_id": "E10003",
                        "leave_type": "Sabbatical",
                        "start_date": "2025-11-01",
                        "end_date": "2025-11-30",
                        "status": "Approved",
                        "notes": "One-month unpaid sabbatical approved."
                    }
                },
            },
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10003",
                    "updates": {
                        "status": "On Leave"
                    }
                },
            },
            {
                "name": "ListLeaveRecords",
                "arguments": {
                    "employee_id": "E10003"
                }
            }
        ],
        "outputs": [
                "Unpaid sabbatical LV6102 approved for Emma Rodriguez; status set to 'On Leave.'"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_11",
        "instruction": "Log a Performance Improvement Plan for Michael Park: assess PR5019 pertaining to 2025-11-01 through 2025-11-30, assigning the rating 'Needs Improvement'.",
        "actions": [
            {
                "name": "SearchEmployees",
                "arguments": {
                    "filters": {
                        "first_name": "Daniel",
                        "last_name": "Kim"
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
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR5019",
                        "employee_id": "E10002",
                        "period_start": "2025-11-01",
                        "period_end": "2025-11-30",
                        "rating": "Needs Improvement"
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
                "Performance Improvement Plan PR5019 recorded for Michael Park."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_12",
        "instruction": "Change Isabella Chen's work location to Remote \u2013 Seattle.",
        "actions": [
            {
                "name": "SearchEmployees",
                "arguments": {
                    "filters": {
                        "first_name": "Sophia",
                        "last_name": "Nguyen"
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
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10001",
                    "updates": {
                        "work_location": "Remote - Seattle"
                    }
                }
            }
        ],
        "outputs": [
                "Isabella Chen work location set to Remote - Seattle."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_13",
        "instruction": "Handle a data review on past leave for Emma Rodriguez (E10003). Her parental leave (LV6001) is finished but is still indicated as 'Scheduled'. Modify the leave record's status to 'Taken' to accurately denote its completion. Ensure her main employment status is 'Active'. For confirmation, obtain her updated leave schedule.",
        "actions": [
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
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "ListLeaveRecords",
                "arguments": {
                    "employee_id": "E10003"
                }
            }
        ],
        "outputs": [
                "\n            {\n              \"count\": 1,\n              \"results\": [\n                {\n                  \"leave_id\": \"LV6001\",\n                  \"employee_id\": \"E10003\",\n                  \"leave_type\": \"Parental\",\n                  \"start_date\": \"2024-11-01\",\n                  \"end_date\": \"2025-02-01\",\n                  \"status\": \"Taken\"\n                }\n              ]\n            }\n            "
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_14",
        "instruction": "Document holiday bonus BON3004 of USD 4,000 for Emma Rodriguez dated 2026-12-15.",
        "actions": [
            {
                "name": "SearchEmployees",
                "arguments": {
                    "filters": {
                        "first_name": "Amelia",
                        "last_name": "Garcia"
                    }
                },
            },
            {
                "name": "AddBonusPayment",
                "arguments": {
                    "bonus": {
                        "bonus_id": "BON3004",
                        "employee_id": "E10003",
                        "amount": 4000,
                        "currency": "USD",
                        "payment_date": "2026-12-15"
                    }
                },
            },
            {
                "name": "ListBonusPayments",
                "arguments": {
                    "employee_id": "E10003"
                }
            }
        ],
        "outputs": [
                "Holiday bonus BON3004 of $4,000 recorded for Emma Rodriguez."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_15",
        "instruction": "Archive the education document ED7005 (Executive MBA enrollment dated 2026-07-05) associated with Isabella Chen.",
        "actions": [
            {
                "name": "SearchEmployees",
                "arguments": {
                    "filters": {
                        "first_name": "Sophia",
                        "last_name": "Nguyen"
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
                "name": "AddEmployeeDocument",
                "arguments": {
                    "document": {
                        "doc_id": "ED7005",
                        "employee_id": "E10001",
                        "doc_type": "Education",
                        "title": "Executive MBA Enrollment",
                        "date": "2026-07-05"
                    }
                },
            },
            {
                "name": "ListEmployeeDocuments",
                "arguments": {
                    "employee_id": "E10001"
                }
            }
        ],
        "outputs": [
                "Document ED7005 stored for Isabella Chen."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_16",
        "instruction": "Elevate Michael Park to Lead Analyst (level L.3), adjust his base salary with a 10% increase effective 2026-09-01, and record the modification.",
        "actions": [
            {
                "name": "SearchEmployees",
                "arguments": {
                    "filters": {
                        "first_name": "Daniel",
                        "last_name": "Kim"
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
                        "level_id": "L.3"
                    }
                },
            },
            {
                "name": "IncreaseEmployeeCompensation",
                "arguments": {
                    "employee_id": "E10002",
                    "compensation_id": "COMP2015",
                    "effective_date": "2026-09-01",
                    "salary_increase_pct": 10
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
                "Michael Park promoted to L.3 with 10% salary increase (compensation COMP2015)."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_17",
        "instruction": "Register Emma Rodriguez IND the Vision Plan (BEN4006) to be effective right away and document the benefit modification.",
        "actions": [
            {
                "name": "SearchEmployees",
                "arguments": {
                    "filters": {
                        "first_name": "Amelia",
                        "last_name": "Garcia"
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
                    "employee_id": "E10003"
                }
            }
        ],
        "outputs": [
                "Vision Plan BEN4006 added for Emma Rodriguez."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_18",
        "instruction": "Raise Isabella Chen's equity grant by $15,000 with an effective date of 2026-08-10 and record the adjustment.",
        "actions": [
            {
                "name": "SearchEmployees",
                "arguments": {
                    "filters": {
                        "first_name": "Sophia",
                        "last_name": "Nguyen"
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
                "name": "IncreaseEmployeeCompensation",
                "arguments": {
                    "employee_id": "E10001",
                    "compensation_id": "COMP2016",
                    "effective_date": "2026-08-10",
                    "equity_increase_amount": 15000
                },
            },
            {
                "name": "GetCompensation",
                "arguments": {
                    "employee_id": "E10001"
                }
            }
        ],
        "outputs": [
                "Isabella Chen equity grant increased by $15,000 (compensation COMP2016)."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_19",
        "instruction": "Update Michael Park's work location to the San Diego Office and document the change.",
        "actions": [
            {
                "name": "SearchEmployees",
                "arguments": {
                    "filters": {
                        "first_name": "Daniel",
                        "last_name": "Kim"
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
                        "work_location": "San Diego Office"
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
                "Michael Park work location updated to San Diego Office."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_20",
        "instruction": "Log the spot bonus BON3005 IND the amount of USD 6,000 for Isabella Chen on the date 2026-09-30.",
        "actions": [
            {
                "name": "SearchEmployees",
                "arguments": {
                    "filters": {
                        "first_name": "Sophia",
                        "last_name": "Nguyen"
                    }
                },
            },
            {
                "name": "AddBonusPayment",
                "arguments": {
                    "bonus": {
                        "bonus_id": "BON3005",
                        "employee_id": "E10001",
                        "amount": 6000,
                        "currency": "USD",
                        "payment_date": "2026-09-30"
                    }
                },
            },
            {
                "name": "ListBonusPayments",
                "arguments": {
                    "employee_id": "E10001"
                }
            }
        ],
        "outputs": [
                "$6,000 spot bonus BON3005 recorded for Isabella Chen."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_21",
        "instruction": "Log the approved volunteer leave LV6106 for Michael Park, spanning from 2026-09-15 to 2026-09-19, and update his status to 'On Leave'.",
        "actions": [
            {
                "name": "SearchEmployees",
                "arguments": {
                    "filters": {
                        "first_name": "Daniel",
                        "last_name": "Kim"
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
                "name": "AddLeaveRecord",
                "arguments": {
                    "leave": {
                        "leave_id": "LV6106",
                        "employee_id": "E10002",
                        "leave_type": "Volunteer Leave",
                        "start_date": "2026-09-15",
                        "end_date": "2026-09-19",
                        "status": "Approved"
                    }
                },
            },
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10002",
                    "updates": {
                        "status": "On Leave"
                    }
                },
            },
            {
                "name": "ListLeaveRecords",
                "arguments": {
                    "employee_id": "E10002"
                }
            }
        ],
        "outputs": [
                "Volunteer leave LV6106 recorded; Michael Park status set to 'On Leave'."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_22",
        "instruction": "Adjust Michael Park's equity grant by adding $10,000 to the compensation record COMP5003 as of 2026-01-15, then show the revised compensation history.",
        "actions": [
            {
                "name": "IncreaseEmployeeCompensation",
                "arguments": {
                    "employee_id": "E10002",
                    "compensation_id": "COMP5003",
                    "effective_date": "2026-01-15",
                    "equity_increase_amount": 10000
                },
            },
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10002",
                    "updates": {
                        "performance_review_ids": [
                            "PR5002",
                            "PR8003"
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
                "Compensation history includes new record COMP5003 with +$10,000 equity."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_23",
        "instruction": "File certification document ED7006 (AWS Solutions Architect, 2026-09-22) on behalf of Emma Rodriguez.",
        "actions": [
            {
                "name": "SearchEmployees",
                "arguments": {
                    "filters": {
                        "first_name": "Amelia",
                        "last_name": "Garcia"
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
                "name": "AddEmployeeDocument",
                "arguments": {
                    "document": {
                        "doc_id": "ED7006",
                        "employee_id": "E10003",
                        "doc_type": "Certification",
                        "title": "AWS Solutions Architect",
                        "date": "2026-09-22"
                    }
                },
            },
            {
                "name": "ListEmployeeDocuments",
                "arguments": {
                    "employee_id": "E10003"
                }
            }
        ],
        "outputs": [
                "Document ED7006 stored for Emma Rodriguez."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_24",
        "instruction": "Generate compensation record COMP2017 for Michael Park, incorporating a bonus target of 17% effective from 2026-10-01.",
        "actions": [
            {
                "name": "SearchEmployees",
                "arguments": {
                    "filters": {
                        "first_name": "Daniel",
                        "last_name": "Kim"
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
                "name": "SetCompensation",
                "arguments": {
                    "compensation": {
                        "compensation_id": "COMP2017",
                        "employee_id": "E10002",
                        "base_salary": 210000,
                        "currency": "USD",
                        "bonus_target_pct": 17,
                        "equity_grant": 40000,
                        "effective_date": "2026-10-01"
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
                "Michael Park bonus target set to 17 % (compensation COMP2017)."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_25",
        "instruction": "Document Q2-2026 performance review PR5050 (rating 'Exceeds') for Emma Rodriguez.",
        "actions": [
            {
                "name": "SearchEmployees",
                "arguments": {
                    "filters": {
                        "first_name": "Amelia",
                        "last_name": "Garcia"
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
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR5050",
                        "employee_id": "E10003",
                        "period_start": "2026-04-01",
                        "period_end": "2026-06-30",
                        "rating": "Exceeds",
                        "manager_id": "E10001"
                    }
                },
            },
            {
                "name": "ListPerformanceReviews",
                "arguments": {
                    "employee_id": "E10003"
                }
            }
        ],
        "outputs": [
                "Q2 2026 review PR5050 recorded for Emma Rodriguez."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_26",
        "instruction": "Should Olivia Martinez's salary be under 75,000 EUR or her bonus target be less than 8 %, implement compensation record COMP2018 (salary 78 000 EUR, bonus 10 %) starting from 2025-07-15 and display the revised compensation.",
        "actions": [
            {
                "name": "SearchEmployees",
                "arguments": {
                    "filters": {
                        "first_name": "Elena",
                        "last_name": "Rodriguez"
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
                "name": "GetCompensation",
                "arguments": {
                    "employee_id": "E10005"
                },
            },
            {
                "name": "ConditionalCompensationCheckAndUpdate",
                "arguments": {
                    "employee_id": "E10005",
                    "compensation_id": "COMP2018",
                    "effective_date": "2025-07-15",
                    "salary_threshold": 75000,
                    "target_salary": 78000,
                    "bonus_threshold": 8,
                    "target_bonus": 10
                },
            },
            {
                "name": "ListPerformanceReviews",
                "arguments": {
                    "employee_id": "E10005"
                },
            },
            {
                "name": "GetCompensation",
                "arguments": {
                    "employee_id": "E10005"
                }
            }
        ],
        "outputs": [
                "Compensation updated for Olivia Martinez if thresholds met (see COMP2018)."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_27",
        "instruction": "Handle the approval of William Liu's sabbatical LV6107 from 2025-08-01 to 2025-08-21, approve any outstanding leaves, change status to 'On Leave', and save approval document ED7007.",
        "actions": [
            {
                "name": "SearchEmployees",
                "arguments": {
                    "filters": {
                        "first_name": "Marcus",
                        "last_name": "Chen"
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
                "name": "ListLeaveRecords",
                "arguments": {
                    "employee_id": "E10006"
                },
            },
            {
                "name": "UpdateLeaveRecordsByStatus",
                "arguments": {
                    "employee_id": "E10006",
                    "current_status": "Pending",
                    "new_status": "Approved"
                },
            },
            {
                "name": "AddLeaveRecord",
                "arguments": {
                    "leave": {
                        "leave_id": "LV6107",
                        "employee_id": "E10006",
                        "leave_type": "Sabbatical",
                        "start_date": "2025-08-01",
                        "end_date": "2025-08-21",
                        "status": "Approved"
                    }
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
                        "doc_id": "ED7007",
                        "employee_id": "E10006",
                        "doc_type": "Leave",
                        "title": "Sabbatical Approval",
                        "date": "2025-07-20"
                    }
                },
            },
            {
                "name": "ListEmployeeDocuments",
                "arguments": {
                    "employee_id": "E10006"
                },
            },
            {
                "name": "ListLeaveRecords",
                "arguments": {
                    "employee_id": "E10006"
                }
            }
        ],
        "outputs": [
                "William Liu sabbatical LV6107 recorded; status On Leave; doc ED7007 stored."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_28",
        "instruction": "Move Arjun Patel to Finance (DEPT1004) under manager E10011; if the latest rating is 'Exceeds', elevate level to L.3; incorporate benefit BEN4005.",
        "actions": [
            {
                "name": "SearchEmployees",
                "arguments": {
                    "filters": {
                        "first_name": "Rahul",
                        "last_name": "Singh"
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
                "name": "ListPerformanceReviews",
                "arguments": {
                    "employee_id": "E10004"
                },
            },
            {
                "name": "GetDepartment",
                "arguments": {
                    "department_id": "DEPT1004"
                },
            },
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10004",
                    "updates": {
                        "department_id": "DEPT1004",
                        "manager_id": "E10011"
                    }
                },
            },
            {
                "name": "ConditionalLevelUpdate",
                "arguments": {
                    "employee_id": "E10004",
                    "required_rating": "Exceeds",
                    "new_level": "L.3"
                },
            },
            {
                "name": "SetEmployeeBenefits",
                "arguments": {
                    "employee_id": "E10004",
                    "benefit_plan_ids": [
                        "BEN4001",
                        "BEN4003",
                        "BEN4005"
                    ]
                },
            },
            {
                "name": "GetEmployee",
                "arguments": {
                    "employee_id": "E10004"
                },
            },
            {
                "name": "ListPerformanceReviews",
                "arguments": {
                    "employee_id": "E10004"
                }
            }
        ],
        "outputs": [
                "Arjun Patel transferred to Finance; level updated if eligible; benefit BEN4005 added."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_29",
        "instruction": "Log the Q2-2025 review PR5053 (rating 'Exceeds') for Emma Rodriguez; should the bonus target be less than 18 %, adjust it to 20 % using COMP2019 and provide a $5 500 bonus through BON3006.",
        "actions": [
            {
                "name": "SearchEmployees",
                "arguments": {
                    "filters": {
                        "first_name": "Amelia",
                        "last_name": "Garcia"
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
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR5053",
                        "employee_id": "E10003",
                        "period_start": "2025-04-01",
                        "period_end": "2025-06-30",
                        "rating": "Exceeds",
                        "manager_id": "E10001",
                        "summary": "Outstanding Q2 performance with significant contributions to platform improvements."
                    }
                },
            },
            {
                "name": "ConditionalCompensationIncrease",
                "arguments": {
                    "employee_id": "E10003",
                    "compensation_id": "COMP2019",
                    "effective_date": "2025-07-25",
                    "condition": "bonus_target_pct < 18",
                    "new_bonus_target_pct": 20
                },
            },
            {
                "name": "AddBonusPayment",
                "arguments": {
                    "bonus": {
                        "bonus_id": "BON3006",
                        "employee_id": "E10003",
                        "amount": 5500,
                        "currency": "USD",
                        "payment_date": "2025-07-25",
                        "reason": "Q2 2025 performance bonus for exceeding targets."
                    }
                },
            },
            {
                "name": "ListPerformanceReviews",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "ListBonusPayments",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "GetCompensation",
                "arguments": {
                    "employee_id": "E10003"
                }
            }
        ],
        "outputs": [
                "PR5053 recorded; bonus target conditionally set to 20 %; bonus BON3006 awarded."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_30",
        "instruction": "Restore Michael Park's status to Active, verify benefits encompass BEN4006, retain medical clearance ED7008, and affirm up-to-date compensation.",
        "actions": [
            {
                "name": "SearchEmployees",
                "arguments": {
                    "filters": {
                        "first_name": "Daniel",
                        "last_name": "Kim"
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
                "name": "ListLeaveRecords",
                "arguments": {
                    "employee_id": "E10002"
                },
            },
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10002",
                    "updates": {
                        "status": "Active"
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
                        "BEN4003",
                        "BEN4006"
                    ]
                },
            },
            {
                "name": "AddEmployeeDocument",
                "arguments": {
                    "document": {
                        "doc_id": "ED7008",
                        "employee_id": "E10002",
                        "doc_type": "Medical",
                        "title": "Return to Work Clearance",
                        "date": "2025-07-30",
                        "notes": "Medical clearance for return to active duty after leave period."
                    }
                },
            },
            {
                "name": "GetCompensation",
                "arguments": {
                    "employee_id": "E10002"
                },
            },
            {
                "name": "ListEmployeeDocuments",
                "arguments": {
                    "employee_id": "E10002"
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
                "Michael Park onboarding complete: status Active, benefits restored, medical doc ED7008 stored."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_31",
        "instruction": "Handle Olivia Martinez's promotion to Senior Financial Analyst (L.2), boosting her base salary by 15% effective 2025-08-01, allocating 5,000 EUR IND equity to her, and enroll her IND the 401(k) plan if it's currently not part of her benefits. Make sure the promotion is documented.",
        "actions": [
            {
                "name": "SearchEmployees",
                "arguments": {
                    "filters": {
                        "first_name": "Elena",
                        "last_name": "Rodriguez"
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
                        "level_id": "L.2"
                    }
                },
            },
            {
                "name": "SetCompensation",
                "arguments": {
                    "compensation": {
                        "compensation_id": "COMP2005",
                        "employee_id": "E10005",
                        "base_salary": 135700,
                        "currency": "USD",
                        "bonus_target_pct": 10,
                        "equity_grant": 5000,
                        "effective_date": "2025-08-01"
                    }
                },
            },
            {
                "name": "AddEmployeeBenefitIfMissing",
                "arguments": {
                    "employee_id": "E10005",
                    "benefit_plan_id": "BEN4003",
                    "current_benefit_plan_ids": [
                        "BEN4001",
                        "BEN4005"
                    ]
                },
            },
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
                }
            }
        ],
        "outputs": [
                "Olivia Martinez promoted, compensation COMP20250801 added, 401(k) benefit ensured."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_32",
        "instruction": "Attend to Isabella Chen's request for 4 weeks of unpaid personal leave (LV6108) stretching from 2025-09-01 to 2025-09-28. Should her current equity grant exceed 70,000, ensure her benefits are sustained during leave. Adjust status as necessary and submit leave documentation.",
        "actions": [
            {
                "name": "SearchEmployees",
                "arguments": {
                    "filters": {
                        "first_name": "Sophia",
                        "last_name": "Nguyen"
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
                "name": "ListLeaveRecords",
                "arguments": {
                    "employee_id": "E10001"
                },
            },
            {
                "name": "ConditionalBenefitMaintenance",
                "arguments": {
                    "employee_id": "E10001",
                    "equity_threshold": 70000,
                    "maintain_benefits": [
                        "BEN4001",
                        "BEN4002",
                        "BEN4003",
                        "BEN4006"
                    ],
                    "reduced_benefits": [
                        "BEN4001"
                    ]
                },
            },
            {
                "name": "AddLeaveRecord",
                "arguments": {
                    "leave": {
                        "leave_id": "LV6108",
                        "employee_id": "E10001",
                        "leave_type": "Personal Leave",
                        "start_date": "2025-09-01",
                        "end_date": "2025-09-28",
                        "status": "Approved",
                        "notes": "4-week unpaid personal leave with conditional benefit maintenance based on equity level."
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
                "name": "AddEmployeeDocument",
                "arguments": {
                    "document": {
                        "doc_id": "ED7009",
                        "employee_id": "E10001",
                        "doc_type": "Leave",
                        "title": "Personal Leave Authorization",
                        "date": "2025-08-15"
                    }
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR5056",
                        "employee_id": "E10001",
                        "period_start": "2025-09-01",
                        "period_end": "2025-09-28",
                        "rating": "N/A",
                        "manager_id": "N/A",
                        "summary": "Personal leave approved with conditional benefit maintenance based on equity level analysis."
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
                "name": "ListLeaveRecords",
                "arguments": {
                    "employee_id": "E10001"
                }
            }
        ],
        "outputs": [
                "Personal leave LV6108 recorded for Isabella Chen; benefits adjusted per equity threshold; doc ED7009 stored."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_33",
        "instruction": "Initiate the termination process for William Liu, set to begin on 2025-09-15. Compute the final compensation, remove all active benefits excluding Legal Insurance, upload the termination documents, and if there is any pending leave, ensure it is marked as cancelled.",
        "actions": [
            {
                "name": "SearchEmployees",
                "arguments": {
                    "filters": {
                        "first_name": "Marcus",
                        "last_name": "Chen"
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
                "name": "GetCompensation",
                "arguments": {
                    "employee_id": "E10006"
                },
            },
            {
                "name": "ListLeaveRecords",
                "arguments": {
                    "employee_id": "E10006"
                },
            },
            {
                "name": "UpdateLeaveRecordsByStatus",
                "arguments": {
                    "employee_id": "E10006",
                    "current_status": "Pending",
                    "new_status": "Cancelled"
                },
            },
            {
                "name": "AddBonusPayment",
                "arguments": {
                    "bonus": {
                        "bonus_id": "BON3010",
                        "employee_id": "E10006",
                        "amount": 2500,
                        "currency": "EUR",
                        "payment_date": "2025-09-15"
                    }
                },
            },
            {
                "name": "TerminateEmployee",
                "arguments": {
                    "employee_id": "E10006",
                    "termination_date": "2025-09-15"
                },
            },
            {
                "name": "SetEmployeeBenefits",
                "arguments": {
                    "employee_id": "E10006",
                    "benefit_plan_ids": [
                        "BEN9999"
                    ]
                },
            },
            {
                "name": "AddEmployeeDocument",
                "arguments": {
                    "document": {
                        "doc_id": "ED7010",
                        "employee_id": "E10006",
                        "doc_type": "Termination",
                        "title": "Termination Notice",
                        "date": "2025-09-15",
                        "notes": "Voluntary termination with final compensation calculated and benefits transition completed."
                    }
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR5057",
                        "employee_id": "E10006",
                        "period_start": "2025-09-15",
                        "period_end": "2025-09-15",
                        "rating": "N/A",
                        "manager_id": "E10012",
                        "summary": "Termination processed with final compensation payout and benefit adjustments, pending leave cancelled."
                    }
                },
            },
            {
                "name": "ListEmployeeDocuments",
                "arguments": {
                    "employee_id": "E10006"
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
                "William Liu termination processed; leave cancelled; bonus BON3010 paid; benefits set to Legal Insurance; doc ED7010 stored."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_34",
        "instruction": "Delegate Arjun Patel to a 6-month cross-functional project IND collaboration with Marketing (temporary assignment). Verify his current department, temporarily assign his manager to E10013, incorporate a project assignment review, and if his bonus target is currently under 12%, adjust it to 15%.",
        "actions": [
            {
                "name": "SearchEmployees",
                "arguments": {
                    "filters": {
                        "first_name": "Rahul",
                        "last_name": "Singh"
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
                "name": "GetDepartment",
                "arguments": {
                    "department_id": "DEPT1005"
                },
            },
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10004",
                    "updates": {
                        "manager_id": "E10013",
                        "notes": "Temporary assignment to Marketing cross-functional project for 6 months."
                    }
                },
            },
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10004",
                    "updates": {
                        "manager_id": "E10013"
                    }
                },
            },
            {
                "name": "ConditionalCompensationIncrease",
                "arguments": {
                    "employee_id": "E10004",
                    "compensation_id": "COMP2021",
                    "effective_date": "2025-08-01",
                    "condition": "bonus_target_pct < 12",
                    "new_bonus_target_pct": 15
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR5058",
                        "employee_id": "E10004",
                        "period_start": "2025-08-01",
                        "period_end": "2026-01-31",
                        "rating": "N/A",
                        "manager_id": "E10013",
                        "summary": "Assigned to 6-month cross-functional Marketing project with bonus target increased to 15%."
                    }
                },
            },
            {
                "name": "AddEmployeeDocument",
                "arguments": {
                    "document": {
                        "doc_id": "ED7011",
                        "employee_id": "E10004",
                        "doc_type": "Assignment",
                        "title": "Cross-functional Project Assignment",
                        "date": "2025-08-01",
                        "notes": "6-month temporary assignment to Marketing department for strategic initiative."
                    }
                },
            },
            {
                "name": "ListPerformanceReviews",
                "arguments": {
                    "employee_id": "E10004"
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
                "Arjun Patel assigned to Marketing project; bonus target adjusted via COMP2021; doc ED7011 stored."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_35",
        "instruction": "Authorize Emma Rodriguez's 2-month research sabbatical (LV6109) from 2025-10-01 to 2025-11-30. If she holds a current level of L.3 or above, ensure her full compensation remains intact during the sabbatical. Upload the sabbatical agreement and update her status as necessary.",
        "actions": [
            {
                "name": "SearchEmployees",
                "arguments": {
                    "filters": {
                        "first_name": "Amelia",
                        "last_name": "Garcia"
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
                "name": "ListLeaveRecords",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "ConditionalSabbaticalCompensation",
                "arguments": {
                    "employee_id": "E10003",
                    "level_threshold": "L.3",
                    "paid_leave_type": "Research Sabbatical - Paid",
                    "unpaid_leave_type": "Research Sabbatical - Unpaid"
                },
            },
            {
                "name": "AddLeaveRecord",
                "arguments": {
                    "leave": {
                        "leave_id": "LV6109",
                        "employee_id": "E10003",
                        "leave_type": "Research Sabbatical",
                        "start_date": "2025-10-01",
                        "end_date": "2025-11-30",
                        "status": "Approved",
                        "notes": "2-month research sabbatical with conditional compensation based on level L.3+ threshold."
                    }
                },
            },
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10003",
                    "updates": {
                        "status": "On Sabbatical"
                    }
                },
            },
            {
                "name": "AddEmployeeDocument",
                "arguments": {
                    "document": {
                        "doc_id": "ED7012",
                        "employee_id": "E10003",
                        "doc_type": "Agreement",
                        "title": "Research Sabbatical Agreement",
                        "date": "2025-09-15"
                    }
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR5059",
                        "employee_id": "E10003",
                        "period_start": "2025-10-01",
                        "period_end": "2025-11-30",
                        "rating": "N/A",
                        "manager_id": "E10001",
                        "summary": "Research sabbatical approved with compensation maintenance."
                    }
                },
            },
            {
                "name": "ListEmployeeDocuments",
                "arguments": {
                    "employee_id": "E10003"
                },
            },
            {
                "name": "ListLeaveRecords",
                "arguments": {
                    "employee_id": "E10003"
                }
            }
        ],
        "outputs": [
                "Emma Rodriguez research sabbatical LV6109 recorded; compensation maintained; doc ED7012 stored."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_36",
        "instruction": "Establish a Performance Improvement Plan for Michael Park beginning 2025-08-15. Develop a 90-day PIP review, temporarily lower his bonus target to 20%, upload the PIP documentation, and plan follow-up milestone reviews at the 30 and 60-day marks.",
        "actions": [
            {
                "name": "SearchEmployees",
                "arguments": {
                    "filters": {
                        "first_name": "Daniel",
                        "last_name": "Kim"
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
                "name": "SetCompensation",
                "arguments": {
                    "compensation": {
                        "compensation_id": "COMP2022",
                        "employee_id": "E10002",
                        "base_salary": 210000,
                        "currency": "USD",
                        "bonus_target_pct": 20,
                        "equity_grant": 40000,
                        "effective_date": "2025-08-15"
                    }
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR5060",
                        "employee_id": "E10002",
                        "period_start": "2025-08-15",
                        "period_end": "2025-11-15",
                        "rating": "Needs Improvement"
                    }
                },
            },
            {
                "name": "AddEmployeeDocument",
                "arguments": {
                    "document": {
                        "doc_id": "ED7013",
                        "employee_id": "E10002",
                        "doc_type": "PIP",
                        "title": "Performance Improvement Plan",
                        "date": "2025-08-15"
                    }
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR5061",
                        "employee_id": "E10002",
                        "period_start": "2025-09-15",
                        "period_end": "2025-09-15",
                        "rating": "Pending",
                        "manager_id": "E10012",
                        "summary": "30-day PIP milestone review - progress assessment scheduled."
                    }
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR5062",
                        "employee_id": "E10002",
                        "period_start": "2025-10-15",
                        "period_end": "2025-10-15",
                        "rating": "Pending",
                        "manager_id": "E10012",
                        "summary": "60-day PIP milestone review - mid-point evaluation scheduled."
                    }
                },
            },
            {
                "name": "ListPerformanceReviews",
                "arguments": {
                    "employee_id": "E10002"
                },
            },
            {
                "name": "ListEmployeeDocuments",
                "arguments": {
                    "employee_id": "E10002"
                }
            }
        ],
        "outputs": [
                "Michael Park PIP initiated; bonus target set to 20 %; doc ED7013 stored."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_37",
        "instruction": "Handle the transfer of Olivia Martinez from the Barcelona Office to the Manchester Office starting from 2025-09-01. Modify her work location, verify the need for any EU Commuter Stipend changes, apply a $3,000 relocation bonus, and submit the relocation documentation.",
        "actions": [
            {
                "name": "SearchEmployees",
                "arguments": {
                    "filters": {
                        "first_name": "Elena",
                        "last_name": "Rodriguez"
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
                        "work_location": "Manchester Office"
                    }
                },
            },
            {
                "name": "SetEmployeeBenefits",
                "arguments": {
                    "employee_id": "E10005",
                    "benefit_plan_ids": [
                        "BEN4001",
                        "BEN4003",
                        "BEN4005"
                    ]
                },
            },
            {
                "name": "AddBonusPayment",
                "arguments": {
                    "bonus": {
                        "bonus_id": "BON3007",
                        "employee_id": "E10005",
                        "amount": 3000,
                        "currency": "EUR",
                        "payment_date": "2025-09-01"
                    }
                },
            },
            {
                "name": "AddEmployeeDocument",
                "arguments": {
                    "document": {
                        "doc_id": "ED7014",
                        "employee_id": "E10005",
                        "doc_type": "Relocation",
                        "title": "Office Relocation Authorization",
                        "date": "2025-08-20"
                    }
                },
            },
            {
                "name": "ListBonusPayments",
                "arguments": {
                    "employee_id": "E10005"
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
                "Olivia Martinez relocated to Manchester Office; bonus BON3007 paid; doc ED7014 stored."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_38",
        "instruction": "Examine Isabella Chen's equity position, and if it is currently below 80,000, increase it by 10,000, effective on 2025-08-30. Additionally, review her 2024 performance evaluations and if marked as 'Exceeds', grant a $12,000 leadership bonus.",
        "actions": [
            {
                "name": "SearchEmployees",
                "arguments": {
                    "filters": {
                        "first_name": "Sophia",
                        "last_name": "Nguyen"
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
                "name": "ListPerformanceReviews",
                "arguments": {
                    "employee_id": "E10001"
                },
            },
            {
                "name": "IncreaseEmployeeCompensation",
                "arguments": {
                    "employee_id": "E10001",
                    "compensation_id": "COMP2023",
                    "effective_date": "2025-08-30",
                    "equity_increase_amount": 10000
                },
            },
            {
                "name": "AddBonusPayment",
                "arguments": {
                    "bonus": {
                        "bonus_id": "BON3008",
                        "employee_id": "E10001",
                        "amount": 12000,
                        "currency": "USD",
                        "payment_date": "2025-08-30"
                    }
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR5064",
                        "employee_id": "E10001",
                        "period_start": "2025-08-30",
                        "period_end": "2025-08-30",
                        "rating": "N/A"
                    }
                },
            },
            {
                "name": "ListBonusPayments",
                "arguments": {
                    "employee_id": "E10001"
                },
            },
            {
                "name": "GetCompensation",
                "arguments": {
                    "employee_id": "E10001"
                }
            }
        ],
        "outputs": [
                "Isabella Chen equity increased; leadership bonus BON3008 awarded; review PR5064 recorded."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_39",
        "instruction": "Handle the process for emergency family leave for Arjun Patel (LV6110) from 2025-07-10 to 2025-07-24. Set the status as 'Emergency Leave', keep all benefits intact, upload the necessary emergency documentation, and IND case he has project duties, inform the temporary cover personnel.",
        "actions": [
            {
                "name": "SearchEmployees",
                "arguments": {
                    "filters": {
                        "first_name": "Rahul",
                        "last_name": "Singh"
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
                "name": "ListLeaveRecords",
                "arguments": {
                    "employee_id": "E10004"
                },
            },
            {
                "name": "AddLeaveRecord",
                "arguments": {
                    "leave": {
                        "leave_id": "LV6110",
                        "employee_id": "E10004",
                        "leave_type": "Emergency Family Leave",
                        "start_date": "2025-07-10",
                        "end_date": "2025-07-24",
                        "status": "Approved",
                        "notes": "Emergency family leave with full benefits maintained and project coverage arranged."
                    }
                },
            },
            {
                "name": "UpdateEmployee",
                "arguments": {
                    "employee_id": "E10004",
                    "updates": {
                        "status": "Emergency Leave"
                    }
                },
            },
            {
                "name": "AddEmployeeDocument",
                "arguments": {
                    "document": {
                        "doc_id": "ED7015",
                        "employee_id": "E10004",
                        "doc_type": "Emergency Leave",
                        "title": "Emergency Family Leave Authorization",
                        "date": "2025-07-10"
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
                "name": "ListLeaveRecords",
                "arguments": {
                    "employee_id": "E10004"
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
                "Arjun Patel emergency leave LV6110 recorded; status set; doc ED7015 stored."
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_40",
        "instruction": "Coordinate the completion of the annual review cycle for William Liu. If his status reads 'Active', prepare his 2025 annual review with a 'Meets' rating, verify whether his bonus target needs adjustment according to the L.4 level defaults, and grant a year-end bonus of $4,200.",
        "actions": [
            {
                "name": "SearchEmployees",
                "arguments": {
                    "filters": {
                        "first_name": "Marcus",
                        "last_name": "Chen"
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
                "name": "GetCompensation",
                "arguments": {
                    "employee_id": "E10006"
                },
            },
            {
                "name": "ListPerformanceReviews",
                "arguments": {
                    "employee_id": "E10006"
                },
            },
            {
                "name": "AddPerformanceReview",
                "arguments": {
                    "review": {
                        "review_id": "PR5066",
                        "employee_id": "E10006",
                        "period_start": "2025-01-01",
                        "period_end": "2025-12-31",
                        "rating": "Meets"
                    }
                },
            },
            {
                "name": "ConditionalBonusTargetNormalization",
                "arguments": {
                    "employee_id": "E10006",
                    "compensation_id": "COMP2024",
                    "effective_date": "2025-12-31",
                    "target_bonus_pct": 15
                },
            },
            {
                "name": "AddBonusPayment",
                "arguments": {
                    "bonus": {
                        "bonus_id": "BON3009",
                        "employee_id": "E10006",
                        "amount": 4200,
                        "currency": "EUR",
                        "payment_date": "2025-12-31"
                    }
                },
            },
            {
                "name": "ListPerformanceReviews",
                "arguments": {
                    "employee_id": "E10006"
                },
            },
            {
                "name": "ListBonusPayments",
                "arguments": {
                    "employee_id": "E10006"
                },
            },
            {
                "name": "GetCompensation",
                "arguments": {
                    "employee_id": "E10006"
                }
            }
        ],
        "outputs": [
                "William Liu annual review PR5066 recorded; bonus target normalized if needed; year-end bonus BON3009 awarded."
        ]
    }
]
