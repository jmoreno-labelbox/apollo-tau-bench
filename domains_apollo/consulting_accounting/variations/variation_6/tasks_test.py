from tau_bench.types import Action, Task

TASKS = [
    Task(
        annotator="v6",
        user_id="task_01",
        instruction=(
            "Handle the creation of the August 2025 Accounts Receivable report for all outstanding invoices issued up to 2025-08-23, and archive a dashboard snapshot. Utilize the period label '2025-08' and designate the precise PDF location as 'https://test.storage.com/reports/accounts_receivable_2025-08.pdf'. Calculate collection KPIs over a 12-month period. Generate a dashboard snapshot dated '2025-08-23' that points to that identical PDF path. Success is determined by the report path matching that URL and the existence of a snapshot for 2025-08-23 with the precise pdf_path."
        ),
        actions=[
            Action(
                name="QueryInvoices",
                kwargs={"status": "open", "date_to": "2025-08-23"},
            ),
            Action(name="DeriveCollectionKpis", kwargs={"window_months": 12}),
            Action(
                name="RenderAccountsReceivableReport",
                kwargs={"period_label": "2025-08"},
            ),
            Action(
                name="CreateDashboardSnapshot",
                kwargs={
                    "snapshot_date": "2025-08-23",
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2025-08.pdf",
                },
            ),
            Action(
                name="FetchDashboardSnapshot", kwargs={"snapshot_date": "2025-08-23"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_02",
        instruction="Ensure confirmation of your immediate due status and carry out an export with proofing in September 2024. Your final outcome should include: computing days outstanding for '2024-024' using a period_end of '2024-10-31' and today '2024-10-29' as -2 days, categorized as 'upcoming_due'; open invoices are reviewed; confirming the existence of the Account Receivable aging PDF for '2024-09' and saving a dashboard snapshot for '2024-09-30' that refers to 'https://test.storage.com/reports/accounts_receivable_2024-09.pdf' and is accessible by id; recording an audit event 'risk_reviewed' for '2024-024' which should be listable."
                    "Your end state: days outstanding for '2024-024' using period_end '2024-10-31' and today '2024-10-29' "
                    "are computed as -2 days and categorized as 'upcoming_due'; open invoices are reviewed; "
                    "the Account Receivable aging PDF exists for '2024-09' and a dashboard snapshot for '2024-09-30' "
                    "referencing 'https://test.storage.com/reports/accounts_receivable_2024-09.pdf' is saved and readable by id; "
                    "an audit event 'risk_reviewed' is recorded for '2024-024' and is listable.",
        actions=[
            Action(
                name="DeriveDaysOutstanding",
                kwargs={
                    "invoices": [
                        {"invoice_number": "2024-024", "period_end": "2024-10-31"}
                    ],
                    "today": "2024-10-29",
                },
            ),
            Action(
                name="BucketizeAging",
                kwargs={
                    "aging": [{"days_outstanding": -2, "invoice_number": "2024-024"}]
                },
            ),
            Action(name="QueryInvoices", kwargs={"status": "open"}),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-09"}),
            Action(
                name="CreateDashboardSnapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-09.pdf",
                    "snapshot_date": "2024-09-30",
                },
            ),
            Action(name="FetchDashboardSnapshot", kwargs={"snapshot_id": 1}),
            Action(
                name="LogInvoiceEvent",
                kwargs={"event_type": "risk_reviewed", "invoice_number": "2024-024"},
            ),
            Action(name="ListInvoiceEvents", kwargs={"invoice_number": "2024-024"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_03",
        instruction="Handle the creation of a November 2024 email for invoice '2024-010' and log the audit with context. In your final state: invoice_number '2024-010' is sent via email utilizing publisher_id 'PUB004' and consultant_id 'CONS001' with the subject 'Invoice 2024-010 (November 2024)', body 'Please see attached invoice 2024-010.' and attachment 'https://test.storage.com/invoices/2024/INV-2024-010.pdf', and ensure the invoice is re-examined with sent_at filled in; an audit event 'emailed' is documented and available for listing; examine open invoices; make 12-month KPIs accessible; and generate the Account Receivable aging PDF for '2024-11'."
                    "Your end state: invoice_number '2024-010' is emailed using publisher_id 'PUB004' and consultant_id '"
                    "CONS001' with subject 'Invoice 2024-010 (November 2024)', body 'Please see attached invoice 2024-010.' "
                    "and attachment 'https://test.storage.com/invoices/2024/INV-2024-010.pdf', and the "
                    "invoice is re‑read with sent_at populated; an audit event 'emailed' is recorded and listable; "
                    "open invoices are reviewed; 12‑month KPIs are available; the Account Receivable aging PDF exists for '2024-11'.",
        actions=[
            Action(
                name="DispatchInvoiceEmail",
                kwargs={
                    "attachment": "https://test.storage.com/invoices/2024/INV-2024-010.pdf",
                    "body_text": "Please see attached invoice 2024-010.",
                    "consultant_id": "CONS001",
                    "invoice_number": "2024-010",
                    "publisher_id": "PUB004",
                    "subject": "Invoice 2024-010 (November 2024)",
                },
            ),
            Action(name="FetchInvoiceRecord", kwargs={"invoice_number": "2024-010"}),
            Action(
                name="LogInvoiceEvent",
                kwargs={"event_type": "emailed", "invoice_number": "2024-010"},
            ),
            Action(name="ListInvoiceEvents", kwargs={"invoice_number": "2024-010"}),
            Action(name="QueryInvoices", kwargs={"status": "open"}),
            Action(name="DeriveCollectionKpis", kwargs={"window_months": 12}),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-11"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_04",
        instruction="Coordinate the update of contact information and validate a September 2024 total with context. In the resulting state: update contact_email for publisher_id 'PUB003' to 'accounts@canopypress.ca' ensuring it is visible; change consultant_id 'CONS001' phone to '+1-416-555-0199' ensuring it is visible; inspect open invoices (status 'open') and calculate 12-month KPIs; determine resolve rates for ['PROJ001','PROJ003'] and calculate sample totals (3h @85.0 and 2h @75.0 with hst_rate 0.13); generate the Account Receivable aging '2024-09'. Confirm each update through a subsequent verification read.",
        actions=[
            Action(
                name="MutateClientContact",
                kwargs={
                    "contact_email": "accounts@canopypress.ca",
                    "publisher_id": "PUB003",
                },
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB003"}),
            Action(
                name="MutateConsultantContact",
                kwargs={"consultant_id": "CONS001", "phone": "+1-416-555-0199"},
            ),
            Action(name="FetchConsultantProfile", kwargs={"consultant_id": "CONS001"}),
            Action(name="QueryInvoices", kwargs={"status": "open"}),
            Action(name="DeriveCollectionKpis", kwargs={"window_months": 12}),
            Action(
                name="MapHourlyRates",
                kwargs={"project_id_list": ["PROJ001", "PROJ003"]},
            ),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={
                    "hst_rate": 0.13,
                    "lines": [{"hours": 3, "rate": 85.0}, {"hours": 2, "rate": 75.0}],
                },
            ),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-09"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_05",
        instruction="Handle the addition of publisher_id 'PUB056' named 'Cobalt Creek Press' and coordinate a September‑2024 sample with rates. Your objective: 'PUB056' is created and accessible; project_id 'PROJ3083' is established with isbn '978-1-3100-3083-6', project_title 'Intro Sociology, 1e', default_hourly_rate 86.0 and is accessible; rates are resolved for ['PROJ3083','PROJ001']; compute a sample total (2h @86.0 and 1h @85.0 with hst_rate 0.13); ensure the Account Receivable aging PDF is available for '2024-09'.",
        actions=[
            Action(
                name="AddClientProfile",
                kwargs={"name": "Cobalt Creek Press", "publisher_id": "PUB056"},
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB056"}),
            Action(
                name="AddProjectCard",
                kwargs={
                    "default_hourly_rate": 86.0,
                    "isbn": "978-1-3100-3083-6",
                    "project_id": "PROJ3083",
                    "project_title": "Intro Sociology, 1e",
                    "publisher_id": "PUB056",
                },
            ),
            Action(name="FetchProjectCard", kwargs={"project_id": "PROJ3083"}),
            Action(
                name="MapHourlyRates",
                kwargs={"project_id_list": ["PROJ3083", "PROJ001"]},
            ),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={
                    "hst_rate": 0.13,
                    "lines": [{"hours": 2, "rate": 86.0}, {"hours": 1, "rate": 85.0}],
                },
            ),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-09"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_06",
        instruction="Document a September‑2024 invoice for publisher_id 'PUB001' and maintain its audit, ensuring time entries are validated initially. Your objective: verify a representative time‑entry row with description 'September hours', isbn '978-1-3100-0001-0', account_code 'ENG-1E' and hours_worked 6; make sure invoice_number '2024-132' is present for period_start '2024-09-01' and period_end '2024-09-30' with totals (subtotal 510.0, hst_amount 66.3, total_due 576.3) and is accessible; ensure an audit event 'generated' is recorded and can be listed; confirm the Account Receivable aging PDF is available for '2024-09'. Utilize pdf_path 'https://test.storage.com/invoices/2024/INV-2024-132.pdf'.",
        actions=[
            Action(
                name="AuditTimeEntries",
                kwargs={
                    "rows": [
                        {
                            "account_code": "ENG-1E",
                            "description": "September hours",
                            "hours_worked": 6,
                            "isbn": "978-1-3100-0001-0",
                        }
                    ]
                },
            ),
            Action(
                name="CreateInvoiceRecord",
                kwargs={
                    "hst_amount": 66.3,
                    "invoice_date": "2024-09-30",
                    "invoice_number": "2024-132",
                    "pdf_path": "https://test.storage.com/invoices/2024/INV-2024-132.pdf",
                    "period_end": "2024-09-30",
                    "period_start": "2024-09-01",
                    "publisher_id": "PUB001",
                    "subtotal": 510.0,
                    "total_due": 576.3,
                },
            ),
            Action(name="FetchInvoiceRecord", kwargs={"invoice_number": "2024-132"}),
            Action(
                name="LogInvoiceEvent",
                kwargs={"event_type": "generated", "invoice_number": "2024-132"},
            ),
            Action(name="ListInvoiceEvents", kwargs={"invoice_number": "2024-132"}),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-09"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_07",
        instruction="Handle an Account Receivable health pass and onboard a fresh client. Your objective: new publisher_id 'PUB011' is created with precisely name 'Canopy Learning Ltd.', address '77 Front St E, Montreal, ON', contact_email 'ap@canopylearning.ca', gst_number 'GST-999-011' and is accessible; 12-month collection KPIs (window_months 12) are derived; the Account Receivable aging for period_label '2024-09' is exported; and publisher_id 'PUB003' has contact_email changed to 'ap@canopypress.ca' and is accessible. Each write operation is confirmed through a subsequent read.",
        actions=[
            Action(
                name="AddClientProfile",
                kwargs={
                    "address": "77 Front St E, Montreal, ON",
                    "contact_email": "ap@canopylearning.ca",
                    "gst_number": "GST-999-011",
                    "name": "Canopy Learning Ltd.",
                    "publisher_id": "PUB011",
                },
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB011"}),
            Action(name="DeriveCollectionKpis", kwargs={"window_months": 12}),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-09"}),
            Action(
                name="MutateClientContact",
                kwargs={"contact_email": "ap@canopypress.ca", "publisher_id": "PUB003"},
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB003"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_08",
        instruction="Coordinate the normalization of contacts and assess an October‒2024 sample for publisher_id 'PUB003' with an aging classification. Your objective: 'PUB003' contact_email is 'accounts@canopypress.ca' and is accessible; CONS001 address is '1234 Oak Street, Montreal, ON M5V 3A8' and is accessible; rates are settled for ['PROJ003']; a sample total is determined (2h @75.0 with hst_rate 0.13); days overdue for '2024-010' as of '2024-11-15' using period_end '2024-10-31' (15 days) are classified; the Account Receivable aging PDF exists for '2024-10'.",
        actions=[
            Action(
                name="MutateClientContact",
                kwargs={
                    "contact_email": "accounts@canopypress.ca",
                    "publisher_id": "PUB003",
                },
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB003"}),
            Action(
                name="MutateConsultantContact",
                kwargs={
                    "address": "1234 Oak Street, Montreal, ON M5V 3A8",
                    "consultant_id": "CONS001",
                },
            ),
            Action(name="FetchConsultantProfile", kwargs={"consultant_id": "CONS001"}),
            Action(
                name="MapHourlyRates", kwargs={"project_id_list": ["PROJ003"]}
            ),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 2, "rate": 75.0}]},
            ),
            Action(
                name="DeriveDaysOutstanding",
                kwargs={
                    "invoices": [
                        {"invoice_number": "2024-010", "period_end": "2024-10-31"}
                    ],
                    "today": "2024-11-15",
                },
            ),
            Action(
                name="BucketizeAging",
                kwargs={
                    "aging": [{"days_outstanding": 15, "invoice_number": "2024-010"}]
                },
            ),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-10"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_09",
        instruction="Handle publisher_id 'PUB024' under the name 'Aurora Study House' and synchronize the September‑2024 reporting. Your final outcome: 'PUB024' is present and can be seen; open invoices are checked; KPIs spanning 12 months can be accessed; the Account Receivable aging PDF for '2024-09' is available and a snapshot is saved for '2024-09-30' referring to that PDF; a sample total is calculated (2h @85.0 and 2h @75.0 with hst_rate 0.13) applying rates for ['PROJ001','PROJ003'].",
        actions=[
            Action(
                name="AddClientProfile",
                kwargs={"name": "Aurora Study House", "publisher_id": "PUB024"},
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB024"}),
            Action(name="QueryInvoices", kwargs={"status": "open"}),
            Action(name="DeriveCollectionKpis", kwargs={"window_months": 12}),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-09"}),
            Action(
                name="CreateDashboardSnapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-09.pdf",
                    "snapshot_date": "2024-09-30",
                },
            ),
            Action(
                name="FetchDashboardSnapshot",
                kwargs={"snapshot_date": "2024-09-30"},
            ),
            Action(
                name="MapHourlyRates",
                kwargs={"project_id_list": ["PROJ001", "PROJ003"]},
            ),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={
                    "hst_rate": 0.13,
                    "lines": [{"hours": 2, "rate": 85.0}, {"hours": 2, "rate": 75.0}],
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_10",
        instruction="Coordinate a computation and classification of a November‑2024 aging check and confirm with a stored snapshot. The desired result: days outstanding for invoice '2024-021' as of '2024-11-20' using period_end '2024-10-31' (20 days) are classified; projects are itemized; 'PROJ003' details are accessible; rates are identified for ['PROJ003']; a sample total is determined (1h @75.0 with hst_rate 0.13); open invoices are checked; KPIs over 12 months are accessible; the Account Receivable aging PDF for '2024-11' exists; a dashboard snapshot is recorded for '2024-11-30' and can be viewed by date.",
        actions=[
            Action(
                name="DeriveDaysOutstanding",
                kwargs={
                    "invoices": [
                        {"invoice_number": "2024-021", "period_end": "2024-10-31"}
                    ],
                    "today": "2024-11-20",
                },
            ),
            Action(
                name="BucketizeAging",
                kwargs={
                    "aging": [{"days_outstanding": 20, "invoice_number": "2024-021"}]
                },
            ),
            Action(name="ListProjectsCatalog", kwargs={}),
            Action(name="FetchProjectCard", kwargs={"project_id": "PROJ003"}),
            Action(
                name="MapHourlyRates", kwargs={"project_id_list": ["PROJ003"]}
            ),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 1, "rate": 75.0}]},
            ),
            Action(name="QueryInvoices", kwargs={"status": "open"}),
            Action(name="DeriveCollectionKpis", kwargs={"window_months": 12}),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-11"}),
            Action(
                name="CreateDashboardSnapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-11.pdf",
                    "snapshot_date": "2024-11-30",
                },
            ),
            Action(
                name="FetchDashboardSnapshot",
                kwargs={"snapshot_date": "2024-11-30"},
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_11",
        instruction="Ensure readiness for November 2024 for publisher_id 'PUB004' by initiating a data science project and verifying totals with an aging categorization. The desired outcome: project_id 'PROJ3081' exists with isbn '978-1-3100-3081-2', project_title 'Data Science Projects, 1e', default_hourly_rate 106.0 and is readable; rates are resolved for ['PROJ3081']; compute a sample total (1h @106.0 with hst_rate 0.13); review open invoices; Account Receivable aging PDF is available for '2024-11'; categorize 15 days as outstanding for '2024-010' as of '2024-11-15' using period_end '2024-10-31'.",
        actions=[
            Action(
                name="AddProjectCard",
                kwargs={
                    "default_hourly_rate": 106.0,
                    "isbn": "978-1-3100-3081-2",
                    "project_id": "PROJ3081",
                    "project_title": "Data Science Projects, 1e",
                    "publisher_id": "PUB004",
                },
            ),
            Action(name="FetchProjectCard", kwargs={"project_id": "PROJ3081"}),
            Action(
                name="MapHourlyRates", kwargs={"project_id_list": ["PROJ3081"]}
            ),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 1, "rate": 106.0}]},
            ),
            Action(name="QueryInvoices", kwargs={"status": "open"}),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-11"}),
            Action(
                name="DeriveDaysOutstanding",
                kwargs={
                    "invoices": [
                        {"invoice_number": "2024-010", "period_end": "2024-10-31"}
                    ],
                    "today": "2024-11-15",
                },
            ),
            Action(
                name="BucketizeAging",
                kwargs={
                    "aging": [{"days_outstanding": 15, "invoice_number": "2024-010"}]
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_12",
        instruction="Add a focused writing project and synchronize October 2024 reporting for publisher_id 'PUB004'. The goal is: project_id 'PROJ1011' exists with isbn '978-1-3100-1011-0', project_title 'Writing Workshop, 1e', default_hourly_rate 94.0 and is visible; 'PUB004' is readable; rates are solved for ['PROJ1011','PROJ001'] and calculate a sample total (2h @94.0 plus 3h @85.0 with hst_rate 0.13); review open invoices and ensure 12-month KPIs are accessible; the Account Receivable aging PDF is present for '2024-10' and save a snapshot for '2024-10-31' referencing that PDF.",
        actions=[
            Action(
                name="AddProjectCard",
                kwargs={
                    "default_hourly_rate": 94.0,
                    "isbn": "978-1-3100-1011-0",
                    "project_id": "PROJ1011",
                    "project_title": "Writing Workshop, 1e",
                    "publisher_id": "PUB004",
                },
            ),
            Action(name="FetchProjectCard", kwargs={"project_id": "PROJ1011"}),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB004"}),
            Action(
                name="MapHourlyRates",
                kwargs={"project_id_list": ["PROJ1011", "PROJ001"]},
            ),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={
                    "hst_rate": 0.13,
                    "lines": [{"hours": 2, "rate": 94.0}, {"hours": 3, "rate": 85.0}],
                },
            ),
            Action(name="QueryInvoices", kwargs={"status": "open"}),
            Action(name="DeriveCollectionKpis", kwargs={"window_months": 12}),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-10"}),
            Action(
                name="CreateDashboardSnapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-10.pdf",
                    "snapshot_date": "2024-10-31",
                },
            ),
            Action(
                name="FetchDashboardSnapshot",
                kwargs={"snapshot_date": "2024-10-31"},
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_13",
        instruction="Handle the creation of publisher_id 'PUB045' with the name 'Northern Summit Press' and arrange a July‑2024 sample. Your end state: 'PUB045' should exist and be readable; project_id 'PROJ3059' is present with isbn '978-1-3100-3059-6', project_title 'Intro Philosophy, 1e', default_hourly_rate 87.0 and it is accessible; rates are decided for ['PROJ3059','PROJ001']; a sample total must be calculated (1h @87.0 and 1h @85.0 with hst_rate 0.13); the Account Receivable aging PDF is available for '2024-07'.",
        actions=[
            Action(
                name="AddClientProfile",
                kwargs={"name": "Northern Summit Press", "publisher_id": "PUB045"},
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB045"}),
            Action(
                name="AddProjectCard",
                kwargs={
                    "default_hourly_rate": 87.0,
                    "isbn": "978-1-3100-3059-6",
                    "project_id": "PROJ3059",
                    "project_title": "Intro Philosophy, 1e",
                    "publisher_id": "PUB045",
                },
            ),
            Action(name="FetchProjectCard", kwargs={"project_id": "PROJ3059"}),
            Action(
                name="MapHourlyRates",
                kwargs={"project_id_list": ["PROJ3059", "PROJ001"]},
            ),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={
                    "hst_rate": 0.13,
                    "lines": [{"hours": 1, "rate": 87.0}, {"hours": 1, "rate": 85.0}],
                },
            ),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-07"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_14",
        instruction="Coordinate the finalization of a September‑2024 invoice for publisher_id 'PUB003' and document its audit. Your end state: invoice_number '2024-142' is established for period_start '2024-09-01' and period_end '2024-09-30' with accurate totals (2h @97.0, hst_rate 0.13) and is accessible; a single line entry is located for project_id 'PROJ003' with isbn '978-1-3100-0003-7' for 2h @97.0 and is listable; an audit event 'generated' is recorded and listable. Utilize pdf_path 'https://test.storage.com/invoices/2024/INV-2024-142.pdf'.",
        actions=[
            Action(
                name="CreateInvoiceRecord",
                kwargs={
                    "hst_amount": 25.22,
                    "invoice_date": "2024-09-30",
                    "invoice_number": "2024-142",
                    "pdf_path": "https://test.storage.com/invoices/2024/INV-2024-142.pdf",
                    "period_end": "2024-09-30",
                    "period_start": "2024-09-01",
                    "publisher_id": "PUB003",
                    "subtotal": 194.0,
                    "total_due": 219.22,
                },
            ),
            Action(name="FetchInvoiceRecord", kwargs={"invoice_number": "2024-142"}),
            Action(
                name="CreateInvoiceLines",
                kwargs={
                    "invoice_number": "2024-142",
                    "lines": [
                        {
                            "hours": 2,
                            "isbn": "978-1-3100-0003-7",
                            "project_id": "PROJ003",
                            "rate": 97.0,
                        }
                    ],
                },
            ),
            Action(name="ListInvoiceLinesByInvoice", kwargs={"invoice_number": "2024-142"}),
            Action(
                name="LogInvoiceEvent",
                kwargs={"event_type": "generated", "invoice_number": "2024-142"},
            ),
            Action(name="ListInvoiceEvents", kwargs={"invoice_number": "2024-142"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_15",
        instruction="Handle the formalization of a November‑2024 email for invoice '2024-010' and document the audit with context. The desired outcome: invoice_number '2024-010' is sent via email using publisher_id 'PUB004' and consultant_id 'CONS001' with the subject 'Invoice 2024-010 (November 2024)', body 'Please see attached invoice 2024-010.' and attachment 'https://test.storage.com/invoices/2024/INV-2024-010.pdf', and ensure the invoice is re‑examined with sent_at updated; an 'emailed' audit event is logged and made listable; review open invoices; ensure 12‑month KPIs are available; verify the existence of the Account Receivable aging PDF for '2024-11'."
                    "Your end state: invoice_number '2024-010' is emailed using publisher_id 'PUB004' and consultant_id '"
                    "CONS001' with subject 'Invoice 2024-010 (November 2024)', body 'Please see attached invoice 2024-010.' "
                    "and attachment 'https://test.storage.com/invoices/2024/INV-2024-010.pdf', and the "
                    "invoice is re‑read with sent_at populated; an audit event 'emailed' is recorded and listable; "
                    "open invoices are reviewed; 12‑month KPIs are available; the Account Receivable aging PDF exists for '2024-11'.",
        actions=[
            Action(
                name="DispatchInvoiceEmail",
                kwargs={
                    "attachment": "https://test.storage.com/invoices/2024/INV-2024-010.pdf",
                    "body_text": "Please see attached invoice 2024-010.",
                    "consultant_id": "CONS001",
                    "invoice_number": "2024-010",
                    "publisher_id": "PUB004",
                    "subject": "Invoice 2024-010 (November 2024)",
                },
            ),
            Action(name="FetchInvoiceRecord", kwargs={"invoice_number": "2024-010"}),
            Action(
                name="LogInvoiceEvent",
                kwargs={"event_type": "emailed", "invoice_number": "2024-010"},
            ),
            Action(name="ListInvoiceEvents", kwargs={"invoice_number": "2024-010"}),
            Action(name="QueryInvoices", kwargs={"status": "open"}),
            Action(name="DeriveCollectionKpis", kwargs={"window_months": 12}),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-11"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_16",
        instruction="Coordinate the onboarding of publisher_id 'PUB040' with the name 'Red Maple Learning' and include a math project while preparing a September‑2024 snapshot. The final outcome: 'PUB040' is established and accessible; project_id 'PROJ2053' is created with isbn '978-1-3100-2053-4', project_title 'Pre‑Calculus, 1e', default_hourly_rate 99.0 and is accessible; calculate a sample total (2h @99.0 with hst_rate 0.13); ensure the Account Receivable aging PDF is available for '2024-09' and a dashboard snapshot is stored for '2024-09-30' linked to 'https://test.storage.com/reports/accounts_receivable_2024-09.pdf' and accessible by id.",
        actions=[
            Action(
                name="AddClientProfile",
                kwargs={"name": "Red Maple Learning", "publisher_id": "PUB040"},
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB040"}),
            Action(
                name="AddProjectCard",
                kwargs={
                    "default_hourly_rate": 99.0,
                    "isbn": "978-1-3100-2053-4",
                    "project_id": "PROJ2053",
                    "project_title": "Pre‑Calculus, 1e",
                    "publisher_id": "PUB040",
                },
            ),
            Action(name="FetchProjectCard", kwargs={"project_id": "PROJ2053"}),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 2, "rate": 99.0}]},
            ),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-09"}),
            Action(
                name="CreateDashboardSnapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-09.pdf",
                    "snapshot_date": "2024-09-30",
                },
            ),
            Action(name="FetchDashboardSnapshot", kwargs={"snapshot_id": 1}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_17",
        instruction="Handle the creation of a November‑2024 invoice for publisher_id 'PUB005' and ensure its audit is logged. Desired outcome: prior to invoicing, confirm a representative time‑entry row with the description 'Hours for November', isbn '978-1-3100-2027-8', account_code 'DATA-LIT-1E', and hours_worked 3; calculate totals for one line (3h @90.0, hst_rate 0.13); verify that invoice_number '2024-130' is present for period_start '2024-11-01' and period_end '2024-11-30' with the specified totals and that it is accessible; an audit event 'generated' should be documented and available for listing. Ensure the pdf_path 'https://test.storage.com/invoices/2024/INV-2024-130.pdf' is used.",
        actions=[
            Action(
                name="AuditTimeEntries",
                kwargs={
                    "rows": [
                        {
                            "account_code": "DATA-LIT-1E",
                            "description": "Hours for November",
                            "hours_worked": 3,
                            "isbn": "978-1-3100-2027-8",
                        }
                    ]
                },
            ),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 3, "rate": 90.0}]},
            ),
            Action(
                name="CreateInvoiceRecord",
                kwargs={
                    "hst_amount": 35.1,
                    "invoice_date": "2024-11-30",
                    "invoice_number": "2024-130",
                    "pdf_path": "https://test.storage.com/invoices/2024/INV-2024-130.pdf",
                    "period_end": "2024-11-30",
                    "period_start": "2024-11-01",
                    "publisher_id": "PUB005",
                    "subtotal": 270.0,
                    "total_due": 305.1,
                },
            ),
            Action(name="FetchInvoiceRecord", kwargs={"invoice_number": "2024-130"}),
            Action(
                name="LogInvoiceEvent",
                kwargs={"event_type": "generated", "invoice_number": "2024-130"},
            ),
            Action(name="ListInvoiceEvents", kwargs={"invoice_number": "2024-130"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_18",
        instruction="Coordinate the normalization of contact info and finalize a September‑2024 review for publisher_id 'PUB001'. Desired outcome: contact_email is 'ap@nelson-edu.ca' and accessible; invoice_number '2024-021' is accessible; an audit event 'review_follow_up' is logged for '2024-021' and available for listing; export the Account Receivable aging for '2024-09' and save a dashboard snapshot for '2024-09-30'; execute a quick risk evaluation by determining days outstanding for '2024-021' from due_date '2024-09-15' to today '2024-10-01' and categorize accordingly.",
        actions=[
            Action(
                name="MutateClientContact",
                kwargs={"contact_email": "ap@nelson-edu.ca", "publisher_id": "PUB001"},
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB001"}),
            Action(name="FetchInvoiceRecord", kwargs={"invoice_number": "2024-021"}),
            Action(
                name="LogInvoiceEvent",
                kwargs={"event_type": "review_follow_up", "invoice_number": "2024-021"},
            ),
            Action(name="ListInvoiceEvents", kwargs={"invoice_number": "2024-021"}),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-09"}),
            Action(
                name="CreateDashboardSnapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-09.pdf",
                    "snapshot_date": "2024-09-30",
                },
            ),
            Action(
                name="FetchDashboardSnapshot",
                kwargs={"snapshot_date": "2024-09-30"},
            ),
            Action(
                name="DeriveDaysOutstanding",
                kwargs={
                    "invoices": [
                        {
                            "due_date": "2024-09-15",
                            "invoice_date": "2024-09-15",
                            "invoice_number": "2024-021",
                        }
                    ],
                    "today": "2024-10-01",
                },
            ),
            Action(
                name="BucketizeAging",
                kwargs={
                    "aging": [{"days_outstanding": 16, "invoice_number": "2024-021"}]
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_19",
        instruction="Handle the addition of publisher_id 'PUB057' with the name 'Harbor Lights Learning' and organize an August‑2024 dashboard reflecting a minimal total. Your end state should achieve: 'PUB057' existing and readable; an example total calculated (1h @85.0 with hst_rate 0.13) utilizing the rate for ['PROJ001']; the Account Receivable aging PDF being available for '2024-08'; a dashboard snapshot saved for '2024-08-31' and accessible by date; days outstanding for '2024-010' as of '2024-08-15', using period_end '2024-07-31' (15 days), are categorized.",
        actions=[
            Action(
                name="AddClientProfile",
                kwargs={"name": "Harbor Lights Learning", "publisher_id": "PUB057"},
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB057"}),
            Action(
                name="MapHourlyRates", kwargs={"project_id_list": ["PROJ001"]}
            ),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 1, "rate": 85.0}]},
            ),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-08"}),
            Action(
                name="CreateDashboardSnapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-08.pdf",
                    "snapshot_date": "2024-08-31",
                },
            ),
            Action(
                name="FetchDashboardSnapshot",
                kwargs={"snapshot_date": "2024-08-31"},
            ),
            Action(
                name="DeriveDaysOutstanding",
                kwargs={
                    "invoices": [
                        {"invoice_number": "2024-010", "period_end": "2024-07-31"}
                    ],
                    "today": "2024-08-15",
                },
            ),
            Action(
                name="BucketizeAging",
                kwargs={
                    "aging": [{"days_outstanding": 15, "invoice_number": "2024-010"}]
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_20",
        instruction="Coordinate the creation of a September‑2024 invoice for publisher_id 'PUB003'. Your end state should confirm that invoice_number '2024-131' exists for period_start '2024-09-01' and period_end '2024-09-30', with totals subtotal 388.0, hst_amount 50.44, total_due 438.44 using hst_rate 0.13, and is readable; invoice lines are inserted for project_id 'PROJ2032' with isbn '978-1-3100-2032-2' (4h @97.0) and can be listed; an audit event 'generated' is recorded and listable. Employ pdf_path 'https://test.storage.com/invoices/2024/INV-2024-131.pdf'.",
        actions=[
            Action(
                name="CreateInvoiceRecord",
                kwargs={
                    "hst_amount": 50.44,
                    "invoice_date": "2024-09-30",
                    "invoice_number": "2024-131",
                    "pdf_path": "https://test.storage.com/invoices/2024/INV-2024-131.pdf",
                    "period_end": "2024-09-30",
                    "period_start": "2024-09-01",
                    "publisher_id": "PUB003",
                    "subtotal": 388.0,
                    "total_due": 438.44,
                },
            ),
            Action(name="FetchInvoiceRecord", kwargs={"invoice_number": "2024-131"}),
            Action(
                name="CreateInvoiceLines",
                kwargs={
                    "invoice_number": "2024-131",
                    "lines": [
                        {
                            "hours": 4,
                            "isbn": "978-1-3100-2032-2",
                            "project_id": "PROJ2032",
                            "rate": 97.0,
                        }
                    ],
                },
            ),
            Action(name="ListInvoiceLinesByInvoice", kwargs={"invoice_number": "2024-131"}),
            Action(
                name="LogInvoiceEvent",
                kwargs={"event_type": "generated", "invoice_number": "2024-131"},
            ),
            Action(name="ListInvoiceEvents", kwargs={"invoice_number": "2024-131"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_21",
        instruction="Handle the addition of publisher_id 'PUB039' with the name 'Coastal Curriculum Press' and prepare a simultaneous export. Your goal state: 'PUB039' is present and accessible; the Account Receivable aging PDFs for '2024-08' and '2024-09' are available; a dashboard snapshot for '2024-08-31' is archived, reflecting the '2024-08' PDF, and is accessible; open invoices undergo evaluation.",
        actions=[
            Action(
                name="AddClientProfile",
                kwargs={"name": "Coastal Curriculum Press", "publisher_id": "PUB039"},
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB039"}),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-08"}),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-09"}),
            Action(
                name="CreateDashboardSnapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-08.pdf",
                    "snapshot_date": "2024-08-31",
                },
            ),
            Action(
                name="FetchDashboardSnapshot",
                kwargs={"snapshot_date": "2024-08-31"},
            ),
            Action(name="QueryInvoices", kwargs={"status": "open"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_22",
        instruction="Register publisher_id 'PUB037' called 'Seaway Academics' and construct a snapshot for September–2024. Your final condition: 'PUB037' is present and accessible; project_id 'PROJ2046' is available under 'PUB037' featuring isbn '978-1-3100-2046-1', project_title 'Statistics Primer, 1e', with default_hourly_rate 95.0, and is viewable; a sample total calculation is conducted (2h @95.0 with hst_rate 0.13); open invoices are assessed; the Account Receivable aging PDF exists for '2024-09' and a snapshot is documented for '2024-09-30' linked to 'https://test.storage.com/reports/accounts_receivable_2024-09.pdf' and is viewable by id.",
        actions=[
            Action(
                name="AddClientProfile",
                kwargs={"name": "Seaway Academics", "publisher_id": "PUB037"},
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB037"}),
            Action(
                name="AddProjectCard",
                kwargs={
                    "default_hourly_rate": 95.0,
                    "isbn": "978-1-3100-2046-1",
                    "project_id": "PROJ2046",
                    "project_title": "Statistics Primer, 1e",
                    "publisher_id": "PUB037",
                },
            ),
            Action(name="FetchProjectCard", kwargs={"project_id": "PROJ2046"}),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 2, "rate": 95.0}]},
            ),
            Action(name="QueryInvoices", kwargs={"status": "open"}),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-09"}),
            Action(
                name="CreateDashboardSnapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-09.pdf",
                    "snapshot_date": "2024-09-30",
                },
            ),
            Action(name="FetchDashboardSnapshot", kwargs={"snapshot_id": 1}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_23",
        instruction="Handle the addition of publisher_id 'PUB041' titled 'Evergreen Academic House' and a writing project, followed by confirming October‑2024 totals. Your end state should be: 'PUB041' exists and is visible; 'PROJ2055' exists, having isbn '978-1-3100-2055-8', project_title 'Essay Skills, 1e', default_hourly_rate 91.0 and is visible; rates are resolved for ['PROJ2055','PROJ001'] and a sample total is calculated (2h @91.0 and 1h @85.0 with hst_rate 0.13); the Account Receivable aging PDF exists for '2024-10'.",
        actions=[
            Action(
                name="AddClientProfile",
                kwargs={"name": "Evergreen Academic House", "publisher_id": "PUB041"},
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB041"}),
            Action(
                name="AddProjectCard",
                kwargs={
                    "default_hourly_rate": 91.0,
                    "isbn": "978-1-3100-2055-8",
                    "project_id": "PROJ2055",
                    "project_title": "Essay Skills, 1e",
                    "publisher_id": "PUB041",
                },
            ),
            Action(name="FetchProjectCard", kwargs={"project_id": "PROJ2055"}),
            Action(
                name="MapHourlyRates",
                kwargs={"project_id_list": ["PROJ2055", "PROJ001"]},
            ),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={
                    "hst_rate": 0.13,
                    "lines": [{"hours": 2, "rate": 91.0}, {"hours": 1, "rate": 85.0}],
                },
            ),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-10"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_24",
        instruction="Coordinate the updating of October‑2024 contacts and the execution of KPIs with a brief risk check. Your end state should be: publisher_id 'PUB004' contact_email is 'ap@bluepeakpublishing.ca' and is readable; open invoices have been reviewed and 12‑month KPIs are accessible; Account Receivable aging for '2024-10' is exported and a snapshot saved for '2024-10-31'; for risk, days outstanding are calculated for invoice_number '2024-024' using due_date '2024-10-31' as of '2024-11-05' and categorized.",
        actions=[
            Action(
                name="MutateClientContact",
                kwargs={
                    "contact_email": "ap@bluepeakpublishing.ca",
                    "publisher_id": "PUB004",
                },
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB004"}),
            Action(name="QueryInvoices", kwargs={"status": "open"}),
            Action(name="DeriveCollectionKpis", kwargs={"window_months": 12}),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-10"}),
            Action(
                name="CreateDashboardSnapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-10.pdf",
                    "snapshot_date": "2024-10-31",
                },
            ),
            Action(
                name="FetchDashboardSnapshot",
                kwargs={"snapshot_date": "2024-10-31"},
            ),
            Action(
                name="DeriveDaysOutstanding",
                kwargs={
                    "invoices": [
                        {
                            "due_date": "2024-10-31",
                            "invoice_date": "2024-10-31",
                            "invoice_number": "2024-024",
                        }
                    ],
                    "today": "2024-11-05",
                },
            ),
            Action(
                name="BucketizeAging",
                kwargs={
                    "aging": [{"days_outstanding": 5, "invoice_number": "2024-024"}]
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_25",
        instruction="Handle the registration of publisher_id 'PUB052' with the name 'Aurora Ridge Press' and deposit a snapshot for November‑2024 along with a small sample. Your end state: 'PUB052' is in existence and can be read; open invoices have been reviewed; 12‑month KPIs are accessible; rates are settled for ['PROJ001']; calculate a sample total (1h @85.0 with hst_rate 0.13); the Account Receivable aging PDF for '2024-11' is available; a dashboard snapshot for '2024-11-30' is stored and accessible by date.",
        actions=[
            Action(
                name="AddClientProfile",
                kwargs={"name": "Aurora Ridge Press", "publisher_id": "PUB052"},
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB052"}),
            Action(name="QueryInvoices", kwargs={"status": "open"}),
            Action(name="DeriveCollectionKpis", kwargs={"window_months": 12}),
            Action(
                name="MapHourlyRates", kwargs={"project_id_list": ["PROJ001"]}
            ),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 1, "rate": 85.0}]},
            ),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-11"}),
            Action(
                name="CreateDashboardSnapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-11.pdf",
                    "snapshot_date": "2024-11-30",
                },
            ),
            Action(
                name="FetchDashboardSnapshot",
                kwargs={"snapshot_date": "2024-11-30"},
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_26",
        instruction="Coordinate the November‑2024 email process for a pending invoice. Your end state: invoice_number '2024-011' has been emailed using publisher_id 'PUB005' and consultant_id 'CONS001' with the subject 'Invoice 2024-011 (November 2024)', body 'Friendly reminder: attached is invoice 2024-011.' and attachment 'https://test.storage.com/invoices/2024/INV-2024-011.pdf', and ensure the invoice is re‑reviewed with sent_at filled in; an audit event 'emailed' is logged and can be listed; open invoices are examined; 12‑month KPIs are on hand; the Account Receivable aging PDF is available for '2024-11'.",
        actions=[
            Action(
                name="DispatchInvoiceEmail",
                kwargs={
                    "attachment": "https://test.storage.com/invoices/2024/INV-2024-011.pdf",
                    "body_text": "Friendly reminder: attached is invoice 2024-011.",
                    "consultant_id": "CONS001",
                    "invoice_number": "2024-011",
                    "publisher_id": "PUB005",
                    "subject": "Invoice 2024-011 (November 2024)",
                },
            ),
            Action(name="FetchInvoiceRecord", kwargs={"invoice_number": "2024-011"}),
            Action(
                name="LogInvoiceEvent",
                kwargs={"event_type": "emailed", "invoice_number": "2024-011"},
            ),
            Action(name="ListInvoiceEvents", kwargs={"invoice_number": "2024-011"}),
            Action(name="QueryInvoices", kwargs={"status": "open"}),
            Action(name="DeriveCollectionKpis", kwargs={"window_months": 12}),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-11"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_27",
        instruction=(
            "Begin a new publisher setup and ensure alignment with a November-2024 review. Your objective: publisher_id 'PUB022' named 'Bayview K12' is established and accessible; project_id 'PROJ1104' is present under 'PUB022' with isbn '978-1-3100-1013-2', project_title 'Civics Basics, 1e', default_hourly_rate 80.0, and is accessible; rates are finalized for ['PROJ1104']; calculate a sample total for 6h @80.0 using compute_invoice_totals considering HST rate 0.13; review open invoices and obtain 12-month KPIs; export Accounts Receivable aging for '2024-11' as a PDF (PDF: 'https://test.storage.com/reports/accounts_receivable_2024-11.pdf'); ensure a dashboard snapshot for '2024-11-30' is available and accessible by snapshot_date—if one already exists for that day, utilize it; otherwise, save a snapshot for '2024-11-30' using the same A/R PDF and confirm by fetching with the snapshot_date."
        ),
    actions=[
            Action(
                name="AddClientProfile",
                kwargs={"name": "Bayview K12", "publisher_id": "PUB022"},
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB022"}),
            Action(
                name="AddProjectCard",
                kwargs={
                    "default_hourly_rate": 80.0,
                    "isbn": "978-1-3100-1013-2",
                    "project_id": "PROJ1104",
                    "project_title": "Civics Basics, 1e",
                    "publisher_id": "PUB022",
                },
            ),
            Action(name="FetchProjectCard", kwargs={"project_id": "PROJ1104"}),
            Action(
                name="MapHourlyRates", kwargs={"project_id_list": ["PROJ1104"]}
            ),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 6, "rate": 80.0}]},
            ),
            Action(name="QueryInvoices", kwargs={"status": "open"}),
            Action(name="DeriveCollectionKpis", kwargs={"window_months": 12}),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-11"}),
            Action(
                name="CreateDashboardSnapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-11.pdf",
                    "snapshot_date": "2024-11-30",
                },
            ),
            Action(
                name="FetchDashboardSnapshot",
                kwargs={"snapshot_date": "2024-11-30"},
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_28",
        instruction="Revise GST references and confirm July‑2024 Account Receivable. Your objective: publisher_id 'PUB002' gst_number is updated to 'GST-UPDATED-002' and visible; consultant_id 'CONS001' gst_number is '123456789RT0001' and visible; review open invoices; 12‑month KPIs are available; ensure the Account Receivable aging PDF exists for '2024-07'.",
        actions=[
            Action(
                name="MutateClientContact",
                kwargs={"gst_number": "GST-UPDATED-002", "publisher_id": "PUB002"},
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB002"}),
            Action(
                name="MutateConsultantContact",
                kwargs={"consultant_id": "CONS001", "gst_number": "123456789RT0001"},
            ),
            Action(name="FetchConsultantProfile", kwargs={"consultant_id": "CONS001"}),
            Action(name="QueryInvoices", kwargs={"status": "open"}),
            Action(name="DeriveCollectionKpis", kwargs={"window_months": 12}),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-07"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_29",
        instruction="Coordinate the reconciliation of the July‑2024 Account Receivable for publisher_id 'PUB002'. Achieve the following: publisher_id 'PUB002' remains accessible; conduct a risk check to calculate days outstanding for invoice_number '2024-023' using due_date '2024-07-15' as of '2024-07-20' and categorize it accordingly; export the Account Receivable aging for '2024-07' and store a snapshot for '2024-07-31'.",
        actions=[
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB002"}),
            Action(
                name="DeriveDaysOutstanding",
                kwargs={
                    "invoices": [
                        {"invoice_number": "2024-023", "period_end": "2024-07-15"}
                    ],
                    "today": "2024-07-20",
                },
            ),
            Action(
                name="BucketizeAging",
                kwargs={
                    "aging": [{"days_outstanding": 5, "invoice_number": "2024-023"}]
                },
            ),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-07"}),
            Action(
                name="CreateDashboardSnapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-07.pdf",
                    "snapshot_date": "2024-07-31",
                },
            ),
            Action(
                name="FetchDashboardSnapshot",
                kwargs={"snapshot_date": "2024-07-31"},
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_30",
        instruction="Handle the generation of an October‑2024 invoice for publisher_id 'PUB004'. Ensure the following end state: invoice_number '2024-120' is available for period_start '2024-10-01' and period_end '2024-10-31' with accurately calculated totals for a single line (5h @102.0 with hst_rate 0.13), and is accessible; add a line for project_id 'PROJ2024' featuring isbn '978-1-3100-2024-6' (5h @102.0) that is listable; make sure the Account Receivable aging PDF for period label '2024-10' is in place. Utilize pdf_path 'https://test.storage.com/invoices/2024/INV-2024-120.pdf'.",
        actions=[
            Action(
                name="ComputeInvoiceTotals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 5, "rate": 102.0}]},
            ),
            Action(
                name="CreateInvoiceRecord",
                kwargs={
                    "hst_amount": 66.3,
                    "invoice_date": "2024-10-31",
                    "invoice_number": "2024-120",
                    "pdf_path": "https://test.storage.com/invoices/2024/INV-2024-120.pdf",
                    "period_end": "2024-10-31",
                    "period_start": "2024-10-01",
                    "publisher_id": "PUB004",
                    "subtotal": 510.0,
                    "total_due": 576.3,
                },
            ),
            Action(name="FetchInvoiceRecord", kwargs={"invoice_number": "2024-120"}),
            Action(
                name="CreateInvoiceLines",
                kwargs={
                    "invoice_number": "2024-120",
                    "lines": [
                        {
                            "hours": 5,
                            "isbn": "978-1-3100-2024-6",
                            "project_id": "PROJ2024",
                            "rate": 102.0,
                        }
                    ],
                },
            ),
            Action(name="ListInvoiceLinesByInvoice", kwargs={"invoice_number": "2024-120"}),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-10"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_31",
        instruction="Coordinate the normalization of contact data and create a September‑2024 Account Receivable snapshot for validation. Your final outcome: publisher_id 'PUB001' contact_email matches 'accounts@nelson-edu.ca' and is visible; consultant_id 'CONS001' email matches 'sarah.thompson@consultingpro.ca' and is visible; review open invoices (status 'open') and ensure 12‑month KPIs are accessible; resolve rates for ['PROJ001'] and compute a sample total (6h @85.0 with hst_rate 0.13); ensure Account Receivable aging PDFs are available for period labels '2024-09' and '2024-08'; list projects and ensure details for 'PROJ001' are visible; verify representative open invoices '2024-009' and '2024-021' are readable, and an audit event 'reviewed' is recorded for '2024-009' and documented.",
        actions=[
            Action(
                name="MutateClientContact",
                kwargs={
                    "contact_email": "accounts@nelson-edu.ca",
                    "publisher_id": "PUB001",
                },
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB001"}),
            Action(
                name="MutateConsultantContact",
                kwargs={
                    "consultant_id": "CONS001",
                    "email": "sarah.thompson@consultingpro.ca",
                },
            ),
            Action(name="FetchConsultantProfile", kwargs={"consultant_id": "CONS001"}),
            Action(name="QueryInvoices", kwargs={"status": "open"}),
            Action(name="DeriveCollectionKpis", kwargs={"window_months": 12}),
            Action(
                name="MapHourlyRates", kwargs={"project_id_list": ["PROJ001"]}
            ),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 6, "rate": 85.0}]},
            ),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-09"}),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-08"}),
            Action(name="ListProjectsCatalog", kwargs={}),
            Action(name="FetchProjectCard", kwargs={"project_id": "PROJ001"}),
            Action(name="FetchInvoiceRecord", kwargs={"invoice_number": "2024-009"}),
            Action(
                name="LogInvoiceEvent",
                kwargs={"event_type": "reviewed", "invoice_number": "2024-009"},
            ),
            Action(name="ListInvoiceEvents", kwargs={"invoice_number": "2024-009"}),
            Action(name="FetchInvoiceRecord", kwargs={"invoice_number": "2024-021"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_32",
        instruction="Handle the addition of publisher_id 'PUB042' named 'Bright Horizons Press' and produce a November‑2024 dashboard. Your final outcome: 'PUB042' is present and readable; review open invoices and ensure 12‑month KPIs are accessible; the Account Receivable aging PDF is available for '2024-11' and a dashboard snapshot is saved for '2024-11-30', referencing that PDF, and is readable by id; verify a representative invoice '2024-021' is readable; for confirmation, resolve the rate for ['PROJ001'] and compute a sample total (2h @85.0 with hst_rate 0.13).",
        actions=[
            Action(
                name="AddClientProfile",
                kwargs={"name": "Bright Horizons Press", "publisher_id": "PUB042"},
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB042"}),
            Action(name="QueryInvoices", kwargs={"status": "open"}),
            Action(name="DeriveCollectionKpis", kwargs={"window_months": 12}),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-11"}),
            Action(
                name="CreateDashboardSnapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-11.pdf",
                    "snapshot_date": "2024-11-30",
                },
            ),
            Action(name="FetchDashboardSnapshot", kwargs={"snapshot_id": 1}),
            Action(name="FetchInvoiceRecord", kwargs={"invoice_number": "2024-021"}),
            Action(
                name="MapHourlyRates", kwargs={"project_id_list": ["PROJ001"]}
            ),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 2, "rate": 85.0}]},
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_33",
        instruction="Handle the addition of publisher_id 'PUB051' with the name 'Maple Grove Education' and register a writing project for a check in October‑2024. Your final state: 'PUB051' exists and is readable; project_id 'PROJ3073' exists with isbn '978-1-3100-3073-8', project_title 'Advanced Composition, 1e', default_hourly_rate 95.0 and is readable; rates are resolved for ['PROJ3073','PROJ001']; a sample total is calculated (2h @95.0 and 1h @85.0 with hst_rate 0.13); the Account Receivable aging PDF is available for '2024-10'.",
        actions=[
            Action(
                name="AddClientProfile",
                kwargs={"name": "Maple Grove Education", "publisher_id": "PUB051"},
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB051"}),
            Action(
                name="AddProjectCard",
                kwargs={
                    "default_hourly_rate": 95.0,
                    "isbn": "978-1-3100-3073-8",
                    "project_id": "PROJ3073",
                    "project_title": "Advanced Composition, 1e",
                    "publisher_id": "PUB051",
                },
            ),
            Action(name="FetchProjectCard", kwargs={"project_id": "PROJ3073"}),
            Action(
                name="MapHourlyRates",
                kwargs={"project_id_list": ["PROJ3073", "PROJ001"]},
            ),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={
                    "hst_rate": 0.13,
                    "lines": [{"hours": 2, "rate": 95.0}, {"hours": 1, "rate": 85.0}],
                },
            ),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-10"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_34",
        instruction="Arrange for the generation of an August‑2024 invoice for publisher_id 'PUB002' and ensure its audit is logged. Your final state: invoice_number '2024-146' exists for period_start '2024-08-01' and period_end '2024-08-31' with correct totals (2h @85.0, hst_rate 0.13) and is readable; one line for 'PROJ001' with isbn '978-1-3100-0001-0' (2h @85.0) is included and is listable; an audit event 'generated' is documented and listable. Utilize pdf_path 'https://test.storage.com/invoices/2024/INV-2024-146.pdf'.",
        actions=[
            Action(
                name="CreateInvoiceRecord",
                kwargs={
                    "hst_amount": 22.1,
                    "invoice_date": "2024-08-31",
                    "invoice_number": "2024-146",
                    "pdf_path": "https://test.storage.com/invoices/2024/INV-2024-146.pdf",
                    "period_end": "2024-08-31",
                    "period_start": "2024-08-01",
                    "publisher_id": "PUB002",
                    "subtotal": 170.0,
                    "total_due": 192.1,
                },
            ),
            Action(name="FetchInvoiceRecord", kwargs={"invoice_number": "2024-146"}),
            Action(
                name="CreateInvoiceLines",
                kwargs={
                    "invoice_number": "2024-146",
                    "lines": [
                        {
                            "hours": 2,
                            "isbn": "978-1-3100-0001-0",
                            "project_id": "PROJ001",
                            "rate": 85.0,
                        }
                    ],
                },
            ),
            Action(name="ListInvoiceLinesByInvoice", kwargs={"invoice_number": "2024-146"}),
            Action(
                name="LogInvoiceEvent",
                kwargs={"event_type": "generated", "invoice_number": "2024-146"},
            ),
            Action(name="ListInvoiceEvents", kwargs={"invoice_number": "2024-146"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_35",
        instruction="Organize the contact details for September‑2024 and record a classification labeled as upcoming‑due, taking note of the context. Aim to achieve: publisher_id 'PUB001' with contact_email 'accounts@nelson-edu.ca' is accessible; days outstanding for invoice '2024-024' on '2024-09-29' using a period_end of '2024-10-01' (‑2 days) are marked as 'upcoming_due'; an audit log 'aging_categorized' is made for '2024-024' and should be listable; assess open invoices; make sure 12‑month KPIs are provided; ensure the Account Receivable aging PDF for '2024-09' is accessible.",
        actions=[
            Action(
                name="MutateClientContact",
                kwargs={
                    "contact_email": "accounts@nelson-edu.ca",
                    "publisher_id": "PUB001",
                },
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB001"}),
            Action(
                name="DeriveDaysOutstanding",
                kwargs={
                    "invoices": [
                        {"invoice_number": "2024-024", "period_end": "2024-10-01"}
                    ],
                    "today": "2024-09-29",
                },
            ),
            Action(
                name="BucketizeAging",
                kwargs={
                    "aging": [{"days_outstanding": -2, "invoice_number": "2024-024"}]
                },
            ),
            Action(
                name="LogInvoiceEvent",
                kwargs={
                    "event_type": "aging_categorized",
                    "invoice_number": "2024-024",
                },
            ),
            Action(name="ListInvoiceEvents", kwargs={"invoice_number": "2024-024"}),
            Action(name="QueryInvoices", kwargs={"status": "open"}),
            Action(name="DeriveCollectionKpis", kwargs={"window_months": 12}),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-09"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_36",
        instruction="Compile a succinct July‑2024 invoice for publisher_id 'PUB004' and update the audit log. Target state: invoice_number '2024-134' is verified for period_start '2024-07-01' and period_end '2024-07-31' with totals (subtotal 340.0, hst_amount 44.2, total_due 384.2) and can be read; add a line for project_id 'PROJ001' with isbn '978-1-3100-0001-0' (4h @85.0) that is listable; an audit event 'generated' is noted and should be listable. Reference pdf_path 'https://test.storage.com/invoices/2024/INV-2024-134.pdf'.",
        actions=[
            Action(
                name="CreateInvoiceRecord",
                kwargs={
                    "hst_amount": 44.2,
                    "invoice_date": "2024-07-31",
                    "invoice_number": "2024-134",
                    "pdf_path": "https://test.storage.com/invoices/2024/INV-2024-134.pdf",
                    "period_end": "2024-07-31",
                    "period_start": "2024-07-01",
                    "publisher_id": "PUB004",
                    "subtotal": 340.0,
                    "total_due": 384.2,
                },
            ),
            Action(name="FetchInvoiceRecord", kwargs={"invoice_number": "2024-134"}),
            Action(
                name="CreateInvoiceLines",
                kwargs={
                    "invoice_number": "2024-134",
                    "lines": [
                        {
                            "hours": 4,
                            "isbn": "978-1-3100-0001-0",
                            "project_id": "PROJ001",
                            "rate": 85.0,
                        }
                    ],
                },
            ),
            Action(name="ListInvoiceLinesByInvoice", kwargs={"invoice_number": "2024-134"}),
            Action(
                name="LogInvoiceEvent",
                kwargs={"event_type": "generated", "invoice_number": "2024-134"},
            ),
            Action(name="ListInvoiceEvents", kwargs={"invoice_number": "2024-134"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_37",
        instruction="Handle the formalization of a November‒2024 email for invoice '2024-010' and ensure the audit is captured with context. Your final outcome: invoice_number '2024-010' is emailed using publisher_id 'PUB004' and consultant_id 'CONS001' with subject 'Invoice 2024-010 (November 2024)', body 'Please see attached invoice 2024-010.' and attachment 'https://test.storage.com/invoices/2024/INV-2024-010.pdf', and the invoice is re‑read with sent_at populated; an audit event 'emailed' is recorded and listable; open invoices are reviewed; 12‑month KPIs are available; the Account Receivable aging PDF exists for '2024-11'."
                    "Your end state: invoice_number '2024-010' is emailed using publisher_id 'PUB004' and consultant_id '"
                    "CONS001' with subject 'Invoice 2024-010 (November 2024)', body 'Please see attached invoice 2024-010.' "
                    "and attachment 'https://test.storage.com/invoices/2024/INV-2024-010.pdf', and the "
                    "invoice is re‑read with sent_at populated; an audit event 'emailed' is recorded and listable; "
                    "open invoices are reviewed; 12‑month KPIs are available; the Account Receivable aging PDF exists for '2024-11'.",
        actions=[
            Action(
                name="DispatchInvoiceEmail",
                kwargs={
                    "attachment": "https://test.storage.com/invoices/2024/INV-2024-010.pdf",
                    "body_text": "Please see attached invoice 2024-010.",
                    "consultant_id": "CONS001",
                    "invoice_number": "2024-010",
                    "publisher_id": "PUB004",
                    "subject": "Invoice 2024-010 (November 2024)",
                },
            ),
            Action(name="FetchInvoiceRecord", kwargs={"invoice_number": "2024-010"}),
            Action(
                name="LogInvoiceEvent",
                kwargs={"event_type": "emailed", "invoice_number": "2024-010"},
            ),
            Action(name="ListInvoiceEvents", kwargs={"invoice_number": "2024-010"}),
            Action(name="QueryInvoices", kwargs={"status": "open"}),
            Action(name="DeriveCollectionKpis", kwargs={"window_months": 12}),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-11"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_38",
        instruction="Coordinate the onboarding of publisher_id 'PUB043' named 'Evergreen Learning Co.' and prepare an October‑2024 baseline. Your end result: 'PUB043' exists and is readable; project_id 'PROJ3053' under 'PUB043' exists with isbn '978-1-3100-3053-1', project_title 'Media Literacy, 1e', default_hourly_rate 93.0 and is readable; rates are resolved for ['PROJ3053','PROJ001']; a sample total is computed (2h @93.0 and 1h @85.0 with hst_rate 0.13); the Account Receivable aging PDF exists for '2024-10'; a dashboard snapshot is stored for '2024-10-31' referencing that PDF and is readable by date.",
        actions=[
            Action(
                name="AddClientProfile",
                kwargs={"name": "Evergreen Learning Co.", "publisher_id": "PUB043"},
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB043"}),
            Action(
                name="AddProjectCard",
                kwargs={
                    "default_hourly_rate": 93.0,
                    "isbn": "978-1-3100-3053-1",
                    "project_id": "PROJ3053",
                    "project_title": "Media Literacy, 1e",
                    "publisher_id": "PUB043",
                },
            ),
            Action(name="FetchProjectCard", kwargs={"project_id": "PROJ3053"}),
            Action(
                name="MapHourlyRates",
                kwargs={"project_id_list": ["PROJ3053", "PROJ001"]},
            ),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={
                    "hst_rate": 0.13,
                    "lines": [{"hours": 2, "rate": 93.0}, {"hours": 1, "rate": 85.0}],
                },
            ),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-10"}),
            Action(
                name="CreateDashboardSnapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-10.pdf",
                    "snapshot_date": "2024-10-31",
                },
            ),
            Action(
                name="FetchDashboardSnapshot",
                kwargs={"snapshot_date": "2024-10-31"},
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_39",
        instruction="Handle the registration of a data-science project and finalize an October-2024 risk assessment for publisher_id 'PUB004'. Target state: project_id 'PROJ1105' is established with isbn '978-1-3100-1014-9', project title 'Data Science Labs, 1e', default hourly rate 105.0, and accessibility ensured. Calculate a sample total (4h @105.0 with hst_rate 0.13); ensure the '2024-10' Account Receivable aging is exported and a snapshot is saved for '2024-10-31'. Execute a risk evaluation to compute days outstanding for invoice_number '2024-024' using the due_date '2024-10-31' as of '2024-11-10' and classify it accordingly.",
        actions=[
            Action(
                name="AddProjectCard",
                kwargs={
                    "default_hourly_rate": 105.0,
                    "isbn": "978-1-3100-1014-9",
                    "project_id": "PROJ1105",
                    "project_title": "Data Science Labs, 1e",
                    "publisher_id": "PUB004",
                },
            ),
            Action(name="FetchProjectCard", kwargs={"project_id": "PROJ1105"}),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 4, "rate": 105.0}]},
            ),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-10"}),
            Action(
                name="CreateDashboardSnapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-10.pdf",
                    "snapshot_date": "2024-10-31",
                },
            ),
            Action(
                name="FetchDashboardSnapshot",
                kwargs={"snapshot_date": "2024-10-31"},
            ),
            Action(
                name="DeriveDaysOutstanding",
                kwargs={
                    "invoices": [
                        {"invoice_number": "2024-024", "period_end": "2024-10-31"}
                    ],
                    "today": "2024-11-10",
                },
            ),
            Action(
                name="BucketizeAging",
                kwargs={
                    "aging": [{"days_outstanding": 10, "invoice_number": "2024-024"}]
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_40",
        instruction="Coordinate the addition of a STEM project and evaluate November-2024 risk. Desired outcome: project_id 'PROJ1013' is in place under 'PUB003', equipped with isbn '978-1-3100-1013-4', project title 'Applied Physics, 1e', default hourly rate 98.0, and visibility confirmed. Review open invoices and 12-month KPIs to be accessible; compute a sample total (4h @98.0 with hst_rate 0.13). For risk, determine days outstanding for invoice '2024-010' as of '2024-11-15' (15 days) and categorize appropriately.",
        actions=[
            Action(
                name="AddProjectCard",
                kwargs={
                    "default_hourly_rate": 98.0,
                    "isbn": "978-1-3100-1013-4",
                    "project_id": "PROJ1013",
                    "project_title": "Applied Physics, 1e",
                    "publisher_id": "PUB003",
                },
            ),
            Action(name="FetchProjectCard", kwargs={"project_id": "PROJ1013"}),
            Action(name="QueryInvoices", kwargs={"status": "open"}),
            Action(name="DeriveCollectionKpis", kwargs={"window_months": 12}),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 4, "rate": 98.0}]},
            ),
            Action(
                name="DeriveDaysOutstanding",
                kwargs={
                    "invoices": [
                        {"invoice_number": "2024-010", "period_end": "2024-10-31"}
                    ],
                    "today": "2024-11-15",
                },
            ),
            Action(
                name="BucketizeAging",
                kwargs={
                    "aging": [{"days_outstanding": 15, "invoice_number": "2024-010"}]
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_41",
        instruction="Handle the creation of a January‑2025 risk classification for two invoices and affirm the September Account Receivable. Your final stage: come '2025-01-15', days outstanding are calculated for '2024-026' with period_end '2024-06-30' and '2024-013' with period_end '2024-06-15' resulting in 199 and 214 days and are categorized; open invoices for publisher_id 'PUB001' are assessed; the Account Receivable aging PDF exists for '2024-09'; an audit event 'risk_categorized' is recorded for '2024-026' and is listable.",
        actions=[
            Action(
                name="DeriveDaysOutstanding",
                kwargs={
                    "invoices": [
                        {"invoice_number": "2024-026", "period_end": "2024-06-30"},
                        {"invoice_number": "2024-013", "period_end": "2024-06-15"},
                    ],
                    "today": "2025-01-15",
                },
            ),
            Action(
                name="BucketizeAging",
                kwargs={
                    "aging": [
                        {"days_outstanding": 199, "invoice_number": "2024-026"},
                        {"days_outstanding": 214, "invoice_number": "2024-013"},
                    ]
                },
            ),
            Action(
                name="QueryInvoices",
                kwargs={"publisher_id": "PUB001", "status": "open"},
            ),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-09"}),
            Action(
                name="LogInvoiceEvent",
                kwargs={"event_type": "risk_categorized", "invoice_number": "2024-026"},
            ),
            Action(name="ListInvoiceEvents", kwargs={"invoice_number": "2024-026"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_42",
        instruction="Coordinate the alignment of rates and contacts for a September‑2024 confirmation. Your final stage: consultant_id 'CONS001' email matches 'accounts+ar@consultingpro.ca' and is visible; publisher_id 'PUB001' contact_email corresponds to 'ap@nelson-edu.ca' and is visible; rates are settled for ['PROJ001','PROJ003'] and a sample total is computed (2h @85.0 and 2h @75.0 with hst_rate 0.13); open invoices are assessed; 12‑month KPIs are available; the Account Receivable aging PDF exists for '2024-09'.",
        actions=[
            Action(
                name="MutateConsultantContact",
                kwargs={
                    "consultant_id": "CONS001",
                    "email": "accounts+ar@consultingpro.ca",
                },
            ),
            Action(name="FetchConsultantProfile", kwargs={"consultant_id": "CONS001"}),
            Action(
                name="MutateClientContact",
                kwargs={"contact_email": "ap@nelson-edu.ca", "publisher_id": "PUB001"},
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB001"}),
            Action(
                name="MapHourlyRates",
                kwargs={"project_id_list": ["PROJ001", "PROJ003"]},
            ),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={
                    "hst_rate": 0.13,
                    "lines": [{"hours": 2, "rate": 85.0}, {"hours": 2, "rate": 75.0}],
                },
            ),
            Action(name="QueryInvoices", kwargs={"status": "open"}),
            Action(name="DeriveCollectionKpis", kwargs={"window_months": 12}),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-09"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_43",
        instruction="Handle the verification of August‑2024 context regarding 'PROJ003' and ensure appropriate proofing is added. Your goal: projects are organized and 'PROJ003' information is accessible; rates for ['PROJ003'] are calculated and a sample total (5h @75.0 with hst_rate 0.13) is processed; review open invoices and ensure 12‑month KPIs are visible; export the Account Receivable aging for '2024-08' and save a dashboard snapshot for '2024-08-31' that references 'https://test.storage.com/reports/accounts_receivable_2024-08.pdf', ensuring it is accessible by id; an audit event labeled 'reviewed' is logged for invoice '2024-009' and can be listed.",
        actions=[
            Action(name="ListProjectsCatalog", kwargs={}),
            Action(name="FetchProjectCard", kwargs={"project_id": "PROJ003"}),
            Action(
                name="MapHourlyRates", kwargs={"project_id_list": ["PROJ003"]}
            ),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 5, "rate": 75.0}]},
            ),
            Action(name="QueryInvoices", kwargs={"status": "open"}),
            Action(name="DeriveCollectionKpis", kwargs={"window_months": 12}),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-08"}),
            Action(
                name="CreateDashboardSnapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-08.pdf",
                    "snapshot_date": "2024-08-31",
                },
            ),
            Action(name="FetchDashboardSnapshot", kwargs={"snapshot_id": 1}),
            Action(
                name="LogInvoiceEvent",
                kwargs={"event_type": "reviewed", "invoice_number": "2024-009"},
            ),
            Action(name="ListInvoiceEvents", kwargs={"invoice_number": "2024-009"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_44",
        instruction="Coordinate the opening of publisher_id 'PUB034' titled 'Silver Birch Academic' and complete a November‑2024 aging snapshot with contextual details. Your objective: ensure 'PUB034' is available and its contents are accessible; assess open invoices; make 12‑month KPIs visible; confirm that the Account Receivable aging PDF for '2024-11' is present and save a dashboard snapshot for '2024-11-30' that references this PDF and is accessible by id; to verify, calculate the rate for ['PROJ001'] and compute a sample total (2h @85.0, hst_rate 0.13).",
        actions=[
            Action(
                name="AddClientProfile",
                kwargs={"name": "Silver Birch Academic", "publisher_id": "PUB034"},
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB034"}),
            Action(name="QueryInvoices", kwargs={"status": "open"}),
            Action(name="DeriveCollectionKpis", kwargs={"window_months": 12}),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-11"}),
            Action(
                name="CreateDashboardSnapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-11.pdf",
                    "snapshot_date": "2024-11-30",
                },
            ),
            Action(name="FetchDashboardSnapshot", kwargs={"snapshot_id": 1}),
            Action(
                name="MapHourlyRates", kwargs={"project_id_list": ["PROJ001"]}
            ),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 2, "rate": 85.0}]},
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_45",
        instruction="Create the project_id 'PROJ1018' for 'PUB004' and calculate a November 2024 sample. Your final outcome: 'PROJ1018' should be established with isbn '978-1-3100-1018-9', project_title 'Intro Data Science, 2e', default_hourly_rate 105.0 and be visible; a sample total should be calculated (4h @105.0 with hst_rate 0.13); the Account Receivable aging PDF should exist for '2024-11'.",
        actions=[
            Action(
                name="AddProjectCard",
                kwargs={
                    "default_hourly_rate": 105.0,
                    "isbn": "978-1-3100-1018-9",
                    "project_id": "PROJ1018",
                    "project_title": "Intro Data Science, 2e",
                    "publisher_id": "PUB004",
                },
            ),
            Action(name="FetchProjectCard", kwargs={"project_id": "PROJ1018"}),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 4, "rate": 105.0}]},
            ),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-11"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_46",
        instruction="Record an October 2024 invoice for publisher_id 'PUB005' and confirm its line items. The desired result: invoice_number '2024-147' is established for period_start '2024-10-01' and period_end '2024-10-31' with accurate totals (4h @90.0, hst_rate 0.13) and is readable; insert a single line for project_id 'PROJ003' with isbn '978-1-3100-0003-7' (4h @90.0), ensuring it is listable; an audit event 'generated' should be captured and made listable. Use pdf_path 'https://test.storage.com/invoices/2024/INV-2024-147.pdf'.",
        actions=[
            Action(
                name="CreateInvoiceRecord",
                kwargs={
                    "hst_amount": 46.8,
                    "invoice_date": "2024-10-31",
                    "invoice_number": "2024-147",
                    "pdf_path": "https://test.storage.com/invoices/2024/INV-2024-147.pdf",
                    "period_end": "2024-10-31",
                    "period_start": "2024-10-01",
                    "publisher_id": "PUB005",
                    "subtotal": 360.0,
                    "total_due": 406.8,
                },
            ),
            Action(name="FetchInvoiceRecord", kwargs={"invoice_number": "2024-147"}),
            Action(
                name="CreateInvoiceLines",
                kwargs={
                    "invoice_number": "2024-147",
                    "lines": [
                        {
                            "hours": 4,
                            "isbn": "978-1-3100-0003-7",
                            "project_id": "PROJ003",
                            "rate": 90.0,
                        }
                    ],
                },
            ),
            Action(name="ListInvoiceLinesByInvoice", kwargs={"invoice_number": "2024-147"}),
            Action(
                name="LogInvoiceEvent",
                kwargs={"event_type": "generated", "invoice_number": "2024-147"},
            ),
            Action(name="ListInvoiceEvents", kwargs={"invoice_number": "2024-147"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_47",
        instruction="Handle the refresh of November‑2024 context and organize a sample invoice, preserving a dashboard snapshot. Your final goal: open invoices are evaluated; 12‑month KPIs are accessible; days overdue for invoice '2024-009' as of '2024-11-15' using period_end '2024-09-30' (46 days) are sorted; the Account Receivable aging PDF is available for '2024-11'; a dashboard snapshot is preserved for '2024-11-30' referencing that PDF and is date-accessible.",
        actions=[
            Action(name="QueryInvoices", kwargs={"status": "open"}),
            Action(name="DeriveCollectionKpis", kwargs={"window_months": 12}),
            Action(
                name="DeriveDaysOutstanding",
                kwargs={
                    "invoices": [
                        {"invoice_number": "2024-009", "period_end": "2024-09-30"}
                    ],
                    "today": "2024-11-15",
                },
            ),
            Action(
                name="BucketizeAging",
                kwargs={
                    "aging": [{"days_outstanding": 46, "invoice_number": "2024-009"}]
                },
            ),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-11"}),
            Action(
                name="CreateDashboardSnapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-11.pdf",
                    "snapshot_date": "2024-11-30",
                },
            ),
            Action(
                name="FetchDashboardSnapshot",
                kwargs={"snapshot_date": "2024-11-30"},
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_48",
        instruction="Coordinate the setup of publisher_id 'PUB053' named 'Pine Valley Learning' and verify an August‑2024 math sample. Your objective: 'PUB053' is present and accessible; project_id 'PROJ3076' exists with isbn '978-1-3100-3076-7', project_title 'Linear Algebra, 1e', default_hourly_rate 101.0 and is accessible; a sample total is calculated (2h @101.0 with hst_rate 0.13); the Account Receivable aging PDF is available for '2024-08'.",
        actions=[
            Action(
                name="AddClientProfile",
                kwargs={"name": "Pine Valley Learning", "publisher_id": "PUB053"},
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB053"}),
            Action(
                name="AddProjectCard",
                kwargs={
                    "default_hourly_rate": 101.0,
                    "isbn": "978-1-3100-3076-7",
                    "project_id": "PROJ3076",
                    "project_title": "Linear Algebra, 1e",
                    "publisher_id": "PUB053",
                },
            ),
            Action(name="FetchProjectCard", kwargs={"project_id": "PROJ3076"}),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 2, "rate": 101.0}]},
            ),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-08"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_49",
        instruction="Create a November‑2024 preparation context for publisher_id 'PUB003'. Ensure that project_id 'PROJ999' is associated with 'PUB003', having isbn '978-1-3100-0007-3', project_title 'Literature Survey, 1e', default_hourly_rate 91.0, and is visible; make sure 'PUB003' can be accessed; review any open invoices and ensure 12‑month collection KPIs are accessible; resolve rates for ['PROJ999','PROJ003'] and compute sample totals (1h @91.0 and 2h @91.0 with hst_rate 0.13); generate an Account Receivable aging PDF for the period labeled '2024-11'; display projects and ensure details for 'PROJ003' are accessible;",
        actions=[
            Action(
                name="AddProjectCard",
                kwargs={
                    "default_hourly_rate": 91.0,
                    "isbn": "978-1-3100-0007-3",
                    "project_id": "PROJ999",
                    "project_title": "Literature Survey, 1e",
                    "publisher_id": "PUB003",
                },
            ),
            Action(name="FetchProjectCard", kwargs={"project_id": "PROJ999"}),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB003"}),
            Action(name="QueryInvoices", kwargs={"status": "open"}),
            Action(name="DeriveCollectionKpis", kwargs={"window_months": 12}),
            Action(
                name="MapHourlyRates",
                kwargs={"project_id_list": ["PROJ999", "PROJ003"]},
            ),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={
                    "hst_rate": 0.13,
                    "lines": [{"hours": 1, "rate": 91.0}, {"hours": 2, "rate": 91.0}],
                },
            ),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-11"}),
            Action(name="ListProjectsCatalog", kwargs={}),
            Action(name="FetchProjectCard", kwargs={"project_id": "PROJ003"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_50",
        instruction="Access publisher_id 'PUB031' named 'Cardinal Academic' to register a November‑2024 package. Verify that 'PUB031' is set up correctly and can be accessed; ensure project_id 'PROJ2026A' is linked to 'PUB031' with isbn '978-1-3100-2026-1', project_title 'Advanced Writing, 1e', default_hourly_rate 96.0, and is accessible; resolve the rate for ['PROJ2026A'] and calculate a sample total (3h @96.0 with hst_rate 0.13); review any open invoices; ensure 12‑month KPIs are available; generate the Account Receivable aging PDF for '2024-11' and save a dashboard snapshot for '2024-11-30', with reference 'https://test.storage.com/reports/accounts_receivable_2024-11.pdf' and ensure it is accessible by id.",
        actions=[
            Action(
                name="AddClientProfile",
                kwargs={"name": "Cardinal Academic", "publisher_id": "PUB031"},
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB031"}),
            Action(
                name="AddProjectCard",
                kwargs={
                    "default_hourly_rate": 96.0,
                    "isbn": "978-1-3100-2026-1",
                    "project_id": "PROJ2026A",
                    "project_title": "Advanced Writing, 1e",
                    "publisher_id": "PUB031",
                },
            ),
            Action(name="FetchProjectCard", kwargs={"project_id": "PROJ2026A"}),
            Action(
                name="MapHourlyRates", kwargs={"project_id_list": ["PROJ2026A"]}
            ),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 3, "rate": 96.0}]},
            ),
            Action(name="QueryInvoices", kwargs={"status": "open"}),
            Action(name="DeriveCollectionKpis", kwargs={"window_months": 12}),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-11"}),
            Action(
                name="CreateDashboardSnapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-11.pdf",
                    "snapshot_date": "2024-11-30",
                },
            ),
            Action(name="FetchDashboardSnapshot", kwargs={"snapshot_id": 1}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_51",
        instruction=(
            "Handle the onboarding of 'Everest Academy' and conduct a check for October-2024. Your end goal: ensure publisher_id 'PUB024' named 'Everest Academy' is present and accessible; examine open invoices and provide 12-month KPIs; resolve rates for ['PROJ001']; calculate a sample total for 2h @85.0 via compute_invoice_totals applying HST rate 0.13; export Accounts Receivable aging for '2024-10' (PDF: 'https://test.storage.com/reports/accounts_receivable_2024-10.pdf'); ensure a dashboard snapshot for '2024-10-31' is present and accessible by snapshot_date—if it doesn't exist for that date, create and store one using the same A/R PDF; for risk assessment, calculate days outstanding for invoice_number '2024-021' as of '2024-10-10' with due_date '2024-09-15' and classify it into aging categories."
        ),
    actions=[
            Action(
                name="AddClientProfile",
                kwargs={"name": "Everest Academy", "publisher_id": "PUB024"},
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB024"}),
            Action(name="QueryInvoices", kwargs={"status": "open"}),
            Action(name="DeriveCollectionKpis", kwargs={"window_months": 12}),
            Action(
                name="MapHourlyRates", kwargs={"project_id_list": ["PROJ001"]}
            ),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 2, "rate": 85.0}]},
            ),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-10"}),
            Action(
                name="CreateDashboardSnapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-10.pdf",
                    "snapshot_date": "2024-10-31",
                },
            ),
            Action(
                name="FetchDashboardSnapshot",
                kwargs={"snapshot_date": "2024-10-31"},
            ),
            Action(
                name="DeriveDaysOutstanding",
                kwargs={
                    "invoices": [
                        {
                            "due_date": "2024-09-15",
                            "invoice_date": "2024-09-15",
                            "invoice_number": "2024-021",
                        }
                    ],
                    "today": "2024-10-10",
                },
            ),
            Action(
                name="BucketizeAging",
                kwargs={
                    "aging": [{"days_outstanding": 25, "invoice_number": "2024-021"}]
                },
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_52",
        instruction="Coordinate the formalization of an invoice for August-2024 for publisher_id 'PUB005' related to an algebra project. Your final objective: ensure project_id 'PROJ2056' is established with isbn '978-1-3100-2056-5', project_title 'Algebra Toolkit, 1e', default_hourly_rate 92.0 and is accessible; guarantee invoice_number '2024-135' exists for period_start '2024-08-01' and period_end '2024-08-31' with accurate totals (3h @92.0, hst_rate 0.13) and is accessible; confirm an audit event 'generated' is documented and can be listed. Utilize pdf_path 'https://test.storage.com/invoices/2024/INV-2024-135.pdf'.",
        actions=[
            Action(
                name="AddProjectCard",
                kwargs={
                    "default_hourly_rate": 92.0,
                    "isbn": "978-1-3100-2056-5",
                    "project_id": "PROJ2056",
                    "project_title": "Algebra Toolkit, 1e",
                    "publisher_id": "PUB005",
                },
            ),
            Action(name="FetchProjectCard", kwargs={"project_id": "PROJ2056"}),
            Action(
                name="CreateInvoiceRecord",
                kwargs={
                    "hst_amount": 35.88,
                    "invoice_date": "2024-08-31",
                    "invoice_number": "2024-135",
                    "pdf_path": "https://test.storage.com/invoices/2024/INV-2024-135.pdf",
                    "period_end": "2024-08-31",
                    "period_start": "2024-08-01",
                    "publisher_id": "PUB005",
                    "subtotal": 276.0,
                    "total_due": 311.88,
                },
            ),
            Action(name="FetchInvoiceRecord", kwargs={"invoice_number": "2024-135"}),
            Action(
                name="LogInvoiceEvent",
                kwargs={"event_type": "generated", "invoice_number": "2024-135"},
            ),
            Action(name="ListInvoiceEvents", kwargs={"invoice_number": "2024-135"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_53",
        instruction="Handle a July‑2024 billing summary and update primary contacts. Extract time entries for ['PROJ001','PROJ003'] covering 2024-07-01 to 2024-07-31, determine rates for these projects, and compute a sample two‑line totals utilizing the determined rates (12h @85.0 and 8h @75.0, HST 0.13). Modify CONS001 email to sarah.thompson+billing@consultingpro.ca and verify it. Change PUB002 AP email to ap@northernlights-edu.ca and verify it. Generate the Account Receivable aging report for period label 2024-07.",
        actions=[
            Action(
                name="ReadTimeEntries",
                kwargs={
                    "period_end": "2024-07-31",
                    "period_start": "2024-07-01",
                    "project_id_list": ["PROJ001", "PROJ003"],
                },
            ),
            Action(
                name="MapHourlyRates",
                kwargs={"project_id_list": ["PROJ001", "PROJ003"]},
            ),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={
                    "hst_rate": 0.13,
                    "lines": [{"hours": 12, "rate": 85.0}, {"hours": 8, "rate": 75.0}],
                },
            ),
            Action(
                name="MutateConsultantContact",
                kwargs={
                    "consultant_id": "CONS001",
                    "email": "sarah.thompson+billing@consultingpro.ca",
                },
            ),
            Action(name="FetchConsultantProfile", kwargs={"consultant_id": "CONS001"}),
            Action(
                name="MutateClientContact",
                kwargs={
                    "contact_email": "ap@northernlights-edu.ca",
                    "publisher_id": "PUB002",
                },
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB002"}),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-07"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_54",
        instruction="Coordinate the creation of a precise August‑2024 invoice for publisher_id 'PUB002' and document its development. Your desired outcome: invoice_number '2024-133' exists for period_start '2024-08-01' and period_end '2024-08-31' with totals (subtotal 300.0, hst_amount 39.0, total_due 339.0) and is accessible; a single entry is added for 'PROJ003' with isbn '978-1-3100-0003-7' (4h @75.0) and is presentable; an audit event 'generated' is logged and viewable. Utilize pdf_path 'https://test.storage.com/invoices/2024/INV-2024-133.pdf'.",
        actions=[
            Action(
                name="CreateInvoiceRecord",
                kwargs={
                    "hst_amount": 39.0,
                    "invoice_date": "2024-08-31",
                    "invoice_number": "2024-133",
                    "pdf_path": "https://test.storage.com/invoices/2024/INV-2024-133.pdf",
                    "period_end": "2024-08-31",
                    "period_start": "2024-08-01",
                    "publisher_id": "PUB002",
                    "subtotal": 300.0,
                    "total_due": 339.0,
                },
            ),
            Action(name="FetchInvoiceRecord", kwargs={"invoice_number": "2024-133"}),
            Action(
                name="CreateInvoiceLines",
                kwargs={
                    "invoice_number": "2024-133",
                    "lines": [
                        {
                            "hours": 4,
                            "isbn": "978-1-3100-0003-7",
                            "project_id": "PROJ003",
                            "rate": 75.0,
                        }
                    ],
                },
            ),
            Action(name="ListInvoiceLinesByInvoice", kwargs={"invoice_number": "2024-133"}),
            Action(
                name="LogInvoiceEvent",
                kwargs={"event_type": "generated", "invoice_number": "2024-133"},
            ),
            Action(name="ListInvoiceEvents", kwargs={"invoice_number": "2024-133"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_55",
        instruction="Handle the update of contact information and verify the totals for August‑2024. Ensure that: the phone for 'CONS001' is '+1-647-555-2244' and displayed; 'PUB004' is accessible; rates are calculated for ['PROJ001'] and a sample total is determined (4h @85.0 with hst_rate 0.13); the Account Receivable aging PDF exists for '2024-08'.",
        actions=[
            Action(
                name="MutateConsultantContact",
                kwargs={"consultant_id": "CONS001", "phone": "+1-647-555-2244"},
            ),
            Action(name="FetchConsultantProfile", kwargs={"consultant_id": "CONS001"}),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB004"}),
            Action(
                name="MapHourlyRates", kwargs={"project_id_list": ["PROJ001"]}
            ),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 4, "rate": 85.0}]},
            ),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-08"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_56",
        instruction="Coordinate the establishment of publisher_id 'PUB033' with the name 'Prairie Learning Co.' and prepare a September‑2024 snapshot. Ensure that: 'PUB033' is present and accessible; project_id 'PROJ2034' is available with isbn '978-1-3100-2034-6', project_title 'Prairie Math, 1e', and default_hourly_rate 89.0, and accessible; compute a sample total (3h @89.0, hst_rate 0.13); review the open invoices; the Account Receivable aging PDF for '2024-09' exists and a dashboard snapshot is saved for '2024-09-30' pointing to 'https://test.storage.com/reports/accounts_receivable_2024-09.pdf' which is accessible by id.",
        actions=[
            Action(
                name="AddClientProfile",
                kwargs={"name": "Prairie Learning Co.", "publisher_id": "PUB033"},
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB033"}),
            Action(
                name="AddProjectCard",
                kwargs={
                    "default_hourly_rate": 89.0,
                    "isbn": "978-1-3100-2034-6",
                    "project_id": "PROJ2034",
                    "project_title": "Prairie Math, 1e",
                    "publisher_id": "PUB033",
                },
            ),
            Action(name="FetchProjectCard", kwargs={"project_id": "PROJ2034"}),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 3, "rate": 89.0}]},
            ),
            Action(name="QueryInvoices", kwargs={"status": "open"}),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-09"}),
            Action(
                name="CreateDashboardSnapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-09.pdf",
                    "snapshot_date": "2024-09-30",
                },
            ),
            Action(name="FetchDashboardSnapshot", kwargs={"snapshot_id": 1}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_57",
        instruction="Handle the creation of a September 2024 invoice for publisher_id 'PUB002' consisting of one line, and ensure its audit is recorded. Ensure the final outcome: invoice_number '2024-144' is present for period_start '2024-09-01' and period_end '2024-09-30' with accurate totals (3h @75.0, hst_rate 0.13) and is accessible; include a single line for 'PROJ003' with isbn '978-1-3100-0003-7' (3h @75.0) and verify its listability; document and make listable an audit event 'generated'. Employ pdf_path 'https://test.storage.com/invoices/2024/INV-2024-144.pdf'.",
        actions=[
            Action(
                name="CreateInvoiceRecord",
                kwargs={
                    "hst_amount": 29.25,
                    "invoice_date": "2024-09-30",
                    "invoice_number": "2024-144",
                    "pdf_path": "https://test.storage.com/invoices/2024/INV-2024-144.pdf",
                    "period_end": "2024-09-30",
                    "period_start": "2024-09-01",
                    "publisher_id": "PUB002",
                    "subtotal": 225.0,
                    "total_due": 254.25,
                },
            ),
            Action(name="FetchInvoiceRecord", kwargs={"invoice_number": "2024-144"}),
            Action(
                name="CreateInvoiceLines",
                kwargs={
                    "invoice_number": "2024-144",
                    "lines": [
                        {
                            "hours": 3,
                            "isbn": "978-1-3100-0003-7",
                            "project_id": "PROJ003",
                            "rate": 75.0,
                        }
                    ],
                },
            ),
            Action(name="ListInvoiceLinesByInvoice", kwargs={"invoice_number": "2024-144"}),
            Action(
                name="LogInvoiceEvent",
                kwargs={"event_type": "generated", "invoice_number": "2024-144"},
            ),
            Action(name="ListInvoiceEvents", kwargs={"invoice_number": "2024-144"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_58",
        instruction="Coordinate the addition of project_id 'PROJ3054' for publisher_id 'PUB005' and verify a November 2024 sample alongside an explicit aging check. Your target state: 'PROJ3054' is created and includes isbn '978-1-3100-3054-8', project_title 'Canadian Literature, 2e', default_hourly_rate 90.0 and is viewable; rates are correctly established for ['PROJ3054']; a sample total is formulated (3h @90.0 with hst_rate 0.13); classify days outstanding for '2024-010' as of '2024-11-15' utilizing period_end '2024-10-31' (15 days); confirm the presence of the Account Receivable aging PDF for '2024-11'.",
        actions=[
            Action(
                name="AddProjectCard",
                kwargs={
                    "default_hourly_rate": 90.0,
                    "isbn": "978-1-3100-3054-8",
                    "project_id": "PROJ3054",
                    "project_title": "Canadian Literature, 2e",
                    "publisher_id": "PUB005",
                },
            ),
            Action(name="FetchProjectCard", kwargs={"project_id": "PROJ3054"}),
            Action(
                name="MapHourlyRates", kwargs={"project_id_list": ["PROJ3054"]}
            ),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 3, "rate": 90.0}]},
            ),
            Action(
                name="DeriveDaysOutstanding",
                kwargs={
                    "invoices": [
                        {"invoice_number": "2024-010", "period_end": "2024-10-31"}
                    ],
                    "today": "2024-11-15",
                },
            ),
            Action(
                name="BucketizeAging",
                kwargs={
                    "aging": [{"days_outstanding": 15, "invoice_number": "2024-010"}]
                },
            ),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-11"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_59",
        instruction="Handle the normalization of contacts and formulate a July‑2024 risk assessment. The final condition: publisher_id 'PUB002' with contact_email 'ap@northernlights-edu.ca' must be visible; consultant_id 'CONS001' with gst_number '123456789RT0001' must be accessible; review open invoices and ensure 12‑month KPIs are obtainable; confirm the existence of the Account Receivable aging PDF for '2024-07'; compute days outstanding for '2024-023' by '2024-08-01' (17 days) and classify them; list projects and ensure 'PROJ003' details are visible.",
        actions=[
            Action(
                name="MutateClientContact",
                kwargs={
                    "contact_email": "ap@northernlights-edu.ca",
                    "publisher_id": "PUB002",
                },
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB002"}),
            Action(
                name="MutateConsultantContact",
                kwargs={"consultant_id": "CONS001", "gst_number": "123456789RT0001"},
            ),
            Action(name="FetchConsultantProfile", kwargs={"consultant_id": "CONS001"}),
            Action(name="QueryInvoices", kwargs={"status": "open"}),
            Action(name="DeriveCollectionKpis", kwargs={"window_months": 12}),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-07"}),
            Action(
                name="DeriveDaysOutstanding",
                kwargs={
                    "invoices": [
                        {"invoice_number": "2024-023", "period_end": "2024-07-15"}
                    ],
                    "today": "2024-08-01",
                },
            ),
            Action(
                name="BucketizeAging",
                kwargs={
                    "aging": [{"days_outstanding": 17, "invoice_number": "2024-023"}]
                },
            ),
            Action(name="ListProjectsCatalog", kwargs={}),
            Action(name="FetchProjectCard", kwargs={"project_id": "PROJ003"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_60",
        instruction="Coordinate the addition of publisher_id 'PUB054' with the name 'Aspen Trail Press' and prepare for a September‑2024 readiness check. The end condition: 'PUB054' is established and readable; ensure project_id 'PROJ3078' is present with isbn '978-1-3100-3078-1', project_title 'World History, 1e', default_hourly_rate 92.0 and is accessible; resolve rates for ['PROJ3078']; calculate a sample total (3h @92.0 with hst_rate 0.13); verify the Account Receivable aging PDF is present for '2024-09'.",
        actions=[
            Action(
                name="AddClientProfile",
                kwargs={"name": "Aspen Trail Press", "publisher_id": "PUB054"},
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB054"}),
            Action(
                name="AddProjectCard",
                kwargs={
                    "default_hourly_rate": 92.0,
                    "isbn": "978-1-3100-3078-1",
                    "project_id": "PROJ3078",
                    "project_title": "World History, 1e",
                    "publisher_id": "PUB054",
                },
            ),
            Action(name="FetchProjectCard", kwargs={"project_id": "PROJ3078"}),
            Action(
                name="MapHourlyRates", kwargs={"project_id_list": ["PROJ3078"]}
            ),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 3, "rate": 92.0}]},
            ),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-09"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_61",
        instruction="Handle the refreshing of AP contacts and confirm October‑2024 Account Receivable for two publishers. Your final condition should be: 'PUB004' contact_email is 'ap@bluepeakpublishing.ca' and is visible; 'PUB005' contact_email is 'ap@westwoodpress.ca' and is visible; open invoices are verified; 12‑month KPIs are accessible; projects are displayed and 'PROJ004' details are visible; the Account Receivable aging PDF is present for '2024-10'.",
        actions=[
            Action(
                name="MutateClientContact",
                kwargs={
                    "contact_email": "ap@bluepeakpublishing.ca",
                    "publisher_id": "PUB004",
                },
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB004"}),
            Action(
                name="MutateClientContact",
                kwargs={
                    "contact_email": "ap@westwoodpress.ca",
                    "publisher_id": "PUB005",
                },
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB005"}),
            Action(name="QueryInvoices", kwargs={"status": "open"}),
            Action(name="DeriveCollectionKpis", kwargs={"window_months": 12}),
            Action(name="ListProjectsCatalog", kwargs={}),
            Action(name="FetchProjectCard", kwargs={"project_id": "PROJ004"}),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-10"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_62",
        instruction="Coordinate the introduction of publisher_id 'PUB013' named 'Maple STEM Press' and align with a September‑2024 billing check. Your final outcome should be: 'PUB013' exists with the name 'Maple STEM Press' and is readable; publisher_id 'PUB002' is readable; open invoices with status 'open' are verified and 12‑month KPIs are calculated; resolve rates for ['PROJ003'] and compute sample totals (6h @75.0 and 2h @75.0 with hst_rate 0.13); export the Account Receivable aging for '2024-09'. Every write should be confirmed through a subsequent read.",
        actions=[
            Action(
                name="AddClientProfile",
                kwargs={"name": "Maple STEM Press", "publisher_id": "PUB013"},
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB013"}),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB002"}),
            Action(name="QueryInvoices", kwargs={"status": "open"}),
            Action(name="DeriveCollectionKpis", kwargs={"window_months": 12}),
            Action(
                name="MapHourlyRates", kwargs={"project_id_list": ["PROJ003"]}
            ),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={
                    "hst_rate": 0.13,
                    "lines": [{"hours": 6, "rate": 75.0}, {"hours": 2, "rate": 75.0}],
                },
            ),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-09"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_63",
        instruction="Arrange November‑2024 contact data and calculate a confirmation total with context. Your goal: publisher_id 'PUB005' contact_email should be updated to 'ap@westwoodpress.ca' and remain readable; consultant_id 'CONS001' email is updated to 'sarah.thompson@consultingpro.ca' and remains readable; review open invoices (status 'open') and compute 12‑month KPIs; resolve rates for ['PROJ003'] and calculate a sample total (2h @75.0 with hst_rate 0.13); export Account Receivable aging '2024-11'. Each write must be verified through a subsequent read.",
        actions=[
            Action(
                name="MutateClientContact",
                kwargs={
                    "contact_email": "ap@westwoodpress.ca",
                    "publisher_id": "PUB005",
                },
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB005"}),
            Action(
                name="MutateConsultantContact",
                kwargs={
                    "consultant_id": "CONS001",
                    "email": "sarah.thompson@consultingpro.ca",
                },
            ),
            Action(name="FetchConsultantProfile", kwargs={"consultant_id": "CONS001"}),
            Action(name="QueryInvoices", kwargs={"status": "open"}),
            Action(name="DeriveCollectionKpis", kwargs={"window_months": 12}),
            Action(
                name="MapHourlyRates", kwargs={"project_id_list": ["PROJ003"]}
            ),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 2, "rate": 75.0}]},
            ),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-11"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_64",
        instruction="Formalize a September‑2024 invoice for publisher_id 'PUB004' with one project and verify context. Your goal: invoice_number '2024-148' should exist for period_start '2024-09-01' and period_end '2024-09-30' with correct totals (2h @85.0, hst_rate 0.13) and be readable; a single line is inserted for 'PROJ001' (2h @85.0, isbn '978-1-3100-0001-0') and be listable; an audit event 'generated' should be recorded and listable. Use pdf_path 'https://test.storage.com/invoices/2024/INV-2024-148.pdf'.",
        actions=[
            Action(
                name="CreateInvoiceRecord",
                kwargs={
                    "hst_amount": 22.1,
                    "invoice_date": "2024-09-30",
                    "invoice_number": "2024-148",
                    "pdf_path": "https://test.storage.com/invoices/2024/INV-2024-148.pdf",
                    "period_end": "2024-09-30",
                    "period_start": "2024-09-01",
                    "publisher_id": "PUB004",
                    "subtotal": 170.0,
                    "total_due": 192.1,
                },
            ),
            Action(name="FetchInvoiceRecord", kwargs={"invoice_number": "2024-148"}),
            Action(
                name="CreateInvoiceLines",
                kwargs={
                    "invoice_number": "2024-148",
                    "lines": [
                        {
                            "hours": 2,
                            "isbn": "978-1-3100-0001-0",
                            "project_id": "PROJ001",
                            "rate": 85.0,
                        }
                    ],
                },
            ),
            Action(name="ListInvoiceLinesByInvoice", kwargs={"invoice_number": "2024-148"}),
            Action(
                name="LogInvoiceEvent",
                kwargs={"event_type": "generated", "invoice_number": "2024-148"},
            ),
            Action(name="ListInvoiceEvents", kwargs={"invoice_number": "2024-148"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_65",
        instruction=(
            "Handle the onboarding of a new client and synchronize with an October-2024 snapshot. The final objective: publisher_id 'PUB021' labeled as 'Algonquin Scholastic' is in existence and accessible; project_id 'PROJ1102' is present under 'PUB021' possessing isbn '978-1-3100-1010-1', project_title 'Intro Statistics, 1e', default_hourly_rate 95.0, and remains accessible; finalize rates for ['PROJ1102','PROJ001']; calculate sample totals by measuring 3h @95.0 and 2h @85.0 utilizing HST rate 0.13 (hst_rate=0.13); Export Accounts Receivable aging for '2024-10' and ensure a snapshot is stored for '2024-10-31' using the identical PDF."
        ),
        actions=[
            Action(
                name="AddClientProfile",
                kwargs={"name": "Algonquin Scholastic", "publisher_id": "PUB021"},
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB021"}),
            Action(
                name="AddProjectCard",
                kwargs={
                    "default_hourly_rate": 95.0,
                    "isbn": "978-1-3100-1010-1",
                    "project_id": "PROJ1102",
                    "project_title": "Intro Statistics, 1e",
                    "publisher_id": "PUB021",
                },
            ),
            Action(name="FetchProjectCard", kwargs={"project_id": "PROJ1102"}),
            Action(
                name="MapHourlyRates",
                kwargs={"project_id_list": ["PROJ1102", "PROJ001"]},
            ),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={
                    "hst_rate": 0.13,
                    "lines": [{"hours": 3, "rate": 95.0}, {"hours": 2, "rate": 85.0}],
                },
            ),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-10"}),
            Action(
                name="CreateDashboardSnapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-10.pdf",
                    "snapshot_date": "2024-10-31",
                },
            ),
            Action(
                name="FetchDashboardSnapshot",
                kwargs={"snapshot_date": "2024-10-31"},
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_66",
        instruction="Facilitate the update of contacts and verify a total for September—2024. Achieve the following: contact_email for 'PUB003' should be 'accounts@canopypress.ca' and be visible; 'CONS001' should have phone number '+1-416-555-0199' and be visible; ascertain rates for ['PROJ001','PROJ003'] and compute sample totals (3h @85.0 and 2h @75.0 using hst_rate 0.13); ensure the Account Receivable aging PDF is available for '2024-09'.",
        actions=[
            Action(
                name="MutateClientContact",
                kwargs={
                    "contact_email": "accounts@canopypress.ca",
                    "publisher_id": "PUB003",
                },
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB003"}),
            Action(
                name="MutateConsultantContact",
                kwargs={"consultant_id": "CONS001", "phone": "+1-416-555-0199"},
            ),
            Action(name="FetchConsultantProfile", kwargs={"consultant_id": "CONS001"}),
            Action(
                name="MapHourlyRates",
                kwargs={"project_id_list": ["PROJ001", "PROJ003"]},
            ),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={
                    "hst_rate": 0.13,
                    "lines": [{"hours": 3, "rate": 85.0}, {"hours": 2, "rate": 75.0}],
                },
            ),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-09"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_67",
        instruction="Begin by adding publisher_id 'PUB050' known as 'Riverbend Academic' and save an August–2024 dashboard with a small sample. Your end state should be that 'PUB050' exists and is accessible; open invoices are analyzed; 12-month KPIs are provided; rates are settled for ['PROJ001']; a sample total is calculated (1h @85.0 with hst_rate 0.13); the Account Receivable aging PDF is present for '2024-08'; a dashboard snapshot is saved for '2024-08-31' and can be accessed by date.",
        actions=[
            Action(
                name="AddClientProfile",
                kwargs={"name": "Riverbend Academic", "publisher_id": "PUB050"},
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB050"}),
            Action(name="QueryInvoices", kwargs={"status": "open"}),
            Action(name="DeriveCollectionKpis", kwargs={"window_months": 12}),
            Action(
                name="MapHourlyRates", kwargs={"project_id_list": ["PROJ001"]}
            ),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 1, "rate": 85.0}]},
            ),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-08"}),
            Action(
                name="CreateDashboardSnapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-08.pdf",
                    "snapshot_date": "2024-08-31",
                },
            ),
            Action(
                name="FetchDashboardSnapshot",
                kwargs={"snapshot_date": "2024-08-31"},
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_68",
        instruction="Confirm November–2024 visibility and an illustrative invoice. Your final condition should showcase that projects are listed and 'PROJ001' details are accessible; open invoices are examined and 12-month KPIs are shown; the Account Receivable aging PDF is available for '2024-11'; to verify, the rate resolves for ['PROJ001'] and a sample total is calculated (1h @85.0 with hst_rate 0.13); invoice '2024-025' can be accessed; an audit event 'reviewed' is logged for '2024-025' and is listable.",
        actions=[
            Action(name="ListProjectsCatalog", kwargs={}),
            Action(name="FetchProjectCard", kwargs={"project_id": "PROJ001"}),
            Action(name="QueryInvoices", kwargs={"status": "open"}),
            Action(name="DeriveCollectionKpis", kwargs={"window_months": 12}),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-11"}),
            Action(
                name="MapHourlyRates", kwargs={"project_id_list": ["PROJ001"]}
            ),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 1, "rate": 85.0}]},
            ),
            Action(name="FetchInvoiceRecord", kwargs={"invoice_number": "2024-025"}),
            Action(
                name="LogInvoiceEvent",
                kwargs={"event_type": "reviewed", "invoice_number": "2024-025"},
            ),
            Action(name="ListInvoiceEvents", kwargs={"invoice_number": "2024-025"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_69",
        instruction=(
            "Handle the creation of a social studies project and align it with a July-2024 snapshot. Your final outcome: project_id 'PROJ1109' is established for 'PUB005' with isbn '978-1-3100-1018-7', project_title 'Social Studies, 1e', default_hourly_rate 90.0, and is accessible; compute sample totals for two time entries (2h @90.0 and 2h @90.0) using HST rate 0.13; export the Accounts Receivable aging for '2024-07', making it available at 'https://test.storage.com/reports/accounts_receivable_2024-07.pdf'; ensure a dashboard snapshot dated '2024-07-31' exists, is accessible by snapshot_date, and links to the same A/R PDF."
        ),
    actions=[
            Action(
                name="AddProjectCard",
                kwargs={
                    "default_hourly_rate": 90.0,
                    "isbn": "978-1-3100-1018-7",
                    "project_id": "PROJ1109",
                    "project_title": "Social Studies, 1e",
                    "publisher_id": "PUB005",
                },
            ),
            Action(name="FetchProjectCard", kwargs={"project_id": "PROJ1109"}),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={
                    "hst_rate": 0.13,
                    "lines": [{"hours": 2, "rate": 90.0}, {"hours": 2, "rate": 90.0}],
                },
            ),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-07"}),
            Action(
                name="CreateDashboardSnapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-07.pdf",
                    "snapshot_date": "2024-07-31",
                },
            ),
            Action(
                name="FetchDashboardSnapshot",
                kwargs={"snapshot_date": "2024-07-31"},
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_70",
        instruction="Coordinate the establishment of publisher_id 'PUB027' named 'North Coast Education' and complete an August snapshot. Your final outcome: 'PUB027' is established and visible; the Account Receivable aging PDF is present for '2024-08' and a snapshot is stored for '2024-08-31', linking to that PDF; calculate a sample total (5h @85.0 with hst_rate 0.13) using rates for ['PROJ001'].",
        actions=[
            Action(
                name="AddClientProfile",
                kwargs={"name": "North Coast Education", "publisher_id": "PUB027"},
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB027"}),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-08"}),
            Action(
                name="CreateDashboardSnapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-08.pdf",
                    "snapshot_date": "2024-08-31",
                },
            ),
            Action(
                name="FetchDashboardSnapshot",
                kwargs={"snapshot_date": "2024-08-31"},
            ),
            Action(
                name="MapHourlyRates", kwargs={"project_id_list": ["PROJ001"]}
            ),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 5, "rate": 85.0}]},
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_71",
        instruction="Handle the establishment of base records and contacts, then generate a context snapshot for August‑2024. Your objective: publisher_id 'PUB010' is created with exact details including name 'Maple Leaf Educational', address '100 Bloor St W, Montreal, ON', contact_email 'ap@mapleleafedu.ca', gst_number 'GST-999-010' and is confirmable; publisher_id 'PUB002' contact_email is modified to 'ap@northernlights-edu.ca' and is confirmable; consultant_id 'CONS001' phone is corrected to '+1-416-555-0199' and is confirmable; August‑2024 time entries for ['PROJ001'] are retrieved spanning '2024-08-01' to '2024-08-31'; hourly rate determination for ['PROJ001'] is completed; a computation of a single-line sample total is handled (10 hours at 85.0 with hst_rate 0.13); and the Account Receivable aging for '2024-08' is exported. Each writing operation is substantiated through a subsequent reading, utilizing only accessible tools.",
        actions=[
            Action(
                name="AddClientProfile",
                kwargs={
                    "address": "100 Bloor St W, Montreal, ON",
                    "contact_email": "ap@mapleleafedu.ca",
                    "gst_number": "GST-999-010",
                    "name": "Maple Leaf Educational",
                    "publisher_id": "PUB010",
                },
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB010"}),
            Action(
                name="MutateClientContact",
                kwargs={
                    "contact_email": "ap@northernlights-edu.ca",
                    "publisher_id": "PUB002",
                },
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB002"}),
            Action(
                name="MutateConsultantContact",
                kwargs={"consultant_id": "CONS001", "phone": "+1-416-555-0199"},
            ),
            Action(name="FetchConsultantProfile", kwargs={"consultant_id": "CONS001"}),
            Action(
                name="ReadTimeEntries",
                kwargs={
                    "period_end": "2024-08-31",
                    "period_start": "2024-08-01",
                    "project_id_list": ["PROJ001"],
                },
            ),
            Action(
                name="MapHourlyRates", kwargs={"project_id_list": ["PROJ001"]}
            ),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 10, "rate": 85.0}]},
            ),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-08"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_72",
        instruction="Coordinate the preparation of a November‑2024 email for invoice '2024-010' and document the audit with context. Your final stage: invoice_number '2024-010' is dispatched using publisher_id 'PUB004' and consultant_id 'CONS001' with subject line 'Invoice 2024-010 (November 2024)', email body 'Please see attached invoice 2024-010.' and attachment at 'https://test.storage.com/invoices/2024/INV-2024-010.pdf', and it is re-checked with sent_at populated; an 'emailed' audit event is logged and accessible; open invoices are assessed; 12-month KPIs are provided; the Account Receivable aging PDF for '2024-11' is in existence."
                    "Your end state: invoice_number '2024-010' is emailed using publisher_id 'PUB004' and consultant_id '"
                    "CONS001' with subject 'Invoice 2024-010 (November 2024)', body 'Please see attached invoice 2024-010.' "
                    "and attachment 'https://test.storage.com/invoices/2024/INV-2024-010.pdf', and the "
                    "invoice is re‑read with sent_at populated; an audit event 'emailed' is recorded and listable; "
                    "open invoices are reviewed; 12‑month KPIs are available; the Account Receivable aging PDF exists for '2024-11'.",
        actions=[
            Action(
                name="DispatchInvoiceEmail",
                kwargs={
                    "attachment": "https://test.storage.com/invoices/2024/INV-2024-010.pdf",
                    "body_text": "Please see attached invoice 2024-010.",
                    "consultant_id": "CONS001",
                    "invoice_number": "2024-010",
                    "publisher_id": "PUB004",
                    "subject": "Invoice 2024-010 (November 2024)",
                },
            ),
            Action(name="FetchInvoiceRecord", kwargs={"invoice_number": "2024-010"}),
            Action(
                name="LogInvoiceEvent",
                kwargs={"event_type": "emailed", "invoice_number": "2024-010"},
            ),
            Action(name="ListInvoiceEvents", kwargs={"invoice_number": "2024-010"}),
            Action(name="QueryInvoices", kwargs={"status": "open"}),
            Action(name="DeriveCollectionKpis", kwargs={"window_months": 12}),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-11"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_73",
        instruction="Handle the addition of publisher_id 'PUB047' with the name 'Horizon Peak Education' and record an August‑2024 snapshot including sample math totals. Desired outcome: 'PUB047' is present and accessible; project_id 'PROJ3064' is available with isbn '978-1-3100-3064-0', project_title 'Discrete Math, 1e', default_hourly_rate 104.0 and is accessible; a sample total is calculated (1h @104.0 with hst_rate 0.13); the Accounts Receivable aging PDF for '2024-08' is available and a dashboard snapshot for '2024-08-31' is stored, referencing that PDF and accessible by date.",
        actions=[
            Action(
                name="AddClientProfile",
                kwargs={"name": "Horizon Peak Education", "publisher_id": "PUB047"},
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB047"}),
            Action(
                name="AddProjectCard",
                kwargs={
                    "default_hourly_rate": 104.0,
                    "isbn": "978-1-3100-3064-0",
                    "project_id": "PROJ3064",
                    "project_title": "Discrete Math, 1e",
                    "publisher_id": "PUB047",
                },
            ),
            Action(name="FetchProjectCard", kwargs={"project_id": "PROJ3064"}),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 1, "rate": 104.0}]},
            ),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-08"}),
            Action(
                name="CreateDashboardSnapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-08.pdf",
                    "snapshot_date": "2024-08-31",
                },
            ),
            Action(
                name="FetchDashboardSnapshot",
                kwargs={"snapshot_date": "2024-08-31"},
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_74",
        instruction=(
            "Ensure October-2024 time tracking is accurate for a preliminary billing estimate. Outcome: time entries for ['PROJ001','PROJ003'] from '2024-10-01' to '2024-10-31' are retrieved and verified; hours are categorized by ISBN; rates are confirmed for ['PROJ001','PROJ003']; a sample total for 5h @85.0 and 3h @75.0 is computed using HST rate 0.13; Accounts Receivable aging for '2024-10' is exported and can be accessed at 'https://test.storage.com/reports/accounts_receivable_2024-10.pdf'; a dashboard snapshot dated '2024-10-31' exists, is accessible by snapshot_date, and references the identical A/R PDF; an audit event 'reviewed' for invoice_number '2024-010' is logged and visible."
        ),
    actions=[
            Action(
                name="ReadTimeEntries",
                kwargs={
                    "period_end": "2024-10-31",
                    "period_start": "2024-10-01",
                    "project_id_list": ["PROJ001", "PROJ003"],
                },
            ),
            Action(name="AuditTimeEntries", kwargs={"rows": []}),
            Action(name="AggregateHoursByIsbn", kwargs={"rows": []}),
            Action(
                name="MapHourlyRates",
                kwargs={"project_id_list": ["PROJ001", "PROJ003"]},
            ),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={
                    "hst_rate": 0.13,
                    "lines": [{"hours": 5, "rate": 85.0}, {"hours": 3, "rate": 75.0}],
                },
            ),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-10"}),
            Action(
                name="CreateDashboardSnapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-10.pdf",
                    "snapshot_date": "2024-10-31",
                },
            ),
            Action(
                name="FetchDashboardSnapshot",
                kwargs={"snapshot_date": "2024-10-31"},
            ),
            Action(
                name="LogInvoiceEvent",
                kwargs={"event_type": "reviewed", "invoice_number": "2024-010"},
            ),
            Action(name="ListInvoiceEvents", kwargs={"invoice_number": "2024-010"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_75",
        instruction="Compose a succinct November‑2024 invoice for publisher_id 'PUB004' and document its audit. The end result should be: invoice_number '2024-141' is generated for period_start '2024-11-01' to period_end '2024-11-30' with accurate totals (4h @88.0, hst_rate 0.13) and is legible; a single entry is added for project_id 'PROJ003' with isbn '978-1-3100-0003-7' for 4h @88.0 and is accessible; an audit event 'generated' has been recorded and is accessible. Utilize pdf_path 'https://test.storage.com/invoices/2024/INV-2024-141.pdf'.",
        actions=[
            Action(
                name="CreateInvoiceRecord",
                kwargs={
                    "hst_amount": 45.76,
                    "invoice_date": "2024-11-30",
                    "invoice_number": "2024-141",
                    "pdf_path": "https://test.storage.com/invoices/2024/INV-2024-141.pdf",
                    "period_end": "2024-11-30",
                    "period_start": "2024-11-01",
                    "publisher_id": "PUB004",
                    "subtotal": 352.0,
                    "total_due": 397.76,
                },
            ),
            Action(name="FetchInvoiceRecord", kwargs={"invoice_number": "2024-141"}),
            Action(
                name="CreateInvoiceLines",
                kwargs={
                    "invoice_number": "2024-141",
                    "lines": [
                        {
                            "hours": 4,
                            "isbn": "978-1-3100-0003-7",
                            "project_id": "PROJ003",
                            "rate": 88.0,
                        }
                    ],
                },
            ),
            Action(name="ListInvoiceLinesByInvoice", kwargs={"invoice_number": "2024-141"}),
            Action(
                name="LogInvoiceEvent",
                kwargs={"event_type": "generated", "invoice_number": "2024-141"},
            ),
            Action(name="ListInvoiceEvents", kwargs={"invoice_number": "2024-141"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_76",
        instruction=(
            "Revise billing contacts and carry out a November-2024 billing review. The final state: publisher_id 'PUB003' holds contact_email 'ap@canopypress.ca' and is accessible; consultant_id 'CONS001' possesses email 'sarah.thompson+ar@consultingpro.ca' and is accessible; rates are verified for ['PROJ001','PROJ003']; calculate a sample total for 2h @85.0 and 2h @75.0 via compute_invoice_totals applying an HST rate of 0.13; Accounts Receivable aging for '2024-11' is saved (PDF: 'https://test.storage.com/reports/accounts_receivable_2024-11.pdf')."
        ),
    actions=[
            Action(
                name="MutateClientContact",
                kwargs={"contact_email": "ap@canopypress.ca", "publisher_id": "PUB003"},
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB003"}),
            Action(
                name="MutateConsultantContact",
                kwargs={
                    "consultant_id": "CONS001",
                    "email": "sarah.thompson+ar@consultingpro.ca",
                },
            ),
            Action(name="FetchConsultantProfile", kwargs={"consultant_id": "CONS001"}),
            Action(
                name="MapHourlyRates",
                kwargs={"project_id_list": ["PROJ001", "PROJ003"]},
            ),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={
                    "hst_rate": 0.13,
                    "lines": [{"hours": 2, "rate": 85.0}, {"hours": 2, "rate": 75.0}],
                },
            ),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-11"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_77",
        instruction="Handle the addition of a project for 'PUB001' and validate a total for August‑2024. Final state: project_id 'PROJ2035' is present with isbn '978-1-3100-2035-3', project_title 'Chemistry Workbook, 1e', default_hourly_rate 87.0 and is visible; rates are resolved for ['PROJ2035','PROJ001'] and a sample total is calculated (2h @87.0 and 2h @85.0 with hst_rate 0.13); the Account Receivable aging PDF is generated for '2024-08'.",
        actions=[
            Action(
                name="AddProjectCard",
                kwargs={
                    "default_hourly_rate": 87.0,
                    "isbn": "978-1-3100-2035-3",
                    "project_id": "PROJ2035",
                    "project_title": "Chemistry Workbook, 1e",
                    "publisher_id": "PUB001",
                },
            ),
            Action(name="FetchProjectCard", kwargs={"project_id": "PROJ2035"}),
            Action(
                name="MapHourlyRates",
                kwargs={"project_id_list": ["PROJ2035", "PROJ001"]},
            ),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={
                    "hst_rate": 0.13,
                    "lines": [{"hours": 2, "rate": 87.0}, {"hours": 2, "rate": 85.0}],
                },
            ),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-08"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_78",
        instruction="Coordinate the creation of publisher_id 'PUB049' named 'Blue Shore Academics' with a civics project and verify a context for September‑2024. Final state: 'PUB049' is established and accessible; project_id 'PROJ3069' is established with isbn '978-1-3100-3069-4', project_title 'Civics Foundations, 1e', default_hourly_rate 88.0 and is accessible; open invoices are examined; 12‑month KPIs are obtainable; a sample total is calculated (2h @88.0 with hst_rate 0.13); the Account Receivable aging PDF is generated for '2024-09'.",
        actions=[
            Action(
                name="AddClientProfile",
                kwargs={"name": "Blue Shore Academics", "publisher_id": "PUB049"},
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB049"}),
            Action(
                name="AddProjectCard",
                kwargs={
                    "default_hourly_rate": 88.0,
                    "isbn": "978-1-3100-3069-4",
                    "project_id": "PROJ3069",
                    "project_title": "Civics Foundations, 1e",
                    "publisher_id": "PUB049",
                },
            ),
            Action(name="FetchProjectCard", kwargs={"project_id": "PROJ3069"}),
            Action(name="QueryInvoices", kwargs={"status": "open"}),
            Action(name="DeriveCollectionKpis", kwargs={"window_months": 12}),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 2, "rate": 88.0}]},
            ),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-09"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_79",
        instruction="Organize contacts and conduct a quick October‑2024 health check. Your target outcome: consultant_id 'CONS001' has the phone number '+1-416-555-0177' which is accessible; publisher_id 'PUB004' is accessible; open invoices have been reviewed and 12‑month KPIs are accessible; the Account Receivable aging report for '2024-10' is exported.",
        actions=[
            Action(
                name="MutateConsultantContact",
                kwargs={"consultant_id": "CONS001", "phone": "+1-416-555-0177"},
            ),
            Action(name="FetchConsultantProfile", kwargs={"consultant_id": "CONS001"}),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB004"}),
            Action(name="QueryInvoices", kwargs={"status": "open"}),
            Action(name="DeriveCollectionKpis", kwargs={"window_months": 12}),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-10"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_80",
        instruction="Introduce publisher_id 'PUB046' with the name 'Lantern House Education' and organize a snapshot for November‑2024. Your target outcome: 'PUB046' is created and accessible; project_id 'PROJ3061' is established with isbn '978-1-3100-3061-9', project_title 'Critical Thinking, 1e', default_hourly_rate 99.0 and is accessible; open invoices have been reviewed; 12‑month KPIs are accessible; an Account Receivable aging PDF for '2024-11' is available; a dashboard snapshot for '2024-11-30' is filed and can be accessed by date.",
        actions=[
            Action(
                name="AddClientProfile",
                kwargs={"name": "Lantern House Education", "publisher_id": "PUB046"},
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB046"}),
            Action(
                name="AddProjectCard",
                kwargs={
                    "default_hourly_rate": 99.0,
                    "isbn": "978-1-3100-3061-9",
                    "project_id": "PROJ3061",
                    "project_title": "Critical Thinking, 1e",
                    "publisher_id": "PUB046",
                },
            ),
            Action(name="FetchProjectCard", kwargs={"project_id": "PROJ3061"}),
            Action(name="QueryInvoices", kwargs={"status": "open"}),
            Action(name="DeriveCollectionKpis", kwargs={"window_months": 12}),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-11"}),
            Action(
                name="CreateDashboardSnapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-11.pdf",
                    "snapshot_date": "2024-11-30",
                },
            ),
            Action(
                name="FetchDashboardSnapshot",
                kwargs={"snapshot_date": "2024-11-30"},
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_81",
        instruction="Handle the creation of publisher_id 'PUB055' with the name 'Summit Ridge Learning' and set up an October‑2024 dashboard featuring a small sample. End state goals: ensure 'PUB055' is established and accessible; open invoices are verified; provide 12‑month KPIs; resolve rates for ['PROJ001']; a sample total is calculated (1h @85.0 with hst_rate 0.13); produce the Account Receivable aging PDF for '2024-10'; archive a dashboard snapshot for '2024-10-31' citing that PDF, accessible by date.",
        actions=[
            Action(
                name="AddClientProfile",
                kwargs={"name": "Summit Ridge Learning", "publisher_id": "PUB055"},
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB055"}),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-10"}),
            Action(
                name="CreateDashboardSnapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-10.pdf",
                    "snapshot_date": "2024-10-31",
                },
            ),
            Action(
                name="FetchDashboardSnapshot",
                kwargs={"snapshot_date": "2024-10-31"},
            ),
            Action(name="QueryInvoices", kwargs={"status": "open"}),
            Action(name="DeriveCollectionKpis", kwargs={"window_months": 12}),
            Action(
                name="MapHourlyRates", kwargs={"project_id_list": ["PROJ001"]}
            ),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 1, "rate": 85.0}]},
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_82",
        instruction="Open project_id 'PROJ2044' for 'PUB004' and conduct a check for November‑2024. Aim for the following end state: ensure 'PROJ2044' is created with isbn '978-1-3100-2044-7', project_title 'Media Literacy, 1e', default_hourly_rate 101.0, and is viewable; confirm rate resolutions for ['PROJ2044'] and calculate a sample total (3h @101.0 with hst_rate 0.13); generate the Account Receivable aging PDF for '2024-11'; make sure representative invoice '2024-010' can be accessed for reading.",
        actions=[
            Action(
                name="AddProjectCard",
                kwargs={
                    "default_hourly_rate": 101.0,
                    "isbn": "978-1-3100-2044-7",
                    "project_id": "PROJ2044",
                    "project_title": "Media Literacy, 1e",
                    "publisher_id": "PUB004",
                },
            ),
            Action(name="FetchProjectCard", kwargs={"project_id": "PROJ2044"}),
            Action(
                name="MapHourlyRates", kwargs={"project_id_list": ["PROJ2044"]}
            ),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 3, "rate": 101.0}]},
            ),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-11"}),
            Action(name="FetchInvoiceRecord", kwargs={"invoice_number": "2024-010"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_83",
        instruction="Handle the addition of publisher_id 'PUB035' named 'Northern Ridge Press' and set a July‑2024 baseline. Your goal: Ensure 'PUB035' is established and viewable; confirm project_id 'PROJ2041' under 'PUB035' is created with isbn '978-1-3100-2041-6', project_title 'Algebra Readiness, 1e', default_hourly_rate 93.0 and is accessible; compute a sample total (2h @93.0 with hst_rate 0.13); generate the Account Receivable aging PDF for '2024-07' and store a snapshot for '2024-07-31' that references that PDF and is accessible.",
        actions=[
            Action(
                name="AddClientProfile",
                kwargs={"name": "Northern Ridge Press", "publisher_id": "PUB035"},
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB035"}),
            Action(
                name="AddProjectCard",
                kwargs={
                    "default_hourly_rate": 93.0,
                    "isbn": "978-1-3100-2041-6",
                    "project_id": "PROJ2041",
                    "project_title": "Algebra Readiness, 1e",
                    "publisher_id": "PUB035",
                },
            ),
            Action(name="FetchProjectCard", kwargs={"project_id": "PROJ2041"}),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 2, "rate": 93.0}]},
            ),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-07"}),
            Action(
                name="CreateDashboardSnapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-07.pdf",
                    "snapshot_date": "2024-07-31",
                },
            ),
            Action(
                name="FetchDashboardSnapshot",
                kwargs={"snapshot_date": "2024-07-31"},
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_84",
        instruction=(
            "Coordinate the addition of a humanities project and schedule an August-2024 review. The final state: project_id 'PROJ1106' is created for 'PUB003' with isbn '978-1-3100-1015-6', project_title 'Philosophy Primer, 1e', default_hourly_rate 91.0, and is viewable; resolve rates for ['PROJ1106']; compute a sample total for 2h @91.0 applying HST rate 0.13; export Accounts Receivable aging for '2024-08' and ensure availability at 'https://test.storage.com/reports/accounts_receivable_2024-08.pdf'; produce a dashboard snapshot dated '2024-08-31', ensuring it is accessible by snapshot_date and references the same A/R PDF."
        ),
    actions=[
            Action(
                name="AddProjectCard",
                kwargs={
                    "default_hourly_rate": 91.0,
                    "isbn": "978-1-3100-1015-6",
                    "project_id": "PROJ1106",
                    "project_title": "Philosophy Primer, 1e",
                    "publisher_id": "PUB003",
                },
            ),
            Action(name="FetchProjectCard", kwargs={"project_id": "PROJ1106"}),
            Action(
                name="MapHourlyRates", kwargs={"project_id_list": ["PROJ1106"]}
            ),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 2, "rate": 91.0}]},
            ),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-08"}),
            Action(
                name="CreateDashboardSnapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-08.pdf",
                    "snapshot_date": "2024-08-31",
                },
            ),
            Action(
                name="FetchDashboardSnapshot",
                kwargs={"snapshot_date": "2024-08-31"},
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_85",
        instruction=(
            "Handle the creation and emailing of an invoice for August-2024 for publisher_id 'PUB003'. Your final goal: ensure invoice_number 'INV-2024-209' is established with invoice_date '2024-08-31', period_start '2024-08-01', period_end '2024-08-31', subtotal 875.0, hst_amount 113.75, total_due 988.75, pdf_path '/invoices/2024/INV-2024-209.pdf' and is accessible; confirm the invoice email has been dispatched from consultant_id 'CONS001' with subject 'Invoice INV-2024-209', body_text 'August 2024 invoice attached.' along with the attachment; verify the invoice record shows a completed 'sent_at' timestamp; ensure an 'emailed' audit for 'INV-2024-209' is logged and visible."
        ),
    actions=[
            Action(
                name="CreateInvoiceRecord",
                kwargs={
                    "hst_amount": 113.75,
                    "invoice_date": "2024-08-31",
                    "invoice_number": "INV-2024-209",
                    "pdf_path": "/invoices/2024/INV-2024-209.pdf",
                    "period_end": "2024-08-31",
                    "period_start": "2024-08-01",
                    "publisher_id": "PUB003",
                    "subtotal": 875.0,
                    "total_due": 988.75,
                },
            ),
            Action(
                name="FetchInvoiceRecord", kwargs={"invoice_number": "INV-2024-209"}
            ),
            Action(
                name="DispatchInvoiceEmail",
                kwargs={
                    "attachment": "/invoices/2024/INV-2024-209.pdf",
                    "body_text": "August 2024 invoice attached.",
                    "consultant_id": "CONS001",
                    "invoice_number": "INV-2024-209",
                    "publisher_id": "PUB003",
                    "subject": "Invoice INV-2024-209",
                },
            ),
            Action(
                name="LogInvoiceEvent",
                kwargs={"event_type": "emailed", "invoice_number": "INV-2024-209"},
            ),
            Action(
                name="ListInvoiceEvents", kwargs={"invoice_number": "INV-2024-209"}
            ),
            Action(
                name="FetchInvoiceRecord", kwargs={"invoice_number": "INV-2024-209"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_86",
        instruction="Coordinate the update of the October–2024 Account Receivable context and verify key contacts. Your objective: assess open invoices (status 'open'); ensure Account Receivable aging exports are available for period labels '2024-10' and '2024-09'; update publisher_id 'PUB004' contact_email to 'ap@bluepeakpublishing.ca' and confirm its visibility; validate consultant_id 'CONS001' address by documenting '1234 Oak Street, Montreal, ON M5V 3A8' and reviewing it; calculate 12–month collection KPIs (window_months 12); list projects ensuring project_id 'PROJ004' details are accessible; and, for an immediate risk assessment, determine days outstanding using invoice_number '2024-010' with due_date '2024-10-31' and today '2024-11-15' (15 days) and categorize that result. Confirm each write through a follow-up read utilizing only available domain tools.",
        actions=[
            Action(name="QueryInvoices", kwargs={"status": "open"}),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-10"}),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-09"}),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB004"}),
            Action(
                name="MutateClientContact",
                kwargs={
                    "contact_email": "ap@bluepeakpublishing.ca",
                    "publisher_id": "PUB004",
                },
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB004"}),
            Action(name="FetchConsultantProfile", kwargs={"consultant_id": "CONS001"}),
            Action(
                name="MutateConsultantContact",
                kwargs={
                    "address": "1234 Oak Street, Montreal, ON M5V 3A8",
                    "consultant_id": "CONS001",
                },
            ),
            Action(name="FetchConsultantProfile", kwargs={"consultant_id": "CONS001"}),
            Action(name="DeriveCollectionKpis", kwargs={"window_months": 12}),
            Action(
                name="DeriveDaysOutstanding",
                kwargs={
                    "invoices": [
                        {"invoice_number": "2024-010", "period_end": "2024-10-31"}
                    ],
                    "today": "2024-11-15",
                },
            ),
            Action(
                name="BucketizeAging",
                kwargs={
                    "aging": [{"days_outstanding": 15, "invoice_number": "2024-010"}]
                },
            ),
            Action(name="ListProjectsCatalog", kwargs={}),
            Action(name="FetchProjectCard", kwargs={"project_id": "PROJ004"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_87",
        instruction="Handle publisher_id 'PUB044' titled 'Cedar Ridge Press' and ensure alignment for an August‑2024 snapshot. Your desired outcome: 'PUB044' is established and accessible; project_id 'PROJ3057' exists with isbn '978-1-3100-3057-2', named 'Financial Literacy, 1e', has a default_hourly_rate of 91.0 and is readable; calculate a sample total (2h @91.0 with hst_rate 0.13); make sure the Account Receivable aging PDF is available for '2024-08' and store a dashboard snapshot for '2024-08-31' referencing the mentioned PDF, ensuring it remains accessible by date.",
        actions=[
            Action(
                name="AddClientProfile",
                kwargs={"name": "Cedar Ridge Press", "publisher_id": "PUB044"},
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB044"}),
            Action(
                name="AddProjectCard",
                kwargs={
                    "default_hourly_rate": 91.0,
                    "isbn": "978-1-3100-3057-2",
                    "project_id": "PROJ3057",
                    "project_title": "Financial Literacy, 1e",
                    "publisher_id": "PUB044",
                },
            ),
            Action(name="FetchProjectCard", kwargs={"project_id": "PROJ3057"}),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 2, "rate": 91.0}]},
            ),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-08"}),
            Action(
                name="CreateDashboardSnapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-08.pdf",
                    "snapshot_date": "2024-08-31",
                },
            ),
            Action(
                name="FetchDashboardSnapshot",
                kwargs={"snapshot_date": "2024-08-31"},
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_88",
        instruction="Initiate addition of publisher_id 'PUB048' with the name 'Bright Pine Press' and coordinate November‑2024 reporting with a minor sample. Aim for a state where: 'PUB048' is included and accessible; review any open invoices; ensure availability of 12‑month KPIs; rates are finalized for ['PROJ001']; compute a sample total (1h @85.0 with hst_rate 0.13); verify the availability of the Account Receivable aging PDF for '2024-11'; make sure a dashboard snapshot for '2024-11-30' is stored and remains accessible by date.",
        actions=[
            Action(
                name="AddClientProfile",
                kwargs={"name": "Bright Pine Press", "publisher_id": "PUB048"},
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB048"}),
            Action(name="QueryInvoices", kwargs={"status": "open"}),
            Action(name="DeriveCollectionKpis", kwargs={"window_months": 12}),
            Action(
                name="MapHourlyRates", kwargs={"project_id_list": ["PROJ001"]}
            ),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 1, "rate": 85.0}]},
            ),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-11"}),
            Action(
                name="CreateDashboardSnapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-11.pdf",
                    "snapshot_date": "2024-11-30",
                },
            ),
            Action(
                name="FetchDashboardSnapshot",
                kwargs={"snapshot_date": "2024-11-30"},
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_89",
        instruction="Handle the introduction of publisher_id 'PUB021' named 'Pioneer Learning Press' and initiate an August‑2024 snapshot. Your final state: 'PUB021' is present and visible; establish a small project 'PROJ1012' under 'PUB021' with isbn '978-1-3100-1012-7', project_title 'Civics Primer, 1e', default_hourly_rate 86.0 and ensure visibility; calculate sample totals (2h @86.0 with hst_rate 0.13); ensure the Account Receivable aging PDF for '2024-08' is available and store a dashboard snapshot for '2024-08-31' that references the PDF.",
        actions=[
            Action(
                name="AddClientProfile",
                kwargs={"name": "Pioneer Learning Press", "publisher_id": "PUB021"},
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB021"}),
            Action(
                name="AddProjectCard",
                kwargs={
                    "default_hourly_rate": 86.0,
                    "isbn": "978-1-3100-1012-7",
                    "project_id": "PROJ1012",
                    "project_title": "Civics Primer, 1e",
                    "publisher_id": "PUB021",
                },
            ),
            Action(name="FetchProjectCard", kwargs={"project_id": "PROJ1012"}),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 2, "rate": 86.0}]},
            ),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-08"}),
            Action(
                name="CreateDashboardSnapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-08.pdf",
                    "snapshot_date": "2024-08-31",
                },
            ),
            Action(
                name="FetchDashboardSnapshot",
                kwargs={"snapshot_date": "2024-08-31"},
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_90",
        instruction="Coordinate validation for readiness around project_id 'PROJ001' for November‑2024 and document an aging categorization. Your final state: projects are displayed and 'PROJ001' details are accessible; resolve rates for ['PROJ001']; compute a sample total (3h @85.0 with hst_rate 0.13); review open invoices; make 12‑month KPIs accessible; ensure the Account Receivable aging PDF is available for '2024-11'; categorize days outstanding for invoice '2024-010' as of '2024-11-20' using period_end '2024-10-31' (20 days); record an invoice audit event 'aging_categorized' for '2024-010' and ensure listability.",
        actions=[
            Action(name="ListProjectsCatalog", kwargs={}),
            Action(name="FetchProjectCard", kwargs={"project_id": "PROJ001"}),
            Action(
                name="MapHourlyRates", kwargs={"project_id_list": ["PROJ001"]}
            ),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 3, "rate": 85.0}]},
            ),
            Action(name="QueryInvoices", kwargs={"status": "open"}),
            Action(name="DeriveCollectionKpis", kwargs={"window_months": 12}),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-11"}),
            Action(
                name="DeriveDaysOutstanding",
                kwargs={
                    "invoices": [
                        {"invoice_number": "2024-010", "period_end": "2024-10-31"}
                    ],
                    "today": "2024-11-20",
                },
            ),
            Action(
                name="BucketizeAging",
                kwargs={
                    "aging": [{"days_outstanding": 20, "invoice_number": "2024-010"}]
                },
            ),
            Action(
                name="LogInvoiceEvent",
                kwargs={
                    "event_type": "aging_categorized",
                    "invoice_number": "2024-010",
                },
            ),
            Action(name="ListInvoiceEvents", kwargs={"invoice_number": "2024-010"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_91",
        instruction="Initiate a new publisher and submit an August‑2024 snapshot. Your desired outcome: publisher_id 'PUB023' named 'North Shore Academy' is existent and accessible; contact_email is 'accounts@northshoreacademy.ca' and is accessible; Account Receivable aging for '2024-08' is exported and a snapshot is stored for '2024-08-31'.",
        actions=[
            Action(
                name="AddClientProfile",
                kwargs={"name": "North Shore Academy", "publisher_id": "PUB023"},
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB023"}),
            Action(
                name="MutateClientContact",
                kwargs={
                    "contact_email": "accounts@northshoreacademy.ca",
                    "publisher_id": "PUB023",
                },
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB023"}),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-08"}),
            Action(
                name="CreateDashboardSnapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-08.pdf",
                    "snapshot_date": "2024-08-31",
                },
            ),
            Action(
                name="FetchDashboardSnapshot",
                kwargs={"snapshot_date": "2024-08-31"},
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_92",
        instruction="Register project_id 'PROJ1015' for 'PUB005' and calculate an October‑2024 sample with context. Your desired outcome: 'PROJ1015' is existent with isbn '978-1-3100-1015-8', project_title 'Canadian Geography, 2e', default_hourly_rate 90.0 and is visible; 'PUB005' is accessible; a sample total is computed (4h @90.0 with hst_rate 0.13); the Account Receivable aging PDF is existent for '2024-10'.",
        actions=[
            Action(
                name="AddProjectCard",
                kwargs={
                    "default_hourly_rate": 90.0,
                    "isbn": "978-1-3100-1015-8",
                    "project_id": "PROJ1015",
                    "project_title": "Canadian Geography, 2e",
                    "publisher_id": "PUB005",
                },
            ),
            Action(name="FetchProjectCard", kwargs={"project_id": "PROJ1015"}),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB005"}),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 4, "rate": 90.0}]},
            ),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-10"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_93",
        instruction="Handle the creation of publisher_id 'PUB025' with the name 'Lakeside Scholastic' and conclude an August snapshot. Your end state is that 'PUB025' exists and is visible; the Account Receivable aging PDF is available for '2024-08' with a dashboard snapshot saved for '2024-08-31' referencing that PDF; calculate a sample total (2h @85.0 with hst_rate 0.13) using rates for ['PROJ001'].",
        actions=[
            Action(
                name="AddClientProfile",
                kwargs={"name": "Lakeside Scholastic", "publisher_id": "PUB025"},
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB025"}),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-08"}),
            Action(
                name="CreateDashboardSnapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-08.pdf",
                    "snapshot_date": "2024-08-31",
                },
            ),
            Action(
                name="FetchDashboardSnapshot",
                kwargs={"snapshot_date": "2024-08-31"},
            ),
            Action(
                name="MapHourlyRates", kwargs={"project_id_list": ["PROJ001"]}
            ),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 2, "rate": 85.0}]},
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_94",
        instruction="Coordinate the registration of publisher_id 'PUB036' under the name 'Cedar Grove Texts' and organize an October–2024 summary. Your end state: 'PUB036' exists and is visible; open invoices have been reviewed; 12‑month KPIs are available; the Account Receivable aging PDF for '2024-10' exists; ensure that the contact for 'PUB003' is 'ap@canopypress.ca' and it is readable.",
        actions=[
            Action(
                name="AddClientProfile",
                kwargs={"name": "Cedar Grove Texts", "publisher_id": "PUB036"},
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB036"}),
            Action(name="QueryInvoices", kwargs={"status": "open"}),
            Action(name="DeriveCollectionKpis", kwargs={"window_months": 12}),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-10"}),
            Action(
                name="MutateClientContact",
                kwargs={"contact_email": "ap@canopypress.ca", "publisher_id": "PUB003"},
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB003"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_95",
        instruction="Handle the updating of two AP contacts and verify the KPIs for November‑2024. Your final state: 'PUB001' contact_email is 'accounts@nelson-edu.ca' and it is visible; 'PUB003' contact_email is 'accounts@canopypress.ca' and it is visible; ensure open invoices are examined; 12‑month KPIs should be accessible; ensure the Account Receivable aging PDF exists for '2024-11'.",
        actions=[
            Action(
                name="MutateClientContact",
                kwargs={
                    "contact_email": "accounts@nelson-edu.ca",
                    "publisher_id": "PUB001",
                },
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB001"}),
            Action(
                name="MutateClientContact",
                kwargs={
                    "contact_email": "accounts@canopypress.ca",
                    "publisher_id": "PUB003",
                },
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB003"}),
            Action(name="QueryInvoices", kwargs={"status": "open"}),
            Action(name="DeriveCollectionKpis", kwargs={"window_months": 12}),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-11"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_96",
        instruction="Coordinate the registration of publisher_id 'PUB032' with the name 'Harborview Education' and archive the summer Account Receivable snapshots. Your desired outcome: 'PUB032' is present and viewable; Account Receivable aging PDFs are available for '2024-07' and '2024-06'; dashboard snapshots are saved for '2024-07-31' and '2024-06-30' relating to those PDFs and should be viewable by id; verify that open invoices are examined and 12‑month KPIs can be accessed.",
        actions=[
            Action(
                name="AddClientProfile",
                kwargs={"name": "Harborview Education", "publisher_id": "PUB032"},
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB032"}),
            Action(name="QueryInvoices", kwargs={"status": "open"}),
            Action(name="DeriveCollectionKpis", kwargs={"window_months": 12}),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-07"}),
            Action(
                name="CreateDashboardSnapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-07.pdf",
                    "snapshot_date": "2024-07-31",
                },
            ),
            Action(name="FetchDashboardSnapshot", kwargs={"snapshot_id": 1}),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-06"}),
            Action(
                name="CreateDashboardSnapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-06.pdf",
                    "snapshot_date": "2024-06-30",
                },
            ),
            Action(name="FetchDashboardSnapshot", kwargs={"snapshot_id": 2}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_97",
        instruction="Handle the preparation and dispatch of an October‑2024 invoice for publisher_id 'PUB001'. Your end goal: invoice_number 'INV-2024-230' is generated with invoice_date '2024-10-31', period_start '2024-10-01', period_end '2024-10-31', subtotal 850.0, hst_amount 110.5, total_due 960.5, pdf_path '/invoices/2024/INV-2024-230.pdf' and is accessible; the invoice is sent via email from consultant_id 'CONS001' with subject 'Invoice INV-2024-230' and body_text 'October 2024 invoice attached.' as well as an attachment; an 'emailed' audit entry is noted and displayed.",
        actions=[
            Action(
                name="CreateInvoiceRecord",
                kwargs={
                    "hst_amount": 110.5,
                    "invoice_date": "2024-10-31",
                    "invoice_number": "INV-2024-230",
                    "pdf_path": "/invoices/2024/INV-2024-230.pdf",
                    "period_end": "2024-10-31",
                    "period_start": "2024-10-01",
                    "publisher_id": "PUB001",
                    "subtotal": 850.0,
                    "total_due": 960.5,
                },
            ),
            Action(
                name="FetchInvoiceRecord", kwargs={"invoice_number": "INV-2024-230"}
            ),
            Action(
                name="DispatchInvoiceEmail",
                kwargs={
                    "attachment": "/invoices/2024/INV-2024-230.pdf",
                    "body_text": "October 2024 invoice attached.",
                    "consultant_id": "CONS001",
                    "invoice_number": "INV-2024-230",
                    "publisher_id": "PUB001",
                    "subject": "Invoice INV-2024-230",
                },
            ),
            Action(
                name="LogInvoiceEvent",
                kwargs={"event_type": "emailed", "invoice_number": "INV-2024-230"},
            ),
            Action(
                name="ListInvoiceEvents", kwargs={"invoice_number": "INV-2024-230"}
            ),
            Action(
                name="FetchInvoiceRecord", kwargs={"invoice_number": "INV-2024-230"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_98",
        instruction="Organize PUB010 and its project, followed by an August‑2024 micro‑billing assessment. Your end state: publisher_id 'PUB010' is created with precisely name 'Maple Leaf Educational', address '100 Bloor St W, Montreal, ON', contact_email 'ap@mapleleafedu.ca', gst_number 'GST-999-010' and is accessible; project_id 'PROJ990' is set under 'PUB010' with isbn '978-1-9876-5432-1', project_title 'Intro Statistics, 5e', default_hourly_rate 105.0, override_hourly_rate None, account_code 'STAT-5E-2025', is_active True and is accessible; determine the rate for ['PROJ990'] and calculate a single‑line sample total (4 hours at 105.0 with hst_rate 0.13); and export the Account Receivable aging for period_label '2024-08'. Ensure each write is confirmed by a follow-up read.",
        actions=[
            Action(
                name="AddClientProfile",
                kwargs={
                    "address": "100 Bloor St W, Montreal, ON",
                    "contact_email": "ap@mapleleafedu.ca",
                    "gst_number": "GST-999-010",
                    "name": "Maple Leaf Educational",
                    "publisher_id": "PUB010",
                },
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB010"}),
            Action(
                name="AddProjectCard",
                kwargs={
                    "account_code": "STAT-5E-2025",
                    "default_hourly_rate": 105.0,
                    "is_active": True,
                    "isbn": "978-1-9876-5432-1",
                    "override_hourly_rate": None,
                    "project_id": "PROJ990",
                    "project_title": "Intro Statistics, 5e",
                    "publisher_id": "PUB010",
                },
            ),
            Action(name="FetchProjectCard", kwargs={"project_id": "PROJ990"}),
            Action(
                name="MapHourlyRates", kwargs={"project_id_list": ["PROJ990"]}
            ),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 4, "rate": 105.0}]},
            ),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-08"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_99",
        instruction="You must refine August–2024 contact data and confirm KPIs. Your final condition: 'PUB001' contact_email equals 'ap@nelson-edu.ca' and is visible; 'CONS001' address equals '1234 Oak Street, Montreal, ON M5V 3A8' and is visible; open invoices are assessed and 12–month KPIs are available; calculate a sample total (3h @85.0 with hst_rate 0.13); ensure the Account Receivable aging PDF exists for '2024-08'.",
        actions=[
            Action(
                name="MutateClientContact",
                kwargs={"contact_email": "ap@nelson-edu.ca", "publisher_id": "PUB001"},
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB001"}),
            Action(
                name="MutateConsultantContact",
                kwargs={
                    "address": "1234 Oak Street, Montreal, ON M5V 3A8",
                    "consultant_id": "CONS001",
                },
            ),
            Action(name="FetchConsultantProfile", kwargs={"consultant_id": "CONS001"}),
            Action(name="QueryInvoices", kwargs={"status": "open"}),
            Action(name="DeriveCollectionKpis", kwargs={"window_months": 12}),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 3, "rate": 85.0}]},
            ),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-08"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="V2",
        user_id="task_100",
        instruction="Include publisher_id 'PUB057' named 'Harbor Lights Learning' and set up an August–2024 dashboard with a minor total. The desired state: 'PUB057' exists and is accessible; calculate a sample total (1h @85.0 with hst_rate 0.13) using the rate for ['PROJ001']; ensure the Account Receivable aging PDF is present for '2024-08'; a dashboard snapshot is stored for '2024-08-31' referencing 'https://test.storage.com/reports/accounts_receivable_2024-08.pdf' and is accessible by date; days outstanding for '2024-010' as of '2024-08-15' using period_end '2024-07-31' (15 days) are classified.",
        actions=[
            Action(
                name="AddClientProfile",
                kwargs={"name": "Harbor Lights Learning", "publisher_id": "PUB057"},
            ),
            Action(name="FetchClientProfile", kwargs={"publisher_id": "PUB057"}),
            Action(
                name="MapHourlyRates", kwargs={"project_id_list": ["PROJ001"]}
            ),
            Action(
                name="ComputeInvoiceTotals",
                kwargs={"hst_rate": 0.13, "lines": [{"hours": 1, "rate": 85.0}]},
            ),
            Action(name="RenderAccountsReceivableReport", kwargs={"period_label": "2024-08"}),
            Action(
                name="CreateDashboardSnapshot",
                kwargs={
                    "pdf_path": "https://test.storage.com/reports/accounts_receivable_2024-08.pdf",
                    "snapshot_date": "2024-08-31",
                },
            ),
            Action(
                name="FetchDashboardSnapshot",
                kwargs={"snapshot_date": "2024-08-31"},
            ),
            Action(
                name="DeriveDaysOutstanding",
                kwargs={
                    "invoices": [
                        {"invoice_number": "2024-010", "period_end": "2024-07-31"}
                    ],
                    "today": "2024-08-15",
                },
            ),
            Action(
                name="BucketizeAging",
                kwargs={
                    "aging": [{"days_outstanding": 15, "invoice_number": "2024-010"}]
                },
            ),
        ],
        outputs=[]
    ),
]
