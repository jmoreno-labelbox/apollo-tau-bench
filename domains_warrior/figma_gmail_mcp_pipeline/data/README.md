# Figma-Gmail MCP Pipeline Mock Database

This directory contains a comprehensive mock database for testing and developing the Figma-Gmail MCP Pipeline workflows. The database includes realistic data with proper foreign key relationships and supports all 4 main workflow tasks.

## Database Schema Overview

### Core Entities (Figma and Gmail)
- **`figma_artifacts.json`** - Figma design artifacts (files, pages, frames)
- **`assets.json`** - Exported assets from Figma artifacts
- **`gmail_threads.json`** - Email thread information
- **`gmail_messages.json`** - Individual email messages
- **`figma_comments.json`** - Comments on Figma artifacts

### Task 1: Review Workflow
- **`review_cycles.json`** - Design review cycle tracking
- **`review_approvals.json`** - Individual approvals within cycles

### Task 2: Release Workflow
- **`releases.json`** - Figma version releases
- **`release_diffs.json`** - Changes between releases

### Task 3: Audit Workflow
- **`audits.json`** - Design system and accessibility audits
- **`audit_findings_ds.json`** - Design system mapping findings
- **`audit_findings_a11y.json`** - Accessibility violation findings

### Task 4: Fix Plan Workflow
- **`fix_plans.json`** - Remediation plan management
- **`fix_items.json`** - Individual fix suggestions

### System Configuration and Logs
- **`system_config.json`** - Workflow configurations and settings
- **`terminal_logs.json`** - System operation logs

## Task Workflows

### Task 1: Email-Centric Design Review & Approval

**Purpose:** Facilitate email-based reviews of Figma designs with bidirectional feedback sync.

**Key Data Tables:**
- `figma_artifacts` - Frames tagged with "needs-review"
- `assets` - Exported PNG assets for review emails
- `review_cycles` - Review lifecycle (IN_FLIGHT → NEEDS_REVIEW → APPROVED/CHANGES_REQUESTED)
- `gmail_threads` - Email threads with Design/ labels
- `gmail_messages` - Review request emails and replies
- `figma_comments` - Feedback sync between Gmail and Figma
- `review_approvals` - Approval tracking and quorum management
- `system_config` - Review workflow settings

**Workflow Example:**
1. Detect frames tagged "needs-review" in `figma_artifacts`
2. Export frames to `assets` with PNG 2x profile
3. Create `review_cycles` entry with SLA deadline
4. Send review email via `gmail_threads` and `gmail_messages`
5. Monitor replies and sync to `figma_comments`
6. Track approvals in `review_approvals`
7. Update status based on quorum rules

**Key Features:**
- DLP pre-send checks on email content
- Intent keyword parsing (APPROVE, CHANGES, BLOCKER)
- Approval quorum management
- SLA breach escalation
- Bidirectional feedback sync

### Task 2: Release Notes & Asset Handoff

**Purpose:** Generate and distribute release notes when design milestones are reached.

**Key Data Tables:**
- `releases` - Version releases with "release/" prefix
- `release_diffs` - Detailed change tracking (frames added/updated/removed)
- `assets` - Hero frames and before/after visuals
- `gmail_threads` - Release email threads
- `gmail_messages` - HTML release notes with structured content
- `system_config` - Release workflow settings

**Workflow Example:**
1. Detect "release/" version events in `releases`
2. Compute diffs and store in `release_diffs`
3. Export hero frames to `assets`
4. Generate before/after visuals
5. Compose HTML release emails in `gmail_messages`
6. Send to stakeholders via `gmail_threads`

**Key Features:**
- Version diff computation
- Hero frame export
- Before/after visual generation
- Structured HTML email composition
- Attachment policy management

### Task 3: Design System Audit & Accessibility Check

**Purpose:** Audit Figma designs for DS compliance and accessibility standards.

**Key Data Tables:**
- `audits` - Combined DS/A11y audit sessions
- `audit_findings_ds` - Design system mapping findings
- `audit_findings_a11y` - Accessibility violation findings
- `assets` - PDF audit reports
- `system_config` - Audit workflow settings

**Workflow Example:**
1. Initialize audit session in `audits`
2. Identify custom groups and map to DS components
3. Record findings in `audit_findings_ds` (UNMAPPED, SUBSTITUTE_RECOMMENDED, AMBIGUOUS)
4. Evaluate accessibility in `audit_findings_a11y` (TOUCH_TARGET, CONTRAST, TEXT_SIZING, RTL)
5. Generate PDF report in `assets`
6. Update audit status to COMPLETED

**Key Features:**
- Component mapping with Code Connect links
- Touch target evaluation (44x44px minimum)
- Contrast ratio checking (4.5:1 threshold)
- Text sizing validation (16px minimum)
- RTL compliance checking
- Comprehensive PDF reporting

### Task 4: Minimal Fix Plan & Handoff

**Purpose:** Convert audit findings into actionable remediation steps.

