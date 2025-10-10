from domains.dto import Task, Action

TASKS = [
    Task(
        annotator='gokulsaireddy',
        user_id='task_001',
        instruction=
        "Your task is to produce a 7-day cash flow forecast for the period August 26, 2025 (2025-08-26), to September 2, 2025 (2025-09-02). The final analysis, which must be logged in the scheduler for 2025-08-26T13:00:00Z with a note '7-day cash flow forecast', should find the net cash flow posed by 'Maple Leaf Publishing House' by comparing their total unpaid expected inflows against the company's total recurring outflows for the period. This assessment should be supported by the publisher's historical payment profile.",
        actions=[
            Action(name='GetPublisherByName',
                   kwargs={'publisher_name': 'Maple Leaf Publishing House'}),
            Action(name='FilterInvoices',
                   kwargs={
                       'publisher_id': 'PUB001',
                       'unpaid_only': True
                   }),
            Action(name='CalculateTotalInflows',
                   kwargs={
                       'start_date': '2025-08-26',
                       'end_date': '2025-09-02',
                       'invoices_to_consider': ['INV009', 'INV021', 'INV026']
                   }),
            Action(name='CalculateTotalOutflows',
                   kwargs={
                       'start_date': '2025-08-26',
                       'end_date': '2025-09-02'
                   }),
            Action(name='ComputeNetCashFlow',
                   kwargs={
                       'inflows': 4477.06,
                       'outflows': 4552.94
                   }),
            Action(name='GetPaymentBehavior',
                   kwargs={'publisher_id': 'PUB001'}),
            Action(name='AddSchedulerRun',
                   kwargs={
                       'run_date': '2025-08-26T13:00:00Z',
                       'note': '7-day cash flow forecast'
                   })
        ],
        outputs=['PUB001', '4477.06', '4552.94', 'BEH001', -75.88]),
    Task(
        annotator='gokulsaireddy',
        user_id='task_002',
        instruction=
        "You issue an April 2024 invoice for Coastal Educational Resources, numbered '2024-004' and dated 2024-04-30, covering the full month of April. The invoice must show a subtotal of 600.0 CAD, HST of 78.0 CAD, and a total due of 678.0 CAD. It includes a line item for project PROJ011 with 6.0 hours at a rate of 100.0. The line details are visible, and the invoice is reflected in the April dashboard snapshot (SNAP004) dated 2024-04-30, with the snapshot confirming the updated record.",
        actions=[
            Action(name='GetPublisherByName',
                   kwargs={'publisher_name': 'Coastal Educational Resources'}),
            Action(name='CreateInvoice',
                   kwargs={
                       'invoice_number': '2024-004',
                       'publisher_id': 'PUB004',
                       'invoice_date': '2024-04-30',
                       'period_start': '2024-04-01',
                       'period_end': '2024-04-30',
                       'subtotal': 600.0,
                       'hst_amount': 78.0,
                       'total_due': 678.0
                   }),
            Action(name='CreateInvoiceLine',
                   kwargs={
                       'invoice_id': 'INV2024-004',
                       'project_id': 'PROJ011',
                       'hours': 6.0,
                       'rate': 100.0,
                       'hst_rate': 0.13
                   }),
            Action(name='GetInvoiceLines',
                   kwargs={'invoice_id': 'INV2024-004'}),
            Action(name='CreateDashboardSnapshot',
                   kwargs={
                       'snapshot_id': 'SNAP004',
                       'snapshot_date': '2024-04-30',
                       'year': 2024
                   }),
            Action(name='GetDashboardSnapshot',
                   kwargs={'snapshot_id': 'SNAP004'})
        ],
        outputs=['INV2024-004', 'SNAP004']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_003',
        instruction=
        "Your task is to create a dedicated micro-invoice for the work completed under time entry 'TIME002'. The system must be updated to include a new, single-line invoice that has the 6.0 billable hours and 85.0 project rate. ('2025-T002' for $510.00 subtotal, $66.30 HST, $576.30 total_due) dated on 2025-08-26. Ensure the new invoice and its corresponding line item are created and that the action is recorded in the audit trail.",
        actions=[
            Action(name='GetTimeEntryDetails',
                   kwargs={'time_entry_id': 'TIME002'}),
            Action(name='GetProjectDetails', kwargs={'project_id': 'PROJ001'}),
            Action(name='CreateInvoice',
                   kwargs={
                       'invoice_number': '2025-T002',
                       'publisher_id': 'PUB001',
                       'subtotal': 510.0,
                       'hst_amount': 66.3,
                       'total_due': 576.3,
                       'invoice_date': '2025-08-26'
                   }),
            Action(name='CreateInvoiceLine',
                   kwargs={
                       'invoice_id': 'INV2025-T002',
                       'project_id': 'PROJ001',
                       'hours': 6.0,
                       'rate': 85.0,
                       'hst_rate': 0.13
                   }),
            Action(name='RecordInvoiceAudit',
                   kwargs={
                       'invoice_number': '2025-T002',
                       'event_type': 'created'
                   }),
            Action(name='ListInvoiceAudit',
                   kwargs={'invoice_id': 'INV2025-T002'})
        ],
        outputs=['AUD_INV2025-T002_45', 'INV2025-T002', 'LINE-0030']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_004',
        instruction=
        "Your task is to create a dedicated micro-invoice for the work completed under time entry 'TIME004'. The system must be updated to include a new, single-line invoice that has the 5.5 billable hours and 75.0 project rate. ('2025-T004' for $412.50 subtotal, $53.62 HST, $466.13 total_due) dated on 2025-08-26. Ensure the new invoice and its corresponding line item are created and that the action is recorded in the audit trail.",
        actions=[
            Action(name='GetTimeEntryDetails',
                   kwargs={'time_entry_id': 'TIME004'}),
            Action(name='GetProjectDetails', kwargs={'project_id': 'PROJ003'}),
            Action(name='CreateInvoice',
                   kwargs={
                       'invoice_number': '2025-T004',
                       'publisher_id': 'PUB002',
                       'subtotal': 412.5,
                       'hst_amount': 53.62,
                       'total_due': 466.13,
                       'invoice_date': '2025-08-26'
                   }),
            Action(name='CreateInvoiceLine',
                   kwargs={
                       'invoice_id': 'INV2025-T004',
                       'project_id': 'PROJ003',
                       'hours': 5.5,
                       'rate': 75.0,
                       'hst_rate': 0.13
                   }),
            Action(name='RecordInvoiceAudit',
                   kwargs={
                       'invoice_number': '2025-T004',
                       'event_type': 'created'
                   }),
            Action(name='ListInvoiceAudit',
                   kwargs={'invoice_id': 'INV2025-T004'})
        ],
        outputs=['AUD_INV2025-T004_45', 'INV2025-T004', 'LINE-0030']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_005',
        instruction=
        "You should record a September 2024 office rent expense of 2200.00 CAD paid to 'Regus Offices' under category_code 'RENT'. The expense_date is 2024-09-01 and it is paid by bank_transfer. The expense has expense_id 'EXP2024-09-001'. It should be also present in the September 2024 dashboard snapshot (SNAP009), which you create for date '2024-09-30'. The expense impact is added as a monthly entry with revenue 2200.00, where total monthly expenses are updated and visible.",
        actions=[
            Action(name='GetExpensesByCategory',
                   kwargs={'category_code': 'RENT'}),
            Action(name='AddExpenseRecord',
                   kwargs={
                       'expense_id': 'EXP2024-09-001',
                       'vendor': 'Regus Offices',
                       'expense_date': '2024-09-01',
                       'amount': 2200.0,
                       'payment_method': 'bank_transfer',
                       'category_code': 'RENT'
                   }),
            Action(name='GetExpensesByCategory',
                   kwargs={'category_code': 'RENT'}),
            Action(name='CreateDashboardSnapshot',
                   kwargs={
                       'snapshot_id': 'SNAP009',
                       'snapshot_date': '2024-09-30',
                       'year': 2024
                   }),
            Action(name='AddMonthlyExpense',
                   kwargs={
                       'snapshot_id': 'SNAP009',
                       'month': '2024-09',
                       'amount': 2200.0
                   }),
            Action(name='GetMonthlyExpenseBySnapshot',
                   kwargs={'snapshot_id': 'SNAP009'}),
            Action(name='GetDashboardSnapshot',
                   kwargs={'snapshot_id': 'SNAP009'})
        ],
        outputs=['SNAP009_2024-09', 'SNAP009']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_006',
        instruction=
        "Your task is to perform a full onboarding for the new publisher 'Apex Digital Learning' ('PUB055') with contact mail (billing@apex-digital.ca) as of September 2025. The end state must show that the publisher and their new project, 'Interactive Biology Courseware' ('PROJ4006'), with isbn 978-6-1600-4006-6 at 105.0 hourly rate have been created. Furthermore, their first setup fee invoice ('2025-A001' for $1500.00 subtotal, $195.00 HST, 1695.00 total_due) must be created dated 2025-09-01, immediately emailed to the client with subject: '2025-A001' ",
        actions=[
            Action(name='CreatePublisher',
                   kwargs={
                       'publisher_id': 'PUB055',
                       'name': 'Apex Digital Learning',
                       'contact_email': 'billing@apex-digital.ca'
                   }),
            Action(name='GetPublisherInfo', kwargs={'publisher_id': 'PUB055'}),
            Action(name='CreateProject',
                   kwargs={
                       'project_id': 'PROJ4006',
                       'publisher_id': 'PUB055',
                       'isbn': '978-6-1600-4006-6',
                       'project_title': 'Interactive Biology Courseware',
                       'default_hourly_rate': 105.0
                   }),
            Action(name='GetProjectDetails', kwargs={'project_id':
                                                     'PROJ4006'}),
            Action(name='CreateInvoice',
                   kwargs={
                       'invoice_number': '2025-A001',
                       'publisher_id': 'PUB055',
                       'subtotal': 1500.0,
                       'hst_amount': 195.0,
                       'total_due': 1695.0,
                       'invoice_date': '2025-09-01'
                   }),
            Action(name='SendInvoiceEmail',
                   kwargs={
                       'publisher_id': 'PUB055',
                       'invoice_number': '2025-A001',
                       'subject': '2025-A001'
                   }),
            Action(name='GetInvoiceDetails',
                   kwargs={'invoice_number': '2025-A001'})
        ],
        outputs=['INV2025-A001']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_007',
        instruction=
        "Your task is to create an invoice for project 'Computer Programming Workbook Series (3 volumes)' as of October 25, 2025 (2025-10-25). The system should include an auditable invoice ('2025-K003') for the initial setup fee, which has a subtotal of 1000.00 CAD, HST of 130.00 CAD, and a total of 1130.00 CAD. Also, audit this invoice with a 'generated' event and verify it. Furthermore, a financial dashboard for the date must be created for this new income, showing a new year-to-date revenue of 12563.78 CAD. Finally, include a monthly audit with the same subtotal and verify it.",
        actions=[
            Action(name='GetProjectPublisher',
                   kwargs={
                       'name':
                       'Computer Programming Workbook Series (3 volumes)'
                   }),
            Action(name='CreateInvoice',
                   kwargs={
                       'invoice_number': '2025-K003',
                       'publisher_id': 'PUB004',
                       'invoice_date': '2025-10-25',
                       'subtotal': 1000.0,
                       'hst_amount': 130.0,
                       'total_due': 1130.0
                   }),
            Action(name='LogInvoiceAuditEvent',
                   kwargs={
                       'invoice_id': 'INV2025-K003',
                       'event_type': 'generated'
                   }),
            Action(name='CreateDashboardSnapshotWithInvoiceId',
                   kwargs={
                       'invoice_id': 'INV2025-K003',
                       'snapshot_date': '2025-10-25',
                       'year': 2025,
                       'ytd_revenue': 12563.78
                   }),
            Action(name='AddMonthlyAudit',
                   kwargs={
                       'snapshot_id': 'SNAP_INV2025-K003',
                       'month': '2025-10',
                       'amount': 1000.0
                   }),
            Action(name='GetMonthlyAuditBySnapshot',
                   kwargs={'snapshot_id': 'SNAP_INV2025-K003'}),
            Action(name='ListInvoiceAudit',
                   kwargs={'audit_id': 'AUD_INV2025-K003'})
        ],
        outputs=[
            'PUB004', 'INV2025-K003', 'AUD_INV2025-K003', 'SNAP_INV2025-K003',
            'SNAP_INV2025-K003_2025-10'
        ]),
    Task(
        annotator='gokulsaireddy',
        user_id='task_008',
        instruction=
        "Your goal is to fully onboard the new publisher 'CodeCrafters Publishing' ('PUB058') and their email 'billing@codecrafters.dev' as of September 2025. The publisher and their project 'Advanced Python Patterns' ('PROJ4009', ISBN '978-9-1900-4009-9', rate 120.0) must be created and verifiable. A key part of this onboarding is to issue and immediately email their first invoice '2025-B003' on 2025-09-01 for $2260.00 total_due ($2000.00 subtotal, $260.00 HST).",
        actions=[
            Action(name='CreatePublisher',
                   kwargs={
                       'publisher_id': 'PUB058',
                       'name': 'CodeCrafters Publishing',
                       'contact_email': 'billing@codecrafters.dev'
                   }),
            Action(name='GetPublisherInfo', kwargs={'publisher_id': 'PUB058'}),
            Action(name='CreateProject',
                   kwargs={
                       'project_id': 'PROJ4009',
                       'publisher_id': 'PUB058',
                       'isbn': '978-9-1900-4009-9',
                       'project_title': 'Advanced Python Patterns',
                       'default_hourly_rate': 120.0
                   }),
            Action(name='GetProjectDetails', kwargs={'project_id':
                                                     'PROJ4009'}),
            Action(name='CreateInvoice',
                   kwargs={
                       'invoice_number': '2025-B003',
                       'publisher_id': 'PUB058',
                       'subtotal': 2000.0,
                       'hst_amount': 260.0,
                       'total_due': 2260.0,
                       'invoice_date': '2025-09-01'
                   }),
            Action(name='SendInvoiceEmail',
                   kwargs={
                       'publisher_id': 'PUB058',
                       'invoice_number': '2025-B003',
                       'subject': '2025-B003'
                   }),
            Action(name='GetInvoiceDetails',
                   kwargs={'invoice_number': '2025-B003'})
        ],
        outputs=['INV2025-B003']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_009',
        instruction=
        "Your task is to process a payment for invoice '2024-023'. The system must be updated to show the invoice was paid on '2025-09-03T10:00:00Z'. A 'payment_received' event must be logged in the audit trail. Finally, the balance of the primary 'checking' account must be updated to reflect the deposit, resulting in a new balance of $16149.60.",
        actions=[
            Action(name='FilterInvoices',
                   kwargs={'invoice_number': '2024-023'}),
            Action(name='UpdateInvoicePayment',
                   kwargs={
                       'invoice_id': 'INV023',
                       'paid_at': '2025-09-03T10:00:00Z'
                   }),
            Action(name='LogInvoiceAuditEvent',
                   kwargs={
                       'invoice_id': 'INV023',
                       'event_type': 'payment_received'
                   }),
            Action(name='GetBankAccountDetails',
                   kwargs={'account_type': 'checking'}),
            Action(name='UpdateBankAccountBalance',
                   kwargs={
                       'account_id': 'CHK001',
                       'balance': 16149.6
                   })
        ],
        outputs=['INV023', 'CHK001', 'AUD_INV023']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_010',
        instruction=
        "Your task is to create a dedicated financial snapshot for the 'Canadian History Comprehensive Guide' project. The snapshot, with ID 'SNAP_PROJ003', must be dated for 2025-08-31 for the year 2025. Before creating the report, you must confirm that the project's total lifetime logged hours is 14.5. The final snapshot must be populated with the project's total lifetime revenue of $1087.50, using the record ID 'PR_SNAP003_PROJ003'.",
        actions=[
            Action(name='GetProjectByName',
                   kwargs={
                       'project_name': 'Canadian History Comprehensive Guide'
                   }),
            Action(name='GetProjectTimeEntries',
                   kwargs={'project_id': 'PROJ003'}),
            Action(name='CreateDashboardSnapshot',
                   kwargs={
                       'snapshot_id': 'SNAP_PROJ003',
                       'snapshot_date': '2025-08-31',
                       'year': 2025
                   }),
            Action(name='AddProjectRevenue',
                   kwargs={
                       'row_id': 'PR_SNAP003_PROJ003',
                       'snapshot_id': 'SNAP_PROJ003',
                       'project_id': 'PROJ003',
                       'revenue': 1087.5
                   }),
            Action(name='GetProjectRevenueSummary',
                   kwargs={'snapshot_id': 'SNAP_PROJ003'})
        ],
        outputs=['PROJ003', 'SNAP_PROJ003', 'PR_SNAP003_PROJ003', 14.5]),
    Task(
        annotator='gokulsaireddy',
        user_id='task_011',
        instruction=
        "You issue a May 2024 invoice for Horizon Academic Press, numbered '2024-005' and dated 2024-05-31, covering the full month of May. The invoice must show a subtotal of 1650.0 CAD, HST of 214.5 CAD, and a total due of 1864.5 CAD. It includes two line items: project PROJ005 with 10.0 hours at 90.0, and project PROJ006 with 7.5 hours at 100.0. The line details are visible, and the invoice is reflected in the May dashboard snapshot (SNAP005) dated 2024-05-31, with the snapshot.",
        actions=[
            Action(name='GetPublisherByName',
                   kwargs={'publisher_name': 'Horizon Academic Press'}),
            Action(name='CreateInvoice',
                   kwargs={
                       'invoice_number': '2024-005',
                       'publisher_id': 'PUB003',
                       'invoice_date': '2024-05-31',
                       'period_start': '2024-05-01',
                       'period_end': '2024-05-31',
                       'subtotal': 1650.0,
                       'hst_amount': 214.5,
                       'total_due': 1864.5
                   }),
            Action(name='CreateInvoiceLine',
                   kwargs={
                       'invoice_id': 'INV2024-005',
                       'project_id': 'PROJ005',
                       'hours': 10.0,
                       'rate': 90.0,
                       'hst_rate': 0.13
                   }),
            Action(name='CreateInvoiceLine',
                   kwargs={
                       'invoice_id': 'INV2024-005',
                       'project_id': 'PROJ006',
                       'hours': 7.5,
                       'rate': 100.0,
                       'hst_rate': 0.13
                   }),
            Action(name='GetInvoiceLines',
                   kwargs={'invoice_id': 'INV2024-005'}),
            Action(name='CreateDashboardSnapshot',
                   kwargs={
                       'snapshot_id': 'SNAP005',
                       'snapshot_date': '2024-05-31',
                       'year': 2024
                   })
        ],
        outputs=['INV2024-005', 'SNAP005']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_012',
        instruction=
        "Your task is to produce a quarter-wise cash flow forecast for Q4 2025, covering the period October 1, 2025 (2025-10-01), to December 31, 2025 (2025-12-31). The final analysis, which must be logged in the scheduler for 2025-09-30T17:00:00Z with a note 'Q4 2025 cash flow forecast', should find the net cash flow posed by 'Coastal Educational Resources' by comparing their total unpaid expected inflows against the company's total recurring outflows for the period. This assessment should be supported by the publisher's historical payment profile.",
        actions=[
            Action(name='GetPublisherByName',
                   kwargs={'publisher_name': 'Coastal Educational Resources'}),
            Action(name='FilterInvoices',
                   kwargs={
                       'publisher_id': 'PUB004',
                       'unpaid_only': True
                   }),
            Action(name='CalculateTotalInflows',
                   kwargs={
                       'start_date': '2025-10-01',
                       'end_date': '2025-12-31',
                       'invoices_to_consider': ['INV010', 'INV024']
                   }),
            Action(name='CalculateTotalOutflows',
                   kwargs={
                       'start_date': '2025-10-01',
                       'end_date': '2025-12-31'
                   }),
            Action(name='ComputeNetCashFlow',
                   kwargs={
                       'inflows': 3627.3,
                       'outflows': 10477.86
                   }),
            Action(name='GetPaymentBehavior',
                   kwargs={'publisher_id': 'PUB004'}),
            Action(name='AddSchedulerRun',
                   kwargs={
                       'run_date': '2025-09-30T17:00:00Z',
                       'note': 'Q4 2025 cash flow forecast'
                   })
        ],
        outputs=['PUB004', '3627.3', '10477.86', 'BEH004', -6850.56]),
    Task(
        annotator='gokulsaireddy',
        user_id='task_013',
        instruction=
        "Your task is to create a dedicated micro-invoice for the work completed under time entry 'TIME010'. The system must be updated to include a new, single-line invoice that has the 8.5 billable hours and 95.0 project rate. ('2025-T010' for $807.50 subtotal, $104.98 HST, $912.48 total_due) dated on 2025-08-26. Ensure the new invoice and its corresponding line item are created and that the action is recorded in the audit trail.",
        actions=[
            Action(name='GetTimeEntryDetails',
                   kwargs={'time_entry_id': 'TIME010'}),
            Action(name='GetProjectDetails', kwargs={'project_id': 'PROJ008'}),
            Action(name='CreateInvoice',
                   kwargs={
                       'invoice_number': '2025-T010',
                       'publisher_id': 'PUB004',
                       'subtotal': 807.5,
                       'hst_amount': 104.98,
                       'total_due': 912.48,
                       'invoice_date': '2025-08-26'
                   }),
            Action(name='CreateInvoiceLine',
                   kwargs={
                       'invoice_id': 'INV2025-T010',
                       'project_id': 'PROJ008',
                       'hours': 8.5,
                       'rate': 95.0,
                       'hst_rate': 0.13
                   }),
            Action(name='RecordInvoiceAudit',
                   kwargs={
                       'invoice_number': '2025-T010',
                       'event_type': 'created'
                   }),
            Action(name='ListInvoiceAudit',
                   kwargs={'invoice_id': 'INV2025-T010'})
        ],
        outputs=['AUD_INV2025-T010_45', 'INV2025-T010', 'LINE-0030']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_014',
        instruction=
        "Your task is to create an invoice for project 'Computer Programming Fundamentals - Updated Curriculum' as of March 25, 2026 (2026-03-25). The system should have an auditable invoice ('2026-K03') for the initial setup fee, which has a subtotal of 1400.00 CAD, HST of 182.00 CAD, and a total of 1582.00 CAD. This transaction must be fully auditable, with the invoice appearing in the financial records under a generated event, verified.The dashboard should reflect the new income, bringing year-to-date revenue for 2026 to 3100.00 CAD, and the monthly reporting confirms the same subtotal in the audit trail.",
        actions=[
            Action(name='GetProjectPublisher',
                   kwargs={
                       'name':
                       'Computer Programming Fundamentals - Updated Curriculum'
                   }),
            Action(name='CreateInvoice',
                   kwargs={
                       'invoice_number': '2026-K03',
                       'publisher_id': 'PUB003',
                       'invoice_date': '2026-03-25',
                       'subtotal': 1400.0,
                       'hst_amount': 182.0,
                       'total_due': 1582.0
                   }),
            Action(name='LogInvoiceAuditEvent',
                   kwargs={
                       'invoice_id': 'INV2026-K03',
                       'event_type': 'generated'
                   }),
            Action(name='CreateDashboardSnapshotWithInvoiceId',
                   kwargs={
                       'invoice_id': 'INV2026-K03',
                       'snapshot_date': '2026-03-25',
                       'year': 2026,
                       'ytd_revenue': 3100.0
                   }),
            Action(name='AddMonthlyAudit',
                   kwargs={
                       'snapshot_id': 'SNAP_INV2026-K03',
                       'month': '2026-03',
                       'amount': 1400.0
                   }),
            Action(name='GetMonthlyAuditBySnapshot',
                   kwargs={'snapshot_id': 'SNAP_INV2026-K03'}),
            Action(name='ListInvoiceAudit',
                   kwargs={'audit_id': 'AUD_INV2026-K03'})
        ],
        outputs=[
            'PUB003', 'INV2026-K03', 'AUD_INV2026-K03', 'SNAP_INV2026-K03',
            'SNAP_INV2026-K03_2026-03'
        ]),
    Task(
        annotator='gokulsaireddy',
        user_id='task_015',
        instruction=
        "Your task is to process a payment for invoice '2024-011'. The system must be updated to show the invoice was paid on '2025-09-02T10:00:00Z'. A 'payment_received' event must be logged in the audit trail. Finally, the balance of the primary 'checking' account must be updated to reflect the deposit, resulting in a new balance of $16285.20.",
        actions=[
            Action(name='FilterInvoices',
                   kwargs={'invoice_number': '2024-011'}),
            Action(name='UpdateInvoicePayment',
                   kwargs={
                       'invoice_id': 'INV011',
                       'paid_at': '2025-09-02T10:00:00Z'
                   }),
            Action(name='LogInvoiceAuditEvent',
                   kwargs={
                       'invoice_id': 'INV011',
                       'event_type': 'payment_received'
                   }),
            Action(name='GetBankAccountDetails',
                   kwargs={'account_type': 'checking'}),
            Action(name='UpdateBankAccountBalance',
                   kwargs={
                       'account_id': 'CHK001',
                       'balance': 16285.2
                   })
        ],
        outputs=['INV011', 'CHK001', 'AUD_INV011']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_016',
        instruction=
        "You issue an August 2024 invoice for Northern Lights Educational Books, numbered '2024-008' and dated 2024-08-31, covering the full month of August. The invoice must show a subtotal of 860.0 CAD, HST of 111.8 CAD, and a total due of 971.8 CAD. It includes a line item for project PROJ1012 with 10.0 hours at a rate of 86.0. The line details are visible, and the invoice is reflected in the August dashboard snapshot (SNAP008) dated 2024-08-31, with the snapshot confirming the updated record.",
        actions=[
            Action(
                name='GetPublisherByName',
                kwargs={'publisher_name':
                        'Northern Lights Educational Books'}),
            Action(name='CreateInvoice',
                   kwargs={
                       'invoice_number': '2024-008',
                       'publisher_id': 'PUB002',
                       'invoice_date': '2024-08-31',
                       'period_start': '2024-08-01',
                       'period_end': '2024-08-31',
                       'subtotal': 860.0,
                       'hst_amount': 111.8,
                       'total_due': 971.8
                   }),
            Action(name='CreateInvoiceLine',
                   kwargs={
                       'invoice_id': 'INV2024-008',
                       'project_id': 'PROJ1012',
                       'hours': 10.0,
                       'rate': 86.0,
                       'hst_rate': 0.13
                   }),
            Action(name='GetInvoiceLines',
                   kwargs={'invoice_id': 'INV2024-008'}),
            Action(name='CreateDashboardSnapshot',
                   kwargs={
                       'snapshot_id': 'SNAP008',
                       'snapshot_date': '2024-08-31',
                       'year': 2024
                   }),
            Action(name='GetDashboardSnapshot',
                   kwargs={'snapshot_id': 'SNAP008'})
        ],
        outputs=['INV2024-008', 'SNAP008']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_017',
        instruction=
        "Your task is to create a dedicated financial snapshot for the 'Advanced Mathematics Textbook - Grade 12' project. The snapshot, with ID 'SNAP_PROJ001', must be dated for 2025-08-31 for the year 2025. Before creating the report, you must confirm that the project's total lifetime logged hours is 23.5. The final snapshot must be populated with the project's total lifetime revenue of $1997.50, using the record ID 'PR_SNAP001_PROJ001'.",
        actions=[
            Action(name='GetProjectByName',
                   kwargs={
                       'project_name':
                       'Advanced Mathematics Textbook - Grade 12'
                   }),
            Action(name='GetProjectTimeEntries',
                   kwargs={'project_id': 'PROJ001'}),
            Action(name='CreateDashboardSnapshot',
                   kwargs={
                       'snapshot_id': 'SNAP_PROJ001',
                       'snapshot_date': '2025-08-31',
                       'year': 2025
                   }),
            Action(name='AddProjectRevenue',
                   kwargs={
                       'row_id': 'PR_SNAP001_PROJ001',
                       'snapshot_id': 'SNAP_PROJ001',
                       'project_id': 'PROJ001',
                       'revenue': 1997.5
                   }),
            Action(name='GetProjectRevenueSummary',
                   kwargs={'snapshot_id': 'SNAP_PROJ001'})
        ],
        outputs=['PROJ001', 'SNAP_PROJ001', 'PR_SNAP001_PROJ001', 23.5]),
    Task(
        annotator='gokulsaireddy',
        user_id='task_018',
        instruction=
        "Your task is to process a payment for invoice '2024-024'. The system must be updated to show the invoice was paid on '2025-09-03T10:00:00Z'. A 'payment_received' event must be logged in the audit trail. Finally, the balance of the primary 'checking' account must be updated to reflect the deposit, resulting in a new balance of $17511.25.",
        actions=[
            Action(name='FilterInvoices',
                   kwargs={'invoice_number': '2024-024'}),
            Action(name='UpdateInvoicePayment',
                   kwargs={
                       'invoice_id': 'INV024',
                       'paid_at': '2025-09-03T10:00:00Z'
                   }),
            Action(name='LogInvoiceAuditEvent',
                   kwargs={
                       'invoice_id': 'INV024',
                       'event_type': 'payment_received'
                   }),
            Action(name='GetBankAccountDetails',
                   kwargs={'account_type': 'checking'}),
            Action(name='UpdateBankAccountBalance',
                   kwargs={
                       'account_id': 'CHK001',
                       'balance': 17511.25
                   })
        ],
        outputs=['INV024', 'CHK001', 'AUD_INV024']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_019',
        instruction=
        "You issue a June 2024 invoice for Maple Leaf Publishing House, numbered '2024-006' and dated 2024-06-30, covering the full month of June. The invoice must show a subtotal of 1200.0 CAD, HST of 156.0 CAD, and a total due of 1356.0 CAD. It includes a line item for project PROJ003 with 16.0 hours at a rate of 75.0. The line details are visible, and the invoice is reflected in the June dashboard snapshot (SNAP006) dated 2024-06-30, with the snapshot confirming the updated record.",
        actions=[
            Action(name='GetPublisherByName',
                   kwargs={'publisher_name': 'Maple Leaf Publishing House'}),
            Action(name='CreateInvoice',
                   kwargs={
                       'invoice_number': '2024-006',
                       'publisher_id': 'PUB001',
                       'invoice_date': '2024-06-30',
                       'period_start': '2024-06-01',
                       'period_end': '2024-06-30',
                       'subtotal': 1200.0,
                       'hst_amount': 156.0,
                       'total_due': 1356.0
                   }),
            Action(name='CreateInvoiceLine',
                   kwargs={
                       'invoice_id': 'INV2024-006',
                       'project_id': 'PROJ003',
                       'hours': 16.0,
                       'rate': 75.0,
                       'hst_rate': 0.13
                   }),
            Action(name='GetInvoiceLines',
                   kwargs={'invoice_id': 'INV2024-006'}),
            Action(name='CreateDashboardSnapshot',
                   kwargs={
                       'snapshot_id': 'SNAP006',
                       'snapshot_date': '2024-06-30',
                       'year': 2024
                   }),
            Action(name='GetDashboardSnapshot',
                   kwargs={'snapshot_id': 'SNAP006'})
        ],
        outputs=['INV2024-006', 'SNAP006']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_020',
        instruction=
        "You log a May 2024 travel expense of 543.21 CAD for 'Air Canada', paid by Business Credit Card on 2024-05-22 under category TRAVEL_EXPENSE. This expense is captured with id 'EXP_0070' and dated 2024-05-22. It must also appear in the May 2024 dashboard snapshot with SNAP005, dated 2024-05-31, where the monthly totals include this expense with amount 543.21 CAD.",
        actions=[
            Action(name='GetExpensesByCategory',
                   kwargs={'category_code': 'TRAVEL_EXPENSE'}),
            Action(name='AddExpenseRecord',
                   kwargs={
                       'expense_id': 'EXP_0070',
                       'vendor': 'Air Canada',
                       'expense_date': '2024-05-22',
                       'amount': 543.21,
                       'payment_method': 'Business Credit Card',
                       'category_code': 'TRAVEL_EXPENSE'
                   }),
            Action(name='GetExpensesByCategory',
                   kwargs={'category_code': 'TRAVEL_EXPENSE'}),
            Action(name='CreateDashboardSnapshot',
                   kwargs={
                       'snapshot_id': 'SNAP005',
                       'snapshot_date': '2024-05-31',
                       'year': 2024
                   }),
            Action(name='AddMonthlyExpense',
                   kwargs={
                       'snapshot_id': 'SNAP005',
                       'month': '2024-05',
                       'amount': 543.21
                   }),
            Action(name='GetMonthlyExpenseBySnapshot',
                   kwargs={'snapshot_id': 'SNAP005'}),
            Action(name='GetDashboardSnapshot',
                   kwargs={'snapshot_id': 'SNAP005'})
        ],
        outputs=['SNAP005_2024-05', 'SNAP005']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_021',
        instruction=
        "Your task is to create an invoice for project 'Business Communications Handbook - 2nd Edition' as of February 25, 2026 (2026-02-25). The system should include an auditable invoice ('2026-K002') for the initial setup fee, which has a subtotal of 800.00 CAD, HST of 104.00 CAD, and a total of 904.00 CAD. Also, audit this invoice with a 'generated' event and verify it. Furthermore, a financial dashboard for the date must be created for this new income, showing a new year-to-date revenue of 1700.00 CAD. Finally, include a monthly audit with the same subtotal and verify it.",
        actions=[
            Action(name='GetProjectPublisher',
                   kwargs={
                       'name': 'Business Communications Handbook - 2nd Edition'
                   }),
            Action(name='CreateInvoice',
                   kwargs={
                       'invoice_number': '2026-K002',
                       'publisher_id': 'PUB005',
                       'invoice_date': '2026-02-25',
                       'subtotal': 800.0,
                       'hst_amount': 104.0,
                       'total_due': 904.0
                   }),
            Action(name='LogInvoiceAuditEvent',
                   kwargs={
                       'invoice_id': 'INV2026-K002',
                       'event_type': 'generated'
                   }),
            Action(name='CreateDashboardSnapshotWithInvoiceId',
                   kwargs={
                       'invoice_id': 'INV2026-K002',
                       'snapshot_date': '2026-02-25',
                       'year': 2026,
                       'ytd_revenue': 1700.0
                   }),
            Action(name='AddMonthlyAudit',
                   kwargs={
                       'snapshot_id': 'SNAP_INV2026-K002',
                       'month': '2026-02',
                       'amount': 800.0
                   }),
            Action(name='GetMonthlyAuditBySnapshot',
                   kwargs={'snapshot_id': 'SNAP_INV2026-K002'}),
            Action(name='ListInvoiceAudit',
                   kwargs={'audit_id': 'AUD_INV2026-K002'})
        ],
        outputs=[
            'PUB005', 'INV2026-K002', 'AUD_INV2026-K002', 'SNAP_INV2026-K002',
            'SNAP_INV2026-K002_2026-02'
        ]),
    Task(
        annotator='gokulsaireddy',
        user_id='task_022',
        instruction=
        "Your task is to process a payment for invoice '2024-009'. The system must be updated to show the invoice was paid on '2025-08-31T11:00:00Z'. A 'payment_received' event must be logged in the audit trail. Finally, the balance of the primary 'checking' account must be updated to reflect the deposit, resulting in a new balance of $16112.31.",
        actions=[
            Action(name='FilterInvoices',
                   kwargs={'invoice_number': '2024-009'}),
            Action(name='UpdateInvoicePayment',
                   kwargs={
                       'invoice_id': 'INV009',
                       'paid_at': '2025-08-31T11:00:00Z'
                   }),
            Action(name='LogInvoiceAuditEvent',
                   kwargs={
                       'invoice_id': 'INV009',
                       'event_type': 'payment_received'
                   }),
            Action(name='GetBankAccountDetails',
                   kwargs={'account_type': 'checking'}),
            Action(name='UpdateBankAccountBalance',
                   kwargs={
                       'account_id': 'CHK001',
                       'balance': 16112.31
                   })
        ],
        outputs=['INV009', 'CHK001', 'AUD_INV009']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_023',
        instruction=
        "You log a September 2024 office supplies expense of 1299.99 CAD for 'Dell Canada', paid by Business Credit Card on 2024-09-05 under category OFFICE_SUPPLIES. This expense is captured with id 'EXP_0120' and dated on 2024-09-05. It must also appear in the September 2024 dashboard snapshot with SNAP009, dated 2024-09-30, where the monthly totals include this expense with amount 1299.99 CAD.",
        actions=[
            Action(name='GetExpensesByCategory',
                   kwargs={'category_code': 'OFFICE_SUPPLIES'}),
            Action(name='AddExpenseRecord',
                   kwargs={
                       'expense_id': 'EXP_0120',
                       'vendor': 'Dell Canada',
                       'expense_date': '2024-09-05',
                       'amount': 1299.99,
                       'payment_method': 'Business Credit Card',
                       'category_code': 'OFFICE_SUPPLIES'
                   }),
            Action(name='GetExpensesByCategory',
                   kwargs={'category_code': 'OFFICE_SUPPLIES'}),
            Action(name='CreateDashboardSnapshot',
                   kwargs={
                       'snapshot_id': 'SNAP009',
                       'snapshot_date': '2024-09-30',
                       'year': 2024
                   }),
            Action(name='AddMonthlyExpense',
                   kwargs={
                       'snapshot_id': 'SNAP009',
                       'month': '2024-09',
                       'amount': 1299.99
                   }),
            Action(name='GetMonthlyExpenseBySnapshot',
                   kwargs={'snapshot_id': 'SNAP009'}),
            Action(name='GetDashboardSnapshot',
                   kwargs={'snapshot_id': 'SNAP009'})
        ],
        outputs=['SNAP009_2024-09', 'SNAP009']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_024',
        instruction=
        "Your task is to set up the new publisher 'Quantum Education Partners' ('PUB051') and their initial project, 'Intro to Quantum Mechanics, 2e' ('PROJ4002'), with ISBN '978-2-5200-4002-2' and a default hourly rate of 110.0. The end state for the November 2024 context should show that the new publisher and project are readable, all unpaid invoices have been reviewed, 12-month KPIs are available, a sample invoice total for 1.5 hours at the project rate with 13% HST has been calculated, and the A/R aging report for '2024-11' has been exported.",
        actions=[
            Action(name='CreatePublisher',
                   kwargs={
                       'publisher_id': 'PUB051',
                       'name': 'Quantum Education Partners'
                   }),
            Action(name='GetPublisherInfo', kwargs={'publisher_id': 'PUB051'}),
            Action(name='CreateProject',
                   kwargs={
                       'project_id': 'PROJ4002',
                       'publisher_id': 'PUB051',
                       'isbn': '978-2-5200-4002-2',
                       'project_title': 'Intro to Quantum Mechanics, 2e',
                       'default_hourly_rate': 110.0
                   }),
            Action(name='GetProjectDetails', kwargs={'project_id':
                                                     'PROJ4002'}),
            Action(name='FilterInvoices', kwargs={'unpaid_only': True}),
            Action(name='ComputeCollectionKPIs', kwargs={'window_months': 12}),
            Action(name='CalculateInvoiceTotals',
                   kwargs={
                       'lines': [{
                           'hours': 1.5,
                           'rate': 110.0
                       }],
                       'hst_rate': 0.13
                   }),
            Action(name='ExportARAgingReport',
                   kwargs={'period_label': '2024-11'})
        ],
        outputs=[
            'PUB051', '/reports/ar_aging/AR_Aging_Report_2024-11.pdf', 21.45,
            186.45, 165.0
        ]),
    Task(
        annotator='gokulsaireddy',
        user_id='task_025',
        instruction=
        "Your task is to perform a full onboarding for the new publisher 'Artisan Culinary Books' ('PUB060') with contact mail 'invoices@artisan-culinary.com' as of September 2025. The end state must show that the publisher and their new project, 'The Art of Pastry Making' ('PROJ4011'), with isbn '978-2-2100-4011-2' at a 115.0 hourly rate have been created. Furthermore, their first setup fee invoice ('2025-B005' for $1800.00 subtotal, $234.00 HST, $2034.00 total_due) must be created dated 2025-09-01, and immediately emailed to the client with subject: '2025-B005'.",
        actions=[
            Action(name='CreatePublisher',
                   kwargs={
                       'publisher_id': 'PUB060',
                       'name': 'Artisan Culinary Books',
                       'contact_email': 'invoices@artisan-culinary.com'
                   }),
            Action(name='GetPublisherInfo', kwargs={'publisher_id': 'PUB060'}),
            Action(name='CreateProject',
                   kwargs={
                       'project_id': 'PROJ4011',
                       'publisher_id': 'PUB060',
                       'isbn': '978-2-2100-4011-2',
                       'project_title': 'The Art of Pastry Making',
                       'default_hourly_rate': 115.0
                   }),
            Action(name='GetProjectDetails', kwargs={'project_id':
                                                     'PROJ4011'}),
            Action(name='CreateInvoice',
                   kwargs={
                       'invoice_number': '2025-B005',
                       'publisher_id': 'PUB060',
                       'subtotal': 1800.0,
                       'hst_amount': 234.0,
                       'total_due': 2034.0,
                       'invoice_date': '2025-09-01'
                   }),
            Action(name='SendInvoiceEmail',
                   kwargs={
                       'publisher_id': 'PUB060',
                       'invoice_number': '2025-B005',
                       'subject': '2025-B005'
                   }),
            Action(name='GetInvoiceDetails',
                   kwargs={'invoice_number': '2025-B005'})
        ],
        outputs=['INV2025-B005']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_026',
        instruction=
        "Your task is to process a payment for invoice '2024-013'. The system must be updated to show the invoice was paid on '2025-09-04T10:00:00Z'. A 'payment_received' event must be logged in the audit trail. Finally, the balance of the primary 'checking' account must be updated to reflect the deposit, resulting in a new balance of $16437.75.",
        actions=[
            Action(name='FilterInvoices',
                   kwargs={'invoice_number': '2024-013'}),
            Action(name='UpdateInvoicePayment',
                   kwargs={
                       'invoice_id': 'INV013',
                       'paid_at': '2025-09-04T10:00:00Z'
                   }),
            Action(name='LogInvoiceAuditEvent',
                   kwargs={
                       'invoice_id': 'INV013',
                       'event_type': 'payment_received'
                   }),
            Action(name='GetBankAccountDetails',
                   kwargs={'account_type': 'checking'}),
            Action(name='UpdateBankAccountBalance',
                   kwargs={
                       'account_id': 'CHK001',
                       'balance': 16437.75
                   })
        ],
        outputs=['INV013', 'CHK001', 'AUD_INV013']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_027',
        instruction=
        "Your task is to create an invoice for project 'Economics Textbook Revision - 3rd Edition' as of September 25, 2025 (2025-09-25). The system should include an auditable invoice ('2025-K002') for the initial setup fee, which has a subtotal of 750.00 CAD, HST of 97.50 CAD, and a total of 847.50 CAD. Also, audit this invoice with a 'generated' event and verify it. Furthermore, a financial dashboard for the date must be created for this new income, showing a new year-to-date revenue of 11563.78 CAD. Finally, include a monthly audit with the same subtotal and verify it.",
        actions=[
            Action(
                name='GetProjectPublisher',
                kwargs={'name': 'Economics Textbook Revision - 3rd Edition'}),
            Action(name='CreateInvoice',
                   kwargs={
                       'invoice_number': '2025-K002',
                       'publisher_id': 'PUB001',
                       'invoice_date': '2025-09-25',
                       'subtotal': 750.0,
                       'hst_amount': 97.5,
                       'total_due': 847.5
                   }),
            Action(name='LogInvoiceAuditEvent',
                   kwargs={
                       'invoice_id': 'INV2025-K002',
                       'event_type': 'generated'
                   }),
            Action(name='CreateDashboardSnapshotWithInvoiceId',
                   kwargs={
                       'invoice_id': 'INV2025-K002',
                       'snapshot_date': '2025-09-25',
                       'year': 2025,
                       'ytd_revenue': 11563.78
                   }),
            Action(name='AddMonthlyAudit',
                   kwargs={
                       'snapshot_id': 'SNAP_INV2025-K002',
                       'month': '2025-09',
                       'amount': 750.0
                   }),
            Action(name='GetMonthlyAuditBySnapshot',
                   kwargs={'snapshot_id': 'SNAP_INV2025-K002'}),
            Action(name='ListInvoiceAudit',
                   kwargs={'audit_id': 'AUD_INV2025-K002'})
        ],
        outputs=[
            'PUB001', 'INV2025-K002', 'AUD_INV2025-K002', 'SNAP_INV2025-K002',
            'SNAP_INV2025-K002_2025-09'
        ]),
    Task(
        annotator='gokulsaireddy',
        user_id='task_028',
        instruction=
        "You log a November 2024 advertising expense of 216.00 CAD for 'Squarespace', paid by Business Credit Card on 2024-11-15 under category ADVERTISING. This expense is captured with id 'EXP_0150' and dated on 2024-11-15. It must also appear in the November 2024 dashboard snapshot with SNAP011, dated 2024-11-30, where the monthly totals include this expense with amount 216.00 CAD.",
        actions=[
            Action(name='GetExpensesByCategory',
                   kwargs={'category_code': 'ADVERTISING'}),
            Action(name='AddExpenseRecord',
                   kwargs={
                       'expense_id': 'EXP_0150',
                       'vendor': 'Squarespace',
                       'expense_date': '2024-11-15',
                       'amount': 216.0,
                       'payment_method': 'Business Credit Card',
                       'category_code': 'ADVERTISING'
                   }),
            Action(name='GetExpensesByCategory',
                   kwargs={'category_code': 'ADVERTISING'}),
            Action(name='CreateDashboardSnapshot',
                   kwargs={
                       'snapshot_id': 'SNAP011',
                       'snapshot_date': '2024-11-30',
                       'year': 2024
                   }),
            Action(name='AddMonthlyExpense',
                   kwargs={
                       'snapshot_id': 'SNAP011',
                       'month': '2024-11',
                       'amount': 216.0
                   }),
            Action(name='GetMonthlyExpenseBySnapshot',
                   kwargs={'snapshot_id': 'SNAP011'}),
            Action(name='GetDashboardSnapshot',
                   kwargs={'snapshot_id': 'SNAP011'})
        ],
        outputs=['SNAP011_2024-11', 'SNAP011']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_029',
        instruction=
        "Your task is to process a payment for invoice '2024-021'. The system must be updated to show the invoice was paid on '2025-08-29T12:00:00Z'. A 'payment_received' event must be logged in the audit trail. Finally, the balance of the primary 'checking' account must be updated to reflect the deposit, resulting in a new balance of $16833.25.",
        actions=[
            Action(name='FilterInvoices',
                   kwargs={'invoice_number': '2024-021'}),
            Action(name='UpdateInvoicePayment',
                   kwargs={
                       'invoice_id': 'INV021',
                       'paid_at': '2025-08-29T12:00:00Z'
                   }),
            Action(name='LogInvoiceAuditEvent',
                   kwargs={
                       'invoice_id': 'INV021',
                       'event_type': 'payment_received'
                   }),
            Action(name='GetBankAccountDetails',
                   kwargs={'account_type': 'checking'}),
            Action(name='UpdateBankAccountBalance',
                   kwargs={
                       'account_id': 'CHK001',
                       'balance': 16833.25
                   })
        ],
        outputs=['INV021', 'CHK001', 'AUD_INV021']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_030',
        instruction=
        "You need to execute the onboarding for the new client 'Mindful Growth Books' ('PUB063') and their email 'billing@mindfulgrowth.org' in the context of September 2025. The publisher and their first project, 'Psychology of Human Behavior' ('PROJ4014', ISBN '978-5-2400-4014-5', rate 90.0), must be added to the system. You must also generate and email their first invoice, '2026-B008', for a subtotal of $1300.00 plus $169.00 HST ($1469.00 total) dated 2025-09-01.",
        actions=[
            Action(name='CreatePublisher',
                   kwargs={
                       'publisher_id': 'PUB063',
                       'name': 'Mindful Growth Books',
                       'contact_email': 'billing@mindfulgrowth.org'
                   }),
            Action(name='GetPublisherInfo', kwargs={'publisher_id': 'PUB063'}),
            Action(name='CreateProject',
                   kwargs={
                       'project_id': 'PROJ4014',
                       'publisher_id': 'PUB063',
                       'isbn': '978-5-2400-4014-5',
                       'project_title': 'Psychology of Human Behavior',
                       'default_hourly_rate': 90.0
                   }),
            Action(name='GetProjectDetails', kwargs={'project_id':
                                                     'PROJ4014'}),
            Action(name='CreateInvoice',
                   kwargs={
                       'invoice_number': '2026-B008',
                       'publisher_id': 'PUB063',
                       'subtotal': 1300.0,
                       'hst_amount': 169.0,
                       'total_due': 1469.0,
                       'invoice_date': '2025-09-01'
                   }),
            Action(name='SendInvoiceEmail',
                   kwargs={
                       'publisher_id': 'PUB063',
                       'invoice_number': '2026-B008',
                       'subject': '2026-B008'
                   }),
            Action(name='GetInvoiceDetails',
                   kwargs={'invoice_number': '2026-B008'})
        ],
        outputs=['INV2026-B008']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_031',
        instruction=
        "You log a May 2024 travel expense of 289.99 CAD for 'Fairmont Hotel Vancouver', paid by Business Credit Card on 2024-05-23 under category TRAVEL_EXPENSE. This expense is captured with id 'EXP_0080' and dated 2024-05-23. It must also appear in the May 2024 dashboard snapshot with SNAP005, dated 2024-05-31, where the monthly totals include this expense with amount 289.99 CAD.",
        actions=[
            Action(name='GetExpensesByCategory',
                   kwargs={'category_code': 'TRAVEL_EXPENSE'}),
            Action(name='AddExpenseRecord',
                   kwargs={
                       'expense_id': 'EXP_0080',
                       'vendor': 'Fairmont Hotel Vancouver',
                       'expense_date': '2024-05-23',
                       'amount': 289.99,
                       'payment_method': 'Business Credit Card',
                       'category_code': 'TRAVEL_EXPENSE'
                   }),
            Action(name='GetExpensesByCategory',
                   kwargs={'category_code': 'TRAVEL_EXPENSE'}),
            Action(name='CreateDashboardSnapshot',
                   kwargs={
                       'snapshot_id': 'SNAP005',
                       'snapshot_date': '2024-05-31',
                       'year': 2024
                   }),
            Action(name='AddMonthlyExpense',
                   kwargs={
                       'snapshot_id': 'SNAP005',
                       'month': '2024-05',
                       'amount': 289.99
                   }),
            Action(name='GetMonthlyExpenseBySnapshot',
                   kwargs={'snapshot_id': 'SNAP005'}),
            Action(name='GetDashboardSnapshot',
                   kwargs={'snapshot_id': 'SNAP005'})
        ],
        outputs=['SNAP005_2024-05', 'SNAP005']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_032',
        instruction=
        "Your goal is to complete setup and invoicing for the new publisher 'Momentum Sports Science' ('PUB064', contact 'ap@momentumsports.sci') as of September 2025. The end state requires the creation of the publisher and their project 'Biomechanics of Athletic Performance' ('PROJ4015') with a rate of 125.0 and ISBN '978-6-2500-4015-6'. Conclude by creating and emailing invoice '2026-B009' for $2486.00 total ($2200.00 subtotal + $286.00 HST) on 2025-09-01.",
        actions=[
            Action(name='CreatePublisher',
                   kwargs={
                       'publisher_id': 'PUB064',
                       'name': 'Momentum Sports Science',
                       'contact_email': 'ap@momentumsports.sci'
                   }),
            Action(name='GetPublisherInfo', kwargs={'publisher_id': 'PUB064'}),
            Action(name='CreateProject',
                   kwargs={
                       'project_id': 'PROJ4015',
                       'publisher_id': 'PUB064',
                       'isbn': '978-6-2500-4015-6',
                       'project_title': 'Biomechanics of Athletic Performance',
                       'default_hourly_rate': 125.0
                   }),
            Action(name='GetProjectDetails', kwargs={'project_id':
                                                     'PROJ4015'}),
            Action(name='CreateInvoice',
                   kwargs={
                       'invoice_number': '2026-B009',
                       'publisher_id': 'PUB064',
                       'subtotal': 2200.0,
                       'hst_amount': 286.0,
                       'total_due': 2486.0,
                       'invoice_date': '2025-09-01'
                   }),
            Action(name='SendInvoiceEmail',
                   kwargs={
                       'publisher_id': 'PUB064',
                       'invoice_number': '2026-B009',
                       'subject': '2026-B009'
                   }),
            Action(name='GetInvoiceDetails',
                   kwargs={'invoice_number': '2026-B009'})
        ],
        outputs=['INV2026-B009']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_033',
        instruction=
        "Your task is to process a payment for invoice '2024-022'. The system must be updated to show the invoice was paid on '2025-08-28T11:00:00Z'. A 'payment_received' event must be logged in the audit trail. Finally, the balance of the primary 'checking' account must be updated to reflect the deposit, resulting in a new balance of $16409.50.",
        actions=[
            Action(name='FilterInvoices',
                   kwargs={'invoice_number': '2024-022'}),
            Action(name='UpdateInvoicePayment',
                   kwargs={
                       'invoice_id': 'INV022',
                       'paid_at': '2025-08-28T11:00:00Z'
                   }),
            Action(name='LogInvoiceAuditEvent',
                   kwargs={
                       'invoice_id': 'INV022',
                       'event_type': 'payment_received'
                   }),
            Action(name='GetBankAccountDetails',
                   kwargs={'account_type': 'checking'}),
            Action(name='UpdateBankAccountBalance',
                   kwargs={
                       'account_id': 'CHK001',
                       'balance': 16409.5
                   })
        ],
        outputs=['INV022', 'CHK001', 'AUD_INV022']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_034',
        instruction=
        "You log an April 2024 vehicle expense of 78.45 CAD for 'Shell Canada', paid by Business Credit Card on 2024-04-08 under category VEHICLE_EXPENSE. This expense is captured with id 'EXP006' and dated 2024-04-08. It must also appear in the April 2024 dashboard snapshot with SNAP004, dated 2024-04-30, where the monthly totals include this expense with amount 78.45 CAD.",
        actions=[
            Action(name='AddExpenseRecord',
                   kwargs={
                       'expense_id': 'EXP006',
                       'vendor': 'Shell Canada',
                       'expense_date': '2024-04-08',
                       'amount': 78.45,
                       'payment_method': 'Business Credit Card',
                       'category_code': 'VEHICLE_EXPENSE'
                   }),
            Action(name='CreateDashboardSnapshot',
                   kwargs={
                       'snapshot_id': 'SNAP004',
                       'snapshot_date': '2024-04-30',
                       'year': 2024
                   }),
            Action(name='AddMonthlyExpense',
                   kwargs={
                       'snapshot_id': 'SNAP004',
                       'month': '2024-04',
                       'amount': 78.45
                   }),
            Action(name='GetMonthlyExpenseBySnapshot',
                   kwargs={'snapshot_id': 'SNAP004'}),
            Action(name='GetDashboardSnapshot',
                   kwargs={'snapshot_id': 'SNAP004'})
        ],
        outputs=['SNAP004_2024-04', 'SNAP004']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_035',
        instruction=
        "Your task is to properly document a significant equipment expense of $2100.00 from 'Dell Canada' dated 2025-12-10, which is associated with project 'Computer Science Programming Fundamentals'. Also, create a financial snapshot for December 2025 with ID 'SNAP_EXP_1225', dated 2025-12-31 and log the month's existing total expenses of $0.00. Create a new Dell Canada expense record with ID 'EXP_DELL_001' under the 'OFFICE_SUPPLIES' category. Ensure the main 'checking' account balance is updated to reflect this new expenditure, resulting in a final balance of $13320.75.",
        actions=[
            Action(name='GetProjectByName',
                   kwargs={
                       'project_name':
                       'Computer Science Programming Fundamentals'
                   }),
            Action(name='CreateDashboardSnapshot',
                   kwargs={
                       'snapshot_id': 'SNAP_EXP_1225',
                       'snapshot_date': '2025-12-31',
                       'year': 2025
                   }),
            Action(name='AddMonthlyExpense',
                   kwargs={
                       'snapshot_id': 'SNAP_EXP_1225',
                       'month': '2025-12',
                       'amount': 0.0
                   }),
            Action(name='AddExpenseRecord',
                   kwargs={
                       'expense_id': 'EXP_DELL_001',
                       'project_id': 'PROJ008',
                       'vendor': 'Dell Canada',
                       'expense_date': '2025-12-10',
                       'amount': 2100.0,
                       'category_code': 'OFFICE_SUPPLIES'
                   }),
            Action(name='GetBankAccountDetails',
                   kwargs={'account_type': 'checking'}),
            Action(name='UpdateBankAccountBalance',
                   kwargs={
                       'account_id': 'CHK001',
                       'balance': 13320.75
                   })
        ],
        outputs=['CHK001', 'SNAP_EXP_1225_2025-12', 'CHK001']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_036',
        instruction=
        "You log a March 2024 professional fees expense of 450.00 CAD for 'H&R Block', paid by Business Bank Transfer on 2024-03-15 under category PROF_FEES. This expense is captured with id 'EXP_005' and dated 2024-03-15. It must also appear in the March 2024 dashboard snapshot with SNAP003, dated 2024-03-31, where the monthly totals include this expense with amount 450.00 CAD.",
        actions=[
            Action(name='GetExpensesByCategory',
                   kwargs={'category_code': 'PROF_FEES'}),
            Action(name='AddExpenseRecord',
                   kwargs={
                       'expense_id': 'EXP_005',
                       'vendor': 'H&R Block',
                       'expense_date': '2024-03-15',
                       'amount': 450.0,
                       'payment_method': 'Business Bank Transfer',
                       'category_code': 'PROF_FEES'
                   }),
            Action(name='GetExpensesByCategory',
                   kwargs={'category_code': 'PROF_FEES'}),
            Action(name='CreateDashboardSnapshot',
                   kwargs={
                       'snapshot_id': 'SNAP003',
                       'snapshot_date': '2024-03-31',
                       'year': 2024
                   }),
            Action(name='AddMonthlyExpense',
                   kwargs={
                       'snapshot_id': 'SNAP003',
                       'month': '2024-03',
                       'amount': 450.0
                   }),
            Action(name='GetMonthlyExpenseBySnapshot',
                   kwargs={'snapshot_id': 'SNAP003'}),
            Action(name='GetDashboardSnapshot',
                   kwargs={'snapshot_id': 'SNAP003'})
        ],
        outputs=['SNAP003_2024-03', 'SNAP003']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_037',
        instruction=
        "Your task is to create a dedicated financial snapshot for the 'Physics Problem Solving Handbook' project. The snapshot, with ID 'SNAP_PROJ005', must be dated for 2025-08-31 for the year 2025. Before creating the report, you must confirm that the project's total lifetime logged hours is 19.0. The final snapshot must be populated with the project's total lifetime revenue of $1710.00, using the record ID 'PR_SNAP005_PROJ005'.",
        actions=[
            Action(name='GetProjectByName',
                   kwargs={'project_name':
                           'Physics Problem Solving Handbook'}),
            Action(name='GetProjectTimeEntries',
                   kwargs={'project_id': 'PROJ005'}),
            Action(name='CreateDashboardSnapshot',
                   kwargs={
                       'snapshot_id': 'SNAP_PROJ005',
                       'snapshot_date': '2025-08-31',
                       'year': 2025
                   }),
            Action(name='AddProjectRevenue',
                   kwargs={
                       'row_id': 'PR_SNAP005_PROJ005',
                       'snapshot_id': 'SNAP_PROJ005',
                       'project_id': 'PROJ005',
                       'revenue': 1710.0
                   }),
            Action(name='GetProjectRevenueSummary',
                   kwargs={'snapshot_id': 'SNAP_PROJ005'})
        ],
        outputs=['PROJ005', 'SNAP_PROJ005', 'PR_SNAP005_PROJ005', 19.0]),
    Task(
        annotator='gokulsaireddy',
        user_id='task_038',
        instruction=
        "You log an October 2024 office rent expense of 15.67 CAD for 'Enbridge Gas', paid by Business Bank Transfer on 2024-10-15 under category OFFICE_RENT. This expense is captured with id 'EXP_0130' and dated on 2024-10-15. It must also appear in the October 2024 dashboard snapshot with SNAP010, dated 2024-10-31, where the monthly totals include this expense with amount 15.67 CAD.",
        actions=[
            Action(name='GetExpensesByCategory',
                   kwargs={'category_code': 'OFFICE_RENT'}),
            Action(name='AddExpenseRecord',
                   kwargs={
                       'expense_id': 'EXP_0130',
                       'vendor': 'Enbridge Gas',
                       'expense_date': '2024-10-15',
                       'amount': 15.67,
                       'payment_method': 'Business Bank Transfer',
                       'category_code': 'OFFICE_RENT'
                   }),
            Action(name='GetExpensesByCategory',
                   kwargs={'category_code': 'OFFICE_RENT'}),
            Action(name='CreateDashboardSnapshot',
                   kwargs={
                       'snapshot_id': 'SNAP010',
                       'snapshot_date': '2024-10-31',
                       'year': 2024
                   }),
            Action(name='AddMonthlyExpense',
                   kwargs={
                       'snapshot_id': 'SNAP010',
                       'month': '2024-10',
                       'amount': 15.67
                   }),
            Action(name='GetMonthlyExpenseBySnapshot',
                   kwargs={'snapshot_id': 'SNAP010'}),
            Action(name='GetDashboardSnapshot',
                   kwargs={'snapshot_id': 'SNAP010'})
        ],
        outputs=['SNAP010_2024-10', 'SNAP010']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_039',
        instruction=
        "Your task is to properly document a significant supply expense of $1120.00 from 'Sigma-Aldrich' dated 2025-08-28, which is associated with project 'Chemistry Lab Procedures Manual'. Also, create a financial snapshot for August 2025 with ID 'SNAP_EXP_0825_D' dated 2025-08-31 and log the month's existing total expenses of $831.65. Create a new Sigma-Aldrich expense record with ID 'EXP_SIGMA_001' under the 'OFFICE_SUPPLIES' category. Ensure the main 'checking' account balance is updated to reflect this new expenditure, resulting in a final balance of $14300.75.",
        actions=[
            Action(name='GetProjectByName',
                   kwargs={'project_name': 'Chemistry Lab Procedures Manual'}),
            Action(name='CreateDashboardSnapshot',
                   kwargs={
                       'snapshot_id': 'SNAP_EXP_0825_D',
                       'snapshot_date': '2025-08-31',
                       'year': 2025
                   }),
            Action(name='AddMonthlyExpense',
                   kwargs={
                       'snapshot_id': 'SNAP_EXP_0825_D',
                       'month': '2025-08',
                       'amount': 831.65
                   }),
            Action(name='AddExpenseRecord',
                   kwargs={
                       'expense_id': 'EXP_SIGMA_001',
                       'project_id': 'PROJ006',
                       'vendor': 'Sigma-Aldrich',
                       'expense_date': '2025-08-28',
                       'amount': 1120.0,
                       'category_code': 'OFFICE_SUPPLIES'
                   }),
            Action(name='GetBankAccountDetails',
                   kwargs={'account_type': 'checking'}),
            Action(name='UpdateBankAccountBalance',
                   kwargs={
                       'account_id': 'CHK001',
                       'balance': 14300.75
                   })
        ],
        outputs=['CHK001', 'SNAP_EXP_0825_D_2025-08']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_040',
        instruction=
        "Your task is to set up the new publisher 'Blue Shore Academics' ('PUB049') and their initial project, 'Civics Foundations, 1e' ('PROJ3069'), with ISBN '978-1-3100-3069-4' and a default hourly rate of 88.0. The end state for the September 2024 context should show that the new publisher and project are readable, all open invoices have been reviewed, 12-month KPIs are available, a sample invoice total for 2 hours at the project rate with 13% HST has been calculated, and the A/R aging report for '2024-09' has been exported.",
        actions=[
            Action(name='CreatePublisher',
                   kwargs={
                       'publisher_id': 'PUB049',
                       'name': 'Blue Shore Academics'
                   }),
            Action(name='GetPublisherInfo', kwargs={'publisher_id': 'PUB049'}),
            Action(name='CreateProject',
                   kwargs={
                       'project_id': 'PROJ3069',
                       'publisher_id': 'PUB049',
                       'isbn': '978-1-3100-3069-4',
                       'project_title': 'Civics Foundations, 1e',
                       'default_hourly_rate': 88.0
                   }),
            Action(name='GetProjectDetails', kwargs={'project_id':
                                                     'PROJ3069'}),
            Action(name='FilterInvoices', kwargs={'unpaid_only': True}),
            Action(name='ComputeCollectionKPIs', kwargs={'window_months': 12}),
            Action(name='CalculateInvoiceTotals',
                   kwargs={
                       'lines': [{
                           'hours': 2,
                           'rate': 88.0
                       }],
                       'hst_rate': 0.13
                   }),
            Action(name='ExportARAgingReport',
                   kwargs={'period_label': '2024-09'})
        ],
        outputs=['PUB049', 'reports/ar_aging/AR_Aging_Report_2024-09.pdf']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_041',
        instruction=
        "Your task is to create a dedicated micro-invoice for the work completed under time entry 'TIME008'. The system must be updated to include a new, single-line invoice that has the 4.0 billable hours and 100.0 project rate. ('2025-T008' for $400.00 subtotal, $52.00 HST, $452.00 total_due) dated on 2025-08-26. Ensure the new invoice and its corresponding line item are created and that the action is recorded in the audit trail.",
        actions=[
            Action(name='GetTimeEntryDetails',
                   kwargs={'time_entry_id': 'TIME008'}),
            Action(name='GetProjectDetails', kwargs={'project_id': 'PROJ006'}),
            Action(name='CreateInvoice',
                   kwargs={
                       'invoice_number': '2025-T008',
                       'publisher_id': 'PUB003',
                       'subtotal': 400.0,
                       'hst_amount': 52.0,
                       'total_due': 452.0,
                       'invoice_date': '2025-08-26'
                   }),
            Action(name='CreateInvoiceLine',
                   kwargs={
                       'invoice_id': 'INV2025-T008',
                       'project_id': 'PROJ006',
                       'hours': 4.0,
                       'rate': 100.0,
                       'hst_rate': 0.13
                   }),
            Action(name='RecordInvoiceAudit',
                   kwargs={
                       'invoice_number': '2025-T008',
                       'event_type': 'created'
                   }),
            Action(name='ListInvoiceAudit',
                   kwargs={'invoice_id': 'INV2025-T008'})
        ],
        outputs=['AUD_INV2025-T008_45', 'INV2025-T008', 'LINE-0030']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_042',
        instruction=
        "Your task is to create a dedicated micro-invoice for the work completed under time entry 'TIME011'. The system must be updated to include a new, single-line invoice that has the 6.0 billable hours and 85.0 project rate. ('2025-T011' for $510.00 subtotal, $66.30 HST, $576.30 total_due) dated on 2025-08-26. Ensure the new invoice and its corresponding line item are created and that the action is recorded in the audit trail.",
        actions=[
            Action(name='GetTimeEntryDetails',
                   kwargs={'time_entry_id': 'TIME011'}),
            Action(name='GetProjectDetails', kwargs={'project_id': 'PROJ010'}),
            Action(name='CreateInvoice',
                   kwargs={
                       'invoice_number': '2025-T011',
                       'publisher_id': 'PUB005',
                       'subtotal': 510.0,
                       'hst_amount': 66.3,
                       'total_due': 576.3,
                       'invoice_date': '2025-08-26'
                   }),
            Action(name='CreateInvoiceLine',
                   kwargs={
                       'invoice_id': 'INV2025-T011',
                       'project_id': 'PROJ010',
                       'hours': 6.0,
                       'rate': 85.0,
                       'hst_rate': 0.13
                   }),
            Action(name='RecordInvoiceAudit',
                   kwargs={
                       'invoice_number': '2025-T011',
                       'event_type': 'created'
                   }),
            Action(name='ListInvoiceAudit',
                   kwargs={'invoice_id': 'INV2025-T011'})
        ],
        outputs=['AUD_INV2025-T011_45', 'INV2025-T011', 'LINE-0030']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_043',
        instruction=
        "Your task is to update the payment behavior profile for 'Horizon Academic Press' and document the change for the August 2025 period. Based on a recent analysis, their new average days to pay is 75.2 and their late payment frequency is now 0.90 and verify it. After updating their profile, send an internal notification email to the consultant 'Sarah Thompson' with the subject 'Client KPI Update: Horizon Academic Press'. Finally, create a new financial snapshot for August 2025 ('SNAP_BEHAV_0825_PUB003') for 2025-08-26, to archive the new status and A/R aging report is also exported for this period ('2025-08').",
        actions=[
            Action(name='GetPublisherByName',
                   kwargs={'publisher_name': 'Horizon Academic Press'}),
            Action(name='GetConsultantProfile',
                   kwargs={'name': 'Sarah Thompson'}),
            Action(name='UpdatePaymentBehavior',
                   kwargs={
                       'publisher_id': 'PUB003',
                       'avg_days_to_pay': 75.2,
                       'late_payment_frequency': 0.9
                   }),
            Action(name='GetPaymentBehavior',
                   kwargs={'publisher_id': 'PUB003'}),
            Action(name='SendNotificationEmail',
                   kwargs={
                       'publisher_id': 'PUB003',
                       'consultant_id': 'CONS001',
                       'subject': 'Client KPI Update: Horizon Academic Press'
                   }),
            Action(name='CreateDashboardSnapshot',
                   kwargs={
                       'snapshot_id': 'SNAP_BEHAV_0825_PUB003',
                       'snapshot_date': '2025-08-26',
                       'year': 2025
                   }),
            Action(name='ExportARAgingReport',
                   kwargs={'period_label': '2025-08'})
        ],
        outputs=[
            'PUB003', 'CONS001', 'BEH003',
            '/reports/ar_aging/AR_Aging_Report_2025-08.pdf',
            'Notification email sent.', 'SNAP_BEHAV_0825_PUB003'
        ]),
    Task(
        annotator='gokulsaireddy',
        user_id='task_044',
        instruction=
        "Your task is to produce a 30-day cash flow forecast for the period August 26, 2025 (2025-08-26), to September 25, 2025 (2025-09-25). The final analysis, which must be logged in the scheduler for 2025-08-26T12:00:00Z with a note '30-day cash flow forecast', should find the net cash flow posed by 'Coastal Educational Resources' by comparing their total unpaid expected inflows against the company's total recurring outflows for the period. This assessment should be supported by the publisher's historical payment profile.",
        actions=[
            Action(name='GetPublisherByName',
                   kwargs={'publisher_name': 'Coastal Educational Resources'}),
            Action(name='FilterInvoices',
                   kwargs={
                       'publisher_id': 'PUB004',
                       'unpaid_only': True
                   }),
            Action(name='CalculateTotalInflows',
                   kwargs={
                       'start_date': '2025-08-26',
                       'end_date': '2025-09-25',
                       'invoices_to_consider': ['INV010', 'INV024']
                   }),
            Action(name='CalculateTotalOutflows',
                   kwargs={
                       'start_date': '2025-08-26',
                       'end_date': '2025-09-25'
                   }),
            Action(name='ComputeNetCashFlow',
                   kwargs={
                       'inflows': 3627.3,
                       'outflows': 4638.93
                   }),
            Action(name='GetPaymentBehavior',
                   kwargs={'publisher_id': 'PUB004'}),
            Action(name='AddSchedulerRun',
                   kwargs={
                       'run_date': '2025-08-26T12:00:00Z',
                       'note': '30-day cash flow forecast'
                   })
        ],
        outputs=['PUB004', '3627.3', '4638.93', 'BEH004', -1011.63]),
    Task(
        annotator='gokulsaireddy',
        user_id='task_045',
        instruction=
        "Your task is to create a dedicated micro-invoice for the work completed under time entry 'TIME007'. The system must be updated to include a new, single-line invoice that has the 6.5 billable hours and 90.0 project rate. ('2025-T007' for $585.00 subtotal, $76.05 HST, $661.05 total_due) dated on 2025-08-26. Ensure the new invoice and its corresponding line item are created and that the action is recorded in the audit trail.",
        actions=[
            Action(name='GetTimeEntryDetails',
                   kwargs={'time_entry_id': 'TIME007'}),
            Action(name='GetProjectDetails', kwargs={'project_id': 'PROJ005'}),
            Action(name='CreateInvoice',
                   kwargs={
                       'invoice_number': '2025-T007',
                       'publisher_id': 'PUB003',
                       'subtotal': 585.0,
                       'hst_amount': 76.05,
                       'total_due': 661.05,
                       'invoice_date': '2025-08-26'
                   }),
            Action(name='CreateInvoiceLine',
                   kwargs={
                       'invoice_id': 'INV2025-T007',
                       'project_id': 'PROJ005',
                       'hours': 6.5,
                       'rate': 90.0,
                       'hst_rate': 0.13
                   }),
            Action(name='RecordInvoiceAudit',
                   kwargs={
                       'invoice_number': '2025-T007',
                       'event_type': 'created'
                   }),
            Action(name='ListInvoiceAudit',
                   kwargs={'invoice_id': 'INV2025-T007'})
        ],
        outputs=['AUD_INV2025-T007_45', 'INV2025-T007', 'LINE-0030']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_046',
        instruction=
        "Your task is to create an invoice for project 'Advanced Chemistry Textbook - University Level' as of November 25, 2025 (2025-11-25). The system should include an auditable invoice ('2025-K004') for the initial setup fee, which has a subtotal of 1200.00 CAD, HST of 156.00 CAD, and a total of 1356.00 CAD. Also, audit this invoice with a 'generated' event and verify it. Furthermore, a financial dashboard for the date must be created for this new income, showing a new year-to-date revenue of 13763.78 CAD. Finally, include a monthly audit with the same subtotal and verify it.",
        actions=[
            Action(name='GetProjectPublisher',
                   kwargs={
                       'name': 'Advanced Chemistry Textbook - University Level'
                   }),
            Action(name='CreateInvoice',
                   kwargs={
                       'invoice_number': '2025-K004',
                       'publisher_id': 'PUB001',
                       'invoice_date': '2025-11-25',
                       'subtotal': 1200.0,
                       'hst_amount': 156.0,
                       'total_due': 1356.0
                   }),
            Action(name='LogInvoiceAuditEvent',
                   kwargs={
                       'invoice_id': 'INV2025-K004',
                       'event_type': 'generated'
                   }),
            Action(name='CreateDashboardSnapshotWithInvoiceId',
                   kwargs={
                       'invoice_id': 'INV2025-K004',
                       'snapshot_date': '2025-11-25',
                       'year': 2025,
                       'ytd_revenue': 13763.78
                   }),
            Action(name='AddMonthlyAudit',
                   kwargs={
                       'snapshot_id': 'SNAP_INV2025-K004',
                       'month': '2025-11',
                       'amount': 1200.0
                   }),
            Action(name='GetMonthlyAuditBySnapshot',
                   kwargs={'snapshot_id': 'SNAP_INV2025-K004'}),
            Action(name='ListInvoiceAudit',
                   kwargs={'audit_id': 'AUD_INV2025-K004'})
        ],
        outputs=[
            'PUB001', 'INV2025-K004', 'AUD_INV2025-K004', 'SNAP_INV2025-K004',
            'SNAP_INV2025-K004_2025-11'
        ]),
    Task(
        annotator='gokulsaireddy',
        user_id='task_047',
        instruction=
        "Your task is to produce a 30-day cash flow forecast for the period August 26, 2025 (2025-08-26), to September 25, 2025 (2025-09-25). The final analysis, which must be logged in the scheduler for 2025-08-26T12:00:00Z with a note '30-day cash flow forecast', should find the net cash flow posed by 'Maple Leaf Publishing House' by comparing their total unpaid expected inflows against the company's total recurring outflows for the period. This assessment should be supported by the publisher's historical payment profile.",
        actions=[
            Action(name='GetPublisherByName',
                   kwargs={'publisher_name': 'Maple Leaf Publishing House'}),
            Action(name='FilterInvoices',
                   kwargs={
                       'publisher_id': 'PUB001',
                       'unpaid_only': True
                   }),
            Action(name='CalculateTotalInflows',
                   kwargs={
                       'start_date': '2025-08-26',
                       'end_date': '2025-09-25',
                       'invoices_to_consider': ['INV009', 'INV021', 'INV026']
                   }),
            Action(name='CalculateTotalOutflows',
                   kwargs={
                       'start_date': '2025-08-26',
                       'end_date': '2025-09-25'
                   }),
            Action(name='ComputeNetCashFlow',
                   kwargs={
                       'inflows': 4477.06,
                       'outflows': 4638.93
                   }),
            Action(name='GetPaymentBehavior',
                   kwargs={'publisher_id': 'PUB001'}),
            Action(name='AddSchedulerRun',
                   kwargs={
                       'run_date': '2025-08-26T12:00:00Z',
                       'note': '30-day cash flow forecast'
                   })
        ],
        outputs=['PUB001', '4477.06', '4638.93', 'BEH001', -161.87]),
    Task(
        annotator='gokulsaireddy',
        user_id='task_048',
        instruction=
        "You log a June 2024 software subscription expense of 359.88 CAD for 'Adobe Systems', paid by Business Credit Card on 2024-06-15 under category SOFTWARE_SUBSCR. This expense is captured with id 'EXP_0090' and dated 2024-06-15. It must also appear in the June 2024 dashboard snapshot with SNAP006, dated 2024-06-30, where the monthly totals include this expense with amount 359.88 CAD.",
        actions=[
            Action(name='GetExpensesByCategory',
                   kwargs={'category_code': 'SOFTWARE_SUBSCR'}),
            Action(name='AddExpenseRecord',
                   kwargs={
                       'expense_id': 'EXP_0090',
                       'vendor': 'Adobe Systems',
                       'expense_date': '2024-06-15',
                       'amount': 359.88,
                       'payment_method': 'Business Credit Card',
                       'category_code': 'SOFTWARE_SUBSCR'
                   }),
            Action(name='GetExpensesByCategory',
                   kwargs={'category_code': 'SOFTWARE_SUBSCR'}),
            Action(name='CreateDashboardSnapshot',
                   kwargs={
                       'snapshot_id': 'SNAP006',
                       'snapshot_date': '2024-06-30',
                       'year': 2024
                   }),
            Action(name='AddMonthlyExpense',
                   kwargs={
                       'snapshot_id': 'SNAP006',
                       'month': '2024-06',
                       'amount': 359.88
                   }),
            Action(name='GetMonthlyExpenseBySnapshot',
                   kwargs={'snapshot_id': 'SNAP006'}),
            Action(name='GetDashboardSnapshot',
                   kwargs={'snapshot_id': 'SNAP006'})
        ],
        outputs=['SNAP006_2024-06', 'SNAP006']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_049',
        instruction=
        "You log a July 2024 bank fees expense of 24.95 CAD for 'RBC Royal Bank', paid by Direct Debit on 2024-07-31 under category BANK_FEES. This expense is captured with id 'EXP_0100' and dated 2024-07-31. It must also appear in the July 2024 dashboard snapshot with SNAP007, dated 2024-07-31, where the monthly totals include this expense with amount 24.95 CAD.",
        actions=[
            Action(name='GetExpensesByCategory',
                   kwargs={'category_code': 'BANK_FEES'}),
            Action(name='AddExpenseRecord',
                   kwargs={
                       'expense_id': 'EXP_0100',
                       'vendor': 'RBC Royal Bank',
                       'expense_date': '2024-07-31',
                       'amount': 24.95,
                       'payment_method': 'Direct Debit',
                       'category_code': 'BANK_FEES'
                   }),
            Action(name='GetExpensesByCategory',
                   kwargs={'category_code': 'BANK_FEES'}),
            Action(name='CreateDashboardSnapshot',
                   kwargs={
                       'snapshot_id': 'SNAP007',
                       'snapshot_date': '2024-07-31',
                       'year': 2024
                   }),
            Action(name='AddMonthlyExpense',
                   kwargs={
                       'snapshot_id': 'SNAP007',
                       'month': '2024-07',
                       'amount': 24.95
                   }),
            Action(name='GetMonthlyExpenseBySnapshot',
                   kwargs={'snapshot_id': 'SNAP007'}),
            Action(name='GetDashboardSnapshot',
                   kwargs={'snapshot_id': 'SNAP007'})
        ],
        outputs=['SNAP007_2024-07', 'SNAP007']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_050',
        instruction=
        "Your task is to properly document a significant lab supply expense of $975.50 from 'Bio-Rad Laboratories' dated 2025-08-28, which is associated with project 'Biology Lab Manual - University Level'. Also, create a financial snapshot for August 2025 with ID 'SNAP_EXP_0825_B' dated 2025-08-31 and log the month's existing total expenses of $831.65. Create a new Bio-Rad Laboratories expense record with ID 'EXP_BIORAD_001' under the 'OFFICE_SUPPLIES' category. Ensure the main 'checking' account balance is updated to reflect this new expenditure, resulting in a final balance of $14445.25.",
        actions=[
            Action(name='GetProjectByName',
                   kwargs={
                       'project_name': 'Biology Lab Manual - University Level'
                   }),
            Action(name='CreateDashboardSnapshot',
                   kwargs={
                       'snapshot_id': 'SNAP_EXP_0825_B',
                       'snapshot_date': '2025-08-31',
                       'year': 2025
                   }),
            Action(name='AddMonthlyExpense',
                   kwargs={
                       'snapshot_id': 'SNAP_EXP_0825_B',
                       'month': '2025-08',
                       'amount': 831.65
                   }),
            Action(name='AddExpenseRecord',
                   kwargs={
                       'expense_id': 'EXP_BIORAD_001',
                       'project_id': 'PROJ002',
                       'vendor': 'Bio-Rad Laboratories',
                       'expense_date': '2025-08-28',
                       'amount': 975.5,
                       'category_code': 'OFFICE_SUPPLIES'
                   }),
            Action(name='GetBankAccountDetails',
                   kwargs={'account_type': 'checking'}),
            Action(name='UpdateBankAccountBalance',
                   kwargs={
                       'account_id': 'CHK001',
                       'balance': 14445.25
                   })
        ],
        outputs=['CHK001', 'SNAP_EXP_0825_B_2025-08']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_051',
        instruction=
        "You need to set up the new client, 'Cosmic Press' ('PUB056'), with contact email 'editor@cosmicpress.com', effective September 2025. The final state requires that the publisher and their new project, 'Astronomy for Beginners' ('PROJ4007'), with ISBN '978-7-1700-4007-7' and a rate of 95.0, are created. Additionally, their initial setup invoice '2025-B001' (subtotal $1200.00, HST $156.00, total $1356.00) for 2025-09-01 must be generated and emailed with the subject '2025-B001'.",
        actions=[
            Action(name='CreatePublisher',
                   kwargs={
                       'publisher_id': 'PUB056',
                       'name': 'Cosmic Press',
                       'contact_email': 'editor@cosmicpress.com'
                   }),
            Action(name='GetPublisherInfo', kwargs={'publisher_id': 'PUB056'}),
            Action(name='CreateProject',
                   kwargs={
                       'project_id': 'PROJ4007',
                       'publisher_id': 'PUB056',
                       'isbn': '978-7-1700-4007-7',
                       'project_title': 'Astronomy for Beginners',
                       'default_hourly_rate': 95.0
                   }),
            Action(name='GetProjectDetails', kwargs={'project_id':
                                                     'PROJ4007'}),
            Action(name='CreateInvoice',
                   kwargs={
                       'invoice_number': '2025-B001',
                       'publisher_id': 'PUB056',
                       'subtotal': 1200.0,
                       'hst_amount': 156.0,
                       'total_due': 1356.0,
                       'invoice_date': '2025-09-01'
                   }),
            Action(name='SendInvoiceEmail',
                   kwargs={
                       'publisher_id': 'PUB056',
                       'invoice_number': '2025-B001',
                       'subject': '2025-B001'
                   }),
            Action(name='GetInvoiceDetails',
                   kwargs={'invoice_number': '2025-B001'})
        ],
        outputs=['INV2025-B001']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_052',
        instruction=
        "Your task is to create a dedicated financial snapshot for the 'French Language Learning Series - Volume 1' project. The snapshot, with ID 'SNAP_PROJ004', must be dated for 2025-08-31 for the year 2025. Before creating the report, you must confirm that the project's total lifetime logged hours is 9.25. The final snapshot must be populated with the project's total lifetime revenue of $740.00, using the record ID 'PR_SNAP004_PROJ004'.",
        actions=[
            Action(name='GetProjectByName',
                   kwargs={
                       'project_name':
                       'French Language Learning Series - Volume 1'
                   }),
            Action(name='GetProjectTimeEntries',
                   kwargs={'project_id': 'PROJ004'}),
            Action(name='CreateDashboardSnapshot',
                   kwargs={
                       'snapshot_id': 'SNAP_PROJ004',
                       'snapshot_date': '2025-08-31',
                       'year': 2025
                   }),
            Action(name='AddProjectRevenue',
                   kwargs={
                       'row_id': 'PR_SNAP004_PROJ004',
                       'snapshot_id': 'SNAP_PROJ004',
                       'project_id': 'PROJ004',
                       'revenue': 740.0
                   }),
            Action(name='GetProjectRevenueSummary',
                   kwargs={'snapshot_id': 'SNAP_PROJ004'})
        ],
        outputs=['PROJ004', 'SNAP_PROJ004', 'PR_SNAP004_PROJ004', 9.25]),
    Task(
        annotator='gokulsaireddy',
        user_id='task_053',
        instruction=
        "Your task is to create an invoice for project 'Mathematics Problem Bank - Grades 9-12' as of August 25, 2025 (2025-08-25) The system should include a auditable invoice ('2025-K001') for the initial setup fee, which has a subtotal of 500.00 CAD, HST of 65.00 CAD, and a total of 565.00 CAD.Also, audit this invoice with generated event and verify it. Furthermore, the financial dashboard for the date must be created for this new income, showing a new year-to-date revenue of 10813.78 CADFinally, Include a monthly audit with same subtotal and verify it.",
        actions=[
            Action(name='GetProjectPublisher',
                   kwargs={'name': 'Mathematics Problem Bank - Grades 9-12'}),
            Action(name='CreateInvoice',
                   kwargs={
                       'invoice_number': '2025-K001',
                       'publisher_id': 'PUB001',
                       'invoice_date': '2025-08-25',
                       'subtotal': 500.0,
                       'hst_amount': 65.0,
                       'total_due': 565.0
                   }),
            Action(name='LogInvoiceAuditEvent',
                   kwargs={
                       'invoice_id': 'INV2025-K001',
                       'event_type': 'generated'
                   }),
            Action(name='CreateDashboardSnapshotWithInvoiceId',
                   kwargs={
                       'invoice_id': 'INV2025-K001',
                       'snapshot_date': '2025-08-25',
                       'year': 2025,
                       'ytd_revenue': 10813.78
                   }),
            Action(name='AddMonthlyAudit',
                   kwargs={
                       'snapshot_id': 'SNAP_INV2025-K001',
                       'month': '2025-08',
                       'amount': 500.0
                   }),
            Action(name='GetMonthlyAuditBySnapshot',
                   kwargs={'snapshot_id': 'SNAP_INV2025-K001'}),
            Action(name='ListInvoiceAudit',
                   kwargs={'audit_id': 'AUD_INV2025-K001'})
        ],
        outputs=[
            'PUB001', 'INV2025-K001', 'AUD_INV2025-K001', 'SNAP_INV2025-K001',
            'SNAP_INV2025-K001_2025-08'
        ]),
    Task(
        annotator='gokulsaireddy',
        user_id='task_054',
        instruction=
        "Your task is to properly document a significant travel expense of $450.75 from 'VIA Rail' dated 2025-10-05, which is associated with project 'Canadian History Comprehensive Guide'. Also, create a financial snapshot for October 2025 with ID 'SNAP_EXP_1025', dated 2025-10-31 and log the month's existing total expenses of $46.52. Create a new VIA Rail expense record with ID 'EXP_VIA_001' under the 'TRAVEL_EXPENSE' category. Ensure the main 'checking' account balance is updated to reflect this new expenditure, resulting in a final balance of $14969.00.",
        actions=[
            Action(name='GetProjectByName',
                   kwargs={
                       'project_name': 'Canadian History Comprehensive Guide'
                   }),
            Action(name='CreateDashboardSnapshot',
                   kwargs={
                       'snapshot_id': 'SNAP_EXP_1025',
                       'snapshot_date': '2025-10-31',
                       'year': 2025
                   }),
            Action(name='AddMonthlyExpense',
                   kwargs={
                       'snapshot_id': 'SNAP_EXP_1025',
                       'month': '2025-10',
                       'amount': 46.52
                   }),
            Action(name='AddExpenseRecord',
                   kwargs={
                       'expense_id': 'EXP_VIA_001',
                       'project_id': 'PROJ003',
                       'vendor': 'VIA Rail',
                       'expense_date': '2025-10-05',
                       'amount': 450.75,
                       'category_code': 'TRAVEL_EXPENSE'
                   }),
            Action(name='GetBankAccountDetails',
                   kwargs={'account_type': 'checking'}),
            Action(name='UpdateBankAccountBalance',
                   kwargs={
                       'account_id': 'CHK001',
                       'balance': 14969.0
                   })
        ],
        outputs=['CHK001', 'SNAP_EXP_1025_2025-10', 'CHK001']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_055',
        instruction=
        "You issue a May 2024 invoice for Maple Leaf Publishing House, numbered '2024-005' and dated 2024-05-31, covering the full month of May. The invoice must show a subtotal of 1540.0 CAD, HST of 200.2 CAD, and a total due of 1740.2 CAD. It includes two line items: project PROJ003 with 10.0 hours at 90.0, and project PROJ004 with 8.0 hours at 80.0. Both line details are visible, and the invoice is reflected in the May dashboard snapshot (SNAP005) dated 2024-05-31, with the snapshot.",
        actions=[
            Action(name='GetPublisherByName',
                   kwargs={'publisher_name': 'Maple Leaf Publishing House'}),
            Action(name='CreateInvoice',
                   kwargs={
                       'invoice_number': '2024-005',
                       'publisher_id': 'PUB001',
                       'invoice_date': '2024-05-31',
                       'period_start': '2024-05-01',
                       'period_end': '2024-05-31',
                       'subtotal': 1540.0,
                       'hst_amount': 200.2,
                       'total_due': 1740.2
                   }),
            Action(name='CreateInvoiceLine',
                   kwargs={
                       'invoice_id': 'INV2024-005',
                       'project_id': 'PROJ003',
                       'hours': 10.0,
                       'rate': 90.0,
                       'hst_rate': 0.13
                   }),
            Action(name='CreateInvoiceLine',
                   kwargs={
                       'invoice_id': 'INV2024-005',
                       'project_id': 'PROJ004',
                       'hours': 8.0,
                       'rate': 80.0,
                       'hst_rate': 0.13
                   }),
            Action(name='GetInvoiceLines',
                   kwargs={'invoice_id': 'INV2024-005'}),
            Action(name='CreateDashboardSnapshot',
                   kwargs={
                       'snapshot_id': 'SNAP005',
                       'snapshot_date': '2024-05-31',
                       'year': 2024
                   })
        ],
        outputs=['INV2024-005', 'SNAP005']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_056',
        instruction=
        "Your task is to process a payment for invoice '2024-026'. The system must be updated to show the invoice was paid on '2025-08-27T10:00:00Z'. A 'payment_received' event must be logged in the audit trail. Finally, the balance of the primary 'checking' account must be updated to reflect the deposit, resulting in a new balance of $17793.75.",
        actions=[
            Action(name='FilterInvoices',
                   kwargs={'invoice_number': '2024-026'}),
            Action(name='UpdateInvoicePayment',
                   kwargs={
                       'invoice_id': 'INV026',
                       'paid_at': '2025-08-27T10:00:00Z'
                   }),
            Action(name='LogInvoiceAuditEvent',
                   kwargs={
                       'invoice_id': 'INV026',
                       'event_type': 'payment_received'
                   }),
            Action(name='GetBankAccountDetails',
                   kwargs={'account_type': 'checking'}),
            Action(name='UpdateBankAccountBalance',
                   kwargs={
                       'account_id': 'CHK001',
                       'balance': 17793.75
                   })
        ],
        outputs=['INV026', 'CHK001', 'AUD_INV026']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_057',
        instruction=
        "You issue a February 2024 invoice for Maple Leaf Publishing House, numbered '2024-002' and dated 2024-02-29, covering the full month of February. The invoice must show a subtotal of 975.0 CAD, HST of 126.75 CAD, and a total due of 1101.75 CAD. It includes a line item for project PROJ004 with 13.0 hours at a rate of 75.0. The line details are visible, and the invoice is reflected in the February dashboard snapshot (SNAP002) dated 2024-02-29, with the snapshot confirming the updated record.",
        actions=[
            Action(name='GetPublisherByName',
                   kwargs={'publisher_name': 'Maple Leaf Publishing House'}),
            Action(name='CreateInvoice',
                   kwargs={
                       'invoice_number': '2024-002',
                       'publisher_id': 'PUB001',
                       'invoice_date': '2024-02-29',
                       'period_start': '2024-02-01',
                       'period_end': '2024-02-29',
                       'subtotal': 975.0,
                       'hst_amount': 126.75,
                       'total_due': 1101.75
                   }),
            Action(name='CreateInvoiceLine',
                   kwargs={
                       'invoice_id': 'INV2024-002',
                       'project_id': 'PROJ004',
                       'hours': 13.0,
                       'rate': 75.0,
                       'hst_rate': 0.13
                   }),
            Action(name='GetInvoiceLines',
                   kwargs={'invoice_id': 'INV2024-002'}),
            Action(name='CreateDashboardSnapshot',
                   kwargs={
                       'snapshot_id': 'SNAP002',
                       'snapshot_date': '2024-02-29',
                       'year': 2024
                   }),
            Action(name='GetDashboardSnapshot',
                   kwargs={'snapshot_id': 'SNAP002'})
        ],
        outputs=['INV2024-002', 'SNAP002']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_058',
        instruction=
        "You log a November 2024 insurance expense of 875.00 CAD for 'Professional Liability Insurance Co.', paid by Business Bank Transfer on 2024-11-01 under category INSURANCE. This expense is captured with id 'EXP_0140' and dated on 2024-11-01. It must also appear in the November 2024 dashboard snapshot with SNAP011, dated 2024-11-30, where the monthly totals include this expense with amount 875.00 CAD.",
        actions=[
            Action(name='GetExpensesByCategory',
                   kwargs={'category_code': 'INSURANCE'}),
            Action(name='AddExpenseRecord',
                   kwargs={
                       'expense_id': 'EXP_0140',
                       'vendor': 'Professional Liability Insurance Co.',
                       'expense_date': '2024-11-01',
                       'amount': 875.0,
                       'payment_method': 'Business Bank Transfer',
                       'category_code': 'INSURANCE'
                   }),
            Action(name='GetExpensesByCategory',
                   kwargs={'category_code': 'INSURANCE'}),
            Action(name='CreateDashboardSnapshot',
                   kwargs={
                       'snapshot_id': 'SNAP011',
                       'snapshot_date': '2024-11-30',
                       'year': 2024
                   }),
            Action(name='AddMonthlyExpense',
                   kwargs={
                       'snapshot_id': 'SNAP011',
                       'month': '2024-11',
                       'amount': 875.0
                   }),
            Action(name='GetMonthlyExpenseBySnapshot',
                   kwargs={'snapshot_id': 'SNAP011'}),
            Action(name='GetDashboardSnapshot',
                   kwargs={'snapshot_id': 'SNAP011'})
        ],
        outputs=['SNAP011_2024-11', 'SNAP011']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_059',
        instruction=
        "Your task is to create a dedicated micro-invoice for the work completed under time entry 'TIME003'. The system must be updated to include a new, single-line invoice that has the 8.0 billable hours and 95.0 project rate. ('2025-T003' for $760.00 subtotal, $98.80 HST, $858.80 total_due) dated on 2025-08-26. Ensure the new invoice and its corresponding line item are created and that the action is recorded in the audit trail.",
        actions=[
            Action(name='GetTimeEntryDetails',
                   kwargs={'time_entry_id': 'TIME003'}),
            Action(name='GetProjectDetails', kwargs={'project_id': 'PROJ002'}),
            Action(name='CreateInvoice',
                   kwargs={
                       'invoice_number': '2025-T003',
                       'publisher_id': 'PUB001',
                       'subtotal': 760.0,
                       'hst_amount': 98.8,
                       'total_due': 858.8,
                       'invoice_date': '2025-08-26'
                   }),
            Action(name='CreateInvoiceLine',
                   kwargs={
                       'invoice_id': 'INV2025-T003',
                       'project_id': 'PROJ002',
                       'hours': 8.0,
                       'rate': 95.0,
                       'hst_rate': 0.13
                   }),
            Action(name='RecordInvoiceAudit',
                   kwargs={
                       'invoice_number': '2025-T003',
                       'event_type': 'created'
                   }),
            Action(name='ListInvoiceAudit',
                   kwargs={'invoice_id': 'INV2025-T003'})
        ],
        outputs=['AUD_INV2025-T003_45', 'INV2025-T003', 'LINE-0030']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_060',
        instruction=
        "You log a January 2024 communications expense of 85.99 CAD for 'Bell Canada', paid by `Business Credit Card` on 2024-01-15 under category COMMUNICATIONS. This expense is captured with id 'EXP_002' and dated on 2024-01-15'. It must also appear in the January 2024 dashboard snapshot with SNAP001, dated 2024-01-31, where the monthly totals include this expense with amount 85.99 CAD.",
        actions=[
            Action(name='GetExpensesByCategory',
                   kwargs={'category_code': 'COMMUNICATIONS'}),
            Action(name='AddExpenseRecord',
                   kwargs={
                       'expense_id': 'EXP_002',
                       'vendor': 'Bell Canada',
                       'expense_date': '2024-01-15',
                       'amount': 85.99,
                       'payment_method': 'Business Credit Card',
                       'category_code': 'COMMUNICATIONS'
                   }),
            Action(name='GetExpensesByCategory',
                   kwargs={'category_code': 'COMMUNICATIONS'}),
            Action(name='CreateDashboardSnapshot',
                   kwargs={
                       'snapshot_id': 'SNAP001',
                       'snapshot_date': '2024-01-31',
                       'year': 2024
                   }),
            Action(name='AddMonthlyExpense',
                   kwargs={
                       'snapshot_id': 'SNAP001',
                       'month': '2024-01',
                       'amount': 85.99
                   }),
            Action(name='GetMonthlyExpenseBySnapshot',
                   kwargs={'snapshot_id': 'SNAP001'}),
            Action(name='GetDashboardSnapshot',
                   kwargs={'snapshot_id': 'SNAP001'})
        ],
        outputs=['SNAP001_2024-01', 'SNAP001']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_061',
        instruction=
        "Your task is to properly document a significant professional fee of $650.00 from 'Translate Canada' dated 2025-08-28, which is associated with project 'French Language Learning Series - Volume 1'. Also, create a financial snapshot for August 2025 with ID 'SNAP_EXP_0825_C' dated 2025-08-31 and log the month's existing total expenses of $831.65. Create a new Translate Canada expense record with ID 'EXP_TRANS_001' under the 'PROF_FEES' category. Ensure the main 'checking' account balance is updated to reflect this new expenditure, resulting in a final balance of $14770.75.",
        actions=[
            Action(name='GetProjectByName',
                   kwargs={
                       'project_name':
                       'French Language Learning Series - Volume 1'
                   }),
            Action(name='CreateDashboardSnapshot',
                   kwargs={
                       'snapshot_id': 'SNAP_EXP_0825_C',
                       'snapshot_date': '2025-08-31',
                       'year': 2025
                   }),
            Action(name='AddMonthlyExpense',
                   kwargs={
                       'snapshot_id': 'SNAP_EXP_0825_C',
                       'month': '2025-08',
                       'amount': 831.65
                   }),
            Action(name='AddExpenseRecord',
                   kwargs={
                       'expense_id': 'EXP_TRANS_001',
                       'project_id': 'PROJ004',
                       'vendor': 'Translate Canada',
                       'expense_date': '2025-08-28',
                       'amount': 650.0,
                       'category_code': 'PROF_FEES'
                   }),
            Action(name='GetBankAccountDetails',
                   kwargs={'account_type': 'checking'}),
            Action(name='UpdateBankAccountBalance',
                   kwargs={
                       'account_id': 'CHK001',
                       'balance': 14770.75
                   })
        ],
        outputs=['CHK001', 'SNAP_EXP_0825_C_2025-08']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_062',
        instruction=
        "Your task is to update the payment behavior profile for 'Maple Leaf Publishing House' and document the change for the August 2025 period. Based on a recent analysis, their new average days to pay is 17.5 and their late payment frequency is now 0.0 and verify it. After updating their profile, send an internal notification email to the consultant 'Sarah Thompson' with the subject 'Client KPI Update: Maple Leaf Publishing House'. Finally, create a new financial snapshot for August 2025 ('SNAP_BEHAV_0825') for 2025-08-26, to archive the new status and  A/R aging report is also exported for this period ('2025-08').",
        actions=[
            Action(name='GetPublisherByName',
                   kwargs={'publisher_name': 'Maple Leaf Publishing House'}),
            Action(name='GetConsultantProfile',
                   kwargs={'name': 'Sarah Thompson'}),
            Action(name='UpdatePaymentBehavior',
                   kwargs={
                       'publisher_id': 'PUB001',
                       'avg_days_to_pay': 17.5,
                       'late_payment_frequency': 0.0
                   }),
            Action(name='GetPaymentBehavior',
                   kwargs={'publisher_id': 'PUB001'}),
            Action(name='SendNotificationEmail',
                   kwargs={
                       'publisher_id': 'PUB001',
                       'consultant_id': 'CONS001',
                       'subject':
                       'Client KPI Update: Maple Leaf Publishing House'
                   }),
            Action(name='CreateDashboardSnapshot',
                   kwargs={
                       'snapshot_id': 'SNAP_BEHAV_0825',
                       'snapshot_date': '2025-08-26',
                       'year': 2025
                   }),
            Action(name='ExportARAgingReport',
                   kwargs={'period_label': '2025-08'})
        ],
        outputs=[
            'PUB001', 'CONS001', 'BEH001',
            '/reports/ar_aging/AR_Aging_Report_2025-08.pdf',
            'Notification email sent.'
        ]),
    Task(
        annotator='gokulsaireddy',
        user_id='task_063',
        instruction=
        "You complete the onboarding of EcoSphere Publishing ('PUB062') in September 2025, establishing it as a new client with contact mail 'green@ecosphere.pub' its project 'Renewable Energy Systems' ('PROJ4013') set up at a rate of 110.0 and ISBN '978-4-2300-4013-4'. The process results in a first invoice, numbered '2026-B007' and dated 2025-09-05, which reflects a subtotal of 1750.00 CAD, HST of 227.50 CAD, and a total of 1977.50 CAD. The invoice is formally issued and confirms the start of the publisher’s active relationship.",
        actions=[
            Action(name='CreatePublisher',
                   kwargs={
                       'publisher_id': 'PUB062',
                       'name': 'EcoSphere Publishing',
                       'contact_email': 'green@ecosphere.pub'
                   }),
            Action(name='GetPublisherInfo', kwargs={'publisher_id': 'PUB062'}),
            Action(name='CreateProject',
                   kwargs={
                       'project_id': 'PROJ4013',
                       'publisher_id': 'PUB062',
                       'isbn': '978-4-2300-4013-4',
                       'project_title': 'Renewable Energy Systems',
                       'default_hourly_rate': 110.0
                   }),
            Action(name='GetProjectDetails', kwargs={'project_id':
                                                     'PROJ4013'}),
            Action(name='CreateInvoice',
                   kwargs={
                       'invoice_number': '2026-B007',
                       'publisher_id': 'PUB062',
                       'subtotal': 1750.0,
                       'hst_amount': 227.5,
                       'total_due': 1977.5,
                       'invoice_date': '2025-09-05'
                   }),
            Action(name='SendInvoiceEmail',
                   kwargs={
                       'publisher_id': 'PUB062',
                       'invoice_number': '2026-B007',
                       'subject': '2026-B007'
                   }),
            Action(name='GetInvoiceDetails',
                   kwargs={'invoice_number': '2026-B007'})
        ],
        outputs=['INV2026-B007']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_064',
        instruction=
        "You follow up on an overdue invoice for Prairie Knowledge Publishers and their invoices. The invoice dated 2024-11-15, is still unpaid as of 2025-02-28, with having total due of maximum 900.0, making it more than 80 days overdue. By collections policy, this overdue balance is treated as high-risk and requires a escalation. The action is recorded in the audit trail, confirming the escalation. The February dashboard must accurately reflect the invoice's overdue status and financial audit, dated 2025-02-28.with the snapshot confirming the updated record. Include this as monthly audit with amount 500.00 CAD",
        actions=[
            Action(name='GetPublisherByName',
                   kwargs={'publisher_name': 'Prairie Knowledge Publishers'}),
            Action(name='GetPublisherInvoices',
                   kwargs={'publisher_id': 'PUB005'}),
            Action(name='FilterInvoices',
                   kwargs={
                       'publisher_id': 'PUB005',
                       'invoice_date': '2024-11-15',
                       'unpaid_only': True,
                       'max_amount': 900.0
                   }),
            Action(name='ComputeInvoiceAging',
                   kwargs={
                       'invoice_id': 'INV025',
                       'as_of_date': '2025-02-28'
                   }),
            Action(name='LogInvoiceAuditEvent',
                   kwargs={
                       'invoice_id': 'INV025',
                       'event_type': 'collections_hold'
                   }),
            Action(name='ListInvoiceAudit', kwargs={'audit_id': 'AUD_INV025'}),
            Action(name='CreateDashboardSnapshotWithInvoiceId',
                   kwargs={
                       'invoice_id': 'INV025',
                       'snapshot_date': '2025-02-28'
                   }),
            Action(name='GetDashboardSnapshot',
                   kwargs={'snapshot_id': 'SNAP_INV025'}),
            Action(name='AddMonthlyAudit',
                   kwargs={
                       'snapshot_id': 'SNAP_INV025',
                       'month': '2025-02',
                       'amount': 500.0
                   }),
            Action(name='GetMonthlyAuditBySnapshot',
                   kwargs={'snapshot_id': 'SNAP_INV025'})
        ],
        outputs=['AUD_INV025', 'SNAP_INV025', '90+', 'SNAP_INV025_2025-02']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_065',
        instruction=
        "Your task is to properly document a significant travel expense of $892.50 from 'Air Canada' dated 2025-08-27, which is associated with project 'Environmental Science Field Guide'. Also, create a financial snapshot for August 2025 with ID 'SNAP_EXP_0825', dated 2025-08-31 and log the month's existing total expenses of $831.65. Create a new Air Canada expense record with ID 'EXP_AIR_CAN_001' under the 'TRAVEL_EXPENSE' category.Ensure the main 'checking' account balance is updated to reflect this new expenditure, resulting in a final balance of $14528.25.",
        actions=[
            Action(
                name='GetProjectByName',
                kwargs={'project_name': 'Environmental Science Field Guide'}),
            Action(name='CreateDashboardSnapshot',
                   kwargs={
                       'snapshot_id': 'SNAP_EXP_0825',
                       'snapshot_date': '2025-08-31',
                       'year': 2025
                   }),
            Action(name='AddMonthlyExpense',
                   kwargs={
                       'snapshot_id': 'SNAP_EXP_0825',
                       'month': '2025-08',
                       'amount': 831.65
                   }),
            Action(name='AddExpenseRecord',
                   kwargs={
                       'expense_id': 'EXP_AIR_CAN_001',
                       'project_id': 'PROJ007',
                       'vendor': 'Air Canada',
                       'expense_date': '2025-08-27',
                       'amount': 892.5,
                       'category_code': 'TRAVEL_EXPENSE'
                   }),
            Action(name='GetBankAccountDetails',
                   kwargs={'account_type': 'checking'}),
            Action(name='UpdateBankAccountBalance',
                   kwargs={
                       'account_id': 'CHK001',
                       'balance': 14528.25
                   })
        ],
        outputs=['CHK001', 'SNAP_EXP_0825_2025-08']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_066',
        instruction=
        "You follow up on an overdue invoice for Northern Lights Educational Books and their invoices. The invoice dated 2024-07-15, is still unpaid as of 2024-10-15, with having total due of maximum 500.0, making it more than 80 days overdue. By collections policy, this overdue balance is treated as high-risk and requires a escalation. The action is recorded in the audit trail, confirming the escalation. The October dashboard must accurately reflect the invoice's overdue status and financial audit, dated 2024-10-15.with the snapshot confirming the updated record. Include this as monthly audit with amount 216.00 CAD",
        actions=[
            Action(
                name='GetPublisherByName',
                kwargs={'publisher_name':
                        'Northern Lights Educational Books'}),
            Action(name='GetPublisherInvoices',
                   kwargs={'publisher_id': 'PUB002'}),
            Action(name='FilterInvoices',
                   kwargs={
                       'publisher_id': 'PUB002',
                       'invoice_date': '2024-07-15',
                       'unpaid_only': True,
                       'max_amount': 500.0
                   }),
            Action(name='ComputeInvoiceAging',
                   kwargs={
                       'invoice_id': 'INV012',
                       'as_of_date': '2024-10-15'
                   }),
            Action(name='LogInvoiceAuditEvent',
                   kwargs={
                       'invoice_id': 'INV012',
                       'event_type': 'collections_hold'
                   }),
            Action(name='ListInvoiceAudit', kwargs={'audit_id': 'AUD_INV012'}),
            Action(name='CreateDashboardSnapshotWithInvoiceId',
                   kwargs={
                       'invoice_id': 'INV012',
                       'snapshot_date': '2024-10-15'
                   }),
            Action(name='GetDashboardSnapshot',
                   kwargs={'snapshot_id': 'SNAP_INV012'}),
            Action(name='AddMonthlyAudit',
                   kwargs={
                       'snapshot_id': 'SNAP_INV012',
                       'month': '2024-10',
                       'amount': 216.0
                   }),
            Action(name='GetMonthlyAuditBySnapshot',
                   kwargs={'snapshot_id': 'SNAP_INV012'})
        ],
        outputs=['AUD_INV012', 'SNAP_INV012', '90+', 'SNAP_INV012_2024-10']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_067',
        instruction=
        "You log a February 2024 meals and entertainment expense of 156.78 CAD for 'The Keg Restaurant', paid by Business Credit Card on 2024-02-14 under category MEALS_ENTERTAIN. This expense is captured with id 'EXP_004' and dated 2024-02-14. It must also appear in the February 2024 dashboard snapshot with SNAP002, dated 2024-02-29, where the monthly totals include this expense with amount 156.78 CAD.",
        actions=[
            Action(name='GetExpensesByCategory',
                   kwargs={'category_code': 'MEALS_ENTERTAIN'}),
            Action(name='AddExpenseRecord',
                   kwargs={
                       'expense_id': 'EXP_004',
                       'vendor': 'The Keg Restaurant',
                       'expense_date': '2024-02-14',
                       'amount': 156.78,
                       'payment_method': 'Business Credit Card',
                       'category_code': 'MEALS_ENTERTAIN'
                   }),
            Action(name='GetExpensesByCategory',
                   kwargs={'category_code': 'MEALS_ENTERTAIN'}),
            Action(name='CreateDashboardSnapshot',
                   kwargs={
                       'snapshot_id': 'SNAP002',
                       'snapshot_date': '2024-02-29',
                       'year': 2024
                   }),
            Action(name='AddMonthlyExpense',
                   kwargs={
                       'snapshot_id': 'SNAP002',
                       'month': '2024-02',
                       'amount': 156.78
                   }),
            Action(name='GetMonthlyExpenseBySnapshot',
                   kwargs={'snapshot_id': 'SNAP002'}),
            Action(name='GetDashboardSnapshot',
                   kwargs={'snapshot_id': 'SNAP002'})
        ],
        outputs=['SNAP002_2024-02', 'SNAP002']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_068',
        instruction=
        "Your task is to create a dedicated micro-invoice for the work completed under time entry 'TIME009'. The system must be updated to include a new, single-line invoice that has the 5.0 billable hours and 80.0 project rate. ('2025-T009' for $400.00 subtotal, $52.00 HST, $452.00 total_due) dated on 2025-08-26. Ensure the new invoice and its corresponding line item are created and that the action is recorded in the audit trail.",
        actions=[
            Action(name='GetTimeEntryDetails',
                   kwargs={'time_entry_id': 'TIME009'}),
            Action(name='GetProjectDetails', kwargs={'project_id': 'PROJ007'}),
            Action(name='CreateInvoice',
                   kwargs={
                       'invoice_number': '2025-T009',
                       'publisher_id': 'PUB004',
                       'subtotal': 400.0,
                       'hst_amount': 52.0,
                       'total_due': 452.0,
                       'invoice_date': '2025-08-26'
                   }),
            Action(name='CreateInvoiceLine',
                   kwargs={
                       'invoice_id': 'INV2025-T009',
                       'project_id': 'PROJ007',
                       'hours': 5.0,
                       'rate': 80.0,
                       'hst_rate': 0.13
                   }),
            Action(name='RecordInvoiceAudit',
                   kwargs={
                       'invoice_number': '2025-T009',
                       'event_type': 'created'
                   }),
            Action(name='ListInvoiceAudit',
                   kwargs={'invoice_id': 'INV2025-T009'})
        ],
        outputs=['AUD_INV2025-T009_45', 'INV2025-T009', 'LINE-0030']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_069',
        instruction=
        "Your task is to process a payment for invoice '2024-012'. The system must be updated to show the invoice was paid on '2025-09-03T10:00:00Z'. A 'payment_received' event must be logged in the audit trail. Finally, the balance of the primary 'checking' account must be updated to reflect the deposit, resulting in a new balance of $15895.35.",
        actions=[
            Action(name='FilterInvoices',
                   kwargs={'invoice_number': '2024-012'}),
            Action(name='UpdateInvoicePayment',
                   kwargs={
                       'invoice_id': 'INV012',
                       'paid_at': '2025-09-03T10:00:00Z'
                   }),
            Action(name='LogInvoiceAuditEvent',
                   kwargs={
                       'invoice_id': 'INV012',
                       'event_type': 'payment_received'
                   }),
            Action(name='GetBankAccountDetails',
                   kwargs={'account_type': 'checking'}),
            Action(name='UpdateBankAccountBalance',
                   kwargs={
                       'account_id': 'CHK001',
                       'balance': 15895.35
                   })
        ],
        outputs=['INV012', 'CHK001', 'AUD_INV012']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_070',
        instruction=
        "Your task is to create a dedicated financial snapshot for the 'Biology Lab Manual - University Level' project. The snapshot, with ID 'SNAP_PROJ002', must be dated for 2025-08-31 for the year 2025. Before creating the report, you must confirm that the project's total lifetime logged hours is 16.0. The final snapshot must be populated with the project's total lifetime revenue of $1520.00, using the record ID 'PR_SNAP002_PROJ002'.",
        actions=[
            Action(name='GetProjectByName',
                   kwargs={
                       'project_name': 'Biology Lab Manual - University Level'
                   }),
            Action(name='GetProjectTimeEntries',
                   kwargs={'project_id': 'PROJ002'}),
            Action(name='CreateDashboardSnapshot',
                   kwargs={
                       'snapshot_id': 'SNAP_PROJ002',
                       'snapshot_date': '2025-08-31',
                       'year': 2025
                   }),
            Action(name='AddProjectRevenue',
                   kwargs={
                       'row_id': 'PR_SNAP002_PROJ002',
                       'snapshot_id': 'SNAP_PROJ002',
                       'project_id': 'PROJ002',
                       'revenue': 1520.0
                   }),
            Action(name='GetProjectRevenueSummary',
                   kwargs={'snapshot_id': 'SNAP_PROJ002'})
        ],
        outputs=['PROJ002', 'SNAP_PROJ002', 'PR_SNAP002_PROJ002', 16.0]),
    Task(
        annotator='gokulsaireddy',
        user_id='task_071',
        instruction=
        "Your task is to process a payment for invoice '2024-008'. The system must be updated to show the invoice was paid on '2025-08-30T10:00:00Z'. A 'payment_received' event must be logged in the audit trail. Finally, the balance of the primary 'checking' account must be updated to reflect the deposit, resulting in a new balance of $17138.35.",
        actions=[
            Action(name='FilterInvoices',
                   kwargs={'invoice_number': '2024-008'}),
            Action(name='UpdateInvoicePayment',
                   kwargs={
                       'invoice_id': 'INV008',
                       'paid_at': '2025-08-30T10:00:00Z'
                   }),
            Action(name='LogInvoiceAuditEvent',
                   kwargs={
                       'invoice_id': 'INV008',
                       'event_type': 'payment_received'
                   }),
            Action(name='GetBankAccountDetails',
                   kwargs={'account_type': 'checking'}),
            Action(name='UpdateBankAccountBalance',
                   kwargs={
                       'account_id': 'CHK001',
                       'balance': 17138.35
                   })
        ],
        outputs=['INV008', 'CHK001', 'AUD_INV008']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_072',
        instruction=
        "Your task is to create a dedicated micro-invoice for the work completed under time entry 'TIME006'. The system must be updated to include a new, single-line invoice that has the 7.0 billable hours and 80.0 project rate. ('2025-T006' for $560.00 subtotal, $72.80 HST, $632.80 total_due) dated on 2025-08-26. Ensure the new invoice and its corresponding line item are created and that the action is recorded in the audit trail.",
        actions=[
            Action(name='GetTimeEntryDetails',
                   kwargs={'time_entry_id': 'TIME006'}),
            Action(name='GetProjectDetails', kwargs={'project_id': 'PROJ004'}),
            Action(name='CreateInvoice',
                   kwargs={
                       'invoice_number': '2025-T006',
                       'publisher_id': 'PUB002',
                       'subtotal': 560.0,
                       'hst_amount': 72.8,
                       'total_due': 632.8,
                       'invoice_date': '2025-08-26'
                   }),
            Action(name='CreateInvoiceLine',
                   kwargs={
                       'invoice_id': 'INV2025-T006',
                       'project_id': 'PROJ004',
                       'hours': 7.0,
                       'rate': 80.0,
                       'hst_rate': 0.13
                   }),
            Action(name='RecordInvoiceAudit',
                   kwargs={
                       'invoice_number': '2025-T006',
                       'event_type': 'created'
                   }),
            Action(name='ListInvoiceAudit',
                   kwargs={'invoice_id': 'INV2025-T006'})
        ],
        outputs=['AUD_INV2025-T006_45', 'INV2025-T006', 'LINE-0030']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_073',
        instruction=
        "Your task is to produce a 30-day cash flow forecast for the period August 26, 2025 (2025-08-26), to September 25, 2025 (2025-09-25). The final analysis, which must be logged in the scheduler for 2025-08-26T12:00:00Z with a note '30-day cash flow forecast', should find the net cash flow by 'Northern Lights Educational Books' by comparing their total unpaid expected inflows against the company's total recurring outflows for the period. This assessment should be supported by the publisher's historical payment profile.",
        actions=[
            Action(
                name='GetPublisherByName',
                kwargs={'publisher_name':
                        'Northern Lights Educational Books'}),
            Action(name='FilterInvoices',
                   kwargs={
                       'publisher_id': 'PUB002',
                       'unpaid_only': True
                   }),
            Action(name='CalculateTotalInflows',
                   kwargs={
                       'start_date': '2025-08-26',
                       'end_date': '2025-09-25',
                       'invoices_to_consider': ['INV012', 'INV023']
                   }),
            Action(name='CalculateTotalOutflows',
                   kwargs={
                       'start_date': '2025-08-26',
                       'end_date': '2025-09-25'
                   }),
            Action(name='ComputeNetCashFlow',
                   kwargs={
                       'inflows': 1203.45,
                       'outflows': 4638.93
                   }),
            Action(name='GetPaymentBehavior',
                   kwargs={'publisher_id': 'PUB002'}),
            Action(name='AddSchedulerRun',
                   kwargs={
                       'run_date': '2025-08-26T12:00:00Z',
                       'note': '30-day cash flow forecast'
                   })
        ],
        outputs=['PUB002', '1203.45', '4638.93', 'BEH002', -3435.48]),
    Task(
        annotator='gokulsaireddy',
        user_id='task_074',
        instruction=
        "Your task is to onboard the new publisher 'HealthWise Editions' ('PUB059') with email 'payables@healthwise.ed' for September 2025. The system's end state should reflect the creation of the publisher and their first project, 'Modern Nutritional Science' ('PROJ4010'), which has an ISBN of '978-1-2000-4010-1' and a 100.0 hourly rate. Finally, generate and email their setup fee invoice with subject '2025-B004' dated 2025-09-01, for a subtotal of $1600.00, HST of $208.00, and total of $1808.00.",
        actions=[
            Action(name='CreatePublisher',
                   kwargs={
                       'publisher_id': 'PUB059',
                       'name': 'HealthWise Editions',
                       'contact_email': 'payables@healthwise.ed'
                   }),
            Action(name='GetPublisherInfo', kwargs={'publisher_id': 'PUB059'}),
            Action(name='CreateProject',
                   kwargs={
                       'project_id': 'PROJ4010',
                       'publisher_id': 'PUB059',
                       'isbn': '978-1-2000-4010-1',
                       'project_title': 'Modern Nutritional Science',
                       'default_hourly_rate': 100.0
                   }),
            Action(name='GetProjectDetails', kwargs={'project_id':
                                                     'PROJ4010'}),
            Action(name='CreateInvoice',
                   kwargs={
                       'invoice_number': '2025-B004',
                       'publisher_id': 'PUB059',
                       'subtotal': 1600.0,
                       'hst_amount': 208.0,
                       'total_due': 1808.0,
                       'invoice_date': '2025-09-01'
                   }),
            Action(name='SendInvoiceEmail',
                   kwargs={
                       'publisher_id': 'PUB059',
                       'invoice_number': '2025-B004',
                       'subject': '2025-B004'
                   }),
            Action(name='GetInvoiceDetails',
                   kwargs={'invoice_number': '2025-B004'})
        ],
        outputs=['INV2025-B004']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_075',
        instruction=
        "Your task is to properly document a significant software expense of $1500.00 from 'SPSS Inc.' dated 2025-08-28, which is associated with project 'Statistics and Data Analysis Workbook'. Also, create a financial snapshot for August 2025 with ID 'SNAP_EXP_0825_F' dated 2025-08-31 and log the month's existing total expenses of $831.65. Create a new SPSS Inc. expense record with ID 'EXP_SPSS_001' under the 'SOFTWARE_SUBSCR' category. Ensure the main 'checking' account balance is updated to reflect this new expenditure, resulting in a final balance of $13920.75.",
        actions=[
            Action(name='GetProjectByName',
                   kwargs={
                       'project_name': 'Statistics and Data Analysis Workbook'
                   }),
            Action(name='CreateDashboardSnapshot',
                   kwargs={
                       'snapshot_id': 'SNAP_EXP_0825_F',
                       'snapshot_date': '2025-08-31',
                       'year': 2025
                   }),
            Action(name='AddMonthlyExpense',
                   kwargs={
                       'snapshot_id': 'SNAP_EXP_0825_F',
                       'month': '2025-08',
                       'amount': 831.65
                   }),
            Action(name='AddExpenseRecord',
                   kwargs={
                       'expense_id': 'EXP_SPSS_001',
                       'project_id': 'PROJ010',
                       'vendor': 'SPSS Inc.',
                       'expense_date': '2025-08-28',
                       'amount': 1500.0,
                       'category_code': 'SOFTWARE_SUBSCR'
                   }),
            Action(name='GetBankAccountDetails',
                   kwargs={'account_type': 'checking'}),
            Action(name='UpdateBankAccountBalance',
                   kwargs={
                       'account_id': 'CHK001',
                       'balance': 13920.75
                   })
        ],
        outputs=['CHK001', 'SNAP_EXP_0825_F_2025-08']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_076',
        instruction=
        "You log an August 2024 training and development expense of 195.00 CAD for 'Professional Writers Association of Canada', paid by Business Credit Card on 2024-08-12 under category TRAINING_DEV. This expense is captured with id 'EXP_0110' and dated on 2024-08-12. It must also appear in the August 2024 dashboard snapshot with SNAP008, dated 2024-08-31, where the monthly totals include this expense with amount 195.00 CAD.",
        actions=[
            Action(name='GetExpensesByCategory',
                   kwargs={'category_code': 'TRAINING_DEV'}),
            Action(name='AddExpenseRecord',
                   kwargs={
                       'expense_id': 'EXP_0110',
                       'vendor': 'Professional Writers Association of Canada',
                       'expense_date': '2024-08-12',
                       'amount': 195.0,
                       'payment_method': 'Business Credit Card',
                       'category_code': 'TRAINING_DEV'
                   }),
            Action(name='GetExpensesByCategory',
                   kwargs={'category_code': 'TRAINING_DEV'}),
            Action(name='CreateDashboardSnapshot',
                   kwargs={
                       'snapshot_id': 'SNAP008',
                       'snapshot_date': '2024-08-31',
                       'year': 2024
                   }),
            Action(name='AddMonthlyExpense',
                   kwargs={
                       'snapshot_id': 'SNAP008',
                       'month': '2024-08',
                       'amount': 195.0
                   }),
            Action(name='GetMonthlyExpenseBySnapshot',
                   kwargs={'snapshot_id': 'SNAP008'}),
            Action(name='GetDashboardSnapshot',
                   kwargs={'snapshot_id': 'SNAP008'})
        ],
        outputs=['SNAP008_2024-08', 'SNAP008']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_077',
        instruction=
        "Your task is to create an invoice for project 'Environmental Science Lab Guide - High School' as of December 25, 2025 (2025-12-25). The system should include an auditable invoice ('2025-K005') for the initial setup fee, which has a subtotal of 650.00 CAD, HST of 84.50 CAD, and a total of 734.50 CAD. Also, audit this invoice with a 'generated' event and verify it. Furthermore, a financial dashboard for the date must be created for this new income, showing a new year-to-date revenue of 14413.78 CAD. Finally, include a monthly audit with the same subtotal and verify it.",
        actions=[
            Action(name='GetProjectPublisher',
                   kwargs={
                       'name': 'Environmental Science Lab Guide - High School'
                   }),
            Action(name='CreateInvoice',
                   kwargs={
                       'invoice_number': '2025-K005',
                       'publisher_id': 'PUB003',
                       'invoice_date': '2025-12-25',
                       'subtotal': 650.0,
                       'hst_amount': 84.5,
                       'total_due': 734.5
                   }),
            Action(name='LogInvoiceAuditEvent',
                   kwargs={
                       'invoice_id': 'INV2025-K005',
                       'event_type': 'generated'
                   }),
            Action(name='CreateDashboardSnapshotWithInvoiceId',
                   kwargs={
                       'invoice_id': 'INV2025-K005',
                       'snapshot_date': '2025-12-25',
                       'year': 2025,
                       'ytd_revenue': 14413.78
                   }),
            Action(name='AddMonthlyAudit',
                   kwargs={
                       'snapshot_id': 'SNAP_INV2025-K005',
                       'month': '2025-12',
                       'amount': 650.0
                   }),
            Action(name='GetMonthlyAuditBySnapshot',
                   kwargs={'snapshot_id': 'SNAP_INV2025-K005'}),
            Action(name='ListInvoiceAudit',
                   kwargs={'audit_id': 'AUD_INV2025-K005'})
        ],
        outputs=[
            'PUB003', 'INV2025-K005', 'AUD_INV2025-K005', 'SNAP_INV2025-K005',
            'SNAP_INV2025-K005_2025-12'
        ]),
    Task(
        annotator='gokulsaireddy',
        user_id='task_078',
        instruction=
        "You issue a March 2024 invoice for Prairie Knowledge Publishers, numbered '2024-003' and dated 2024-03-31, covering the full month of March. The invoice must show a subtotal of 1120.0 CAD, HST of 145.6 CAD, and a total due of 1265.6 CAD. It includes a line item for project PROJ009 with 14.0 hours at a rate of 80.0. The line details are visible, and the invoice is reflected in the March dashboard snapshot (SNAP003) dated 2024-03-31, with the snapshot confirming the updated record.",
        actions=[
            Action(name='GetPublisherByName',
                   kwargs={'publisher_name': 'Prairie Knowledge Publishers'}),
            Action(name='CreateInvoice',
                   kwargs={
                       'invoice_number': '2024-003',
                       'publisher_id': 'PUB005',
                       'invoice_date': '2024-03-31',
                       'period_start': '2024-03-01',
                       'period_end': '2024-03-31',
                       'subtotal': 1120.0,
                       'hst_amount': 145.6,
                       'total_due': 1265.6
                   }),
            Action(name='CreateInvoiceLine',
                   kwargs={
                       'invoice_id': 'INV2024-003',
                       'project_id': 'PROJ009',
                       'hours': 14.0,
                       'rate': 80.0,
                       'hst_rate': 0.13
                   }),
            Action(name='GetInvoiceLines',
                   kwargs={'invoice_id': 'INV2024-003'}),
            Action(name='CreateDashboardSnapshot',
                   kwargs={
                       'snapshot_id': 'SNAP003',
                       'snapshot_date': '2024-03-31',
                       'year': 2024
                   }),
            Action(name='GetDashboardSnapshot',
                   kwargs={'snapshot_id': 'SNAP003'})
        ],
        outputs=['INV2024-003', 'SNAP003']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_079',
        instruction=
        "Your task is to update the payment behavior profile for 'Coastal Educational Resources' and document the change for the August 2025 period. Based on a recent analysis, their new average days to pay is 27.5 and their late payment frequency is now 0.10 and verify it. After updating their profile, send an internal notification email to the consultant 'Sarah Thompson' with the subject 'Client KPI Update: Coastal Educational Resources'. Finally, create a new financial snapshot for August 2025 ('SNAP_BEHAV_0825_PUB004') for 2025-08-26, to archive the new status and A/R aging report is also exported for this period ('2025-08').",
        actions=[
            Action(name='GetPublisherByName',
                   kwargs={'publisher_name': 'Coastal Educational Resources'}),
            Action(name='GetConsultantProfile',
                   kwargs={'name': 'Sarah Thompson'}),
            Action(name='UpdatePaymentBehavior',
                   kwargs={
                       'publisher_id': 'PUB004',
                       'avg_days_to_pay': 27.5,
                       'late_payment_frequency': 0.1
                   }),
            Action(name='GetPaymentBehavior',
                   kwargs={'publisher_id': 'PUB004'}),
            Action(name='SendNotificationEmail',
                   kwargs={
                       'publisher_id':
                       'PUB004',
                       'consultant_id':
                       'CONS001',
                       'subject':
                       'Client KPI Update: Coastal Educational Resources'
                   }),
            Action(name='CreateDashboardSnapshot',
                   kwargs={
                       'snapshot_id': 'SNAP_BEHAV_0825_PUB004',
                       'snapshot_date': '2025-08-26',
                       'year': 2025
                   }),
            Action(name='ExportARAgingReport',
                   kwargs={'period_label': '2025-08'})
        ],
        outputs=[
            'PUB004', 'CONS001', 'BEH004',
            '/reports/ar_aging/AR_Aging_Report_2025-08.pdf',
            'Notification email sent.'
        ]),
    Task(
        annotator='gokulsaireddy',
        user_id='task_080',
        instruction=
        "Your task is to process a payment for invoice '2024-010'. The system must be updated to show the invoice was paid on '2025-09-01T12:00:00Z'. A 'payment_received' event must be logged in the audit trail. Finally, the balance of the primary 'checking' account must be updated to reflect the deposit, resulting in a new balance of $16957.55.",
        actions=[
            Action(name='FilterInvoices',
                   kwargs={'invoice_number': '2024-010'}),
            Action(name='UpdateInvoicePayment',
                   kwargs={
                       'invoice_id': 'INV010',
                       'paid_at': '2025-09-01T12:00:00Z'
                   }),
            Action(name='LogInvoiceAuditEvent',
                   kwargs={
                       'invoice_id': 'INV010',
                       'event_type': 'payment_received'
                   }),
            Action(name='GetBankAccountDetails',
                   kwargs={'account_type': 'checking'}),
            Action(name='UpdateBankAccountBalance',
                   kwargs={
                       'account_id': 'CHK001',
                       'balance': 16957.55
                   })
        ],
        outputs=['INV010', 'CHK001', 'AUD_INV010']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_081',
        instruction=
        "You prepare a January 2026 invoice for the project 'Advanced Physics Laboratory Manual - University Level'. The invoice, numbered '2026-K001' and dated 2026-01-25, records the initial setup fee with a subtotal of 900.00 CAD, HST of 117.00 CAD, and a total of 1017.00 CAD. This transaction must be fully auditable, with the invoice appearing in the financial records under a generated event. The January 25 dashboard should reflect the new income, bringing year-to-date revenue for 2026 to 900.00 CAD, and the monthly reporting confirms the same subtotal in the audit trail.",
        actions=[
            Action(name='GetProjectPublisher',
                   kwargs={
                       'name':
                       'Advanced Physics Laboratory Manual - University Level'
                   }),
            Action(name='CreateInvoice',
                   kwargs={
                       'invoice_number': '2026-K001',
                       'publisher_id': 'PUB003',
                       'invoice_date': '2026-01-25',
                       'subtotal': 900.0,
                       'hst_amount': 117.0,
                       'total_due': 1017.0
                   }),
            Action(name='LogInvoiceAuditEvent',
                   kwargs={
                       'invoice_id': 'INV2026-K001',
                       'event_type': 'generated'
                   }),
            Action(name='CreateDashboardSnapshotWithInvoiceId',
                   kwargs={
                       'invoice_id': 'INV2026-K001',
                       'snapshot_date': '2026-01-25',
                       'year': 2026,
                       'ytd_revenue': 900.0
                   }),
            Action(name='AddMonthlyAudit',
                   kwargs={
                       'snapshot_id': 'SNAP_INV2026-K001',
                       'month': '2026-01',
                       'amount': 900.0
                   }),
            Action(name='GetMonthlyAuditBySnapshot',
                   kwargs={'snapshot_id': 'SNAP_INV2026-K001'}),
            Action(name='ListInvoiceAudit',
                   kwargs={'audit_id': 'AUD_INV2026-K001'})
        ],
        outputs=[
            'PUB003', 'INV2026-K001', 'AUD_INV2026-K001', 'SNAP_INV2026-K001',
            'SNAP_INV2026-K001_2026-01'
        ]),
    Task(
        annotator='gokulsaireddy',
        user_id='task_082',
        instruction=
        "You follow up on an overdue invoice for Maple Leaf Publishing House and their invoices. The invoice dated 2024-06-30, is still unpaid as of 2024-09-20, making it more than 80 days overdue. By collections policy, this overdue balance is treated as high-risk and requires a escalation. The action is recorded in the audit trail, confirming the escalation. The September dashboard must accurately reflect the invoice's overdue status and financial audit, dated 2024-09-20.with the snapshot confirming the updated record. Include this as monthly audit with amount 216.00 CAD",
        actions=[
            Action(name='GetPublisherByName',
                   kwargs={'publisher_name': 'Maple Leaf Publishing House'}),
            Action(name='GetPublisherInvoices',
                   kwargs={'publisher_id': 'PUB001'}),
            Action(name='FilterInvoices',
                   kwargs={
                       'publisher_id': 'PUB001',
                       'invoice_date': '2024-06-30',
                       'unpaid_only': True
                   }),
            Action(name='ComputeInvoiceAging',
                   kwargs={
                       'invoice_id': 'INV026',
                       'as_of_date': '2024-09-20'
                   }),
            Action(name='LogInvoiceAuditEvent',
                   kwargs={
                       'invoice_id': 'INV026',
                       'event_type': 'phone_call'
                   }),
            Action(name='ListInvoiceAudit', kwargs={'audit_id': 'AUD_INV026'}),
            Action(name='CreateDashboardSnapshotWithInvoiceId',
                   kwargs={
                       'invoice_id': 'INV026',
                       'snapshot_date': '2024-09-20'
                   }),
            Action(name='GetDashboardSnapshot',
                   kwargs={'snapshot_id': 'SNAP_INV026'}),
            Action(name='AddMonthlyAudit',
                   kwargs={
                       'snapshot_id': 'SNAP_INV026',
                       'month': '2024-09',
                       'amount': 216.0
                   }),
            Action(name='GetMonthlyAuditBySnapshot',
                   kwargs={'snapshot_id': 'SNAP_INV026'})
        ],
        outputs=['AUD_INV026', 'SNAP_INV026', '61-90', 'SNAP_INV026_2024-09']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_083',
        instruction=
        "You log a February 2024 software subscription expense of 129.99 CAD for 'Microsoft Canada', paid by Business Credit Card on 2024-02-01 under category SOFTWARE_SUBSCR. This expense is captured with id 'EXP_003' and dated 2024-02-01. It must also appear in the February 2024 dashboard snapshot with SNAP002, dated 2024-02-29, where the monthly totals include this expense with amount 129.99 CAD.",
        actions=[
            Action(name='GetExpensesByCategory',
                   kwargs={'category_code': 'SOFTWARE_SUBSCR'}),
            Action(name='AddExpenseRecord',
                   kwargs={
                       'expense_id': 'EXP_003',
                       'vendor': 'Microsoft Canada',
                       'expense_date': '2024-02-01',
                       'amount': 129.99,
                       'payment_method': 'Business Credit Card',
                       'category_code': 'SOFTWARE_SUBSCR'
                   }),
            Action(name='GetExpensesByCategory',
                   kwargs={'category_code': 'SOFTWARE_SUBSCR'}),
            Action(name='CreateDashboardSnapshot',
                   kwargs={
                       'snapshot_id': 'SNAP002',
                       'snapshot_date': '2024-02-29',
                       'year': 2024
                   }),
            Action(name='AddMonthlyExpense',
                   kwargs={
                       'snapshot_id': 'SNAP002',
                       'month': '2024-02',
                       'amount': 129.99
                   }),
            Action(name='GetMonthlyExpenseBySnapshot',
                   kwargs={'snapshot_id': 'SNAP002'}),
            Action(name='GetDashboardSnapshot',
                   kwargs={'snapshot_id': 'SNAP002'})
        ],
        outputs=['SNAP002_2024-02', 'SNAP002']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_084',
        instruction=
        "Your task is to update the payment behavior profile for 'Northern Lights Educational Books' and document the change for the August 2025 period. Based on a recent analysis, their new average days to pay is 45.0 and their late payment frequency is now 0.65 and verify it. After updating their profile, send an internal notification email to the consultant 'Sarah Thompson' with the subject 'Client KPI Update: Northern Lights Educational Books'. Finally, create a new financial snapshot for August 2025 ('SNAP_BEHAV_0825_PUB002') for 2025-08-26, to archive the new status and A/R aging report is also exported for this period ('2025-08').",
        actions=[
            Action(
                name='GetPublisherByName',
                kwargs={'publisher_name':
                        'Northern Lights Educational Books'}),
            Action(name='GetConsultantProfile',
                   kwargs={'name': 'Sarah Thompson'}),
            Action(name='UpdatePaymentBehavior',
                   kwargs={
                       'publisher_id': 'PUB002',
                       'avg_days_to_pay': 45.0,
                       'late_payment_frequency': 0.65
                   }),
            Action(name='GetPaymentBehavior',
                   kwargs={'publisher_id': 'PUB002'}),
            Action(name='SendNotificationEmail',
                   kwargs={
                       'publisher_id':
                       'PUB002',
                       'consultant_id':
                       'CONS001',
                       'subject':
                       'Client KPI Update: Northern Lights Educational Books'
                   }),
            Action(name='CreateDashboardSnapshot',
                   kwargs={
                       'snapshot_id': 'SNAP_BEHAV_0825_PUB002',
                       'snapshot_date': '2025-08-26',
                       'year': 2025
                   }),
            Action(name='ExportARAgingReport',
                   kwargs={'period_label': '2025-08'})
        ],
        outputs=[
            'PUB002', 'CONS001', 'BEH002',
            '/reports/ar_aging/AR_Aging_Report_2025-08.pdf',
            'Notification email sent.'
        ]),
    Task(
        annotator='gokulsaireddy',
        user_id='task_085',
        instruction=
        "Your task is to update the payment behavior profile for 'Prairie Knowledge Publishers' and document the change for the August 2025 period. Based on a recent analysis, their new average days to pay is 32.0 and their late payment frequency is now 0.35 and verify it. After updating their profile, send an internal notification email to the consultant 'Sarah Thompson' with the subject 'Client KPI Update: Prairie Knowledge Publishers'. Finally, create a new financial snapshot for August 2025 ('SNAP_BEHAV_0825_PUB005') for 2025-08-26, to archive the new status and A/R aging report is also exported for this period ('2025-08').",
        actions=[
            Action(name='GetPublisherByName',
                   kwargs={'publisher_name': 'Prairie Knowledge Publishers'}),
            Action(name='GetConsultantProfile',
                   kwargs={'name': 'Sarah Thompson'}),
            Action(name='UpdatePaymentBehavior',
                   kwargs={
                       'publisher_id': 'PUB005',
                       'avg_days_to_pay': 32.0,
                       'late_payment_frequency': 0.35
                   }),
            Action(name='GetPaymentBehavior',
                   kwargs={'publisher_id': 'PUB005'}),
            Action(name='SendNotificationEmail',
                   kwargs={
                       'publisher_id': 'PUB005',
                       'consultant_id': 'CONS001',
                       'subject':
                       'Client KPI Update: Prairie Knowledge Publishers'
                   }),
            Action(name='CreateDashboardSnapshot',
                   kwargs={
                       'snapshot_id': 'SNAP_BEHAV_0825_PUB005',
                       'snapshot_date': '2025-08-26',
                       'year': 2025
                   }),
            Action(name='ExportARAgingReport',
                   kwargs={'period_label': '2025-08'})
        ],
        outputs=[
            'PUB005', 'CONS001', 'BEH005',
            '/reports/ar_aging/AR_Aging_Report_2025-08.pdf',
            'Notification email sent.'
        ]),
    Task(
        annotator='gokulsaireddy',
        user_id='task_086',
        instruction=
        "Your task is to process a payment for invoice '2024-025'. The system must be updated to show the invoice was paid on '2025-09-02T10:00:00Z'. A 'payment_received' event must be logged in the audit trail. Finally, the balance of the primary 'checking' account must be updated to reflect the deposit, resulting in a new balance of $16234.35.",
        actions=[
            Action(name='FilterInvoices',
                   kwargs={'invoice_number': '2024-025'}),
            Action(name='UpdateInvoicePayment',
                   kwargs={
                       'invoice_id': 'INV025',
                       'paid_at': '2025-09-02T10:00:00Z'
                   }),
            Action(name='LogInvoiceAuditEvent',
                   kwargs={
                       'invoice_id': 'INV025',
                       'event_type': 'payment_received'
                   }),
            Action(name='GetBankAccountDetails',
                   kwargs={'account_type': 'checking'}),
            Action(name='UpdateBankAccountBalance',
                   kwargs={
                       'account_id': 'CHK001',
                       'balance': 16234.35
                   })
        ],
        outputs=['INV025', 'CHK001', 'AUD_INV025']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_087',
        instruction=
        "Your task is to perform a full onboarding for the new publisher 'Innovate Forward Press' ('PUB065') with contact mail 'payments@innovateforward.tech' as of September 2025. The end state must show that the publisher and their new project, 'The Future of AI Ethics' ('PROJ4016'), with isbn '978-7-2600-4016-7' at a 150.0 hourly rate have been created. Furthermore, their first setup fee invoice ('2026-B010' for $3000.00 subtotal, $390.00 HST, $3390.00 total_due) must be created dated 2025-09-01, and immediately emailed to the client with subject: '2026-B010'.",
        actions=[
            Action(name='CreatePublisher',
                   kwargs={
                       'publisher_id': 'PUB065',
                       'name': 'Innovate Forward Press',
                       'contact_email': 'payments@innovateforward.tech'
                   }),
            Action(name='GetPublisherInfo', kwargs={'publisher_id': 'PUB065'}),
            Action(name='CreateProject',
                   kwargs={
                       'project_id': 'PROJ4016',
                       'publisher_id': 'PUB065',
                       'isbn': '978-7-2600-4016-7',
                       'project_title': 'The Future of AI Ethics',
                       'default_hourly_rate': 150.0
                   }),
            Action(name='GetProjectDetails', kwargs={'project_id':
                                                     'PROJ4016'}),
            Action(name='CreateInvoice',
                   kwargs={
                       'invoice_number': '2026-B010',
                       'publisher_id': 'PUB065',
                       'subtotal': 3000.0,
                       'hst_amount': 390.0,
                       'total_due': 3390.0,
                       'invoice_date': '2025-09-01'
                   }),
            Action(name='SendInvoiceEmail',
                   kwargs={
                       'publisher_id': 'PUB065',
                       'invoice_number': '2026-B010',
                       'subject': '2026-B010'
                   }),
            Action(name='GetInvoiceDetails',
                   kwargs={'invoice_number': '2026-B010'})
        ],
        outputs=['INV2026-B010']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_088',
        instruction=
        "You follow up on an overdue invoice for Horizon Academic Press and their invoices. The invoice dated 2024-06-15, is still unpaid as of 2024-09-30, with having total due of maximum 1220.0, making it more than 80 days overdue. By collections policy, this overdue balance is treated as high-risk and requires a escalation. The action is recorded in the audit trail, confirming the escalation. The September dashboard must accurately reflect the invoice's overdue status and financial audit, dated 2024-09-30.with the snapshot confirming the updated record. Include this as monthly audit with amount 250.00 CAD",
        actions=[
            Action(name='GetPublisherByName',
                   kwargs={'publisher_name': 'Horizon Academic Press'}),
            Action(name='GetPublisherInvoices',
                   kwargs={'publisher_id': 'PUB003'}),
            Action(name='FilterInvoices',
                   kwargs={
                       'publisher_id': 'PUB003',
                       'invoice_date': '2024-06-15',
                       'unpaid_only': True,
                       'max_amount': 1220.0
                   }),
            Action(name='ComputeInvoiceAging',
                   kwargs={
                       'invoice_id': 'INV013',
                       'as_of_date': '2024-09-30'
                   }),
            Action(name='LogInvoiceAuditEvent',
                   kwargs={
                       'invoice_id': 'INV013',
                       'event_type': 'collections_hold'
                   }),
            Action(name='ListInvoiceAudit', kwargs={'audit_id': 'AUD_INV013'}),
            Action(name='CreateDashboardSnapshotWithInvoiceId',
                   kwargs={
                       'invoice_id': 'INV013',
                       'snapshot_date': '2024-09-30'
                   }),
            Action(name='GetDashboardSnapshot',
                   kwargs={'snapshot_id': 'SNAP_INV013'}),
            Action(name='AddMonthlyAudit',
                   kwargs={
                       'snapshot_id': 'SNAP_INV013',
                       'month': '2024-09',
                       'amount': 250.0
                   }),
            Action(name='GetMonthlyAuditBySnapshot',
                   kwargs={'snapshot_id': 'SNAP_INV013'})
        ],
        outputs=['AUD_INV013', 'SNAP_INV013', '90+', 'SNAP_INV013_2024-09']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_089',
        instruction=
        "Your task is to create a dedicated micro-invoice for the work completed under time entry 'TIME005'. The system must be updated to include a new, single-line invoice that has the 3.0 billable hours and 85.0 project rate. ('2025-T005' for $255.00 subtotal, $33.15 HST, $288.15 total_due) dated on 2025-08-26. Ensure the new invoice and its corresponding line item are created and that the action is recorded in the audit trail.",
        actions=[
            Action(name='GetTimeEntryDetails',
                   kwargs={'time_entry_id': 'TIME005'}),
            Action(name='GetProjectDetails', kwargs={'project_id': 'PROJ001'}),
            Action(name='CreateInvoice',
                   kwargs={
                       'invoice_number': '2025-T005',
                       'publisher_id': 'PUB001',
                       'subtotal': 255.0,
                       'hst_amount': 33.15,
                       'total_due': 288.15,
                       'invoice_date': '2025-08-26'
                   }),
            Action(name='CreateInvoiceLine',
                   kwargs={
                       'invoice_id': 'INV2025-T005',
                       'project_id': 'PROJ001',
                       'hours': 3.0,
                       'rate': 85.0,
                       'hst_rate': 0.13
                   }),
            Action(name='RecordInvoiceAudit',
                   kwargs={
                       'invoice_number': '2025-T005',
                       'event_type': 'created'
                   }),
            Action(name='ListInvoiceAudit',
                   kwargs={'invoice_id': 'INV2025-T005'})
        ],
        outputs=['AUD_INV2025-T005_45', 'INV2025-T005', 'LINE-0030']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_090',
        instruction=
        "You issue an August 2024 invoice for Prairie Knowledge Publishers, numbered '2024-008' and dated 2024-08-31, covering the full month of August. The invoice must show a subtotal of 2050.00 CAD, HST of 266.5 CAD, and a total due of 2316.5 CAD. It includes two line items: project PROJ007 with 12.0 hours at 100.0, and project PROJ008 with 10.0 hours at 85.0. Both line details are visible, and the invoice is reflected in the August dashboard snapshot (SNAP008) dated 2024-08-31, with the snapshot.",
        actions=[
            Action(name='GetPublisherByName',
                   kwargs={'publisher_name': 'Prairie Knowledge Publishers'}),
            Action(name='CreateInvoice',
                   kwargs={
                       'invoice_number': '2024-008',
                       'publisher_id': 'PUB005',
                       'invoice_date': '2024-08-31',
                       'period_start': '2024-08-01',
                       'period_end': '2024-08-31',
                       'subtotal': 2050.0,
                       'hst_amount': 266.5,
                       'total_due': 2316.5
                   }),
            Action(name='CreateInvoiceLine',
                   kwargs={
                       'invoice_id': 'INV2024-008',
                       'project_id': 'PROJ007',
                       'hours': 12.0,
                       'rate': 100.0,
                       'hst_rate': 0.13
                   }),
            Action(name='CreateInvoiceLine',
                   kwargs={
                       'invoice_id': 'INV2024-008',
                       'project_id': 'PROJ008',
                       'hours': 10.0,
                       'rate': 85.0,
                       'hst_rate': 0.13
                   }),
            Action(name='GetInvoiceLines',
                   kwargs={'invoice_id': 'INV2024-008'}),
            Action(name='CreateDashboardSnapshot',
                   kwargs={
                       'snapshot_id': 'SNAP008',
                       'snapshot_date': '2024-08-31',
                       'year': 2024
                   })
        ],
        outputs=['INV2024-008', 'SNAP008']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_091',
        instruction=
        "Your task is to properly document a significant professional fee of $750.00 from 'Physics Review Inc.' dated 2025-11-20, which is associated with project 'Physics Problem Solving Handbook'. Also, create a financial snapshot for November 2025 with ID 'SNAP_EXP_1125', dated 2025-11-30 and log the month's existing total expenses of $1120.95. Create a new Physics Review Inc. expense record with ID 'EXP_PHYS_001' under the 'PROF_FEES' category. Ensure the main 'checking' account balance is updated to reflect this new expenditure, resulting in a final balance of $14670.75.",
        actions=[
            Action(name='GetProjectByName',
                   kwargs={'project_name':
                           'Physics Problem Solving Handbook'}),
            Action(name='CreateDashboardSnapshot',
                   kwargs={
                       'snapshot_id': 'SNAP_EXP_1125',
                       'snapshot_date': '2025-11-30',
                       'year': 2025
                   }),
            Action(name='AddMonthlyExpense',
                   kwargs={
                       'snapshot_id': 'SNAP_EXP_1125',
                       'month': '2025-11',
                       'amount': 1120.95
                   }),
            Action(name='AddExpenseRecord',
                   kwargs={
                       'expense_id': 'EXP_PHYS_001',
                       'project_id': 'PROJ005',
                       'vendor': 'Physics Review Inc.',
                       'expense_date': '2025-11-20',
                       'amount': 750.0,
                       'category_code': 'PROF_FEES'
                   }),
            Action(name='GetBankAccountDetails',
                   kwargs={'account_type': 'checking'}),
            Action(name='UpdateBankAccountBalance',
                   kwargs={
                       'account_id': 'CHK001',
                       'balance': 14670.75
                   })
        ],
        outputs=['CHK001', 'SNAP_EXP_1125_2025-11', 'CHK001']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_092',
        instruction=
        "Your task is to produce a 30-day cash flow forecast for the period August 26, 2025 (2025-08-26), to September 25, 2025 (2025-09-25). The final analysis, which must be logged in the scheduler for 2025-08-26T12:00:00Z with a note '30-day cash flow forecast', should find the net cash flow posed by 'Prairie Knowledge Publishers' by comparing their total unpaid expected inflows against the company's total recurring outflows for the period. This assessment should be supported by the publisher's historical payment profile.",
        actions=[
            Action(name='GetPublisherByName',
                   kwargs={'publisher_name': 'Prairie Knowledge Publishers'}),
            Action(name='FilterInvoices',
                   kwargs={
                       'publisher_id': 'PUB005',
                       'unpaid_only': True
                   }),
            Action(name='CalculateTotalInflows',
                   kwargs={
                       'start_date': '2025-08-26',
                       'end_date': '2025-09-25',
                       'invoices_to_consider': ['INV011', 'INV025']
                   }),
            Action(name='CalculateTotalOutflows',
                   kwargs={
                       'start_date': '2025-08-26',
                       'end_date': '2025-09-25'
                   }),
            Action(name='ComputeNetCashFlow',
                   kwargs={
                       'inflows': 1678.05,
                       'outflows': 4638.93
                   }),
            Action(name='GetPaymentBehavior',
                   kwargs={'publisher_id': 'PUB005'}),
            Action(name='AddSchedulerRun',
                   kwargs={
                       'run_date': '2025-08-26T12:00:00Z',
                       'note': '30-day cash flow forecast'
                   })
        ],
        outputs=['PUB005', '1678.05', '4638.93', 'BEH005', -2960.88]),
    Task(
        annotator='gokulsaireddy',
        user_id='task_093',
        instruction=
        "Your task is to create a dedicated micro-invoice for the work completed under time entry 'TIME001'. The system must be updated to include a new, single-line invoice that has the 4.5 billable hours and 85.0 project rate. ('2025-T001' for $382.50 subtotal, $49.73 HST, $432.23 total_due) dated on 2025-08-26. Ensure the new invoice and its corresponding line item are created and that the action is recorded in the audit trail.",
        actions=[
            Action(name='GetTimeEntryDetails',
                   kwargs={'time_entry_id': 'TIME001'}),
            Action(name='GetProjectDetails', kwargs={'project_id': 'PROJ001'}),
            Action(name='CreateInvoice',
                   kwargs={
                       'invoice_number': '2025-T001',
                       'publisher_id': 'PUB001',
                       'subtotal': 382.5,
                       'hst_amount': 49.73,
                       'total_due': 432.23,
                       'invoice_date': '2025-08-26'
                   }),
            Action(name='CreateInvoiceLine',
                   kwargs={
                       'invoice_id': 'INV2025-T001',
                       'project_id': 'PROJ001',
                       'hours': 4.5,
                       'rate': 85.0,
                       'hst_rate': 0.13
                   }),
            Action(name='RecordInvoiceAudit',
                   kwargs={
                       'invoice_number': '2025-T001',
                       'event_type': 'created'
                   }),
            Action(name='ListInvoiceAudit',
                   kwargs={'invoice_id': 'INV2025-T001'})
        ],
        outputs=['AUD_INV2025-T001_45', 'INV2025-T001', 'LINE-0030']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_094',
        instruction=
        "You log a January 2024 office supplies expense of 247.83 CAD for 'Staples Business Depot', paid by Business Credit Card on 2024-01-22 under category OFFICE_SUPPLIES. This expense is captured with id 'EXP_0020' and dated 2024-01-22. It must also appear in the January 2024 dashboard snapshot with SNAP001, dated 2024-01-31, where the monthly totals include this expense with amount 247.83 CAD.",
        actions=[
            Action(name='GetExpensesByCategory',
                   kwargs={'category_code': 'OFFICE_SUPPLIES'}),
            Action(name='AddExpenseRecord',
                   kwargs={
                       'expense_id': 'EXP_0020',
                       'vendor': 'Staples Business Depot',
                       'expense_date': '2024-01-22',
                       'amount': 247.83,
                       'payment_method': 'Business Credit Card',
                       'category_code': 'OFFICE_SUPPLIES'
                   }),
            Action(name='GetExpensesByCategory',
                   kwargs={'category_code': 'OFFICE_SUPPLIES'}),
            Action(name='CreateDashboardSnapshot',
                   kwargs={
                       'snapshot_id': 'SNAP001',
                       'snapshot_date': '2024-01-31',
                       'year': 2024
                   }),
            Action(name='AddMonthlyExpense',
                   kwargs={
                       'snapshot_id': 'SNAP001',
                       'month': '2024-01',
                       'amount': 247.83
                   }),
            Action(name='GetMonthlyExpenseBySnapshot',
                   kwargs={'snapshot_id': 'SNAP001'}),
            Action(name='GetDashboardSnapshot',
                   kwargs={'snapshot_id': 'SNAP001'})
        ],
        outputs=['SNAP001_2024-01', 'SNAP001']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_095',
        instruction=
        "You issue a July 2024 invoice for Horizon Academic Press, numbered '2024-007' and dated 2024-07-31, covering the full month of July. The invoice must show a subtotal of 720.0 CAD, HST of 93.6 CAD, and a total due of 813.6 CAD. It includes a line item for project PROJ005 with 8.0 hours at a rate of 90.0. The line details are visible, and the invoice is reflected in the July dashboard snapshot (SNAP007) dated 2024-07-31, with the snapshot confirming the updated record.",
        actions=[
            Action(name='GetPublisherByName',
                   kwargs={'publisher_name': 'Horizon Academic Press'}),
            Action(name='CreateInvoice',
                   kwargs={
                       'invoice_number': '2024-007',
                       'publisher_id': 'PUB003',
                       'invoice_date': '2024-07-31',
                       'period_start': '2024-07-01',
                       'period_end': '2024-07-31',
                       'subtotal': 720.0,
                       'hst_amount': 93.6,
                       'total_due': 813.6
                   }),
            Action(name='CreateInvoiceLine',
                   kwargs={
                       'invoice_id': 'INV2024-007',
                       'project_id': 'PROJ005',
                       'hours': 8.0,
                       'rate': 90.0,
                       'hst_rate': 0.13
                   }),
            Action(name='GetInvoiceLines',
                   kwargs={'invoice_id': 'INV2024-007'}),
            Action(name='CreateDashboardSnapshot',
                   kwargs={
                       'snapshot_id': 'SNAP007',
                       'snapshot_date': '2024-07-31',
                       'year': 2024
                   }),
            Action(name='GetDashboardSnapshot',
                   kwargs={'snapshot_id': 'SNAP007'})
        ],
        outputs=['INV2024-007', 'SNAP007']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_096',
        instruction=
        "Your task is to properly document a significant subscription expense of $2000.00 from 'Bloomberg Terminal' dated 2025-08-28, which is associated with project 'Economics Study Guide - Microeconomics'. Also, create a financial snapshot for August 2025 with ID 'SNAP_EXP_0825_E' dated 2025-08-31 and log the month's existing total expenses of $831.65. Create a new Bloomberg Terminal expense record with ID 'EXP_BLOOM_001' under the 'SOFTWARE_SUBSCR' category. Ensure the main 'checking' account balance is updated to reflect this new expenditure, resulting in a final balance of $13420.75.",
        actions=[
            Action(name='GetProjectByName',
                   kwargs={
                       'project_name': 'Economics Study Guide - Microeconomics'
                   }),
            Action(name='CreateDashboardSnapshot',
                   kwargs={
                       'snapshot_id': 'SNAP_EXP_0825_E',
                       'snapshot_date': '2025-08-31',
                       'year': 2025
                   }),
            Action(name='AddMonthlyExpense',
                   kwargs={
                       'snapshot_id': 'SNAP_EXP_0825_E',
                       'month': '2025-08',
                       'amount': 831.65
                   }),
            Action(name='AddExpenseRecord',
                   kwargs={
                       'expense_id': 'EXP_BLOOM_001',
                       'project_id': 'PROJ009',
                       'vendor': 'Bloomberg Terminal',
                       'expense_date': '2025-08-28',
                       'amount': 2000.0,
                       'category_code': 'SOFTWARE_SUBSCR'
                   }),
            Action(name='GetBankAccountDetails',
                   kwargs={'account_type': 'checking'}),
            Action(name='UpdateBankAccountBalance',
                   kwargs={
                       'account_id': 'CHK001',
                       'balance': 13420.75
                   })
        ],
        outputs=['CHK001', 'SNAP_EXP_0825_E_2025-08']),
    Task(
        annotator='gokulsaireddy',
        user_id='task_097',
        instruction=
        "Your task is to set up the new publisher 'Starlight Press' ('PUB050') and their initial project, 'History of Ancient Rome, 1e' ('PROJ4001'), with ISBN '978-1-4100-4001-1' and a default hourly rate of 90.0. The end state for the October 2024 context should show that the new publisher and project are readable, all unpaid invoices have been reviewed, 12-month KPIs are available, a sample invoice total for 3 hours at the project rate with 13% HST has been calculated, and the A/R aging report for '2024-10' has been exported.",
        actions=[
            Action(name='CreatePublisher',
                   kwargs={
                       'publisher_id': 'PUB050',
                       'name': 'Starlight Press'
                   }),
            Action(name='GetPublisherInfo', kwargs={'publisher_id': 'PUB050'}),
            Action(name='CreateProject',
                   kwargs={
                       'project_id': 'PROJ4001',
                       'publisher_id': 'PUB050',
                       'isbn': '978-1-4100-4001-1',
                       'project_title': 'History of Ancient Rome, 1e',
                       'default_hourly_rate': 90.0
                   }),
            Action(name='GetProjectDetails', kwargs={'project_id':
                                                     'PROJ4001'}),
            Action(name='FilterInvoices', kwargs={'unpaid_only': True}),
            Action(name='ComputeCollectionKPIs', kwargs={'window_months': 12}),
            Action(name='CalculateInvoiceTotals',
                   kwargs={
                       'lines': [{
                           'hours': 3,
                           'rate': 90.0
                       }],
                       'hst_rate': 0.13
                   }),
            Action(name='ExportARAgingReport',
                   kwargs={'period_label': '2024-10'})
        ],
        outputs=[
            'PUB050', 53.47, '/reports/ar_aging/AR_Aging_Report_2024-10.pdf',
            14709.21, 275.09, 305.1
        ]),
    Task(
        annotator='gokulsaireddy',
        user_id='task_098',
        instruction=
        "Your task is to set up the new publisher 'Culinary Arts Press' ('PUB054') and their initial project, 'Advanced Culinary Techniques' ('PROJ4005'), with ISBN '978-5-8500-4005-5' and a default hourly rate of 100.0. The end state for the February 2025 context should show that the new publisher and project are readable, all unpaid invoices have been reviewed, 12-month KPIs are available, a sample invoice total for 5 hours at the project rate with 13% HST has been calculated, and the A/R aging report for '2025-02' has been exported.",
        actions=[
            Action(name='CreatePublisher',
                   kwargs={
                       'publisher_id': 'PUB054',
                       'name': 'Culinary Arts Press'
                   }),
            Action(name='GetPublisherInfo', kwargs={'publisher_id': 'PUB054'}),
            Action(name='CreateProject',
                   kwargs={
                       'project_id': 'PROJ4005',
                       'publisher_id': 'PUB054',
                       'isbn': '978-5-8500-4005-5',
                       'project_title': 'Advanced Culinary Techniques',
                       'default_hourly_rate': 100.0
                   }),
            Action(name='GetProjectDetails', kwargs={'project_id':
                                                     'PROJ4005'}),
            Action(name='FilterInvoices', kwargs={'unpaid_only': True}),
            Action(name='ComputeCollectionKPIs', kwargs={'window_months': 12}),
            Action(name='CalculateInvoiceTotals',
                   kwargs={
                       'lines': [{
                           'hours': 5,
                           'rate': 100.0
                       }],
                       'hst_rate': 0.13
                   }),
            Action(name='ExportARAgingReport',
                   kwargs={'period_label': '2025-02'})
        ],
        outputs=[
            'PUB054', 14709.21, 275.09,
            '/reports/ar_aging/AR_Aging_Report_2025-02.pdf', 500.0, 565.0
        ]),
    Task(
        annotator='gokulsaireddy',
        user_id='task_099',
        instruction=
        "Your task is to produce a 30-day cash flow forecast for the period August 26, 2025 (2025-08-26), to September 25, 2025 (2025-09-25). The final analysis, which must be logged in the scheduler for 2025-08-26T12:00:00Z with a note; 30-day cash flow forecast, should find the net cash flow posed by 'Horizon Academic Press' by comparing their total unpaid expected inflows against the company's total recurring outflows for the period. This assessment should be supported by the publisher's historical payment profile.",
        actions=[
            Action(name='GetPublisherByName',
                   kwargs={'publisher_name': 'Horizon Academic Press'}),
            Action(name='FilterInvoices',
                   kwargs={
                       'publisher_id': 'PUB003',
                       'unpaid_only': True
                   }),
            Action(name='CalculateTotalInflows',
                   kwargs={
                       'start_date': '2025-08-26',
                       'end_date': '2025-09-25',
                       'invoices_to_consider': ['INV008', 'INV013', 'INV022']
                   }),
            Action(name='CalculateTotalOutflows',
                   kwargs={
                       'start_date': '2025-08-26',
                       'end_date': '2025-09-25'
                   }),
            Action(name='ComputeNetCashFlow',
                   kwargs={
                       'inflows': 3723.35,
                       'outflows': 4638.93
                   }),
            Action(name='GetPaymentBehavior',
                   kwargs={'publisher_id': 'PUB003'}),
            Action(name='AddSchedulerRun',
                   kwargs={
                       'run_date': '2025-08-26T12:00:00Z',
                       'note': '30-day cash flow forecast'
                   })
        ],
        outputs=['PUB003', '3723.35', '4638.93', 'BEH003', -915.58]),
    Task(
        annotator='gokulsaireddy',
        user_id='task_100',
        instruction=
        "Your task is to properly document a significant software expense of $1250.00 from 'Wolfram Research' dated 2025-09-10, which is associated with project 'Advanced Mathematics Textbook - Grade 12'. Also, create a financial snapshot for September 2025 with ID 'SNAP_EXP_0925', dated 2025-09-30 and log the month's existing total expenses of $1322.79. Create a new Wolfram Research expense record with ID 'EXP_WOLF_001' under the 'SOFTWARE_SUBSCR' category. Ensure the main 'checking' account balance is updated to reflect this new expenditure, resulting in a final balance of $14170.75.",
        actions=[
            Action(name='GetProjectByName',
                   kwargs={
                       'project_name':
                       'Advanced Mathematics Textbook - Grade 12'
                   }),
            Action(name='CreateDashboardSnapshot',
                   kwargs={
                       'snapshot_id': 'SNAP_EXP_0925',
                       'snapshot_date': '2025-09-30',
                       'year': 2025
                   }),
            Action(name='AddMonthlyExpense',
                   kwargs={
                       'snapshot_id': 'SNAP_EXP_0925',
                       'month': '2025-09',
                       'amount': 1322.79
                   }),
            Action(name='AddExpenseRecord',
                   kwargs={
                       'expense_id': 'EXP_WOLF_001',
                       'project_id': 'PROJ001',
                       'vendor': 'Wolfram Research',
                       'expense_date': '2025-09-10',
                       'amount': 1250.0,
                       'category_code': 'SOFTWARE_SUBSCR'
                   }),
            Action(name='GetBankAccountDetails',
                   kwargs={'account_type': 'checking'}),
            Action(name='UpdateBankAccountBalance',
                   kwargs={
                       'account_id': 'CHK001',
                       'balance': 14170.75
                   })
        ],
        outputs=['CHK001', 'SNAP_EXP_0925_2025-09'])
]
