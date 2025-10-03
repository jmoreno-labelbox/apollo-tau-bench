# Copyright Sierra

tasks = [
    {
        "annotator": 0,
        "user_id": "01",
        "instruction": "As the financial controller for 'Northern Star Publishers' (PUB001), handle an accounts receivable aging review for the date '2024-11-30' concerning invoices INV001, INV004, INV009, and INV021. Access the respective details for each invoice and calculate their aging using today='2024-11-30'. In line with company policy, send an 'email_reminder' with the message 'Overdue 31\u201360 days' for invoices overdue by 31 to 60 days, and a 'second_notice' with 'Overdue >60 days' for invoices overdue by more than 60 days. Document each follow-up action in the invoice audit trail. Lastly, produce two lists directly in the task output: (a) all invoice IDs necessitating action and (b) those needing escalation due to being overdue beyond 60 days.",
        "actions": [
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV001"
                },
            },
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV004"
                },
            },
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV009"
                },
            },
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV021"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV001",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV004",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV009",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV021",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV009",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV021",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                }
            }
        ],
        "outputs": [
                [
                    "INV009",
                    "INV021"
                ],
                [
                    "INV009",
                    "INV021"
                ]
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "02",
        "instruction": "Coordinate the delivery of the Q3-2024 office & travel pack. For the period '2024-07-01' to '2024-09-30', ensure deductibility normalization on EXP012 (OFFICE_SUPPLIES) as well as EXP022/EXP023 (TRAVEL_EXPENSE), then prepare the '2024-Q3' dashboard and archive KPI 'Q3_Mixed_Compliance_2024-09-30' as of '2024-09-30' focusing on sections ['ExpenseMix','Deductibility']. Provide the path to the dashboard.",
        "actions": [
            {
                "name": "ListExpensesByDateRangeAndCategory",
                "arguments": {
                    "start_date": "2024-07-01",
                    "end_date": "2024-09-30",
                    "categories": [
                        "OFFICE_SUPPLIES",
                        "TRAVEL_EXPENSE"
                    ]
                },
            },
            {
                "name": "ApplyDeductibilityRules",
                "arguments": {
                    "expense_id": "EXP012"
                },
            },
            {
                "name": "ApplyDeductibilityRules",
                "arguments": {
                    "expense_id": "EXP022"
                },
            },
            {
                "name": "ApplyDeductibilityRules",
                "arguments": {
                    "expense_id": "EXP023"
                },
            },
            {
                "name": "GenerateExpenseDashboard",
                "arguments": {
                    "quarter": "2024-Q3",
                    "included_expenses": [
                        "EXP012",
                        "EXP022",
                        "EXP023"
                    ]
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-09-30",
                    "artifact_name": "Q3_Mixed_Compliance_2024-09-30",
                    "sections": [
                        "ExpenseMix",
                        "Deductibility"
                    ]
                }
            }
        ],
        "outputs": [
                "/dashboards/ExpenseDashboards/2024-Q3/expense_dashboard_2024-Q3.pdf"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "03",
        "instruction": "Serving as the accounts receivable specialist for 'Summit Educational Publishing' (PUB003), as of '2024-11-30', you are required to handle an aging review on invoices INV013, INV008, INV024, and INV025. Retrieve the details for each invoice and calculate the aging using the date='2024-11-30'. According to policy, send an 'email_reminder' with the note 'Overdue 31\u201360 days' for invoices overdue 31\u201360 days, and a 'second_notice' with the note 'Overdue >60 days' for those overdue more than 60 days. Log each follow-up in the invoice audit trail. Lastly, provide two lists: (a) all invoice IDs that needed action, and (b) only those necessitating escalation beyond 60 days.",
        "actions": [
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV013"
                },
            },
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV008"
                },
            },
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV024"
                },
            },
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV025"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV013",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV008",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV024",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV025",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV013",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV008",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                }
            }
        ],
        "outputs": [
                [
                    "INV013",
                    "INV008"
                ],
                [
                    "INV013",
                    "INV008"
                ]
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "04",
        "instruction": "Create a PUB005 wrap memo dated '2024-11-30'. Classify INV022 and INV026 with today '2024-11-30'; items over 60 days need a 'second_notice' with notes 'Overdue >60 days'. Archive KPI 'PUB005_Wrap_Memo_2024-11-30' as_of '2024-11-30' under sections ['Collections']. Provide lists of both acted and escalated items.",
        "actions": [
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV022",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV026",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV022",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV026",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "artifact_name": "PUB005_Wrap_Memo_2024-11-30",
                    "sections": [
                        "Collections"
                    ]
                }
            }
        ],
        "outputs": [
                [
                    "INV022",
                    "INV026"
                ],
                [
                    "INV022",
                    "INV026"
                ]
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "05",
        "instruction": "As the accounts receivable specialist for 'Summit Educational Publishing' (PUB003), your task as of '2024-11-30' is to handle an aging review for invoices INV008, INV009, INV010, and INV011. For each invoice, access details and calculate aging with today='2024-11-30'. According to policy, invoices 31\u201360 days overdue must be issued an 'email_reminder' with the note 'Overdue 31\u201360 days', while invoices overdue more than 60 days need a 'second_notice' with the note 'Overdue >60 days'. Ensure each follow-up is logged in the invoice audit trail. Lastly, generate two lists: (a) all invoice IDs needing action, and (b) those requiring escalation beyond 60 days.",
        "actions": [
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV008"
                },
            },
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV009"
                },
            },
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV010"
                },
            },
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV011"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV008",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV009",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV010",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV011",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV008",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV009",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                }
            }
        ],
        "outputs": [
                [
                    "INV008",
                    "INV009"
                ],
                [
                    "INV008",
                    "INV009"
                ]
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "06",
        "instruction": "Serving as the A/R lead for 'Northern Star Publishers' (PUB001), as of '2024-11-30', you need to coordinate an aging review for INV004, INV009, INV021, and INV026 according to policy, document necessary follow-ups, and produce two lists: (a) all invoice IDs that needed action and (b) those needing escalation past 60 days.",
        "actions": [
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV004"
                },
            },
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV009"
                },
            },
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV021"
                },
            },
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV026"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV004",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV009",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV021",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV026",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV009",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV021",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV026",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                }
            }
        ],
        "outputs": [
                [
                    "INV009",
                    "INV021",
                    "INV026"
                ],
                [
                    "INV009",
                    "INV021",
                    "INV026"
                ]
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "07",
        "instruction": "As the A/R coordinator for 'Summit Educational Publishing' (PUB003), starting from '2024-11-30', handle a review of aging for INV008, INV009, and INV010 according to the policy. Document necessary follow-ups and compile two lists: (a) all invoice IDs that necessitated action and (b) those requiring escalation beyond 60 days.",
        "actions": [
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV008"
                },
            },
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV009"
                },
            },
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV010"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV008",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV009",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV010",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV008",
                    "event_type": "second_notice",
                    "notes": "system"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV009",
                    "event_type": "second_notice",
                    "notes": "system"
                }
            }
        ],
        "outputs": [
                [
                    "INV008",
                    "INV009"
                ],
                [
                    "INV008",
                    "INV009"
                ]
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "08",
        "instruction": "In your role as the financial controller for 'Aurora Academic Press' (PUB002), beginning on '2024-11-30', you need to examine open invoices INV012, INV023, and INV007, calculate aging as of today='2024-11-30', and log follow-ups that comply with the policy. Any invoice overdue by more than 60 days must receive a 'second_notice' with notes 'Overdue >60 days'; invoices that are paid require no action. Return two lists: (a) all invoice IDs that needed follow-up and (b) those that require escalation beyond 60 days.",
        "actions": [
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV012"
                },
            },
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV023"
                },
            },
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV007"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV012",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV023",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV007",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV012",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV023",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                }
            }
        ],
        "outputs": [
                [
                    "INV012",
                    "INV023"
                ],
                [
                    "INV012",
                    "INV023"
                ]
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "09",
        "instruction": "As the financial controller for 'Midwest Education House' (PUB005), as of '2024-11-30', handle an accounts receivable review focusing on invoices INV011, INV022, INV025, and INV026. For each, gather details and determine aging with today='2024-11-30'. According to policy, invoices overdue by 31\u201360 days should receive an 'email_reminder' with the note 'Overdue 31\u201360 days', while those overdue more than 60 days need a 'second_notice' with the note 'Overdue >60 days'. Ensure each follow-up is logged in the audit trail. Finally, create two lists: (a) all invoice IDs needing action, and (b) those requiring escalation beyond 60 days.",
        "actions": [
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV011"
                },
            },
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV022"
                },
            },
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV025"
                },
            },
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV026"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV011",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV022",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV025",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV026",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV022",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV026",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                }
            }
        ],
        "outputs": [
                [
                    "INV022",
                    "INV026"
                ],
                [
                    "INV022",
                    "INV026"
                ]
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "10",
        "instruction": "Implement A/R follow-ups as of '2024-11-30' for invoices ['INV008','INV009','INV021','INV011']. Sort each invoice using today '2024-11-30', and if any are more than 60 days overdue, log a 'second_notice' with the note 'Overdue >60 days'. Produce two lists: (a) all invoices needing action, and (b) those escalated beyond 60 days.",
        "actions": [
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV008",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV009",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV021",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV011",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV008",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV009",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV021",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                }
            }
        ],
        "outputs": [
                [
                    "INV008",
                    "INV009",
                    "INV021"
                ],
                [
                    "INV008",
                    "INV009",
                    "INV021"
                ]
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "11",
        "instruction": "Handle A/R enforcement validation for 'Aurora Academic Press' (PUB002) as of '2024-11-30'. From the open items of PUB002, determine the aging for invoices ['INV012','INV023'] using today's date '2024-11-30' and, according to policy, record a 'second_notice' with the note 'Overdue >60 days' for any items overdue by more than 60 days. Archive a KPI artifact as_of '2024-11-30' under sections ['Collections'] with the artifact_name 'PUB002_Collections_2024-11-30'. Provide two lists in return: the invoices that were acted upon and those that were escalated.",
        "actions": [
            {
                "name": "ListPublisherOpenInvoices",
                "arguments": {
                    "publisher_id": "PUB002"
                },
            },
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV012"
                },
            },
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV023"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV012",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV023",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV012",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV023",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "sections": [
                        "Collections"
                    ],
                    "artifact_name": "PUB002_Collections_2024-11-30"
                }
            }
        ],
        "outputs": [
                [
                    "INV012",
                    "INV023"
                ],
                [
                    "INV012",
                    "INV023"
                ]
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "12",
        "instruction": "Coordinate the preparation of a collections snapshot for 'Aurora Academic Press' (PUB002) as of '2024-11-30'. Compute aging from PUB002's open items for ['INV012','INV023'], log a 'second_notice' with notes 'Overdue >60 days' where necessary, and archive the KPI with an as_of date of '2024-11-30' within sections ['Collections'] under the name 'PUB002_Collections_Snapshot_2024-11-30'. Return two lists: those invoices that were acted upon and those escalated.",
        "actions": [
            {
                "name": "ListPublisherOpenInvoices",
                "arguments": {
                    "publisher_id": "PUB002"
                },
            },
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV012"
                },
            },
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV023"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV012",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV023",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV012",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV023",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "sections": [
                        "Collections"
                    ],
                    "artifact_name": "PUB002_Collections_Snapshot_2024-11-30"
                }
            }
        ],
        "outputs": [
                [
                    "INV012",
                    "INV023"
                ],
                [
                    "INV012",
                    "INV023"
                ]
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "13",
        "instruction": "Handle the issuance of a zero-total November 2024 shell invoice for 'Northern Star Publishers' (PUB001). Ensure to include invoice_id 'INV-AUTO-2024-404', invoice_number 'INV-2024-404', invoice_date '2024-11-30', and period '2024-11-01'..'2024-11-30'; HST 0.13 on subtotal 0.00. Archive the PDF, document 'generated' audit, and archive KPI 'PUB001_Shell_Close_2024-11' as_of '2024-11-30' with sections ['Issuance']. Return 'INV-2024-404'.",
        "actions": [
            {
                "name": "CalculateTotals",
                "arguments": {
                    "invoice_lines": [],
                    "hst_rate": 0.13
                },
            },
            {
                "name": "ComposeInvoicePdf",
                "arguments": {
                    "invoice_id": "INV-AUTO-2024-404",
                    "publisher_id": "PUB001"
                },
            },
            {
                "name": "InsertInvoice",
                "arguments": {
                    "invoice_id": "INV-AUTO-2024-404",
                    "publisher_id": "PUB001",
                    "subtotal": 0.0,
                    "hst_amount": 0.0,
                    "total_due": 0.0,
                    "invoice_number": "INV-2024-404",
                    "invoice_date": "2024-11-30",
                    "period_start": "2024-11-01",
                    "period_end": "2024-11-30",
                    "pdf_path": "/invoices/auto/INV-AUTO-2024-404.pdf"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV-AUTO-2024-404",
                    "event_type": "generated",
                    "notes": "Invoice generated"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "artifact_name": "PUB001_Shell_Close_2024-11",
                    "sections": [
                        "Issuance"
                    ]
                }
            }
        ],
        "outputs": [
                "INV-2024-404"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "14",
        "instruction": "Coordinate the compilation of a risk overview for PUB003 as of '2024-11-30'. Calculate expected inflows for ['INV008','INV013','INV022'] using probability_rule 'overdue_60=0.3' and record 'second_notice' with notes 'Overdue >60 days' for items overdue >60 days. Archive the KPI as_of '2024-11-30' in sections ['Collections'] (artifact_name 'PUB003_Risk_Overview_2024-11-30'). Return the KPI path.",
        "actions": [
            {
                "name": "ForecastInflows",
                "arguments": {
                    "invoices": [
                        "INV008",
                        "INV013",
                        "INV022"
                    ],
                    "probability_rule": "overdue_60=0.3"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV008",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV013",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV022",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "sections": [
                        "Collections"
                    ],
                    "artifact_name": "PUB003_Risk_Overview_2024-11-30"
                }
            }
        ],
        "outputs": [
                "/reports/kpi/PUB003_Risk_Overview_2024-11-30.pdf"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "15",
        "instruction": "You are responsible for validating Q2-2024 MEALS_ENTERTAIN controls. Analyze '2024-04-01' to '2024-06-30' with a threshold of 150.0, record a zero-value memo 'Q2 meals scan \u2013 no exceptions' in 'Governance Memo', and store KPI 'Q2_Meals_Controls_2024-06-30' as_of '2024-06-30' with sections ['Deductibility']. Return the KPI path.",
        "actions": [
            {
                "name": "ListExpensesByDateRangeAndCategory",
                "arguments": {
                    "start_date": "2024-04-01",
                    "end_date": "2024-06-30",
                    "categories": [
                        "MEALS_ENTERTAIN"
                    ]
                },
            },
            {
                "name": "FlagHighValueMeals",
                "arguments": {
                    "expenses_ref": {
                        "expenses": [
                            {
                                "expense_id": "EXP019",
                                "category_code": "MEALS_ENTERTAIN",
                                "gross_amount": 18.75
                            }
                        ]
                    },
                    "threshold": 150.0
                },
            },
            {
                "name": "PostJournalEntry",
                "arguments": {
                    "date": "2024-06-30",
                    "account": "Governance Memo",
                    "amount_ref": {
                        "adjustment": 0.0
                    },
                    "memo": "Q2 meals scan – no exceptions"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-06-30",
                    "artifact_name": "Q2_Meals_Controls_2024-06-30",
                    "sections": [
                        "Deductibility"
                    ]
                }
            }
        ],
        "outputs": [
                "/reports/kpi/Q2_Meals_Controls_2024-06-30.pdf"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "16",
        "instruction": "Your task is to prepare a PUB002 collections snapshot as of '2024-11-30'. Assess ['INV012','INV023'] using today '2024-11-30'. Policy: items beyond 60 days receive a 'second_notice' with notes 'Overdue >60 days'. In a snapshot memo, no escalation is opened; provide two lists in order: acted (notices sent) and escalated (empty for this snapshot). Archive KPI as_of '2024-11-30' with sections ['Collections'] (artifact_name 'PUB002_Collections_Snapshot_2024-11-30').",
        "actions": [
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV012",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV023",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV012",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV023",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "sections": [
                        "Collections"
                    ],
                    "artifact_name": "PUB002_Collections_Snapshot_2024-11-30"
                }
            }
        ],
        "outputs": [
                [
                    "INV012",
                    "INV023"
                ],
                []
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "17",
        "instruction": "Handle issuing a November 2024 invoice for 'Midwest Education House' (PUB005) on project PROJ010 using time entry TIME017. The invoice must utilize invoice_id 'INV-AUTO-2024-604', invoice_number 'INV-2024-604', invoice_date '2024-11-30', and apply HST 0.13. Archive the PDF and document audit 'generated' with notes 'Invoice generated'. Return the invoice_number.",
        "actions": [
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV012",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV023",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV012",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV023",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "sections": [
                        "Aging"
                    ],
                    "artifact_name": "PUB002_AR_Health_2024-11-30"
                }
            }
        ],
        "outputs": [
                [
                    "INV012",
                    "INV023"
                ],
                []
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "18",
        "instruction": "Coordinate the drafting of a PUB003 AR follow-up memo dated '2024-11-30'. Evaluate ['INV008','INV022'] using the current date '2024-11-30'. Dispatch 'second_notice' for those over 60 days, including notes 'Overdue >60 days'. Provide two arrays sequentially: acted (notices sent) and escalated (none here). Store KPI as_of '2024-11-30' in sections ['Aging'] (artifact_name 'PUB003_Followup_Memo_2024-11-30').",
        "actions": [
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV008",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV022",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV008",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV022",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "sections": [
                        "Aging"
                    ],
                    "artifact_name": "PUB003_Followup_Memo_2024-11-30"
                }
            }
        ],
        "outputs": [
                [
                    "INV008",
                    "INV022"
                ],
                []
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "20",
        "instruction": "Conduct a PUB005 escalation audit effective '2024-11-30' for ['INV022','INV026'] using today's date '2024-11-30'. Ensure to log 'second_notice' with notes 'Overdue >60 days' where applicable for >60 days. Return both acted and escalated entries. Archive KPI dated '2024-11-30' in sections ['Collections'] (artifact_name 'PUB005_Escalation_Audit_2024-11-30').",
        "actions": [
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV022",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV026",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV022",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV026",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "sections": [
                        "Collections"
                    ],
                    "artifact_name": "PUB005_Escalation_Audit_2024-11-30"
                }
            }
        ],
        "outputs": [
                [
                    "INV022",
                    "INV026"
                ],
                []
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "21",
        "instruction": "Prepare an aging digest for PUB001 and PUB002 as of '2024-11-30'. PUB001 involves: ['INV004','INV009']; PUB002 involves: ['INV012']; as of today's date '2024-11-30'. Implement the policy (>60 days => 'second_notice' with notes 'Overdue >60 days'). Return two arrays in this order: those acted upon (notices sent across both publishers) and escalations (none for this digest). Archive KPI as of '2024-11-30' within sections ['Aging'] (artifact_name 'Mixed_Aging_Digest_2024-11-30').",
        "actions": [
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV004",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV009",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV012",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV009",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV012",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "sections": [
                        "Aging"
                    ],
                    "artifact_name": "Mixed_Aging_Digest_2024-11-30"
                }
            }
        ],
        "outputs": [
                [
                    "INV009",
                    "INV012"
                ],
                []
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "22",
        "instruction": "Flag high-value meals for Q2 2024 in MEALS_ENTERTAIN during '2024-04-01'..'2024-06-30' with a threshold of 150.0. Make a governance memo entry and archive KPI as_of '2024-06-30' sections ['Deductibility'] (artifact_name 'Q2_Meals_Flag_2024-06-30'). Return KPI path.",
        "actions": [
            {
                "name": "ListExpensesByDateRangeAndCategory",
                "arguments": {
                    "start_date": "2024-04-01",
                    "end_date": "2024-06-30",
                    "categories": [
                        "MEALS_ENTERTAIN"
                    ]
                },
            },
            {
                "name": "FlagHighValueMeals",
                "arguments": {
                    "expenses_ref": {
                        "expenses": [
                            {
                                "expense_id": "EXP019",
                                "category_code": "MEALS_ENTERTAIN",
                                "gross_amount": 18.75
                            }
                        ]
                    },
                    "threshold": 150.0
                },
            },
            {
                "name": "PostJournalEntry",
                "arguments": {
                    "date": "2024-06-30",
                    "account": "Governance Memo",
                    "amount": 0.0,
                    "memo": "High-value meals scan completed (threshold=150.0)"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-06-30",
                    "sections": [
                        "Deductibility"
                    ],
                    "artifact_name": "Q2_Meals_Flag_2024-06-30"
                }
            }
        ],
        "outputs": [
                "/reports/kpi/Q2_Meals_Flag_2024-06-30.pdf"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "23",
        "instruction": "Assemble a risk overview for PUB003 as of '2024-11-30' using expected inflows for ['INV008','INV013','INV022'] with probability_rule 'overdue_60=0.3' and note required second notices for items exceeding 60 days. Archive KPI as_of '2024-11-30' sections ['Collections'] (artifact_name 'PUB003_Risk_Overview_2024-11-30'). Return KPI path.",
        "actions": [
            {
                "name": "ForecastInflows",
                "arguments": {
                    "invoices": [
                        "INV008",
                        "INV013",
                        "INV022"
                    ],
                    "probability_rule": "overdue_60=0.3"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV008",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV013",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV022",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "sections": [
                        "Collections"
                    ],
                    "artifact_name": "PUB003_Risk_Overview_2024-11-30"
                }
            }
        ],
        "outputs": [
                "/reports/kpi/PUB003_Risk_Overview_2024-11-30.pdf"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "24",
        "instruction": "Handle the preparation of a collections digest for PUB003 dated '2024-11-30' using anticipated inflows for ['INV008','INV013','INV022'] with probability_rule 'overdue_60=0.3'. Archive KPI for as_of '2024-11-30' sections ['Collections'] (artifact_name 'PUB003_Collections_Digest_2024-11-30'). Provide the KPI path.",
        "actions": [
            {
                "name": "ForecastInflows",
                "arguments": {
                    "invoices": [
                        "INV008",
                        "INV013",
                        "INV022"
                    ],
                    "probability_rule": "overdue_60=0.3"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "sections": [
                        "Collections"
                    ],
                    "artifact_name": "PUB003_Collections_Digest_2024-11-30"
                }
            }
        ],
        "outputs": [
                "/reports/kpi/PUB003_Collections_Digest_2024-11-30.pdf"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "25",
        "instruction": "Coordinate the creation of a PUB003 AR bundle dated '2024-11-30' validating ['INV008','INV022'] as of today '2024-11-30'. Dispatch 'second_notice' for items overdue by over 60 days and archive KPI for as_of '2024-11-30' sections ['Aging','Collections'] (artifact_name 'PUB003_AR_Bundle_2024-11-30'). Produce two arrays: acted (notices sent) and escalated (none).",
        "actions": [
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV008",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV022",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV008",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV022",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "sections": [
                        "Aging",
                        "Collections"
                    ],
                    "artifact_name": "PUB003_AR_Bundle_2024-11-30"
                }
            }
        ],
        "outputs": [
                [
                    "INV008",
                    "INV022"
                ],
                []
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "26",
        "instruction": "Prepare a PUB002 collections snapshot dated '2024-11-30'. Assess ['INV012','INV023'] as of today '2024-11-30'. Any items older than 60 days should be issued a 'second_notice' with the notes 'Overdue >60 days'. Provide two arrays in order: acted (notices sent) and escalated (empty for this snapshot). Store KPI with the date '2024-11-30' in sections ['Collections'] (artifact_name 'PUB002_Collections_Snapshot_2024-11-30').",
        "actions": [
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV012",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV023",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV012",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV023",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "sections": [
                        "Collections"
                    ],
                    "artifact_name": "PUB002_Collections_Snapshot_2024-11-30"
                }
            }
        ],
        "outputs": [
                [
                    "INV012",
                    "INV023"
                ],
                []
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "27",
        "instruction": "Conduct an audit of Q2 2024 expenses for TRAINING_DEV and MEALS_ENTERTAIN for the period '2024-04-01'..'2024-06-30'. Implement deductibility for EXP018 and EXP019 and save the KPI as_of '2024-06-30' in sections ['Deductibility'] (artifact_name 'Q2_Expense_Audit_2024-06-30'). Deliver the KPI path.",
        "actions": [
            {
                "name": "ListExpensesByDateRangeAndCategory",
                "arguments": {
                    "start_date": "2024-04-01",
                    "end_date": "2024-06-30",
                    "categories": [
                        "TRAINING_DEV",
                        "MEALS_ENTERTAIN"
                    ]
                },
            },
            {
                "name": "ApplyDeductibilityRules",
                "arguments": {
                    "expense_id": "EXP018"
                },
            },
            {
                "name": "ApplyDeductibilityRules",
                "arguments": {
                    "expense_id": "EXP019"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-06-30",
                    "sections": [
                        "Deductibility"
                    ],
                    "artifact_name": "Q2_Expense_Audit_2024-06-30"
                }
            }
        ],
        "outputs": [
                "/reports/kpi/Q2_Expense_Audit_2024-06-30.pdf"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "28",
        "instruction": "Initiate a PUB002 late-stage AR assessment as of '2024-11-30' for ['INV012','INV023'] using today '2024-11-30'. Dispatch 'second_notice' for items older than 60 days and archive KPI as_of '2024-11-30' within sections ['Collections'] (artifact_name 'PUB002_LateStage_2024-11-30'). Provide two lists: acted (notices sent) and escalated (none).",
        "actions": [
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV012",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV023",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV012",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV023",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "sections": [
                        "Collections"
                    ],
                    "artifact_name": "PUB002_LateStage_2024-11-30"
                }
            }
        ],
        "outputs": [
                [
                    "INV012",
                    "INV023"
                ],
                []
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "29",
        "instruction": "Generate a zero-total November 2024 shell invoice for 'Northern Star Publishers' (PUB001). Use invoice_id 'INV-AUTO-2024-034' and invoice_number 'INV-2024-034' with invoice_date '2024-11-30', period '2024-11-01'..'2024-11-30', and pdf_path '/invoices/auto/INV-AUTO-2024-034.pdf'. Record 'generated' with the comment 'Invoice generated' and archive KPI as_of '2024-11-30' within sections ['Issuance'] (artifact_name 'PUB001_Shell_Issue_2024-11'). Return 'INV-2024-034'.",
        "actions": [
            {
                "name": "CalculateTotals",
                "arguments": {
                    "invoice_lines": [],
                    "hst_rate": 0.13
                },
            },
            {
                "name": "InsertInvoice",
                "arguments": {
                    "invoice_id": "INV-AUTO-2024-034",
                    "publisher_id": "PUB001",
                    "subtotal": 0.0,
                    "hst_amount": 0.0,
                    "total_due": 0.0,
                    "invoice_number": "INV-2024-034",
                    "invoice_date": "2024-11-30",
                    "period_start": "2024-11-01",
                    "period_end": "2024-11-30",
                    "pdf_path": "/invoices/auto/INV-AUTO-2024-034.pdf"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV-AUTO-2024-034",
                    "event_type": "generated",
                    "notes": "Invoice generated"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "sections": [
                        "Issuance"
                    ],
                    "artifact_name": "PUB001_Shell_Issue_2024-11"
                }
            }
        ],
        "outputs": [
                "INV-2024-034"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "30",
        "instruction": "Handle the issuance of a November 2024 invoice for 'Summit Educational Publishing' (PUB003) related to project PROJ006. Bill for work approved in November ('2024-11-01'..'2024-11-30') using time entry TIME018. Ensure the invoice uses invoice_id 'INV-AUTO-2024-601', invoice_number 'INV-2024-601', invoice_date '2024-11-30', and include HST 0.13. Archive the PDF and log an audit event 'generated' with notes 'Invoice generated'. Return the invoice_number.",
        "actions": [
            {
                "name": "ResolveHourlyRate",
                "arguments": {
                    "project_id": "PROJ006"
                },
            },
            {
                "name": "ListTimeEntries",
                "arguments": {
                    "project_id": "PROJ006",
                    "month": "2024-11"
                },
            },
            {
                "name": "BuildInvoiceLines",
                "arguments": {
                    "time_entries": [
                        "TIME018"
                    ],
                    "hourly_rate": 100.0
                },
            },
            {
                "name": "CalculateTotals",
                "arguments": {
                    "invoice_lines": [
                        {
                            "line_amount": 600.0
                        }
                    ],
                    "hst_rate": 0.13
                },
            },
            {
                "name": "ComposeInvoicePdf",
                "arguments": {
                    "invoice_id": "INV-AUTO-2024-601",
                    "publisher_id": "PUB003"
                },
            },
            {
                "name": "InsertInvoice",
                "arguments": {
                    "invoice_id": "INV-AUTO-2024-601",
                    "publisher_id": "PUB003",
                    "subtotal": 600.0,
                    "hst_amount": 78.0,
                    "total_due": 678.0,
                    "invoice_number": "INV-2024-601",
                    "invoice_date": "2024-11-30",
                    "pdf_path": "/invoices/auto/INV-AUTO-2024-601.pdf"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV-AUTO-2024-601",
                    "event_type": "generated",
                    "notes": "Invoice generated"
                }
            }
        ],
        "outputs": [
                "INV-2024-601"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "31",
        "instruction": "Coordinate the production of a collections outlook for PUB003 as of '2024-11-30'. Utilize expected inflows for ['INV008','INV013','INV022'] with probability_rule 'overdue_60=0.3' and archive KPI as_of '2024-11-30' with sections ['Collections'] (artifact_name 'PUB003_Collections_Outlook_2024-11-30'). Return the KPI pdf path.",
        "actions": [
            {
                "name": "ForecastInflows",
                "arguments": {
                    "invoices": [
                        "INV008",
                        "INV013",
                        "INV022"
                    ],
                    "probability_rule": "overdue_60=0.3"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "sections": [
                        "Collections"
                    ],
                    "artifact_name": "PUB003_Collections_Outlook_2024-11-30"
                }
            }
        ],
        "outputs": [
                "/reports/kpi/PUB003_Collections_Outlook_2024-11-30.pdf"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "32",
        "instruction": "Handle the validation of a PUB003 collections digest as of '2024-11-30'. Use expected inflows from ['INV008','INV013','INV022'] with the probability_rule 'overdue_60=0.3' and save the archive KPI as_of '2024-11-30' with sections ['Collections'] (artifact_name 'PUB003_Collections_Digest_2024-11-30'). Provide the KPI pdf path.",
        "actions": [
            {
                "name": "ForecastInflows",
                "arguments": {
                    "invoices": [
                        "INV008",
                        "INV013",
                        "INV022"
                    ],
                    "probability_rule": "overdue_60=0.3"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "sections": [
                        "Collections"
                    ],
                    "artifact_name": "PUB003_Collections_Digest_2024-11-30"
                }
            }
        ],
        "outputs": [
                "/reports/kpi/PUB003_Collections_Digest_2024-11-30.pdf"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "33",
        "instruction": "Oversee the enforcement of A/R follow-ups for 'Summit Educational Publishing' (PUB003) as of '2024-11-30'. Assess ['INV008','INV022'] with today's date '2024-11-30'. According to policy, dispatch 'second_notice' with the message 'Overdue >60 days' for all items exceeding 60 days; handle escalated items as the 90+ bucket exclusively. Save a KPI as_of '2024-11-30' with sections ['Aging','Collections'] (artifact_name 'PUB003_AR_Followups_2024-11-30'). Deliver two lists: acted items (>60d) and escalated items (90+).",
        "actions": [
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV008",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV022",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV008",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV022",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "sections": [
                        "Aging",
                        "Collections"
                    ],
                    "artifact_name": "PUB003_AR_Followups_2024-11-30"
                }
            }
        ],
        "outputs": [
                [
                    "INV008",
                    "INV022"
                ],
                [
                    "INV008",
                    "INV022"
                ]
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "34",
        "instruction": "Produce a PUB001 spot check dated '2024-11-30'. Categorize ['INV004','INV009'] effective '2024-11-30'; issue 'second_notice' for items overdue by >60 days and consider past due as 90+. Store KPI as_of '2024-11-30' with categories ['Aging'] (artifact_name 'PUB001_Spot_2024-11-30'). Provide lists of acted and escalated cases.",
        "actions": [
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV004",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV009",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV009",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "sections": [
                        "Aging"
                    ],
                    "artifact_name": "PUB001_Spot_2024-11-30"
                }
            }
        ],
        "outputs": [
                [
                    "INV009"
                ],
                []
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "50",
        "instruction": "Coordinate PUB003\u2019s collections posture for month-end. Effective '2024-11-30', both 'INV008' and 'INV022' reflect their determined aging and, if 60+ days overdue, an audit titled 'second_notice' with the annotation 'Overdue >60 days'. A collections KPI 'PUB003_MonthEnd_Collections_2024-11-30' completes the picture. Final scenario: the necessary 'second_notice' entries are present and the KPI PDF is generated.",
        "actions": [
            {
                "name": "ForecastInflows",
                "arguments": {
                    "invoices": [
                        "INV008",
                        "INV013",
                        "INV022"
                    ],
                    "probability_rule": "overdue_60=0.3"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "sections": [
                        "Collections"
                    ],
                    "artifact_name": "PUB003_Collections_Prob_2024-11-30"
                }
            }
        ],
        "outputs": [
                "/reports/kpi/PUB003_Collections_Prob_2024-11-30.pdf"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "35",
        "instruction": "Handle the creation of a PUB003 enforcement bundle as of '2024-11-30'. Classify ['INV008','INV022'] on the date '2024-11-30'; dispatch 'second_notice' after >60d; escalated as 90+. Archive KPI as_of '2024-11-30' with sections ['Aging','Collections'] (artifact_name 'PUB003_Enforcement_2024-11-30'). Provide lists of acted and escalated items.",
        "actions": [
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV008",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV022",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV008",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV022",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "sections": [
                        "Aging",
                        "Collections"
                    ],
                    "artifact_name": "PUB003_Enforcement_2024-11-30"
                }
            }
        ],
        "outputs": [
                [
                    "INV008",
                    "INV022"
                ],
                [
                    "INV008",
                    "INV022"
                ]
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "36",
        "instruction": "Coordinate the delivery of the Q3-2024 mixed expense pack. For the period '2024-07-01' to '2024-09-30', standardize the deductibility for EXP012 (OFFICE_SUPPLIES) and EXP022/EXP023 (TRAVEL_EXPENSE), produce the '2024-Q3' dashboard, and archive KPI 'Q3_Mixed_Pack_2024-09-30' as_of '2024-09-30' with sections ['ExpenseMix','Deductibility']. Provide the path to the dashboard.",
        "actions": [
            {
                "name": "ListExpensesByDateRangeAndCategory",
                "arguments": {
                    "start_date": "2024-07-01",
                    "end_date": "2024-09-30",
                    "categories": [
                        "OFFICE_SUPPLIES",
                        "TRAVEL_EXPENSE"
                    ]
                },
            },
            {
                "name": "ApplyDeductibilityRules",
                "arguments": {
                    "expense_id": "EXP012"
                },
            },
            {
                "name": "ApplyDeductibilityRules",
                "arguments": {
                    "expense_id": "EXP022"
                },
            },
            {
                "name": "ApplyDeductibilityRules",
                "arguments": {
                    "expense_id": "EXP023"
                },
            },
            {
                "name": "GenerateExpenseDashboard",
                "arguments": {
                    "quarter": "2024-Q3",
                    "included_expenses": [
                        "EXP012",
                        "EXP022",
                        "EXP023"
                    ]
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-09-30",
                    "artifact_name": "Q3_Mixed_Pack_2024-09-30",
                    "sections": [
                        "ExpenseMix",
                        "Deductibility"
                    ]
                }
            }
        ],
        "outputs": [
                "/dashboards/ExpenseDashboards/2024-Q3/expense_dashboard_2024-Q3.pdf"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "37",
        "instruction": "Confirm the November 2024 tax reserve at month_end '2024-11-30'. Align the 2024 reserve with 'SNAP004' (threshold 0.01), record 157.87 to 'Tax Reserve' (memo 'YTD tax reserve true-up'), and archive KPI as_of '2024-11-30' (artifact_name 'TaxReserve_Alignment_2024-11'). Return 157.87.",
        "actions": [
            {
                "name": "ComputeYtdFromMonthlyRevenue",
                "arguments": {
                    "year": 2024,
                    "through_month": 11
                },
            },
            {
                "name": "ComputeTaxReserve",
                "arguments": {
                    "ytd_revenue": 10909.5,
                    "tax_year": 2024
                },
            },
            {
                "name": "GetDashboardSnapshot",
                "arguments": {
                    "snapshot_id": "SNAP004"
                },
            },
            {
                "name": "ReconcileTaxReserve",
                "arguments": {
                    "computed_tax_reserve_ref": {
                        "tax_reserve": 2891.02
                    },
                    "snapshot_ref": {
                        "ytd_tax_reserve": 2733.15
                    },
                    "threshold": 0.01
                },
            },
            {
                "name": "PostJournalEntry",
                "arguments": {
                    "date": "2024-11-30",
                    "account": "Tax Reserve",
                    "amount_ref": {
                        "adjustment": 157.87
                    },
                    "memo": "YTD tax reserve true-up"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "sections": [
                        "TaxReserve"
                    ],
                    "artifact_name": "TaxReserve_Alignment_2024-11"
                }
            }
        ],
        "outputs": [
                "157.87"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "38",
        "instruction": "Verify November 2024 tax reserve values at month_end '2024-11-30'. Align with 'SNAP004' (threshold 0.01), record 157.87 to 'Tax Reserve' (memo 'YTD tax reserve true-up'), and archive KPI as_of '2024-11-30' (artifact_name 'TaxReserve_Verify_2024-11'). Return 157.87.",
        "actions": [
            {
                "name": "ComputeYtdFromMonthlyRevenue",
                "arguments": {
                    "year": 2024,
                    "through_month": 11
                },
            },
            {
                "name": "ComputeTaxReserve",
                "arguments": {
                    "ytd_revenue": 10909.5,
                    "tax_year": 2024
                },
            },
            {
                "name": "GetDashboardSnapshot",
                "arguments": {
                    "snapshot_id": "SNAP004"
                },
            },
            {
                "name": "ReconcileTaxReserve",
                "arguments": {
                    "computed_tax_reserve_ref": {
                        "tax_reserve": 2891.02
                    },
                    "snapshot_ref": {
                        "ytd_tax_reserve": 2733.15
                    },
                    "threshold": 0.01
                },
            },
            {
                "name": "PostJournalEntry",
                "arguments": {
                    "date": "2024-11-30",
                    "account": "Tax Reserve",
                    "amount_ref": {
                        "adjustment": 157.87
                    },
                    "memo": "YTD tax reserve true-up"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "sections": [
                        "TaxReserve"
                    ],
                    "artifact_name": "TaxReserve_Verify_2024-11"
                }
            }
        ],
        "outputs": [
                "157.87"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "39",
        "instruction": "Handle A/R enforcement verification for 'Aurora Academic Press' (PUB002) as of '2024-11-30'. From PUB002 open items, calculate aging for invoices ['INV012','INV023'] using today '2024-11-30' and, following the policy, record a 'second_notice' with notes 'Overdue >60 days' for any over 60 days. Archive a KPI artifact as_of '2024-11-30' with artifact_name 'PUB002_Collections_2024-11-30'. Provide two lists: acted invoices and escalated ones.",
        "actions": [
            {
                "name": "ListPublisherOpenInvoices",
                "arguments": {
                    "publisher_id": "PUB002"
                },
            },
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV012"
                },
            },
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV023"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV012",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV023",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV012",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV023",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "artifact_name": "PUB002_Collections_2024-11-30"
                }
            }
        ],
        "outputs": [
                [
                    "INV012",
                    "INV023"
                ],
                [
                    "INV012",
                    "INV023"
                ]
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "40",
        "instruction": "Coordinate the final review of a PUB002 late-stage AR check as of '2024-11-30'. Evaluate ['INV012','INV023'] using today '2024-11-30', document 'second_notice' for >60d and 'escalated' for 90+, and archive KPI as_of '2024-11-30' with artifact_name 'PUB002_LateStage_2024-11-30'. Provide acted and escalated lists.",
        "actions": [
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV012",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV023",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV012",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV023",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV012",
                    "event_type": "escalated",
                    "notes": "Overdue 90+ days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV023",
                    "event_type": "escalated",
                    "notes": "Overdue 90+ days"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "artifact_name": "PUB002_LateStage_2024-11-30"
                }
            }
        ],
        "outputs": [
                [
                    "INV012",
                    "INV023"
                ],
                [
                    "INV012",
                    "INV023"
                ]
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "41",
        "instruction": "You are drafting a PUB003 follow-up memo dated '2024-11-30'. Categorize ['INV008','INV022'] with today '2024-11-30', dispatch 'second_notice' for more than 60 days and record 'escalated' for 90+. Store KPI as_of '2024-11-30' under the name 'PUB003_Followup_Memo_2024-11-30'. Provide lists of actions taken and escalated cases.",
        "actions": [
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV008",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV022",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV008",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV022",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV008",
                    "event_type": "escalated",
                    "notes": "Overdue 90+ days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV022",
                    "event_type": "escalated",
                    "notes": "Overdue 90+ days"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "artifact_name": "PUB003_Followup_Memo_2024-11-30"
                }
            }
        ],
        "outputs": [
                [
                    "INV008",
                    "INV022"
                ],
                [
                    "INV008",
                    "INV022"
                ]
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "42",
        "instruction": "You are organizing a PUB002 late-stage memo dated '2024-11-30'. Examine ['INV012','INV023'] with today '2024-11-30', document 'second_notice' for over 60 days and 'escalated' for 90+, and file KPI as_of '2024-11-30' with the title 'PUB002_LateStage_Memo_2024-11-30'. Present lists of actions and escalated situations.",
        "actions": [
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV012",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV023",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV012",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV023",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV012",
                    "event_type": "escalated",
                    "notes": "Overdue 90+ days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV023",
                    "event_type": "escalated",
                    "notes": "Overdue 90+ days"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "artifact_name": "PUB002_LateStage_Memo_2024-11-30"
                }
            }
        ],
        "outputs": [
                [
                    "INV012",
                    "INV023"
                ],
                [
                    "INV012",
                    "INV023"
                ]
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "43",
        "instruction": "Handle validation of PUB002 collections as of '2024-11-30'. Assess ['INV012','INV023'] from PUB002 using today's date '2024-11-30'; log 'second_notice' with the note 'Overdue >60 days' for items exceeding 60 days. Store a KPI as_of '2024-11-30' with the artifact_name 'PUB002_Collections_Validate_2024-11-30'. Provide two lists: acted and escalated (>60).",
        "actions": [
            {
                "name": "ListPublisherOpenInvoices",
                "arguments": {
                    "publisher_id": "PUB002"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV012",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV023",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV012",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV023",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "artifact_name": "PUB002_Collections_Validate_2024-11-30"
                }
            }
        ],
        "outputs": [
                [
                    "INV012",
                    "INV023"
                ],
                [
                    "INV012",
                    "INV023"
                ]
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "44",
        "instruction": "Coordinate the validation of PUB001 follow-ups as of '2024-11-30'. Calculate aging for ['INV009','INV021','INV026'] with the date '2024-11-30' and log 'second_notice' with the note 'Overdue >60 days' for those past 60 days. Store a KPI as_of '2024-11-30' with the artifact_name 'PUB001_Followups_2024-11-30'. Supply acted and escalated (>60) lists.",
        "actions": [
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV009",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV021",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV026",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV009",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV021",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV026",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "artifact_name": "PUB001_Followups_2024-11-30"
                }
            }
        ],
        "outputs": [
                [
                    "INV009",
                    "INV021",
                    "INV026"
                ],
                [
                    "INV009",
                    "INV021",
                    "INV026"
                ]
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "45",
        "instruction": "Handle PUB005 follow-ups as of '2024-11-30'. Investigate ['INV011','INV022','INV026'] with the date '2024-11-30'; record 'second_notice' with the note 'Overdue >60 days' for any item exceeding 60 days. Save a KPI as_of '2024-11-30' with artifact_name 'PUB005_Followups_2024-11-30'. Provide two lists: acted and escalated (>60).",
        "actions": [
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV011",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV022",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV026",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV022",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV026",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "artifact_name": "PUB005_Followups_2024-11-30"
                }
            }
        ],
        "outputs": [
                [
                    "INV022",
                    "INV026"
                ],
                [
                    "INV022",
                    "INV026"
                ]
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "46",
        "instruction": "Coordinate a PUB001 AR bundle consolidation as of '2024-11-30'. Examine ['INV009','INV021','INV026'] using the date '2024-11-30'; document 'second_notice' with 'Overdue >60 days'; store a KPI as_of '2024-11-30' with artifact_name 'PUB001_AR_Bundle_2024-11-30'. Supply lists of acted and escalated (>60).",
        "actions": [
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV009",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV021",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV026",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV009",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV021",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV026",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "artifact_name": "PUB001_AR_Bundle_2024-11-30"
                }
            }
        ],
        "outputs": [
                [
                    "INV009",
                    "INV021",
                    "INV026"
                ],
                [
                    "INV009",
                    "INV021",
                    "INV026"
                ]
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "47",
        "instruction": "Handle the assembly of a PUB005 AR wrap-up as of '2024-11-30'. Evaluate ['INV011','INV022','INV026'] on the date '2024-11-30'; record 'second_notice' with 'Overdue >60 days' for any item exceeding 60 days overdue; archive a KPI as_of '2024-11-30' with artifact_name 'PUB005_AR_Wrap_2024-11-30'. Provide two lists in return: acted and escalated (>60).",
        "actions": [
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV011"
                },
            },
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV022"
                },
            },
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV026"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV011",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV022",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV026",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV022",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV026",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "artifact_name": "PUB005_AR_Wrap_2024-11-30"
                }
            }
        ],
        "outputs": [
                [
                    "INV022",
                    "INV026"
                ],
                [
                    "INV022",
                    "INV026"
                ]
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "48",
        "instruction": "Coordinate the completion of PUB003's A/R review for '2024-11-30'. Concentrate on invoices 'INV008' and 'INV022' as of '2024-11-30'; if any item is 60+ days overdue, assign its record a 'second_notice' with notes 'Overdue >60 days'. Conclude the review by saving a collections KPI under artifact_name 'PUB003_AR_Review_2024-11-30' for that date. End state: 'INV008' and 'INV022' are reviewed and aged as of '2024-11-30'; any 60+ day overdue item carries a 'second_notice' (notes 'Overdue >60 days'); the KPI PDF for 'PUB003_AR_Review_2024-11-30' is generated.",
        "actions": [
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV008"
                },
            },
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV022"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV008",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV022",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV008",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV022",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "sections": [
                        "Collections"
                    ],
                    "artifact_name": "PUB003_AR_Review_2024-11-30"
                }
            }
        ],
        "outputs": [
                "/reports/kpi/PUB003_AR_Review_2024-11-30.pdf"
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "49",
        "instruction": "Handle the closure of PUB003 A/R dated '2024-11-30'. On this day, invoices 'INV008' and 'INV022' are recorded; any item overdue by more than 60 days includes an audit tagged 'second_notice' with the note 'Overdue >60 days'. Archive a collections KPI labeled 'PUB003_AR_Review_2024-11-30' in sections ['Collections']. Final situation: both invoices are reviewed and aged as of '2024-11-30'; any item over 60 days carries a 'second_notice' marked as 'Overdue >60 days'; the KPI PDF is available for 'PUB003_AR_Review_2024-11-30'.",
        "actions": [
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV008"
                },
            },
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV022"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV008",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV022",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV008",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV022",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "sections": [
                        "Collections"
                    ],
                    "artifact_name": "PUB003_AR_Review_2024-11-30"
                }
            }
        ],
        "outputs": [
                "/reports/kpi/PUB003_AR_Review_2024-11-30.pdf"
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "50",
        "instruction": "Coordinate PUB003\u2019s collections posture for month-end. Effective '2024-11-30', both 'INV008' and 'INV022' reflect their determined aging and, if 60+ days overdue, an audit titled 'second_notice' with the annotation 'Overdue >60 days'. A collections KPI 'PUB003_MonthEnd_Collections_2024-11-30' completes the picture. Final scenario: the necessary 'second_notice' entries are present and the KPI PDF is generated.",
        "actions": [
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV008",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV008",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV022",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV022",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "sections": [
                        "Collections"
                    ],
                    "artifact_name": "PUB003_MonthEnd_Collections_2024-11-30"
                }
            }
        ],
        "outputs": [
                "/reports/kpi/PUB003_MonthEnd_Collections_2024-11-30.pdf"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "51",
        "instruction": "As a financial consulting worker, your task is to support PUB003's A/R reflecting the date '2024-11-30' for Summit Educational Publishing. Handle 'INV008' and 'INV022', determine the aging as of '2024-11-30', and document 'second_notice' with the note 'Overdue >60 days' for items exceeding 60 days. Archive a KPI dated '2024-11-30', ensuring it includes sections ['Collections'] and assign the artifact_name 'PUB003_AR_Review_2024-11-30'. Provide '/reports/kpi/PUB003_AR_Review_2024-11-30.pdf'.",
        "actions": [
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV008"
                },
            },
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV022"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV008",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV022",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV008",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV022",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "sections": [
                        "Collections"
                    ],
                    "artifact_name": "PUB003_AR_Review_2024-11-30"
                }
            }
        ],
        "outputs": [
                "/reports/kpi/PUB003_AR_Review_2024-11-30.pdf"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "52",
        "instruction": "Act as a financial consulting worker closing PUB001 AR transactions for the date '2024-11-30' at Northern Star Publishers. Calculate the aging for ['INV009','INV021','INV026'] on '2024-11-30', log 'second_notice' with the annotation 'Overdue >60 days' for all items beyond 60 days, and preserve a KPI as_of '2024-11-30' with sections like ['Collections'], naming the artifact 'PUB001_Collections_2024-11-30'. Deliver ['/reports/kpi/PUB001_Collections_2024-11-30.pdf'].",
        "actions": [
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV009",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV021",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV026",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV009",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV021",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV026",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "sections": [
                        "Collections"
                    ],
                    "artifact_name": "PUB001_Collections_2024-11-30"
                }
            }
        ],
        "outputs": [
                "/reports/kpi/PUB001_Collections_2024-11-30.pdf"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "53",
        "instruction": "As a financial consulting worker, handle a cross-publisher AR sweep as of '2024-11-30' for PUB003, PUB002, and PUB001. Calculate aging for ['INV008','INV012','INV009'] using today '2024-11-30', log 'second_notice' with notes 'Overdue >60 days' for all >60d, and store a KPI as_of '2024-11-30' with sections ['Collections'] and artifact_name 'Cross_AR_Sweep_2024-11-30'. Return ['/reports/kpi/Cross_AR_Sweep_2024-11-30.pdf'].",
        "actions": [
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV008",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV012",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV009",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV008",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV012",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV009",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "sections": [
                        "Collections"
                    ],
                    "artifact_name": "Cross_AR_Sweep_2024-11-30"
                }
            }
        ],
        "outputs": [
                "/reports/kpi/Cross_AR_Sweep_2024-11-30.pdf"
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "54",
        "instruction": "In your role as a financial consulting worker, manage a PUB002 collections summary as of '2024-11-30'. Calculate aging for ['INV012','INV023'] using today '2024-11-30', log 'second_notice' with notes 'Overdue >60 days', and preserve a KPI as_of '2024-11-30' with sections ['Collections'] and artifact_name 'PUB002_Collections_2024-11-30'. Return '/reports/kpi/PUB002_Collections_2024-11-30.pdf'.",
        "actions": [
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV012",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV023",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV012",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV023",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "sections": [
                        "Collections"
                    ],
                    "artifact_name": "PUB002_Collections_2024-11-30"
                }
            }
        ],
        "outputs": [
                "/reports/kpi/PUB002_Collections_2024-11-30.pdf"
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "55",
        "instruction": "As a financial consulting worker for Aurora Academic Press (PUB002), verify on '2024-11-30' that the overdue-notice policy is accurately captured on ['INV012','INV023'] and maintain a dated aging record ('PUB002_Aging_2024-11-30') for that date. Provide '/reports/kpi/PUB002_Aging_2024-11-30.pdf'.",
        "actions": [
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV012"
                },
            },
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV023"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV012",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV023",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV012",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV023",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "sections": [
                        "Aging"
                    ],
                    "artifact_name": "PUB002_Aging_2024-11-30"
                }
            }
        ],
        "outputs": [
                "/reports/kpi/PUB002_Aging_2024-11-30.pdf"
        ]
    }
    ,
    {
        "annotator": A,
        "user_id": "56",
        "instruction": "Coordinate the delivery of a Maple Leaf Publishing (PUB001) enforcement note for '2024-11-30'. Sort 'INV004','INV009','INV021' as of today '2024-11-30', disregarding any paid or current items; issue 'second_notice' for entries older than 60 days. Store the KPI 'PUB001_Enforcement_2024-11-30' under the categories ['Aging','Collections'].",
        "actions": [
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV004"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV004",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV009",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV021",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV009",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV021",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "sections": [
                        "Aging",
                        "Collections"
                    ],
                    "artifact_name": "PUB001_Enforcement_2024-11-30"
                }
            }
        ],
        "outputs": [
                "/reports/kpi/PUB001_Enforcement_2024-11-30.pdf"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "57",
        "instruction": "As a financial consulting professional, validate the governance of Q3-2024 OFFICE_SUPPLIES (EXP012) for the dates '2024-07-01' to '2024-09-30'. Implement deductibility, draft a policy review memo for 'Governance Memo' with the memo text 'OFFICE_SUPPLIES Q3 checked (EXP012)', and store a KPI as_of '2024-09-30' with the artifact name 'Q3_OfficeSupplies_Check_2024-09-30'. Provide the path to the KPI.",
        "actions": [
            {
                "name": "ListExpensesByDateRangeAndCategory",
                "arguments": {
                    "start_date": "2024-07-01",
                    "end_date": "2024-09-30",
                    "categories": [
                        "OFFICE_SUPPLIES"
                    ]
                },
            },
            {
                "name": "ApplyDeductibilityRules",
                "arguments": {
                    "expense_id": "EXP012"
                },
            },
            {
                "name": "PostJournalEntry",
                "arguments": {
                    "date": "2024-09-30",
                    "account": "Governance Memo",
                    "amount": 0.0,
                    "memo": "OFFICE_SUPPLIES Q3 checked (EXP012)"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-09-30",
                    "artifact_name": "Q3_OfficeSupplies_Check_2024-09-30"
                }
            }
        ],
        "outputs": [
                "/reports/kpi/Q3_OfficeSupplies_Check_2024-09-30.pdf"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "58",
        "instruction": "As a financial consulting professional, carry out a PUB002 late-stage check dated '2024-11-30' for INV012 and INV023. Issue 'second_notice' for any delinquency over 60 days and document a KPI as_of '2024-11-30' with the artifact name 'PUB002_LateStage_2024-11-30'. Present two arrays: acted (list of notices sent) and escalated (none).",
        "actions": [
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV012",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV023",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV012",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV023",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "artifact_name": "PUB002_LateStage_2024-11-30"
                }
            }
        ],
        "outputs": [
                [
                    "INV012",
                    "INV023"
                ],
                []
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "59",
        "instruction": "As a financial consulting worker, handle PUB001 aging controls dated '2024-11-30'. Organize INV004, INV009, INV021 with today's date '2024-11-30'; issue 'second_notice' for invoices exceeding 60 days and archive a KPI for '2024-11-30' (artifact_name 'PUB001_Aging_Controls_2024-11-30'). Ensure both acted and escalated cases are returned.",
        "actions": [
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV004",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV009",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV021",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV009",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV021",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "artifact_name": "PUB001_Aging_Controls_2024-11-30"
                }
            }
        ],
        "outputs": [
                [
                    "INV009",
                    "INV021"
                ],
                []
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "60",
        "instruction": "Tasked as a financial consulting worker, manage a PUB001 aging pass effective '2024-11-30'. Categorize INV004, INV009, INV021 using today's date '2024-11-30'; dispatch 'second_notice' for cases over 60 days and record a KPI for '2024-11-30' (artifact_name 'PUB001_Aging_Pass_2024-11-30'). Provide lists of acted and escalated items as a result.",
        "actions": [
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV004"
                },
            },
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV009"
                },
            },
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV021"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV004",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV009",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV021",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV009",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV021",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "artifact_name": "PUB001_Aging_Pass_2024-11-30"
                }
            }
        ],
        "outputs": [
                [
                    "INV009",
                    "INV021"
                ],
                [
                    "INV009",
                    "INV021"
                ]
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "61",
        "instruction": "As a financial consulting worker, your task is to prepare a cashflow outlook as of '2024-11-30'. Utilize balances, 3-month schedules, anticipated inflows from INV008/INV009/INV010 with the probability_rule 'overdue_60=0.3', and consider outflows including taxes. Construct a 3-month monthly view, save a KPI as_of '2024-11-30' (artifact_name 'Cashflow_Outlook_2024-11-30'), and document a zero-value memo to 'Liquidity Review Memo'. Provide the KPI path.",
        "actions": [
            {
                "name": "GetBankBalances",
                "arguments": {
                {}
                },
            },
            {
                "name": "ListRecurringSchedules",
                "arguments": {
                    "horizon_months": 3
                },
            },
            {
                "name": "ForecastInflows",
                "arguments": {
                    "invoices": [
                        "INV008",
                        "INV009",
                        "INV010"
                    ],
                    "probability_rule": "overdue_60=0.3"
                },
            },
            {
                "name": "ForecastOutflows",
                "arguments": {
                    "recurring_schedules": true,
                    "taxes": true,
                    "horizon_months": 3
                },
            },
            {
                "name": "BuildCashflowView",
                "arguments": {
                    "horizon_months": 3,
                    "granularity": "monthly"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "artifact_name": "Cashflow_Outlook_2024-11-30"
                },
            },
            {
                "name": "PostJournalEntry",
                "arguments": {
                    "date": "2024-11-30",
                    "account": "Liquidity Review Memo",
                    "amount": 0.0
                }
            }
        ],
        "outputs": [
                "/reports/kpi/Cashflow_Outlook_2024-11-30.pdf"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "62",
        "instruction": "As a financial consulting worker, your responsibility is to prepare a PUB005 wrap-up by '2024-11-30'. Review INV011, INV022, INV026 with the date '2024-11-30'; dispatch 'second_notice' for any items over 60 days overdue; store a KPI as_of '2024-11-30' (artifact_name 'PUB005_Wrap_2024-11-30'). Provide the lists of actions taken and escalated items.",
        "actions": [
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV011",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV022",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV026",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV022",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV026",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "artifact_name": "PUB005_Wrap_2024-11-30"
                }
            }
        ],
        "outputs": [
                [
                    "INV022",
                    "INV026"
                ],
                [
                    "INV022",
                    "INV026"
                ]
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "63",
        "instruction": "As a financial consulting professional, compile a Q3-2024 office & travel integrity note. For '2024-07-01' to '2024-09-30', include items categorized under OFFICE_SUPPLIES and TRAVEL_EXPENSE (EXP012, EXP022, EXP023), create the '2024-Q3' dashboard, and save a KPI snapshot as_of '2024-09-30' with the artifact name 'Q3_Mixed_Integrity_2024-09-30'. Provide the path to the dashboard.",
        "actions": [
            {
                "name": "ListExpensesByDateRangeAndCategory",
                "arguments": {
                    "start_date": "2024-07-01",
                    "end_date": "2024-09-30",
                    "categories": [
                        "OFFICE_SUPPLIES",
                        "TRAVEL_EXPENSE"
                    ]
                },
            },
            {
                "name": "GenerateExpenseDashboard",
                "arguments": {
                    "quarter": "2024-Q3",
                    "included_expenses": [
                        "EXP012",
                        "EXP022",
                        "EXP023"
                    ],
                    "as_of": "2024-09-30",
                    "artifact_name": "Q3_Mixed_Integrity_2024-09-30"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-09-30",
                    "artifact_name": "Q3_Mixed_Integrity_2024-09-30"
                }
            }
        ],
        "outputs": [
                "/dashboards/ExpenseDashboards/2024-Q3/expense_dashboard_2024-Q3.pdf"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "64",
        "instruction": "Your task is to verify PUB001 follow-ups as of '2024-11-30'. Sort INV009 and INV021; any item older than 60 days should be marked with a 'second_notice' labeled 'Overdue >60 days'. Preserve the KPI 'PUB001_Followups_2024-11-30' as_of '2024-11-30' including sections ['Collections']. Present lists of items acted on and those escalated (>60 days).",
        "actions": [
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV009",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV021",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV009",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV021",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "artifact_name": "PUB001_Followups_2024-11-30",
                    "sections": [
                        "Collections"
                    ]
                }
            }
        ],
        "outputs": [
                [
                    "INV009",
                    "INV021"
                ],
                [
                    "INV009",
                    "INV021"
                ]
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "17",
        "instruction": "Handle issuing a November 2024 invoice for 'Midwest Education House' (PUB005) on project PROJ010 using time entry TIME017. The invoice must utilize invoice_id 'INV-AUTO-2024-604', invoice_number 'INV-2024-604', invoice_date '2024-11-30', and apply HST 0.13. Archive the PDF and document audit 'generated' with notes 'Invoice generated'. Return the invoice_number.",
        "actions": [
            {
                "name": "ResolveHourlyRate",
                "arguments": {
                    "project_id": "PROJ010"
                },
            },
            {
                "name": "ListTimeEntries",
                "arguments": {
                    "project_id": "PROJ010",
                    "month": "2024-11"
                },
            },
            {
                "name": "BuildInvoiceLines",
                "arguments": {
                    "time_entries": [
                        "TIME017"
                    ],
                    "hourly_rate": 85.0
                },
            },
            {
                "name": "CalculateTotals",
                "arguments": {
                    "invoice_lines": [
                        {
                            "line_amount": 382.5
                        }
                    ],
                    "hst_rate": 0.13
                },
            },
            {
                "name": "ComposeInvoicePdf",
                "arguments": {
                    "invoice_id": "INV-AUTO-2024-604",
                    "publisher_id": "PUB005"
                },
            },
            {
                "name": "InsertInvoice",
                "arguments": {
                    "invoice_id": "INV-AUTO-2024-604",
                    "publisher_id": "PUB005",
                    "subtotal": 382.5,
                    "hst_amount": 49.73,
                    "total_due": 432.23,
                    "invoice_number": "INV-2024-604",
                    "invoice_date": "2024-11-30",
                    "pdf_path": "/invoices/auto/INV-AUTO-2024-604.pdf"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV-AUTO-2024-604",
                    "event_type": "generated",
                    "notes": "Invoice generated"
                }
            }
        ],
        "outputs": [
                "INV-2024-604"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "66",
        "instruction": "Coordinate verification as a financial consulting worker for Q2-2024 MEALS_ENTERTAIN controls. Scan '2024-04-01'..'2024-06-30' and ensure no threshold breach at 150.0; record a zero-value memo to 'Governance Memo' with memo 'Q2 meals scan \u2013 no exceptions'; archive a KPI as_of '2024-06-30' (artifact_name 'Q2_Meals_Scan_2024-06-30'). Return the KPI path.",
        "actions": [
            {
                "name": "ListExpensesByDateRangeAndCategory",
                "arguments": {
                    "start_date": "2024-04-01",
                    "end_date": "2024-06-30",
                    "categories": [
                        "MEALS_ENTERTAIN"
                    ]
                },
            },
            {
                "name": "FlagHighValueMeals",
                "arguments": {
                    "expenses_ref": {
                        "expenses": [
                            {
                                "expense_id": "EXP019",
                                "category_code": "MEALS_ENTERTAIN",
                                "gross_amount": 18.75
                            }
                        ]
                    },
                    "threshold": 150.0
                },
            },
            {
                "name": "PostJournalEntry",
                "arguments": {
                    "date": "2024-06-30",
                    "account": "Governance Memo",
                    "amount": 0.0,
                    "memo": "Q2 meals scan – no exceptions"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-06-30",
                    "artifact_name": "Q2_Meals_Scan_2024-06-30"
                }
            }
        ],
        "outputs": [
                "/reports/kpi/Q2_Meals_Scan_2024-06-30.pdf"
        ]
    }
    ,
    {
        "annotator": 1,
        "user_id": "67",
        "instruction": "As a financial consulting professional, you are supporting PUB003 and PUB002 together. By '2024-11-30', identify and document necessary A/R procedures across INV008, INV022, INV012, and INV023, then compose a memo KPI as_of '2024-11-30' (artifact_name 'Cross_Action_Memo_2024-11-30'). Provide the KPI path.",
        "actions": [
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV008",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV022",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV012",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV023",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV008",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV022",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV012",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV023",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "artifact_name": "Cross_Action_Memo_2024-11-30"
                }
            }
        ],
        "outputs": [
                "/reports/kpi/Cross_Action_Memo_2024-11-30.pdf"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "68",
        "instruction": "In your role as a financial consulting expert, you will implement PUB001 collections as of '2024-11-30'. Focus exclusively on open items; calculate the aging for INV009 and INV021 using today's date '2024-11-30'. Document 'second_notice' for any items over 60 days, and save a KPI as_of '2024-11-30' (artifact_name 'PUB001_Aging_2024-11-30'). Deliver the result for items acted on (>60 days) and also mark them as escalated (>60 days).",
        "actions": [
            {
                "name": "ListPublisherOpenInvoices",
                "arguments": {
                    "publisher_id": "PUB001"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV009",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV021",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV009",
                    "event_type": "second_notice"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV021",
                    "event_type": "second_notice"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "artifact_name": "PUB001_Aging_2024-11-30"
                }
            }
        ],
        "outputs": [
                [
                    "INV009",
                    "INV021"
                ],
                [
                    "INV009",
                    "INV021"
                ]
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "69",
        "instruction": "As a financial consulting worker, handle a PUB002 A/R health sweep effective from '2024-11-30'. Determine the aging for INV012 and INV023 as of today '2024-11-30'; for any that are >60 days overdue, log 'second_notice'. Preserve a KPI as_of '2024-11-30' (artifact_name 'PUB002_AR_Health_2024-11-30'). Provide feedback on actions taken (>60 days) and likewise categorize as escalated (>60 days).",
        "actions": [
            {
                "name": "ListPublisherOpenInvoices",
                "arguments": {
                    "publisher_id": "PUB002"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV012",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV023",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV012",
                    "event_type": "second_notice"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV023",
                    "event_type": "second_notice"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "artifact_name": "PUB002_AR_Health_2024-11-30"
                }
            }
        ],
        "outputs": [
                [
                    "INV012",
                    "INV023"
                ],
                [
                    "INV012",
                    "INV023"
                ]
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "70",
        "instruction": "Assume the role of a financial consulting worker and manage PUB003 follow-ups effective from '2024-11-30'. Analyze INV008 and INV022 as of today '2024-11-30'; dispatch a 'second_notice' for any over >60 days and document a KPI as_of '2024-11-30' (artifact_name 'PUB003_AR_Followups_2024-11-30'). Report on actions taken (>60 days) and similarly classify as escalated (>60 days).",
        "actions": [
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV008",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV022",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV008",
                    "event_type": "second_notice"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV022",
                    "event_type": "second_notice"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "artifact_name": "PUB003_AR_Followups_2024-11-30"
                }
            }
        ],
        "outputs": [
                [
                    "INV008",
                    "INV022"
                ],
                [
                    "INV008",
                    "INV022"
                ]
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "71",
        "instruction": "You are a financial consulting worker handling a PUB001 A/R spot sweep dated '2024-11-30'. Investigate INV004, INV009, INV021 using today '2024-11-30'; issue 'second_notice' for any that are >60 days overdue and compile a KPI as_of '2024-11-30' (artifact_name 'PUB001_SpotSweep_2024-11-30'). Provide acted upon (>60 days) and escalated (>60 days) invoice lists.",
        "actions": [
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV004"
                },
            },
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV009"
                },
            },
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV021"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV004",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV009",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV021",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV009",
                    "event_type": "second_notice"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV021",
                    "event_type": "second_notice"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "artifact_name": "PUB001_SpotSweep_2024-11-30"
                }
            }
        ],
        "outputs": [
                [
                    "INV009",
                    "INV021"
                ],
                [
                    "INV009",
                    "INV021"
                ]
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "72",
        "instruction": "You are a financial consulting worker coordinating a PUB001 enforcement note as of '2024-11-30'. Analyze INV004, INV009, INV021 with today '2024-11-30'; dispatch 'second_notice' for any over >60 days old; prepare a KPI as_of '2024-11-30' (artifact_name 'PUB001_Enforcement_2024-11-30'). Return two lists where each represents invoices over >60 days (second notices sent).",
        "actions": [
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV004",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV009",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV021",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV009",
                    "event_type": "second_notice"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV021",
                    "event_type": "second_notice"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "artifact_name": "PUB001_Enforcement_2024-11-30"
                }
            }
        ],
        "outputs": [
                [
                    "INV009",
                    "INV021"
                ],
                [
                    "INV009",
                    "INV021"
                ]
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "73",
        "instruction": "As a financial consulting worker, your task is to generate a PUB005 A/R summary dated '2024-11-30'. Assess INV011, INV022, INV026 using the date '2024-11-30'; dispatch 'second_notice' only if they are outstanding for more than 60 days; record a KPI as_of '2024-11-30' (artifact_name 'PUB005_AR_Summary_2024-11-30'). Return those addressed (>60 days) and treat the same set as escalated (>60 days).",
        "actions": [
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV011",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV022",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV026",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV022",
                    "event_type": "second_notice"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV026",
                    "event_type": "second_notice"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "artifact_name": "PUB005_AR_Summary_2024-11-30"
                }
            }
        ],
        "outputs": [
                [
                    "INV022",
                    "INV026"
                ],
                [
                    "INV022",
                    "INV026"
                ]
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "74",
        "instruction": "As a financial consulting worker, finalize the closure of PUB003 A/R as of '2024-11-30'. Review INV008 and INV022 on the date '2024-11-30', note 'second_notice' for any items exceeding 60 days, and document a KPI as_of '2024-11-30' (artifact_name 'PUB003_AR_Close_2024-11-30'). Provide the acted upon (>60 days) and consider the same set for escalation (>60 days).",
        "actions": [
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV008"
                },
            },
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV022"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV008",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV022",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV008",
                    "event_type": "second_notice"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV022",
                    "event_type": "second_notice"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "artifact_name": "PUB003_AR_Close_2024-11-30"
                }
            }
        ],
        "outputs": [
                [
                    "INV008",
                    "INV022"
                ],
                [
                    "INV008",
                    "INV022"
                ]
        ]
    }
    ,
    {
        "annotator": new,
        "user_id": "75",
        "instruction": "As a financial consulting worker, handle the preparation of a PUB001 targeted follow-up note. Utilizing the date '2024-11-30', apply the A/R policy for INV009 and INV021 using today's date '2024-11-30'; ensure to log 'second_notice' only for items exceeding 60 days, with notes specified as 'Overdue >60 days'. Archive a KPI as_of '2024-11-30' featuring sections ['Collections'] and the artifact_name 'PUB001_Targeted_2024-11-30'. Provide the link to the KPI path.",
        "actions": [
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV009",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV021",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV009",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV021",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "sections": [
                        "Collections"
                    ],
                    "artifact_name": "PUB001_Targeted_2024-11-30"
                }
            }
        ],
        "outputs": [
                "/reports/kpi/PUB001_Targeted_2024-11-30.pdf"
        ]
    }
    ,
    {
        "annotator": new,
        "user_id": "76",
        "instruction": "Coordinate the preparation of a PUB002 late-stage wrap for Aurora Academic Press as a financial consulting worker. On '2024-11-30', enforce follow-ups concerning INV012 and INV023 utilizing today's '2024-11-30' date; for items greater than 60 days, record 'second_notice' accompanied by the notes 'Overdue >60 days'. Archive a KPI as_of '2024-11-30' with the ['Aging'] sections and designate the artifact_name as 'PUB002_LateStage_2024-11-30'. Present the KPI path.",
        "actions": [
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV012",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV023",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV012",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV023",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "sections": [
                        "Aging"
                    ],
                    "artifact_name": "PUB002_LateStage_2024-11-30"
                }
            }
        ],
        "outputs": [
                "/reports/kpi/PUB002_LateStage_2024-11-30.pdf"
        ]
    }
    ,
    {
        "annotator": new,
        "user_id": "77",
        "instruction": "As a financial consulting worker, you're tasked with preparing the November 2024 tax-reserve true-up for the practice. Confirm that, as of '2024-11-30', the 2024 reserve derived from 10909.5 matches 'SNAP004' within a 0.01 threshold and record any discrepancies in 'Tax Reserve' with the memo 'YTD tax reserve true-up'. Archive a KPI dated '2024-11-30' including sections ['TaxReserve'] and use the artifact name 'TaxReserve_NovTrueUp_2024-11'. Return 157.87.",
        "actions": [
            {
                "name": "ComputeYtdFromMonthlyRevenue",
                "arguments": {
                    "year": 2024,
                    "through_month": 11
                },
            },
            {
                "name": "ComputeTaxReserve",
                "arguments": {
                    "ytd_revenue": 10909.5,
                    "tax_year": 2024
                },
            },
            {
                "name": "GetDashboardSnapshot",
                "arguments": {
                    "snapshot_id": "SNAP004"
                },
            },
            {
                "name": "ReconcileTaxReserve",
                "arguments": {
                    "computed_tax_reserve_ref": {
                        "tax_reserve": 2891.02
                    },
                    "snapshot_ref": {
                        "ytd_tax_reserve": 2733.15
                    },
                    "threshold": 0.01
                },
            },
            {
                "name": "PostJournalEntry",
                "arguments": {
                    "date": "2024-11-30",
                    "account": "Tax Reserve",
                    "amount_ref": {
                        "adjustment": 157.87
                    },
                    "memo": "YTD tax reserve true-up"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "sections": [
                        "TaxReserve"
                    ],
                    "artifact_name": "TaxReserve_NovTrueUp_2024-11"
                }
            }
        ],
        "outputs": [
                "157.87"
        ]
    }
    ,
    {
        "annotator": new,
        "user_id": "78",
        "instruction": "Your role as a financial consulting worker involves performing a PUB001 cross-check. Validate, as of '2024-11-30', the A/R notices related to INV009, INV021, and INV026 with the date '2024-11-30'; generate 'second_notice' exclusively for items overdue by more than 60 days, with the notation 'Overdue >60 days'. Archive a KPI for '2024-11-30' featuring sections ['Aging'] and use the artifact name 'PUB001_CrossCheck_2024-11-30'. Return the KPI path.",
        "actions": [
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV009",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV021",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV026",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV009",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV021",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV026",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "sections": [
                        "Aging"
                    ],
                    "artifact_name": "PUB001_CrossCheck_2024-11-30"
                }
            }
        ],
        "outputs": [
                "/reports/kpi/PUB001_CrossCheck_2024-11-30.pdf"
        ]
    }
    ,
    {
        "annotator": new,
        "user_id": "79",
        "instruction": "As a financial consulting worker, you are tasked with providing a Q3 2024 mixed expense snapshot for the practice. Between '2024-07-01' and '2024-09-30', handle the normalization of deductibility on EXP012 (OFFICE_SUPPLIES) and EXP022/EXP023 (TRAVEL_EXPENSE), compile the '2024-Q3' dashboard incorporating these elements, and store a KPI as_of '2024-09-30' featuring sections ['ExpenseMix','Deductibility'] and artifact_name 'Q3_Mixed_Snapshot_2024-09-30'. Provide the path to the dashboard.",
        "actions": [
            {
                "name": "ListExpensesByDateRangeAndCategory",
                "arguments": {
                    "start_date": "2024-07-01",
                    "end_date": "2024-09-30",
                    "categories": [
                        "OFFICE_SUPPLIES",
                        "TRAVEL_EXPENSE"
                    ]
                },
            },
            {
                "name": "ApplyDeductibilityRules",
                "arguments": {
                    "expense_id": "EXP012"
                },
            },
            {
                "name": "ApplyDeductibilityRules",
                "arguments": {
                    "expense_id": "EXP022"
                },
            },
            {
                "name": "ApplyDeductibilityRules",
                "arguments": {
                    "expense_id": "EXP023"
                },
            },
            {
                "name": "GenerateExpenseDashboard",
                "arguments": {
                    "quarter": "2024-Q3",
                    "included_expenses": [
                        "EXP012",
                        "EXP022",
                        "EXP023"
                    ]
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-09-30",
                    "sections": [
                        "ExpenseMix",
                        "Deductibility"
                    ],
                    "artifact_name": "Q3_Mixed_Snapshot_2024-09-30"
                }
            }
        ],
        "outputs": [
                "/dashboards/ExpenseDashboards/2024-Q3/expense_dashboard_2024-Q3.pdf"
        ]
    }
    ,
    {
        "annotator": new,
        "user_id": "80",
        "instruction": "As a financial consulting worker, you need to create a PUB005 November collections note. By '2024-11-30', manage policy actions for INV022 and INV026 using today's date '2024-11-30'; document 'second_notice' for items overdue more than 60 days with remarks 'Overdue >60 days'. Archive a KPI as_of '2024-11-30' involving sections ['Collections'] and artifact_name 'PUB005_Collections_2024-11-30'. Supply the KPI path.",
        "actions": [
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV022",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV026",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV022",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV026",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "sections": [
                        "Collections"
                    ],
                    "artifact_name": "PUB005_Collections_2024-11-30"
                }
            }
        ],
        "outputs": [
                "/reports/kpi/PUB005_Collections_2024-11-30.pdf"
        ]
    }
    ,
    {
        "annotator": new,
        "user_id": "81",
        "instruction": "As a financial consulting worker, you are documenting a PUB002\u2013PUB003 joint action log. By '2024-11-30', record A/R actions for INV012, INV023, and INV008 on '2024-11-30'; note 'second_notice' exclusively for items overdue more than 60 days with comments 'Overdue >60 days'. Store a KPI as_of '2024-11-30' encompassing sections ['Aging'] and with the artifact_name 'Joint_Action_Log_2024-11-30'. Provide the KPI path.",
        "actions": [
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV012",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV023",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV008",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV012",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV023",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV008",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "sections": [
                        "Aging"
                    ],
                    "artifact_name": "Joint_Action_Log_2024-11-30"
                }
            }
        ],
        "outputs": [
                "/reports/kpi/Joint_Action_Log_2024-11-30.pdf"
        ]
    }
    ,
    {
        "annotator": new,
        "user_id": "82",
        "instruction": "In your role as a financial consulting worker, you need to write a PUB003 escalation note. As of '2024-11-30', enforce policy for INV008 and INV022 with the date '2024-11-30'; document 'second_notice' solely for items older than 60 days with remarks 'Overdue >60 days'. Save a KPI as_of '2024-11-30' including sections ['Aging'] with the artifact_name 'PUB003_Escalation_2024-11-30'. Deliver the KPI path.",
        "actions": [
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV008",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV022",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV008",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV022",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "sections": [
                        "Aging"
                    ],
                    "artifact_name": "PUB003_Escalation_2024-11-30"
                }
            }
        ],
        "outputs": [
                "/reports/kpi/PUB003_Escalation_2024-11-30.pdf"
        ]
    }
    ,
    {
        "annotator": new,
        "user_id": "83",
        "instruction": "As a financial consulting worker, handle a PUB003\u2013PUB005 cross-publisher actions brief. As of '2024-11-30', record A/R actions for INV008, INV022, and INV026 using today '2024-11-30'; log 'second_notice' exclusively for items >60 days with notes 'Overdue >60 days'. Archive a KPI as_of '2024-11-30' within sections ['Collections'] and artifact_name 'PUB3_5_Cross_Brief_2024-11-30'. Provide the KPI path.",
        "actions": [
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV008",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV022",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV026",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV008",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV022",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV026",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "sections": [
                        "Collections"
                    ],
                    "artifact_name": "PUB3_5_Cross_Brief_2024-11-30"
                }
            }
        ],
        "outputs": [
                "/reports/kpi/PUB3_5_Cross_Brief_2024-11-30.pdf"
        ]
    }
    ,
    {
        "annotator": new,
        "user_id": "84",
        "instruction": "As a financial consulting worker, coordinate a PUB003 A/R closure. As of '2024-11-30', enforce policy for INV008 and INV022 using today '2024-11-30'; log 'second_notice' only for items overdue >60 days with notes 'Overdue >60 days'. Archive a KPI as_of '2024-11-30' within sections ['Aging'] and artifact_name 'PUB003_AR_Close_2024-11-30'. Provide the KPI path.",
        "actions": [
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV008"
                },
            },
            {
                "name": "GetInvoiceDetails",
                "arguments": {
                    "invoice_id": "INV022"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV008",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV022",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV008",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV022",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "sections": [
                        "Aging"
                    ],
                    "artifact_name": "PUB003_AR_Close_2024-11-30"
                }
            }
        ],
        "outputs": [
                "/reports/kpi/PUB003_AR_Close_2024-11-30.pdf"
        ]
    }
    ,
    {
        "annotator": new,
        "user_id": "85",
        "instruction": "Handle the role of a financial consultant compiling a consolidated actions register. As of '2024-11-30', implement policy for INV009, INV021, and INV026 using today's date '2024-11-30'; note 'second_notice' only for items overdue by more than 60 days with the comment 'Overdue >60 days'. Store a KPI dated '2024-11-30' under sections ['Collections'] with the artifact name 'Consolidated_Actions_2024-11-30'. Provide the KPI path.",
        "actions": [
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV009",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV021",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV026",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV009",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV021",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV026",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "sections": [
                        "Collections"
                    ],
                    "artifact_name": "Consolidated_Actions_2024-11-30"
                }
            }
        ],
        "outputs": [
                "/reports/kpi/Consolidated_Actions_2024-11-30.pdf"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "86",
        "instruction": "Coordinate the preparation of Q3 2024 expense governance as a financial consultant. Utilize dates between '2024-07-01' and '2024-09-30' for OFFICE_SUPPLIES and TRAVEL_EXPENSE, ensure deductibility is applied to EXP012, EXP022, EXP023, create a dashboard, and save a KPI with the artifact name 'Q3_Expense_Governance_2024-09-30'. Provide the dashboard path.",
        "actions": [
            {
                "name": "ListExpensesByDateRangeAndCategory",
                "arguments": {
                    "start_date": "2024-07-01",
                    "end_date": "2024-09-30",
                    "categories": [
                        "OFFICE_SUPPLIES",
                        "TRAVEL_EXPENSE"
                    ]
                },
            },
            {
                "name": "ApplyDeductibilityRules",
                "arguments": {
                    "expense_id": "EXP012"
                },
            },
            {
                "name": "ApplyDeductibilityRules",
                "arguments": {
                    "expense_id": "EXP022"
                },
            },
            {
                "name": "ApplyDeductibilityRules",
                "arguments": {
                    "expense_id": "EXP023"
                },
            },
            {
                "name": "GenerateExpenseDashboard",
                "arguments": {
                    "quarter": "2024-Q3",
                    "included_expenses": [
                        "EXP012",
                        "EXP022",
                        "EXP023"
                    ],
                    "as_of": "2024-09-30",
                    "artifact_name": "Q3_Expense_Governance_2024-09-30"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-09-30",
                    "artifact_name": "Q3_Expense_Governance_2024-09-30"
                }
            }
        ],
        "outputs": [
                "/dashboards/ExpenseDashboards/2024-Q3/expense_dashboard_2024-Q3.pdf"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "87",
        "instruction": "Handle the reconciliation of the practice's November month-end 2024 tax reserve on '2024-11-30'. Calculate the year-to-date revenue for 2024 up to month 11, determine the 2024 corporate tax reserve using the tax rate table, compare it against snapshot 'SNAP004', and calculate an adjustment with a threshold of 0.01. Record the adjustment in account 'Tax Reserve' with a memo 'YTD tax reserve true-up', and archive a KPI artifact as_of '2024-11-30' titled 'TaxReserve_Nov_Recon_2024-11'. Additionally, save a dashboard snapshot using the calculated YTD revenue and tax reserve along with the KPI PDF path. Return the adjustment amount.",
        "actions": [
            {
                "name": "ComputeYtdFromMonthlyRevenue",
                "arguments": {
                    "year": 2024,
                    "through_month": 11
                },
            },
            {
                "name": "ComputeTaxReserve",
                "arguments": {
                    "ytd_revenue": 10909.5,
                    "tax_year": 2024
                },
            },
            {
                "name": "GetDashboardSnapshot",
                "arguments": {
                    "snapshot_id": "SNAP004"
                },
            },
            {
                "name": "ReconcileTaxReserve",
                "arguments": {
                    "computed_tax_reserve_ref": {
                        "tax_reserve": 2891.02
                    },
                    "snapshot_ref": {
                        "ytd_tax_reserve": 2733.15
                    },
                    "threshold": 0.01
                },
            },
            {
                "name": "PostJournalEntry",
                "arguments": {
                    "date": "2024-11-30",
                    "account": "Tax Reserve",
                    "amount_ref": {
                        "adjustment": 157.87
                    },
                    "memo": "YTD tax reserve true-up"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "sections": [
                        "TaxReserve"
                    ],
                    "artifact_name": "TaxReserve_Nov_Recon_2024-11"
                },
            },
            {
                "name": "CreateDashboardSnapshot",
                "arguments": {
                    "snapshot_date": "2024-11-30",
                    "ytd_revenue": 10909.5,
                    "ytd_tax_reserve": 2891.02,
                    "pdf_path": "/reports/kpi/TaxReserve_Nov_Recon_2024-11.pdf"
                }
            }
        ],
        "outputs": [
                "157.87"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "88",
        "instruction": "Coordinate the compilation of a cross-publisher collections bundle as of '2024-11-30' for PUB001 and PUB003. Enumerate open invoices for PUB001 and PUB003, gather payment behavior data for both (PUB001, PUB003), predict expected inflows on ['INV009','INV021','INV008','INV022'] using probability_rule 'overdue_60=0.3', and store a KPI artifact as_of '2024-11-30' with sections ['Collections','Behavior'] titled 'Cross_PUB001_PUB003_2024-11-30'. Return the KPI path.",
        "actions": [
            {
                "name": "ListPublisherOpenInvoices",
                "arguments": {
                    "publisher_id": "PUB001"
                },
            },
            {
                "name": "ListPublisherOpenInvoices",
                "arguments": {
                    "publisher_id": "PUB003"
                },
            },
            {
                "name": "ComputePaymentBehavior",
                "arguments": {
                    "publisher_id": "PUB001"
                },
            },
            {
                "name": "ComputePaymentBehavior",
                "arguments": {
                    "publisher_id": "PUB003"
                },
            },
            {
                "name": "ForecastInflows",
                "arguments": {
                    "invoices": [
                        "INV009",
                        "INV021",
                        "INV008",
                        "INV022"
                    ],
                    "probability_rule": "overdue_60=0.3"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "sections": [
                        "Collections",
                        "Behavior"
                    ],
                    "artifact_name": "Cross_PUB001_PUB003_2024-11-30"
                }
            }
        ],
        "outputs": [
                "/reports/kpi/Cross_PUB001_PUB003_2024-11-30.pdf"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "89",
        "instruction": "Handle the closure of November 2024 tax posture effective '2024-11-30'. Validate 2024 YTD revenue up to month 11, calculate the 2024 corporate tax reserve, and reconcile with snapshot 'SNAP004' allowing a 0.01 margin. Record the calculated difference to the account 'Tax Reserve' using the memo 'YTD tax reserve true-up'. Archive a KPI artifact titled 'TaxReserve_Close_2024-11' and save a dashboard snapshot linked to the KPI path, including the computed YTD and reserve figures. Deliver 157.87 as the result.",
        "actions": [
            {
                "name": "ComputeYtdFromMonthlyRevenue",
                "arguments": {
                    "year": 2024,
                    "through_month": 11
                },
            },
            {
                "name": "ComputeTaxReserve",
                "arguments": {
                    "ytd_revenue": 10909.5,
                    "tax_year": 2024
                },
            },
            {
                "name": "GetDashboardSnapshot",
                "arguments": {
                    "snapshot_id": "SNAP004"
                },
            },
            {
                "name": "ReconcileTaxReserve",
                "arguments": {
                    "computed_tax_reserve_ref": {
                        "tax_reserve": 2891.02
                    },
                    "snapshot_ref": {
                        "ytd_tax_reserve": 2733.15
                    },
                    "threshold": 0.01
                },
            },
            {
                "name": "PostJournalEntry",
                "arguments": {
                    "date": "2024-11-30",
                    "account": "Tax Reserve",
                    "amount_ref": {
                        "adjustment": 157.87
                    },
                    "memo": "YTD tax reserve true-up"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "sections": [
                        "TaxReserve"
                    ],
                    "artifact_name": "TaxReserve_Close_2024-11"
                },
            },
            {
                "name": "CreateDashboardSnapshot",
                "arguments": {
                    "snapshot_date": "2024-11-30",
                    "ytd_revenue": 10909.5,
                    "ytd_tax_reserve": 2891.02,
                    "pdf_path": "/reports/kpi/TaxReserve_Close_2024-11.pdf"
                }
            }
        ],
        "outputs": [
                "157.87"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "90",
        "instruction": "Coordinate the creation of a four-month cashflow overview as of '2024-11-30'. Utilize current bank balances, incorporate active recurring schedules over 4 months with taxes accounted for, and project expected inflows from ['INV008','INV009','INV010'] using the probability_rule 'overdue_60=0.3'. Develop a monthly forecast for the four-month period. Archive a KPI labeled 'Cashflow_4M_Outlook_2024-11-30' with the date '2024-11-30' and issue a zero-value memo to the account 'Liquidity Review Memo' containing the text '4-month cashflow outlook archived'. Provide the KPI path.",
        "actions": [
            {
                "name": "GetBankBalances",
                "arguments": {
                {}
                },
            },
            {
                "name": "ListRecurringSchedules",
                "arguments": {
                    "horizon_months": 4
                },
            },
            {
                "name": "ForecastInflows",
                "arguments": {
                    "invoices": [
                        "INV008",
                        "INV009",
                        "INV010"
                    ],
                    "probability_rule": "overdue_60=0.3"
                },
            },
            {
                "name": "ForecastOutflows",
                "arguments": {
                    "recurring_schedules": true,
                    "taxes": true,
                    "horizon_months": 4
                },
            },
            {
                "name": "BuildCashflowView",
                "arguments": {
                    "horizon_months": 4,
                    "granularity": "monthly"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "sections": [
                        "Cashflow"
                    ],
                    "artifact_name": "Cashflow_4M_Outlook_2024-11-30"
                },
            },
            {
                "name": "PostJournalEntry",
                "arguments": {
                    "date": "2024-11-30",
                    "account": "Liquidity Review Memo",
                    "amount_ref": {
                        "adjustment": 0.0
                    },
                    "memo": "4-month cashflow outlook archived"
                }
            }
        ],
        "outputs": [
                "/reports/kpi/Cashflow_4M_Outlook_2024-11-30.pdf"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "91",
        "instruction": "Coordinate a November 2024 reserve verification as of '2024-11-30'. Verify 2024 YTD revenue through month 11, calculate the 2024 reserve, align to 'SNAP004' with a threshold of 0.01, record any discrepancies to 'Tax Reserve' with the memo 'YTD tax reserve true-up', and store a KPI named 'TaxReserve_Verification_2024-11' dated '2024-11-30'. Return 157.87.",
        "actions": [
            {
                "name": "ComputeYtdFromMonthlyRevenue",
                "arguments": {
                    "year": 2024,
                    "through_month": 11
                },
            },
            {
                "name": "ComputeTaxReserve",
                "arguments": {
                    "ytd_revenue": 10909.5,
                    "tax_year": 2024
                },
            },
            {
                "name": "GetDashboardSnapshot",
                "arguments": {
                    "snapshot_id": "SNAP004"
                },
            },
            {
                "name": "ReconcileTaxReserve",
                "arguments": {
                    "computed_tax_reserve_ref": {
                        "tax_reserve": 2891.02
                    },
                    "snapshot_ref": {
                        "ytd_tax_reserve": 2733.15
                    },
                    "threshold": 0.01
                },
            },
            {
                "name": "PostJournalEntry",
                "arguments": {
                    "date": "2024-11-30",
                    "account": "Tax Reserve",
                    "amount_ref": {
                        "adjustment": 157.87
                    },
                    "memo": "YTD tax reserve true-up"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "sections": [
                        "TaxReserve"
                    ],
                    "artifact_name": "TaxReserve_Verification_2024-11"
                }
            }
        ],
        "outputs": [
                "157.87"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "92",
        "instruction": "Prepare a cross-publisher collections brief as of '2024-11-30' concerning PUB002 and PUB005. Enumerate open invoices for these publishers, detail their payment patterns, estimate expected inflows on ['INV012','INV023','INV022','INV026'] using probability_rule 'overdue_60=0.3', and save a KPI artifact dated '2024-11-30' including sections ['Collections','Behavior'] titled 'PUB002_PUB005_Collections_2024-11-30'. Provide the KPI path.",
        "actions": [
            {
                "name": "ListPublisherOpenInvoices",
                "arguments": {
                    "publisher_id": "PUB002"
                },
            },
            {
                "name": "ListPublisherOpenInvoices",
                "arguments": {
                    "publisher_id": "PUB005"
                },
            },
            {
                "name": "ComputePaymentBehavior",
                "arguments": {
                    "publisher_id": "PUB002"
                },
            },
            {
                "name": "ComputePaymentBehavior",
                "arguments": {
                    "publisher_id": "PUB005"
                },
            },
            {
                "name": "ForecastInflows",
                "arguments": {
                    "invoices": [
                        "INV012",
                        "INV023",
                        "INV022",
                        "INV026"
                    ],
                    "probability_rule": "overdue_60=0.3"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "sections": [
                        "Collections",
                        "Behavior"
                    ],
                    "artifact_name": "PUB002_PUB005_Collections_2024-11-30"
                }
            }
        ],
        "outputs": [
                "/reports/kpi/PUB002_PUB005_Collections_2024-11-30.pdf"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "93",
        "instruction": "Handle a cashflow outlook for five months starting '2024-11-30'. Utilize current bank balances, ensure recurring schedules=True and taxes=True for the 5-month span, project anticipated inflows from invoices ['INV008','INV009','INV010'] employing the probability_rule 'overdue_60=0.3'. Develop a monthly perspective over 5 months, archive a KPI titled 'Cashflow_5M_Outlook_2024-11-30' as_of '2024-11-30', and post a memo with zero-value to account 'Liquidity Review Memo' containing the text '5-month cashflow outlook archived'. Provide the KPI path.",
        "actions": [
            {
                "name": "GetBankBalances",
                "arguments": {
                {}
                },
            },
            {
                "name": "ListRecurringSchedules",
                "arguments": {
                    "horizon_months": 5
                },
            },
            {
                "name": "ForecastInflows",
                "arguments": {
                    "invoices": [
                        "INV008",
                        "INV009",
                        "INV010"
                    ],
                    "probability_rule": "overdue_60=0.3"
                },
            },
            {
                "name": "ForecastOutflows",
                "arguments": {
                    "recurring_schedules": true,
                    "taxes": true,
                    "horizon_months": 5
                },
            },
            {
                "name": "BuildCashflowView",
                "arguments": {
                    "horizon_months": 5,
                    "granularity": "monthly"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "artifact_name": "Cashflow_5M_Outlook_2024-11-30",
                    "sections": [
                        "Cashflow"
                    ]
                },
            },
            {
                "name": "PostJournalEntry",
                "arguments": {
                    "date": "2024-11-30",
                    "account": "Liquidity Review Memo",
                    "amount_ref": {
                        "adjustment": 0.0
                    },
                    "memo": "5-month cashflow outlook archived"
                }
            }
        ],
        "outputs": [
                "/reports/kpi/Cashflow_5M_Outlook_2024-11-30.pdf"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "94",
        "instruction": "Coordinate the issue of a zero-total shell invoice for November 2024 to 'Summit Educational Publishing' (PUB003). Utilize invoice_id 'INV-AUTO-2024-302' and invoice_number 'INV-2024-302', with invoice_date '2024-11-30', period '2024-11-01'..'2024-11-30'. Apply HST at 0.13 (subtotal 0.00), archive the PDF, and record an audit event 'generated' including notes 'Invoice generated'. Additionally, archive a KPI as_of '2024-11-30' named 'PUB003_Shell_Issue_2024-11'. Provide 'INV-2024-302'.",
        "actions": [
            {
                "name": "CalculateTotals",
                "arguments": {
                    "invoice_lines": [],
                    "hst_rate": 0.13
                },
            },
            {
                "name": "ComposeInvoicePdf",
                "arguments": {
                    "invoice_id": "INV-AUTO-2024-302",
                    "publisher_id": "PUB003"
                },
            },
            {
                "name": "InsertInvoice",
                "arguments": {
                    "invoice_id": "INV-AUTO-2024-302",
                    "publisher_id": "PUB003",
                    "subtotal": 0.0,
                    "hst_amount": 0.0,
                    "total_due": 0.0,
                    "invoice_number": "INV-2024-302",
                    "invoice_date": "2024-11-30",
                    "period_start": "2024-11-01",
                    "period_end": "2024-11-30",
                    "pdf_path": "/invoices/auto/INV-AUTO-2024-302.pdf"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV-AUTO-2024-302",
                    "event_type": "generated",
                    "notes": "Invoice generated"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "artifact_name": "PUB003_Shell_Issue_2024-11",
                    "sections": []
                }
            }
        ],
        "outputs": [
                "INV-2024-302"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "95",
        "instruction": "Administer PUB002 A/R actions effective '2024-11-30'. Enumerate PUB002 outstanding items, determine the aging for INV012 and INV023 using the date '2024-11-30', annotate 'second_notice' with the note 'Overdue >60 days' when relevant, and preserve a KPI dated '2024-11-30' with the title 'PUB002_Actions_2024-11-30'. Produce two arrays: acted and escalated (>60 days).",
        "actions": [
            {
                "name": "ListPublisherOpenInvoices",
                "arguments": {
                    "publisher_id": "PUB002"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV012",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV023",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV012",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV023",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "artifact_name": "PUB002_Actions_2024-11-30",
                    "sections": []
                }
            }
        ],
        "outputs": [
                [
                    "INV012",
                    "INV023"
                ],
                [
                    "INV012",
                    "INV023"
                ]
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "96",
        "instruction": "Verify Q2-2024 MEALS_ENTERTAIN governance. Examine dates '2024-04-01'..'2024-06-30' with a threshold of 150.0, ensure there are no exceptions, record a zero-amount memo to account 'Governance Memo' with the description 'Q2 meals scan \u2013 no exceptions', and save a KPI as_of '2024-06-30' titled 'Q2_Meals_Scan_2024-06-30'. Provide the KPI path.",
        "actions": [
            {
                "name": "ListExpensesByDateRangeAndCategory",
                "arguments": {
                    "start_date": "2024-04-01",
                    "end_date": "2024-06-30",
                    "categories": [
                        "MEALS_ENTERTAIN"
                    ]
                },
            },
            {
                "name": "FlagHighValueMeals",
                "arguments": {
                    "expenses_ref": {
                        "expenses": [
                            {
                                "expense_id": "EXP019",
                                "category_code": "MEALS_ENTERTAIN",
                                "gross_amount": 18.75
                            }
                        ]
                    },
                    "threshold": 150.0
                },
            },
            {
                "name": "PostJournalEntry",
                "arguments": {
                    "date": "2024-06-30",
                    "account": "Governance Memo",
                    "amount_ref": {
                        "adjustment": 0.0
                    },
                    "memo": "Q2 meals scan – no exceptions"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-06-30",
                    "artifact_name": "Q2_Meals_Scan_2024-06-30",
                    "sections": []
                }
            }
        ],
        "outputs": [
                "/reports/kpi/Q2_Meals_Scan_2024-06-30.pdf"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "97",
        "instruction": "Handle A/R follow-ups for 'Northern Star Publishers' (PUB001) as of '2024-11-30'. Focus on open items INV009 and INV021; items exceeding 60 days should include a 'second_notice' with notes 'Overdue >60 days'. Archive a KPI as_of '2024-11-30' titled 'PUB001_Enforcement_2024-11-30' with sections ['Collections']. Return two arrays: acted and escalated (>60 days).",
        "actions": [
            {
                "name": "ListPublisherOpenInvoices",
                "arguments": {
                    "publisher_id": "PUB001"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV009",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV021",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV009",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV021",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "artifact_name": "PUB001_Enforcement_2024-11-30",
                    "sections": [
                        "Collections"
                    ]
                }
            }
        ],
        "outputs": [
                [
                    "INV009",
                    "INV021"
                ],
                [
                    "INV009",
                    "INV021"
                ]
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "98",
        "instruction": "Coordinate PUB002 collections memo creation as of '2024-11-30'. Concentrate on open items INV012 and INV023; items over 60 days must include a 'second_notice' annotated 'Overdue >60 days'. Archive KPI 'PUB002_Collections_Memo_2024-11-30' as_of '2024-11-30' with sections ['Collections']. Return two arrays: acted and escalated (>60 days).",
        "actions": [
            {
                "name": "ListPublisherOpenInvoices",
                "arguments": {
                    "publisher_id": "PUB002"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV012",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV023",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV012",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV023",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "artifact_name": "PUB002_Collections_Memo_2024-11-30",
                    "sections": [
                        "Collections"
                    ]
                }
            }
        ],
        "outputs": [
                [
                    "INV012",
                    "INV023"
                ],
                [
                    "INV012",
                    "INV023"
                ]
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "99",
        "instruction": "You are preparing a PUB003 enforcement update effective '2024-11-30'. Implement the policy to INV008 and INV022 using today '2024-11-30'; for items exceeding 60 days, attach 'second_notice' with notes 'Overdue >60 days'. Save KPI 'PUB003_Enforcement_Update_2024-11-30' as_of '2024-11-30' including sections ['Aging','Collections']. Provide lists of acted and escalated (>60 days) items.",
        "actions": [
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV008",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "ComputeInvoiceAging",
                "arguments": {
                    "invoice_id": "INV022",
                    "today": "2024-11-30"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV008",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "CreateAuditEntry",
                "arguments": {
                    "invoice_id": "INV022",
                    "event_type": "second_notice",
                    "notes": "Overdue >60 days"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "artifact_name": "PUB003_Enforcement_Update_2024-11-30",
                    "sections": [
                        "Aging",
                        "Collections"
                    ]
                }
            }
        ],
        "outputs": [
                [
                    "INV008",
                    "INV022"
                ],
                [
                    "INV008",
                    "INV022"
                ]
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "100",
        "instruction": "You are verifying the November 2024 tax reserve at month_end '2024-11-30'. Calculate 2024 YTD through month 11 and the 2024 reserve; align with 'SNAP004' maintaining a 0.01 threshold, record the difference to 'Tax Reserve' with memo 'YTD tax reserve true-up', and save KPI 'TaxReserve_Confirm_2024-11' as_of '2024-11-30' with sections ['TaxReserve']. Provide a return of 157.87.",
        "actions": [
            {
                "name": "ComputeYtdFromMonthlyRevenue",
                "arguments": {
                    "year": 2024,
                    "through_month": 11
                },
            },
            {
                "name": "ComputeTaxReserve",
                "arguments": {
                    "ytd_revenue": 10909.5,
                    "tax_year": 2024
                },
            },
            {
                "name": "GetDashboardSnapshot",
                "arguments": {
                    "snapshot_id": "SNAP004"
                },
            },
            {
                "name": "ReconcileTaxReserve",
                "arguments": {
                    "computed_tax_reserve_ref": {
                        "tax_reserve": 2891.02
                    },
                    "snapshot_ref": {
                        "ytd_tax_reserve": 2733.15
                    },
                    "threshold": 0.01
                },
            },
            {
                "name": "PostJournalEntry",
                "arguments": {
                    "date": "2024-11-30",
                    "account": "Tax Reserve",
                    "amount_ref": {
                        "adjustment": 157.87
                    },
                    "memo": "YTD tax reserve true-up"
                },
            },
            {
                "name": "BuildKpiReport",
                "arguments": {
                    "as_of": "2024-11-30",
                    "artifact_name": "TaxReserve_Confirm_2024-11",
                    "sections": [
                        "TaxReserve"
                    ]
                }
            }
        ],
        "outputs": [
                "157.87"
        ]
    }
]
