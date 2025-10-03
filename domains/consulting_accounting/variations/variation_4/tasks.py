from domains.dto import Task, Action

TASKS = [
    Task(
        annotator="A",
        user_id="ca_v4_001",
        instruction=(
            "Handle the establishment of base records and contacts, then generate an August‑2024 context snapshot. End state: publisher_id 'PUB010' is created with precisely name 'Maple Leaf Educational', address '100 Bloor St W, Montreal, ON', contact_email 'ap@mapleleafedu.ca', gst_number 'GST-999-010' and is readable; update publisher_id 'PUB002' contact_email to 'ap@northernlights-edu.ca' and ensure readability; change consultant_id 'CONS001' phone number to '+1-416-555-0199' and confirm readability; retrieve August‑2024 time entries for ['PROJ001'] covering period_start '2024-08-01' to period_end '2024-08-31'; determine the hourly rate for ['PROJ001']; compute a sample total on a single line (10 hours at 85.0 with hst_rate 0.13); and export the A/R aging for period_label '2024-08'. Verify each write by performing a subsequent read, utilizing only available tools."
        ),
        actions=[
            Action(name="CreatePublisher", kwargs={
                "publisher_id": "PUB010",
                "name": "Maple Leaf Educational",
                "address": "100 Bloor St W, Montreal, ON",
                "contact_email": "ap@mapleleafedu.ca",
                "gst_number": "GST-999-010"
            }),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB010"}),

            Action(name="UpdatePublisherContact", kwargs={
                "publisher_id": "PUB002",
                "contact_email": "ap@northernlights-edu.ca"
            }),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB002"}),

            Action(name="UpdateConsultantContact", kwargs={
                "consultant_id": "CONS001",
                "phone": "+1-416-555-0199"
            }),
            Action(name="GetConsultantProfile", kwargs={"consultant_id": "CONS001"}),

            Action(name="FetchTimeEntries", kwargs={
                "project_id_list": ["PROJ001"],
                "period_start": "2024-08-01",
                "period_end": "2024-08-31"
            }),
            Action(name="ResolveHourlyRates", kwargs={"project_id_list": ["PROJ001"]}),
            Action(name="CalculateInvoiceTotals", kwargs={
                "lines": [{"hours": 10, "rate": 85.0}],
                "hst_rate": 0.13
            }),

            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-08"}),
        ],
        outputs=[
            "PUB010 created & read; PUB002 AP updated & read; CONS001 phone updated & read; "
            "Aug‑2024 entries fetched; rate resolved for PROJ001; sample total computed; AR_Aging_2024-08 exported."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_002",
        instruction=(
            "Conduct an A/R health pass and introduce a new client. End state: establish new publisher_id 'PUB011' with exactly name 'Canopy Learning Ltd.', address '77 Front St E, Montreal, ON', contact_email 'ap@canopylearning.ca', gst_number 'GST-999-011' and ensure readability; calculate 12‑month collection KPIs (window_months 12); export the A/R aging for period_label '2024-09'; and update publisher_id 'PUB003' contact_email to 'ap@canopypress.ca' and confirm readability. Each write must be verified by a subsequent read."
        ),
        actions=[
            Action(name="CreatePublisher", kwargs={
                "publisher_id": "PUB011",
                "name": "Canopy Learning Ltd.",
                "address": "77 Front St E, Montreal, ON",
                "contact_email": "ap@canopylearning.ca",
                "gst_number": "GST-999-011"
            }),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB011"}),
            Action(name="ComputeCollectionKpis", kwargs={"window_months": 12}),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-09"}),
            Action(name="UpdatePublisherContact", kwargs={
                "publisher_id": "PUB003",
                "contact_email": "ap@canopypress.ca"
            }),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB003"}),
        ],
        outputs=[
            "PUB011 created & read; 12‑month KPIs computed; AR_Aging_2024-09 exported; "
            "PUB003 AP updated & read."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_003",
        instruction=(
            "Handle the preparation of a July‑2024 billing overview and update key contacts. Retrieve time entries for ['PROJ001','PROJ003'] from 2024-07-01 to 2024-07-31, determine rates for those projects, and execute a sample two‑line totals using the calculated rates (12h @85.0 and 8h @75.0, HST 0.13). Modify CONS001 email to sarah.thompson+billing@consultingpro.ca and confirm it. Change PUB002 AP email to ap@northernlights-edu.ca and verify it. Generate the A/R aging report for period label 2024-07."
        ),
        actions=[
            Action(name="FetchTimeEntries", kwargs={"project_id_list": ["PROJ001", "PROJ003"], "period_start": "2024-07-01", "period_end": "2024-07-31"}),
            Action(name="ResolveHourlyRates", kwargs={"project_id_list": ["PROJ001", "PROJ003"]}),
            Action(name="CalculateInvoiceTotals", kwargs={"lines": [{"hours": 12, "rate": 85.0}, {"hours": 8, "rate": 75.0}], "hst_rate": 0.13}),

            Action(name="UpdateConsultantContact", kwargs={"consultant_id": "CONS001", "email": "sarah.thompson+billing@consultingpro.ca"}),
            Action(name="GetConsultantProfile", kwargs={"consultant_id": "CONS001"}),

            Action(name="UpdatePublisherContact", kwargs={"publisher_id": "PUB002", "contact_email": "ap@northernlights-edu.ca"}),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB002"}),

            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-07"}),
        ],
        outputs=[
            "July context fetched/resolved; sample totals computed; CONS001 email updated & read; "
            "PUB002 AP updated & read; AR_Aging_2024-07 exported."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_004",
        instruction=(
            "Facilitate the setup of PUB010 along with its project, then conduct an August‑2024 micro‑billing evaluation. End result: publisher_id 'PUB010' is established with exactly name 'Maple Leaf Educational', address '100 Bloor St W, Montreal, ON', contact_email 'ap@mapleleafedu.ca', gst_number 'GST-999-010' and can be accessed; project_id 'PROJ990' is created under 'PUB010' with isbn '978-1-9876-5432-1', project_title 'Intro Statistics, 5e', default_hourly_rate 105.0, override_hourly_rate None, account_code 'STAT-5E-2025', is_active True and can be accessed; you calculate the rate for ['PROJ990'] and determine a single‑line sample total (4 hours at 105.0 with hst_rate 0.13); and the A/R aging for period_label '2024-08' is generated. Confirm each modification through a subsequent read."
        ),
        actions=[
            Action(name="CreatePublisher", kwargs={
                "publisher_id": "PUB010",
                "name": "Maple Leaf Educational",
                "address": "100 Bloor St W, Montreal, ON",
                "contact_email": "ap@mapleleafedu.ca",
                "gst_number": "GST-999-010"
            }),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB010"}),
            Action(name="CreateProject", kwargs={
                "project_id": "PROJ990",
                "publisher_id": "PUB010",
                "isbn": "978-1-9876-5432-1",
                "project_title": "Intro Statistics, 5e",
                "default_hourly_rate": 105.0,
                "override_hourly_rate": None,
                "account_code": "STAT-5E-2025",
                "is_active": True
            }),
            Action(name="GetProjectDetails", kwargs={"project_id": "PROJ990"}),
            Action(name="ResolveHourlyRates", kwargs={"project_id_list": ["PROJ990"]}),
            Action(name="CalculateInvoiceTotals", kwargs={
                "lines": [{"hours": 4, "rate": 105.0}],
                "hst_rate": 0.13
            }),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-08"}),
        ],
        outputs=[
            "PUB010 created & read; PROJ990 created & read; PROJ990 rate resolved; "
            "4h micro‑total computed; AR_Aging_2024-08 exported."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_005",
        instruction=(
            "Handle a refresh of the October‑2024 A/R context and validate key contacts. End state: open invoices (status 'open') have been assessed; A/R aging exports are available for period labels '2024-10' and '2024-09'; the contact_email for publisher_id 'PUB004' is set to 'ap@bluepeakpublishing.ca' and is accessible; the address for consultant_id 'CONS001' is verified by entering '1234 Oak Street, Montreal, ON M5V 3A8' and confirming it; 12‑month collection KPIs are calculated (window_months 12); projects are compiled and the details of project_id 'PROJ004' are accessible; and, to quickly check risk, assess days outstanding using invoice_number '2024-010' with due_date '2024-10-31' and today '2024-11-15' (15 days) and categorize that value. Every write action must be validated through a subsequent read using only the available domain tools."
        ),
        actions=[
            Action(name="FetchInvoices", kwargs={"status": "open"}),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-10"}),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-09"}),

            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB004"}),
            Action(name="UpdatePublisherContact", kwargs={"publisher_id": "PUB004", "contact_email": "ap@bluepeakpublishing.ca"}),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB004"}),

            Action(name="GetConsultantProfile", kwargs={"consultant_id": "CONS001"}),
            Action(name="UpdateConsultantContact", kwargs={"consultant_id": "CONS001", "address": "1234 Oak Street, Montreal, ON M5V 3A8"}),
            Action(name="GetConsultantProfile", kwargs={"consultant_id": "CONS001"}),

            Action(name="ComputeCollectionKpis", kwargs={"window_months": 12}),

            Action(name="ComputeDaysOutstanding", kwargs={
                "invoices": [{"invoice_number": "2024-010", "period_end": "2024-10-31"}],
                "today": "2024-11-15"
            }),
            Action(name="CategorizeAging", kwargs={
                "aging": [{"invoice_number": "2024-010", "days_outstanding": 15}]
            }),

            Action(name="FetchProjects", kwargs={}),
            Action(name="GetProjectDetails", kwargs={"project_id": "PROJ004"}),
        ],
        outputs=[
            "Open invoices listed; AR_Aging_2024-10 and AR_Aging_2024-09 exported; PUB004 AP updated & read; "
            "CONS001 address confirmed & read; KPIs computed; 15 days categorized; projects listed; PROJ004 read."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_006",
        instruction=(
            "Establish a new publisher_id 'PUB013' under the name 'Maple STEM Press' and coordinate a billing verification for September‑2024. End state: 'PUB013' has been added with the name 'Maple STEM Press' and is accessible; publisher_id 'PUB002' can be accessed; open invoices (status 'open') are checked and 12‑month KPIs are calculated; resolve rates for ['PROJ003'] and compute sample totals (6h @75.0 and 2h @75.0 with hst_rate 0.13); export the A/R aging for '2024-09'. Ensure each write action is confirmed by a subsequent read."
        ),
        actions=[
            Action(name="CreatePublisher", kwargs={
                "publisher_id": "PUB013",
                "name": "Maple STEM Press"
            }),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB013"}),

            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB002"}),

            Action(name="FetchInvoices", kwargs={"status": "open"}),
            Action(name="ComputeCollectionKpis", kwargs={"window_months": 12}),

            Action(name="ResolveHourlyRates", kwargs={"project_id_list": ["PROJ003"]}),
            Action(name="CalculateInvoiceTotals", kwargs={
                "lines": [{"hours": 6, "rate": 75.0}, {"hours": 2, "rate": 75.0}],
                "hst_rate": 0.13
            }),

            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-09"}),
        ],
        outputs=[
            "PUB013 created & read; PUB002 read; open invoices reviewed; KPIs computed; rates resolved; sample totals; AR_Aging_2024-09 exported."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_007",
        instruction=(
            "Handle the organization of November 2024 contact information and calculate a confirmation total with context. End state: publisher_id 'PUB005' contact_email is updated to 'ap@westwoodpress.ca' and is readable; consultant_id 'CONS001' email is updated to 'sarah.thompson@consultingpro.ca' and is readable; review open invoices (status 'open') and compute 12-month KPIs; resolve rates for ['PROJ003'] and calculate a sample total (2h @75.0 with hst_rate 0.13); export A/R aging '2024-11'. Each write is verified through a subsequent read."
        ),
        actions=[
            Action(name="UpdatePublisherContact", kwargs={
                "publisher_id": "PUB005",
                "contact_email": "ap@westwoodpress.ca"
            }),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB005"}),

            Action(name="UpdateConsultantContact", kwargs={
                "consultant_id": "CONS001",
                "email": "sarah.thompson@consultingpro.ca"
            }),
            Action(name="GetConsultantProfile", kwargs={"consultant_id": "CONS001"}),

            Action(name="FetchInvoices", kwargs={"status": "open"}),
            Action(name="ComputeCollectionKpis", kwargs={"window_months": 12}),

            Action(name="ResolveHourlyRates", kwargs={"project_id_list": ["PROJ003"]}),
            Action(name="CalculateInvoiceTotals", kwargs={
                "lines": [{"hours": 2, "rate": 75.0}],
                "hst_rate": 0.13
            }),

            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-11"}),
        ],
        outputs=[
            "PUB005 AP updated & read; CONS001 email updated & read; open invoices reviewed; KPIs computed; rate resolved; sample total; aging exported."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_008",
        instruction=(
            "Establish a November 2024 readiness context for publisher_id 'PUB003'. End state: ensure project_id 'PROJ999' exists under 'PUB003' with isbn '978-1-3100-0007-3', project_title 'Literature Survey, 1e', default_hourly_rate 91.0 and is visible; 'PUB003' is readable; open invoices (status 'open') are reviewed and 12-month collection KPIs are available; resolve rates for ['PROJ999','PROJ003'] and calculate sample totals (1h @91.0 and 2h @91.0 with hst_rate 0.13); an A/R aging PDF exists for period label '2024-11'; list projects and ensure details for 'PROJ003' are visible;"
        ),
        actions=[
            Action(name="CreateProject", kwargs={
                "project_id": "PROJ999",
                "publisher_id": "PUB003",
                "isbn": "978-1-3100-0007-3",
                "project_title": "Literature Survey, 1e",
                "default_hourly_rate": 91.0
            }),
            Action(name="GetProjectDetails", kwargs={"project_id": "PROJ999"}),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB003"}),
            Action(name="FetchInvoices", kwargs={"status": "open"}),
            Action(name="ComputeCollectionKpis", kwargs={"window_months": 12}),
            Action(name="ResolveHourlyRates", kwargs={"project_id_list": ["PROJ999", "PROJ003"]}),
            Action(name="CalculateInvoiceTotals", kwargs={
                "lines": [{"hours": 1, "rate": 91.0}, {"hours": 2, "rate": 91.0}],
                "hst_rate": 0.13
            }),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-11"}),
            Action(name="FetchProjects", kwargs={}),
            Action(name="GetProjectDetails", kwargs={"project_id": "PROJ003"}),
            Action(name="GetInvoiceDetails", kwargs={"invoice_number": "2024-010"}),
        ],
        outputs=[
            "PROJ999 created & read; PUB003 read; open invoices reviewed; KPIs computed; rates resolved; sample totals; "
            "AR_Aging_2024-11 exported; projects listed; PROJ003 read; invoice 2024-010 read;"
        ],
    ),    
    Task(
        annotator="A",
        user_id="ca_v4_009",
        instruction=(
            "Handle the normalization of contact data and generate a September‑2024 A/R snapshot for validation. End state: publisher_id 'PUB001' contact_email must match 'accounts@nelson-edu.ca' and be shown; consultant_id 'CONS001' email should be 'sarah.thompson@consultingpro.ca' and be shown; review open invoices (status 'open') and ensure 12‑month KPIs are accessible; rates should be calculated for ['PROJ001'] and a sample total is to be determined (6h @85.0 with hst_rate 0.13); A/R aging PDFs must be created for period labels '2024-09' and '2024-08'; ensure project listings and visibility of details for 'PROJ001'; make representative open invoices '2024-009' and '2024-021' readable, and an audit event 'reviewed' must be logged for '2024-009' and documented."
        ),
        actions=[
            Action(name="UpdatePublisherContact", kwargs={
                "publisher_id": "PUB001",
                "contact_email": "accounts@nelson-edu.ca"
            }),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB001"}),

            Action(name="UpdateConsultantContact", kwargs={
                "consultant_id": "CONS001",
                "email": "sarah.thompson@consultingpro.ca"
            }),
            Action(name="GetConsultantProfile", kwargs={"consultant_id": "CONS001"}),

            Action(name="FetchInvoices", kwargs={"status": "open"}),
            Action(name="ComputeCollectionKpis", kwargs={"window_months": 12}),

            Action(name="ResolveHourlyRates", kwargs={"project_id_list": ["PROJ001"]}),
            Action(name="CalculateInvoiceTotals", kwargs={
                "lines": [{"hours": 6, "rate": 85.0}],
                "hst_rate": 0.13
            }),

            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-09"}),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-08"}),

            Action(name="FetchProjects", kwargs={}),
            Action(name="GetProjectDetails", kwargs={"project_id": "PROJ001"}),

            Action(name="GetInvoiceDetails", kwargs={"invoice_number": "2024-009"}),
            Action(name="RecordInvoiceAudit", kwargs={
                "invoice_number": "2024-009",
                "event_type": "reviewed"
            }),
            Action(name="ListInvoiceAudit", kwargs={"invoice_number": "2024-009"}),
            Action(name="GetInvoiceDetails", kwargs={"invoice_number": "2024-021"}),
        ],
        outputs=[
            "PUB001 AP updated & read; CONS001 email updated & read; open invoices reviewed; KPIs computed; "
            "rate resolved; total computed; AR_Aging_2024-09 and AR_Aging_2024-08 exported; projects listed; PROJ001 read; "
            "invoices 2024-009 and 2024-021 read; audit for 2024-009 recorded & listed."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_010",
        instruction=(
            "Coordinate the updating of contact information and verify a September‑2024 total with context. End state: publisher_id 'PUB003' contact_email needs to be updated to 'accounts@canopypress.ca' and be viewable; consultant_id 'CONS001' phone should change to '+1-416-555-0199' and be viewable; open invoices (status 'open') are to be reviewed and 12‑month KPIs calculated; ensure rates are adjusted for ['PROJ001','PROJ003'] and sample totals are calculated (3h @85.0 and 2h @75.0 with hst_rate 0.13); perform export of A/R aging '2024-09'. Every write action must be confirmed with a subsequent read."
        ),
        actions=[
            Action(name="UpdatePublisherContact", kwargs={
                "publisher_id": "PUB003",
                "contact_email": "accounts@canopypress.ca"
            }),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB003"}),

            Action(name="UpdateConsultantContact", kwargs={
                "consultant_id": "CONS001",
                "phone": "+1-416-555-0199"
            }),
            Action(name="GetConsultantProfile", kwargs={"consultant_id": "CONS001"}),

            Action(name="FetchInvoices", kwargs={"status": "open"}),
            Action(name="ComputeCollectionKpis", kwargs={"window_months": 12}),

            Action(name="ResolveHourlyRates", kwargs={"project_id_list": ["PROJ001", "PROJ003"]}),
            Action(name="CalculateInvoiceTotals", kwargs={
                "lines": [{"hours": 3, "rate": 85.0}, {"hours": 2, "rate": 75.0}],
                "hst_rate": 0.13
            }),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-09"}),
        ],
        outputs=[
            "PUB003 AP updated & read; CONS001 phone updated & read; open invoices reviewed; KPIs computed; rates resolved; totals computed; aging exported."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_011",
        instruction=(
            "Introduce a focused writing project and coordinate the October‑2024 reporting alignment for publisher_id 'PUB004'. Final outcome: project_id 'PROJ1011' is created with isbn '978-1-3100-1011-0', project_title 'Writing Workshop, 1e', default_hourly_rate 94.0, and is accessible; 'PUB004' remains viewable; rates for ['PROJ1011','PROJ001'] are resolved and a sample total is calculated (2h @94.0 and 3h @85.0 with hst_rate 0.13); open invoices are inspected and 12‑month KPIs are accessible; the A/R aging PDF is available for '2024-10' and a snapshot is recorded for '2024-10-31' referencing that PDF."
        ),
        actions=[
            Action(name="CreateProject", kwargs={
                "project_id": "PROJ1011",
                "publisher_id": "PUB004",
                "isbn": "978-1-3100-1011-0",
                "project_title": "Writing Workshop, 1e",
                "default_hourly_rate": 94.0
            }),
            Action(name="GetProjectDetails", kwargs={"project_id": "PROJ1011"}),

            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB004"}),

            Action(name="ResolveHourlyRates", kwargs={"project_id_list": ["PROJ1011", "PROJ001"]}),
            Action(name="CalculateInvoiceTotals", kwargs={"lines": [{"hours": 2, "rate": 94.0}, {"hours": 3, "rate": 85.0}], "hst_rate": 0.13}),

            Action(name="FetchInvoices", kwargs={"status": "open"}),
            Action(name="ComputeCollectionKpis", kwargs={"window_months": 12}),

            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-10"}),
            Action(name="InsertDashboardSnapshot", kwargs={"snapshot_date": "2024-10-31", "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-10.pdf"}),
            Action(name="GetDashboardSnapshotDetails", kwargs={"snapshot_date": "2024-10-31"}),
        ],
        outputs=[
            "PROJ1011 created & read; PUB004 read; rates resolved; totals computed; open invoices reviewed; KPIs computed; "
            "AR_Aging_2024-10 exported; snapshot saved & read."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_012",
        instruction=(
            "Initiate publisher_id 'PUB021' labeled 'Pioneer Learning Press' and prepare an August‑2024 snapshot. Final state: 'PUB021' is created and visible; a minor project 'PROJ1012' under 'PUB021' is established with isbn '978-1-3100-1012-7', project_title 'Civics Primer, 1e', default_hourly_rate 86.0, and is accessible; sample totals are calculated (2h @86.0 with hst_rate 0.13); the A/R aging PDF is available for '2024-08' and a dashboard snapshot is retained for '2024-08-31' referencing that PDF."
        ),
        actions=[
            Action(name="CreatePublisher", kwargs={"publisher_id": "PUB021", "name": "Pioneer Learning Press"}),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB021"}),

            Action(name="CreateProject", kwargs={
                "project_id": "PROJ1012",
                "publisher_id": "PUB021",
                "isbn": "978-1-3100-1012-7",
                "project_title": "Civics Primer, 1e",
                "default_hourly_rate": 86.0
            }),
            Action(name="GetProjectDetails", kwargs={"project_id": "PROJ1012"}),

            Action(name="CalculateInvoiceTotals", kwargs={"lines": [{"hours": 2, "rate": 86.0}], "hst_rate": 0.13}),

            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-08"}),
            Action(name="InsertDashboardSnapshot", kwargs={"snapshot_date": "2024-08-31", "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-08.pdf"}),
            Action(name="GetDashboardSnapshotDetails", kwargs={"snapshot_date": "2024-08-31"}),
        ],
        outputs=[
            "PUB021 created & read; PROJ1012 created & read; sample total computed; AR_Aging_2024-08 exported; snapshot saved & read."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_013",
        instruction=(
            "Handle the addition of a STEM project and evaluate the risk for November‑2024. End state: project_id 'PROJ1013' is found under 'PUB003', assigned the isbn '978-1-3100-1013-4', with the project_title 'Applied Physics, 1e', a default_hourly_rate of 98.0, and is made visible; open invoices are checked and 12‑month KPIs are accessible; a sample total calculation is done (4h @98.0 with hst_rate 0.13); in terms of risk, calculate the days outstanding for invoice '2024-010' as of '2024-11-15' (15 days) and categorize it."
        ),
        actions=[
            Action(name="CreateProject", kwargs={
                "project_id": "PROJ1013",
                "publisher_id": "PUB003",
                "isbn": "978-1-3100-1013-4",
                "project_title": "Applied Physics, 1e",
                "default_hourly_rate": 98.0
            }),
            Action(name="GetProjectDetails", kwargs={"project_id": "PROJ1013"}),

            Action(name="FetchInvoices", kwargs={"status": "open"}),
            Action(name="ComputeCollectionKpis", kwargs={"window_months": 12}),

            Action(name="CalculateInvoiceTotals", kwargs={"lines": [{"hours": 4, "rate": 98.0}], "hst_rate": 0.13}),

            Action(name="ComputeDaysOutstanding", kwargs={"invoices": [{"invoice_number": "2024-010", "period_end": "2024-10-31"}], "today": "2024-11-15"}),
            Action(name="CategorizeAging", kwargs={"aging": [{"invoice_number": "2024-010", "days_outstanding": 15}]}),
        ],
        outputs=[
            "PROJ1013 created & read; open invoices reviewed; KPIs computed; sample total; 15 days categorized for 2024-010."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_014",
        instruction=(
            "Coordinate the registration of project_id 'PROJ1015' for 'PUB005' and perform an October‑2024 sample computation with context. End state: 'PROJ1015' is present, featuring isbn '978-1-3100-1015-8', project_title 'Canadian Geography, 2e', a default_hourly_rate of 90.0, and is visible; 'PUB005' can be read; compute a sample total (4h @90.0 with hst_rate 0.13); ensure the A/R aging PDF exists for '2024-10'."
        ),
        actions=[
            Action(name="CreateProject", kwargs={
                "project_id": "PROJ1015",
                "publisher_id": "PUB005",
                "isbn": "978-1-3100-1015-8",
                "project_title": "Canadian Geography, 2e",
                "default_hourly_rate": 90.0
            }),
            Action(name="GetProjectDetails", kwargs={"project_id": "PROJ1015"}),

            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB005"}),

            Action(name="CalculateInvoiceTotals", kwargs={"lines": [{"hours": 4, "rate": 90.0}], "hst_rate": 0.13}),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-10"}),
        ],
        outputs=[
            "PROJ1015 created & read; PUB005 read; sample total; AR_Aging_2024-10 exported."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_015",
        instruction=(
            "Handle August‑2024 contact data management and KPI verification. Final goal: 'PUB001' contact_email is set to 'ap@nelson-edu.ca' and displayed; 'CONS001' address is '1234 Oak Street, Montreal, ON M5V 3A8' and displayed; assess open invoices and ensure 12‑month KPIs are accessible; calculate a sample total (3h @85.0 with hst_rate 0.13); confirm the presence of the A/R aging PDF for '2024-08'."
        ),
        actions=[
            Action(name="UpdatePublisherContact", kwargs={"publisher_id": "PUB001", "contact_email": "ap@nelson-edu.ca"}),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB001"}),

            Action(name="UpdateConsultantContact", kwargs={"consultant_id": "CONS001", "address": "1234 Oak Street, Montreal, ON M5V 3A8"}),
            Action(name="GetConsultantProfile", kwargs={"consultant_id": "CONS001"}),

            Action(name="FetchInvoices", kwargs={"status": "open"}),
            Action(name="ComputeCollectionKpis", kwargs={"window_months": 12}),

            Action(name="CalculateInvoiceTotals", kwargs={"lines": [{"hours": 3, "rate": 85.0}], "hst_rate": 0.13}),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-08"}),
        ],
        outputs=[
            "PUB001 AP updated & read; CONS001 address updated & read; open invoices reviewed; KPIs computed; sample total; AR_Aging_2024-08 exported."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_016",
        instruction=(
            "Access publisher_id 'PUB024' under the name 'Aurora Study House' and synchronize reporting for September‑2024. Final goal: Ensure 'PUB024' is present and displayed; examine open invoices; verify availability of 12-month KPIs; confirm the A/R aging PDF for '2024-09' exists and preserve a snapshot for '2024-09-30' in relation to that PDF; compute a sample total (2h @85.0 and 2h @75.0 with hst_rate 0.13) using rates for ['PROJ001','PROJ003']."
        ),
        actions=[
            Action(name="CreatePublisher", kwargs={"publisher_id": "PUB024", "name": "Aurora Study House"}),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB024"}),

            Action(name="FetchInvoices", kwargs={"status": "open"}),
            Action(name="ComputeCollectionKpis", kwargs={"window_months": 12}),

            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-09"}),
            Action(name="InsertDashboardSnapshot", kwargs={"snapshot_date": "2024-09-30", "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-09.pdf"}),
            Action(name="GetDashboardSnapshotDetails", kwargs={"snapshot_date": "2024-09-30"}),

            Action(name="ResolveHourlyRates", kwargs={"project_id_list": ["PROJ001", "PROJ003"]}),
            Action(name="CalculateInvoiceTotals", kwargs={"lines": [{"hours": 2, "rate": 85.0}, {"hours": 2, "rate": 75.0}], "hst_rate": 0.13}),
        ],
        outputs=[
            "PUB024 created & read; open invoices reviewed; KPIs computed; AR_Aging_2024-09 exported; snapshot saved & read; rates resolved; totals computed."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_017",
        instruction=(
            "Handle the update of contact details and confirm August‑2024 totals. End state: 'CONS001' phone matches '+1-647-555-2244' and is visible; 'PUB004' remains readable; rates correctly resolve for ['PROJ001'] and a sample total is computed (4h @85.0 with hst_rate 0.13); the A/R aging PDF is generated for '2024-08'."
        ),
        actions=[
            Action(name="UpdateConsultantContact", kwargs={"consultant_id": "CONS001", "phone": "+1-647-555-2244"}),
            Action(name="GetConsultantProfile", kwargs={"consultant_id": "CONS001"}),

            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB004"}),

            Action(name="ResolveHourlyRates", kwargs={"project_id_list": ["PROJ001"]}),
            Action(name="CalculateInvoiceTotals", kwargs={"lines": [{"hours": 4, "rate": 85.0}], "hst_rate": 0.13}),

            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-08"}),
        ],
        outputs=[
            "CONS001 phone updated & read; PUB004 read; rate resolved; total computed; AR_Aging_2024-08 exported."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_018",
        instruction=(
            "Coordinate the creation of publisher_id 'PUB025' named 'Lakeside Scholastic' and complete an August snapshot. End state: 'PUB025' is established and visible; the A/R aging PDF exists for '2024-08' and a dashboard snapshot is saved for '2024-08-31' referencing that PDF; a sample total is calculated (2h @85.0 with hst_rate 0.13) using rates for ['PROJ001']."
        ),
        actions=[
            Action(name="CreatePublisher", kwargs={"publisher_id": "PUB025", "name": "Lakeside Scholastic"}),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB025"}),

            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-08"}),
            Action(name="InsertDashboardSnapshot", kwargs={"snapshot_date": "2024-08-31", "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-08.pdf"}),
            Action(name="GetDashboardSnapshotDetails", kwargs={"snapshot_date": "2024-08-31"}),

            Action(name="ResolveHourlyRates", kwargs={"project_id_list": ["PROJ001"]}),
            Action(name="CalculateInvoiceTotals", kwargs={"lines": [{"hours": 2, "rate": 85.0}], "hst_rate": 0.13}),
        ],
        outputs=[
            "PUB025 created & read; AR_Aging_2024-08 exported; snapshot saved & read; rate resolved; total computed."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_019",
        instruction=(
            "Initiate the creation of project_id 'PROJ1018' for 'PUB004' to compute a November 2024 sample. End state: 'PROJ1018' is established with isbn '978-1-3100-1018-9', project_title 'Intro Data Science, 2e', default_hourly_rate 105.0 and visible; calculate a sample total (4h @105.0 with hst_rate 0.13); ensure the A/R aging PDF for '2024-11' is generated."
        ),
        actions=[
            Action(name="CreateProject", kwargs={
                "project_id": "PROJ1018",
                "publisher_id": "PUB004",
                "isbn": "978-1-3100-1018-9",
                "project_title": "Intro Data Science, 2e",
                "default_hourly_rate": 105.0
            }),
            Action(name="GetProjectDetails", kwargs={"project_id": "PROJ1018"}),

            Action(name="CalculateInvoiceTotals", kwargs={"lines": [{"hours": 4, "rate": 105.0}], "hst_rate": 0.13}),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-11"}),
        ],
        outputs=[
            "PROJ1018 created & read; sample total; AR_Aging_2024-11 exported."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_020",
        instruction=(
            "Modify the contacts and verify a September 2024 total. End state: 'PUB003' contact_email is set to 'accounts@canopypress.ca' and visible; 'CONS001' phone is updated to '+1-416-555-0199' and visible; resolve rates for ['PROJ001','PROJ003'] and calculate sample totals (3h @85.0 and 2h @75.0 with hst_rate 0.13); confirm the A/R aging PDF exists for '2024-09'."
        ),
        actions=[
            Action(name="UpdatePublisherContact", kwargs={"publisher_id": "PUB003", "contact_email": "accounts@canopypress.ca"}),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB003"}),

            Action(name="UpdateConsultantContact", kwargs={"consultant_id": "CONS001", "phone": "+1-416-555-0199"}),
            Action(name="GetConsultantProfile", kwargs={"consultant_id": "CONS001"}),

            Action(name="ResolveHourlyRates", kwargs={"project_id_list": ["PROJ001", "PROJ003"]}),
            Action(name="CalculateInvoiceTotals", kwargs={"lines": [{"hours": 3, "rate": 85.0}, {"hours": 2, "rate": 75.0}], "hst_rate": 0.13}),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-09"}),
        ],
        outputs=[
            "PUB003 AP updated & read; CONS001 phone updated & read; rates resolved; totals computed; AR_Aging_2024-09 exported."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_021",
        instruction=(
            "Handle the setup of publisher_id 'PUB027', named 'North Coast Education', and achieve completion of an August snapshot. Final condition: 'PUB027' is created and accessible; the A/R aging PDF is available for '2024-08', and a snapshot is captured for '2024-08-31' referencing that PDF; a sample total is calculated (5h @85.0 with hst_rate 0.13) using rates for ['PROJ001']."
        ),
        actions=[
            Action(name="CreatePublisher", kwargs={"publisher_id": "PUB027", "name": "North Coast Education"}),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB027"}),

            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-08"}),
            Action(name="InsertDashboardSnapshot", kwargs={"snapshot_date": "2024-08-31", "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-08.pdf"}),
            Action(name="GetDashboardSnapshotDetails", kwargs={"snapshot_date": "2024-08-31"}),

            Action(name="ResolveHourlyRates", kwargs={"project_id_list": ["PROJ001"]}),
            Action(name="CalculateInvoiceTotals", kwargs={"lines": [{"hours": 5, "rate": 85.0}], "hst_rate": 0.13}),
        ],
        outputs=[
            "PUB027 created & read; AR_Aging_2024-08 exported; snapshot saved & read; rate resolved; total computed."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_022",
        instruction=(
            "Coordinate the addition of project_id 'PROJ1019' for 'PUB001' and determine a July‑2024 confirmation. Final condition: 'PROJ1019' is established with isbn '978-1-3100-1019-6', project_title 'Intro Chemistry, 2e', default_hourly_rate 85.0 and is visible; a sample total is calculated (4h @85.0 with hst_rate 0.13); the A/R aging PDF is available for '2024-07'."
        ),
        actions=[
            Action(name="CreateProject", kwargs={
                "project_id": "PROJ1019",
                "publisher_id": "PUB001",
                "isbn": "978-1-3100-1019-6",
                "project_title": "Intro Chemistry, 2e",
                "default_hourly_rate": 85.0
            }),
            Action(name="GetProjectDetails", kwargs={"project_id": "PROJ1019"}),

            Action(name="CalculateInvoiceTotals", kwargs={"lines": [{"hours": 4, "rate": 85.0}], "hst_rate": 0.13}),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-07"}),
        ],
        outputs=[
            "PROJ1019 created & read; sample total; AR_Aging_2024-07 exported."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_023",
        instruction=(
            "Handle the normalization of contacts and creation of a July‑2024 risk overview. End state: publisher_id 'PUB002' contact_email is 'ap@northernlights-edu.ca' and remains visible; consultant_id 'CONS001' gst_number is '123456789RT0001' and is visible; open invoices should be reviewed, and 12‑month KPIs are to be available; ensure the A/R aging PDF is present for '2024-07'; compute days outstanding for '2024-023' as of '2024-08-01' (17 days) and categorize them; list projects and make 'PROJ003' details visible."
        ),
        actions=[
            Action(name="UpdatePublisherContact", kwargs={"publisher_id": "PUB002", "contact_email": "ap@northernlights-edu.ca"}),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB002"}),

            Action(name="UpdateConsultantContact", kwargs={"consultant_id": "CONS001", "gst_number": "123456789RT0001"}),
            Action(name="GetConsultantProfile", kwargs={"consultant_id": "CONS001"}),

            Action(name="FetchInvoices", kwargs={"status": "open"}),
            Action(name="ComputeCollectionKpis", kwargs={"window_months": 12}),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-07"}),

            Action(name="ComputeDaysOutstanding", kwargs={
                "invoices": [{"invoice_number": "2024-023", "period_end": "2024-07-15"}],
                "today": "2024-08-01"
            }),
            Action(name="CategorizeAging", kwargs={"aging": [{"invoice_number": "2024-023", "days_outstanding": 17}]}),

            Action(name="FetchProjects", kwargs={}),
            Action(name="GetProjectDetails", kwargs={"project_id": "PROJ003"})
        ],
        outputs=[
            "PUB002 AP updated & read; CONS001 GST updated & read; open invoices reviewed; KPIs computed; AR_Aging_2024-07 exported; "
            "17 days categorized for 2024-023; projects listed; PROJ003 read."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_024",
        instruction=(
            "Coordinate the alignment of rates and contacts for a September‑2024 confirmation. End state: consultant_id 'CONS001' email is 'accounts+ar@consultingpro.ca' and remains visible; publisher_id 'PUB001' contact_email is 'ap@nelson-edu.ca' and remains visible; resolve rates for ['PROJ001', 'PROJ003'] and compute a sample total (2h @85.0 and 2h @75.0 with hst_rate 0.13); review open invoices; ensure 12‑month KPIs are available; verify that the A/R aging PDF exists for '2024-09'."
        ),
        actions=[
            Action(name="UpdateConsultantContact", kwargs={"consultant_id": "CONS001", "email": "accounts+ar@consultingpro.ca"}),
            Action(name="GetConsultantProfile", kwargs={"consultant_id": "CONS001"}),

            Action(name="UpdatePublisherContact", kwargs={"publisher_id": "PUB001", "contact_email": "ap@nelson-edu.ca"}),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB001"}),

            Action(name="ResolveHourlyRates", kwargs={"project_id_list": ["PROJ001", "PROJ003"]}),
            Action(name="CalculateInvoiceTotals", kwargs={"lines": [{"hours": 2, "rate": 85.0}, {"hours": 2, "rate": 75.0}], "hst_rate": 0.13}),

            Action(name="FetchInvoices", kwargs={"status": "open"}),
            Action(name="ComputeCollectionKpis", kwargs={"window_months": 12}),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-09"})
        ],
        outputs=[
            "CONS001 email updated & read; PUB001 AP updated & read; rates resolved; totals computed; open invoices reviewed; KPIs computed; AR_Aging_2024-09 exported."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_025",
        instruction=(
            "Handle the refresh of AP contacts and ensure the October‑2024 A/R is verified for two publishers. Final state: 'PUB004' contact_email remains 'ap@bluepeakpublishing.ca' and is accessible; 'PUB005' contact_email remains 'ap@westwoodpress.ca' and is accessible; all open invoices are examined; 12‑month KPIs are retrievable; projects are enumerated and 'PROJ004' details are accessible; the A/R aging PDF for '2024-10' is present."
        ),
        actions=[
            Action(name="UpdatePublisherContact", kwargs={"publisher_id": "PUB004", "contact_email": "ap@bluepeakpublishing.ca"}),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB004"}),

            Action(name="UpdatePublisherContact", kwargs={"publisher_id": "PUB005", "contact_email": "ap@westwoodpress.ca"}),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB005"}),

            Action(name="FetchInvoices", kwargs={"status": "open"}),
            Action(name="ComputeCollectionKpis", kwargs={"window_months": 12}),

            Action(name="FetchProjects", kwargs={}),
            Action(name="GetProjectDetails", kwargs={"project_id": "PROJ004"}),

            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-10"})
        ],
        outputs=[
            "PUB004 and PUB005 AP updated & read; open invoices reviewed; KPIs computed; projects listed; PROJ004 read; AR_Aging_2024-10 exported."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_026",
        instruction=(
            "Coordinate the addition of a project for 'PUB001' and verify the total for August‑2024. Final state: project_id 'PROJ2035' persists with isbn '978-1-3100-2035-3', project_title 'Chemistry Workbook, 1e', default_hourly_rate 87.0 and is accessible; rates are clarified for ['PROJ2035','PROJ001'] and a sample total is calculated (2h @87.0 and 2h @85.0 with hst_rate 0.13); the A/R aging PDF for '2024-08' is present."
        ),
        actions=[
            Action(name="CreateProject", kwargs={
                "project_id": "PROJ2035",
                "publisher_id": "PUB001",
                "isbn": "978-1-3100-2035-3",
                "project_title": "Chemistry Workbook, 1e",
                "default_hourly_rate": 87.0
            }),
            Action(name="GetProjectDetails", kwargs={"project_id": "PROJ2035"}),

            Action(name="ResolveHourlyRates", kwargs={"project_id_list": ["PROJ2035", "PROJ001"]}),
            Action(name="CalculateInvoiceTotals", kwargs={"lines": [{"hours": 2, "rate": 87.0}, {"hours": 2, "rate": 85.0}], "hst_rate": 0.13}),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-08"})
        ],
        outputs=[
            "PROJ2035 created & read; rates resolved; totals computed; AR_Aging_2024-08 exported."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_027",
        instruction=(
            "Handle the updating of GST references and confirm the July 2024 A/R. Desired outcome: publisher_id 'PUB002' gst_number is 'GST-UPDATED-002' and displayed; consultant_id 'CONS001' gst_number is '123456789RT0001' and displayed; ensure open invoices have been reviewed; 12-month KPIs should be accessible; there should be an A/R aging PDF for '2024-07'."
        ),
        actions=[
            Action(name="UpdatePublisherContact", kwargs={"publisher_id": "PUB002", "gst_number": "GST-UPDATED-002"}),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB002"}),

            Action(name="UpdateConsultantContact", kwargs={"consultant_id": "CONS001", "gst_number": "123456789RT0001"}),
            Action(name="GetConsultantProfile", kwargs={"consultant_id": "CONS001"}),

            Action(name="FetchInvoices", kwargs={"status": "open"}),
            Action(name="ComputeCollectionKpis", kwargs={"window_months": 12}),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-07"})
        ],
        outputs=[
            "PUB002 GST updated & read; CONS001 GST updated & read; open invoices reviewed; KPIs computed; AR_Aging_2024-07 exported."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_028",
        instruction=(
            "Introduce publisher_id 'PUB035' with the name 'Northern Ridge Press' and set a baseline for July 2024. Desired outcome: 'PUB035' should be present and displayed; project_id 'PROJ2041' under 'PUB035' should exist with isbn '978-1-3100-2041-6', project_title 'Algebra Readiness, 1e', default_hourly_rate 93.0 and be displayed; calculate a sample total (2h @93.0 with hst_rate 0.13); ensure the A/R aging PDF for '2024-07' exists and a snapshot dated '2024-07-31' referencing that PDF is legible."
        ),
        actions=[
            Action(name="CreatePublisher", kwargs={"publisher_id": "PUB035", "name": "Northern Ridge Press"}),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB035"}),

            Action(name="CreateProject", kwargs={
                "project_id": "PROJ2041",
                "publisher_id": "PUB035",
                "isbn": "978-1-3100-2041-6",
                "project_title": "Algebra Readiness, 1e",
                "default_hourly_rate": 93.0
            }),
            Action(name="GetProjectDetails", kwargs={"project_id": "PROJ2041"}),

            Action(name="CalculateInvoiceTotals", kwargs={"lines": [{"hours": 2, "rate": 93.0}], "hst_rate": 0.13}),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-07"}),
            Action(name="InsertDashboardSnapshot", kwargs={"snapshot_date": "2024-07-31", "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-07.pdf"}),
            Action(name="GetDashboardSnapshotDetails", kwargs={"snapshot_date": "2024-07-31"})
        ],
        outputs=[
            "PUB035 created & read; PROJ2041 created & read; sample total; AR_Aging_2024-07 exported; snapshot saved & read."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_029",
        instruction=(
            "Handle registration of publisher_id 'PUB036' with the name 'Cedar Grove Texts' and organize a summary for October‑2024. End state: 'PUB036' is created and visible; open invoices are assessed; 12‑month KPIs are provided; the A/R aging PDF is available for '2024-10'; the contact for 'PUB003' matches 'ap@canopypress.ca' and is readable."
        ),
        actions=[
            Action(name="CreatePublisher", kwargs={"publisher_id": "PUB036", "name": "Cedar Grove Texts"}),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB036"}),

            Action(name="FetchInvoices", kwargs={"status": "open"}),
            Action(name="ComputeCollectionKpis", kwargs={"window_months": 12}),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-10"}),

            Action(name="UpdatePublisherContact", kwargs={"publisher_id": "PUB003", "contact_email": "ap@canopypress.ca"}),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB003"})
        ],
        outputs=[
            "PUB036 created & read; open invoices reviewed; KPIs computed; AR_Aging_2024-10 exported; PUB003 AP updated & read."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_030",
        instruction=(
            "Initialize project_id 'PROJ2044' for 'PUB004' and conduct a check for November‑2024. End state: 'PROJ2044' is established with isbn '978-1-3100-2044-7', project_title 'Media Literacy, 1e', default_hourly_rate 101.0 and visible; rates are resolved for ['PROJ2044'] and a sample total is calculated (3h @101.0 with hst_rate 0.13); the A/R aging PDF is present for '2024-11'; representative invoice '2024-010' is viewable."
        ),
        actions=[
            Action(name="CreateProject", kwargs={
                "project_id": "PROJ2044",
                "publisher_id": "PUB004",
                "isbn": "978-1-3100-2044-7",
                "project_title": "Media Literacy, 1e",
                "default_hourly_rate": 101.0
            }),
            Action(name="GetProjectDetails", kwargs={"project_id": "PROJ2044"}),

            Action(name="ResolveHourlyRates", kwargs={"project_id_list": ["PROJ2044"]}),
            Action(name="CalculateInvoiceTotals", kwargs={"lines": [{"hours": 3, "rate": 101.0}], "hst_rate": 0.13}),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-11"}),

            Action(name="GetInvoiceDetails", kwargs={"invoice_number": "2024-010"})
        ],
        outputs=[
            "PROJ2044 created & read; rate resolved; total computed; AR_Aging_2024-11 exported; invoice 2024-010 read."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_031",
        instruction=(
            "Initiate the addition of publisher_id 'PUB039' with the name 'Coastal Curriculum Press' and prepare a dual export. Desired outcome: 'PUB039' should be present and visible; the A/R aging PDFs for '2024-08' and '2024-09' are available; a dashboard snapshot dated '2024-08-31' related to the '2024-08' PDF is saved and can be viewed; open invoices undergo examination."
        ),
        actions=[
            Action(name="CreatePublisher", kwargs={"publisher_id": "PUB039", "name": "Coastal Curriculum Press"}),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB039"}),

            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-08"}),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-09"}),
            Action(name="InsertDashboardSnapshot", kwargs={"snapshot_date": "2024-08-31", "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-08.pdf"}),
            Action(name="GetDashboardSnapshotDetails", kwargs={"snapshot_date": "2024-08-31"}),

            Action(name="FetchInvoices", kwargs={"status": "open"})
        ],
        outputs=[
            "PUB039 created & read; AR_Aging_2024-08 and AR_Aging_2024-09 exported; snapshot 2024-08-31 saved & read; open invoices reviewed."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_032",
        instruction=(
            "Modify two AP contacts and verify KPIs for November‒2024. Desired outcome: 'PUB001' has contact_email set to 'accounts@nelson-edu.ca' and is visible; 'PUB003' has contact_email set to 'accounts@canopypress.ca' and is visible; open invoices undergo examination; 12‒month KPIs are accessible; the A/R aging PDF for '2024-11' is available."
        ),
        actions=[
            Action(name="UpdatePublisherContact", kwargs={"publisher_id": "PUB001", "contact_email": "accounts@nelson-edu.ca"}),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB001"}),

            Action(name="UpdatePublisherContact", kwargs={"publisher_id": "PUB003", "contact_email": "accounts@canopypress.ca"}),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB003"}),

            Action(name="FetchInvoices", kwargs={"status": "open"}),
            Action(name="ComputeCollectionKpis", kwargs={"window_months": 12}),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-11"})
        ],
        outputs=[
            "PUB001 and PUB003 AP updated & read; open invoices reviewed; KPIs computed; AR_Aging_2024-11 exported."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_033",
        instruction=(
            "Initiate the addition of publisher_id 'PUB041' with the name 'Evergreen Academic House' along with a writing project, then verify totals for October‑2024. Final state: 'PUB041' is present and viewable; 'PROJ2055' is established containing isbn '978-1-3100-2055-8', project_title 'Essay Skills, 1e', default_hourly_rate 91.0 and remains accessible; the rates are computed for ['PROJ2055','PROJ001'] and a sample total calculation (2h @91.0 and 1h @85.0 with hst_rate 0.13) is conducted; A/R aging PDF for '2024-10' is available."
        ),
        actions=[
            Action(name="CreatePublisher", kwargs={"publisher_id": "PUB041", "name": "Evergreen Academic House"}),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB041"}),

            Action(name="CreateProject", kwargs={
                "project_id": "PROJ2055",
                "publisher_id": "PUB041",
                "isbn": "978-1-3100-2055-8",
                "project_title": "Essay Skills, 1e",
                "default_hourly_rate": 91.0
            }),
            Action(name="GetProjectDetails", kwargs={"project_id": "PROJ2055"}),

            Action(name="ResolveHourlyRates", kwargs={"project_id_list": ["PROJ2055", "PROJ001"]}),
            Action(name="CalculateInvoiceTotals", kwargs={"lines": [{"hours": 2, "rate": 91.0}, {"hours": 1, "rate": 85.0}], "hst_rate": 0.13}),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-10"})
        ],
        outputs=[
            "PUB041 created & read; PROJ2055 created & read; rates resolved; totals computed; AR_Aging_2024-10 exported."
        ],
    ),




    Task(
        annotator="A",
        user_id="ca_v4_034",
        instruction=(
            "Create an invoice for October‑2024 for publisher_id 'PUB004'. Final state: invoice_number '2024-120' is generated covering period_start '2024-10-01' and period_end '2024-10-31' with precise totals for one line item (5h @102.0 with hst_rate 0.13) and is viewable; a line is added for project_id 'PROJ2024' involving isbn '978-1-3100-2024-6' (5h @102.0) and is available for listing; the A/R aging PDF for period '2024-10' is present. Apply pdf_path 'https://storage.example.com/invoices/2024/INV-2024-120.pdf'."
        ),
        actions=[
            Action(name="CalculateInvoiceTotals", kwargs={
                "lines": [{"hours": 5, "rate": 102.0}],
                "hst_rate": 0.13
            }),
            Action(name="InsertInvoice", kwargs={
                "invoice_number": "2024-120",
                "publisher_id": "PUB004",
                "invoice_date": "2024-10-31",
                "period_start": "2024-10-01",
                "period_end": "2024-10-31",
                "subtotal": 510.0,
                "hst_amount": 66.3,
                "total_due": 576.3,
                "pdf_path": "https://storage.example.com/invoices/2024/INV-2024-120.pdf"
            }),
            Action(name="GetInvoiceDetails", kwargs={"invoice_number": "2024-120"}),
            Action(name="InsertInvoiceLines", kwargs={
                "invoice_number": "2024-120",
                "lines": [{"project_id": "PROJ2024", "isbn": "978-1-3100-2024-6", "hours": 5, "rate": 102.0}]
            }),
            Action(name="ListInvoiceLines", kwargs={"invoice_number": "2024-120"}),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-10"}),
        ],
        outputs=[
            "Invoice 2024-120 inserted & read with correct totals; line inserted & listed; AR_Aging_2024-10 exported."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_035",
        instruction=(
            "Handle publisher_id 'PUB031' named 'Cardinal Academic' and initiate the registration of a November‑2024 package. End state: 'PUB031' is present and accessible; project_id 'PROJ2026A' is established under 'PUB031' with isbn '978-1-3100-2026-1', project_title 'Advanced Writing, 1e', default_hourly_rate 96.0 and is accessible; the rate is calculated for ['PROJ2026A'] and a sample total is determined (3h @96.0 with hst_rate 0.13); open invoices undergo review; 12‑month KPIs become available; the A/R aging PDF is generated for '2024-11' and a dashboard snapshot is saved for '2024-11-30' referencing 'https://storage.example.com/reports/AR_Aging_2024-11.pdf' and is accessible by id."
        ),
        actions=[
            Action(name="CreatePublisher", kwargs={"publisher_id": "PUB031", "name": "Cardinal Academic"}),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB031"}),
            Action(name="CreateProject", kwargs={
                "project_id": "PROJ2026A",
                "publisher_id": "PUB031",
                "isbn": "978-1-3100-2026-1",
                "project_title": "Advanced Writing, 1e",
                "default_hourly_rate": 96.0
            }),
            Action(name="GetProjectDetails", kwargs={"project_id": "PROJ2026A"}),
            Action(name="ResolveHourlyRates", kwargs={"project_id_list": ["PROJ2026A"]}),
            Action(name="CalculateInvoiceTotals", kwargs={"lines": [{"hours": 3, "rate": 96.0}], "hst_rate": 0.13}),
            Action(name="FetchInvoices", kwargs={"status": "open"}),
            Action(name="ComputeCollectionKpis", kwargs={"window_months": 12}),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-11"}),
            Action(name="InsertDashboardSnapshot", kwargs={
                "snapshot_date": "2024-11-30",
                "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-11.pdf"
            }),
            Action(name="GetDashboardSnapshotDetails", kwargs={"snapshot_id": 1}),
        ],
        outputs=[
            "PUB031 created & read; PROJ2026A created & read; rate resolved & sample total computed; "
            "open invoices reviewed; KPIs computed; AR_Aging_2024-11 exported; snapshot saved & read by id."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_036",
        instruction=(
            "Coordinate the registration of publisher_id 'PUB032' named 'Harborview Education' and manage the filing of summer A/R snapshots. End state: 'PUB032' is established and accessible; A/R aging PDFs are created for '2024-07' and '2024-06'; dashboard snapshots are saved for '2024-07-31' and '2024-06-30' referencing those PDFs and are accessible by id; open invoices are evaluated and 12‑month KPIs are available."
        ),
        actions=[
            Action(name="CreatePublisher", kwargs={"publisher_id": "PUB032", "name": "Harborview Education"}),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB032"}),
            Action(name="FetchInvoices", kwargs={"status": "open"}),
            Action(name="ComputeCollectionKpis", kwargs={"window_months": 12}),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-07"}),
            Action(name="InsertDashboardSnapshot", kwargs={
                "snapshot_date": "2024-07-31",
                "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-07.pdf"
            }),
            Action(name="GetDashboardSnapshotDetails", kwargs={"snapshot_id": 1}),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-06"}),
            Action(name="InsertDashboardSnapshot", kwargs={
                "snapshot_date": "2024-06-30",
                "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-06.pdf"
            }),
            Action(name="GetDashboardSnapshotDetails", kwargs={"snapshot_id": 2}),
        ],
        outputs=[
            "PUB032 created & read; open invoices reviewed; KPIs computed; AR_Aging_2024-07 and AR_Aging_2024-06 exported; both snapshots saved & read by id."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_037",
        instruction=(
            "Handle the creation of a January‑2025 risk classification for two invoices and verify the September A/R. End state: by '2025-01-15', compute days outstanding for '2024-026' with a period_end of '2024-06-30' and '2024-013' with a period_end of '2024-06-15' resulting in 199 and 214 days and categorize them; review open invoices for publisher_id 'PUB001'; ensure the A/R aging PDF is available for '2024-09'; log an audit event 'risk_categorized' for '2024-026' making it listable."
        ),
        actions=[
            Action(name="ComputeDaysOutstanding", kwargs={
                "invoices": [
                    {"invoice_number": "2024-026", "period_end": "2024-06-30"},
                    {"invoice_number": "2024-013", "period_end": "2024-06-15"}
                ],
                "today": "2025-01-15"
            }),
            Action(name="CategorizeAging", kwargs={
                "aging": [
                    {"invoice_number": "2024-026", "days_outstanding": 199},
                    {"invoice_number": "2024-013", "days_outstanding": 214}
                ]
            }),
            Action(name="FetchInvoices", kwargs={"status": "open", "publisher_id": "PUB001"}),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-09"}),
            Action(name="RecordInvoiceAudit", kwargs={"invoice_number": "2024-026", "event_type": "risk_categorized"}),
            Action(name="ListInvoiceAudit", kwargs={"invoice_number": "2024-026"}),
        ],
        outputs=[
            "Aging computed & categorized; PUB001 open invoices reviewed; AR_Aging_2024-09 exported; risk audit recorded & listed for 2024-026."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_038",
        instruction=(
            "Coordinate the generation of a September‑2024 invoice for publisher_id 'PUB003'. End state: ensure invoice_number '2024-131' exists for period_start '2024-09-01' and period_end '2024-09-30' with totals consisting of subtotal 388.0, hst_amount 50.44, total_due 438.44 using hst_rate 0.13, making it readable; input invoice lines for project_id 'PROJ2032' with isbn '978-1-3100-2032-2' (4h @97.0) ensuring they are listable; record a listable audit event 'generated'. Utilize pdf_path 'https://storage.example.com/invoices/2024/INV-2024-131.pdf'."
        ),
        actions=[
            Action(name="InsertInvoice", kwargs={
                "invoice_number": "2024-131",
                "publisher_id": "PUB003",
                "invoice_date": "2024-09-30",
                "period_start": "2024-09-01",
                "period_end": "2024-09-30",
                "subtotal": 388.0,
                "hst_amount": 50.44,
                "total_due": 438.44,
                "pdf_path": "https://storage.example.com/invoices/2024/INV-2024-131.pdf"
            }),
            Action(name="GetInvoiceDetails", kwargs={"invoice_number": "2024-131"}),
            Action(name="InsertInvoiceLines", kwargs={
                "invoice_number": "2024-131",
                "lines": [{"project_id": "PROJ2032", "isbn": "978-1-3100-2032-2", "hours": 4, "rate": 97.0}]
            }),
            Action(name="ListInvoiceLines", kwargs={"invoice_number": "2024-131"}),
            Action(name="RecordInvoiceAudit", kwargs={"invoice_number": "2024-131", "event_type": "generated"}),
            Action(name="ListInvoiceAudit", kwargs={"invoice_number": "2024-131"}),
        ],
        outputs=[
            "Invoice 2024-131 inserted & read; lines inserted & listed; audit recorded & listed."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_039",
        instruction=(
            "Handle the creation of publisher_id 'PUB033' with the name 'Prairie Learning Co.' and prepare a snapshot for September‑2024. Final outcome: 'PUB033' exists and is accessible; project_id 'PROJ2034' is in place, featuring isbn '978-1-3100-2034-6', project_title 'Prairie Math, 1e', default_hourly_rate 89.0 and is accessible; calculate a sample total (3h @89.0, hst_rate 0.13); inspect open invoices; confirm the A/R aging PDF is available for '2024-09'; store a dashboard snapshot for '2024-09-30' at 'https://storage.example.com/reports/AR_Aging_2024-09.pdf' ensuring it is accessible by id."
        ),
        actions=[
            Action(name="CreatePublisher", kwargs={"publisher_id": "PUB033", "name": "Prairie Learning Co."}),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB033"}),
            Action(name="CreateProject", kwargs={
                "project_id": "PROJ2034",
                "publisher_id": "PUB033",
                "isbn": "978-1-3100-2034-6",
                "project_title": "Prairie Math, 1e",
                "default_hourly_rate": 89.0
            }),
            Action(name="GetProjectDetails", kwargs={"project_id": "PROJ2034"}),
            Action(name="CalculateInvoiceTotals", kwargs={"lines": [{"hours": 3, "rate": 89.0}], "hst_rate": 0.13}),
            Action(name="FetchInvoices", kwargs={"status": "open"}),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-09"}),
            Action(name="InsertDashboardSnapshot", kwargs={
                "snapshot_date": "2024-09-30",
                "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-09.pdf"
            }),
            Action(name="GetDashboardSnapshotDetails", kwargs={"snapshot_id": 1}),
        ],
        outputs=[
            "PUB033 created & read; PROJ2034 created & read; sample total; open invoices reviewed; AR_Aging_2024-09 exported; snapshot saved & read by id."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_040",
        instruction=(
            "Confirm the August‑2024 context concerning 'PROJ003' and integrate necessary proofing. Final outcome: project listings are updated and 'PROJ003' details are retrievable; resolve rates for ['PROJ003'] and calculate a sample total (5h @75.0 with hst_rate 0.13); inspect open invoices and ensure 12‑month KPIs can be accessed; export the A/R aging for '2024-08' and secure a dashboard snapshot for '2024-08-31' at 'https://storage.example.com/reports/AR_Aging_2024-08.pdf', ensuring readability by id; log an audit event 'reviewed' for invoice '2024-009' and make it listable."
        ),
        actions=[
            Action(name="FetchProjects", kwargs={}),
            Action(name="GetProjectDetails", kwargs={"project_id": "PROJ003"}),
            Action(name="ResolveHourlyRates", kwargs={"project_id_list": ["PROJ003"]}),
            Action(name="CalculateInvoiceTotals", kwargs={"lines": [{"hours": 5, "rate": 75.0}], "hst_rate": 0.13}),
            Action(name="FetchInvoices", kwargs={"status": "open"}),
            Action(name="ComputeCollectionKpis", kwargs={"window_months": 12}),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-08"}),
            Action(name="InsertDashboardSnapshot", kwargs={
                "snapshot_date": "2024-08-31",
                "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-08.pdf"
            }),
            Action(name="GetDashboardSnapshotDetails", kwargs={"snapshot_id": 1}),
            Action(name="RecordInvoiceAudit", kwargs={"invoice_number": "2024-009", "event_type": "reviewed"}),
            Action(name="ListInvoiceAudit", kwargs={"invoice_number": "2024-009"}),
        ],
        outputs=[
            "Projects listed; PROJ003 read; rate resolved; total computed; open invoices reviewed; KPIs computed; "
            "AR_Aging_2024-08 exported; snapshot saved & read by id; invoice 2024-009 audit recorded & listed."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_041",
        instruction=(
            "Handle the opening of publisher_id 'PUB034' named 'Silver Birch Academic' and complete a November‑2024 aging snapshot with context. Final condition: 'PUB034' exists and can be read; open invoices are inspected; 12‑month KPIs are obtainable; the A/R aging PDF for '2024-11' is created and a dashboard snapshot for '2024-11-30' referencing that PDF is saved and can be accessed by id; for verification, the rate resolves for ['PROJ001'] and a sample total is calculated (2h @85.0, hst_rate 0.13)."
        ),
        actions=[
            Action(name="CreatePublisher", kwargs={"publisher_id": "PUB034", "name": "Silver Birch Academic"}),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB034"}),
            Action(name="FetchInvoices", kwargs={"status": "open"}),
            Action(name="ComputeCollectionKpis", kwargs={"window_months": 12}),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-11"}),
            Action(name="InsertDashboardSnapshot", kwargs={
                "snapshot_date": "2024-11-30",
                "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-11.pdf"
            }),
            Action(name="GetDashboardSnapshotDetails", kwargs={"snapshot_id": 1}),
            Action(name="ResolveHourlyRates", kwargs={"project_id_list": ["PROJ001"]}),
            Action(name="CalculateInvoiceTotals", kwargs={"lines": [{"hours": 2, "rate": 85.0}], "hst_rate": 0.13}),
        ],
        outputs=[
            "PUB034 created & read; open invoices reviewed; KPIs computed; AR_Aging_2024-11 exported; snapshot saved & read by id; rate resolved & sample total computed."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_042",
        instruction=(
            "Ensure near‑term due status and prepare a September‑2024 export with proofing. Final condition: days outstanding for '2024-024' using period_end '2024-10-31' and today '2024-10-29' are determined as -2 days and classified as 'upcoming_due'; open invoices are examined; the A/R aging PDF for '2024-09' is present and a dashboard snapshot for '2024-09-30' referencing 'https://storage.example.com/reports/AR_Aging_2024-09.pdf' is saved and accessible by id; an audit event 'risk_reviewed' is logged for '2024-024' and is available for listing."
        ),
        actions=[
            Action(name="ComputeDaysOutstanding", kwargs={
                "invoices": [{"invoice_number": "2024-024", "period_end": "2024-10-31"}],
                "today": "2024-10-29"
            }),
            Action(name="CategorizeAging", kwargs={"aging": [{"invoice_number": "2024-024", "days_outstanding": -2}]}),
            Action(name="FetchInvoices", kwargs={"status": "open"}),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-09"}),
            Action(name="InsertDashboardSnapshot", kwargs={
                "snapshot_date": "2024-09-30",
                "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-09.pdf"
            }),
            Action(name="GetDashboardSnapshotDetails", kwargs={"snapshot_id": 1}),
            Action(name="RecordInvoiceAudit", kwargs={"invoice_number": "2024-024", "event_type": "risk_reviewed"}),
            Action(name="ListInvoiceAudit", kwargs={"invoice_number": "2024-024"}),
        ],
        outputs=[
            "Upcoming‑due flagged for 2024-024; open invoices reviewed; AR_Aging_2024-09 exported; snapshot saved & read by id; risk audit recorded & listed."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_043",
        instruction=(
            "Handle the registration of publisher_id 'PUB037' named 'Seaway Academics' and prepare a snapshot for September‑2024. Final state: 'PUB037' is created and accessible; project_id 'PROJ2046' is present under 'PUB037' with isbn '978-1-3100-2046-1', project_title 'Statistics Primer, 1e', default_hourly_rate 95.0, and is accessible; a sample total is calculated (2h @95.0 with hst_rate 0.13); open invoices are assessed; the A/R aging PDF for '2024-09' is available and a snapshot for '2024-09-30' is stored at 'https://storage.example.com/reports/AR_Aging_2024-09.pdf' and is accessible by id."
        ),
        actions=[
            Action(name="CreatePublisher", kwargs={"publisher_id": "PUB037", "name": "Seaway Academics"}),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB037"}),
            Action(name="CreateProject", kwargs={
                "project_id": "PROJ2046",
                "publisher_id": "PUB037",
                "isbn": "978-1-3100-2046-1",
                "project_title": "Statistics Primer, 1e",
                "default_hourly_rate": 95.0
            }),
            Action(name="GetProjectDetails", kwargs={"project_id": "PROJ2046"}),
            Action(name="CalculateInvoiceTotals", kwargs={"lines": [{"hours": 2, "rate": 95.0}], "hst_rate": 0.13}),
            Action(name="FetchInvoices", kwargs={"status": "open"}),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-09"}),
            Action(name="InsertDashboardSnapshot", kwargs={
                "snapshot_date": "2024-09-30",
                "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-09.pdf"
            }),
            Action(name="GetDashboardSnapshotDetails", kwargs={"snapshot_id": 1}),
        ],
        outputs=[
            "PUB037 created & read; PROJ2046 created & read; sample total; open invoices reviewed; AR_Aging_2024-09 exported; snapshot saved & read by id."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_044",
        instruction=(
            "Confirm November‑2024 visibility and provide a representative invoice. Final state: project listings are available and 'PROJ001' details are accessible; open invoices are assessed and 12‑month KPIs are available; the A/R aging PDF for '2024-11' is present; ensure that the rate for ['PROJ001'] resolves correctly with a sample total calculated (1h @85.0 with hst_rate 0.13); invoice '2024-025' is accessible; an audit event 'reviewed' is recorded for '2024-025' and can be listed."
        ),
        actions=[
            Action(name="FetchProjects", kwargs={}),
            Action(name="GetProjectDetails", kwargs={"project_id": "PROJ001"}),
            Action(name="FetchInvoices", kwargs={"status": "open"}),
            Action(name="ComputeCollectionKpis", kwargs={"window_months": 12}),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-11"}),
            Action(name="ResolveHourlyRates", kwargs={"project_id_list": ["PROJ001"]}),
            Action(name="CalculateInvoiceTotals", kwargs={"lines": [{"hours": 1, "rate": 85.0}], "hst_rate": 0.13}),
            Action(name="GetInvoiceDetails", kwargs={"invoice_number": "2024-025"}),
            Action(name="RecordInvoiceAudit", kwargs={"invoice_number": "2024-025", "event_type": "reviewed"}),
            Action(name="ListInvoiceAudit", kwargs={"invoice_number": "2024-025"}),
        ],
        outputs=[
            "Projects listed; PROJ001 read; open invoices reviewed; KPIs computed; AR_Aging_2024-11 exported; sample total computed; invoice 2024-025 read; audit recorded & listed."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_045",
        instruction=(
            "Handle the creation of a concise July‑2024 invoice for publisher_id 'PUB004' and ensure audit logging. End state: invoice_number '2024-134' is established for period_start '2024-07-01' and period_end '2024-07-31' with totals (subtotal 340.0, hst_amount 44.2, total_due 384.2) and is accessible; one line is added for project_id 'PROJ001' with isbn '978-1-3100-0001-0' (4h @85.0) and is retrievable; an audit event 'generated' is recorded and accessible. Utilize pdf_path 'https://storage.example.com/invoices/2024/INV-2024-134.pdf'."
        ),
        actions=[
            Action(name="InsertInvoice", kwargs={
                "invoice_number": "2024-134",
                "publisher_id": "PUB004",
                "invoice_date": "2024-07-31",
                "period_start": "2024-07-01",
                "period_end": "2024-07-31",
                "subtotal": 340.0,
                "hst_amount": 44.2,
                "total_due": 384.2,
                "pdf_path": "https://storage.example.com/invoices/2024/INV-2024-134.pdf"
            }),
            Action(name="GetInvoiceDetails", kwargs={"invoice_number": "2024-134"}),
            Action(name="InsertInvoiceLines", kwargs={
                "invoice_number": "2024-134",
                "lines": [{"project_id": "PROJ001", "isbn": "978-1-3100-0001-0", "hours": 4, "rate": 85.0}]
            }),
            Action(name="ListInvoiceLines", kwargs={"invoice_number": "2024-134"}),
            Action(name="RecordInvoiceAudit", kwargs={"invoice_number": "2024-134", "event_type": "generated"}),
            Action(name="ListInvoiceAudit", kwargs={"invoice_number": "2024-134"}),
        ],
        outputs=[
            "Invoice 2024-134 inserted & read; line inserted & listed; audit recorded & listed."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_046",
        instruction=(
            "Coordinate the onboarding of publisher_id 'PUB040' named 'Red Maple Learning' and incorporate a math project, then compile a September‑2024 snapshot. End state: 'PUB040' is present and viewable; project_id 'PROJ2053' is available with isbn '978-1-3100-2053-4', project_title 'Pre‑Calculus, 1e', default_hourly_rate 99.0 and is accessible; a sample total is calculated (2h @99.0 with hst_rate 0.13); the A/R aging PDF is present for '2024-09' and a dashboard snapshot is secured for '2024-09-30' linking to 'https://storage.example.com/reports/AR_Aging_2024-09.pdf' and is accessible by id."
        ),
        actions=[
            Action(name="CreatePublisher", kwargs={"publisher_id": "PUB040", "name": "Red Maple Learning"}),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB040"}),
            Action(name="CreateProject", kwargs={
                "project_id": "PROJ2053",
                "publisher_id": "PUB040",
                "isbn": "978-1-3100-2053-4",
                "project_title": "Pre‑Calculus, 1e",
                "default_hourly_rate": 99.0
            }),
            Action(name="GetProjectDetails", kwargs={"project_id": "PROJ2053"}),
            Action(name="CalculateInvoiceTotals", kwargs={"lines": [{"hours": 2, "rate": 99.0}], "hst_rate": 0.13}),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-09"}),
            Action(name="InsertDashboardSnapshot", kwargs={
                "snapshot_date": "2024-09-30",
                "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-09.pdf"
            }),
            Action(name="GetDashboardSnapshotDetails", kwargs={"snapshot_id": 1}),
        ],
        outputs=[
            "PUB040 created & read; PROJ2053 created & read; sample total; AR_Aging_2024-09 exported; snapshot saved & read by id."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_047",
        instruction=(
            "Handle the formalization of an August‑2024 invoice for publisher_id 'PUB005' from an algebra project. Final state: project_id 'PROJ2056' is ensured to exist with isbn '978-1-3100-2056-5', project_title 'Algebra Toolkit, 1e', default_hourly_rate 92.0 and is accessible for reading; invoice_number '2024-135' is created for period_start '2024-08-01' and period_end '2024-08-31' with accurate totals (3h @92.0, hst_rate 0.13) and is accessible for reading; an audit event 'generated' is logged and can be listed. Utilize pdf_path 'https://storage.example.com/invoices/2024/INV-2024-135.pdf'."
        ),
        actions=[
            Action(name="CreateProject", kwargs={
                "project_id": "PROJ2056",
                "publisher_id": "PUB005",
                "isbn": "978-1-3100-2056-5",
                "project_title": "Algebra Toolkit, 1e",
                "default_hourly_rate": 92.0
            }),
            Action(name="GetProjectDetails", kwargs={"project_id": "PROJ2056"}),
            Action(name="InsertInvoice", kwargs={
                "invoice_number": "2024-135",
                "publisher_id": "PUB005",
                "invoice_date": "2024-08-31",
                "period_start": "2024-08-01",
                "period_end": "2024-08-31",
                "subtotal": 276.0,
                "hst_amount": 35.88,
                "total_due": 311.88,
                "pdf_path": "https://storage.example.com/invoices/2024/INV-2024-135.pdf"
            }),
            Action(name="GetInvoiceDetails", kwargs={"invoice_number": "2024-135"}),
            Action(name="RecordInvoiceAudit", kwargs={"invoice_number": "2024-135", "event_type": "generated"}),
            Action(name="ListInvoiceAudit", kwargs={"invoice_number": "2024-135"}),
        ],
        outputs=[
            "PROJ2056 created & read; invoice 2024-135 inserted & read; audit recorded & listed."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_048",
        instruction=(
            "Coordinate the addition of publisher_id 'PUB042' named 'Bright Horizons Press' and secure a November‑2024 dashboard. Final state: 'PUB042' is ensured to exist and is accessible for reading; open invoices have been reviewed and 12‑month KPIs are made available; the A/R aging PDF is created for '2024-11' and a dashboard snapshot is saved for '2024-11-30' referencing that PDF and can be accessed by id; a representative invoice '2024-021' is accessible for reading; for verification, the rate is resolved for ['PROJ001'] and a sample total is calculated (2h @85.0 with hst_rate 0.13)."
        ),
        actions=[
            Action(name="CreatePublisher", kwargs={"publisher_id": "PUB042", "name": "Bright Horizons Press"}),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB042"}),
            Action(name="FetchInvoices", kwargs={"status": "open"}),
            Action(name="ComputeCollectionKpis", kwargs={"window_months": 12}),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-11"}),
            Action(name="InsertDashboardSnapshot", kwargs={
                "snapshot_date": "2024-11-30",
                "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-11.pdf"
            }),
            Action(name="GetDashboardSnapshotDetails", kwargs={"snapshot_id": 1}),
            Action(name="GetInvoiceDetails", kwargs={"invoice_number": "2024-021"}),
            Action(name="ResolveHourlyRates", kwargs={"project_id_list": ["PROJ001"]}),
            Action(name="CalculateInvoiceTotals", kwargs={"lines": [{"hours": 2, "rate": 85.0}], "hst_rate": 0.13}),
        ],
        outputs=[
            "PUB042 created & read; open invoices reviewed; KPIs computed; AR_Aging_2024-11 exported; snapshot saved & read by id; invoice 2024-021 read; sample total computed."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_049",
        instruction=(
            "Handle the creation of a November‑2024 invoice for publisher_id 'PUB005' and ensure its audit is logged. End state: prior to invoicing, validate a representative time‑entry row with the description 'Hours for November', isbn '978-1-3100-2027-8', account_code 'DATA-LIT-1E', and hours_worked 3; calculate totals for a single line (3h @90.0, hst_rate 0.13); confirm invoice_number '2024-130' exists for period_start '2024-11-01' and period_end '2024-11-30' with those totals and is readable; record and list an audit event 'generated'. Utilize pdf_path 'https://storage.example.com/invoices/2024/INV-2024-130.pdf'."
        ),
        actions=[
            Action(name="ValidateTimeEntries", kwargs={
                "rows": [{
                    "description": "Hours for November",
                    "isbn": "978-1-3100-2027-8",
                    "account_code": "DATA-LIT-1E",
                    "hours_worked": 3
                }]
            }),
            Action(name="CalculateInvoiceTotals", kwargs={
                "lines": [{"hours": 3, "rate": 90.0}],
                "hst_rate": 0.13
            }),
            Action(name="InsertInvoice", kwargs={
                "invoice_number": "2024-130",
                "publisher_id": "PUB005",
                "invoice_date": "2024-11-30",
                "period_start": "2024-11-01",
                "period_end": "2024-11-30",
                "subtotal": 270.0,
                "hst_amount": 35.1,
                "total_due": 305.1,
                "pdf_path": "https://storage.example.com/invoices/2024/INV-2024-130.pdf"
            }),
            Action(name="GetInvoiceDetails", kwargs={"invoice_number": "2024-130"}),
            Action(name="RecordInvoiceAudit", kwargs={
                "invoice_number": "2024-130",
                "event_type": "generated"
            }),
            Action(name="ListInvoiceAudit", kwargs={"invoice_number": "2024-130"}),
        ],
        outputs=[
            "Time entries validated; totals computed; invoice 2024-130 inserted & read; audit recorded & listed."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_050",
        instruction=(
            "Coordinate the November‑2024 email step for a pending invoice. End state: send invoice_number '2024-011' via email using publisher_id 'PUB005' and consultant_id 'CONS001' with the subject 'Invoice 2024-011 (November 2024)', body 'Friendly reminder: attached is invoice 2024-011.' and attachment 'https://storage.example.com/invoices/2024/INV-2024-011.pdf', and ensure the invoice is re‑read with sent_at filled; record and list an audit event 'emailed'; review open invoices; ensure 12‑month KPIs are available; verify the A/R aging PDF exists for '2024-11'."
        ),
        actions=[
            Action(name="SendInvoiceEmail", kwargs={
                "publisher_id": "PUB005",
                "consultant_id": "CONS001",
                "invoice_number": "2024-011",
                "subject": "Invoice 2024-011 (November 2024)",
                "body_text": "Friendly reminder: attached is invoice 2024-011.",
                "attachment": "https://storage.example.com/invoices/2024/INV-2024-011.pdf"
            }),
            Action(name="GetInvoiceDetails", kwargs={"invoice_number": "2024-011"}),
            Action(name="RecordInvoiceAudit", kwargs={"invoice_number": "2024-011", "event_type": "emailed"}),
            Action(name="ListInvoiceAudit", kwargs={"invoice_number": "2024-011"}),
            Action(name="FetchInvoices", kwargs={"status": "open"}),
            Action(name="ComputeCollectionKpis", kwargs={"window_months": 12}),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-11"}),
        ],
        outputs=[
            "Invoice 2024-011 emailed & re‑read; audit recorded & listed; open invoices reviewed; KPIs computed; AR_Aging_2024-11 exported."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_051",
        instruction=(
            "Handle a September‑2024 invoice for publisher_id 'PUB001' and document its audit, ensuring time entries are validated first. End state: a specific time‑entry row with description 'September hours', isbn '978-1-3100-0001-0', account_code 'ENG-1E' and hours_worked 6 is validated; invoice_number '2024-132' exists for period_start '2024-09-01' and period_end '2024-09-30' with totals (subtotal 510.0, hst_amount 66.3, total_due 576.3) and is readable; an audit event 'generated' is recorded and listable; the A/R aging PDF exists for '2024-09'. Use pdf_path 'https://storage.example.com/invoices/2024/INV-2024-132.pdf'."
        ),
        actions=[
            Action(name="ValidateTimeEntries", kwargs={
                "rows": [{
                    "description": "September hours",
                    "isbn": "978-1-3100-0001-0",
                    "account_code": "ENG-1E",
                    "hours_worked": 6
                }]
            }),
            Action(name="InsertInvoice", kwargs={
                "invoice_number": "2024-132",
                "publisher_id": "PUB001",
                "invoice_date": "2024-09-30",
                "period_start": "2024-09-01",
                "period_end": "2024-09-30",
                "subtotal": 510.0,
                "hst_amount": 66.3,
                "total_due": 576.3,
                "pdf_path": "https://storage.example.com/invoices/2024/INV-2024-132.pdf"
            }),
            Action(name="GetInvoiceDetails", kwargs={"invoice_number": "2024-132"}),
            Action(name="RecordInvoiceAudit", kwargs={"invoice_number": "2024-132", "event_type": "generated"}),
            Action(name="ListInvoiceAudit", kwargs={"invoice_number": "2024-132"}),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-09"}),
        ],
        outputs=[
            "Time entries validated; invoice 2024-132 inserted & read; audit recorded & listed; AR_Aging_2024-09 exported."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_052",
        instruction=(
            "Coordinate the creation of a concise August‑2024 invoice for publisher_id 'PUB002' and record its lifecycle. End state: invoice_number '2024-133' exists for period_start '2024-08-01' and period_end '2024-08-31' with totals (subtotal 300.0, hst_amount 39.0, total_due 339.0) and is readable; a single line is inserted for 'PROJ003' with isbn '978-1-3100-0003-7' (4h @75.0) and is listable; an audit event 'generated' is recorded and listable. Use pdf_path 'https://storage.example.com/invoices/2024/INV-2024-133.pdf'."
        ),
        actions=[
            Action(name="InsertInvoice", kwargs={
                "invoice_number": "2024-133",
                "publisher_id": "PUB002",
                "invoice_date": "2024-08-31",
                "period_start": "2024-08-01",
                "period_end": "2024-08-31",
                "subtotal": 300.0,
                "hst_amount": 39.0,
                "total_due": 339.0,
                "pdf_path": "https://storage.example.com/invoices/2024/INV-2024-133.pdf"
            }),
            Action(name="GetInvoiceDetails", kwargs={"invoice_number": "2024-133"}),
            Action(name="InsertInvoiceLines", kwargs={
                "invoice_number": "2024-133",
                "lines": [
                    {"project_id": "PROJ003", "isbn": "978-1-3100-0003-7", "hours": 4, "rate": 75.0}
                ]
            }),
            Action(name="ListInvoiceLines", kwargs={"invoice_number": "2024-133"}),
            Action(name="RecordInvoiceAudit", kwargs={"invoice_number": "2024-133", "event_type": "generated"}),
            Action(name="ListInvoiceAudit", kwargs={"invoice_number": "2024-133"}),
        ],
        outputs=[
            "Invoice 2024-133 inserted & read; line inserted & listed; audit recorded & listed."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_053",
        instruction=(
            "Handle the onboarding of publisher_id 'PUB043' with the name 'Evergreen Learning Co.' and set up an October‑2024 baseline. End state: 'PUB043' is present and accessible; project_id 'PROJ3053' under 'PUB043' is present with isbn '978-1-3100-3053-1', project_title 'Media Literacy, 1e', default_hourly_rate 93.0 and is accessible; ensure rates are determined for ['PROJ3053','PROJ001']; a sample total is calculated (2h @93.0 and 1h @85.0 with hst_rate 0.13); confirm the existence of the A/R aging PDF for '2024-10'; a dashboard snapshot is archived for '2024-10-31' referencing that PDF and is accessible by date."
        ),
        actions=[
            Action(name="CreatePublisher", kwargs={"publisher_id": "PUB043", "name": "Evergreen Learning Co."}),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB043"}),

            Action(name="CreateProject", kwargs={
                "project_id": "PROJ3053",
                "publisher_id": "PUB043",
                "isbn": "978-1-3100-3053-1",
                "project_title": "Media Literacy, 1e",
                "default_hourly_rate": 93.0
            }),
            Action(name="GetProjectDetails", kwargs={"project_id": "PROJ3053"}),

            Action(name="ResolveHourlyRates", kwargs={"project_id_list": ["PROJ3053", "PROJ001"]}),
            Action(name="CalculateInvoiceTotals", kwargs={"lines": [{"hours": 2, "rate": 93.0}, {"hours": 1, "rate": 85.0}], "hst_rate": 0.13}),

            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-10"}),
            Action(name="InsertDashboardSnapshot", kwargs={
                "snapshot_date": "2024-10-31",
                "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-10.pdf"
            }),
            Action(name="GetDashboardSnapshotDetails", kwargs={"snapshot_date": "2024-10-31"}),
        ],
        outputs=[
            "PUB043 created & read; PROJ3053 created & read; rates resolved; sample total computed; "
            "AR_Aging_2024-10 exported; snapshot saved & read by date."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_054",
        instruction=(
            "Coordinate the creation of a concise November‑2024 invoice for publisher_id 'PUB004' and document its audit. End state: invoice_number '2024-141' is available for period_start '2024-11-01' and period_end '2024-11-30' with correct totals (4h @88.0, hst_rate 0.13) and is accessible; ensure a single line is added for project_id 'PROJ003' with isbn '978-1-3100-0003-7' for 4h @88.0 and is listable; record and list an audit event 'generated'. Utilize pdf_path 'https://storage.example.com/invoices/2024/INV-2024-141.pdf'."
        ),
        actions=[
            Action(name="InsertInvoice", kwargs={
                "invoice_number": "2024-141",
                "publisher_id": "PUB004",
                "invoice_date": "2024-11-30",
                "period_start": "2024-11-01",
                "period_end": "2024-11-30",
                "subtotal": 352.0,
                "hst_amount": 45.76,
                "total_due": 397.76,
                "pdf_path": "https://storage.example.com/invoices/2024/INV-2024-141.pdf"
            }),
            Action(name="GetInvoiceDetails", kwargs={"invoice_number": "2024-141"}),

            Action(name="InsertInvoiceLines", kwargs={
                "invoice_number": "2024-141",
                "lines": [{"project_id": "PROJ003", "isbn": "978-1-3100-0003-7", "hours": 4, "rate": 88.0}]
            }),
            Action(name="ListInvoiceLines", kwargs={"invoice_number": "2024-141"}),

            Action(name="RecordInvoiceAudit", kwargs={"invoice_number": "2024-141", "event_type": "generated"}),
            Action(name="ListInvoiceAudit", kwargs={"invoice_number": "2024-141"}),
        ],
        outputs=[
            "Invoice 2024-141 inserted & read; line inserted & listed; audit recorded & listed."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_055",
        instruction=(
            "Handle publisher_id 'PUB044' named 'Cedar Ridge Press' and coordinate an August‑2024 snapshot. End state: 'PUB044' exists and is readable; project_id 'PROJ3057' exists with isbn '978-1-3100-3057-2', project_title 'Financial Literacy, 1e', default_hourly_rate 91.0 and is readable; a sample total is computed (2h @91.0 with hst_rate 0.13); the A/R aging PDF exists for '2024-08' and a dashboard snapshot is stored for '2024-08-31' referencing that PDF and is readable by date."
        ),
        actions=[
            Action(name="CreatePublisher", kwargs={"publisher_id": "PUB044", "name": "Cedar Ridge Press"}),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB044"}),

            Action(name="CreateProject", kwargs={
                "project_id": "PROJ3057",
                "publisher_id": "PUB044",
                "isbn": "978-1-3100-3057-2",
                "project_title": "Financial Literacy, 1e",
                "default_hourly_rate": 91.0
            }),
            Action(name="GetProjectDetails", kwargs={"project_id": "PROJ3057"}),

            Action(name="CalculateInvoiceTotals", kwargs={"lines": [{"hours": 2, "rate": 91.0}], "hst_rate": 0.13}),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-08"}),
            Action(name="InsertDashboardSnapshot", kwargs={"snapshot_date": "2024-08-31", "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-08.pdf"}),
            Action(name="GetDashboardSnapshotDetails", kwargs={"snapshot_date": "2024-08-31"}),
        ],
        outputs=[
            "PUB044 created & read; PROJ3057 created & read; sample total; AR_Aging_2024-08 exported; snapshot saved & read by date."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_056",
        instruction=(
            "Initiate publisher_id 'PUB045' named 'Northern Summit Press' and prepare a July‑2024 sample. End state: 'PUB045' exists and is readable; project_id 'PROJ3059' exists with isbn '978-1-3100-3059-6', project_title 'Intro Philosophy, 1e', default_hourly_rate 87.0 and is readable; rates are resolved for ['PROJ3059','PROJ001']; a sample total is computed (1h @87.0 and 1h @85.0 with hst_rate 0.13); the A/R aging PDF exists for '2024-07'."
        ),
        actions=[
            Action(name="CreatePublisher", kwargs={"publisher_id": "PUB045", "name": "Northern Summit Press"}),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB045"}),

            Action(name="CreateProject", kwargs={
                "project_id": "PROJ3059",
                "publisher_id": "PUB045",
                "isbn": "978-1-3100-3059-6",
                "project_title": "Intro Philosophy, 1e",
                "default_hourly_rate": 87.0
            }),
            Action(name="GetProjectDetails", kwargs={"project_id": "PROJ3059"}),

            Action(name="ResolveHourlyRates", kwargs={"project_id_list": ["PROJ3059", "PROJ001"]}),
            Action(name="CalculateInvoiceTotals", kwargs={"lines": [{"hours": 1, "rate": 87.0}, {"hours": 1, "rate": 85.0}], "hst_rate": 0.13}),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-07"}),
        ],
        outputs=[
            "PUB045 created & read; PROJ3059 created & read; rates resolved; sample total; AR_Aging_2024-07 exported."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_057",
        instruction=(
            "Handle the formalization of a September‑2024 invoice for publisher_id 'PUB003' and record its audit. End state: invoice_number '2024-142' exists for period_start '2024-09-01' and period_end '2024-09-30' with correct totals (2h @97.0, hst_rate 0.13) and is readable; a single line is inserted for project_id 'PROJ003' with isbn '978-1-3100-0003-7' for 2h @97.0 and is listable; an audit event 'generated' is recorded and listable. Use pdf_path 'https://storage.example.com/invoices/2024/INV-2024-142.pdf'."
        ),
        actions=[
            Action(name="InsertInvoice", kwargs={
                "invoice_number": "2024-142",
                "publisher_id": "PUB003",
                "invoice_date": "2024-09-30",
                "period_start": "2024-09-01",
                "period_end": "2024-09-30",
                "subtotal": 194.0,
                "hst_amount": 25.22,
                "total_due": 219.22,
                "pdf_path": "https://storage.example.com/invoices/2024/INV-2024-142.pdf"
            }),
            Action(name="GetInvoiceDetails", kwargs={"invoice_number": "2024-142"}),
            Action(name="InsertInvoiceLines", kwargs={
                "invoice_number": "2024-142",
                "lines": [{"project_id": "PROJ003", "isbn": "978-1-3100-0003-7", "hours": 2, "rate": 97.0}]
            }),
            Action(name="ListInvoiceLines", kwargs={"invoice_number": "2024-142"}),
            Action(name="RecordInvoiceAudit", kwargs={"invoice_number": "2024-142", "event_type": "generated"}),
            Action(name="ListInvoiceAudit", kwargs={"invoice_number": "2024-142"}),
        ],
        outputs=[
            "Invoice 2024-142 inserted & read; line inserted & listed; audit recorded & listed."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_058",
        instruction=(
            "Coordinate the addition of publisher_id 'PUB047' named 'Horizon Peak Education' and document an August‑2024 snapshot with sample math totals. End state: 'PUB047' exists and is readable; project_id 'PROJ3064' exists with isbn '978-1-3100-3064-0', project_title 'Discrete Math, 1e', default_hourly_rate 104.0 and is readable; a sample total is computed (1h @104.0 with hst_rate 0.13); the A/R aging PDF exists for '2024-08' and a dashboard snapshot is stored for '2024-08-31' referencing that PDF and is readable by date."
        ),
        actions=[
            Action(name="CreatePublisher", kwargs={"publisher_id": "PUB047", "name": "Horizon Peak Education"}),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB047"}),

            Action(name="CreateProject", kwargs={
                "project_id": "PROJ3064",
                "publisher_id": "PUB047",
                "isbn": "978-1-3100-3064-0",
                "project_title": "Discrete Math, 1e",
                "default_hourly_rate": 104.0
            }),
            Action(name="GetProjectDetails", kwargs={"project_id": "PROJ3064"}),

            Action(name="CalculateInvoiceTotals", kwargs={"lines": [{"hours": 1, "rate": 104.0}], "hst_rate": 0.13}),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-08"}),
            Action(name="InsertDashboardSnapshot", kwargs={"snapshot_date": "2024-08-31", "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-08.pdf"}),
            Action(name="GetDashboardSnapshotDetails", kwargs={"snapshot_date": "2024-08-31"}),
        ],
        outputs=[
            "PUB047 created & read; PROJ3064 created & read; sample total; aging exported; snapshot saved & read by date."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_059",
        instruction=(
            "Construct a September‑2024 invoice for publisher_id 'PUB002' including a single line and log its audit. End state: invoice_number '2024-144' is present for period_start '2024-09-01' and period_end '2024-09-30' with accurate totals (3h @75.0, hst_rate 0.13) and is accessible; a single line is added for 'PROJ003' with isbn '978-1-3100-0003-7' (3h @75.0) and is listable; an audit event 'generated' is logged and listable. Utilize pdf_path 'https://storage.example.com/invoices/2024/INV-2024-144.pdf'."
        ),
        actions=[
            Action(name="InsertInvoice", kwargs={
                "invoice_number": "2024-144",
                "publisher_id": "PUB002",
                "invoice_date": "2024-09-30",
                "period_start": "2024-09-01",
                "period_end": "2024-09-30",
                "subtotal": 225.0,
                "hst_amount": 29.25,
                "total_due": 254.25,
                "pdf_path": "https://storage.example.com/invoices/2024/INV-2024-144.pdf"
            }),
            Action(name="GetInvoiceDetails", kwargs={"invoice_number": "2024-144"}),

            Action(name="InsertInvoiceLines", kwargs={
                "invoice_number": "2024-144",
                "lines": [
                    {"project_id": "PROJ003", "isbn": "978-1-3100-0003-7", "hours": 3, "rate": 75.0}
                ]
            }),
            Action(name="ListInvoiceLines", kwargs={"invoice_number": "2024-144"}),
            Action(name="RecordInvoiceAudit", kwargs={"invoice_number": "2024-144", "event_type": "generated"}),
            Action(name="ListInvoiceAudit", kwargs={"invoice_number": "2024-144"}),
        ],
        outputs=[
            "Invoice 2024-144 inserted & read; line inserted & listed; audit recorded & listed."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_060",
        instruction=(
            "Register publisher_id 'PUB051' under the name 'Maple Grove Education' and initiate a writing project for an October‑2024 review. End state: 'PUB051' is created and accessible; project_id 'PROJ3073' is established with isbn '978-1-3100-3073-8', project_title 'Advanced Composition, 1e', default_hourly_rate 95.0 and is accessible; rates are determined for ['PROJ3073','PROJ001']; a sample total is calculated (2h @95.0 and 1h @85.0 with hst_rate 0.13); the A/R aging PDF exists for '2024-10'."
        ),
        actions=[
            Action(name="CreatePublisher", kwargs={"publisher_id": "PUB051", "name": "Maple Grove Education"}),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB051"}),

            Action(name="CreateProject", kwargs={
                "project_id": "PROJ3073",
                "publisher_id": "PUB051",
                "isbn": "978-1-3100-3073-8",
                "project_title": "Advanced Composition, 1e",
                "default_hourly_rate": 95.0
            }),
            Action(name="GetProjectDetails", kwargs={"project_id": "PROJ3073"}),

            Action(name="ResolveHourlyRates", kwargs={"project_id_list": ["PROJ3073", "PROJ001"]}),
            Action(name="CalculateInvoiceTotals", kwargs={"lines": [{"hours": 2, "rate": 95.0}, {"hours": 1, "rate": 85.0}], "hst_rate": 0.13}),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-10"}),
        ],
        outputs=[
            "PUB051 created & read; PROJ3073 created & read; rates resolved; sample total; AR_Aging_2024-10 exported."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_061",
        instruction=(
            "Coordinate the setup of publisher_id 'PUB053' named 'Pine Valley Learning' and ensure an August‑2024 math sample is confirmed. End state: 'PUB053' is present and accessible; project_id 'PROJ3076' is available with isbn '978-1-3100-3076-7', project_title 'Linear Algebra, 1e', default_hourly_rate 101.0 and is accessible; a sample total is calculated (2h @101.0 with hst_rate 0.13); the A/R aging PDF is present for '2024-08'."
        ),
        actions=[
            Action(name="CreatePublisher", kwargs={"publisher_id": "PUB053", "name": "Pine Valley Learning"}),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB053"}),

            Action(name="CreateProject", kwargs={
                "project_id": "PROJ3076",
                "publisher_id": "PUB053",
                "isbn": "978-1-3100-3076-7",
                "project_title": "Linear Algebra, 1e",
                "default_hourly_rate": 101.0
            }),
            Action(name="GetProjectDetails", kwargs={"project_id": "PROJ3076"}),

            Action(name="CalculateInvoiceTotals", kwargs={"lines": [{"hours": 2, "rate": 101.0}], "hst_rate": 0.13}),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-08"}),
        ],
        outputs=[
            "PUB053 created & read; PROJ3076 created & read; sample total; AR_Aging_2024-08 exported."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_062",
        instruction=(
            "Handle the update of November‑2024 context and organize a representative invoice, saving a snapshot of the dashboard. End state: open invoices are assessed; 12‑month KPIs are accessible; days outstanding for invoice '2024-009' as of '2024-11-15' with period_end '2024-09-30' (46 days) are arranged; the A/R aging PDF is present for '2024-11'; a dashboard snapshot is saved for '2024-11-30' aligning with that PDF and is viewable by date."
        ),
        actions=[
            Action(name="FetchInvoices", kwargs={"status": "open"}),
            Action(name="ComputeCollectionKpis", kwargs={"window_months": 12}),
            Action(name="ComputeDaysOutstanding", kwargs={
                "invoices": [{"invoice_number": "2024-009", "period_end": "2024-09-30"}],
                "today": "2024-11-15"
            }),
            Action(name="CategorizeAging", kwargs={"aging": [{"invoice_number": "2024-009", "days_outstanding": 46}]}),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-11"}),
            Action(name="InsertDashboardSnapshot", kwargs={"snapshot_date": "2024-11-30", "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-11.pdf"}),
            Action(name="GetDashboardSnapshotDetails", kwargs={"snapshot_date": "2024-11-30"}),
        ],
        outputs=[
            "Open invoices reviewed; KPIs computed; 46 days categorized for 2024-009; AR_Aging_2024-11 exported; snapshot saved & read by date."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_063",
        instruction=(
            "Handle the addition of publisher_id 'PUB054' known as 'Aspen Trail Press' and initiate a readiness check for September‑2024. End state: 'PUB054' is present and can be accessed; project_id 'PROJ3078' is present with isbn '978-1-3100-3078-1', project_title 'World History, 1e', default_hourly_rate 92.0 and can be accessed; rates are confirmed for ['PROJ3078']; a sample total is calculated (3h @92.0 with hst_rate 0.13); the A/R aging PDF is available for '2024-09'."
        ),
        actions=[
            Action(name="CreatePublisher", kwargs={"publisher_id": "PUB054", "name": "Aspen Trail Press"}),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB054"}),

            Action(name="CreateProject", kwargs={
                "project_id": "PROJ3078",
                "publisher_id": "PUB054",
                "isbn": "978-1-3100-3078-1",
                "project_title": "World History, 1e",
                "default_hourly_rate": 92.0
            }),
            Action(name="GetProjectDetails", kwargs={"project_id": "PROJ3078"}),

            Action(name="ResolveHourlyRates", kwargs={"project_id_list": ["PROJ3078"]}),
            Action(name="CalculateInvoiceTotals", kwargs={"lines": [{"hours": 3, "rate": 92.0}], "hst_rate": 0.13}),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-09"}),
        ],
        outputs=[
            "PUB054 created & read; PROJ3078 created & read; rate resolved; sample total; AR_Aging_2024-09 exported."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_064",
        instruction=(
            "Coordinate the creation of an August‑2024 invoice for publisher_id 'PUB002' and ensure its audit is logged. End state: invoice_number '2024-146' is available for period_start '2024-08-01' and period_end '2024-08-31' with accurate totals (2h @85.0, hst_rate 0.13) and is accessible; a line entry is added for 'PROJ001' with isbn '978-1-3100-0001-0' (2h @85.0) and is displayable; an audit event 'generated' is documented and displayable. Utilize pdf_path 'https://storage.example.com/invoices/2024/INV-2024-146.pdf'."
        ),
        actions=[
            Action(name="InsertInvoice", kwargs={
                "invoice_number": "2024-146",
                "publisher_id": "PUB002",
                "invoice_date": "2024-08-31",
                "period_start": "2024-08-01",
                "period_end": "2024-08-31",
                "subtotal": 170.0,
                "hst_amount": 22.1,
                "total_due": 192.1,
                "pdf_path": "https://storage.example.com/invoices/2024/INV-2024-146.pdf"
            }),
            Action(name="GetInvoiceDetails", kwargs={"invoice_number": "2024-146"}),

            Action(name="InsertInvoiceLines", kwargs={
                "invoice_number": "2024-146",
                "lines": [{"project_id": "PROJ001", "isbn": "978-1-3100-0001-0", "hours": 2, "rate": 85.0}]
            }),
            Action(name="ListInvoiceLines", kwargs={"invoice_number": "2024-146"}),

            Action(name="RecordInvoiceAudit", kwargs={"invoice_number": "2024-146", "event_type": "generated"}),
            Action(name="ListInvoiceAudit", kwargs={"invoice_number": "2024-146"}),
        ],
        outputs=[
            "Invoice 2024-146 inserted & read; line inserted & listed; audit recorded & listed."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_065",
        instruction=(
            "Handle the creation of publisher_id 'PUB055' with the name 'Summit Ridge Learning' and set up an October 2024 dashboard with a small sample. Desired outcomes: 'PUB055' is created and accessible; open invoices are checked; 12-month KPIs are available; rates are finalized for ['PROJ001']; a sample total is calculated (1h @85.0 with hst_rate 0.13); the A/R aging PDF for '2024-10' is generated; a dashboard snapshot dated '2024-10-31' that includes this PDF is stored and date-readable."
        ),
        actions=[
            Action(name="CreatePublisher", kwargs={"publisher_id": "PUB055", "name": "Summit Ridge Learning"}),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB055"}),

            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-10"}),
            Action(name="InsertDashboardSnapshot", kwargs={"snapshot_date": "2024-10-31", "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-10.pdf"}),
            Action(name="GetDashboardSnapshotDetails", kwargs={"snapshot_date": "2024-10-31"}),

            Action(name="FetchInvoices", kwargs={"status": "open"}),
            Action(name="ComputeCollectionKpis", kwargs={"window_months": 12}),

            Action(name="ResolveHourlyRates", kwargs={"project_id_list": ["PROJ001"]}),
            Action(name="CalculateInvoiceTotals", kwargs={"lines": [{"hours": 1, "rate": 85.0}], "hst_rate": 0.13}),
        ],
        outputs=[
            "PUB055 created & read; AR_Aging_2024-10 exported; snapshot saved & read by date; open invoices reviewed; KPIs computed; rate resolved; sample total."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_066",
        instruction=(
            "Manage the addition of publisher_id 'PUB056' under the name 'Cobalt Creek Press' and organize a September 2024 sample with rates. Desired outcomes: 'PUB056' is established and accessible; project_id 'PROJ3083' exists with isbn '978-1-3100-3083-6', project_title 'Intro Sociology, 1e', default_hourly_rate 86.0 and is accessible; rates are finalized for ['PROJ3083', 'PROJ001']; a sample total is calculated (2h @86.0 and 1h @85.0 with hst_rate 0.13); the A/R aging PDF for '2024-09' is generated."
        ),
        actions=[
            Action(name="CreatePublisher", kwargs={"publisher_id": "PUB056", "name": "Cobalt Creek Press"}),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB056"}),

            Action(name="CreateProject", kwargs={
                "project_id": "PROJ3083",
                "publisher_id": "PUB056",
                "isbn": "978-1-3100-3083-6",
                "project_title": "Intro Sociology, 1e",
                "default_hourly_rate": 86.0
            }),
            Action(name="GetProjectDetails", kwargs={"project_id": "PROJ3083"}),

            Action(name="ResolveHourlyRates", kwargs={"project_id_list": ["PROJ3083", "PROJ001"]}),
            Action(name="CalculateInvoiceTotals", kwargs={"lines": [{"hours": 2, "rate": 86.0}, {"hours": 1, "rate": 85.0}], "hst_rate": 0.13}),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-09"}),
        ],
        outputs=[
            "PUB056 created & read; PROJ3083 created & read; rates resolved; sample total; AR_Aging_2024-09 exported."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_067",
        instruction=(
            "Handle the recording of an October‑2024 invoice for publisher_id 'PUB005' and ensure the accuracy of its line items. Final state: invoice_number '2024-147' is established for period_start '2024-10-01' and period_end '2024-10-31' with precise totals (4h @90.0, hst_rate 0.13) and is accessible in readable format; a single entry is added for project_id 'PROJ003' with isbn '978-1-3100-0003-7' (4h @90.0) and is available for listing; an audit event 'generated' is logged and can be listed. Utilize pdf_path 'https://storage.example.com/invoices/2024/INV-2024-147.pdf'."
        ),
        actions=[
            Action(name="InsertInvoice", kwargs={
                "invoice_number": "2024-147",
                "publisher_id": "PUB005",
                "invoice_date": "2024-10-31",
                "period_start": "2024-10-01",
                "period_end": "2024-10-31",
                "subtotal": 360.0,
                "hst_amount": 46.8,
                "total_due": 406.8,
                "pdf_path": "https://storage.example.com/invoices/2024/INV-2024-147.pdf"
            }),
            Action(name="GetInvoiceDetails", kwargs={"invoice_number": "2024-147"}),

            Action(name="InsertInvoiceLines", kwargs={
                "invoice_number": "2024-147",
                "lines": [{"project_id": "PROJ003", "isbn": "978-1-3100-0003-7", "hours": 4, "rate": 90.0}]
            }),
            Action(name="ListInvoiceLines", kwargs={"invoice_number": "2024-147"}),
            Action(name="RecordInvoiceAudit", kwargs={"invoice_number": "2024-147", "event_type": "generated"}),
            Action(name="ListInvoiceAudit", kwargs={"invoice_number": "2024-147"}),
        ],
        outputs=[
            "Invoice 2024-147 inserted & read; line inserted & listed; audit recorded & listed."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_068",
        instruction=(
            "Coordinate the formalization of a September‑2024 invoice for publisher_id 'PUB004' that includes one project and confirm the context. Final state: invoice_number '2024-148' is established for period_start '2024-09-01' and period_end '2024-09-30' with precise totals (2h @85.0, hst_rate 0.13) and is accessible in readable format; a single entry is added for 'PROJ001' (2h @85.0, isbn '978-1-3100-0001-0') and is available for listing; an audit event 'generated' is logged and can be listed. Use pdf_path 'https://storage.example.com/invoices/2024/INV-2024-148.pdf'."
        ),
        actions=[
            Action(name="InsertInvoice", kwargs={
                "invoice_number": "2024-148",
                "publisher_id": "PUB004",
                "invoice_date": "2024-09-30",
                "period_start": "2024-09-01",
                "period_end": "2024-09-30",
                "subtotal": 170.0,
                "hst_amount": 22.1,
                "total_due": 192.1,
                "pdf_path": "https://storage.example.com/invoices/2024/INV-2024-148.pdf"
            }),
            Action(name="GetInvoiceDetails", kwargs={"invoice_number": "2024-148"}),

            Action(name="InsertInvoiceLines", kwargs={
                "invoice_number": "2024-148",
                "lines": [
                    {"project_id": "PROJ001", "isbn": "978-1-3100-0001-0", "hours": 2, "rate": 85.0}
                ]
            }),
            Action(name="ListInvoiceLines", kwargs={"invoice_number": "2024-148"}),
            Action(name="RecordInvoiceAudit", kwargs={"invoice_number": "2024-148", "event_type": "generated"}),
            Action(name="ListInvoiceAudit", kwargs={"invoice_number": "2024-148"}),
        ],
        outputs=[
            "Invoice 2024-148 inserted & read; line inserted & listed; audit recorded & listed."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_069",
        instruction=(
            "Handle the addition of project_id 'PROJ3054' for publisher_id 'PUB005' and ensure a November‑2024 sample with an explicit aging check. End state: 'PROJ3054' is present with isbn '978-1-3100-3054-8', project_title 'Canadian Literature, 2e', default_hourly_rate 90.0 and is accessible; rates are resolved for ['PROJ3054']; a sample total calculation occurs (3h @90.0 with hst_rate 0.13); categorize days outstanding for '2024-010' as of '2024-11-15' with period_end '2024-10-31' (15 days); the A/R aging PDF is available for '2024-11'."
        ),
        actions=[
            Action(name="CreateProject", kwargs={
                "project_id": "PROJ3054",
                "publisher_id": "PUB005",
                "isbn": "978-1-3100-3054-8",
                "project_title": "Canadian Literature, 2e",
                "default_hourly_rate": 90.0
            }),
            Action(name="GetProjectDetails", kwargs={"project_id": "PROJ3054"}),
            Action(name="ResolveHourlyRates", kwargs={"project_id_list": ["PROJ3054"]}),
            Action(name="CalculateInvoiceTotals", kwargs={"lines": [{"hours": 3, "rate": 90.0}], "hst_rate": 0.13}),
            Action(name="ComputeDaysOutstanding", kwargs={
                "invoices": [{"invoice_number": "2024-010", "period_end": "2024-10-31"}],
                "today": "2024-11-15"
            }),
            Action(name="CategorizeAging", kwargs={"aging": [{"invoice_number": "2024-010", "days_outstanding": 15}]}),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-11"}),
        ],
        outputs=[
            "PROJ3054 created & read; rate resolved; sample total computed; 15 days categorized for 2024-010; AR_Aging_2024-11 exported."
        ],
    ),    
    Task(
        annotator="A",
        user_id="ca_v4_070",
        instruction=(
            "Coordinate readiness validation for November‑2024 concerning project_id 'PROJ001' and log an aging categorization. End state: projects are displayed and 'PROJ001' details are accessible; rates are resolved for ['PROJ001']; compute a sample total (3h @85.0 with hst_rate 0.13); inspect open invoices; 12‑month KPIs are accessible; the A/R aging PDF is available for '2024-11'; categorize days outstanding for invoice '2024-010' as of '2024-11-20' with period_end '2024-10-31' (20 days); document an invoice audit event 'aging_categorized' for '2024-010' and make it listable."
        ),
        actions=[
            Action(name="FetchProjects", kwargs={}),
            Action(name="GetProjectDetails", kwargs={"project_id": "PROJ001"}),

            Action(name="ResolveHourlyRates", kwargs={"project_id_list": ["PROJ001"]}),
            Action(name="CalculateInvoiceTotals", kwargs={"lines": [{"hours": 3, "rate": 85.0}], "hst_rate": 0.13}),

            Action(name="FetchInvoices", kwargs={"status": "open"}),
            Action(name="ComputeCollectionKpis", kwargs={"window_months": 12}),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-11"}),

            Action(name="ComputeDaysOutstanding", kwargs={
                "invoices": [{"invoice_number": "2024-010", "period_end": "2024-10-31"}],
                "today": "2024-11-20"
            }),
            Action(name="CategorizeAging", kwargs={"aging": [{"invoice_number": "2024-010", "days_outstanding": 20}]}),
            Action(name="RecordInvoiceAudit", kwargs={"invoice_number": "2024-010", "event_type": "aging_categorized"}),
            Action(name="ListInvoiceAudit", kwargs={"invoice_number": "2024-010"}),
        ],
        outputs=[
            "Projects listed; PROJ001 read; rate resolved; sample total; open invoices reviewed; KPIs computed; AR_Aging_2024-11 exported; "
            "20 days categorized for 2024-010; audit recorded & listed."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_071",
        instruction=(
            "Coordinate normalization of contacts and ensure verification of an October‑2024 sample for publisher_id 'PUB003' using an aging categorization. Result: Confirm 'PUB003' contact_email equals 'accounts@canopypress.ca' and is accessible; Ensure CONS001 address equals '1234 Oak Street, Montreal, ON M5V 3A8' and is accessible; Resolve rates for ['PROJ003']; Compute a sample total (2h @75.0 with hst_rate 0.13); Categorize days outstanding for '2024-010' as of '2024-11-15' based on period_end '2024-10-31' (15 days); Verify the existence of the A/R aging PDF for '2024-10'."
        ),
        actions=[
            Action(name="UpdatePublisherContact", kwargs={"publisher_id": "PUB003", "contact_email": "accounts@canopypress.ca"}),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB003"}),

            Action(name="UpdateConsultantContact", kwargs={"consultant_id": "CONS001", "address": "1234 Oak Street, Montreal, ON M5V 3A8"}),
            Action(name="GetConsultantProfile", kwargs={"consultant_id": "CONS001"}),

            Action(name="ResolveHourlyRates", kwargs={"project_id_list": ["PROJ003"]}),
            Action(name="CalculateInvoiceTotals", kwargs={"lines": [{"hours": 2, "rate": 75.0}], "hst_rate": 0.13}),
            Action(name="ComputeDaysOutstanding", kwargs={
                "invoices": [{"invoice_number": "2024-010", "period_end": "2024-10-31"}],
                "today": "2024-11-15"
            }),
            Action(name="CategorizeAging", kwargs={"aging": [{"invoice_number": "2024-010", "days_outstanding": 15}]}),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-10"}),
        ],
        outputs=[
            "PUB003 AP updated & read; CONS001 address updated & read; rate resolved; sample total; 15 days categorized for 2024-010; AR_Aging_2024-10 exported."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_072",
        instruction=(
            "Handle the creation of publisher_id 'PUB049' named 'Blue Shore Academics' with a civics project and confirm its September‑2024 context. Final state: Ensure 'PUB049' is created and accessible; Verify project_id 'PROJ3069' exists with isbn '978-1-3100-3069-4', project_title 'Civics Foundations, 1e', default_hourly_rate 88.0 and is accessible; Review open invoices; Provide 12‑month KPIs; Compute a sample total (2h @88.0 with hst_rate 0.13); Ensure the A/R aging PDF exists for '2024-09'."
        ),
        actions=[
            Action(name="CreatePublisher", kwargs={"publisher_id": "PUB049", "name": "Blue Shore Academics"}),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB049"}),

            Action(name="CreateProject", kwargs={
                "project_id": "PROJ3069",
                "publisher_id": "PUB049",
                "isbn": "978-1-3100-3069-4",
                "project_title": "Civics Foundations, 1e",
                "default_hourly_rate": 88.0
            }),
            Action(name="GetProjectDetails", kwargs={"project_id": "PROJ3069"}),

            Action(name="FetchInvoices", kwargs={"status": "open"}),
            Action(name="ComputeCollectionKpis", kwargs={"window_months": 12}),
            Action(name="CalculateInvoiceTotals", kwargs={"lines": [{"hours": 2, "rate": 88.0}], "hst_rate": 0.13}),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-09"}),
        ],
        outputs=[
            "PUB049 created & read; PROJ3069 created & read; open invoices reviewed; KPIs computed; sample total; AR_Aging_2024-09 exported."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_073",
        instruction=(
            "Formalize an email for the November‑2024 invoice '2024-010' and document the audit with context. Final state: invoice_number '2024-010' is emailed using publisher_id 'PUB005' and consultant_id 'CONS001' with subject 'Invoice 2024-010 (November 2024)', body 'Please see attached invoice 2024-010.' and attachment 'https://storage.example.com/invoices/2024/INV-2024-010.pdf', and the invoice is re‑read with sent_at field populated; an audit event 'emailed' is logged and listable; open invoices are evaluated; 12‑month KPIs are accessible; the A/R aging PDF is available for '2024-11'."
        ),
        actions=[
            Action(name="SendInvoiceEmail", kwargs={
                "publisher_id": "PUB005",
                "consultant_id": "CONS001",
                "invoice_number": "2024-010",
                "subject": "Invoice 2024-010 (November 2024)",
                "body_text": "Please see attached invoice 2024-010.",
                "attachment": "https://storage.example.com/invoices/2024/INV-2024-010.pdf"
            }),
            Action(name="GetInvoiceDetails", kwargs={"invoice_number": "2024-010"}),
            Action(name="RecordInvoiceAudit", kwargs={"invoice_number": "2024-010", "event_type": "emailed"}),
            Action(name="ListInvoiceAudit", kwargs={"invoice_number": "2024-010"}),
            Action(name="FetchInvoices", kwargs={"status": "open"}),
            Action(name="ComputeCollectionKpis", kwargs={"window_months": 12}),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-11"}),
        ],
        outputs=[
            "Invoice 2024-010 emailed & re‑read; audit recorded & listed; open invoices reviewed; KPIs computed; AR_Aging_2024-11 exported."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_074",
        instruction=(
            "Secure November‑2024 readiness for publisher_id 'PUB004' by initiating a data science project and verifying totals through an aging categorization. Final state: project_id 'PROJ3081' exists with isbn '978-1-3100-3081-2', project_title 'Data Science Projects, 1e', default_hourly_rate 106.0 and is accessible; rates are established for ['PROJ3081']; a sample total is calculated (1h @106.0 with hst_rate 0.13); open invoices are evaluated; the A/R aging PDF is available for '2024-11'; days outstanding for '2024-010' as of '2024-11-15' using period_end '2024-10-31' (15 days) are categorized."
        ),
        actions=[
            Action(name="CreateProject", kwargs={
                "project_id": "PROJ3081",
                "publisher_id": "PUB004",
                "isbn": "978-1-3100-3081-2",
                "project_title": "Data Science Projects, 1e",
                "default_hourly_rate": 106.0
            }),
            Action(name="GetProjectDetails", kwargs={"project_id": "PROJ3081"}),

            Action(name="ResolveHourlyRates", kwargs={"project_id_list": ["PROJ3081"]}),
            Action(name="CalculateInvoiceTotals", kwargs={"lines": [{"hours": 1, "rate": 106.0}], "hst_rate": 0.13}),
            Action(name="FetchInvoices", kwargs={"status": "open"}),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-11"}),

            Action(name="ComputeDaysOutstanding", kwargs={
                "invoices": [{"invoice_number": "2024-010", "period_end": "2024-10-31"}],
                "today": "2024-11-15"
            }),
            Action(name="CategorizeAging", kwargs={"aging": [{"invoice_number": "2024-010", "days_outstanding": 15}]}),
        ],
        outputs=[
            "PROJ3081 created & read; rate resolved; sample total; open invoices reviewed; AR_Aging_2024-11 exported; 15 days categorized for 2024-010."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_075",
        instruction=(
            "Organize the September‑2024 contact information and record an upcoming‑due classification with context. End state: publisher_id 'PUB001' contact_email equals 'accounts@nelson-edu.ca' and is accessible; days outstanding for invoice '2024-024' as of '2024-09-29' with a period_end of '2024-10-01' (‑2 days) are categorized as 'upcoming_due'; an invoice audit event 'aging_categorized' is logged for '2024-024' and can be listed; open invoices are inspected; 12‑month KPIs are made available; the A/R aging PDF is present for '2024-09'."
        ),
        actions=[
            Action(name="UpdatePublisherContact", kwargs={"publisher_id": "PUB001", "contact_email": "accounts@nelson-edu.ca"}),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB001"}),

            Action(name="ComputeDaysOutstanding", kwargs={
                "invoices": [{"invoice_number": "2024-024", "period_end": "2024-10-01"}],
                "today": "2024-09-29"
            }),
            Action(name="CategorizeAging", kwargs={"aging": [{"invoice_number": "2024-024", "days_outstanding": -2}]}),

            Action(name="RecordInvoiceAudit", kwargs={"invoice_number": "2024-024", "event_type": "aging_categorized"}),
            Action(name="ListInvoiceAudit", kwargs={"invoice_number": "2024-024"}),

            Action(name="FetchInvoices", kwargs={"status": "open"}),
            Action(name="ComputeCollectionKpis", kwargs={"window_months": 12}),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-09"}),
        ],
        outputs=[
            "PUB001 AP updated & read; upcoming‑due flagged for 2024-024; audit recorded & listed; open invoices reviewed; KPIs computed; AR_Aging_2024-09 exported."
        ],
    ),    
    Task(
        annotator="A",
        user_id="ca_v4_076",
        instruction=(
            "Incorporate publisher_id 'PUB048' called 'Bright Pine Press' and coordinate November‑2024 reporting with a small sample. End state: 'PUB048' is present and can be accessed; open invoices are examined; 12‑month KPIs are provided; rates are finalized for ['PROJ001']; a sample total is calculated (1h @85.0 with hst_rate 0.13); the A/R aging PDF is produced for '2024-11'; a dashboard snapshot is saved for '2024-11-30' and is accessible by date."
        ),
        actions=[
            Action(name="CreatePublisher", kwargs={"publisher_id": "PUB048", "name": "Bright Pine Press"}),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB048"}),

            Action(name="FetchInvoices", kwargs={"status": "open"}),
            Action(name="ComputeCollectionKpis", kwargs={"window_months": 12}),
            Action(name="ResolveHourlyRates", kwargs={"project_id_list": ["PROJ001"]}),
            Action(name="CalculateInvoiceTotals", kwargs={"lines": [{"hours": 1, "rate": 85.0}], "hst_rate": 0.13}),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-11"}),
            Action(name="InsertDashboardSnapshot", kwargs={"snapshot_date": "2024-11-30", "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-11.pdf"}),
            Action(name="GetDashboardSnapshotDetails", kwargs={"snapshot_date": "2024-11-30"}),
        ],
        outputs=[
            "PUB048 created & read; open invoices reviewed; KPIs computed; rate resolved; sample total; AR_Aging_2024-11 exported; snapshot saved & read by date."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_077",
        instruction=(
            "Insert publisher_id 'PUB057' with the name 'Harbor Lights Learning' and organize an August‑2024 dashboard featuring a minimal total. Final state: 'PUB057' is present and viewable; a sample total is calculated (1h @85.0 with hst_rate 0.13) using the rate for ['PROJ001']; the A/R aging PDF is available for '2024-08'; a dashboard snapshot is saved for '2024-08-31' and can be accessed by date; days outstanding for '2024-010' as of '2024-08-15' using period_end '2024-07-31' (15 days) are sorted."
        ),
        actions=[
            Action(name="CreatePublisher", kwargs={"publisher_id": "PUB057", "name": "Harbor Lights Learning"}),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB057"}),

            Action(name="ResolveHourlyRates", kwargs={"project_id_list": ["PROJ001"]}),
            Action(name="CalculateInvoiceTotals", kwargs={"lines": [{"hours": 1, "rate": 85.0}], "hst_rate": 0.13}),

            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-08"}),
            Action(name="InsertDashboardSnapshot", kwargs={"snapshot_date": "2024-08-31", "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-08.pdf"}),
            Action(name="GetDashboardSnapshotDetails", kwargs={"snapshot_date": "2024-08-31"}),

            Action(name="ComputeDaysOutstanding", kwargs={
                "invoices": [{"invoice_number": "2024-010", "period_end": "2024-07-31"}],
                "today": "2024-08-15"
            }),
            Action(name="CategorizeAging", kwargs={"aging": [{"invoice_number": "2024-010", "days_outstanding": 15}]}),
        ],
        outputs=[
            "PUB057 created & read; rate resolved; sample total; AR_Aging_2024-08 exported; snapshot saved & read by date; 15 days categorized for 2024-010."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_078",
        instruction=(
            "Introduce publisher_id 'PUB046' with the name 'Lantern House Education' and set up a November‑2024 snapshot. Final state: 'PUB046' is present and viewable; project_id 'PROJ3061' is created with isbn '978-1-3100-3061-9', project_title 'Critical Thinking, 1e', default_hourly_rate 99.0 and is accessible; pending invoices are checked; 12‑month KPIs are accessible; the A/R aging PDF is available for '2024-11'; a dashboard snapshot is stored for '2024-11-30' and can be accessed by date."
        ),
        actions=[
            Action(name="CreatePublisher", kwargs={"publisher_id": "PUB046", "name": "Lantern House Education"}),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB046"}),

            Action(name="CreateProject", kwargs={
                "project_id": "PROJ3061",
                "publisher_id": "PUB046",
                "isbn": "978-1-3100-3061-9",
                "project_title": "Critical Thinking, 1e",
                "default_hourly_rate": 99.0
            }),
            Action(name="GetProjectDetails", kwargs={"project_id": "PROJ3061"}),

            Action(name="FetchInvoices", kwargs={"status": "open"}),
            Action(name="ComputeCollectionKpis", kwargs={"window_months": 12}),

            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-11"}),
            Action(name="InsertDashboardSnapshot", kwargs={"snapshot_date": "2024-11-30", "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-11.pdf"}),
            Action(name="GetDashboardSnapshotDetails", kwargs={"snapshot_date": "2024-11-30"}),
        ],
        outputs=[
            "PUB046 created & read; PROJ3061 created & read; open invoices reviewed; KPIs computed; aging exported; snapshot saved & read by date."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_079",
        instruction=(
            "Handle the computation and categorization of a November‑2024 aging check and confirm context with an existing snapshot. End state: The '2024-021' invoice's days outstanding as of '2024-11-20', using period_end '2024-10-31' (20 days), are categorized; projects are listed; 'PROJ003' details are accessible; rates for ['PROJ003'] are resolved; compute a sample total (1h @75.0 with hst_rate 0.13); open invoices are reviewed; 12‑month KPIs are available; the A/R aging PDF for '2024-11' exists; a dashboard snapshot is stored for '2024-11-30' and can be accessed by date."
        ),
        actions=[
            Action(name="ComputeDaysOutstanding", kwargs={
                "invoices": [{"invoice_number": "2024-021", "period_end": "2024-10-31"}],
                "today": "2024-11-20"
            }),
            Action(name="CategorizeAging", kwargs={"aging": [{"invoice_number": "2024-021", "days_outstanding": 20}]}),

            Action(name="FetchProjects", kwargs={}),
            Action(name="GetProjectDetails", kwargs={"project_id": "PROJ003"}),
            Action(name="ResolveHourlyRates", kwargs={"project_id_list": ["PROJ003"]}),
            Action(name="CalculateInvoiceTotals", kwargs={"lines": [{"hours": 1, "rate": 75.0}], "hst_rate": 0.13}),

            Action(name="FetchInvoices", kwargs={"status": "open"}),
            Action(name="ComputeCollectionKpis", kwargs={"window_months": 12}),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-11"}),
            Action(name="InsertDashboardSnapshot", kwargs={"snapshot_date": "2024-11-30", "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-11.pdf"}),
            Action(name="GetDashboardSnapshotDetails", kwargs={"snapshot_date": "2024-11-30"}),
        ],
        outputs=[
            "20 days categorized for 2024-021; projects listed; PROJ003 read; rate resolved; sample total; open invoices reviewed; KPIs computed; "
            "AR_Aging_2024-11 exported; snapshot saved & read by date."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_080",
        instruction=(
            "Coordinate the addition of publisher_id 'PUB050' with the name 'Riverbend Academic' and store an August‑2024 dashboard with a small sample. End state: 'PUB050' is present and can be accessed; open invoices are reviewed; 12‑month KPIs are available; rates are resolved for ['PROJ001']; calculate a sample total (1h @85.0 with hst_rate 0.13); the A/R aging PDF for '2024-08' exists; a dashboard snapshot is stored for '2024-08-31' and can be accessed by date."
        ),
        actions=[
            Action(name="CreatePublisher", kwargs={"publisher_id": "PUB050", "name": "Riverbend Academic"}),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB050"}),

            Action(name="FetchInvoices", kwargs={"status": "open"}),
            Action(name="ComputeCollectionKpis", kwargs={"window_months": 12}),
            Action(name="ResolveHourlyRates", kwargs={"project_id_list": ["PROJ001"]}),
            Action(name="CalculateInvoiceTotals", kwargs={"lines": [{"hours": 1, "rate": 85.0}], "hst_rate": 0.13}),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-08"}),
            Action(name="InsertDashboardSnapshot", kwargs={"snapshot_date": "2024-08-31", "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-08.pdf"}),
            Action(name="GetDashboardSnapshotDetails", kwargs={"snapshot_date": "2024-08-31"}),
        ],
        outputs=[
            "PUB050 created & read; open invoices reviewed; KPIs computed; rate resolved; sample total; AR_Aging_2024-08 exported; snapshot saved & read by date."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_081",
        instruction=(
            "Handle the registration of publisher_id 'PUB052' labeled 'Aurora Ridge Press' and save a snapshot for November‑2024 including a small sample. Final outcome: 'PUB052' is present and accessible; open invoices are checked; 12‑month KPIs are accessible; rates are clarified for ['PROJ001']; a sample total is calculated (1h @85.0 with hst_rate 0.13); the A/R aging PDF is available for '2024-11'; a dashboard snapshot is stored for '2024-11-30' and accessible by date."
        ),
        actions=[
            Action(name="CreatePublisher", kwargs={"publisher_id": "PUB052", "name": "Aurora Ridge Press"}),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB052"}),

            Action(name="FetchInvoices", kwargs={"status": "open"}),
            Action(name="ComputeCollectionKpis", kwargs={"window_months": 12}),
            Action(name="ResolveHourlyRates", kwargs={"project_id_list": ["PROJ001"]}),
            Action(name="CalculateInvoiceTotals", kwargs={"lines": [{"hours": 1, "rate": 85.0}], "hst_rate": 0.13}),
            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-11"}),
            Action(name="InsertDashboardSnapshot", kwargs={"snapshot_date": "2024-11-30", "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-11.pdf"}),
            Action(name="GetDashboardSnapshotDetails", kwargs={"snapshot_date": "2024-11-30"}),
        ],
        outputs=[
            "PUB052 created & read; open invoices reviewed; KPIs computed; rate resolved; sample total; AR_Aging_2024-11 exported; snapshot saved & read by date."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_082",
        instruction=(
            "Coordinate the addition of publisher_id 'PUB057' with the name 'Harbor Lights Learning' and prepare an August‑2024 dashboard with a small total. Final outcome: 'PUB057' is present and accessible; a sample total is calculated (1h @85.0 with hst_rate 0.13) using rate for ['PROJ001']; the A/R aging PDF is available for '2024-08'; a dashboard snapshot is saved for '2024-08-31' referencing 'https://storage.example.com/reports/AR_Aging_2024-08.pdf' and accessible by date; days outstanding for '2024-010' as of '2024-08-15' using period_end '2024-07-31' (15 days) are categorized."
        ),
        actions=[
            Action(name="CreatePublisher", kwargs={"publisher_id": "PUB057", "name": "Harbor Lights Learning"}),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB057"}),

            Action(name="ResolveHourlyRates", kwargs={"project_id_list": ["PROJ001"]}),
            Action(name="CalculateInvoiceTotals", kwargs={"lines": [{"hours": 1, "rate": 85.0}], "hst_rate": 0.13}),

            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-08"}),
            Action(name="InsertDashboardSnapshot", kwargs={"snapshot_date": "2024-08-31", "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-08.pdf"}),
            Action(name="GetDashboardSnapshotDetails", kwargs={"snapshot_date": "2024-08-31"}),

            Action(name="ComputeDaysOutstanding", kwargs={
                "invoices": [{"invoice_number": "2024-010", "period_end": "2024-07-31"}],
                "today": "2024-08-15"
            }),
            Action(name="CategorizeAging", kwargs={"aging": [{"invoice_number": "2024-010", "days_outstanding": 15}]}),
        ],
        outputs=[
            "PUB057 created & read; rate resolved; sample total; AR_Aging_2024-08 exported; snapshot saved & read by date; 15 days categorized for 2024-010."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_083",
        instruction=(
            "Handle the onboarding of a new client and align an October‑2024 snapshot. End state: publisher_id 'PUB021' named 'Algonquin Scholastic' exists and is readable; project_id 'PROJ1102' exists under 'PUB021' with isbn '978-1-3100-1010-1', project_title 'Intro Statistics, 1e', default_hourly_rate 95.0 and is readable; rates are resolved for ['PROJ1102','PROJ001'] and sample totals are computed (3h @95.0 and 2h @85.0); A/R aging for '2024-10' is exported and a snapshot stored for '2024-10-31' with the same PDF."
        ),
        actions=[
            Action(name="CreatePublisher", kwargs={
                "publisher_id": "PUB021",
                "name": "Algonquin Scholastic"
            }),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB021"}),

            Action(name="CreateProject", kwargs={
                "project_id": "PROJ1102",
                "publisher_id": "PUB021",
                "isbn": "978-1-3100-1010-1",
                "project_title": "Intro Statistics, 1e",
                "default_hourly_rate": 95.0
            }),
            Action(name="GetProjectDetails", kwargs={"project_id": "PROJ1102"}),

            Action(name="ResolveHourlyRates", kwargs={"project_id_list": ["PROJ1102", "PROJ001"]}),
            Action(name="CalculateInvoiceTotals", kwargs={
                "lines": [{"hours": 3, "rate": 95.0}, {"hours": 2, "rate": 85.0}],
                "hst_rate": 0.13
            }),

            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-10"}),
            Action(name="InsertDashboardSnapshot", kwargs={
                "snapshot_date": "2024-10-31",
                "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-10.pdf"
            }),
            Action(name="GetDashboardSnapshotDetails", kwargs={"snapshot_date": "2024-10-31"}),
        ],
        outputs=[
            "PUB021 created & read; PROJ1102 created & read; rates resolved; totals computed; AR_Aging_2024-10 exported; snapshot saved & read."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_084",
        instruction=(
            "Coordinate the opening of a new publisher and align a November‑2024 review. End state: publisher_id 'PUB022' named 'Bayview K12' exists and is readable; project_id 'PROJ1104' exists under 'PUB022' with isbn '978-1-3100-1013-2', project_title 'Civics Basics, 1e', default_hourly_rate 80.0 and is readable; rates are resolved for ['PROJ1104'] and a sample total is computed (6h @80.0); open invoices are reviewed and 12‑month KPIs are available; A/R aging for '2024-11' is exported and a snapshot stored for '2024-11-30'."
        ),
        actions=[
            Action(name="CreatePublisher", kwargs={
                "publisher_id": "PUB022",
                "name": "Bayview K12"
            }),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB022"}),

            Action(name="CreateProject", kwargs={
                "project_id": "PROJ1104",
                "publisher_id": "PUB022",
                "isbn": "978-1-3100-1013-2",
                "project_title": "Civics Basics, 1e",
                "default_hourly_rate": 80.0
            }),
            Action(name="GetProjectDetails", kwargs={"project_id": "PROJ1104"}),

            Action(name="ResolveHourlyRates", kwargs={"project_id_list": ["PROJ1104"]}),
            Action(name="CalculateInvoiceTotals", kwargs={
                "lines": [{"hours": 6, "rate": 80.0}],
                "hst_rate": 0.13
            }),

            Action(name="FetchInvoices", kwargs={"status": "open"}),
            Action(name="ComputeCollectionKpis", kwargs={"window_months": 12}),

            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-11"}),
            Action(name="InsertDashboardSnapshot", kwargs={
                "snapshot_date": "2024-11-30",
                "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-11.pdf"
            }),
            Action(name="GetDashboardSnapshotDetails", kwargs={"snapshot_date": "2024-11-30"}),
        ],
        outputs=[
            "PUB022 created & read; PROJ1104 created & read; rate resolved; total computed; open invoices reviewed; KPIs computed; AR_Aging_2024-11 exported; snapshot saved & read."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_085",
        instruction=(
            "Handle the normalization of contacts and perform a quick October‑2024 health assessment. Final outcome: consultant_id 'CONS001' phone is set to '+1-416-555-0177' and remains accessible; publisher_id 'PUB004' is accessible; open invoices are scrutinized and 12‑month KPIs are accessible; A/R aging details for '2024-10' are exported."
        ),
        actions=[
            Action(name="UpdateConsultantContact", kwargs={
                "consultant_id": "CONS001",
                "phone": "+1-416-555-0177"
            }),
            Action(name="GetConsultantProfile", kwargs={"consultant_id": "CONS001"}),

            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB004"}),

            Action(name="FetchInvoices", kwargs={"status": "open"}),
            Action(name="ComputeCollectionKpis", kwargs={"window_months": 12}),

            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-10"}),
        ],
        outputs=[
            "CONS001 phone updated & read; PUB004 read; open invoices reviewed; KPIs computed; AR_Aging_2024-10 exported."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_086",
        instruction=(
            "Coordinate the registration of a data‑science project and execute an October‑2024 risk evaluation for publisher_id 'PUB004'. Final outcome: project_id 'PROJ1105' is established with isbn '978-1-3100-1014-9', project_title 'Data Science Labs, 1e', default_hourly_rate 105.0 and remains accessible; a sample total is generated (4h @105.0 with hst_rate 0.13); A/R aging details for '2024-10' are exported and a snapshot is saved for '2024-10-31'; a risk assessment quantifies days outstanding for invoice_number '2024-024' using due_date '2024-10-31' as of '2024-11-10' and classifies it."
        ),
        actions=[
            Action(name="CreateProject", kwargs={
                "project_id": "PROJ1105",
                "publisher_id": "PUB004",
                "isbn": "978-1-3100-1014-9",
                "project_title": "Data Science Labs, 1e",
                "default_hourly_rate": 105.0
            }),
            Action(name="GetProjectDetails", kwargs={"project_id": "PROJ1105"}),

            Action(name="CalculateInvoiceTotals", kwargs={
                "lines": [{"hours": 4, "rate": 105.0}],
                "hst_rate": 0.13
            }),

            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-10"}),
            Action(name="InsertDashboardSnapshot", kwargs={
                "snapshot_date": "2024-10-31",
                "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-10.pdf"
            }),
            Action(name="GetDashboardSnapshotDetails", kwargs={"snapshot_date": "2024-10-31"}),

            Action(name="ComputeDaysOutstanding", kwargs={
                "invoices": [{"invoice_number": "2024-024", "period_end": "2024-10-31"}],
                "today": "2024-11-10"
            }),
            Action(name="CategorizeAging", kwargs={
                "aging": [{"invoice_number": "2024-024", "days_outstanding": 10}]
            }),
        ],
        outputs=[
            "PROJ1105 created & read; sample total; AR_Aging_2024-10 exported; snapshot saved & read; 2024-024 aging categorized."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_087",
        instruction=(
            "Handle a new publisher setup and prepare an August‑2024 snapshot. End state: publisher_id 'PUB023' named 'North Shore Academy' is established and accessible; contact_email matches 'accounts@northshoreacademy.ca' and is accessible; A/R aging for '2024-08' is exported and a snapshot is preserved for '2024-08-31'."
        ),
        actions=[
            Action(name="CreatePublisher", kwargs={
                "publisher_id": "PUB023",
                "name": "North Shore Academy"
            }),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB023"}),

            Action(name="UpdatePublisherContact", kwargs={
                "publisher_id": "PUB023",
                "contact_email": "accounts@northshoreacademy.ca"
            }),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB023"}),

            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-08"}),
            Action(name="InsertDashboardSnapshot", kwargs={
                "snapshot_date": "2024-08-31",
                "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-08.pdf"
            }),
            Action(name="GetDashboardSnapshotDetails", kwargs={"snapshot_date": "2024-08-31"}),
        ],
        outputs=[
            "PUB023 created & read; AP updated & read; AR_Aging_2024-08 exported; snapshot saved & read."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_088",
        instruction=(
            "Coordinate the reconciliation of July‑2024 A/R for publisher_id 'PUB002'. End state: publisher_id 'PUB002' remains accessible; a risk assessment measures days outstanding for invoice_number '2024-023' using due_date '2024-07-15' as of '2024-07-20' and categorizes accordingly; A/R aging for '2024-07' is exported, and a snapshot is retained for '2024-07-31'."
        ),
        actions=[
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB002"}),

            Action(name="ComputeDaysOutstanding", kwargs={
                "invoices": [{"invoice_number": "2024-023", "period_end": "2024-07-15"}],
                "today": "2024-07-20"
            }),
            Action(name="CategorizeAging", kwargs={
                "aging": [{"invoice_number": "2024-023", "days_outstanding": 5}]
            }),

            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-07"}),
            Action(name="InsertDashboardSnapshot", kwargs={
                "snapshot_date": "2024-07-31",
                "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-07.pdf"
            }),
            Action(name="GetDashboardSnapshotDetails", kwargs={"snapshot_date": "2024-07-31"}),
        ],
        outputs=[
            "PUB002 read; 2024-023 aging categorized; AR_Aging_2024-07 exported; snapshot saved & read."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_089",
        instruction=(
            "Handle a humanities project addition and coordinate an August‒2024 review alignment. End state: project_id 'PROJ1106' is created for 'PUB003' with isbn '978-1-3100-1015-6', project_title 'Philosophy Primer, 1e', default_hourly_rate 91.0, and is accessible; rates are determined for ['PROJ1106'] and a sample total is calculated (2h @91.0); A/R aging for '2024-08' is exported and a snapshot is saved for '2024-08-31'."
        ),
        actions=[
            Action(name="CreateProject", kwargs={
                "project_id": "PROJ1106",
                "publisher_id": "PUB003",
                "isbn": "978-1-3100-1015-6",
                "project_title": "Philosophy Primer, 1e",
                "default_hourly_rate": 91.0
            }),
            Action(name="GetProjectDetails", kwargs={"project_id": "PROJ1106"}),

            Action(name="ResolveHourlyRates", kwargs={"project_id_list": ["PROJ1106"]}),
            Action(name="CalculateInvoiceTotals", kwargs={
                "lines": [{"hours": 2, "rate": 91.0}],
                "hst_rate": 0.13
            }),

            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-08"}),
            Action(name="InsertDashboardSnapshot", kwargs={
                "snapshot_date": "2024-08-31",
                "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-08.pdf"
            }),
            Action(name="GetDashboardSnapshotDetails", kwargs={"snapshot_date": "2024-08-31"}),
        ],
        outputs=[
            "PROJ1106 created & read; rate resolved; total computed; AR_Aging_2024-08 exported; snapshot saved & read."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_090",
        instruction=(
            "Coordinate the update of billing contacts and prepare a November‒2024 confirmation calculation. End state: publisher_id 'PUB003' contact_email is set to 'ap@canopypress.ca' and is accessible; consultant_id 'CONS001' email is assigned as 'sarah.thompson+ar@consultingpro.ca' and is accessible; rates are determined for ['PROJ001','PROJ003'] and a sample total is calculated (2h @85.0 and 2h @75.0); A/R aging for '2024-11' is exported."
        ),
        actions=[
            Action(name="UpdatePublisherContact", kwargs={
                "publisher_id": "PUB003",
                "contact_email": "ap@canopypress.ca"
            }),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB003"}),

            Action(name="UpdateConsultantContact", kwargs={
                "consultant_id": "CONS001",
                "email": "sarah.thompson+ar@consultingpro.ca"
            }),
            Action(name="GetConsultantProfile", kwargs={"consultant_id": "CONS001"}),

            Action(name="ResolveHourlyRates", kwargs={"project_id_list": ["PROJ001", "PROJ003"]}),
            Action(name="CalculateInvoiceTotals", kwargs={
                "lines": [{"hours": 2, "rate": 85.0}, {"hours": 2, "rate": 75.0}],
                "hst_rate": 0.13
            }),

            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-11"}),
        ],
        outputs=[
            "PUB003 AP updated & read; CONS001 email updated & read; rates resolved; total computed; AR_Aging_2024-11 exported."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_091",
        instruction=(
            "Prepare a social studies project and reconcile a snapshot from July 2024. End state: project_id 'PROJ1109' is established for 'PUB005' with isbn '978-1-3100-1018-7', project_title 'Social Studies, 1e', default_hourly_rate 90.0 and is readable; sample totals (2h @90.0 and 2h @90.0) are calculated; A/R aging '2024-07' is exported and a snapshot saved for '2024-07-31'."
        ),
        actions=[
            Action(name="CreateProject", kwargs={
                "project_id": "PROJ1109",
                "publisher_id": "PUB005",
                "isbn": "978-1-3100-1018-7",
                "project_title": "Social Studies, 1e",
                "default_hourly_rate": 90.0
            }),
            Action(name="GetProjectDetails", kwargs={"project_id": "PROJ1109"}),

            Action(name="CalculateInvoiceTotals", kwargs={
                "lines": [{"hours": 2, "rate": 90.0}, {"hours": 2, "rate": 90.0}],
                "hst_rate": 0.13
            }),

            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-07"}),
            Action(name="InsertDashboardSnapshot", kwargs={
                "snapshot_date": "2024-07-31",
                "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-07.pdf"
            }),
            Action(name="GetDashboardSnapshotDetails", kwargs={"snapshot_date": "2024-07-31"}),
        ],
        outputs=[
            "PROJ1109 created & read; sample totals; AR_Aging_2024-07 exported; snapshot saved & read."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_092",
        instruction=(
            "Produce and deliver an invoice for December 2024 for publisher_id 'PUB004'. End state: invoice_number 'INV-2024-401' is created for 'PUB004' with invoice_date '2024-12-31', period_start '2024-12-01', period_end '2024-12-31', subtotal 1200.0, hst_amount 156.0, total_due 1356.0, pdf_path '/invoices/2024/INV-2024-401.pdf' and is readable; the invoice is sent via email from consultant_id 'CONS001' with subject 'Invoice INV-2024-401' and body_text 'December 2024 invoice attached.' and attachment '/invoices/2024/INV-2024-401.pdf'; an 'emailed' audit is documented and recorded."
        ),
        actions=[
            Action(name="InsertInvoice", kwargs={
                "invoice_number": "INV-2024-401",
                "publisher_id": "PUB004",
                "invoice_date": "2024-12-31",
                "period_start": "2024-12-01",
                "period_end": "2024-12-31",
                "subtotal": 1200.0,
                "hst_amount": 156.0,
                "total_due": 1356.0,
                "pdf_path": "/invoices/2024/INV-2024-401.pdf"
            }),
            Action(name="GetInvoiceDetails", kwargs={"invoice_number": "INV-2024-401"}),

            Action(name="SendInvoiceEmail", kwargs={
                "publisher_id": "PUB004",
                "consultant_id": "CONS001",
                "invoice_number": "INV-2024-401",
                "subject": "Invoice INV-2024-401",
                "body_text": "December 2024 invoice attached.",
                "attachment": "/invoices/2024/INV-2024-401.pdf"
            }),
            Action(name="RecordInvoiceAudit", kwargs={
                "invoice_number": "INV-2024-401",
                "event_type": "emailed"
            }),
            Action(name="ListInvoiceAudit", kwargs={"invoice_number": "INV-2024-401"}),
            Action(name="GetInvoiceDetails", kwargs={"invoice_number": "INV-2024-401"}),
        ],
        outputs=[
            "Invoice INV-2024-401 inserted & read; emailed; emailed audit recorded & listed; invoice re-read."
        ],
    ),    
    Task(
        annotator="A",
        user_id="ca_v4_093",
        instruction=(
            "Manage the normalization of contact information and conclude a September‑2024 review for publisher_id 'PUB001'. Final status: contact_email becomes 'ap@nelson-edu.ca' and is readable; invoice_number '2024-021' is readable; an audit event 'review_follow_up' is logged for '2024-021' and displayed; A/R aging for '2024-09' is exported and a dashboard snapshot is saved for '2024-09-30'; a swift risk analysis calculates days outstanding for '2024-021' using the due_date '2024-09-15' with today's date '2024-10-01' and classifies it."
        ),
        actions=[
            Action(name="UpdatePublisherContact", kwargs={
                "publisher_id": "PUB001",
                "contact_email": "ap@nelson-edu.ca"
            }),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB001"}),

            Action(name="GetInvoiceDetails", kwargs={"invoice_number": "2024-021"}),
            Action(name="RecordInvoiceAudit", kwargs={
                "invoice_number": "2024-021",
                "event_type": "review_follow_up"
            }),
            Action(name="ListInvoiceAudit", kwargs={"invoice_number": "2024-021"}),

            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-09"}),
            Action(name="InsertDashboardSnapshot", kwargs={
                "snapshot_date": "2024-09-30",
                "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-09.pdf"
            }),
            Action(name="GetDashboardSnapshotDetails", kwargs={"snapshot_date": "2024-09-30"}),

            Action(name="ComputeDaysOutstanding", kwargs={
                "invoices": [{"invoice_number": "2024-021", "due_date": "2024-09-15", "invoice_date": "2024-09-15"}],
                "today": "2024-10-01"
            }),
            Action(name="CategorizeAging", kwargs={
                "aging": [{"invoice_number": "2024-021", "days_outstanding": 16}]
            }),
        ],
        outputs=[
            "PUB001 AP updated & read; 2024-021 read; audit recorded & listed; AR_Aging_2024-09 exported; snapshot saved & read; 2024-021 aging categorized."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_094",
        instruction=(
            "Review and verify October‑2024 time tracking for a preliminary billing estimate. Final outcome: time entries for ['PROJ001','PROJ003'] from '2024-10-01' to '2024-10-31' are retrieved and validated; working hours are sorted by ISBN; rates are identified for ['PROJ001','PROJ003'] and a sample total is calculated (5h @85.0 and 3h @75.0); A/R aging for '2024-10' is exported and a dashboard snapshot is preserved for '2024-10-31' using that PDF; an audit 'reviewed' is documented for invoice_number '2024-010' and presented."
        ),
        actions=[
            Action(name="FetchTimeEntries", kwargs={
                "project_id_list": ["PROJ001", "PROJ003"],
                "period_start": "2024-10-01",
                "period_end": "2024-10-31"
            }),
            Action(name="ValidateTimeEntries", kwargs={"rows": []}),
            Action(name="GroupHoursByIsbn", kwargs={"rows": []}),

            Action(name="ResolveHourlyRates", kwargs={"project_id_list": ["PROJ001", "PROJ003"]}),
            Action(name="CalculateInvoiceTotals", kwargs={
                "lines": [{"hours": 5, "rate": 85.0}, {"hours": 3, "rate": 75.0}],
                "hst_rate": 0.13
            }),

            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-10"}),
            Action(name="InsertDashboardSnapshot", kwargs={
                "snapshot_date": "2024-10-31",
                "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-10.pdf"
            }),
            Action(name="GetDashboardSnapshotDetails", kwargs={"snapshot_date": "2024-10-31"}),

            Action(name="RecordInvoiceAudit", kwargs={
                "invoice_number": "2024-010",
                "event_type": "reviewed"
            }),
            Action(name="ListInvoiceAudit", kwargs={"invoice_number": "2024-010"}),
        ],
        outputs=[
            "Time entries fetched; validated; grouped; rates resolved; totals computed; AR_Aging_2024-10 exported; snapshot saved & read; audit recorded & listed."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_095",
        instruction=(
            "You prepare and dispatch an October‑2024 invoice for publisher_id 'PUB001'. End state: invoice_number 'INV-2024-230' exists with invoice_date '2024-10-31', period_start '2024-10-01', period_end '2024-10-31', subtotal 850.0, hst_amount 110.5, total_due 960.5, pdf_path '/invoices/2024/INV-2024-230.pdf' and is readable; the invoice is sent via email from consultant_id 'CONS001' with subject 'Invoice INV-2024-230' and body_text 'October 2024 invoice attached.' and attachment; an 'emailed' audit is recorded and listed."
        ),
        actions=[
            Action(name="InsertInvoice", kwargs={
                "invoice_number": "INV-2024-230",
                "publisher_id": "PUB001",
                "invoice_date": "2024-10-31",
                "period_start": "2024-10-01",
                "period_end": "2024-10-31",
                "subtotal": 850.0,
                "hst_amount": 110.5,
                "total_due": 960.5,
                "pdf_path": "/invoices/2024/INV-2024-230.pdf"
            }),
            Action(name="GetInvoiceDetails", kwargs={"invoice_number": "INV-2024-230"}),

            Action(name="SendInvoiceEmail", kwargs={
                "publisher_id": "PUB001",
                "consultant_id": "CONS001",
                "invoice_number": "INV-2024-230",
                "subject": "Invoice INV-2024-230",
                "body_text": "October 2024 invoice attached.",
                "attachment": "/invoices/2024/INV-2024-230.pdf"
            }),
            Action(name="RecordInvoiceAudit", kwargs={
                "invoice_number": "INV-2024-230",
                "event_type": "emailed"
            }),
            Action(name="ListInvoiceAudit", kwargs={"invoice_number": "INV-2024-230"}),
            Action(name="GetInvoiceDetails", kwargs={"invoice_number": "INV-2024-230"}),
        ],
        outputs=[
            "Invoice INV-2024-230 inserted & read; emailed; emailed audit recorded & listed; invoice re-read."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_096",
        instruction=(
            "You generate and send a September‑2024 invoice for publisher_id 'PUB005'. End state: invoice_number 'INV-2024-361' exists with invoice_date '2024-09-30', period_start '2024-09-01', period_end '2024-09-30', subtotal 765.0, hst_amount 99.45, total_due 864.45, pdf_path '/invoices/2024/INV-2024-361.pdf' and is readable; it is sent via email from consultant_id 'CONS001' with subject 'Invoice INV-2024-361' and body_text 'September 2024 invoice attached.' and attachment; an 'emailed' audit is recorded and listed."
        ),
        actions=[
            Action(name="InsertInvoice", kwargs={
                "invoice_number": "INV-2024-361",
                "publisher_id": "PUB005",
                "invoice_date": "2024-09-30",
                "period_start": "2024-09-01",
                "period_end": "2024-09-30",
                "subtotal": 765.0,
                "hst_amount": 99.45,
                "total_due": 864.45,
                "pdf_path": "/invoices/2024/INV-2024-361.pdf"
            }),
            Action(name="GetInvoiceDetails", kwargs={"invoice_number": "INV-2024-361"}),

            Action(name="SendInvoiceEmail", kwargs={
                "publisher_id": "PUB005",
                "consultant_id": "CONS001",
                "invoice_number": "INV-2024-361",
                "subject": "Invoice INV-2024-361",
                "body_text": "September 2024 invoice attached.",
                "attachment": "/invoices/2024/INV-2024-361.pdf"
            }),
            Action(name="RecordInvoiceAudit", kwargs={
                "invoice_number": "INV-2024-361",
                "event_type": "emailed"
            }),
            Action(name="ListInvoiceAudit", kwargs={"invoice_number": "INV-2024-361"}),
            Action(name="GetInvoiceDetails", kwargs={"invoice_number": "INV-2024-361"}),
        ],
        outputs=[
            "Invoice INV-2024-361 inserted & read; emailed; emailed audit recorded & listed; invoice re-read."
        ],
    ),  
    Task(
        annotator="A",
        user_id="ca_v4_097",
        instruction=(
            "Handle updates to October‑2024 contacts and conduct KPIs with a brief risk assessment. End state: publisher_id 'PUB004' contact_email is set to 'ap@bluepeakpublishing.ca' and remains accessible; open invoices undergo evaluation and 12‑month KPIs should be available; A/R aging for '2024-10' is exported and a snapshot is stored for '2024-10-31'; regarding risk, days outstanding are calculated for invoice_number '2024-024' using due_date '2024-10-31' as of '2024-11-05' and classified."
        ),
        actions=[
            Action(name="UpdatePublisherContact", kwargs={
                "publisher_id": "PUB004",
                "contact_email": "ap@bluepeakpublishing.ca"
            }),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB004"}),

            Action(name="FetchInvoices", kwargs={"status": "open"}),
            Action(name="ComputeCollectionKpis", kwargs={"window_months": 12}),

            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-10"}),
            Action(name="InsertDashboardSnapshot", kwargs={
                "snapshot_date": "2024-10-31",
                "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-10.pdf"
            }),
            Action(name="GetDashboardSnapshotDetails", kwargs={"snapshot_date": "2024-10-31"}),

            Action(name="ComputeDaysOutstanding", kwargs={
                "invoices": [{"invoice_number": "2024-024", "due_date": "2024-10-31", "invoice_date": "2024-10-31"}],
                "today": "2024-11-05"
            }),
            Action(name="CategorizeAging", kwargs={
                "aging": [{"invoice_number": "2024-024", "days_outstanding": 5}]
            }),
        ],
        outputs=[
            "PUB004 AP updated & read; open invoices reviewed; KPIs computed; AR_Aging_2024-10 exported; snapshot saved & read; 2024-024 aging categorized."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_098",
        instruction=(
            "Coordinate the composition and emailing of an August‑2024 invoice for publisher_id 'PUB003'. End state: invoice_number 'INV-2024-209' is created with invoice_date '2024-08-31', period_start '2024-08-01', period_end '2024-08-31', subtotal 875.0, hst_amount 113.75, total_due 988.75, pdf_path '/invoices/2024/INV-2024-209.pdf' and remains accessible; the invoice is sent via email from consultant_id 'CONS001' with subject 'Invoice INV-2024-209' and body_text 'August 2024 invoice attached.' including the attachment; an 'emailed' audit entry is documented and listed."
        ),
        actions=[
            Action(name="InsertInvoice", kwargs={
                "invoice_number": "INV-2024-209",
                "publisher_id": "PUB003",
                "invoice_date": "2024-08-31",
                "period_start": "2024-08-01",
                "period_end": "2024-08-31",
                "subtotal": 875.0,
                "hst_amount": 113.75,
                "total_due": 988.75,
                "pdf_path": "/invoices/2024/INV-2024-209.pdf"
            }),
            Action(name="GetInvoiceDetails", kwargs={"invoice_number": "INV-2024-209"}),

            Action(name="SendInvoiceEmail", kwargs={
                "publisher_id": "PUB003",
                "consultant_id": "CONS001",
                "invoice_number": "INV-2024-209",
                "subject": "Invoice INV-2024-209",
                "body_text": "August 2024 invoice attached.",
                "attachment": "/invoices/2024/INV-2024-209.pdf"
            }),
            Action(name="RecordInvoiceAudit", kwargs={
                "invoice_number": "INV-2024-209",
                "event_type": "emailed"
            }),
            Action(name="ListInvoiceAudit", kwargs={"invoice_number": "INV-2024-209"}),
            Action(name="GetInvoiceDetails", kwargs={"invoice_number": "INV-2024-209"}),
        ],
        outputs=[
            "Invoice INV-2024-209 inserted & read; emailed; emailed audit recorded & listed; invoice re-read."
        ],
    ),
    Task(
        annotator="A",
        user_id="ca_v4_099",
        instruction=(
            "Coordinate the alignment of a November‑2024 invoice for publisher_id 'PUB001' and verify delivery. End state: invoice_number 'INV-2024-231' exists with invoice_date '2024-11-30', period_start '2024-11-01', period_end '2024-11-30', subtotal 900.0, hst_amount 117.0, total_due 1017.0, pdf_path '/invoices/2024/INV-2024-231.pdf' and is readable; it is emailed from consultant_id 'CONS001' with subject 'Invoice INV-2024-231' and body_text 'November 2024 invoice attached.' and attachment; an 'emailed' audit is recorded and listed."
        ),
        actions=[
            Action(name="InsertInvoice", kwargs={
                "invoice_number": "INV-2024-231",
                "publisher_id": "PUB001",
                "invoice_date": "2024-11-30",
                "period_start": "2024-11-01",
                "period_end": "2024-11-30",
                "subtotal": 900.0,
                "hst_amount": 117.0,
                "total_due": 1017.0,
                "pdf_path": "/invoices/2024/INV-2024-231.pdf"
            }),
            Action(name="GetInvoiceDetails", kwargs={"invoice_number": "INV-2024-231"}),

            Action(name="SendInvoiceEmail", kwargs={
                "publisher_id": "PUB001",
                "consultant_id": "CONS001",
                "invoice_number": "INV-2024-231",
                "subject": "Invoice INV-2024-231",
                "body_text": "November 2024 invoice attached.",
                "attachment": "/invoices/2024/INV-2024-231.pdf"
            }),
            Action(name="RecordInvoiceAudit", kwargs={
                "invoice_number": "INV-2024-231",
                "event_type": "emailed"
            }),
            Action(name="ListInvoiceAudit", kwargs={"invoice_number": "INV-2024-231"}),
            Action(name="GetInvoiceDetails", kwargs={"invoice_number": "INV-2024-231"}),
        ],
        outputs=[
            "Invoice INV-2024-231 inserted & read; emailed; emailed audit recorded & listed; invoice re-read."
        ],
    ),

    Task(
        annotator="A",
        user_id="ca_v4_100",
        instruction=(
            "Facilitate the onboarding of 'Everest Academy' and execute an October‑2024 check. End state: publisher_id 'PUB024' named 'Everest Academy' exists and is readable; open invoices are reviewed and 12‑month KPIs are available; rates are resolved for ['PROJ001'] and a sample total is computed (2h @85.0); A/R aging '2024-10' is exported and a snapshot stored for '2024-10-31'; for risk assessment, calculate days outstanding for invoice_number '2024-021' using due_date '2024-09-15' as of '2024-10-10' and categorize it."
        ),
        actions=[
            Action(name="CreatePublisher", kwargs={
                "publisher_id": "PUB024",
                "name": "Everest Academy"
            }),
            Action(name="GetPublisherInfo", kwargs={"publisher_id": "PUB024"}),

            Action(name="FetchInvoices", kwargs={"status": "open"}),
            Action(name="ComputeCollectionKpis", kwargs={"window_months": 12}),

            Action(name="ResolveHourlyRates", kwargs={"project_id_list": ["PROJ001"]}),
            Action(name="CalculateInvoiceTotals", kwargs={
                "lines": [{"hours": 2, "rate": 85.0}],
                "hst_rate": 0.13
            }),

            Action(name="ExportArAgingReport", kwargs={"period_label": "2024-10"}),
            Action(name="InsertDashboardSnapshot", kwargs={
                "snapshot_date": "2024-10-31",
                "pdf_path": "https://storage.example.com/reports/AR_Aging_2024-10.pdf"
            }),
            Action(name="GetDashboardSnapshotDetails", kwargs={"snapshot_date": "2024-10-31"}),

            Action(name="ComputeDaysOutstanding", kwargs={
                "invoices": [{"invoice_number": "2024-021", "due_date": "2024-09-15", "invoice_date": "2024-09-15"}],
                "today": "2024-10-10"
            }),
            Action(name="CategorizeAging", kwargs={
                "aging": [{"invoice_number": "2024-021", "days_outstanding": 25}]
            }),
        ],
        outputs=[
            "PUB024 created & read; open invoices reviewed; KPIs computed; rate resolved; total computed; AR_Aging_2024-10 exported; snapshot saved & read; 2024-021 aging categorized."
        ],
    ),
]