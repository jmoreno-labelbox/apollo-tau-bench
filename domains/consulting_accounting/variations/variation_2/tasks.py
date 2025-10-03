from domains.dto import Task, Action

TASKS = [

    Task(
        annotator="variation_2",
        user_id="task1",
        instruction=(
            "Handle the payment processing for invoice INV008 from Summit Educational Publishing on December 15, 2024 at 3:45 PM. Ensure that the payment is fully processed with the proper audit trail AUD602, and carry out strategic client relationship analysis encompassing payment behavior assessment, a review of the active project portfolio, profitability analysis of their primary project PROJ005, and YTD revenue impact assessment to aid ongoing account management decisions. Log the completion with scheduler run RUN201 for Payment_Processing_Analysis with success status."
        ),
        actions=[


            Action(name="CaV2GetInvoiceById", kwargs={
                "invoice_id": "INV008"
            }),


            Action(name="CaV2FindPublisherByName", kwargs={
                "publisher_name": "Summit Educational Publishing"
            }),


            Action(name="CaV2UpdateInvoicePayment", kwargs={
                "invoice_id": "INV008",
                "paid_at": "2024-12-15T15:45:00Z"
            }),


            Action(name="CaV2CreateInvoiceAuditEntry", kwargs={
                "audit_id": "AUD602",
                "invoice_id": "INV008",
                "event_type": "payment_received",
                "event_timestamp": "2024-12-15T15:45:00Z",
                "notes": "AUD602_payment_received_INV008"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB003"
            }),


             Action(name="CaV2GetProjectsByPublisher", kwargs={
                "publisher_id": "PUB003",
                 "active_only": True
             }),


            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ005"
            }),


            Action(name="CaV2CalculateYtdRevenue", kwargs={
                "year": "2024"
            }),


            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN201",
                "task_name": "Payment_Processing_Analysis",
                "status": "success"
            }),
        ],
        outputs=["1717.60"],  # Total payment amount from invoice INV008
    ),#

        Task(
        annotator="variation_2",
        user_id="task2",
        instruction=(
            "Coordinate the payment processing for invoice INV021 from Northern Star Publishers on December 20, 2024 at 2:30 PM. Ensure that the payment processing is completed with the correct audit trail AUD602, and execute strategic client relationship analysis covering payment behavior assessment, active project portfolio review, profitability analysis of their primary project PROJ001, and YTD revenue impact assessment to assist ongoing account management decisions. Record completion with scheduler run RUN202 for Payment_Processing_Analysis with success status."
        ),
        actions=[


            Action(name="CaV2GetInvoiceById", kwargs={
                "invoice_id": "INV021"
            }),


            Action(name="CaV2FindPublisherByName", kwargs={
                "publisher_name": "Northern Star Publishers"
            }),


            Action(name="CaV2UpdateInvoicePayment", kwargs={
                "invoice_id": "INV021",
                "paid_at": "2024-12-20T14:30:00Z"
            }),


            Action(name="CaV2CreateInvoiceAuditEntry", kwargs={
                "audit_id": "AUD602",
                "invoice_id": "INV021",
                "event_type": "payment_received",
                "event_timestamp": "2024-12-20T14:30:00Z",
                "notes": "AUD602_payment_received_INV021"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),


            Action(name="CaV2GetProjectsByPublisher", kwargs={
                "publisher_id": "PUB001",
                "active_only": True
            }),


            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),


            Action(name="CaV2CalculateYtdRevenue", kwargs={
                "year": "2024"
            }),


            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN202",
                "task_name": "Payment_Processing_Analysis",
                "status": "success"
            }),
        ],
        outputs=["1412.50"],  # Total payment amount from invoice INV021
    ),#

    Task(
        annotator="variation_2",
        user_id="task3",
        instruction=(
            "Handle the payment for invoice INV003 from Summit Educational Publishing on March 31, 2024, at 11:15 AM. Ensure the payment is fully processed with the appropriate audit trail AUD604 and carry out a strategic client relationship analysis, which includes evaluating payment behavior, reviewing the active project portfolio, analyzing the profitability of their main project PROJ005, and assessing the YTD revenue impact to aid ongoing account management decisions. Record the completion using scheduler run RUN301 for Payment_Processing_Analysis with a success status."
        ),
        actions=[


            Action(name="CaV2GetInvoiceById", kwargs={
                "invoice_id": "INV003"
            }),


            Action(name="CaV2FindPublisherByName", kwargs={
                "publisher_name": "Summit Educational Publishing"
            }),


            Action(name="CaV2UpdateInvoicePayment", kwargs={
                "invoice_id": "INV003",
                "paid_at": "2024-03-31T11:15:00Z"
            }),


            Action(name="CaV2CreateInvoiceAuditEntry", kwargs={
                "audit_id": "AUD604",
                "invoice_id": "INV003",
                "event_type": "payment_received",
                "event_timestamp": "2024-03-31T11:15:00Z",
                "notes": "AUD604_payment_received_INV003"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB003"
            }),


            Action(name="CaV2GetProjectsByPublisher", kwargs={
                "publisher_id": "PUB003",
                "active_only": True
            }),


            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ005"
            }),


            Action(name="CaV2CalculateYtdRevenue", kwargs={
                "year": "2024"
            }),


            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN301",
                "task_name": "Payment_Processing_Analysis",
                "status": "success"
            }),
                ],
        outputs=["1440.75"],  # Total payment amount from invoice INV003
    ),#

    Task(
        annotator="variation_2",
        user_id="task4",
        instruction=(
            "Handle the payment for invoice INV004 from Northern Star Publishers on April 30, 2024, at 5:00 PM. Ensure the payment is fully processed with the appropriate audit trail AUD605 and carry out a strategic client relationship analysis, which includes evaluating payment behavior, reviewing the active project portfolio, analyzing the profitability of their main project PROJ001, and assessing the YTD revenue impact to aid ongoing account management decisions. Record the completion using scheduler run RUN401 for Payment_Processing_Analysis with a success status."
        ),
        actions=[


            Action(name="CaV2GetInvoiceById", kwargs={
                "invoice_id": "INV004"
            }),


            Action(name="CaV2FindPublisherByName", kwargs={
                "publisher_name": "Northern Star Publishers"
            }),


            Action(name="CaV2UpdateInvoicePayment", kwargs={
                "invoice_id": "INV004",
                "paid_at": "2024-04-30T17:00:00Z"
            }),


            Action(name="CaV2CreateInvoiceAuditEntry", kwargs={
                "audit_id": "AUD605",
                "invoice_id": "INV004",
                "event_type": "payment_received",
                "event_timestamp": "2024-04-30T17:00:00Z",
                "notes": "AUD605_payment_received_INV004"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),


            Action(name="CaV2GetProjectsByPublisher", kwargs={
                "publisher_id": "PUB001",
                "active_only": True
            }),


            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),


            Action(name="CaV2CalculateYtdRevenue", kwargs={
                "year": "2024"
            }),


            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN401",
                "task_name": "Payment_Processing_Analysis",
                "status": "success"
            }),
        ],
        outputs=["576.30"],  # Total payment amount from invoice INV004
    ),#

    Task(
        annotator="variation_2",
        user_id="task5",
        instruction=(
            "Handle the development of comprehensive strategic market intelligence and competitive performance evaluation on December 5, 2024. Analyze payment behavior for publishers PUB001, PUB002, PUB003, and PUB004 to evaluate their market positioning and collection strategies. Calculate profitability for projects PROJ001, PROJ002, PROJ003, and PROJ004 to identify strategic value creation opportunities. Determine the hours worked for projects PROJ001 and PROJ002 from November 20-December 5, 2024 for evaluating operational efficiency. Create database scheduler run RUN3005 for Strategic_Market_Intelligence_Performance, scheduled at 2:30 PM and executed at 4:15 PM on December 5, 2024, with a success status."
        ),
        actions=[


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB002"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB003"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB004"
            }),


            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),


            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ002"
            }),


            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ003"
            }),


            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ004"
            }),


            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2024-11-20",
                "end_date": "2024-12-05",
                "project_ids": ["PROJ001"]
            }),


            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2024-11-20",
                "end_date": "2024-12-05",
                "project_ids": ["PROJ002"]
            }),


            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3005",
                "task_name": "Strategic_Market_Intelligence_Performance",
                "scheduled_for": "2024-12-05T14:30:00Z",
                "executed_at": "2024-12-05T16:15:00Z",
                "status": "success"
            }),
        ],
        outputs=["success"],  # Scheduler run status
    ),#

    Task(
        annotator="variation_2",
        user_id="task6",
        instruction=(
            "Coordinate the payment processing for invoice INV009 from Northern Star Publishers on December 12, 2024, at 2:30 PM. Ensure the payment processing is completed with a proper audit trail AUD601, and conduct a strategic client relationship analysis including the assessment of payment behavior, active project portfolio review, profitability analysis of their primary project PROJ001, and YTD revenue impact assessment to aid ongoing account management decisions. Document the completion with scheduler run RUN701 for Payment_Processing_Analysis with a success status."
        ),
                actions=[


            Action(name="CaV2GetInvoiceById", kwargs={
                "invoice_id": "INV009"
            }),


            Action(name="CaV2FindPublisherByName", kwargs={
                "publisher_name": "Northern Star Publishers"
            }),


            Action(name="CaV2UpdateInvoicePayment", kwargs={
                "invoice_id": "INV009",
                "paid_at": "2024-12-12T14:30:00Z"
            }),


            Action(name="CaV2CreateInvoiceAuditEntry", kwargs={
                "audit_id": "AUD601",
                "invoice_id": "INV009",
                "event_type": "payment_received",
                "event_timestamp": "2024-12-12T14:30:00Z",
                "notes": "AUD601_payment_received_INV009"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),


            Action(name="CaV2GetProjectsByPublisher", kwargs={
                "publisher_id": "PUB001",
                "active_only": True
            }),


            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),


            Action(name="CaV2CalculateYtdRevenue", kwargs={
                "year": "2024"
            }),


             Action(name="CaV2CreateSchedulerRun", kwargs={
                 "run_id": "RUN701",
                 "task_name": "Payment_Processing_Analysis",
                 "status": "success"
             }),
        ],
        outputs=["691.56"],  # Total payment amount from invoice
    ),#

      Task(
          annotator="variation_2",
          user_id="task7",
        instruction=(
            "Carry out a comprehensive strategic business intelligence and competitive market analysis on December 30, 2024. Analyze payment behavior for publishers PUB001, PUB002, PUB003, PUB004, and PUB005 to assess market positioning and collection strategies. Calculate profitability for projects PROJ001, PROJ002, PROJ003, PROJ004, and PROJ005 to identify strategic value creation opportunities. Determine hours worked for projects PROJ001, PROJ002, and PROJ003 from December 15-30, 2024 to evaluate operational excellence. Create a database scheduler run RUN3007 for Strategic_Business_Intelligence_Market_Analysis scheduled at 3:00 PM and executed at 4:45 PM on December 30, 2024, ensuring success status."
        ),
          actions=[


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB002"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB003"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB004"
            }),


              Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB005"
            }),


            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),


            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ002"
            }),


            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ003"
            }),


            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ004"
            }),


            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ005"
            }),


            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2024-12-15",
                "end_date": "2024-12-30",
                "project_ids": ["PROJ001"]
            }),


            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2024-12-15",
                "end_date": "2024-12-30",
                "project_ids": ["PROJ002"]
            }),


            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2024-12-15",
                "end_date": "2024-12-30",
                "project_ids": ["PROJ003"]
            }),


              Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3007",
                "task_name": "Strategic_Business_Intelligence_Market_Analysis",
                "scheduled_for": "2024-12-30T15:00:00Z",
                "executed_at": "2024-12-30T16:45:00Z",
                  "status": "success"
              }),
          ],
        outputs=["success"],  # Scheduler run status
      ),#

    Task(
        annotator="variation_2",
        user_id="task8",
        instruction=(
            "Initiate a thorough development of business intelligence and strategic planning on February 5, 2025. Examine payment behavior for publishers PUB001, PUB002, PUB003, and PUB005 to evaluate collection patterns and revenue predictability. Compute profitability for projects PROJ001, PROJ002, PROJ004, and PROJ005 to evaluate portfolio performance. Calculate hours worked for projects PROJ002, PROJ004, and PROJ005 from January 15-February 5, 2025 for effective resource planning. Conduct a database scheduler run RUN3008 for Business_Intelligence_Strategic_Planning, confirming its success status."
        ),
        actions=[


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB002"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB003"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB005"
            }),


            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),


            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ002"
            }),


            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ004"
            }),


            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ005"
            }),


            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-01-15",
                "end_date": "2025-02-05",
                "project_ids": ["PROJ002"]
            }),


            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-01-15",
                "end_date": "2025-02-05",
                "project_ids": ["PROJ004"]
            }),


            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-01-15",
                "end_date": "2025-02-05",
                "project_ids": ["PROJ005"]
            }),

            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3008",
                "task_name": "Business_Intelligence_Strategic_Planning",
                "status": "success"
            }),
        ],
        outputs=["success"],  # Scheduler run status
    ),#

    Task(
        annotator="variation_2",
        user_id="task9",
        instruction=(
            "Handle strategic performance evaluation and conduct a market analysis on December 10, 2024. Analyze payment behavior for publishers PUB002, PUB003, PUB004, and PUB005 to determine market position and collection efficiency. Calculate profitability for projects PROJ001, PROJ003, PROJ006, and PROJ007 to assess strategic value creation. Evaluate hours worked for projects PROJ001, PROJ003, and PROJ006 from December 1-10, 2024 for performance evaluation. Coordinate the creation of database scheduler run RUN3009 for Strategic_Performance_Market_Analysis scheduled at 2:00 PM and executed at 3:30 PM on December 10, 2024 ensuring success status."
        ),
        actions=[


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB002"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB003"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB004"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB005"
            }),


            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),


            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ003"
            }),


            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ006"
            }),


            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ007"
            }),


            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2024-12-01",
                "end_date": "2024-12-10",
                "project_ids": ["PROJ001"]
            }),


            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2024-12-01",
                "end_date": "2024-12-10",
                "project_ids": ["PROJ003"]
            }),


            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2024-12-01",
                "end_date": "2024-12-10",
                "project_ids": ["PROJ006"]
            }),


            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3009",
                "task_name": "Strategic_Performance_Market_Analysis",
                "scheduled_for": "2024-12-10T14:00:00Z",
                "executed_at": "2024-12-10T15:30:00Z",
                "status": "success"
            }),
        ],
        outputs=["success"],  # Scheduler run status
    ),#

    Task(
        annotator="variation_2",
        user_id="task10",
        instruction=(
            "Coordinate the development of a comprehensive strategic portfolio performance and competitive intelligence on January 12, 2025. Analyze payment behavior for publishers PUB001, PUB002, PUB003, PUB004, and PUB005 to assess market positioning and collection strategies. Determine profitability for projects PROJ001, PROJ002, PROJ003, PROJ004, and PROJ005 to evaluate opportunities for strategic value creation. Review hours worked for projects PROJ001, PROJ002, and PROJ003 from December 28, 2024-January 12, 2025 to ensure operational excellence. Arrange for database scheduler run RUN3010 to be created for Strategic_Portfolio_Performance_Intelligence with a success status."
        ),
        actions=[


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB002"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB003"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB004"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB005"
            }),


            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),


            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ002"
            }),


            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ003"
            }),


            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ004"
            }),


            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ005"
            }),


            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2024-12-28",
                "end_date": "2025-01-12",
                "project_ids": ["PROJ001", "PROJ002", "PROJ003"]
            }),


            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3010",
                "task_name": "Strategic_Portfolio_Performance_Intelligence",
                "status": "success"
            }),
        ],
        outputs=["success"],  # Scheduler run status
     ),#

       Task(
           annotator="variation_2",
           user_id="task11",
        instruction=(
            "Handle a thorough multi-publisher portfolio analysis on December 25, 2024. Examine payment behavior for Aurora Academic Press PUB002 and Northern Star Publishers PUB001. Assess profitability for projects PROJ003 and PROJ001, and tally hours worked for both projects from December 1-20, 2024. Evaluate pipeline opportunities with a minimum probability threshold of 0.6 and compute YTD revenue for 2024. Generate database scheduler run RUN1201 for Multi_Publisher_Portfolio_Analysis with a success status."
        ),
           actions=[


               Action(name="CaV2FindPublisherByName", kwargs={
                   "publisher_name": "Aurora Academic Press"
               }),


               Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                   "publisher_id": "PUB002"
               }),


               Action(name="CaV2FindPublisherByName", kwargs={
                   "publisher_name": "Northern Star Publishers"
               }),


               Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                   "publisher_id": "PUB001"
               }),


               Action(name="CaV2CalculateProjectProfitability", kwargs={
                   "project_id": "PROJ003"
               }),


               Action(name="CaV2CalculateProjectProfitability", kwargs={
                   "project_id": "PROJ001"
               }),


               Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                   "start_date": "2024-12-01",
                   "end_date": "2024-12-20",
                   "project_ids": ["PROJ003"]
               }),


               Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                   "start_date": "2024-12-01",
                   "end_date": "2024-12-20",
                   "project_ids": ["PROJ001"]
               }),


               Action(name="CaV2GetPipelineOpportunities", kwargs={
                   "min_probability": 0.6
               }),


               Action(name="CaV2CalculateYtdRevenue", kwargs={
                   "year": "2024"
               }),


               Action(name="CaV2CreateSchedulerRun", kwargs={
                   "run_id": "RUN1201",
                   "task_name": "Multi_Publisher_Portfolio_Analysis",
                   "status": "success"
               }),
           ],
           outputs=["19249.5"],  # YTD revenue from comprehensive analysis
       ),#

    Task(
        annotator="variation_2",
            user_id="task12",
        instruction=(
            "Coordinate a detailed accounts receivable aging analysis and cash flow assessment on December 26, 2024. Inspect unpaid invoices to determine collection status and compute the total outstanding amounts. Review payment behavior patterns for publisher PUB003 to understand collection risks. Evaluate profitability for project PROJ006 to assess revenue quality. Project cash flow for December 26, 2024, and assess pipeline opportunities with a minimum probability of 0.7. Analyze time entry patterns for project PROJ001 from December 1-20, 2024, and tally hours worked. Initiate database scheduler run RUN1301 for AR_Aging_Cash_Flow_Analysis with a success status."
        ),
        actions=[
                Action(name="CaV2GetUnpaidInvoices", kwargs={}),


                Action(name="CaV2CalculateInvoiceAging", kwargs={
                    "current_date": "2024-12-26"
                }),


                Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                    "publisher_id": "PUB003"
                }),


                Action(name="CaV2CalculateProjectProfitability", kwargs={
                    "project_id": "PROJ006"
                }),


                Action(name="CaV2ForecastCashFlow", kwargs={
                    "current_date": "2024-12-26"
                }),


                Action(name="CaV2GetPipelineOpportunities", kwargs={
                    "min_probability": 0.7
                }),


                Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                    "start_date": "2024-12-01",
                    "end_date": "2024-12-20",
                    "project_ids": ["PROJ001"]
                }),


                Action(name="CaV2CreateSchedulerRun", kwargs={
                    "run_id": "RUN1301",
                    "task_name": "AR_Aging_Cash_Flow_Analysis",
                "status": "success"
            }),
        ],
            outputs=["success"],  # Task completion status
        ),#

       Task(
           annotator="variation_2",
           user_id="task13",
        instruction=(
            "Handle strategic business intelligence and reporting on December 27, 2024. Analyze time entry patterns for projects PROJ001, PROJ003, and PROJ006 from December 1-25, 2024. Assess profitability for each of these projects and review payment behavior for publishers PUB001, PUB002, and PUB003. Evaluate pipeline opportunities with a minimum probability threshold of 0.5 and calculate YTD revenue for 2024. Create database scheduler run RUN1401 for Strategic_Business_Intelligence, ensuring it achieves success status."
        ),
           actions=[
               Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                   "start_date": "2024-12-01",
                   "end_date": "2024-12-25",
                   "project_ids": ["PROJ001"]
               }),


               Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                   "start_date": "2024-12-01",
                   "end_date": "2024-12-25",
                   "project_ids": ["PROJ003"]
               }),


               Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                   "start_date": "2024-12-01",
                   "end_date": "2024-12-25",
                   "project_ids": ["PROJ006"]
               }),


               Action(name="CaV2CalculateProjectProfitability", kwargs={
                   "project_id": "PROJ001"
               }),


               Action(name="CaV2CalculateProjectProfitability", kwargs={
                   "project_id": "PROJ003"
               }),


               Action(name="CaV2CalculateProjectProfitability", kwargs={
                   "project_id": "PROJ006"
               }),


               Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                   "publisher_id": "PUB001"
               }),


               Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                   "publisher_id": "PUB002"
               }),


               Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                   "publisher_id": "PUB003"
               }),


               Action(name="CaV2GetPipelineOpportunities", kwargs={
                   "min_probability": 0.5
               }),


               Action(name="CaV2CalculateYtdRevenue", kwargs={
                   "year": "2024"
               }),


               Action(name="CaV2CreateSchedulerRun", kwargs={
                   "run_id": "RUN1401",
                   "task_name": "Strategic_Business_Intelligence",
                   "status": "success"
               }),
           ],
           outputs=["8.0", "5.5", "4.75", "19249.5"],  # Total hours worked for all three projects and YTD revenue from comprehensive analysis
       ),

         Task(
             annotator="variation_2",
             user_id="task14",
        instruction=(
            "Coordinate a comprehensive financial analysis and strategic planning on February 15, 2024. Investigate payment behavior for publishers PUB001, PUB002, PUB003, PUB004, and PUB005 to evaluate collection efficiency and market positioning. Determine profitability for projects PROJ002, PROJ003, PROJ004, PROJ005, and PROJ006 to assess strategic portfolio value. Calculate the hours worked for projects PROJ002, PROJ004, and PROJ005 from January 25-February 15, 2024 for resource optimization. Create database scheduler run RUN3014 for Comprehensive_Financial_Strategic_Planning and ensure it succeeds."
        ),
             actions=[
            # Get payment behavior for PUB001
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),

            # Get payment behavior for PUB002
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB002"
            }),

            # Get payment behavior for PUB003
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB003"
            }),

            # Get payment behavior for PUB004
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB004"
            }),

            # Get payment behavior for PUB005
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB005"
            }),

            # Calculate profitability for PROJ002
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ002"
            }),

            # Calculate profitability for PROJ003
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ003"
            }),

            # Calculate profitability for PROJ004
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ004"
            }),

            # Calculate profitability for PROJ005
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ005"
            }),

            # Calculate profitability for PROJ006
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ006"
            }),

            # Calculate hours worked for PROJ002
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2024-01-25",
                "end_date": "2024-02-15",
                "project_ids": ["PROJ002"]
            }),

            # Calculate hours worked for PROJ004
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2024-01-25",
                "end_date": "2024-02-15",
                "project_ids": ["PROJ004"]
            }),

            # Calculate hours worked for PROJ005
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2024-01-25",
                "end_date": "2024-02-15",
                "project_ids": ["PROJ005"]
            }),

            # Log comprehensive financial strategic planning completion
                 Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3014",
                "task_name": "Comprehensive_Financial_Strategic_Planning",
                     "status": "success"
                 }),
             ],
        outputs=["success"],  # Scheduler run status
         ),

    Task(
        annotator="variation_2",
        user_id="task15",
        instruction=(
            "Handle the development of comprehensive strategic portfolio management and performance analytics on April 15, 2024. It is necessary to analyze payment behavior for publishers PUB001, PUB002, and PUB003 to assess collection patterns and revenue predictability. Calculate profitability for projects PROJ001, PROJ002, and PROJ003 to evaluate portfolio performance. Determine hours worked for projects PROJ001, PROJ002, and PROJ003 from March 25-April 15, 2024, for resource planning. Create database scheduler run RUN3015 for Strategic_Portfolio_Management_Performance_Analytics with success status."
        ),
        actions=[
            # Get payment behavior for PUB001
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),

            # Get payment behavior for PUB002
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB002"
            }),

            # Get payment behavior for PUB003
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB003"
            }),

            # Calculate profitability for PROJ001
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),

            # Calculate profitability for PROJ002
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ002"
            }),

            # Calculate profitability for PROJ003
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ003"
            }),

            # Calculate hours worked for PROJ001
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2024-03-25",
                "end_date": "2024-04-15",
                "project_ids": ["PROJ001"]
            }),

            # Calculate hours worked for PROJ002
            # Calculate hours worked for PROJ002
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2024-03-25",
                "end_date": "2024-04-15",
                "project_ids": ["PROJ002"]
            }),

            # Calculate hours worked for PROJ003
            # Calculate hours worked for PROJ003
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2024-03-25",
                "end_date": "2024-04-15",
                "project_ids": ["PROJ003"]
            }),

            # Log strategic portfolio management performance analytics completion
            # Log strategic portfolio management performance analytics completion
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3015",
                "task_name": "Strategic_Portfolio_Management_Performance_Analytics",
                "status": "success"
            }),
        ],
        outputs=["success"],
    ),#

         Task(
             annotator="variation_2",
             user_id="task16",
        instruction=(
            "Coordinate a comprehensive invoice management and collection analysis on December 30, 2024. Analyze invoice aging for December 30, 2024, and forecast cash flow for collection planning. Review all unpaid invoices to assess collection status and calculate total outstanding amounts. Examine payment behavior for publishers PUB001, PUB002, and PUB003. Evaluate profitability for projects PROJ001, PROJ003, and PROJ006 to understand revenue sources. Set up database scheduler run RUN1701 for Invoice_Collection_Analysis with success status."
        ),
             actions=[
                 Action(name="CaV2CalculateInvoiceAging", kwargs={
                     "current_date": "2024-12-30"
                 }),


                 Action(name="CaV2ForecastCashFlow", kwargs={
                     "current_date": "2024-12-30"
                 }),


                 Action(name="CaV2GetUnpaidInvoices", kwargs={}),


                 Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                     "publisher_id": "PUB001"
                 }),


                 Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                     "publisher_id": "PUB002"
                 }),


                 Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                     "publisher_id": "PUB003"
                 }),


                 Action(name="CaV2CalculateProjectProfitability", kwargs={
                     "project_id": "PROJ001"
                 }),


                 Action(name="CaV2CalculateProjectProfitability", kwargs={
                     "project_id": "PROJ003"
                 }),


                 Action(name="CaV2CalculateProjectProfitability", kwargs={
                     "project_id": "PROJ006"
                 }),


                 Action(name="CaV2CreateSchedulerRun", kwargs={
                     "run_id": "RUN1701",
                     "task_name": "Invoice_Collection_Analysis",
                     "status": "success"
                 }),
             ],
             outputs=["14709.21"],  # Total outstanding amounts from comprehensive analysis
         ),#

      Task(
          annotator="variation_2",
          user_id="task17",
        instruction=(
            "Handle time entry approval and project performance analysis on December 31, 2024. Proceed with reviewing time entries for project PROJ001 from December 1-31, 2024 and approve time entry TIME019 with reason 'year_end_approval'. Conduct an analysis of time entry patterns for projects PROJ001 and PROJ003 from December 1-31, 2024. Evaluate the profitability for both projects and review payment behavior for publishers PUB001 and PUB002. Investigate pipeline opportunities using a 0.7 minimum probability threshold and calculate YTD revenue for 2024. Coordinate the creation of database scheduler run RUN1801 for Time_Entry_Project_Analysis with success status."
        ),
          actions=[
              Action(name="CaV2GetTimeEntriesForPeriod", kwargs={
                  "project_id": "PROJ001",
                  "start_date": "2024-12-01",
                  "end_date": "2024-12-31"
              }),


              Action(name="CaV2ApproveTimeEntry", kwargs={
                  "entry_id": "TIME019",
                  "approved_by": "consultant",
                  "approval_reason": "year_end_approval"
              }),


              Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                  "start_date": "2024-12-01",
                  "end_date": "2024-12-31",
                  "project_ids": ["PROJ001"]
              }),


              Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                  "start_date": "2024-12-01",
                  "end_date": "2024-12-31",
                  "project_ids": ["PROJ003"]
              }),


              Action(name="CaV2CalculateProjectProfitability", kwargs={
                  "project_id": "PROJ001"
              }),


              Action(name="CaV2CalculateProjectProfitability", kwargs={
                  "project_id": "PROJ003"
              }),


              Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                  "publisher_id": "PUB001"
              }),


              Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                  "publisher_id": "PUB002"
              }),


              Action(name="CaV2GetPipelineOpportunities", kwargs={
                  "min_probability": 0.7
              }),


              Action(name="CaV2CalculateYtdRevenue", kwargs={
                  "year": "2024"
              }),


              Action(name="CaV2CreateSchedulerRun", kwargs={
                  "run_id": "RUN1801",
                  "task_name": "Time_Entry_Project_Analysis",
                  "status": "success"
              }),
          ],
          outputs=["19249.5"],  # YTD revenue from calculation
      ),

         Task(
        annotator="variation_2",
        user_id="task18",
        instruction=(
            "Coordinate bank account management and liquidity analysis on September 15, 2024. Assess all bank accounts and calculate total liquid assets for immediate liquidity assessment. Conduct invoice aging analysis for September 15, 2024 and forecast cash flow for liquidity planning. Review payment behavior for publishers PUB001, PUB002, and PUB003 to understand cash inflows. Analyze profitability for projects PROJ001, PROJ004, and PROJ006 to ascertain revenue sources. Examine pipeline opportunities with an 0.8 minimum probability threshold for future cash flow. Manage the creation of database scheduler run RUN1901 for Bank_Liquidity_Analysis with success status."
        ),
        actions=[
            # Get all bank accounts
            Action(name="CaV2GetBankAccounts", kwargs={}),

            # Calculate total liquid assets
            Action(name="CaV2CalculateBankTotal", kwargs={}),

                       # Calculate invoice aging
            Action(name="CaV2CalculateInvoiceAging", kwargs={
                "current_date": "2024-09-15"
            }),

            # Forecast cash flow
            Action(name="CaV2ForecastCashFlow", kwargs={
                "current_date": "2024-09-15"
            }),

            # Get payment behavior for PUB001
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),

            # Get payment behavior for PUB002
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB002"
            }),

            # Get payment behavior for PUB003
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB003"
            }),

            # Calculate profitability for PROJ001
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),

            # Calculate profitability for PROJ004
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ004"
            }),

            # Calculate profitability for PROJ006
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ006"
            }),

             # Get pipeline opportunities
             Action(name="CaV2GetPipelineOpportunities", kwargs={
                 "min_probability": 0.8
             }),

             # Log bank liquidity analysis completion
             Action(name="CaV2CreateSchedulerRun", kwargs={
                 "run_id": "RUN1901",
                 "task_name": "Bank_Liquidity_Analysis",
                 "status": "success"
             }),
         ],
         outputs=["success"],  # Task completion status
     ),#

    Task(
        annotator="variation_2",
           user_id="task19",
        instruction=(
            "Handle payment processing for invoice INV013 from Summit Educational Publishing on August 20, 2024, at 4:20 PM. Ensure the payment is processed completely with the proper audit trail AUD619. Coordinate a strategic client relationship analysis that includes evaluating payment behavior, reviewing the active project portfolio, analyzing the profitability of their primary project PROJ005, and assessing YTD revenue impact for 2024 to support decisions in account management. Record the completion of these tasks with scheduler run RUN1902 for Payment_Processing_Analysis, confirming a success status."
        ),
        actions=[


            Action(name="CaV2GetInvoiceById", kwargs={
                "invoice_id": "INV013"
            }),


            Action(name="CaV2FindPublisherByName", kwargs={
                "publisher_name": "Summit Educational Publishing"
            }),


            Action(name="CaV2UpdateInvoicePayment", kwargs={
                "invoice_id": "INV013",
                "paid_at": "2024-08-20T16:20:00Z"
            }),


            Action(name="CaV2CreateInvoiceAuditEntry", kwargs={
                "audit_id": "AUD619",
                "invoice_id": "INV013",
                "event_type": "payment_received",
                "event_timestamp": "2024-08-20T16:20:00Z",
                "notes": "AUD619_payment_received_INV013"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB003"
            }),


            Action(name="CaV2GetProjectsByPublisher", kwargs={
                "publisher_id": "PUB003",
                "active_only": True
            }),


            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ005"
            }),


               Action(name="CaV2CalculateYtdRevenue", kwargs={
                "year": "2024"
            }),


            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN1902",
                "task_name": "Payment_Processing_Analysis",
                "status": "success"
            }),
        ],
        outputs=["1017.00"],
    ),#

    Task(
        annotator="variation_2",
         user_id="task20",
        instruction=(
            "Conduct advanced business intelligence and reporting on January 4, 2025. Analyze the time entry patterns for projects PROJ001, PROJ003, and PROJ004 from December 1-31, 2024. Evaluate the profitability of all three projects and review the payment behavior for publishers PUB001 and PUB002. Assess pipeline opportunities with a minimum probability threshold of 0.5 and calculate the YTD revenue for 2024. Set up database scheduler run RUN2101 for Advanced_Business_Intelligence, ensuring it concludes with a success status."
        ),
            actions=[
             Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                 "start_date": "2024-12-01",
                 "end_date": "2024-12-31",
                 "project_ids": ["PROJ001"]
             }),


             Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                 "start_date": "2024-12-01",
                 "end_date": "2024-12-31",
                 "project_ids": ["PROJ003"]
             }),


             Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                 "start_date": "2024-12-01",
                 "end_date": "2024-12-31",
                 "project_ids": ["PROJ004"]
             }),


             Action(name="CaV2CalculateProjectProfitability", kwargs={
                 "project_id": "PROJ001"
             }),


             Action(name="CaV2CalculateProjectProfitability", kwargs={
                 "project_id": "PROJ003"
             }),


             Action(name="CaV2CalculateProjectProfitability", kwargs={
                 "project_id": "PROJ004"
             }),


             Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                 "publisher_id": "PUB001"
             }),


             Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                 "publisher_id": "PUB002"
             }),

             Action(name="CaV2GetPipelineOpportunities", kwargs={
                 "min_probability": 0.5
             }),

             Action(name="CaV2CalculateYtdRevenue", kwargs={
                "year": "2024"
            }),

             Action(name="CaV2CreateSchedulerRun", kwargs={
                 "run_id": "RUN2101",
                 "task_name": "Advanced_Business_Intelligence",
                 "status": "success"
             }),
         ],
         outputs=["19249.5"],  # YTD revenue from calculation
     ),#

     Task(
         annotator="variation_2",
         user_id="task21",
        instruction=(
            "Handle project portfolio and revenue analysis scheduled for January 5, 2025. Make sure to examine time entry patterns for projects PROJ001 and PROJ003 spanning December 1-31, 2024. Assess profitability for both projects and investigate payment behavior for publishers PUB001 and PUB002. Evaluate pipeline opportunities with at least a 0.6 probability threshold and figure out YTD revenue for 2024. Create database scheduler run RUN2201 for Project_Portfolio_Analysis ensuring it achieves success status."
        ),
         actions=[
             Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2024-12-01",
                 "end_date": "2024-12-31",
                 "project_ids": ["PROJ001"]
             }),

             Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                 "start_date": "2024-12-01",
                 "end_date": "2024-12-31",
                 "project_ids": ["PROJ003"]
             }),

             Action(name="CaV2CalculateProjectProfitability", kwargs={
                 "project_id": "PROJ001"
             }),

             Action(name="CaV2CalculateProjectProfitability", kwargs={
                 "project_id": "PROJ003"
             }),


             Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                 "publisher_id": "PUB001"
             }),


             Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                 "publisher_id": "PUB002"
             }),

             Action(name="CaV2GetPipelineOpportunities", kwargs={
                 "min_probability": 0.6
             }),

             Action(name="CaV2CalculateYtdRevenue", kwargs={
                 "year": "2024"
             }),

             Action(name="CaV2CreateSchedulerRun", kwargs={
                 "run_id": "RUN2201",
                 "task_name": "Project_Portfolio_Analysis",
                 "status": "success"
             }),
         ],
         outputs=["19249.5"],  # YTD revenue from calculation
     ),#

         Task(
             annotator="variation_2",
             user_id="task22",
        instruction=(
            "Coordinate the optimization of portfolio performance and strategic resource management on February 20, 2025. Investigate payment behavior for publishers PUB001, PUB003, PUB004, and PUB005 to gauge market stability and collection trends. Calculate profitability for projects PROJ001, PROJ003, PROJ005, PROJ006, and PROJ007 to assess strategic portfolio positioning. Determine hours worked for projects PROJ003, PROJ005, and PROJ006 from February 1-20, 2025 for an operational efficiency evaluation. Initiate database scheduler run RUN3022 for Portfolio_Performance_Strategic_Resource_Management and ensure it completes with success status."
        ),
            actions=[


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB003"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB004"
                }),


                Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                    "publisher_id": "PUB005"
                }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),
                Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ003"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ005"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ006"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ007"
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-02-01",
                "end_date": "2025-02-20",
                "project_ids": ["PROJ003"]
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-02-01",
                "end_date": "2025-02-20",
                "project_ids": ["PROJ005"]
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-02-01",
                "end_date": "2025-02-20",
                "project_ids": ["PROJ006"]
            }),
                Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3022",
                "task_name": "Portfolio_Performance_Strategic_Resource_Management",
                    "status": "success"
                }),
            ],
        outputs=["success"],  # Scheduler run status
        ),#

     Task(
         annotator="variation_2",
         user_id="task23",
        instruction=(
            "Handle revenue tracking and strategic planning on January 7, 2025. Examine time entry patterns for projects PROJ003 and PROJ004 from December 1-31, 2024. Assess the profitability of both projects and review payment behavior for publishers PUB002 and PUB003. Evaluate pipeline opportunities with at least a 0.8 probability threshold and compute YTD revenue for 2024. Create the database scheduler run RUN2401 for Revenue_Tracking_Strategic_Planning ensuring it completes successfully."
        ),
         actions=[
             Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                 "start_date": "2024-12-01",
                 "end_date": "2024-12-31",
                 "project_ids": ["PROJ003"]
             }),
             Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                 "start_date": "2024-12-01",
                 "end_date": "2024-12-31",
                 "project_ids": ["PROJ004"]
             }),
             Action(name="CaV2CalculateProjectProfitability", kwargs={
                 "project_id": "PROJ003"
             }),
             Action(name="CaV2CalculateProjectProfitability", kwargs={
                 "project_id": "PROJ004"
             }),


             Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                 "publisher_id": "PUB002"
             }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB003"
            }),
             Action(name="CaV2GetPipelineOpportunities", kwargs={
                 "min_probability": 0.8
             }),
             Action(name="CaV2CalculateYtdRevenue", kwargs={
                 "year": "2024"
             }),
            Action(name="CaV2CreateSchedulerRun", kwargs={
                 "run_id": "RUN2401",
                 "task_name": "Revenue_Tracking_Strategic_Planning",
                "status": "success"
            }),
        ],
        outputs=["19249.5"],  # YTD revenue from calculation
    ),#

    Task(
        annotator="variation_2",
           user_id="task24",
        instruction=(
            "Coordinate expense analysis and tax planning on January 8, 2025. Retrieve specific expenses for SOFTWARE_SUBSCR and PROF_FEES categories from January 1, 2024, to January 8, 2025. Obtain payment behavior for publisher PUB001. Determine the tax rate for the year 2024 and calculate YTD revenue for tax planning purposes. Generate the database scheduler run RUN2501 for Expense_Tax_Planning with a successful outcome."
        ),
        actions=[


               Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                   "publisher_id": "PUB001"
               }),

            Action(name="CaV2GetExpensesByCategory", kwargs={
                "category_code": "SOFTWARE_SUBSCR",
                "start_date": "2024-01-01",
                   "end_date": "2025-01-08"
            }),

            Action(name="CaV2GetExpensesByCategory", kwargs={
                "category_code": "PROF_FEES",
                "start_date": "2024-01-01",
                   "end_date": "2025-01-08"
               }),
            Action(name="CaV2GetTaxRateByYear", kwargs={
                "year": "2024"
            }),
            Action(name="CaV2CalculateYtdRevenue", kwargs={
                "year": "2024"
            }),
               Action(name="CaV2CreateSchedulerRun", kwargs={
                   "run_id": "RUN2501",
                   "task_name": "Expense_Tax_Planning",
                   "status": "success"
               }),
           ],
           outputs=["19249.5"],  # YTD revenue from calculation
       ),#

     Task(
         annotator="variation_2",
         user_id="task25",
        instruction=(
            "Handle strategic financial analysis and reporting on January 9, 2025. It is necessary to analyze time entry patterns for projects PROJ001 and PROJ006 from December 1-31, 2024. Assess profitability for both projects and review payment behavior for publishers PUB001 and PUB003. Evaluate pipeline opportunities with a 0.5 minimum probability threshold and calculate YTD revenue for 2024. Establish database scheduler run RUN2601 for Strategic_Financial_Analysis_Reporting with a success status."
        ),
         actions=[
             Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                 "start_date": "2024-12-01",
                 "end_date": "2024-12-31",
                 "project_ids": ["PROJ001"]
             }),
             Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                 "start_date": "2024-12-01",
                 "end_date": "2024-12-31",
                 "project_ids": ["PROJ006"]
             }),
             Action(name="CaV2CalculateProjectProfitability", kwargs={
                 "project_id": "PROJ001"
             }),
             Action(name="CaV2CalculateProjectProfitability", kwargs={
                 "project_id": "PROJ006"
             }),


             Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                 "publisher_id": "PUB001"
             }),


             Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                 "publisher_id": "PUB003"
             }),
             Action(name="CaV2GetPipelineOpportunities", kwargs={
                 "min_probability": 0.5
             }),
             Action(name="CaV2CalculateYtdRevenue", kwargs={
                 "year": "2024"
             }),
             Action(name="CaV2CreateSchedulerRun", kwargs={
                 "run_id": "RUN2601",
                 "task_name": "Strategic_Financial_Analysis_Reporting",
                 "status": "success"
             }),
         ],
         outputs=["19249.5"],  # YTD revenue from calculation
     ),#

       Task(
           annotator="variation_2",
           user_id="task26",
        instruction=(
            "Coordinate financial intelligence and analysis on January 10, 2025. Examine time entry patterns for projects PROJ001 and PROJ003 from December 1-31, 2024. Determine profitability for both projects and review payment behavior for publishers PUB001 and PUB002. Evaluate pipeline opportunities with a 0.6 minimum probability threshold and calculate YTD revenue for 2024. Create database scheduler run RUN2701 for Comprehensive_Financial_Intelligence ensuring success status."
        ),
           actions=[
               Action(name="CaV2GetTimeEntriesForPeriod", kwargs={
                   "project_id": "PROJ001",
                   "start_date": "2024-12-01",
                   "end_date": "2024-12-31"
               }),
               Action(name="CaV2GetTimeEntriesForPeriod", kwargs={
                   "project_id": "PROJ003",
                   "start_date": "2024-12-01",
                   "end_date": "2024-12-31"
               }),
               Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                   "start_date": "2024-12-01",
                   "end_date": "2024-12-31",
                   "project_ids": ["PROJ001"]
               }),
               Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                   "start_date": "2024-12-01",
                   "end_date": "2024-12-31",
                   "project_ids": ["PROJ003"]
               }),
               Action(name="CaV2CalculateProjectProfitability", kwargs={
                   "project_id": "PROJ001"
               }),
               Action(name="CaV2CalculateProjectProfitability", kwargs={
                   "project_id": "PROJ003"
               }),


               Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                   "publisher_id": "PUB001"
               }),


               Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                   "publisher_id": "PUB002"
               }),
               Action(name="CaV2GetPipelineOpportunities", kwargs={
                   "min_probability": 0.6
               }),
               Action(name="CaV2CalculateYtdRevenue", kwargs={
                   "year": "2024"
               }),
               Action(name="CaV2CreateSchedulerRun", kwargs={
                   "run_id": "RUN2701",
                   "task_name": "Comprehensive_Financial_Intelligence",
                   "status": "success"
               }),
           ],
           outputs=["19249.5"],  # YTD revenue from calculation
       ),#

     Task(
         annotator="variation_2",
         user_id="task27",
        instruction=(
            "Handle the revenue performance and strategic assessment on January 11, 2025. Be sure to analyze time entry patterns for project PROJ003 from December 1-31, 2024. It is necessary to assess profitability for the project and examine payment behavior for publisher PUB002. Evaluate pipeline opportunities with a minimum probability threshold of 0.7 and compute YTD revenue for 2024. Create database scheduler run RUN2801 for Revenue_Performance_Strategic_Assessment, ensuring it has a success status."
        ),
         actions=[
             Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                 "start_date": "2024-12-01",
                 "end_date": "2024-12-31",
                 "project_ids": ["PROJ003"]
             }),
             Action(name="CaV2CalculateProjectProfitability", kwargs={
                 "project_id": "PROJ003"
             }),


             Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                 "publisher_id": "PUB002"
             }),
             Action(name="CaV2GetPipelineOpportunities", kwargs={
                 "min_probability": 0.7
             }),
             Action(name="CaV2CalculateYtdRevenue", kwargs={
                 "year": "2024"
             }),
             Action(name="CaV2CreateSchedulerRun", kwargs={
                 "run_id": "RUN2801",
                 "task_name": "Revenue_Performance_Strategic_Assessment",
                 "status": "success"
             }),
         ],
         outputs=["19249.5"],  # YTD revenue from calculation
     ),#

     Task(
         annotator="variation_2",
         user_id="task28",
        instruction=(
            "Coordinate the multi-project portfolio and financial intelligence analysis on January 12, 2025. Remember to analyze time entry patterns for projects PROJ001, PROJ004, and PROJ006 from December 1-31, 2024. Ensure you assess profitability for all three projects and scrutinize payment behavior for publishers PUB001, PUB002, and PUB003. Evaluate pipeline opportunities with a minimum probability threshold of 0.8 and determine YTD revenue for 2024. Initiate database scheduler run RUN2901 for Multi_Project_Portfolio_Financial_Intelligence, confirming a success status."
        ),
         actions=[
             Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                 "start_date": "2024-12-01",
                 "end_date": "2024-12-31",
                 "project_ids": ["PROJ001"]
             }),
             Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                 "start_date": "2024-12-01",
                 "end_date": "2024-12-31",
                 "project_ids": ["PROJ004"]
             }),
             Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                 "start_date": "2024-12-01",
                 "end_date": "2024-12-31",
                 "project_ids": ["PROJ006"]
             }),
             Action(name="CaV2CalculateProjectProfitability", kwargs={
                 "project_id": "PROJ001"
             }),
             Action(name="CaV2CalculateProjectProfitability", kwargs={
                 "project_id": "PROJ004"
             }),
             Action(name="CaV2CalculateProjectProfitability", kwargs={
                 "project_id": "PROJ006"
             }),


             Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                 "publisher_id": "PUB001"
             }),


             Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                 "publisher_id": "PUB002"
             }),


             Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                 "publisher_id": "PUB003"
             }),
             Action(name="CaV2GetPipelineOpportunities", kwargs={
                 "min_probability": 0.8
             }),
             Action(name="CaV2CalculateYtdRevenue", kwargs={
                 "year": "2024"
             }),
             Action(name="CaV2CreateSchedulerRun", kwargs={
                 "run_id": "RUN2901",
                 "task_name": "Multi_Project_Portfolio_Financial_Intelligence",
                 "status": "success"
             }),
         ],
         outputs=["19249.5"],  # YTD revenue from calculation
     ),#

     Task(
         annotator="variation_2",
         user_id="task29",
        instruction=(
            "Handle consultant profile and project management analysis by January 13, 2025. Retrieve consultant profile details and assess time entry trends for projects PROJ001 and PROJ004 from December 1-31, 2024. Evaluate profitability for both projects and examine payment patterns for publishers PUB001 and PUB002. Assess pipeline opportunities with a minimum probability threshold of 0.9 and compute the YTD revenue for 2024. Establish database scheduler run RUN3001 for Consultant_Project_Management with a success status."
        ),
         actions=[
             Action(name="CaV2GetConsultantProfile", kwargs={}),
             Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                 "start_date": "2024-12-01",
                 "end_date": "2024-12-31",
                 "project_ids": ["PROJ001"]
             }),
             Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                 "start_date": "2024-12-01",
                 "end_date": "2024-12-31",
                 "project_ids": ["PROJ004"]
             }),
             Action(name="CaV2CalculateProjectProfitability", kwargs={
                 "project_id": "PROJ001"
             }),
             Action(name="CaV2CalculateProjectProfitability", kwargs={
                 "project_id": "PROJ004"
             }),


             Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                 "publisher_id": "PUB001"
             }),


             Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                 "publisher_id": "PUB002"
             }),
             Action(name="CaV2GetPipelineOpportunities", kwargs={
                 "min_probability": 0.9
             }),
             Action(name="CaV2CalculateYtdRevenue", kwargs={
                 "year": "2024"
             }),
             Action(name="CaV2CreateSchedulerRun", kwargs={
                 "run_id": "RUN3001",
                 "task_name": "Consultant_Project_Management",
                 "status": "success"
             }),
         ],
         outputs=["19249.5"],  # YTD revenue from calculation
     ),#

     Task(
         annotator="variation_2",
         user_id="task30",
        instruction=(
            "Coordinate portfolio and revenue intelligence analysis by January 14, 2025. Analyze time entry patterns for projects PROJ001, PROJ003, and PROJ004 from December 1-31, 2024. Determine profitability for all three projects and assess payment behavior for publishers PUB001 and PUB002. Examine pipeline opportunities with a 0.5 minimum probability threshold and compute YTD revenue for 2024. Initiate database scheduler run RUN3101 for Advanced_Portfolio_Revenue_Intelligence with a success status."
        ),
         actions=[
             Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                 "start_date": "2024-12-01",
                 "end_date": "2024-12-31",
                 "project_ids": ["PROJ001"]
             }),
             Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                 "start_date": "2024-12-01",
                 "end_date": "2024-12-31",
                 "project_ids": ["PROJ003"]
             }),
             Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                 "start_date": "2024-12-01",
                 "end_date": "2024-12-31",
                 "project_ids": ["PROJ004"]
             }),
             Action(name="CaV2CalculateProjectProfitability", kwargs={
                 "project_id": "PROJ001"
             }),
             Action(name="CaV2CalculateProjectProfitability", kwargs={
                 "project_id": "PROJ003"
             }),
             Action(name="CaV2CalculateProjectProfitability", kwargs={
                 "project_id": "PROJ004"
             }),


             Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                 "publisher_id": "PUB001"
             }),


             Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                 "publisher_id": "PUB002"
             }),
             Action(name="CaV2GetPipelineOpportunities", kwargs={
                 "min_probability": 0.5
             }),
             Action(name="CaV2CalculateYtdRevenue", kwargs={
                 "year": "2024"
             }),
             Action(name="CaV2CreateSchedulerRun", kwargs={
                 "run_id": "RUN3101",
                 "task_name": "Advanced_Portfolio_Revenue_Intelligence",
                 "status": "success"
             }),
         ],
         outputs=["19249.5"],  # YTD revenue from calculation
     ),#

    Task(
        annotator="variation_2",
        user_id="task31",
        instruction=(
            "Handle the development of comprehensive strategic business intelligence and portfolio optimization on March 10, 2024. Analyze payment behavior for publishers PUB001, PUB002, PUB003, PUB004, and PUB005 to gauge collection trends and market positioning. Ensure profitability calculations for projects PROJ001, PROJ002, PROJ003, PROJ004, and PROJ005 to evaluate strategic portfolio performance. Coordinate the calculation of hours worked on projects PROJ001, PROJ002, and PROJ003 from February 15-March 10, 2024 to determine resource allocation efficiency. Generate database scheduler run RUN3031 for Strategic_Business_Intelligence_Portfolio_Optimization, scheduled at 2:00 PM and executed at 3:45 PM on March 10, 2024, with a success status."
        ),
        actions=[


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB002"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB003"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB004"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB005"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ002"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ003"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ004"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ005"
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2024-02-15",
                "end_date": "2024-03-10",
                "project_ids": ["PROJ001"]
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2024-02-15",
                "end_date": "2024-03-10",
                "project_ids": ["PROJ002"]
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2024-02-15",
                "end_date": "2024-03-10",
                "project_ids": ["PROJ003"]
            }),
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3031",
                "task_name": "Strategic_Business_Intelligence_Portfolio_Optimization",
                "scheduled_for": "2024-03-10T14:00:00Z",
                "executed_at": "2024-03-10T15:45:00Z",
                "status": "success"
            }),
        ],
        outputs=["success"],  # Scheduler run status
    ),#

    Task(
        annotator="variation_2",
        user_id="task32",
        instruction=(
            "Coordinate strategic expense analysis and tax planning on January 16, 2025. Examine expense trends across SOFTWARE_SUBSCR, PROF_FEES, and OFFICE_SUPPLIES categories from January 1 to December 31, 2024 to pinpoint cost optimization opportunities. Assess tax implications for 2024 and review YTD revenue performance for strategic financial planning. Analyze specific expenditures for each category to gain insight into spending patterns and locate optimization potential. Initiate database scheduler run RUN3202 for Strategic_Expense_Analysis_Tax_Planning with a success status."
        ),
        actions=[
            Action(name="CaV2CalculateExpenseSummary", kwargs={
                "category_filter": ["SOFTWARE_SUBSCR"],
                "start_date": "2024-01-01",
                "end_date": "2024-12-31"
            }),
            Action(name="CaV2CalculateExpenseSummary", kwargs={
                "category_filter": ["PROF_FEES"],
                "start_date": "2024-01-01",
                "end_date": "2024-12-31"
            }),
            Action(name="CaV2CalculateExpenseSummary", kwargs={
                "category_filter": ["OFFICE_SUPPLIES"],
                "start_date": "2024-01-01",
                "end_date": "2024-12-31"
            }),
            Action(name="CaV2GetTaxRateByYear", kwargs={
                "year": "2024"
            }),
            Action(name="CaV2CalculateYtdRevenue", kwargs={
                "year": "2024"
            }),
            Action(name="CaV2GetExpensesByCategory", kwargs={
                "category_code": "SOFTWARE_SUBSCR",
                "start_date": "2024-01-01",
                "end_date": "2024-12-31"
            }),
            Action(name="CaV2GetExpensesByCategory", kwargs={
                "category_code": "PROF_FEES",
                "start_date": "2024-01-01",
                "end_date": "2024-12-31"
            }),
            Action(name="CaV2GetExpensesByCategory", kwargs={
                "category_code": "OFFICE_SUPPLIES",
                "start_date": "2024-01-01",
                "end_date": "2024-12-31"
            }),
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3202",
                "task_name": "Strategic_Expense_Analysis_Tax_Planning",
                "status": "success"
            }),
        ],
        outputs=["success"],  # Scheduler run status
    ),#

    Task(
        annotator="variation_2",
        user_id="task33",
        instruction=(
            "Handle the analysis of time tracking and project performance on January 17, 2025. Determine hours worked for projects PROJ001, PROJ003, and PROJ005 from January 1-15, 2025. Scrutinize payment behavior for publishers PUB001 and PUB002 to examine collection patterns. Calculate profitability for all three projects to evaluate performance metrics. Set up database scheduler run RUN3203 for Time_Tracking_Performance_Analysis and ensure it concludes with success status."
        ),
        actions=[
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-01-01",
                "end_date": "2025-01-15",
                "project_ids": ["PROJ001"]
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-01-01",
                "end_date": "2025-01-15",
                "project_ids": ["PROJ003"]
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-01-01",
                "end_date": "2025-01-15",
                "project_ids": ["PROJ005"]
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB002"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ003"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ005"
            }),
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3203",
                "task_name": "Time_Tracking_Performance_Analysis",
                "status": "success"
            }),
        ],
        outputs=["success"],  # Scheduler run status
    ),

    Task(
        annotator="variation_2",
        user_id="task34",
        instruction=(
            "Coordinate the collection of comprehensive strategic business intelligence and competitive analysis data on November 28, 2024. Gather payment behavior data for publishers PUB001, PUB002, PUB003, PUB004, and PUB005 to enhance market positioning and assess collection performance. Compile profitability data for projects PROJ001, PROJ002, PROJ003, PROJ004, and PROJ005 to support strategic value creation and competitive advantage assessment. Collect hours worked data for projects PROJ001, PROJ002, and PROJ003 from November 15-28, 2024 to aid in operational efficiency benchmarking. Schedule database scheduler run RUN3034 for Strategic_Business_Intelligence_Competitive_Analysis set for 4:00 PM and executed at 5:45 PM on November 28, 2024, ensuring it achieves a success status."
        ),
        actions=[
            # Get payment behavior for PUB001
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),

            # Get payment behavior for PUB002
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB002"
            }),

            # Get payment behavior for PUB003
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB003"
            }),

            # Get payment behavior for PUB004
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB004"
            }),

             # Get payment behavior for PUB005
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB005"
            }),

            # Calculate profitability for PROJ001
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),

            # Calculate profitability for PROJ002
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ002"
            }),

            # Calculate profitability for PROJ003
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ003"
            }),

            # Calculate profitability for PROJ004
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ004"
            }),

            # Calculate profitability for PROJ005
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ005"
            }),

            # Calculate hours worked for all analyzed projects
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2024-11-15",
                "end_date": "2024-11-28",
                "project_ids": ["PROJ001", "PROJ002", "PROJ003"]
            }),

            # Log strategic business intelligence competitive analysis completion
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3034",
                "task_name": "Strategic_Business_Intelligence_Competitive_Analysis",
                "scheduled_for": "2024-11-28T16:00:00Z",
                "executed_at": "2024-11-28T17:45:00Z",
                "status": "success"
            }),
        ],
        outputs=["success"],  # Scheduler run status
    ),

    Task(
        annotator="variation_2",
        user_id="task35",
        instruction=(
            "Handle the payment for invoice INV011 from Midwest Education House on December 15, 2024 at 3:30 PM. Ensure the entire payment process is accompanied by a proper audit trail AUD625 and coordinate strategic client relationship analysis, involving a payment behavior assessment, a review of the active project portfolio, a profitability analysis of their main project PROJ010, and an assessment of YTD revenue impact to aid in ongoing account management decisions. Record completion with scheduler run RUN3501 for Payment_Processing_Analysis with a success status."
        ),
                actions=[
            # Get invoice INV011 details
            Action(name="CaV2GetInvoiceById", kwargs={
                "invoice_id": "INV011"
            }),

            # Find Midwest Education House
            Action(name="CaV2FindPublisherByName", kwargs={
                "publisher_name": "Midwest Education House"
            }),

            # Update payment status
            Action(name="CaV2UpdateInvoicePayment", kwargs={
                "invoice_id": "INV011",
                "paid_at": "2024-12-15T15:30:00Z"
            }),

            # Create payment audit AUD625
            Action(name="CaV2CreateInvoiceAuditEntry", kwargs={
                "audit_id": "AUD625",
                "invoice_id": "INV011",
                "event_type": "payment_received",
                "event_timestamp": "2024-12-15T15:30:00Z",
                "notes": "AUD625_payment_received_INV011"
            }),

            # Get payment behavior for PUB005
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB005"
            }),

            # Get active projects for PUB005
            Action(name="CaV2GetProjectsByPublisher", kwargs={
                "publisher_id": "PUB005",
                "active_only": True
            }),

            # Calculate profitability for main project PROJ010
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ010"
            }),

            # Calculate YTD revenue for comparison
            Action(name="CaV2CalculateYtdRevenue", kwargs={
                "year": "2024"
            }),

            # Log payment processing completion
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3501",
                "task_name": "Payment_Processing_Analysis",
                "status": "success"
            }),
        ],
        outputs=["864.45"],  # Total payment amount from invoice INV011
    ),

    Task(
        annotator="variation_2",
        user_id="task36",
        instruction=(
            "Manage the payment processing for invoice INV026 from Northern Star Publishers on January 20, 2024 at 2:45 PM. Confirm complete payment processing with the necessary audit trail AUD626 and carry out strategic client relationship analysis, which includes evaluating payment behavior, reviewing the active project portfolio, analyzing profitability of their key project PROJ001, and assessing YTD revenue impact to facilitate ongoing account management decisions. Log completion with scheduler run RUN3601 for Payment_Processing_Analysis with success status."
        ),
                actions=[
            # Get invoice INV026 details
            Action(name="CaV2GetInvoiceById", kwargs={
                "invoice_id": "INV026"
            }),

            # Find Northern Star Publishers
            Action(name="CaV2FindPublisherByName", kwargs={
                "publisher_name": "Northern Star Publishers"
            }),

            # Update payment status
            Action(name="CaV2UpdateInvoicePayment", kwargs={
                "invoice_id": "INV026",
                "paid_at": "2024-01-20T14:45:00Z"
            }),

            # Create payment audit AUD626
            Action(name="CaV2CreateInvoiceAuditEntry", kwargs={
                "audit_id": "AUD626",
                "invoice_id": "INV026",
                "event_type": "payment_received",
                "event_timestamp": "2024-01-20T14:45:00Z",
                "notes": "AUD626_payment_received_INV026"
            }),

            # Get payment behavior for PUB001
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),

            # Get active projects for PUB001
            Action(name="CaV2GetProjectsByPublisher", kwargs={
                "publisher_id": "PUB001",
                "active_only": True
            }),

            # Calculate profitability for main project PROJ001
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),

            # Calculate YTD revenue for comparison
            Action(name="CaV2CalculateYtdRevenue", kwargs={
                "year": "2024"
            }),

            # Log payment processing completion
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3601",
                "task_name": "Payment_Processing_Analysis",
                "status": "success"
            }),
        ],
        outputs=["2373.00"],
    ),

    Task(
        annotator="variation_2",
        user_id="task37",
        instruction=(
            "Handle the payment processing for invoice INV022 from Summit Educational Publishing on July 15, 2024, at 10:30 AM. Ensure comprehensive payment processing with the correct audit trail AUD637, and carry out strategic client relationship analysis, including payment behavior assessment, active project portfolio review, profitability analysis of their main project PROJ005, and 2024 YTD revenue impact assessment to assist ongoing account management decisions. Confirm completion with scheduler run RUN3701 for Payment_Processing_Analysis marked with a success status."
        ),
        actions=[
            # Get invoice INV022 details
            Action(name="CaV2GetInvoiceById", kwargs={
                "invoice_id": "INV022"
            }),

            # Find Summit Educational Publishing
            Action(name="CaV2FindPublisherByName", kwargs={
                "publisher_name": "Summit Educational Publishing"
            }),

            # Update payment status
            Action(name="CaV2UpdateInvoicePayment", kwargs={
                "invoice_id": "INV022",
                "paid_at": "2024-07-15T10:30:00Z"
            }),

            # Create payment audit AUD637
            Action(name="CaV2CreateInvoiceAuditEntry", kwargs={
                "audit_id": "AUD637",
                "invoice_id": "INV022",
                "event_type": "payment_received",
                "event_timestamp": "2024-07-15T10:30:00Z",
                "notes": "AUD637_payment_received_INV022"
            }),

            # Get payment behavior for PUB003
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB003"
            }),

            # Get active projects for PUB003
            Action(name="CaV2GetProjectsByPublisher", kwargs={
                "publisher_id": "PUB003",
                "active_only": True
            }),

            # Calculate profitability for main project PROJ005
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ005"
            }),

            # Calculate YTD revenue for comparison
            Action(name="CaV2CalculateYtdRevenue", kwargs={
                "year": "2024"
            }),

            # Log payment processing completion
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3701",
                "task_name": "Payment_Processing_Analysis",
                "status": "success"
            }),
        ],
        outputs=["988.75"],
    ),

    Task(
        annotator="variation_2",
        user_id="task38",
        instruction=(
            "Coordinate the payment processing for invoice INV024 from Maritime Learning Materials on November 15, 2024, at 9:15 AM. You must ensure complete payment processing with the proper audit trail AUD638 and execute strategic client relationship analysis, including payment behavior assessment, active project portfolio review, profitability analysis of their primary project PROJ007, and the 2024 YTD revenue impact evaluation to support ongoing account management decisions. Mark completion with scheduler run RUN3801 for Payment_Processing_Analysis with a successful status."
        ),
        actions=[
            # Get invoice INV024 details
            Action(name="CaV2GetInvoiceById", kwargs={
                "invoice_id": "INV024"
            }),

            # Find Maritime Learning Materials
            Action(name="CaV2FindPublisherByName", kwargs={
                "publisher_name": "Maritime Learning Materials"
            }),

            # Update payment status
            Action(name="CaV2UpdateInvoicePayment", kwargs={
                "invoice_id": "INV024",
                "paid_at": "2024-11-15T09:15:00Z"
            }),

            # Create payment audit AUD638
            Action(name="CaV2CreateInvoiceAuditEntry", kwargs={
                "audit_id": "AUD638",
                "invoice_id": "INV024",
                "event_type": "payment_received",
                "event_timestamp": "2024-11-15T09:15:00Z",
                "notes": "AUD638_payment_received_INV024"
            }),

            # Get payment behavior for PUB004
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB004"
            }),

            # Get active projects for PUB004
            Action(name="CaV2GetProjectsByPublisher", kwargs={
                "publisher_id": "PUB004",
                "active_only": True
            }),

            # Calculate profitability for main project PROJ007
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ007"
            }),

            # Calculate current year YTD revenue for comparison
            Action(name="CaV2CalculateYtdRevenue", kwargs={
                "year": "2024"
            }),

            # Log payment processing completion
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3801",
                "task_name": "Payment_Processing_Analysis",
                "status": "success"
            }),
        ],
        outputs=["2090.50"],  # Total payment amount from invoice INV024
    ),

    Task(
        annotator="variation_2",
        user_id="task39",
        instruction=(
            "Handle the payment processing for invoice INV010 from Maritime Learning Materials on October 10, 2024, at 11:30 AM. Ensure to fully process the payment, maintaining a proper audit trail AUD639. Conduct a strategic analysis of client relationships, which includes assessing payment behavior, reviewing active project portfolios, analyzing the profitability of their primary project PROJ007, and evaluating the current year 2024 YTD revenue impact to aid ongoing account management decisions. Document the task completion using scheduler run RUN3209 for Payment_Processing_Analysis with a success status."
        ),
        actions=[
            # Get invoice INV010 details
            Action(name="CaV2GetInvoiceById", kwargs={
                "invoice_id": "INV010"
            }),

            # Find Maritime Learning Materials
            Action(name="CaV2FindPublisherByName", kwargs={
                "publisher_name": "Maritime Learning Materials"
            }),

            # Update payment status
            Action(name="CaV2UpdateInvoicePayment", kwargs={
                "invoice_id": "INV010",
                "paid_at": "2024-10-10T11:30:00Z"
            }),

            # Create payment audit AUD639
            Action(name="CaV2CreateInvoiceAuditEntry", kwargs={
                "audit_id": "AUD639",
                "invoice_id": "INV010",
                "event_type": "payment_received",
                "event_timestamp": "2024-10-10T11:30:00Z",
                "notes": "AUD639_payment_received_INV010"
            }),

            # Get payment behavior for PUB004
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB004"
            }),

            # Get active projects for PUB004
            Action(name="CaV2GetProjectsByPublisher", kwargs={
                "publisher_id": "PUB004",
                "active_only": True
            }),

            # Calculate profitability for main project PROJ007
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ007"
            }),

            # Calculate current year YTD revenue for comparison
            Action(name="CaV2CalculateYtdRevenue", kwargs={
                "year": "2024"
            }),

            # Log payment processing completion
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3209",
                "task_name": "Payment_Processing_Analysis",
                "status": "success"
            }),
        ],
        outputs=["1536.80"],  # Total payment amount from invoice INV010
    ),

    Task(
        annotator="variation_2",
        user_id="task40",
        instruction=(
            "Coordinate comprehensive strategic portfolio management and performance analytics on March 25, 2024. Analyze payment behavior for publishers PUB001, PUB002, and PUB003 to evaluate collection patterns and predict revenue. Calculate the profitability of projects PROJ001, PROJ002, and PROJ003 to assess the performance of the portfolio. Determine hours worked on projects PROJ001, PROJ002, and PROJ003 from February 15 to March 25, 2024, for resource planning purposes. Create a database scheduler run RUN4001 for Strategic_Portfolio_Management_Performance_Analytics with a success status."
        ),
        actions=[
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={"publisher_id": "PUB001"}),
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={"publisher_id": "PUB002"}),
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={"publisher_id": "PUB003"}),
            Action(name="CaV2CalculateProjectProfitability", kwargs={"project_id": "PROJ001"}),
            Action(name="CaV2CalculateProjectProfitability", kwargs={"project_id": "PROJ002"}),
            Action(name="CaV2CalculateProjectProfitability", kwargs={"project_id": "PROJ003"}),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={"start_date": "2024-02-15", "end_date": "2024-03-25", "project_ids": ["PROJ001"]}),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={"start_date": "2024-02-15", "end_date": "2024-03-25", "project_ids": ["PROJ002"]}),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={"start_date": "2024-02-15", "end_date": "2024-03-25", "project_ids": ["PROJ003"]}),
            Action(name="CaV2CreateSchedulerRun", kwargs={"run_id": "RUN4001", "task_name": "Strategic_Portfolio_Management_Performance_Analytics", "status": "success"}),
        ],
        outputs=["success"],
    ),

    Task(
        annotator="variation_2",
        user_id="task41",
        instruction=(
            "Handle comprehensive multi-project performance analysis on January 25, 2025. Calculate profitability for projects PROJ001, PROJ002, PROJ003, and PROJ004 to evaluate revenue distribution. Analyze payment behavior for publishers PUB001, PUB002, and PUB003 to assess collection efficiency. Calculate hours worked for projects PROJ001 and PROJ003 from January 1-25, 2025 to evaluate resource utilization. Review pipeline opportunities and create database scheduler run RUN3211 for Multi_Project_Performance_Analysis with success status."
        ),
        actions=[
            # Calculate profitability for PROJ001
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),

            # Calculate profitability for PROJ002
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ002"
            }),

            # Calculate profitability for PROJ003
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ003"
            }),

            # Calculate profitability for PROJ004
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ004"
            }),

            # Get payment behavior for PUB001
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),

            # Get payment behavior for PUB002
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB002"
            }),

            # Get payment behavior for PUB003
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB003"
            }),

            # Calculate hours worked for PROJ001
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-01-01",
                "end_date": "2025-01-25",
                "project_ids": ["PROJ001"]
            }),

            # Calculate hours worked for PROJ003
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-01-01",
                "end_date": "2025-01-25",
                "project_ids": ["PROJ003"]
            }),

            # Get pipeline opportunities
            Action(name="CaV2GetPipelineOpportunities", kwargs={}),

            # Log multi-project performance analysis completion
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3211",
                "task_name": "Multi_Project_Performance_Analysis",
                "status": "success"
            }),
        ],
        outputs=["success"],  # Scheduler run status
    ),

    Task(
        annotator="variation_2",
        user_id="task42",
        instruction=(
            "Coordinate the preparation of financial compliance and tax planning report on January 26, 2024. Calculate expense summary for categories OFFICE_SUPPLIES, TRAVEL_EXPENSE, and ADVERTISING from January 1-26, 2024. Acquire the tax rate for 2024 and calculate YTD revenue for comprehensive tax planning. Analyze payment behavior for publishers PUB001 and PUB002 to assess cash flow impact. Calculate profitability for projects PROJ001, PROJ003, and PROJ005 to evaluate revenue streams. Create database scheduler run RUN3212 for Financial_Compliance_Tax_Planning with success status."
        ),
        actions=[
            # Calculate expense summary for office supplies
            # Calculate expense summary for office supplies
            Action(name="CaV2CalculateExpenseSummary", kwargs={
                "category_filter": ["OFFICE_SUPPLIES"],
                "start_date": "2024-01-01",
                "end_date": "2024-01-26"
            }),

            # Calculate expense summary for travel
            # Calculate expense summary for travel
            Action(name="CaV2CalculateExpenseSummary", kwargs={
                "category_filter": ["TRAVEL_EXPENSE"],
                "start_date": "2024-01-01",
                "end_date": "2024-01-26"
            }),

            # Calculate expense summary for marketing
            # Calculate expense summary for marketing
            Action(name="CaV2CalculateExpenseSummary", kwargs={
                "category_filter": ["ADVERTISING"],
                "start_date": "2024-01-01",
                "end_date": "2024-01-26"
            }),

            # Get tax rate for 2024
            # Get tax rate for 2024
            Action(name="CaV2GetTaxRateByYear", kwargs={
                "year": "2024"
            }),

            # Calculate YTD revenue for tax planning
            # Calculate YTD revenue for tax planning
            Action(name="CaV2CalculateYtdRevenue", kwargs={
                "year": "2024"
            }),

            # Get payment behavior for PUB001
            # Get payment behavior for PUB001
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),

            # Get payment behavior for PUB002
            # Get payment behavior for PUB002
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB002"
            }),

            # Calculate profitability for PROJ001
            # Calculate profitability for PROJ001
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),

            # Calculate profitability for PROJ003
            # Calculate profitability for PROJ003
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ003"
            }),

            # Calculate profitability for PROJ005
            # Calculate profitability for PROJ005
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ005"
            }),

            # Log financial compliance tax planning completion
            # Log financial compliance tax planning completion
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3212",
                "task_name": "Financial_Compliance_Tax_Planning",
                "status": "success"
            }),
        ],
        outputs=["success"],  # Scheduler run completion status
    ),

    Task(
        annotator="variation_2",
        user_id="task43",
        instruction=(
            "Handle strategic publisher relationship optimization and revenue enhancement by March 30, 2025. Analyze payment behavior of publishers PUB001, PUB002, PUB003, and PUB004 to assess collection patterns and relationship stability. Calculate profitability for projects PROJ001, PROJ002, PROJ003, PROJ004, and PROJ005 to identify revenue optimization opportunities. Determine hours worked for projects PROJ002, PROJ003, and PROJ005 from March 10-30, 2025, for resource efficiency evaluation. Initiate database scheduler run RUN3043 for Strategic_Publisher_Relationship_Optimization_Revenue_Enhancement and ensure it achieves success status."
        ),
        actions=[
            # Get payment behavior for PUB001
            # Get payment behavior for PUB001
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),

            # Get payment behavior for PUB002
            # Get payment behavior for PUB002
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB002"
            }),

            # Get payment behavior for PUB003
            # Get payment behavior for PUB003
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB003"
            }),

            # Get payment behavior for PUB004
            # Get payment behavior for PUB004
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB004"
            }),

            # Calculate profitability for PROJ001
            # Calculate profitability for PROJ001
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),

            # Calculate profitability for PROJ002
            # Calculate profitability for PROJ002
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ002"
            }),

            # Calculate profitability for PROJ003
            # Calculate profitability for PROJ003
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ003"
            }),

            # Calculate profitability for PROJ004
            # Calculate profitability for PROJ004
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ004"
            }),

            # Calculate profitability for PROJ005
            # Calculate profitability for PROJ005
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ005"
            }),

            # Calculate hours worked for PROJ002
            # Calculate hours worked for PROJ002
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-03-10",
                "end_date": "2025-03-30",
                "project_ids": ["PROJ002"]
            }),

            # Calculate hours worked for PROJ003
            # Calculate hours worked for PROJ003
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-03-10",
                "end_date": "2025-03-30",
                "project_ids": ["PROJ003"]
            }),

            # Calculate hours worked for PROJ005
            # Calculate hours worked for PROJ005
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-03-10",
                "end_date": "2025-03-30",
                "project_ids": ["PROJ005"]
            }),

            # Log strategic publisher relationship optimization revenue enhancement completion
            # Log strategic publisher relationship optimization revenue enhancement completion
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3043",
                "task_name": "Strategic_Publisher_Relationship_Optimization_Revenue_Enhancement",
                "status": "success"
            }),
        ],
        outputs=["success"],  # Scheduler run status
    ),

    Task(
        annotator="variation_2",
        user_id="task44",
        instruction=(
            "Coordinate optimization of time management and resource allocation by January 28, 2025. Determine hours worked for projects PROJ001, PROJ002, PROJ003, and PROJ004 from January 1-28, 2025. Calculate profitability across all four projects for resource efficiency evaluation. Assess payment behavior of publishers PUB001 and PUB002 to evaluate revenue impact. Initiate database scheduler run RUN3214 for Time_Management_Resource_Optimization and confirm it reaches success status."
        ),
        actions=[
            # Calculate hours worked for PROJ001
            # Calculate hours worked for PROJ001
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-01-01",
                "end_date": "2025-01-28",
                "project_ids": ["PROJ001"]
            }),

            # Calculate hours worked for PROJ002
            # Calculate hours worked for PROJ002
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-01-01",
                "end_date": "2025-01-28",
                "project_ids": ["PROJ002"]
            }),

            # Calculate hours worked for PROJ003
            # Calculate hours worked for PROJ003
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-01-01",
                "end_date": "2025-01-28",
                "project_ids": ["PROJ003"]
            }),

            # Calculate hours worked for PROJ004
            # Calculate hours worked for PROJ004
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-01-01",
                "end_date": "2025-01-28",
                "project_ids": ["PROJ004"]
            }),

            # Get payment behavior for PUB001
            # Get payment behavior for PUB001
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),

            # Get payment behavior for PUB002
            # Get payment behavior for PUB002
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB002"
            }),

            # Calculate profitability for PROJ001
            # Calculate profitability for PROJ001
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),

            # Calculate profitability for PROJ002
            # Calculate profitability for PROJ002
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ002"
            }),

            # Calculate profitability for PROJ003
            # Calculate profitability for PROJ003
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ003"
            }),

            # Calculate profitability for PROJ004
            # Calculate profitability for PROJ004
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ004"
            }),

            # Log time management resource optimization completion
            # Log time management resource optimization completion
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3214",
                "task_name": "Time_Management_Resource_Optimization",
                "status": "success"
            }),
        ],
        outputs=["success"],  # Scheduler run status
    ),

    Task(
        annotator="variation_2",
        user_id="task45",
        instruction=(
            "Conduct advanced business intelligence and strategic performance optimization on April 5, 2025. Analyze payment behavior for publishers PUB001, PUB002, PUB003, PUB004, and PUB005 to evaluate collection efficiency and market position assessment. Calculate profitability for projects PROJ001, PROJ002, PROJ003, PROJ004, and PROJ005 to assess strategic revenue optimization opportunities. Calculate hours worked for projects PROJ001, PROJ002, and PROJ003 from March 15-April 5, 2025 for operational performance evaluation. Create database scheduler run RUN3045 for Advanced_Business_Intelligence_Strategic_Performance_Optimization with success status."
        ),
        actions=[
            # Get payment behavior for PUB001
            # Get payment behavior for PUB001
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),

            # Get payment behavior for PUB002
            # Get payment behavior for PUB002
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB002"
            }),

            # Get payment behavior for PUB003
            # Get payment behavior for PUB003
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB003"
            }),

            # Get payment behavior for PUB004
            # Get payment behavior for PUB004
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB004"
            }),

            # Get payment behavior for PUB005
            # Get payment behavior for PUB005
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB005"
            }),

            # Calculate profitability for PROJ001
            # Calculate profitability for PROJ001
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),

            # Calculate profitability for PROJ002
            # Calculate profitability for PROJ002
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ002"
            }),

            # Calculate profitability for PROJ003
            # Calculate profitability for PROJ003
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ003"
            }),

            # Calculate profitability for PROJ004
            # Calculate profitability for PROJ004
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ004"
            }),

            # Calculate profitability for PROJ005
            # Calculate profitability for PROJ005
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ005"
            }),

            # Calculate hours worked for PROJ001
            # Calculate hours worked for PROJ001
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-03-15",
                "end_date": "2025-04-05",
                "project_ids": ["PROJ001"]
            }),

            # Calculate hours worked for PROJ002
            # Calculate hours worked for PROJ002
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-03-15",
                "end_date": "2025-04-05",
                "project_ids": ["PROJ002"]
            }),

            # Calculate hours worked for PROJ003
            # Calculate hours worked for PROJ003
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-03-15",
                "end_date": "2025-04-05",
                "project_ids": ["PROJ003"]
            }),

            # Log advanced business intelligence strategic performance optimization completion
            # Log advanced business intelligence strategic performance optimization completion
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3045",
                "task_name": "Advanced_Business_Intelligence_Strategic_Performance_Optimization",
                "status": "success"
            }),
        ],
        outputs=["success"],  # Scheduler run status
    ),

    Task(
        annotator="variation_2",
        user_id="task46",
        instruction=(
            "Process payment for invoice INV026 from Northern Star Publishers on July 15, 2024 at 2:00 PM. Ensure complete payment processing with proper audit trail AUD646 and conduct strategic client relationship analysis including payment behavior assessment, active project portfolio review, profitability analysis of their primary project PROJ001, and YTD revenue impact assessment to support ongoing account management decisions. Document completion with scheduler run RUN4601 for Payment_Processing_Analysis with success status."
        ),
        actions=[
            # Get invoice INV026 details
            # Get invoice INV026 details
            Action(name="CaV2GetInvoiceById", kwargs={
                "invoice_id": "INV026"
            }),

            # Find Northern Star Publishers
            # Find Northern Star Publishers
            Action(name="CaV2FindPublisherByName", kwargs={
                "publisher_name": "Northern Star Publishers"
            }),

            # Update payment status
            # Update payment status
            Action(name="CaV2UpdateInvoicePayment", kwargs={
                "invoice_id": "INV026",
                "paid_at": "2024-07-15T14:00:00Z"
            }),

            # Create payment audit AUD646
            # Create payment audit AUD646
            Action(name="CaV2CreateInvoiceAuditEntry", kwargs={
                "audit_id": "AUD646",
                "invoice_id": "INV026",
                "event_type": "payment_received",
                "event_timestamp": "2024-07-15T14:00:00Z",
                "notes": "AUD646_payment_received_INV026"
            }),

            # Get payment behavior for PUB001
            # Get payment behavior for PUB001
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),

            # Get active projects for PUB001
            # Get active projects for PUB001
            Action(name="CaV2GetProjectsByPublisher", kwargs={
                "publisher_id": "PUB001",
                "active_only": True
            }),

            # Calculate profitability for main project PROJ001
            # Calculate profitability for main project PROJ001
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),

            # Calculate YTD revenue for comparison
            # Calculate YTD revenue for comparison
            Action(name="CaV2CalculateYtdRevenue", kwargs={
                "year": "2024"
            }),

            # Log payment processing completion
            # Log payment processing completion
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN4601",
                "task_name": "Payment_Processing_Analysis",
                "status": "success"
            }),
        ],
        outputs=["2373.00"]  # Total payment amount from invoice INV026
    ),

    Task(
        annotator="variation_2",
        user_id="task47",
        instruction=(
            "Handle strategic cash flow and investment planning on January 31, 2025. Evaluate collection efficiency by analyzing payment behavior for publishers PUB001 and PUB002. Calculate profitability for projects PROJ001, PROJ002, PROJ003, and PROJ004 to assess revenue streams. Create the database scheduler run RUN3217 for Strategic_Cash_Flow_Investment_Planning and ensure it has a success status."
        ),
        actions=[
            # Get payment behavior for PUB001
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),

            # Get payment behavior for PUB002
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB002"
            }),

            # Calculate profitability for PROJ001
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),

            # Calculate profitability for PROJ002
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ002"
            }),

            # Calculate profitability for PROJ003
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ003"
            }),

            # Calculate profitability for PROJ004
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ004"
            }),

            # Log strategic cash flow investment planning completion
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3217",
                "task_name": "Strategic_Cash_Flow_Investment_Planning",
                "status": "success"
            }),
        ],
        outputs=["success"],  # Scheduler run status
    ),

    Task(
        annotator="variation_2",
        user_id="task48",
        instruction=(
            "Handle the payment processing for invoice INV012 from Aurora Academic Press on October 1, 2024 at 10:30 AM. Ensure complete payment processing with proper audit trail AUD648, and conduct strategic client relationship analysis. This includes assessing payment behavior, reviewing the active project portfolio, analyzing profitability of their primary project PROJ003, and evaluating the impact on current year 2024 YTD revenue to support ongoing account management decisions. Document the completion with scheduler run RUN4801 for Payment_Processing_Analysis, ensuring a success status."
        ),
        actions=[
            # Get invoice INV012 details
            Action(name="CaV2GetInvoiceById", kwargs={
                "invoice_id": "INV012"
            }),

            # Find Aurora Academic Press
            Action(name="CaV2FindPublisherByName", kwargs={
                "publisher_name": "Aurora Academic Press"
            }),

            # Update payment status
            Action(name="CaV2UpdateInvoicePayment", kwargs={
                "invoice_id": "INV012",
                "paid_at": "2024-10-01T10:30:00Z"
            }),

            # Create payment audit AUD648
            Action(name="CaV2CreateInvoiceAuditEntry", kwargs={
                "audit_id": "AUD648",
                "invoice_id": "INV012",
                "event_type": "payment_received",
                "event_timestamp": "2024-10-01T10:30:00Z",
                "notes": "AUD648_payment_received_INV012"
            }),

            # Get payment behavior for PUB002
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB002"
            }),

            # Get active projects for PUB002
            Action(name="CaV2GetProjectsByPublisher", kwargs={
                "publisher_id": "PUB002",
                "active_only": True
            }),

            # Calculate profitability for main project PROJ003
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ003"
            }),

            # Calculate current year YTD revenue for comparison
            Action(name="CaV2CalculateYtdRevenue", kwargs={
                "year": "2024"
            }),

            # Log payment processing completion
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN4801",
                "task_name": "Payment_Processing_Analysis",
                "status": "success"
            }),
        ],
        outputs=["474.60"]  # Total payment amount from invoice INV012
    ),

    Task(
        annotator="variation_2",
        user_id="task49",
        instruction=(
            "Handle comprehensive business performance and analytics on February 2, 2024. Ensure you calculate hours worked for projects PROJ001, PROJ002, PROJ003, and PROJ004 from January 1-February 2, 2024. Determine profitability for all four projects to evaluate performance metrics. Assess payment behavior for publishers PUB001, PUB002, and PUB003 to analyze revenue impact. Review pipeline opportunities and create database scheduler run RUN3219 for Comprehensive_Business_Performance_Analytics with success status."
        ),
        actions=[
            # Calculate hours worked for PROJ001
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2024-01-01",
                "end_date": "2024-02-02",
                "project_ids": ["PROJ001"]
            }),

            # Calculate hours worked for PROJ002
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2024-01-01",
                "end_date": "2024-02-02",
                "project_ids": ["PROJ002"]
            }),

            # Calculate hours worked for PROJ003
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2024-01-01",
                "end_date": "2024-02-02",
                "project_ids": ["PROJ003"]
            }),

            # Calculate hours worked for PROJ004
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2024-01-01",
                "end_date": "2024-02-02",
                "project_ids": ["PROJ004"]
            }),

            # Get payment behavior for PUB001
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),

            # Get payment behavior for PUB002
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB002"
            }),

            # Get payment behavior for PUB003
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB003"
            }),

            # Calculate profitability for PROJ001
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),

            # Calculate profitability for PROJ002
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ002"
            }),

            # Calculate profitability for PROJ003
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ003"
            }),

            # Calculate profitability for PROJ004
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ004"
            }),

            # Get pipeline opportunities
            Action(name="CaV2GetPipelineOpportunities", kwargs={}),

            # Log comprehensive business performance analytics completion
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3219",
                "task_name": "Comprehensive_Business_Performance_Analytics",
                "status": "success"
            }),
        ],
        outputs=["success"],  # Scheduler run status
    ),

    Task(
        annotator="variation_2",
        user_id="task50",
        instruction=(
            "Coordinate comprehensive market intelligence and operational optimization on April 10, 2025. Examine payment behavior for publishers PUB001, PUB002, PUB003, and PUB004 to evaluate market positioning and collection dynamics. Assess profitability for projects PROJ002, PROJ003, PROJ004, PROJ005, and PROJ006 to identify strategic value creation opportunities. Determine hours worked for projects PROJ002, PROJ003, and PROJ004 from March 20-April 10, 2025 for resource allocation analysis. Establish database scheduler run RUN3050 for Market_Intelligence_Operational_Optimization with success status."
        ),
        actions=[
            # Get payment behavior for PUB001
            # Get payment behavior for PUB001
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),

            # Get payment behavior for PUB002
            # Get payment behavior for PUB002
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB002"
            }),

            # Get payment behavior for PUB003
            # Get payment behavior for PUB003
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB003"
            }),

            # Get payment behavior for PUB004
            # Get payment behavior for PUB004
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB004"
            }),

            # Calculate profitability for PROJ002
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ002"
            }),

            # Calculate profitability for PROJ003
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ003"
            }),

            # Calculate profitability for PROJ004
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ004"
            }),

            # Calculate profitability for PROJ005
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ005"
            }),

            # Calculate profitability for PROJ006
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ006"
            }),

            # Calculate hours worked for all analyzed projects
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-03-20",
                "end_date": "2025-04-10",
                "project_ids": ["PROJ002", "PROJ003", "PROJ004"]
            }),

            # Log market intelligence operational optimization completion
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3050",
                "task_name": "Market_Intelligence_Operational_Optimization",
                "status": "success"
            }),
        ],
        outputs=["success"],  # Scheduler run status
    ),

    Task(
        annotator="variation_2",
        user_id="task51",
        instruction=(
            "Handle optimization of advanced publisher portfolio and revenue strategies on February 4, 2025. Analyze payment behavior for publishers PUB001, PUB002, PUB003, and PUB004 to determine collection efficiency. Calculate profitability for projects PROJ001, PROJ002, PROJ003, PROJ004, and PROJ005 to assess revenue distribution. Review pipeline opportunities and compute YTD revenue for strategic planning. Create database scheduler run RUN3221 for Advanced_Publisher_Portfolio_Optimization with success status."
        ),
                actions=[
            # Get payment behavior for PUB001
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),

            # Get payment behavior for PUB002
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB002"
            }),

            # Get payment behavior for PUB003
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB003"
            }),

            # Get payment behavior for PUB004
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB004"
            }),

            # Calculate profitability for PROJ001
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),

            # Calculate profitability for PROJ002
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ002"
            }),

            # Calculate profitability for PROJ003
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ003"
            }),

            # Calculate profitability for PROJ004
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ004"
            }),

            # Calculate profitability for PROJ005
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ005"
            }),

            # Get pipeline opportunities
            Action(name="CaV2GetPipelineOpportunities", kwargs={}),

            # Calculate YTD revenue for strategic planning
            Action(name="CaV2CalculateYtdRevenue", kwargs={
                "year": "2025"
            }),

            # Log advanced publisher portfolio optimization completion
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3221",
                "task_name": "Advanced_Publisher_Portfolio_Optimization",
                "status": "success"
            }),
        ],
        outputs=["success"],  # Scheduler run status
    ),

    Task(
        annotator="variation_2",
        user_id="task52",
        instruction=(
            "Coordinate implementation of comprehensive time tracking and resource management on February 5, 2025. Calculate hours worked for projects PROJ001, PROJ002, and PROJ003 from January 1-February 5, 2025. Analyze payment behavior for publishers PUB001 and PUB002 to understand collection patterns. Calculate profitability for projects PROJ001, PROJ002, and PROJ003 to evaluate resource efficiency. Review pipeline opportunities and establish database scheduler run RUN3222 for Comprehensive_Time_Tracking_Resource_Management with success status."
        ),
        actions=[
            # Calculate hours worked for PROJ001
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-01-01",
                "end_date": "2025-02-05",
                "project_ids": ["PROJ001"]
            }),

            # Calculate hours worked for PROJ002
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-01-01",
                "end_date": "2025-02-05",
                "project_ids": ["PROJ002"]
            }),

            # Calculate hours worked for PROJ003
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-01-01",
                "end_date": "2025-02-05",
                "project_ids": ["PROJ003"]
            }),

            # Get payment behavior for PUB001
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),

            # Get payment behavior for PUB002
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB002"
            }),

            # Calculate profitability for PROJ001
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),

            # Calculate profitability for PROJ002
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ002"
            }),

            # Calculate profitability for PROJ003
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ003"
            }),

            # Get pipeline opportunities
            Action(name="CaV2GetPipelineOpportunities", kwargs={}),

            # Log comprehensive time tracking resource management completion
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3222",
                "task_name": "Comprehensive_Time_Tracking_Resource_Management",
                "status": "success"
            }),
        ],
        outputs=["success"],  # Scheduler run status
    ),

    Task(
        annotator="variation_2",
        user_id="task53",
        instruction=(
            "Handle the payment processing for invoice INV023 from Aurora Academic Press on February 6, 2024, at 2:30 PM. Ensure the full processing of the payment with an accurate audit trail AUD653 and perform an in-depth client relationship analysis, which includes assessing payment behavior, reviewing active project portfolios, analyzing the profitability of their main project PROJ009, and evaluating the current year 2024 YTD revenue impact to inform ongoing account management strategies. Finalize documentation by executing scheduler run RUN5301 for Payment_Processing_Analysis, ensuring it concludes with a success status."
        ),
                actions=[
            # Get invoice INV023 details
            Action(name="CaV2GetInvoiceById", kwargs={
                "invoice_id": "INV023"
            }),

            # Find Aurora Academic Press
            Action(name="CaV2FindPublisherByName", kwargs={
                "publisher_name": "Aurora Academic Press"
            }),

            # Update payment status
            Action(name="CaV2UpdateInvoicePayment", kwargs={
                "invoice_id": "INV023",
                "paid_at": "2024-02-06T14:30:00Z"
            }),

            # Create payment audit AUD653
            Action(name="CaV2CreateInvoiceAuditEntry", kwargs={
                "audit_id": "AUD653",
                "invoice_id": "INV023",
                "event_type": "payment_received",
                "event_timestamp": "2024-02-06T14:30:00Z",
                "notes": "AUD653_payment_received_INV023"
            }),

            # Get payment behavior for PUB002
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB002"
            }),

            # Get active projects for PUB002
            Action(name="CaV2GetProjectsByPublisher", kwargs={
                "publisher_id": "PUB002",
                "active_only": True
            }),

            # Calculate profitability for main project PROJ009
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ009"
            }),

            # Calculate current year YTD revenue for comparison
            Action(name="CaV2CalculateYtdRevenue", kwargs={
                "year": "2024"
            }),

            # Log payment processing completion
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN5301",
                "task_name": "Payment_Processing_Analysis",
                "status": "success"
            }),

        ],
        outputs=["success"],
    ),

    Task(
        annotator="variation_2",
        user_id="task54",
        instruction=(
            "Coordinate the collection of in-depth business intelligence and performance data on February 7, 2025. Assemble resource utilization information for projects PROJ001, PROJ002, and PROJ003 covering the period from January 1-February 7, 2025, to facilitate capacity planning analysis. Gather payment behavior data for publishers PUB001, PUB002, and PUB003 to enhance accounts receivable management optimization. Compile performance metrics data for all three projects to aid in strategic decision-making analysis. Examine pipeline opportunities and accrue YTD revenue data to support strategic planning. Set up database scheduler run RUN3224 for Advanced_Business_Intelligence_Performance_Analytics, ensuring its success status."
        ),
        actions=[
            # Calculate hours worked for PROJ001
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-01-01",
                "end_date": "2025-02-07",
                "project_ids": ["PROJ001"]
            }),

            # Calculate hours worked for PROJ002
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-01-01",
                "end_date": "2025-02-07",
                "project_ids": ["PROJ002"]
            }),

            # Calculate hours worked for PROJ003
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-01-01",
                "end_date": "2025-02-07",
                "project_ids": ["PROJ003"]
            }),

            # Get payment behavior for PUB001
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),

            # Get payment behavior for PUB002
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB002"
            }),

            # Get payment behavior for PUB003
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB003"
            }),

            # Calculate profitability for PROJ001
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),

            # Calculate profitability for PROJ002
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ002"
            }),

            # Calculate profitability for PROJ003
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ003"
            }),

            # Get pipeline opportunities
            Action(name="CaV2GetPipelineOpportunities", kwargs={}),

            # Calculate YTD revenue for strategic planning
            Action(name="CaV2CalculateYtdRevenue", kwargs={
                "year": "2025"
            }),

            # Log advanced business intelligence performance analytics completion
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3224",
                "task_name": "Advanced_Business_Intelligence_Performance_Analytics",
                "status": "success"
            }),
        ],
        outputs=["success"],  # Scheduler run status
    ),#

    Task(
        annotator="variation_2",
        user_id="task55",
        instruction=(
            "Handle an extensive strategic market intelligence and operational excellence assessment on December 20, 2024. Analyze payment behavior for publishers PUB001, PUB002, PUB003, PUB004, and PUB005 to assess market positioning and collection strategies. Compute profitability for projects PROJ001, PROJ002, PROJ003, PROJ004, and PROJ005 to explore strategic value optimization potential. Determine hours worked for projects PROJ001, PROJ002, and PROJ003 from December 5-20, 2024 for operational excellence benchmarking. Develop database scheduler run RUN3055 for Strategic_Market_Intelligence_Operational_Excellence scheduled at 3:30 PM with execution at 5:15 PM on December 20, 2024, ensuring success status."
        ),
        actions=[


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB002"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB003"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB004"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB005"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ002"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ003"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ004"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ005"
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2024-12-05",
                "end_date": "2024-12-20",
                "project_ids": ["PROJ001"]
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2024-12-05",
                "end_date": "2024-12-20",
                "project_ids": ["PROJ002"]
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2024-12-05",
                "end_date": "2024-12-20",
                "project_ids": ["PROJ003"]
            }),
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3055",
                "task_name": "Strategic_Market_Intelligence_Operational_Excellence",
                "scheduled_for": "2024-12-20T15:30:00Z",
                "executed_at": "2024-12-20T17:15:00Z",
                "status": "success"
            }),
        ],
        outputs=["success"],  # Scheduler run status
    ),#

    Task(
        annotator="variation_2",
        user_id="task56",
        instruction=(
            "Coordinate a thorough portfolio performance analysis on January 18, 2025, by evaluating payment behavior patterns across publishers PUB001, PUB002, PUB003, PUB004, and PUB005 to discern collection efficiency trends. Judge profitability metrics for projects PROJ001, PROJ002, PROJ003, PROJ004, and PROJ005 to ascertain revenue optimization potential. Quantify resource utilization for PROJ001, PROJ002, and PROJ003 from January 5-18, 2025 to appraise operational efficiency. Finalize the analysis with scheduler run RUN3056 for Strategic_Portfolio_Optimization_Market_Intelligence ensuring success status."
        ),
        actions=[


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB002"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB003"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB004"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB005"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ002"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ003"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ004"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ005"
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-01-05",
                "end_date": "2025-01-18",
                "project_ids": ["PROJ001"]
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-01-05",
                "end_date": "2025-01-18",
                "project_ids": ["PROJ002"]
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-01-05",
                "end_date": "2025-01-18",
                "project_ids": ["PROJ003"]
            }),
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3056",
                "task_name": "Strategic_Portfolio_Optimization_Market_Intelligence",
                "status": "success"
            }),
        ],
        outputs=["success"],  # Scheduler run status
    ),#

    Task(
        annotator="variation_2",
        user_id="task57",
        instruction=(
            "Handle comprehensive strategic business intelligence and competitive performance analysis on February 22, 2025. Evaluate payment behavior for publishers PUB001, PUB002, PUB003, PUB004, and PUB005 to assess market positioning and collection strategies. Determine profitability for projects PROJ001, PROJ002, PROJ003, PROJ004, and PROJ005 to evaluate strategic value creation and competitive advantage. Calculate hours worked for projects PROJ001, PROJ002, and PROJ003 from February 10-22, 2025 for operational excellence evaluation. Create database scheduler run RUN3057 for Strategic_Business_Intelligence_Competitive_Performance scheduled 2:15 PM executed 4:00 PM February 22, 2025 with success status."
        ),
        actions=[


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB002"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB003"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB004"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB005"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ002"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ003"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ004"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ005"
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-02-10",
                "end_date": "2025-02-22",
                "project_ids": ["PROJ001"]
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-02-10",
                "end_date": "2025-02-22",
                "project_ids": ["PROJ002"]
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-02-10",
                "end_date": "2025-02-22",
                "project_ids": ["PROJ003"]
            }),
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3057",
                "task_name": "Strategic_Business_Intelligence_Competitive_Performance",
                "scheduled_for": "2025-02-22T14:15:00Z",
                "executed_at": "2025-02-22T16:00:00Z",
                "status": "success"
            }),
        ],
        outputs=["success"],  # Scheduler run status
    ),#

    Task(
        annotator="variation_2",
        user_id="task58",
        instruction=(
            "Coordinate comprehensive publisher analysis and revenue strategy on February 11, 2025. Analyze payment behavior for publishers PUB001, PUB002, and PUB003 to assess collection efficiency and cash flow patterns. Determine profitability for projects PROJ001, PROJ002, and PROJ003 to evaluate revenue distribution and performance metrics. Calculate hours worked for projects PROJ001 and PROJ002 from January 1-February 11, 2025 to assess resource utilization. Create database scheduler run RUN3228 for Comprehensive_Publisher_Analysis_Revenue_Strategy with success status."
        ),
        actions=[


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB002"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB003"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ002"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ003"
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-01-01",
                "end_date": "2025-02-11",
                "project_ids": ["PROJ001"]
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-01-01",
                "end_date": "2025-02-11",
                "project_ids": ["PROJ002"]
            }),
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3228",
                "task_name": "Comprehensive_Publisher_Analysis_Revenue_Strategy",
                "status": "success"
            }),
        ],
        outputs=["success"],  # Scheduler run status
    ),

    Task(
        annotator="variation_2",
        user_id="task59",
        instruction=(
            "Handle the development of a comprehensive financial intelligence and tax strategy on February 12, 2024. Evaluate payment behavior for publishers PUB001, PUB002, and PUB003 to understand collection patterns and revenue predictability. Calculate profitability for projects PROJ001, PROJ002, and PROJ003 to assess portfolio performance. Calculate hours worked for projects PROJ001, PROJ002, and PROJ003 from January 15-February 12, 2024 for resource planning. Create database scheduler run RUN3229 for Advanced_Financial_Intelligence_Tax_Strategy with success status."
        ),
        actions=[
            # Get payment behavior for PUB001
            # Get payment behavior for PUB001
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),

            # Get payment behavior for PUB002
            # Get payment behavior for PUB002
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB002"
            }),

            # Get payment behavior for PUB003
            # Get payment behavior for PUB003
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB003"
            }),

            # Calculate profitability for PROJ001
            # Calculate profitability for PROJ001
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),

            # Calculate profitability for PROJ002
            # Calculate profitability for PROJ002
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ002"
            }),

            # Calculate profitability for PROJ003
            # Calculate profitability for PROJ003
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ003"
            }),

            # Calculate hours worked for PROJ001
            # Calculate hours worked for PROJ001
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2024-01-15",
                "end_date": "2024-02-12",
                "project_ids": ["PROJ001"]
            }),

            # Calculate hours worked for PROJ002
            # Calculate hours worked for PROJ002
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2024-01-15",
                "end_date": "2024-02-12",
                "project_ids": ["PROJ002"]
            }),

            # Calculate hours worked for PROJ003
            # Calculate hours worked for PROJ003
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2024-01-15",
                "end_date": "2024-02-12",
                "project_ids": ["PROJ003"]
            }),

            # Log advanced financial intelligence tax strategy completion
            # Log advanced financial intelligence tax strategy completion
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3229",
                "task_name": "Advanced_Financial_Intelligence_Tax_Strategy",
                "status": "success"
            }),
        ],
        outputs=["success"],
    ),

    Task(
        annotator="variation_2",
        user_id="task60",
        instruction=(
            "Coordinate the optimization of strategic business performance and resource allocation on February 13, 2025 by conducting a comprehensive workforce productivity analysis for PROJ001, PROJ002, and PROJ003 over the recent completed period from January 1-February 13, 2025. Assess collection efficiency through payment behavior evaluation for key publishers PUB001 and PUB002, and conduct profitability analysis across all three projects to facilitate strategic decision-making. Conclude the analysis with scheduler run RUN3230 for Strategic_Business_Performance_Resource_Optimization."
        ),
        actions=[
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-01-01",
                "end_date": "2025-02-13",
                "project_ids": ["PROJ001", "PROJ002", "PROJ003"]
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB002"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ002"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ003"
            }),
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3230",
                "task_name": "Strategic_Business_Performance_Resource_Optimization",
                "status": "success"
            }),
        ],
        outputs=["success"],  # Scheduler run status
    ),#

    Task(
        annotator="variation_2",
        user_id="task61",
        instruction=(
            "Handle the payment process for invoice INV011 from Midwest Education House on February 14, 2024, at 11:45 AM. Ensure the payment is fully processed with a complete audit trail AUD661 and carry out an analysis of the client's strategic relationship, including an assessment of payment behavior, a review of the active project portfolio, a profitability analysis of their key project PROJ010, and an evaluation of the current year 2024 YTD revenue impact to support ongoing account management decisions. Record the completion using scheduler run RUN6101 for Payment_Processing_Analysis with success status."
        ),
        actions=[


            Action(name="CaV2GetInvoiceById", kwargs={
                "invoice_id": "INV011"
            }),


            Action(name="CaV2FindPublisherByName", kwargs={
                "publisher_name": "Midwest Education House"
            }),


            Action(name="CaV2UpdateInvoicePayment", kwargs={
                "invoice_id": "INV011",
                "paid_at": "2024-02-14T11:45:00Z"
            }),


            Action(name="CaV2CreateInvoiceAuditEntry", kwargs={
                "audit_id": "AUD661",
                "invoice_id": "INV011",
                "event_type": "payment_received",
                "event_timestamp": "2024-02-14T11:45:00Z",
                "notes": "AUD661_payment_received_INV011"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB005"
            }),


            Action(name="CaV2GetProjectsByPublisher", kwargs={
                "publisher_id": "PUB005",
                "active_only": True
            }),


            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ010"
            }),

            Action(name="CaV2CalculateYtdRevenue", kwargs={
                "year": "2024"
            }),


            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN6101",
                "task_name": "Payment_Processing_Analysis",
                "status": "success"
            }),
        ],
        outputs=["success"],
    ),#

    Task(
        annotator="variation_2",
        user_id="task62",
        instruction=(
            "Coordinate the implementation of strategic time management and performance analytics on February 15, 2025. Calculate the hours worked for projects PROJ001, PROJ002, and PROJ003 from January 1-February 15, 2025. Analyze the payment behavior for publishers PUB001, PUB002, and PUB003 to evaluate collection efficiency. Calculate the profitability of all three projects to assess performance metrics. Create a database scheduler run RUN3232 for Strategic_Time_Management_Performance_Analytics with success status."
        ),
        actions=[
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-01-01",
                "end_date": "2025-02-15",
                "project_ids": ["PROJ001"]
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-01-01",
                "end_date": "2025-02-15",
                "project_ids": ["PROJ002"]
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-01-01",
                "end_date": "2025-02-15",
                "project_ids": ["PROJ003"]
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB002"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB003"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ002"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ003"
            }),
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3232",
                "task_name": "Strategic_Time_Management_Performance_Analytics",
                "status": "success"
            }),
        ],
        outputs=["success"],  # Scheduler run status
    ),#

    Task(
        annotator="variation_2",
        user_id="task63",
        instruction=(
            "Handle the development of a comprehensive publisher portfolio and revenue strategy on February 16, 2025. Analyze payment behavior for publishers PUB001, PUB002, PUB003, PUB004, and PUB005 to assess collection patterns. Calculate profitability for projects PROJ001, PROJ002, PROJ003, PROJ004, and PROJ005 to evaluate revenue streams. Determine hours worked for projects PROJ001, PROJ002, and PROJ003 from January 1-February 16, 2025 to assess resource utilization. Create database scheduler run RUN3233 for Comprehensive_Publisher_Portfolio_Revenue_Strategy with success status."
        ),
        actions=[


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB002"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB003"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB004"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB005"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ002"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ003"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ004"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ005"
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-01-01",
                "end_date": "2025-02-16",
                "project_ids": ["PROJ001"]
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-01-01",
                "end_date": "2025-02-16",
                "project_ids": ["PROJ002"]
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-01-01",
                "end_date": "2025-02-16",
                "project_ids": ["PROJ003"]
            }),
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3233",
                "task_name": "Comprehensive_Publisher_Portfolio_Revenue_Strategy",
                "status": "success"
            }),
        ],
        outputs=["success"],  # Scheduler run status
    ),

    Task(
        annotator="variation_2",
        user_id="task64",
        instruction=(
            "Coordinate the implementation of advanced expense management and financial intelligence on February 17, 2024. Evaluate expense patterns across OFFICE_SUPPLIES, TRAVEL_EXPENSE, and ADVERTISING categories from January 1-February 17, 2024 for cost optimization insights. Assess tax implications for 2024 and evaluate current year 2024 YTD revenue performance for strategic financial planning. Analyze payment behavior patterns for publishers PUB001, PUB002, and PUB003 to optimize cash flow management. Assess profitability metrics for projects PROJ001, PROJ002, and PROJ003 to inform resource allocation decisions. Create database scheduler run RUN3234 for Advanced_Expense_Management_Financial_Intelligence with success status."
        ),
        actions=[
            # Calculate expense summary for office supplies
            # Calculate expense summary for office supplies
            Action(name="CaV2CalculateExpenseSummary", kwargs={
                "category_filter": ["OFFICE_SUPPLIES"],
                "start_date": "2024-01-01",
                "end_date": "2024-02-17"
            }),

            # Calculate expense summary for travel
            # Calculate expense summary for travel
            Action(name="CaV2CalculateExpenseSummary", kwargs={
                "category_filter": ["TRAVEL_EXPENSE"],
                "start_date": "2024-01-01",
                "end_date": "2024-02-17"
            }),

            # Calculate expense summary for marketing
            # Calculate expense summary for marketing
            Action(name="CaV2CalculateExpenseSummary", kwargs={
                "category_filter": ["ADVERTISING"],
                "start_date": "2024-01-01",
                "end_date": "2024-02-17"
            }),

            # Get current tax rate for 2024
            # Get current tax rate for 2024
            Action(name="CaV2GetTaxRateByYear", kwargs={
                "year": "2024"
            }),

            # Calculate current year YTD revenue for financial planning
            # Calculate current year YTD revenue for financial planning
            Action(name="CaV2CalculateYtdRevenue", kwargs={
                "year": "2024"
            }),

            # Get payment behavior for PUB001
            # Get payment behavior for PUB001
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),

            # Get payment behavior for PUB002
            # Get payment behavior for PUB002
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB002"
            }),

            # Get payment behavior for PUB003
            # Get payment behavior for PUB003
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB003"
            }),

            # Calculate profitability for PROJ001
            # Calculate profitability for PROJ001
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),

            # Calculate profitability for PROJ002
            # Calculate profitability for PROJ002
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ002"
            }),

            # Calculate profitability for PROJ003
            # Calculate profitability for PROJ003
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ003"
            }),

            # Log advanced expense management financial intelligence completion
            # Log advanced expense management financial intelligence completion
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3234",
                "task_name": "Advanced_Expense_Management_Financial_Intelligence",
                "status": "success"
            }),
        ],
        outputs=["success"],  # Scheduler run status
    ),#