**Key Data Tables:**
- `fix_plans` - Fix plan lifecycle management
- `fix_items` - Prioritized fix suggestions
- `figma_comments` - Anchored fix comments
- `system_config` - Fix workflow settings

**Workflow Example:**
1. Load audit findings from Tasks 3
2. Prioritize by severity, impact, and ease of fix
3. Apply change budget (5 items max per frame)
4. Generate fix suggestions in `fix_items`
5. Deliver via chosen method:
   - **COMMENTS:** Post anchored Figma comments
   - **TICKETS:** Create external tracker tickets
   - **PDF:** Export handoff document
6. Notify owners and schedule follow-up

**Key Features:**
- Change budget management
- Multiple delivery methods
- Code Connect snippet attachment
- Deferral handling for budget-exceeding items
- Owner assignment and notification
- Follow-up audit scheduling

## Data Relationships

### Foreign Key Relationships
- `assets.artifact_id_nullable` → `figma_artifacts.artifact_id`
- `review_cycles.artifact_id` → `figma_artifacts.artifact_id`
- `review_cycles.thread_id_nullable` → `gmail_threads.thread_id`
- `gmail_messages.thread_id` → `gmail_threads.thread_id`
- `figma_comments.artifact_id` → `figma_artifacts.artifact_id`
- `review_approvals.cycle_id` → `review_cycles.cycle_id`
- `releases.thread_id_nullable` → `gmail_threads.thread_id`
- `release_diffs.release_id` → `releases.release_id`
- `audits.artifact_id` → `figma_artifacts.artifact_id`
- `audit_findings_ds.audit_id` → `audits.audit_id`
- `audit_findings_a11y.audit_id` → `audits.audit_id`
- `fix_plans.audit_id` → `audits.audit_id`
- `fix_items.plan_id` → `fix_plans.plan_id`
- `fix_items.finding_id` → `audit_findings_ds.finding_id` or `audit_findings_a11y.finding_id`

### Cross-Task Data Flow
1. **Task 1 → Task 2:** Approved designs from review cycles become release candidates
2. **Task 3 → Task 4:** Audit findings become inputs for fix plan generation
3. **All Tasks → Logs:** Complete workflow tracking in terminal_logs

## Configuration

### System Configuration (`system_config.json`)
- **Review Workflow:** Export profiles, Gmail limits, SLA settings, approval quorum
- **Release Workflow:** Stakeholder aliases, attachment policies, email templates
- **Audit Workflow:** Component maps, Code Connect settings, A11y guidelines
- **Fix Workflow:** Change budgets, delivery methods, ownership mapping

### Key Settings
- **Change Budget:** 5 items maximum per frame
- **Touch Target Minimum:** 44x44px
- **Contrast Threshold:** 4.5:1 ratio
- **Text Size Minimum:** 16px for body content
- **Follow-up Cadence:** 2 weeks
- **Delivery Methods:** COMMENTS, TICKETS, PDF

## Usage Examples

### Testing Task 1
```json
// Find frames needing review
SELECT * FROM figma_artifacts WHERE 'needs-review' IN current_tags;

// Check review cycles
SELECT * FROM review_cycles WHERE status = 'NEEDS_REVIEW';

// Verify email threads
SELECT * FROM gmail_threads WHERE 'Design/Needs-Review' IN current_labels;
```

### Testing Task 2
```json
// Find release events
SELECT * FROM releases WHERE version_tag LIKE 'release/%';

// Check release diffs
SELECT * FROM release_diffs WHERE release_id = 'release_011';

// Verify release emails
SELECT * FROM gmail_threads WHERE 'Design/Release' IN current_labels;
```

### Testing Task 3
```json
// Find audit sessions
SELECT * FROM audits WHERE audit_type = 'COMBINED_DS_A11Y';

// Check DS findings
SELECT * FROM audit_findings_ds WHERE finding_type = 'UNMAPPED';

// Check A11y findings
SELECT * FROM audit_findings_a11y WHERE violation_type = 'TOUCH_TARGET';
```

### Testing Task 4
```json
// Find fix plans
SELECT * FROM fix_plans WHERE status = 'ARCHIVED';

// Check fix items
SELECT * FROM fix_items WHERE status = 'PENDING';

// Verify comments
SELECT * FROM figma_comments WHERE author_email LIKE '%bot@company.com';
```

## Data Quality

### Realistic Mock Data
- **5-10 rows per table** as required
- **Proper foreign key relationships** maintained
- **Realistic file sizes** and timestamps
- **Authentic email content** and Figma metadata
- **Consistent user assignments** across workflows

### Workflow States
- **Review Cycles:** IN_FLIGHT → NEEDS_REVIEW → APPROVED/CHANGES_REQUESTED/ESCALATED
- **Audits:** RUNNING → COMPLETED
- **Fix Plans:** DRAFTED → DELIVERED → ARCHIVED
- **Fix Items:** PENDING → APPLIED/DEFERRED

This mock database provides a comprehensive foundation for testing and developing the Figma-Gmail MCP Pipeline workflows with realistic data and proper relationships.
