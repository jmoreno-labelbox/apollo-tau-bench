from domains.dto import Task, Action

TASKS = [
    Task(
        annotator="0",
        user_id="task_001",
        instruction=(
            "You need to coordinate a comprehensive design review process for artifacts requiring feedback. "
            "You should focus on 'needs-review' tagged artifacts and prepare them for stakeholder evaluation. "
            "Your export format should be PNG at 2x scale for optimal review quality. You will be working as "
            "'design-lead@company.com' with recipients design-review@company.com and ux-team@company.com. "
            "You should use 'design-review' and 'figma' labels for thread organization, and ensure each "
            "artifact gets NEEDS_REVIEW status for proper tracking."
        ),
        actions=[
            Action(
                name="filter_figma_artifacts_by_tags",
                kwargs={"tags": ["needs-review"]}
            ),
            Action(
                name="export_figma_artifacts_to_assets",
                kwargs={"artifact_ids": ["art_001", "art_007"], "export_profile": {"format": "PNG", "scale": "2x"}}
            ),
            Action(
                name="create_gmail_thread",
                kwargs={
                    "sender_email": "design-lead@company.com",
                    "recipients_emails": ["design-review@company.com", "ux-team@company.com"],
                    "workflow_type": "review",
                    "current_labels": ["design-review", "figma"]
                }
            ),
            Action(
                name="create_review_cycle",
                kwargs={"artifact_id": "art_001", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="create_review_cycle",
                kwargs={"artifact_id": "art_007", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="create_gmail_message",
                kwargs={
                    "sender_email": "design-lead@company.com",
                    "workflow_type": "review",
                    "thread_id": "thread_015",
                    "attachments_asset_ids": ["asset_art_001_png_2x", "asset_art_007_png_2x"]
                }
            )
        ],
        outputs=[
            {
                "filtered_artifacts": ["art_001", "art_007"],
                "exported_asset_ids": ["asset_art_001_png_2x", "asset_art_007_png_2x"],
                "gmail_thread_id": "thread_015",
                "review_cycle_ids": ["cycle_013", "cycle_014"],
                "gmail_message_id": "msg_017"
            }
        ]
    ),
    Task(
        annotator="0",
        user_id="task_002",
        instruction=(
            "You need to manage the review workflow for component library updates that require team coordination. "
            "You should target artifacts tagged with 'component' and prepare them for developer handoff. "
            "Your export format should be SVG at 1x scale for optimal development integration. You will be "
            "operating as 'ux-lead@company.com' with design-review@company.com and ux-team@company.com as "
            "recipients. You should apply 'components', 'design-system', and 'design-review' labels for "
            "proper categorization, and set NEEDS_REVIEW status for systematic tracking."
        ),
        actions=[
            Action(
                name="filter_figma_artifacts_by_tags",
                kwargs={"tags": ["component"]}
            ),
            Action(
                name="export_figma_artifacts_to_assets",
                kwargs={"artifact_ids": ["art_009", "art_011"], "export_profile": {"format": "SVG", "scale": "1x"}}
            ),
            Action(
                name="create_gmail_thread",
                kwargs={
                    "sender_email": "ux-lead@company.com",
                    "recipients_emails": ["design-review@company.com", "ux-team@company.com"],
                    "workflow_type": "review",
                    "current_labels": ["components", "design-system", "design-review"]
                }
            ),
            Action(
                name="create_review_cycle",
                kwargs={"artifact_id": "art_009", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="create_review_cycle",
                kwargs={"artifact_id": "art_011", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="create_gmail_message",
                kwargs={
                    "sender_email": "ux-lead@company.com",
                    "workflow_type": "review",
                    "thread_id": "thread_015",
                    "attachments_asset_ids": ["asset_art_009_svg_1x", "asset_art_011_svg_1x"]
                }
            )
        ],
        outputs=[
            {
                "filtered_artifacts": ["art_009", "art_011"],
                "exported_asset_ids": ["asset_art_009_svg_1x", "asset_art_011_svg_1x"],
                "gmail_thread_id": "thread_015",
                "review_cycle_ids": ["cycle_013", "cycle_014"],
                "gmail_message_id": "msg_017"
            }
        ]
    ),
    Task(
        annotator="0",
        user_id="task_003",
        instruction=(
            "You need to facilitate a comprehensive review process for mobile app interface updates requiring "
            "detailed evaluation. You should focus on 'mobile' tagged artifacts and prepare high-resolution "
            "documentation. Your export format should be PDF at 4x scale for detailed review documentation. "
            "You will be working as 'mobile-lead@company.com' with design-review@company.com and ux-team@company.com "
            "as recipients. You should use 'mobile', 'ux', and 'feedback' labels for thread organization, "
            "and ensure NEEDS_REVIEW status for comprehensive mobile design evaluation."
        ),
        actions=[
            Action(
                name="filter_figma_artifacts_by_tags",
                kwargs={"tags": ["mobile"]}
            ),
            Action(
                name="export_figma_artifacts_to_assets",
                kwargs={"artifact_ids": ["art_004", "art_012"], "export_profile": {"format": "PDF", "scale": "4x"}}
            ),
            Action(
                name="create_gmail_thread",
                kwargs={
                    "sender_email": "mobile-lead@company.com",
                    "recipients_emails": ["design-review@company.com", "ux-team@company.com"],
                    "workflow_type": "review",
                    "current_labels": ["mobile", "ux", "feedback"]
                }
            ),
            Action(
                name="create_review_cycle",
                kwargs={"artifact_id": "art_004", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="create_review_cycle",
                kwargs={"artifact_id": "art_012", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="create_gmail_message",
                kwargs={
                    "sender_email": "mobile-lead@company.com",
                    "workflow_type": "review",
                    "thread_id": "thread_015",
                    "attachments_asset_ids": ["asset_art_004_pdf_4x", "asset_art_012_pdf_4x"]
                }
            )
        ],
        outputs=[
            {
                "filtered_artifacts": ["art_004", "art_012"],
                "exported_asset_ids": ["asset_art_004_pdf_4x", "asset_art_012_pdf_4x"],
                "gmail_thread_id": "thread_015",
                "review_cycle_ids": ["cycle_013", "cycle_014"],
                "gmail_message_id": "msg_017"
            }
        ]
    ),
    Task(
        annotator="0",
        user_id="task_004",
        instruction=(
            "You need to coordinate a brand consistency review for header component standardization across the "
            "design system. You should target 'header' tagged artifacts and prepare them for visual consistency "
            "evaluation. Your export format should be JPG at 2x scale for detailed visual documentation. "
            "You will be operating as 'brand-lead@company.com' with design-review@company.com and ux-team@company.com "
            "as recipients. You should apply 'brand', 'guidelines', and 'design-review' labels to support the "
            "brand consistency initiative, and use NEEDS_REVIEW status for systematic evaluation."
        ),
        actions=[
            Action(
                name="filter_figma_artifacts_by_tags",
                kwargs={"tags": ["header"]}
            ),
            Action(
                name="export_figma_artifacts_to_assets",
                kwargs={"artifact_ids": ["art_002", "art_008"], "export_profile": {"format": "JPG", "scale": "2x"}}
            ),
            Action(
                name="create_gmail_thread",
                kwargs={
                    "sender_email": "brand-lead@company.com",
                    "recipients_emails": ["design-review@company.com", "ux-team@company.com"],
                    "workflow_type": "review",
                    "current_labels": ["brand", "guidelines", "design-review"]
                }
            ),
            Action(
                name="create_review_cycle",
                kwargs={"artifact_id": "art_002", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="create_review_cycle",
                kwargs={"artifact_id": "art_008", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="create_gmail_message",
                kwargs={
                    "sender_email": "brand-lead@company.com",
                    "workflow_type": "review",
                    "thread_id": "thread_015",
                    "attachments_asset_ids": ["asset_art_002_jpg_2x", "asset_art_008_jpg_2x"]
                }
            )
        ],
        outputs=[
            {
                "filtered_artifacts": ["art_002", "art_008"],
                "exported_asset_ids": ["asset_art_002_jpg_2x", "asset_art_008_jpg_2x"],
                "gmail_thread_id": "thread_015",
                "review_cycle_ids": ["cycle_013", "cycle_014"],
                "gmail_message_id": "msg_017"
            }
        ]
    ),
    Task(
        annotator="0",
        user_id="task_005",
        instruction=(
            "You need to oversee dashboard interface review preparation within the product development cycle. "
            "Your focus should be on 'dashboard' tagged artifacts for production readiness assessment. "
            "You should use PNG format at 1x scale for production documentation standards. Your role will be "
            "'product-lead@company.com' coordinating with design-review@company.com and ux-team@company.com. "
            "You should assign 'launch', 'admin', and 'approval' labels to facilitate the product review process, "
            "and establish NEEDS_REVIEW status for systematic evaluation before launch."
        ),
        actions=[
            Action(
                name="filter_figma_artifacts_by_tags",
                kwargs={"tags": ["dashboard"]}
            ),
            Action(
                name="export_figma_artifacts_to_assets",
                kwargs={"artifact_ids": ["art_004", "art_008"], "export_profile": {"format": "PNG", "scale": "1x"}}
            ),
            Action(
                name="create_gmail_thread",
                kwargs={
                    "sender_email": "product-lead@company.com",
                    "recipients_emails": ["design-review@company.com", "ux-team@company.com"],
                    "workflow_type": "review",
                    "current_labels": ["launch", "admin", "approval"]
                }
            ),
            Action(
                name="create_review_cycle",
                kwargs={"artifact_id": "art_004", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="create_review_cycle",
                kwargs={"artifact_id": "art_008", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="create_gmail_message",
                kwargs={
                    "sender_email": "product-lead@company.com",
                    "workflow_type": "review",
                    "thread_id": "thread_015",
                    "attachments_asset_ids": ["asset_art_004_png_1x", "asset_art_008_png_1x"]
                }
            )
        ],
        outputs=[
            {
                "filtered_artifacts": ["art_004", "art_008"],
                "exported_asset_ids": ["asset_art_004_png_1x", "asset_art_008_png_1x"],
                "gmail_thread_id": "thread_015",
                "review_cycle_ids": ["cycle_013", "cycle_014"],
                "gmail_message_id": "msg_017"
            }
        ]
    ),
    Task(
        annotator="0",
        user_id="task_006",
        instruction=(
            "You need to coordinate a pricing page optimization initiative to improve conversion rates. "
            "Your target should be 'pricing' tagged artifacts for revenue optimization evaluation. "
            "You should export them as SVG assets at 4x scale for high-resolution vector implementation. "
            "Your coordination role will be 'conversion-lead@company.com' working with design-review@company.com "
            "and ux-team@company.com. You should apply 'marketing', 'pricing', and 'approval' labels to "
            "support the revenue optimization campaign, and use NEEDS_REVIEW status for systematic assessment."
        ),
        actions=[
            Action(
                name="filter_figma_artifacts_by_tags",
                kwargs={"tags": ["pricing"]}
            ),
            Action(
                name="export_figma_artifacts_to_assets",
                kwargs={"artifact_ids": ["art_007"], "export_profile": {"format": "SVG", "scale": "4x"}}
            ),
            Action(
                name="create_gmail_thread",
                kwargs={
                    "sender_email": "conversion-lead@company.com",
                    "recipients_emails": ["design-review@company.com", "ux-team@company.com"],
                    "workflow_type": "review",
                    "current_labels": ["marketing", "pricing", "approval"]
                }
            ),
            Action(
                name="create_review_cycle",
                kwargs={"artifact_id": "art_007", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="create_gmail_message",
                kwargs={
                    "sender_email": "conversion-lead@company.com",
                    "workflow_type": "review",
                    "thread_id": "thread_015",
                    "attachments_asset_ids": ["asset_art_007_svg_4x"]
                }
            )
        ],
        outputs=[
            {
                "filtered_artifacts": ["art_007"],
                "exported_asset_ids": ["asset_art_007_svg_4x"],
                "gmail_thread_id": "thread_015",
                "review_cycle_ids": ["cycle_013"],
                "gmail_message_id": "msg_017"
            }
        ]
    ),
    Task(
        annotator="0",
        user_id="task_007",
        instruction=(
            "You need to manage navigation system standardization across the platform for improved information "
            "architecture. Your focus should be on 'navigation' tagged artifacts for consistency evaluation. "
            "You should export them as PDF assets at 2x scale for documentation and developer handoff. "
            "Your coordination role will be 'ui-lead@company.com' working with design-review@company.com "
            "and ux-team@company.com. You should apply 'navigation', 'design-system', and 'responsive' labels "
            "to facilitate the information architecture initiative, and use NEEDS_REVIEW status for systematic review."
        ),
        actions=[
            Action(
                name="filter_figma_artifacts_by_tags",
                kwargs={"tags": ["navigation"]}
            ),
            Action(
                name="export_figma_artifacts_to_assets",
                kwargs={"artifact_ids": ["art_002"], "export_profile": {"format": "PDF", "scale": "2x"}}
            ),
            Action(
                name="create_gmail_thread",
                kwargs={
                    "sender_email": "ui-lead@company.com",
                    "recipients_emails": ["design-review@company.com", "ux-team@company.com"],
                    "workflow_type": "review",
                    "current_labels": ["navigation", "design-system", "responsive"]
                }
            ),
            Action(
                name="create_review_cycle",
                kwargs={"artifact_id": "art_002", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="create_gmail_message",
                kwargs={
                    "sender_email": "ui-lead@company.com",
                    "workflow_type": "review",
                    "thread_id": "thread_015",
                    "attachments_asset_ids": ["asset_art_002_pdf_2x"]
                }
            )
        ],
        outputs=[
            {
                "filtered_artifacts": ["art_002"],
                "exported_asset_ids": ["asset_art_002_pdf_2x"],
                "gmail_thread_id": "thread_015",
                "review_cycle_ids": ["cycle_013"],
                "gmail_message_id": "msg_017"
            }
        ]
    ),
    Task(
        annotator="0",
        user_id="task_008",
        instruction=(
            "You need to conduct a brand identity consistency audit to ensure brand standards compliance. "
            "Your focus should be on 'brand' tagged artifacts for comprehensive brand evaluation. "
            "You should export them as JPG assets at 1x scale for brand compliance documentation. "
            "Your coordination role will be 'brand-manager@company.com' working with design-review@company.com "
            "and ux-team@company.com. You should apply 'brand', 'audit', and 'guidelines' labels to "
            "support the brand compliance initiative, and use NEEDS_REVIEW status for systematic assessment."
        ),
        actions=[
            Action(
                name="filter_figma_artifacts_by_tags",
                kwargs={"tags": ["brand"]}
            ),
            Action(
                name="export_figma_artifacts_to_assets",
                kwargs={"artifact_ids": ["art_010"], "export_profile": {"format": "JPG", "scale": "1x"}}
            ),
            Action(
                name="create_gmail_thread",
                kwargs={
                    "sender_email": "brand-manager@company.com",
                    "recipients_emails": ["design-review@company.com", "ux-team@company.com"],
                    "workflow_type": "review",
                    "current_labels": ["brand", "audit", "guidelines"]
                }
            ),
            Action(
                name="create_review_cycle",
                kwargs={"artifact_id": "art_010", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="create_gmail_message",
                kwargs={
                    "sender_email": "brand-manager@company.com",
                    "workflow_type": "review",
                    "thread_id": "thread_015",
                    "attachments_asset_ids": ["asset_art_010_jpg_1x"]
                }
            )
        ],
        outputs=[
            {
                "filtered_artifacts": ["art_010"],
                "exported_asset_ids": ["asset_art_010_jpg_1x"],
                "gmail_thread_id": "thread_015",
                "review_cycle_ids": ["cycle_013"],
                "gmail_message_id": "msg_017"
            }
        ]
    ),
    Task(
        annotator="0",
        user_id="task_009",
        instruction=(
            "You need to coordinate a comprehensive review process for hero section components that will "
            "impact landing page conversion rates. Your target should be 'hero' tagged artifacts for "
            "optimization evaluation. You should export them using PDF format at 4x scale for "
            "high-quality print documentation. Your coordination role will be 'marketing-lead@company.com' "
            "working with design-review@company.com and ux-team@company.com. You should apply 'marketing', "
            "'urgent', and 'responsive' labels to facilitate the landing page design review, and use "
            "NEEDS_REVIEW status for systematic evaluation emphasizing hero section optimization importance."
        ),
        actions=[
            Action(
                name="filter_figma_artifacts_by_tags",
                kwargs={"tags": ["hero"]}
            ),
            Action(
                name="export_figma_artifacts_to_assets",
                kwargs={"artifact_ids": ["art_001"], "export_profile": {"format": "PDF", "scale": "4x"}}
            ),
            Action(
                name="create_gmail_thread",
                kwargs={
                    "sender_email": "marketing-lead@company.com",
                    "recipients_emails": ["design-review@company.com", "ux-team@company.com"],
                    "workflow_type": "review",
                    "current_labels": ["marketing", "urgent", "responsive"]
                }
            ),
            Action(
                name="create_review_cycle",
                kwargs={"artifact_id": "art_001", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="create_gmail_message",
                kwargs={
                    "sender_email": "marketing-lead@company.com",
                    "workflow_type": "review",
                    "thread_id": "thread_015",
                    "attachments_asset_ids": ["asset_art_001_pdf_4x"]
                }
            )
        ],
        outputs=[
            {
                "filtered_artifacts": ["art_001"],
                "exported_asset_ids": ["asset_art_001_pdf_4x"],
                "gmail_thread_id": "thread_015",
                "review_cycle_ids": ["cycle_013"],
                "gmail_message_id": "msg_017"
            }
        ]
    ),
    Task(
        annotator="0",
        user_id="task_010",
        instruction=(
            "You need to manage a comprehensive review process for user profile interface components with "
            "focus on accessibility standards and inclusive design. Your target should be 'profile' tagged "
            "artifacts for accessibility compliance evaluation. You should export them using SVG format at "
            "2x scale for scalable vector graphics suitable for web implementation. Your coordination role "
            "will be 'accessibility-lead@company.com' working with design-review@company.com and ux-team@company.com. "
            "You should apply 'accessibility', 'profile', and 'ux' labels to ensure compliance with accessibility "
            "standards, and use NEEDS_REVIEW status for systematic evaluation highlighting inclusive design importance."
        ),
        actions=[
            Action(
                name="filter_figma_artifacts_by_tags",
                kwargs={"tags": ["profile"]}
            ),
            Action(
                name="export_figma_artifacts_to_assets",
                kwargs={"artifact_ids": ["art_005"], "export_profile": {"format": "SVG", "scale": "2x"}}
            ),
            Action(
                name="create_gmail_thread",
                kwargs={
                    "sender_email": "accessibility-lead@company.com",
                    "recipients_emails": ["design-review@company.com", "ux-team@company.com"],
                    "workflow_type": "review",
                    "current_labels": ["accessibility", "profile", "ux"]
                }
            ),
            Action(
                name="create_review_cycle",
                kwargs={"artifact_id": "art_005", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="create_gmail_message",
                kwargs={
                    "sender_email": "accessibility-lead@company.com",
                    "workflow_type": "review",
                    "thread_id": "thread_015",
                    "attachments_asset_ids": ["asset_art_005_svg_2x"]
                }
            )
        ],
        outputs=[
            {
                "filtered_artifacts": ["art_005"],
                "exported_asset_ids": ["asset_art_005_svg_2x"],
                "gmail_thread_id": "thread_015",
                "review_cycle_ids": ["cycle_013"],
                "gmail_message_id": "msg_017"
            }
        ]
    ),
    Task(
        annotator="0",
        user_id="task_011",
        instruction=(
            "You need to process comprehensive design approval feedback from multiple stakeholders and "
            "finalize the approval workflow for hero section components requiring immediate attention. "
            "You should identify hero-tagged artifacts that need approval processing and ensure proper "
            "bidirectional feedback tracking by synchronizing Gmail message 'msg_002' with artifact "
            "'art_001' for seamless collaboration between email and design platforms. The review cycle "
            "'cycle_001' requires status update to APPROVED to signal implementation readiness to the "
            "development team. You must create a formal review approval record using approver email "
            "'mike.ux@company.com' to document the design approval and maintain complete audit trail "
            "for governance, ensuring compliance with project management requirements and stakeholder "
            "accountability for design decisions in the approval workflow."
        ),
        actions=[
            Action(
                name="filter_figma_artifacts_by_tags",
                kwargs={"tags": ["hero"]}
            ),
            Action(
                name="create_figma_comment_from_gmail_message",
                kwargs={"artifact_id": "art_001", "gmail_message_id": "msg_002"}
            ),
            Action(
                name="update_review_cycle_status",
                kwargs={"cycle_id": "cycle_001", "new_status": "APPROVED"}
            ),
            Action(
                name="create_review_approval",
                kwargs={"cycle_id": "cycle_001", "approver_email": "mike.ux@company.com"}
            )
        ],
        outputs=[
            {
                "filtered_artifacts": ["art_001"],
                "figma_comment_id": "comment_019",
                "updated_cycle_id": "cycle_001",
                "previous_status": "NEEDS_REVIEW",
                "new_status": "APPROVED",
                "approval_id": "approval_012"
            }
        ]
    ),
    Task(
        annotator="0",
        user_id="task_012",
        instruction=(
            "You need to process feedback for pricing page components requiring changes. First filter "
            "components tagged 'pricing', then sync Gmail message 'msg_004' to artifact 'art_007', "
            "update cycle 'cycle_003' status to CHANGES_REQUESTED, and create approval record with "
            "approver 'lisa.marketing@company.com'."
        ),
        actions=[
            Action(
                name="filter_figma_artifacts_by_tags",
                kwargs={"tags": ["pricing"]}
            ),
            Action(
                name="create_figma_comment_from_gmail_message",
                kwargs={"artifact_id": "art_007", "gmail_message_id": "msg_004"}
            ),
            Action(
                name="update_review_cycle_status",
                kwargs={"cycle_id": "cycle_003", "new_status": "CHANGES_REQUESTED"}
            ),
            Action(
                name="create_review_approval",
                kwargs={"cycle_id": "cycle_003", "approver_email": "lisa.marketing@company.com"}
            )
        ],
        outputs=[
            {
                "filtered_artifacts": ["art_007"],
                "figma_comment_id": "comment_019",
                "updated_cycle_id": "cycle_003",
                "previous_status": "CHANGES_REQUESTED",
                "new_status": "CHANGES_REQUESTED",
                "approval_id": "approval_012"
            }
        ]
    ),
    Task(
        annotator="0",
        user_id="task_013",
        instruction=(
            "You're handling critical approval for mobile design components requiring immediate "
            "stakeholder sign-off to meet sprint deadlines. Export approved mobile components in "
            "PNG format at 2x scale for developer handoff, review and address comprehensive "
            "accessibility feedback from 'msg_005' regarding color contrast, ARIA compliance, "
            "and keyboard navigation issues for mobile component 'art_002', update review "
            "'cycle_008' to APPROVED status to finalize the mobile component review and enable "
            "developer implementation, and record formal approval from 'alex.dev@company.com' "
            "to proceed with production deployment across all mobile touchpoints."
        ),
        actions=[
            Action(
                name="export_figma_artifacts_to_assets",
                kwargs={"artifact_ids": ["art_002"], "export_profile": {"format": "PNG", "scale": "2x"}}
            ),
            Action(
                name="create_figma_comment_from_gmail_message",
                kwargs={"artifact_id": "art_002", "gmail_message_id": "msg_005"}
            ),
            Action(
                name="update_review_cycle_status",
                kwargs={"cycle_id": "cycle_008", "new_status": "APPROVED"}
            ),
            Action(
                name="create_review_approval",
                kwargs={"cycle_id": "cycle_008", "approver_email": "alex.dev@company.com"}
            )
        ],
        outputs=[
            {
                "exported_asset_ids": ["asset_art_002_png_2x"],
                "figma_comment_id": "comment_019",
                "updated_cycle_id": "cycle_008",
                "previous_status": "NEEDS_REVIEW",
                "new_status": "APPROVED",
                "approval_id": "approval_012"
            }
        ]
    ),
    Task(
        annotator="0",
        user_id="task_014",
        instruction=(
            "You're finalizing critical brand guideline components that require immediate revision "
            "and stakeholder escalation. First review artifacts tagged 'brand' and 'guidelines' to identify guideline updates, "
            "then address comprehensive feedback from 'msg_006' regarding brand consistency issues, "
            "escalate 'cycle_010' to ESCALATED status due to missed deadline and "
            "stakeholder concerns, and document formal approval from 'emma.brand@company.com' to "
            "proceed with emergency brand updates and implementation across all product touchpoints."
        ),
        actions=[
            Action(
                name="filter_figma_artifacts_by_tags",
                kwargs={"tags": ["brand", "guidelines"]}
            ),
            Action(
                name="create_figma_comment_from_gmail_message",
                kwargs={"artifact_id": "art_010", "gmail_message_id": "msg_006"}
            ),
            Action(
                name="update_review_cycle_status",
                kwargs={"cycle_id": "cycle_010", "new_status": "ESCALATED"}
            ),
            Action(
                name="create_review_approval",
                kwargs={"cycle_id": "cycle_010", "approver_email": "emma.brand@company.com"}
            )
        ],
        outputs=[
            {
                "filtered_artifacts": ["art_010"],
                "figma_comment_id": "comment_019",
                "updated_cycle_id": "cycle_010",
                "previous_status": "APPROVED",
                "new_status": "ESCALATED",
                "approval_id": "approval_012"
            }
        ]
    ),
    Task(
        annotator="0",
        user_id="task_015",
        instruction=(
            "You're wrapping up component library updates with UX feedback. Filter artifacts "
            "specifically tagged with 'components', export them in SVG format at 1x scale for "
            "development compatibility, incorporate insights from 'msg_003' into 'art_006', "
            "transition 'cycle_009' to APPROVED, and secure sign-off from 'mike.ux@company.com'."
        ),
        actions=[
            Action(
                name="filter_figma_artifacts_by_tags",
                kwargs={"tags": ["components"]}
            ),
            Action(
                name="export_figma_artifacts_to_assets",
                kwargs={"artifact_ids": ["art_003"], "export_profile": {"format": "SVG", "scale": "1x"}}
            ),
            Action(
                name="create_figma_comment_from_gmail_message",
                kwargs={"artifact_id": "art_006", "gmail_message_id": "msg_003"}
            ),
            Action(
                name="update_review_cycle_status",
                kwargs={"cycle_id": "cycle_009", "new_status": "APPROVED"}
            ),
            Action(
                name="create_review_approval",
                kwargs={"cycle_id": "cycle_009", "approver_email": "mike.ux@company.com"}
            )
        ],
        outputs=[
            {
                "filtered_artifacts": ["art_003"],
                "exported_asset_ids": ["asset_art_003_svg_1x"],
                "figma_comment_id": "comment_019",
                "updated_cycle_id": "cycle_009",
                "previous_status": "IN_FLIGHT",
                "new_status": "APPROVED",
                "approval_id": "approval_012"
            }
        ]
    ),
    Task(
        annotator="0",
        user_id="task_016",
        instruction=(
            "You're alex.dev@company.com, launching admin interface reviews for the dev team. Filter "
            "artifacts tagged with 'admin' to target admin panel components, export as PDF at 1x scale "
            "for documentation clarity, notify design and UX teams with 'admin' and 'review' labels, "
            "and track progress with NEEDS_REVIEW status."
        ),
        actions=[
            Action(
                name="filter_figma_artifacts_by_tags",
                kwargs={"tags": ["admin"]}
            ),
            Action(
                name="export_figma_artifacts_to_assets",
                kwargs={"artifact_ids": ["art_008"], "export_profile": {"format": "PDF", "scale": "1x"}}
            ),
            Action(
                name="create_gmail_thread",
                kwargs={
                    "sender_email": "alex.dev@company.com",
                    "recipients_emails": ["design-review@company.com", "ux-team@company.com"],
                    "workflow_type": "review",
                    "current_labels": ["admin", "review"]
                }
            ),
            Action(
                name="create_review_cycle",
                kwargs={"artifact_id": "art_008", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="create_gmail_message",
                kwargs={
                    "sender_email": "alex.dev@company.com",
                    "workflow_type": "review",
                    "thread_id": "thread_015",
                    "attachments_asset_ids": ["asset_art_008_pdf_1x"]
                }
            )
        ],
        outputs=[
            {
                "filtered_artifacts": ["art_008"],
                "exported_asset_ids": ["asset_art_008_pdf_1x"],
                "thread_id": "thread_015",
                "cycle_id": "cycle_013",
                "message_id": "msg_017"
            }
        ]
    ),
    Task(
        annotator="0",
        user_id="task_017",
        instruction=(
            "You're managing marketing campaign assets as marketing.lead@company.com. Filter artifacts "
            "specifically tagged with 'marketing', export them in SVG format at 1x scale for web "
            "compatibility, coordinate with design and UX teams using 'marketing' and 'launch' labels, "
            "and establish review tracking with NEEDS_REVIEW status."
        ),
        actions=[
            Action(
                name="filter_figma_artifacts_by_tags",
                kwargs={"tags": ["marketing"]}
            ),
            Action(
                name="export_figma_artifacts_to_assets",
                kwargs={"artifact_ids": ["art_006"], "export_profile": {"format": "SVG", "scale": "1x"}}
            ),
            Action(
                name="create_gmail_thread",
                kwargs={
                    "sender_email": "marketing.lead@company.com",
                    "recipients_emails": ["design-review@company.com", "ux-team@company.com"],
                    "workflow_type": "review",
                    "current_labels": ["marketing", "launch"]
                }
            ),
            Action(
                name="create_review_cycle",
                kwargs={"artifact_id": "art_006", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="create_gmail_message",
                kwargs={
                    "sender_email": "marketing.lead@company.com",
                    "workflow_type": "review",
                    "thread_id": "thread_015",
                    "attachments_asset_ids": ["asset_art_006_svg_1x"]
                }
            )
        ],
        outputs=[
            {
                "filtered_artifacts": ["art_006"],
                "exported_asset_ids": ["asset_art_006_svg_1x"],
                "thread_id": "thread_015",
                "cycle_id": "cycle_013",
                "message_id": "msg_017"
            }
        ]
    ),
    Task(
        annotator="0",
        user_id="task_018",
        instruction=(
            "You're coordinating component library reviews as design.systems@company.com. Filter "
            "artifacts tagged with 'component' to target all component library items, generate PNG "
            "assets at 4x scale for high-resolution development handoff, communicate with design "
            "and UX teams using 'components' and 'library' labels, and initiate tracking with "
            "NEEDS_REVIEW status."
        ),
        actions=[
            Action(
                name="filter_figma_artifacts_by_tags",
                kwargs={"tags": ["component"]}
            ),
            Action(
                name="export_figma_artifacts_to_assets",
                kwargs={"artifact_ids": ["art_009", "art_011"], "export_profile": {"format": "PNG", "scale": "4x"}}
            ),
            Action(
                name="create_gmail_thread",
                kwargs={
                    "sender_email": "design.systems@company.com",
                    "recipients_emails": ["design-review@company.com", "ux-team@company.com"],
                    "workflow_type": "review",
                    "current_labels": ["components", "library"]
                }
            ),
            Action(
                name="create_review_cycle",
                kwargs={"artifact_id": "art_009", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="create_review_cycle",
                kwargs={"artifact_id": "art_011", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="create_gmail_message",
                kwargs={
                    "sender_email": "design.systems@company.com",
                    "workflow_type": "review",
                    "thread_id": "thread_015",
                    "attachments_asset_ids": ["asset_art_009_png_4x", "asset_art_011_png_4x"]
                }
            )
        ],
        outputs=[
            {
                "filtered_artifacts": ["art_009", "art_011"],
                "exported_asset_ids": ["asset_art_009_png_4x", "asset_art_011_png_4x"],
                "thread_id": "thread_015",
                "cycle_id_1": "cycle_013",
                "cycle_id_2": "cycle_014",
                "message_id": "msg_017"
            }
        ]
    ),
    Task(
        annotator="0",
        user_id="task_019",
        instruction=(
            "You're coordinating a comprehensive form component evaluation as forms.lead@company.com. "
            "Focus on interactive form elements that need stakeholder validation for user experience "
            "optimization. Export components in PDF format at 1x scale for detailed documentation "
            "review. Coordinate with design and UX teams using 'component' and 'review' labels, and "
            "establish proper review tracking with NEEDS_REVIEW status for thorough evaluation."
        ),
        actions=[
            Action(
                name="filter_figma_artifacts_by_tags",
                kwargs={"tags": ["form"]}
            ),
            Action(
                name="export_figma_artifacts_to_assets",
                kwargs={"artifact_ids": ["art_011"], "export_profile": {"format": "PDF", "scale": "1x"}}
            ),
            Action(
                name="create_gmail_thread",
                kwargs={
                    "sender_email": "forms.lead@company.com",
                    "recipients_emails": ["design-review@company.com", "ux-team@company.com"],
                    "workflow_type": "review",
                    "current_labels": ["component", "review"]
                }
            ),
            Action(
                name="create_review_cycle",
                kwargs={"artifact_id": "art_011", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="create_gmail_message",
                kwargs={
                    "sender_email": "forms.lead@company.com",
                    "workflow_type": "review",
                    "thread_id": "thread_015",
                    "attachments_asset_ids": ["asset_art_011_pdf_1x"]
                }
            )
        ],
        outputs=[
            {
                "filtered_artifacts": ["art_011"],
                "exported_asset_ids": ["asset_art_011_pdf_1x"],
                "thread_id": "thread_015",
                "cycle_id": "cycle_013",
                "message_id": "msg_017"
            }
        ]
    ),
    Task(
        annotator="0",
        user_id="task_020",
        instruction=(
            "You're reviewing user settings and profile interfaces as settings.lead@company.com. "
            "Focus on settings-related artifacts that need SVG exports at 2x scale for crisp "
            "interface rendering, coordinate with design and UX teams using 'profile' and "
            "'ux' labels for proper categorization, and establish NEEDS_REVIEW status "
            "to track evaluation progress."
        ),
        actions=[
            Action(
                name="filter_figma_artifacts_by_tags",
                kwargs={"tags": ["settings"]}
            ),
            Action(
                name="export_figma_artifacts_to_assets",
                kwargs={"artifact_ids": ["art_005", "art_012"], "export_profile": {"format": "SVG", "scale": "2x"}}
            ),
            Action(
                name="create_gmail_thread",
                kwargs={
                    "sender_email": "settings.lead@company.com",
                    "recipients_emails": ["design-review@company.com", "ux-team@company.com"],
                    "workflow_type": "review",
                    "current_labels": ["profile", "ux"]
                }
            ),
            Action(
                name="create_review_cycle",
                kwargs={"artifact_id": "art_005", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="create_review_cycle",
                kwargs={"artifact_id": "art_012", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="create_gmail_message",
                kwargs={
                    "sender_email": "settings.lead@company.com",
                    "workflow_type": "review",
                    "thread_id": "thread_015",
                    "attachments_asset_ids": ["asset_art_005_svg_2x", "asset_art_012_svg_2x"]
                }
            )
        ],
        outputs=[
            {
                "filtered_artifacts": ["art_005", "art_012"],
                "exported_asset_ids": ["asset_art_005_svg_2x", "asset_art_012_svg_2x"],
                "thread_id": "thread_015",
                "cycle_id_1": "cycle_013",
                "cycle_id_2": "cycle_014",
                "message_id": "msg_017"
            }
        ]
    ),
    Task(
        annotator="0",
        user_id="task_021",
        instruction=(
            "You're managing design system token documentation as tokens.lead@company.com. "
            "Filter Figma artifacts specifically tagged with 'tokens' to target design artifacts "
            "with token specifications that require PDF export at 1x scale for documentation clarity, "
            "collaborate with design and UX teams using 'design-system' and 'components' labels for "
            "systematic organization, and establish NEEDS_REVIEW status for comprehensive token validation."
        ),
        actions=[
            Action(
                name="filter_figma_artifacts_by_tags",
                kwargs={"tags": ["tokens"]}
            ),
            Action(
                name="export_figma_artifacts_to_assets",
                kwargs={"artifact_ids": ["art_003"], "export_profile": {"format": "PDF", "scale": "1x"}}
            ),
            Action(
                name="create_gmail_thread",
                kwargs={
                    "sender_email": "tokens.lead@company.com",
                    "recipients_emails": ["design-review@company.com", "ux-team@company.com"],
                    "workflow_type": "review",
                    "current_labels": ["design-system", "components"]
                }
            ),
            Action(
                name="create_review_cycle",
                kwargs={"artifact_id": "art_003", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="create_gmail_message",
                kwargs={
                    "sender_email": "tokens.lead@company.com",
                    "workflow_type": "review",
                    "thread_id": "thread_015",
                    "attachments_asset_ids": ["asset_art_003_pdf_1x"]
                }
            )
        ],
        outputs=[
            {
                "filtered_artifacts": ["art_003"],
                "exported_asset_ids": ["asset_art_003_pdf_1x"],
                "thread_id": "thread_015",
                "cycle_id": "cycle_013",
                "message_id": "msg_017"
            }
        ]
    ),
    Task(
        annotator="0",
        user_id="task_022",
        instruction=(
            "You need to facilitate a design review for administrative dashboard components that require "
            "stakeholder approval. Your focus should be on artifacts tagged with 'admin' and 'dashboard' "
            "to ensure consistent administrative interface design. You should export these designs as "
            "SVG format at 2x scale to maintain scalability and crisp quality for developer handoff. Working as "
            "'admin-reviewer@company.com', you'll coordinate with design-review@company.com and "
            "ux-team@company.com recipients. Your Gmail thread should be organized with 'admin' and "
            "'design-review' labels, and you need to establish NEEDS_REVIEW status for proper "
            "review cycle tracking."
        ),
        actions=[
            Action(
                name="filter_figma_artifacts_by_tags",
                kwargs={"tags": ["admin", "dashboard"]}
            ),
            Action(
                name="export_figma_artifacts_to_assets",
                kwargs={"artifact_ids": ["art_008"], "export_profile": {"format": "SVG", "scale": "2x"}}
            ),
            Action(
                name="create_gmail_thread",
                kwargs={
                    "sender_email": "admin-reviewer@company.com",
                    "recipients_emails": ["design-review@company.com", "ux-team@company.com"],
                    "workflow_type": "review",
                    "current_labels": ["admin", "design-review"]
                }
            ),
            Action(
                name="create_review_cycle",
                kwargs={"artifact_id": "art_008", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="create_gmail_message",
                kwargs={
                    "sender_email": "admin-reviewer@company.com",
                    "workflow_type": "review",
                    "thread_id": "thread_015",
                    "attachments_asset_ids": ["asset_art_008_svg_2x"]
                }
            )
        ],
        outputs=[
            {
                "filtered_artifacts": ["art_008"],
                "exported_asset_ids": ["asset_art_008_svg_2x"],
                "gmail_thread_id": "thread_015",
                "review_cycle_ids": ["cycle_013"],
                "gmail_message_id": "msg_017"
            }
        ]
    ),
    Task(
        annotator="0",
        user_id="task_023",
        instruction=(
            "You need to initiate a comprehensive review process for data visualization components that "
            "require stakeholder validation. Your attention should be directed toward artifacts tagged "
            "with 'table' to ensure consistent data presentation standards across the platform. You "
            "should generate high-resolution JPG exports at 4x scale for detailed component inspection "
            "and documentation purposes. Operating as 'data-reviewer@company.com', you'll collaborate "
            "with design-review@company.com and ux-team@company.com recipients to gather comprehensive "
            "feedback. Your communication thread should be categorized with 'data-table' and 'component' "
            "labels for systematic organization, and you must establish NEEDS_REVIEW status to initiate "
            "the formal review cycle."
        ),
        actions=[
            Action(
                name="filter_figma_artifacts_by_tags",
                kwargs={"tags": ["table"]}
            ),
            Action(
                name="export_figma_artifacts_to_assets",
                kwargs={"artifact_ids": ["art_009"], "export_profile": {"format": "JPG", "scale": "4x"}}
            ),
            Action(
                name="create_gmail_thread",
                kwargs={
                    "sender_email": "data-reviewer@company.com",
                    "recipients_emails": ["design-review@company.com", "ux-team@company.com"],
                    "workflow_type": "review",
                    "current_labels": ["data-table", "component"]
                }
            ),
            Action(
                name="create_review_cycle",
                kwargs={"artifact_id": "art_009", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="create_gmail_message",
                kwargs={
                    "sender_email": "data-reviewer@company.com",
                    "workflow_type": "review",
                    "thread_id": "thread_015",
                    "attachments_asset_ids": ["asset_art_009_jpg_4x"]
                }
            )
        ],
        outputs=[
            {
                "filtered_artifacts": ["art_009"],
                "exported_asset_ids": ["asset_art_009_jpg_4x"],
                "gmail_thread_id": "thread_015",
                "review_cycle_ids": ["cycle_013"],
                "gmail_message_id": "msg_017"
            }
        ]
    ),
    Task(
        annotator="0",
        user_id="task_024",
        instruction=(
            "You need to establish a thorough review process for responsive design components that "
            "require cross-device compatibility validation. Your focus should be on artifacts tagged "
            "with 'responsive' to ensure consistent user experience across multiple screen sizes and "
            "platforms. You should create standard-resolution PNG exports at 1x scale for baseline "
            "documentation and reference purposes. Working as 'responsive-lead@company.com', you'll "
            "engage with design-review@company.com and ux-team@company.com recipients to coordinate "
            "comprehensive responsive design evaluation. Your Gmail thread should be organized with "
            "'responsive' and 'design-review' labels for effective categorization, and you must "
            "initiate NEEDS_REVIEW status to begin the systematic review workflow."
        ),
        actions=[
            Action(
                name="filter_figma_artifacts_by_tags",
                kwargs={"tags": ["responsive"]}
            ),
            Action(
                name="export_figma_artifacts_to_assets",
                kwargs={"artifact_ids": ["art_001"], "export_profile": {"format": "PNG", "scale": "1x"}}
            ),
            Action(
                name="create_gmail_thread",
                kwargs={
                    "sender_email": "responsive-lead@company.com",
                    "recipients_emails": ["design-review@company.com", "ux-team@company.com"],
                    "workflow_type": "review",
                    "current_labels": ["responsive", "design-review"]
                }
            ),
            Action(
                name="create_review_cycle",
                kwargs={"artifact_id": "art_001", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="create_gmail_message",
                kwargs={
                    "sender_email": "responsive-lead@company.com",
                    "workflow_type": "review",
                    "thread_id": "thread_015",
                    "attachments_asset_ids": ["asset_art_001_png_1x"]
                }
            )
        ],
        outputs=[
            {
                "filtered_artifacts": ["art_001"],
                "exported_asset_ids": ["asset_art_001_png_1x"],
                "gmail_thread_id": "thread_015",
                "review_cycle_ids": ["cycle_013"],
                "gmail_message_id": "msg_017"
            }
        ]
    ),
    Task(
        annotator="0",
        user_id="task_025",
        instruction=(
            "You need to orchestrate a detailed review process for landing page components that "
            "require responsive design validation across multiple breakpoints. Your concentration "
            "should be on artifacts tagged with both 'landing-page' and 'responsive' to ensure "
            "optimal conversion experiences across all device types and screen resolutions. You "
            "should produce high-quality JPG exports at 2x scale for comprehensive visual assessment "
            "and stakeholder presentation. Operating as 'conversion-lead@company.com', you'll "
            "coordinate with design-review@company.com and ux-team@company.com recipients to gather "
            "strategic feedback on conversion optimization. Your communication thread should be "
            "systematically labeled with 'marketing' and 'responsive' tags for effective project "
            "tracking, and you must establish NEEDS_REVIEW status to activate the comprehensive "
            "evaluation process."
        ),
        actions=[
            Action(
                name="filter_figma_artifacts_by_tags",
                kwargs={"tags": ["landing-page", "responsive"]}
            ),
            Action(
                name="export_figma_artifacts_to_assets",
                kwargs={"artifact_ids": ["art_001"], "export_profile": {"format": "JPG", "scale": "2x"}}
            ),
            Action(
                name="create_gmail_thread",
                kwargs={
                    "sender_email": "conversion-lead@company.com",
                    "recipients_emails": ["design-review@company.com", "ux-team@company.com"],
                    "workflow_type": "review",
                    "current_labels": ["marketing", "responsive"]
                }
            ),
            Action(
                name="create_review_cycle",
                kwargs={"artifact_id": "art_001", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="create_gmail_message",
                kwargs={
                    "sender_email": "conversion-lead@company.com",
                    "workflow_type": "review",
                    "thread_id": "thread_015",
                    "attachments_asset_ids": ["asset_art_001_jpg_2x"]
                }
            )
        ],
        outputs=[
            {
                "filtered_artifacts": ["art_001"],
                "exported_asset_ids": ["asset_art_001_jpg_2x"],
                "gmail_thread_id": "thread_015",
                "review_cycle_ids": ["cycle_013"],
                "gmail_message_id": "msg_017"
            }
        ]
    ),
    Task(
        annotator="0",
        user_id="task_026",
        instruction=(
            "You need to orchestrate a comprehensive design release announcement for the latest system updates. "
            "You should focus on release_001 which contains significant design system enhancements. "
            "Your role involves validating this as a legitimate release version, analyzing what's changed since "
            "the previous iteration, and creating compelling before/after documentation. You'll be documenting "
            "key improvements including 'Enhanced component library', 'Improved accessibility standards', and "
            "'Updated design tokens'. Your communications should go as 'sarah.designer@company.com' to "
            "stakeholders at 'design-team@company.com' and 'product-leads@company.com' with appropriate "
            "'Design/Release' and 'design-system' labels for visibility. You should export hero frames using "
            "SVG format at 2x resolution for crisp scalable graphics."
        ),
        actions=[
            Action(
                name="detect_release_version",
                kwargs={"release_id": "release_001"}
            ),
            Action(
                name="compute_release_diffs",
                kwargs={
                    "release_id": "release_001",
                    "changelog_highlights": ["Enhanced component library", "Improved accessibility standards", "Updated design tokens"]
                }
            ),
            Action(
                name="save_release_diffs",
                kwargs={
                    "release_id": "release_001",
                    "prior_release_id_nullable": "release_006",
                    "frames_added": ["1:3", "1:4"],
                    "frames_updated": ["1:5"],
                    "frames_removed": [],
                    "component_version_bumps": ["HomepageHeroSection-v1.19", "NavigationBar-v1.13", "DesignSystem-v1.12", "ContactFormComponent-v1.20"],
                    "changelog_highlights": ["Enhanced component library", "Improved accessibility standards", "Updated design tokens"]
                }
            ),
            Action(
                name="filter_figma_artifacts_by_tags",
                kwargs={"tags": ["hero"]}
            ),
            Action(
                name="export_figma_artifacts_to_assets",
                kwargs={"artifact_ids": ["art_001"], "export_profile": {"format": "SVG", "scale": "2x"}}
            ),
            Action(
                name="generate_before_after_visuals",
                kwargs={
                    "release_id": "release_001",
                    "hero_artifact_ids": ["art_001"]
                }
            ),
            Action(
                name="create_gmail_thread",
                kwargs={
                    "sender_email": "sarah.designer@company.com",
                    "recipients_emails": ["design-team@company.com", "product-leads@company.com"],
                    "workflow_type": "release",
                    "current_labels": ["Design/Release", "design-system"]
                }
            ),
            Action(
                name="create_gmail_message",
                kwargs={
                    "sender_email": "sarah.designer@company.com",
                    "workflow_type": "release",
                    "thread_id": "thread_015",
                    "attachments_asset_ids": ["asset_art_001_svg_2x"]
                }
            )
        ],
        outputs=[
            {
                "is_release_version": True,
                "computed_diffs": {
                    "prior_release_id_nullable": "release_006",
                    "frames_added": ["1:3", "1:4"],
                    "frames_updated": ["1:5"],
                    "component_version_bumps": ["HomepageHeroSection-v1.19", "NavigationBar-v1.13", "DesignSystem-v1.12", "ContactFormComponent-v1.20"]
                },
                "saved_diff_id": "diff_001",
                "hero_artifacts": ["art_001"],
                "exported_assets": ["asset_art_001_svg_2x"],
                "visual_name": "before_after_visual_release_001_5894",
                "gmail_thread_id": "thread_015",
                "gmail_message_id": "msg_017"
            }
        ]
    ),
    Task(
        annotator="0",
        user_id="task_027",
        instruction=(
            "You're tasked with announcing a major mobile application release that represents a significant "
            "milestone in user experience evolution. You should work with release_002 which encompasses "
            "comprehensive mobile interface improvements and user workflow enhancements. Your responsibility "
            "includes verifying this qualifies as an official release candidate, conducting thorough change "
            "analysis since the previous mobile iteration, and creating impactful visual documentation. "
            "You'll be highlighting critical improvements like 'Revolutionary dashboard redesign', "
            "'Enhanced user onboarding flow', 'Performance optimization features', and 'Advanced personalization options'. "
            "Your communications will originate from 'mike.ux@company.com' and reach key stakeholders including "
            "'mobile-team@company.com', 'product-strategy@company.com', and 'executive-leadership@company.com'. "
            "You should apply strategic labeling with 'Design/Release', 'mobile', and 'launch' for maximum "
            "organizational visibility. Your visual assets should utilize high-resolution PNG format for "
            "detailed interface documentation."
        ),
        actions=[
            Action(
                name="detect_release_version",
                kwargs={"release_id": "release_002"}
            ),
            Action(
                name="compute_release_diffs",
                kwargs={
                    "release_id": "release_002",
                    "changelog_highlights": ["Revolutionary dashboard redesign", "Enhanced user onboarding flow", "Performance optimization features", "Advanced personalization options"]
                }
            ),
            Action(
                name="save_release_diffs",
                kwargs={
                    "release_id": "release_002",
                    "prior_release_id_nullable": "release_007",
                    "frames_added": ["2:2"],
                    "frames_updated": ["2:3", "2:4"],
                    "frames_removed": [],
                    "component_version_bumps": ["MobileAppDashboard-v1.18", "UserProfileScreen-v1.17", "SettingsScreen-v1.14"],
                    "changelog_highlights": ["Revolutionary dashboard redesign", "Enhanced user onboarding flow", "Performance optimization features", "Advanced personalization options"]
                }
            ),
            Action(
                name="filter_figma_artifacts_by_tags",
                kwargs={"tags": ["hero"]}
            ),
            Action(
                name="export_figma_artifacts_to_assets",
                kwargs={"artifact_ids": ["art_001"], "export_profile": {"format": "PNG", "scale": "4x"}}
            ),
            Action(
                name="generate_before_after_visuals",
                kwargs={
                    "release_id": "release_002",
                    "hero_artifact_ids": ["art_001"]
                }
            ),
            Action(
                name="create_gmail_thread",
                kwargs={
                    "sender_email": "mike.ux@company.com",
                    "recipients_emails": ["mobile-team@company.com", "product-strategy@company.com", "executive-leadership@company.com"],
                    "workflow_type": "release",
                    "current_labels": ["Design/Release", "mobile", "launch"]
                }
            ),
            Action(
                name="create_gmail_message",
                kwargs={
                    "sender_email": "mike.ux@company.com",
                    "workflow_type": "release",
                    "thread_id": "thread_015",
                    "attachments_asset_ids": ["asset_art_001_png_4x"]
                }
            )
        ],
        outputs=[
            {
                "is_release_version": True,
                "computed_diffs": {
                    "prior_release_id_nullable": "release_007",
                    "frames_added": ["2:2"],
                    "frames_updated": ["2:3", "2:4"],
                    "component_version_bumps": ["MobileAppDashboard-v1.18", "UserProfileScreen-v1.17", "SettingsScreen-v1.14"]
                },
                "saved_diff_id": "diff_002",
                "hero_artifacts": ["art_001"],
                "exported_assets": ["asset_art_001_png_4x"],
                # "visual_name": "before_after_visual_release_002_0139",
                # "visual_name": "before_after_visual_release_002_3016",
                "visual_name": "before_after_visual_release_002_5894",
                "gmail_thread_id": "thread_015",
                "gmail_message_id": "msg_017"
            }
        ]
    ),
    Task(
        annotator="0",
        user_id="task_028",
        instruction=(
            "You need to orchestrate the final marketing website launch announcement, marking a crucial "
            "milestone for the company's digital presence. You're responsible for handling release_003, "
            "which represents the culmination of months of brand alignment and user experience refinements. "
            "Your mission involves validating this as the official v1.0.0 launch candidate, conducting "
            "comprehensive analysis of updates since the previous marketing iteration, and creating "
            "compelling launch documentation. You'll need to highlight the transformative improvements "
            "including 'New brand integration', 'Performance optimizations', 'Mobile responsive design', "
            "and 'Enhanced user experience'. Your announcement should originate from 'lisa.marketing@company.com' "
            "and reach key business stakeholders including 'executive-team@company.com', 'marketing-leads@company.com', "
            "and 'brand-partners@company.com' with strategic labeling using 'launch', 'marketing', and "
            "'brand' for maximum organizational impact. You should deliver high-quality hero visuals "
            "using PDF format at 1x scale to ensure professional presentation standards."
        ),
        actions=[
            Action(
                name="detect_release_version",
                kwargs={"release_id": "release_003"}
            ),
            Action(
                name="compute_release_diffs",
                kwargs={
                    "release_id": "release_003",
                    "changelog_highlights": ["New brand integration", "Performance optimizations", "Mobile responsive design", "Enhanced user experience"]
                }
            ),
            Action(
                name="save_release_diffs",
                kwargs={
                    "release_id": "release_003",
                    "prior_release_id_nullable": "release_008",
                    "frames_added": [],
                    "frames_updated": ["3:3"],
                    "frames_removed": [],
                    "component_version_bumps": ["MarketingWebsite-v1.16", "PricingPage-v1.11"],
                    "changelog_highlights": ["New brand integration", "Performance optimizations", "Mobile responsive design", "Enhanced user experience"]
                }
            ),
            Action(
                name="filter_figma_artifacts_by_tags",
                kwargs={"tags": ["hero"]}
            ),
            Action(
                name="export_figma_artifacts_to_assets",
                kwargs={"artifact_ids": ["art_001"], "export_profile": {"format": "PDF", "scale": "1x"}}
            ),
            Action(
                name="generate_before_after_visuals",
                kwargs={
                    "release_id": "release_003",
                    "hero_artifact_ids": ["art_001"]
                }
            ),
            Action(
                name="create_gmail_thread",
                kwargs={
                    "sender_email": "lisa.marketing@company.com",
                    "recipients_emails": ["executive-team@company.com", "marketing-leads@company.com", "brand-partners@company.com"],
                    "workflow_type": "release",
                    "current_labels": ["launch", "marketing", "brand"]
                }
            ),
            Action(
                name="create_gmail_message",
                kwargs={
                    "sender_email": "lisa.marketing@company.com",
                    "workflow_type": "release",
                    "thread_id": "thread_015",
                    "attachments_asset_ids": ["asset_art_001_pdf_1x"]
                }
            )
        ],
        outputs=[
            {
                "is_release_version": True,
                "computed_diffs": {
                    "prior_release_id_nullable": "release_008",
                    "frames_added": [],
                    "frames_updated": ["3:3"],
                    "component_version_bumps": ["MarketingWebsite-v1.16", "PricingPage-v1.11"]
                },
                "saved_diff_id": "diff_003",
                "hero_artifacts": ["art_001"],
                "exported_assets": ["asset_art_001_pdf_1x"],
                "visual_name": "before_after_visual_release_003_5894",
                "gmail_thread_id": "thread_015",
                "gmail_message_id": "msg_017"
            }
        ]
    ),
    Task(
        annotator="0",
        user_id="task_029",
        instruction=(
            "You are spearheading the comprehensive accessibility transformation for the admin panel, "
            "ensuring compliance with the highest standards while revolutionizing the user experience "
            "for all team members. Your oversight involves release_004, which represents a pivotal "
            "advancement toward universal design principles and regulatory adherence. You must validate "
            "this as the definitive v3.0.0 accessibility milestone, systematically analyze the "
            "comprehensive improvements spanning 'Enhanced accessibility compliance', 'WCAG 2.1 AA standards', "
            "'Improved screen reader support', and 'Keyboard navigation updates'. Since this represents "
            "a major architectural overhaul, you should note there is no prior release baseline to "
            "compare against (prior release ID will be null). Your communication strategy should engage critical stakeholders including "
            "'accessibility-team@company.com', 'design-review@company.com', and 'compliance-officer@company.com' "
            "through strategic correspondence initiated from 'alex.dev@company.com' with purposeful "
            "categorization using 'accessibility', 'launch', and 'admin' labels for maximum organizational "
            "transparency. You should ensure premium visual documentation using JPG format at 4x resolution "
            "to demonstrate compliance achievements effectively."
        ),
        actions=[
            Action(
                name="detect_release_version",
                kwargs={"release_id": "release_004"}
            ),
            Action(
                name="compute_release_diffs",
                kwargs={
                    "release_id": "release_004",
                    "changelog_highlights": ["Enhanced accessibility compliance", "WCAG 2.1 AA standards", "Improved screen reader support", "Keyboard navigation updates"]
                }
            ),
            Action(
                name="save_release_diffs",
                kwargs={
                    "release_id": "release_004",
                    "prior_release_id_nullable": None,
                    "frames_added": ["4:2", "4:3"],
                    "frames_updated": [],
                    "frames_removed": [],
                    "component_version_bumps": ["AdminPanelHeader-v1.16", "DataTableComponent-v1.18"],
                    "changelog_highlights": ["Enhanced accessibility compliance", "WCAG 2.1 AA standards", "Improved screen reader support", "Keyboard navigation updates"]
                }
            ),
            Action(
                name="filter_figma_artifacts_by_tags",
                kwargs={"tags": ["hero"]}
            ),
            Action(
                name="export_figma_artifacts_to_assets",
                kwargs={
                    "artifact_ids": ["art_001"],
                    "export_profile": {"format": "JPG", "scale": "4x"}
                }
            ),
            Action(
                name="generate_before_after_visuals",
                kwargs={
                    "release_id": "release_004",
                    "hero_artifact_ids": ["art_001"]
                }
            ),
            Action(
                name="create_gmail_thread",
                kwargs={
                    "sender_email": "alex.dev@company.com",
                    "recipients_emails": ["accessibility-team@company.com", "design-review@company.com", "compliance-officer@company.com"],
                    "workflow_type": "release",
                    "current_labels": ["accessibility", "launch", "admin"]
                }
            ),
            Action(
                name="create_gmail_message",
                kwargs={
                    "sender_email": "alex.dev@company.com",
                    "workflow_type": "release",
                    "thread_id": "thread_015",
                    "attachments_asset_ids": ["asset_art_001_jpg_4x"]
                }
            )
        ],
        outputs=[{
            "release_detected": {
                "release_id": "release_004",
                "version_id": "v3.0.0",
                "release_name": "Admin Panel v3.0.0 - Accessibility Improvements",
                "is_release_version": False
            },
            "diffs_computed": {
                "frames_added": ["4:2", "4:3"],
                "frames_updated": [],
                "component_version_bumps": ["AdminPanelHeader-v1.16", "DataTableComponent-v1.18"],
                "prior_release_id": None
            },
            "accessibility_focus": {
                "compliance_standards": ["WCAG 2.1 AA", "Enhanced accessibility"],
                "improvements": ["Screen reader support", "Keyboard navigation"]
            },
            "hero_artifacts_filtered": ["art_001"],
            "assets_exported": ["asset_art_001_jpg_4x"],
            "visual_generated": "before_after_visual_release_004_5894",
            "communication_established": {
                "thread_id": "thread_015",
                "message_id": "msg_017",
                "compliance_stakeholders_notified": 3
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_030",
        instruction=(
            "You are orchestrating the definitive brand transformation that will establish the "
            "company's visual identity for years to come. Your strategic leadership encompasses "
            "release_005, representing the culmination of extensive brand research and stakeholder "
            "alignment across all organizational touchpoints. You must champion this as the official "
            "v2.0.0 brand standard, meticulously documenting the evolutionary changes encompassing "
            "'Brand color palette refresh', 'Typography system overhaul', 'Logo usage guidelines', "
            "and 'Visual identity standards'. This initiative represents a comprehensive rebrand "
            "with no legacy constraints from previous brand iterations (prior release will be null). "
            "Your influence extends to critical brand stewards including 'brand-partners@company.com', "
            "'marketing-leads@company.com', and 'design-team@company.com' through authoritative "
            "communication from 'emma.brand@company.com' with precision labeling using 'brand', "
            "'guidelines', and 'launch' for comprehensive organizational adoption. You should deliver "
            "crystal-clear vector documentation using SVG format at standard resolution to preserve "
            "brand integrity across all digital platforms and ensure scalable implementation."
        ),
        actions=[
            Action(
                name="detect_release_version",
                kwargs={"release_id": "release_005"}
            ),
            Action(
                name="compute_release_diffs",
                kwargs={
                    "release_id": "release_005",
                    "changelog_highlights": ["Brand color palette refresh", "Typography system overhaul", "Logo usage guidelines", "Visual identity standards"]
                }
            ),
            Action(
                name="save_release_diffs",
                kwargs={
                    "release_id": "release_005",
                    "prior_release_id_nullable": None,
                    "frames_added": [],
                    "frames_updated": [],
                    "frames_removed": [],
                    "component_version_bumps": ["BrandGuidelines-v1.15"],
                    "changelog_highlights": ["Brand color palette refresh", "Typography system overhaul", "Logo usage guidelines", "Visual identity standards"]
                }
            ),
            Action(
                name="filter_figma_artifacts_by_tags",
                kwargs={"tags": ["hero"]}
            ),
            Action(
                name="export_figma_artifacts_to_assets",
                kwargs={
                    "artifact_ids": ["art_001"],
                    "export_profile": {"format": "SVG", "scale": "1x"}
                }
            ),
            Action(
                name="generate_before_after_visuals",
                kwargs={
                    "release_id": "release_005",
                    "hero_artifact_ids": ["art_001"]
                }
            ),
            Action(
                name="create_gmail_thread",
                kwargs={
                    "sender_email": "emma.brand@company.com",
                    "recipients_emails": ["brand-partners@company.com", "marketing-leads@company.com", "design-team@company.com"],
                    "workflow_type": "release",
                    "current_labels": ["brand", "guidelines", "launch"]
                }
            ),
            Action(
                name="create_gmail_message",
                kwargs={
                    "sender_email": "emma.brand@company.com",
                    "workflow_type": "release",
                    "thread_id": "thread_015",
                    "attachments_asset_ids": ["asset_art_001_svg_1x"]
                }
            )
        ],
        outputs=[{
            "release_detected": {
                "release_id": "release_005",
                "version_id": "v2.0.0",
                "release_name": "Brand Guidelines v2.0.0 - Updated Palette",
                "is_release_version": False
            },
            "diffs_computed": {
                "frames_added": [],
                "frames_updated": [],
                "frames_removed": [],
                "component_version_bumps": ["BrandGuidelines-v1.15"],
                "prior_release_id": None
            },
            "brand_transformation": {
                "palette_refresh": "Brand color palette refresh",
                "typography_overhaul": "Typography system overhaul",
                "guidelines_established": ["Logo usage guidelines", "Visual identity standards"]
            },
            "hero_artifacts_filtered": ["art_001"],
            "assets_exported": ["asset_art_001_svg_1x"],
            "visual_generated": "before_after_visual_release_005_5894",
            "communication_established": {
                "thread_id": "thread_015",
                "message_id": "msg_017",
                "brand_stakeholders_notified": 3
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_031",
        instruction=(
            "You are leading the evolution of your organization's design system through strategic "
            "navigation component improvements that will fundamentally enhance user wayfinding across "
            "all digital products. Your technical mastery drives release_006, representing the v1.1.0 "
            "milestone that builds upon the foundational work of release_010, systematically advancing "
            "the navigation ecosystem through 'Navigation menu redesign', 'Breadcrumb improvements', "
            "'Sidebar component updates', and 'Mobile navigation patterns'. This comprehensive enhancement "
            "spans both structural additions (frame 1:3) and critical updates to existing navigation "
            "frameworks (frames 1:4 and 1:5), establishing new standards through HomepageHeroSection-v1.19, "
            "NavigationBar-v1.13, DesignSystem-v1.12, and ContactFormComponent-v1.20 component versions. "
            "Your leadership coordinates essential stakeholders including 'design-system@company.com', "
            "'frontend-team@company.com', and 'product-team@company.com' through authoritative communication "
            "from 'sarah.designer@company.com' with strategic categorization using 'design-system', "
            "'navigation', and 'components' labels for comprehensive organizational implementation. You "
            "should deliver detailed documentation using PDF format at standard resolution to provide "
            "comprehensive technical specifications for development teams."
        ),
        actions=[
            Action(
                name="detect_release_version",
                kwargs={"release_id": "release_006"}
            ),
            Action(
                name="compute_release_diffs",
                kwargs={
                    "release_id": "release_006",
                    "changelog_highlights": ["Navigation menu redesign", "Breadcrumb improvements", "Sidebar component updates", "Mobile navigation patterns"]
                }
            ),
            Action(
                name="save_release_diffs",
                kwargs={
                    "release_id": "release_006",
                    "prior_release_id_nullable": "release_010",
                    "frames_added": ["1:3"],
                    "frames_updated": ["1:4", "1:5"],
                    "frames_removed": [],
                    "component_version_bumps": ["HomepageHeroSection-v1.19", "NavigationBar-v1.13", "DesignSystem-v1.12", "ContactFormComponent-v1.20"],
                    "changelog_highlights": ["Navigation menu redesign", "Breadcrumb improvements", "Sidebar component updates", "Mobile navigation patterns"]
                }
            ),
            Action(
                name="filter_figma_artifacts_by_tags",
                kwargs={"tags": ["hero"]}
            ),
            Action(
                name="export_figma_artifacts_to_assets",
                kwargs={
                    "artifact_ids": ["art_001"],
                    "export_profile": {"format": "PDF", "scale": "1x"}
                }
            ),
            Action(
                name="generate_before_after_visuals",
                kwargs={
                    "release_id": "release_006",
                    "hero_artifact_ids": ["art_001"]
                }
            ),
            Action(
                name="create_gmail_thread",
                kwargs={
                    "sender_email": "sarah.designer@company.com",
                    "recipients_emails": ["design-system@company.com", "frontend-team@company.com", "product-team@company.com"],
                    "workflow_type": "release",
                    "current_labels": ["design-system", "navigation", "components"]
                }
            ),
            Action(
                name="create_gmail_message",
                kwargs={
                    "sender_email": "sarah.designer@company.com",
                    "workflow_type": "release",
                    "thread_id": "thread_015",
                    "attachments_asset_ids": ["asset_art_001_pdf_1x"]
                }
            )
        ],
        outputs=[{
            "release_detected": {
                "release_id": "release_006",
                "version_id": "v1.1.0",
                "release_name": "Design System v1.1.0 - Navigation Components",
                "is_release_version": False
            },
            "diffs_computed": {
                "frames_added": ["1:3"],
                "frames_updated": ["1:4", "1:5"],
                "frames_removed": [],
                "component_version_bumps": ["HomepageHeroSection-v1.19", "NavigationBar-v1.13", "DesignSystem-v1.12", "ContactFormComponent-v1.20"],
                "prior_release_id": "release_010"
            },
            # "navigation_system_evolution": {
            #     "menu_redesign": "Navigation menu redesign",
            #     "breadcrumb_improvements": "Breadcrumb improvements",
            #     "sidebar_updates": "Sidebar component updates",
            #     "mobile_patterns": "Mobile navigation patterns"
            # },
            "hero_artifacts_filtered": ["art_001"],
            "assets_exported": ["asset_art_001_pdf_1x"],
            "visual_generated": "before_after_visual_release_006_5894",
            "communication_established": {
                "thread_id": "thread_015",
                "message_id": "msg_017",
                # "design_system_stakeholders_notified": 3
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_032",
        instruction=(
            "You need to manage the design release process for release_007 with changelog highlights including "
            "'Dashboard layout optimization', 'Mobile navigation improvements', 'Widget personalization features', "
            "and 'Performance optimizations'. You should coordinate with recipients 'mobile-team@company.com', "
            "'product-owners@company.com', and 'qa-team@company.com' using sender 'mike.ux@company.com' with "
            "labels 'mobile', 'ux', and 'launch'. Export visuals in JPG format at 2x scale."
        ),
        actions=[
            Action(
                name="detect_release_version",
                kwargs={"release_id": "release_007"}
            ),
            Action(
                name="compute_release_diffs",
                kwargs={
                    "release_id": "release_007",
                    "changelog_highlights": ["Dashboard layout optimization", "Mobile navigation improvements", "Widget personalization features", "Performance optimizations"]
                }
            ),
            Action(
                name="save_release_diffs",
                kwargs={
                    "release_id": "release_007",
                    "prior_release_id_nullable": None,
                    "frames_added": ["2:2", "2:3", "2:4"],
                    "frames_updated": [],
                    "frames_removed": [],
                    "component_version_bumps": ["MobileAppDashboard-v1.18", "UserProfileScreen-v1.17", "SettingsScreen-v1.14"],
                    "changelog_highlights": ["Dashboard layout optimization", "Mobile navigation improvements", "Widget personalization features", "Performance optimizations"]
                }
            ),
            Action(
                name="filter_figma_artifacts_by_tags",
                kwargs={"tags": ["hero"]}
            ),
            Action(
                name="export_figma_artifacts_to_assets",
                kwargs={
                    "artifact_ids": ["art_001"],
                    "export_profile": {"format": "JPG", "scale": "2x"}
                }
            ),
            Action(
                name="generate_before_after_visuals",
                kwargs={
                    "release_id": "release_007",
                    "hero_artifact_ids": ["art_001"]
                }
            ),
            Action(
                name="create_gmail_thread",
                kwargs={
                    "sender_email": "mike.ux@company.com",
                    "recipients_emails": ["mobile-team@company.com", "product-owners@company.com", "qa-team@company.com"],
                    "workflow_type": "release",
                    "current_labels": ["mobile", "ux", "launch"]
                }
            ),
            Action(
                name="create_gmail_message",
                kwargs={
                    "sender_email": "mike.ux@company.com",
                    "workflow_type": "release",
                    "thread_id": "thread_015",
                    "attachments_asset_ids": ["asset_art_001_jpg_2x"]
                }
            )
        ],
        outputs=[{
            "release_detected": {
                "release_id": "release_007",
                "version_id": "v2.0.0",
                "release_name": "Mobile App v2.0.0 - Dashboard Redesign",
                "is_release_version": False
            },
            "diffs_computed": {
                "frames_added": ["2:2", "2:3", "2:4"],
                "frames_updated": [],
                "frames_removed": [],
                "component_version_bumps": ["MobileAppDashboard-v1.18", "UserProfileScreen-v1.17", "SettingsScreen-v1.14"],
                "prior_release_id": None
            },
            "mobile_experience_revolution": {
                "dashboard_optimization": "Dashboard layout optimization",
                "navigation_improvements": "Mobile navigation improvements",
                "personalization_features": "Widget personalization features",
                "performance_optimizations": "Performance optimizations"
            },
            "hero_artifacts_filtered": ["art_001"],
            "assets_exported": ["asset_art_001_jpg_2x"],
            "visual_generated": "before_after_visual_release_007_5894",
            "communication_established": {
                "thread_id": "thread_015",
                "message_id": "msg_017",
                "mobile_stakeholders_notified": 3
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_033",
        instruction=(
            "You are spearheading the ambitious market expansion initiative that will position your "
            "organization at the forefront of digital marketing innovation through strategic beta release "
            "orchestration. Your transformative leadership encompasses release_008, representing the "
            "pioneering v0.9.0 beta milestone that establishes new market positioning standards with "
            "no preceding marketing foundation (prior release will be null). This groundbreaking initiative "
            "demands comprehensive implementation of 'Marketing page optimization', 'Beta feature previews', "
            "'Lead capture enhancements', and 'Content personalization'."
            "Your strategic vision coordinates essential marketing stakeholders including 'marketing@company.com', "
            "'growth-team@company.com', and 'content-team@company.com' through decisive communication from "
            "'lisa.marketing@company.com' with targeted categorization using 'marketing', 'launch', and "
            "'ab-testing' labels for comprehensive organizational market penetration. You should deliver "
            "ultra-high-resolution visual documentation using PNG format at 4x scale to showcase marketing "
            "excellence and beta feature demonstrations with maximum clarity for stakeholder presentations "
            "and market validation processes."
        ),
        actions=[
            Action(
                name="detect_release_version",
                kwargs={"release_id": "release_008"}
            ),
            Action(
                name="compute_release_diffs",
                kwargs={
                    "release_id": "release_008",
                    "changelog_highlights": ["Marketing page optimization", "Beta feature previews", "Lead capture enhancements", "Content personalization"]
                }
            ),
            Action(
                name="save_release_diffs",
                kwargs={
                    "release_id": "release_008",
                    "prior_release_id_nullable": None,
                    "frames_added": ["3:3"],
                    "frames_updated": [],
                    "frames_removed": [],
                    "component_version_bumps": ["MarketingWebsite-v1.16", "PricingPage-v1.11"],
                    "changelog_highlights": ["Marketing page optimization", "Beta feature previews", "Lead capture enhancements", "Content personalization"]
                }
            ),
            Action(
                name="filter_figma_artifacts_by_tags",
                kwargs={"tags": ["hero"]}
            ),
            Action(
                name="export_figma_artifacts_to_assets",
                kwargs={
                    "artifact_ids": ["art_001"],
                    "export_profile": {"format": "PNG", "scale": "4x"}
                }
            ),
            Action(
                name="generate_before_after_visuals",
                kwargs={
                    "release_id": "release_008",
                    "hero_artifact_ids": ["art_001"]
                }
            ),
            Action(
                name="create_gmail_thread",
                kwargs={
                    "sender_email": "lisa.marketing@company.com",
                    "recipients_emails": ["marketing@company.com", "growth-team@company.com", "content-team@company.com"],
                    "workflow_type": "release",
                    "current_labels": ["marketing", "launch", "ab-testing"]
                }
            ),
            Action(
                name="create_gmail_message",
                kwargs={
                    "sender_email": "lisa.marketing@company.com",
                    "workflow_type": "release",
                    "thread_id": "thread_015",
                    "attachments_asset_ids": ["asset_art_001_png_4x"]
                }
            )
        ],
        outputs=[{
            "release_detected": {
                "release_id": "release_008",
                "version_id": "v0.9.0",
                "release_name": "Marketing Website v0.9.0 - Beta Release",
                "is_release_version": False
            },
            "diffs_computed": {
                "diff_id": "diff_008",
                "frames_added": ["3:3"],
                "frames_updated": [],
                "frames_removed": [],
                "component_version_bumps": ["MarketingWebsite-v1.16", "PricingPage-v1.11"],
                "prior_release_id": None
            },
            # "market_expansion_initiative": {
            #     "page_optimization": "Marketing page optimization",
            #     "beta_previews": "Beta feature previews",
            #     "lead_capture": "Lead capture enhancements",
            #     "content_personalization": "Content personalization"
            # },
            "hero_artifacts_filtered": ["art_001"],
            "assets_exported": ["asset_art_001_png_4x"],
            "visual_generated": "before_after_visual_release_008_5894",
            "communication_established": {
                "thread_id": "thread_015",
                "message_id": "msg_017",
                # "marketing_stakeholders_notified": 3
            },

        }]
    ),
    Task(
        annotator="0",
        user_id="task_034",
        instruction=(
            "You need to manage the deployment of data table improvements for the admin panel system. "
            "Review and process release_009 to update data visualization components and notify administrative teams. "
            "You must compute the differences from any previous releases, save the diff analysis, and coordinate communication "
            "with admin-team@company.com, data-team@company.com, and backend-team@company.com about the improvements. "
            "Filter for hero artifacts to highlight in your communications, export them as 1x SVG assets for technical documentation, "
            "and generate before/after visuals to demonstrate the enhancements. Create a comprehensive email thread "
            "with appropriate admin and data-table labels to track this deployment across all stakeholder groups. "
            "Your changelog should focus on data table improvements, advanced filtering features, pagination enhancements, "
            "and column customization options that will enhance user workflows."
        ),
        actions=[
            Action(
                name="detect_release_version",
                kwargs={"release_id": "release_009"}
            ),
            Action(
                name="compute_release_diffs",
                kwargs={
                    "release_id": "release_009",
                    "changelog_highlights": ["Data table improvements", "Advanced filtering features", "Pagination enhancements", "Column customization options"]
                }
            ),
            Action(
                name="save_release_diffs",
                kwargs={
                    "release_id": "release_009",
                    "prior_release_id_nullable": None,
                    "frames_added": ["4:2", "4:3"],
                    "frames_updated": [],
                    "frames_removed": [],
                    "component_version_bumps": ["AdminPanelHeader-v1.16", "DataTableComponent-v1.18"],
                    "changelog_highlights": ["Data table improvements", "Advanced filtering features", "Pagination enhancements", "Column customization options"]
                }
            ),
            Action(
                name="filter_figma_artifacts_by_tags",
                kwargs={"tags": ["hero"]}
            ),
            Action(
                name="export_figma_artifacts_to_assets",
                kwargs={
                    "artifact_ids": ["art_001"],
                    "export_profile": {"format": "SVG", "scale": "1x"}
                }
            ),
            Action(
                name="generate_before_after_visuals",
                kwargs={
                    "release_id": "release_009",
                    "hero_artifact_ids": ["art_001"]
                }
            ),
            Action(
                name="create_gmail_thread",
                kwargs={
                    "sender_email": "alex.dev@company.com",
                    "recipients_emails": ["admin-team@company.com", "data-team@company.com", "backend-team@company.com"],
                    "workflow_type": "release",
                    "current_labels": ["admin", "data-table"] # , "launch"]
                }
            ),
            Action(
                name="create_gmail_message",
                kwargs={
                    "sender_email": "alex.dev@company.com",
                    "workflow_type": "release",
                    "thread_id": "thread_015",
                    "attachments_asset_ids": ["asset_art_001_svg_1x"]
                }
            )
        ],
        outputs=[{
            "release_detected": {
                "release_id": "release_009",
                "version_id": "v2.5.0",
                "release_name": "Admin Panel v2.5.0 - Data Table Components",
                "is_release_version": False
            },
            "diffs_computed": {
                "frames_added": ["4:2", "4:3"],
                "frames_updated": [],
                "frames_removed": [],
                "component_version_bumps": ["AdminPanelHeader-v1.16", "DataTableComponent-v1.18"],
                "prior_release_id": None
            },
            # "enterprise_data_transformation": {
            #     "table_improvements": "Data table improvements",
            #     "filtering_features": "Advanced filtering features",
            #     "pagination_enhancements": "Pagination enhancements",
            #     "customization_options": "Column customization options"
            # },
            "hero_artifacts_filtered": ["art_001"],
            "assets_exported": ["asset_art_001_svg_1x"],
            "visual_generated": "before_after_visual_release_009_5894",
            "communication_established": {
                "thread_id": "thread_015",
                "message_id": "msg_017",
                "admin_stakeholders_notified": 3
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_035",
        instruction=(
            "You need to announce the launch of your organization's comprehensive design system v1.0.0. "
            "This is a foundational release that establishes core button components, input field standards, and a complete typography system. "
            "You want to ensure development teams and design system stakeholders receive formal documentation detailing the available components. "
            "Your communication should include complete PDF documentation in 1x scale to serve as implementation reference. "
            "The recipients should be dev-team@company.com and design-system@company.com, with labels 'design-system', 'launch', and 'components' for proper tracking. "
            "You should use release_010 for this announcement, with changelog highlights covering 'Core button components', 'Input field standards', and 'Typography system'. "
            "Your output should include the visual asset identifier and communication thread details."
        ),
        actions=[
            Action(
                name="detect_release_version",
                kwargs={"release_id": "release_010"}
            ),
            Action(
                name="compute_release_diffs",
                kwargs={
                    "release_id": "release_010",
                    "changelog_highlights": ["Core button components", "Input field standards", "Typography system"]
                }
            ),
            Action(
                name="save_release_diffs",
                kwargs={
                    "release_id": "release_010",
                    "prior_release_id_nullable": None,
                    "frames_added": ["1:3", "1:4", "1:5"],
                    "frames_updated": [],
                    "frames_removed": [],
                    "component_version_bumps": ["HomepageHeroSection-v1.19", "NavigationBar-v1.13", "DesignSystem-v1.12", "ContactFormComponent-v1.20"],
                    "changelog_highlights": ["Core button components", "Input field standards", "Typography system"]
                }
            ),
            Action(
                name="filter_figma_artifacts_by_tags",
                kwargs={"tags": ["hero"]}
            ),
            Action(
                name="export_figma_artifacts_to_assets",
                kwargs={
                    "artifact_ids": ["art_001"],
                    "export_profile": {"format": "PDF", "scale": "1x"}
                }
            ),
            Action(
                name="generate_before_after_visuals",
                kwargs={
                    "release_id": "release_010",
                    "hero_artifact_ids": ["art_001"]
                }
            ),
            Action(
                name="create_gmail_thread",
                kwargs={
                    "sender_email": "sarah.designer@company.com",
                    "recipients_emails": ["dev-team@company.com", "design-system@company.com"],
                    "workflow_type": "release",
                    "current_labels": ["design-system", "launch", "components"]
                }
            ),
            Action(
                name="create_gmail_message",
                kwargs={
                    "sender_email": "sarah.designer@company.com",
                    "workflow_type": "release",
                    "thread_id": "thread_015",
                    "attachments_asset_ids": ["asset_art_001_pdf_1x"]
                }
            )
        ],
        outputs=[{
            "release_detected": {
                "release_id": "release_010",
                "version_id": "v1.0.0",
                "release_name": "Design System v1.0.0 - Initial Release",
                "is_release_version": True
            },
            "diffs_computed": {
                "frames_added": ["1:3", "1:4", "1:5"],
                "frames_updated": [],
                "frames_removed": [],
                "component_version_bumps": ["HomepageHeroSection-v1.19", "NavigationBar-v1.13", "DesignSystem-v1.12", "ContactFormComponent-v1.20"],
                "prior_release_id": None
            },
            "design_system_launch": {
                "release_name": "Design System v1.0.0 - Initial Release",
                "visual_asset": "before_after_visual_release_010_5894",
                "thread_id": "thread_015",
                "message_id": "msg_017",
                # "documentation_format": "PDF 1x",
                # "stakeholder_groups": 2
            },
            "hero_artifacts_filtered": ["art_001"],
            "assets_exported": ["asset_art_001_pdf_1x"],
            "visual_generated": "before_after_visual_release_010_5894",
            "communication_established": {
                "thread_id": "thread_015",
                "message_id": "msg_017",
                "design_system_stakeholders_notified": 2
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_036",
        instruction=(
            "You need to coordinate a comprehensive mobile application release campaign for the latest user experience improvements. "
            "Your focus should be on release_002 which represents significant mobile app enhancements including user dashboard upgrades and "
            "profile editing capabilities. You want to ensure this qualifies as a proper release version before proceeding with stakeholder "
            "communications. Your analysis should capture the evolution from the previous version, documenting key improvements through "
            "'Enhanced user dashboard', 'New profile editor', 'Improved mobile responsive design', and 'Updated navigation patterns'. "
            "You should prepare high-resolution documentation using PNG format at 4x scale for detailed visual review. Your communications "
            "will originate from 'mike.ux@company.com' and reach key stakeholders at 'product-team@company.com', 'dev-team@company.com', "
            "and 'stakeholders@company.com'. You should ensure proper categorization using 'Design/Release', 'mobile', and 'launch' "
            "labels for effective project tracking and visibility across teams."
        ),
        actions=[
            Action(
                name="detect_release_version",
                kwargs={"release_id": "release_002"}
            ),
            Action(
                name="compute_release_diffs",
                kwargs={
                    "release_id": "release_002",
                    "changelog_highlights": ["Enhanced user dashboard", "New profile editor", "Improved mobile responsive design", "Updated navigation patterns"]
                }
            ),
            Action(
                name="save_release_diffs",
                kwargs={
                    "release_id": "release_002",
                    "prior_release_id_nullable": "release_007",
                    "frames_added": ["2:2"],
                    "frames_updated": ["2:3", "2:4"],
                    "frames_removed": [],
                    "component_version_bumps": ["MobileAppDashboard-v1.18", "UserProfileScreen-v1.17", "SettingsScreen-v1.14"],
                    "changelog_highlights": ["Enhanced user dashboard", "New profile editor", "Improved mobile responsive design", "Updated navigation patterns"]
                }
            ),
            Action(
                name="filter_figma_artifacts_by_tags",
                kwargs={"tags": ["hero"]}
            ),
            Action(
                name="export_figma_artifacts_to_assets",
                kwargs={"artifact_ids": ["art_001"], "export_profile": {"format": "PNG", "scale": "4x"}}
            ),
            Action(
                name="generate_before_after_visuals",
                kwargs={
                    "release_id": "release_002",
                    "hero_artifact_ids": ["art_001"]
                }
            ),
            Action(
                name="create_gmail_thread",
                kwargs={
                    "sender_email": "mike.ux@company.com",
                    "recipients_emails": ["product-team@company.com", "dev-team@company.com", "stakeholders@company.com"],
                    "workflow_type": "release",
                    "current_labels": ["Design/Release", "mobile", "launch"]
                }
            ),
            Action(
                name="create_gmail_message",
                kwargs={
                    "sender_email": "mike.ux@company.com",
                    "workflow_type": "release",
                    "thread_id": "thread_015",
                    "attachments_asset_ids": ["asset_art_001_png_4x"]
                }
            )
        ],
        outputs=[
            {
                "is_release_version": True,
                "release_info": {
                    "release_id": "release_002",
                    "version_tag": "release/mobile-app-v2.1.0",
                    "release_name": "Mobile App v2.1.0 - User Profile & Dashboard"
                },
                "computed_diffs": {
                    "prior_release_id_nullable": "release_007",
                    "frames_added": ["2:2"],
                    "frames_updated": ["2:3", "2:4"],
                    "component_version_bumps": ["MobileAppDashboard-v1.18", "UserProfileScreen-v1.17", "SettingsScreen-v1.14"]
                },
                "saved_diff_id": "diff_002",
                "hero_artifacts": ["art_001"],
                "exported_assets": ["asset_art_001_png_4x"],
                "visual_name": "before_after_visual_release_002_5894",
                "gmail_thread_id": "thread_015",
                "gmail_message_id": "msg_017"
            }
        ]
    ),
    Task(
        annotator="0",
        user_id="task_037",
        instruction=(
            "You are orchestrating the release communication for a major design system update focused on accessibility and form enhancements. "
            "You need to handle release_011 which represents significant advancements in form components and accessibility standards. "
            "Your responsibility includes confirming this as a valid release candidate, documenting the evolution from previous iterations, "
            "and generating comprehensive visual documentation. You should highlight the key improvements: 'Advanced form components', "
            "'Enhanced accessibility features', and 'Improved user interactions'. Your communication approach involves reaching out to "
            "technical teams as 'sarah.designer@company.com' targeting 'engineering-team@company.com', 'qa-team@company.com', and "
            "'product-managers@company.com' with clear 'Design/Release', 'design-system', and 'components' categorization. "
            "You want to export hero graphics in JPG format at 2x resolution for balanced quality and file size."
        ),
        actions=[
            Action(
                name="detect_release_version",
                kwargs={"release_id": "release_011"}
            ),
            Action(
                name="compute_release_diffs",
                kwargs={
                    "release_id": "release_011",
                    "changelog_highlights": ["Advanced form components", "Enhanced accessibility features", "Improved user interactions"]
                }
            ),
            Action(
                name="save_release_diffs",
                kwargs={
                    "release_id": "release_011",
                    "prior_release_id_nullable": "release_001",
                    "frames_added": ["1:3", "1:4"],
                    "frames_updated": ["1:5"],
                    "frames_removed": [],
                    "component_version_bumps": ["HomepageHeroSection-v1.19", "NavigationBar-v1.13", "DesignSystem-v1.12", "ContactFormComponent-v1.20"],
                    "changelog_highlights": ["Advanced form components", "Enhanced accessibility features", "Improved user interactions"]
                }
            ),
            Action(
                name="filter_figma_artifacts_by_tags",
                kwargs={"tags": ["hero"]}
            ),
            Action(
                name="export_figma_artifacts_to_assets",
                kwargs={"artifact_ids": ["art_001"], "export_profile": {"format": "JPG", "scale": "2x"}}
            ),
            Action(
                name="generate_before_after_visuals",
                kwargs={
                    "release_id": "release_011",
                    "hero_artifact_ids": ["art_001"]
                }
            ),
            Action(
                name="create_gmail_thread",
                kwargs={
                    "sender_email": "sarah.designer@company.com",
                    "recipients_emails": ["engineering-team@company.com", "qa-team@company.com", "product-managers@company.com"],
                    "workflow_type": "release",
                    "current_labels": ["Design/Release", "design-system", "components"]
                }
            ),
            Action(
                name="create_gmail_message",
                kwargs={
                    "sender_email": "sarah.designer@company.com",
                    "workflow_type": "release",
                    "thread_id": "thread_015",
                    "attachments_asset_ids": ["asset_art_001_jpg_2x"]
                }
            )
        ],
        outputs=[
            {
                "is_release_version": True,
                "release_info": {
                    "release_id": "release_011",
                    "version_tag": "release/design-system-v1.3.0",
                    "release_name": "Design System v1.3.0 - Form Components & Accessibility"
                },
                "computed_diffs": {
                    "prior_release_id_nullable": "release_001",
                    "frames_added": ["1:3", "1:4"],
                    "frames_updated": ["1:5"],
                    "frames_removed": [],
                    "component_version_bumps": ["HomepageHeroSection-v1.19", "NavigationBar-v1.13", "DesignSystem-v1.12", "ContactFormComponent-v1.20"],
                    "changelog_highlights": ["Advanced form components", "Enhanced accessibility features", "Improved user interactions"]
                },
                "saved_diff_id": "diff_011",
                "hero_artifacts": ["art_001"],
                "exported_assets": ["asset_art_001_jpg_2x"],
                "visual_name": "before_after_visual_release_011_5894",
                "gmail_thread_id": "thread_015",
                "gmail_message_id": "msg_017"
            }
        ]
    ),
    Task(
        annotator="0",
        user_id="task_038",
        instruction=(
            "You need to orchestrate the mobile app release communication for the latest profile and settings enhancements. "
            "You want to process the mobile app release_012 version 2.2.0 release that introduces enhanced user profile management and settings controls. "
            "Your responsibility involves generating comprehensive release documentation with scalable vector graphics at 4x resolution to ensure crisp visuals across all viewing contexts. "
            "You should use your email, mike.ux@company.com, to target product managers at product@company.com, development teams at dev-team@company.com, and QA personnel at qa@company.com who need detailed technical information about the release changes. "
            "Your communication will focus on the 'Profile Settings Enhancement', 'Privacy Controls Update', 'Notification Preferences', and 'Account Management' improvements. "
            "You should apply Design/Release labels along with mobile, profile, and update categorization for proper organization. "
            "Expected output includes successful release processing confirmation, exported assets, and stakeholder email communication."
        ),
        actions=[
            Action(
                name="detect_release_version",
                kwargs={"release_id": "release_012"}
            ),
            Action(
                name="compute_release_diffs",
                kwargs={"release_id": "release_012", "changelog_highlights": ["Profile Settings Enhancement", "Privacy Controls Update", "Notification Preferences", "Account Management"]}
            ),
            Action(
                name="save_release_diffs",
                kwargs={"release_id": "release_012", "prior_release_id_nullable": "release_002", "frames_added": ["2:2", "2:3"], "frames_updated": ["2:4"], "frames_removed": [], "component_version_bumps": ["MobileAppDashboard-v1.18", "UserProfileScreen-v1.17", "SettingsScreen-v1.14"], "changelog_highlights": ["Profile Settings Enhancement", "Privacy Controls Update", "Notification Preferences", "Account Management"]}
            ),
            Action(
                name="filter_figma_artifacts_by_tags",
                kwargs={"tags": ["hero"]}
            ),
            Action(
                name="export_figma_artifacts_to_assets",
                kwargs={"artifact_ids": ["art_001"], "export_profile": {"format": "SVG", "scale": "4x"}}
            ),
            Action(
                name="generate_before_after_visuals",
                kwargs={"release_id": "release_012", "hero_artifact_ids": ["art_001"]}
            ),
            Action(
                name="create_gmail_thread",
                kwargs={"sender_email": "mike.ux@company.com", "recipients_emails": ["product@company.com", "dev-team@company.com", "qa@company.com"], "workflow_type": "release", "current_labels": ["Design/Release", "mobile", "profile", "update"]}
            ),
            Action(
                name="create_gmail_message",
                kwargs={"sender_email": "mike.ux@company.com", "workflow_type": "release", "thread_id": "thread_015", "attachments_asset_ids": ["asset_art_001_svg_4x"]}
            )
        ],
        outputs=[
            {
                "release_detected": True,
                "release_info": {
                    "release_id": "release_012",
                    "version": "v2.2.0",
                    "release_name": "Mobile App v2.2.0 - Settings & Profile Enhancements"
                },
                "diff_processing": {
                    "prior_release": "release_002",
                    "frames_added": 2,
                    "frames_updated": 1,
                    "component_bumps": 3
                },
                "hero_artifacts_exported": ["art_001"],
                "export_format": "SVG",
                "export_scale": "4x",
                "visual_generation": "before_after_visual_release_012_5894",
                "gmail_thread_id": "thread_015",
                "gmail_message_id": "msg_017"
            }
        ]
    ),
    Task(
        annotator="0",
        user_id="task_039",
        instruction=(
            "You need to spearhead a comprehensive design system communication initiative targeting technical implementation teams. "
            "Your focus centers on the enhanced component library release_001 that introduces fundamental improvements to cross-platform compatibility and developer experience. "
            "You want to coordinate the release_001 announcement, emphasizing the 'Component Library Overhaul', 'Token System Refinement', 'Cross-Platform Compatibility' enhancements, and 'Developer Experience' improvements. "
            "Your communication strategy should leverage high-quality JPEG assets at 2x resolution to ensure optimal rendering across diverse technical documentation platforms. "
            "You should engage engineering teams at engineering@company.com, design system specialists at design-system@company.com, and accessibility experts at accessibility@company.com, from your email address sarah.designer@company.com, who require detailed technical specifications for implementation. "
            "You should apply Design/Release labels along with design-system, accessibility, and components categorization for proper organization. "
            "Your outreach will bridge the gap between design innovation and technical execution, ensuring seamless adoption across all development environments. "
            "Expected output includes validated release processing, optimized visual assets, and targeted stakeholder communication."
        ),
        actions=[
            Action(
                name="detect_release_version",
                kwargs={"release_id": "release_001"}
            ),
            Action(
                name="compute_release_diffs",
                kwargs={"release_id": "release_001", "changelog_highlights": ["Component Library Overhaul", "Token System Refinement", "Cross-Platform Compatibility", "Developer Experience"]}
            ),
            Action(
                name="save_release_diffs",
                kwargs={"release_id": "release_001", "prior_release_id_nullable": "release_006", "frames_added": ["1:3", "1:4"], "frames_updated": ["1:5"], "frames_removed": [], "component_version_bumps": ["HomepageHeroSection-v1.19", "NavigationBar-v1.13", "DesignSystem-v1.12", "ContactFormComponent-v1.20"], "changelog_highlights": ["Component Library Overhaul", "Token System Refinement", "Cross-Platform Compatibility", "Developer Experience"]}
            ),
            Action(
                name="filter_figma_artifacts_by_tags",
                kwargs={"tags": ["hero"]}
            ),
            Action(
                name="export_figma_artifacts_to_assets",
                kwargs={"artifact_ids": ["art_001"], "export_profile": {"format": "JPG", "scale": "2x"}}
            ),
            Action(
                name="generate_before_after_visuals",
                kwargs={"release_id": "release_001", "hero_artifact_ids": ["art_001"]}
            ),
            Action(
                name="create_gmail_thread",
                kwargs={"sender_email": "sarah.designer@company.com", "recipients_emails": ["engineering@company.com", "design-system@company.com", "accessibility@company.com"], "workflow_type": "release", "current_labels": ["Design/Release", "design-system", "accessibility", "components"]}
            ),
            Action(
                name="create_gmail_message",
                kwargs={"sender_email": "sarah.designer@company.com", "workflow_type": "release", "thread_id": "thread_015", "attachments_asset_ids": ["asset_art_001_jpg_2x"]}
            )
        ],
        outputs=[
            {
                "release_validated": True,
                "release_info": {
                    "release_id": "release_001",
                    "version": "v1.2.0",
                    "release_name": "Design System v1.2.0 - Enhanced Components"
                },
                "diff_computation": {
                    "prior_release": "release_006",
                    "frames_added": 2,
                    "frames_updated": 1,
                    "component_bumps": 4
                },
                "hero_artifacts_exported": ["art_001"],
                "export_format": "JPG",
                "export_scale": "2x",
                "visual_generation": "before_after_visual_release_001_5894",
                "technical_stakeholder_outreach": {
                    "engineering_team": True,
                    "design_system_team": True,
                    "accessibility_team": True
                },
                "gmail_thread_id": "thread_015",
                "gmail_message_id": "msg_017"
            }
        ]
    ),
    Task(
        annotator="0",
        user_id="task_040",
        instruction=(
            "You need to coordinate a detailed review of data table designs requiring technical feedback. "
            "Your focus should be on 'table' tagged artifacts to ensure data visualization meets backend "
            "integration requirements. You should export using PNG format at 1x scale for clear technical "
            "review details. You will be working as 'data-architect@company.com' with recipients "
            "backend-team@company.com and qa-engineers@company.com. Use 'data-table', 'review', and 'admin' "
            "labels for proper categorization, and ensure the artifact gets NEEDS_REVIEW status for tracking."
        ),
        actions=[
            Action(
                name="filter_figma_artifacts_by_tags",
                kwargs={"tags": ["table"]}
            ),
            Action(
                name="export_figma_artifacts_to_assets",
                kwargs={"artifact_ids": ["art_009"], "export_profile": {"format": "PNG", "scale": "1x"}}
            ),
            Action(
                name="create_gmail_thread",
                kwargs={
                    "sender_email": "data-architect@company.com",
                    "recipients_emails": ["backend-team@company.com", "qa-engineers@company.com"],
                    "workflow_type": "review",
                    "current_labels": ["data-table", "review", "admin"]
                }
            ),
            Action(
                name="create_review_cycle",
                kwargs={"artifact_id": "art_009", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="create_gmail_message",
                kwargs={
                    "sender_email": "data-architect@company.com",
                    "workflow_type": "review",
                    "thread_id": "thread_015",
                    "attachments_asset_ids": ["asset_art_009_png_1x"]
                }
            )
        ],
        outputs=[
            {
                "filtered_artifacts": ["art_009"],
                "exported_asset_ids": ["asset_art_009_png_1x"],
                "gmail_thread_id": "thread_015",
                "review_cycle_id": "cycle_013",
                "gmail_message_id": "msg_017"
            }
        ]
    ),
    Task(
        annotator="0",
        user_id="task_041",
        instruction=(
            "You need to facilitate a comprehensive user experience review focusing on profile interface design. "
            "Your responsibility involves coordinating feedback from product teams and user research specialists "
            "for 'user' tagged artifacts to ensure interface usability meets design standards. You should export "
            "using SVG format at 2x scale for high-quality vector graphics suitable for detailed UX analysis. "
            "You will communicate as 'ux-designer@company.com' with recipients product-team@company.com and "
            "user-research@company.com. Apply 'ux', 'review', and 'profile' labels for proper workflow tracking, "
            "and establish NEEDS_REVIEW status to initiate the review process."
        ),
        actions=[
            Action(
                name="filter_figma_artifacts_by_tags",
                kwargs={"tags": ["user"]}
            ),
            Action(
                name="export_figma_artifacts_to_assets",
                kwargs={"artifact_ids": ["art_005"], "export_profile": {"format": "SVG", "scale": "2x"}}
            ),
            Action(
                name="create_gmail_thread",
                kwargs={
                    "sender_email": "ux-designer@company.com",
                    "recipients_emails": ["product-team@company.com", "user-research@company.com"],
                    "workflow_type": "review",
                    "current_labels": ["ux", "review", "profile"]
                }
            ),
            Action(
                name="create_review_cycle",
                kwargs={"artifact_id": "art_005", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="create_gmail_message",
                kwargs={
                    "sender_email": "ux-designer@company.com",
                    "workflow_type": "review",
                    "thread_id": "thread_015",
                    "attachments_asset_ids": ["asset_art_005_svg_2x"]
                }
            )
        ],
        outputs=[
            {
                "filtered_artifacts": ["art_005"],
                "exported_asset_ids": ["asset_art_005_svg_2x"],
                "gmail_thread_id": "thread_015",
                "review_cycle_id": "cycle_013",
                "gmail_message_id": "msg_017"
            }
        ]
    ),
    Task(
        annotator="0",
        user_id="task_042",
        instruction=(
            "You need to coordinate the release announcement for critical accessibility improvements in the admin panel. "
            "You should focus on release_004 which delivers significant WCAG 2.1 compliance enhancements including "
            "ARIA-compliant form elements, High contrast color schemes, Keyboard navigation improvements, and "
            "Screen reader compatibility enhancements. Your responsibility involves detecting version information, "
            "computing comprehensive release differences that may include no prior release (prior_release_id_nullable: None), "
            "documenting changes with frames added, component version bumps, and specific changelog highlights. "
            "Your communication should originate from 'accessibility-lead@company.com' and reach stakeholders at "
            "'admin-team@company.com' and 'compliance-team@company.com' with appropriate 'Design/Release', "
            "'accessibility', and 'admin' labels for proper categorization. You should export documentation using "
            "PDF format at 1x scale for comprehensive accessibility compliance records."
        ),
        actions=[
            Action(
                name="detect_release_version",
                kwargs={"release_id": "release_004"}
            ),
            Action(
                name="compute_release_diffs",
                kwargs={
                    "release_id": "release_004",
                    "changelog_highlights": ["ARIA-compliant form elements", "High contrast color schemes", "Keyboard navigation improvements", "Screen reader compatibility enhancements"]
                }
            ),
            Action(
                name="save_release_diffs",
                kwargs={
                    "release_id": "release_004",
                    "prior_release_id_nullable": None,
                    "frames_added": ["4:2", "4:3"],
                    "frames_updated": [],
                    "frames_removed": [],
                    "component_version_bumps": ["AdminPanelHeader-v1.16", "DataTableComponent-v1.18"],
                    "changelog_highlights": ["ARIA-compliant form elements", "High contrast color schemes", "Keyboard navigation improvements", "Screen reader compatibility enhancements"]
                }
            ),
            Action(
                name="filter_figma_artifacts_by_tags",
                kwargs={"tags": ["hero"]}
            ),
            Action(
                name="export_figma_artifacts_to_assets",
                kwargs={"artifact_ids": ["art_001"], "export_profile": {"format": "PDF", "scale": "1x"}}
            ),
            Action(
                name="generate_before_after_visuals",
                kwargs={
                    "release_id": "release_004",
                    "hero_artifact_ids": ["art_001"]
                }
            ),
            Action(
                name="create_gmail_thread",
                kwargs={
                    "sender_email": "accessibility-lead@company.com",
                    "recipients_emails": ["admin-team@company.com", "compliance-team@company.com"],
                    "workflow_type": "release",
                    "current_labels": ["Design/Release", "accessibility", "admin"]
                }
            ),
            Action(
                name="create_gmail_message",
                kwargs={
                    "sender_email": "accessibility-lead@company.com",
                    "workflow_type": "release",
                    "thread_id": "thread_015",
                    "attachments_asset_ids": ["asset_art_001_pdf_1x"]
                }
            )
        ],
        outputs=[
            {
                "is_release_version": False,
                "computed_diffs": {
                    "prior_release_id_nullable": None,
                    "frames_added": ["4:2", "4:3"],
                    "frames_updated": [],
                    "component_version_bumps": ["AdminPanelHeader-v1.16", "DataTableComponent-v1.18"]
                },
                "saved_diff_id": "diff_004",
                "hero_artifacts": ["art_001"],
                "exported_assets": ["asset_art_001_pdf_1x"],
                "visual_name": "before_after_visual_release_004_5894",
                "gmail_thread_id": "thread_015",
                "gmail_message_id": "msg_017"
            }
        ]
    ),
    Task(
        annotator="0",
        user_id="task_043",
        instruction=(
            "You need to coordinate the beta release communication for the marketing website redesign project. "
            "Your objective centers on release_008, representing the v0.9.0 beta release that introduces significant "
            "testing integrations and performance optimizations. You want to establish comprehensive release documentation "
            "and stakeholder communication for the marketing team's latest achievements in beta functionality and user experience refinements. "
            "Your communication strategy should emphasize the Beta Testing Integration, Performance Optimization, Bug Fixes, and Feature Completion enhancements "
            "while building upon the foundation established by release_007. "
            "You should prioritize PNG assets at 4x resolution to ensure maximum visual clarity across all marketing channels and stakeholder presentations. "
            "Your communication should reach both technical team@company.com and dev@company.com stakeholders through appropriate team distribution channels using 'marketing' and 'launch' organizational labels."
        ),
        actions=[
            Action(
                name="detect_release_version",
                kwargs={"release_id": "release_008"}
            ),
            Action(
                name="compute_release_diffs",
                kwargs={"release_id": "release_008", "changelog_highlights": ["Beta Testing Integration", "Performance Optimization", "Bug Fixes", "Feature Completion"]}
            ),
            Action(
                name="save_release_diffs",
                kwargs={"release_id": "release_008", "prior_release_id_nullable": "release_007", "frames_added": ["3:3"], "frames_updated": [], "frames_removed": [], "component_version_bumps": ["MarketingWebsite-v1.16", "PricingPage-v1.11"], "changelog_highlights": ["Beta Testing Integration", "Performance Optimization", "Bug Fixes", "Feature Completion"]}
            ),
            Action(
                name="filter_figma_artifacts_by_tags",
                kwargs={"tags": ["hero"]}
            ),
            Action(
                name="export_figma_artifacts_to_assets",
                kwargs={"artifact_ids": ["art_001"], "export_profile": {"format": "PNG", "scale": "4x"}}
            ),
            Action(
                name="generate_before_after_visuals",
                kwargs={"release_id": "release_008", "hero_artifact_ids": ["art_001"]}
            ),
            Action(
                name="create_gmail_thread",
                kwargs={"sender_email": "lisa.marketing@company.com", "recipients_emails": ["team@company.com", "dev@company.com"], "workflow_type": "release", "current_labels": ["marketing", "launch"]}
            ),
            Action(
                name="create_gmail_message",
                kwargs={"sender_email": "lisa.marketing@company.com", "workflow_type": "release", "thread_id": "thread_015", "attachments_asset_ids": ["asset_art_001_png_4x"] }
            )
        ],
        outputs=[
            {
                "release_info": {
                    "release_id": "release_008",
                    "version_tag": "marketing-website-v0.9.0",
                    "release_name": "Marketing Website v0.9.0 - Beta Release",
                    "is_release_version": False
                },
                "computed_diffs": {
                    "frames_added": ["3:3"],
                    "frames_updated": [],
                    "component_version_bumps": ["MarketingWebsite-v1.16", "PricingPage-v1.11"]
                },
                "saved_diff_id": "diff_008",
                "marketing_artifacts": ["art_001"],
                "exported_assets": ["asset_art_001_png_4x"],
                "export_format": "PNG",
                "export_scale": "4x",
                "visual_generated": "before_after_visual_release_008_5894",
                "gmail_thread_id": "thread_015",
                "gmail_message_id": "msg_017"
            }
        ]
    ),
    Task(
        annotator="0",
        user_id="task_044",
        instruction=(
            "You need to orchestrate the admin panel release communication for the latest data table component enhancements. "
            "Your responsibility encompasses release_009, representing the v2.5.0 milestone that introduces significant "
            "Data Table Enhancement, Admin Dashboard Refinement, Component Architecture improvements, and User Experience Improvement features. "
            "You want to establish comprehensive documentation and stakeholder alignment for the administrative platform's evolution, "
            "building upon the foundational work established in release_006. "
            "You should prioritize scalable SVG assets at 1x resolution to ensure crisp rendering across diverse administrative interfaces and documentation systems. "
            "Your communication strategy should reach admin-team@company.com and stakeholders@company.com through targeted distribution using 'admin' and 'components' organizational labels "
            "from your email address alex.dev@company.com."
        ),
        actions=[
            Action(
                name="detect_release_version",
                kwargs={"release_id": "release_009"}
            ),
            Action(
                name="compute_release_diffs",
                kwargs={"release_id": "release_009", "changelog_highlights": ["Data Table Enhancement", "Admin Dashboard Refinement", "Component Architecture", "User Experience Improvement"]}
            ),
            Action(
                name="save_release_diffs",
                kwargs={"release_id": "release_009", "prior_release_id_nullable": "release_006", "frames_added": ["4:2", "4:3"], "frames_updated": [], "frames_removed": [], "component_version_bumps": ['AdminPanelHeader-v1.16','DataTableComponent-v1.18'], "changelog_highlights": ["Data Table Enhancement", "Admin Dashboard Refinement", "Component Architecture", "User Experience Improvement"]}
            ),
            Action(
                name="filter_figma_artifacts_by_tags",
                kwargs={"tags": ["hero"]}
            ),
            Action(
                name="export_figma_artifacts_to_assets",
                kwargs={"artifact_ids": ["art_001"], "export_profile": {"format": "SVG", "scale": "1x"}}
            ),
            Action(
                name="generate_before_after_visuals",
                kwargs={"release_id": "release_009", "hero_artifact_ids": ["art_001"]}
            ),
            Action(
                name="create_gmail_thread",
                kwargs={"sender_email": "alex.dev@company.com", "recipients_emails": ["admin-team@company.com", "stakeholders@company.com"], "workflow_type": "release", "current_labels": ["admin", "components"]}
            ),
            Action(
                name="create_gmail_message",
                kwargs={"sender_email": "alex.dev@company.com", "workflow_type": "release", "thread_id": "thread_015", "attachments_asset_ids": ["asset_art_001_svg_1x"]}
            )
        ],
        outputs=[
            {
                "release_info": {
                    "release_id": "release_009",
                    "version_tag": "admin-panel-v2.5.0",
                    "release_name": "Admin Panel v2.5.0 - Data Table Components",
                    "is_release_version": False
                },
                "computed_diffs": {
                    "frames_added": ["4:2", "4:3"],
                    "frames_updated": [],
                    "component_version_bumps": ["AdminPanelHeader-v1.16", "DataTableComponent-v1.18"]
                },
                "saved_diff_id": "diff_009",
                "hero_artifacts": ["art_001"],
                "exported_assets": ["asset_art_001_svg_1x"],
                "export_format": "SVG",
                "export_scale": "1x",
                "visual_generated": "before_after_visual_release_009_5894",
                "gmail_thread_id": "thread_015",
                "gmail_message_id": "msg_017"
            }
        ]
    ),

        Task(
        annotator="0",
        user_id="task_045",
        instruction=(
            "You need to manage the release communication for the Admin Panel v2.5.0 data table component update. "
            "You want to coordinate the design handoff between development and stakeholder teams for this significant "
            "component architecture enhancement. Your focus should be on the release_009 version, which introduces "
            "table filtering improvements, data pagination updates, and component accessibility enhancements. "
            "You should build upon the previous release_006 version to establish proper diff tracking. "
            "You should export assets in SVG format at 1x scale for optimal development handoff. Your communication "
            "should come from alex.dev@company.com and target admin-team@company.com and stakeholders@company.com. "
            "You need to ensure proper tagging with admin, data-table, and Design/Release labels for effective "
            "categorization and tracking of this component-focused release."
        ),
        actions=[
            Action(
                name="detect_release_version",
                kwargs={"release_id": "release_009"}
            ),
            Action(
                name="compute_release_diffs",
                kwargs={
                    "release_id": "release_009",
                    "changelog_highlights": ["table filtering improvements", "data pagination updates", "component accessibility enhancements"]
                }
            ),
            Action(
                name="save_release_diffs",
                kwargs={
                    "release_id": "release_009",
                    "prior_release_id_nullable": "release_006",
                    "frames_added": ["4:2", "4:3"],
                    "frames_updated": [],
                    "frames_removed": [],
                    "component_version_bumps": ["AdminPanelHeader-v1.16", "DataTableComponent-v1.18"],
                    "changelog_highlights": ["table filtering improvements", "data pagination updates", "component accessibility enhancements"]
                }
            ),
            Action(
                name="filter_figma_artifacts_by_tags",
                kwargs={"tags": ["hero"]}
            ),
            Action(
                name="export_figma_artifacts_to_assets",
                kwargs={
                    "artifact_ids": ["art_001"],
                    "export_profile": {"format": "SVG", "scale": "1x"}
                }
            ),
            Action(
                name="generate_before_after_visuals",
                kwargs={
                    "release_id": "release_009",
                    "hero_artifact_ids": ["art_001"]
                }
            ),
            Action(
                name="create_gmail_thread",
                kwargs={
                    "sender_email": "alex.dev@company.com",
                    "recipients_emails": ["admin-team@company.com", "stakeholders@company.com"],
                    "workflow_type": "release",
                    "current_labels": ["admin", "data-table", "Design/Release"]
                }
            ),
            Action(
                name="create_gmail_message",
                kwargs={
                    "sender_email": "alex.dev@company.com",
                    "workflow_type": "release",
                    "thread_id": "thread_015",
                    "attachments_asset_ids": ["asset_art_001_svg_1x"]
                }
            )
        ],
        outputs=[{
            "release_info": {
                "release_id": "release_009",
                "version_tag": "admin-panel-v2.5.0",
                "release_name": "Admin Panel v2.5.0 - Data Table Components",
                "owner_email": "alex.dev@company.com"
            },
            "prior_release_id": "release_006",
            "frames_added": ["4:2", "4:3"],
            "component_version_bumps": ["AdminPanelHeader-v1.16", "DataTableComponent-v1.18"],
            "hero_artifacts": ["art_001"],
            "exported_assets": ["asset_art_001_svg_1x"],
            "visual_generated": "before_after_visual_release_009_5894",
            "thread_id": "thread_015",
            "message_id": "msg_017"
        }]
    ),
    Task(
        annotator="0",
        user_id="task_046",
        instruction=(
            "You need to perform a comprehensive design system audit for the Homepage Hero Section (art_001)."
        ),
        actions=[
            Action(
                name="create_audit_session",
                kwargs={"artifact_id": "art_001", "audit_type": "DS_MAPPING"}
            ),
            Action(
                name="identify_custom_groups_and_map_to_ds_components",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="record_ds_audit_findings",
                kwargs={
                    "audit_id": "audit_013",
                    "layer_id": "1:2",
                    "layer_name": "Homepage Hero Section",
                    "finding_type": "SUBSTITUTE_RECOMMENDED",
                    "recommended_component_id_nullable": "Homepage-v1.2",
                    # "code_connect_link_nullable": None,
                    "severity": "HIGH"
                }
            ),
            Action(
                name="generate_audit_report",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="link_audit_report_asset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            ),
            Action(
                name="update_audit_status",
                kwargs={"audit_id": "audit_013", "status": "COMPLETED"}
            )
        ],
        outputs=[{
            "audit_id": "audit_013",
            "finding_id": "finding_ds_016",
            "report_asset_id": "asset_019",
            # "audit_status": "COMPLETED"
        }]
    ),
    Task(
        annotator="0",
        user_id="task_047",
        instruction=(
            "You are a professional designer and need to conduct a thorough design system audit for the Product Features Display (art_002)."
        ),
        actions=[
            Action(
                name="create_audit_session",
                kwargs={"artifact_id": "art_002", "audit_type": "DS_MAPPING"}
            ),
            Action(
                name="identify_custom_groups_and_map_to_ds_components",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="record_ds_audit_findings",
                kwargs={
                    "audit_id": "audit_013",
                    "layer_id": "1:2",
                    "layer_name": "Navigation Bar",
                    "finding_type": "UNMAPPED",
                    "recommended_component_id_nullable": "Navigation-v2.3",
                    # "code_connect_link_nullable": None,
                    "severity": "HIGH"
                }
            ),
            Action(
                name="generate_audit_report",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="link_audit_report_asset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            ),
            Action(
                name="update_audit_status",
                kwargs={"audit_id": "audit_013", "status": "COMPLETED"}
            )
        ],
        outputs=[{
            "audit_id": "audit_013",
            "finding_id": "finding_ds_016",
            "report_asset_id": "asset_019",
            # "audit_status": "COMPLETED"
        }]
    ),
    Task(
        annotator="0",
        user_id="task_048",
        instruction=(
            "You are about to perform a big rebrand and you need to execute a design system audit on the User Navigation Menu (art_003)?"
        ),
        actions=[
            Action(
                name="create_audit_session",
                kwargs={"artifact_id": "art_003", "audit_type": "DS_MAPPING"}
            ),
            Action(
                name="identify_custom_groups_and_map_to_ds_components",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="record_ds_audit_findings",
                kwargs={
                    "audit_id": "audit_013",
                    "layer_id": "1:2",
                    "layer_name": "Design System",
                    "finding_type": "AMBIGUOUS",
                    "recommended_component_id_nullable": "Design-v1.4",
                    # "code_connect_link_nullable": None,
                    "severity": "HIGH"
                }
            ),
            Action(
                name="generate_audit_report",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="link_audit_report_asset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            ),
            Action(
                name="update_audit_status",
                kwargs={"audit_id": "audit_013", "status": "COMPLETED"}
            )
        ],
        outputs=[{
            "audit_id": "audit_013",
            "finding_id": "finding_ds_016",
            "report_asset_id": "asset_019",
            # "audit_status": "COMPLETED"
        }]
    ),
    Task(
        annotator="0",
        user_id="task_049",
        instruction=(
            "You have been notified that you must run a design system audit for the Footer Contact Form (art_004)."
        ),
        actions=[
            Action(
                name="create_audit_session",
                kwargs={"artifact_id": "art_004", "audit_type": "DS_MAPPING"}
            ),
            Action(
                name="identify_custom_groups_and_map_to_ds_components",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="record_ds_audit_findings",
                kwargs={
                    "audit_id": "audit_013",
                    "layer_id": "2:1",
                    "layer_name": "Mobile App Dashboard",
                    "finding_type": "SUBSTITUTE_RECOMMENDED",
                    "recommended_component_id_nullable": "Mobile-v2.5",
                    # "code_connect_link_nullable": None,
                    "severity": "HIGH"
                }
            ),
            Action(
                name="generate_audit_report",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="link_audit_report_asset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            ),
            Action(
                name="update_audit_status",
                kwargs={"audit_id": "audit_013", "status": "COMPLETED"}
            )
        ],
        outputs=[{
            "audit_id": "audit_013",
            "finding_id": "finding_ds_016",
            "report_asset_id": "asset_019",
        }]
    ),
    Task(
        annotator="0",
        user_id="task_050",
        instruction=(
            "You have been requested to perform a design system audit on the Shopping Cart Widget (art_005)."
        ),
        actions=[
            Action(
                name="create_audit_session",
                kwargs={"artifact_id": "art_005", "audit_type": "DS_MAPPING"}
            ),
            Action(
                name="identify_custom_groups_and_map_to_ds_components",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="record_ds_audit_findings",
                kwargs={
                    "audit_id": "audit_013",
                    "layer_id": "2:1",
                    "layer_name": "User Profile Screen",
                    "finding_type": "UNMAPPED",
                    "recommended_component_id_nullable": "User-v1.6",
                    # "code_connect_link_nullable": None,
                    "severity": "HIGH"
                }
            ),
            Action(
                name="generate_audit_report",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="link_audit_report_asset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            ),
            Action(
                name="update_audit_status",
                kwargs={"audit_id": "audit_013", "status": "COMPLETED"}
            )
        ],
        outputs=[{
            "audit_id": "audit_013",
            "finding_id": "finding_ds_016",
            "report_asset_id": "asset_019",
            # "audit_status": "COMPLETED"
        }]
    ),
    Task(
        annotator="0",
        user_id="task_051",
        instruction=(
            "You have been requested to analyze the Social Media Feed (art_006) with a design system audit."
        ),
        actions=[
            Action(
                name="create_audit_session",
                kwargs={"artifact_id": "art_006", "audit_type": "DS_MAPPING"}
            ),
            Action(
                name="identify_custom_groups_and_map_to_ds_components",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="record_ds_audit_findings",
                kwargs={
                    "audit_id": "audit_013",
                    "layer_id": "3:1",
                    "layer_name": "Marketing Website",
                    "finding_type": "AMBIGUOUS",
                    "recommended_component_id_nullable": "Marketing-v2.7",
                    # "code_connect_link_nullable": None,
                    "severity": "HIGH"
                }
            ),
            Action(
                name="generate_audit_report",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="link_audit_report_asset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            ),
            Action(
                name="update_audit_status",
                kwargs={"audit_id": "audit_013", "status": "COMPLETED"}
            )
        ],
        outputs=[{
            "audit_id": "audit_013",
            "finding_id": "finding_ds_016",
            "report_asset_id": "asset_019",
            # "audit_status": "COMPLETED"
        }]
    ),
    Task(
        annotator="0",
        user_id="task_052",
        instruction=(
            "You would like to assess the Mobile App Sidebar (art_007) through a design system audit."
        ),
        actions=[
            Action(
                name="create_audit_session",
                kwargs={"artifact_id": "art_007", "audit_type": "DS_MAPPING"}
            ),
            Action(
                name="identify_custom_groups_and_map_to_ds_components",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="record_ds_audit_findings",
                kwargs={
                    "audit_id": "audit_013",
                    "layer_id": "3:2",
                    "layer_name": "Pricing Page",
                    "finding_type": "SUBSTITUTE_RECOMMENDED",
                    "recommended_component_id_nullable": "Pricing-v1.8",
                    # "code_connect_link_nullable": None,
                    "severity": "LOW"
                }
            ),
            Action(
                name="generate_audit_report",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="link_audit_report_asset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            ),
            Action(
                name="update_audit_status",
                kwargs={"audit_id": "audit_013", "status": "COMPLETED"}
            )
        ],
        outputs=[{
            "audit_id": "audit_013",
            "finding_id": "finding_ds_016",
            "report_asset_id": "asset_019",
            # "audit_status": "COMPLETED"
        }]
    ),
    Task(
        annotator="0",
        user_id="task_053",
        instruction=(
            "You would like to test your new workflow for design system audits on the Dashboard Charts Panel (art_008)."
        ),
        actions=[
            Action(
                name="create_audit_session",
                kwargs={"artifact_id": "art_008", "audit_type": "DS_MAPPING"}
            ),
            Action(
                name="identify_custom_groups_and_map_to_ds_components",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="record_ds_audit_findings",
                kwargs={
                    "audit_id": "audit_013",
                    "layer_id": "4:1",
                    "layer_name": "Admin Panel Header",
                    "finding_type": "UNMAPPED",
                    "recommended_component_id_nullable": "Admin-v2.9",
                    # "code_connect_link_nullable": None,
                    "severity": "LOW"
                }
            ),
            Action(
                name="generate_audit_report",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="link_audit_report_asset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            ),
            Action(
                name="update_audit_status",
                kwargs={"audit_id": "audit_013", "status": "COMPLETED"}
            )
        ],
        outputs=[{
            "audit_id": "audit_013",
            "finding_id": "finding_ds_016",
            "report_asset_id": "asset_019",
            # "audit_status": "COMPLETED"
        }]
    ),
    Task(
        annotator="0",
        user_id="task_054",
        instruction=(
            "You must initiate a design system audit on the Login Modal Dialog (art_009) to evaluate the work of a new team member."
        ),
        actions=[
            Action(
                name="create_audit_session",
                kwargs={"artifact_id": "art_009", "audit_type": "DS_MAPPING"}
            ),
            Action(
                name="identify_custom_groups_and_map_to_ds_components",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="record_ds_audit_findings",
                kwargs={
                    "audit_id": "audit_013",
                    "layer_id": "4:1",
                    "layer_name": "Data Table Component",
                    "finding_type": "AMBIGUOUS",
                    "recommended_component_id_nullable": "Data-v1.0",
                    # "code_connect_link_nullable": None,
                    "severity": "LOW"
                }
            ),
            Action(
                name="generate_audit_report",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="link_audit_report_asset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            ),
            Action(
                name="update_audit_status",
                kwargs={"audit_id": "audit_013", "status": "COMPLETED"}
            )
        ],
        outputs=[{
            "audit_id": "audit_013",
            "finding_id": "finding_ds_016",
            "report_asset_id": "asset_019",
            # "audit_status": "COMPLETED"
        }]
    ),
    Task(
        annotator="0",
        user_id="task_055",
        instruction=(
            "You have been requested by your boss to evaluate the Search Results Layout (art_010) using a design system audit."
        ),
        actions=[
            Action(
                name="create_audit_session",
                kwargs={"artifact_id": "art_010", "audit_type": "DS_MAPPING"}
            ),
            Action(
                name="identify_custom_groups_and_map_to_ds_components",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="record_ds_audit_findings",
                kwargs={
                    "audit_id": "audit_013",
                    "layer_id": "5:1",
                    "layer_name": "Brand Guidelines",
                    "finding_type": "SUBSTITUTE_RECOMMENDED",
                    "recommended_component_id_nullable": "Brand-v1.2",
                    # "code_connect_link_nullable": None,
                    "severity": "LOW"
                }
            ),
            Action(
                name="generate_audit_report",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="link_audit_report_asset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            ),
            Action(
                name="update_audit_status",
                kwargs={"audit_id": "audit_013", "status": "COMPLETED"}
            )
        ],
        outputs=[{
            "audit_id": "audit_013",
            "finding_id": "finding_ds_016",
            "report_asset_id": "asset_019",
            # "audit_status": "COMPLETED"
        }]
    ),
    Task(
        annotator="0",
        user_id="task_056",
        instruction=(
            "You must execute a design system audit on the Profile Settings Card (art_011) to ensure that your design systems make sense."
        ),
        actions=[
            Action(
                name="create_audit_session",
                kwargs={"artifact_id": "art_011", "audit_type": "DS_MAPPING"}
            ),
            Action(
                name="identify_custom_groups_and_map_to_ds_components",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="record_ds_audit_findings",
                kwargs={
                    "audit_id": "audit_013",
                    "layer_id": "1:2",
                    "layer_name": "Contact Form Component",
                    "finding_type": "UNMAPPED",
                    "recommended_component_id_nullable": "Contact-v2.3",
                    # "code_connect_link_nullable": None,
                    "severity": "LOW"
                }
            ),
            Action(
                name="generate_audit_report",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="link_audit_report_asset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            ),
            Action(
                name="update_audit_status",
                kwargs={"audit_id": "audit_013", "status": "COMPLETED"}
            )
        ],
        outputs=[{
            "audit_id": "audit_013",
            "finding_id": "finding_ds_016",
            "report_asset_id": "asset_019",
            # "audit_status": "COMPLETED"
        }]
    ),
    Task(
        annotator="0",
        user_id="task_057",
        instruction=(
            "You are releasing a new app and must perform a design system audit for the Notification Center (art_012)?"
        ),
        actions=[
            Action(
                name="create_audit_session",
                kwargs={"artifact_id": "art_012", "audit_type": "DS_MAPPING"}
            ),
            Action(
                name="identify_custom_groups_and_map_to_ds_components",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="record_ds_audit_findings",
                kwargs={
                    "audit_id": "audit_013",
                    "layer_id": "2:1",
                    "layer_name": "Settings Screen",
                    "finding_type": "AMBIGUOUS",
                    "recommended_component_id_nullable": "Settings-v1.4",
                    # "code_connect_link_nullable": None,
                    "severity": "LOW"
                }
            ),
            Action(
                name="generate_audit_report",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="link_audit_report_asset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            ),
            Action(
                name="update_audit_status",
                kwargs={"audit_id": "audit_013", "status": "COMPLETED"}
            )
        ],
        outputs=[{
            "audit_id": "audit_013",
            "finding_id": "finding_ds_016",
            "report_asset_id": "asset_019",
            # "audit_status": "COMPLETED"
        }]
    ),
    Task(
        annotator="0",
        user_id="task_058",
        instruction=(
            "You need to perform an accessibility audit on the Navigation Bar artifact."
        ),
        actions=[
            Action(
                name="get_artifact_id_from_name",
                kwargs={"artifact_name": "Navigation Bar"}
            ),
            Action(
                name="create_audit_session",
                kwargs={"artifact_id": "art_002", "audit_type": "A11Y"}
            ),
            Action(
                name="evaluate_accessibility",
                kwargs={"artifact_id": "art_002"}
            ),
            Action(
                name="record_accessibility_audit_findings",
                kwargs={
                    "audit_id": "audit_013",
                    "layer_id": "1:2",
                    "layer_name": "Navigation Bar",
                    "violation_type": "RTL",
                    "violation_details_json": {"issue": "Icon alignment", "description": "Layout doesn't adapt to RTL languages"},
                    "severity": "HIGH",
                    "recommended_fix_summary": "Implement flexible layout that supports RTL languages"
                }
            ),
            Action(
                name="generate_audit_report",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="link_audit_report_asset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            ),
            Action(
                name="update_audit_status",
                kwargs={"audit_id": "audit_013", "status": "COMPLETED"}
            )
        ],
        outputs=[{
            "audit_id": "audit_013",
            "finding_id": "finding_a11y_016",
            "report_asset_id": "asset_019",
            # "audit_status": "COMPLETED"
        }]
    ),
    Task(
        annotator="0",
        user_id="task_059",
        instruction=(
            "You need to conduct an accessibility audit for the Homepage Hero Section. The task involves finding the artifact, creating an audit session, evaluating accessibility issues, recording findings, generating a report, linking the report to the audit, and completing the audit. Return the audit session details, accessibility violations found, audit findings recorded, and the final audit report asset information."
        ),
        actions=[
            Action(
                name="get_artifact_id_from_name",
                kwargs={"artifact_name": "Homepage Hero Section"}
            ),
            Action(
                name="create_audit_session",
                kwargs={"artifact_id": "art_001", "audit_type": "A11Y"}
            ),
            Action(
                name="evaluate_accessibility",
                kwargs={"artifact_id": "art_001"}
            ),
            Action(
                name="record_accessibility_audit_findings",
                kwargs={
                    "audit_id": "audit_013",
                    "layer_id": "1:2",
                    "layer_name": "Homepage Hero Section",
                    "violation_type": "TEXT_SIZING",
                    "violation_details_json": {"current_size": "12px", "required_size": "16px", "description": "Text too small for readability"},
                    "severity": "HIGH",
                    "recommended_fix_summary": "Increase font size to minimum 16px for better readability"
                }
            ),
            Action(
                name="generate_audit_report",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="link_audit_report_asset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            ),
            Action(
                name="update_audit_status",
                kwargs={"audit_id": "audit_013", "status": "COMPLETED"}
            )
        ],
        outputs=[{
            "audit_id": "audit_013",
            "finding_id": "finding_a11y_016",
            "report_asset_id": "asset_019",
            # "audit_status": "COMPLETED"
        }]
    ),
    Task(
        annotator="0",
        user_id="task_060",
        instruction=(
            "You need to perform an accessibility audit on the Contact Form Component artifact using workflow 3b."
        ),
        actions=[
            Action(
                name="get_artifact_id_from_name",
                kwargs={"artifact_name": "Contact Form Component"}
            ),
            Action(
                name="create_audit_session",
                kwargs={"artifact_id": "art_011", "audit_type": "A11Y"}
            ),
            Action(
                name="evaluate_accessibility",
                kwargs={"artifact_id": "art_011"}
            ),
            Action(
                name="record_accessibility_audit_findings",
                kwargs={
                    "audit_id": "audit_013",
                    "layer_id": "1:2",
                    "layer_name": "Contact Form Component",
                    "violation_type": "CONTRAST",
                    "violation_details_json": {"current_ratio": "2.1:1", "required_ratio": "4.5:1", "colors": {"foreground": "#666666", "background": "#ffffff"}},
                    "severity": "MEDIUM",
                    "recommended_fix_summary": "Increase text color contrast to meet WCAG AA standards"
                }
            ),
            Action(
                name="generate_audit_report",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="link_audit_report_asset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            ),
            Action(
                name="update_audit_status",
                kwargs={"audit_id": "audit_013", "status": "COMPLETED"}
            )
        ],
        outputs=[{
            "audit_id": "audit_013",
            "finding_id": "finding_a11y_016",
            "report_asset_id": "asset_019",
            # "audit_status": "COMPLETED"
        }]
    ),
    Task(
        annotator="0",
        user_id="task_061",
        instruction=(
            "You need to perform an accessibility audit on the Data Table Component artifact using workflow 3b."
        ),
        actions=[
            Action(
                name="get_artifact_id_from_name",
                kwargs={"artifact_name": "Data Table Component"}
            ),
            Action(
                name="create_audit_session",
                kwargs={"artifact_id": "art_009", "audit_type": "A11Y"}
            ),
            Action(
                name="evaluate_accessibility",
                kwargs={"artifact_id": "art_009"}
            ),
            Action(
                name="record_accessibility_audit_findings",
                kwargs={
                    "audit_id": "audit_013",
                    "layer_id": "4:1",
                    "layer_name": "Data Table Component",
                    "violation_type": "TEXT_SIZING",
                    "violation_details_json": {"current_size": "12px", "required_size": "16px", "description": "Text too small for readability"},
                    "severity": "HIGH",
                    "recommended_fix_summary": "Increase font size to minimum 16px for better readability"
                }
            ),
            Action(
                name="generate_audit_report",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="link_audit_report_asset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            ),
            Action(
                name="update_audit_status",
                kwargs={"audit_id": "audit_013", "status": "COMPLETED"}
            )
        ],
        outputs=[{
            "audit_id": "audit_013",
            "finding_id": "finding_a11y_016",
            "report_asset_id": "asset_019",
            # "audit_status": "COMPLETED"
        }]
    ),
    Task(
        annotator="0",
        user_id="task_062",
        instruction=(
            "You need to perform an accessibility audit on the Settings Screen artifact using workflow 3b."
        ),
        actions=[
            Action(
                name="get_artifact_id_from_name",
                kwargs={"artifact_name": "Settings Screen"}
            ),
            Action(
                name="create_audit_session",
                kwargs={"artifact_id": "art_012", "audit_type": "A11Y"}
            ),
            Action(
                name="evaluate_accessibility",
                kwargs={"artifact_id": "art_012"}
            ),
            Action(
                name="record_accessibility_audit_findings",
                kwargs={
                    "audit_id": "audit_013",
                    "layer_id": "2:1",
                    "layer_name": "Settings Screen",
                    "violation_type": "TEXT_SIZING",
                    "violation_details_json": {"current_size": "12px", "required_size": "16px", "description": "Text too small for readability"},
                    "severity": "MEDIUM",
                    "recommended_fix_summary": "Increase font size to minimum 16px for better readability"
                }
            ),
            Action(
                name="generate_audit_report",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="link_audit_report_asset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            ),
            Action(
                name="update_audit_status",
                kwargs={"audit_id": "audit_013", "status": "COMPLETED"}
            )
        ],
        outputs=[{
            "audit_id": "audit_013",
            "finding_id": "finding_a11y_016",
            "report_asset_id": "asset_019",
            # "audit_status": "COMPLETED"
        }]
    ),
    Task(
        annotator="0",
        user_id="task_063",
        instruction=(
            "You need to perform an accessibility audit on the Admin Panel Header artifact using workflow 3b."
        ),
        actions=[
            Action(
                name="get_artifact_id_from_name",
                kwargs={"artifact_name": "Admin Panel Header"}
            ),
            Action(
                name="create_audit_session",
                kwargs={"artifact_id": "art_008", "audit_type": "A11Y"}
            ),
            Action(
                name="evaluate_accessibility",
                kwargs={"artifact_id": "art_008"}
            ),
            Action(
                name="record_accessibility_audit_findings",
                kwargs={
                    "audit_id": "audit_013",
                    "layer_id": "4:1",
                    "layer_name": "Admin Panel Header",
                    "violation_type": "CONTRAST",
                    "violation_details_json": {"current_ratio": "2.8:1", "required_ratio": "4.5:1", "colors": {"foreground": "#666666", "background": "#ffffff"}},
                    "severity": "HIGH",
                    "recommended_fix_summary": "Increase text color contrast to meet WCAG AA standards"
                }
            ),
            Action(
                name="generate_audit_report",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="link_audit_report_asset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            ),
            Action(
                name="update_audit_status",
                kwargs={"audit_id": "audit_013", "status": "COMPLETED"}
            )
        ],
        outputs=[{
            "audit_id": "audit_013",
            "finding_id": "finding_a11y_016",
            "report_asset_id": "asset_019",
            # "audit_status": "COMPLETED"
        }]
    ),
    Task(
        annotator="0",
        user_id="task_064",
        instruction=(
            "You need to conduct a comprehensive accessibility audit for the Pricing Page design component. "
            "You should perform a thorough evaluation to identify potential accessibility violations and create "
            "a detailed audit report. You will record any findings with HIGH severity issues that need "
            "immediate attention, generate a comprehensive PDF audit report, and update the audit status to "
            "COMPLETED when finished."
        ),
        actions=[
            Action(
                name="get_artifact_id_from_name",
                kwargs={"artifact_name": "Pricing Page"}
            ),
            Action(
                name="create_audit_session",
                kwargs={"artifact_id": "art_007", "audit_type": "A11Y"}
            ),
            Action(
                name="evaluate_accessibility",
                kwargs={"artifact_id": "art_007"}
            ),
            Action(
                name="record_accessibility_audit_findings",
                kwargs={
                    "audit_id": "audit_013",
                    "layer_id": "3:2",
                    "layer_name": "Pricing Page",
                    "violation_type": "TOUCH_TARGET",
                    "violation_details_json": {
                        "current_size": "32x32px",
                        "required_size": "44x44px",
                        "description": "Touch target too small for mobile accessibility"
                    },
                    "severity": "HIGH",
                    "recommended_fix_summary": "Increase button size to minimum 44x44px for touch accessibility"
                }
            ),
            Action(
                name="generate_audit_report",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="link_audit_report_asset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            ),
            Action(
                name="update_audit_status",
                kwargs={"audit_id": "audit_013", "status": "COMPLETED"}
            )
        ],
        outputs=[{
            "audit_id": "audit_013",
            "finding_id": "finding_a11y_016",
            "report_asset_id": "asset_019",
            # "audit_status": "COMPLETED"
        }]
    ),
    Task(
        annotator="0",
        user_id="task_065",
        instruction=(
            "You need to conduct a comprehensive accessibility audit for the Mobile App Dashboard design. "
            "You should evaluate the interface for color contrast compliance and other accessibility standards "
            "to ensure WCAG AA conformance. Your analysis will identify any violations that prevent users with "
            "visual impairments from effectively using the dashboard. You will document any HIGH severity "
            "contrast issues and generate a detailed audit report with specific remediation recommendations."
        ),
        actions=[
            Action(
                name="get_artifact_id_from_name",
                kwargs={"artifact_name": "Mobile App Dashboard"}
            ),
            Action(
                name="create_audit_session",
                kwargs={"artifact_id": "art_004", "audit_type": "A11Y"}
            ),
            Action(
                name="evaluate_accessibility",
                kwargs={"artifact_id": "art_004"}
            ),
            Action(
                name="record_accessibility_audit_findings",
                kwargs={
                    "audit_id": "audit_013",
                    "layer_id": "2:1",
                    "layer_name": "Mobile App Dashboard",
                    "violation_type": "CONTRAST",
                    "violation_details_json": {
                        "current_ratio": "2.1:1",
                        "required_ratio": "4.5:1",
                        "colors": {
                            "foreground": "#777777",
                            "background": "#ffffff"
                        }
                    },
                    "severity": "HIGH",
                    "recommended_fix_summary": "Increase text color contrast to meet WCAG AA standards"
                }
            ),
            Action(
                name="generate_audit_report",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="link_audit_report_asset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            ),
            Action(
                name="update_audit_status",
                kwargs={"audit_id": "audit_013", "status": "COMPLETED"}
            )
        ],
        outputs=[{
            "audit_id": "audit_013",
            "finding_id": "finding_a11y_016",
            "report_asset_id": "asset_019",
            # "audit_status": "COMPLETED"
        }]
    ),
    Task(
        annotator="0",
        user_id="task_066",
        instruction=(
            "You need to perform a comprehensive accessibility audit for the Design System page to ensure "
            "all design components meet accessibility standards. Your audit will "
            "identify any HIGH severity violations that require immediate remediation and generate a detailed "
            "PDF report with specific recommendations for improving accessibility compliance."
        ),
        actions=[
            Action(
                name="get_artifact_id_from_name",
                kwargs={"artifact_name": "Design System"}
            ),
            Action(
                name="create_audit_session",
                kwargs={"artifact_id": "art_003", "audit_type": "A11Y"}
            ),
            Action(
                name="evaluate_accessibility",
                kwargs={"artifact_id": "art_003"}
            ),
            Action(
                name="record_accessibility_audit_findings",
                kwargs={
                    "audit_id": "audit_013",
                    "layer_id": "1:2",
                    "layer_name": "Design System",
                    "violation_type": "TOUCH_TARGET",
                    "violation_details_json": {
                        "current_size": "40x40px",
                        "required_size": "44x44px",
                        "description": "Touch target too small for mobile accessibility"
                    },
                    "severity": "HIGH",
                    "recommended_fix_summary": "Increase button size to minimum 44x44px for touch accessibility"
                }
            ),
            Action(
                name="generate_audit_report",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="link_audit_report_asset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            ),
            Action(
                name="update_audit_status",
                kwargs={"audit_id": "audit_013", "status": "COMPLETED"}
            )
        ],
        outputs=[{
            "audit_id": "audit_013",
            "finding_id": "finding_a11y_016",
            "report_asset_id": "asset_019",
            # "audit_status": "COMPLETED"
        }]
    ),
    Task(
        annotator="0",
        user_id="task_067",
        instruction=(
            "You need to conduct a thorough accessibility audit for the User Profile Screen to ensure "
            "optimal usability for all users. You should evaluate text sizing, readability standards, "
            "and other accessibility compliance factors to identify areas needing improvement. Your audit "
            "will focus on HIGH severity text sizing issues that impact user experience and generate a "
            "comprehensive report with actionable recommendations for meeting accessibility guidelines."
        ),
        actions=[
            Action(
                name="get_artifact_id_from_name",
                kwargs={"artifact_name": "User Profile Screen"}
            ),
            Action(
                name="create_audit_session",
                kwargs={"artifact_id": "art_005", "audit_type": "A11Y"}
            ),
            Action(
                name="evaluate_accessibility",
                kwargs={"artifact_id": "art_005"}
            ),
            Action(
                name="record_accessibility_audit_findings",
                kwargs={
                    "audit_id": "audit_013",
                    "layer_id": "2:1",
                    "layer_name": "User Profile Screen",
                    "violation_type": "TEXT_SIZING",
                    "violation_details_json": {
                        "current_size": "12px",
                        "required_size": "16px",
                        "description": "Text too small for readability"
                    },
                    "severity": "HIGH",
                    "recommended_fix_summary": "Increase font size to minimum 16px for better readability"
                }
            ),
            Action(
                name="generate_audit_report",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="link_audit_report_asset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            ),
            Action(
                name="update_audit_status",
                kwargs={"audit_id": "audit_013", "status": "COMPLETED"}
            )
        ],
        outputs=[{
            "audit_id": "audit_013",
            "finding_id": "finding_a11y_016",
            "report_asset_id": "asset_019",
            # "audit_status": "COMPLETED"
        }]
    ),
    Task(
        annotator="0",
        user_id="task_068",
        instruction=(
            "You need to perform an accessibility audit on the Marketing Website. "
            "You want to identify any RTL language support issues and generate a comprehensive audit report."
        ),
        actions=[
            Action(
                name="get_artifact_id_from_name",
                kwargs={"artifact_name": "Marketing Website"}
            ),
            Action(
                name="create_audit_session",
                kwargs={"artifact_id": "art_006", "audit_type": "A11Y"}
            ),
            Action(
                name="evaluate_accessibility",
                kwargs={"artifact_id": "art_006"}
            ),
            Action(
                name="record_accessibility_audit_findings",
                kwargs={
                    "audit_id": "audit_013",
                    "layer_id": "3:1",
                    "layer_name": "Marketing Website",
                    "violation_type": "RTL",
                    "violation_details_json": {"issue": "Icon alignment", "description": "Layout doesn't adapt to RTL languages"},
                    "severity": "HIGH",
                    "recommended_fix_summary": "Implement flexible layout that supports RTL languages"
                }
            ),
            Action(
                name="generate_audit_report",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="link_audit_report_asset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            ),
            Action(
                name="update_audit_status",
                kwargs={"audit_id": "audit_013", "status": "COMPLETED"}
            )
        ],
        outputs=[{"audit_id": "audit_013", "finding_id": "finding_a11y_016", "report_asset_id": "asset_019"}]
    ),
    Task(
        annotator="0",
        user_id="task_069",
        instruction=(
            "You need to perform an accessibility audit on the Brand Guidelines. "
            "You want to identify any touch target sizing issues and generate a comprehensive audit report."
        ),
        actions=[
            Action(
                name="get_artifact_id_from_name",
                kwargs={"artifact_name": "Brand Guidelines"}
            ),
            Action(
                name="create_audit_session",
                kwargs={"artifact_id": "art_010", "audit_type": "A11Y"}
            ),
            Action(
                name="evaluate_accessibility",
                kwargs={"artifact_id": "art_010"}
            ),
            Action(
                name="record_accessibility_audit_findings",
                kwargs={
                    "audit_id": "audit_013",
                    "layer_id": "5:1",
                    "layer_name": "Brand Guidelines",
                    "violation_type": "TOUCH_TARGET",
                    "violation_details_json": {"current_size": "40x40px", "required_size": "44x44px", "description": "Touch target too small for mobile accessibility"},
                    "severity": "MEDIUM",
                    "recommended_fix_summary": "Increase button size to minimum 44x44px for touch accessibility"
                }
            ),
            Action(
                name="generate_audit_report",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="link_audit_report_asset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            ),
            Action(
                name="update_audit_status",
                kwargs={"audit_id": "audit_013", "status": "COMPLETED"}
            )
        ],
        outputs=[{"audit_id": "audit_013", "finding_id": "finding_a11y_016", "report_asset_id": "asset_019"}]
    ),
    Task(
        annotator="0",
        user_id="task_070",
        instruction=(
            "You need to perform a combined design system and accessibility audit on the Homepage Hero Section. "
            "You want to identify both design system compliance issues and accessibility violations to ensure comprehensive quality standards."
        ),
        actions=[
            Action(
                name="get_artifact_id_from_name",
                kwargs={"artifact_name": "Homepage Hero Section"}
            ),
            Action(
                name="create_audit_session",
                kwargs={"artifact_id": "art_001", "audit_type": "COMBINED_DS_A11Y"}
            ),
            Action(
                name="identify_custom_groups_and_map_to_ds_components",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="record_ds_audit_findings",
                kwargs={
                    "audit_id": "audit_013",
                    "layer_id": "1:2",
                    "layer_name": "Homepage Hero Section",
                    "finding_type": "SUBSTITUTE_RECOMMENDED",
                    "recommended_component_id_nullable": "Homepage-v1.2",
                    "severity": "HIGH"
                }
            ),
            Action(
                name="evaluate_accessibility",
                kwargs={"artifact_id": "art_001"}
            ),
            Action(
                name="record_accessibility_audit_findings",
                kwargs={
                    "audit_id": "audit_013",
                    "layer_id": "1:2",
                    "layer_name": "Homepage Hero Section",
                    "violation_type": "TEXT_SIZING",
                    "violation_details_json": {"current_size": "12px", "required_size": "16px", "description": "Text too small for readability"},
                    "severity": "HIGH",
                    "recommended_fix_summary": "Increase font size to minimum 16px for better readability"
                }
            ),
            Action(
                name="generate_audit_report",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="update_audit_status",
                kwargs={"audit_id": "audit_013", "status": "COMPLETED"}
            ),
            Action(
                name="link_audit_report_asset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            )
        ],
        outputs=[{"audit_id": "audit_013", "finding_ds_id": "finding_ds_016", "finding_a11y_id": "finding_a11y_016", "report_asset_id": "asset_019"}]
    ),
    Task(
        annotator="0",
        user_id="task_071",
        instruction=(
            "You want to perform a comprehensive combined design system and accessibility audit on the Navigation Bar artifact. "
            "This will evaluate both design system component mapping and accessibility compliance in a single comprehensive audit process."
        ),
        actions=[
            Action(
                name="get_artifact_id_from_name",
                kwargs={"artifact_name": "Navigation Bar"}
            ),
            Action(
                name="create_audit_session",
                kwargs={"artifact_id": "art_002", "audit_type": "COMBINED_DS_A11Y"}
            ),
            Action(
                name="identify_custom_groups_and_map_to_ds_components",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="record_ds_audit_findings",
                kwargs={"audit_id": "audit_013", "layer_id": "1:2", "layer_name": "Navigation Bar", "finding_type": "UNMAPPED", "recommended_component_id_nullable": "Navigation-v2.3", "severity": "HIGH"}
            ),
            Action(
                name="evaluate_accessibility",
                kwargs={"artifact_id": "art_002"}
            ),
            Action(
                name="record_accessibility_audit_findings",
                kwargs={"audit_id": "audit_013", "layer_id": "1:2", "layer_name": "Navigation Bar", "violation_type": "RTL", "violation_details_json": {"issue": "Icon alignment", "description": "Layout doesn't adapt to RTL languages"}, "severity": "HIGH", "recommended_fix_summary": "Implement flexible layout that supports RTL languages"}
            ),
            Action(
                name="generate_audit_report",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="update_audit_status",
                kwargs={"audit_id": "audit_013", "status": "COMPLETED"}
            ),
            Action(
                name="link_audit_report_asset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            )
        ],
        outputs=[{"audit_id": "audit_013", "finding_ds_id": "finding_ds_016", "finding_a11y_id": "finding_a11y_016", "report_asset_id": "asset_019"}]
    ),
    Task(
        annotator="0",
        user_id="task_072",
        instruction=(
            "You want to perform a comprehensive combined design system and accessibility audit on the Design System artifact. "
            "This will evaluate both design system component mapping and accessibility compliance in a single comprehensive audit process."
        ),
        actions=[
            Action(
                name="get_artifact_id_from_name",
                kwargs={"artifact_name": "Design System"}
            ),
            Action(
                name="create_audit_session",
                kwargs={"artifact_id": "art_003", "audit_type": "COMBINED_DS_A11Y"}
            ),
            Action(
                name="identify_custom_groups_and_map_to_ds_components",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="record_ds_audit_findings",
                kwargs={"audit_id": "audit_013", "layer_id": "1:2", "layer_name": "Design System", "finding_type": "AMBIGUOUS", "recommended_component_id_nullable": "Design-v1.4", "severity": "HIGH"}
            ),
            Action(
                name="evaluate_accessibility",
                kwargs={"artifact_id": "art_003"}
            ),
            Action(
                name="record_accessibility_audit_findings",
                kwargs={"audit_id": "audit_013", "layer_id": "1:2", "layer_name": "Design System", "violation_type": "TOUCH_TARGET", "violation_details_json": {"current_size": "40x40px", "required_size": "44x44px", "description": "Touch target too small for mobile accessibility"}, "severity": "HIGH", "recommended_fix_summary": "Increase button size to minimum 44x44px for touch accessibility"}
            ),
            Action(
                name="generate_audit_report",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="update_audit_status",
                kwargs={"audit_id": "audit_013", "status": "COMPLETED"}
            ),
            Action(
                name="link_audit_report_asset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            )
        ],
        outputs=[{"audit_id": "audit_013", "finding_ds_id": "finding_ds_016", "finding_a11y_id": "finding_a11y_016", "report_asset_id": "asset_019"}]
    ),
    Task(
        annotator="0",
        user_id="task_073",
        instruction=(
            "You want to perform a comprehensive combined design system and accessibility audit on the Mobile App Dashboard artifact. "
            "This will evaluate both design system component mapping and accessibility compliance in a single comprehensive audit process."
        ),
        actions=[
            Action(
                name="get_artifact_id_from_name",
                kwargs={"artifact_name": "Mobile App Dashboard"}
            ),
            Action(
                name="create_audit_session",
                kwargs={"artifact_id": "art_004", "audit_type": "COMBINED_DS_A11Y"}
            ),
            Action(
                name="identify_custom_groups_and_map_to_ds_components",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="record_ds_audit_findings",
                kwargs={"audit_id": "audit_013", "layer_id": "2:1", "layer_name": "Mobile App Dashboard", "finding_type": "SUBSTITUTE_RECOMMENDED", "recommended_component_id_nullable": "Mobile-v2.5", "severity": "HIGH"}
            ),
            Action(
                name="evaluate_accessibility",
                kwargs={"artifact_id": "art_004"}
            ),
            Action(
                name="record_accessibility_audit_findings",
                kwargs={"audit_id": "audit_013", "layer_id": "2:1", "layer_name": "Mobile App Dashboard", "violation_type": "CONTRAST", "violation_details_json": {"current_ratio": "2.1:1", "required_ratio": "4.5:1", "colors": {"foreground": "#777777", "background": "#ffffff"}}, "severity": "HIGH", "recommended_fix_summary": "Increase text color contrast to meet WCAG AA standards"}
            ),
            Action(
                name="generate_audit_report",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="update_audit_status",
                kwargs={"audit_id": "audit_013", "status": "COMPLETED"}
            ),
            Action(
                name="link_audit_report_asset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            )
        ],
        outputs=[{"audit_id": "audit_013", "finding_ds_id": "finding_ds_016", "finding_a11y_id": "finding_a11y_016", "report_asset_id": "asset_019"}]
    ),
    Task(
        annotator="0",
        user_id="task_074",
        instruction=(
            "You are conducting a combined design system and accessibility audit using workflow 3c. "
            "You want to perform a comprehensive audit of the 'User Profile Screen' artifact to identify "
            "both design system mapping issues and accessibility violations. The audit should evaluate "
            "component compliance with the design system and check for accessibility standards including "
            "text sizing, touch targets, and contrast requirements."
        ),
        actions=[
            Action(
                name="get_artifact_id_from_name",
                kwargs={"artifact_name": "User Profile Screen"}
            ),
            Action(
                name="create_audit_session",
                kwargs={"artifact_id": "art_005", "audit_type": "COMBINED_DS_A11Y"}
            ),
            Action(
                name="identify_custom_groups_and_map_to_ds_components",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="record_ds_audit_findings",
                kwargs={
                    "audit_id": "audit_013",
                    "layer_id": "2:1",
                    "layer_name": "User Profile Screen",
                    "finding_type": "UNMAPPED",
                    "recommended_component_id_nullable": "User-v1.6",
                    # "code_connect_link_nullable": "",
                    "severity": "HIGH"
                }
            ),
            Action(
                name="evaluate_accessibility",
                kwargs={"artifact_id": "art_005"}
            ),
            Action(
                name="record_accessibility_audit_findings",
                kwargs={
                    "audit_id": "audit_013",
                    "layer_id": "2:1",
                    "layer_name": "User Profile Screen",
                    "violation_type": "TEXT_SIZING",
                    "violation_details_json": {
                        "current_size": "12px",
                        "required_size": "16px",
                        "description": "Text too small for readability"
                    },
                    "severity": "HIGH",
                    "recommended_fix_summary": "Increase font size to minimum 16px for better readability"
                }
            ),
            Action(
                name="generate_audit_report",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="update_audit_status",
                kwargs={"audit_id": "audit_013", "status": "COMPLETED"}
            ),
            Action(
                name="link_audit_report_asset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            )
        ],
        outputs=[{
            "audit_id": "audit_013",
            "ds_finding_id": "finding_ds_016",
            "a11y_finding_id": "finding_a11y_016",
            "report_asset_id": "asset_019"
        }]
    ),
    Task(
        annotator="0",
        user_id="task_075",
        instruction=(
            "You are conducting a combined design system and accessibility audit using workflow 3c. "
            "You want to perform a comprehensive audit of the 'Marketing Website' artifact to identify "
            "both design system mapping issues and accessibility violations. The audit should evaluate "
            "component compliance with the design system and check for accessibility standards including "
            "RTL support, touch targets, and design component clarity."
        ),
        actions=[
            Action(
                name="get_artifact_id_from_name",
                kwargs={"artifact_name": "Marketing Website"}
            ),
            Action(
                name="create_audit_session",
                kwargs={"artifact_id": "art_006", "audit_type": "COMBINED_DS_A11Y"}
            ),
            Action(
                name="identify_custom_groups_and_map_to_ds_components",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="record_ds_audit_findings",
                kwargs={
                    "audit_id": "audit_013",
                    "layer_id": "3:1",
                    "layer_name": "Marketing Website",
                    "finding_type": "AMBIGUOUS",
                    "recommended_component_id_nullable": "Marketing-v2.7",
                    # "code_connect_link_nullable": "null",
                    "severity": "HIGH"
                }
            ),
            Action(
                name="evaluate_accessibility",
                kwargs={"artifact_id": "art_006"}
            ),
            Action(
                name="record_accessibility_audit_findings",
                kwargs={
                    "audit_id": "audit_013",
                    "layer_id": "3:1",
                    "layer_name": "Marketing Website",
                    "violation_type": "RTL",
                    "violation_details_json": {
                        "issue": "Icon alignment",
                        "description": "Layout doesn't adapt to RTL languages"
                    },
                    "severity": "HIGH",
                    "recommended_fix_summary": "Implement flexible layout that supports RTL languages"
                }
            ),
            Action(
                name="generate_audit_report",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="update_audit_status",
                kwargs={"audit_id": "audit_013", "status": "COMPLETED"}
            ),
            Action(
                name="link_audit_report_asset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            )
        ],
        outputs=[{
            "audit_id": "audit_013",
            "ds_finding_id": "finding_ds_016",
            "a11y_finding_id": "finding_a11y_016",
            "report_asset_id": "asset_019"
        }]
    ),
    Task(
        annotator="0",
        user_id="task_076",
        instruction=(
            "You want to perform a combined design system and accessibility audit on the Pricing Page artifact. "
            "This comprehensive audit will analyze both design system compliance and accessibility standards, "
            "identifying component mapping issues and accessibility violations that need to be addressed."
        ),
        actions=[
            Action(
                name="get_artifact_id_from_name",
                kwargs={"artifact_name": "Pricing Page"}
            ),
            Action(
                name="create_audit_session",
                kwargs={"artifact_id": "art_007", "audit_type": "COMBINED_DS_A11Y"}
            ),
            Action(
                name="identify_custom_groups_and_map_to_ds_components",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="record_ds_audit_findings",
                kwargs={"audit_id": "audit_013", "layer_id": "3:2", "layer_name": "Pricing Page", "finding_type": "SUBSTITUTE_RECOMMENDED", "recommended_component_id_nullable": "Pricing-v1.8", "severity": "LOW"}
            ),
            Action(
                name="evaluate_accessibility",
                kwargs={"artifact_id": "art_007"}
            ),
            Action(
                name="record_accessibility_audit_findings",
                kwargs={"audit_id": "audit_013", "layer_id": "3:2", "layer_name": "Pricing Page", "violation_type": "TOUCH_TARGET", "violation_details_json": {"current_size": "32x32px", "required_size": "44x44px", "description": "Touch target too small for mobile accessibility"}, "severity": "HIGH", "recommended_fix_summary": "Increase button size to minimum 44x44px for touch accessibility"}
            ),
            Action(
                name="generate_audit_report",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="update_audit_status",
                kwargs={"audit_id": "audit_013", "status": "COMPLETED"}
            ),
            Action(
                name="link_audit_report_asset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            )
        ],
        outputs=[{"audit_id": "audit_013", "finding_ds_id": "finding_ds_016", "finding_a11y_id": "finding_a11y_016", "report_asset_id": "asset_019"}]
    ),
    Task(
        annotator="0",
        user_id="task_077",
        instruction=(
            "You want to perform a combined design system and accessibility audit on the Admin Panel Header artifact. "
            "This comprehensive audit will analyze both design system compliance and accessibility standards, "
            "identifying component mapping issues and accessibility violations that need to be addressed."
        ),
        actions=[
            Action(
                name="get_artifact_id_from_name",
                kwargs={"artifact_name": "Admin Panel Header"}
            ),
            Action(
                name="create_audit_session",
                kwargs={"artifact_id": "art_008", "audit_type": "COMBINED_DS_A11Y"}
            ),
            Action(
                name="identify_custom_groups_and_map_to_ds_components",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="record_ds_audit_findings",
                kwargs={"audit_id": "audit_013", "layer_id": "4:1", "layer_name": "Admin Panel Header", "finding_type": "UNMAPPED", "recommended_component_id_nullable": "Admin-v2.9", "severity": "LOW"}
            ),
            Action(
                name="evaluate_accessibility",
                kwargs={"artifact_id": "art_008"}
            ),
            Action(
                name="record_accessibility_audit_findings",
                kwargs={"audit_id": "audit_013", "layer_id": "4:1", "layer_name": "Admin Panel Header", "violation_type": "CONTRAST", "violation_details_json": {"current_ratio": "2.8:1", "required_ratio": "4.5:1", "colors": {"foreground": "#666666", "background": "#ffffff"}}, "severity": "HIGH", "recommended_fix_summary": "Increase text color contrast to meet WCAG AA standards"}
            ),
            Action(
                name="generate_audit_report",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="update_audit_status",
                kwargs={"audit_id": "audit_013", "status": "COMPLETED"}
            ),
            Action(
                name="link_audit_report_asset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            )
        ],
        outputs=[{"audit_id": "audit_013", "finding_ds_id": "finding_ds_016", "finding_a11y_id": "finding_a11y_016", "report_asset_id": "asset_019"}]
    ),
    Task(
        annotator="0",
        user_id="task_078",
        instruction=(
            "You want to perform a combined design system and accessibility audit on the Data Table Component artifact. "
            "This comprehensive audit will analyze both design system compliance and accessibility standards, "
            "identifying component mapping issues and accessibility violations that need to be addressed."
        ),
        actions=[
            Action(
                name="get_artifact_id_from_name",
                kwargs={"artifact_name": "Data Table Component"}
            ),
            Action(
                name="create_audit_session",
                kwargs={"artifact_id": "art_009", "audit_type": "COMBINED_DS_A11Y"}
            ),
            Action(
                name="identify_custom_groups_and_map_to_ds_components",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="record_ds_audit_findings",
                kwargs={"audit_id": "audit_013", "layer_id": "4:1", "layer_name": "Data Table Component", "finding_type": "AMBIGUOUS", "recommended_component_id_nullable": "Data-v1.0", "severity": "LOW"}
            ),
            Action(
                name="evaluate_accessibility",
                kwargs={"artifact_id": "art_009"}
            ),
            Action(
                name="record_accessibility_audit_findings",
                kwargs={"audit_id": "audit_013", "layer_id": "4:1", "layer_name": "Data Table Component", "violation_type": "TEXT_SIZING", "violation_details_json": {"current_size": "12px", "required_size": "16px", "description": "Text too small for readability"}, "severity": "HIGH", "recommended_fix_summary": "Increase font size to minimum 16px for better readability"}
            ),
            Action(
                name="generate_audit_report",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="update_audit_status",
                kwargs={"audit_id": "audit_013", "status": "COMPLETED"}
            ),
            Action(
                name="link_audit_report_asset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            )
        ],
        outputs=[{"audit_id": "audit_013", "finding_ds_id": "finding_ds_016", "finding_a11y_id": "finding_a11y_016", "report_asset_id": "asset_019"}]
    ),
    Task(
        annotator="0",
        user_id="task_079",
        instruction=(
            "You want to perform a combined design system and accessibility audit on the Brand Guidelines artifact. "
            "This audit will evaluate both design system component mapping compliance and accessibility standards "
            "to ensure comprehensive quality assessment."
        ),
        actions=[
            Action(
                name="get_artifact_id_from_name",
                kwargs={"artifact_name": "Brand Guidelines"}
            ),
            Action(
                name="create_audit_session",
                kwargs={"artifact_id": "art_010", "audit_type": "COMBINED_DS_A11Y"}
            ),
            Action(
                name="identify_custom_groups_and_map_to_ds_components",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="record_ds_audit_findings",
                kwargs={"audit_id": "audit_013", "layer_id": "5:1", "layer_name": "Brand Guidelines", "finding_type": "SUBSTITUTE_RECOMMENDED", "recommended_component_id_nullable": "Brand-v1.2", "severity": "LOW"}
            ),
            Action(
                name="evaluate_accessibility",
                kwargs={"artifact_id": "art_010"}
            ),
            Action(
                name="record_accessibility_audit_findings",
                kwargs={"audit_id": "audit_013", "layer_id": "5:1", "layer_name": "Brand Guidelines", "violation_type": "TOUCH_TARGET", "violation_details_json": {"current_size": "40x40px", "required_size": "44x44px", "description": "Touch target too small for mobile accessibility"}, "severity": "MEDIUM", "recommended_fix_summary": "Increase button size to minimum 44x44px for touch accessibility"}
            ),
            Action(
                name="generate_audit_report",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="update_audit_status",
                kwargs={"audit_id": "audit_013", "status": "COMPLETED"}
            ),
            Action(
                name="link_audit_report_asset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            )
        ],
        outputs=[{"audit_id": "audit_013", "finding_ds_id": "finding_ds_016", "finding_a11y_id": "finding_a11y_016", "report_asset_id": "asset_019"}]
    ),
    Task(
        annotator="0",
        user_id="task_080",
        instruction=(
            "You want to perform a combined design system and accessibility audit on the Contact Form Component artifact. "
            "This audit will evaluate both design system component mapping compliance and accessibility standards "
            "to ensure comprehensive quality assessment."
        ),
        actions=[
            Action(
                name="get_artifact_id_from_name",
                kwargs={"artifact_name": "Contact Form Component"}
            ),
            Action(
                name="create_audit_session",
                kwargs={"artifact_id": "art_011", "audit_type": "COMBINED_DS_A11Y"}
            ),
            Action(
                name="identify_custom_groups_and_map_to_ds_components",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="record_ds_audit_findings",
                kwargs={"audit_id": "audit_013", "layer_id": "1:2", "layer_name": "Contact Form Component", "finding_type": "UNMAPPED", "recommended_component_id_nullable": "Contact-v2.3", "severity": "LOW"}
            ),
            Action(
                name="evaluate_accessibility",
                kwargs={"artifact_id": "art_011"}
            ),
            Action(
                name="record_accessibility_audit_findings",
                kwargs={"audit_id": "audit_013", "layer_id": "1:2", "layer_name": "Contact Form Component", "violation_type": "CONTRAST", "violation_details_json": {"current_ratio": "2.1:1", "required_ratio": "4.5:1", "colors": {"foreground": "#666666", "background": "#ffffff"}}, "severity": "MEDIUM", "recommended_fix_summary": "Increase text color contrast to meet WCAG AA standards"}
            ),
            Action(
                name="generate_audit_report",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="update_audit_status",
                kwargs={"audit_id": "audit_013", "status": "COMPLETED"}
            ),
            Action(
                name="link_audit_report_asset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            )
        ],
        outputs=[{"audit_id": "audit_013", "finding_ds_id": "finding_ds_016", "finding_a11y_id": "finding_a11y_016", "report_asset_id": "asset_019"}]
    ),
    Task(
        annotator="0",
        user_id="task_081",
        instruction=(
            "You need to perform a combined design system and accessibility audit for the Settings Screen. "
            "You want to evaluate both design system component mapping and accessibility compliance to ensure "
            "the artifact meets standards. You should identify any unmapped components and accessibility violations "
            "to provide comprehensive audit coverage."
        ),
        actions=[
            Action(
                name="get_artifact_id_from_name",
                kwargs={"artifact_name": "Settings Screen"}
            ),
            Action(
                name="create_audit_session",
                kwargs={"artifact_id": "art_012", "audit_type": "COMBINED_DS_A11Y"}
            ),
            Action(
                name="identify_custom_groups_and_map_to_ds_components",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="record_ds_audit_findings",
                kwargs={"audit_id": "audit_013", "layer_id": "2:1", "layer_name": "Settings Screen", "finding_type": "AMBIGUOUS", "recommended_component_id_nullable": "Settings-v1.4", "severity": "LOW"}
            ),
            Action(
                name="evaluate_accessibility",
                kwargs={"artifact_id": "art_012"}
            ),
            Action(
                name="record_accessibility_audit_findings",
                kwargs={"audit_id": "audit_013", "layer_id": "2:1", "layer_name": "Settings Screen", "violation_type": "TEXT_SIZING", "violation_details_json": {"current_size": "12px", "required_size": "16px", "description": "Text too small for readability"}, "severity": "MEDIUM", "recommended_fix_summary": "Increase font size to minimum 16px for better readability"}
            ),
            Action(
                name="generate_audit_report",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="update_audit_status",
                kwargs={"audit_id": "audit_013", "status": "COMPLETED"}
            ),
            Action(
                name="link_audit_report_asset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            )
        ],
        outputs=[{"audit_id": "audit_013", "finding_ds_id": "finding_ds_016", "finding_a11y_id": "finding_a11y_016", "report_asset_id": "asset_019"}]
    ),

    Task(
        annotator="0",
        user_id="task_082",
        instruction=(
            "You need to implement the fix plan and handoff workflow for completed accessibility audits. "
            "You should load findings from audit 'audit_001' and coordinate the remediation process with "
            "'designer@company.com' as the owner. The stakeholder notification should include "
            "'manager@company.com' and 'ux-lead@company.com'."
        ),
        actions=[
            Action(
                name="load_audit_findings",
                kwargs={"audit_id": "audit_001"}
            ),
            Action(
                name="prioritize_audit_findings",
                kwargs={"finding_ids_list": ["finding_a11y_005", "finding_a11y_009"]}
            ),
            Action(
                name="create_fix_plan",
                kwargs={"audit_id": "audit_001", "owner_email": "designer@company.com"}
            ),
            Action(
                name="create_fix_item",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_a11y_005"}
            ),
            Action(
                name="create_fix_item",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_a11y_009"}
            ),
            Action(
                name="create_and_deliver_fix_plan",
                kwargs={"plan_id": "plan_013"}
            ),
            Action(
                name="notify_stakeholders",
                kwargs={"plan_id": "plan_013", "stakeholder_emails": ["manager@company.com", "ux-lead@company.com"], "audit_id": "audit_001", "status": "DRAFTED", "owner_email": "designer@company.com"}
            )
        ],
        outputs=[{"plan_id": "plan_013", "item_id_1": "item_021", "item_id_2": "item_022", "asset_id": "asset_019", "thread_id": "thread_015", "message_id": "msg_017"}]
    ),

    Task(
        annotator="0",
        user_id="task_083",
        instruction=(
            "You need to execute the fix plan and handoff workflow for design system and accessibility "
            "findings 'finding_ds_010' and 'finding_a11y_007' from audit 'audit_005'. You should coordinate with "
            "'lead-designer@company.com' as the owner and notify 'product-manager@company.com' and "
            "'design-lead@company.com' as stakeholders."
        ),
        actions=[
            Action(
                name="load_audit_findings",
                kwargs={"audit_id": "audit_005"}
            ),
            Action(
                name="prioritize_audit_findings",
                kwargs={"finding_ids_list": ["finding_ds_010", "finding_a11y_007"]}
            ),
            Action(
                name="create_fix_plan",
                kwargs={"audit_id": "audit_005", "owner_email": "lead-designer@company.com"}
            ),
            Action(
                name="create_fix_item",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_ds_010"}
            ),
            Action(
                name="create_fix_item",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_a11y_007"}
            ),
            Action(
                name="create_and_deliver_fix_plan",
                kwargs={"plan_id": "plan_013"}
            ),
            Action(
                name="notify_stakeholders",
                kwargs={"plan_id": "plan_013", "stakeholder_emails": ["product-manager@company.com", "design-lead@company.com"], "audit_id": "audit_005", "status": "DRAFTED", "owner_email": "lead-designer@company.com"}
            )
        ],
        outputs=[{"plan_id": "plan_013", "item_id_1": "item_021", "item_id_2": "item_022", "comment_id": "comment_019", "thread_id": "thread_015", "message_id": "msg_017"}]
    ),
    Task(
        annotator="0",
        user_id="task_084",
        instruction=(
            "You need to execute the fix plan and handoff workflow for design system findings "
            "'finding_ds_001' and 'finding_ds_002' from audit 'audit_003'. You should coordinate with "
            "'senior-designer@company.com' as the owner and notify 'qa-lead@company.com' and "
            "'dev-team@company.com' as stakeholders."
        ),
        actions=[
            Action(
                name="load_audit_findings",
                kwargs={"audit_id": "audit_003"}
            ),
            Action(
                name="prioritize_audit_findings",
                kwargs={"finding_ids_list": ["finding_ds_001", "finding_ds_002"]}
            ),
            Action(
                name="create_fix_plan",
                kwargs={"audit_id": "audit_003", "owner_email": "senior-designer@company.com"}
            ),
            Action(
                name="create_fix_item",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_ds_001"}
            ),
            Action(
                name="create_fix_item",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_ds_002"}
            ),
            Action(
                name="create_and_deliver_fix_plan",
                kwargs={"plan_id": "plan_013"}
            ),
            Action(
                name="notify_stakeholders",
                kwargs={"plan_id": "plan_013", "stakeholder_emails": ["qa-lead@company.com", "dev-team@company.com"], "audit_id": "audit_003", "status": "DRAFTED", "owner_email": "senior-designer@company.com"}
            )
        ],
        outputs=[{"plan_id": "plan_013", "item_id_1": "item_021", "item_id_2": "item_022", "asset_id": "asset_019", "thread_id": "thread_015", "message_id": "msg_017"}]
    ),
    Task(
        annotator="0",
        user_id="task_085",
        instruction=(
            "You need to execute the fix plan and handoff workflow for accessibility findings "
            "'finding_a11y_003' and 'finding_a11y_007' from audit 'audit_004'. You should coordinate with "
            "'accessibility-lead@company.com' as the owner and notify 'ux-team@company.com' and "
            "'compliance-officer@company.com' as stakeholders."
        ),
        actions=[
            Action(
                name="load_audit_findings",
                kwargs={"audit_id": "audit_004"}
            ),
            Action(
                name="prioritize_audit_findings",
                kwargs={"finding_ids_list": ["finding_a11y_003", "finding_a11y_007"]}
            ),
            Action(
                name="create_fix_plan",
                kwargs={"audit_id": "audit_004", "owner_email": "accessibility-lead@company.com"}
            ),
            Action(
                name="create_fix_item",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_a11y_003"}
            ),
            Action(
                name="create_fix_item",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_a11y_007"}
            ),
            Action(
                name="create_and_deliver_fix_plan",
                kwargs={"plan_id": "plan_013"}
            ),
            Action(
                name="notify_stakeholders",
                kwargs={"plan_id": "plan_013", "stakeholder_emails": ["ux-team@company.com", "compliance-officer@company.com"], "audit_id": "audit_004", "status": "DRAFTED", "owner_email": "accessibility-lead@company.com"}
            )
        ],
        outputs=[{"plan_id": "plan_013", "item_id_1": "item_021", "item_id_2": "item_022", "ticket_id": "JIRA-9215", "thread_id": "thread_015", "message_id": "msg_017"}]
    ),
    Task(
        annotator="0",
        user_id="task_086",
        instruction=(
            "You need to execute the fix plan and handoff workflow for accessibility findings "
            "'finding_a11y_005' and 'finding_a11y_009' from audit 'audit_001'. You should coordinate with "
            "'ux-designer@company.com' as the owner and notify 'design-system@company.com' and "
            "'product-owner@company.com' as stakeholders."
        ),
        actions=[
            Action(
                name="load_audit_findings",
                kwargs={"audit_id": "audit_001"}
            ),
            Action(
                name="prioritize_audit_findings",
                kwargs={"finding_ids_list": ["finding_a11y_005", "finding_a11y_009"]}
            ),
            Action(
                name="create_fix_plan",
                kwargs={"audit_id": "audit_001", "owner_email": "ux-designer@company.com"}
            ),
            Action(
                name="create_fix_item",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_a11y_005"}
            ),
            Action(
                name="create_fix_item",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_a11y_009"}
            ),
            Action(
                name="create_and_deliver_fix_plan",
                kwargs={"plan_id": "plan_013"}
            ),
            Action(
                name="notify_stakeholders",
                kwargs={"plan_id": "plan_013", "stakeholder_emails": ["design-system@company.com", "product-owner@company.com"], "audit_id": "audit_001", "status": "DRAFTED", "owner_email": "ux-designer@company.com"}
            )
        ],
        outputs=[{"plan_id": "plan_013", "item_id_1": "item_021", "item_id_2": "item_022", "ticket_id": "JIRA-9215", "thread_id": "thread_015", "message_id": "msg_017"}]
    ),
    Task(
        annotator="0",
        user_id="task_087",
        instruction=(
            "You need to create and deliver a comprehensive fix plan for accessibility violations "
            "found in a touch target accessibility audit. Your task involves loading the audit findings "
            "for audit_002, prioritizing the high-severity touch target issues, and creating a detailed "
            "remediation plan. You should focus on the critical admin header button touch target issue "
            "and the search input touch target problem. Create fix items for both findings, deliver the "
            "plan via Figma comments, and notify ui-team@company.com and accessibility-expert@company.com "
            "about the plan. The plan should be owned by frontend-dev@company.com and stakeholders should "
            "be informed of the drafted status."
        ),
        actions=[
            Action(
                name="load_audit_findings",
                kwargs={"audit_id": "audit_002"}
            ),
            Action(
                name="prioritize_audit_findings",
                kwargs={"finding_ids_list": ["finding_a11y_001", "finding_a11y_006"]}
            ),
            Action(
                name="create_fix_plan",
                kwargs={"audit_id": "audit_002", "owner_email": "frontend-dev@company.com"}
            ),
            Action(
                name="create_fix_item",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_a11y_001"}
            ),
            Action(
                name="create_fix_item",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_a11y_006"}
            ),
            Action(
                name="create_and_deliver_fix_plan",
                kwargs={"plan_id": "plan_013"}
            ),
            Action(
                name="notify_stakeholders",
                kwargs={"plan_id": "plan_013", "stakeholder_emails": ["ui-team@company.com", "accessibility-expert@company.com"], "audit_id": "audit_002", "status": "DRAFTED", "owner_email": "frontend-dev@company.com"}
            )
        ],
        outputs=[{"plan_id": "plan_013", "item_id_1": "item_021", "item_id_2": "item_022", "comment_id": "comment_019", "thread_id": "thread_015", "message_id": "msg_017"}]
    ),
    Task(
        annotator="0",
        user_id="task_088",
        instruction=(
            "You need to create and deliver a fix plan for design system mapping issues found "
            "in a component audit. Your task involves loading audit findings for audit_006, "
            "prioritizing the design system violations, and creating a remediation plan. Focus "
            "on the data table header substitute recommendation and pagination controls unmapped "
            "component issues. Create fix items for both findings, deliver the plan as a PDF "
            "document, and notify design-system@company.com and component-library@company.com "
            "about the plan. The plan should be owned by component-dev@company.com and "
            "stakeholders should be informed of the drafted status."
        ),
        actions=[
            Action(
                name="load_audit_findings",
                kwargs={"audit_id": "audit_006"}
            ),
            Action(
                name="prioritize_audit_findings",
                kwargs={"finding_ids_list": ["finding_ds_003", "finding_ds_007"]}
            ),
            Action(
                name="create_fix_plan",
                kwargs={"audit_id": "audit_006", "owner_email": "component-dev@company.com"}
            ),
            Action(
                name="create_fix_item",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_ds_003"}
            ),
            Action(
                name="create_fix_item",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_ds_007"}
            ),
            Action(
                name="create_and_deliver_fix_plan",
                kwargs={"plan_id": "plan_013"}
            ),
            Action(
                name="notify_stakeholders",
                kwargs={"plan_id": "plan_013", "stakeholder_emails": ["design-system@company.com", "component-library@company.com"], "audit_id": "audit_006", "status": "DRAFTED", "owner_email": "component-dev@company.com"}
            )
        ],
        outputs=[{"plan_id": "plan_013", "item_id_1": "item_021", "item_id_2": "item_022", "asset_id": "asset_019", "thread_id": "thread_015", "message_id": "msg_017"}]
    ),
    Task(
        annotator="0",
        user_id="task_089",
        instruction=(
            "You need to create and deliver a fix plan for internationalization accessibility issues "
            "found in an RTL and text sizing audit. Your task involves loading audit findings for "
            "audit_007, prioritizing the navigation menu RTL compliance and footer link text sizing "
            "issues. Create fix items for both findings, deliver the plan as a PDF document, and "
            "notify i18n-team@company.com and accessibility-qa@company.com about the plan. The plan "
            "should be owned by internationalization-dev@company.com and stakeholders should be "
            "informed of the drafted status."
        ),
        actions=[
            Action(
                name="load_audit_findings",
                kwargs={"audit_id": "audit_007"}
            ),
            Action(
                name="prioritize_audit_findings",
                kwargs={"finding_ids_list": ["finding_a11y_004", "finding_a11y_008"]}
            ),
            Action(
                name="create_fix_plan",
                kwargs={"audit_id": "audit_007", "owner_email": "internationalization-dev@company.com"}
            ),
            Action(
                name="create_fix_item",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_a11y_004"}
            ),
            Action(
                name="create_fix_item",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_a11y_008"}
            ),
            Action(
                name="create_and_deliver_fix_plan",
                kwargs={"plan_id": "plan_013"}
            ),
            Action(
                name="notify_stakeholders",
                kwargs={"plan_id": "plan_013", "stakeholder_emails": ["i18n-team@company.com", "accessibility-qa@company.com"], "audit_id": "audit_007", "status": "DRAFTED", "owner_email": "internationalization-dev@company.com"}
            )
        ],
        outputs=[{"plan_id": "plan_013", "item_id_1": "item_021", "item_id_2": "item_022", "asset_id": "asset_019", "thread_id": "thread_015", "message_id": "msg_017"}]
    ),
    Task(
        annotator="0",
        user_id="task_090",
        instruction=(
            "You need to create and deliver a fix plan for design system component mapping issues "
            "found in a profile and form interface audit. Your task involves loading audit findings "
            "for audit_008, prioritizing the unmapped profile avatar component and ambiguous form "
            "input mapping issues. Create fix items for both findings, deliver the plan via Figma "
            "comments, and notify ds-governance@company.com and product-design@company.com about "
            "the plan. The plan should be owned by platform-team@company.com and stakeholders "
            "should be informed of the drafted status."
        ),
        actions=[
            Action(
                name="load_audit_findings",
                kwargs={"audit_id": "audit_008"}
            ),
            Action(
                name="prioritize_audit_findings",
                kwargs={"finding_ids_list": ["finding_ds_004", "finding_ds_008"]}
            ),
            Action(
                name="create_fix_plan",
                kwargs={"audit_id": "audit_008", "owner_email": "platform-team@company.com"}
            ),
            Action(
                name="create_fix_item",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_ds_004"}
            ),
            Action(
                name="create_fix_item",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_ds_008"}
            ),
            Action(
                name="create_and_deliver_fix_plan",
                kwargs={"plan_id": "plan_013"}
            ),
            Action(
                name="notify_stakeholders",
                kwargs={"plan_id": "plan_013", "stakeholder_emails": ["ds-governance@company.com", "product-design@company.com"], "audit_id": "audit_008", "status": "DRAFTED", "owner_email": "platform-team@company.com"}
            )
        ],
        outputs=[{"plan_id": "plan_013", "item_id_1": "item_021", "item_id_2": "item_022", "comment_id": "comment_019", "thread_id": "thread_015", "message_id": "msg_017"}]
    ),
    Task(
        annotator="0",
        user_id="task_091",
        instruction=(
            "You need to address brand consistency and design system compliance issues identified during audit_010. "
            "Your responsibility is to load the audit findings, prioritize them based on their impact on brand integrity, and create a comprehensive fix plan. "
            "You should prioritize the Brand Logo ambiguous mapping (finding_ds_005) and Typography Heading substitution recommendation (finding_ds_009). "
            "You want to create a fix plan owned by brand-team@company.com and generate fix items for both findings to ensure proper brand representation. "
            "Your plan should include delivering the fixes through tickets and notifying key stakeholders including brand-guidelines@company.com and marketing-design@company.com. "
            "The output should provide the plan ID, individual fix item IDs, ticket information, and confirmation of stakeholder notifications."
        ),
        actions=[
            Action(
                name="load_audit_findings",
                kwargs={"audit_id": "audit_010"}
            ),
            Action(
                name="prioritize_audit_findings",
                kwargs={"finding_ids_list": ["finding_ds_005", "finding_ds_009"]}
            ),
            Action(
                name="create_fix_plan",
                kwargs={"audit_id": "audit_010", "owner_email": "brand-team@company.com"}
            ),
            Action(
                name="create_fix_item",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_ds_005"}
            ),
            Action(
                name="create_fix_item",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_ds_009"}
            ),
            Action(
                name="create_and_deliver_fix_plan",
                kwargs={"plan_id": "plan_013"}
            ),
            Action(
                name="notify_stakeholders",
                kwargs={"plan_id": "plan_013", "stakeholder_emails": ["brand-guidelines@company.com", "marketing-design@company.com"], "audit_id": "audit_010", "status": "DRAFTED", "owner_email": "brand-team@company.com"}
            )
        ],
        outputs=[{"plan_id": "plan_013", "item_id_1": "item_021", "item_id_2": "item_022", "ticket_id": "JIRA-9215", "thread_id": "thread_015", "message_id": "msg_017"}]
    ),
    Task(
        annotator="0",
        user_id="task_092",
        instruction=(
            "You need to create a fix plan for contact form design issues identified in audit_011. "
            "Your responsibility is to load the audit findings, prioritize the Contact Form Input unmapped component (finding_ds_011) and Submit Button touch target issue (finding_a11y_012). "
            "You want to create a fix plan owned by form-team@company.com and generate fix items for both critical findings. "
            "Your plan should deliver fixes through tickets and notify key stakeholders contact-form-dev@company.com and ui-accessibility@company.com."
        ),
        actions=[
            Action(
                name="load_audit_findings",
                kwargs={"audit_id": "audit_011"}
            ),
            Action(
                name="prioritize_audit_findings",
                kwargs={"finding_ids_list": ["finding_ds_011", "finding_a11y_012"]}
            ),
            Action(
                name="create_fix_plan",
                kwargs={"audit_id": "audit_011", "owner_email": "form-team@company.com"}
            ),
            Action(
                name="create_fix_item",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_ds_011"}
            ),
            Action(
                name="create_fix_item",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_a11y_012"}
            ),
            Action(
                name="create_and_deliver_fix_plan",
                kwargs={"plan_id": "plan_013"}
            ),
            Action(
                name="notify_stakeholders",
                kwargs={"plan_id": "plan_013", "stakeholder_emails": ["contact-form-dev@company.com", "ui-accessibility@company.com"], "audit_id": "audit_011", "status": "DRAFTED", "owner_email": "form-team@company.com"}
            )
        ],
        outputs=[{"plan_id": "plan_013", "item_id_1": "item_021", "item_id_2": "item_022", "ticket_id": "JIRA-9215", "thread_id": "thread_015", "message_id": "msg_017"}]
    ),
    Task(
        annotator="0",
        user_id="task_093",
        instruction=(
            "You need to implement Workflow 4 - Fix Plan & Handoff to convert audit findings into actionable "
            "remediation steps. You should process audit_011 which contains contact form design issues, with "
            "designer@company.com as the owner. Focus on creating fix items for the two highest priority findings "
            "and deliver the plan with DELIVERED status to reviewer@company.com for implementation tracking."
        ),
        actions=[
            Action(
                name="load_audit_findings",
                kwargs={"audit_id": "audit_011"}
            ),
            Action(
                name="prioritize_audit_findings",
                kwargs={"finding_ids_list": ["finding_ds_011", "finding_ds_012", "finding_ds_013", "finding_a11y_011", "finding_a11y_012", "finding_a11y_013"]}
            ),
            Action(
                name="create_fix_plan",
                kwargs={"audit_id": "audit_011", "owner_email": "designer@company.com"}
            ),
            Action(
                name="create_fix_item",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_ds_011"}
            ),
            Action(
                name="create_fix_item",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_a11y_011"}
            ),
            Action(
                name="create_and_deliver_fix_plan",
                kwargs={"plan_id": "plan_013"}
            ),
            Action(
                name="notify_stakeholders",
                kwargs={"plan_id": "plan_013", "stakeholder_emails": ["reviewer@company.com"], "audit_id": "audit_011", "status": "DELIVERED", "owner_email": "designer@company.com"}
            )
        ],
        outputs=[{"plan_id": "plan_013", "item_ids": ["item_021", "item_022"], "asset_id": "asset_019", "thread_id": "thread_015", "message_id": "msg_017"}]
    ),
    Task(
        annotator="0",
        user_id="task_094",
        instruction=(
            "You need to implement Workflow 4 - Fix Plan & Handoff to convert audit findings into actionable "
            "remediation steps. You should process audit_012 which contains settings interface design issues, with "
            "ux-lead@company.com as the owner. Focus on creating fix items for the two highest priority findings and "
            "deliver the plan with DELIVERED status to product-manager@company.com for implementation tracking."
        ),
        actions=[
            Action(
                name="load_audit_findings",
                kwargs={"audit_id": "audit_012"}
            ),
            Action(
                name="prioritize_audit_findings",
                kwargs={"finding_ids_list": ["finding_ds_014", "finding_ds_015", "finding_a11y_014", "finding_a11y_015"]}
            ),
            Action(
                name="create_fix_plan",
                kwargs={"audit_id": "audit_012", "owner_email": "ux-lead@company.com"}
            ),
            Action(
                name="create_fix_item",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_ds_014"}
            ),
            Action(
                name="create_fix_item",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_a11y_014"}
            ),
            Action(
                name="create_and_deliver_fix_plan",
                kwargs={"plan_id": "plan_013"}
            ),
            Action(
                name="notify_stakeholders",
                kwargs={"plan_id": "plan_013", "stakeholder_emails": ["product-manager@company.com"], "audit_id": "audit_012", "status": "DELIVERED", "owner_email": "ux-lead@company.com"}
            )
        ],
        outputs=[{"plan_id": "plan_013", "item_ids": ["item_021", "item_022"], "asset_id": "asset_019", "thread_id": "thread_015", "message_id": "msg_017"}]
    ),
    Task(
        annotator="0",
        user_id="task_095",
        instruction=(
            "You need to implement Workflow 4 - Fix Plan & Handoff to convert audit findings into actionable "
            "remediation steps. You should process audit_010 which contains brand and typography design system "
            "issues, with brand-manager@company.com as the owner. Focus on creating multiple fix items for all findings "
            "and deliver the plan with DELIVERED status to design-team@company.com for implementation tracking."
        ),
        actions=[
            Action(
                name="load_audit_findings",
                kwargs={"audit_id": "audit_010"}
            ),
            Action(
                name="prioritize_audit_findings",
                kwargs={"finding_ids_list": ["finding_ds_005", "finding_ds_009"]}
            ),
            Action(
                name="create_fix_plan",
                kwargs={"audit_id": "audit_010", "owner_email": "brand-manager@company.com"}
            ),
            Action(
                name="create_fix_item",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_ds_005"}
            ),
            Action(
                name="create_fix_item",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_ds_009"}
            ),
            # Action(
            #     name="create_fix_item",
            #     kwargs={"plan_id": "plan_013", "finding_id": "finding_ds_005"}
            # ),
            Action(
                name="create_and_deliver_fix_plan",
                kwargs={"plan_id": "plan_013"}
            ),
            Action(
                name="notify_stakeholders",
                kwargs={"plan_id": "plan_013", "stakeholder_emails": ["design-team@company.com"], "audit_id": "audit_010", "status": "DELIVERED", "owner_email": "brand-manager@company.com"}
            )
        ],
        outputs=[{"plan_id": "plan_013", "item_ids": ["item_021", "item_022"], "ticket_id": "JIRA-9215", "thread_id": "thread_015", "message_id": "msg_017"}]
    ),
    Task(
        annotator="0",
        user_id="task_096",
        instruction=(
            "You need to implement Workflow 4 Fix Plan & Handoff for audit_007 with accessibility.lead@company.com as the owner. "
            "You want to convert accessibility audit findings into actionable remediation steps and notify stakeholders (accessibility.lead@othercompany.com) with DELIVERED status."
        ),
        actions=[
            Action(
                name="load_audit_findings",
                kwargs={"audit_id": "audit_007"}
            ),
            Action(
                name="prioritize_audit_findings",
                kwargs={"finding_ids_list": ["finding_a11y_004", "finding_a11y_008"]}
            ),
            Action(
                name="create_fix_plan",
                kwargs={"audit_id": "audit_007", "owner_email": "accessibility.lead@company.com"}
            ),
            Action(
                name="create_fix_item",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_a11y_004"}
            ),
            Action(
                name="create_fix_item",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_a11y_008"}
            ),
            # Action(
            #     name="create_fix_item",
            #     kwargs={"plan_id": "plan_013", "finding_id": "finding_a11y_004"}
            # ),
            Action(
                name="create_and_deliver_fix_plan",
                kwargs={"plan_id": "plan_013"}
            ),
            Action(
                name="notify_stakeholders",
                kwargs={"plan_id": "plan_013", "stakeholder_emails": ["accessibility.lead@othercompany.com"], "audit_id": "audit_007", "status": "DELIVERED", "owner_email": "accessibility.lead@company.com"}
            )
        ],
        outputs=[{"plan_id": "plan_013", "item_ids": ["item_021", "item_022"], "ticket_id": "JIRA-9215", "thread_id": "thread_015", "message_id": "msg_017"}]
    ),
    Task(
        annotator="0",
        user_id="task_097",
        instruction=(
            "You need to implement Workflow 4 Fix Plan & Handoff for audit_004 with ux.engineer@company.com as the owner. "
            "You want to convert accessibility audit findings into actionable remediation steps and notify stakeholders (ux.engineer@othercompany.com) with DELIVERED status."
        ),
        actions=[
            Action(
                name="load_audit_findings",
                kwargs={"audit_id": "audit_004"}
            ),
            Action(
                name="prioritize_audit_findings",
                kwargs={"finding_ids_list": ["finding_a11y_003", "finding_a11y_007"]}
            ),
            Action(
                name="create_fix_plan",
                kwargs={"audit_id": "audit_004", "owner_email": "ux.engineer@company.com"}
            ),
            Action(
                name="create_fix_item",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_a11y_003"}
            ),
            Action(
                name="create_fix_item",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_a11y_007"}
            ),
            # Action(
            #     name="create_fix_item",
            #     kwargs={"plan_id": "plan_013", "finding_id": "finding_a11y_003"}
            # ),
            Action(
                name="create_and_deliver_fix_plan",
                kwargs={"plan_id": "plan_013"}
            ),
            Action(
                name="notify_stakeholders",
                kwargs={"plan_id": "plan_013", "stakeholder_emails": ["ux.engineer@othercompany.com"], "audit_id": "audit_004", "status": "DELIVERED", "owner_email": "ux.engineer@company.com"}
            )
        ],
        outputs=[{"plan_id": "plan_013", "item_ids": ["item_021", "item_022"], "comment_id": "comment_019", "thread_id": "thread_015", "message_id": "msg_017"}]
    ),
    Task(
        annotator="0",
        user_id="task_098",
        instruction=(
            "You need to implement Workflow 4 Fix Plan & Handoff for audit_010 with design.lead@company.com as the owner. "
            "You want to convert design system mapping audit findings into actionable remediation steps and notify stakeholders (design.lead@company.com) with DELIVERED status."
        ),
        actions=[
            Action(
                name="load_audit_findings",
                kwargs={"audit_id": "audit_010"}
            ),
            Action(
                name="prioritize_audit_findings",
                kwargs={"finding_ids_list": ["finding_ds_005", "finding_ds_009"]}
            ),
            Action(
                name="create_fix_plan",
                kwargs={"audit_id": "audit_010", "owner_email": "design.lead@company.com"}
            ),
            Action(
                name="create_fix_item",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_ds_005"}
            ),
            Action(
                name="create_fix_item",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_ds_009"}
            ),
            # Action(
            #     name="create_fix_item",
            #     kwargs={"plan_id": "plan_013", "finding_id": "finding_ds_005"}
            # ),
            Action(
                name="create_and_deliver_fix_plan",
                kwargs={"plan_id": "plan_013"}
            ),
            Action(
                name="notify_stakeholders",
                kwargs={"plan_id": "plan_013", "stakeholder_emails": ["design.lead@company.com"], "audit_id": "audit_010", "status": "DELIVERED", "owner_email": "design.lead@company.com"}
            )
        ],
        outputs=[{"plan_id": "plan_013", "item_ids": ["item_021", "item_022"], "comment_id": "comment_019", "thread_id": "thread_015", "message_id": "msg_017"}]
    ),
    Task(
        annotator="0",
        user_id="task_099",
        instruction=(
            "You need to implement Workflow 4 Fix Plan & Handoff for audit_003 with senior.dev@company.com as the owner. "
            "You want to convert design system mapping audit findings into actionable remediation steps and notify stakeholders (senior.dev@othercompany.com) with DELIVERED status."
        ),
        actions=[
            Action(
                name="load_audit_findings",
                kwargs={"audit_id": "audit_003"}
            ),
            Action(
                name="prioritize_audit_findings",
                kwargs={"finding_ids_list": ["finding_ds_001", "finding_ds_002", "finding_ds_006", "finding_ds_010"]}
            ),
            Action(
                name="create_fix_plan",
                kwargs={"audit_id": "audit_003", "owner_email": "senior.dev@company.com"}
            ),
            Action(
                name="create_fix_item",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_ds_001"}
            ),
            Action(
                name="create_fix_item",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_ds_002"}
            ),
            Action(
                name="create_fix_item",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_ds_006"}
            ),
            Action(
                name="create_fix_item",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_ds_010"}
            ),
            Action(
                name="create_and_deliver_fix_plan",
                kwargs={"plan_id": "plan_013"}
            ),
            Action(
                name="notify_stakeholders",
                kwargs={"plan_id": "plan_013", "stakeholder_emails": ["senior.dev@othercompany.com"], "audit_id": "audit_003", "status": "DELIVERED", "owner_email": "senior.dev@company.com"}
            )
        ],
        outputs=[{"plan_id": "plan_013", "item_ids": ["item_021", "item_022", "item_023", "item_024"], "ticket_id": "JIRA-9215", "thread_id": "thread_015", "message_id": "msg_017"}]
    ),
    Task(
        annotator="0",
        user_id="task_100",
        instruction=(
            "You need to implement Workflow 4 Fix Plan & Handoff for audit_002 with ui.accessibility@company.com as the owner. "
            "You want to convert accessibility audit findings into actionable remediation steps and notify stakeholders with DELIVERED status."
        ),
        actions=[
            Action(
                name="load_audit_findings",
                kwargs={"audit_id": "audit_002"}
            ),
            Action(
                name="prioritize_audit_findings",
                kwargs={"finding_ids_list": ["finding_a11y_001", "finding_a11y_002", "finding_a11y_006", "finding_a11y_010"]}
            ),
            Action(
                name="create_fix_plan",
                kwargs={"audit_id": "audit_002", "owner_email": "ui.accessibility@company.com"}
            ),
            Action(
                name="create_fix_item",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_a11y_001"}
            ),
            Action(
                name="create_fix_item",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_a11y_002"}
            ),
            Action(
                name="create_fix_item",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_a11y_006"}
            ),
            Action(
                name="create_fix_item",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_a11y_010"}
            ),
            Action(
                name="create_and_deliver_fix_plan",
                kwargs={"plan_id": "plan_013"}
            ),
            Action(
                name="notify_stakeholders",
                kwargs={"plan_id": "plan_013", "stakeholder_emails": ["ui.accessibility@company.com"], "audit_id": "audit_002", "status": "DELIVERED", "owner_email": "ui.accessibility@company.com"}
            )
        ],
        outputs=[{"plan_id": "plan_013", "item_ids": ["item_021", "item_022", "item_023", "item_024"], "comment_id": "comment_019", "thread_id": "thread_015", "message_id": "msg_017"}]
    ),


]