#
    Task(
        annotator="variation_2",
        user_id="task65",
        instruction=(
            "Handle optimization of strategic business performance and resource allocation on February 18, 2025. Calculate hours worked for projects PROJ001, PROJ002, and PROJ003 from January 1-February 18, 2025. Analyze payment behavior for publishers PUB001 and PUB002 to assess collection efficiency. Compute profitability for all three projects to evaluate performance metrics. Create database scheduler run RUN3235 for Strategic_Business_Performance_Resource_Optimization with success status."
        ),
        actions=[
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-01-01",
                "end_date": "2025-02-18",
                "project_ids": ["PROJ001"]
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-01-01",
                "end_date": "2025-02-18",
                "project_ids": ["PROJ002"]
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-01-01",
                "end_date": "2025-02-18",
                "project_ids": ["PROJ003"]
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB002"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ002"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ003"
            }),
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3235",
                "task_name": "Strategic_Business_Performance_Resource_Optimization",
                "status": "success"
            }),
        ],
        outputs=["success"],  # Scheduler run status
    ),

    Task(
        annotator="variation_2",
        user_id="task66",
        instruction=(
            "Coordinate the processing of payment for invoice INV008 from Summit Educational Publishing on February 19, 2024 at 3:15 PM. Ensure the fully completed payment processing with a proper audit trail AUD666 and conduct a strategic client relationship analysis including a payment behavior assessment, an active project portfolio review, a profitability analysis of their primary project PROJ005, and a current year 2024 YTD revenue impact assessment to support ongoing account management decisions. Document completion with scheduler run RUN6601 for Payment_Processing_Analysis with success status."
        ),
        actions=[
            # Get invoice INV008 details
            # Get invoice INV008 details
            Action(name="CaV2GetInvoiceById", kwargs={
                "invoice_id": "INV008"
            }),

            # Find Summit Educational Publishing
            # Find Summit Educational Publishing
            Action(name="CaV2FindPublisherByName", kwargs={
                "publisher_name": "Summit Educational Publishing"
            }),

            # Update payment status
            # Update payment status
            Action(name="CaV2UpdateInvoicePayment", kwargs={
                "invoice_id": "INV008",
                "paid_at": "2024-02-19T15:15:00Z"
            }),

            # Create payment audit AUD666
            # Create payment audit AUD666
            Action(name="CaV2CreateInvoiceAuditEntry", kwargs={
                "audit_id": "AUD666",
                "invoice_id": "INV008",
                "event_type": "payment_received",
                "event_timestamp": "2024-02-19T15:15:00Z",
                "notes": "AUD666_payment_received_INV008"
            }),

            # Get payment behavior for PUB003
            # Get payment behavior for PUB003
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB003"
            }),

            # Get active projects for PUB003
            # Get active projects for PUB003
            Action(name="CaV2GetProjectsByPublisher", kwargs={
                "publisher_id": "PUB003",
                "active_only": True
            }),

            # Calculate profitability for main project PROJ005
            # Calculate profitability for main project PROJ005
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ005"
            }),

            # Calculate current year YTD revenue for comparison
            # Calculate current year YTD revenue for comparison
            Action(name="CaV2CalculateYtdRevenue", kwargs={
                "year": "2024"
            }),

            # Log payment processing completion
            # Log payment processing completion
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN6601",
                "task_name": "Payment_Processing_Analysis",
                "status": "success"
            }),
        ],
        outputs=["1717.60"]  # Total payment amount from invoice INV008
    ),#

    Task(
        annotator="variation_2",
        user_id="task67",
        instruction=(
            "Handle the task of strategic time management and performance analytics on February 20, 2025. Evaluate resource utilization across projects PROJ001, PROJ002, and PROJ003 from January 1-February 20, 2025 for capacity planning. Assess the collection efficiency patterns for publishers PUB001, PUB002, and PUB003 to optimize accounts receivable management. Evaluate performance metrics for all three projects to inform strategic decision-making. Create database scheduler run RUN3237 for Strategic_Time_Management_Performance_Analytics with success status."
        ),
        actions=[
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-01-01",
                "end_date": "2025-02-20",
                "project_ids": ["PROJ001"]
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-01-01",
                "end_date": "2025-02-20",
                "project_ids": ["PROJ002"]
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-01-01",
                "end_date": "2025-02-20",
                "project_ids": ["PROJ003"]
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB002"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB003"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ002"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ003"
            }),
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3237",
                "task_name": "Strategic_Time_Management_Performance_Analytics",
                "status": "success"
            }),
        ],
        outputs=["success"],  # Scheduler run status
    ),#

    Task(
        annotator="variation_2",
        user_id="task68",
        instruction=(
            "Coordinate the development of a comprehensive publisher portfolio and revenue strategy on February 21, 2025. Analyze payment behavior for publishers PUB001, PUB002, PUB003, PUB004, and PUB005 to assess collection patterns. Calculate profitability for projects PROJ001, PROJ002, PROJ003, PROJ004, and PROJ005 to evaluate revenue streams. Calculate hours worked for projects PROJ001, PROJ002, and PROJ003 from January 1-February 21, 2025 to assess resource utilization. Create database scheduler run RUN3238 for Comprehensive_Publisher_Portfolio_Revenue_Strategy with success status."
        ),
        actions=[


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB002"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB003"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB004"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB005"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ002"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ003"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ004"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ005"
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-01-01",
                "end_date": "2025-02-21",
                "project_ids": ["PROJ001"]
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-01-01",
                "end_date": "2025-02-21",
                "project_ids": ["PROJ002"]
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-01-01",
                "end_date": "2025-02-21",
                "project_ids": ["PROJ003"]
            }),
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3238",
                "task_name": "Comprehensive_Publisher_Portfolio_Revenue_Strategy",
                "status": "success"
            }),
        ],
        outputs=["success"],  # Scheduler run status
    ),#

    Task(
        annotator="variation_2",
        user_id="task69",
        instruction=(
            "Handle advanced financial analytics and tax planning on February 24, 2025. Analyze expense patterns across the categories of office supplies, travel, and marketing from January 1-February 24, 2024. Gather tax rate information for 2024 and assess the year-to-date revenue performance for comprehensive tax planning. Evaluate payment behavior patterns for publishers PUB001, PUB002, and PUB003 to understand cash flow dynamics. Assess profitability metrics for projects PROJ001, PROJ002, and PROJ003 to evaluate revenue quality. Create database scheduler run RUN3239 for Advanced_Financial_Analytics_Tax_Planning with success status."
        ),
        actions=[
            Action(name="CaV2CalculateExpenseSummary", kwargs={
                "category_filter": ["OFFICE_SUPPLIES", "TRAVEL", "MARKETING"],
                "start_date": "2024-01-01",
                "end_date": "2024-02-24"
            }),
            Action(name="CaV2GetTaxRateByYear", kwargs={
                "year": "2024"
            }),
            Action(name="CaV2CalculateYtdRevenue", kwargs={
                "year": "2024"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB002"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB003"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ002"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ003"
            }),
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3239",
                "task_name": "Advanced_Financial_Analytics_Tax_Planning",
                "status": "success"
            }),
        ],
        outputs=["success"],  # Scheduler run status
    ),#

    Task(
        annotator="variation_2",
        user_id="task70",
        instruction=(
            "Coordinate strategic time management and performance analytics on February 25, 2025. Evaluate resource utilization across projects PROJ001, PROJ002, and PROJ003 from January 1-February 25, 2025 for capacity planning. Assess collection efficiency patterns for publishers PUB001, PUB002, and PUB003 to optimize accounts receivable management. Evaluate performance metrics for all three projects to inform strategic decision-making. Create database scheduler run RUN3240 for Strategic_Time_Management_Performance_Analytics with success status."
        ),
        actions=[
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-01-01",
                "end_date": "2025-02-25",
                "project_ids": ["PROJ001"]
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-01-01",
                "end_date": "2025-02-25",
                "project_ids": ["PROJ002"]
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-01-01",
                "end_date": "2025-02-25",
                "project_ids": ["PROJ003"]
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB002"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB003"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ002"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ003"
            }),
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3240",
                "task_name": "Strategic_Time_Management_Performance_Analytics",
                "status": "success"
            }),
        ],
        outputs=["success"],  # Scheduler run status
    ),#

    Task(
        annotator="variation_2",
        user_id="task71",
        instruction=(
            "Handle the creation of a comprehensive publisher portfolio and revenue strategy by February 26, 2025. Analyze payment behaviors for publishers PUB001, PUB002, PUB003, PUB004, and PUB005 to evaluate collection trends. Calculate the profitability for projects PROJ001, PROJ002, PROJ003, PROJ004, and PROJ005 to determine the revenue streams. Calculate hours worked for projects PROJ001, PROJ002, and PROJ003 from January 1-February 26, 2025 to analyze resource usage. Create database scheduler run RUN3241 for Comprehensive_Publisher_Portfolio_Revenue_Strategy ensuring it has a success status."
        ),
        actions=[


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB002"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB003"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB004"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB005"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ002"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ003"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ004"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ005"
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-01-01",
                "end_date": "2025-02-26",
                "project_ids": ["PROJ001"]
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-01-01",
                "end_date": "2025-02-26",
                "project_ids": ["PROJ002"]
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-01-01",
                "end_date": "2025-02-26",
                "project_ids": ["PROJ003"]
            }),
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3241",
                "task_name": "Comprehensive_Publisher_Portfolio_Revenue_Strategy",
                "status": "success"
            }),
        ],
        outputs=["success"],  # Scheduler run status
    ),#

    Task(
        annotator="variation_2",
        user_id="task72",
        instruction=(
            "Coordinate the implementation of advanced expense management and financial intelligence on February 27, 2025. Calculate expense summaries for office_supplies, travel, marketing, and equipment categories from January 1-February 27, 2024 to pinpoint cost optimization opportunities. Retrieve the tax rate for 2024 and calculate YTD revenue for 2025 to assess tax obligations and strategic financial planning. Acquire payment behavior data for publishers PUB001, PUB002, PUB003, and PUB004 to examine cash flow patterns. Calculate profitability metrics for projects PROJ001, PROJ002, PROJ003, and PROJ004 to assess resource allocation effectiveness. Create database scheduler run RUN3242 for Advanced_Expense_Management_Financial_Intelligence with a success status."
        ),
        actions=[
            Action(name="CaV2CalculateExpenseSummary", kwargs={
                "category_filter": ["office_supplies"],
                "start_date": "2024-01-01",
                "end_date": "2024-02-27"
            }),
            Action(name="CaV2CalculateExpenseSummary", kwargs={
                "category_filter": ["travel"],
                "start_date": "2024-01-01",
                "end_date": "2024-02-27"
            }),
            Action(name="CaV2CalculateExpenseSummary", kwargs={
                "category_filter": ["marketing"],
                "start_date": "2024-01-01",
                "end_date": "2024-02-27"
            }),
            Action(name="CaV2CalculateExpenseSummary", kwargs={
                "category_filter": ["equipment"],
                "start_date": "2024-01-01",
                "end_date": "2024-02-27"
            }),
            Action(name="CaV2GetTaxRateByYear", kwargs={
                "year": "2024"
            }),
            Action(name="CaV2CalculateYtdRevenue", kwargs={
                "year": "2025"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB002"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB003"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB004"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ002"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ003"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ004"
            }),
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3242",
                "task_name": "Advanced_Expense_Management_Financial_Intelligence",
                "status": "success"
            }),
        ],
        outputs=["success"],  # Scheduler run status
    ),#

    Task(
        annotator="variation_2",
        user_id="task73",
        instruction=(
            "Handle the optimization of strategic business performance and resource allocation by February 28, 2025. Make sure to calculate the hours worked for projects PROJ001, PROJ002, and PROJ003 from January 1-February 28, 2025. Analyze the payment behavior for publishers PUB001 and PUB002 to evaluate collection efficiency. Determine the profitability for all three projects to assess performance metrics. Create a database scheduler run RUN3243 for Strategic_Business_Performance_Resource_Optimization with a success status."
        ),
        actions=[
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-01-01",
                "end_date": "2025-02-28",
                "project_ids": ["PROJ001"]
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-01-01",
                "end_date": "2025-02-28",
                "project_ids": ["PROJ002"]
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-01-01",
                "end_date": "2025-02-28",
                "project_ids": ["PROJ003"]
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB002"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ002"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ003"
            }),
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3243",
                "task_name": "Strategic_Business_Performance_Resource_Optimization",
                "status": "success"
            }),
        ],
        outputs=["success"],  # Scheduler run status
    ),#

    Task(
        annotator="variation_2",
        user_id="task74",
        instruction=(
            "Coordinate the processing of payment for invoice INV009 from Northern Star Publishers on March 1, 2025, at 4:15 PM. Ensure the payment processing is complete with a proper audit trail AUD616 and carry out a strategic client relationship analysis, which includes a payment behavior assessment, active project portfolio review, profitability analysis of their primary project PROJ001, and an assessment of the current year 2025 YTD revenue impact to support ongoing account management decisions. Document completion with scheduler run RUN7401 for Account_Reconciliation_Analysis with a success status."
        ),
        actions=[


            Action(name="CaV2GetInvoiceById", kwargs={
                "invoice_id": "INV009"
            }),


            Action(name="CaV2FindPublisherByName", kwargs={
                "publisher_name": "Northern Star Publishers"
            }),


            Action(name="CaV2UpdateInvoicePayment", kwargs={
                "invoice_id": "INV009",
                "paid_at": "2025-03-01T16:15:00Z"
            }),


            Action(name="CaV2CreateInvoiceAuditEntry", kwargs={
                "audit_id": "AUD616",
                "invoice_id": "INV009",
                "event_type": "payment_received",
                "event_timestamp": "2025-03-01T16:15:00Z",
                "notes": "AUD616_payment_received_INV009"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),


            Action(name="CaV2GetProjectsByPublisher", kwargs={
                "publisher_id": "PUB001",
                "active_only": True
            }),


            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),
            Action(name="CaV2CalculateYtdRevenue", kwargs={
                "year": "2025"
            }),


            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN7401",
                "task_name": "Account_Reconciliation_Analysis",
                "status": "success"
            }),
        ],
        outputs=["691.56"],  # Total payment amount from invoice INV009
    ),#

    Task(
        annotator="variation_2",
        user_id="task75",
        instruction=(
            "Handle advanced financial analytics and tax planning on March 2, 2025. Calculate expense summaries for office_supplies, travel, and marketing categories from January 1-March 2, 2024 to identify cost optimization opportunities. Obtain the tax rate for 2024 and calculate YTD revenue for 2025 to assess tax implications and strategic financial planning. Acquire payment behavior data for publishers PUB001, PUB002, and PUB003 to evaluate cash flow patterns. Compute profitability metrics for projects PROJ001, PROJ002, and PROJ003 to assess resource allocation effectiveness. Create database scheduler run RUN3245 for Advanced_Financial_Analytics_Tax_Planning with success status."
        ),
        actions=[
            Action(name="CaV2CalculateExpenseSummary", kwargs={
                "category_filter": ["office_supplies"],
                "start_date": "2024-01-01",
                "end_date": "2024-03-02"
            }),
            Action(name="CaV2CalculateExpenseSummary", kwargs={
                "category_filter": ["travel"],
                "start_date": "2024-01-01",
                "end_date": "2024-03-02"
            }),
            Action(name="CaV2CalculateExpenseSummary", kwargs={
                "category_filter": ["marketing"],
                "start_date": "2024-01-01",
                "end_date": "2024-03-02"
            }),
            Action(name="CaV2GetTaxRateByYear", kwargs={
                "year": "2024"
            }),
            Action(name="CaV2CalculateYtdRevenue", kwargs={
                "year": "2025"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB002"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB003"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ002"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ003"
            }),
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3245",
                "task_name": "Advanced_Financial_Analytics_Tax_Planning",
                "status": "success"
            }),
        ],
        outputs=["success"],  # Scheduler run status
    ),#

    Task(
        annotator="variation_2",
        user_id="task76",
        instruction=(
            "Coordinate strategic time management and performance analytics on March 3, 2025. Determine hours worked for projects PROJ001, PROJ002, and PROJ003 from January 1-March 3, 2024 to evaluate resource utilization for capacity planning. Gather payment behavior data for publishers PUB001, PUB002, and PUB003 to assess collection efficiency patterns. Assess profitability metrics for all three projects to evaluate performance and inform strategic decision-making. Create database scheduler run RUN3246 for Strategic_Time_Management_Performance_Analytics with success status."
        ),
        actions=[
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2024-01-01",
                "end_date": "2024-03-03",
                "project_ids": ["PROJ001"]
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2024-01-01",
                "end_date": "2024-03-03",
                "project_ids": ["PROJ002"]
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2024-01-01",
                "end_date": "2024-03-03",
                "project_ids": ["PROJ003"]
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB002"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB003"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ002"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ003"
            }),
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3246",
                "task_name": "Strategic_Time_Management_Performance_Analytics",
                "status": "success"
            }),
        ],
        outputs=["success"],  # Scheduler run status
    ),#

    Task(
        annotator="variation_2",
        user_id="task77",
        instruction=(
            "Coordinate the development of a detailed publisher portfolio and revenue strategy on March 4, 2025. Analyze payment behavior for publishers PUB001, PUB002, PUB003, PUB004, and PUB005 to evaluate collection patterns. Calculate profitability for projects PROJ001, PROJ002, PROJ003, PROJ004, and PROJ005 to examine revenue streams. Calculate hours worked for projects PROJ001, PROJ002, and PROJ003 from January 1-March 4, 2024 to evaluate resource utilization. Create database scheduler run RUN3247 for Comprehensive_Publisher_Portfolio_Revenue_Strategy with success status."
        ),
        actions=[


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB002"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB003"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB004"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB005"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ002"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ003"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ004"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ005"
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2024-01-01",
                "end_date": "2024-03-04",
                "project_ids": ["PROJ001"]
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2024-01-01",
                "end_date": "2024-03-04",
                "project_ids": ["PROJ002"]
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2024-01-01",
                "end_date": "2024-03-04",
                "project_ids": ["PROJ003"]
            }),
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3247",
                "task_name": "Comprehensive_Publisher_Portfolio_Revenue_Strategy",
                "status": "success"
            }),
        ],
        outputs=["success"],  # Scheduler run status
    ),

    Task(
        annotator="variation_2",
        user_id="task78",
        instruction=(
            "Handle the implementation of advanced expense management and financial intelligence on March 5, 2024. Assess payment behavior for publishers PUB001 and PUB002 to evaluate collection patterns and revenue predictability. Determine profitability for projects PROJ001 and PROJ002 to analyze portfolio performance. Compute hours worked for projects PROJ001 and PROJ002 from January 15-March 5, 2024 for resource planning. Create database scheduler run RUN3248 for Advanced_Expense_Management_Financial_Intelligence with success status."
        ),
        actions=[
            # Get payment behavior for PUB001
            # Get payment behavior for PUB001
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),

            # Get payment behavior for PUB002
            # Get payment behavior for PUB002
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB002"
            }),

            # Calculate profitability for PROJ001
            # Calculate profitability for PROJ001
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),

            # Calculate profitability for PROJ002
            # Calculate profitability for PROJ002
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ002"
            }),

            # Calculate hours worked for all analyzed projects
            # Calculate hours worked for all analyzed projects
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2024-01-15",
                "end_date": "2024-03-05",
                "project_ids": ["PROJ001", "PROJ002"]
            }),

            # Log advanced expense management financial intelligence completion
            # Log advanced expense management financial intelligence completion
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3248",
                "task_name": "Advanced_Expense_Management_Financial_Intelligence",
                "status": "success"
            }),
        ],
        outputs=["success"],
    ),

    Task(
        annotator="variation_2",
        user_id="task79",
        instruction=(
            "Handle the optimization of strategic business performance and resource allocation on March 6, 2025. Evaluate resource utilization across projects PROJ001, PROJ002, and PROJ003 from January 1-March 6, 2025, to aid in capacity planning. Assess collection efficiency patterns for publishers PUB001 and PUB002 in order to enhance accounts receivable management. Evaluate performance metrics for all three projects to support strategic decision-making. Create database scheduler run RUN3249 for Strategic_Business_Performance_Resource_Optimization with success status."
        ),
        actions=[
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-01-01",
                "end_date": "2025-03-06",
                "project_ids": ["PROJ001"]
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-01-01",
                "end_date": "2025-03-06",
                "project_ids": ["PROJ002"]
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-01-01",
                "end_date": "2025-03-06",
                "project_ids": ["PROJ003"]
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB002"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ002"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ003"
            }),
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3249",
                "task_name": "Strategic_Business_Performance_Resource_Optimization",
                "status": "success"
            }),
        ],
        outputs=["success"],  # Scheduler run status
    ),#

    Task(
        annotator="variation_2",
        user_id="task80",
        instruction=(
            "Coordinate the processing of payment for invoice INV012 from Aurora Academic Press on September 1, 2024, at 10:30 AM. Ensure comprehensive payment processing with an appropriate audit trail AUD680 and conduct a strategic client relationship analysis, including an assessment of payment behavior, active project portfolio review, profitability analysis of their primary project PROJ003, and a current year 2024 YTD revenue impact assessment to inform ongoing account management decisions. Document completion with scheduler run RUN8001 for Payment_Processing_Analysis with success status."
        ),
        actions=[


            Action(name="CaV2GetInvoiceById", kwargs={
                "invoice_id": "INV012"
            }),


            Action(name="CaV2FindPublisherByName", kwargs={
                "publisher_name": "Aurora Academic Press"
            }),


            Action(name="CaV2UpdateInvoicePayment", kwargs={
                "invoice_id": "INV012",
                "paid_at": "2024-09-01T10:30:00Z"
            }),


            Action(name="CaV2CreateInvoiceAuditEntry", kwargs={
                "audit_id": "AUD680",
                "invoice_id": "INV012",
                "event_type": "payment_received",
                "event_timestamp": "2024-09-01T10:30:00Z",
                "notes": "AUD680_payment_received_INV012"
            }),
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB002"
            }),


            Action(name="CaV2GetProjectsByPublisher", kwargs={
                "publisher_id": "PUB002",
                "active_only": True
            }),


            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ003"
            }),
            Action(name="CaV2CalculateYtdRevenue", kwargs={
                "year": "2024"
            }),


            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN8001",
                "task_name": "Payment_Processing_Analysis",
                "status": "success"
            }),
        ],
        outputs=["474.60"],  # Total payment amount from invoice INV012
    ),#

    Task(
        annotator="variation_2",
        user_id="task81",
        instruction=(
            "Handle the payment processing for invoice INV009 from Northern Star Publishers on November 1, 2024 at 2:15 PM. Ensure that the payment processing is fully completed with a proper audit trail AUD681. Conduct a strategic analysis of the client relationship, including assessment of their payment behavior, review of the active project portfolio, profitability analysis of their main project PROJ001, and evaluation of the year-to-date revenue impact for 2024 to aid in ongoing account management decisions. Confirm the completion by running scheduler RUN8101 for Payment_Processing_Analysis and ensure it ends with success status."
        ),
        actions=[


            Action(name="CaV2GetInvoiceById", kwargs={
                "invoice_id": "INV009"
            }),


            Action(name="CaV2FindPublisherByName", kwargs={
                "publisher_name": "Northern Star Publishers"
            }),


            Action(name="CaV2UpdateInvoicePayment", kwargs={
                "invoice_id": "INV009",
                "paid_at": "2024-11-01T14:15:00Z"
            }),


            Action(name="CaV2CreateInvoiceAuditEntry", kwargs={
                "audit_id": "AUD681",
                "invoice_id": "INV009",
                "event_type": "payment_received",
                "event_timestamp": "2024-11-01T14:15:00Z",
                "notes": "AUD681_payment_received_INV009"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),


            Action(name="CaV2GetProjectsByPublisher", kwargs={
                "publisher_id": "PUB001",
                "active_only": True
            }),


            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),
            Action(name="CaV2CalculateYtdRevenue", kwargs={
                "year": "2024"
            }),


            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN8101",
                "task_name": "Payment_Processing_Analysis",
                "status": "success"
            }),
        ],
        outputs=["691.56"],  # Total payment amount from invoice INV009
    ),

    Task(
        annotator="variation_2",
        user_id="task82",
        instruction=(
            "Coordinate comprehensive strategic portfolio management and performance analytics to be implemented on April 20, 2024. Analyze the payment behavior for publishers PUB001, PUB002, and PUB003 in order to assess collection patterns and the predictability of revenue. Calculate the profitability of projects PROJ001, PROJ002, and PROJ003 to evaluate the performance of the portfolio. Determine the hours worked for projects PROJ001, PROJ002, and PROJ003 from March 25-April 20, 2024 for resource planning purposes. Generate a database scheduler run RUN3252 for Strategic_Portfolio_Management_Performance_Analytics ensuring it is completed with success status."
        ),
        actions=[
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={"publisher_id": "PUB001"}),
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={"publisher_id": "PUB002"}),
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={"publisher_id": "PUB003"}),
            Action(name="CaV2CalculateProjectProfitability", kwargs={"project_id": "PROJ001"}),
            Action(name="CaV2CalculateProjectProfitability", kwargs={"project_id": "PROJ002"}),
            Action(name="CaV2CalculateProjectProfitability", kwargs={"project_id": "PROJ003"}),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={"start_date": "2024-03-25", "end_date": "2024-04-20", "project_ids": ["PROJ001"]}),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={"start_date": "2024-03-25", "end_date": "2024-04-20", "project_ids": ["PROJ002"]}),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={"start_date": "2024-03-25", "end_date": "2024-04-20", "project_ids": ["PROJ003"]}),
            Action(name="CaV2CreateSchedulerRun", kwargs={"run_id": "RUN3252", "task_name": "Strategic_Portfolio_Management_Performance_Analytics", "status": "success"}),
        ],
        outputs=["success"],
    ),

    Task(
        annotator="variation_2",
        user_id="task83",
        instruction=(
            "Handle payment processing for invoice INV009 from Northern Star Publishers on October 5, 2024 at 1:45 PM. Ensure that the payment is processed completely with a proper audit trail AUD683. Conduct a strategic client relationship analysis encompassing payment behavior assessment, active project portfolio review, profitability analysis of their primary project PROJ001, and an evaluation of the current year 2024 YTD revenue impact to aid ongoing account management decisions. Document the task completion with scheduler run RUN8301 for Payment_Processing_Analysis indicating success."
        ),
        actions=[
            # Get invoice INV009 details
            Action(name="CaV2GetInvoiceById", kwargs={
                "invoice_id": "INV009"
            }),

            # Find Northern Star Publishers
            Action(name="CaV2FindPublisherByName", kwargs={
                "publisher_name": "Northern Star Publishers"
            }),

            # Update payment status
            Action(name="CaV2UpdateInvoicePayment", kwargs={
                "invoice_id": "INV009",
                "paid_at": "2024-10-05T13:45:00Z"
            }),

            # Create payment audit AUD683
            Action(name="CaV2CreateInvoiceAuditEntry", kwargs={
                "audit_id": "AUD683",
                "invoice_id": "INV009",
                "event_type": "payment_received",
                "event_timestamp": "2024-10-05T13:45:00Z",
                "notes": "AUD683_payment_received_INV009"
            }),

            # Get payment behavior for PUB001
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),

            # Get active projects for PUB001
            Action(name="CaV2GetProjectsByPublisher", kwargs={
                "publisher_id": "PUB001",
                "active_only": True
            }),

            # Calculate profitability for main project PROJ001
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),

            # Calculate current year YTD revenue for comparison
            Action(name="CaV2CalculateYtdRevenue", kwargs={
                "year": "2024"
            }),

            # Log payment processing completion
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN8301",
                "task_name": "Payment_Processing_Analysis",
                "status": "success"
            }),
        ],
        outputs=["success"],  # Task completion status
    ),#

    Task(
        annotator="variation_2",
        user_id="task84",
        instruction=(
            "Coordinate the optimization of strategic performance management and resource planning on May 25, 2025. Calculate the hours worked for projects PROJ001, PROJ002, PROJ003, and PROJ004 from March 15-May 25, 2025 for efficient capacity planning. Assess the patterns of collection efficiency for publishers PUB001, PUB002, and PUB003 to enhance accounts receivable management. Evaluate the performance metrics for all four projects to guide strategic decision-making. Create a database scheduler run RUN3254 for Strategic_Performance_Management_Resource_Planning with success status."
        ),
        actions=[
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-03-15",
                "end_date": "2025-05-25",
                "project_ids": ["PROJ001"]
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-03-15",
                "end_date": "2025-05-25",
                "project_ids": ["PROJ002"]
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-03-15",
                "end_date": "2025-05-25",
                "project_ids": ["PROJ003"]
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-03-15",
                "end_date": "2025-05-25",
                "project_ids": ["PROJ004"]
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB002"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB003"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ002"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ003"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ004"
            }),
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3254",
                "task_name": "Strategic_Performance_Management_Resource_Planning",
                "status": "success"
            }),
        ],
        outputs=["success"],  # Scheduler run status
    ),#

    Task(
        annotator="variation_2",
        user_id="task85",
        instruction=(
            "Handle the payment processing for invoice INV023 from Aurora Academic Press on July 15, 2024, at 11:20 AM. Ensure complete payment processing with proper audit trail AUD685 and conduct a strategic client relationship analysis including payment behavior assessment, active project portfolio review, profitability analysis of their primary project PROJ003, and current year 2024 YTD revenue impact assessment to support ongoing account management decisions. Document completion with scheduler run RUN8501 for Payment_Processing_Analysis with success status."
        ),
        actions=[


            Action(name="CaV2GetInvoiceById", kwargs={
                "invoice_id": "INV023"
            }),


            Action(name="CaV2FindPublisherByName", kwargs={
                "publisher_name": "Aurora Academic Press"
            }),


            Action(name="CaV2UpdateInvoicePayment", kwargs={
                "invoice_id": "INV023",
                "paid_at": "2024-07-15T11:20:00Z"
            }),


            Action(name="CaV2CreateInvoiceAuditEntry", kwargs={
                "audit_id": "AUD685",
                "invoice_id": "INV023",
                "event_type": "payment_received",
                "event_timestamp": "2024-07-15T11:20:00Z",
                "notes": "AUD685_payment_received_INV023"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB002"
            }),


            Action(name="CaV2GetProjectsByPublisher", kwargs={
                "publisher_id": "PUB002",
                "active_only": True
            }),


            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ003"
            }),
            Action(name="CaV2CalculateYtdRevenue", kwargs={
                "year": "2024"
            }),


            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN8501",
                "task_name": "Payment_Processing_Analysis",
                "status": "success"
            }),
        ],
        outputs=["728.85"],  # Total payment amount from invoice INV023
    ),

    Task(
        annotator="variation_2",
        user_id="task86",
        instruction=(
            "Coordinate advanced resource management and financial analysis on June 20, 2025. Analyze resource utilization across projects PROJ001, PROJ002, and PROJ003 from April 10-June 20, 2025, for capacity planning. Assess collection efficiency patterns for publishers PUB001, PUB002, and PUB003 to optimize accounts receivable management. Evaluate profitability and performance metrics for all three projects to inform strategic decision-making. Create database scheduler run RUN3256 for Advanced_Resource_Management_Financial_Analysis with success status."
        ),
        actions=[
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-04-10",
                "end_date": "2025-06-20",
                "project_ids": ["PROJ001"]
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-04-10",
                "end_date": "2025-06-20",
                "project_ids": ["PROJ002"]
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-04-10",
                "end_date": "2025-06-20",
                "project_ids": ["PROJ003"]
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB002"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB003"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ002"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ003"
            }),
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3256",
                "task_name": "Advanced_Resource_Management_Financial_Analysis",
                "status": "success"
            }),
        ],
        outputs=["success"],  # Scheduler run status
    ),

    Task(
        annotator="variation_2",
        user_id="task87",
        instruction=(
            "Handle the payment processing for invoice INV024 from Maritime Learning Materials on August 10, 2024 at 3:45 PM. Ensure the full completion of the payment process with an accurate audit trail AUD687 and perform a strategic analysis of client relationships. This includes assessing payment behavior, reviewing the active project portfolio, analyzing the profitability of their main project PROJ007, and evaluating the 2024 year-to-date revenue impact to aid in ongoing account management decisions. Conclude the documentation by executing scheduler run RUN8701 for Payment_Processing_Analysis, confirming it is successful."
        ),
        actions=[
            # Get invoice INV024 details
            Action(name="CaV2GetInvoiceById", kwargs={
                "invoice_id": "INV024"
            }),

            # Find Maritime Learning Materials
            Action(name="CaV2FindPublisherByName", kwargs={
                "publisher_name": "Maritime Learning Materials"
            }),

            # Update payment status
            Action(name="CaV2UpdateInvoicePayment", kwargs={
                "invoice_id": "INV024",
                "paid_at": "2024-08-10T15:45:00Z"
            }),

            # Create payment audit AUD687
            Action(name="CaV2CreateInvoiceAuditEntry", kwargs={
                "audit_id": "AUD687",
                "invoice_id": "INV024",
                "event_type": "payment_received",
                "event_timestamp": "2024-08-10T15:45:00Z",
                "notes": "AUD687_payment_received_INV024"
            }),

            # Get payment behavior for PUB004
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB004"
            }),

            # Get active projects for PUB004
            Action(name="CaV2GetProjectsByPublisher", kwargs={
                "publisher_id": "PUB004",
                "active_only": True
            }),

            # Calculate profitability for main project PROJ007
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ007"
            }),

            # Calculate current year YTD revenue for comparison
            Action(name="CaV2CalculateYtdRevenue", kwargs={
                "year": "2024"
            }),

            # Log payment processing completion
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN8701",
                "task_name": "Payment_Processing_Analysis",
                "status": "success"
            }),
        ],
        outputs=["2090.50"],  # Total payment amount from invoice INV024
    ),

    Task(
        annotator="variation_2",
        user_id="task88",
        instruction=(
            "Coordinate the optimization of advanced business performance and resource allocation on July 15, 2025. Calculate the hours worked on projects PROJ001, PROJ002, and PROJ003 from May 20 through July 15, 2025 for effective capacity planning. Examine the collection efficiency patterns for publishers PUB001, PUB002, PUB003, and PUB004 to enhance accounts receivable management. Evaluate performance metrics for all three projects to support strategic decision-making. Initiate the creation of a database scheduler run RUN3258 for Advanced_Business_Performance_Resource_Optimization ensuring it is completed with success."
        ),
        actions=[
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-05-20",
                "end_date": "2025-07-15",
                "project_ids": ["PROJ001"]
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-05-20",
                "end_date": "2025-07-15",
                "project_ids": ["PROJ002"]
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-05-20",
                "end_date": "2025-07-15",
                "project_ids": ["PROJ003"]
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB002"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB003"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB004"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ002"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ003"
            }),
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3258",
                "task_name": "Advanced_Business_Performance_Resource_Optimization",
                "status": "success"
            }),
        ],
        outputs=["success"],  # Scheduler run status
    ),

    Task(
        annotator="variation_2",
        user_id="task89",
        instruction=(
            "Handle the payment processing for invoice INV010 from Maritime Learning Materials scheduled on August 10, 2024 at 4:20 PM. Ensure the payment is thoroughly processed along with a proper audit trail AUD689. Conduct a strategic analysis of the client relationship, which includes the assessment of payment behavior, reviewing the active project portfolio, analyzing the profitability of their primary project PROJ007, and evaluating the current year 2024 YTD revenue impact to aid in ongoing account management decisions. Document the completion with scheduler run RUN8901 for Payment_Processing_Analysis marked as successful."
        ),
        actions=[
            # Get invoice INV010 details
            Action(name="CaV2GetInvoiceById", kwargs={
                "invoice_id": "INV010"
            }),

            # Find Maritime Learning Materials
            Action(name="CaV2FindPublisherByName", kwargs={
                "publisher_name": "Maritime Learning Materials"
            }),

            # Update payment status
            Action(name="CaV2UpdateInvoicePayment", kwargs={
                "invoice_id": "INV010",
                "paid_at": "2024-08-10T16:20:00Z"
            }),

            # Create payment audit AUD689
            Action(name="CaV2CreateInvoiceAuditEntry", kwargs={
                "audit_id": "AUD689",
                "invoice_id": "INV010",
                "event_type": "payment_received",
                "event_timestamp": "2024-08-10T16:20:00Z",
                "notes": "AUD689_payment_received_INV010"
            }),

            # Get payment behavior for PUB004
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB004"
            }),

            # Get active projects for PUB004
            Action(name="CaV2GetProjectsByPublisher", kwargs={
                "publisher_id": "PUB004",
                "active_only": True
            }),

            # Calculate profitability for main project PROJ007
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ007"
            }),

            # Calculate current year YTD revenue for comparison
            Action(name="CaV2CalculateYtdRevenue", kwargs={
                "year": "2024"
            }),

            # Log payment processing completion
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN8901",
                "task_name": "Payment_Processing_Analysis",
                "status": "success"
            }),
        ],
        outputs=["1536.80"],  # Total payment amount from invoice INV010
    ),

    Task(
        annotator="variation_2",
        user_id="task90",
        instruction=(
            "Coordinate the implementation of strategic resource management and performance analysis set for August 15, 2025. Calculate the hours worked for projects PROJ001, PROJ002, and PROJ003 within the period of June 10-August 15, 2025, for capacity planning purposes. Assess the efficiency patterns in collections for publishers PUB001, PUB002, and PUB003 to enhance the management of accounts receivable. Evaluate the performance metrics across all three projects to support strategic decision-making. Initiate the creation of database scheduler run RUN3260 for Strategic_Resource_Management_Performance_Analysis with a successful status."
        ),
        actions=[
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-06-10",
                "end_date": "2025-08-15",
                "project_ids": ["PROJ001"]
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-06-10",
                "end_date": "2025-08-15",
                "project_ids": ["PROJ002"]
            }),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={
                "start_date": "2025-06-10",
                "end_date": "2025-08-15",
                "project_ids": ["PROJ003"]
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB002"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB003"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ002"
            }),
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ003"
            }),
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN3260",
                "task_name": "Strategic_Resource_Management_Performance_Analysis",
                "status": "success"
            }),
        ],
        outputs=["success"],  # Scheduler run status
    ),

    Task(
        annotator="variation_2",
        user_id="task91",
        instruction=(
            "Handle payment processing for invoice INV025 from Midwest Education House scheduled on September 1, 2024 at 2:30 PM. Ensure thorough payment completion with an accurate audit trail AUD691 and perform a strategic analysis of the client relationship including payment behavior evaluation, active project portfolio review, profitability analysis of their key project PROJ010, and evaluation of the current year 2024 YTD revenue impact to aid ongoing account management choices. Record the completion with the scheduler run RUN9101 for Payment_Processing_Analysis with a success status."
        ),
        actions=[
            # Get invoice INV025 details
            Action(name="CaV2GetInvoiceById", kwargs={
                "invoice_id": "INV025"
            }),

            # Find Midwest Education House
            Action(name="CaV2FindPublisherByName", kwargs={
                "publisher_name": "Midwest Education House"
            }),

            # Update payment status
            Action(name="CaV2UpdateInvoicePayment", kwargs={
                "invoice_id": "INV025",
                "paid_at": "2024-09-01T14:30:00Z"
            }),

            # Create payment audit AUD691
            Action(name="CaV2CreateInvoiceAuditEntry", kwargs={
                "audit_id": "AUD691",
                "invoice_id": "INV025",
                "event_type": "payment_received",
                "event_timestamp": "2024-09-01T14:30:00Z",
                "notes": "AUD691_payment_received_INV025"
            }),

            # Get payment behavior for PUB005
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB005"
            }),

            # Get active projects for PUB005
            Action(name="CaV2GetProjectsByPublisher", kwargs={
                "publisher_id": "PUB005",
                "active_only": True
            }),

            # Calculate profitability for main project PROJ010
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ010"
            }),

            # Calculate current year YTD revenue for comparison
            Action(name="CaV2CalculateYtdRevenue", kwargs={
                "year": "2024"
            }),

            # Log payment processing completion
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN9101",
                "task_name": "Payment_Processing_Analysis",
                "status": "success"
            }),
        ],
        outputs=["813.60"],  # Total payment amount from invoice INV025
    ),
    Task(
        annotator="variation_2",
        user_id="task92",
        instruction=(
            "Coordinate resource allocation and performance analysis set for September 15, 2025. Calculate the hours worked on projects PROJ001, PROJ002, and PROJ003 from July 20-September 15, 2025 for effective capacity planning. Evaluate collection efficiency patterns for publishers PUB001, PUB002, PUB003, and PUB004 to enhance accounts receivable management. Appraise performance metrics for all three projects to inform strategic decisions. Establish a database scheduler run RUN3262 for Resource_Allocation_Performance_Analysis with a success status."
        ),
        actions=[
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={"start_date": "2025-07-20", "end_date": "2025-09-15", "project_ids": ["PROJ001"]}),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={"start_date": "2025-07-20", "end_date": "2025-09-15", "project_ids": ["PROJ002"]}),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={"start_date": "2025-07-20", "end_date": "2025-09-15", "project_ids": ["PROJ003"]}),
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={"publisher_id": "PUB001"}),
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={"publisher_id": "PUB002"}),
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={"publisher_id": "PUB003"}),
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={"publisher_id": "PUB004"}),
            Action(name="CaV2CalculateProjectProfitability", kwargs={"project_id": "PROJ001"}),
            Action(name="CaV2CalculateProjectProfitability", kwargs={"project_id": "PROJ002"}),
            Action(name="CaV2CalculateProjectProfitability", kwargs={"project_id": "PROJ003"}),
            Action(name="CaV2CreateSchedulerRun", kwargs={"run_id": "RUN3262", "task_name": "Resource_Allocation_Performance_Analysis", "status": "success"}),
        ],
        outputs=["success"],
    ),
    Task(
        annotator="variation_2",
        user_id="task94",
        instruction=(
            "Handle the optimization of performance management and resource planning on October 15, 2025. Calculate the hours worked for projects PROJ001, PROJ002, and PROJ003 between August 25 and October 15, 2025 for capacity planning purposes. Assess the collection efficiency patterns for the publishers PUB001, PUB002, and PUB003 to enhance accounts receivable management. Evaluate the performance metrics for all three projects to aid in strategic decision-making. Create the database scheduler run RUN3264 for Performance_Management_Resource_Planning with a success status."
        ),
        actions=[
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={"start_date": "2025-08-25", "end_date": "2025-10-15", "project_ids": ["PROJ001"]}),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={"start_date": "2025-08-25", "end_date": "2025-10-15", "project_ids": ["PROJ002"]}),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={"start_date": "2025-08-25", "end_date": "2025-10-15", "project_ids": ["PROJ003"]}),
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={"publisher_id": "PUB001"}),
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={"publisher_id": "PUB002"}),
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={"publisher_id": "PUB003"}),
            Action(name="CaV2CalculateProjectProfitability", kwargs={"project_id": "PROJ001"}),
            Action(name="CaV2CalculateProjectProfitability", kwargs={"project_id": "PROJ002"}),
            Action(name="CaV2CalculateProjectProfitability", kwargs={"project_id": "PROJ003"}),
            Action(name="CaV2CreateSchedulerRun", kwargs={"run_id": "RUN3264", "task_name": "Performance_Management_Resource_Planning", "status": "success"}),
        ],
        outputs=["success"],
    ),
    Task(
        annotator="variation_2",
        user_id="task95",
        instruction=(
            "Coordinate the processing of the payment for invoice INV021 from Northern Star Publishers on December 10, 2024, at 2:15 PM. Ensure the payment processing is complete with the proper audit trail AUD695 and perform a strategic client relationship analysis, including assessing payment behavior, reviewing the active project portfolio, analyzing the profitability of their primary project PROJ001, and evaluating the current year 2024 YTD revenue impact to support ongoing account management decisions. Document the completion with scheduler run RUN9501 for Payment_Processing_Analysis with a success status."
        ),
        actions=[


            Action(name="CaV2GetInvoiceById", kwargs={
                "invoice_id": "INV021"
            }),


            Action(name="CaV2FindPublisherByName", kwargs={
                "publisher_name": "Northern Star Publishers"
            }),


            Action(name="CaV2UpdateInvoicePayment", kwargs={
                "invoice_id": "INV021",
                "paid_at": "2024-12-10T14:15:00Z"
            }),


            Action(name="CaV2CreateInvoiceAuditEntry", kwargs={
                "audit_id": "AUD695",
                "invoice_id": "INV021",
                "event_type": "payment_received",
                "event_timestamp": "2024-12-10T14:15:00Z",
                "notes": "AUD695_payment_received_INV021"
            }),


            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB001"
            }),


            Action(name="CaV2GetProjectsByPublisher", kwargs={
                "publisher_id": "PUB001",
                "active_only": True
            }),


            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ001"
            }),
            Action(name="CaV2CalculateYtdRevenue", kwargs={
                "year": "2024"
            }),


            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN9501",
                "task_name": "Payment_Processing_Analysis",
                "status": "success"
            }),
        ],
        outputs=["1412.50"],  # Total payment amount from invoice INV021
    ),

    Task(
        annotator="variation_2",
        user_id="task93",
        instruction=(
            "Carry out a thorough strategic business intelligence and competitive analysis on October 1, 2024. Analyze payment behavior for publishers PUB001, PUB002, PUB003, PUB004, and PUB005 to assess market positioning and collection performance. Calculate profitability for projects PROJ001, PROJ002, PROJ003, PROJ004, and PROJ005 to evaluate strategic value creation and competitive advantage. Determine hours worked for projects PROJ001, PROJ002, and PROJ003 from August 15-October 1, 2024 for operational efficiency benchmarking. Create database scheduler run RUN3263 for Strategic_Business_Intelligence_Competitive_Analysis with success status."
        ),
        actions=[
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={"publisher_id": "PUB001"}),
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={"publisher_id": "PUB002"}),
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={"publisher_id": "PUB003"}),
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={"publisher_id": "PUB004"}),
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={"publisher_id": "PUB005"}),
            Action(name="CaV2CalculateProjectProfitability", kwargs={"project_id": "PROJ001"}),
            Action(name="CaV2CalculateProjectProfitability", kwargs={"project_id": "PROJ002"}),
            Action(name="CaV2CalculateProjectProfitability", kwargs={"project_id": "PROJ003"}),
            Action(name="CaV2CalculateProjectProfitability", kwargs={"project_id": "PROJ004"}),
            Action(name="CaV2CalculateProjectProfitability", kwargs={"project_id": "PROJ005"}),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={"start_date": "2024-08-15", "end_date": "2024-10-01", "project_ids": ["PROJ001"]}),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={"start_date": "2024-08-15", "end_date": "2024-10-01", "project_ids": ["PROJ002"]}),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={"start_date": "2024-08-15", "end_date": "2024-10-01", "project_ids": ["PROJ003"]}),
            Action(name="CaV2CreateSchedulerRun", kwargs={"run_id": "RUN3263", "task_name": "Strategic_Business_Intelligence_Competitive_Analysis", "status": "success"}),
        ],
        outputs=["success"],
    ),

    Task(
        annotator="variation_2",
        user_id="task96",
        instruction=(
            "Coordinate resource management and financial analysis on November 15, 2024. Determine hours worked for projects PROJ001, PROJ002, and PROJ003 from September 30-November 15, 2024 for capacity planning. Assess collection efficiency patterns for publishers PUB001, PUB002, and PUB003 to optimize accounts receivable management. Evaluate performance metrics for all three projects to inform strategic decision-making. Set up database scheduler run RUN3266 for Resource_Management_Financial_Analysis with success status."
        ),
        actions=[
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={"start_date": "2024-09-30", "end_date": "2024-11-15", "project_ids": ["PROJ001", "PROJ002", "PROJ003"]}),
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={"publisher_id": "PUB001"}),
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={"publisher_id": "PUB002"}),
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={"publisher_id": "PUB003"}),
            Action(name="CaV2CalculateProjectProfitability", kwargs={"project_id": "PROJ001"}),
            Action(name="CaV2CalculateProjectProfitability", kwargs={"project_id": "PROJ002"}),
            Action(name="CaV2CalculateProjectProfitability", kwargs={"project_id": "PROJ003"}),
            Action(name="CaV2CreateSchedulerRun", kwargs={"run_id": "RUN3266", "task_name": "Resource_Management_Financial_Analysis", "status": "success"}),
        ],
        outputs=["success"],
    ),

    Task(
        annotator="variation_2",
        user_id="task97",
        instruction=(
            "Handle the payment processing for invoice INV024 from Maritime Learning Materials scheduled on November 15, 2024 at 11:15 AM. Ensure that the payment processing is completed with a proper audit trail AUD697. Additionally, conduct a strategic client relationship analysis, which includes assessing payment behavior, reviewing the active project portfolio, analyzing the profitability of their primary project PROJ007, and assessing the 2024 year-to-date revenue impact to support ongoing account management decisions. Record the completion with the scheduler run RUN9701 for Payment_Processing_Analysis with a success status."
        ),
        actions=[
            # Get invoice INV024 details
            Action(name="CaV2GetInvoiceById", kwargs={
                "invoice_id": "INV024"
            }),

            # Find Maritime Learning Materials
            Action(name="CaV2FindPublisherByName", kwargs={
                "publisher_name": "Maritime Learning Materials"
            }),

            # Update payment status
            Action(name="CaV2UpdateInvoicePayment", kwargs={
                "invoice_id": "INV024",
                "paid_at": "2024-11-15T11:15:00Z"
            }),

            # Create payment audit AUD697
            Action(name="CaV2CreateInvoiceAuditEntry", kwargs={
                "audit_id": "AUD697",
                "invoice_id": "INV024",
                "event_type": "payment_received",
                "event_timestamp": "2024-11-15T11:15:00Z",
                "notes": "AUD697_payment_received_INV024"
            }),

            # Get payment behavior for PUB004
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={
                "publisher_id": "PUB004"
            }),

            # Get active projects for PUB004
            Action(name="CaV2GetProjectsByPublisher", kwargs={
                "publisher_id": "PUB004",
                "active_only": True
            }),

            # Calculate profitability for main project PROJ007
            Action(name="CaV2CalculateProjectProfitability", kwargs={
                "project_id": "PROJ007"
            }),

            # Calculate current year YTD revenue for comparison
            Action(name="CaV2CalculateYtdRevenue", kwargs={
                "year": "2024"
            }),

            # Log payment processing completion
            Action(name="CaV2CreateSchedulerRun", kwargs={
                "run_id": "RUN9701",
                "task_name": "Payment_Processing_Analysis",
                "status": "success"
            }),
        ],
        outputs=["2090.50"],  # Total payment amount from invoice INV024
    ),
    Task(
        annotator="variation_2",
        user_id="task98",
        instruction=(
            "Coordinate the optimization of business performance and resource allocation on December 15, 2024. Analyze resource utilization across projects PROJ001, PROJ002, and PROJ003 from October 15 to December 15, 2024, for capacity planning. Evaluate collection efficiency patterns for publishers PUB001, PUB002, and PUB003 to enhance accounts receivable management. Assess the performance metrics for projects PROJ001, PROJ002, and PROJ003 to guide strategic decision-making. Generate a database scheduler run RUN3268 for Business_Performance_Resource_Optimization with a success status."
        ),
        actions=[
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={"start_date": "2024-10-15", "end_date": "2024-12-15", "project_ids": ["PROJ001", "PROJ002", "PROJ003"]}),
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={"publisher_id": "PUB001"}),
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={"publisher_id": "PUB002"}),
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={"publisher_id": "PUB003"}),
            Action(name="CaV2CalculateProjectProfitability", kwargs={"project_id": "PROJ001"}),
            Action(name="CaV2CalculateProjectProfitability", kwargs={"project_id": "PROJ002"}),
            Action(name="CaV2CalculateProjectProfitability", kwargs={"project_id": "PROJ003"}),
            Action(name="CaV2CreateSchedulerRun", kwargs={"run_id": "RUN3268", "task_name": "Business_Performance_Resource_Optimization", "status": "success"}),
        ],
        outputs=["success"],
    ),
    Task(
        annotator="variation_2",
        user_id="task99",
        instruction=(
            "Handle the development of a revenue strategy and financial intelligence on January 1, 2026. Coordinate the calculation of expense summaries for the categories of equipment_rental, storage, and transportation from December 1, 2024-January 1, 2025 to pinpoint cost optimization opportunities. Obtain the tax rate for 2022 and compute YTD revenue for 2023 to evaluate tax implications and strategic financial planning. Gather payment behavior data for publishers PUB001, PUB002, and PUB003 to assess cash flow patterns. Initiate database scheduler run RUN3269 for Revenue_Strategy_Financial_Intelligence, ensuring a successful status."
        ),
        actions=[
            Action(name="CaV2CalculateExpenseSummary", kwargs={"category_filter": ["equipment_rental"], "start_date": "2024-12-01", "end_date": "2025-01-01"}),
            Action(name="CaV2CalculateExpenseSummary", kwargs={"category_filter": ["storage"], "start_date": "2024-12-01", "end_date": "2025-01-01"}),
            Action(name="CaV2CalculateExpenseSummary", kwargs={"category_filter": ["transportation"], "start_date": "2024-12-01", "end_date": "2025-01-01"}),
            Action(name="CaV2GetTaxRateByYear", kwargs={"year": "2022"}),
            Action(name="CaV2CalculateYtdRevenue", kwargs={"year": "2023"}),
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={"publisher_id": "PUB001"}),
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={"publisher_id": "PUB002"}),
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={"publisher_id": "PUB003"}),
            Action(name="CaV2CreateSchedulerRun", kwargs={"run_id": "RUN3269", "task_name": "Revenue_Strategy_Financial_Intelligence", "status": "success"}),
        ],
        outputs=["success"],
    ),#

    Task(
        annotator="variation_2",
        user_id="task100",
        instruction=(
            "Coordinate resource management and performance analysis implementation on January 15, 2026. Calculate hours worked for projects PROJ001, PROJ002, and PROJ003 between November 30, 2025-January 15, 2026 for capacity planning purposes. Evaluate collection efficiency patterns for publishers PUB001, PUB002, PUB003, and PUB004 to enhance accounts receivable management. Analyze performance metrics for all three projects to guide strategic decision-making. Set up database scheduler run RUN3270 for Resource_Management_Performance_Analysis, aiming for a successful status."
        ),
        actions=[
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={"start_date": "2025-11-30", "end_date": "2026-01-15", "project_ids": ["PROJ001"]}),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={"start_date": "2025-11-30", "end_date": "2026-01-15", "project_ids": ["PROJ002"]}),
            Action(name="CaV2CalculateHoursWorkedInPeriod", kwargs={"start_date": "2025-11-30", "end_date": "2026-01-15", "project_ids": ["PROJ003"]}),
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={"publisher_id": "PUB001"}),
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={"publisher_id": "PUB002"}),
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={"publisher_id": "PUB003"}),
            Action(name="CaV2GetPaymentBehaviorByPublisher", kwargs={"publisher_id": "PUB004"}),
            Action(name="CaV2CalculateProjectProfitability", kwargs={"project_id": "PROJ001"}),
            Action(name="CaV2CalculateProjectProfitability", kwargs={"project_id": "PROJ002"}),
            Action(name="CaV2CalculateProjectProfitability", kwargs={"project_id": "PROJ003"}),
            Action(name="CaV2CreateSchedulerRun", kwargs={"run_id": "RUN3270", "task_name": "Resource_Management_Performance_Analysis", "status": "success"}),
        ],
        outputs=["success"],
    ),

]
