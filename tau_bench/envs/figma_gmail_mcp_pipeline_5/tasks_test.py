from tau_bench.types import Action, Task

TASKS = [
    Task(
        annotator="0",
        user_id="MED_1",
        instruction="As a cross-channel design-review posture coordinator, your responsibilities include ensuring triage consistency, policy alignment, and audit-ready traceability across Gmail and Figma. The focus is on the Gmail conversation labeled 'design-review' involving chris.engineer@company.com, where the subject contains the keyword 'Design'. The active conversation under consideration is thread_001, which requires a standardized triage posture and eligibility for synchronization. Ensure alignment with the organization's DLP configuration and intent keywords to maintain secure communication and consistent stakeholder reporting. The coordination goal is to create a stakeholder-ready record in which thread_001 shows a triaged, figma-sync status with the 'urgent' designation removed effective 2024-08-22T12:00:00Z. A DLP assessment should confirm the conversation is clean, offering timestamped evidence for audit transparency and Figma synchronization. Constants to maintain: label design-review; participant chris.engineer@company.com; keyword Design; thread_id thread_001; add_labels [triaged, figma-sync]; remove_labels [urgent]; changed_ts 2024-08-22T12:00:00Z.",
        actions=[
            Action(name="SearchGmailThreads", kwargs={"label": "design-review", "participant": "chris.engineer@company.com", "keyword": "Design"}),
            Action(name="UpdateThreadLabels", kwargs={"thread_id": "thread_001", "add_labels": ["triaged", "figma-sync"], "remove_labels": ["urgent"], "changed_ts": "2024-08-22T12:00:00Z"}),
            Action(name="DlpScanThread", kwargs={"thread_id": "thread_001"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="MED_2",
        instruction=(
            "Draft a succinct release announcement and verify changes for release_001 without over-detailing the process. Consider the public release catalog under version_prefix release/ (artifact_id None) as the framework for change verification, after which you'll prepare a message in thread_006 from emma.creative@company.com at 2024-08-22T17:00:00Z. Make sure the announcement uses the subject 'Release 1.2.0 Announcement' and contains the body text 'Highlights and changes included.' to track the resulting draft id. Adhere strictly to constants: version_prefix release/, artifact_id None, release_id release_001, thread_id thread_006, from_email emma.creative@company.com, created_ts 2024-08-22T17:00:00Z, subject 'Release 1.2.0 Announcement', body 'Highlights and changes included.'."
        ),
        actions=[
            Action(name="ListReleases", kwargs={"version_prefix": "release/", "artifact_id": None}),
            Action(name="GetReleaseDiffSummary", kwargs={"release_id": "release_001"}),
            Action(name="ComposeReleaseEmailDraft", kwargs={"release_id": "release_001", "thread_id": "thread_006", "from_email": "emma.creative@company.com", "created_ts": "2024-08-22T17:00:00Z", "subject": "Release 1.2.0 Announcement", "body": "Highlights and changes included."})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="MED_3",
        instruction=(
            "You are responsible for the audit follow-up of art_001. Your objective is to ensure that the completed findings are comprehended, a new combined design-system/accessibility review exists, and the preparation is logged with the appropriate configuration context. Ground your reasoning using these fixed references: artifact_id art_001, status COMPLETED, audit_id audit_001, created_ts 2024-08-23T09:00:00Z, audit_type COMBINED_DS_A11Y, config_key dlp_config, log_ts 2024-08-23T09:05:00Z, message 'Prepared audit session for art_001'. Avoid listing prescriptive steps; it is expected that the mentioned identifiers and timestamps are incorporated in the updated state and the final note."
        ),
        actions=[
            Action(name="ListAudits", kwargs={"artifact_id": "art_001", "status": "COMPLETED"}),
            Action(name="SummarizeAudit", kwargs={"audit_id": "audit_001"}),
            Action(name="CreateAuditSession", kwargs={"artifact_id": "art_001", "created_ts": "2024-08-23T09:00:00Z", "audit_type": "COMBINED_DS_A11Y"}),
            Action(name="ReadSystemConfig", kwargs={"config_key": "dlp_config"}),
            Action(name="LogTerminalEvent", kwargs={"log_ts": "2024-08-23T09:05:00Z", "message": "Prepared audit session for art_001"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="MED_4",
        instruction=(
            "You are coordinating the release announcement, ensuring the safety of the draft and label alignment for the 1.4.0 rollout. Sustain a compliant stance for the current Release 1.4.0 conversation and portray a clear draft state without prescribing the order of steps. Employ the constants: release_id release_004, thread_id thread_008, message_id relmsg_f9e9c1b6, from_email emma.creative@company.com, created_ts 2024-08-23T16:30:00Z, changed_ts 2024-08-23T16:35:00Z, subject 'Release 1.4.0 Announcement', body 'Changelog and new components included.'"
        ),
        actions=[
            Action(name="ComposeReleaseEmailDraft", kwargs={
                "release_id": "release_004",
                "thread_id": "thread_008",
                "from_email": "emma.creative@company.com",
                "created_ts": "2024-08-23T16:30:00Z",
                "subject": "Release 1.4.0 Announcement",
                "body": "Changelog and new components included."
            }),
            Action(name="GuardAttachmentPolicyOnDraft", kwargs={"message_id": "relmsg_f9e9c1b6"}),
            Action(name="UpdateThreadLabels", kwargs={
                "thread_id": "thread_008",
                "add_labels": ["release-draft"],
                "remove_labels": [],
                "changed_ts": "2024-08-23T16:35:00Z"
            }),
            Action(name="DlpScanThread", kwargs={"thread_id": "thread_008"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="MED_5",
        instruction="Act as a release communications and DLP posture steward for the Design Tokens update. Your role involves managing the traceability and audit-grade labeling of stakeholder-safe announcements through Gmail collaboration threads while being mindful of the Figma library token context. Work is tied to release release_011 and focuses on discussion thread thread_013 related to pm.lead@company.com; the announcement is set as “Candidate build ready for stakeholder walkthrough.” with a timestamp of 2024-08-23T19:20:00Z. Ensure policy context is consistent with the organization's DLP settings and intent keywords to maintain safe, consistent, and reportable communication, enabling deterministic outcomes in downstream dashboards and audit logs. The expected outcome is: the Gmail thread shows the candidate announcement at the specified time, and the DLP posture of the thread is evaluated once; if any sensitive terms are found, the thread receives a dlp-flag label with timestamped traceability at 2024-08-23T19:22:00Z, otherwise no label is applied. Constants: release_id release_011; thread_id thread_013; from_email pm.lead@company.com; created_ts 2024-08-23T19:20:00Z; body “Candidate build ready for stakeholder walkthrough.”; dlp_label_if_found dlp-flag with dlp_changed_ts 2024-08-23T19:22:00Z.",
        actions=[
            Action(name="AppendMessageToThread", kwargs={
                "thread_id": "thread_013",
                "from_email": "pm.lead@company.com",
                "body": "Candidate build ready for stakeholder walkthrough.",
                "created_ts": "2024-08-23T19:20:00Z"
            }),
            Action(name="DlpScanAndLabelThread", kwargs={
                "thread_id": "thread_013",
                "label_if_found": "dlp-flag",
                "changed_ts": "2024-08-23T19:22:00Z"
            })
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="MED_6",
        instruction=(
            "Serve as a design-system release coordination owner, ensuring that announcements are in line with catalog scope and safety posture. Handle the design-system navigation update without dictating the sequence of tools and conclude by scanning the DLP thread. Use the following constants: version_prefix release/, release_id release_006, thread_id thread_010, from_email emma.creative@company.com, created_ts 2024-08-23T18:20:00Z, subject 'Design System v1.1.0 - Navigation Components', body 'Tokens and components updated.'"
        ),
        actions=[
            Action(name="GetReleaseDiffSummary", kwargs={"release_id": "release_006"}),
            Action(name="ComposeReleaseEmailDraft", kwargs={
                "release_id": "release_006",
                "thread_id": "thread_010",
                "from_email": "emma.creative@company.com",
                "created_ts": "2024-08-23T18:20:00Z",
                "subject": "Design System v1.1.0 - Navigation Components",
                "body": "Tokens and components updated."
            }),
            Action(name="DlpScanThread", kwargs={"thread_id": "thread_010"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="MED_7",
        instruction=(
            "As a Figma accessibility coordination specialist, your role involves aligning dashboard header compliance and ensuring audit traceability. Focus your efforts on the dashboard header frame art_004, managed by jake.design@company.com, within the dashboard working set; the area of interest includes the FRAME type modified since 2024-08-01T00:00:00Z. Maintain policy context in line with the organization's dlp configuration and intent keywords to guarantee secure, uniform communication and precise stakeholder reporting. The goal of your coordination is to produce a brief, stakeholder-prepared summary of the finalized audit audit_004 and an artifact status marked as a11y-reviewed, complete with timestamped traceability. Constants: owner_email jake.design@company.com, tag dashboard, artifact_type FRAME, modified_since 2024-08-01T00:00:00Z, artifact_id art_004, audit_id audit_004, tag a11y-reviewed at 2024-08-23T18:30:00Z."
        ),
        actions=[
            Action(name="ReadSystemConfig", kwargs={"config_key": "dlp_config"}),
            Action(name="ReadSystemConfig", kwargs={"config_key": "intent_keywords"}),
            Action(name="ListArtifacts", kwargs={
                "owner_email": "jake.design@company.com",
                "tag": "dashboard",
                "artifact_type": "FRAME",
                "modified_since": "2024-08-01T00:00:00Z"
            }),
            Action(name="ListAudits", kwargs={"artifact_id": "art_004", "status": "COMPLETED"}),
            Action(name="SummarizeAudit", kwargs={"audit_id": "audit_004"}),
            Action(name="AddArtifactTag", kwargs={
                "artifact_id": "art_004",
                "tag": "a11y-reviewed",
                "changed_ts": "2024-08-23T18:30:00Z"
            })
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="MED_8",
        instruction=(
            "Act as a review progression and approval traceability owner for pricing components, ensuring that the status aligns with stakeholder expectations and audit-grade documentation is maintained. Your work centers on the active cycle cycle_008, focusing on deterministic timing, explicit approver identification, and policy-compliant visibility. Record the approval with pm.lead@company.com marked as APPROVED at 2024-08-23T20:10:00Z along with the note 'Looks good to ship.', and update an operational note 'Approval recorded for pricing review' at 2024-08-23T20:12:00Z for traceability. Ensure the review state indicates a final APPROVED status by 2024-08-23T20:15:00Z to maintain consistent release readiness and reporting. Constants: cycle_id cycle_008; approver_email pm.lead@company.com; decision APPROVED at 2024-08-23T20:10:00Z; approval_comment 'Looks good to ship.'; op_note 'Approval recorded for pricing review' at 2024-08-23T20:12:00Z; final_status APPROVED at 2024-08-23T20:15:00Z."
        ),
        actions=[
            Action(name="RecordReviewApproval", kwargs={
                "cycle_id": "cycle_008",
                "approver_email": "pm.lead@company.com",
                "decision": "APPROVED",
                "decided_ts": "2024-08-23T20:10:00Z",
                "comment": "Looks good to ship."
            }),
            Action(name="LogTerminalEvent", kwargs={
                "log_ts": "2024-08-23T20:12:00Z",
                "message": "Approval recorded for pricing review"
            }),
            Action(name="AdvanceReviewStatus", kwargs={
                "cycle_id": "cycle_008",
                "new_status": "APPROVED",
                "changed_ts": "2024-08-23T20:15:00Z"
            })
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="MED_9",
        instruction="As a cross-surface coordination owner, manage a data-table design discussion to ensure Gmail thread discoverability, a safety posture aligned with DLP, and that copy is consistent with the related Figma artifacts. The focus is on thread thread_009; the scope includes label hygiene and preparing a stakeholder-ready PM nudge that avoids sensitive terms. The coordination result should be a clear PM message recorded in-thread and a label posture indicating a design-review with timestamped traceability, ensuring a clean DLP scan (blocked_terms_found=[]). Constants to use: thread_id thread_009; add_labels ['design-review'] at 2024-08-23T18:00:00Z; from_email pm.lead@company.com; created_ts 2024-08-23T18:05:00Z; body 'Copy update alignment requested for homepage hero and pricing sections.'",
        actions=[
            Action(name="UpdateThreadLabels", kwargs={
                "thread_id": "thread_009",
                "add_labels": ["design-review"],
                "remove_labels": [],
                "changed_ts": "2024-08-23T18:00:00Z"
            }),
            Action(name="AppendMessageToThread", kwargs={
                "thread_id": "thread_009",
                "from_email": "pm.lead@company.com",
                "body": "Copy update alignment requested for homepage hero and pricing sections.",
                "created_ts": "2024-08-23T18:05:00Z"
            }),
            Action(name="DlpScanThread", kwargs={"thread_id": "thread_009"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="MED_10",
        instruction="Take on the role of handoff coordinator to ensure the pricing page frame is marked ready and that all necessary assets are enumerated for delivery. Base your actions on these precise anchors: Gmail owner_email anna.brand@company.com, tag needs-review, Figma artifact_type FRAME, modified_since 2024-08-01T00:00:00Z, artifact_id art_007, add_tag handoff-ready, changed_ts 2024-08-23T08:45:00Z. Capture the asset snapshot for art_007 following the tag update.",
        actions=[
            Action(name="ListArtifacts", kwargs={ 'owner_email': 'anna.brand@company.com', 'tag': 'needs-review', 'artifact_type': 'FRAME', 'modified_since': '2024-08-01T00:00:00Z' }),
            Action(name="AddArtifactTag", kwargs={ 'artifact_id': 'art_007', 'tag': 'handoff-ready', 'changed_ts': '2024-08-23T08:45:00Z' }),
            Action(name="ListAssetsForArtifact", kwargs={ 'artifact_id': 'art_007' })
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="MED_11",
        instruction="As the approval-traceability owner for the Figma Navigation Bar review, articulate a policy-compliant audit narrative. Begin when art_002 initiates a review at 2024-08-23T10:00:00Z, moves to NEEDS_REVIEW at 10:05:00Z, documents a decision APPROVED from Gmail chris.engineer@company.com at 10:06:00Z with the rationale 'Looks good.', and finally attains terminal status APPROVED at 10:07:00Z. Anchor this narrative within the system of record by providing the canonical artifact summary for art_002; refrain from altering identifiers, statuses, timestamps, approver, or comment.",
        actions=[
            Action(name="StartReviewCycle", kwargs={ 'artifact_id': 'art_002', 'created_ts': '2024-08-23T10:00:00Z' }),
            Action(name="AdvanceReviewStatus", kwargs={ 'cycle_id': 'cycle_2c0e9232', 'new_status': 'NEEDS_REVIEW', 'changed_ts': '2024-08-23T10:05:00Z' }),
            Action(name="RecordReviewApproval", kwargs={ 'cycle_id': 'cycle_2c0e9232', 'approver_email': 'chris.engineer@company.com', 'decision': 'APPROVED', 'decided_ts': '2024-08-23T10:06:00Z', 'comment': 'Looks good.' }),
            Action(name="AdvanceReviewStatus", kwargs={ 'cycle_id': 'cycle_2c0e9232', 'new_status': 'APPROVED', 'changed_ts': '2024-08-23T10:07:00Z' }),
            Action(name="GetArtifactSummary", kwargs={ 'artifact_id': 'art_002' })
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="MED_12",
        instruction="Draft a succinct release note for the mobile app v2.1.0 and ensure it adheres to the attachment policy. Create this in thread_id thread_007 with release_id release_002, sending it from from_email jake.design@company.com at created_ts 2024-08-23T12:30:00Z, using the subject 'Mobile App v2.1.0 Release' and body 'Shipping profile & dashboard improvements.' Subsequently, execute a guard check with the generated message_id.",
        actions=[
            Action(name="ComposeReleaseEmailDraft", kwargs={ 'release_id': 'release_002', 'thread_id': 'thread_007', 'from_email': 'jake.design@company.com', 'created_ts': '2024-08-23T12:30:00Z', 'subject': 'Mobile App v2.1.0 Release', 'body': 'Shipping profile & dashboard improvements.' }),
            Action(name="GuardAttachmentPolicyOnDraft", kwargs={ 'message_id': 'relmsg_5b8194ea' })
        ],
        outputs=[]
    ),


    # complexity_edges: 8
    Task(
        annotator="0",
        user_id="MED_13",
        instruction=(
            "Handle the drafting of a concise release announcement and validate the attachment policy; then confirm the linked assets. Utilize constants precisely: release_id release_001, thread_id thread_006, from_email emma.creative@company.com, created_ts 2024-08-22T17:00:00Z, subject 'Release 1.2.0 Announcement', body 'Highlights and changes included.', and lastly, list the assets for artifact_id art_001."
        ),
        actions=[
            Action(name="ComposeReleaseEmailDraft", kwargs={"release_id": "release_001", "thread_id": "thread_006", "from_email": "emma.creative@company.com", "created_ts": "2024-08-22T17:00:00Z", "subject": "Release 1.2.0 Announcement", "body": "Highlights and changes included."}),
            Action(name="GuardAttachmentPolicyOnDraft", kwargs={"message_id": "relmsg_9cc87e81"}),
            Action(name="ListAssetsForArtifact", kwargs={"artifact_id": "art_001"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="MED_14",
        instruction="Coordinate as a token-policy compliance coordinator for marketing, focusing on asset enumeration and reporting artifacts that are ready for stakeholders. Activities center around the marketing file set owned by anna.brand@company.com within the website tag. The scope includes the FILE type modified since 2024-08-01T00:00:00Z, targeting artifact art_006. Ensure policy alignment with configuration design_system_mappings, providing outputs that are Figma deep-link aware and appropriate for Gmail sharing. The coordination should result in a concise and traceable summary of art_006, along with an operational Gmail note capturing “Checked marketing file assets” at 2024-08-23T13:30:00Z. Constants are: config_key design_system_mappings; owner_email anna.brand@company.com; tag website; artifact_type FILE; modified_since 2024-08-01T00:00:00Z; artifact_id art_006; log_ts 2024-08-23T13:30:00Z; message “Checked marketing file assets”.",
        actions=[
            Action(name="ReadSystemConfig", kwargs={"config_key": "design_system_mappings"}),
            Action(name="ListArtifacts", kwargs={"owner_email": "anna.brand@company.com", "tag": "website", "artifact_type": "FILE", "modified_since": "2024-08-01T00:00:00Z"}),
            Action(name="ListAssetsForArtifact", kwargs={"artifact_id": "art_006"}),
            Action(name="LogTerminalEvent", kwargs={"log_ts": "2024-08-23T13:30:00Z", "message": "Checked marketing file assets"}),
            Action(name="GetArtifactSummary", kwargs={"artifact_id": "art_006"})
        ],
        outputs=[]
    ),

    # complexity_edges: 9
    Task(
        annotator="0",
        user_id="MED_15",
        instruction="Act as a cross-channel review coordination manager for Gmail nudges and Figma asset verification, ensuring the delivery of auditable reminders, alignment of label taxonomy, and reporting on availability. Tasks relate to conversation thread thread_003 and artifact art_001; ensure that communication remains concise, compliant with policies, and traceable for stakeholders. The outcome of the coordination should be a timestamped reviewer nudge under john.pm@company.com, a thread state showcasing the needs-review label for tracking, and an up-to-date asset inventory for reporting. Constants: thread_id thread_003; from_email john.pm@company.com; message body “Please review the latest update today.” at 2024-08-23T13:07:00Z; label needs-review at 2024-08-23T13:08:00Z; artifact_id art_001.",
        actions=[
            Action(name="AppendMessageToThread", kwargs={"thread_id": "thread_003", "from_email": "john.pm@company.com", "body": "Please review the latest update today.", "created_ts": "2024-08-23T13:07:00Z"}),
            Action(name="UpdateThreadLabels", kwargs={"thread_id": "thread_003", "add_labels": ["needs-review"], "remove_labels": [], "changed_ts": "2024-08-23T13:08:00Z"}),
            Action(name="ListAssetsForArtifact", kwargs={"artifact_id": "art_001"})
        ],
        outputs=[]
    ),


    # complexity_edges: 7
    Task(
        annotator="0",
        user_id="MED_16",
        instruction=(
            "Coordinate the formalization of approval tracking on art_004: initiate the review cycle at 2024-08-23T13:00:00Z, followed by recording APPROVED by chris.engineer@company.com at 2024-08-23T13:25:00Z with the comment 'LGTM'. Conclude by listing assets for art_001."
        ),
        actions=[
            Action(name="StartReviewCycle", kwargs={"artifact_id": "art_004", "created_ts": "2024-08-23T13:00:00Z"}),
            Action(name="RecordReviewApproval", kwargs={"cycle_id": "cycle_1dc59e3f", "approver_email": "chris.engineer@company.com", "decision": "APPROVED", "decided_ts": "2024-08-23T13:25:00Z", "comment": "LGTM"}),
            Action(name="ListAssetsForArtifact", kwargs={"artifact_id": "art_001"})
        ],
        outputs=[]
    ),


    # complexity_edges: 9
    Task(
        annotator="0",
        user_id="MED_17",
        instruction=(
            "Handle the removal of a deprecated tag and ensure the thread is accurately labeled; subsequently, verify the exported assets. For art_005, delete the tag deprecated at changed_ts 2024-08-23T10:50:00Z; for thread_005, apply the label housekeeping at changed_ts 2024-08-23T10:55:00Z. Finalize by listing assets for art_001."
        ),
        actions=[
            Action(name="RemoveArtifactTag", kwargs={"artifact_id": "art_005", "tag": "deprecated", "changed_ts": "2024-08-23T10:50:00Z"}),
            Action(name="UpdateThreadLabels", kwargs={"thread_id": "thread_005", "add_labels": ["housekeeping"], "remove_labels": [], "changed_ts": "2024-08-23T10:55:00Z"}),
            Action(name="ListAssetsForArtifact", kwargs={"artifact_id": "art_001"})
        ],
        outputs=[]
    ),

    # complexity_edges: 8
    Task(
        annotator="0",
        user_id="MED_18",
        instruction=(
            "Coordinate a concise release communication and incorporate a deterministic asset reference. Validate the diff context with release_id release_001, next draft a message in thread_id thread_006 from from_email emma.creative@company.com at created_ts 2024-08-22T17:00:00Z using the subject 'Release 1.2.0 Summary' and the body 'Highlights and changes included.'. Provide the exported assets for artifact_id art_001."
        ),
        actions=[
            Action(name="GetReleaseDiffSummary", kwargs={"release_id": "release_001"}),
            Action(name="ComposeReleaseEmailDraft", kwargs={"release_id": "release_001", "thread_id": "thread_006", "from_email": "emma.creative@company.com", "created_ts": "2024-08-22T17:00:00Z", "subject": "Release 1.2.0 Summary", "body": "Highlights and changes included."}),
            Action(name="ListAssetsForArtifact", kwargs={"artifact_id": "art_001"}),
        ],
        outputs=[]
    ),

    # complexity_edges: 13
    Task(
        annotator="0",
        user_id="MED_19",
        instruction="Handle the role of design-review conversation steward to ensure precise label posture, a single concise reviewer cue, and maintain a stable asset reference. Concentrate on the conversation corresponding to label design-review, participant jake.design@company.com, keyword 'Review'; adjust thread_001 so that needs-attention and Design/Needs-Review are included and old-tag is removed with label state remaining effective on 2024-08-24T10:15:00Z. Retain a brief reviewer prompt from emma.creative@company.com at 10:16:00Z with the text 'Requesting review for art_002.' exactly. Provide the exported assets for art_001 as the follow-up anchor.",
        actions=[
            Action(name="SearchGmailThreads", kwargs={"label": "design-review", "participant": "jake.design@company.com", "keyword": "Review"}),
            Action(name="UpdateThreadLabels", kwargs={"thread_id": "thread_001", "add_labels": ["needs-attention", "Design/Needs-Review"], "remove_labels": ["old-tag"], "changed_ts": "2024-08-24T10:15:00Z"}),
            Action(name="AppendMessageToThread", kwargs={"thread_id": "thread_001", "from_email": "emma.creative@company.com", "body": "Requesting review for art_002.", "created_ts": "2024-08-24T10:16:00Z"}),
            Action(name="ListAssetsForArtifact", kwargs={"artifact_id": "art_001"}),
        ],
        outputs=[]
    ),

    # complexity_edges: 13
    Task(
        annotator="0",
        user_id="MED_20",
        instruction="Coordinate the pricing-page audit-readiness steward role ensuring a policy-consistent snapshot and an accurate status marker. The main record should confirm: completed audits on art_007 along with a summary for audit_005; art_007 positioned as audit-pending effective 2024-08-25T12:01:00Z; a new COMBINED_DS_A11Y session on art_007 with a creation timestamp of 2024-08-25T12:00:00Z; audit_workflow_config as the recognized scope authority; make asset visibility for art_007 available; and log the final program with the exact wording 'Initiated combined audit session for art_007' at 2024-08-25T12:02:00Z.",
        actions=[
            Action(name="ListAudits", kwargs={"artifact_id": "art_007", "status": "COMPLETED"}),
            Action(name="SummarizeAudit", kwargs={"audit_id": "audit_005"}),
            Action(name="AddArtifactTag", kwargs={"artifact_id": "art_007", "tag": "audit-pending", "changed_ts": "2024-08-25T12:01:00Z"}),
            Action(name="CreateAuditSession", kwargs={"artifact_id": "art_007", "created_ts": "2024-08-25T12:00:00Z", "audit_type": "COMBINED_DS_A11Y"}),
            Action(name="ReadSystemConfig", kwargs={"config_key": "audit_workflow_config"}),
            Action(name="ListAssetsForArtifact", kwargs={"artifact_id": "art_007"}),
            Action(name="LogTerminalEvent", kwargs={"log_ts": "2024-08-25T12:02:00Z", "message": "Initiated combined audit session for art_007"})
        ],
        outputs=[]
    ),

    # Auto Task 11
    Task(
        annotator="0",
        user_id="HARD_1",
        instruction=(
            "Handle the synchronization of review sentiment from Gmail into a review cycle for art_004 and measure it. The cycle you manage is identified as cycle_id cycle_1dc59e3f linked to thread_003. Incorporate two deterministic messages for intent parsing at created_ts 2024-08-23T13:10:00Z and 2024-08-23T13:15:00Z, with the exact bodies 'Looks good—LGTM from marketing.' from email anna.brand@company.com, and 'Please REVISE the grid spacing to 8px multiples.' from chris.engineer@company.com, respectively. Grounding constants include: artifact_id art_004, cycle_id cycle_1dc59e3f, thread_id thread_003, and created_ts 2024-08-23T13:00:00Z/13:05:00Z/13:10:00Z/13:15:00Z."
        ),
        actions=[
            Action(name="StartReviewCycle", kwargs={"artifact_id": "art_004", "created_ts": "2024-08-23T13:00:00Z"}),
            Action(name="LinkReviewToThread", kwargs={"cycle_id": "cycle_1dc59e3f", "thread_id": "thread_003", "changed_ts": "2024-08-23T13:05:00Z"}),
            Action(name="AppendMessageToThread", kwargs={"thread_id": "thread_003", "from_email": "anna.brand@company.com", "body": "Looks good—LGTM from marketing.", "created_ts": "2024-08-23T13:10:00Z"}),
            Action(name="AppendMessageToThread", kwargs={"thread_id": "thread_003", "from_email": "chris.engineer@company.com", "body": "Please REVISE the grid spacing to 8px multiples.", "created_ts": "2024-08-23T13:15:00Z"}),
            Action(name="SyncGmailIntentsToReview", kwargs={"cycle_id": "cycle_1dc59e3f", "thread_id": "thread_003"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="HARD_2",
        instruction="As the QA readiness provenance steward, ensure signal alignment and database-state maintenance across the Figma↔Gmail workflow. Provide an audit-ready record (facts, not procedures) linked to artifact art_009 and thread thread_011—not dependent on order and showing only persisted DB changes—confirming: tag qa-ready is present on art_009 effective 2024-08-23T19:00:00Z; a Figma comment by qa.lead@company.com at node-9:3 with exact text 'QA ready. Please create checklist.' at 2024-08-23T19:05:00Z; a Gmail message on thread_011 from qa.lead@company.com at 2024-08-23T19:10:00Z with body 'QA checklist attached. Please review.'; and a DLP evaluation of thread_011 using label dlp-flag at 2024-08-23T19:12:00Z. Return a brief summary of DLP findings and indicate if a label was applied.",
        actions=[
            Action(name="AddArtifactTag", kwargs={
                "artifact_id": "art_009",
                "tag": "qa-ready",
                "changed_ts": "2024-08-23T19:00:00Z"
            }),
            Action(name="CreateFigmaComment", kwargs={
                "artifact_id": "art_009",
                "author_email": "qa.lead@company.com",
                "body": "QA ready. Please create checklist.",
                "anchor_ref": "node-9:3",
                "created_ts": "2024-08-23T19:05:00Z"
            }),
            Action(name="AppendMessageToThread", kwargs={
                "thread_id": "thread_011",
                "from_email": "qa.lead@company.com",
                "body": "QA checklist attached. Please review.",
                "created_ts": "2024-08-23T19:10:00Z"
            }),
            Action(name="DlpScanAndLabelThread", kwargs={
                "thread_id": "thread_011",
                "label_if_found": "dlp-flag",
                "changed_ts": "2024-08-23T19:12:00Z"
            })
        ],
        outputs=[]
    ),


    # --- Fixed user_229 ---
    Task(
        annotator="0",
        user_id="HARD_3",
        instruction=(
            "Manage the announcement of a hotfix incorporating deterministic labeling and a singular safety assessment. Make use of constants: release_id release_010, thread_id thread_011, from_email pm.lead@company.com at created_ts 2024-08-24T13:30:00Z subject 'Hotfix 2.0.1 Patch' body 'Fixes urgent bug.', ack_from qa.lead@company.com at 2024-08-24T13:40:00Z 'LGTM for hotfix.', triage_changed_ts 2024-08-24T13:35:00Z, dlp_label_if_found dlp-flag with dlp_changed_ts 2024-08-24T13:42:00Z."
        ),
        actions=[
            Action(name="UpdateThreadLabels", kwargs={
                "thread_id": "thread_011",
                "add_labels": ["triaged"],
                "remove_labels": [],
                "changed_ts": "2024-08-24T13:35:00Z"
            }),
            Action(name="ComposeReleaseEmailDraft", kwargs={
                "release_id": "release_010",
                "thread_id": "thread_011",
                "from_email": "pm.lead@company.com",
                "created_ts": "2024-08-24T13:30:00Z",
                "subject": "Hotfix 2.0.1 Patch",
                "body": "Fixes urgent bug."
            }),
            Action(name="AppendMessageToThread", kwargs={
                "thread_id": "thread_011",
                "from_email": "qa.lead@company.com",
                "body": "LGTM for hotfix.",
                "created_ts": "2024-08-24T13:40:00Z"
            }),
            Action(name="ReadSystemConfig", kwargs={"config_key": "dlp_config"}),
            Action(name="DlpScanAndLabelThread", kwargs={
                "thread_id": "thread_011",
                "label_if_found": "dlp-flag",
                "changed_ts": "2024-08-24T13:42:00Z"
            })
        ],
        outputs=[]
    ),


    # --- Fixed user_221 ---
    Task(
        annotator="0",
        user_id="HARD_4",
        instruction=(
            "Oversee homepage readiness by ensuring artifact prioritization, clear guidance, and aligned communication without unnecessary discovery. Direct attention to art_001 homepage hero and its discussion: establish a priority signal, document a guidance note, prompt the team, and confirm safety. Make use of constants: artifact_id art_001, tag priority at 2024-08-23T16:50:00Z, author_email emma.creative@company.com, body 'Prioritize above-the-fold tweaks.', anchor_ref node-1:2, comment_created_ts 2024-08-23T16:52:00Z, thread_id thread_001, nudge_from product.owner@company.com, nudge_created_ts 2024-08-23T16:55:00Z, nudge 'Homepage priority flagged—tracking in sprint.'"
        ),
        actions=[
            Action(name="AddArtifactTag", kwargs={
                "artifact_id": "art_001",
                "tag": "priority",
                "changed_ts": "2024-08-23T16:50:00Z"
            }),
            Action(name="CreateFigmaComment", kwargs={
                "artifact_id": "art_001",
                "author_email": "emma.creative@company.com",
                "body": "Prioritize above-the-fold tweaks.",
                "anchor_ref": "node-1:2",
                "created_ts": "2024-08-23T16:52:00Z"
            }),
            Action(name="AppendMessageToThread", kwargs={
                "thread_id": "thread_001",
                "from_email": "product.owner@company.com",
                "body": "Homepage priority flagged—tracking in sprint.",
                "created_ts": "2024-08-23T16:55:00Z"
            }),
            Action(name="DlpScanThread", kwargs={"thread_id": "thread_001"})
        ],
        outputs=[]
    ),


    Task(
        annotator="0",
        user_id="HARD_5",
        instruction=(
            "As a review cycle coordinator, your role is to interpret Gmail intent into measurable review progress for the dashboard without using predefined cycle identifiers. On 2024-08-24T16:25:00Z, document a deterministic approval intent in thread_002, assign a review-ready tag to art_007, confirm the safety posture, and present artifact and asset context based on design_system_mappings and DLP policy. Employ the intent “Approve CTA placement.” by anna.brand@company.com at 2024-08-24T16:20:00Z. Constants remain: artifact_id art_007, thread_id thread_002, log_ts 2024-08-24T16:26:00Z, message 'Intent captured and posture verified for art_007'"
        ),
        actions=[
            Action(name="AppendMessageToThread", kwargs={
                "thread_id": "thread_002",
                "from_email": "anna.brand@company.com",
                "body": "Approve CTA placement.",
                "created_ts": "2024-08-24T16:20:00Z"
            }),
            Action(name="AddArtifactTag", kwargs={"artifact_id": "art_007", "tag": "review-ready", "changed_ts": "2024-08-24T16:25:00Z"}),
            Action(name="ListAssetsForArtifact", kwargs={"artifact_id": "art_007"}),
            Action(name="ReadSystemConfig", kwargs={"config_key": "design_system_mappings"}),
            Action(name="ReadSystemConfig", kwargs={"config_key": "dlp_config"}),
            Action(name="GetArtifactSummary", kwargs={"artifact_id": "art_007"}),
            Action(name="DlpScanThread", kwargs={"thread_id": "thread_002"}),
            Action(name="LogTerminalEvent", kwargs={"log_ts": "2024-08-24T16:26:00Z", "message": "Intent captured and posture verified for art_007"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="HARD_6",
        instruction="Your task is to manage pricing review intent and safety posture with Figma↔Gmail coordination, focusing on auditability and definitive db-modifying state changes without imposing order. Desired outcome: the cycle is associated with its record conversation, an approval signal is present and synced as intent, the thread remains DLP-clean, and the conversation is searchable under “Pricing.” Use constants: artifact_id art_007 at created_ts 2024-08-23T12:00:00Z; cycle_id cycle_38980610 connected to thread_id thread_008 at changed_ts 2024-08-23T12:05:00Z; approval from chris.engineer@company.com with body 'APPROVED - ship it' at created_ts 2024-08-23T12:06:00Z; DLP confirmation on thread_008; keyword Pricing.",
        actions=[
            Action(name="StartReviewCycle", kwargs={ 'artifact_id': 'art_007', 'created_ts': '2024-08-23T12:00:00Z' }),
            Action(name="LinkReviewToThread", kwargs={ 'cycle_id': 'cycle_38980610', 'thread_id': 'thread_008', 'changed_ts': '2024-08-23T12:05:00Z' }),
            Action(name="AppendMessageToThread", kwargs={ 'thread_id': 'thread_008', 'from_email': 'chris.engineer@company.com', 'body': 'APPROVED - ship it', 'created_ts': '2024-08-23T12:06:00Z' }),
            Action(name="SyncGmailIntentsToReview", kwargs={ 'cycle_id': 'cycle_38980610', 'thread_id': 'thread_008' }),
            Action(name="DlpScanThread", kwargs={ 'thread_id': 'thread_008' }),
            Action(name="SearchGmailThreads", kwargs={ 'keyword': 'Pricing' })
        ],
        outputs=[]
    ),

    # complexity_edges: 15
    Task(
        annotator="0",
        user_id="HARD_7",
        instruction="You act as the coordinator for release communications and brand guidance. Create a release announcement draft compliant with guidelines for release_001 in thread_006, written by emma.creative@company.com on 2024-08-22T17:00:00Z. The subject should be 'Release 1.2.0 Announcement' and the body 'Highlights and changes included.' Ensure the draft aligns with policies by validating it against message_id relmsg_9cc87e81. Record brand direction on art_003 by adding a designer note from sophie.marketing@company.com at node-2:7 on 2024-08-23T12:00:00Z, stating 'Please update the brand color token to Brand/Primary/600.' Provide the comment history by the author on art_003 from 2024-08-01T00:00:00Z for audit visibility.",
        actions=[
            Action(name="ComposeReleaseEmailDraft", kwargs={"release_id": "release_001", "thread_id": "thread_006", "from_email": "emma.creative@company.com", "created_ts": "2024-08-22T17:00:00Z", "subject": "Release 1.2.0 Announcement", "body": "Highlights and changes included."}),
            Action(name="GuardAttachmentPolicyOnDraft", kwargs={"message_id": "relmsg_9cc87e81"}),
            Action(name="CreateFigmaComment", kwargs={"artifact_id": "art_003", "author_email": "sophie.marketing@company.com", "body": "Please update the brand color token to Brand/Primary/600.", "anchor_ref": "node-2:7", "created_ts": "2024-08-23T12:00:00Z"}),
            Action(name="ListFigmaComments", kwargs={"artifact_id": "art_003", "author_email": "sophie.marketing@company.com", "since_ts": "2024-08-01T00:00:00Z"})
        ],
        outputs=[]
    ),


    # complexity_edges: 15
    Task(
        annotator="0",
        user_id="HARD_8",
        instruction="You perform the role of compliance steward, ensuring Gmail security memos and Figma design directives align for an audit-ready snapshot without specified sequence. Your focus areas are mail thread_002 and artifact art_003. The confirmed record must clearly document: a memo on thread_002 by emma.creative@company.com sent on 2024-08-23T11:00:00Z containing the body “Please note: temporary password is abcd-1234; rotate after testing.”; a DLP status where label_if_found dlp-flag is implemented on thread_002 when sensitive content is identified, effective from 2024-08-23T11:05:00Z; and a brand note on art_003 at node-2:7 by sophie.marketing@company.com on 2024-08-23T12:00:00Z saying “Please update the brand color token to Brand/Primary/600.” Core constants: thread_id thread_002, artifact_id art_003, anchor_ref node-2:7, and the mentioned timestamps. Provide the author-filtered comment history on Figma for art_003 focused on sophie.marketing@company.com since 2024-08-01T00:00:00Z, detailing the recorded (db) changes.",
        actions=[
            Action(name="AppendMessageToThread", kwargs={"thread_id": "thread_002", "from_email": "emma.creative@company.com", "body": "Please note: temporary password is abcd-1234; rotate after testing.", "created_ts": "2024-08-23T11:00:00Z"}),
            Action(name="DlpScanAndLabelThread", kwargs={"thread_id": "thread_002", "label_if_found": "dlp-flag", "changed_ts": "2024-08-23T11:05:00Z"}),
            Action(name="CreateFigmaComment", kwargs={"artifact_id": "art_003", "author_email": "sophie.marketing@company.com", "body": "Please update the brand color token to Brand/Primary/600.", "anchor_ref": "node-2:7", "created_ts": "2024-08-23T12:00:00Z"}),
            Action(name="ListFigmaComments", kwargs={"artifact_id": "art_003", "author_email": "sophie.marketing@company.com", "since_ts": "2024-08-01T00:00:00Z"})
        ],
        outputs=[]
    ),


    # complexity_edges: 15
    Task(
        annotator="0",
        user_id="HARD_9",
        instruction="Handle the readiness of release communications and ensure QA traceability for release_001. Desired result: creation of a release announcement draft for release_001 in thread_006 from emma.creative@company.com at 2024-08-22T17:00:00Z with the subject 'Release 1.2.0 Announcement' and the body 'Highlights and changes included.' This draft needs validation against the attachment policy using message_id relmsg_9cc87e81; thread_006 should carry the label release-ready with changed_ts 2024-08-22T17:10:00Z; a QA confirmation note must be present in thread_006 from qa.lead@company.com with creation time 2024-08-22T17:06:00Z and body 'QA sign-off complete'; for the handoff, ensure the exported assets associated with artifact art_001 are returned.",
        actions=[
            Action(name="ComposeReleaseEmailDraft", kwargs={"release_id": "release_001", "thread_id": "thread_006", "from_email": "emma.creative@company.com", "created_ts": "2024-08-22T17:00:00Z", "subject": "Release 1.2.0 Announcement", "body": "Highlights and changes included."}),
            Action(name="GuardAttachmentPolicyOnDraft", kwargs={"message_id": "relmsg_9cc87e81"}),
            Action(name="UpdateThreadLabels", kwargs={"thread_id": "thread_006", "add_labels": ["release-ready"], "remove_labels": [], "changed_ts": "2024-08-22T17:10:00Z"}),
            Action(name="AppendMessageToThread", kwargs={"thread_id": "thread_006", "from_email": "qa.lead@company.com", "body": "QA sign-off complete", "created_ts": "2024-08-22T17:06:00Z"}),
            Action(name="ListAssetsForArtifact", kwargs={"artifact_id": "art_001"})
        ],
        outputs=[]
    ),


    # complexity_edges: 15
    Task(
        annotator="0",
        user_id="HARD_10",
        instruction="Coordinate the kickoff for a cross-channel review of the homepage frame, align the labels, and provide the asset snapshot for engineering. Within the scoped areas of the homepage owned by emma.creative@company.com—restricted to FRAME artifacts tagged with needs-review and updated on or after 2024-08-01T00:00:00Z—focus on art_001. Record the review kickoff at 2024-08-24T09:30:00Z. Maintain conversation hygiene in the ongoing design-review thread that includes chris.engineer@company.com and meets the keyword “Design”: adjust its labels by adding triaged and figma-sync while removing urgent, with the change timestamp at 2024-08-24T09:40:00Z. Make sure the exported assets linked to art_001 are returned.",
        actions=[
            Action(name="ListArtifacts", kwargs={"owner_email": "emma.creative@company.com", "tag": "needs-review", "artifact_type": "FRAME", "modified_since": "2024-08-01T00:00:00Z"}),
            Action(name="StartReviewCycle", kwargs={"artifact_id": "art_001", "created_ts": "2024-08-24T09:30:00Z"}),
            Action(name="SearchGmailThreads", kwargs={"label": "design-review", "participant": "chris.engineer@company.com", "keyword": "Design"}),
            Action(name="UpdateThreadLabels", kwargs={"thread_id": "thread_001", "add_labels": ["triaged", "figma-sync"], "remove_labels": ["urgent"], "changed_ts": "2024-08-24T09:40:00Z"}),
            Action(name="ListAssetsForArtifact", kwargs={"artifact_id": "art_001"}),
        ],
        outputs=[]
    ),


    # complexity_edges: 13
    Task(
        annotator="0",
        user_id="HARD_11",
        instruction="You are responsible for confirming the formal design review for art_004 and ensuring cross-artifact visibility. Verify that a review instance is scheduled for 2024-08-23T13:00:00Z related to art_004, correctly linked to the Gmail conversation via cycle_1dc59e3f → thread_003 with linkage timestamp at 2024-08-23T13:05:00Z. Log the final decision as APPROVED by chris.engineer@company.com at 2024-08-23T13:25:00Z, including the comment 'Ship it'. For reporting purposes, present the author-filtered comment timeline on art_003 for sophie.marketing@company.com starting from 2024-08-01T00:00:00Z.",
        actions=[
            Action(name="StartReviewCycle", kwargs={"artifact_id": "art_004", "created_ts": "2024-08-23T13:00:00Z"}),
            Action(name="LinkReviewToThread", kwargs={"cycle_id": "cycle_1dc59e3f", "thread_id": "thread_003", "changed_ts": "2024-08-23T13:05:00Z"}),
            Action(name="RecordReviewApproval", kwargs={"cycle_id": "cycle_1dc59e3f", "approver_email": "chris.engineer@company.com", "decision": "APPROVED", "decided_ts": "2024-08-23T13:25:00Z", "comment": "Ship it"}),
            Action(name="ListFigmaComments", kwargs={"artifact_id": "art_003", "author_email": "sophie.marketing@company.com", "since_ts": "2024-08-01T00:00:00Z"})
        ],
        outputs=[]
    ),


    # complexity_edges: 15
    Task(
        annotator="0",
        user_id="HARD_12",
        instruction="You oversee the readiness for the marketing frame handoff while enhancing data-loss posture and creating a minimal coordination trace. In art_003, make sure the artifact state shows the handoff milestone at 2024-08-24T12:00:00Z; capture the collaboration context with a design note by jake.design@company.com at 2024-08-24T12:05:00Z anchored on node-5:1 including the text “Prep handoff”. The associated marketing discussion is thread_002 and records an alert from emma.creative@company.com at 2024-08-23T11:00:00Z: “Please note: temporary password is abcd-1234; rotate after testing.” DLP compliance is critical—if violations are detected, the thread is marked with label dlp-flag, with change time 2024-08-23T11:05:00Z. Present the scan-and-label result.",
        actions=[
            Action(name="AddArtifactTag", kwargs={"artifact_id": "art_003", "tag": "handoff-ready", "changed_ts": "2024-08-24T12:00:00Z"}),
            Action(name="CreateFigmaComment", kwargs={"artifact_id": "art_003", "author_email": "jake.design@company.com", "body": "Prep handoff", "anchor_ref": "node-5:1", "created_ts": "2024-08-24T12:05:00Z"}),
            Action(name="AppendMessageToThread", kwargs={"thread_id": "thread_002", "from_email": "emma.creative@company.com", "body": "Please note: temporary password is abcd-1234; rotate after testing.", "created_ts": "2024-08-23T11:00:00Z"}),
            Action(name="DlpScanAndLabelThread", kwargs={"thread_id": "thread_002", "label_if_found": "dlp-flag", "changed_ts": "2024-08-23T11:05:00Z"}),
        ],
        outputs=[]
    ),


    # complexity_edges: 14
    Task(
        annotator="0",
        user_id="HARD_13",
        instruction="Handle the finalization of a release announcement based on the release/lineage and make sure the discussion conveys a positive release tone. Use release_001 as the main reference for this announcement. The announcement is saved as a draft in thread_006 from emma.creative@company.com on 2024-08-22T17:00:00Z with the subject “Release 1.2.0 Announcement” and body “Highlights and changes included.” The draft message relmsg_9cc87e81 adheres to the attachment policy, and the thread is marked with Design/Release and sentiment/positive with change time 2024-08-22T17:05:00Z. Submit the exported assets associated with art_001.",
        actions=[
            Action(name="ListReleases", kwargs={"version_prefix": "release/"}),
            Action(name="GetReleaseDiffSummary", kwargs={"release_id": "release_001"}),
            Action(name="ComposeReleaseEmailDraft", kwargs={"release_id": "release_001", "thread_id": "thread_006", "from_email": "emma.creative@company.com", "created_ts": "2024-08-22T17:00:00Z", "subject": "Release 1.2.0 Announcement", "body": "Highlights and changes included."}),
            Action(name="GuardAttachmentPolicyOnDraft", kwargs={"message_id": "relmsg_9cc87e81"}),
            Action(name="UpdateThreadLabels", kwargs={"thread_id": "thread_006", "add_labels": ["Design/Release", "sentiment/positive"], "remove_labels": [], "changed_ts": "2024-08-22T17:05:00Z"}),
            Action(name="ListAssetsForArtifact", kwargs={"artifact_id": "art_001"}),
        ],
        outputs=[]
    ),


    # complexity_edges: 14
    Task(
        annotator="0",
        user_id="HARD_14",
        instruction="Coordinate the integrated design-system/accessibility audit generating an explicit preparation footprint. Utilize design_system_mappings as the basis and limit the investigation to FILE artifacts owned by anna.brand@company.com that are tagged with website and changed on or after 2024-08-01T00:00:00Z. The target art_006 is recorded with an audit of type COMBINED_DS_A11Y at 2024-08-24T13:00:00Z, alongside a prep log 'Prepared audit for art_006' at 2024-08-24T13:05:00Z, and is labeled with a working tag audit-in-progress effective 2024-08-24T13:06:00Z. Provide the canonical artifact summary for art_006 to substantiate this record.",
        actions=[
            Action(name="ReadSystemConfig", kwargs={"config_key": "design_system_mappings"}),
            Action(name="ListArtifacts", kwargs={"owner_email": "anna.brand@company.com", "tag": "website", "artifact_type": "FILE", "modified_since": "2024-08-01T00:00:00Z"}),
            Action(name="CreateAuditSession", kwargs={"artifact_id": "art_006", "created_ts": "2024-08-24T13:00:00Z", "audit_type": "COMBINED_DS_A11Y"}),
            Action(name="LogTerminalEvent", kwargs={"log_ts": "2024-08-24T13:05:00Z", "message": "Prepared audit for art_006"}),
            Action(name="AddArtifactTag", kwargs={"artifact_id": "art_006", "tag": "audit-in-progress", "changed_ts": "2024-08-24T13:06:00Z"}),
            Action(name="GetArtifactSummary", kwargs={"artifact_id": "art_006"}),
        ],
        outputs=[]
    ),

    # complexity_edges: 17
    Task(
        annotator="0",
        user_id="HARD_15",
        instruction=(
            "Translate Gmail intent into quantified review sentiment for the dashboard review without setting a sequence. Operate on art_004 with cycle_id cycle_1dc59e3f linked to thread_003. Record two deterministic intents for parsing: 'Looks good—LGTM from marketing.' from anna.brand@company.com at 2024-08-23T13:10:00Z and 'Please REVISE the grid spacing to 8px multiples.' from chris.engineer@company.com at 2024-08-23T13:15:00Z. Grounding constants: artifact_id art_004, cycle_id cycle_1dc59e3f, thread_id thread_003, created_ts 2024-08-23T13:00:00Z and 2024-08-23T13:05:00Z for cycle/link, and the two message timestamps above. Provide the synced intent counts."
        ),
        actions=[
            Action(name="StartReviewCycle", kwargs={"artifact_id": "art_004", "created_ts": "2024-08-23T13:00:00Z"}),
            Action(name="LinkReviewToThread", kwargs={"cycle_id": "cycle_1dc59e3f", "thread_id": "thread_003", "changed_ts": "2024-08-23T13:05:00Z"}),
            Action(name="AppendMessageToThread", kwargs={"thread_id": "thread_003", "from_email": "anna.brand@company.com", "body": "Looks good—LGTM from marketing.", "created_ts": "2024-08-23T13:10:00Z"}),
            Action(name="AppendMessageToThread", kwargs={"thread_id": "thread_003", "from_email": "chris.engineer@company.com", "body": "Please REVISE the grid spacing to 8px multiples.", "created_ts": "2024-08-23T13:15:00Z"}),
            Action(name="SyncGmailIntentsToReview", kwargs={"cycle_id": "cycle_1dc59e3f", "thread_id": "thread_003"})
        ],
        outputs=[]
    ),

    # complexity_edges: 18
    Task(
        annotator="0",
        user_id="HARD_16",
        instruction=(
            "Coordinate brand-aligned release communications and ensure audit-ready traceability without specifying a tool order. Draft a concise communication then verify attachment policy, and capture a durable FIGMA brand note with author-scoped history. Constants: release_id release_001, thread_id thread_006, from_email emma.creative@company.com, created_ts 2024-08-22T17:00:00Z, subject 'Release 1.2.0 Announcement', body 'Highlights and changes included.', message_id relmsg_9cc87e81; artifact_id art_003, author_email sophie.marketing@company.com, anchor_ref node-2:7, comment_created_ts 2024-08-23T12:00:00Z, since_ts 2024-08-01T00:00:00Z."
        ),
        actions=[
            Action(name="ComposeReleaseEmailDraft", kwargs={
                "release_id": "release_001",
                "thread_id": "thread_006",
                "from_email": "emma.creative@company.com",
                "created_ts": "2024-08-22T17:00:00Z",
                "subject": "Release 1.2.0 Announcement",
                "body": "Highlights and changes included."
            }),
            Action(name="GuardAttachmentPolicyOnDraft", kwargs={"message_id": "relmsg_9cc87e81"}),
            Action(name="CreateFigmaComment", kwargs={
                "artifact_id": "art_003",
                "author_email": "sophie.marketing@company.com",
                "body": "Please update the brand color token to Brand/Primary/600.",
                "anchor_ref": "node-2:7",
                "created_ts": "2024-08-23T12:00:00Z"
            }),
            Action(name="ListFigmaComments", kwargs={
                "artifact_id": "art_003",
                "author_email": "sophie.marketing@company.com",
                "since_ts": "2024-08-01T00:00:00Z"
            })
        ],
        outputs=[]
    ),

    # complexity_edges: 17
    Task(
        annotator="0",
        user_id="HARD_17",
        instruction="As a homepage review coordination specialist, you must ensure audit-grade traceability and policy-aligned status visibility across Figma and Gmail. The focus is on artifact art_001 owned by emma.creative@company.com, within the needs-review FRAME scope that has been revised since 2024-08-01T00:00:00Z. The confirmed posture should represent a review cycle initiated on 2024-08-24T09:30:00Z; Gmail evidence under the design-review label from chris.engineer@company.com containing the keyword “Design”; and a labeled state for thread_001 including triaged and figma-sync present and urgent absent, effective from 2024-08-24T09:40:00Z. The result of this coordination is to be a clear and stakeholder-ready asset list for art_001, complete with timestamped traceability. Constants remain: owner_email emma.creative@company.com, tag needs-review, artifact_type FRAME, modified_since 2024-08-01T00:00:00Z, artifact_id art_001, review_created 2024-08-24T09:30:00Z, gmail_label design-review, participant chris.engineer@company.com, keyword Design, thread_id thread_001, add_labels [triaged, figma-sync], remove_labels [urgent], changed_ts 2024-08-24T09:40:00Z.",
        actions=[
            Action(name="ListArtifacts", kwargs={"owner_email": "emma.creative@company.com", "tag": "needs-review", "artifact_type": "FRAME", "modified_since": "2024-08-01T00:00:00Z"}),
            Action(name="StartReviewCycle", kwargs={"artifact_id": "art_001", "created_ts": "2024-08-24T09:30:00Z"}),
            Action(name="SearchGmailThreads", kwargs={"label": "design-review", "participant": "chris.engineer@company.com", "keyword": "Design"}),
            Action(name="UpdateThreadLabels", kwargs={"thread_id": "thread_001", "add_labels": ["triaged", "figma-sync"], "remove_labels": ["urgent"], "changed_ts": "2024-08-24T09:40:00Z"}),
            Action(name="ListAssetsForArtifact", kwargs={"artifact_id": "art_001"})
        ],
        outputs=[]
    ),

    # complexity_edges: 14
    Task(
        annotator="0",
        user_id="HARD_18",
        instruction="Your task is to integrate Gmail feedback signals and Figma release posture into one audit-ready snapshot without establishing sequence. The scope is anchored by artifact context art_002 and mail context thread_006. Accurately record two key notes for parsing — “Approve pricing grid.” from pm.lead@company.com at 2024-08-24T18:05:00Z and “Revise discount footnote.” from qa.lead@company.com at 2024-08-24T18:10:00Z; ensure safety through a single DLP check on thread_006; and indicate release status by assigning the tag approved-for-release to art_002 starting 2024-08-24T18:16:00Z (db mutation). The deliverable is the exported asset list for art_002. The grounding constants include: artifact_id art_002, thread_id thread_006, and the specified timestamps.",
        actions=[
            Action(name="AppendMessageToThread", kwargs={
                "thread_id": "thread_006",
                "from_email": "pm.lead@company.com",
                "body": "Approve pricing grid.",
                "created_ts": "2024-08-24T18:05:00Z"
            }),
            Action(name="AppendMessageToThread", kwargs={
                "thread_id": "thread_006",
                "from_email": "qa.lead@company.com",
                "body": "Revise discount footnote.",
                "created_ts": "2024-08-24T18:10:00Z"
            }),
            Action(name="AddArtifactTag", kwargs={"artifact_id": "art_002", "tag": "approved-for-release", "changed_ts": "2024-08-24T18:16:00Z"}),
            Action(name="ListAssetsForArtifact", kwargs={"artifact_id": "art_002"}),
            Action(name="DlpScanThread", kwargs={"thread_id": "thread_006"})
        ],
        outputs=[]
    ),

    # complexity_edges: 14
    Task(
        annotator="0",
        user_id="HARD_19",
        instruction="Handle the role of landing-page kickoff and triage steward, ensuring the creation of an audit-ready coordination snapshot. Scope details: owner emma.creative@company.com, artifact type FRAME, tag landing-page, and modified on/after 2024-08-01T00:00:00Z; artifact context art_001 and mail context thread_001. The confirmed record must clearly demonstrate a kickoff note written by emma.creative@company.com at 2024-08-25T09:00:00Z with exact wording 'Handoff kickoff for landing page.'; a label stance on thread_001 where triaged and handoff are included and dlp-flag is excluded effective 2024-08-25T09:05:00Z; and the resulting deliverable is the exported asset list associated with art_001.",
        actions=[
            Action(name="ListArtifacts", kwargs={
            "owner_email": "emma.creative@company.com",
            "tag": "landing-page",
            "artifact_type": "FRAME",
            "modified_since": "2024-08-01T00:00:00Z"
            }),
            Action(name="AppendMessageToThread", kwargs={
            "thread_id": "thread_001",
            "from_email": "emma.creative@company.com",
            "body": "Handoff kickoff for landing page.",
            "created_ts": "2024-08-25T09:00:00Z"
            }),
            Action(name="UpdateThreadLabels", kwargs={
            "thread_id": "thread_001",
            "add_labels": ["triaged", "handoff"],
            "remove_labels": ["dlp-flag"],
            "changed_ts": "2024-08-25T09:05:00Z"
            }),
            Action(name="ListAssetsForArtifact", kwargs={"artifact_id": "art_001"}),
        ],
        outputs=[]
    ),

    # complexity_edges: 13
    Task(
        annotator="0",
        user_id="HARD_20",
        instruction="Coordinate the handoff as the pricing page coordinator, guaranteeing a persistent designer note and a clear readiness position. Scope includes: owner anna.brand@company.com, tag needs-review, artifact type FRAME, modified on/after 2024-08-01T00:00:00Z; target art_007. The audit-ready condition records a definitive design note on art_007, anchored node-7:2 by anna.brand@company.com at 2024-08-25T10:40:00Z with precise text 'Mark CTA “Sign up”.' and reflects art_007 marked with tag handoff-ready effective 2024-08-25T10:45:00Z. The deliverable is the exported asset snapshot for art_007.",
        actions=[
            Action(name="ListArtifacts", kwargs={
                "owner_email": "anna.brand@company.com",
                "tag": "needs-review",
                "artifact_type": "FRAME",
                "modified_since": "2024-08-01T00:00:00Z"
            }),
            Action(name="CreateFigmaComment", kwargs={
                "artifact_id": "art_007",
                "author_email": "anna.brand@company.com",
                "body": "Mark CTA “Sign up”.",
                "anchor_ref": "node-7:2",
                "created_ts": "2024-08-25T10:40:00Z"
            }),
            Action(name="AddArtifactTag", kwargs={
                "artifact_id": "art_007",
                "tag": "handoff-ready",
                "changed_ts": "2024-08-25T10:45:00Z"
            }),
            Action(name="ListAssetsForArtifact", kwargs={"artifact_id": "art_007"}),
        ],
        outputs=[]
        ),

    # complexity_edges: 14
    Task(
        annotator="0",
        user_id="HARD_21",
        instruction="Manage the review-sentiment normalization by aligning lifecycle signals with conversation intent. Lifecycle anchor: cycle_003 for the pricing/table discussion linked to thread_003 at 2024-08-25T10:05:00Z. The authoritative conversation record displays two distinct notes that should be uploaded to db — anna.brand@company.com 'Looks good—LGTM from marketing.' at 2024-08-25T10:10:00Z and chris.engineer@company.com 'Please REVISE the grid spacing to 8px multiples.' at 2024-08-25T10:15:00Z — and the cycle includes synchronized mail intents from thread_003. Deliver the intent count roll-up for the cycle_003 ↔ thread_003 pair.",
        actions=[
            Action(name="LinkReviewToThread", kwargs={
            "cycle_id": "cycle_003",
            "thread_id": "thread_003",
            "changed_ts": "2024-08-25T10:05:00Z"
            }),
            Action(name="AppendMessageToThread", kwargs={
            "thread_id": "thread_003",
            "from_email": "anna.brand@company.com",
            "body": "Looks good—LGTM from marketing.",
            "created_ts": "2024-08-25T10:10:00Z"
            }),
            Action(name="AppendMessageToThread", kwargs={
            "thread_id": "thread_003",
            "from_email": "chris.engineer@company.com",
            "body": "Please REVISE the grid spacing to 8px multiples.",
            "created_ts": "2024-08-25T10:15:00Z"
            }),
            Action(name="SyncGmailIntentsToReview", kwargs={
            "cycle_id": "cycle_003",
            "thread_id": "thread_003"
            }),
        ],
        outputs=[]
    ),

    # complexity_edges: 13
    Task(
        annotator="0",
        user_id="HARD_22",
        instruction="Coordinate admin-navigation efforts to ensure durable design notes, synced mail visibility, and a stable reference snapshot. The authoritative record should include: a canonical design observation on art_011 by design.lead@company.com at 2024-08-25T12:30:00Z anchored at node-11:4 with text 'Tighten header spacing to 8px rhythm.'; thread_013 presenting a sync touchpoint from design.lead@company.com at 2024-08-25T12:32:00Z with 'Design note logged on art_011.'; a label stance on thread_013 where figma-sync is present effective 2024-08-25T12:33:00Z; and, for downstream consumers, the exported assets for art_001 as the stable reference.",
        actions=[
            Action(name="CreateFigmaComment", kwargs={
                "artifact_id": "art_011",
                "author_email": "design.lead@company.com",
                "body": "Tighten header spacing to 8px rhythm.",
                "anchor_ref": "node-11:4",
                "created_ts": "2024-08-25T12:30:00Z"
            }),
            Action(name="AppendMessageToThread", kwargs={
                "thread_id": "thread_013",
                "from_email": "design.lead@company.com",
                "body": "Design note logged on art_011.",
                "created_ts": "2024-08-25T12:32:00Z"
            }),
            Action(name="UpdateThreadLabels", kwargs={
                "thread_id": "thread_013",
                "add_labels": ["figma-sync"],
                "remove_labels": [],
                "changed_ts": "2024-08-25T12:33:00Z"
            }),
            Action(name="ListAssetsForArtifact", kwargs={"artifact_id": "art_001"}),
        ],
        outputs=[]
    ),

    # complexity_edges: 12
    Task(
        annotator="0",
        user_id="HARD_23",
        instruction="Act as the coordinator for the pricing audit kickoff, responsible for governance alignment, ensuring stakeholder visibility, and creating an audit snapshot that can be traced. Utilize fix_workflow_config and intent_keywords as the definitive governance context. The completed kickoff snapshot should demonstrate a COMBINED_DS_A11Y kickoff on art_003 (created 2024-08-25T09:00:00Z), include a program checkpoint note 'Fix planning kickoff' at 2024-08-25T09:02:00Z, ensure stakeholder visibility on thread_006 from sophie.marketing@company.com at 2024-08-25T09:03:00Z with 'Kickoff: reviewing audit_c924d63d and preparing plan.', and ensure the email summary reflects planning presence as of 2024-08-25T09:04:00Z. Provide the summarized counts for audit_c924d63d.",
        actions=[
            Action(name="ReadSystemConfig", kwargs={"config_key": "fix_workflow_config"}),
            Action(name="ReadSystemConfig", kwargs={"config_key": "intent_keywords"}),
            Action(name="CreateAuditSession", kwargs={
                "artifact_id": "art_003",
                "created_ts": "2024-08-25T09:00:00Z",
                "audit_type": "COMBINED_DS_A11Y"
            }),
            Action(name="LogTerminalEvent", kwargs={
                "log_ts": "2024-08-25T09:02:00Z",
                "message": "Fix planning kickoff"
            }),
            Action(name="AppendMessageToThread", kwargs={
                "thread_id": "thread_006",
                "from_email": "sophie.marketing@company.com",
                "body": "Kickoff: reviewing audit_c924d63d and preparing plan.",
                "created_ts": "2024-08-25T09:03:00Z"
            }),
            Action(name="UpdateThreadLabels", kwargs={
                "thread_id": "thread_006",
                "add_labels": ["planning"],
                "remove_labels": [],
                "changed_ts": "2024-08-25T09:04:00Z"
            }),
            Action(name="SummarizeAudit", kwargs={"audit_id": "audit_c924d63d"}),
        ],
        outputs=[]
    ),

    # complexity_edges: 14
    Task(
        annotator="0",
        user_id="HARD_24",
        instruction="Oversee thread-hygiene and sync-state for the Navigation discussion, delivering an audit-ready snapshot without dictating sequence. Scope anchors include: Gmail label responsive, participant chris.engineer@company.com, keyword Navigation; and thread context thread_010. Vocabulary authority is the canonical label set named gmail_labels from system configuration—normalize/validate any label writes against this (db modification). Compliance expected by 2024-08-25T10:00:00Z: on thread_010, the status should be triaged, with figma-sync present and responsive absent; along with a brief status ping written by emma.creative@company.com at 2024-08-25T10:02:00Z with the exact text 'Design synced to Figma.'; plus one DLP safety confirmation indicating no blocked terms. Keep all identifiers and literals exactly as provided and return the verified state.",
        actions=[
            Action(name="SearchGmailThreads", kwargs={"label": "responsive", "participant": "chris.engineer@company.com", "keyword": "Navigation"}),
            Action(name="UpdateThreadLabels", kwargs={"thread_id": "thread_010", "add_labels": ["triaged", "figma-sync"], "remove_labels": ["responsive"], "changed_ts": "2024-08-25T10:00:00Z"}),
            Action(name="ReadSystemConfig", kwargs={"config_key": "gmail_labels"}),
            Action(name="AppendMessageToThread", kwargs={"thread_id": "thread_010", "from_email": "emma.creative@company.com", "body": "Design synced to Figma.", "created_ts": "2024-08-25T10:02:00Z"}),
            Action(name="DlpScanThread", kwargs={"thread_id": "thread_010"})
        ],
        outputs=[]
    ),

    # complexity_edges: 15
    Task(
        annotator="0",
        user_id="HARD_25",
        instruction="Handle an audit-ready governance snapshot for the Pricing Page within the Figma/Gmail context without prescribing order. Scope anchors: FRAME artifacts owned by anna.brand@company.com tagged pricing and modified on/after 2024-08-01T00:00:00Z; focal artifact art_007. The verified record must clearly display: the latest COMPLETED audits for art_007 with audit_005 summarized; art_007 tagged audit-pending effective 2024-08-25T12:01:00Z; a COMBINED_DS_A11Y session created at 2024-08-25T12:00:00Z; audit_workflow_config as the authoritative scope; and inclusion of the exported asset list for art_007. Return the consolidated evidence bundle.",
        actions=[
            Action(name="ListArtifacts", kwargs={
                "owner_email": "anna.brand@company.com",
                "tag": "pricing",
                "artifact_type": "FRAME",
                "modified_since": "2024-08-01T00:00:00Z"
            }),
            Action(name="ListAudits", kwargs={
                "artifact_id": "art_007",
                "status": "COMPLETED"
            }),
            Action(name="SummarizeAudit", kwargs={
                "audit_id": "audit_005"
            }),
            Action(name="AddArtifactTag", kwargs={
                "artifact_id": "art_007",
                "tag": "audit-pending",
                "changed_ts": "2024-08-25T12:01:00Z"
            }),
            Action(name="CreateAuditSession", kwargs={
                "artifact_id": "art_007",
                "created_ts": "2024-08-25T12:00:00Z",
                "audit_type": "COMBINED_DS_A11Y"
            }),
            Action(name="ReadSystemConfig", kwargs={
                "config_key": "audit_workflow_config"
            }),
            Action(name="ListAssetsForArtifact", kwargs={
                "artifact_id": "art_007"
            })
        ],
        outputs=[]
    ),


    # complexity_edges: 13
    Task(
        annotator="0",
        user_id="HARD_26",
        instruction="Coordinate the preparation of a concise public note for the marketing website launch and confirm the communications guardrails under the release governance. Consider the release/ catalog (with artifact_id None) as authoritative and quantify release_003 via its deterministic message context. The audit-ready thread_003 record should demonstrate: an announcement draft by anna.brand@company.com at 2024-08-25T13:45:00Z with subject 'Release 1.0.0 Announcement' and body 'Launching marketing website.' validated under message_id relmsg_ddbea77f; label vocabulary aligned to gmail_labels with release-draft present as of 2024-08-25T13:50:00Z; and a DLP safety confirmation showing the thread is clean.",
        actions=[
            Action(name="ListReleases", kwargs={
                "version_prefix": "release/",
                "artifact_id": None
            }),
            Action(name="ComposeReleaseEmailDraft", kwargs={
                "release_id": "release_003",
                "thread_id": "thread_003",
                "from_email": "anna.brand@company.com",
                "created_ts": "2024-08-25T13:45:00Z",
                "subject": "Release 1.0.0 Announcement",
                "body": "Launching marketing website."
            }),
            Action(name="GuardAttachmentPolicyOnDraft", kwargs={
                "message_id": "relmsg_ddbea77f"
            }),
            Action(name="ReadSystemConfig", kwargs={
                "config_key": "gmail_labels"
            }),
            Action(name="UpdateThreadLabels", kwargs={
                "thread_id": "thread_003",
                "add_labels": ["release-draft"],
                "remove_labels": [],
                "changed_ts": "2024-08-25T13:50:00Z"
            }),
            Action(name="DlpScanThread", kwargs={
                "thread_id": "thread_003"
            })
        ],
        outputs=[]
    ),

    # complexity_edges: 15
    Task(
        annotator="0",
        user_id="HARD_27",
        instruction="Handle the finalization of landing-page campaign readiness by utilizing a goal-based policy—no fixed sequence—that aligns Figma brand guidance with Gmail implementation evidence and coordinates one deterministic DLP evaluation. Use constants: artifact_id art_006; tag handoff-ready with changed_ts 2024-08-24T14:00:00Z; Figma comment by sophie.marketing@company.com anchored node-6:45 at 2024-08-24T14:02:00Z body 'Use latest brand tokens.'; Gmail thread thread_010 message from chris.engineer@company.com at 2024-08-24T14:05:00Z body 'Updated hero copy applied.'; DLP label_if_found dlp-flag with changed_ts 2024-08-24T14:12:00Z. Return the DLP outcome deterministically.",
        actions=[
            Action(name="AddArtifactTag", kwargs={
                "artifact_id": "art_006",
                "tag": "handoff-ready",
                "changed_ts": "2024-08-24T14:00:00Z"
            }),
            Action(name="CreateFigmaComment", kwargs={
                "artifact_id": "art_006",
                "author_email": "sophie.marketing@company.com",
                "body": "Use latest brand tokens.",
                "anchor_ref": "node-6:45",
                "created_ts": "2024-08-24T14:02:00Z"
            }),
            Action(name="AppendMessageToThread", kwargs={
                "thread_id": "thread_010",
                "from_email": "chris.engineer@company.com",
                "body": "Updated hero copy applied.",
                "created_ts": "2024-08-24T14:05:00Z"
            }),
            Action(name="DlpScanAndLabelThread", kwargs={
                "thread_id": "thread_010",
                "label_if_found": "dlp-flag",
                "changed_ts": "2024-08-24T14:12:00Z"
            })
        ],
        outputs=[]
    ),


    # complexity_edges: 13
    Task(
        annotator="0",
        user_id="HARD_28",
        instruction="Oversee the hero handoff within the Figma↔Gmail design-to-build pipeline. Within FRAME artifacts modified on/after 2024-08-01T00:00:00Z and tagged landing-page (email emma.creative@company.com), the homepage frame's authoritative identity is art_001. The finalized record should illustrate: art_001 carrying status handoff-ready effective 2024-08-25T09:00:00Z; a coordination note by jake.design@company.com anchored node-1:3 at 2024-08-25T09:05:00Z with body 'Ready for implementation; confirm responsive behavior.'; and the exported assets listing for art_001 as the stable reference snapshot.",
        actions=[
        Action(name="ListArtifacts", kwargs={
        "owner_email": "emma.creative@company.com",
        "tag": "landing-page",
        "artifact_type": "FRAME",
        "modified_since": "2024-08-01T00:00:00Z"
        }),
        Action(name="AddArtifactTag", kwargs={
        "artifact_id": "art_001",
        "tag": "handoff-ready",
        "changed_ts": "2024-08-25T09:00:00Z"
        }),
        Action(name="CreateFigmaComment", kwargs={
        "artifact_id": "art_001",
        "author_email": "jake.design@company.com",
        "body": "Ready for implementation; confirm responsive behavior.",
        "anchor_ref": "node-1:3",
        "created_ts": "2024-08-25T09:05:00Z"
        }),
        Action(name="ListAssetsForArtifact", kwargs={
        "artifact_id": "art_001"
        })
        ],
        outputs=[]
    ),

    # complexity_edges:  15
    Task(
        annotator="0",
        user_id="HARD_29",
        instruction="Translate Gmail thread sentiments into intents for review regarding a Figma FRAME artifact without dictating the order of calls. Focus anchors: search within FRAME artifacts owned by jake.design@company.com that are tagged 'revise' and have been modified_since 2024-08-01T00:00:00Z; include artifact context art_012; within review cycle cycle_19bc41cf; and mail thread thread_012. Consider grounding constants: review created_ts 2024-08-25T11:00:00Z, link changed_ts 2024-08-25T11:02:00Z, and an exact approval approval from jake.design@company.com at 2024-08-25T11:05:00Z with precise body 'Looks good — LGTM to proceed.'. Deliverable: maintain a synchronized intent summary for {cycle_id: cycle_19bc41cf, thread_id: thread_012} where counts reflect the complete thread history, including this approval.",
        actions=[
            Action(name="ListArtifacts", kwargs={
                "owner_email": "jake.design@company.com",
                "tag": "revise",
                "artifact_type": "FRAME",
                "modified_since": "2024-08-01T00:00:00Z"
            }),
            Action(name="StartReviewCycle", kwargs={
                "artifact_id": "art_012",
                "created_ts": "2024-08-25T11:00:00Z"
            }),
            Action(name="LinkReviewToThread", kwargs={
                "cycle_id": "cycle_19bc41cf",
                "thread_id": "thread_012",
                "changed_ts": "2024-08-25T11:02:00Z"
            }),
            Action(name="AppendMessageToThread", kwargs={
                "thread_id": "thread_012",
                "from_email": "jake.design@company.com",
                "body": "Looks good — LGTM to proceed.",
                "created_ts": "2024-08-25T11:05:00Z"
            }),
            Action(name="SyncGmailIntentsToReview", kwargs={
                "cycle_id": "cycle_19bc41cf",
                "thread_id": "thread_012"
            })
        ],
        outputs=[]
    ),

    # complexity_edges: 13
    Task(
        annotator="0",
        user_id="HARD_30",
        instruction="Coordinate the creation of a brief mobile release summary while ensuring thread cleanliness aligns with policy standards. Regard the release/lineage as definitive, with quantified distinctions for release_002. The audit-ready record for thread_007 must display: a deterministic summary draft composed by emma.creative@company.com at 2024-08-24T11:00:00Z with subject 'Release 1.3.0 Summary' and content 'Key highlights prepared.'; a label status indicating Design/Release along with 'announced' as present as of 2024-08-24T11:05:00Z; and a DLP safety assurance on the same thread. Supply the release_002 diff summary as part of the evidence.",
        actions=[
            Action(name="ListReleases", kwargs={"version_prefix": "release/"}),
            Action(name="GetReleaseDiffSummary", kwargs={"release_id": "release_002"}),
            Action(name="ComposeReleaseEmailDraft", kwargs={
                "release_id": "release_002",
                "thread_id": "thread_007",
                "from_email": "emma.creative@company.com",
                "created_ts": "2024-08-24T11:00:00Z",
                "subject": "Release 1.3.0 Summary",
                "body": "Key highlights prepared."
            }),
            Action(name="UpdateThreadLabels", kwargs={
                "thread_id": "thread_007",
                "add_labels": ["Design/Release", "announced"],
                "remove_labels": [],
                "changed_ts": "2024-08-24T11:05:00Z"
            }),
            Action(name="DlpScanThread", kwargs={"thread_id": "thread_007"})
        ],
        outputs=[]
    ),

    # complexity_edges: 14
    Task(
        annotator="0",
        user_id="HARD_31",
        instruction="Handle the initiation of a combined DS+A11Y audit for the Homepage Hero Section, ensuring evidence is maintained and the policy is tool-agnostic. Scope: Figma FRAME artifacts belonging to emma.creative@company.com, tagged as hero, modified post 2024-08-01T00:00:00Z. Grounding constants: artifact_id art_001, audit_id audit_001, tag audit-pending with changed_ts 2024-08-25T18:35:00Z, audit_type COMBINED_DS_A11Y with created_ts 2024-08-25T18:36:00Z, config_key audit_workflow_config. Include an overview of the already exported assets for provenance, considering Gmail traceability (without sending). Policy: identify and summarize the most recent COMPLETED audit for that artifact; ensure the pending status and session readiness appear in the database without specifying an order. Return only the summarized audit counts.",
        actions=[
            Action(name="ListArtifacts", kwargs={
                "owner_email": "emma.creative@company.com",
                "tag": "hero",
                "artifact_type": "FRAME",
                "modified_since": "2024-08-01T00:00:00Z"
            }),
            Action(name="ListAudits", kwargs={
                "artifact_id": "art_001",
                "status": "COMPLETED"
            }),
            Action(name="SummarizeAudit", kwargs={
                "audit_id": "audit_001"
            }),
            Action(name="AddArtifactTag", kwargs={
                "artifact_id": "art_001",
                "tag": "audit-pending",
                "changed_ts": "2024-08-25T18:35:00Z"
            }),
            Action(name="CreateAuditSession", kwargs={
                "artifact_id": "art_001",
                "created_ts": "2024-08-25T18:36:00Z",
                "audit_type": "COMBINED_DS_A11Y"
            }),
            Action(name="ReadSystemConfig", kwargs={
                "config_key": "audit_workflow_config"
            }),
            Action(name="ListAssetsForArtifact", kwargs={
                "artifact_id": "art_001"
            })
        ],
        outputs=[]
        ),

    # complexity_edges: 13
    Task(
        annotator="0",
        user_id="HARD_32",
        instruction="Interpret brand guidance into provenance and review context, leaving sequence unscripted. Employ constants: artifact_id art_003, thread_id thread_003; Gmail note from design.system@company.com on 2024-08-23T12:10:00Z with text 'Brand tokens aligned with DS v3.'; review annotation on Figma fixed at node-2:7 by sophie.marketing@company.com on 2024-08-23T12:00:00Z stating 'Please update the brand color token to Brand/Primary/600.'. Incorporate a DLP safety check on the Gmail thread. Return the author-specific comment history for art_003 filtered to author_email sophie.marketing@company.com since 2024-08-01T00:00:00Z.",
        actions=[
            Action(name="AppendMessageToThread", kwargs={
                "thread_id": "thread_003",
                "from_email": "design.system@company.com",
                "body": "Brand tokens aligned with DS v3.",
                "created_ts": "2024-08-23T12:10:00Z"
            }),
            Action(name="DlpScanThread", kwargs={"thread_id": "thread_003"}),
            Action(name="CreateFigmaComment", kwargs={
                "artifact_id": "art_003",
                "author_email": "sophie.marketing@company.com",
                "body": "Please update the brand color token to Brand/Primary/600.",
                "anchor_ref": "node-2:7",
                "created_ts": "2024-08-23T12:00:00Z"
            }),
            Action(name="ListFigmaComments", kwargs={
                "artifact_id": "art_003",
                "author_email": "sophie.marketing@company.com",
                "since_ts": "2024-08-01T00:00:00Z"
            })
        ],
        outputs=[]
    ),

    # complexity_edges: 13
    Task(
        annotator="0",
        user_id="HARD_33",
        instruction="Act as a Figma↔Gmail workflow steward completing a pricing review in a compliant, audit-ready manner. In FRAME artifacts identified with pricing and belonging to anna.brand@company.com (changed since 2024-08-01T00:00:00Z), the main identifier for the homepage pricing frame is art_007. The official snapshot must demonstrate: the removal of stale status without needs-review as of 2024-08-25T18:40:00Z; a provenance annotation on the artifact by pm.lead@company.com linking node-3:3 at 2024-08-25T18:41:00Z containing this precise text 'Removed 'needs-review' after approval; proceeding to implementation.'; and the concluding artifact summary for art_007 serving as the definitive reference for downstream access within the MCP pipeline.",
        actions=[
            Action(name="ListArtifacts", kwargs={
                "owner_email": "anna.brand@company.com",
                "tag": "pricing",
                "artifact_type": "FRAME",
                "modified_since": "2024-08-01T00:00:00Z"
            }),
            Action(name="RemoveArtifactTag", kwargs={
                "artifact_id": "art_007",
                "tag": "needs-review",
                "changed_ts": "2024-08-25T18:40:00Z"
            }),
            Action(name="CreateFigmaComment", kwargs={
                "artifact_id": "art_007",
                "author_email": "pm.lead@company.com",
                "body": "Removed 'needs-review' after approval; proceeding to implementation.",
                "anchor_ref": "node-3:3",
                "created_ts": "2024-08-25T18:41:00Z"
            }),
            Action(name="GetArtifactSummary", kwargs={
                "artifact_id": "art_007"
            })
        ],
        outputs=[]
        ),

    # complexity_edges:  14
    Task(
        annotator="0",
        user_id="HARD_34",
        instruction="Serve as the release-comms safety coordinator managing operations between Gmail and the release catalog to ensure policy-clean visibility. The audit-ready documentation must present: source mail thread_003 with a sensitive note from anna.brand@company.com at 2024-08-23T09:00:00Z stating 'Temporary password is abcd-1234. Rotate after testing.' and a solo safety assessment implementing dlp-flag at 2024-08-23T09:05:00Z; additionally, a decisive 1.4.0 announcement draft for release_004 in thread_008 by emma.creative@company.com at 2024-08-23T16:30:00Z titled 'Release 1.4.0 Announcement' with content 'Changelog and new components included.' The outcome is a collection of threads categorized under the label dlp-flag, aligning with the Release Notes & Asset Handoff workflow.",
        actions=[
            Action(name="AppendMessageToThread", kwargs={
                "thread_id": "thread_003",
                "from_email": "anna.brand@company.com",
                "body": "Temporary password is abcd-1234. Rotate after testing.",
                "created_ts": "2024-08-23T09:00:00Z"
            }),
            Action(name="DlpScanAndLabelThread", kwargs={
                "thread_id": "thread_003",
                "label_if_found": "dlp-flag",
                "changed_ts": "2024-08-23T09:05:00Z"
            }),
            Action(name="ComposeReleaseEmailDraft", kwargs={
                "release_id": "release_004",
                "thread_id": "thread_008",
                "from_email": "emma.creative@company.com",
                "created_ts": "2024-08-23T16:30:00Z",
                "subject": "Release 1.4.0 Announcement",
                "body": "Changelog and new components included."
            }),
            Action(name="SearchGmailThreads", kwargs={"label": "dlp-flag"})
        ],
        outputs=[]
    ),

    # complexity_edges: 14
    Task(
        annotator="0",
        user_id="HARD_35",
        instruction="Finalize a ready-for-release dialogue ensuring asset lineage is retained for downstream transfer. Ensure the authoritative snapshot includes: the preserved release_001 draft in thread_006 by emma.creative@company.com on 2024-08-22T17:00:00Z with subject 'Release 1.2.0 Announcement' and body 'Highlights and changes included.'; a QA memo from qa.lead@company.com on 2024-08-22T17:06:00Z with body 'QA sign-off complete'; a conversational status indicating readiness for release effective 2024-08-22T17:10:00Z; and the listing of exported assets for artifact_id art_001 as the stable asset reference aligned to the Figma↔Gmail release workflow.",
        actions=[
            Action(name="ComposeReleaseEmailDraft", kwargs={
                "release_id": "release_001",
                "thread_id": "thread_006",
                "from_email": "emma.creative@company.com",
                "created_ts": "2024-08-22T17:00:00Z",
                "subject": "Release 1.2.0 Announcement",
                "body": "Highlights and changes included."
            }),
            Action(name="AppendMessageToThread", kwargs={
                "thread_id": "thread_006",
                "from_email": "qa.lead@company.com",
                "body": "QA sign-off complete",
                "created_ts": "2024-08-22T17:06:00Z"
            }),
            Action(name="UpdateThreadLabels", kwargs={
                "thread_id": "thread_006",
                "add_labels": ["release-ready"],
                "remove_labels": [],
                "changed_ts": "2024-08-22T17:10:00Z"
            }),
            Action(name="ListAssetsForArtifact", kwargs={"artifact_id": "art_001"})
        ],
        outputs=[]
    ),

    # complexity_edges: 13
    Task(
        annotator="0",
        user_id="HARD_36",
        instruction="Convert Gmail pricing feedback into a governed review process including one safety evaluation and obtainable evidence—without mandating sequence. Adhere to the Email-Centric Design Review policy (Figma↔Gmail). Key constants: artifact_id art_007, cycle_id cycle_38980610, thread_id thread_008; created_ts 2024-08-23T12:00:00Z and changed_ts 2024-08-23T12:05:00Z; and one clear intent “APPROVED - ship it” from chris.engineer@company.com at 2024-08-23T12:06:00Z. Deliver an audit-capable snapshot where review intents for cycle_38980610/thread_008 are represented, a single safety evaluation is documented, and evidence can be located with the keyword “Pricing”.",
        actions=[
            Action(name="StartReviewCycle", kwargs={"artifact_id": "art_007", "created_ts": "2024-08-23T12:00:00Z"}),
            Action(name="LinkReviewToThread", kwargs={
                "cycle_id": "cycle_38980610",
                "thread_id": "thread_008",
                "changed_ts": "2024-08-23T12:05:00Z"
            }),
            Action(name="AppendMessageToThread", kwargs={
                "thread_id": "thread_008",
                "from_email": "chris.engineer@company.com",
                "body": "APPROVED - ship it",
                "created_ts": "2024-08-23T12:06:00Z"
            }),
            Action(name="SyncGmailIntentsToReview", kwargs={
                "cycle_id": "cycle_38980610",
                "thread_id": "thread_008"
            }),
            Action(name="DlpScanThread", kwargs={"thread_id": "thread_008"}),
            Action(name="SearchGmailThreads", kwargs={"keyword": "Pricing"})
        ],
        outputs=[]
    ),

    # complexity_edges: 15
    Task(
        annotator="0",
        user_id="HARD_37",
        instruction="As the Figma↔Gmail release communications steward, ensure lineage, attachment guardrails, and downstream discoverability are maintained. The audit-ready record must show: releases identified under the prefix release/ with the definitive diff for release_001; a fixed announcement draft in Google thread_006 by emma.creative@company.com dated 2024-08-22T17:00:00Z with subject “Release 1.2.0 Announcement” and the body “Highlights and changes included.”; attachment guardrails noted under message_id relmsg_9cc87e81; a conversation stance with Design/Release and announced status effective 2024-08-22T17:06:30Z; along with the diff summary for release_001 serving as the stable reference for stakeholders within the Release Notes workflow.",
        actions=[
            Action(name="ListReleases", kwargs={"version_prefix": "release/"}),
            Action(name="GetReleaseDiffSummary", kwargs={"release_id": "release_001"}),
            Action(name="ComposeReleaseEmailDraft", kwargs={
                "release_id": "release_001",
                "thread_id": "thread_006",
                "from_email": "emma.creative@company.com",
                "created_ts": "2024-08-22T17:00:00Z",
                "subject": "Release 1.2.0 Announcement",
                "body": "Highlights and changes included."
            }),
            Action(name="GuardAttachmentPolicyOnDraft", kwargs={"message_id": "relmsg_9cc87e81"}),
            Action(name="UpdateThreadLabels", kwargs={
                "thread_id": "thread_006",
                "add_labels": ["Design/Release", "announced"],
                "remove_labels": [],
                "changed_ts": "2024-08-22T17:06:30Z"
            }),
            Action(name="GetReleaseDiffSummary", kwargs={"release_id": "release_001"})
        ],
        outputs=[]
    ),

    # complexity_edges: 14
    Task(
        annotator="0",
        user_id="HARD_38",
        instruction="Oversee the Figma↔Gmail review orchestration for the pricing module, ensuring controlled progress, safety posture, and searchable traceability within the Email-Centric Design Review & Approval workflow. Provide an audit-ready snapshot capturing—as immutable facts—the following details: a review for Figma artifact art_007 with creation time 2024-08-23T12:00:00Z logged under cycle_38980610; linked to the source conversation thread_008 effective 2024-08-23T12:05:00Z; a definitive approval signal in the Google conversation from chris.engineer@company.com timestamped at 2024-08-23T12:06:00Z with the precise text “APPROVED - ship it”; synchronized intent counts within the same review cycle; and a safety confirmation for thread_008. For downstream discoverability, also ensure inclusion of threads searchable by the keyword “Pricing.” Adhere strictly to all literals and refrain from introducing substitutes.",
        actions=[
            Action(name="StartReviewCycle", kwargs={"artifact_id": "art_007", "created_ts": "2024-08-23T12:00:00Z"}),
            Action(name="LinkReviewToThread", kwargs={
                "cycle_id": "cycle_38980610",
                "thread_id": "thread_008",
                "changed_ts": "2024-08-23T12:05:00Z"
            }),
            Action(name="AppendMessageToThread", kwargs={
                "thread_id": "thread_008",
                "from_email": "chris.engineer@company.com",
                "body": "APPROVED - ship it",
                "created_ts": "2024-08-23T12:06:00Z"
            }),
            Action(name="SyncGmailIntentsToReview", kwargs={
                "cycle_id": "cycle_38980610",
                "thread_id": "thread_008"
            }),
            Action(name="DlpScanThread", kwargs={"thread_id": "thread_008"}),
            Action(name="SearchGmailThreads", kwargs={"keyword": "Pricing"})
        ],
        outputs=[]
    ),

    # complexity_edges: 14
    Task(
        annotator="0",
        user_id="HARD_39",
        instruction="Act as the cross-channel asset-readiness manager for the Release Notes & Asset Handoff process, ensuring export lineage, coordinated safety posture, and cross-system discoverability across Figma↔Gmail. Generate an audit-ready snapshot that demonstrates—as immutable facts (a record, not a procedure)—the following: Figma artifact art_001 in status handoff-ready effective 2024-08-24T10:00:00Z; an outcomes note authored by jake.design@company.com anchored node-1:12 at 2024-08-24T10:02:00Z with the exact body 'Hero assets exported—keep alt text synced.'; source mail context thread_004 recording a coordination note from design.system@company.com at 2024-08-24T10:03:00Z with the exact text 'Assets exported for homepage hero.'; and a single safety evaluation documented as of 08-24T10:04:00Z, where dlp-flag is used only upon detection. Include the exported assets listing for artifact_id art_001 as the stable delivery reference. Honor the literals exactly and introduce no substitutes.",
        actions=[
            Action(name="AddArtifactTag", kwargs={
                "artifact_id": "art_001",
                "tag": "handoff-ready",
                "changed_ts": "2024-08-24T10:00:00Z"
            }),
            Action(name="CreateFigmaComment", kwargs={
                "artifact_id": "art_001",
                "author_email": "jake.design@company.com",
                "body": "Hero assets exported—keep alt text synced.",
                "anchor_ref": "node-1:12",
                "created_ts": "2024-08-24T10:02:00Z"
            }),
            Action(name="AppendMessageToThread", kwargs={
                "thread_id": "thread_004",
                "from_email": "design.system@company.com",
                "body": "Assets exported for homepage hero.",
                "created_ts": "2024-08-24T10:03:00Z"
            }),
            Action(name="DlpScanAndLabelThread", kwargs={
                "thread_id": "thread_004",
                "label_if_found": "dlp-flag",
                "changed_ts": "2024-08-24T10:04:00Z"
            }),
            Action(name="ListAssetsForArtifact", kwargs={"artifact_id": "art_001"})
        ],
        outputs=[]
    ),

    # complexity_edges: 14
    Task(
        annotator="0",
        user_id="HARD_40",
        instruction=(
            "Assume the role of the guarded release-draft coordinator ensuring lineage, attachment safety, and a release-ready posture. Document a non-procedural, audit-ready snapshot that verifies: operation within the release/ lineage with release_001 as the diff authority; a release Gmail draft in thread_006 from emma.creative@company.com at 2024-08-22T17:00:00Z with subject 'Release 1.2.0 Announcement' and body 'Highlights and changes included.'; attachment-policy validation via message_id relmsg_9cc87e81; and a conversation state where Design/Release and release-ready are present effective 2024-08-22T17:06:00Z. Provide the exported assets tied to art_001 as the stable reference."
        ),
        actions=[
            Action(name="ListReleases", kwargs={"version_prefix": "release/"}),
            Action(name="GetReleaseDiffSummary", kwargs={"release_id": "release_001"}),
            Action(name="ComposeReleaseEmailDraft", kwargs={"release_id": "release_001", "thread_id": "thread_006", "from_email": "emma.creative@company.com", "created_ts": "2024-08-22T17:00:00Z", "subject": "Release 1.2.0 Announcement", "body": "Highlights and changes included."}),
            Action(name="GuardAttachmentPolicyOnDraft", kwargs={"message_id": "relmsg_9cc87e81"}),
            Action(name="UpdateThreadLabels", kwargs={"thread_id": "thread_006", "add_labels": ["Design/Release", "release-ready"], "remove_labels": [], "changed_ts": "2024-08-22T17:06:00Z"}),
            Action(name="ListAssetsForArtifact", kwargs={"artifact_id": "art_001"}),
        ],
        outputs=[]
    ),

    # complexity_edges: 13
    Task(
        annotator="0",
        user_id="HARD_41",
        instruction="Act as the steward responsible for ensuring readiness for handoff by maintaining alignment between Figma and Gmail in terms of posture and tag organization. Provide an audit-ready record (focusing on facts rather than procedures) demonstrating: configuration baselines, design_system_mappings, and intent_keywords consulted; art_001 set as handoff-ready effective 2024-08-25T08:00:00Z; terminal note 'Applied temporary handoff tag for art_001' logged at 2024-08-25T08:01:00Z; handoff-check present by 2024-08-25T08:05:00Z and removed by 2024-08-25T08:25:00Z; the status of being handoff-ready removed by 2024-08-25T08:30:00Z; and terminal note 'Removed temporary handoff tag for art_001' documented at 2024-08-25T08:31:00Z; alongside the exported asset list for art_001 serving as a stable reference. Consider tag and log changes as lasting modifications to the database, maintaining immutable timestamps.",
        actions=[
            Action(name="ReadSystemConfig", kwargs={"config_key": "design_system_mappings"}),
            Action(name="AddArtifactTag", kwargs={"artifact_id": "art_001", "tag": "handoff-ready", "changed_ts": "2024-08-25T08:00:00Z"}),
            Action(name="LogTerminalEvent", kwargs={"log_ts": "2024-08-25T08:01:00Z", "message": "Applied temporary handoff tag for art_001"}),
            Action(name="AddArtifactTag", kwargs={"artifact_id": "art_001", "tag": "handoff-check", "changed_ts": "2024-08-25T08:05:00Z"}),
            Action(name="RemoveArtifactTag", kwargs={"artifact_id": "art_001", "tag": "handoff-check", "changed_ts": "2024-08-25T08:25:00Z"}),
            Action(name="RemoveArtifactTag", kwargs={"artifact_id": "art_001", "tag": "handoff-ready", "changed_ts": "2024-08-25T08:30:00Z"}),
            Action(name="LogTerminalEvent", kwargs={"log_ts": "2024-08-25T08:31:00Z", "message": "Removed temporary handoff tag for art_001"}),
            Action(name="ReadSystemConfig", kwargs={"config_key": "intent_keywords"}),
            Action(name="ListAssetsForArtifact", kwargs={"artifact_id": "art_001"}),
        ],
        outputs=[]
    ),


    # complexity_edges: 15
    Task(
        annotator="0",
        user_id="HARD_42",
        instruction="Serve as the steward for ensuring communications are release-ready and conform to attachment guardrails. Deliver a non-procedural, audit-ready snapshot verifying: a deterministic Gmail draft for release_001 within thread_006 from emma.creative@company.com at 2024-08-22T17:00:00Z, carrying the subject 'Release 1.2.0 Announcement' and content 'Highlights and changes included.'; confirmation of attachment-policy through Gmail message_id relmsg_9cc87e81; the conversation stance noted on Figma thread_006 with Design/Release and sentiment/positive identified and draft noted as absent by 08-22T17:05:00Z; the QA note 'QA sign-off complete' created by qa.lead@company.com at 08-22T17:06:00Z; and the exported assets linked to art_001 serving as the stable evidence.",
        actions=[
            Action(name="ComposeReleaseEmailDraft", kwargs={"release_id": "release_001", "thread_id": "thread_006", "from_email": "emma.creative@company.com", "created_ts": "2024-08-22T17:00:00Z", "subject": "Release 1.2.0 Announcement", "body": "Highlights and changes included."}),
            Action(name="GuardAttachmentPolicyOnDraft", kwargs={"message_id": "relmsg_9cc87e81"}),
            Action(name="UpdateThreadLabels", kwargs={"thread_id": "thread_006", "add_labels": ["Design/Release", "sentiment/positive"], "remove_labels": ["draft"], "changed_ts": "2024-08-22T17:05:00Z"}),
            Action(name="AppendMessageToThread", kwargs={"thread_id": "thread_006", "from_email": "qa.lead@company.com", "body": "QA sign-off complete", "created_ts": "2024-08-22T17:06:00Z"}),
            Action(name="ListAssetsForArtifact", kwargs={"artifact_id": "art_001"}),
        ],
        outputs=[]
    ),

    # complexity_edges: 17
    Task(
        annotator="0",
        user_id="HARD_43",
        instruction="As the provenance steward responsible for finalizing the review process with label normalization accordance, deliver an audit-ready, non-procedural snapshot that confirms: a cycle for art_004 initiated at 2024-08-23T13:00:00Z (cycle_1dc59e3f) and connected to thread_003 at 08-23T13:05:00Z; status NEEDS_REVIEW effective 08-23T13:20:00Z; an APPROVED decision by chris.engineer@company.com at 08-23T13:25:00Z with the comment 'LGTM'; a normalized label posture on thread_003 indicating that Design/Approved is present and Design/Needs-Review is not present as of 08-23T13:30:00Z; the terminal log 'Review approved and labels aligned' at 08-23T13:31:00Z; and the exported assets for art_001 as the stable reference.",
        actions=[
            Action(name="StartReviewCycle", kwargs={"artifact_id": "art_004", "created_ts": "2024-08-23T13:00:00Z"}),
            Action(name="LinkReviewToThread", kwargs={"cycle_id": "cycle_1dc59e3f", "thread_id": "thread_003", "changed_ts": "2024-08-23T13:05:00Z"}),
            Action(name="AdvanceReviewStatus", kwargs={"cycle_id": "cycle_1dc59e3f", "new_status": "NEEDS_REVIEW", "changed_ts": "2024-08-23T13:20:00Z"}),
            Action(name="RecordReviewApproval", kwargs={"cycle_id": "cycle_1dc59e3f", "approver_email": "chris.engineer@company.com", "decision": "APPROVED", "decided_ts": "2024-08-23T13:25:00Z", "comment": "LGTM"}),
            Action(name="UpdateThreadLabels", kwargs={"thread_id": "thread_003", "add_labels": ["Design/Approved"], "remove_labels": ["Design/Needs-Review"], "changed_ts": "2024-08-23T13:30:00Z"}),
            Action(name="LogTerminalEvent", kwargs={"log_ts": "2024-08-23T13:31:00Z", "message": "Review approved and labels aligned"}),
            Action(name="ListAssetsForArtifact", kwargs={"artifact_id": "art_001"}),
        ],
        outputs=[]
    ),


    # complexity_edges: 14
    Task(
        annotator="0",
        user_id="HARD_44",
        instruction="Act as the Gmail→Figma signal-quantification steward tasked with ensuring sentiment posture without specifying steps. Generate an audit-ready, non-procedural record that provides evidence showing: a review for Figma art_004 initiated at 2024-08-23T13:00:00Z within deterministic cycle_id cycle_1dc59e3f; connection to source conversation thread_003 effective 2024-08-23T13:05:00Z; two Gmail messages identified as intents—'Looks good—LGTM from marketing.' from anna.brand@company.com at 2024-08-23T13:10:00Z and 'Please REVISE the grid spacing to 8px multiples.' from chris.engineer@company.com at 2024-08-23T13:15:00Z; a conversation stance on thread_003 with sentiment/mixed present effective 2024-08-23T13:16:00Z; synchronized Gmail intents on the same cycle; and the exported assets for art_001 as the stable handoff reference.",
        actions=[
            Action(name="StartReviewCycle", kwargs={"artifact_id": "art_004", "created_ts": "2024-08-23T13:00:00Z"}),
            Action(name="LinkReviewToThread", kwargs={"cycle_id": "cycle_1dc59e3f", "thread_id": "thread_003", "changed_ts": "2024-08-23T13:05:00Z"}),
            Action(name="AppendMessageToThread", kwargs={"thread_id": "thread_003", "from_email": "anna.brand@company.com", "body": "Looks good—LGTM from marketing.", "created_ts": "2024-08-23T13:10:00Z"}),
            Action(name="AppendMessageToThread", kwargs={"thread_id": "thread_003", "from_email": "chris.engineer@company.com", "body": "Please REVISE the grid spacing to 8px multiples.", "created_ts": "2024-08-23T13:15:00Z"}),
            Action(name="UpdateThreadLabels", kwargs={"thread_id": "thread_003", "add_labels": ["sentiment/mixed"], "remove_labels": [], "changed_ts": "2024-08-23T13:16:00Z"}),
            Action(name="SyncGmailIntentsToReview", kwargs={"cycle_id": "cycle_1dc59e3f", "thread_id": "thread_003"}),
            Action(name="ListAssetsForArtifact", kwargs={"artifact_id": "art_001"}),
        ],
        outputs=[]
    ),


    # complexity_edges: 13
    Task(
        annotator="0",
        user_id="HARD_45",
        instruction="Translate governance intent into a standard audit state for marketing navigation without establishing a sequence. Utilize constants: artifact_id art_006; audit_type COMBINED_DS_A11Y with created_ts 2024-08-28T13:00:00Z; terminal log at 2024-08-28T13:05:00Z message 'Prepared audit for art_006'; tag audit-in-progress added at 2024-08-28T13:06:00Z and removed at 2024-08-28T13:20:00Z; config_key design_system_mappings. Context: Figma FILE with Gmail-linked traceability (no email required). Policy: verify design-system mapping, maintain the audit posture and tag lifecycle in the database, and consider the canonical artifact summary as authoritative. Deliver only the artifact summary for art_006 reflecting modified_ts 2024-08-28T13:20:00Z.",
        actions=[
            Action(name="ReadSystemConfig", kwargs={"config_key": "design_system_mappings"}),
            Action(name="CreateAuditSession", kwargs={
                "artifact_id": "art_006",
                "created_ts": "2024-08-28T13:00:00Z",
                "audit_type": "COMBINED_DS_A11Y"
            }),
            Action(name="LogTerminalEvent", kwargs={
                "log_ts": "2024-08-28T13:05:00Z",
                "message": "Prepared audit for art_006"
            }),
            Action(name="AddArtifactTag", kwargs={
                "artifact_id": "art_006",
                "tag": "audit-in-progress",
                "changed_ts": "2024-08-28T13:06:00Z"
            }),
            Action(name="RemoveArtifactTag", kwargs={
                "artifact_id": "art_006",
                "tag": "audit-in-progress",
                "changed_ts": "2024-08-28T13:20:00Z"
            }),
            Action(name="GetArtifactSummary", kwargs={"artifact_id": "art_006"}),
        ],
        outputs=[]
    ),

    # complexity_edges: 13
    Task(
        annotator="0",
        user_id="HARD_46",
        instruction="Serve as a budget-disciplined fix-planning steward for marketing website accessibility who documents an audit-ready record of planning signals without a detailed prescription. Governance orientation cites fix_workflow_config; planning lifecycle for art_006 shows a11y-queued present at 2024-08-28T15:05:00Z, fix-planned present at 2024-08-28T15:10:00Z, the narrative “Fix plan drafted for art_006” captured at 2024-08-28T15:11:00Z, and fix-planned cleared at 2024-08-28T15:30:00Z; authoritative status is depicted by the canonical artifact summary for art_006 reflecting modified_ts 2024-08-28T15:30:00Z.",
        actions=[
            Action(name="ReadSystemConfig", kwargs={"config_key": "fix_workflow_config"}),
            Action(name="AddArtifactTag", kwargs={
                "artifact_id": "art_006",
                "tag": "a11y-queued",
                "changed_ts": "2024-08-28T15:05:00Z"
            }),
            Action(name="AddArtifactTag", kwargs={
                "artifact_id": "art_006",
                "tag": "fix-planned",
                "changed_ts": "2024-08-28T15:10:00Z"
            }),
            Action(name="LogTerminalEvent", kwargs={
                "log_ts": "2024-08-28T15:11:00Z",
                "message": "Fix plan drafted for art_006"
            }),
            Action(name="RemoveArtifactTag", kwargs={
                "artifact_id": "art_006",
                "tag": "fix-planned",
                "changed_ts": "2024-08-28T15:30:00Z"
            }),
            Action(name="GetArtifactSummary", kwargs={"artifact_id": "art_006"}),
        ],
        outputs=[]
    ),

    # complexity_edges: 14
    Task(
        annotator="0",
        user_id="HARD_47",
        instruction="You are responsible for capturing brand accessibility directives across Figma↔Gmail. Desired outcome: intent_keywords referenced; art_012 features a brand note by sophie.marketing@company.com at 2024-08-26T09:00:00Z linked to node-12:1 with the content “Align tokens with brand v3.” and a QA note by brand.qa@company.com at 2024-08-26T09:05:00Z linked to node-12:2 with the content “Verify logo safe-area usage.”; thread_001 includes triaged and figma-sync and omits urgent with a changed_ts of 2024-08-26T09:06:00Z; an audit log entry “Brand feedback captured for art_012” at 2024-08-26T09:07:00Z; and exported assets for art_001 for discoverability.",
        actions=[
            Action(name="ReadSystemConfig", kwargs={"config_key": "intent_keywords"}),
            Action(name="CreateFigmaComment", kwargs={"artifact_id": "art_012", "author_email": "sophie.marketing@company.com", "body": "Align tokens with brand v3.", "anchor_ref": "node-12:1", "created_ts": "2024-08-26T09:00:00Z"}),
            Action(name="CreateFigmaComment", kwargs={"artifact_id": "art_012", "author_email": "brand.qa@company.com", "body": "Verify logo safe-area usage.", "anchor_ref": "node-12:2", "created_ts": "2024-08-26T09:05:00Z"}),
            Action(name="UpdateThreadLabels", kwargs={"thread_id": "thread_001", "add_labels": ["triaged", "figma-sync"], "remove_labels": ["urgent"], "changed_ts": "2024-08-26T09:06:00Z"}),
            Action(name="LogTerminalEvent", kwargs={"log_ts": "2024-08-26T09:07:00Z", "message": "Brand feedback captured for art_012"}),
            Action(name="ListAssetsForArtifact", kwargs={"artifact_id": "art_001"}),
        ],
        outputs=[]
    ),

    # complexity_edges: 13
    Task(
        annotator="0",
        user_id="HARD_48",
        instruction="You act as the steward for brand-guidance provenance, guaranteeing traceability aligned with policies for design-system tokens through the Figma↔Gmail workflow. Generate an audit-compliant record (facts only) that verifies: the policy config intent_keywords was consulted; on art_003 a Figma comment linked to node-2:7 by sophie.marketing@company.com (Gmail identity) at 2024-08-28T09:05:00Z with the exact message “Please update the brand color token to Brand/Primary/600.”; thread_005 reflects DB label hygiene with triaged present and update absent as of 2024-08-28T09:06:00Z; a terminal log entry “Brand guidance captured for Design System” at 2024-08-28T09:07:00Z; and the canonical artifact summary for art_003 as the result of the coordination.",
        actions=[
            Action(name="ReadSystemConfig", kwargs={"config_key": "intent_keywords"}),
            Action(name="UpdateThreadLabels", kwargs={"thread_id": "thread_005", "add_labels": ["triaged"], "remove_labels": ["update"], "changed_ts": "2024-08-28T09:06:00Z"}),
            Action(name="CreateFigmaComment", kwargs={"artifact_id": "art_003", "author_email": "sophie.marketing@company.com", "body": "Please update the brand color token to Brand/Primary/600.", "anchor_ref": "node-2:7", "created_ts": "2024-08-28T09:05:00Z"}),
            Action(name="LogTerminalEvent", kwargs={"log_ts": "2024-08-28T09:07:00Z", "message": "Brand guidance captured for Design System"}),
            Action(name="GetArtifactSummary", kwargs={"artifact_id": "art_003"}),
        ],
        outputs=[]
    ),

    # complexity_edges: 13
    Task(
        annotator="0",
        user_id="HARD_49",
        instruction="As an intake coordinator focused on review intents, your duty is to convert Gmail feedback into deterministic evidence without modifying the review status. The primary task involves managing review provenance for art_004 associated with cycle_id cycle_b73c0216, connected to thread_010 (initiated 2024-08-24T09:00:00Z / linked 2024-08-24T09:05:00Z). The intake procedure concentrates on two intent messages: one from chris.engineer@company.com at 2024-08-24T09:10:00Z with the text 'Looks good—LGTM from engineering.' and another from anna.brand@company.com at 2024-08-24T09:12:00Z with the message 'Please adjust spacing to 8px grid; otherwise fine.' Deliver the outcome of the most recent appended message.",
        actions=[
            Action(name="StartReviewCycle", kwargs={
                "artifact_id": "art_004",
                "created_ts": "2024-08-24T09:00:00Z"
            }),
            Action(name="LinkReviewToThread", kwargs={
                "cycle_id": "cycle_b73c0216",
                "thread_id": "thread_010",
                "changed_ts": "2024-08-24T09:05:00Z"
            }),
            Action(name="AppendMessageToThread", kwargs={
                "thread_id": "thread_010",
                "from_email": "chris.engineer@company.com",
                "body": "Looks good—LGTM from engineering.",
                "created_ts": "2024-08-24T09:10:00Z"
            }),
            Action(name="AppendMessageToThread", kwargs={
                "thread_id": "thread_010",
                "from_email": "anna.brand@company.com",
                "body": "Please adjust spacing to 8px grid; otherwise fine.",
                "created_ts": "2024-08-24T09:12:00Z"
            }),
        ],
        outputs=[]
    ),

    # complexity_edges: 13
    Task(
        annotator="0",
        user_id="HARD_50",
        instruction="Coordinate the consolidation of release communications into a unified Gmail thread with deterministic provenance and state supported by a database, without determining the order. Utilize constants: release_id release_001, thread_id thread_010, from_email emma.creative@company.com with creation timestamp 2024-08-22T17:00:00Z, subject 'Release 1.2.0 Announcement', body 'Highlights and changes included.', label 'announced' with updated timestamp 2024-08-22T17:06:00Z, along with an approval note 'APPROVE rollout.' at 2024-08-22T17:07:00Z. Adhere to the policy: ensure the draft, announced status, and approval are recorded so that the DB reflects Gmail; Figma context may be utilized as metadata. Return only the result of the final append.",
        actions=[
            Action(name="ComposeReleaseEmailDraft", kwargs={
                "release_id": "release_001",
                "thread_id": "thread_010",
                "from_email": "emma.creative@company.com",
                "created_ts": "2024-08-22T17:00:00Z",
                "subject": "Release 1.2.0 Announcement",
                "body": "Highlights and changes included."
            }),
            Action(name="UpdateThreadLabels", kwargs={
                "thread_id": "thread_010",
                "add_labels": ["announced"],
                "remove_labels": [],
                "changed_ts": "2024-08-22T17:06:00Z"
            }),
            Action(name="AppendMessageToThread", kwargs={
                "thread_id": "thread_010",
                "from_email": "emma.creative@company.com",
                "body": "APPROVE rollout.",
                "created_ts": "2024-08-22T17:07:00Z"
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="EXP_1",
        instruction=(
            "You manage structured review coordination, tasked with converting admin navigation update signals into an auditable trail for artifact_id art_011 and thread_id thread_013. Capture, align, and surface stakeholder intent and design guidance to ensure decision traceability and accessibility of the review record. Coordinate capturing two primary decision signals—msg1 at 2024-08-23T22:10:00Z from pm.lead@company.com stating 'Approve navigation density.' and msg2 at 2024-08-23T22:15:00Z from qa.lead@company.com noting 'Blocker: overflow on mobile filter.'—and reflect the review posture through label alignment when 'triaged' and 'needs-review' are present with changed_ts 2024-08-23T22:25:00Z. Design oversight is indicated by a design note at 2024-08-23T22:30:00Z from design.lead@company.com linked to node-11:3 providing guidance 'Proceed after mobile fix.' Ensure compliance with safety governance using data loss prevention policy; if blocked content is found, the thread is flagged with dlp-flag and dlp_changed_ts 2024-08-23T22:35:00Z. Your role is to guarantee coherent review coordination, traceable decision signals, proper DLP posture application, and a complete auditable navigation update trail."
        ),
        actions=[
            Action(name="AppendMessageToThread", kwargs={
                "thread_id": "thread_013",
                "from_email": "pm.lead@company.com",
                "body": "Approve navigation density.",
                "created_ts": "2024-08-23T22:10:00Z"
            }),
            Action(name="AppendMessageToThread", kwargs={
                "thread_id": "thread_013",
                "from_email": "qa.lead@company.com",
                "body": "Blocker: overflow on mobile filter.",
                "created_ts": "2024-08-23T22:15:00Z"
            }),
            Action(name="UpdateThreadLabels", kwargs={
                "thread_id": "thread_013",
                "add_labels": ["triaged", "needs-review"],
                "remove_labels": [],
                "changed_ts": "2024-08-23T22:25:00Z"
            }),
            Action(name="CreateFigmaComment", kwargs={
                "artifact_id": "art_011",
                "author_email": "design.lead@company.com",
                "body": "Proceed after mobile fix.",
                "anchor_ref": "node-11:3",
                "created_ts": "2024-08-23T22:30:00Z"
            }),
            Action(name="DlpScanAndLabelThread", kwargs={
                "thread_id": "thread_013",
                "label_if_found": "dlp-flag",
                "changed_ts": "2024-08-23T22:35:00Z"
            })
        ],
        outputs=[]
    ),


    Task(
        annotator="0",
        user_id="EXP_2",
        instruction=(
            "As the admin panel coordination owner, align comment traceability, asset visibility, release awareness, and safety posture without imposing a fixed sequence. Concentrate on art_008 and its discussion in thread_004: document a deterministic resolution note by jake.design@company.com positioned at node-8:13 at 2024-08-24T18:46:00Z with the content 'Admin header focus order and ARIA attributes validated; keyboard navigation confirmed.' Maintain a current snapshot of assets for art_008 to indicate readiness. Record a precise coordination update in thread_004 from design.system@company.com at 2024-08-24T18:48:00Z with the content 'Admin panel changes synced—moving to validation.' Preserve the safety posture through a single evaluation in thread_004 with label_if_found dlp-flag and changed_ts 2024-08-24T18:50:00Z. Base decisions on dlp_config and design_system_mappings, and sustain awareness of release_002 with a diff snapshot. Constants: artifact_id art_008, comment_id comment_006, asset_id asset_007, thread_id thread_004, release_id release_002."
        ),
        actions=[
            Action(name="ListFigmaComments", kwargs={"artifact_id": "art_008"}),
            Action(name="CreateFigmaComment", kwargs={
                "artifact_id": "art_008",
                "author_email": "jake.design@company.com",
                "body": "Admin header focus order and ARIA attributes validated; keyboard navigation confirmed",
                "anchor_ref": "node-8:13",
                "created_ts": "2024-08-24T18:46:00Z"
            }),
            Action(name="ListAssetsForArtifact", kwargs={"artifact_id": "art_008"}),
            Action(name="AppendMessageToThread", kwargs={
                "thread_id": "thread_004",
                "from_email": "design.system@company.com",
                "body": "Admin panel changes synced—moving to validation.",
                "created_ts": "2024-08-24T18:48:00Z"
            }),
            Action(name="DlpScanAndLabelThread", kwargs={"thread_id": "thread_004", "label_if_found": "dlp-flag", "changed_ts": "2024-08-24T18:50:00Z"}),
            Action(name="GetReleaseDiffSummary", kwargs={"release_id": "release_002"}),
            Action(name="ReadSystemConfig", kwargs={"config_key": "dlp_config"}),
            Action(name="ReadSystemConfig", kwargs={"config_key": "design_system_mappings"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="EXP_3",
        instruction="As the review-to-approval provenance steward, ensure that Gmail↔Figma signals remain consistent without detailing specific steps. Provide an audit-ready verification (focusing on facts rather than procedures) that confirms: thread_006 contains two directives—a message from pm.lead@company.com at 2024-08-24T18:05:00Z with content 'Approve pricing grid.' and a message from qa.lead@company.com at 2024-08-24T18:10:00Z stating 'Revise discount footnote.'—both having verified DLP statuses; the design_system_mappings policy served for terminology consistency; art_002 indicates a database state alteration where tag approved-for-release is active starting from 2024-08-24T18:16:00Z; the assets list for art_002 is displayed; and the final log 'Review intents captured and tag applied for art_002' is documented at 2024-08-24T18:17:00Z. Constants: artifact_id art_002; thread_id thread_006.",
        actions=[
            Action(name="AppendMessageToThread", kwargs={
                "thread_id": "thread_006",
                "from_email": "pm.lead@company.com",
                "body": "Approve pricing grid.",
                "created_ts": "2024-08-24T18:05:00Z"
            }),
            Action(name="AppendMessageToThread", kwargs={
                "thread_id": "thread_006",
                "from_email": "qa.lead@company.com",
                "body": "Revise discount footnote.",
                "created_ts": "2024-08-24T18:10:00Z"
            }),
            Action(name="AddArtifactTag", kwargs={"artifact_id": "art_002", "tag": "approved-for-release", "changed_ts": "2024-08-24T18:16:00Z"}),
            Action(name="ListAssetsForArtifact", kwargs={"artifact_id": "art_002"}),
            Action(name="ReadSystemConfig", kwargs={"config_key": "design_system_mappings"}),
            Action(name="DlpScanThread", kwargs={"thread_id": "thread_006"}),
            Action(name="LogTerminalEvent", kwargs={"log_ts": "2024-08-24T18:17:00Z", "message": "Review intents captured and tag applied for art_002"})
        ],
        outputs=[]
    ),

    # complexity_edges: 16
    Task(
        annotator="0",
        user_id="EXP_4",
        instruction="Oversee visibility tagging, ensure release communications abide by compliance, and confirm brand guidance verification. Implement a temporary visibility tag cycle on art_001 by using the tag handoff-ready with an initiation timestamp of 2024-08-23T10:10:00Z and a removal timestamp of 2024-08-23T10:40:00Z. Draft the release_001 announcement in thread_006 from emma.creative@company.com on 2024-08-22T17:00:00Z with subject 'Release 1.2.0 Announcement' and content 'Highlights and changes included.', ensuring attachment policy compliance under message_id relmsg_9cc87e81. Record a brand note on art_003 created by sophie.marketing@company.com located at node-2:7 on 2024-08-23T12:00:00Z stating 'Please update the brand color token to Brand/Primary/600.', then compile the author's comment history on art_003 since 2024-08-01T00:00:00Z.",
        actions=[
            Action(name="AddArtifactTag", kwargs={"artifact_id": "art_001", "tag": "handoff-ready", "changed_ts": "2024-08-23T10:10:00Z"}),
            Action(name="RemoveArtifactTag", kwargs={"artifact_id": "art_001", "tag": "handoff-ready", "changed_ts": "2024-08-23T10:40:00Z"}),
            Action(name="ComposeReleaseEmailDraft", kwargs={"release_id": "release_001", "thread_id": "thread_006", "from_email": "emma.creative@company.com", "created_ts": "2024-08-22T17:00:00Z", "subject": "Release 1.2.0 Announcement", "body": "Highlights and changes included."}),
            Action(name="GuardAttachmentPolicyOnDraft", kwargs={"message_id": "relmsg_9cc87e81"}),
            Action(name="CreateFigmaComment", kwargs={"artifact_id": "art_003", "author_email": "sophie.marketing@company.com", "body": "Please update the brand color token to Brand/Primary/600.", "anchor_ref": "node-2:7", "created_ts": "2024-08-23T12:00:00Z"}),
            Action(name="ListFigmaComments", kwargs={"artifact_id": "art_003", "author_email": "sophie.marketing@company.com", "since_ts": "2024-08-01T00:00:00Z"})
        ],
        outputs=[]
    ),


    # complexity_edges: 18
    Task(
        annotator="0",
        user_id="EXP_5",
        instruction="Handle compliance-aware escalation through email and design review with brand guidance tracking. Aim for the deterministic state where: thread_002 includes a memo from emma.creative@company.com at 2024-08-23T11:00:00Z with body 'Please note: temporary password is abcd-1234; rotate after testing.' and carries DLP posture marked as dlp-flag with changed_ts 2024-08-23T11:05:00Z if sensitive content is detected; art_004 has a review tagged as cycle_1dc59e3f connected to thread_003 and showing interim status NEEDS_REVIEW at 2024-08-23T13:20:00Z with a creation timestamp of 2024-08-23T13:00:00Z and linkage timestamp 2024-08-23T13:05:00Z; brand direction is documented on art_003 from sophie.marketing@company.com anchored at node-2:7 at 2024-08-23T12:00:00Z with text 'Please update the brand color token to Brand/Primary/600.'; provide the author-filtered comment history for art_003 limited to sophie.marketing@company.com since 2024-08-01T00:00:00Z.",
        actions=[
            Action(name="AppendMessageToThread", kwargs={"thread_id": "thread_002", "from_email": "emma.creative@company.com", "body": "Please note: temporary password is abcd-1234; rotate after testing.", "created_ts": "2024-08-23T11:00:00Z"}),
            Action(name="DlpScanAndLabelThread", kwargs={"thread_id": "thread_002", "label_if_found": "dlp-flag", "changed_ts": "2024-08-23T11:05:00Z"}),
            Action(name="StartReviewCycle", kwargs={"artifact_id": "art_004", "created_ts": "2024-08-23T13:00:00Z"}),
            Action(name="LinkReviewToThread", kwargs={"cycle_id": "cycle_1dc59e3f", "thread_id": "thread_003", "changed_ts": "2024-08-23T13:05:00Z"}),
            Action(name="AdvanceReviewStatus", kwargs={"cycle_id": "cycle_1dc59e3f", "new_status": "NEEDS_REVIEW", "changed_ts": "2024-08-23T13:20:00Z"}),
            Action(name="CreateFigmaComment", kwargs={"artifact_id": "art_003", "author_email": "sophie.marketing@company.com", "body": "Please update the brand color token to Brand/Primary/600.", "anchor_ref": "node-2:7", "created_ts": "2024-08-23T12:00:00Z"}),
            Action(name="ListFigmaComments", kwargs={"artifact_id": "art_003", "author_email": "sophie.marketing@company.com", "since_ts": "2024-08-01T00:00:00Z"})
        ],
        outputs=[]
    ),


    # complexity_edges: 17
    Task(
        annotator="0",
        user_id="EXP_6",
        instruction="Act as the review-provenance steward to ensure Figma-Gmail intent alignment for release readiness and brand guidance. Generate an audit-ready record (facts, not procedures) confirming: a review cycle cycle_1dc59e3f for art_004 originated at 2024-08-23T13:00:00Z and linked to thread_003 effective 2024-08-23T13:05:00Z; thread_003 holds two explicit signals—qa.lead@company.com “this needs changes” at 2024-08-23T13:12:00Z and build.bot@company.com “blocker: build failing” at 2024-08-23T13:14:00Z—and these intents are reflected in cycle_1dc59e3f; a release_001 announcement draft in thread_006 from emma.creative@company.com created at 2024-08-22T17:00:00Z with subject “Release 1.2.0 Announcement” and body “Highlights and changes included.” confirmed via message_id relmsg_9cc87e81 under attachment policy; and brand guidance on art_003 documented as a Figma note anchored node-2:7 by sophie.marketing@company.com at 2024-08-23T12:00:00Z stating “Please update the brand color token to Brand/Primary/600.” Produce the author-scoped comment history for art_003 filtered to sophie.marketing@company.com since 2024-08-01T00:00:00Z.",
        actions=[
            Action(name="StartReviewCycle", kwargs={"artifact_id": "art_004", "created_ts": "2024-08-23T13:00:00Z"}),
            Action(name="LinkReviewToThread", kwargs={"cycle_id": "cycle_1dc59e3f", "thread_id": "thread_003", "changed_ts": "2024-08-23T13:05:00Z"}),
            Action(name="AppendMessageToThread", kwargs={"thread_id": "thread_003", "from_email": "qa.lead@company.com", "body": "this needs changes", "created_ts": "2024-08-23T13:12:00Z"}),
            Action(name="AppendMessageToThread", kwargs={"thread_id": "thread_003", "from_email": "build.bot@company.com", "body": "blocker: build failing", "created_ts": "2024-08-23T13:14:00Z"}),
            Action(name="SyncGmailIntentsToReview", kwargs={"cycle_id": "cycle_1dc59e3f", "thread_id": "thread_003"}),
            Action(name="ComposeReleaseEmailDraft", kwargs={"release_id": "release_001", "thread_id": "thread_006", "from_email": "emma.creative@company.com", "created_ts": "2024-08-22T17:00:00Z", "subject": "Release 1.2.0 Announcement", "body": "Highlights and changes included."}),
            Action(name="GuardAttachmentPolicyOnDraft", kwargs={"message_id": "relmsg_9cc87e81"}),
            Action(name="CreateFigmaComment", kwargs={"artifact_id": "art_003", "author_email": "sophie.marketing@company.com", "body": "Please update the brand color token to Brand/Primary/600.", "anchor_ref": "node-2:7", "created_ts": "2024-08-23T12:00:00Z"}),
            Action(name="ListFigmaComments", kwargs={"artifact_id": "art_003", "author_email": "sophie.marketing@company.com", "since_ts": "2024-08-01T00:00:00Z"})
        ],
        outputs=[]
    ),


    # complexity_edges: 19
    Task(
        annotator="0",
        user_id="EXP_7",
        instruction="You handle the entire process, spanning from reviewing progression to acquiring approvals, ensuring compliance labeling, distributing release communications, and following brand guidance. The target state must specifically encompass: art_004 review (cycle_1dc59e3f) linked to thread_003, initiated at 2024-08-23T13:00:00Z with linkage at 2024-08-23T13:05:00Z, reflecting an interim status of NEEDS_REVIEW at 2024-08-23T13:20:00Z, and a conclusive decision of APPROVED by chris.engineer@company.com at 2024-08-23T13:25:00Z with the comment 'LGTM'; thread_002 features 'temporary password abcd-1234 for staging' from devops@company.com at 2024-08-23T11:15:00Z and exhibits DLP posture by labeling dlp-flag at changed_ts 2024-08-23T11:16:00Z when sensitive content arises; a draft for release_001 announcement can be found in thread_006 from emma.creative@company.com created at 2024-08-22T17:00:00Z with the subject 'Release 1.2.0 Announcement' and body 'Highlights and changes included.' verified through message_id relmsg_9cc87e81; brand direction is illustrated on art_003 from sophie.marketing@company.com situated at node-2:7 at 2024-08-23T12:00:00Z, stating 'Please update the brand color token to Brand/Primary/600.'; the output is the filtered comment history for art_003 limited to sophie.marketing@company.com since 2024-08-01T00:00:00Z.",
        actions=[
            Action(name="StartReviewCycle", kwargs={"artifact_id": "art_004", "created_ts": "2024-08-23T13:00:00Z"}),
            Action(name="LinkReviewToThread", kwargs={"cycle_id": "cycle_1dc59e3f", "thread_id": "thread_003", "changed_ts": "2024-08-23T13:05:00Z"}),
            Action(name="AdvanceReviewStatus", kwargs={"cycle_id": "cycle_1dc59e3f", "new_status": "NEEDS_REVIEW", "changed_ts": "2024-08-23T13:20:00Z"}),
            Action(name="RecordReviewApproval", kwargs={"cycle_id": "cycle_1dc59e3f", "approver_email": "chris.engineer@company.com", "decision": "APPROVED", "decided_ts": "2024-08-23T13:25:00Z", "comment": "LGTM"}),
            Action(name="AppendMessageToThread", kwargs={"thread_id": "thread_002", "from_email": "devops@company.com", "body": "temporary password abcd-1234 for staging", "created_ts": "2024-08-23T11:15:00Z"}),
            Action(name="DlpScanAndLabelThread", kwargs={"thread_id": "thread_002", "label_if_found": "dlp-flag", "changed_ts": "2024-08-23T11:16:00Z"}),
            Action(name="ComposeReleaseEmailDraft", kwargs={"release_id": "release_001", "thread_id": "thread_006", "from_email": "emma.creative@company.com", "created_ts": "2024-08-22T17:00:00Z", "subject": "Release 1.2.0 Announcement", "body": "Highlights and changes included."}),
            Action(name="GuardAttachmentPolicyOnDraft", kwargs={"message_id": "relmsg_9cc87e81"}),
            Action(name="CreateFigmaComment", kwargs={"artifact_id": "art_003", "author_email": "sophie.marketing@company.com", "body": "Please update the brand color token to Brand/Primary/600.", "anchor_ref": "node-2:7", "created_ts": "2024-08-23T12:00:00Z"}),
            Action(name="ListFigmaComments", kwargs={"artifact_id": "art_003", "author_email": "sophie.marketing@company.com", "since_ts": "2024-08-01T00:00:00Z"})
        ],
        outputs=[]
    ),


    # complexity_edges: 19
    Task(
        annotator="0",
        user_id="EXP_8",
        instruction="You coordinate an integrated release communication featuring attachment and DLP guardrails, followed by providing a consistent asset reference. Manage operations within the release/ lineage utilizing release_001 as the definitive difference. The announcement is prepared as a draft in thread_006 from emma.creative@company.com at 2024-08-22T17:00:00Z with the subject “Release 1.2.0 Announcement” and a body of “Highlights and changes included.” The draft message relmsg_9cc87e81 adheres to the attachment policy; conversation status mirrors Design/Release and was announced with the draft removed at 2024-08-22T17:06:00Z; a final note “APPROVE rollout.” from emma.creative@company.com is captured at 2024-08-22T17:07:00Z; DLP posture is confirmed on the same thread. Provide the exported assets for art_001.",
        actions=[
            Action(name="ListReleases", kwargs={"version_prefix": "release/"}),
            Action(name="GetReleaseDiffSummary", kwargs={"release_id": "release_001"}),
            Action(name="ComposeReleaseEmailDraft", kwargs={"release_id": "release_001", "thread_id": "thread_006", "from_email": "emma.creative@company.com", "created_ts": "2024-08-22T17:00:00Z", "subject": "Release 1.2.0 Announcement", "body": "Highlights and changes included."}),
            Action(name="GuardAttachmentPolicyOnDraft", kwargs={"message_id": "relmsg_9cc87e81"}),
            Action(name="UpdateThreadLabels", kwargs={"thread_id": "thread_006", "add_labels": ["Design/Release", "announced"], "remove_labels": ["draft"], "changed_ts": "2024-08-22T17:06:00Z"}),
            Action(name="AppendMessageToThread", kwargs={"thread_id": "thread_006", "from_email": "emma.creative@company.com", "body": "APPROVE rollout.", "created_ts": "2024-08-22T17:07:00Z"}),
            Action(name="DlpScanThread", kwargs={"thread_id": "thread_006"}),
            Action(name="ListAssetsForArtifact", kwargs={"artifact_id": "art_001"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="EXP_9",
        instruction="Act as the brand-governance custodian ensuring Gmail↔Figma signal consistency and audit-ready authorship for art_012. Compile an audit-ready record indicating: governance references intent_keywords and dlp_config were reviewed; a definitive brand note by sophie.marketing@company.com at 2024-08-24T13:00:00Z affixed node-12:1 with exact wording 'Align tokens with brand v3.'; a supplementary QA note by brand.qa@company.com at 2024-08-24T13:05:00Z affixed node-12:2 with precise wording 'Verify logo safe-area usage.'; and a final DB-visible change at 2024-08-24T13:10:00Z documenting 'Brand page comments added.' Present the author-specific comment view for art_012 restricted to sophie.marketing@company.com beginning 2024-08-01T00:00:00Z.",
        actions=[
            Action(name="ReadSystemConfig", kwargs={"config_key": "intent_keywords"}),
            Action(name="ReadSystemConfig", kwargs={"config_key": "dlp_config"}),
            Action(name="CreateFigmaComment", kwargs={
                "artifact_id": "art_012",
                "author_email": "sophie.marketing@company.com",
                "body": "Align tokens with brand v3.",
                "anchor_ref": "node-12:1",
                "created_ts": "2024-08-24T13:00:00Z"
            }),
            Action(name="CreateFigmaComment", kwargs={
                "artifact_id": "art_012",
                "author_email": "brand.qa@company.com",
                "body": "Verify logo safe-area usage.",
                "anchor_ref": "node-12:2",
                "created_ts": "2024-08-24T13:05:00Z"
            }),
            Action(name="LogTerminalEvent", kwargs={
                "log_ts": "2024-08-24T13:10:00Z",
                "message": "Brand page comments added"
            }),
            Action(name="ListFigmaComments", kwargs={
                "artifact_id": "art_012",
                "author_email": "sophie.marketing@company.com",
                "since_ts": "2024-08-01T00:00:00Z"
            })
        ],
        outputs=[]
    ),

    # complexity_edges: 21
    Task(
        annotator="0",
        user_id="EXP_10",
        instruction="Serve as the landing-page review coordination expert responsible for posture alignment, DLP-clean communication standards, and handoff readiness. Target the art_001 landing-page frame managed by emma.creative@company.com (artifact type FRAME, tag landing-page, updated on/after 2024-08-01T00:00:00Z) with email context in thread_001. The finalized state must adhere to all of the following conditions: (1) art_001 possesses review posture needs-review with an effective time of 2024-08-24T09:45:00Z; (2) the review record reflects a single ongoing review instance for art_001 with status IN_FLIGHT created at 2024-08-24T09:46:00Z; (3) thread_001 documents an initiation by emma.creative@company.com at 2024-08-24T09:47:00Z with text “Please REVIEW design; awaiting APPROVE or CHANGES.”; (4) as of 2024-08-24T09:48:00Z the thread's label posture includes Design/Needs-Review and triaged and excludes dlp-flag; (5) DLP validation exists for thread_001; (6) supply the exported asset list for art_001.",
        actions=[
            Action(name="ListArtifacts", kwargs={"owner_email": "emma.creative@company.com", "tag": "landing-page", "artifact_type": "FRAME", "modified_since": "2024-08-01T00:00:00Z"}),
            Action(name="AddArtifactTag", kwargs={"artifact_id": "art_001", "tag": "needs-review", "changed_ts": "2024-08-24T09:45:00Z"}),
            Action(name="StartReviewCycle", kwargs={"artifact_id": "art_001", "created_ts": "2024-08-24T09:46:00Z", "status": "IN_FLIGHT"}),
            Action(name="AppendMessageToThread", kwargs={"thread_id": "thread_001", "from_email": "emma.creative@company.com", "body": "Please REVIEW design; awaiting APPROVE or CHANGES.", "created_ts": "2024-08-24T09:47:00Z"}),
            Action(name="UpdateThreadLabels", kwargs={"thread_id": "thread_001", "add_labels": ["Design/Needs-Review", "triaged"], "remove_labels": ["dlp-flag"], "changed_ts": "2024-08-24T09:48:00Z"}),
            Action(name="DlpScanThread", kwargs={"thread_id": "thread_001"}),
            Action(name="ListAssetsForArtifact", kwargs={"artifact_id": "art_001"}),
        ],
        outputs=[]
    ),


    # complexity_edges: 23
    Task(
        annotator="0",
        user_id="EXP_11",
        instruction="You are responsible for the ongoing design-review triage, ensuring mail↔artifact signal consistency under DLP policy. Concentrate on the discussion that matches label design-review, involving participant chris.engineer@company.com, keyword 'Design'. The validated state includes: thread_001 with labels triaged, figma-sync, Design/Needs-Review, excluding urgent (effective 2024-08-24T12:00:00Z); the conversation log features a reviewer response by chris.engineer@company.com at 2024-08-24T12:05:00Z with the precise content 'CHANGES: Please adjust spacing.' and a confirmed DLP status; and the artifact counterpart mirrors triage with art_001 labeled triaged effective 2024-08-24T12:10:00Z, plus a design note at node-1:2 by chris.engineer@company.com at 2024-08-24T12:11:00Z stating 'CHANGES requested noted.' Provide the exported assets for art_001.",
        actions=[
            Action(name="SearchGmailThreads", kwargs={"label": "design-review", "participant": "chris.engineer@company.com", "keyword": "Design"}),
            Action(name="UpdateThreadLabels", kwargs={"thread_id": "thread_001", "add_labels": ["triaged", "figma-sync", "Design/Needs-Review"], "remove_labels": ["urgent"], "changed_ts": "2024-08-24T12:00:00Z"}),
            Action(name="AppendMessageToThread", kwargs={"thread_id": "thread_001", "from_email": "chris.engineer@company.com", "body": "CHANGES: Please adjust spacing.", "created_ts": "2024-08-24T12:05:00Z"}),
            Action(name="DlpScanThread", kwargs={"thread_id": "thread_001"}),
            Action(name="AddArtifactTag", kwargs={"artifact_id": "art_001", "tag": "triaged", "changed_ts": "2024-08-24T12:10:00Z"}),
            Action(name="CreateFigmaComment", kwargs={"artifact_id": "art_001", "author_email": "chris.engineer@company.com", "body": "CHANGES requested noted.", "anchor_ref": "node-1:2", "created_ts": "2024-08-24T12:11:00Z"}),
            Action(name="ListAssetsForArtifact", kwargs={"artifact_id": "art_001"}),
        ],
        outputs=[]
    ),

    # complexity_edges: 21
    Task(
        annotator="0",
        user_id="EXP_12",
        instruction="You have the role of pricing-modification triage steward ensuring signal alignment and discoverability within the Figma↔Gmail workflow. Produce an audit-ready documentation (facts, not procedures) confirming: art_007 's review initiated at 2024-08-23T12:00:00Z under cycle_38980610 and linked to thread_008 effective 2024-08-24T19:05:00Z; the Gmail thread contains a blocker message by qa.lead@company.com at 2024-08-24T19:06:00Z with the text 'BLOCKER: consent modal failing on Safari' and confirmed DLP status; synchronized intents are maintained; the review database state shows updates—status ESCALATED at 2024-08-24T19:07:00Z and the decision CHANGES_REQUESTED by chris.engineer@company.com at 2024-08-24T19:10:00Z with the remark 'Address Safari issue'; and the thread can be found using keyword 'Pricing'. Provide the surfaced conversation metadata.",
        actions=[
            Action(name="StartReviewCycle", kwargs={"artifact_id": "art_007", "created_ts": "2024-08-23T12:00:00Z"}),
            Action(name="LinkReviewToThread", kwargs={"cycle_id": "cycle_38980610", "thread_id": "thread_008", "changed_ts": "2024-08-24T19:05:00Z"}),
            Action(name="AppendMessageToThread", kwargs={"thread_id": "thread_008", "from_email": "qa.lead@company.com", "body": "BLOCKER: consent modal failing on Safari", "created_ts": "2024-08-24T19:06:00Z"}),
            Action(name="SyncGmailIntentsToReview", kwargs={"cycle_id": "cycle_38980610", "thread_id": "thread_008"}),
            Action(name="AdvanceReviewStatus", kwargs={"cycle_id": "cycle_38980610", "new_status": "ESCALATED", "changed_ts": "2024-08-24T19:07:00Z"}),
            Action(name="RecordReviewApproval", kwargs={"cycle_id": "cycle_38980610", "approver_email": "chris.engineer@company.com", "decision": "CHANGES_REQUESTED", "decided_ts": "2024-08-24T19:10:00Z", "comment": "Address Safari issue"}),
            Action(name="DlpScanThread", kwargs={"thread_id": "thread_008"}),
            Action(name="SearchGmailThreads", kwargs={"keyword": "Pricing"}),
        ],
        outputs=[]
    ),

    # complexity_edges: 15
    Task(
        annotator="0",
        user_id="EXP_13",
        instruction="Handle the closure of navigation updates while ensuring a clear decision-making process and maintaining email safety. Your audit-ready results must clearly show: on cycle_1dc59e3f a decision of APPROVED made by design.lead@company.com on 2024-08-25T18:20:00Z, with the comment 'Ship after QA signoff.'; a mail status on thread_003 where Design/Approved and triaged are noted and needs-review and dlp-flag are absent as of 2024-08-25T18:25:00Z; and a brief closure note by design.lead@company.com at 2024-08-25T18:26:00Z with content 'Approved pending QA.'. Provide the confirmed DLP safety outcome for thread_003 (no blocked terms expected).",
        actions=[
            Action(name="RecordReviewApproval", kwargs={
                "cycle_id": "cycle_1dc59e3f",
                "approver_email": "design.lead@company.com",
                "decision": "APPROVED",
                "decided_ts": "2024-08-25T18:20:00Z",
                "comment": "Ship after QA signoff."
            }),
            Action(name="UpdateThreadLabels", kwargs={
                "thread_id": "thread_003",
                "add_labels": ["Design/Approved", "triaged"],
                "remove_labels": ["needs-review", "dlp-flag"],
                "changed_ts": "2024-08-25T18:25:00Z"
            }),
            Action(name="AppendMessageToThread", kwargs={
                "thread_id": "thread_003",
                "from_email": "design.lead@company.com",
                "body": "Approved pending QA.",
                "created_ts": "2024-08-25T18:26:00Z"
            }),
            Action(name="DlpScanThread", kwargs={"thread_id": "thread_003"}),
        ],
        outputs=[]
    ),

    # complexity_edges: 17
    Task(
        annotator="0",
        user_id="EXP_14",
        instruction="Coordinate the maintenance of needs-review provenance, ensuring Figma and Gmail signals are aligned and maintaining label cleanliness (database modifications must be traceable) within DLP guidelines. Produce an audit-ready snapshot with factual details covering: scope filter owner emma.creative@company.com, tag landing-page, artifact type FRAME, modified_since 2024-08-01T00:00:00Z; art_001 displays tag needs-review as of 2024-08-24T09:45:00Z; a review for art_001 initiated on 2024-08-24T09:46:00Z with the status IN_FLIGHT; thread_001 includes a kickoff note by emma.creative@company.com at 2024-08-24T09:47:00Z stating “Please REVIEW design; awaiting APPROVE or CHANGES.”; thread_001's label status shows Design/Needs-Review and triaged present and dlp-flag absent as of 2024-08-24T09:48:00Z with confirmation from a DLP scan on mail safety. Output the exported assets for art_001.",
        actions=[
            Action(name="ListArtifacts", kwargs={
                "owner_email": "emma.creative@company.com",
                "tag": "landing-page",
                "artifact_type": "FRAME",
                "modified_since": "2024-08-01T00:00:00Z"
            }),
            Action(name="AddArtifactTag", kwargs={
                "artifact_id": "art_001",
                "tag": "needs-review",
                "changed_ts": "2024-08-24T09:45:00Z"
            }),
            Action(name="StartReviewCycle", kwargs={
                "artifact_id": "art_001",
                "created_ts": "2024-08-24T09:46:00Z",
                "status": "IN_FLIGHT"
            }),
            Action(name="AppendMessageToThread", kwargs={
                "thread_id": "thread_001",
                "from_email": "emma.creative@company.com",
                "body": "Please REVIEW design; awaiting APPROVE or CHANGES.",
                "created_ts": "2024-08-24T09:47:00Z"
            }),
            Action(name="UpdateThreadLabels", kwargs={
                "thread_id": "thread_001",
                "add_labels": ["Design/Needs-Review", "triaged"],
                "remove_labels": ["dlp-flag"],
                "changed_ts": "2024-08-24T09:48:00Z"
            }),
            Action(name="DlpScanThread", kwargs={"thread_id": "thread_001"}),
            Action(name="ListAssetsForArtifact", kwargs={"artifact_id": "art_001"}),
        ],
        outputs=[]
    ),

    # complexity_edges: 19
    Task(
        annotator="0",
        user_id="EXP_15",
        instruction="Act as the release-communications handler ensuring Figma↔Gmail signal alignment, compliant labeling, and preserved design lineage. Provide an audit-ready record (facts only, no procedures) verifying: releases under version prefix 'release/' including the diff for release_001; a single announcement draft by emma.creative@company.com captured at 2024-08-22T17:00:00Z in thread_006 with the subject 'Release 1.2.0 Announcement' and body 'Highlights and changes included.' identified as relmsg_9cc87e81 and compliant with attachments; a DB-visible thread_006 posture where Design/Release and announced are present but draft is absent effective 2024-08-22T17:06:00Z; a closing confirmation by emma.creative@company.com at 2024-08-22T17:07:00Z stating 'APPROVE rollout.'; and DLP safety verification documented for thread_006. Include the exported asset list linked to art_001.",
        actions=[
            Action(name="ListReleases", kwargs={"version_prefix": "release/"}),
            Action(name="GetReleaseDiffSummary", kwargs={"release_id": "release_001"}),
            Action(name="ComposeReleaseEmailDraft", kwargs={
                "release_id": "release_001",
                "thread_id": "thread_006",
                "from_email": "emma.creative@company.com",
                "created_ts": "2024-08-22T17:00:00Z",
                "subject": "Release 1.2.0 Announcement",
                "body": "Highlights and changes included."
            }),
            Action(name="GuardAttachmentPolicyOnDraft", kwargs={"message_id": "relmsg_9cc87e81"}),
            Action(name="UpdateThreadLabels", kwargs={
                "thread_id": "thread_006",
                "add_labels": ["Design/Release", "announced"],
                "remove_labels": ["draft"],
                "changed_ts": "2024-08-22T17:06:00Z"
            }),
            Action(name="AppendMessageToThread", kwargs={
                "thread_id": "thread_006",
                "from_email": "emma.creative@company.com",
                "body": "APPROVE rollout.",
                "created_ts": "2024-08-22T17:07:00Z"
            }),
            Action(name="DlpScanThread", kwargs={"thread_id": "thread_006"}),
            Action(name="ListAssetsForArtifact", kwargs={"artifact_id": "art_001"}),
        ],
        outputs=[]
    ),

    # complexity_edges: 20
    Task(
        annotator="0",
        user_id="EXP_16",
        instruction="Serve as the accessibility-readiness and DLP-assurance coordinator for the admin header. Work within the admin dashboard frame scope (owned by chris.engineer@company.com, tag dashboard, FRAME, modified_since 2024-08-01T00:00:00Z). Create an audit-ready snapshot that documents, without detailing steps: art_008 in posture a11y-reviewed effective 2024-08-25T15:00:00Z; an outcomes note by chris.engineer@company.com anchored node-8:11 at 2024-08-25T15:05:00Z with the exact body 'A11y review completed: focus order and ARIA roles verified.'; and origin mail thread_004 containing a verification note from chris.engineer@company.com at 2024-08-25T15:10:00Z with the exact text 'Including test ssn 000-12-3456 for DLP verification only.' The safety posture is indicated by a single evaluation captured at 2024-08-25T15:12:00Z and governed by dlp_config; the record indicates the detection and the policy label dlp-flag applied.",
        actions=[
            Action(name="ListArtifacts", kwargs={"owner_email": "chris.engineer@company.com", "tag": "dashboard", "artifact_type": "FRAME", "modified_since": "2024-08-01T00:00:00Z"}),
            Action(name="AddArtifactTag", kwargs={"artifact_id": "art_008", "tag": "a11y-reviewed", "changed_ts": "2024-08-25T15:00:00Z"}),
            Action(name="CreateFigmaComment", kwargs={"artifact_id": "art_008", "author_email": "chris.engineer@company.com", "body": "A11y review completed: focus order and ARIA roles verified.", "anchor_ref": "node-8:11", "created_ts": "2024-08-25T15:05:00Z"}),
            Action(name="AppendMessageToThread", kwargs={"thread_id": "thread_004", "from_email": "chris.engineer@company.com", "body": "Including test ssn 000-12-3456 for DLP verification only.", "created_ts": "2024-08-25T15:10:00Z"}),
            Action(name="ReadSystemConfig", kwargs={"config_key": "dlp_config"}),
            Action(name="DlpScanAndLabelThread", kwargs={"thread_id": "thread_004", "label_if_found": "dlp-flag", "changed_ts": "2024-08-25T15:12:00Z"})
        ],
        outputs=[]
    ),

    # complexity_edges: 18
    Task(
        annotator="0",
        user_id="EXP_17",
        instruction="Oversee mobile release communications by coordinating the alignment of Figma assets and Gmail stance. Compile an audit-ready document (facts only, not methods) establishing: the release catalog defined by version_prefix release/ and artifact_id None as the primary index; a quantified difference for release_012; a deterministic draft on thread_014 created by jake.design@company.com at 2024-08-25T16:00:00Z with subject 'Mobile App v2.2.0 - Release Notes' and body 'Changelog and enhancements for Settings & Profile.'; compliance with attachment policy for message_id relmsg_b607ec35; a label posture with release-draft and triaged present as of 2024-08-25T16:05:00Z; acceptance by qa.lead@company.com at 2024-08-25T16:06:00Z with the precise text 'ACK: No blocking issues in QA.'; and a DLP safety confirmation indicating no issues on thread_014.",
        actions=[
            Action(name="ListReleases", kwargs={"version_prefix": "release/", "artifact_id": None}),
            Action(name="GetReleaseDiffSummary", kwargs={"release_id": "release_012"}),
            Action(name="ComposeReleaseEmailDraft", kwargs={"release_id": "release_012", "thread_id": "thread_014", "from_email": "jake.design@company.com", "created_ts": "2024-08-25T16:00:00Z", "subject": "Mobile App v2.2.0 - Release Notes", "body": "Changelog and enhancements for Settings & Profile."}),
            Action(name="GuardAttachmentPolicyOnDraft", kwargs={"message_id": "relmsg_b607ec35"}),
            Action(name="UpdateThreadLabels", kwargs={"thread_id": "thread_014", "add_labels": ["release-draft", "triaged"], "remove_labels": [], "changed_ts": "2024-08-25T16:05:00Z"}),
            Action(name="AppendMessageToThread", kwargs={"thread_id": "thread_014", "from_email": "qa.lead@company.com", "body": "ACK: No blocking issues in QA.", "created_ts": "2024-08-25T16:06:00Z"}),
            Action(name="DlpScanThread", kwargs={"thread_id": "thread_014"})
        ],
        outputs=[]
    ),

    # complexity_edges: 20
    Task(
        annotator="0",
        user_id="EXP_18",
        instruction="Manage the release-provenance for the 1.2.0 web rollout, ensuring Figma↔Gmail cleanliness. Compile an audit-ready document (facts only, not methods) confirming: lineage under release/ with the primary difference for release_001; a deterministic announcement draft for release_001 in thread_006 composed by emma.creative@company.com at 2024-08-22T17:00:00Z with subject 'Release 1.2.0 Announcement' and body 'Highlights and changes included.' validated through message_id relmsg_9cc87e81 and conforming to attachment-policy standards; a label posture where Design/Release and final are included and draft is excluded effective 2024-08-22T17:06:00Z; a closing note from emma.creative@company.com at 2024-08-22T17:07:30Z stating 'APPROVED for rollout.'; a DLP safety confirmation for thread_006; and the exported assets listing for art_001 as the stable handoff reference.",
        actions=[
            Action(name="ListReleases", kwargs={"version_prefix": "release/"}),
            Action(name="GetReleaseDiffSummary", kwargs={"release_id": "release_001"}),
            Action(name="ComposeReleaseEmailDraft", kwargs={
                "release_id": "release_001",
                "thread_id": "thread_006",
                "from_email": "emma.creative@company.com",
                "created_ts": "2024-08-22T17:00:00Z",
                "subject": "Release 1.2.0 Announcement",
                "body": "Highlights and changes included."
            }),
            Action(name="GuardAttachmentPolicyOnDraft", kwargs={"message_id": "relmsg_9cc87e81"}),
            Action(name="UpdateThreadLabels", kwargs={
                "thread_id": "thread_006",
                "add_labels": ["Design/Release", "final"],
                "remove_labels": ["draft"],
                "changed_ts": "2024-08-22T17:06:00Z"
            }),
            Action(name="AppendMessageToThread", kwargs={
                "thread_id": "thread_006",
                "from_email": "emma.creative@company.com",
                "body": "APPROVED for rollout.",
                "created_ts": "2024-08-22T17:07:30Z"
            }),
            Action(name="DlpScanThread", kwargs={"thread_id": "thread_006"}),
            Action(name="ListAssetsForArtifact", kwargs={"artifact_id": "art_001"})
        ],
        outputs=[]
    ),

    # complexity_edges: 20
    Task(
        annotator="0",
        user_id="EXP_19",
        instruction="As the a11y readiness steward, oversee the enforcement of DLP guardrails throughout the Figma↔Gmail surface. Create an audit-ready snapshot, without outlining steps, illustrating: the scope includes FRAME artifacts labeled dashboard, belonging to chris.engineer@company.com, and altered on or after 2024-08-01T00:00:00Z; art_008 in the status a11y-reviewed, effective 2024-08-25T15:00:00Z; a comment from chris.engineer@company.com linked to node-8:11 at 2024-08-25T15:05:00Z containing the text 'A11y review completed: focus order and ARIA roles verified.'; source email thread_004 having a verification note from chris.engineer@company.com at 2024-08-25T15:10:00Z with the literal text 'Including password for DLP verification only.'; and a solitary DLP evaluation occurring at 2024-08-25T15:12:00Z, guided by dlp_config, that definitively logs the blocked token 'password' and enacts the policy label dlp-flag.",
        actions=[
            Action(name="ListArtifacts", kwargs={
                "owner_email": "chris.engineer@company.com",
                "tag": "dashboard",
                "artifact_type": "FRAME",
                "modified_since": "2024-08-01T00:00:00Z"
            }),
            Action(name="AddArtifactTag", kwargs={
                "artifact_id": "art_008",
                "tag": "a11y-reviewed",
                "changed_ts": "2024-08-25T15:00:00Z"
            }),
            Action(name="CreateFigmaComment", kwargs={
                "artifact_id": "art_008",
                "author_email": "chris.engineer@company.com",
                "body": "A11y review completed: focus order and ARIA roles verified.",
                "anchor_ref": "node-8:11",
                "created_ts": "2024-08-25T15:05:00Z"
            }),
            Action(name="AppendMessageToThread", kwargs={
                "thread_id": "thread_004",
                "from_email": "chris.engineer@company.com",
                "body": "Including password for DLP verification only.",
                "created_ts": "2024-08-25T15:10:00Z"
            }),
            Action(name="ReadSystemConfig", kwargs={
                "config_key": "dlp_config"
            }),
            Action(name="DlpScanAndLabelThread", kwargs={
                "thread_id": "thread_004",
                "label_if_found": "dlp-flag",
                "changed_ts": "2024-08-25T15:12:00Z"
            })
        ],
        outputs=[]
    ),

    # complexity_edges: 14
    Task(
        annotator="0",
        user_id="EXP_20",
        instruction="Ensure a compliant release-ready condition while maintaining asset context within the Figma↔Gmail release workflow. The authoritative record must show: the preserved draft for release_001 in thread_006 by emma.creative@company.com at 2024-08-22T17:00:00Z with the subject 'Release 1.2.0 Announcement' and body 'Highlights and changes included.'; a QA approval from qa.lead@company.com at 2024-08-22T17:06:00Z with body 'QA sign-off complete'; validation of attachment-policy under message_id relmsg_9cc87e81; a conversation status where release-ready is active from 2024-08-22T17:10:00Z; and in an artifact-side trace where art_001 holds a temporary handoff-ready tag applied on 2024-08-23T10:10:00Z and removed on 2024-08-23T10:40:00Z. Supply the exported assets list for art_001 as the definitive reference.",
        actions=[
            Action(name="ComposeReleaseEmailDraft", kwargs={
                "release_id": "release_001",
                "thread_id": "thread_006",
                "from_email": "emma.creative@company.com",
                "created_ts": "2024-08-22T17:00:00Z",
                "subject": "Release 1.2.0 Announcement",
                "body": "Highlights and changes included."
            }),
            Action(name="AppendMessageToThread", kwargs={
                "thread_id": "thread_006",
                "from_email": "qa.lead@company.com",
                "body": "QA sign-off complete",
                "created_ts": "2024-08-22T17:06:00Z"
            }),
            Action(name="GuardAttachmentPolicyOnDraft", kwargs={"message_id": "relmsg_9cc87e81"}),
            Action(name="UpdateThreadLabels", kwargs={
                "thread_id": "thread_006",
                "add_labels": ["release-ready"],
                "remove_labels": [],
                "changed_ts": "2024-08-22T17:10:00Z"
            }),
            Action(name="AddArtifactTag", kwargs={
                "artifact_id": "art_001",
                "tag": "handoff-ready",
                "changed_ts": "2024-08-23T10:10:00Z"
            }),
            Action(name="RemoveArtifactTag", kwargs={
                "artifact_id": "art_001",
                "tag": "handoff-ready",
                "changed_ts": "2024-08-23T10:40:00Z"
            }),
            Action(name="ListAssetsForArtifact", kwargs={"artifact_id": "art_001"})
        ],
        outputs=[]
    ),

    # complexity_edges: 15
    Task(
        annotator="0",
        user_id="EXP_21",
        instruction="Handle the finalization of review provenance and document brand guidance with definitive evidence. The audit-ready snapshot must include: for art_004, a review created 2024-08-23T13:00:00Z (cycle_1dc59e3f), associated with thread_003 at 2024-08-23T13:05:00Z, transitioned to NEEDS_REVIEW at 2024-08-23T13:20:00Z, and concluded with an APPROVED decision by chris.engineer@company.com at 2024-08-23T13:25:00Z with comment 'LGTM'; and, separately, a brand note on art_003 by sophie.marketing@company.com anchored at node-2:7 on 2024-08-23T12:00:00Z with body 'Please update the brand color token to Brand/Primary/600.' The deliverable is the comment history for artifact_id art_003, scoped to author_email sophie.marketing@company.com, since 2024-08-01T00:00:00Z.",
        actions=[
            Action(name="StartReviewCycle", kwargs={"artifact_id": "art_004", "created_ts": "2024-08-23T13:00:00Z"}),
            Action(name="LinkReviewToThread", kwargs={
                "cycle_id": "cycle_1dc59e3f",
                "thread_id": "thread_003",
                "changed_ts": "2024-08-23T13:05:00Z"
            }),
            Action(name="AdvanceReviewStatus", kwargs={
                "cycle_id": "cycle_1dc59e3f",
                "new_status": "NEEDS_REVIEW",
                "changed_ts": "2024-08-23T13:20:00Z"
            }),
            Action(name="RecordReviewApproval", kwargs={
                "cycle_id": "cycle_1dc59e3f",
                "approver_email": "chris.engineer@company.com",
                "decision": "APPROVED",
                "decided_ts": "2024-08-23T13:25:00Z",
                "comment": "LGTM"
            }),
            Action(name="CreateFigmaComment", kwargs={
                "artifact_id": "art_003",
                "author_email": "sophie.marketing@company.com",
                "body": "Please update the brand color token to Brand/Primary/600.",
                "anchor_ref": "node-2:7",
                "created_ts": "2024-08-23T12:00:00Z"
            }),
            Action(name="ListFigmaComments", kwargs={
                "artifact_id": "art_003",
                "author_email": "sophie.marketing@company.com",
                "since_ts": "2024-08-01T00:00:00Z"
            })
        ],
        outputs=[]
    ),

    # complexity_edges: 14
    Task(
        annotator="0",
        user_id="EXP_22",
        instruction="Coordinate the compliant marketing approval and release stance across Gmail and Figma while initiating release governance without explicit steps. The audit-ready snapshot needs to include: source mail thread_003 with a sensitive note from anna.brand@company.com at 2024-08-23T09:00:00Z containing 'Temporary password is abcd-1234. Rotate after testing.' and a singular safety evaluation executing dlp-flag at 2024-08-23T09:05:00Z; additionally, a deterministic 1.4.0 announcement draft for Figma release_004 in thread_008 crafted by emma.creative@company.com at 2024-08-23T16:30:00Z with subject 'Release 1.4.0 Announcement' and body 'Changelog and new components included.' authenticated through Google message_id relmsg_f9e9c1b6, with a labeling position where release-draft exists as of 2024-08-23T16:35:00Z. The deliverable contains the set of threads tagged with label dlp-flag.",
        actions=[
            Action(name="AppendMessageToThread", kwargs={
                "thread_id": "thread_003",
                "from_email": "anna.brand@company.com",
                "body": "Temporary password is abcd-1234. Rotate after testing.",
                "created_ts": "2024-08-23T09:00:00Z"
            }),
            Action(name="DlpScanAndLabelThread", kwargs={
                "thread_id": "thread_003",
                "label_if_found": "dlp-flag",
                "changed_ts": "2024-08-23T09:05:00Z"
            }),
            Action(name="ComposeReleaseEmailDraft", kwargs={
                "release_id": "release_004",
                "thread_id": "thread_008",
                "from_email": "emma.creative@company.com",
                "created_ts": "2024-08-23T16:30:00Z",
                "subject": "Release 1.4.0 Announcement",
                "body": "Changelog and new components included."
            }),
            Action(name="GuardAttachmentPolicyOnDraft", kwargs={"message_id": "relmsg_f9e9c1b6"}),
            Action(name="UpdateThreadLabels", kwargs={
                "thread_id": "thread_008",
                "add_labels": ["release-draft"],
                "remove_labels": [],
                "changed_ts": "2024-08-23T16:35:00Z"
            }),
            Action(name="SearchGmailThreads", kwargs={"label": "dlp-flag"})
        ],
        outputs=[]
    ),

    # complexity_edges: 15
    Task(
        annotator="0",
        user_id="EXP_23",
        instruction="You are responsible for ensuring the alignment of database states across the Figma↔Gmail workflow as the review-provenance steward. Compile an audit-ready snapshot that confirms: the review for artifact art_004 initiated at 2024-08-23T13:00:00Z under cycle_1dc59e3f; its link to thread_003 confirmed on 2024-08-23T13:05:00Z; two specific Gmail messages—anna.brand@company.com “Looks good—LGTM from marketing.” at 2024-08-23T13:10:00Z and chris.engineer@company.com “Please REVISE the grid spacing to 8px multiples.” at 2024-08-23T13:15:00Z—captured with authors/timestamps/bodies; and Gmail intent tallies aligned with cycle_1dc59e3f. Record only post-fact DB changes. Present only the exported assets for art_001 as the stable handoff reference.",
        actions=[
            Action(name="StartReviewCycle", kwargs={"artifact_id": "art_004", "created_ts": "2024-08-23T13:00:00Z"}),
            Action(name="LinkReviewToThread", kwargs={"cycle_id": "cycle_1dc59e3f", "thread_id": "thread_003", "changed_ts": "2024-08-23T13:05:00Z"}),
            Action(name="AppendMessageToThread", kwargs={"thread_id": "thread_003", "from_email": "anna.brand@company.com", "body": "Looks good—LGTM from marketing.", "created_ts": "2024-08-23T13:10:00Z"}),
            Action(name="AppendMessageToThread", kwargs={"thread_id": "thread_003", "from_email": "chris.engineer@company.com", "body": "Please REVISE the grid spacing to 8px multiples.", "created_ts": "2024-08-23T13:15:00Z"}),
            Action(name="SyncGmailIntentsToReview", kwargs={"cycle_id": "cycle_1dc59e3f", "thread_id": "thread_003"}),
            Action(name="ListAssetsForArtifact", kwargs={"artifact_id": "art_001"}),
        ],
        outputs=[]
    ),

    # complexity_edges: 18
    Task(
        annotator="0",
        user_id="EXP_24",
        instruction=(
            "You are tasked with ensuring the alignment of signals and the proper hygiene of labels across the Figma↔Gmail workflow as the review-provenance steward. Construct an audit-ready record (facts, not procedures) affirming: the art_004 review set up at 2024-08-23T13:00:00Z under cycle_1dc59e3f; its attachment to thread_003 verified on 2024-08-23T13:05:00Z; the NEEDS_REVIEW status logged at 2024-08-23T13:20:00Z; an APPROVED verdict by chris.engineer@company.com at 2024-08-23T13:25:00Z with the remark 'LGTM'; a normalized conversation state where Design/Approved is shown and Design/Needs-Review is absent as of 2024-08-23T13:30:00Z; and the terminal note 'Review approved and labels aligned' recorded at 2024-08-23T13:31:00Z. Deliver the exported assets for art_001 as the stable handoff reference."
        ),
        actions=[
            Action(name="StartReviewCycle", kwargs={"artifact_id": "art_004", "created_ts": "2024-08-23T13:00:00Z"}),
            Action(name="LinkReviewToThread", kwargs={"cycle_id": "cycle_1dc59e3f", "thread_id": "thread_003", "changed_ts": "2024-08-23T13:05:00Z"}),
            Action(name="AdvanceReviewStatus", kwargs={"cycle_id": "cycle_1dc59e3f", "new_status": "NEEDS_REVIEW", "changed_ts": "2024-08-23T13:20:00Z"}),
            Action(name="RecordReviewApproval", kwargs={"cycle_id": "cycle_1dc59e3f", "approver_email": "chris.engineer@company.com", "decision": "APPROVED", "decided_ts": "2024-08-23T13:25:00Z", "comment": "LGTM"}),
            Action(name="UpdateThreadLabels", kwargs={"thread_id": "thread_003", "add_labels": ["Design/Approved"], "remove_labels": ["Design/Needs-Review"], "changed_ts": "2024-08-23T13:30:00Z"}),
            Action(name="LogTerminalEvent", kwargs={"log_ts": "2024-08-23T13:31:00Z", "message": "Review approved and labels aligned"}),
            Action(name="ListAssetsForArtifact", kwargs={"artifact_id": "art_001"}),
        ],
        outputs=[]
    ),


    # complexity_edges: 19
    Task(
        annotator="0",
        user_id="EXP_25",
        instruction=(
            "As the safety-and-workflow posture coordinator for marketing updates, ensure label maintenance and alignment with policies. The audit-ready snapshot should prove (without detailing steps): thread_010 includes marketing and has been examined as of 2024-08-24T18:20:00Z; the source conversation contains the exact memo 'Requires copy tweak on hero headline and UTM link validation' from anna.brand@company.com at 2024-08-24T18:22:00Z; a single safety evaluation was performed at 2024-08-24T18:23:00Z using only the dlp-flag upon detection and guided by dlp_config; awareness of release_009 through its diff summary; the final note 'Posture confirmed for marketing updates' documented at 2024-08-24T18:24:00Z; and the last label timestamp set at 2024-08-24T18:25:00Z. Deliver the exported assets for art_001 as the reliable point of reference for downstream stakeholders."
        ),
        actions=[
            Action(name="UpdateThreadLabels", kwargs={"thread_id": "thread_010", "add_labels": ["marketing", "triaged"], "remove_labels": [], "changed_ts": "2024-08-24T18:20:00Z"}),
            Action(name="AppendMessageToThread", kwargs={"thread_id": "thread_010", "from_email": "anna.brand@company.com", "body": "Requires copy tweak on hero headline and UTM link validation", "created_ts": "2024-08-24T18:22:00Z"}),
            Action(name="DlpScanAndLabelThread", kwargs={"thread_id": "thread_010", "label_if_found": "dlp-flag", "changed_ts": "2024-08-24T18:23:00Z"}),
            Action(name="GetReleaseDiffSummary", kwargs={"release_id": "release_009"}),
            Action(name="ReadSystemConfig", kwargs={"config_key": "dlp_config"}),
            Action(name="LogTerminalEvent", kwargs={"log_ts": "2024-08-24T18:24:00Z", "message": "Posture confirmed for marketing updates"}),
            Action(name="UpdateThreadLabels", kwargs={"thread_id": "thread_010", "add_labels": [], "remove_labels": [], "changed_ts": "2024-08-24T18:25:00Z"}),
            Action(name="ListAssetsForArtifact", kwargs={"artifact_id": "art_001"}),
        ],
        outputs=[]
    ),

    # complexity_edges: 14
    Task(
    annotator="0",
    user_id="EXP_26",
        instruction=(
            "Act as the a11y preflight and workflow-hygiene coordinator for marketing surfaces, ensuring Figma artifacts and Gmail alignment. Record—without prescribing steps—an audit-ready snapshot demonstrating: FILE artifacts managed by anna.brand@company.com tagged as website and altered on/after 2024-08-01T00:00:00Z within the scope; art_006 undergoing an audit session of type COMBINED_DS_A11Y at 2024-08-24T14:00:00Z; a terminal note 'Preflight started for art_006' at 2024-08-24T14:02:00Z; the tag audit-in-progress applied to art_006 effective 2024-08-24T14:03:00Z; and thread_010 transporting marketing and examined as of 2024-08-24T14:05:00Z. Deliver exported assets for art_001 as the stable handoff reference."
        ),
    actions=[
    Action(name="ListArtifacts", kwargs={"owner_email": "anna.brand@company.com", "tag": "website", "artifact_type": "FILE", "modified_since": "2024-08-01T00:00:00Z"}),
    Action(name="CreateAuditSession", kwargs={"artifact_id": "art_006", "created_ts": "2024-08-24T14:00:00Z", "audit_type": "COMBINED_DS_A11Y"}),
    Action(name="LogTerminalEvent", kwargs={"log_ts": "2024-08-24T14:02:00Z", "message": "Preflight started for art_006"}),
    Action(name="AddArtifactTag", kwargs={"artifact_id": "art_006", "tag": "audit-in-progress", "changed_ts": "2024-08-24T14:03:00Z"}),
    Action(name="UpdateThreadLabels", kwargs={"thread_id": "thread_010", "add_labels": ["marketing", "triaged"], "remove_labels": [], "changed_ts": "2024-08-24T14:05:00Z"}),
    Action(name="ListAssetsForArtifact", kwargs={"artifact_id": "art_001"}),
    ],
    outputs=[]
    ),

    # complexity_edges: 18
    Task(
        annotator="0",
        user_id="EXP_27",
        instruction=(
            "Oversee the end-to-end release communication process, ensuring adherence to lineage, attachment guidelines, and a deterministic closure within the release/catalog. Document an audit-standard snapshot that verifies: Figma release_001 within the release/lineage with its definitive diff; a draft in thread_006 by emma.creative@company.com on 2024-08-22T17:00:00Z (subject 'Release 1.2.0 Announcement', body 'Highlights and changes included.'); attachment verification via Gmail message_id relmsg_9cc87e81; a discussion status where Design/Release and announced are included, and draft is absent as of 2024-08-22T17:06:30Z; the closing note 'Release comms drafted and announced.' at 2024-08-22T17:07:00Z; and a safety review for thread_006 aligned to dlp_config. Return the exported assets for art_001 as the stable reference."
        ),
        actions=[
            Action(name="ListReleases", kwargs={"version_prefix": "release/"}),
            Action(name="GetReleaseDiffSummary", kwargs={"release_id": "release_001"}),
            Action(name="ComposeReleaseEmailDraft", kwargs={"release_id": "release_001", "thread_id": "thread_006", "from_email": "emma.creative@company.com", "created_ts": "2024-08-22T17:00:00Z", "subject": "Release 1.2.0 Announcement", "body": "Highlights and changes included."}),
            Action(name="GuardAttachmentPolicyOnDraft", kwargs={"message_id": "relmsg_9cc87e81"}),
            Action(name="UpdateThreadLabels", kwargs={"thread_id": "thread_006", "add_labels": ["Design/Release", "announced"], "remove_labels": ["draft"], "changed_ts": "2024-08-22T17:06:30Z"}),
            Action(name="AppendMessageToThread", kwargs={"thread_id": "thread_006", "from_email": "emma.creative@company.com", "body": "Release comms drafted and announced.", "created_ts": "2024-08-22T17:07:00Z"}),
            Action(name="DlpScanThread", kwargs={"thread_id": "thread_006"}),
            Action(name="ReadSystemConfig", kwargs={"config_key": "dlp_config"}),
            Action(name="ListAssetsForArtifact", kwargs={"artifact_id": "art_001"}),
        ],
        outputs=[]
    ),

    # complexity_edges: 16
    Task(
        annotator="0",
        user_id="EXP_28",
        instruction="Manage brand-guidance provenance ensuring signal coherence and label integrity throughout the Figma↔Gmail workflow (db-modification traceable) with a focus on safety alignment. Supply an audit-standard document—focusing on facts instead of procedures—confirming: governance inputs intent_keywords and dlp_config acknowledged; a definitive Figma note on art_012 by sophie.marketing@company.com at 2024-08-24T15:00:00Z anchored at node-12:9 with body “Consolidate brand tokens to v3 palette.”; a Gmail collaborative memo in thread_010 from anna.brand@company.com at 2024-08-24T15:05:00Z with body “Brand token rollout scheduled for next sprint.”; a conversational setup where marketing and figma-sync are included as of 2024-08-24T15:06:00Z; and a documented DLP safety review for thread_010. Provide exported assets for art_001 as the stable reference for release-comms alignment.",
        actions=[
            Action(name="ReadSystemConfig", kwargs={"config_key": "intent_keywords"}),
            Action(name="ReadSystemConfig", kwargs={"config_key": "dlp_config"}),
            Action(name="CreateFigmaComment", kwargs={"artifact_id": "art_012", "author_email": "sophie.marketing@company.com", "body": "Consolidate brand tokens to v3 palette.", "anchor_ref": "node-12:9", "created_ts": "2024-08-24T15:00:00Z"}),
            Action(name="AppendMessageToThread", kwargs={"thread_id": "thread_010", "from_email": "anna.brand@company.com", "body": "Brand token rollout scheduled for next sprint.", "created_ts": "2024-08-24T15:05:00Z"}),
            Action(name="UpdateThreadLabels", kwargs={"thread_id": "thread_010", "add_labels": ["marketing", "figma-sync"], "remove_labels": [], "changed_ts": "2024-08-24T15:06:00Z"}),
            Action(name="DlpScanThread", kwargs={"thread_id": "thread_010"}),
            Action(name="ListAssetsForArtifact", kwargs={"artifact_id": "art_001"}),
        ],
        outputs=[]
    ),


    # complexity_edges: 19
    Task(
        annotator="0",
        user_id="EXP_29",
        instruction="Serve as the release-communications steward within the Figma↔Gmail workflow, adhering to the release/ lineage and attachment guardrails. Generate a non-procedural, audit-ready snapshot that verifies the following facts (without detailing how they were produced): release_001 is considered the authoritative diff in the release/ catalog; there is a deterministic draft within thread_006 from emma.creative@company.com dated 2024-08-22T17:00:00Z with the subject 'Release 1.2.0 Announcement' and content 'Highlights and changes included.'; attachment-policy compliance is demonstrated via message_id relmsg_9cc87e81; the conversation posture indicates db modification Design/Release, and the presence announced while draft absent as of 2024-08-22T17:06:00Z; the final note 'APPROVE rollout.' is recorded at 2024-08-22T17:07:00Z; along with a documented safety evaluation for thread_006. Incorporate the exported assets associated with art_001 as the stable reference.",
        actions=[
            Action(name="ListReleases", kwargs={"version_prefix": "release/"}),
            Action(name="GetReleaseDiffSummary", kwargs={"release_id": "release_001"}),
            Action(name="ComposeReleaseEmailDraft", kwargs={"release_id": "release_001", "thread_id": "thread_006", "from_email": "emma.creative@company.com", "created_ts": "2024-08-22T17:00:00Z", "subject": "Release 1.2.0 Announcement", "body": "Highlights and changes included."}),
            Action(name="GuardAttachmentPolicyOnDraft", kwargs={"message_id": "relmsg_9cc87e81"}),
            Action(name="UpdateThreadLabels", kwargs={"thread_id": "thread_006", "add_labels": ["Design/Release", "announced"], "remove_labels": ["draft"], "changed_ts": "2024-08-22T17:06:00Z"}),
            Action(name="AppendMessageToThread", kwargs={"thread_id": "thread_006", "from_email": "emma.creative@company.com", "body": "APPROVE rollout.", "created_ts": "2024-08-22T17:07:00Z"}),
            Action(name="DlpScanThread", kwargs={"thread_id": "thread_006"}),
            Action(name="ListAssetsForArtifact", kwargs={"artifact_id": "art_001"}),
        ],
        outputs=[]
    ),

    # complexity_edges: 14
    Task(
        annotator="0",
        user_id="EXP_30",
        instruction="Act as the audit preparation and cleanup steward for art_006, documenting posture without outlining steps. Compile an audit-ready record presenting evidence showing: design_system_mappings reviewed; a COMBINED_DS_A11Y audit session for art_006 at 2024-08-24T13:00:00Z; the entry 'Prep audit for marketing site' at 2024-08-24T13:02:00Z; tag a11y-queued marked at 2024-08-24T13:03:00Z; tag audit-in-progress noted at 2024-08-24T13:06:00Z; a11y-queued tag removed at 2024-08-24T13:19:00Z; audit-in-progress tag removed at 2024-08-24T13:20:00Z; the entry 'Cleanup audit markers' at 2024-08-24T13:21:00Z; together with the canonical artifact summary for art_006.",
        actions=[
            Action(name="ReadSystemConfig", kwargs={"config_key": "design_system_mappings"}),
            Action(name="CreateAuditSession", kwargs={"artifact_id": "art_006", "created_ts": "2024-08-24T13:00:00Z", "audit_type": "COMBINED_DS_A11Y"}),
            Action(name="LogTerminalEvent", kwargs={"log_ts": "2024-08-24T13:02:00Z", "message": "Prep audit for marketing site"}),
            Action(name="AddArtifactTag", kwargs={"artifact_id": "art_006", "tag": "a11y-queued", "changed_ts": "2024-08-24T13:03:00Z"}),
            Action(name="AddArtifactTag", kwargs={"artifact_id": "art_006", "tag": "audit-in-progress", "changed_ts": "2024-08-24T13:06:00Z"}),
            Action(name="RemoveArtifactTag", kwargs={"artifact_id": "art_006", "tag": "a11y-queued", "changed_ts": "2024-08-24T13:19:00Z"}),
            Action(name="RemoveArtifactTag", kwargs={"artifact_id": "art_006", "tag": "audit-in-progress", "changed_ts": "2024-08-24T13:20:00Z"}),
            Action(name="LogTerminalEvent", kwargs={"log_ts": "2024-08-24T13:21:00Z", "message": "Cleanup audit markers"}),
            Action(name="GetArtifactSummary", kwargs={"artifact_id": "art_006"}),
        ],
        outputs=[]
    ),

#     ### BACKUP TASKS ####
#     #####################
    # # complexity_edges:  18
    # Task(
    #     annotator="0",
    #     user_id="EXP_43",
    #     instruction="You are the safety-and-workflow posture coordinator for marketing updates on thread_010, operating with DLP and intent awareness. Provide a non-procedural, audit-ready record that shows: labels marketing and triaged present on thread_010 effective 2024-08-24T18:20:00Z; a memo from anna.brand@company.com recorded at 2024-08-24T18:22:00Z with exact body 'Requires copy tweak on hero headline and UTM link validation'; a DLP evaluation at 2024-08-24T18:23:00Z that applies label dlp-flag only upon detection; awareness of release_009 via its diff summary; dlp_config and intent_keywords consulted; the terminal log 'DLP posture recorded' at 2024-08-24T18:26:00Z; label safety/checked present at 2024-08-24T18:27:00Z with a no-op confirmation at 2024-08-24T18:28:00Z; and the exported assets for art_001 as the stable reference.",
    #     actions=[
    #         Action(name="UpdateThreadLabels", kwargs={"thread_id": "thread_010", "add_labels": ["marketing", "triaged"], "remove_labels": [], "changed_ts": "2024-08-24T18:20:00Z"}),
    #         Action(name="AppendMessageToThread", kwargs={"thread_id": "thread_010", "from_email": "anna.brand@company.com", "body": "Requires copy tweak on hero headline and UTM link validation", "created_ts": "2024-08-24T18:22:00Z"}),
    #         Action(name="DlpScanAndLabelThread", kwargs={"thread_id": "thread_010", "label_if_found": "dlp-flag", "changed_ts": "2024-08-24T18:23:00Z"}),
    #         Action(name="GetReleaseDiffSummary", kwargs={"release_id": "release_009"}),
    #         Action(name="ReadSystemConfig", kwargs={"config_key": "dlp_config"}),
    #         Action(name="ReadSystemConfig", kwargs={"config_key": "intent_keywords"}),
    #         Action(name="LogTerminalEvent", kwargs={"log_ts": "2024-08-24T18:26:00Z", "message": "DLP posture recorded"}),
    #         Action(name="UpdateThreadLabels", kwargs={"thread_id": "thread_010", "add_labels": ["safety/checked"], "remove_labels": [], "changed_ts": "2024-08-24T18:27:00Z"}),
    #         Action(name="UpdateThreadLabels", kwargs={"thread_id": "thread_010", "add_labels": [], "remove_labels": [], "changed_ts": "2024-08-24T18:28:00Z"}),
    #         Action(name="ListAssetsForArtifact", kwargs={"artifact_id": "art_001"}),
    #     ],
    #     outputs=[
    #         """[
    # {
    # "asset_id": "asset_001",
    # "profile": null,
    # "file_name": null,
    # "mime_type": null
    # },
    # {
    # "asset_id": "asset_002",
    # "profile": null,
    # "file_name": null,
    # "mime_type": null
    # }
    # ]"""
    # ]
    # ),

    # # complexity_edges: 17
    # Task(
    #     annotator="0",
    #     user_id="EXP_44",
    #     instruction="You are the guarded release-communications coordinator operating under the release/ lineage with attachment and DLP guardrails. Provide a non-procedural, audit-ready snapshot confirming: releases discoverable with version_prefix 'release/'; release_001 validated via its diff summary; a draft in thread_006 from emma.creative@company.com at 2024-08-22T17:00:00Z with subject 'Release 1.2.0 Announcement' and body 'Highlights and changes included.'; attachment policy validation via Gmail relmsg_9cc87e81; a conversation posture where Design/Release and announced are present and draft is absent as of 2024-08-22T17:06:00Z; the closing note 'APPROVE rollout.' at 2024-08-22T17:07:00Z; a DLP scan on thread_006 with the terminal log 'DLP scan complete' at 2024-08-22T17:08:00Z; and the exported Figma assets for art_001 as the stable reference.",
    #     actions=[
    #         Action(name="ListReleases", kwargs={"version_prefix": "release/"}),
    #         Action(name="GetReleaseDiffSummary", kwargs={"release_id": "release_001"}),
    #         Action(name="ComposeReleaseEmailDraft", kwargs={"release_id": "release_001", "thread_id": "thread_006", "from_email": "emma.creative@company.com", "created_ts": "2024-08-22T17:00:00Z", "subject": "Release 1.2.0 Announcement", "body": "Highlights and changes included."}),
    #         Action(name="GuardAttachmentPolicyOnDraft", kwargs={"message_id": "relmsg_9cc87e81"}),
    #         Action(name="UpdateThreadLabels", kwargs={"thread_id": "thread_006", "add_labels": ["Design/Release", "announced"], "remove_labels": ["draft"], "changed_ts": "2024-08-22T17:06:00Z"}),
    #         Action(name="AppendMessageToThread", kwargs={"thread_id": "thread_006", "from_email": "emma.creative@company.com", "body": "APPROVE rollout.", "created_ts": "2024-08-22T17:07:00Z"}),
    #         Action(name="DlpScanThread", kwargs={"thread_id": "thread_006"}),
    #         Action(name="LogTerminalEvent", kwargs={"log_ts": "2024-08-22T17:08:00Z", "message": "DLP scan complete"}),
    #         Action(name="ListAssetsForArtifact", kwargs={"artifact_id": "art_001"}),
    #     ],
    #     outputs=[
    #         """[
    # {
    # "asset_id": "asset_001",
    # "profile": null,
    # "file_name": null,
    # "mime_type": null
    # },
    # {
    # "asset_id": "asset_002",
    # "profile": null,
    # "file_name": null,
    # "mime_type": null
    # }
    # ]"""
    # ]
    # ),


    # # complexity_edges: 17
    # Task(
    #     annotator="0",
    #     user_id="EXP_45",
    #     instruction="You are the cross-surface provenance steward coordinating a deterministic brand note within review governance. Provide an audit-ready, non-procedural record that demonstrates: a review for art_003 created at 2024-08-23T12:45:00Z (cycle_7a255cf0) and associated with thread_001 at 2024-08-23T12:50:00Z; status NEEDS_REVIEW effective 2024-08-23T12:55:00Z; a stakeholder nudge captured in thread_001 from sophie.marketing@company.com at 2024-08-23T12:58:00Z with body 'Brand guidance incoming.'; a label stance where Brand/Review is present and urgent absent as of 2024-08-23T12:59:00Z; a brand comment on Figma art_003 by sophie.marketing@company.com anchored node-2:7 at 2024-08-23T12:00:00Z with body 'Please update the brand color token to Brand/Primary/600.'; and the author-scoped Figma comment list for artifact_id art_003 filtered to author_email sophie.marketing@company.com since 2024-08-01T00:00:00Z.",
    #     actions=[
    #         Action(name="StartReviewCycle", kwargs={"artifact_id": "art_003", "created_ts": "2024-08-23T12:45:00Z"}),
    #         Action(name="LinkReviewToThread", kwargs={"cycle_id": "cycle_7a255cf0", "thread_id": "thread_001", "changed_ts": "2024-08-23T12:50:00Z"}),
    #         Action(name="AdvanceReviewStatus", kwargs={"cycle_id": "cycle_7a255cf0", "new_status": "NEEDS_REVIEW", "changed_ts": "2024-08-23T12:55:00Z"}),
    #         Action(name="AppendMessageToThread", kwargs={"thread_id": "thread_001", "from_email": "sophie.marketing@company.com", "body": "Brand guidance incoming.", "created_ts": "2024-08-23T12:58:00Z"}),
    #         Action(name="UpdateThreadLabels", kwargs={"thread_id": "thread_001", "add_labels": ["Brand/Review"], "remove_labels": ["urgent"], "changed_ts": "2024-08-23T12:59:00Z"}),
    #         Action(name="CreateFigmaComment", kwargs={"artifact_id": "art_003", "author_email": "sophie.marketing@company.com", "body": "Please update the brand color token to Brand/Primary/600.", "anchor_ref": "node-2:7", "created_ts": "2024-08-23T12:00:00Z"}),
    #         Action(name="ListFigmaComments", kwargs={"artifact_id": "art_003", "author_email": "sophie.marketing@company.com", "since_ts": "2024-08-01T00:00:00Z"}),
    #     ],
    #     outputs=[
    #         """[
    # {
    # "comment_id": "cmt_10b86546",
    # "author_email": "sophie.marketing@company.com",
    # "anchor_ref": "node-2:7",
    # "body": "Please update the brand color token to Brand/Primary/600.",
    # "created_ts": "2024-08-23T12:00:00Z"
    # }
    # ]"""
    # ]
    # ),

#     # # complexity_edges: 13
#     # Task(
#     #     annotator="0",
#     #     user_id="EXP_46",
#     #     instruction="You own accessibility feedback coordination for the admin panel header. Target state: an active design-review conversation in Gmail (label “design-review”, participant chris.engineer@company.com, keyword “Design”); art_003 carries a canonical note by sophie.marketing@company.com at 2024-08-26T10:00:00Z anchored node-3:header with body “Add ARIA labels and keyboard navigation support.”; thread_001 posture shows a11y and figma-sync present and urgent absent with changed_ts 2024-08-26T10:00:00Z; a kickoff message from chris.engineer@company.com at 2024-08-26T10:01:00Z with body “Accessibility improvements in progress - adding ARIA labels and keyboard navigation support”; and exported assets for art_001 as handoff evidence. Use resolution_notes Accessibility improvements in progress - adding ARIA labels and keyboard navigation support or similar.",
#     #     actions=[
#     #         Action(name="SearchGmailThreads", kwargs={"label": "design-review", "participant": "chris.engineer@company.com", "keyword": "Design"}),
#     #         Action(name="CreateFigmaComment", kwargs={"artifact_id": "art_003", "author_email": "sophie.marketing@company.com", "body": "Add ARIA labels and keyboard navigation support.", "anchor_ref": "node-3:header", "created_ts": "2024-08-26T10:00:00Z"}),
#     #         Action(name="UpdateThreadLabels", kwargs={"thread_id": "thread_001", "add_labels": ["a11y", "figma-sync"], "remove_labels": ["urgent"], "changed_ts": "2024-08-26T10:00:00Z"}),
#     #         Action(name="AppendMessageToThread", kwargs={"thread_id": "thread_001", "from_email": "chris.engineer@company.com", "body": "Accessibility improvements in progress - adding ARIA labels and keyboard navigation support", "created_ts": "2024-08-26T10:01:00Z"}),
#     #         Action(name="ListAssetsForArtifact", kwargs={"artifact_id": "art_001"}),
#     #     ],
#     #     outputs=[
#     #     """[
#     #     {
#     #     "asset_id": "asset_001",
#     #     "profile": null,
#     #     "file_name": null,
#     #     "mime_type": null
#     #     },
#     #     {
#     #     "asset_id": "asset_002",
#     #     "profile": null,
#     #     "file_name": null,
#     #     "mime_type": null
#     #     }
#     #     ]"""
#     #     ]
#     # ),

#     # # complexity_edges: 14
#     # Task(
#     # annotator="0",
#     # user_id="EXP_47",
#     # instruction="You own settings-screen accessibility and brand guidance with FRAME scope. Target state: FRAME artifacts covered for owner jake.design@company.com tagged “revise” modified_since 2024-08-01T00:00:00Z; export availability evidenced by assets for art_012; a brand note on art_012 by sophie.marketing@company.com at 2024-08-28T09:00:00Z anchored node-12:1 with body “Align tokens with brand v3.”; thread_010 labels show a11y and triaged present and design removed with changed_ts 2024-08-28T09:02:00Z; audit narrative “Brand v3 guidance posted for settings screen” at 2024-08-28T09:03:00Z; authoritative reference is the canonical artifact summary for art_012.",
#     # actions=[
#     #     Action(name="ListArtifacts", kwargs={
#     #     "owner_email": "jake.design@company.com",
#     #     "tag": "revise",
#     #     "artifact_type": "FRAME",
#     #     "modified_since": "2024-08-01T00:00:00Z"
#     #     }),
#     #     Action(name="ListAssetsForArtifact", kwargs={"artifact_id": "art_012"}),
#     #     Action(name="CreateFigmaComment", kwargs={
#     #     "artifact_id": "art_012",
#     #     "author_email": "sophie.marketing@company.com",
#     #     "body": "Align tokens with brand v3.",
#     #     "anchor_ref": "node-12:1",
#     #     "created_ts": "2024-08-28T09:00:00Z"
#     #     }),
#     #     Action(name="UpdateThreadLabels", kwargs={
#     #     "thread_id": "thread_010",
#     #     "add_labels": ["a11y", "triaged"],
#     #     "remove_labels": ["design"],
#     #     "changed_ts": "2024-08-28T09:02:00Z"
#     #     }),
#     #     Action(name="LogTerminalEvent", kwargs={
#     #     "log_ts": "2024-08-28T09:03:00Z",
#     #     "message": "Brand v3 guidance posted for settings screen"
#     #     }),
#     #     Action(name="GetArtifactSummary", kwargs={"artifact_id": "art_012"}),
#     # ],
#     # outputs=[
#     # """{
#     # "artifact_id": "art_012",
#     # "artifact_name": "Settings Screen",
#     # "artifact_type": "FRAME",
#     # "owner_email": "jake.design@company.com
#     # ",
#     # "deep_link": "https://www.figma.com/file/xyz789ghi012/Mobile-App?node-id=2%3A4
#     # ",
#     # "current_tags": [
#     # "settings",
#     # "mobile",
#     # "app",
#     # "revise"
#     # ],
#     # "modified_ts": "2024-08-23T10:30:00Z"
#     # }"""
#     # ]
#     # ),

#     # # complexity_edges: 13
#     # Task(
#     #     annotator="0",
#     #     user_id="HARD_401",
#     #     instruction=(
#     #         "You own a11y preparation hygiene for the marketing website FILE scope. "
#     #         "The audit-ready snapshot should evidence: FILE artifacts for owner anna.brand@company.com tagged website and modified on/after 2024-08-01T00:00:00Z confirming art_006; "
#     #         "for art_006, an audit-in-progress lifecycle with the tag present at 2024-08-28T13:00:00Z, a preparation note “Prepared audit for art_006” at 2024-08-28T13:05:00Z, and the tag cleared at 2024-08-28T13:20:00Z. "
#     #         "Return the canonical artifact summary for art_006."
#     #     ),
#     #     actions=[
#     #         Action(name="ListArtifacts", kwargs={"owner_email": "anna.brand@company.com", "tag": "website", "artifact_type": "FILE", "modified_since": "2024-08-01T00:00:00Z"}),
#     #         Action(name="AddArtifactTag", kwargs={"artifact_id": "art_006", "tag": "audit-in-progress", "changed_ts": "2024-08-28T13:00:00Z"}),
#     #         Action(name="LogTerminalEvent", kwargs={"log_ts": "2024-08-28T13:05:00Z", "message": "Prepared audit for art_006"}),
#     #         Action(name="RemoveArtifactTag", kwargs={"artifact_id": "art_006", "tag": "audit-in-progress", "changed_ts": "2024-08-28T13:20:00Z"}),
#     #         Action(name="GetArtifactSummary", kwargs={"artifact_id": "art_006"}),
#     #     ],
#     #     outputs=[
#     #     """{
#     #     "artifact_id": "art_006",
#     #     "artifact_name": "Marketing Website",
#     #     "artifact_type": "FILE",
#     #     "owner_email": "anna.brand@company.com",
#     #     "deep_link": "https://www.figma.com/file/def456ghi789/Marketing-Website",
#     #     "current_tags": [
#     #     "marketing",
#     #     "website",
#     #     "landing-pages"
#     #     ],
#     #     "modified_ts": "2024-08-28T13:20:00Z"
#     #     }"""
#     #     ]
#     # ),

#     # # complexity_edges: 13
#     # Task(
#     #     annotator="0",
#     #     user_id="HARD_402",
#     #     instruction=(
#     #         "You own release-communications readiness for the design system under the release/ lineage. "
#     #         "The audit-ready snapshot should evidence: lineage discoverability via version_prefix “release/”; "
#     #         "for release_001, a draft in thread_006 from emma.creative@company.com created at 2024-08-28T11:00:00Z with subject “Release 1.2.0 Announcement” and body “Highlights and changes included.” validated against attachment policy using message_id relmsg_0d5cb1ea; "
#     #         "thread posture where Design/Release and announced are present and draft is absent with changed_ts 2024-08-28T11:05:00Z. "
#     #         "Return the diff summary for release_001."
#     #     ),
#     #     actions=[
#     #         Action(name="ListReleases", kwargs={"version_prefix": "release/"}),
#     #         Action(name="ComposeReleaseEmailDraft", kwargs={
#     #         "release_id": "release_001",
#     #         "thread_id": "thread_006",
#     #         "from_email": "emma.creative@company.com",
#     #         "created_ts": "2024-08-28T11:00:00Z",
#     #         "subject": "Release 1.2.0 Announcement",
#     #         "body": "Highlights and changes included."
#     #         }),
#     #         Action(name="GuardAttachmentPolicyOnDraft", kwargs={"message_id": "relmsg_0d5cb1ea"}),
#     #         Action(name="UpdateThreadLabels", kwargs={
#     #         "thread_id": "thread_006",
#     #         "add_labels": ["Design/Release", "announced"],
#     #         "remove_labels": ["draft"],
#     #         "changed_ts": "2024-08-28T11:05:00Z"
#     #         }),
#     #         Action(name="GetReleaseDiffSummary", kwargs={"release_id": "release_001"}),
#     #     ],
#     #     outputs=[
#     #     """{
#     #     "release_id": "release_001",
#     #     "added": 0,
#     #     "updated": 0,
#     #     "removed": 0
#     #     }"""
#     #     ]
#     # ),

]
