# Consulting Accounting Domain Data

This directory contains the JSON data files that simulate the operational database for a solo consulting business. The data is designed to be rich and interconnected, supporting a variety of business automation tasks from invoicing and expense tracking to cash flow forecasting.

## JSON File Descriptions

This section details the purpose and structure of each data file.

-   **`consultants.json`**: Stores the profile information for the consultant, including contact details and tax information.
-   **`publishers.json`**: Acts as the client database, containing information for each publisher the consultant works with.
-   **`projects.json`**: Details each project undertaken, linking publishers to specific work items. It includes metadata like ISBN, title, and hourly rates.
-   **`time_entries.json`**: A log of all billable hours worked on various projects. Each entry is linked to a specific project.
-   **`invoices.json`**: Contains the header information for every invoice, including totals, payment status (`paid_at`), and links to publishers.
-   **`invoice_lines.json`**: Provides the detailed line items for each invoice, linking back to projects and showing hours billed and rates applied.
-   **`invoice_audit.json`**: A complete audit trail for each invoice, tracking events like creation, emailing, payment reminders, and escalations.
-   **`expenses.json`**: A comprehensive log of all business expenses, from office supplies to travel. Each expense is categorized for tax purposes.
-   **`expense_categories.json`**: Defines the different categories for expenses and specifies the percentage of the expense that is tax-deductible.
-   **`tax_rates.json`**: Stores the provisional tax rates for different years, used for calculating tax reserves.
-   **`payment_behavior.json`**: Models the historical payment patterns of each publisher, crucial for accurate cash flow forecasting.
-   **`recurring_schedules.json`**: Lists all fixed and recurring financial commitments, such as rent, subscriptions, tax payments, and owner draws.
-   **`pipeline_opportunities.json`**: Tracks potential future projects, including estimated revenue, probability of closing, and expected timelines.
-   **`bank_accounts.json`**: Lists all business bank accounts, credit cards, and lines of credit with their current balances.
-   **`dashboard_snapshots.json`**: Stores summary data for key business dashboards (e.g., YTD revenue) at specific points in time.
-   **`project_revenue.json`**: A data store for aggregated revenue per project, typically linked to a dashboard snapshot.
-   **`monthly_revenue.json`**: A data store for aggregated revenue per month, also linked to a dashboard snapshot.
-   **`scheduler_runs.json`**: A log of all automated tasks that have been executed, recording their status and linking to any generated artifacts.

---

## Task to Data Mapping

This section explains how the tasks defined in `proposal.md` interact with the JSON data files.

### Task 1: A/R Aging Report

This task automates the process of tracking and following up on unpaid invoices.

-   **Input/Read**:
    -   Reads open invoices from `invoices.json` (`paid_at` is null).
    -   Looks up client contact details from `publishers.json`.
    -   Uses historical payment data from `invoices.json` (paid invoices) to compute KPIs.
-   **Output/Write**:
    -   Updates existing or creates new entries in `invoices.json` from an external source.
    -   Can create new client entries in `publishers.json` if they don't exist.
    -   Records all follow-up actions (emails, calls) as new entries in `invoice_audit.json`.
    -   Saves a summary of the report to `dashboard_snapshots.json`.
    -   Logs the successful execution of the task in `scheduler_runs.json`.

### Task 2: YTD Revenue Dashboard

This task generates a year-to-date financial dashboard.

-   **Input/Read**:
    -   Aggregates invoice data from `invoices.json` for the current year.
    -   Retrieves project details from `projects.json`.
    -   Fetches the current tax rate from `tax_rates.json`.
-   **Output/Write**:
    -   Creates a new entry in `dashboard_snapshots.json` with the YTD figures.
    -   Populates `project_revenue.json` with per-project revenue totals for the snapshot.
    -   Populates `monthly_revenue.json` with per-month revenue totals for the snapshot.
    -   Logs the task execution in `scheduler_runs.json`.

### Task 3: Expense Tracking

This task captures and categorizes business expenses from receipts.

-   **Input/Read**:
    -   Reads `expense_categories.json` to classify expenses and apply the correct tax deductibility rules.
-   **Output/Write**:
    -   Creates new entries for each processed receipt in `expenses.json`.
    -   Logs the successful run of the expense tracker task in `scheduler_runs.json`.

### Task 4: Cash Flow Forecasting

This task projects future cash flow based on receivables, pipeline, and scheduled expenses.

-   **Input/Read**:
    -   Reads starting balances from `bank_accounts.json`.
    -   Loads all open invoices from `invoices.json`.
    -   Uses client-specific payment patterns from `payment_behavior.json` to predict payment dates.
    -   Loads future revenue estimates from `pipeline_opportunities.json`.
    -   Loads all scheduled and recurring outflows from `recurring_schedules.json`.
    -   Uses historical `expenses.json` to forecast variable spending.
    -   Reads tax rates from `tax_rates.json` for tax payment planning.
-   **Output/Write**:
    -   Saves the generated forecast report as a new `dashboard_snapshots.json` entry.
    -   Logs the execution of the forecast in `scheduler_runs.json`.

### Task 5: Invoice Generation

This task automates the creation and sending of new invoices for billable work.

-   **Input/Read**:
    -   Reads consultant's details from `consultants.json`.
    -   Reads client's details from `publishers.json`.
    -   Fetches all unbilled work from `time_entries.json` for a given period.
    -   Looks up project details and hourly rates from `projects.json`.
-   **Output/Write**:
    -   Creates a new invoice header in `invoices.json`.
    -   Creates the corresponding detailed line items in `invoice_lines.json`.
    -   Records the "generated" and "emailed" events in `invoice_audit.json`.
    -   Can update the consultant's details in `consultants.json` if necessary.
