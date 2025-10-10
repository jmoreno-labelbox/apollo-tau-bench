RULES = [
    "WORKFLOW 1a - DESIGN REVIEW"
    "STEP 1. Identify figma artifacts with a specific tag"
    "Use filter_figma_artifacts_by_tags, required kwargs 'tags': <list_of_tags_to_filter_by>"

    "STEP 2. Export identified figma artifacts to assets"
    "Use export_figma_artifacts_to_assets, required kwargs 'artifact_ids': <list_of_artifacts_to_export>, 'export_profile': {'format': <one_of_['PNG', 'JPG', 'SVG', 'PDF']>, 'scale': <'1x', '2x' or '4x'>}"

    "STEP 3. Create gmail_threads entry"
    "Use create_gmail_thread, required kwargs 'sender_email': <email_of_sender>, 'recipients_emails': ['design-review@company.com', 'ux-team@company.com'], 'workflow_type': <One of ['review', 'release']>, 'current_labels': <list_of_labels_to_apply_from: ['design-review', 'urgent', 'figma', 'mobile', 'feedback', 'ux', 'marketing', 'approval', 'launch', 'accessibility', 'audit', 'admin', 'brand', 'guidelines', 'update', 'design_system', 'components', 'library', 'implementation', 'profile', 'pricing', 'ab_testing', 'results', 'component', 'review', 'data_table', 'navigation', 'responsive', 'design_needs_review', 'design_approved', 'design_changes_requested', 'design_escalation', 'design_release']>"

    "STEP 4. Create review_cycles entry/entries (1 per artifact)"
    "Use create_review_cycle, required kwargs 'artifact_id': <artifact_id>, 'status': <one_of_['NEEDS_REVIEW', 'APPROVED', 'CHANGES_REQUESTED', 'ESCALATED', 'IN_FLIGHT']>, 'thread_id_nullable': <gmail_thread_id>"

    "STEP 5. Create gmail_messages entry"
    "Use create_gmail_message, required kwargs 'sender_email': <email_of_sender>, 'workflow_type': 'review', 'thread_id': <gmail_thread_id>, 'attachments_asset_ids': <list_of_asset_ids>"

    "PARAMETER SOURCES"
    "The instructions should give the parameters for 'tags', 'export_profile', 'sender_email', 'current_labels', 'status'(should be 'NEEDS_REVIEW')"
    "Other parameters should be sourced from output of previous actions"

    "WORKFLOW 1b - DESIGN APPROVAL"
    "STEP 1. Create figma comment entry from a gmail message"
    "Use create_figma_comment_from_gmail_message, required kwargs 'artifact_id': <artifact_id>, 'gmail_message_id': <gmail_message_id>"

    "STEP 2. Update the related review cycle"
    "Use update_review_cycle_status, required kwargs 'cycle_id': <review_cycle_id>, 'new_status': <one_of_['NEEDS_REVIEW', 'APPROVED', 'CHANGES_REQUESTED', 'ESCALATED', 'IN_FLIGHT']>"

    "STEP 3. Create review approval entry if status is approved"
    "Use create_review_approval, required kwargs 'cycle_id': <review_cycle_id>, and either or both of 'approval_comment_id': <approval_comment_id> and/or approver_email : <approver_email>"

    "WORKFLOW 2 - DESIGN RELEASE"
    "STEP 1. Find out if it is a release version (continue with workflow either way)"
    "Use detect_release_version, required kwargs 'release_id': <release_id>"

    "STEP 2. Compute diffs"
    "Use compute_release_diffs, required kwargs 'release_id': <release_id>, 'changelog_highlights': <a list of short (3-6 words) descriptions of release changes>"

    "STEP 3. Save computed diffs"
    "Use save_release_diffs, required kwargs 'release_id': <release_id>, 'prior_release_id_nullable': <prior_release_id>, 'frames_added': <frames_added>, 'frames_updated': <frames_updated>, 'frames_removed': <frames_removed>, 'component_version_bumps': <component_version_bumps>, 'changelog_highlights': <changelog_highlights>"

    "STEP 4. Get frames tagged with 'hero'"
    "Use filter_figma_artifacts_by_tags, required kwargs 'tags': ['hero']"

    "STEP 5. Export 'hero' frames to assets"
    "Use export_figma_artifacts_to_assets, required kwargs 'artifact_ids': <list_of_hero_artifact_ids>, 'export_profile': {'format': <one_of_['PNG', 'JPG', 'SVG', 'PDF']>, 'scale': <'1x', '2x' or '4x'>}"

    "STEP 6. Generate before/after visuals"
    "Use generate_before_after_visuals, required kwargs 'release_id': <release_id>, 'hero_artifact_ids': <list_of_hero_artifact_ids>"

    "STEP 7. Create release gmail_message"
    "Use create_gmail_message, required kwargs 'sender_email': <email_of_sender>, 'workflow_type': 'release', 'thread_id': <gmail_thread_id>, 'attachments_asset_ids': <list_of_asset_ids>"

    "STEP 8. Create gmail_threads entry"
    "Use create_gmail_thread, required kwargs 'sender_email': <email_of_sender>, 'recipients_emails': <list_of_recipient_emails>, 'workflow_type': 'release', 'current_labels': <list_of_current_labels>"

    "PARAMETER SOURCES"
    "The instructions should give parameters for: release_id, changelog_highlights, sender_email, recipients_emails"
    "Other parameters should be sourced from output of previous actions"

    "WORKFLOW 3a - DESIGN SYSTEM AUDIT"
    "STEP 1. Create audit session"
    "Use create_audit_session, required kwargs 'artifact_id': <artifact_id>, 'audit_type': 'DS_MAPPING'"

    "STEP 2. Identify custom groups and map to DS components"
    "Use identify_custom_groups_and_map_to_ds_components, required kwargs 'audit_id': <audit_id>"

    "STEP 3. Record findings in audit_findings_ds"
    "Use record_ds_audit_findings, required kwargs 'audit_id': <audit_id>, 'layer_id': <layer_id>, 'layer_name': <layer_name>, 'finding_type': <finding_type>, 'recommended_component_id_nullable': <recommended_component_id_nullable>, 'severity': <severity>" #'code_connect_link_nullable'(optional): <code_connect_link_nullable>

    "STEP 4. Generate PDF report"
    "Use generate_audit_report, required kwargs 'audit_id': <audit_id>"

    "STEP 5. Update audit status"
    "Use update_audit_status, required kwargs 'audit_id': <audit_id>, 'status': 'COMPLETED'"

    "STEP 6. Link audit report asset"
    "Use link_audit_report_asset, required kwargs 'audit_id': <audit_id>, 'report_asset_id': <asset_id>"

    "PARAMETER SOURCES"
    "The instructions should ONLY give parameters for: artifact_id"
    "ALL other parameters should be sourced from output of previous actions"

    "OUTPUTS"
    "Only the ID's of new database entries"

    "WORKFLOW 3b - ACCESSIBILITY CHECK/AUDIT"
    "STEP 1. Get artifact_id from artifact_name"
    "Use get_artifact_id_from_name, required kwargs 'artifact_name': <artifact_name>"

    "STEP 2. Create audit session"
    "Use create_audit_session, required kwargs 'artifact_id': <artifact_id>, 'audit_type': 'A11Y'"

    "STEP 3. Evaluate accessibility"
    "Use evaluate_accessibility, required kwargs 'artifact_id': <artifact_id>"

    "STEP 4. Record findings in audit_findings_a11y"
    "Use record_accessibility_audit_findings, required kwargs 'audit_id': <audit_id>, 'layer_id': <layer_id>, 'layer_name': <layer_name>, 'violation_type': <violation_type>, 'violation_details_json': <violation_details_json>, 'severity': <severity>, 'recommended_fix_summary': <recommended_fix_summary>"

    "STEP 5. Generate PDF report"
    "Use generate_audit_report, required kwargs 'audit_id': <audit_id>"

    "STEP 6. Update audit status"
    "Use update_audit_status, required kwargs 'audit_id': <audit_id>, 'status': 'COMPLETED'"

    "STEP 7. Link audit report asset"
    "Use link_audit_report_asset, required kwargs 'audit_id': <audit_id>, 'report_asset_id': <asset_id>"

    "PARAMETER SOURCES"
    "The instructions should ONLY give parameters for: artifact_name"
    "ALL other parameters should be sourced from output of previous actions"

    "OUTPUTS"
    "Only the ID's of new database entries"

    "WORKFLOW 3c - COMBINED DESIGN SYSTEM AND ACCESSIBILITY AUDIT"
    "STEP 1. Get artifact_id from artifact_name"
    "Use get_artifact_id_from_name, required kwargs 'artifact_name': <artifact_name>"

    "STEP 2. Create audit session"
    "Use create_audit_session, required kwargs 'artifact_id': <artifact_id>, 'audit_type': 'COMBINED_DS_A11Y'"

    "STEP 3. Identify custom groups and map to DS components"
    "Use identify_custom_groups_and_map_to_ds_components, required kwargs 'audit_id': <audit_id>"

    "STEP 4. Record findings in audit_findings_ds"
    "Use record_ds_audit_findings, required kwargs 'audit_id': <audit_id>, 'layer_id': <layer_id>, 'layer_name': <layer_name>, 'finding_type': <finding_type>, 'recommended_component_id_nullable': <recommended_component_id_nullable>, 'severity': <severity>"

    "STEP 5. Evaluate accessibility"
    "Use evaluate_accessibility, required kwargs 'artifact_id': <artifact_id>"

    "STEP 6. Record findings in audit_findings_a11y"
    "Use record_accessibility_audit_findings, required kwargs 'audit_id': <audit_id>, 'layer_id': <layer_id>, 'layer_name': <layer_name>, 'violation_type': <violation_type>, 'violation_details_json': <violation_details_json>, 'severity': <severity>, 'recommended_fix_summary': <recommended_fix_summary>"

    "STEP 8. Generate PDF report"
    "Use generate_audit_report, required kwargs 'audit_id': <audit_id>"

    "STEP 9. Update audit status"
    "Use update_audit_status, required kwargs 'audit_id': <audit_id>, 'status': 'COMPLETED'"

    "STEP 10. Link audit report asset"
    "Use link_audit_report_asset, required kwargs 'audit_id': <audit_id>, 'report_asset_id': <asset_id>"

    "OUTPUTS"
    "Only the ID's of new database entries"

    "PARAMETER SOURCES"
    "The instructions should ONLY give parameters for: artifact_id"
    "ALL other parameters should be sourced from output of previous actions"

    "WORKFLOW 4 - FIX PLAN AND HANDOFF"
    "STEP 1. Load audit findings"
    "Use load_audit_findings, required kwargs 'audit_id': <audit_id>"

    "STEP 2. Prioritize findings"
    "Use prioritize_audit_findings, required kwargs 'finding_ids_list': <finding_ids_list>"

    "STEP 3. Create fix plan"
    "Use create_fix_plan, required kwargs 'audit_id': <audit_id>, 'owner_email': <owner_email>"

    "STEP 4. Create fix items in order"
    "Use create_fix_item, required kwargs 'plan_id': <plan_id>, 'finding_id': <finding_id>"

    "STEP 5. Create and deliver fix plan"
    "Use create_and_deliver_fix_plan, required kwargs 'plan_id': <plan_id>"

    "STEP 6. Notify stakeholders"
    "Use notify_stakeholders, required kwargs 'plan_id': <plan_id>, 'stakeholder_emails': <list_of_stakeholder_emails>, 'audit_id': <audit_id>, 'status': <status>, 'owner_email': <owner_email>"

    "PARAMETER SOURCES"
    "The instructions should ONLY give parameters for: audit_id, owner_email"
    "ALL other parameters should be sourced from output of previous actions"

    "OUTPUTS"
    "Only the ID's of new database entries"
]

# **Workflow Example:**
# 1. Load audit findings from Tasks 3
# 2. Prioritize by severity, impact, and ease of fix
# 3. Apply change budget (5 items max per frame)
# 4. Generate fix suggestions in `fix_items`
# 5. Deliver via chosen method:
#    - **COMMENTS:** Post anchored Figma comments
#    - **TICKETS:** Create external tracker tickets
#    - **PDF:** Export handoff document
# 6. Notify owners and schedule follow-up
