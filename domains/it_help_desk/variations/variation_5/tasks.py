# Copyright Sierra

tasks = [
    {
        "annotator": 0,
        "user_id": "onboarding_1",
        "instruction": "HR dispatched memos regarding two upcoming new hires, Briar Campbell and Casey Liu. You will need to allocate the default licenses from rbac_group_map for their respective positions to initiate their work if those aren't already assigned. They should also be provided with CodeHub Enterprise licenses. Should they lack employee accounts and mailboxes, those need to be established. Document these updates in lifecycle_queue. Notify me if it's necessary to generate employee accounts and mailboxes.",
        "actions": [
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Drew",
                    "last_name": "Nelson"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Jordan",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "employeeAccountExists",
                "arguments": {
                    "first_name": "Drew",
                    "last_name": "Nelson"
                },
            },
            {
                "name": "employeeAccountExists",
                "arguments": {
                    "first_name": "Jordan",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "mailboxExists",
                "arguments": {
                    "employee_id": "emp_0039"
                },
            },
            {
                "name": "mailboxExists",
                "arguments": {
                    "employee_id": "emp_0002"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0039"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0002"
                },
            },
            {
                "name": "filterHrMemos",
                "arguments": {
                    "first_name": "Drew",
                    "last_name": "Nelson"
                },
            },
            {
                "name": "filterHrMemos",
                "arguments": {
                    "first_name": "Jordan",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "getJobLicenses",
                "arguments": {
                    "job_title": "Support Manager"
                },
            },
            {
                "name": "getJobLicenses",
                "arguments": {
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "getLicenseInfo",
                "arguments": {
                    "license_name": "CodeHub Enterprise"
                },
            },
            {
                "name": "getLicenseAvailability",
                "arguments": {
                    "license_id": "lic_github_ent"
                },
            },
            {
                "name": "assignLicenses",
                "arguments": {
                    "employee_id": "emp_0039",
                    "license_ids": [
                        "lic_github_ent"
                    ]
                },
            },
            {
                "name": "getLicenseAvailability",
                "arguments": {
                    "license_id": "lic_github_ent"
                },
            },
            {
                "name": "assignLicenses",
                "arguments": {
                    "employee_id": "emp_0002",
                    "license_ids": [
                        "lic_github_ent"
                    ]
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0039",
                    "memo_id": "memo_0008",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0002",
                    "memo_id": "memo_0007",
                    "event": "onboarding"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "license_allocation_1",
        "instruction": "You are an AI agent responsible for automating the allocation of software licenses. Refer to license_inventory and employees to detect users with impending software renewals, marked by the last audit being over 30 days old. Verify active usage of the identified licenses and refresh license_inventory with the new audit. Produce a CSV listing underutilized licenses (utilization_rate < 30%). Initiate low-priority TaskTrack tickets for \"Manage license utilization for license_id\" for every underutilized license.",
        "actions": [
            {
                "name": "licenseRequiresRenewal",
                "arguments": {
                    "num_days": 30
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_m365_e3",
                    "status": "active"
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_m365_e5",
                    "status": "active"
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_adobe_cc",
                    "status": "active"
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_github_ent",
                    "status": "active"
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_slack_ent",
                    "status": "active"
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_salesforce",
                    "status": "active"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_m365_e3"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_m365_e5"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_adobe_cc"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_github_ent"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_slack_ent"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_salesforce"
                },
            },
            {
                "name": "filterLicenses",
                "arguments": {
                    "utilization": 0.3
                },
            },
            {
                "name": "exportUnderutilizedLicenses",
                "arguments": {
                    "output_data": [
                        "lic_m365_e5",
                        "lic_adobe_cc",
                        "lic_github_ent",
                        "lic_salesforce"
                    ]
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "License Allocation",
                    "summary": "Manage license utilization for lic_m365_e5",
                    "priority": "P3"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "License Allocation",
                    "summary": "Manage license utilization for lic_adobe_cc",
                    "priority": "P3"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "License Allocation",
                    "summary": "Manage license utilization for lic_github_ent",
                    "priority": "P3"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "License Allocation",
                    "summary": "Manage license utilization for lic_salesforce",
                    "priority": "P3"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "employee_offboarding_1",
        "instruction": "As an AI agent automating employee offboarding, utilize hr_memos and employees to identify staff designated as \"offboarding.\" Coordinate the execution of the essential offboarding processes, such as disabling their accounts, revoking licenses, archiving mailboxes, and wiping devices assigned in it_assets. Document these finished tasks in lifecycle_queue, and inform management about the offboarding of each employee.",
        "actions": [
            {
                "name": "filterHrMemos",
                "arguments": {
                    "type": "offboarding"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Parker",
                    "last_name": "Davis"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Remy",
                    "last_name": "White"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0007",
                    "status": "disabled"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0019",
                    "status": "disabled"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0007"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0019"
                },
            },
            {
                "name": "archiveMailbox",
                "arguments": {
                    "employee_id": "emp_0007",
                    "department": "IT"
                },
            },
            {
                "name": "archiveMailbox",
                "arguments": {
                    "employee_id": "emp_0019",
                    "department": "Operations"
                },
            },
            {
                "name": "deviceAssignment",
                "arguments": {
                    "employee_id": "emp_0007",
                    "unassign": true
                },
            },
            {
                "name": "deviceAssignment",
                "arguments": {
                    "employee_id": "emp_0019",
                    "unassign": true
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0007",
                    "memo_id": "memo_0009",
                    "event": "offboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0019",
                    "memo_id": "memo_0012",
                    "event": "offboarding"
                },
            },
            {
                "name": "filterEmployees",
                "arguments": {
                    "manager_id": "None"
                },
            },
            {
                "name": "notify",
                "arguments": {
                    "recipient_ids": [
                        "emp_0001",
                        "emp_0002",
                        "emp_0003",
                        "emp_0004",
                        "emp_0005",
                        "emp_0006",
                        "emp_0009",
                        "emp_0017"
                    ],
                    "summary": "Jordan Kim was offboarded."
                },
            },
            {
                "name": "notify",
                "arguments": {
                    "recipient_ids": [
                        "emp_0001",
                        "emp_0002",
                        "emp_0003",
                        "emp_0004",
                        "emp_0005",
                        "emp_0006",
                        "emp_0009",
                        "emp_0017"
                    ],
                    "summary": "Sawyer Harris was offboarded."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "compliance_check_1",
        "instruction": "As an AI agent for quarterly compliance checks, use license_assignments, rbac_group_map, and employees to compare assigned roles in the Marketing department with default licenses in rbac_group_map. Identify and flag anomalies, particularly employees lacking default licenses. Create a review packet in PDF format and log the results in validation_issues.",
        "actions": [
            {
                "name": "filterEmployees",
                "arguments": {
                    "department": "Marketing"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0002",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0012",
                    "job_title": "Design Lead"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0016",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0018",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0021",
                    "job_title": "Design Lead"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0024",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0025",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0027",
                    "job_title": "Growth Marketer"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0031",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0032",
                    "job_title": "Growth Marketer"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0034",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0041",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "generateReviewAndLog",
                "arguments": {
                    "log_data": "emp_0002 is missing no licenses,emp_0012 is missing no licenses, emp_0016 is missing no licenses, emp_0018 is missing no licenses, emp_0021 is missing no licenses, emp_0024 is missing no licenses, emp_0025 is missing no licenses, emp_0027 is missing no licenses, emp_0031 is missing no licenses, emp_0032 is missing no licenses, emp_0034 is missing no licenses, emp_0041 is missing no licenses"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "track_backlog_1",
        "instruction": "As an AI agent responsible for monitoring project backlog, utilize the backlog_snapshot_open database to craft a report highlighting tickets that are not marked \"Resolved\". Ensure to save the report with these results. Initiate TaskTrack tickets for any unresolved urgent tickets with the summary \"Address ticket_id\".",
        "actions": [
            {
                "name": "getTicketsBacklog",
                "arguments": {
                {}
                },
            },
            {
                "name": "filterTickets",
                "arguments": {
                    "ids": [
                        "T5002",
                        "T5003",
                        "T5004",
                        "T5005",
                        "T5006",
                        "T5009",
                        "T5010",
                        "T5011",
                        "T5012",
                        "T5013",
                        "T5014",
                        "T5016",
                        "T5017",
                        "T5020",
                        "T5021",
                        "T5023",
                        "T5024",
                        "T5025",
                        "T5026",
                        "T5027",
                        "T5028",
                        "T5029",
                        "T5030",
                        "T5031",
                        "T5032",
                        "T5035",
                        "T5036",
                        "T5037",
                        "T5039",
                        "T5042",
                        "T5043",
                        "T5044",
                        "T5046",
                        "T5048",
                        "T5049",
                        "T5050",
                        "T5051",
                        "T5053",
                        "T5054",
                        "T5055",
                        "T5056",
                        "T5058",
                        "T5059",
                        "T5060",
                        "T5061",
                        "T5063"
                    ],
                    "not_status": "Resolved"
                },
            },
            {
                "name": "saveReport",
                "arguments": {
                    "save_data": [
                        "T5002",
                        "T5003",
                        "T5004",
                        "T5005",
                        "T5006",
                        "T5009",
                        "T5010",
                        "T5011",
                        "T5012",
                        "T5013",
                        "T5014",
                        "T5016",
                        "T5017",
                        "T5020",
                        "T5021",
                        "T5023",
                        "T5024",
                        "T5025",
                        "T5026",
                        "T5027",
                        "T5028",
                        "T5029",
                        "T5030",
                        "T5031",
                        "T5032",
                        "T5035",
                        "T5036",
                        "T5037",
                        "T5039",
                        "T5042",
                        "T5043",
                        "T5044",
                        "T5046",
                        "T5048",
                        "T5049",
                        "T5050",
                        "T5051",
                        "T5053",
                        "T5054",
                        "T5055",
                        "T5056",
                        "T5058",
                        "T5059",
                        "T5060",
                        "T5061",
                        "T5063"
                    ]
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5002",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5009",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5011",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5017",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5024",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5029",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5036",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5048",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5049",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5050",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5058",
                    "priority": "P1"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "tool_assignment_1",
        "instruction": "As an AI agent tasked with setting up accounts for a new marketing tool, allocate app_tiktok accounts to all employees in the Marketing department. These accounts should be standard for these jobs, so make sure to update the rbac_group_map with this new account. Compile a report summarizing the provisioning process.",
        "actions": [
            {
                "name": "filterEmployees",
                "arguments": {
                    "department": "Marketing"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0002",
                    "app_id": "app_tiktok"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0012",
                    "app_id": "app_tiktok"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0016",
                    "app_id": "app_tiktok"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0018",
                    "app_id": "app_tiktok"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0021",
                    "app_id": "app_tiktok"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0024",
                    "app_id": "app_tiktok"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0025",
                    "app_id": "app_tiktok"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0027",
                    "app_id": "app_tiktok"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0031",
                    "app_id": "app_tiktok"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0032",
                    "app_id": "app_tiktok"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0034",
                    "app_id": "app_tiktok"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0041",
                    "app_id": "app_tiktok"
                },
            },
            {
                "name": "assignRbacLicense",
                "arguments": {
                    "license_id": "app_tiktok",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "assignRbacLicense",
                "arguments": {
                    "license_id": "app_tiktok",
                    "job_title": "Design Lead"
                },
            },
            {
                "name": "assignRbacLicense",
                "arguments": {
                    "license_id": "app_tiktok",
                    "job_title": "Growth Marketer"
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "provisioning",
                    "run_data": [
                        "Added app_tiktok account for emp_0002",
                        "Added app_tiktok account for emp_0012",
                        "Added app_tiktok account for emp_0016",
                        "Added app_tiktok account for emp_0018",
                        "Added app_tiktok account for emp_0021",
                        "Added app_tiktok account for emp_0024",
                        "Added app_tiktok account for emp_0025",
                        "Added app_tiktok account for emp_0027",
                        "Added app_tiktok account for emp_0031",
                        "Added app_tiktok account for emp_0032",
                        "Added app_tiktok account for emp_0034",
                        "Added app_tiktok account for emp_0041"
                    ]
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "sync_lifecycle_1",
        "instruction": "Handle synchronization of user lifecycles as an AI agent. Identify employees labeled \"on_leave.\" This includes Tatum Green. Change their statuses to disabled in the directory_accounts database, withdraw licenses from the license_assignments and license_inventory databases, and inform management that the lifecycles have been synchronized.",
        "actions": [
            {
                "name": "filterEmployees",
                "arguments": {
                    "status": "on_leave"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Wyatt",
                    "last_name": "Hill"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0004",
                    "status": "disabled"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0019",
                    "status": "disabled"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0032",
                    "status": "disabled"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0034",
                    "status": "disabled"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0004"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0019"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0032"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0034"
                },
            },
            {
                "name": "filterEmployees",
                "arguments": {
                    "manager_id": "None"
                },
            },
            {
                "name": "notify",
                "arguments": {
                    "recipient_ids": [
                        "emp_0001",
                        "emp_0002",
                        "emp_0003",
                        "emp_0004",
                        "emp_0005",
                        "emp_0006",
                        "emp_0009",
                        "emp_0017"
                    ],
                    "summary": "The lifecycles were synchronized."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "service_stats_1",
        "instruction": "Coordinate the evaluation of daily service stats as an AI agent. Utilize tickets to compute the average time to resolve a ticket (avg_open_age_hours: 36.2), as well as the average opened (tickets_opened: 1.6667) and closed tickets each day (tickets_closed: 1.2). Alert Jamie Chen (emp_0001), Casey Liu (emp_0002), and Drew Kumar (emp_0003) about your results. Produce a pdf report of your results and document it in validation_issues.",
        "actions": [
            {
                "name": "ticketStatistics",
                "arguments": {
                    "field": "avg_open_age_hours",
                    "type": "avg"
                },
            },
            {
                "name": "ticketStatistics",
                "arguments": {
                    "field": "tickets_opened",
                    "type": "avg"
                },
            },
            {
                "name": "ticketStatistics",
                "arguments": {
                    "field": "tickets_closed",
                    "type": "avg"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Avery",
                    "last_name": "Lee"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Jordan",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Taylor",
                    "last_name": "Patel"
                },
            },
            {
                "name": "notify",
                "arguments": {
                    "recipient_ids": [
                        "emp_0001",
                        "emp_0002",
                        "emp_0003"
                    ],
                    "summary": "The average of avg_open_age_hours is 36.2. The average of tickets_opened is 1.6667. The average of tickets_closed is 1.2."
                },
            },
            {
                "name": "generateReviewAndLog",
                "arguments": {
                    "log_data": "The average of avg_open_age_hours is 36.2. The average of tickets_opened is 1.6667. The average of tickets_closed is 1.2."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "asset_reservations_1",
        "instruction": "You function as an AI agent handling asset reservations. Upon the appearance of new hires in hr_memos, assign each one a laptop that is available from it_assets. Set the status of these assets to \"assigned\" and record a completed entry in lifecycle_queue.",
        "actions": [
            {
                "name": "filterHrMemos",
                "arguments": {
                    "type": "onboarding"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Finley",
                    "last_name": "Robinson"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "River",
                    "last_name": "Scott"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Alex",
                    "last_name": "Brown"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Cameron",
                    "last_name": "Wilson"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Taylor",
                    "last_name": "Patel"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Avery",
                    "last_name": "Lee"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Jordan",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Drew",
                    "last_name": "Nelson"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0025",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0031",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0008",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0011",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0003",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0001",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0002",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0039",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0025",
                    "memo_id": "memo_0001",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0031",
                    "memo_id": "memo_0002",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0008",
                    "memo_id": "memo_0003",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0011",
                    "memo_id": "memo_0004",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0003",
                    "memo_id": "memo_0005",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0001",
                    "memo_id": "memo_0006",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0002",
                    "memo_id": "memo_0007",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0039",
                    "memo_id": "memo_0008",
                    "event": "onboarding"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "unused_licenses_1",
        "instruction": "You perform the role of an AI agent responsible for reclaiming unused software licenses. Cross-reference license_assignments against employees who are terminated or on leave. Revoke those assignments, adjust license_inventory to reflect additional available seats, and create individual PDF reports documenting the changes for each user.",
        "actions": [
            {
                "name": "filterEmployees",
                "arguments": {
                    "status": "terminated"
                },
            },
            {
                "name": "filterEmployees",
                "arguments": {
                    "status": "on_leave"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0007"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0033"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0004"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0019"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0032"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0004"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0019"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0032"
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "unassign_licenses",
                    "run_data": [
                        "emp_0007"
                    ]
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "unassign_licenses",
                    "run_data": [
                        "emp_0033"
                    ]
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "unassign_licenses",
                    "run_data": [
                        "emp_0004",
                        "lic_slack_ent",
                        "lic_github_ent",
                        "lic_m365_e3"
                    ]
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "unassign_licenses",
                    "run_data": [
                        "emp_0019",
                        "lic_slack_ent",
                        "lic_m365_e3"
                    ]
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "unassign_licenses",
                    "run_data": [
                        "emp_0032",
                        "lic_salesforce",
                        "lic_slack_ent",
                        "lic_m365_e3"
                    ]
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "onboarding_2",
        "instruction": "HR circulated memos regarding two individuals joining soon, Briar Campbell and Drew Kumar. You need to provide them with the default licenses from rbac_group_map for their respective roles to commence work if they aren't already assigned. They also require CodeHub Enterprise licenses. Ensure they have employee accounts and mailboxes if they lack them. Record these updates in lifecycle_queue. Inform me if you must set up employee accounts and mailboxes.",
        "actions": [
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Drew",
                    "last_name": "Nelson"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Taylor",
                    "last_name": "Patel"
                },
            },
            {
                "name": "employeeAccountExists",
                "arguments": {
                    "first_name": "Drew",
                    "last_name": "Nelson"
                },
            },
            {
                "name": "employeeAccountExists",
                "arguments": {
                    "first_name": "Taylor",
                    "last_name": "Patel"
                },
            },
            {
                "name": "mailboxExists",
                "arguments": {
                    "employee_id": "emp_0039"
                },
            },
            {
                "name": "mailboxExists",
                "arguments": {
                    "employee_id": "emp_0003"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0039"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0003"
                },
            },
            {
                "name": "filterHrMemos",
                "arguments": {
                    "first_name": "Drew",
                    "last_name": "Nelson"
                },
            },
            {
                "name": "filterHrMemos",
                "arguments": {
                    "first_name": "Taylor",
                    "last_name": "Patel"
                },
            },
            {
                "name": "getJobLicenses",
                "arguments": {
                    "job_title": "Support Manager"
                },
            },
            {
                "name": "getJobLicenses",
                "arguments": {
                    "job_title": "Ops Coordinator"
                },
            },
            {
                "name": "getLicenseInfo",
                "arguments": {
                    "license_name": "CodeHub Enterprise"
                },
            },
            {
                "name": "getLicenseAvailability",
                "arguments": {
                    "license_id": "lic_github_ent"
                },
            },
            {
                "name": "assignLicenses",
                "arguments": {
                    "employee_id": "emp_0039",
                    "license_ids": [
                        "lic_github_ent"
                    ]
                },
            },
            {
                "name": "getLicenseAvailability",
                "arguments": {
                    "license_id": "lic_github_ent"
                },
            },
            {
                "name": "assignLicenses",
                "arguments": {
                    "employee_id": "emp_0003",
                    "license_ids": [
                        "lic_github_ent"
                    ]
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0039",
                    "memo_id": "memo_0008",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0003",
                    "memo_id": "memo_0005",
                    "event": "onboarding"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "license_allocation_2",
        "instruction": "As an AI agent that automates software license allocation, utilize license_inventory and employees to spot users with impending software renewals, shown by the last audit date being more than 30 days ago. Verify that the identified licenses are actively in use, then update license_inventory with the recent audit. Produce a CSV file listing underutilized licenses (utilization_rate < 40%). Create low priority TaskTrack tickets for \"Manage license utilization for license_id\" corresponding to each underutilized license.",
        "actions": [
            {
                "name": "licenseRequiresRenewal",
                "arguments": {
                    "num_days": 30
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_m365_e3",
                    "status": "active"
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_m365_e5",
                    "status": "active"
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_adobe_cc",
                    "status": "active"
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_github_ent",
                    "status": "active"
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_slack_ent",
                    "status": "active"
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_salesforce",
                    "status": "active"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_m365_e3"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_m365_e5"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_adobe_cc"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_github_ent"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_slack_ent"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_salesforce"
                },
            },
            {
                "name": "filterLicenses",
                "arguments": {
                    "utilization": 0.4
                },
            },
            {
                "name": "exportUnderutilizedLicenses",
                "arguments": {
                    "output_data": [
                        "lic_m365_e5",
                        "lic_adobe_cc",
                        "lic_github_ent",
                        "lic_salesforce"
                    ]
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "License Allocation",
                    "summary": "Manage license utilization for lic_m365_e5",
                    "priority": "P3"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "License Allocation",
                    "summary": "Manage license utilization for lic_adobe_cc",
                    "priority": "P3"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "License Allocation",
                    "summary": "Manage license utilization for lic_github_ent",
                    "priority": "P3"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "License Allocation",
                    "summary": "Manage license utilization for lic_salesforce",
                    "priority": "P3"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "employee_offboarding_2",
        "instruction": "As an AI agent focused on automating employee offboarding, utilize hr_memos and employees to identify staff marked as \"offboarding.\" Coordinate the offboarding procedures which include disabling their accounts, revoking licenses, archiving mailboxes, and wiping assigned devices listed in it_assets. Record these completed tasks in lifecycle_queue and notify management about each employee's successful offboarding.",
        "actions": [
            {
                "name": "filterHrMemos",
                "arguments": {
                    "type": "offboarding"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Parker",
                    "last_name": "Davis"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Remy",
                    "last_name": "White"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0007",
                    "status": "disabled"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0019",
                    "status": "disabled"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0007"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0019"
                },
            },
            {
                "name": "archiveMailbox",
                "arguments": {
                    "employee_id": "emp_0007",
                    "department": "IT"
                },
            },
            {
                "name": "archiveMailbox",
                "arguments": {
                    "employee_id": "emp_0019",
                    "department": "Operations"
                },
            },
            {
                "name": "deviceAssignment",
                "arguments": {
                    "employee_id": "emp_0007",
                    "unassign": true
                },
            },
            {
                "name": "deviceAssignment",
                "arguments": {
                    "employee_id": "emp_0019",
                    "unassign": true
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0007",
                    "memo_id": "memo_0009",
                    "event": "offboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0019",
                    "memo_id": "memo_0012",
                    "event": "offboarding"
                },
            },
            {
                "name": "filterEmployees",
                "arguments": {
                    "manager_id": "None"
                },
            },
            {
                "name": "notify",
                "arguments": {
                    "recipient_ids": [
                        "emp_0001",
                        "emp_0002",
                        "emp_0003",
                        "emp_0004",
                        "emp_0005",
                        "emp_0006",
                        "emp_0009",
                        "emp_0017"
                    ],
                    "summary": "Jordan Kim was offboarded."
                },
            },
            {
                "name": "notify",
                "arguments": {
                    "recipient_ids": [
                        "emp_0001",
                        "emp_0002",
                        "emp_0003",
                        "emp_0004",
                        "emp_0005",
                        "emp_0006",
                        "emp_0009",
                        "emp_0017"
                    ],
                    "summary": "Sawyer Harris was offboarded."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "compliance_check_2",
        "instruction": "As an AI agent responsible for annual compliance checks, use license_assignments, rbac_group_map, and employees to compare the assigned roles within the Marketing department against the default licenses in rbac_group_map. Highlight any discrepancies, especially for employees missing default licenses. Create a review packet in PDF format and document the process in validation_issues.",
        "actions": [
            {
                "name": "filterEmployees",
                "arguments": {
                    "department": "Marketing"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0002",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0012",
                    "job_title": "Design Lead"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0016",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0018",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0021",
                    "job_title": "Design Lead"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0024",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0025",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0027",
                    "job_title": "Growth Marketer"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0031",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0032",
                    "job_title": "Growth Marketer"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0034",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0041",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "generateReviewAndLog",
                "arguments": {
                    "log_data": "emp_0002 is missing no licenses,emp_0012 is missing no licenses, emp_0016 is missing no licenses, emp_0018 is missing no licenses, emp_0021 is missing no licenses, emp_0024 is missing no licenses, emp_0025 is missing no licenses, emp_0027 is missing no licenses, emp_0031 is missing no licenses, emp_0032 is missing no licenses, emp_0034 is missing no licenses, emp_0041 is missing no licenses"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "track_backlog_2",
        "instruction": "You are an AI agent responsible for monitoring the project backlog. Using the backlog_snapshot_open database, generate a report that identifies tickets not labeled \"Resolved\". Store the report with these details. Generate TaskTrack tickets for any unresolved urgent tickets with a summary as \"Address ticket_id\".",
        "actions": [
            {
                "name": "getTicketsBacklog",
                "arguments": {
                {}
                },
            },
            {
                "name": "filterTickets",
                "arguments": {
                    "ids": [
                        "T5002",
                        "T5003",
                        "T5004",
                        "T5005",
                        "T5006",
                        "T5009",
                        "T5010",
                        "T5011",
                        "T5012",
                        "T5013",
                        "T5014",
                        "T5016",
                        "T5017",
                        "T5020",
                        "T5021",
                        "T5023",
                        "T5024",
                        "T5025",
                        "T5026",
                        "T5027",
                        "T5028",
                        "T5029",
                        "T5030",
                        "T5031",
                        "T5032",
                        "T5035",
                        "T5036",
                        "T5037",
                        "T5039",
                        "T5042",
                        "T5043",
                        "T5044",
                        "T5046",
                        "T5048",
                        "T5049",
                        "T5050",
                        "T5051",
                        "T5053",
                        "T5054",
                        "T5055",
                        "T5056",
                        "T5058",
                        "T5059",
                        "T5060",
                        "T5061",
                        "T5063"
                    ],
                    "not_status": "Resolved"
                },
            },
            {
                "name": "saveReport",
                "arguments": {
                    "save_data": [
                        "T5002",
                        "T5003",
                        "T5004",
                        "T5005",
                        "T5006",
                        "T5009",
                        "T5010",
                        "T5011",
                        "T5012",
                        "T5013",
                        "T5014",
                        "T5016",
                        "T5017",
                        "T5020",
                        "T5021",
                        "T5023",
                        "T5024",
                        "T5025",
                        "T5026",
                        "T5027",
                        "T5028",
                        "T5029",
                        "T5030",
                        "T5031",
                        "T5032",
                        "T5035",
                        "T5036",
                        "T5037",
                        "T5039",
                        "T5042",
                        "T5043",
                        "T5044",
                        "T5046",
                        "T5048",
                        "T5049",
                        "T5050",
                        "T5051",
                        "T5053",
                        "T5054",
                        "T5055",
                        "T5056",
                        "T5058",
                        "T5059",
                        "T5060",
                        "T5061",
                        "T5063"
                    ]
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5002",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5009",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5011",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5017",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5024",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5029",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5036",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5048",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5049",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5050",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5058",
                    "priority": "P1"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "tool_assignment_2",
        "instruction": "You are an AI agent responsible for provisioning accounts for a new marketing tool. Assign app_instagram accounts to all employees in the Marketing department. These accounts must adhere to standard job requirements, so the rbac_group_map needs to reflect this new account setup. Prepare a report summarizing the provisioning.",
        "actions": [
            {
                "name": "filterEmployees",
                "arguments": {
                    "department": "Marketing"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0002",
                    "app_id": "app_instagram"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0012",
                    "app_id": "app_instagram"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0016",
                    "app_id": "app_instagram"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0018",
                    "app_id": "app_instagram"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0021",
                    "app_id": "app_instagram"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0024",
                    "app_id": "app_instagram"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0025",
                    "app_id": "app_instagram"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0027",
                    "app_id": "app_instagram"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0031",
                    "app_id": "app_instagram"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0032",
                    "app_id": "app_instagram"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0034",
                    "app_id": "app_instagram"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0041",
                    "app_id": "app_instagram"
                },
            },
            {
                "name": "assignRbacLicense",
                "arguments": {
                    "license_id": "app_instagram",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "assignRbacLicense",
                "arguments": {
                    "license_id": "app_instagram",
                    "job_title": "Design Lead"
                },
            },
            {
                "name": "assignRbacLicense",
                "arguments": {
                    "license_id": "app_instagram",
                    "job_title": "Growth Marketer"
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "provisioning",
                    "run_data": [
                        "Added app_instagram account for emp_0002",
                        "Added app_instagram account for emp_0012",
                        "Added app_instagram account for emp_0016",
                        "Added app_instagram account for emp_0018",
                        "Added app_instagram account for emp_0021",
                        "Added app_instagram account for emp_0024",
                        "Added app_instagram account for emp_0025",
                        "Added app_instagram account for emp_0027",
                        "Added app_instagram account for emp_0031",
                        "Added app_instagram account for emp_0032",
                        "Added app_instagram account for emp_0034",
                        "Added app_instagram account for emp_0041"
                    ]
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "sync_lifecycle_2",
        "instruction": "Handle the synchronization of user lifecycles as an AI agent. Identify employees labeled as \"on_leave,\" including Jordan Kim. Change their statuses to disabled in the directory_accounts database, remove licenses in both the license_assignments and license_inventory databases, and inform management that the lifecycles have been synchronized.",
        "actions": [
            {
                "name": "filterEmployees",
                "arguments": {
                    "status": "on_leave"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Parker",
                    "last_name": "Davis"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0004",
                    "status": "disabled"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0019",
                    "status": "disabled"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0032",
                    "status": "disabled"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0007",
                    "status": "disabled"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0004"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0019"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0032"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0007"
                },
            },
            {
                "name": "filterEmployees",
                "arguments": {
                    "manager_id": "None"
                },
            },
            {
                "name": "notify",
                "arguments": {
                    "recipient_ids": [
                        "emp_0001",
                        "emp_0002",
                        "emp_0003",
                        "emp_0004",
                        "emp_0005",
                        "emp_0006",
                        "emp_0009",
                        "emp_0017"
                    ],
                    "summary": "The lifecycles were synchronized."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "service_stats_2",
        "instruction": "Coordinate the evaluation of daily service statistics as an AI agent. Use tickets to determine the average time required to resolve a ticket (avg_open_age_hours: 36.2), as well as the average number of opened (tickets_opened: 1.6667) and closed tickets each day (tickets_closed: 1.2). Provide your findings to Jamie Chen (emp_0001), Casey Liu (emp_0002), and Sam Tran (emp_0004). Create a pdf report of your results and record it in validation_issues.",
        "actions": [
            {
                "name": "ticketStatistics",
                "arguments": {
                    "field": "avg_open_age_hours",
                    "type": "avg"
                },
            },
            {
                "name": "ticketStatistics",
                "arguments": {
                    "field": "tickets_opened",
                    "type": "avg"
                },
            },
            {
                "name": "ticketStatistics",
                "arguments": {
                    "field": "tickets_closed",
                    "type": "avg"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Avery",
                    "last_name": "Lee"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Jordan",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Morgan",
                    "last_name": "Nguyen"
                },
            },
            {
                "name": "notify",
                "arguments": {
                    "recipient_ids": [
                        "emp_0001",
                        "emp_0002",
                        "emp_0004"
                    ],
                    "summary": "The average of avg_open_age_hours is 36.2. The average of tickets_opened is 1.6667. The average of tickets_closed is 1.2."
                },
            },
            {
                "name": "generateReviewAndLog",
                "arguments": {
                    "log_data": "The average of avg_open_age_hours is 36.2. The average of tickets_opened is 1.6667. The average of tickets_closed is 1.2."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "asset_reservations_2",
        "instruction": "You are an AI agent tasked with handling asset reservations. Upon the appearance of new hires in hr_memos, allocate them an available laptop from it_assets. Designate those assets as \"assigned\" and log a completed record into lifecycle_queue.",
        "actions": [
            {
                "name": "filterHrMemos",
                "arguments": {
                    "type": "onboarding"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Finley",
                    "last_name": "Robinson"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "River",
                    "last_name": "Scott"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Alex",
                    "last_name": "Brown"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Cameron",
                    "last_name": "Wilson"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Taylor",
                    "last_name": "Patel"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Avery",
                    "last_name": "Lee"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Jordan",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Drew",
                    "last_name": "Nelson"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0025",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0031",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0008",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0011",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0003",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0001",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0002",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0039",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0025",
                    "memo_id": "memo_0001",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0031",
                    "memo_id": "memo_0002",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0008",
                    "memo_id": "memo_0003",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0011",
                    "memo_id": "memo_0004",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0003",
                    "memo_id": "memo_0005",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0001",
                    "memo_id": "memo_0006",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0002",
                    "memo_id": "memo_0007",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0039",
                    "memo_id": "memo_0008",
                    "event": "onboarding"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "unused_licenses_2",
        "instruction": "You are an AI agent responsible for reclaiming unused software licenses. Compare license_assignments with employees' status to identify terminated individuals or those on leave. Remove these assignments, update license_inventory to incorporate available seats, and produce individual pdf reports of the modifications for each user.",
        "actions": [
            {
                "name": "filterEmployees",
                "arguments": {
                    "status": "terminated"
                },
            },
            {
                "name": "filterEmployees",
                "arguments": {
                    "status": "on_leave"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0007"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0033"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0004"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0019"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0032"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0004"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0019"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0032"
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "unassign_licenses",
                    "run_data": [
                        "emp_0007"
                    ]
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "unassign_licenses",
                    "run_data": [
                        "emp_0033"
                    ]
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "unassign_licenses",
                    "run_data": [
                        "emp_0004",
                        "lic_slack_ent",
                        "lic_github_ent",
                        "lic_m365_e3"
                    ]
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "unassign_licenses",
                    "run_data": [
                        "emp_0019",
                        "lic_slack_ent",
                        "lic_m365_e3"
                    ]
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "unassign_licenses",
                    "run_data": [
                        "emp_0032",
                        "lic_salesforce",
                        "lic_slack_ent",
                        "lic_m365_e3"
                    ]
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "onboarding_3",
        "instruction": "The HR department dispatched memos about two upcoming new hires, Briar Campbell and Jamie Chen. It is your responsibility to allocate them the standard licenses from rbac_group_map according to their roles, assuming they haven't already been given these. Additionally, CodeHub Enterprise licenses need to be assigned to them. Should there be any absence of employee accounts and mailboxes, those will be required as well. Record these updates in lifecycle_queue. Inform me if there's a necessity to generate employee accounts and mailboxes.",
        "actions": [
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Drew",
                    "last_name": "Nelson"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Avery",
                    "last_name": "Lee"
                },
            },
            {
                "name": "employeeAccountExists",
                "arguments": {
                    "first_name": "Drew",
                    "last_name": "Nelson"
                },
            },
            {
                "name": "employeeAccountExists",
                "arguments": {
                    "first_name": "Avery",
                    "last_name": "Lee"
                },
            },
            {
                "name": "mailboxExists",
                "arguments": {
                    "employee_id": "emp_0039"
                },
            },
            {
                "name": "mailboxExists",
                "arguments": {
                    "employee_id": "emp_0001"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0039"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0001"
                },
            },
            {
                "name": "filterHrMemos",
                "arguments": {
                    "first_name": "Drew",
                    "last_name": "Nelson"
                },
            },
            {
                "name": "filterHrMemos",
                "arguments": {
                    "first_name": "Avery",
                    "last_name": "Lee"
                },
            },
            {
                "name": "getJobLicenses",
                "arguments": {
                    "job_title": "Support Manager"
                },
            },
            {
                "name": "getJobLicenses",
                "arguments": {
                    "job_title": "HRBP"
                },
            },
            {
                "name": "getLicenseInfo",
                "arguments": {
                    "license_name": "CodeHub Enterprise"
                },
            },
            {
                "name": "getLicenseAvailability",
                "arguments": {
                    "license_id": "lic_github_ent"
                },
            },
            {
                "name": "assignLicenses",
                "arguments": {
                    "employee_id": "emp_0039",
                    "license_ids": [
                        "lic_github_ent"
                    ]
                },
            },
            {
                "name": "getLicenseAvailability",
                "arguments": {
                    "license_id": "lic_github_ent"
                },
            },
            {
                "name": "assignLicenses",
                "arguments": {
                    "employee_id": "emp_0001",
                    "license_ids": [
                        "lic_github_ent"
                    ]
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0039",
                    "memo_id": "memo_0008",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0001",
                    "memo_id": "memo_0006",
                    "event": "onboarding"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "license_allocation_3",
        "instruction": "As an AI agent tasked with automating software license allocation, utilize license_inventory and employees to pinpoint users with imminent software renewals, signified by the last audit exceeding 30 days. Verify active usage of the identified licenses and refresh license_inventory with the latest audit results. Create a CSV documenting licenses with usage rates below 50%. For each underutilized license, initiate low priority TaskTrack tickets titled \"Manage license utilization for license_id.\"",
        "actions": [
            {
                "name": "licenseRequiresRenewal",
                "arguments": {
                    "num_days": 30
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_m365_e3",
                    "status": "active"
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_m365_e5",
                    "status": "active"
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_adobe_cc",
                    "status": "active"
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_github_ent",
                    "status": "active"
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_slack_ent",
                    "status": "active"
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_salesforce",
                    "status": "active"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_m365_e3"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_m365_e5"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_adobe_cc"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_github_ent"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_slack_ent"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_salesforce"
                },
            },
            {
                "name": "filterLicenses",
                "arguments": {
                    "utilization": 0.5
                },
            },
            {
                "name": "exportUnderutilizedLicenses",
                "arguments": {
                    "output_data": [
                        "lic_m365_e5",
                        "lic_adobe_cc",
                        "lic_github_ent",
                        "lic_slack_ent",
                        "lic_salesforce"
                    ]
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "License Allocation",
                    "summary": "Manage license utilization for lic_m365_e5",
                    "priority": "P3"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "License Allocation",
                    "summary": "Manage license utilization for lic_adobe_cc",
                    "priority": "P3"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "License Allocation",
                    "summary": "Manage license utilization for lic_github_ent",
                    "priority": "P3"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "License Allocation",
                    "summary": "Manage license utilization for lic_slack_ent",
                    "priority": "P3"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "License Allocation",
                    "summary": "Manage license utilization for lic_salesforce",
                    "priority": "P3"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "employee_offboarding_3",
        "instruction": "You are an AI agent designated for automating employee offboarding. Utilize hr_memos and employees to identify staff labeled \"offboarding.\" Handle the offboarding procedures, such as disabling their accounts, revoking licenses, archiving mailboxes, and wiping assigned devices in it_assets. Record these completed tasks in lifecycle_queue, and inform management that each employee has been offboarded.",
        "actions": [
            {
                "name": "filterHrMemos",
                "arguments": {
                    "type": "offboarding"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Parker",
                    "last_name": "Davis"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Remy",
                    "last_name": "White"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0007",
                    "status": "disabled"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0019",
                    "status": "disabled"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0007"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0019"
                },
            },
            {
                "name": "archiveMailbox",
                "arguments": {
                    "employee_id": "emp_0007",
                    "department": "IT"
                },
            },
            {
                "name": "archiveMailbox",
                "arguments": {
                    "employee_id": "emp_0019",
                    "department": "Operations"
                },
            },
            {
                "name": "deviceAssignment",
                "arguments": {
                    "employee_id": "emp_0007",
                    "unassign": true
                },
            },
            {
                "name": "deviceAssignment",
                "arguments": {
                    "employee_id": "emp_0019",
                    "unassign": true
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0007",
                    "memo_id": "memo_0009",
                    "event": "offboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0019",
                    "memo_id": "memo_0012",
                    "event": "offboarding"
                },
            },
            {
                "name": "filterEmployees",
                "arguments": {
                    "manager_id": "None"
                },
            },
            {
                "name": "notify",
                "arguments": {
                    "recipient_ids": [
                        "emp_0001",
                        "emp_0002",
                        "emp_0003",
                        "emp_0004",
                        "emp_0005",
                        "emp_0006",
                        "emp_0009",
                        "emp_0017"
                    ],
                    "summary": "Jordan Kim was offboarded."
                },
            },
            {
                "name": "notify",
                "arguments": {
                    "recipient_ids": [
                        "emp_0001",
                        "emp_0002",
                        "emp_0003",
                        "emp_0004",
                        "emp_0005",
                        "emp_0006",
                        "emp_0009",
                        "emp_0017"
                    ],
                    "summary": "Sawyer Harris was offboarded."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "compliance_check_3",
        "instruction": "You are an AI agent managing quarterly compliance checks. Employ license_assignments, rbac_group_map, and employees to compare assigned roles in the Marketing department with rbac_group_map default licenses. Identify any employees lacking default licenses. Compile a review packet in PDF format and log the run in validation_issues.",
        "actions": [
            {
                "name": "filterEmployees",
                "arguments": {
                    "department": "Marketing"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0002",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0012",
                    "job_title": "Design Lead"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0016",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0018",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0021",
                    "job_title": "Design Lead"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0024",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0025",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0027",
                    "job_title": "Growth Marketer"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0031",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0032",
                    "job_title": "Growth Marketer"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0034",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0041",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "generateReviewAndLog",
                "arguments": {
                    "log_data": "emp_0002 is missing no licenses,emp_0012 is missing no licenses, emp_0016 is missing no licenses, emp_0018 is missing no licenses, emp_0021 is missing no licenses, emp_0024 is missing no licenses, emp_0025 is missing no licenses, emp_0027 is missing no licenses, emp_0031 is missing no licenses, emp_0032 is missing no licenses, emp_0034 is missing no licenses, emp_0041 is missing no licenses"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "track_backlog_3",
        "instruction": "As an AI agent responsible for tracking project backlog, utilize the backlog_snapshot_open database to compile a report that emphasizes tickets not marked as \"Resolved\". Store the report with these observations. Generate TaskTrack tickets for any unresolved urgent tickets using the format \"Address ticket_id\" in the summary.",
        "actions": [
            {
                "name": "getTicketsBacklog",
                "arguments": {
                {}
                },
            },
            {
                "name": "filterTickets",
                "arguments": {
                    "ids": [
                        "T5002",
                        "T5003",
                        "T5004",
                        "T5005",
                        "T5006",
                        "T5009",
                        "T5010",
                        "T5011",
                        "T5012",
                        "T5013",
                        "T5014",
                        "T5016",
                        "T5017",
                        "T5020",
                        "T5021",
                        "T5023",
                        "T5024",
                        "T5025",
                        "T5026",
                        "T5027",
                        "T5028",
                        "T5029",
                        "T5030",
                        "T5031",
                        "T5032",
                        "T5035",
                        "T5036",
                        "T5037",
                        "T5039",
                        "T5042",
                        "T5043",
                        "T5044",
                        "T5046",
                        "T5048",
                        "T5049",
                        "T5050",
                        "T5051",
                        "T5053",
                        "T5054",
                        "T5055",
                        "T5056",
                        "T5058",
                        "T5059",
                        "T5060",
                        "T5061",
                        "T5063"
                    ],
                    "not_status": "Resolved"
                },
            },
            {
                "name": "saveReport",
                "arguments": {
                    "save_data": [
                        "T5002",
                        "T5003",
                        "T5004",
                        "T5005",
                        "T5006",
                        "T5009",
                        "T5010",
                        "T5011",
                        "T5012",
                        "T5013",
                        "T5014",
                        "T5016",
                        "T5017",
                        "T5020",
                        "T5021",
                        "T5023",
                        "T5024",
                        "T5025",
                        "T5026",
                        "T5027",
                        "T5028",
                        "T5029",
                        "T5030",
                        "T5031",
                        "T5032",
                        "T5035",
                        "T5036",
                        "T5037",
                        "T5039",
                        "T5042",
                        "T5043",
                        "T5044",
                        "T5046",
                        "T5048",
                        "T5049",
                        "T5050",
                        "T5051",
                        "T5053",
                        "T5054",
                        "T5055",
                        "T5056",
                        "T5058",
                        "T5059",
                        "T5060",
                        "T5061",
                        "T5063"
                    ]
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5002",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5009",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5011",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5017",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5024",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5029",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5036",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5048",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5049",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5050",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5058",
                    "priority": "P1"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "tool_assignment_3",
        "instruction": "As an AI agent tasked with provisioning accounts for a new marketing tool, allocate app_reddit accounts to all employees within the Marketing department. These accounts should be standardized for their roles, requiring an update to the rbac_group_map with the inclusion of this new account. Assemble a report detailing the provisioning overview.",
        "actions": [
            {
                "name": "filterEmployees",
                "arguments": {
                    "department": "Marketing"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0002",
                    "app_id": "app_reddit"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0012",
                    "app_id": "app_reddit"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0016",
                    "app_id": "app_reddit"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0018",
                    "app_id": "app_reddit"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0021",
                    "app_id": "app_reddit"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0024",
                    "app_id": "app_reddit"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0025",
                    "app_id": "app_reddit"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0027",
                    "app_id": "app_reddit"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0031",
                    "app_id": "app_reddit"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0032",
                    "app_id": "app_reddit"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0034",
                    "app_id": "app_reddit"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0041",
                    "app_id": "app_reddit"
                },
            },
            {
                "name": "assignRbacLicense",
                "arguments": {
                    "license_id": "app_reddit",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "assignRbacLicense",
                "arguments": {
                    "license_id": "app_reddit",
                    "job_title": "Design Lead"
                },
            },
            {
                "name": "assignRbacLicense",
                "arguments": {
                    "license_id": "app_reddit",
                    "job_title": "Growth Marketer"
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "provisioning",
                    "run_data": [
                        "Added app_reddit account for emp_0002",
                        "Added app_reddit account for emp_0012",
                        "Added app_reddit account for emp_0016",
                        "Added app_reddit account for emp_0018",
                        "Added app_reddit account for emp_0021",
                        "Added app_reddit account for emp_0024",
                        "Added app_reddit account for emp_0025",
                        "Added app_reddit account for emp_0027",
                        "Added app_reddit account for emp_0031",
                        "Added app_reddit account for emp_0032",
                        "Added app_reddit account for emp_0034",
                        "Added app_reddit account for emp_0041"
                    ]
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "sync_lifecycle_3",
        "instruction": "You are an AI agent responsible for synchronizing user lifecycles. Identify any employees labeled \"on_leave.\" Include Morgan Lee in your checks as well. Modify their statuses to disabled within the directory_accounts database, withdraw licenses in the license_assignments and license_inventory databases, and inform management that the lifecycles have been synchronized.",
        "actions": [
            {
                "name": "filterEmployees",
                "arguments": {
                    "status": "on_leave"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Alex",
                    "last_name": "Brown"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0004",
                    "status": "disabled"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0019",
                    "status": "disabled"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0032",
                    "status": "disabled"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0008",
                    "status": "disabled"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0004"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0019"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0032"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0008"
                },
            },
            {
                "name": "filterEmployees",
                "arguments": {
                    "manager_id": "None"
                },
            },
            {
                "name": "notify",
                "arguments": {
                    "recipient_ids": [
                        "emp_0001",
                        "emp_0002",
                        "emp_0003",
                        "emp_0004",
                        "emp_0005",
                        "emp_0006",
                        "emp_0009",
                        "emp_0017"
                    ],
                    "summary": "The lifecycles were synchronized."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "service_stats_3",
        "instruction": "You are an AI agent tasked with evaluating daily service statistics. Utilize tickets to compute the average time required to complete a ticket (avg_open_age_hours: 36.2), as well as the average opened (tickets_opened: 1.6667) and closed tickets per day (tickets_closed: 1.2). Report your results to Jamie Chen (emp_0001), Casey Liu (emp_0002), and Robin Jones (emp_0005). Create a pdf report of your findings and record it in validation_issues.",
        "actions": [
            {
                "name": "ticketStatistics",
                "arguments": {
                    "field": "avg_open_age_hours",
                    "type": "avg"
                },
            },
            {
                "name": "ticketStatistics",
                "arguments": {
                    "field": "tickets_opened",
                    "type": "avg"
                },
            },
            {
                "name": "ticketStatistics",
                "arguments": {
                    "field": "tickets_closed",
                    "type": "avg"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Avery",
                    "last_name": "Lee"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Jordan",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Casey",
                    "last_name": "Smith"
                },
            },
            {
                "name": "notify",
                "arguments": {
                    "recipient_ids": [
                        "emp_0001",
                        "emp_0002",
                        "emp_0005"
                    ],
                    "summary": "The average of avg_open_age_hours is 36.2. The average of tickets_opened is 1.6667. The average of tickets_closed is 1.2."
                },
            },
            {
                "name": "generateReviewAndLog",
                "arguments": {
                    "log_data": "The average of avg_open_age_hours is 36.2. The average of tickets_opened is 1.6667. The average of tickets_closed is 1.2."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "asset_reservations_3",
        "instruction": "You are an AI agent responsible for handling asset reservations. Identify employees with onboarding memos in hr_memos and allocate them an available laptop from it_assets. Update the status of those assets as \"assigned\" and document a completed record in lifecycle_queue.",
        "actions": [
            {
                "name": "filterHrMemos",
                "arguments": {
                    "type": "onboarding"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Finley",
                    "last_name": "Robinson"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "River",
                    "last_name": "Scott"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Alex",
                    "last_name": "Brown"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Cameron",
                    "last_name": "Wilson"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Taylor",
                    "last_name": "Patel"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Avery",
                    "last_name": "Lee"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Jordan",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Drew",
                    "last_name": "Nelson"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0025",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0031",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0008",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0011",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0003",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0001",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0002",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0039",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0025",
                    "memo_id": "memo_0001",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0031",
                    "memo_id": "memo_0002",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0008",
                    "memo_id": "memo_0003",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0011",
                    "memo_id": "memo_0004",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0003",
                    "memo_id": "memo_0005",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0001",
                    "memo_id": "memo_0006",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0002",
                    "memo_id": "memo_0007",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0039",
                    "memo_id": "memo_0008",
                    "event": "onboarding"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "unused_licenses_3",
        "instruction": "You are an AI agent managing the reclamation of unused software licenses. By referencing license_assignments and employees, locate users who are either terminated or on leave. Remove their assignments, adjust license_inventory to reflect the newly available seats, and create individual PDF reports detailing the changes for each user.",
        "actions": [
            {
                "name": "filterEmployees",
                "arguments": {
                    "status": "terminated"
                },
            },
            {
                "name": "filterEmployees",
                "arguments": {
                    "status": "on_leave"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0007"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0033"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0004"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0019"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0032"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0004"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0019"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0032"
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "unassign_licenses",
                    "run_data": [
                        "emp_0007"
                    ]
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "unassign_licenses",
                    "run_data": [
                        "emp_0033"
                    ]
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "unassign_licenses",
                    "run_data": [
                        "emp_0004",
                        "lic_slack_ent",
                        "lic_github_ent",
                        "lic_m365_e3"
                    ]
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "unassign_licenses",
                    "run_data": [
                        "emp_0019",
                        "lic_slack_ent",
                        "lic_m365_e3"
                    ]
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "unassign_licenses",
                    "run_data": [
                        "emp_0032",
                        "lic_salesforce",
                        "lic_slack_ent",
                        "lic_m365_e3"
                    ]
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "onboarding_4",
        "instruction": "HR distributed memos regarding two new individuals joining shortly, Casey Liu and Drew Kumar. It is necessary for you to allocate the default licenses from rbac_group_map for their specific roles to initiate their work unless they already possess them. Additionally, they must be provided with CodeHub Enterprise licenses. In case they lack employee accounts and mailboxes, those will need to be established as well. Document these updates to lifecycle_queue. Reach out if there is a need to set up employee accounts and mailboxes.",
        "actions": [
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Jordan",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Taylor",
                    "last_name": "Patel"
                },
            },
            {
                "name": "employeeAccountExists",
                "arguments": {
                    "first_name": "Jordan",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "employeeAccountExists",
                "arguments": {
                    "first_name": "Taylor",
                    "last_name": "Patel"
                },
            },
            {
                "name": "mailboxExists",
                "arguments": {
                    "employee_id": "emp_0002"
                },
            },
            {
                "name": "mailboxExists",
                "arguments": {
                    "employee_id": "emp_0003"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0002"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0003"
                },
            },
            {
                "name": "filterHrMemos",
                "arguments": {
                    "first_name": "Jordan",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "filterHrMemos",
                "arguments": {
                    "first_name": "Taylor",
                    "last_name": "Patel"
                },
            },
            {
                "name": "getJobLicenses",
                "arguments": {
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "getJobLicenses",
                "arguments": {
                    "job_title": "Ops Coordinator"
                },
            },
            {
                "name": "getLicenseInfo",
                "arguments": {
                    "license_name": "CodeHub Enterprise"
                },
            },
            {
                "name": "getLicenseAvailability",
                "arguments": {
                    "license_id": "lic_github_ent"
                },
            },
            {
                "name": "assignLicenses",
                "arguments": {
                    "employee_id": "emp_0002",
                    "license_ids": [
                        "lic_github_ent"
                    ]
                },
            },
            {
                "name": "getLicenseAvailability",
                "arguments": {
                    "license_id": "lic_github_ent"
                },
            },
            {
                "name": "assignLicenses",
                "arguments": {
                    "employee_id": "emp_0003",
                    "license_ids": [
                        "lic_github_ent"
                    ]
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0002",
                    "memo_id": "memo_0007",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0003",
                    "memo_id": "memo_0005",
                    "event": "onboarding"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "license_allocation_4",
        "instruction": "As an AI agent responsible for automating software license distribution, use license_inventory and employees to pinpoint users with impending software renewals, which are flagged if the latest audit exceeds 20 days old. Verify whether the identified licenses are currently in use and refresh license_inventory with the latest audit information. Produce a CSV file listing underutilized licenses (utilization_rate < 30%). Initiate low priority TaskTrack tickets with the topic \"Manage license utilization for license_id\" for each underutilized license.",
        "actions": [
            {
                "name": "licenseRequiresRenewal",
                "arguments": {
                    "num_days": 20
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_m365_e3",
                    "status": "active"
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_m365_e5",
                    "status": "active"
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_adobe_cc",
                    "status": "active"
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_github_ent",
                    "status": "active"
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_slack_ent",
                    "status": "active"
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_salesforce",
                    "status": "active"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_m365_e3"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_m365_e5"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_adobe_cc"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_github_ent"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_slack_ent"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_salesforce"
                },
            },
            {
                "name": "filterLicenses",
                "arguments": {
                    "utilization": 0.3
                },
            },
            {
                "name": "exportUnderutilizedLicenses",
                "arguments": {
                    "output_data": [
                        "lic_m365_e5",
                        "lic_adobe_cc",
                        "lic_github_ent",
                        "lic_salesforce"
                    ]
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "License Allocation",
                    "summary": "Manage license utilization for lic_m365_e5",
                    "priority": "P3"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "License Allocation",
                    "summary": "Manage license utilization for lic_adobe_cc",
                    "priority": "P3"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "License Allocation",
                    "summary": "Manage license utilization for lic_github_ent",
                    "priority": "P3"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "License Allocation",
                    "summary": "Manage license utilization for lic_salesforce",
                    "priority": "P3"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "employee_offboarding_4",
        "instruction": "As an AI agent responsible for automating employee offboarding, locate staff labeled \"offboarding\" within hr_memos and employees. Coordinate the offboarding procedures, which include disabling their accounts, revoking licenses, archiving mailboxes, and wiping devices allocated in it_assets. Draft a log of these finished tasks in lifecycle_queue, and notify management that each employee has been offboarded.",
        "actions": [
            {
                "name": "filterHrMemos",
                "arguments": {
                    "type": "offboarding"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Parker",
                    "last_name": "Davis"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Remy",
                    "last_name": "White"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0007",
                    "status": "disabled"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0019",
                    "status": "disabled"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0007"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0019"
                },
            },
            {
                "name": "archiveMailbox",
                "arguments": {
                    "employee_id": "emp_0007",
                    "department": "IT"
                },
            },
            {
                "name": "archiveMailbox",
                "arguments": {
                    "employee_id": "emp_0019",
                    "department": "Operations"
                },
            },
            {
                "name": "deviceAssignment",
                "arguments": {
                    "employee_id": "emp_0007",
                    "unassign": true
                },
            },
            {
                "name": "deviceAssignment",
                "arguments": {
                    "employee_id": "emp_0019",
                    "unassign": true
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0007",
                    "memo_id": "memo_0009",
                    "event": "offboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0019",
                    "memo_id": "memo_0012",
                    "event": "offboarding"
                },
            },
            {
                "name": "filterEmployees",
                "arguments": {
                    "manager_id": "None"
                },
            },
            {
                "name": "notify",
                "arguments": {
                    "recipient_ids": [
                        "emp_0001",
                        "emp_0002",
                        "emp_0003",
                        "emp_0004",
                        "emp_0005",
                        "emp_0006",
                        "emp_0009",
                        "emp_0017"
                    ],
                    "summary": "Jordan Kim was offboarded."
                },
            },
            {
                "name": "notify",
                "arguments": {
                    "recipient_ids": [
                        "emp_0001",
                        "emp_0002",
                        "emp_0003",
                        "emp_0004",
                        "emp_0005",
                        "emp_0006",
                        "emp_0009",
                        "emp_0017"
                    ],
                    "summary": "Sawyer Harris was offboarded."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "compliance_check_4",
        "instruction": "You are an AI agent tasked with conducting quarterly compliance checks. Leveraging license_assignments, rbac_group_map, and employees, cross-reference assigned roles in the Marketing department with the rbac_group_map default licenses. Identify anomalies, particularly employees who lack default licenses. Compile a review packet as a PDF and document the session in validation_issues.",
        "actions": [
            {
                "name": "filterEmployees",
                "arguments": {
                    "department": "Marketing"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0002",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0012",
                    "job_title": "Design Lead"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0016",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0018",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0021",
                    "job_title": "Design Lead"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0024",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0025",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0027",
                    "job_title": "Growth Marketer"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0031",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0032",
                    "job_title": "Growth Marketer"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0034",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0041",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "generateReviewAndLog",
                "arguments": {
                    "log_data": "emp_0002 is missing no licenses,emp_0012 is missing no licenses, emp_0016 is missing no licenses, emp_0018 is missing no licenses, emp_0021 is missing no licenses, emp_0024 is missing no licenses, emp_0025 is missing no licenses, emp_0027 is missing no licenses, emp_0031 is missing no licenses, emp_0032 is missing no licenses, emp_0034 is missing no licenses, emp_0041 is missing no licenses"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "track_backlog_4",
        "instruction": "As an AI agent monitoring the project backlog, access the backlog_snapshot_open database to generate a report that emphasizes tickets still lacking a \"Resolved\" status. Ensure you save a report with these details. Initiate TaskTrack tickets for any unresolved urgent tickets with the summary as \"Address ticket_id\".",
        "actions": [
            {
                "name": "getTicketsBacklog",
                "arguments": {
                {}
                },
            },
            {
                "name": "filterTickets",
                "arguments": {
                    "ids": [
                        "T5002",
                        "T5003",
                        "T5004",
                        "T5005",
                        "T5006",
                        "T5009",
                        "T5010",
                        "T5011",
                        "T5012",
                        "T5013",
                        "T5014",
                        "T5016",
                        "T5017",
                        "T5020",
                        "T5021",
                        "T5023",
                        "T5024",
                        "T5025",
                        "T5026",
                        "T5027",
                        "T5028",
                        "T5029",
                        "T5030",
                        "T5031",
                        "T5032",
                        "T5035",
                        "T5036",
                        "T5037",
                        "T5039",
                        "T5042",
                        "T5043",
                        "T5044",
                        "T5046",
                        "T5048",
                        "T5049",
                        "T5050",
                        "T5051",
                        "T5053",
                        "T5054",
                        "T5055",
                        "T5056",
                        "T5058",
                        "T5059",
                        "T5060",
                        "T5061",
                        "T5063"
                    ],
                    "not_status": "Resolved"
                },
            },
            {
                "name": "saveReport",
                "arguments": {
                    "save_data": [
                        "T5002",
                        "T5003",
                        "T5004",
                        "T5005",
                        "T5006",
                        "T5009",
                        "T5010",
                        "T5011",
                        "T5012",
                        "T5013",
                        "T5014",
                        "T5016",
                        "T5017",
                        "T5020",
                        "T5021",
                        "T5023",
                        "T5024",
                        "T5025",
                        "T5026",
                        "T5027",
                        "T5028",
                        "T5029",
                        "T5030",
                        "T5031",
                        "T5032",
                        "T5035",
                        "T5036",
                        "T5037",
                        "T5039",
                        "T5042",
                        "T5043",
                        "T5044",
                        "T5046",
                        "T5048",
                        "T5049",
                        "T5050",
                        "T5051",
                        "T5053",
                        "T5054",
                        "T5055",
                        "T5056",
                        "T5058",
                        "T5059",
                        "T5060",
                        "T5061",
                        "T5063"
                    ]
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5002",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5009",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5011",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5017",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5024",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5029",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5036",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5048",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5049",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5050",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5058",
                    "priority": "P1"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "tool_assignment_4",
        "instruction": "As an AI agent responsible for setting up accounts for a new marketing tool, allocate app_twitter accounts to all staff members in the Marketing department. These accounts should adhere to job standards, necessitating an update to the rbac_group_map to include this new account. Prepare a report detailing the provisioning summary.",
        "actions": [
            {
                "name": "filterEmployees",
                "arguments": {
                    "department": "Marketing"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0002",
                    "app_id": "app_twitter"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0012",
                    "app_id": "app_twitter"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0016",
                    "app_id": "app_twitter"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0018",
                    "app_id": "app_twitter"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0021",
                    "app_id": "app_twitter"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0024",
                    "app_id": "app_twitter"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0025",
                    "app_id": "app_twitter"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0027",
                    "app_id": "app_twitter"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0031",
                    "app_id": "app_twitter"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0032",
                    "app_id": "app_twitter"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0034",
                    "app_id": "app_twitter"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0041",
                    "app_id": "app_twitter"
                },
            },
            {
                "name": "assignRbacLicense",
                "arguments": {
                    "license_id": "app_twitter",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "assignRbacLicense",
                "arguments": {
                    "license_id": "app_twitter",
                    "job_title": "Design Lead"
                },
            },
            {
                "name": "assignRbacLicense",
                "arguments": {
                    "license_id": "app_twitter",
                    "job_title": "Growth Marketer"
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "provisioning",
                    "run_data": [
                        "Added app_twitter account for emp_0002",
                        "Added app_twitter account for emp_0012",
                        "Added app_twitter account for emp_0016",
                        "Added app_twitter account for emp_0018",
                        "Added app_twitter account for emp_0021",
                        "Added app_twitter account for emp_0024",
                        "Added app_twitter account for emp_0025",
                        "Added app_twitter account for emp_0027",
                        "Added app_twitter account for emp_0031",
                        "Added app_twitter account for emp_0032",
                        "Added app_twitter account for emp_0034",
                        "Added app_twitter account for emp_0041"
                    ]
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "sync_lifecycle_4",
        "instruction": "Your role is to synchronize user lifecycles as an AI agent. Look for employees marked \"on_leave\". Apply these steps to Avery Zhang too. Change their statuses to disabled in the directory_accounts database, remove licenses in the license_assignments and license_inventory databases, and inform management that the lifecycles have been synchronized.",
        "actions": [
            {
                "name": "filterEmployees",
                "arguments": {
                    "status": "on_leave"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Rowan",
                    "last_name": "Lopez"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0004",
                    "status": "disabled"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0019",
                    "status": "disabled"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0032",
                    "status": "disabled"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0010",
                    "status": "disabled"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0004"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0019"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0032"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0010"
                },
            },
            {
                "name": "filterEmployees",
                "arguments": {
                    "manager_id": "None"
                },
            },
            {
                "name": "notify",
                "arguments": {
                    "recipient_ids": [
                        "emp_0001",
                        "emp_0002",
                        "emp_0003",
                        "emp_0004",
                        "emp_0005",
                        "emp_0006",
                        "emp_0009",
                        "emp_0017"
                    ],
                    "summary": "The lifecycles were synchronized."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "service_stats_4",
        "instruction": "As an AI agent, you are responsible for evaluating daily service statistics. Analyze tickets to determine the average time to complete a ticket (avg_open_age_hours: 36.2), along with the average daily opened (tickets_opened: 1.6667) and closed tickets (tickets_closed: 1.2). Share your findings with Jamie Chen (emp_0001), Drew Kumar (emp_0003), and Sam Tran (emp_0004). Create a pdf report of the findings and record it in validation_issues.",
        "actions": [
            {
                "name": "ticketStatistics",
                "arguments": {
                    "field": "avg_open_age_hours",
                    "type": "avg"
                },
            },
            {
                "name": "ticketStatistics",
                "arguments": {
                    "field": "tickets_opened",
                    "type": "avg"
                },
            },
            {
                "name": "ticketStatistics",
                "arguments": {
                    "field": "tickets_closed",
                    "type": "avg"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Avery",
                    "last_name": "Lee"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Taylor",
                    "last_name": "Patel"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Morgan",
                    "last_name": "Nguyen"
                },
            },
            {
                "name": "notify",
                "arguments": {
                    "recipient_ids": [
                        "emp_0001",
                        "emp_0003",
                        "emp_0004"
                    ],
                    "summary": "The average of avg_open_age_hours is 36.2. The average of tickets_opened is 1.6667. The average of tickets_closed is 1.2."
                },
            },
            {
                "name": "generateReviewAndLog",
                "arguments": {
                    "log_data": "The average of avg_open_age_hours is 36.2. The average of tickets_opened is 1.6667. The average of tickets_closed is 1.2."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "asset_reservations_4",
        "instruction": "Act as an AI agent for asset reservations. Upon identification of new hires in hr_memos, allocate an unused laptop from it_assets to them. Label those assets as \"assigned\" and record a finished entry in lifecycle_queue.",
        "actions": [
            {
                "name": "filterHrMemos",
                "arguments": {
                    "type": "onboarding"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Finley",
                    "last_name": "Robinson"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "River",
                    "last_name": "Scott"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Alex",
                    "last_name": "Brown"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Cameron",
                    "last_name": "Wilson"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Taylor",
                    "last_name": "Patel"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Avery",
                    "last_name": "Lee"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Jordan",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Drew",
                    "last_name": "Nelson"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0025",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0031",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0008",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0011",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0003",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0001",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0002",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0039",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0025",
                    "memo_id": "memo_0001",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0031",
                    "memo_id": "memo_0002",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0008",
                    "memo_id": "memo_0003",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0011",
                    "memo_id": "memo_0004",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0003",
                    "memo_id": "memo_0005",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0001",
                    "memo_id": "memo_0006",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0002",
                    "memo_id": "memo_0007",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0039",
                    "memo_id": "memo_0008",
                    "event": "onboarding"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "unused_licenses_4",
        "instruction": "Function as an AI agent to reclaim unused software licenses. Verify license_assignments against employees who are either terminated or on leave. Revoke such assignments, modify license_inventory to reflect increased seat availability, and create individual pdf reports documenting the changes for each user.",
        "actions": [
            {
                "name": "filterEmployees",
                "arguments": {
                    "status": "terminated"
                },
            },
            {
                "name": "filterEmployees",
                "arguments": {
                    "status": "on_leave"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0007"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0033"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0004"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0019"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0032"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0004"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0019"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0032"
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "unassign_licenses",
                    "run_data": [
                        "emp_0007"
                    ]
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "unassign_licenses",
                    "run_data": [
                        "emp_0033"
                    ]
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "unassign_licenses",
                    "run_data": [
                        "emp_0004",
                        "lic_slack_ent",
                        "lic_github_ent",
                        "lic_m365_e3"
                    ]
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "unassign_licenses",
                    "run_data": [
                        "emp_0019",
                        "lic_slack_ent",
                        "lic_m365_e3"
                    ]
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "unassign_licenses",
                    "run_data": [
                        "emp_0032",
                        "lic_salesforce",
                        "lic_slack_ent",
                        "lic_m365_e3"
                    ]
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "onboarding_5",
        "instruction": "HR distributed memos regarding two individuals commencing shortly, Casey Liu and Jamie Chen. You are responsible for allocating them the default licenses from rbac_group_map according to their respective jobs to begin work if they lack them. Ensure they are assigned CodeHub Enterprise licenses as well. Should they lack employee accounts and mailboxes, these must be provisioned for them too. Record these modifications in lifecycle_queue. Inform me if there is a necessity to create employee accounts and mailboxes.",
        "actions": [
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Jordan",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Avery",
                    "last_name": "Lee"
                },
            },
            {
                "name": "employeeAccountExists",
                "arguments": {
                    "first_name": "Jordan",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "employeeAccountExists",
                "arguments": {
                    "first_name": "Avery",
                    "last_name": "Lee"
                },
            },
            {
                "name": "mailboxExists",
                "arguments": {
                    "employee_id": "emp_0002"
                },
            },
            {
                "name": "mailboxExists",
                "arguments": {
                    "employee_id": "emp_0001"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0002"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0001"
                },
            },
            {
                "name": "filterHrMemos",
                "arguments": {
                    "first_name": "Jordan",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "filterHrMemos",
                "arguments": {
                    "first_name": "Avery",
                    "last_name": "Lee"
                },
            },
            {
                "name": "getJobLicenses",
                "arguments": {
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "getJobLicenses",
                "arguments": {
                    "job_title": "HRBP"
                },
            },
            {
                "name": "getLicenseInfo",
                "arguments": {
                    "license_name": "CodeHub Enterprise"
                },
            },
            {
                "name": "getLicenseAvailability",
                "arguments": {
                    "license_id": "lic_github_ent"
                },
            },
            {
                "name": "assignLicenses",
                "arguments": {
                    "employee_id": "emp_0002",
                    "license_ids": [
                        "lic_github_ent"
                    ]
                },
            },
            {
                "name": "getLicenseAvailability",
                "arguments": {
                    "license_id": "lic_github_ent"
                },
            },
            {
                "name": "assignLicenses",
                "arguments": {
                    "employee_id": "emp_0001",
                    "license_ids": [
                        "lic_github_ent"
                    ]
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0002",
                    "memo_id": "memo_0007",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0001",
                    "memo_id": "memo_0006",
                    "event": "onboarding"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "license_allocation_5",
        "instruction": "As an AI agent tasked with automating software license allocation, utilize license_inventory and employees to identify users due for software renewals, signaled by the last audit surpassing 20 days. Verify that the identified licenses are in active use and refresh license_inventory with the most recent audit. Produce a CSV listing underutilized licenses (utilization_rate < 40%). Initiate low priority TaskTrack tickets for \"Manage license utilization for license_id\" corresponding to each underutilized license.",
        "actions": [
            {
                "name": "licenseRequiresRenewal",
                "arguments": {
                    "num_days": 20
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_m365_e3",
                    "status": "active"
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_m365_e5",
                    "status": "active"
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_adobe_cc",
                    "status": "active"
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_github_ent",
                    "status": "active"
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_slack_ent",
                    "status": "active"
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_salesforce",
                    "status": "active"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_m365_e3"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_m365_e5"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_adobe_cc"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_github_ent"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_slack_ent"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_salesforce"
                },
            },
            {
                "name": "filterLicenses",
                "arguments": {
                    "utilization": 0.4
                },
            },
            {
                "name": "exportUnderutilizedLicenses",
                "arguments": {
                    "output_data": [
                        "lic_m365_e5",
                        "lic_adobe_cc",
                        "lic_github_ent",
                        "lic_salesforce"
                    ]
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "License Allocation",
                    "summary": "Manage license utilization for lic_m365_e5",
                    "priority": "P3"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "License Allocation",
                    "summary": "Manage license utilization for lic_adobe_cc",
                    "priority": "P3"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "License Allocation",
                    "summary": "Manage license utilization for lic_github_ent",
                    "priority": "P3"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "License Allocation",
                    "summary": "Manage license utilization for lic_salesforce",
                    "priority": "P3"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "employee_offboarding_5",
        "instruction": "You are an AI agent tasked with automating the offboarding of employees. Locate individuals labeled \"offboarding\" in hr_memos and employees. Handle all required offboarding tasks, such as disabling their accounts, revoking licenses, archiving mailboxes, and wiping assigned devices in it_assets. Document these finished actions in lifecycle_queue, and inform management that each employee has been offboarded.",
        "actions": [
            {
                "name": "filterHrMemos",
                "arguments": {
                    "type": "offboarding"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Parker",
                    "last_name": "Davis"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Remy",
                    "last_name": "White"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0007",
                    "status": "disabled"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0019",
                    "status": "disabled"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0007"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0019"
                },
            },
            {
                "name": "archiveMailbox",
                "arguments": {
                    "employee_id": "emp_0007",
                    "department": "IT"
                },
            },
            {
                "name": "archiveMailbox",
                "arguments": {
                    "employee_id": "emp_0019",
                    "department": "Operations"
                },
            },
            {
                "name": "deviceAssignment",
                "arguments": {
                    "employee_id": "emp_0007",
                    "unassign": true
                },
            },
            {
                "name": "deviceAssignment",
                "arguments": {
                    "employee_id": "emp_0019",
                    "unassign": true
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0007",
                    "memo_id": "memo_0009",
                    "event": "offboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0019",
                    "memo_id": "memo_0012",
                    "event": "offboarding"
                },
            },
            {
                "name": "filterEmployees",
                "arguments": {
                    "manager_id": "None"
                },
            },
            {
                "name": "notify",
                "arguments": {
                    "recipient_ids": [
                        "emp_0001",
                        "emp_0002",
                        "emp_0003",
                        "emp_0004",
                        "emp_0005",
                        "emp_0006",
                        "emp_0009",
                        "emp_0017"
                    ],
                    "summary": "Jordan Kim was offboarded."
                },
            },
            {
                "name": "notify",
                "arguments": {
                    "recipient_ids": [
                        "emp_0001",
                        "emp_0002",
                        "emp_0003",
                        "emp_0004",
                        "emp_0005",
                        "emp_0006",
                        "emp_0009",
                        "emp_0017"
                    ],
                    "summary": "Sawyer Harris was offboarded."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "compliance_check_5",
        "instruction": "You are an AI agent assigned to execute annual compliance checks. Utilize license_assignments, rbac_group_map, and employees to compare roles allocated in the Marketing department with the default licenses in rbac_group_map. Identify and flag any discrepancies, particularly employees who do not have the default licenses. Compile a review packet PDF and log the execution in validation_issues.",
        "actions": [
            {
                "name": "filterEmployees",
                "arguments": {
                    "department": "Marketing"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0002",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0012",
                    "job_title": "Design Lead"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0016",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0018",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0021",
                    "job_title": "Design Lead"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0024",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0025",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0027",
                    "job_title": "Growth Marketer"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0031",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0032",
                    "job_title": "Growth Marketer"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0034",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0041",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "generateReviewAndLog",
                "arguments": {
                    "log_data": "emp_0002 is missing no licenses,emp_0012 is missing no licenses, emp_0016 is missing no licenses, emp_0018 is missing no licenses, emp_0021 is missing no licenses, emp_0024 is missing no licenses, emp_0025 is missing no licenses, emp_0027 is missing no licenses, emp_0031 is missing no licenses, emp_0032 is missing no licenses, emp_0034 is missing no licenses, emp_0041 is missing no licenses"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "track_backlog_5",
        "instruction": "You are an AI agent tasked with overseeing project backlog. Use the backlog_snapshot_open database to develop a report that emphasizes tickets not labeled \"Resolved\". Safeguard the report containing these details. Generate TaskTrack tickets for any unresolved urgent issues with a summary of \"Address ticket_id\".",
        "actions": [
            {
                "name": "getTicketsBacklog",
                "arguments": {
                {}
                },
            },
            {
                "name": "filterTickets",
                "arguments": {
                    "ids": [
                        "T5002",
                        "T5003",
                        "T5004",
                        "T5005",
                        "T5006",
                        "T5009",
                        "T5010",
                        "T5011",
                        "T5012",
                        "T5013",
                        "T5014",
                        "T5016",
                        "T5017",
                        "T5020",
                        "T5021",
                        "T5023",
                        "T5024",
                        "T5025",
                        "T5026",
                        "T5027",
                        "T5028",
                        "T5029",
                        "T5030",
                        "T5031",
                        "T5032",
                        "T5035",
                        "T5036",
                        "T5037",
                        "T5039",
                        "T5042",
                        "T5043",
                        "T5044",
                        "T5046",
                        "T5048",
                        "T5049",
                        "T5050",
                        "T5051",
                        "T5053",
                        "T5054",
                        "T5055",
                        "T5056",
                        "T5058",
                        "T5059",
                        "T5060",
                        "T5061",
                        "T5063"
                    ],
                    "not_status": "Resolved"
                },
            },
            {
                "name": "saveReport",
                "arguments": {
                    "save_data": [
                        "T5002",
                        "T5003",
                        "T5004",
                        "T5005",
                        "T5006",
                        "T5009",
                        "T5010",
                        "T5011",
                        "T5012",
                        "T5013",
                        "T5014",
                        "T5016",
                        "T5017",
                        "T5020",
                        "T5021",
                        "T5023",
                        "T5024",
                        "T5025",
                        "T5026",
                        "T5027",
                        "T5028",
                        "T5029",
                        "T5030",
                        "T5031",
                        "T5032",
                        "T5035",
                        "T5036",
                        "T5037",
                        "T5039",
                        "T5042",
                        "T5043",
                        "T5044",
                        "T5046",
                        "T5048",
                        "T5049",
                        "T5050",
                        "T5051",
                        "T5053",
                        "T5054",
                        "T5055",
                        "T5056",
                        "T5058",
                        "T5059",
                        "T5060",
                        "T5061",
                        "T5063"
                    ]
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5002",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5009",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5011",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5017",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5024",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5029",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5036",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5048",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5049",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5050",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5058",
                    "priority": "P1"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "tool_assignment_5",
        "instruction": "You are an AI agent responsible for providing accounts for a new marketing tool. Allocate app_facebook accounts to all employees in the Marketing department. These accounts need to be standard for their roles, so update the rbac_group_map with this addition. Compile a report detailing the provisioning summary.",
        "actions": [
            {
                "name": "filterEmployees",
                "arguments": {
                    "department": "Marketing"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0002",
                    "app_id": "app_facebook"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0012",
                    "app_id": "app_facebook"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0016",
                    "app_id": "app_facebook"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0018",
                    "app_id": "app_facebook"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0021",
                    "app_id": "app_facebook"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0024",
                    "app_id": "app_facebook"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0025",
                    "app_id": "app_facebook"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0027",
                    "app_id": "app_facebook"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0031",
                    "app_id": "app_facebook"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0032",
                    "app_id": "app_facebook"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0034",
                    "app_id": "app_facebook"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0041",
                    "app_id": "app_facebook"
                },
            },
            {
                "name": "assignRbacLicense",
                "arguments": {
                    "license_id": "app_facebook",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "assignRbacLicense",
                "arguments": {
                    "license_id": "app_facebook",
                    "job_title": "Design Lead"
                },
            },
            {
                "name": "assignRbacLicense",
                "arguments": {
                    "license_id": "app_facebook",
                    "job_title": "Growth Marketer"
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "provisioning",
                    "run_data": [
                        "Added app_facebook account for emp_0002",
                        "Added app_facebook account for emp_0012",
                        "Added app_facebook account for emp_0016",
                        "Added app_facebook account for emp_0018",
                        "Added app_facebook account for emp_0021",
                        "Added app_facebook account for emp_0024",
                        "Added app_facebook account for emp_0025",
                        "Added app_facebook account for emp_0027",
                        "Added app_facebook account for emp_0031",
                        "Added app_facebook account for emp_0032",
                        "Added app_facebook account for emp_0034",
                        "Added app_facebook account for emp_0041"
                    ]
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "sync_lifecycle_5",
        "instruction": "As an AI agent, you are managing the synchronization of user lifecycles. Identify any employees labeled as \"on_leave.\" Also, perform these tasks for Riley Wang. Alter their statuses to disabled in the directory_accounts database, remove licenses in both the license_assignments and license_inventory databases, and inform management that the lifecycle synchronization is complete.",
        "actions": [
            {
                "name": "filterEmployees",
                "arguments": {
                    "status": "on_leave"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Cameron",
                    "last_name": "Wilson"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0004",
                    "status": "disabled"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0019",
                    "status": "disabled"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0032",
                    "status": "disabled"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0011",
                    "status": "disabled"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0004"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0019"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0032"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0011"
                },
            },
            {
                "name": "filterEmployees",
                "arguments": {
                    "manager_id": "None"
                },
            },
            {
                "name": "notify",
                "arguments": {
                    "recipient_ids": [
                        "emp_0001",
                        "emp_0002",
                        "emp_0003",
                        "emp_0004",
                        "emp_0005",
                        "emp_0006",
                        "emp_0009",
                        "emp_0017"
                    ],
                    "summary": "The lifecycles were synchronized."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "service_stats_5",
        "instruction": "As an AI agent responsible for assessing daily service statistics, determine the average time taken to resolve a ticket (avg_open_age_hours: 36.2), as well as the average number of tickets opened (tickets_opened: 1.6667) and closed each day (tickets_closed: 1.2), using ticket data. Inform Jamie Chen (emp_0001), Drew Kumar (emp_0003), and Robin Jones (emp_0005) with the results. Create a pdf report of the findings and record it in validation_issues.",
        "actions": [
            {
                "name": "ticketStatistics",
                "arguments": {
                    "field": "avg_open_age_hours",
                    "type": "avg"
                },
            },
            {
                "name": "ticketStatistics",
                "arguments": {
                    "field": "tickets_opened",
                    "type": "avg"
                },
            },
            {
                "name": "ticketStatistics",
                "arguments": {
                    "field": "tickets_closed",
                    "type": "avg"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Avery",
                    "last_name": "Lee"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Taylor",
                    "last_name": "Patel"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Casey",
                    "last_name": "Smith"
                },
            },
            {
                "name": "notify",
                "arguments": {
                    "recipient_ids": [
                        "emp_0001",
                        "emp_0003",
                        "emp_0005"
                    ],
                    "summary": "The average of avg_open_age_hours is 36.2. The average of tickets_opened is 1.6667. The average of tickets_closed is 1.2."
                },
            },
            {
                "name": "generateReviewAndLog",
                "arguments": {
                    "log_data": "The average of avg_open_age_hours is 36.2. The average of tickets_opened is 1.6667. The average of tickets_closed is 1.2."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "asset_reservations_5",
        "instruction": "You function as an AI agent managing asset reservations. Upon identifying new hires in hr_memos, allocate an available laptop from it_assets to them. Designate those laptops as \"assigned\" and log a completed record in lifecycle_queue.",
        "actions": [
            {
                "name": "filterHrMemos",
                "arguments": {
                    "type": "onboarding"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Finley",
                    "last_name": "Robinson"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "River",
                    "last_name": "Scott"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Alex",
                    "last_name": "Brown"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Cameron",
                    "last_name": "Wilson"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Taylor",
                    "last_name": "Patel"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Avery",
                    "last_name": "Lee"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Jordan",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Drew",
                    "last_name": "Nelson"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0025",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0031",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0008",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0011",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0003",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0001",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0002",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0039",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0025",
                    "memo_id": "memo_0001",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0031",
                    "memo_id": "memo_0002",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0008",
                    "memo_id": "memo_0003",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0011",
                    "memo_id": "memo_0004",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0003",
                    "memo_id": "memo_0005",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0001",
                    "memo_id": "memo_0006",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0002",
                    "memo_id": "memo_0007",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0039",
                    "memo_id": "memo_0008",
                    "event": "onboarding"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "unused_licenses_5",
        "instruction": "Your role is as an AI agent responsible for reclaiming unused software licenses. Verify license_assignments against employees to identify terminated or users on leave. Detach those assignments, update license_inventory to increase available seats, and produce unique PDF reports of the modifications for each user.",
        "actions": [
            {
                "name": "filterEmployees",
                "arguments": {
                    "status": "terminated"
                },
            },
            {
                "name": "filterEmployees",
                "arguments": {
                    "status": "on_leave"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0007"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0033"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0004"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0019"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0032"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0004"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0019"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0032"
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "unassign_licenses",
                    "run_data": [
                        "emp_0007"
                    ]
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "unassign_licenses",
                    "run_data": [
                        "emp_0033"
                    ]
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "unassign_licenses",
                    "run_data": [
                        "emp_0004",
                        "lic_slack_ent",
                        "lic_github_ent",
                        "lic_m365_e3"
                    ]
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "unassign_licenses",
                    "run_data": [
                        "emp_0019",
                        "lic_slack_ent",
                        "lic_m365_e3"
                    ]
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "unassign_licenses",
                    "run_data": [
                        "emp_0032",
                        "lic_salesforce",
                        "lic_slack_ent",
                        "lic_m365_e3"
                    ]
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "onboarding_6",
        "instruction": "HR distributed memos regarding two new hires joining soon, Drew Kumar and Jamie Chen. You should allocate the default licenses from rbac_group_map corresponding to their roles for them to commence work, if they aren't already assigned. Additionally, they require CodeHub Enterprise licenses. Ensure they also have employee accounts and mailboxes if those are missing. Record these modifications in lifecycle_queue. Inform me if you must establish employee accounts and mailboxes.",
        "actions": [
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Taylor",
                    "last_name": "Patel"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Avery",
                    "last_name": "Lee"
                },
            },
            {
                "name": "employeeAccountExists",
                "arguments": {
                    "first_name": "Taylor",
                    "last_name": "Patel"
                },
            },
            {
                "name": "employeeAccountExists",
                "arguments": {
                    "first_name": "Avery",
                    "last_name": "Lee"
                },
            },
            {
                "name": "mailboxExists",
                "arguments": {
                    "employee_id": "emp_0003"
                },
            },
            {
                "name": "mailboxExists",
                "arguments": {
                    "employee_id": "emp_0001"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0003"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0001"
                },
            },
            {
                "name": "filterHrMemos",
                "arguments": {
                    "first_name": "Taylor",
                    "last_name": "Patel"
                },
            },
            {
                "name": "filterHrMemos",
                "arguments": {
                    "first_name": "Avery",
                    "last_name": "Lee"
                },
            },
            {
                "name": "getJobLicenses",
                "arguments": {
                    "job_title": "Ops Coordinator"
                },
            },
            {
                "name": "getJobLicenses",
                "arguments": {
                    "job_title": "HRBP"
                },
            },
            {
                "name": "getLicenseInfo",
                "arguments": {
                    "license_name": "CodeHub Enterprise"
                },
            },
            {
                "name": "getLicenseAvailability",
                "arguments": {
                    "license_id": "lic_github_ent"
                },
            },
            {
                "name": "assignLicenses",
                "arguments": {
                    "employee_id": "emp_0003",
                    "license_ids": [
                        "lic_github_ent"
                    ]
                },
            },
            {
                "name": "getLicenseAvailability",
                "arguments": {
                    "license_id": "lic_github_ent"
                },
            },
            {
                "name": "assignLicenses",
                "arguments": {
                    "employee_id": "emp_0001",
                    "license_ids": [
                        "lic_github_ent"
                    ]
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0003",
                    "memo_id": "memo_0005",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0001",
                    "memo_id": "memo_0006",
                    "event": "onboarding"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "license_allocation_6",
        "instruction": "You are an AI agent responsible for automating software license allocation. By referencing license_inventory and employees, determine users who have upcoming software renewals, specifically those whose last audit exceeds 20 days. Verify that the identified licenses are in active use and update license_inventory with the new audit data. Create a CSV file of underutilized licenses (utilization_rate < 50%). Initiate low priority TaskTrack tickets titled \"Manage license utilization for license_id\" for each underutilized license.",
        "actions": [
            {
                "name": "licenseRequiresRenewal",
                "arguments": {
                    "num_days": 20
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_m365_e3",
                    "status": "active"
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_m365_e5",
                    "status": "active"
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_adobe_cc",
                    "status": "active"
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_github_ent",
                    "status": "active"
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_slack_ent",
                    "status": "active"
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_salesforce",
                    "status": "active"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_m365_e3"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_m365_e5"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_adobe_cc"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_github_ent"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_slack_ent"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_salesforce"
                },
            },
            {
                "name": "filterLicenses",
                "arguments": {
                    "utilization": 0.5
                },
            },
            {
                "name": "exportUnderutilizedLicenses",
                "arguments": {
                    "output_data": [
                        "lic_m365_e5",
                        "lic_adobe_cc",
                        "lic_github_ent",
                        "lic_slack_ent",
                        "lic_salesforce"
                    ]
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "License Allocation",
                    "summary": "Manage license utilization for lic_m365_e5",
                    "priority": "P3"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "License Allocation",
                    "summary": "Manage license utilization for lic_adobe_cc",
                    "priority": "P3"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "License Allocation",
                    "summary": "Manage license utilization for lic_github_ent",
                    "priority": "P3"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "License Allocation",
                    "summary": "Manage license utilization for lic_slack_ent",
                    "priority": "P3"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "License Allocation",
                    "summary": "Manage license utilization for lic_salesforce",
                    "priority": "P3"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "employee_offboarding_6",
        "instruction": "You are an AI agent programmed to automate the process of employee offboarding. Locate employees identified as \"offboarding\" by accessing the hr_memos and employees databases. Coordinate any necessary offboarding tasks, such as disabling their accounts, revoking licenses, archiving mailboxes, and wiping assigned devices in it_assets. Document these completed actions in the lifecycle_queue, and inform management once each employee has been offboarded.",
        "actions": [
            {
                "name": "filterHrMemos",
                "arguments": {
                    "type": "offboarding"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Parker",
                    "last_name": "Davis"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Remy",
                    "last_name": "White"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0007",
                    "status": "disabled"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0019",
                    "status": "disabled"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0007"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0019"
                },
            },
            {
                "name": "archiveMailbox",
                "arguments": {
                    "employee_id": "emp_0007",
                    "department": "IT"
                },
            },
            {
                "name": "archiveMailbox",
                "arguments": {
                    "employee_id": "emp_0019",
                    "department": "Operations"
                },
            },
            {
                "name": "deviceAssignment",
                "arguments": {
                    "employee_id": "emp_0007",
                    "unassign": true
                },
            },
            {
                "name": "deviceAssignment",
                "arguments": {
                    "employee_id": "emp_0019",
                    "unassign": true
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0007",
                    "memo_id": "memo_0009",
                    "event": "offboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0019",
                    "memo_id": "memo_0012",
                    "event": "offboarding"
                },
            },
            {
                "name": "filterEmployees",
                "arguments": {
                    "manager_id": "None"
                },
            },
            {
                "name": "notify",
                "arguments": {
                    "recipient_ids": [
                        "emp_0001",
                        "emp_0002",
                        "emp_0003",
                        "emp_0004",
                        "emp_0005",
                        "emp_0006",
                        "emp_0009",
                        "emp_0017"
                    ],
                    "summary": "Jordan Kim was offboarded."
                },
            },
            {
                "name": "notify",
                "arguments": {
                    "recipient_ids": [
                        "emp_0001",
                        "emp_0002",
                        "emp_0003",
                        "emp_0004",
                        "emp_0005",
                        "emp_0006",
                        "emp_0009",
                        "emp_0017"
                    ],
                    "summary": "Sawyer Harris was offboarded."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "compliance_check_6",
        "instruction": "You are an AI agent intended to conduct quarterly compliance checks. By utilizing license_assignments, rbac_group_map, and employees, compare assigned roles in the Marketing department against the rbac_group_map default licenses. Identify any employees lacking default licenses. Assemble a review packet as a PDF and log the process in validation_issues.",
        "actions": [
            {
                "name": "filterEmployees",
                "arguments": {
                    "department": "Marketing"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0002",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0012",
                    "job_title": "Design Lead"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0016",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0018",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0021",
                    "job_title": "Design Lead"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0024",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0025",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0027",
                    "job_title": "Growth Marketer"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0031",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0032",
                    "job_title": "Growth Marketer"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0034",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0041",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "generateReviewAndLog",
                "arguments": {
                    "log_data": "emp_0002 is missing no licenses,emp_0012 is missing no licenses, emp_0016 is missing no licenses, emp_0018 is missing no licenses, emp_0021 is missing no licenses, emp_0024 is missing no licenses, emp_0025 is missing no licenses, emp_0027 is missing no licenses, emp_0031 is missing no licenses, emp_0032 is missing no licenses, emp_0034 is missing no licenses, emp_0041 is missing no licenses"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "track_backlog_6",
        "instruction": "As an AI agent monitoring project backlog, utilize the backlog_snapshot_open database to generate a report that emphasizes tickets that have not been marked as \"Resolved\". Preserve this report with the detailed findings. For any urgent tickets that remain unresolved, issue TaskTrack tickets, ensuring the summary states \"Address ticket_id\".",
        "actions": [
            {
                "name": "getTicketsBacklog",
                "arguments": {
                {}
                },
            },
            {
                "name": "filterTickets",
                "arguments": {
                    "ids": [
                        "T5002",
                        "T5003",
                        "T5004",
                        "T5005",
                        "T5006",
                        "T5009",
                        "T5010",
                        "T5011",
                        "T5012",
                        "T5013",
                        "T5014",
                        "T5016",
                        "T5017",
                        "T5020",
                        "T5021",
                        "T5023",
                        "T5024",
                        "T5025",
                        "T5026",
                        "T5027",
                        "T5028",
                        "T5029",
                        "T5030",
                        "T5031",
                        "T5032",
                        "T5035",
                        "T5036",
                        "T5037",
                        "T5039",
                        "T5042",
                        "T5043",
                        "T5044",
                        "T5046",
                        "T5048",
                        "T5049",
                        "T5050",
                        "T5051",
                        "T5053",
                        "T5054",
                        "T5055",
                        "T5056",
                        "T5058",
                        "T5059",
                        "T5060",
                        "T5061",
                        "T5063"
                    ],
                    "not_status": "Resolved"
                },
            },
            {
                "name": "saveReport",
                "arguments": {
                    "save_data": [
                        "T5002",
                        "T5003",
                        "T5004",
                        "T5005",
                        "T5006",
                        "T5009",
                        "T5010",
                        "T5011",
                        "T5012",
                        "T5013",
                        "T5014",
                        "T5016",
                        "T5017",
                        "T5020",
                        "T5021",
                        "T5023",
                        "T5024",
                        "T5025",
                        "T5026",
                        "T5027",
                        "T5028",
                        "T5029",
                        "T5030",
                        "T5031",
                        "T5032",
                        "T5035",
                        "T5036",
                        "T5037",
                        "T5039",
                        "T5042",
                        "T5043",
                        "T5044",
                        "T5046",
                        "T5048",
                        "T5049",
                        "T5050",
                        "T5051",
                        "T5053",
                        "T5054",
                        "T5055",
                        "T5056",
                        "T5058",
                        "T5059",
                        "T5060",
                        "T5061",
                        "T5063"
                    ]
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5002",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5009",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5011",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5017",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5024",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5029",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5036",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5048",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5049",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5050",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5058",
                    "priority": "P1"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "tool_assignment_6",
        "instruction": "As an AI agent in charge of setting up accounts for a new marketing tool, ensure that all Marketing department staff receive app_tiktok accounts. These accounts must be standard for the roles, so update the rbac_group_map with the new account details. Compile a report that outlines the app provisioning process.",
        "actions": [
            {
                "name": "filterEmployees",
                "arguments": {
                    "department": "Marketing"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0002",
                    "app_id": "app_tiktok"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0012",
                    "app_id": "app_tiktok"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0016",
                    "app_id": "app_tiktok"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0018",
                    "app_id": "app_tiktok"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0021",
                    "app_id": "app_tiktok"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0024",
                    "app_id": "app_tiktok"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0025",
                    "app_id": "app_tiktok"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0027",
                    "app_id": "app_tiktok"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0031",
                    "app_id": "app_tiktok"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0032",
                    "app_id": "app_tiktok"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0034",
                    "app_id": "app_tiktok"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0041",
                    "app_id": "app_tiktok"
                },
            },
            {
                "name": "assignRbacLicense",
                "arguments": {
                    "license_id": "app_tiktok",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "assignRbacLicense",
                "arguments": {
                    "license_id": "app_tiktok",
                    "job_title": "Design Lead"
                },
            },
            {
                "name": "assignRbacLicense",
                "arguments": {
                    "license_id": "app_tiktok",
                    "job_title": "Growth Marketer"
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "provisioning",
                    "run_data": [
                        "Added app_tiktok account for emp_0002",
                        "Added app_tiktok account for emp_0012",
                        "Added app_tiktok account for emp_0016",
                        "Added app_tiktok account for emp_0018",
                        "Added app_tiktok account for emp_0021",
                        "Added app_tiktok account for emp_0024",
                        "Added app_tiktok account for emp_0025",
                        "Added app_tiktok account for emp_0027",
                        "Added app_tiktok account for emp_0031",
                        "Added app_tiktok account for emp_0032",
                        "Added app_tiktok account for emp_0034",
                        "Added app_tiktok account for emp_0041"
                    ]
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "sync_lifecycle_6",
        "instruction": "Act as an AI agent to synchronize user lifecycle processes. For employees, identify anyone who is labeled as \"on_leave.\" Apply the same updates for Quinn Miller. Modify their statuses to disabled in the directory_accounts database, withdraw licenses in both the license_assignments and license_inventory databases, and inform management that the lifecycle synchronization has been completed.",
        "actions": [
            {
                "name": "filterEmployees",
                "arguments": {
                    "status": "on_leave"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Reese",
                    "last_name": "Anderson"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0004",
                    "status": "disabled"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0019",
                    "status": "disabled"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0032",
                    "status": "disabled"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0012",
                    "status": "disabled"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0004"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0019"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0032"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0012"
                },
            },
            {
                "name": "filterEmployees",
                "arguments": {
                    "manager_id": "None"
                },
            },
            {
                "name": "notify",
                "arguments": {
                    "recipient_ids": [
                        "emp_0001",
                        "emp_0002",
                        "emp_0003",
                        "emp_0004",
                        "emp_0005",
                        "emp_0006",
                        "emp_0009",
                        "emp_0017"
                    ],
                    "summary": "The lifecycles were synchronized."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "service_stats_6",
        "instruction": "As an AI agent, assess daily service statistics. Using ticket data, compute the average time taken to resolve a ticket, as well as the averages of opened and closed tickets daily. Inform Jamie Chen, Sam Tran, and Robin Jones about the results. Produce a pdf report detailing your findings and log it in validation_issues.",
        "actions": [
            {
                "name": "ticketStatistics",
                "arguments": {
                    "field": "avg_open_age_hours",
                    "type": "avg"
                },
            },
            {
                "name": "ticketStatistics",
                "arguments": {
                    "field": "tickets_opened",
                    "type": "avg"
                },
            },
            {
                "name": "ticketStatistics",
                "arguments": {
                    "field": "tickets_closed",
                    "type": "avg"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Avery",
                    "last_name": "Lee"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Morgan",
                    "last_name": "Nguyen"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Casey",
                    "last_name": "Smith"
                },
            },
            {
                "name": "notify",
                "arguments": {
                    "recipient_ids": [
                        "emp_0001",
                        "emp_0004",
                        "emp_0005"
                    ],
                    "summary": "The average of avg_open_age_hours is 36.2. The average of tickets_opened is 1.6667. The average of tickets_closed is 1.2."
                },
            },
            {
                "name": "generateReviewAndLog",
                "arguments": {
                    "log_data": "The average of avg_open_age_hours is 36.2. The average of tickets_opened is 1.6667. The average of tickets_closed is 1.2."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "asset_reservations_6",
        "instruction": "You are an AI agent crafted to oversee asset reservations. For employees with onboarding memos in hr_memos, allocate them an available laptop from it_assets. Label those assets as \"assigned\" and record a completed entry into lifecycle_queue.",
        "actions": [
            {
                "name": "filterHrMemos",
                "arguments": {
                    "type": "onboarding"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Finley",
                    "last_name": "Robinson"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "River",
                    "last_name": "Scott"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Alex",
                    "last_name": "Brown"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Cameron",
                    "last_name": "Wilson"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Taylor",
                    "last_name": "Patel"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Avery",
                    "last_name": "Lee"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Jordan",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Drew",
                    "last_name": "Nelson"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0025",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0031",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0008",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0011",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0003",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0001",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0002",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0039",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0025",
                    "memo_id": "memo_0001",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0031",
                    "memo_id": "memo_0002",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0008",
                    "memo_id": "memo_0003",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0011",
                    "memo_id": "memo_0004",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0003",
                    "memo_id": "memo_0005",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0001",
                    "memo_id": "memo_0006",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0002",
                    "memo_id": "memo_0007",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0039",
                    "memo_id": "memo_0008",
                    "event": "onboarding"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "unused_licenses_6",
        "instruction": "You are an AI agent created to recover unused software licenses. Using license_assignments and employees as a reference, verify for terminated or users on leave. Eliminate those assignments, adjust license_inventory to increase available seats, and create individual pdf reports of the amendments for each user.",
        "actions": [
            {
                "name": "filterEmployees",
                "arguments": {
                    "status": "terminated"
                },
            },
            {
                "name": "filterEmployees",
                "arguments": {
                    "status": "on_leave"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0007"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0033"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0004"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0019"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0032"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0004"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0019"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0032"
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "unassign_licenses",
                    "run_data": [
                        "emp_0007"
                    ]
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "unassign_licenses",
                    "run_data": [
                        "emp_0033"
                    ]
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "unassign_licenses",
                    "run_data": [
                        "emp_0004",
                        "lic_slack_ent",
                        "lic_github_ent",
                        "lic_m365_e3"
                    ]
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "unassign_licenses",
                    "run_data": [
                        "emp_0019",
                        "lic_slack_ent",
                        "lic_m365_e3"
                    ]
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "unassign_licenses",
                    "run_data": [
                        "emp_0032",
                        "lic_salesforce",
                        "lic_slack_ent",
                        "lic_m365_e3"
                    ]
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "onboarding_7",
        "instruction": "HR distributed memos about three upcoming new starters: Casey Liu, Drew Kumar, and Jamie Chen. You will need to assign them the default licenses from rbac_group_map according to their respective roles to commence their work if they don't have them yet. They also require CodeHub Enterprise licenses. Should they lack employee accounts and mailboxes, these will need to be set up. Record these modifications in lifecycle_queue. Inform me if there's a necessity to create employee accounts and mailboxes.",
        "actions": [
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Jordan",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Taylor",
                    "last_name": "Patel"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Avery",
                    "last_name": "Lee"
                },
            },
            {
                "name": "employeeAccountExists",
                "arguments": {
                    "first_name": "Jordan",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "employeeAccountExists",
                "arguments": {
                    "first_name": "Taylor",
                    "last_name": "Patel"
                },
            },
            {
                "name": "employeeAccountExists",
                "arguments": {
                    "first_name": "Avery",
                    "last_name": "Lee"
                },
            },
            {
                "name": "mailboxExists",
                "arguments": {
                    "employee_id": "emp_0002"
                },
            },
            {
                "name": "mailboxExists",
                "arguments": {
                    "employee_id": "emp_0003"
                },
            },
            {
                "name": "mailboxExists",
                "arguments": {
                    "employee_id": "emp_0001"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0002"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0003"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0001"
                },
            },
            {
                "name": "filterHrMemos",
                "arguments": {
                    "first_name": "Jordan",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "filterHrMemos",
                "arguments": {
                    "first_name": "Taylor",
                    "last_name": "Patel"
                },
            },
            {
                "name": "filterHrMemos",
                "arguments": {
                    "first_name": "Avery",
                    "last_name": "Lee"
                },
            },
            {
                "name": "getJobLicenses",
                "arguments": {
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "getJobLicenses",
                "arguments": {
                    "job_title": "Ops Coordinator"
                },
            },
            {
                "name": "getJobLicenses",
                "arguments": {
                    "job_title": "HRBP"
                },
            },
            {
                "name": "getLicenseInfo",
                "arguments": {
                    "license_name": "CodeHub Enterprise"
                },
            },
            {
                "name": "getLicenseAvailability",
                "arguments": {
                    "license_id": "lic_github_ent"
                },
            },
            {
                "name": "assignLicenses",
                "arguments": {
                    "employee_id": "emp_0002",
                    "license_ids": [
                        "lic_github_ent"
                    ]
                },
            },
            {
                "name": "getLicenseAvailability",
                "arguments": {
                    "license_id": "lic_github_ent"
                },
            },
            {
                "name": "assignLicenses",
                "arguments": {
                    "employee_id": "emp_0003",
                    "license_ids": [
                        "lic_github_ent"
                    ]
                },
            },
            {
                "name": "getLicenseAvailability",
                "arguments": {
                    "license_id": "lic_github_ent"
                },
            },
            {
                "name": "assignLicenses",
                "arguments": {
                    "employee_id": "emp_0001",
                    "license_ids": [
                        "lic_github_ent"
                    ]
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0002",
                    "memo_id": "memo_0007",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0003",
                    "memo_id": "memo_0005",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0001",
                    "memo_id": "memo_0006",
                    "event": "onboarding"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "license_allocation_7",
        "instruction": "Your role as an AI agent involves automating the allocation of software licenses. Utilize license_inventory and employees data to pinpoint users whose software renewals are imminent, signaled by the last audit being over 10 days old. Ensure that the identified licenses are in active use and update license_inventory with the latest audit information. Create a CSV containing details of underutilized licenses (utilization_rate < 30%). Set up low-priority TaskTrack tickets titled \"Manage license utilization for license_id\" for every underutilized license.",
        "actions": [
            {
                "name": "licenseRequiresRenewal",
                "arguments": {
                    "num_days": 10
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_m365_e3",
                    "status": "active"
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_m365_e5",
                    "status": "active"
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_adobe_cc",
                    "status": "active"
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_github_ent",
                    "status": "active"
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_slack_ent",
                    "status": "active"
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_salesforce",
                    "status": "active"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_m365_e3"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_m365_e5"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_adobe_cc"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_github_ent"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_slack_ent"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_salesforce"
                },
            },
            {
                "name": "filterLicenses",
                "arguments": {
                    "utilization": 0.3
                },
            },
            {
                "name": "exportUnderutilizedLicenses",
                "arguments": {
                    "output_data": [
                        "lic_m365_e5",
                        "lic_adobe_cc",
                        "lic_github_ent",
                        "lic_salesforce"
                    ]
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "License Allocation",
                    "summary": "Manage license utilization for lic_m365_e5",
                    "priority": "P3"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "License Allocation",
                    "summary": "Manage license utilization for lic_adobe_cc",
                    "priority": "P3"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "License Allocation",
                    "summary": "Manage license utilization for lic_github_ent",
                    "priority": "P3"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "License Allocation",
                    "summary": "Manage license utilization for lic_salesforce",
                    "priority": "P3"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "employee_offboarding_7",
        "instruction": "Your role as an AI agent is to streamline the employee offboarding process. Locate all employees labeled \"offboarding\" within the hr_memos and employees databases. Carry out the required offboarding steps, which involve deactivating their accounts, removing licenses, archiving email accounts, and erasing data from allocated devices found in it_assets. Document these completed actions in lifecycle_queue, and inform management of each employee's offboarding completion.",
        "actions": [
            {
                "name": "filterHrMemos",
                "arguments": {
                    "type": "offboarding"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Parker",
                    "last_name": "Davis"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Remy",
                    "last_name": "White"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0007",
                    "status": "disabled"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0019",
                    "status": "disabled"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0007"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0019"
                },
            },
            {
                "name": "archiveMailbox",
                "arguments": {
                    "employee_id": "emp_0007",
                    "department": "IT"
                },
            },
            {
                "name": "archiveMailbox",
                "arguments": {
                    "employee_id": "emp_0019",
                    "department": "Operations"
                },
            },
            {
                "name": "deviceAssignment",
                "arguments": {
                    "employee_id": "emp_0007",
                    "unassign": true
                },
            },
            {
                "name": "deviceAssignment",
                "arguments": {
                    "employee_id": "emp_0019",
                    "unassign": true
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0007",
                    "memo_id": "memo_0009",
                    "event": "offboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0019",
                    "memo_id": "memo_0012",
                    "event": "offboarding"
                },
            },
            {
                "name": "filterEmployees",
                "arguments": {
                    "manager_id": "None"
                },
            },
            {
                "name": "notify",
                "arguments": {
                    "recipient_ids": [
                        "emp_0001",
                        "emp_0002",
                        "emp_0003",
                        "emp_0004",
                        "emp_0005",
                        "emp_0006",
                        "emp_0009",
                        "emp_0017"
                    ],
                    "summary": "Jordan Kim was offboarded."
                },
            },
            {
                "name": "notify",
                "arguments": {
                    "recipient_ids": [
                        "emp_0001",
                        "emp_0002",
                        "emp_0003",
                        "emp_0004",
                        "emp_0005",
                        "emp_0006",
                        "emp_0009",
                        "emp_0017"
                    ],
                    "summary": "Sawyer Harris was offboarded."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "compliance_check_7",
        "instruction": "Your function as an AI agent involves conducting quarterly compliance evaluations. Utilizing license_assignments, rbac_group_map, and employees, assess the roles assigned in the Marketing department against the standard licenses in rbac_group_map. Identify and mark any discrepancies, particularly employees lacking the standard licenses. Create a review packet in PDF format and log the operation in validation_issues.",
        "actions": [
            {
                "name": "filterEmployees",
                "arguments": {
                    "department": "Marketing"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0002",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0012",
                    "job_title": "Design Lead"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0016",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0018",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0021",
                    "job_title": "Design Lead"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0024",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0025",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0027",
                    "job_title": "Growth Marketer"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0031",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0032",
                    "job_title": "Growth Marketer"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0034",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0041",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "generateReviewAndLog",
                "arguments": {
                    "log_data": "emp_0002 is missing no licenses,emp_0012 is missing no licenses, emp_0016 is missing no licenses, emp_0018 is missing no licenses, emp_0021 is missing no licenses, emp_0024 is missing no licenses, emp_0025 is missing no licenses, emp_0027 is missing no licenses, emp_0031 is missing no licenses, emp_0032 is missing no licenses, emp_0034 is missing no licenses, emp_0041 is missing no licenses"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "track_backlog_7",
        "instruction": "As an AI agent monitoring the project backlog, consult the backlog_snapshot_open database to generate a report that emphasizes tickets not marked as \"Resolved\". Store a report documenting these results. Submit TaskTrack tickets for any unresolved urgent tickets, summarizing each as \"Address ticket_id\".",
        "actions": [
            {
                "name": "getTicketsBacklog",
                "arguments": {
                {}
                },
            },
            {
                "name": "filterTickets",
                "arguments": {
                    "ids": [
                        "T5002",
                        "T5003",
                        "T5004",
                        "T5005",
                        "T5006",
                        "T5009",
                        "T5010",
                        "T5011",
                        "T5012",
                        "T5013",
                        "T5014",
                        "T5016",
                        "T5017",
                        "T5020",
                        "T5021",
                        "T5023",
                        "T5024",
                        "T5025",
                        "T5026",
                        "T5027",
                        "T5028",
                        "T5029",
                        "T5030",
                        "T5031",
                        "T5032",
                        "T5035",
                        "T5036",
                        "T5037",
                        "T5039",
                        "T5042",
                        "T5043",
                        "T5044",
                        "T5046",
                        "T5048",
                        "T5049",
                        "T5050",
                        "T5051",
                        "T5053",
                        "T5054",
                        "T5055",
                        "T5056",
                        "T5058",
                        "T5059",
                        "T5060",
                        "T5061",
                        "T5063"
                    ],
                    "not_status": "Resolved"
                },
            },
            {
                "name": "saveReport",
                "arguments": {
                    "save_data": [
                        "T5002",
                        "T5003",
                        "T5004",
                        "T5005",
                        "T5006",
                        "T5009",
                        "T5010",
                        "T5011",
                        "T5012",
                        "T5013",
                        "T5014",
                        "T5016",
                        "T5017",
                        "T5020",
                        "T5021",
                        "T5023",
                        "T5024",
                        "T5025",
                        "T5026",
                        "T5027",
                        "T5028",
                        "T5029",
                        "T5030",
                        "T5031",
                        "T5032",
                        "T5035",
                        "T5036",
                        "T5037",
                        "T5039",
                        "T5042",
                        "T5043",
                        "T5044",
                        "T5046",
                        "T5048",
                        "T5049",
                        "T5050",
                        "T5051",
                        "T5053",
                        "T5054",
                        "T5055",
                        "T5056",
                        "T5058",
                        "T5059",
                        "T5060",
                        "T5061",
                        "T5063"
                    ]
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5002",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5009",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5011",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5017",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5024",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5029",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5036",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5048",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5049",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5050",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5058",
                    "priority": "P1"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "tool_assignment_7",
        "instruction": "As an AI agent managing account provisioning for a new marketing tool, allocate app_instagram accounts to all staff members in the Marketing department. Since these accounts are standard for these roles, update the rbac_group_map with the new account data. Compile a report detailing the app provisioning process.",
        "actions": [
            {
                "name": "filterEmployees",
                "arguments": {
                    "department": "Marketing"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0002",
                    "app_id": "app_instagram"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0012",
                    "app_id": "app_instagram"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0016",
                    "app_id": "app_instagram"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0018",
                    "app_id": "app_instagram"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0021",
                    "app_id": "app_instagram"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0024",
                    "app_id": "app_instagram"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0025",
                    "app_id": "app_instagram"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0027",
                    "app_id": "app_instagram"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0031",
                    "app_id": "app_instagram"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0032",
                    "app_id": "app_instagram"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0034",
                    "app_id": "app_instagram"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0041",
                    "app_id": "app_instagram"
                },
            },
            {
                "name": "assignRbacLicense",
                "arguments": {
                    "license_id": "app_instagram",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "assignRbacLicense",
                "arguments": {
                    "license_id": "app_instagram",
                    "job_title": "Design Lead"
                },
            },
            {
                "name": "assignRbacLicense",
                "arguments": {
                    "license_id": "app_instagram",
                    "job_title": "Growth Marketer"
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "provisioning",
                    "run_data": [
                        "Added app_instagram account for emp_0002",
                        "Added app_instagram account for emp_0012",
                        "Added app_instagram account for emp_0016",
                        "Added app_instagram account for emp_0018",
                        "Added app_instagram account for emp_0021",
                        "Added app_instagram account for emp_0024",
                        "Added app_instagram account for emp_0025",
                        "Added app_instagram account for emp_0027",
                        "Added app_instagram account for emp_0031",
                        "Added app_instagram account for emp_0032",
                        "Added app_instagram account for emp_0034",
                        "Added app_instagram account for emp_0041"
                    ]
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "sync_lifecycle_7",
        "instruction": "As an AI agent managing user lifecycle synchronization, identify employees designated as \"on_leave.\" Ensure these procedures are performed for Cameron Patel too. Adjust their directory_accounts database statuses to disabled, remove licenses from the license_assignments and license_inventory databases, and inform management that the user lifecycles have been synchronized.",
        "actions": [
            {
                "name": "filterEmployees",
                "arguments": {
                    "status": "on_leave"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Emerson",
                    "last_name": "Thomas"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0004",
                    "status": "disabled"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0019",
                    "status": "disabled"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0032",
                    "status": "disabled"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0013",
                    "status": "disabled"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0004"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0019"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0032"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0013"
                },
            },
            {
                "name": "filterEmployees",
                "arguments": {
                    "manager_id": "None"
                },
            },
            {
                "name": "notify",
                "arguments": {
                    "recipient_ids": [
                        "emp_0001",
                        "emp_0002",
                        "emp_0003",
                        "emp_0004",
                        "emp_0005",
                        "emp_0006",
                        "emp_0009",
                        "emp_0017"
                    ],
                    "summary": "The lifecycles were synchronized."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "service_stats_7",
        "instruction": "Act as an AI agent assessing daily service statistics. Determine the average resolution time for a ticket, the average number of tickets opened, and the average number of tickets closed daily using ticket data. Communicate your results to Casey Liu, Drew Kumar, and Sam Tran. Create a PDF report with your findings and record it in validation_issues.",
        "actions": [
            {
                "name": "ticketStatistics",
                "arguments": {
                    "field": "avg_open_age_hours",
                    "type": "avg"
                },
            },
            {
                "name": "ticketStatistics",
                "arguments": {
                    "field": "tickets_opened",
                    "type": "avg"
                },
            },
            {
                "name": "ticketStatistics",
                "arguments": {
                    "field": "tickets_closed",
                    "type": "avg"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Jordan",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Taylor",
                    "last_name": "Patel"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Morgan",
                    "last_name": "Nguyen"
                },
            },
            {
                "name": "notify",
                "arguments": {
                    "recipient_ids": [
                        "emp_0002",
                        "emp_0003",
                        "emp_0004"
                    ],
                    "summary": "The average of avg_open_age_hours is 36.2. The average of tickets_opened is 1.6667. The average of tickets_closed is 1.2."
                },
            },
            {
                "name": "generateReviewAndLog",
                "arguments": {
                    "log_data": "The average of avg_open_age_hours is 36.2. The average of tickets_opened is 1.6667. The average of tickets_closed is 1.2."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "asset_reservations_7",
        "instruction": "You are an AI agent tasked with managing asset reservations. Upon the appearance of new hires in hr_memos, allocate an unused laptop from it_assets to them. Update those assets to \"assigned\" and log a completed record in lifecycle_queue.",
        "actions": [
            {
                "name": "filterHrMemos",
                "arguments": {
                    "type": "onboarding"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Finley",
                    "last_name": "Robinson"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "River",
                    "last_name": "Scott"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Alex",
                    "last_name": "Brown"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Cameron",
                    "last_name": "Wilson"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Taylor",
                    "last_name": "Patel"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Avery",
                    "last_name": "Lee"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Jordan",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Drew",
                    "last_name": "Nelson"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0025",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0031",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0008",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0011",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0003",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0001",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0002",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0039",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0025",
                    "memo_id": "memo_0001",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0031",
                    "memo_id": "memo_0002",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0008",
                    "memo_id": "memo_0003",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0011",
                    "memo_id": "memo_0004",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0003",
                    "memo_id": "memo_0005",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0001",
                    "memo_id": "memo_0006",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0002",
                    "memo_id": "memo_0007",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0039",
                    "memo_id": "memo_0008",
                    "event": "onboarding"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "unused_licenses_7",
        "instruction": "You are an AI agent responsible for reclaiming unused software licenses. Match license_assignments with employees to identify those who have been terminated or are on leave. Eliminate those assignments, update license_inventory to increase seat availability, and create individual PDF reports of the changes for each user.",
        "actions": [
            {
                "name": "filterEmployees",
                "arguments": {
                    "status": "terminated"
                },
            },
            {
                "name": "filterEmployees",
                "arguments": {
                    "status": "on_leave"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0007"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0033"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0004"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0019"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0032"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0004"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0019"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0032"
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "unassign_licenses",
                    "run_data": [
                        "emp_0007"
                    ]
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "unassign_licenses",
                    "run_data": [
                        "emp_0033"
                    ]
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "unassign_licenses",
                    "run_data": [
                        "emp_0004",
                        "lic_slack_ent",
                        "lic_github_ent",
                        "lic_m365_e3"
                    ]
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "unassign_licenses",
                    "run_data": [
                        "emp_0019",
                        "lic_slack_ent",
                        "lic_m365_e3"
                    ]
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "unassign_licenses",
                    "run_data": [
                        "emp_0032",
                        "lic_salesforce",
                        "lic_slack_ent",
                        "lic_m365_e3"
                    ]
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "onboarding_8",
        "instruction": "HR distributed memos regarding the upcoming start of three new employees: Briar Campbell, Casey Liu, and Drew Kumar. Please handle the assignment of default licenses from rbac_group_map relevant to their roles to ensure they can begin working, if they are not already equipped. Additionally, they must be provided with CodeHub Enterprise licenses. In cases where they do not yet have employee accounts and mailboxes, these will need to be set up as well. Record these updates in lifecycle_queue. Inform me if it's necessary to create employee accounts and mailboxes.",
        "actions": [
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Drew",
                    "last_name": "Nelson"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Jordan",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Taylor",
                    "last_name": "Patel"
                },
            },
            {
                "name": "employeeAccountExists",
                "arguments": {
                    "first_name": "Drew",
                    "last_name": "Nelson"
                },
            },
            {
                "name": "employeeAccountExists",
                "arguments": {
                    "first_name": "Jordan",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "employeeAccountExists",
                "arguments": {
                    "first_name": "Taylor",
                    "last_name": "Patel"
                },
            },
            {
                "name": "mailboxExists",
                "arguments": {
                    "employee_id": "emp_0039"
                },
            },
            {
                "name": "mailboxExists",
                "arguments": {
                    "employee_id": "emp_0002"
                },
            },
            {
                "name": "mailboxExists",
                "arguments": {
                    "employee_id": "emp_0003"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0039"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0002"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0003"
                },
            },
            {
                "name": "filterHrMemos",
                "arguments": {
                    "first_name": "Drew",
                    "last_name": "Nelson"
                },
            },
            {
                "name": "filterHrMemos",
                "arguments": {
                    "first_name": "Jordan",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "filterHrMemos",
                "arguments": {
                    "first_name": "Taylor",
                    "last_name": "Patel"
                },
            },
            {
                "name": "getJobLicenses",
                "arguments": {
                    "job_title": "Support Manager"
                },
            },
            {
                "name": "getJobLicenses",
                "arguments": {
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "getJobLicenses",
                "arguments": {
                    "job_title": "Ops Coordinator"
                },
            },
            {
                "name": "getLicenseInfo",
                "arguments": {
                    "license_name": "CodeHub Enterprise"
                },
            },
            {
                "name": "getLicenseAvailability",
                "arguments": {
                    "license_id": "lic_github_ent"
                },
            },
            {
                "name": "assignLicenses",
                "arguments": {
                    "employee_id": "emp_0039",
                    "license_ids": [
                        "lic_github_ent"
                    ]
                },
            },
            {
                "name": "getLicenseAvailability",
                "arguments": {
                    "license_id": "lic_github_ent"
                },
            },
            {
                "name": "assignLicenses",
                "arguments": {
                    "employee_id": "emp_0002",
                    "license_ids": [
                        "lic_github_ent"
                    ]
                },
            },
            {
                "name": "getLicenseAvailability",
                "arguments": {
                    "license_id": "lic_github_ent"
                },
            },
            {
                "name": "assignLicenses",
                "arguments": {
                    "employee_id": "emp_0003",
                    "license_ids": [
                        "lic_github_ent"
                    ]
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0039",
                    "memo_id": "memo_0008",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0002",
                    "memo_id": "memo_0007",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0003",
                    "memo_id": "memo_0005",
                    "event": "onboarding"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "license_allocation_8",
        "instruction": "You function as an AI agent dedicated to automating software license allocation. With the assistance of license_inventory and employees, identify users whose software renewals are approaching, indicated when their last audit exceeds 10 days. Verify the active use of the identified licenses and revise license_inventory with the updated audit. Compile a CSV for licenses with low utilization (utilization_rate < 40%). Open low priority TaskTrack tickets for \"Manage license utilization for license_id\" concerning each underutilized license.",
        "actions": [
            {
                "name": "licenseRequiresRenewal",
                "arguments": {
                    "num_days": 10
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_m365_e3",
                    "status": "active"
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_m365_e5",
                    "status": "active"
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_adobe_cc",
                    "status": "active"
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_github_ent",
                    "status": "active"
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_slack_ent",
                    "status": "active"
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_salesforce",
                    "status": "active"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_m365_e3"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_m365_e5"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_adobe_cc"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_github_ent"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_slack_ent"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_salesforce"
                },
            },
            {
                "name": "filterLicenses",
                "arguments": {
                    "utilization": 0.4
                },
            },
            {
                "name": "exportUnderutilizedLicenses",
                "arguments": {
                    "output_data": [
                        "lic_m365_e5",
                        "lic_adobe_cc",
                        "lic_github_ent",
                        "lic_salesforce"
                    ]
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "License Allocation",
                    "summary": "Manage license utilization for lic_m365_e5",
                    "priority": "P3"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "License Allocation",
                    "summary": "Manage license utilization for lic_adobe_cc",
                    "priority": "P3"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "License Allocation",
                    "summary": "Manage license utilization for lic_github_ent",
                    "priority": "P3"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "License Allocation",
                    "summary": "Manage license utilization for lic_salesforce",
                    "priority": "P3"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "employee_offboarding_8",
        "instruction": "You are an AI agent designed for managing employee offboarding. Identify the employees indicated as \"offboarding\" through hr_memos and employees. Conduct the necessary offboarding tasks, such as disabling their accounts, revoking licenses, archiving mailboxes, and wiping assigned devices in it_assets. Document these tasks in lifecycle_queue and notify management that each employee has been offboarded.",
        "actions": [
            {
                "name": "filterHrMemos",
                "arguments": {
                    "type": "offboarding"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Parker",
                    "last_name": "Davis"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Remy",
                    "last_name": "White"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0007",
                    "status": "disabled"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0019",
                    "status": "disabled"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0007"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0019"
                },
            },
            {
                "name": "archiveMailbox",
                "arguments": {
                    "employee_id": "emp_0007",
                    "department": "IT"
                },
            },
            {
                "name": "archiveMailbox",
                "arguments": {
                    "employee_id": "emp_0019",
                    "department": "Operations"
                },
            },
            {
                "name": "deviceAssignment",
                "arguments": {
                    "employee_id": "emp_0007",
                    "unassign": true
                },
            },
            {
                "name": "deviceAssignment",
                "arguments": {
                    "employee_id": "emp_0019",
                    "unassign": true
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0007",
                    "memo_id": "memo_0009",
                    "event": "offboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0019",
                    "memo_id": "memo_0012",
                    "event": "offboarding"
                },
            },
            {
                "name": "filterEmployees",
                "arguments": {
                    "manager_id": "None"
                },
            },
            {
                "name": "notify",
                "arguments": {
                    "recipient_ids": [
                        "emp_0001",
                        "emp_0002",
                        "emp_0003",
                        "emp_0004",
                        "emp_0005",
                        "emp_0006",
                        "emp_0009",
                        "emp_0017"
                    ],
                    "summary": "Jordan Kim was offboarded."
                },
            },
            {
                "name": "notify",
                "arguments": {
                    "recipient_ids": [
                        "emp_0001",
                        "emp_0002",
                        "emp_0003",
                        "emp_0004",
                        "emp_0005",
                        "emp_0006",
                        "emp_0009",
                        "emp_0017"
                    ],
                    "summary": "Sawyer Harris was offboarded."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "compliance_check_8",
        "instruction": "You are an AI agent overseeing quarterly compliance checks. Utilizing license_assignments, rbac_group_map, and employees, examine assigned roles in the Marketing department against the default licenses in rbac_group_map. Mark any employees who are missing default licenses. Compile a review packet PDF and log the run in validation_issues.",
        "actions": [
            {
                "name": "filterEmployees",
                "arguments": {
                    "department": "Marketing"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0002",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0012",
                    "job_title": "Design Lead"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0016",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0018",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0021",
                    "job_title": "Design Lead"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0024",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0025",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0027",
                    "job_title": "Growth Marketer"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0031",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0032",
                    "job_title": "Growth Marketer"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0034",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0041",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "generateReviewAndLog",
                "arguments": {
                    "log_data": "emp_0002 is missing no licenses,emp_0012 is missing no licenses, emp_0016 is missing no licenses, emp_0018 is missing no licenses, emp_0021 is missing no licenses, emp_0024 is missing no licenses, emp_0025 is missing no licenses, emp_0027 is missing no licenses, emp_0031 is missing no licenses, emp_0032 is missing no licenses, emp_0034 is missing no licenses, emp_0041 is missing no licenses"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "track_backlog_8",
        "instruction": "You are an AI agent intended to monitor project backlog. Utilize the backlog_snapshot_open database to generate a report that emphasizes tickets which are not \"Resolved\". Store the report including these details. File TaskTrack tickets for any unresolved urgent issues with a summary as \"Address ticket_id\".",
        "actions": [
            {
                "name": "getTicketsBacklog",
                "arguments": {
                {}
                },
            },
            {
                "name": "filterTickets",
                "arguments": {
                    "ids": [
                        "T5002",
                        "T5003",
                        "T5004",
                        "T5005",
                        "T5006",
                        "T5009",
                        "T5010",
                        "T5011",
                        "T5012",
                        "T5013",
                        "T5014",
                        "T5016",
                        "T5017",
                        "T5020",
                        "T5021",
                        "T5023",
                        "T5024",
                        "T5025",
                        "T5026",
                        "T5027",
                        "T5028",
                        "T5029",
                        "T5030",
                        "T5031",
                        "T5032",
                        "T5035",
                        "T5036",
                        "T5037",
                        "T5039",
                        "T5042",
                        "T5043",
                        "T5044",
                        "T5046",
                        "T5048",
                        "T5049",
                        "T5050",
                        "T5051",
                        "T5053",
                        "T5054",
                        "T5055",
                        "T5056",
                        "T5058",
                        "T5059",
                        "T5060",
                        "T5061",
                        "T5063"
                    ],
                    "not_status": "Resolved"
                },
            },
            {
                "name": "saveReport",
                "arguments": {
                    "save_data": [
                        "T5002",
                        "T5003",
                        "T5004",
                        "T5005",
                        "T5006",
                        "T5009",
                        "T5010",
                        "T5011",
                        "T5012",
                        "T5013",
                        "T5014",
                        "T5016",
                        "T5017",
                        "T5020",
                        "T5021",
                        "T5023",
                        "T5024",
                        "T5025",
                        "T5026",
                        "T5027",
                        "T5028",
                        "T5029",
                        "T5030",
                        "T5031",
                        "T5032",
                        "T5035",
                        "T5036",
                        "T5037",
                        "T5039",
                        "T5042",
                        "T5043",
                        "T5044",
                        "T5046",
                        "T5048",
                        "T5049",
                        "T5050",
                        "T5051",
                        "T5053",
                        "T5054",
                        "T5055",
                        "T5056",
                        "T5058",
                        "T5059",
                        "T5060",
                        "T5061",
                        "T5063"
                    ]
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5002",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5009",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5011",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5017",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5024",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5029",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5036",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5048",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5049",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5050",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5058",
                    "priority": "P1"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "tool_assignment_8",
        "instruction": "You are an AI agent handling the provisioning of accounts for a new marketing tool. Allocate app_reddit accounts to all employees within the Marketing department. As these accounts should be standard for these roles, update the rbac_group_map with this new account information. Compile a report that summarizes the app provisioning.",
        "actions": [
            {
                "name": "filterEmployees",
                "arguments": {
                    "department": "Marketing"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0002",
                    "app_id": "app_reddit"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0012",
                    "app_id": "app_reddit"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0016",
                    "app_id": "app_reddit"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0018",
                    "app_id": "app_reddit"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0021",
                    "app_id": "app_reddit"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0024",
                    "app_id": "app_reddit"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0025",
                    "app_id": "app_reddit"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0027",
                    "app_id": "app_reddit"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0031",
                    "app_id": "app_reddit"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0032",
                    "app_id": "app_reddit"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0034",
                    "app_id": "app_reddit"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0041",
                    "app_id": "app_reddit"
                },
            },
            {
                "name": "assignRbacLicense",
                "arguments": {
                    "license_id": "app_reddit",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "assignRbacLicense",
                "arguments": {
                    "license_id": "app_reddit",
                    "job_title": "Design Lead"
                },
            },
            {
                "name": "assignRbacLicense",
                "arguments": {
                    "license_id": "app_reddit",
                    "job_title": "Growth Marketer"
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "provisioning",
                    "run_data": [
                        "Added app_reddit account for emp_0002",
                        "Added app_reddit account for emp_0012",
                        "Added app_reddit account for emp_0016",
                        "Added app_reddit account for emp_0018",
                        "Added app_reddit account for emp_0021",
                        "Added app_reddit account for emp_0024",
                        "Added app_reddit account for emp_0025",
                        "Added app_reddit account for emp_0027",
                        "Added app_reddit account for emp_0031",
                        "Added app_reddit account for emp_0032",
                        "Added app_reddit account for emp_0034",
                        "Added app_reddit account for emp_0041"
                    ]
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "sync_lifecycle_8",
        "instruction": "Act as an AI agent responsible for coordinating user lifecycle synchronization. Identify any employees labeled as \"on_leave.\" This includes Emerson Davis as well. Adjust their statuses to disabled in the directory_accounts database, remove licenses in both the license_assignments and license_inventory databases, and inform management that the lifecycles have been synchronized.",
        "actions": [
            {
                "name": "filterEmployees",
                "arguments": {
                    "status": "on_leave"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Peyton",
                    "last_name": "Taylor"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0004",
                    "status": "disabled"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0019",
                    "status": "disabled"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0032",
                    "status": "disabled"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0014",
                    "status": "disabled"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0004"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0019"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0032"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0014"
                },
            },
            {
                "name": "filterEmployees",
                "arguments": {
                    "manager_id": "None"
                },
            },
            {
                "name": "notify",
                "arguments": {
                    "recipient_ids": [
                        "emp_0001",
                        "emp_0002",
                        "emp_0003",
                        "emp_0004",
                        "emp_0005",
                        "emp_0006",
                        "emp_0009",
                        "emp_0017"
                    ],
                    "summary": "The lifecycles were synchronized."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "service_stats_8",
        "instruction": "Function as an AI agent tasked with assessing daily service stats. Utilize tickets to determine the average time to complete a ticket, as well as the average number of tickets opened and closed each day. Report your conclusions to Casey Liu, Drew Kumar, and Robin Jones. Create a pdf report with your findings and record it in validation_issues.",
        "actions": [
            {
                "name": "ticketStatistics",
                "arguments": {
                    "field": "avg_open_age_hours",
                    "type": "avg"
                },
            },
            {
                "name": "ticketStatistics",
                "arguments": {
                    "field": "tickets_opened",
                    "type": "avg"
                },
            },
            {
                "name": "ticketStatistics",
                "arguments": {
                    "field": "tickets_closed",
                    "type": "avg"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Jordan",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Taylor",
                    "last_name": "Patel"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Casey",
                    "last_name": "Smith"
                },
            },
            {
                "name": "notify",
                "arguments": {
                    "recipient_ids": [
                        "emp_0002",
                        "emp_0003",
                        "emp_0005"
                    ],
                    "summary": "The average of avg_open_age_hours is 36.2. The average of tickets_opened is 1.6667. The average of tickets_closed is 1.2."
                },
            },
            {
                "name": "generateReviewAndLog",
                "arguments": {
                    "log_data": "The average of avg_open_age_hours is 36.2. The average of tickets_opened is 1.6667. The average of tickets_closed is 1.2."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "asset_reservations_8",
        "instruction": "You are an AI agent designed to oversee asset reservations. When new hires are indicated in hr_memos, allocate an available laptop from it_assets to them. Designate those laptops as \"assigned\" and enter a completed record into lifecycle_queue.",
        "actions": [
            {
                "name": "filterHrMemos",
                "arguments": {
                    "type": "onboarding"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Finley",
                    "last_name": "Robinson"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "River",
                    "last_name": "Scott"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Alex",
                    "last_name": "Brown"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Cameron",
                    "last_name": "Wilson"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Taylor",
                    "last_name": "Patel"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Avery",
                    "last_name": "Lee"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Jordan",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Drew",
                    "last_name": "Nelson"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0025",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0031",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0008",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0011",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0003",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0001",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0002",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0039",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0025",
                    "memo_id": "memo_0001",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0031",
                    "memo_id": "memo_0002",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0008",
                    "memo_id": "memo_0003",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0011",
                    "memo_id": "memo_0004",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0003",
                    "memo_id": "memo_0005",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0001",
                    "memo_id": "memo_0006",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0002",
                    "memo_id": "memo_0007",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0039",
                    "memo_id": "memo_0008",
                    "event": "onboarding"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "unused_licenses_8",
        "instruction": "You are an AI agent responsible for reclaiming unused software licenses. Verify license_assignments against employees for those terminated or users on leave. Detach those assignments, update license_inventory to reflect available seats, and produce unique pdf reports of the changes for each user.",
        "actions": [
            {
                "name": "filterEmployees",
                "arguments": {
                    "status": "terminated"
                },
            },
            {
                "name": "filterEmployees",
                "arguments": {
                    "status": "on_leave"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0007"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0033"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0004"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0019"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0032"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0004"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0019"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0032"
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "unassign_licenses",
                    "run_data": [
                        "emp_0007"
                    ]
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "unassign_licenses",
                    "run_data": [
                        "emp_0033"
                    ]
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "unassign_licenses",
                    "run_data": [
                        "emp_0004",
                        "lic_slack_ent",
                        "lic_github_ent",
                        "lic_m365_e3"
                    ]
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "unassign_licenses",
                    "run_data": [
                        "emp_0019",
                        "lic_slack_ent",
                        "lic_m365_e3"
                    ]
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "unassign_licenses",
                    "run_data": [
                        "emp_0032",
                        "lic_salesforce",
                        "lic_slack_ent",
                        "lic_m365_e3"
                    ]
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "onboarding_9",
        "instruction": "HR distributed memos regarding the upcoming start of three individuals, Briar Campbell, Casey Liu, and Jamie Chen. You should allocate the default licenses from rbac_group_map based on their respective job roles so they can begin working if they aren't already assigned. Ensure they also receive CodeHub Enterprise licenses. If they lack employee accounts and mailboxes, those must be established. Record these modifications in lifecycle_queue. Inform me if you need to set up employee accounts and mailboxes.",
        "actions": [
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Drew",
                    "last_name": "Nelson"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Jordan",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Avery",
                    "last_name": "Lee"
                },
            },
            {
                "name": "employeeAccountExists",
                "arguments": {
                    "first_name": "Drew",
                    "last_name": "Nelson"
                },
            },
            {
                "name": "employeeAccountExists",
                "arguments": {
                    "first_name": "Jordan",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "employeeAccountExists",
                "arguments": {
                    "first_name": "Avery",
                    "last_name": "Lee"
                },
            },
            {
                "name": "mailboxExists",
                "arguments": {
                    "employee_id": "emp_0039"
                },
            },
            {
                "name": "mailboxExists",
                "arguments": {
                    "employee_id": "emp_0002"
                },
            },
            {
                "name": "mailboxExists",
                "arguments": {
                    "employee_id": "emp_0001"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0039"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0002"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0001"
                },
            },
            {
                "name": "filterHrMemos",
                "arguments": {
                    "first_name": "Drew",
                    "last_name": "Nelson"
                },
            },
            {
                "name": "filterHrMemos",
                "arguments": {
                    "first_name": "Jordan",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "filterHrMemos",
                "arguments": {
                    "first_name": "Avery",
                    "last_name": "Lee"
                },
            },
            {
                "name": "getJobLicenses",
                "arguments": {
                    "job_title": "Support Manager"
                },
            },
            {
                "name": "getJobLicenses",
                "arguments": {
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "getJobLicenses",
                "arguments": {
                    "job_title": "HRBP"
                },
            },
            {
                "name": "getLicenseInfo",
                "arguments": {
                    "license_name": "CodeHub Enterprise"
                },
            },
            {
                "name": "getLicenseAvailability",
                "arguments": {
                    "license_id": "lic_github_ent"
                },
            },
            {
                "name": "assignLicenses",
                "arguments": {
                    "employee_id": "emp_0039",
                    "license_ids": [
                        "lic_github_ent"
                    ]
                },
            },
            {
                "name": "getLicenseAvailability",
                "arguments": {
                    "license_id": "lic_github_ent"
                },
            },
            {
                "name": "assignLicenses",
                "arguments": {
                    "employee_id": "emp_0002",
                    "license_ids": [
                        "lic_github_ent"
                    ]
                },
            },
            {
                "name": "getLicenseAvailability",
                "arguments": {
                    "license_id": "lic_github_ent"
                },
            },
            {
                "name": "assignLicenses",
                "arguments": {
                    "employee_id": "emp_0001",
                    "license_ids": [
                        "lic_github_ent"
                    ]
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0039",
                    "memo_id": "memo_0008",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0002",
                    "memo_id": "memo_0007",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0001",
                    "memo_id": "memo_0006",
                    "event": "onboarding"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "license_allocation_9",
        "instruction": "You function as an AI agent responsible for automating the distribution of software licenses. By examining license_inventory and employees, identify users who have software renewals due soon, marked by a last audit that is over 10 days old. Verify that the licenses in question are actively used, and refresh license_inventory with the latest audit. Create a CSV listing underutilized licenses (utilization_rate < 50%). Raise low priority TaskTrack tickets for \"Manage license utilization for license_id\" corresponding to each underutilized license.",
        "actions": [
            {
                "name": "licenseRequiresRenewal",
                "arguments": {
                    "num_days": 10
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_m365_e3",
                    "status": "active"
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_m365_e5",
                    "status": "active"
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_adobe_cc",
                    "status": "active"
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_github_ent",
                    "status": "active"
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_slack_ent",
                    "status": "active"
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_salesforce",
                    "status": "active"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_m365_e3"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_m365_e5"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_adobe_cc"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_github_ent"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_slack_ent"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_salesforce"
                },
            },
            {
                "name": "filterLicenses",
                "arguments": {
                    "utilization": 0.5
                },
            },
            {
                "name": "exportUnderutilizedLicenses",
                "arguments": {
                    "output_data": [
                        "lic_m365_e5",
                        "lic_adobe_cc",
                        "lic_github_ent",
                        "lic_slack_ent",
                        "lic_salesforce"
                    ]
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "License Allocation",
                    "summary": "Manage license utilization for lic_m365_e5",
                    "priority": "P3"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "License Allocation",
                    "summary": "Manage license utilization for lic_adobe_cc",
                    "priority": "P3"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "License Allocation",
                    "summary": "Manage license utilization for lic_github_ent",
                    "priority": "P3"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "License Allocation",
                    "summary": "Manage license utilization for lic_slack_ent",
                    "priority": "P3"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "License Allocation",
                    "summary": "Manage license utilization for lic_salesforce",
                    "priority": "P3"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "employee_offboarding_9",
        "instruction": "You are an AI agent tasked with assisting in employee offboarding. Locate employees marked \"offboarding\" using hr_memos and employees. Coordinate the necessary offboarding steps, which include account disabling, license revocation, mailbox archiving, and device wiping in it_assets. Log these actions in lifecycle_queue, and inform management that each employee has been successfully offboarded.",
        "actions": [
            {
                "name": "filterHrMemos",
                "arguments": {
                    "type": "offboarding"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Parker",
                    "last_name": "Davis"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Remy",
                    "last_name": "White"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0007",
                    "status": "disabled"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0019",
                    "status": "disabled"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0007"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0019"
                },
            },
            {
                "name": "archiveMailbox",
                "arguments": {
                    "employee_id": "emp_0007",
                    "department": "IT"
                },
            },
            {
                "name": "archiveMailbox",
                "arguments": {
                    "employee_id": "emp_0019",
                    "department": "Operations"
                },
            },
            {
                "name": "deviceAssignment",
                "arguments": {
                    "employee_id": "emp_0007",
                    "unassign": true
                },
            },
            {
                "name": "deviceAssignment",
                "arguments": {
                    "employee_id": "emp_0019",
                    "unassign": true
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0007",
                    "memo_id": "memo_0009",
                    "event": "offboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0019",
                    "memo_id": "memo_0012",
                    "event": "offboarding"
                },
            },
            {
                "name": "filterEmployees",
                "arguments": {
                    "manager_id": "None"
                },
            },
            {
                "name": "notify",
                "arguments": {
                    "recipient_ids": [
                        "emp_0001",
                        "emp_0002",
                        "emp_0003",
                        "emp_0004",
                        "emp_0005",
                        "emp_0006",
                        "emp_0009",
                        "emp_0017"
                    ],
                    "summary": "Jordan Kim was offboarded."
                },
            },
            {
                "name": "notify",
                "arguments": {
                    "recipient_ids": [
                        "emp_0001",
                        "emp_0002",
                        "emp_0003",
                        "emp_0004",
                        "emp_0005",
                        "emp_0006",
                        "emp_0009",
                        "emp_0017"
                    ],
                    "summary": "Sawyer Harris was offboarded."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "compliance_check_9",
        "instruction": "You are an AI agent responsible for handling quarterly compliance checks. Utilize license_assignments, rbac_group_map, and employees to compare the assigned roles in the Marketing department against the default licenses in rbac_group_map. Identify and flag employees missing default licenses. Prepare a review packet PDF and document the process in validation_issues.",
        "actions": [
            {
                "name": "filterEmployees",
                "arguments": {
                    "department": "Marketing"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0002",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0012",
                    "job_title": "Design Lead"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0016",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0018",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0021",
                    "job_title": "Design Lead"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0024",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0025",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0027",
                    "job_title": "Growth Marketer"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0031",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0032",
                    "job_title": "Growth Marketer"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0034",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0041",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "generateReviewAndLog",
                "arguments": {
                    "log_data": "emp_0002 is missing no licenses,emp_0012 is missing no licenses, emp_0016 is missing no licenses, emp_0018 is missing no licenses, emp_0021 is missing no licenses, emp_0024 is missing no licenses, emp_0025 is missing no licenses, emp_0027 is missing no licenses, emp_0031 is missing no licenses, emp_0032 is missing no licenses, emp_0034 is missing no licenses, emp_0041 is missing no licenses"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "track_backlog_9",
        "instruction": "You are an AI entity responsible for monitoring project backlog. Make use of the backlog_snapshot_open database to generate a report that underscores tickets not marked as \"Resolved\". Store a document with your findings. Create TaskTrack tickets for any unresolved urgent tickets by summarizing as \"Address ticket_id\".",
        "actions": [
            {
                "name": "getTicketsBacklog",
                "arguments": {
                {}
                },
            },
            {
                "name": "filterTickets",
                "arguments": {
                    "ids": [
                        "T5002",
                        "T5003",
                        "T5004",
                        "T5005",
                        "T5006",
                        "T5009",
                        "T5010",
                        "T5011",
                        "T5012",
                        "T5013",
                        "T5014",
                        "T5016",
                        "T5017",
                        "T5020",
                        "T5021",
                        "T5023",
                        "T5024",
                        "T5025",
                        "T5026",
                        "T5027",
                        "T5028",
                        "T5029",
                        "T5030",
                        "T5031",
                        "T5032",
                        "T5035",
                        "T5036",
                        "T5037",
                        "T5039",
                        "T5042",
                        "T5043",
                        "T5044",
                        "T5046",
                        "T5048",
                        "T5049",
                        "T5050",
                        "T5051",
                        "T5053",
                        "T5054",
                        "T5055",
                        "T5056",
                        "T5058",
                        "T5059",
                        "T5060",
                        "T5061",
                        "T5063"
                    ],
                    "not_status": "Resolved"
                },
            },
            {
                "name": "saveReport",
                "arguments": {
                    "save_data": [
                        "T5002",
                        "T5003",
                        "T5004",
                        "T5005",
                        "T5006",
                        "T5009",
                        "T5010",
                        "T5011",
                        "T5012",
                        "T5013",
                        "T5014",
                        "T5016",
                        "T5017",
                        "T5020",
                        "T5021",
                        "T5023",
                        "T5024",
                        "T5025",
                        "T5026",
                        "T5027",
                        "T5028",
                        "T5029",
                        "T5030",
                        "T5031",
                        "T5032",
                        "T5035",
                        "T5036",
                        "T5037",
                        "T5039",
                        "T5042",
                        "T5043",
                        "T5044",
                        "T5046",
                        "T5048",
                        "T5049",
                        "T5050",
                        "T5051",
                        "T5053",
                        "T5054",
                        "T5055",
                        "T5056",
                        "T5058",
                        "T5059",
                        "T5060",
                        "T5061",
                        "T5063"
                    ]
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5002",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5009",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5011",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5017",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5024",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5029",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5036",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5048",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5049",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5050",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5058",
                    "priority": "P1"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "tool_assignment_9",
        "instruction": "You are an AI system tasked with provisioning accounts for a new marketing tool. Allocate app_twitter accounts to all employees within the Marketing department. These accounts are standard for their roles, so updating the rbac_group_map with this new account is necessary. Generate a report that outlines the app provisioning.",
        "actions": [
            {
                "name": "filterEmployees",
                "arguments": {
                    "department": "Marketing"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0002",
                    "app_id": "app_twitter"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0012",
                    "app_id": "app_twitter"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0016",
                    "app_id": "app_twitter"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0018",
                    "app_id": "app_twitter"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0021",
                    "app_id": "app_twitter"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0024",
                    "app_id": "app_twitter"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0025",
                    "app_id": "app_twitter"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0027",
                    "app_id": "app_twitter"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0031",
                    "app_id": "app_twitter"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0032",
                    "app_id": "app_twitter"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0034",
                    "app_id": "app_twitter"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0041",
                    "app_id": "app_twitter"
                },
            },
            {
                "name": "assignRbacLicense",
                "arguments": {
                    "license_id": "app_twitter",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "assignRbacLicense",
                "arguments": {
                    "license_id": "app_twitter",
                    "job_title": "Design Lead"
                },
            },
            {
                "name": "assignRbacLicense",
                "arguments": {
                    "license_id": "app_twitter",
                    "job_title": "Growth Marketer"
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "provisioning",
                    "run_data": [
                        "Added app_twitter account for emp_0002",
                        "Added app_twitter account for emp_0012",
                        "Added app_twitter account for emp_0016",
                        "Added app_twitter account for emp_0018",
                        "Added app_twitter account for emp_0021",
                        "Added app_twitter account for emp_0024",
                        "Added app_twitter account for emp_0025",
                        "Added app_twitter account for emp_0027",
                        "Added app_twitter account for emp_0031",
                        "Added app_twitter account for emp_0032",
                        "Added app_twitter account for emp_0034",
                        "Added app_twitter account for emp_0041"
                    ]
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "sync_lifecycle_9",
        "instruction": "As an AI agent, you synchronize user lifecycles. Identify anyone labeled \"on_leave\" among employees. Apply these procedures for Peyton Shah as well. Modify their statuses to disabled in the directory_accounts database, rescind licenses in both the license_assignments and license_inventory databases, and inform management that the lifecycles have been synchronized.",
        "actions": [
            {
                "name": "filterEmployees",
                "arguments": {
                    "status": "on_leave"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Hayden",
                    "last_name": "Moore"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0004",
                    "status": "disabled"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0019",
                    "status": "disabled"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0032",
                    "status": "disabled"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0015",
                    "status": "disabled"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0004"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0019"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0032"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0015"
                },
            },
            {
                "name": "filterEmployees",
                "arguments": {
                    "manager_id": "None"
                },
            },
            {
                "name": "notify",
                "arguments": {
                    "recipient_ids": [
                        "emp_0001",
                        "emp_0002",
                        "emp_0003",
                        "emp_0004",
                        "emp_0005",
                        "emp_0006",
                        "emp_0009",
                        "emp_0017"
                    ],
                    "summary": "The lifecycles were synchronized."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "service_stats_9",
        "instruction": "Acting as an AI agent, you assess daily service statistics. With the use of tickets, determine the average time for ticket completion, the average number of tickets opened, and the average number closed daily. Alert Casey Liu, Sam Tran, and Robin Jones with the results. Compile a pdf report of your analysis and record it to validation_issues.",
        "actions": [
            {
                "name": "ticketStatistics",
                "arguments": {
                    "field": "avg_open_age_hours",
                    "type": "avg"
                },
            },
            {
                "name": "ticketStatistics",
                "arguments": {
                    "field": "tickets_opened",
                    "type": "avg"
                },
            },
            {
                "name": "ticketStatistics",
                "arguments": {
                    "field": "tickets_closed",
                    "type": "avg"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Jordan",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Morgan",
                    "last_name": "Nguyen"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Casey",
                    "last_name": "Smith"
                },
            },
            {
                "name": "notify",
                "arguments": {
                    "recipient_ids": [
                        "emp_0002",
                        "emp_0004",
                        "emp_0005"
                    ],
                    "summary": "The average of avg_open_age_hours is 36.2. The average of tickets_opened is 1.6667. The average of tickets_closed is 1.2."
                },
            },
            {
                "name": "generateReviewAndLog",
                "arguments": {
                    "log_data": "The average of avg_open_age_hours is 36.2. The average of tickets_opened is 1.6667. The average of tickets_closed is 1.2."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "asset_reservations_9",
        "instruction": "Acting as an AI agent for asset reservations, handle the allocation of an unused laptop from it_assets to employees noted in hr_memos as having onboarding documentation. Indicate those assets as \"assigned\" and input a finalized entry into lifecycle_queue.",
        "actions": [
            {
                "name": "filterHrMemos",
                "arguments": {
                    "type": "onboarding"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Finley",
                    "last_name": "Robinson"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "River",
                    "last_name": "Scott"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Alex",
                    "last_name": "Brown"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Cameron",
                    "last_name": "Wilson"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Taylor",
                    "last_name": "Patel"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Avery",
                    "last_name": "Lee"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Jordan",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Drew",
                    "last_name": "Nelson"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0025",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0031",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0008",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0011",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0003",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0001",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0002",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0039",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0025",
                    "memo_id": "memo_0001",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0031",
                    "memo_id": "memo_0002",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0008",
                    "memo_id": "memo_0003",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0011",
                    "memo_id": "memo_0004",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0003",
                    "memo_id": "memo_0005",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0001",
                    "memo_id": "memo_0006",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0002",
                    "memo_id": "memo_0007",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0039",
                    "memo_id": "memo_0008",
                    "event": "onboarding"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "unused_licenses_9",
        "instruction": "Function as an AI agent for reclaiming unused software licenses. By examining license_assignments and employees, identify terminated individuals or those on leave. Detach those assignments, update license_inventory to reflect added seat availability, and produce individual pdf reports detailing the changes for each user.",
        "actions": [
            {
                "name": "filterEmployees",
                "arguments": {
                    "status": "terminated"
                },
            },
            {
                "name": "filterEmployees",
                "arguments": {
                    "status": "on_leave"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0007"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0033"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0004"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0019"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0032"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0004"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0019"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0032"
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "unassign_licenses",
                    "run_data": [
                        "emp_0007"
                    ]
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "unassign_licenses",
                    "run_data": [
                        "emp_0033"
                    ]
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "unassign_licenses",
                    "run_data": [
                        "emp_0004",
                        "lic_slack_ent",
                        "lic_github_ent",
                        "lic_m365_e3"
                    ]
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "unassign_licenses",
                    "run_data": [
                        "emp_0019",
                        "lic_slack_ent",
                        "lic_m365_e3"
                    ]
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "unassign_licenses",
                    "run_data": [
                        "emp_0032",
                        "lic_salesforce",
                        "lic_slack_ent",
                        "lic_m365_e3"
                    ]
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "onboarding_10",
        "instruction": "HR distributed memos regarding the upcoming onboarding of three new employees, Briar Campbell, Jamie Chen, and Drew Kumar. Ensure the default licenses from rbac_group_map are allocated for their respective roles if they don't currently possess them. Additionally, CodeHub Enterprise licenses should be provided. Should they lack employee accounts and mailboxes, these will need to be set up. Record these modifications in lifecycle_queue. Inform me if there is a need to establish employee accounts and mailboxes.",
        "actions": [
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Drew",
                    "last_name": "Nelson"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Avery",
                    "last_name": "Lee"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Taylor",
                    "last_name": "Patel"
                },
            },
            {
                "name": "employeeAccountExists",
                "arguments": {
                    "first_name": "Drew",
                    "last_name": "Nelson"
                },
            },
            {
                "name": "employeeAccountExists",
                "arguments": {
                    "first_name": "Avery",
                    "last_name": "Lee"
                },
            },
            {
                "name": "employeeAccountExists",
                "arguments": {
                    "first_name": "Taylor",
                    "last_name": "Patel"
                },
            },
            {
                "name": "mailboxExists",
                "arguments": {
                    "employee_id": "emp_0039"
                },
            },
            {
                "name": "mailboxExists",
                "arguments": {
                    "employee_id": "emp_0001"
                },
            },
            {
                "name": "mailboxExists",
                "arguments": {
                    "employee_id": "emp_0003"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0039"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0001"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0003"
                },
            },
            {
                "name": "filterHrMemos",
                "arguments": {
                    "first_name": "Drew",
                    "last_name": "Nelson"
                },
            },
            {
                "name": "filterHrMemos",
                "arguments": {
                    "first_name": "Avery",
                    "last_name": "Lee"
                },
            },
            {
                "name": "filterHrMemos",
                "arguments": {
                    "first_name": "Taylor",
                    "last_name": "Patel"
                },
            },
            {
                "name": "getJobLicenses",
                "arguments": {
                    "job_title": "Support Manager"
                },
            },
            {
                "name": "getJobLicenses",
                "arguments": {
                    "job_title": "HRBP"
                },
            },
            {
                "name": "getJobLicenses",
                "arguments": {
                    "job_title": "Ops Coordinator"
                },
            },
            {
                "name": "getLicenseInfo",
                "arguments": {
                    "license_name": "CodeHub Enterprise"
                },
            },
            {
                "name": "getLicenseAvailability",
                "arguments": {
                    "license_id": "lic_github_ent"
                },
            },
            {
                "name": "assignLicenses",
                "arguments": {
                    "employee_id": "emp_0039",
                    "license_ids": [
                        "lic_github_ent"
                    ]
                },
            },
            {
                "name": "getLicenseAvailability",
                "arguments": {
                    "license_id": "lic_github_ent"
                },
            },
            {
                "name": "assignLicenses",
                "arguments": {
                    "employee_id": "emp_0001",
                    "license_ids": [
                        "lic_github_ent"
                    ]
                },
            },
            {
                "name": "getLicenseAvailability",
                "arguments": {
                    "license_id": "lic_github_ent"
                },
            },
            {
                "name": "assignLicenses",
                "arguments": {
                    "employee_id": "emp_0003",
                    "license_ids": [
                        "lic_github_ent"
                    ]
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0039",
                    "memo_id": "memo_0008",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0001",
                    "memo_id": "memo_0006",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0003",
                    "memo_id": "memo_0005",
                    "event": "onboarding"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "license_allocation_10",
        "instruction": "You function as an AI system that streamlines software license distribution. By utilizing license_inventory and employees, pinpoint users whose software renewals are approaching, as identified by the last audit surpassing 15 days. Verify active use of the identified licenses and update license_inventory with a fresh audit. Create a CSV file of licenses that are underutilized (utilization_rate < 30%). Initiate low-priority TaskTrack tickets for \"Manage license utilization for license_id\" for each underutilized license.",
        "actions": [
            {
                "name": "licenseRequiresRenewal",
                "arguments": {
                    "num_days": 15
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_m365_e3",
                    "status": "active"
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_m365_e5",
                    "status": "active"
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_adobe_cc",
                    "status": "active"
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_github_ent",
                    "status": "active"
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_slack_ent",
                    "status": "active"
                },
            },
            {
                "name": "getEmployeeByLicense",
                "arguments": {
                    "license_id": "lic_salesforce",
                    "status": "active"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_m365_e3"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_m365_e5"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_adobe_cc"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_github_ent"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_slack_ent"
                },
            },
            {
                "name": "updateLicenseAudit",
                "arguments": {
                    "license_id": "lic_salesforce"
                },
            },
            {
                "name": "filterLicenses",
                "arguments": {
                    "utilization": 0.3
                },
            },
            {
                "name": "exportUnderutilizedLicenses",
                "arguments": {
                    "output_data": [
                        "lic_m365_e5",
                        "lic_adobe_cc",
                        "lic_github_ent",
                        "lic_salesforce"
                    ]
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "License Allocation",
                    "summary": "Manage license utilization for lic_m365_e5",
                    "priority": "P3"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "License Allocation",
                    "summary": "Manage license utilization for lic_adobe_cc",
                    "priority": "P3"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "License Allocation",
                    "summary": "Manage license utilization for lic_github_ent",
                    "priority": "P3"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "License Allocation",
                    "summary": "Manage license utilization for lic_salesforce",
                    "priority": "P3"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "employee_offboarding_10",
        "instruction": "You are an AI agent assigned to assist with employee offboarding. Locate the employees indicated as \"offboarding\" utilizing the employees and hr_memos databases. Handle the offboarding procedures by disabling accounts, revoking licenses, archiving mailboxes, and erasing data from assigned devices in it_assets. Document these tasks in lifecycle_queue, and inform management once each employee has been offboarded.",
        "actions": [
            {
                "name": "filterHrMemos",
                "arguments": {
                    "type": "offboarding"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Parker",
                    "last_name": "Davis"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Remy",
                    "last_name": "White"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0007",
                    "status": "disabled"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0019",
                    "status": "disabled"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0007"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0019"
                },
            },
            {
                "name": "archiveMailbox",
                "arguments": {
                    "employee_id": "emp_0007",
                    "department": "IT"
                },
            },
            {
                "name": "archiveMailbox",
                "arguments": {
                    "employee_id": "emp_0019",
                    "department": "Operations"
                },
            },
            {
                "name": "deviceAssignment",
                "arguments": {
                    "employee_id": "emp_0007",
                    "unassign": true
                },
            },
            {
                "name": "deviceAssignment",
                "arguments": {
                    "employee_id": "emp_0019",
                    "unassign": true
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0007",
                    "memo_id": "memo_0009",
                    "event": "offboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0019",
                    "memo_id": "memo_0012",
                    "event": "offboarding"
                },
            },
            {
                "name": "filterEmployees",
                "arguments": {
                    "manager_id": "None"
                },
            },
            {
                "name": "notify",
                "arguments": {
                    "recipient_ids": [
                        "emp_0001",
                        "emp_0002",
                        "emp_0003",
                        "emp_0004",
                        "emp_0005",
                        "emp_0006",
                        "emp_0009",
                        "emp_0017"
                    ],
                    "summary": "Jordan Kim was offboarded."
                },
            },
            {
                "name": "notify",
                "arguments": {
                    "recipient_ids": [
                        "emp_0001",
                        "emp_0002",
                        "emp_0003",
                        "emp_0004",
                        "emp_0005",
                        "emp_0006",
                        "emp_0009",
                        "emp_0017"
                    ],
                    "summary": "Sawyer Harris was offboarded."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "compliance_check_10",
        "instruction": "You are an AI agent responsible for conducting annual compliance checks. By accessing license_assignments, rbac_group_map, and employees, compare the assigned roles within the Marketing department to the rbac_group_map default licenses. Identify and flag employees lacking default licenses. Coordinate the creation of a review packet PDF and log the operation in validation_issues.",
        "actions": [
            {
                "name": "filterEmployees",
                "arguments": {
                    "department": "Marketing"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0002",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0012",
                    "job_title": "Design Lead"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0016",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0018",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0021",
                    "job_title": "Design Lead"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0024",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0025",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0027",
                    "job_title": "Growth Marketer"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0031",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0032",
                    "job_title": "Growth Marketer"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0034",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "missingLicenses",
                "arguments": {
                    "employee_id": "emp_0041",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "generateReviewAndLog",
                "arguments": {
                    "log_data": "emp_0002 is missing no licenses,emp_0012 is missing no licenses, emp_0016 is missing no licenses, emp_0018 is missing no licenses, emp_0021 is missing no licenses, emp_0024 is missing no licenses, emp_0025 is missing no licenses, emp_0027 is missing no licenses, emp_0031 is missing no licenses, emp_0032 is missing no licenses, emp_0034 is missing no licenses, emp_0041 is missing no licenses"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "track_backlog_10",
        "instruction": "As an AI agent responsible for tracking project backlog, utilize the backlog_snapshot_open database to compile a report emphasizing tickets that remain not \"Resolved\". Create and save a report with these details. For any unresolved urgent tickets, file TaskTrack tickets with a summary that says \"Address ticket_id\".",
        "actions": [
            {
                "name": "getTicketsBacklog",
                "arguments": {
                {}
                },
            },
            {
                "name": "filterTickets",
                "arguments": {
                    "ids": [
                        "T5002",
                        "T5003",
                        "T5004",
                        "T5005",
                        "T5006",
                        "T5009",
                        "T5010",
                        "T5011",
                        "T5012",
                        "T5013",
                        "T5014",
                        "T5016",
                        "T5017",
                        "T5020",
                        "T5021",
                        "T5023",
                        "T5024",
                        "T5025",
                        "T5026",
                        "T5027",
                        "T5028",
                        "T5029",
                        "T5030",
                        "T5031",
                        "T5032",
                        "T5035",
                        "T5036",
                        "T5037",
                        "T5039",
                        "T5042",
                        "T5043",
                        "T5044",
                        "T5046",
                        "T5048",
                        "T5049",
                        "T5050",
                        "T5051",
                        "T5053",
                        "T5054",
                        "T5055",
                        "T5056",
                        "T5058",
                        "T5059",
                        "T5060",
                        "T5061",
                        "T5063"
                    ],
                    "not_status": "Resolved"
                },
            },
            {
                "name": "saveReport",
                "arguments": {
                    "save_data": [
                        "T5002",
                        "T5003",
                        "T5004",
                        "T5005",
                        "T5006",
                        "T5009",
                        "T5010",
                        "T5011",
                        "T5012",
                        "T5013",
                        "T5014",
                        "T5016",
                        "T5017",
                        "T5020",
                        "T5021",
                        "T5023",
                        "T5024",
                        "T5025",
                        "T5026",
                        "T5027",
                        "T5028",
                        "T5029",
                        "T5030",
                        "T5031",
                        "T5032",
                        "T5035",
                        "T5036",
                        "T5037",
                        "T5039",
                        "T5042",
                        "T5043",
                        "T5044",
                        "T5046",
                        "T5048",
                        "T5049",
                        "T5050",
                        "T5051",
                        "T5053",
                        "T5054",
                        "T5055",
                        "T5056",
                        "T5058",
                        "T5059",
                        "T5060",
                        "T5061",
                        "T5063"
                    ]
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5002",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5009",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5011",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5017",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5024",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5029",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5036",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5048",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5049",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5050",
                    "priority": "P1"
                },
            },
            {
                "name": "createJiraTicket",
                "arguments": {
                    "issue_type": "IT Ticket",
                    "summary": "Address T5058",
                    "priority": "P1"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "tool_assignment_10",
        "instruction": "As an AI agent tasked with provisioning accounts for a new marketing tool, allocate app_facebook accounts to all employees in the Marketing department. Ensure these accounts are standard for the roles, necessitating an update to the rbac_group_map with the new account information. Generate a report summarizing the provisioning of the app.",
        "actions": [
            {
                "name": "filterEmployees",
                "arguments": {
                    "department": "Marketing"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0002",
                    "app_id": "app_facebook"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0012",
                    "app_id": "app_facebook"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0016",
                    "app_id": "app_facebook"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0018",
                    "app_id": "app_facebook"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0021",
                    "app_id": "app_facebook"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0024",
                    "app_id": "app_facebook"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0025",
                    "app_id": "app_facebook"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0027",
                    "app_id": "app_facebook"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0031",
                    "app_id": "app_facebook"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0032",
                    "app_id": "app_facebook"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0034",
                    "app_id": "app_facebook"
                },
            },
            {
                "name": "assignAppAccount",
                "arguments": {
                    "employee_id": "emp_0041",
                    "app_id": "app_facebook"
                },
            },
            {
                "name": "assignRbacLicense",
                "arguments": {
                    "license_id": "app_facebook",
                    "job_title": "Content Strategist"
                },
            },
            {
                "name": "assignRbacLicense",
                "arguments": {
                    "license_id": "app_facebook",
                    "job_title": "Design Lead"
                },
            },
            {
                "name": "assignRbacLicense",
                "arguments": {
                    "license_id": "app_facebook",
                    "job_title": "Growth Marketer"
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "provisioning",
                    "run_data": [
                        "Added app_facebook account for emp_0002",
                        "Added app_facebook account for emp_0012",
                        "Added app_facebook account for emp_0016",
                        "Added app_facebook account for emp_0018",
                        "Added app_facebook account for emp_0021",
                        "Added app_facebook account for emp_0024",
                        "Added app_facebook account for emp_0025",
                        "Added app_facebook account for emp_0027",
                        "Added app_facebook account for emp_0031",
                        "Added app_facebook account for emp_0032",
                        "Added app_facebook account for emp_0034",
                        "Added app_facebook account for emp_0041"
                    ]
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "sync_lifecycle_10",
        "instruction": "You are an AI agent tasked with synchronizing user lifecycles. Identify any employees marked as \"on_leave.\" Ensure these actions are performed for Hayden Brown too. Adjust their statuses to disabled in the directory_accounts database, remove licenses from the license_assignments and license_inventory databases, and inform management that the lifecycles have been synchronized.",
        "actions": [
            {
                "name": "filterEmployees",
                "arguments": {
                    "status": "on_leave"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Dakota",
                    "last_name": "Jackson"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0004",
                    "status": "disabled"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0019",
                    "status": "disabled"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0032",
                    "status": "disabled"
                },
            },
            {
                "name": "updateDirectoryAccount",
                "arguments": {
                    "employee_id": "emp_0016",
                    "status": "disabled"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0004"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0019"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0032"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0016"
                },
            },
            {
                "name": "filterEmployees",
                "arguments": {
                    "manager_id": "None"
                },
            },
            {
                "name": "notify",
                "arguments": {
                    "recipient_ids": [
                        "emp_0001",
                        "emp_0002",
                        "emp_0003",
                        "emp_0004",
                        "emp_0005",
                        "emp_0006",
                        "emp_0009",
                        "emp_0017"
                    ],
                    "summary": "The lifecycles were synchronized."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "service_stats_10",
        "instruction": "As an AI agent assessing daily service statistics, use the tickets to determine the average time needed to complete a ticket, along with the average number of tickets opened and closed each day. Communicate your findings to Drew Kumar, Sam Tran, and Robin Jones. Create a pdf report of your results and record it in validation_issues.",
        "actions": [
            {
                "name": "ticketStatistics",
                "arguments": {
                    "field": "avg_open_age_hours",
                    "type": "avg"
                },
            },
            {
                "name": "ticketStatistics",
                "arguments": {
                    "field": "tickets_opened",
                    "type": "avg"
                },
            },
            {
                "name": "ticketStatistics",
                "arguments": {
                    "field": "tickets_closed",
                    "type": "avg"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Taylor",
                    "last_name": "Patel"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Morgan",
                    "last_name": "Nguyen"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Casey",
                    "last_name": "Smith"
                },
            },
            {
                "name": "notify",
                "arguments": {
                    "recipient_ids": [
                        "emp_0003",
                        "emp_0004",
                        "emp_0005"
                    ],
                    "summary": "The average of avg_open_age_hours is 36.2. The average of tickets_opened is 1.6667. The average of tickets_closed is 1.2."
                },
            },
            {
                "name": "generateReviewAndLog",
                "arguments": {
                    "log_data": "The average of avg_open_age_hours is 36.2. The average of tickets_opened is 1.6667. The average of tickets_closed is 1.2."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "asset_reservations_10",
        "instruction": "Act as an AI agent for asset reservations. For employees with onboarding memos in hr_memos, allocate an available laptop from it_assets. Designate those laptops as \"assigned\" and record the completed transaction in lifecycle_queue.",
        "actions": [
            {
                "name": "filterHrMemos",
                "arguments": {
                    "type": "onboarding"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Finley",
                    "last_name": "Robinson"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "River",
                    "last_name": "Scott"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Alex",
                    "last_name": "Brown"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Cameron",
                    "last_name": "Wilson"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Taylor",
                    "last_name": "Patel"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Avery",
                    "last_name": "Lee"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Jordan",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "getEmployeeId",
                "arguments": {
                    "first_name": "Drew",
                    "last_name": "Nelson"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0025",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0031",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0008",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0011",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0003",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0001",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0002",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "assignDevice",
                "arguments": {
                    "employee_id": "emp_0039",
                    "asset_type": "laptop"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0025",
                    "memo_id": "memo_0001",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0031",
                    "memo_id": "memo_0002",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0008",
                    "memo_id": "memo_0003",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0011",
                    "memo_id": "memo_0004",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0003",
                    "memo_id": "memo_0005",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0001",
                    "memo_id": "memo_0006",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0002",
                    "memo_id": "memo_0007",
                    "event": "onboarding"
                },
            },
            {
                "name": "logLifecycle",
                "arguments": {
                    "employee_id": "emp_0039",
                    "memo_id": "memo_0008",
                    "event": "onboarding"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "unused_licenses_10",
        "instruction": "Function as an AI agent reclaiming unused software licenses. By referencing license_assignments and employees, identify any terminated or on-leave users. Eliminate those assignments, modify license_inventory to increment available seats, and produce unique pdf reports reflecting the changes for each user.",
        "actions": [
            {
                "name": "filterEmployees",
                "arguments": {
                    "status": "terminated"
                },
            },
            {
                "name": "filterEmployees",
                "arguments": {
                    "status": "on_leave"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0007"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0033"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0004"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0019"
                },
            },
            {
                "name": "getEmployeeLicenses",
                "arguments": {
                    "employee_id": "emp_0032"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0004"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0019"
                },
            },
            {
                "name": "unassignLicenses",
                "arguments": {
                    "employee_id": "emp_0032"
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "unassign_licenses",
                    "run_data": [
                        "emp_0007"
                    ]
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "unassign_licenses",
                    "run_data": [
                        "emp_0033"
                    ]
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "unassign_licenses",
                    "run_data": [
                        "emp_0004",
                        "lic_slack_ent",
                        "lic_github_ent",
                        "lic_m365_e3"
                    ]
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "unassign_licenses",
                    "run_data": [
                        "emp_0019",
                        "lic_slack_ent",
                        "lic_m365_e3"
                    ]
                },
            },
            {
                "name": "reportRun",
                "arguments": {
                    "report_type": "unassign_licenses",
                    "run_data": [
                        "emp_0032",
                        "lic_salesforce",
                        "lic_slack_ent",
                        "lic_m365_e3"
                    ]
                }
            }
        ],
        "outputs": []
    }
]
