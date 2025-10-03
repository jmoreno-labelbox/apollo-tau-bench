from tau_bench.types import Action, Task

TASKS = [
    Task(
        annotator="0",
        user_id="task_001",
        instruction=(
            "Handle a detailed design review process for artifacts needing feedback. Concentrate on those tagged with 'needs-review' and get them ready for stakeholder evaluation. Export these as PNG at 2x scale for the best review quality. Operate as 'design-lead@company.com' with design-review@company.com and ux-team@company.com as recipients. Utilize 'design-review' and 'figma' labels for organizing threads, and make sure each artifact receives a NEEDS_REVIEW status for proper tracking."
        ),
        actions=[
            Action(
                name="FilterFigmaArtifactsByTags",
                kwargs={"tags": ["needs-review"]}
            ),
            Action(
                name="ExportFigmaArtifactsToAssets",
                kwargs={"artifact_ids": ["art_001", "art_007"], "export_profile": {"format": "PNG", "scale": "2x"}}
            ),
            Action(
                name="CreateGmailThread",
                kwargs={
                    "sender_email": "design-lead@company.com",
                    "recipients_emails": ["design-review@company.com", "ux-team@company.com"],
                    "workflow_type": "review",
                    "current_labels": ["design-review", "figma"]
                }
            ),
            Action(
                name="CreateReviewCycle",
                kwargs={"artifact_id": "art_001", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="CreateReviewCycle",
                kwargs={"artifact_id": "art_007", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="CreateGmailMessage",
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
            "Oversee the review process for component library updates requiring team coordination. Focus on artifacts tagged with 'component' and prepare them for developer handoff. Export these as SVG at 1x scale for ideal development integration. Function as 'ux-lead@company.com' with design-review@company.com and ux-team@company.com as recipients. Assign 'components', 'design-system', and 'design-review' labels for accurate categorization, and apply NEEDS_REVIEW status for systematic tracking."
        ),
        actions=[
            Action(
                name="FilterFigmaArtifactsByTags",
                kwargs={"tags": ["component"]}
            ),
            Action(
                name="ExportFigmaArtifactsToAssets",
                kwargs={"artifact_ids": ["art_009", "art_011"], "export_profile": {"format": "SVG", "scale": "1x"}}
            ),
            Action(
                name="CreateGmailThread",
                kwargs={
                    "sender_email": "ux-lead@company.com",
                    "recipients_emails": ["design-review@company.com", "ux-team@company.com"],
                    "workflow_type": "review",
                    "current_labels": ["components", "design-system", "design-review"]
                }
            ),
            Action(
                name="CreateReviewCycle",
                kwargs={"artifact_id": "art_009", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="CreateReviewCycle",
                kwargs={"artifact_id": "art_011", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="CreateGmailMessage",
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
            "Facilitate a thorough review process for mobile app interface updates that necessitate detailed evaluation. Concentrate on 'mobile' tagged artifacts and generate high-resolution documentation. Ensure your export format is PDF at 4x scale for the in-depth review documentation. Operate as 'mobile-lead@company.com' and include design-review@company.com and ux-team@company.com as recipients. Utilize 'mobile', 'ux', and 'feedback' labels for thread organization and confirm NEEDS_REVIEW status for a comprehensive mobile design evaluation."
        ),
        actions=[
            Action(
                name="FilterFigmaArtifactsByTags",
                kwargs={"tags": ["mobile"]}
            ),
            Action(
                name="ExportFigmaArtifactsToAssets",
                kwargs={"artifact_ids": ["art_004", "art_012"], "export_profile": {"format": "PDF", "scale": "4x"}}
            ),
            Action(
                name="CreateGmailThread",
                kwargs={
                    "sender_email": "mobile-lead@company.com",
                    "recipients_emails": ["design-review@company.com", "ux-team@company.com"],
                    "workflow_type": "review",
                    "current_labels": ["mobile", "ux", "feedback"]
                }
            ),
            Action(
                name="CreateReviewCycle",
                kwargs={"artifact_id": "art_004", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="CreateReviewCycle",
                kwargs={"artifact_id": "art_012", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="CreateGmailMessage",
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
            "Coordinate a brand consistency review aimed at standardizing the header component across the design system. Focus on 'header' tagged artifacts and prepare them for a visual consistency assessment. Export the format as JPG at 2x scale for detailed visual documentation. Function as 'brand-lead@company.com' with design-review@company.com and ux-team@company.com as the recipients. Implement 'brand', 'guidelines', and 'design-review' labels to bolster the brand consistency initiative, and maintain NEEDS_REVIEW status for a systematic evaluation."
        ),
        actions=[
            Action(
                name="FilterFigmaArtifactsByTags",
                kwargs={"tags": ["header"]}
            ),
            Action(
                name="ExportFigmaArtifactsToAssets",
                kwargs={"artifact_ids": ["art_002", "art_008"], "export_profile": {"format": "JPG", "scale": "2x"}}
            ),
            Action(
                name="CreateGmailThread",
                kwargs={
                    "sender_email": "brand-lead@company.com",
                    "recipients_emails": ["design-review@company.com", "ux-team@company.com"],
                    "workflow_type": "review",
                    "current_labels": ["brand", "guidelines", "design-review"]
                }
            ),
            Action(
                name="CreateReviewCycle",
                kwargs={"artifact_id": "art_002", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="CreateReviewCycle",
                kwargs={"artifact_id": "art_008", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="CreateGmailMessage",
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
            "Handle the preparation of the dashboard interface review within the product development cycle. Concentrate on artifacts tagged with 'dashboard' for assessing production readiness. Utilize PNG format at 1x scale as per production documentation standards. Operate in the role of 'product-lead@company.com', collaborating with design-review@company.com and ux-team@company.com. Assign 'launch', 'admin', and 'approval' labels to streamline the product review process, and set the NEEDS_REVIEW status for structured evaluation pre-launch."
        ),
        actions=[
            Action(
                name="FilterFigmaArtifactsByTags",
                kwargs={"tags": ["dashboard"]}
            ),
            Action(
                name="ExportFigmaArtifactsToAssets",
                kwargs={"artifact_ids": ["art_004", "art_008"], "export_profile": {"format": "PNG", "scale": "1x"}}
            ),
            Action(
                name="CreateGmailThread",
                kwargs={
                    "sender_email": "product-lead@company.com",
                    "recipients_emails": ["design-review@company.com", "ux-team@company.com"],
                    "workflow_type": "review",
                    "current_labels": ["launch", "admin", "approval"]
                }
            ),
            Action(
                name="CreateReviewCycle",
                kwargs={"artifact_id": "art_004", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="CreateReviewCycle",
                kwargs={"artifact_id": "art_008", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="CreateGmailMessage",
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
            "Coordinate the initiative for optimizing the pricing page to enhance conversion rates. Focus on artifacts tagged with 'pricing' to evaluate revenue optimization. Export these as SVG assets at 4x scale for high-resolution vector use. Serve as 'conversion-lead@company.com', in conjunction with design-review@company.com and ux-team@company.com. Apply 'marketing', 'pricing', and 'approval' labels to aid the revenue optimization campaign, and employ the NEEDS_REVIEW status for methodical assessment."
        ),
        actions=[
            Action(
                name="FilterFigmaArtifactsByTags",
                kwargs={"tags": ["pricing"]}
            ),
            Action(
                name="ExportFigmaArtifactsToAssets",
                kwargs={"artifact_ids": ["art_007"], "export_profile": {"format": "SVG", "scale": "4x"}}
            ),
            Action(
                name="CreateGmailThread",
                kwargs={
                    "sender_email": "conversion-lead@company.com",
                    "recipients_emails": ["design-review@company.com", "ux-team@company.com"],
                    "workflow_type": "review",
                    "current_labels": ["marketing", "pricing", "approval"]
                }
            ),
            Action(
                name="CreateReviewCycle",
                kwargs={"artifact_id": "art_007", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="CreateGmailMessage",
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
            "Handle the standardization of the navigation system across the platform to enhance information architecture. Concentrate on artifacts tagged with 'navigation' for consistency analysis. These should be exported as PDF assets at 2x scale for documentation purposes and developer handoff. Your role in coordination is 'ui-lead@company.com', in collaboration with design-review@company.com and ux-team@company.com. Apply the labels 'navigation', 'design-system', and 'responsive' to assist the information architecture initiative, and use the NEEDS_REVIEW status for systematic review."
        ),
        actions=[
            Action(
                name="FilterFigmaArtifactsByTags",
                kwargs={"tags": ["navigation"]}
            ),
            Action(
                name="ExportFigmaArtifactsToAssets",
                kwargs={"artifact_ids": ["art_002"], "export_profile": {"format": "PDF", "scale": "2x"}}
            ),
            Action(
                name="CreateGmailThread",
                kwargs={
                    "sender_email": "ui-lead@company.com",
                    "recipients_emails": ["design-review@company.com", "ux-team@company.com"],
                    "workflow_type": "review",
                    "current_labels": ["navigation", "design-system", "responsive"]
                }
            ),
            Action(
                name="CreateReviewCycle",
                kwargs={"artifact_id": "art_002", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="CreateGmailMessage",
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
            "Coordinate a brand identity consistency audit to ensure adherence to brand standards. Focus on artifacts marked with 'brand' to thoroughly evaluate brand consistency. Export these as JPG assets at 1x scale for documentation of brand compliance. Your role in coordination is 'brand-manager@company.com', working alongside design-review@company.com and ux-team@company.com. Attach the labels 'brand', 'audit', and 'guidelines' to aid the brand compliance initiative, and utilize the NEEDS_REVIEW status for systematic assessment."
        ),
        actions=[
            Action(
                name="FilterFigmaArtifactsByTags",
                kwargs={"tags": ["brand"]}
            ),
            Action(
                name="ExportFigmaArtifactsToAssets",
                kwargs={"artifact_ids": ["art_010"], "export_profile": {"format": "JPG", "scale": "1x"}}
            ),
            Action(
                name="CreateGmailThread",
                kwargs={
                    "sender_email": "brand-manager@company.com",
                    "recipients_emails": ["design-review@company.com", "ux-team@company.com"],
                    "workflow_type": "review",
                    "current_labels": ["brand", "audit", "guidelines"]
                }
            ),
            Action(
                name="CreateReviewCycle",
                kwargs={"artifact_id": "art_010", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="CreateGmailMessage",
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
            "Handle a thorough review process for hero section components affecting landing page conversion rates. Focus on 'hero' tagged artifacts for optimization evaluation. Export them in PDF format at 4x scale to ensure high-quality print documentation. Your coordination role is 'marketing-lead@company.com', collaborating with design-review@company.com and ux-team@company.com. Apply 'marketing', 'urgent', and 'responsive' labels to streamline the landing page design review and use NEEDS_REVIEW status to stress the importance of optimizing the hero section."
        ),
        actions=[
            Action(
                name="FilterFigmaArtifactsByTags",
                kwargs={"tags": ["hero"]}
            ),
            Action(
                name="ExportFigmaArtifactsToAssets",
                kwargs={"artifact_ids": ["art_001"], "export_profile": {"format": "PDF", "scale": "4x"}}
            ),
            Action(
                name="CreateGmailThread",
                kwargs={
                    "sender_email": "marketing-lead@company.com",
                    "recipients_emails": ["design-review@company.com", "ux-team@company.com"],
                    "workflow_type": "review",
                    "current_labels": ["marketing", "urgent", "responsive"]
                }
            ),
            Action(
                name="CreateReviewCycle",
                kwargs={"artifact_id": "art_001", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="CreateGmailMessage",
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
            "Coordinate a thorough review process for user profile interface components with an emphasis on accessibility standards and inclusive design. Target 'profile' tagged artifacts for accessibility compliance evaluation. Export them in SVG format at 2x scale suitable for scalable vector graphics meant for web use. Your coordination role is 'accessibility-lead@company.com', in partnership with design-review@company.com and ux-team@company.com. Apply 'accessibility', 'profile', and 'ux' labels to ensure adherence to accessibility standards, and use NEEDS_REVIEW status for systematic evaluation that emphasizes the significance of inclusive design."
        ),
        actions=[
            Action(
                name="FilterFigmaArtifactsByTags",
                kwargs={"tags": ["profile"]}
            ),
            Action(
                name="ExportFigmaArtifactsToAssets",
                kwargs={"artifact_ids": ["art_005"], "export_profile": {"format": "SVG", "scale": "2x"}}
            ),
            Action(
                name="CreateGmailThread",
                kwargs={
                    "sender_email": "accessibility-lead@company.com",
                    "recipients_emails": ["design-review@company.com", "ux-team@company.com"],
                    "workflow_type": "review",
                    "current_labels": ["accessibility", "profile", "ux"]
                }
            ),
            Action(
                name="CreateReviewCycle",
                kwargs={"artifact_id": "art_005", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="CreateGmailMessage",
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
            "Handle comprehensive design approval feedback from multiple stakeholders and finalize the approval workflow for hero section components that need immediate attention. Identify the hero-tagged artifacts requiring approval processing and ensure proper bidirectional feedback tracking by synchronizing Gmail message 'msg_002' with artifact 'art_001' to facilitate seamless collaboration between email and design platforms. Update the review cycle 'cycle_001' status to APPROVED to indicate implementation readiness to the development team. Coordinate the creation of a formal review approval record using approver email 'jake.design@company.com' to document the design approval and maintain a complete audit trail for governance, ensuring compliance with project management requirements and stakeholder accountability for design decisions in the approval workflow."
        ),
        actions=[
            Action(
                name="FilterFigmaArtifactsByTags",
                kwargs={"tags": ["hero"]}
            ),
            Action(
                name="CreateFigmaCommentFromGmailMessage",
                kwargs={"artifact_id": "art_001", "gmail_message_id": "msg_002"}
            ),
            Action(
                name="UpdateReviewCycleStatus",
                kwargs={"cycle_id": "cycle_001", "new_status": "APPROVED"}
            ),
            Action(
                name="CreateReviewApproval",
                kwargs={"cycle_id": "cycle_001", "approver_email": "jake.design@company.com"}
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
            "Manage feedback for pricing page components that require changes. Begin by filtering components tagged 'pricing', then synchronize Gmail message 'msg_004' to artifact 'art_007', update cycle 'cycle_003' status to CHANGES_REQUESTED, and generate an approval record with approver 'anna.brand@company.com'."
        ),
        actions=[
            Action(
                name="FilterFigmaArtifactsByTags",
                kwargs={"tags": ["pricing"]}
            ),
            Action(
                name="CreateFigmaCommentFromGmailMessage",
                kwargs={"artifact_id": "art_007", "gmail_message_id": "msg_004"}
            ),
            Action(
                name="UpdateReviewCycleStatus",
                kwargs={"cycle_id": "cycle_003", "new_status": "CHANGES_REQUESTED"}
            ),
            Action(
                name="CreateReviewApproval",
                kwargs={"cycle_id": "cycle_003", "approver_email": "anna.brand@company.com"}
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
            "Handle the essential approval process for mobile design components needing immediate stakeholder endorsement to comply with sprint deadlines. Export the approved mobile components as PNG files at 2x scale for developer handoff. Review and address thorough accessibility feedback from 'msg_005,' focusing on color contrast, ARIA compliance, and keyboard navigation issues for the mobile component 'art_002.' Update the review 'cycle_008' to APPROVED status to conclude the mobile component review and facilitate developer implementation, and ensure formal approval is recorded from 'chris.engineer@company.com' to proceed with production deployment across all mobile touchpoints."
        ),
        actions=[
            Action(
                name="ExportFigmaArtifactsToAssets",
                kwargs={"artifact_ids": ["art_002"], "export_profile": {"format": "PNG", "scale": "2x"}}
            ),
            Action(
                name="CreateFigmaCommentFromGmailMessage",
                kwargs={"artifact_id": "art_002", "gmail_message_id": "msg_005"}
            ),
            Action(
                name="UpdateReviewCycleStatus",
                kwargs={"cycle_id": "cycle_008", "new_status": "APPROVED"}
            ),
            Action(
                name="CreateReviewApproval",
                kwargs={"cycle_id": "cycle_008", "approver_email": "chris.engineer@company.com"}
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
            "Coordinate the finalization of critical brand guideline components requiring immediate revision and stakeholder escalation. Start by reviewing artifacts tagged 'brand' and 'guidelines' to pinpoint necessary guideline updates. Then address the detailed feedback from 'msg_006' concerning brand consistency issues. Escalate 'cycle_010' to ESCALATED status due to a missed deadline and stakeholder concerns, and document the formal approval from 'sophie.marketing@company.com' to advance with emergency brand updates and their implementation across all product touchpoints."
        ),
        actions=[
            Action(
                name="FilterFigmaArtifactsByTags",
                kwargs={"tags": ["brand", "guidelines"]}
            ),
            Action(
                name="CreateFigmaCommentFromGmailMessage",
                kwargs={"artifact_id": "art_010", "gmail_message_id": "msg_006"}
            ),
            Action(
                name="UpdateReviewCycleStatus",
                kwargs={"cycle_id": "cycle_010", "new_status": "ESCALATED"}
            ),
            Action(
                name="CreateReviewApproval",
                kwargs={"cycle_id": "cycle_010", "approver_email": "sophie.marketing@company.com"}
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
            "Complete the component library updates using UX feedback. Isolate artifacts labeled with 'components', save them as SVG files at a 1x scale to ensure development compatibility, integrate feedback from 'msg_003' into 'art_006', change 'cycle_009' to APPROVED, and obtain confirmation from 'jake.design@company.com'."
        ),
        actions=[
            Action(
                name="FilterFigmaArtifactsByTags",
                kwargs={"tags": ["components"]}
            ),
            Action(
                name="ExportFigmaArtifactsToAssets",
                kwargs={"artifact_ids": ["art_003"], "export_profile": {"format": "SVG", "scale": "1x"}}
            ),
            Action(
                name="CreateFigmaCommentFromGmailMessage",
                kwargs={"artifact_id": "art_006", "gmail_message_id": "msg_003"}
            ),
            Action(
                name="UpdateReviewCycleStatus",
                kwargs={"cycle_id": "cycle_009", "new_status": "APPROVED"}
            ),
            Action(
                name="CreateReviewApproval",
                kwargs={"cycle_id": "cycle_009", "approver_email": "jake.design@company.com"}
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
            "As chris.engineer@company.com, initiate reviews of the admin interface for the development team. Identify artifacts tagged with 'admin' to focus on admin panel components, output as PDF at 1x scale for clear documentation, inform the design and UX teams using 'admin' and 'review' tags, and monitor progress with the NEEDS_REVIEW status."
        ),
        actions=[
            Action(
                name="FilterFigmaArtifactsByTags",
                kwargs={"tags": ["admin"]}
            ),
            Action(
                name="ExportFigmaArtifactsToAssets",
                kwargs={"artifact_ids": ["art_008"], "export_profile": {"format": "PDF", "scale": "1x"}}
            ),
            Action(
                name="CreateGmailThread",
                kwargs={
                    "sender_email": "chris.engineer@company.com",
                    "recipients_emails": ["design-review@company.com", "ux-team@company.com"],
                    "workflow_type": "review",
                    "current_labels": ["admin", "review"]
                }
            ),
            Action(
                name="CreateReviewCycle",
                kwargs={"artifact_id": "art_008", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="CreateGmailMessage",
                kwargs={
                    "sender_email": "chris.engineer@company.com",
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
            "Manage marketing campaign assets under the email marketing.lead@company.com. Identify artifacts that bear the 'marketing' tag, and export these files in SVG format at a scale of 1x to ensure web compatibility. Collaborate with the design and UX teams using the 'marketing' and 'launch' labels, and set up review tracking by assigning NEEDS_REVIEW status."
        ),
        actions=[
            Action(
                name="FilterFigmaArtifactsByTags",
                kwargs={"tags": ["marketing"]}
            ),
            Action(
                name="ExportFigmaArtifactsToAssets",
                kwargs={"artifact_ids": ["art_006"], "export_profile": {"format": "SVG", "scale": "1x"}}
            ),
            Action(
                name="CreateGmailThread",
                kwargs={
                    "sender_email": "marketing.lead@company.com",
                    "recipients_emails": ["design-review@company.com", "ux-team@company.com"],
                    "workflow_type": "review",
                    "current_labels": ["marketing", "launch"]
                }
            ),
            Action(
                name="CreateReviewCycle",
                kwargs={"artifact_id": "art_006", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="CreateGmailMessage",
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
            "Oversee component library reviews as the contact design.systems@company.com. Pinpoint artifacts labeled with 'component' to address all items within the component library. Produce PNG assets at a scale of 4x suitable for high-resolution development handoff. Engage with design and UX teams employing the 'components' and 'library' labels, and commence tracking utilizing the NEEDS_REVIEW status."
        ),
        actions=[
            Action(
                name="FilterFigmaArtifactsByTags",
                kwargs={"tags": ["component"]}
            ),
            Action(
                name="ExportFigmaArtifactsToAssets",
                kwargs={"artifact_ids": ["art_009", "art_011"], "export_profile": {"format": "PNG", "scale": "4x"}}
            ),
            Action(
                name="CreateGmailThread",
                kwargs={
                    "sender_email": "design.systems@company.com",
                    "recipients_emails": ["design-review@company.com", "ux-team@company.com"],
                    "workflow_type": "review",
                    "current_labels": ["components", "library"]
                }
            ),
            Action(
                name="CreateReviewCycle",
                kwargs={"artifact_id": "art_009", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="CreateReviewCycle",
                kwargs={"artifact_id": "art_011", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="CreateGmailMessage",
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
            "As forms.lead@company.com, handle an in-depth assessment of the form component by concentrating on interactive elements requiring stakeholder input for enhancing user experience. Export the components in PDF format at 1x scale to facilitate a detailed documentation review. Collaborate with design and UX teams using 'component' and 'review' labels, and establish effective review tracking with NEEDS_REVIEW status for a comprehensive evaluation."
        ),
        actions=[
            Action(
                name="FilterFigmaArtifactsByTags",
                kwargs={"tags": ["form"]}
            ),
            Action(
                name="ExportFigmaArtifactsToAssets",
                kwargs={"artifact_ids": ["art_011"], "export_profile": {"format": "PDF", "scale": "1x"}}
            ),
            Action(
                name="CreateGmailThread",
                kwargs={
                    "sender_email": "forms.lead@company.com",
                    "recipients_emails": ["design-review@company.com", "ux-team@company.com"],
                    "workflow_type": "review",
                    "current_labels": ["component", "review"]
                }
            ),
            Action(
                name="CreateReviewCycle",
                kwargs={"artifact_id": "art_011", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="CreateGmailMessage",
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
            "As settings.lead@company.com, manage the examination of user settings and profile interfaces. Direct your focus towards settings-related artifacts that necessitate SVG exports at 2x scale to ensure crisp interface rendering. Collaborate with design and UX teams using 'profile' and 'ux' labels for accurate categorization, and set the NEEDS_REVIEW status to monitor evaluation progress."
        ),
        actions=[
            Action(
                name="FilterFigmaArtifactsByTags",
                kwargs={"tags": ["settings"]}
            ),
            Action(
                name="ExportFigmaArtifactsToAssets",
                kwargs={"artifact_ids": ["art_005", "art_012"], "export_profile": {"format": "SVG", "scale": "2x"}}
            ),
            Action(
                name="CreateGmailThread",
                kwargs={
                    "sender_email": "settings.lead@company.com",
                    "recipients_emails": ["design-review@company.com", "ux-team@company.com"],
                    "workflow_type": "review",
                    "current_labels": ["profile", "ux"]
                }
            ),
            Action(
                name="CreateReviewCycle",
                kwargs={"artifact_id": "art_005", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="CreateReviewCycle",
                kwargs={"artifact_id": "art_012", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="CreateGmailMessage",
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
            "As tokens.lead@company.com, handle the documentation of design system tokens. Identify Figma artifacts marked with 'tokens' to isolate design elements with token specifications that need PDF export at 1x scale to ensure clarity in documentation. Coordinate with design and UX teams under 'design-system' and 'components' labels for structured organization, and assign a NEEDS_REVIEW status for thorough validation of tokens."
        ),
        actions=[
            Action(
                name="FilterFigmaArtifactsByTags",
                kwargs={"tags": ["tokens"]}
            ),
            Action(
                name="ExportFigmaArtifactsToAssets",
                kwargs={"artifact_ids": ["art_003"], "export_profile": {"format": "PDF", "scale": "1x"}}
            ),
            Action(
                name="CreateGmailThread",
                kwargs={
                    "sender_email": "tokens.lead@company.com",
                    "recipients_emails": ["design-review@company.com", "ux-team@company.com"],
                    "workflow_type": "review",
                    "current_labels": ["design-system", "components"]
                }
            ),
            Action(
                name="CreateReviewCycle",
                kwargs={"artifact_id": "art_003", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="CreateGmailMessage",
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
            "Facilitate a design review session for administrative dashboard components which require stakeholder authorization. Concentrate on artifacts tagged with 'admin' and 'dashboard' to guarantee uniformity in the administrative interface design. Export these designs in SVG format at a 2x scale to ensure scalability and clear quality for developer transfer. Acting as 'admin-reviewer@company.com', collaborate with recipients at design-review@company.com and ux-team@company.com. Arrange your Gmail thread with 'admin' and 'design-review' labels, and establish a NEEDS_REVIEW status to efficiently monitor the review cycle."
        ),
        actions=[
            Action(
                name="FilterFigmaArtifactsByTags",
                kwargs={"tags": ["admin", "dashboard"]}
            ),
            Action(
                name="ExportFigmaArtifactsToAssets",
                kwargs={"artifact_ids": ["art_008"], "export_profile": {"format": "SVG", "scale": "2x"}}
            ),
            Action(
                name="CreateGmailThread",
                kwargs={
                    "sender_email": "admin-reviewer@company.com",
                    "recipients_emails": ["design-review@company.com", "ux-team@company.com"],
                    "workflow_type": "review",
                    "current_labels": ["admin", "design-review"]
                }
            ),
            Action(
                name="CreateReviewCycle",
                kwargs={"artifact_id": "art_008", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="CreateGmailMessage",
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
            "Handle a comprehensive review process for data visualization components that require stakeholder validation. Focus your attention on artifacts tagged with 'table' to ensure uniform data presentation standards across the platform. Generate high-resolution JPG exports at 4x scale for thorough component inspection and documentation purposes. Operating as 'data-reviewer@company.com', collaborate with design-review@company.com and ux-team@company.com recipients to gather comprehensive feedback. Your communication thread must be categorized with 'data-table' and 'component' labels for systematic organization, and establish NEEDS_REVIEW status to initiate the formal review cycle."
        ),
        actions=[
            Action(
                name="FilterFigmaArtifactsByTags",
                kwargs={"tags": ["table"]}
            ),
            Action(
                name="ExportFigmaArtifactsToAssets",
                kwargs={"artifact_ids": ["art_009"], "export_profile": {"format": "JPG", "scale": "4x"}}
            ),
            Action(
                name="CreateGmailThread",
                kwargs={
                    "sender_email": "data-reviewer@company.com",
                    "recipients_emails": ["design-review@company.com", "ux-team@company.com"],
                    "workflow_type": "review",
                    "current_labels": ["data-table", "component"]
                }
            ),
            Action(
                name="CreateReviewCycle",
                kwargs={"artifact_id": "art_009", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="CreateGmailMessage",
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
            "Coordinate a thorough review process for responsive design components that require cross-device compatibility validation. Concentrate on artifacts tagged with 'responsive' to ensure a consistent user experience across various screen sizes and platforms. Create standard-resolution PNG exports at 1x scale for baseline documentation and reference purposes. Working as 'responsive-lead@company.com', engage with design-review@company.com and ux-team@company.com recipients to facilitate comprehensive responsive design evaluation. Your Gmail thread should be organized with 'responsive' and 'design-review' labels for effective categorization, and you must initiate NEEDS_REVIEW status to commence the systematic review workflow."
        ),
        actions=[
            Action(
                name="FilterFigmaArtifactsByTags",
                kwargs={"tags": ["responsive"]}
            ),
            Action(
                name="ExportFigmaArtifactsToAssets",
                kwargs={"artifact_ids": ["art_001"], "export_profile": {"format": "PNG", "scale": "1x"}}
            ),
            Action(
                name="CreateGmailThread",
                kwargs={
                    "sender_email": "responsive-lead@company.com",
                    "recipients_emails": ["design-review@company.com", "ux-team@company.com"],
                    "workflow_type": "review",
                    "current_labels": ["responsive", "design-review"]
                }
            ),
            Action(
                name="CreateReviewCycle",
                kwargs={"artifact_id": "art_001", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="CreateGmailMessage",
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
            "Handle a thorough review process for landing page elements needing responsive design checks across various breakpoints. Your focus must be on items labeled with both 'landing-page' and 'responsive' to guarantee excellent conversion experiences across different devices and screen resolutions. Produce high-quality JPG exports at 2x scale for a detailed visual examination and presentation to stakeholders. Acting as 'conversion-lead@company.com', you'll align with design-review@company.com and ux-team@company.com to collect insightful feedback on conversion enhancement. Ensure your communication thread is methodically tagged with 'marketing' and 'responsive' for effective project monitoring, and establish NEEDS_REVIEW status to initiate the in-depth evaluation process."
        ),
        actions=[
            Action(
                name="FilterFigmaArtifactsByTags",
                kwargs={"tags": ["landing-page", "responsive"]}
            ),
            Action(
                name="ExportFigmaArtifactsToAssets",
                kwargs={"artifact_ids": ["art_001"], "export_profile": {"format": "JPG", "scale": "2x"}}
            ),
            Action(
                name="CreateGmailThread",
                kwargs={
                    "sender_email": "conversion-lead@company.com",
                    "recipients_emails": ["design-review@company.com", "ux-team@company.com"],
                    "workflow_type": "review",
                    "current_labels": ["marketing", "responsive"]
                }
            ),
            Action(
                name="CreateReviewCycle",
                kwargs={"artifact_id": "art_001", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="CreateGmailMessage",
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
            "Coordinate a detailed design release announcement concerning the latest system updates. Direct your attention to release_001, which includes major enhancements to the design system. Your responsibilities include verifying this as an official release version, reviewing changes from the previous iteration, and compiling engaging before/after materials. Document key advancements, such as 'Enhanced component library', 'Improved accessibility standards', and 'Updated design tokens'. Your messages should be sent as 'emma.creative@company.com' to recipients at 'design-team@company.com' and 'product-leads@company.com', appropriately tagged with 'Design/Release' and 'design-system' for visibility. Export hero frames using SVG format at 2x resolution for sharp scalable graphics."
        ),
        actions=[
            Action(
                name="DetectReleaseVersion",
                kwargs={"release_id": "release_001"}
            ),
            Action(
                name="ComputeReleaseDiffs",
                kwargs={
                    "release_id": "release_001",
                    "changelog_highlights": ["Enhanced component library", "Improved accessibility standards", "Updated design tokens"]
                }
            ),
            Action(
                name="SaveReleaseDiffs",
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
                name="FilterFigmaArtifactsByTags",
                kwargs={"tags": ["hero"]}
            ),
            Action(
                name="ExportFigmaArtifactsToAssets",
                kwargs={"artifact_ids": ["art_001"], "export_profile": {"format": "SVG", "scale": "2x"}}
            ),
            Action(
                name="GenerateBeforeAfterVisuals",
                kwargs={
                    "release_id": "release_001",
                    "hero_artifact_ids": ["art_001"]
                }
            ),
            Action(
                name="CreateGmailThread",
                kwargs={
                    "sender_email": "emma.creative@company.com",
                    "recipients_emails": ["design-team@company.com", "product-leads@company.com"],
                    "workflow_type": "release",
                    "current_labels": ["Design/Release", "design-system"]
                }
            ),
            Action(
                name="CreateGmailMessage",
                kwargs={
                    "sender_email": "emma.creative@company.com",
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
            "Handle the task of announcing a significant mobile application release, which marks a pivotal milestone in the evolution of user experience. Work with release_002, which includes comprehensive enhancements to both the mobile interface and user workflow. Your role is to confirm this qualifies as an official release candidate, carry out a thorough change analysis from the prior mobile version, and create impactful visual documentation. Emphasize vital improvements such as 'Revolutionary dashboard redesign', 'Enhanced user onboarding flow', 'Performance optimization features', and 'Advanced personalization options'. Communications should originate from 'jake.design@company.com' and be directed to key stakeholders like 'mobile-team@company.com', 'product-strategy@company.com', and 'executive-leadership@company.com'. Apply strategic labeling with 'Design/Release', 'mobile', and 'launch' to ensure maximum visibility within the organization. Use high-resolution PNG format for your visual assets to document the interface in detail."
        ),
        actions=[
            Action(
                name="DetectReleaseVersion",
                kwargs={"release_id": "release_002"}
            ),
            Action(
                name="ComputeReleaseDiffs",
                kwargs={
                    "release_id": "release_002",
                    "changelog_highlights": ["Revolutionary dashboard redesign", "Enhanced user onboarding flow", "Performance optimization features", "Advanced personalization options"]
                }
            ),
            Action(
                name="SaveReleaseDiffs",
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
                name="FilterFigmaArtifactsByTags",
                kwargs={"tags": ["hero"]}
            ),
            Action(
                name="ExportFigmaArtifactsToAssets",
                kwargs={"artifact_ids": ["art_001"], "export_profile": {"format": "PNG", "scale": "4x"}}
            ),
            Action(
                name="GenerateBeforeAfterVisuals",
                kwargs={
                    "release_id": "release_002",
                    "hero_artifact_ids": ["art_001"]
                }
            ),
            Action(
                name="CreateGmailThread",
                kwargs={
                    "sender_email": "jake.design@company.com",
                    "recipients_emails": ["mobile-team@company.com", "product-strategy@company.com", "executive-leadership@company.com"],
                    "workflow_type": "release",
                    "current_labels": ["Design/Release", "mobile", "launch"]
                }
            ),
            Action(
                name="CreateGmailMessage",
                kwargs={
                    "sender_email": "jake.design@company.com",
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
            "Coordinate the final launch announcement for the marketing website, marking a crucial milestone for the company's online presence. Manage release_003, which is the result of extensive brand alignment and user experience enhancements over several months. Your task includes validating it as the official v1.0.0 launch candidate, performing a comprehensive analysis of updates from the previous marketing version, and crafting compelling launch documentation. Highlight transformative improvements such as 'New brand integration', 'Performance optimizations', 'Mobile responsive design', and 'Enhanced user experience'. The announcement should start from 'anna.brand@company.com' and be sent to essential business stakeholders like 'executive-team@company.com', 'marketing-leads@company.com', and 'brand-partners@company.com' with strategic labeling of 'launch', 'marketing', and 'brand' for optimal organizational impact. Provide high-quality hero visuals in PDF format at 1x scale to meet professional presentation standards."
        ),
        actions=[
            Action(
                name="DetectReleaseVersion",
                kwargs={"release_id": "release_003"}
            ),
            Action(
                name="ComputeReleaseDiffs",
                kwargs={
                    "release_id": "release_003",
                    "changelog_highlights": ["New brand integration", "Performance optimizations", "Mobile responsive design", "Enhanced user experience"]
                }
            ),
            Action(
                name="SaveReleaseDiffs",
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
                name="FilterFigmaArtifactsByTags",
                kwargs={"tags": ["hero"]}
            ),
            Action(
                name="ExportFigmaArtifactsToAssets",
                kwargs={"artifact_ids": ["art_001"], "export_profile": {"format": "PDF", "scale": "1x"}}
            ),
            Action(
                name="GenerateBeforeAfterVisuals",
                kwargs={
                    "release_id": "release_003",
                    "hero_artifact_ids": ["art_001"]
                }
            ),
            Action(
                name="CreateGmailThread",
                kwargs={
                    "sender_email": "anna.brand@company.com",
                    "recipients_emails": ["executive-team@company.com", "marketing-leads@company.com", "brand-partners@company.com"],
                    "workflow_type": "release",
                    "current_labels": ["launch", "marketing", "brand"]
                }
            ),
            Action(
                name="CreateGmailMessage",
                kwargs={
                    "sender_email": "anna.brand@company.com",
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
            "Handle the extensive accessibility transformation for the admin panel, ensuring it aligns with the highest standards while enhancing the user experience for all team members. Your responsibility includes overseeing release_004, a key step forward toward universal design principles and regulatory compliance. Verify this as the final v3.0.0 accessibility milestone, and systematically review the thorough improvements covering 'Enhanced accessibility compliance', 'WCAG 2.1 AA standards', 'Improved screen reader support', and 'Keyboard navigation updates'. Since this is a major structural upgrade, be aware there is no previous release baseline for comparison (prior release ID will be null). Engage important stakeholders like 'accessibility-team@company.com', 'design-review@company.com', and 'compliance-officer@company.com' through strategic communication from 'chris.engineer@company.com', using 'accessibility', 'launch', and 'admin' labels for optimal organizational clarity. Ensure high-quality visual documentation in JPG format at 4x resolution to effectively illustrate compliance accomplishments."
        ),
        actions=[
            Action(
                name="DetectReleaseVersion",
                kwargs={"release_id": "release_004"}
            ),
            Action(
                name="ComputeReleaseDiffs",
                kwargs={
                    "release_id": "release_004",
                    "changelog_highlights": ["Enhanced accessibility compliance", "WCAG 2.1 AA standards", "Improved screen reader support", "Keyboard navigation updates"]
                }
            ),
            Action(
                name="SaveReleaseDiffs",
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
                name="FilterFigmaArtifactsByTags",
                kwargs={"tags": ["hero"]}
            ),
            Action(
                name="ExportFigmaArtifactsToAssets",
                kwargs={
                    "artifact_ids": ["art_001"],
                    "export_profile": {"format": "JPG", "scale": "4x"}
                }
            ),
            Action(
                name="GenerateBeforeAfterVisuals",
                kwargs={
                    "release_id": "release_004",
                    "hero_artifact_ids": ["art_001"]
                }
            ),
            Action(
                name="CreateGmailThread",
                kwargs={
                    "sender_email": "chris.engineer@company.com",
                    "recipients_emails": ["accessibility-team@company.com", "design-review@company.com", "compliance-officer@company.com"],
                    "workflow_type": "release",
                    "current_labels": ["accessibility", "launch", "admin"]
                }
            ),
            Action(
                name="CreateGmailMessage",
                kwargs={
                    "sender_email": "chris.engineer@company.com",
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
            "Coordinate the critical brand transformation that will define the company's visual identity moving forward. Your strategic guidance covers release_005, which marks the peak of detailed brand research and stakeholder alignment across all organizational interactions. Promote this as the formal v2.0.0 brand standard, thoroughly documenting the progressive changes including 'Brand color palette refresh', 'Typography system overhaul', 'Logo usage guidelines', and 'Visual identity standards'. This is a full rebrand without any constraints from past brand iterations (prior release will be null). Your leadership reaches essential brand stewards such as 'brand-partners@company.com', 'marketing-leads@company.com', and 'design-team@company.com' via decisive communication from 'sophie.marketing@company.com', using precise labeling with 'brand', 'guidelines', and 'launch' for widespread organizational adoption. Provide clear vector documentation in SVG format at standard resolution to maintain brand consistency across all digital platforms and ensure smooth implementation."
        ),
        actions=[
            Action(
                name="DetectReleaseVersion",
                kwargs={"release_id": "release_005"}
            ),
            Action(
                name="ComputeReleaseDiffs",
                kwargs={
                    "release_id": "release_005",
                    "changelog_highlights": ["Brand color palette refresh", "Typography system overhaul", "Logo usage guidelines", "Visual identity standards"]
                }
            ),
            Action(
                name="SaveReleaseDiffs",
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
                name="FilterFigmaArtifactsByTags",
                kwargs={"tags": ["hero"]}
            ),
            Action(
                name="ExportFigmaArtifactsToAssets",
                kwargs={
                    "artifact_ids": ["art_001"],
                    "export_profile": {"format": "SVG", "scale": "1x"}
                }
            ),
            Action(
                name="GenerateBeforeAfterVisuals",
                kwargs={
                    "release_id": "release_005",
                    "hero_artifact_ids": ["art_001"]
                }
            ),
            Action(
                name="CreateGmailThread",
                kwargs={
                    "sender_email": "sophie.marketing@company.com",
                    "recipients_emails": ["brand-partners@company.com", "marketing-leads@company.com", "design-team@company.com"],
                    "workflow_type": "release",
                    "current_labels": ["brand", "guidelines", "launch"]
                }
            ),
            Action(
                name="CreateGmailMessage",
                kwargs={
                    "sender_email": "sophie.marketing@company.com",
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
            "Oversee the evolution of your organization's design system by enhancing the navigation components, crucially improving user wayfinding across all digital products. Your expertise is essential for steering release_006, marking the v1.1.0 milestone that builds upon the base established by release_010, systematically progressing the navigation ecosystem through 'Navigation menu redesign', 'Breadcrumb improvements', 'Sidebar component updates', and 'Mobile navigation patterns'. This extensive enhancement involves both structural additions (frame 1:3) and critical updates to existing navigation frameworks (frames 1:4 and 1:5), creating new standards through HomepageHeroSection-v1.19, NavigationBar-v1.13, DesignSystem-v1.12, and ContactFormComponent-v1.20 component versions. Guide essential stakeholders including 'design-system@company.com', 'frontend-team@company.com', and 'product-team@company.com' through authoritative communication from 'emma.creative@company.com', strategically categorizing using 'design-system', 'navigation', and 'components' labels for comprehensive organizational implementation. Present detailed documentation using PDF format at standard resolution for extensive technical specifications meant for development teams."
        ),
        actions=[
            Action(
                name="DetectReleaseVersion",
                kwargs={"release_id": "release_006"}
            ),
            Action(
                name="ComputeReleaseDiffs",
                kwargs={
                    "release_id": "release_006",
                    "changelog_highlights": ["Navigation menu redesign", "Breadcrumb improvements", "Sidebar component updates", "Mobile navigation patterns"]
                }
            ),
            Action(
                name="SaveReleaseDiffs",
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
                name="FilterFigmaArtifactsByTags",
                kwargs={"tags": ["hero"]}
            ),
            Action(
                name="ExportFigmaArtifactsToAssets",
                kwargs={
                    "artifact_ids": ["art_001"],
                    "export_profile": {"format": "PDF", "scale": "1x"}
                }
            ),
            Action(
                name="GenerateBeforeAfterVisuals",
                kwargs={
                    "release_id": "release_006",
                    "hero_artifact_ids": ["art_001"]
                }
            ),
            Action(
                name="CreateGmailThread",
                kwargs={
                    "sender_email": "emma.creative@company.com",
                    "recipients_emails": ["design-system@company.com", "frontend-team@company.com", "product-team@company.com"],
                    "workflow_type": "release",
                    "current_labels": ["design-system", "navigation", "components"]
                }
            ),
            Action(
                name="CreateGmailMessage",
                kwargs={
                    "sender_email": "emma.creative@company.com",
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
            "Handle the design release process for release_007, featuring changelog highlights such as 'Dashboard layout optimization', 'Mobile navigation improvements', 'Widget personalization features', and 'Performance optimizations'. Coordinate with the recipients 'mobile-team@company.com', 'product-owners@company.com', and 'qa-team@company.com' via sender 'jake.design@company.com', using labels 'mobile', 'ux', and 'launch'. Export visuals in JPG format at 2x scale."
        ),
        actions=[
            Action(
                name="DetectReleaseVersion",
                kwargs={"release_id": "release_007"}
            ),
            Action(
                name="ComputeReleaseDiffs",
                kwargs={
                    "release_id": "release_007",
                    "changelog_highlights": ["Dashboard layout optimization", "Mobile navigation improvements", "Widget personalization features", "Performance optimizations"]
                }
            ),
            Action(
                name="SaveReleaseDiffs",
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
                name="FilterFigmaArtifactsByTags",
                kwargs={"tags": ["hero"]}
            ),
            Action(
                name="ExportFigmaArtifactsToAssets",
                kwargs={
                    "artifact_ids": ["art_001"],
                    "export_profile": {"format": "JPG", "scale": "2x"}
                }
            ),
            Action(
                name="GenerateBeforeAfterVisuals",
                kwargs={
                    "release_id": "release_007",
                    "hero_artifact_ids": ["art_001"]
                }
            ),
            Action(
                name="CreateGmailThread",
                kwargs={
                    "sender_email": "jake.design@company.com",
                    "recipients_emails": ["mobile-team@company.com", "product-owners@company.com", "qa-team@company.com"],
                    "workflow_type": "release",
                    "current_labels": ["mobile", "ux", "launch"]
                }
            ),
            Action(
                name="CreateGmailMessage",
                kwargs={
                    "sender_email": "jake.design@company.com",
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
            "You are overseeing the ambitious market expansion initiative that will position your organization at the forefront of digital marketing innovation through strategic beta release orchestration. Your transformative leadership encompasses release_008, representing the pioneering v0.9.0 beta milestone that establishes new market positioning standards with no preceding marketing foundation (prior release will be null). This groundbreaking initiative requires a comprehensive implementation of 'Marketing page optimization', 'Beta feature previews', 'Lead capture enhancements', and 'Content personalization'. Your strategic vision coordinates essential marketing stakeholders including 'marketing@company.com', 'growth-team@company.com', and 'content-team@company.com' through decisive communication from 'anna.brand@company.com' with targeted categorization using 'marketing', 'launch', and 'ab-testing' labels for comprehensive organizational market penetration. You should provide ultra-high-resolution visual documentation using PNG format at 4x scale to showcase marketing excellence and beta feature demonstrations with maximum clarity for stakeholder presentations and market validation processes."
        ),
        actions=[
            Action(
                name="DetectReleaseVersion",
                kwargs={"release_id": "release_008"}
            ),
            Action(
                name="ComputeReleaseDiffs",
                kwargs={
                    "release_id": "release_008",
                    "changelog_highlights": ["Marketing page optimization", "Beta feature previews", "Lead capture enhancements", "Content personalization"]
                }
            ),
            Action(
                name="SaveReleaseDiffs",
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
                name="FilterFigmaArtifactsByTags",
                kwargs={"tags": ["hero"]}
            ),
            Action(
                name="ExportFigmaArtifactsToAssets",
                kwargs={
                    "artifact_ids": ["art_001"],
                    "export_profile": {"format": "PNG", "scale": "4x"}
                }
            ),
            Action(
                name="GenerateBeforeAfterVisuals",
                kwargs={
                    "release_id": "release_008",
                    "hero_artifact_ids": ["art_001"]
                }
            ),
            Action(
                name="CreateGmailThread",
                kwargs={
                    "sender_email": "anna.brand@company.com",
                    "recipients_emails": ["marketing@company.com", "growth-team@company.com", "content-team@company.com"],
                    "workflow_type": "release",
                    "current_labels": ["marketing", "launch", "ab-testing"]
                }
            ),
            Action(
                name="CreateGmailMessage",
                kwargs={
                    "sender_email": "anna.brand@company.com",
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
            "You are required to oversee the deployment of data table improvements for the admin panel system. Examine and process release_009 to update data visualization components and notify administrative teams. Calculate the differences from any previous releases, save the diff analysis, and coordinate communication with admin-team@company.com, data-team@company.com, and backend-team@company.com about the improvements. Filter for hero artifacts to highlight in your communications, export them as 1x SVG assets for technical documentation, and produce before/after visuals to illustrate the enhancements. Create a comprehensive email thread with appropriate admin and data-table labels to track this deployment across all stakeholder groups. Your changelog should concentrate on data table improvements, advanced filtering features, pagination enhancements, and column customization options that will enhance user workflows."
        ),
        actions=[
            Action(
                name="DetectReleaseVersion",
                kwargs={"release_id": "release_009"}
            ),
            Action(
                name="ComputeReleaseDiffs",
                kwargs={
                    "release_id": "release_009",
                    "changelog_highlights": ["Data table improvements", "Advanced filtering features", "Pagination enhancements", "Column customization options"]
                }
            ),
            Action(
                name="SaveReleaseDiffs",
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
                name="FilterFigmaArtifactsByTags",
                kwargs={"tags": ["hero"]}
            ),
            Action(
                name="ExportFigmaArtifactsToAssets",
                kwargs={
                    "artifact_ids": ["art_001"],
                    "export_profile": {"format": "SVG", "scale": "1x"}
                }
            ),
            Action(
                name="GenerateBeforeAfterVisuals",
                kwargs={
                    "release_id": "release_009",
                    "hero_artifact_ids": ["art_001"]
                }
            ),
            Action(
                name="CreateGmailThread",
                kwargs={
                    "sender_email": "chris.engineer@company.com",
                    "recipients_emails": ["admin-team@company.com", "data-team@company.com", "backend-team@company.com"],
                    "workflow_type": "release",
                    "current_labels": ["admin", "data-table"] # , "launch"]
                }
            ),
            Action(
                name="CreateGmailMessage",
                kwargs={
                    "sender_email": "chris.engineer@company.com",
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
            "Handle the announcement of your organization's comprehensive design system v1.0.0. This foundational release introduces core button components, input field standards, and a complete typography system. Ensure that development teams and design system stakeholders receive formal documentation detailing the available components. Include complete PDF documentation in 1x scale for use as an implementation reference. Send the communication to dev-team@company.com and design-system@company.com, using labels 'design-system', 'launch', and 'components' for proper tracking. Utilize release_010 for this announcement, with changelog highlights including 'Core button components', 'Input field standards', and 'Typography system'. Ensure your output contains the visual asset identifier and communication thread details."
        ),
        actions=[
            Action(
                name="DetectReleaseVersion",
                kwargs={"release_id": "release_010"}
            ),
            Action(
                name="ComputeReleaseDiffs",
                kwargs={
                    "release_id": "release_010",
                    "changelog_highlights": ["Core button components", "Input field standards", "Typography system"]
                }
            ),
            Action(
                name="SaveReleaseDiffs",
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
                name="FilterFigmaArtifactsByTags",
                kwargs={"tags": ["hero"]}
            ),
            Action(
                name="ExportFigmaArtifactsToAssets",
                kwargs={
                    "artifact_ids": ["art_001"],
                    "export_profile": {"format": "PDF", "scale": "1x"}
                }
            ),
            Action(
                name="GenerateBeforeAfterVisuals",
                kwargs={
                    "release_id": "release_010",
                    "hero_artifact_ids": ["art_001"]
                }
            ),
            Action(
                name="CreateGmailThread",
                kwargs={
                    "sender_email": "emma.creative@company.com",
                    "recipients_emails": ["dev-team@company.com", "design-system@company.com"],
                    "workflow_type": "release",
                    "current_labels": ["design-system", "launch", "components"]
                }
            ),
            Action(
                name="CreateGmailMessage",
                kwargs={
                    "sender_email": "emma.creative@company.com",
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
            "Coordinate a comprehensive mobile application release campaign for the latest user experience improvements. Focus on release_002 representing major mobile app enhancements, such as user dashboard upgrades and profile editing capabilities. Verify that this qualifies as a proper release version before initiating communications with stakeholders. Capture the development evolution from the previous version, documenting key improvements like 'Enhanced user dashboard', 'New profile editor', 'Improved mobile responsive design', and 'Updated navigation patterns'. Prepare high-resolution documentation using PNG format at 4x scale for a detailed visual review. Communications will be sent from 'jake.design@company.com' to key stakeholders at 'product-team@company.com', 'dev-team@company.com', and 'stakeholders@company.com'. Ensure proper categorization using 'Design/Release', 'mobile', and 'launch' labels for effective project tracking and visibility across teams."
        ),
        actions=[
            Action(
                name="DetectReleaseVersion",
                kwargs={"release_id": "release_002"}
            ),
            Action(
                name="ComputeReleaseDiffs",
                kwargs={
                    "release_id": "release_002",
                    "changelog_highlights": ["Enhanced user dashboard", "New profile editor", "Improved mobile responsive design", "Updated navigation patterns"]
                }
            ),
            Action(
                name="SaveReleaseDiffs",
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
                name="FilterFigmaArtifactsByTags",
                kwargs={"tags": ["hero"]}
            ),
            Action(
                name="ExportFigmaArtifactsToAssets",
                kwargs={"artifact_ids": ["art_001"], "export_profile": {"format": "PNG", "scale": "4x"}}
            ),
            Action(
                name="GenerateBeforeAfterVisuals",
                kwargs={
                    "release_id": "release_002",
                    "hero_artifact_ids": ["art_001"]
                }
            ),
            Action(
                name="CreateGmailThread",
                kwargs={
                    "sender_email": "jake.design@company.com",
                    "recipients_emails": ["product-team@company.com", "dev-team@company.com", "stakeholders@company.com"],
                    "workflow_type": "release",
                    "current_labels": ["Design/Release", "mobile", "launch"]
                }
            ),
            Action(
                name="CreateGmailMessage",
                kwargs={
                    "sender_email": "jake.design@company.com",
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
            "You are managing the release communication for a major design system update focused on accessibility and form enhancements. Your task is to handle release_011 which marks significant advancements in form components and accessibility standards. Your duties include validating this as a potential release candidate, documenting the progression from previous versions, and creating thorough visual documentation. Ensure to emphasize the key upgrades: 'Advanced form components', 'Enhanced accessibility features', and 'Improved user interactions'. Your communication plan requires contacting technical teams as 'emma.creative@company.com', directing messages to 'engineering-team@company.com', 'qa-team@company.com', and 'product-managers@company.com', using the 'Design/Release', 'design-system', and 'components' categories. Export hero graphics in JPG format at 2x resolution for optimal quality and filesize."
        ),
        actions=[
            Action(
                name="DetectReleaseVersion",
                kwargs={"release_id": "release_011"}
            ),
            Action(
                name="ComputeReleaseDiffs",
                kwargs={
                    "release_id": "release_011",
                    "changelog_highlights": ["Advanced form components", "Enhanced accessibility features", "Improved user interactions"]
                }
            ),
            Action(
                name="SaveReleaseDiffs",
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
                name="FilterFigmaArtifactsByTags",
                kwargs={"tags": ["hero"]}
            ),
            Action(
                name="ExportFigmaArtifactsToAssets",
                kwargs={"artifact_ids": ["art_001"], "export_profile": {"format": "JPG", "scale": "2x"}}
            ),
            Action(
                name="GenerateBeforeAfterVisuals",
                kwargs={
                    "release_id": "release_011",
                    "hero_artifact_ids": ["art_001"]
                }
            ),
            Action(
                name="CreateGmailThread",
                kwargs={
                    "sender_email": "emma.creative@company.com",
                    "recipients_emails": ["engineering-team@company.com", "qa-team@company.com", "product-managers@company.com"],
                    "workflow_type": "release",
                    "current_labels": ["Design/Release", "design-system", "components"]
                }
            ),
            Action(
                name="CreateGmailMessage",
                kwargs={
                    "sender_email": "emma.creative@company.com",
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
            "Your task is to handle the mobile app release communication for the latest profile and settings enhancements. You need to oversee the processing of the mobile app release_012 version 2.2.0 which presents improved user profile management and settings controls. Your role involves creating comprehensive release documentation with scalable vector graphics at 4x resolution to ensure clear visuals in all viewing conditions. Use your email, jake.design@company.com, to target product managers at product@company.com, development teams at dev-team@company.com, and QA staff at qa@company.com who require detailed technical information on the release changes. Your communication will center around the 'Profile Settings Enhancement', 'Privacy Controls Update', 'Notification Preferences', and 'Account Management' improvements. Apply the Design/Release labels in addition to mobile, profile, and update categories for proper organization. The expected outcomes include confirmation of successful release processing, exported assets, and communication with stakeholders through email."
        ),
        actions=[
            Action(
                name="DetectReleaseVersion",
                kwargs={"release_id": "release_012"}
            ),
            Action(
                name="ComputeReleaseDiffs",
                kwargs={"release_id": "release_012", "changelog_highlights": ["Profile Settings Enhancement", "Privacy Controls Update", "Notification Preferences", "Account Management"]}
            ),
            Action(
                name="SaveReleaseDiffs",
                kwargs={"release_id": "release_012", "prior_release_id_nullable": "release_002", "frames_added": ["2:2", "2:3"], "frames_updated": ["2:4"], "frames_removed": [], "component_version_bumps": ["MobileAppDashboard-v1.18", "UserProfileScreen-v1.17", "SettingsScreen-v1.14"], "changelog_highlights": ["Profile Settings Enhancement", "Privacy Controls Update", "Notification Preferences", "Account Management"]}
            ),
            Action(
                name="FilterFigmaArtifactsByTags",
                kwargs={"tags": ["hero"]}
            ),
            Action(
                name="ExportFigmaArtifactsToAssets",
                kwargs={"artifact_ids": ["art_001"], "export_profile": {"format": "SVG", "scale": "4x"}}
            ),
            Action(
                name="GenerateBeforeAfterVisuals",
                kwargs={"release_id": "release_012", "hero_artifact_ids": ["art_001"]}
            ),
            Action(
                name="CreateGmailThread",
                kwargs={"sender_email": "jake.design@company.com", "recipients_emails": ["product@company.com", "dev-team@company.com", "qa@company.com"], "workflow_type": "release", "current_labels": ["Design/Release", "mobile", "profile", "update"]}
            ),
            Action(
                name="CreateGmailMessage",
                kwargs={"sender_email": "jake.design@company.com", "workflow_type": "release", "thread_id": "thread_015", "attachments_asset_ids": ["asset_art_001_svg_4x"]}
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
            "Handle a comprehensive design system communication campaign aimed at technical implementation teams. Concentrate on the enhanced component library release_001, which provides essential upgrades for cross-platform compatibility and developer experience. Coordinate the announcement of release_001, focusing on the 'Component Library Overhaul', 'Token System Refinement', 'Cross-Platform Compatibility' improvements, and enhancements to 'Developer Experience'. Utilize high-quality JPEG assets at 2x resolution to ensure ideal rendering on various technical documentation platforms. Engage with engineering teams via engineering@company.com, design system specialists at design-system@company.com, and accessibility experts at accessibility@company.com, using your email emma.creative@company.com for sending detailed technical specifications required for implementation. Apply Design/Release labels and organize using design-system, accessibility, and components categories. Your efforts will bridge design innovation with technical application, facilitating seamless adoption across all development environments. Anticipated outcomes include validated release processing, enhanced visual assets, and focused stakeholder communication."
        ),
        actions=[
            Action(
                name="DetectReleaseVersion",
                kwargs={"release_id": "release_001"}
            ),
            Action(
                name="ComputeReleaseDiffs",
                kwargs={"release_id": "release_001", "changelog_highlights": ["Component Library Overhaul", "Token System Refinement", "Cross-Platform Compatibility", "Developer Experience"]}
            ),
            Action(
                name="SaveReleaseDiffs",
                kwargs={"release_id": "release_001", "prior_release_id_nullable": "release_006", "frames_added": ["1:3", "1:4"], "frames_updated": ["1:5"], "frames_removed": [], "component_version_bumps": ["HomepageHeroSection-v1.19", "NavigationBar-v1.13", "DesignSystem-v1.12", "ContactFormComponent-v1.20"], "changelog_highlights": ["Component Library Overhaul", "Token System Refinement", "Cross-Platform Compatibility", "Developer Experience"]}
            ),
            Action(
                name="FilterFigmaArtifactsByTags",
                kwargs={"tags": ["hero"]}
            ),
            Action(
                name="ExportFigmaArtifactsToAssets",
                kwargs={"artifact_ids": ["art_001"], "export_profile": {"format": "JPG", "scale": "2x"}}
            ),
            Action(
                name="GenerateBeforeAfterVisuals",
                kwargs={"release_id": "release_001", "hero_artifact_ids": ["art_001"]}
            ),
            Action(
                name="CreateGmailThread",
                kwargs={"sender_email": "emma.creative@company.com", "recipients_emails": ["engineering@company.com", "design-system@company.com", "accessibility@company.com"], "workflow_type": "release", "current_labels": ["Design/Release", "design-system", "accessibility", "components"]}
            ),
            Action(
                name="CreateGmailMessage",
                kwargs={"sender_email": "emma.creative@company.com", "workflow_type": "release", "thread_id": "thread_015", "attachments_asset_ids": ["asset_art_001_jpg_2x"]}
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
            "Coordinate a thorough review of data table designs needing technical feedback. Concentrate on artifacts tagged 'table' to guarantee data visualization aligns with backend integration requirements. Export in PNG format at 1x scale to provide clear details for the technical review. Operate as 'data-architect@company.com' and address emails to backend-team@company.com and qa-engineers@company.com. Implement 'data-table', 'review', and 'admin' labels to ensure correct categorization, and assign the NEEDS_REVIEW status to the artifact for effective tracking."
        ),
        actions=[
            Action(
                name="FilterFigmaArtifactsByTags",
                kwargs={"tags": ["table"]}
            ),
            Action(
                name="ExportFigmaArtifactsToAssets",
                kwargs={"artifact_ids": ["art_009"], "export_profile": {"format": "PNG", "scale": "1x"}}
            ),
            Action(
                name="CreateGmailThread",
                kwargs={
                    "sender_email": "data-architect@company.com",
                    "recipients_emails": ["backend-team@company.com", "qa-engineers@company.com"],
                    "workflow_type": "review",
                    "current_labels": ["data-table", "review", "admin"]
                }
            ),
            Action(
                name="CreateReviewCycle",
                kwargs={"artifact_id": "art_009", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="CreateGmailMessage",
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
            "Handle a comprehensive user experience review concentrating on the profile interface design. Your duty involves organizing feedback from product teams and user research specialists for 'user' tagged artifacts to ensure interface usability aligns with design standards. Export using SVG format at 2x scale for high-quality vector graphics appropriate for detailed UX analysis. Communicate as 'ux-designer@company.com' with recipients product-team@company.com and user-research@company.com. Utilize 'ux', 'review', and 'profile' labels for accurate workflow tracking, and set the status to NEEDS_REVIEW to start the review process."
        ),
        actions=[
            Action(
                name="FilterFigmaArtifactsByTags",
                kwargs={"tags": ["user"]}
            ),
            Action(
                name="ExportFigmaArtifactsToAssets",
                kwargs={"artifact_ids": ["art_005"], "export_profile": {"format": "SVG", "scale": "2x"}}
            ),
            Action(
                name="CreateGmailThread",
                kwargs={
                    "sender_email": "ux-designer@company.com",
                    "recipients_emails": ["product-team@company.com", "user-research@company.com"],
                    "workflow_type": "review",
                    "current_labels": ["ux", "review", "profile"]
                }
            ),
            Action(
                name="CreateReviewCycle",
                kwargs={"artifact_id": "art_005", "status": "NEEDS_REVIEW", "thread_id_nullable": "thread_015"}
            ),
            Action(
                name="CreateGmailMessage",
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
            "Coordinate the release announcement for important accessibility updates in the admin panel. Emphasize release_004 which introduces major WCAG 2.1 compliance enhancements like ARIA-compliant form elements, High contrast color schemes, Keyboard navigation improvements, and Screen reader compatibility enhancements. Your task includes identifying version details, calculating comprehensive release differences that may include no prior release (prior_release_id_nullable: None), documenting changes with frames added, component version updates, and specific changelog highlights. Communicate from 'accessibility-lead@company.com' and address stakeholders at 'admin-team@company.com' and 'compliance-team@company.com' with suitable 'Design/Release', 'accessibility', and 'admin' labels for correct categorization. Export documentation using PDF format at 1x scale for complete accessibility compliance records."
        ),
        actions=[
            Action(
                name="DetectReleaseVersion",
                kwargs={"release_id": "release_004"}
            ),
            Action(
                name="ComputeReleaseDiffs",
                kwargs={
                    "release_id": "release_004",
                    "changelog_highlights": ["ARIA-compliant form elements", "High contrast color schemes", "Keyboard navigation improvements", "Screen reader compatibility enhancements"]
                }
            ),
            Action(
                name="SaveReleaseDiffs",
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
                name="FilterFigmaArtifactsByTags",
                kwargs={"tags": ["hero"]}
            ),
            Action(
                name="ExportFigmaArtifactsToAssets",
                kwargs={"artifact_ids": ["art_001"], "export_profile": {"format": "PDF", "scale": "1x"}}
            ),
            Action(
                name="GenerateBeforeAfterVisuals",
                kwargs={
                    "release_id": "release_004",
                    "hero_artifact_ids": ["art_001"]
                }
            ),
            Action(
                name="CreateGmailThread",
                kwargs={
                    "sender_email": "accessibility-lead@company.com",
                    "recipients_emails": ["admin-team@company.com", "compliance-team@company.com"],
                    "workflow_type": "release",
                    "current_labels": ["Design/Release", "accessibility", "admin"]
                }
            ),
            Action(
                name="CreateGmailMessage",
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
            "Handle the coordination of the beta release communication concerning the marketing website redesign project. Focus specifically on release_008, denoting the v0.9.0 beta release that comes with crucial testing integrations and enhanced performance optimizations. Aim to prepare detailed release documentation and stakeholder communication emphasizing recent gains in beta functionality and user experience improvements by the marketing team. Your strategy should highlight the Beta Testing Integration, Performance Optimization, Bug Fixes, and Feature Completion enhancements, while advancing from the groundwork set by release_007. Prioritize the usage of PNG assets at a 4x resolution to achieve superior visual clarity across all marketing platforms and presentations to stakeholders. Ensure your communication reaches both technical team@company.com and dev@company.com stakeholders via suitable team distribution channels, employing 'marketing' and 'launch' organizational labels."
        ),
        actions=[
            Action(
                name="DetectReleaseVersion",
                kwargs={"release_id": "release_008"}
            ),
            Action(
                name="ComputeReleaseDiffs",
                kwargs={"release_id": "release_008", "changelog_highlights": ["Beta Testing Integration", "Performance Optimization", "Bug Fixes", "Feature Completion"]}
            ),
            Action(
                name="SaveReleaseDiffs",
                kwargs={"release_id": "release_008", "prior_release_id_nullable": "release_007", "frames_added": ["3:3"], "frames_updated": [], "frames_removed": [], "component_version_bumps": ["MarketingWebsite-v1.16", "PricingPage-v1.11"], "changelog_highlights": ["Beta Testing Integration", "Performance Optimization", "Bug Fixes", "Feature Completion"]}
            ),
            Action(
                name="FilterFigmaArtifactsByTags",
                kwargs={"tags": ["hero"]}
            ),
            Action(
                name="ExportFigmaArtifactsToAssets",
                kwargs={"artifact_ids": ["art_001"], "export_profile": {"format": "PNG", "scale": "4x"}}
            ),
            Action(
                name="GenerateBeforeAfterVisuals",
                kwargs={"release_id": "release_008", "hero_artifact_ids": ["art_001"]}
            ),
            Action(
                name="CreateGmailThread",
                kwargs={"sender_email": "anna.brand@company.com", "recipients_emails": ["team@company.com", "dev@company.com"], "workflow_type": "release", "current_labels": ["marketing", "launch"]}
            ),
            Action(
                name="CreateGmailMessage",
                kwargs={"sender_email": "anna.brand@company.com", "workflow_type": "release", "thread_id": "thread_015", "attachments_asset_ids": ["asset_art_001_png_4x"] }
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
            "Arrange the orchestration of the admin panel release communication related to the most recent data table component improvements. This task involves release_009, which signifies the v2.5.0 milestone introducing substantial Data Table Enhancement, Admin Dashboard Refinement, Component Architecture improvements, and User Experience Improvement features. Establish thorough documentation and stakeholder consensus regarding the advancements of the administrative platform, leveraging the foundational elements introduced in release_006. Ensure that scalable SVG assets at 1x resolution are prioritized to provide sharp rendering across various administrative interfaces and documentation systems. Your communication plan should effectively reach admin-team@company.com and stakeholders@company.com, using targeted distribution from your email address chris.engineer@company.com, with 'admin' and 'components' organizational labels."
        ),
        actions=[
            Action(
                name="DetectReleaseVersion",
                kwargs={"release_id": "release_009"}
            ),
            Action(
                name="ComputeReleaseDiffs",
                kwargs={"release_id": "release_009", "changelog_highlights": ["Data Table Enhancement", "Admin Dashboard Refinement", "Component Architecture", "User Experience Improvement"]}
            ),
            Action(
                name="SaveReleaseDiffs",
                kwargs={"release_id": "release_009", "prior_release_id_nullable": "release_006", "frames_added": ["4:2", "4:3"], "frames_updated": [], "frames_removed": [], "component_version_bumps": ['AdminPanelHeader-v1.16','DataTableComponent-v1.18'], "changelog_highlights": ["Data Table Enhancement", "Admin Dashboard Refinement", "Component Architecture", "User Experience Improvement"]}
            ),
            Action(
                name="FilterFigmaArtifactsByTags",
                kwargs={"tags": ["hero"]}
            ),
            Action(
                name="ExportFigmaArtifactsToAssets",
                kwargs={"artifact_ids": ["art_001"], "export_profile": {"format": "SVG", "scale": "1x"}}
            ),
            Action(
                name="GenerateBeforeAfterVisuals",
                kwargs={"release_id": "release_009", "hero_artifact_ids": ["art_001"]}
            ),
            Action(
                name="CreateGmailThread",
                kwargs={"sender_email": "chris.engineer@company.com", "recipients_emails": ["admin-team@company.com", "stakeholders@company.com"], "workflow_type": "release", "current_labels": ["admin", "components"]}
            ),
            Action(
                name="CreateGmailMessage",
                kwargs={"sender_email": "chris.engineer@company.com", "workflow_type": "release", "thread_id": "thread_015", "attachments_asset_ids": ["asset_art_001_svg_1x"]}
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
            "Handle the release communication for the Admin Panel v2.5.0 data table component update. Coordinate the design handoff between development and stakeholder teams for this major component architecture enhancement. Concentrate on the release_009 version, which includes table filtering improvements, data pagination updates, and component accessibility enhancements. Build upon the previous release_006 version to establish proper diff tracking. Export assets in SVG format at 1x scale for optimal development handoff. Ensure that communication originates from chris.engineer@company.com and targets admin-team@company.com and stakeholders@company.com. Guarantee correct tagging with admin, data-table, and Design/Release labels for efficient categorization and tracking of this component-focused release."
        ),
        actions=[
            Action(
                name="DetectReleaseVersion",
                kwargs={"release_id": "release_009"}
            ),
            Action(
                name="ComputeReleaseDiffs",
                kwargs={
                    "release_id": "release_009",
                    "changelog_highlights": ["table filtering improvements", "data pagination updates", "component accessibility enhancements"]
                }
            ),
            Action(
                name="SaveReleaseDiffs",
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
                name="FilterFigmaArtifactsByTags",
                kwargs={"tags": ["hero"]}
            ),
            Action(
                name="ExportFigmaArtifactsToAssets",
                kwargs={
                    "artifact_ids": ["art_001"],
                    "export_profile": {"format": "SVG", "scale": "1x"}
                }
            ),
            Action(
                name="GenerateBeforeAfterVisuals",
                kwargs={
                    "release_id": "release_009",
                    "hero_artifact_ids": ["art_001"]
                }
            ),
            Action(
                name="CreateGmailThread",
                kwargs={
                    "sender_email": "chris.engineer@company.com",
                    "recipients_emails": ["admin-team@company.com", "stakeholders@company.com"],
                    "workflow_type": "release",
                    "current_labels": ["admin", "data-table", "Design/Release"]
                }
            ),
            Action(
                name="CreateGmailMessage",
                kwargs={
                    "sender_email": "chris.engineer@company.com",
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
                "owner_email": "chris.engineer@company.com"
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
            "Conduct a comprehensive design system audit for the Homepage Hero Section (art_001)."
        ),
        actions=[
            Action(
                name="CreateAuditSession",
                kwargs={"artifact_id": "art_001", "audit_type": "DS_MAPPING"}
            ),
            Action(
                name="IdentifyCustomGroupsAndMapToDsComponents",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="RecordDsAuditFindings",
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
                name="GenerateAuditReport",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="LinkAuditReportAsset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            ),
            Action(
                name="UpdateAuditStatus",
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
            "As a professional designer, conduct a comprehensive audit of the design system for the Product Features Display (art_002)."
        ),
        actions=[
            Action(
                name="CreateAuditSession",
                kwargs={"artifact_id": "art_002", "audit_type": "DS_MAPPING"}
            ),
            Action(
                name="IdentifyCustomGroupsAndMapToDsComponents",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="RecordDsAuditFindings",
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
                name="GenerateAuditReport",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="LinkAuditReportAsset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            ),
            Action(
                name="UpdateAuditStatus",
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
            "You are preparing for a major rebranding; coordinate a design system audit on the User Navigation Menu (art_003)."
        ),
        actions=[
            Action(
                name="CreateAuditSession",
                kwargs={"artifact_id": "art_003", "audit_type": "DS_MAPPING"}
            ),
            Action(
                name="IdentifyCustomGroupsAndMapToDsComponents",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="RecordDsAuditFindings",
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
                name="GenerateAuditReport",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="LinkAuditReportAsset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            ),
            Action(
                name="UpdateAuditStatus",
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
            "You are required to conduct a design system audit for the Footer Contact Form (art_004)."
        ),
        actions=[
            Action(
                name="CreateAuditSession",
                kwargs={"artifact_id": "art_004", "audit_type": "DS_MAPPING"}
            ),
            Action(
                name="IdentifyCustomGroupsAndMapToDsComponents",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="RecordDsAuditFindings",
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
                name="GenerateAuditReport",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="LinkAuditReportAsset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            ),
            Action(
                name="UpdateAuditStatus",
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
            "You need to carry out a design system audit on the Shopping Cart Widget (art_005)."
        ),
        actions=[
            Action(
                name="CreateAuditSession",
                kwargs={"artifact_id": "art_005", "audit_type": "DS_MAPPING"}
            ),
            Action(
                name="IdentifyCustomGroupsAndMapToDsComponents",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="RecordDsAuditFindings",
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
                name="GenerateAuditReport",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="LinkAuditReportAsset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            ),
            Action(
                name="UpdateAuditStatus",
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
            "You are required to conduct an analysis of the Social Media Feed (art_006) utilizing a design system audit."
        ),
        actions=[
            Action(
                name="CreateAuditSession",
                kwargs={"artifact_id": "art_006", "audit_type": "DS_MAPPING"}
            ),
            Action(
                name="IdentifyCustomGroupsAndMapToDsComponents",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="RecordDsAuditFindings",
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
                name="GenerateAuditReport",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="LinkAuditReportAsset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            ),
            Action(
                name="UpdateAuditStatus",
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
            "Your goal is to evaluate the Mobile App Sidebar (art_007) by performing a design system audit."
        ),
        actions=[
            Action(
                name="CreateAuditSession",
                kwargs={"artifact_id": "art_007", "audit_type": "DS_MAPPING"}
            ),
            Action(
                name="IdentifyCustomGroupsAndMapToDsComponents",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="RecordDsAuditFindings",
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
                name="GenerateAuditReport",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="LinkAuditReportAsset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            ),
            Action(
                name="UpdateAuditStatus",
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
            "You intend to verify your new workflow for design system audits on the Dashboard Charts Panel (art_008)."
        ),
        actions=[
            Action(
                name="CreateAuditSession",
                kwargs={"artifact_id": "art_008", "audit_type": "DS_MAPPING"}
            ),
            Action(
                name="IdentifyCustomGroupsAndMapToDsComponents",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="RecordDsAuditFindings",
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
                name="GenerateAuditReport",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="LinkAuditReportAsset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            ),
            Action(
                name="UpdateAuditStatus",
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
            "You are required to start a design system audit on the Login Modal Dialog (art_009) to assess the work of a new team member."
        ),
        actions=[
            Action(
                name="CreateAuditSession",
                kwargs={"artifact_id": "art_009", "audit_type": "DS_MAPPING"}
            ),
            Action(
                name="IdentifyCustomGroupsAndMapToDsComponents",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="RecordDsAuditFindings",
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
                name="GenerateAuditReport",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="LinkAuditReportAsset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            ),
            Action(
                name="UpdateAuditStatus",
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
            "Your supervisor has asked you to assess the Search Results Layout (art_010) by conducting a design system audit."
        ),
        actions=[
            Action(
                name="CreateAuditSession",
                kwargs={"artifact_id": "art_010", "audit_type": "DS_MAPPING"}
            ),
            Action(
                name="IdentifyCustomGroupsAndMapToDsComponents",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="RecordDsAuditFindings",
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
                name="GenerateAuditReport",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="LinkAuditReportAsset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            ),
            Action(
                name="UpdateAuditStatus",
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
            "You need to carry out a design system audit on the Profile Settings Card (art_011) to confirm the coherence of your design systems."
        ),
        actions=[
            Action(
                name="CreateAuditSession",
                kwargs={"artifact_id": "art_011", "audit_type": "DS_MAPPING"}
            ),
            Action(
                name="IdentifyCustomGroupsAndMapToDsComponents",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="RecordDsAuditFindings",
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
                name="GenerateAuditReport",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="LinkAuditReportAsset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            ),
            Action(
                name="UpdateAuditStatus",
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
            "A new app is being released and you need to conduct a design system audit for the Notification Center (art_012)."
        ),
        actions=[
            Action(
                name="CreateAuditSession",
                kwargs={"artifact_id": "art_012", "audit_type": "DS_MAPPING"}
            ),
            Action(
                name="IdentifyCustomGroupsAndMapToDsComponents",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="RecordDsAuditFindings",
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
                name="GenerateAuditReport",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="LinkAuditReportAsset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            ),
            Action(
                name="UpdateAuditStatus",
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
            "An accessibility audit must be conducted on the Navigation Bar artifact."
        ),
        actions=[
            Action(
                name="GetArtifactIdFromName",
                kwargs={"artifact_name": "Navigation Bar"}
            ),
            Action(
                name="CreateAuditSession",
                kwargs={"artifact_id": "art_002", "audit_type": "A11Y"}
            ),
            Action(
                name="EvaluateAccessibility",
                kwargs={"artifact_id": "art_002"}
            ),
            Action(
                name="RecordAccessibilityAuditFindings",
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
                name="GenerateAuditReport",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="LinkAuditReportAsset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            ),
            Action(
                name="UpdateAuditStatus",
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
            "Handle an accessibility audit for the Homepage Hero Section. This task includes locating the artifact, setting up an audit session, identifying accessibility issues, documenting observations, producing a report, associating the report with the audit, and finalizing the audit. Provide the audit session details, accessibility violations identified, recorded audit findings, and the information of the final audit report asset."
        ),
        actions=[
            Action(
                name="GetArtifactIdFromName",
                kwargs={"artifact_name": "Homepage Hero Section"}
            ),
            Action(
                name="CreateAuditSession",
                kwargs={"artifact_id": "art_001", "audit_type": "A11Y"}
            ),
            Action(
                name="EvaluateAccessibility",
                kwargs={"artifact_id": "art_001"}
            ),
            Action(
                name="RecordAccessibilityAuditFindings",
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
                name="GenerateAuditReport",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="LinkAuditReportAsset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            ),
            Action(
                name="UpdateAuditStatus",
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
            "Coordinate an accessibility audit on the Contact Form Component artifact by applying workflow 3b."
        ),
        actions=[
            Action(
                name="GetArtifactIdFromName",
                kwargs={"artifact_name": "Contact Form Component"}
            ),
            Action(
                name="CreateAuditSession",
                kwargs={"artifact_id": "art_011", "audit_type": "A11Y"}
            ),
            Action(
                name="EvaluateAccessibility",
                kwargs={"artifact_id": "art_011"}
            ),
            Action(
                name="RecordAccessibilityAuditFindings",
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
                name="GenerateAuditReport",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="LinkAuditReportAsset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            ),
            Action(
                name="UpdateAuditStatus",
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
            "Coordinate an accessibility audit on the Data Table Component artifact utilizing workflow 3b."
        ),
        actions=[
            Action(
                name="GetArtifactIdFromName",
                kwargs={"artifact_name": "Data Table Component"}
            ),
            Action(
                name="CreateAuditSession",
                kwargs={"artifact_id": "art_009", "audit_type": "A11Y"}
            ),
            Action(
                name="EvaluateAccessibility",
                kwargs={"artifact_id": "art_009"}
            ),
            Action(
                name="RecordAccessibilityAuditFindings",
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
                name="GenerateAuditReport",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="LinkAuditReportAsset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            ),
            Action(
                name="UpdateAuditStatus",
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
            "Coordinate an accessibility audit on the Settings Screen artifact utilizing workflow 3b."
        ),
        actions=[
            Action(
                name="GetArtifactIdFromName",
                kwargs={"artifact_name": "Settings Screen"}
            ),
            Action(
                name="CreateAuditSession",
                kwargs={"artifact_id": "art_012", "audit_type": "A11Y"}
            ),
            Action(
                name="EvaluateAccessibility",
                kwargs={"artifact_id": "art_012"}
            ),
            Action(
                name="RecordAccessibilityAuditFindings",
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
                name="GenerateAuditReport",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="LinkAuditReportAsset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            ),
            Action(
                name="UpdateAuditStatus",
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
            "You are required to handle an accessibility audit on the Admin Panel Header artifact using workflow 3b."
        ),
        actions=[
            Action(
                name="GetArtifactIdFromName",
                kwargs={"artifact_name": "Admin Panel Header"}
            ),
            Action(
                name="CreateAuditSession",
                kwargs={"artifact_id": "art_008", "audit_type": "A11Y"}
            ),
            Action(
                name="EvaluateAccessibility",
                kwargs={"artifact_id": "art_008"}
            ),
            Action(
                name="RecordAccessibilityAuditFindings",
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
                name="GenerateAuditReport",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="LinkAuditReportAsset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            ),
            Action(
                name="UpdateAuditStatus",
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
            "You are tasked with conducting a comprehensive accessibility audit for the Pricing Page design component. You should carry out a thorough evaluation to identify potential accessibility issues and create a detailed audit report. Record any findings with HIGH severity issues that demand immediate attention, generate a comprehensive PDF audit report, and update the audit status to COMPLETED upon completion."
        ),
        actions=[
            Action(
                name="GetArtifactIdFromName",
                kwargs={"artifact_name": "Pricing Page"}
            ),
            Action(
                name="CreateAuditSession",
                kwargs={"artifact_id": "art_007", "audit_type": "A11Y"}
            ),
            Action(
                name="EvaluateAccessibility",
                kwargs={"artifact_id": "art_007"}
            ),
            Action(
                name="RecordAccessibilityAuditFindings",
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
                name="GenerateAuditReport",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="LinkAuditReportAsset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            ),
            Action(
                name="UpdateAuditStatus",
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
            "Handle a thorough accessibility audit for the Mobile App Dashboard design. Evaluate the interface to check for color contrast compliance along with other accessibility standards, aiming to achieve WCAG AA conformance. Your analysis should pinpoint any violations hindering users with visual impairments from effectively interacting with the dashboard. Document any HIGH severity contrast issues and compile a detailed audit report including specific remediation recommendations."
        ),
        actions=[
            Action(
                name="GetArtifactIdFromName",
                kwargs={"artifact_name": "Mobile App Dashboard"}
            ),
            Action(
                name="CreateAuditSession",
                kwargs={"artifact_id": "art_004", "audit_type": "A11Y"}
            ),
            Action(
                name="EvaluateAccessibility",
                kwargs={"artifact_id": "art_004"}
            ),
            Action(
                name="RecordAccessibilityAuditFindings",
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
                name="GenerateAuditReport",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="LinkAuditReportAsset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            ),
            Action(
                name="UpdateAuditStatus",
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
            "Coordinate a thorough accessibility audit for the Design System page to ensure all design components align with accessibility standards. Your audit should uncover any HIGH severity violations necessitating immediate remediation and produce a detailed PDF report including specific recommendations to enhance accessibility compliance."
        ),
        actions=[
            Action(
                name="GetArtifactIdFromName",
                kwargs={"artifact_name": "Design System"}
            ),
            Action(
                name="CreateAuditSession",
                kwargs={"artifact_id": "art_003", "audit_type": "A11Y"}
            ),
            Action(
                name="EvaluateAccessibility",
                kwargs={"artifact_id": "art_003"}
            ),
            Action(
                name="RecordAccessibilityAuditFindings",
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
                name="GenerateAuditReport",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="LinkAuditReportAsset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            ),
            Action(
                name="UpdateAuditStatus",
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
            "Handle a thorough accessibility audit for the User Profile Screen to ensure optimal usability for all users. Evaluate text sizing, readability standards, and other accessibility compliance factors to identify areas needing improvement. Focus your audit on HIGH severity text sizing issues that impact user experience and create a comprehensive report with actionable recommendations for meeting accessibility guidelines."
        ),
        actions=[
            Action(
                name="GetArtifactIdFromName",
                kwargs={"artifact_name": "User Profile Screen"}
            ),
            Action(
                name="CreateAuditSession",
                kwargs={"artifact_id": "art_005", "audit_type": "A11Y"}
            ),
            Action(
                name="EvaluateAccessibility",
                kwargs={"artifact_id": "art_005"}
            ),
            Action(
                name="RecordAccessibilityAuditFindings",
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
                name="GenerateAuditReport",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="LinkAuditReportAsset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            ),
            Action(
                name="UpdateAuditStatus",
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
            "Coordinate an accessibility audit on the Marketing Website. Aim to identify any RTL language support issues and compile a comprehensive audit report."
        ),
        actions=[
            Action(
                name="GetArtifactIdFromName",
                kwargs={"artifact_name": "Marketing Website"}
            ),
            Action(
                name="CreateAuditSession",
                kwargs={"artifact_id": "art_006", "audit_type": "A11Y"}
            ),
            Action(
                name="EvaluateAccessibility",
                kwargs={"artifact_id": "art_006"}
            ),
            Action(
                name="RecordAccessibilityAuditFindings",
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
                name="GenerateAuditReport",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="LinkAuditReportAsset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            ),
            Action(
                name="UpdateAuditStatus",
                kwargs={"audit_id": "audit_013", "status": "COMPLETED"}
            )
        ],
        outputs=[{"audit_id": "audit_013", "finding_id": "finding_a11y_016", "report_asset_id": "asset_019"}]
    ),
    Task(
        annotator="0",
        user_id="task_069",
        instruction=(
            "Handle an accessibility audit of the Brand Guidelines. Aim to pinpoint any touch target sizing problems and produce a detailed audit report."
        ),
        actions=[
            Action(
                name="GetArtifactIdFromName",
                kwargs={"artifact_name": "Brand Guidelines"}
            ),
            Action(
                name="CreateAuditSession",
                kwargs={"artifact_id": "art_010", "audit_type": "A11Y"}
            ),
            Action(
                name="EvaluateAccessibility",
                kwargs={"artifact_id": "art_010"}
            ),
            Action(
                name="RecordAccessibilityAuditFindings",
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
                name="GenerateAuditReport",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="LinkAuditReportAsset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            ),
            Action(
                name="UpdateAuditStatus",
                kwargs={"audit_id": "audit_013", "status": "COMPLETED"}
            )
        ],
        outputs=[{"audit_id": "audit_013", "finding_id": "finding_a11y_016", "report_asset_id": "asset_019"}]
    ),
    Task(
        annotator="0",
        user_id="task_070",
        instruction=(
            "Coordinate a joint audit of the Homepage Hero Section focusing on design system and accessibility. Seek to reveal both design system compliance and accessibility breaches to uphold thorough quality standards."
        ),
        actions=[
            Action(
                name="GetArtifactIdFromName",
                kwargs={"artifact_name": "Homepage Hero Section"}
            ),
            Action(
                name="CreateAuditSession",
                kwargs={"artifact_id": "art_001", "audit_type": "COMBINED_DS_A11Y"}
            ),
            Action(
                name="IdentifyCustomGroupsAndMapToDsComponents",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="RecordDsAuditFindings",
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
                name="EvaluateAccessibility",
                kwargs={"artifact_id": "art_001"}
            ),
            Action(
                name="RecordAccessibilityAuditFindings",
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
                name="GenerateAuditReport",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="UpdateAuditStatus",
                kwargs={"audit_id": "audit_013", "status": "COMPLETED"}
            ),
            Action(
                name="LinkAuditReportAsset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            )
        ],
        outputs=[{"audit_id": "audit_013", "finding_ds_id": "finding_ds_016", "finding_a11y_id": "finding_a11y_016", "report_asset_id": "asset_019"}]
    ),
    Task(
        annotator="0",
        user_id="task_071",
        instruction=(
            "Intend to conduct a thorough combined examination of the design system and accessibility for the Navigation Bar artifact. This will assess both the mapping of design system components and adherence to accessibility standards in one complete audit procedure."
        ),
        actions=[
            Action(
                name="GetArtifactIdFromName",
                kwargs={"artifact_name": "Navigation Bar"}
            ),
            Action(
                name="CreateAuditSession",
                kwargs={"artifact_id": "art_002", "audit_type": "COMBINED_DS_A11Y"}
            ),
            Action(
                name="IdentifyCustomGroupsAndMapToDsComponents",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="RecordDsAuditFindings",
                kwargs={"audit_id": "audit_013", "layer_id": "1:2", "layer_name": "Navigation Bar", "finding_type": "UNMAPPED", "recommended_component_id_nullable": "Navigation-v2.3", "severity": "HIGH"}
            ),
            Action(
                name="EvaluateAccessibility",
                kwargs={"artifact_id": "art_002"}
            ),
            Action(
                name="RecordAccessibilityAuditFindings",
                kwargs={"audit_id": "audit_013", "layer_id": "1:2", "layer_name": "Navigation Bar", "violation_type": "RTL", "violation_details_json": {"issue": "Icon alignment", "description": "Layout doesn't adapt to RTL languages"}, "severity": "HIGH", "recommended_fix_summary": "Implement flexible layout that supports RTL languages"}
            ),
            Action(
                name="GenerateAuditReport",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="UpdateAuditStatus",
                kwargs={"audit_id": "audit_013", "status": "COMPLETED"}
            ),
            Action(
                name="LinkAuditReportAsset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            )
        ],
        outputs=[{"audit_id": "audit_013", "finding_ds_id": "finding_ds_016", "finding_a11y_id": "finding_a11y_016", "report_asset_id": "asset_019"}]
    ),
    Task(
        annotator="0",
        user_id="task_072",
        instruction=(
            "Plan to execute an extensive combined audit of design system and accessibility on the Design System artifact. This will analyze both the mapping of design system components and compliance with accessibility criteria within a single exhaustive audit process."
        ),
        actions=[
            Action(
                name="GetArtifactIdFromName",
                kwargs={"artifact_name": "Design System"}
            ),
            Action(
                name="CreateAuditSession",
                kwargs={"artifact_id": "art_003", "audit_type": "COMBINED_DS_A11Y"}
            ),
            Action(
                name="IdentifyCustomGroupsAndMapToDsComponents",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="RecordDsAuditFindings",
                kwargs={"audit_id": "audit_013", "layer_id": "1:2", "layer_name": "Design System", "finding_type": "AMBIGUOUS", "recommended_component_id_nullable": "Design-v1.4", "severity": "HIGH"}
            ),
            Action(
                name="EvaluateAccessibility",
                kwargs={"artifact_id": "art_003"}
            ),
            Action(
                name="RecordAccessibilityAuditFindings",
                kwargs={"audit_id": "audit_013", "layer_id": "1:2", "layer_name": "Design System", "violation_type": "TOUCH_TARGET", "violation_details_json": {"current_size": "40x40px", "required_size": "44x44px", "description": "Touch target too small for mobile accessibility"}, "severity": "HIGH", "recommended_fix_summary": "Increase button size to minimum 44x44px for touch accessibility"}
            ),
            Action(
                name="GenerateAuditReport",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="UpdateAuditStatus",
                kwargs={"audit_id": "audit_013", "status": "COMPLETED"}
            ),
            Action(
                name="LinkAuditReportAsset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            )
        ],
        outputs=[{"audit_id": "audit_013", "finding_ds_id": "finding_ds_016", "finding_a11y_id": "finding_a11y_016", "report_asset_id": "asset_019"}]
    ),
    Task(
        annotator="0",
        user_id="task_073",
        instruction=(
            "You need to handle an extensive combined design system and accessibility audit on the Mobile App Dashboard artifact. This assessment will review both design system component mapping and accessibility adherence within a single, thorough audit process."
        ),
        actions=[
            Action(
                name="GetArtifactIdFromName",
                kwargs={"artifact_name": "Mobile App Dashboard"}
            ),
            Action(
                name="CreateAuditSession",
                kwargs={"artifact_id": "art_004", "audit_type": "COMBINED_DS_A11Y"}
            ),
            Action(
                name="IdentifyCustomGroupsAndMapToDsComponents",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="RecordDsAuditFindings",
                kwargs={"audit_id": "audit_013", "layer_id": "2:1", "layer_name": "Mobile App Dashboard", "finding_type": "SUBSTITUTE_RECOMMENDED", "recommended_component_id_nullable": "Mobile-v2.5", "severity": "HIGH"}
            ),
            Action(
                name="EvaluateAccessibility",
                kwargs={"artifact_id": "art_004"}
            ),
            Action(
                name="RecordAccessibilityAuditFindings",
                kwargs={"audit_id": "audit_013", "layer_id": "2:1", "layer_name": "Mobile App Dashboard", "violation_type": "CONTRAST", "violation_details_json": {"current_ratio": "2.1:1", "required_ratio": "4.5:1", "colors": {"foreground": "#777777", "background": "#ffffff"}}, "severity": "HIGH", "recommended_fix_summary": "Increase text color contrast to meet WCAG AA standards"}
            ),
            Action(
                name="GenerateAuditReport",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="UpdateAuditStatus",
                kwargs={"audit_id": "audit_013", "status": "COMPLETED"}
            ),
            Action(
                name="LinkAuditReportAsset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            )
        ],
        outputs=[{"audit_id": "audit_013", "finding_ds_id": "finding_ds_016", "finding_a11y_id": "finding_a11y_016", "report_asset_id": "asset_019"}]
    ),
    Task(
        annotator="0",
        user_id="task_074",
        instruction=(
            "You are overseeing a combined design system and accessibility audit using workflow 3c. You should coordinate a thorough audit of the 'User Profile Screen' artifact to detect design system mapping issues and accessibility violations. The audit must assess component alignment with the design system and verify adherence to accessibility standards, such as text sizing, touch targets, and contrast requirements."
        ),
        actions=[
            Action(
                name="GetArtifactIdFromName",
                kwargs={"artifact_name": "User Profile Screen"}
            ),
            Action(
                name="CreateAuditSession",
                kwargs={"artifact_id": "art_005", "audit_type": "COMBINED_DS_A11Y"}
            ),
            Action(
                name="IdentifyCustomGroupsAndMapToDsComponents",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="RecordDsAuditFindings",
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
                name="EvaluateAccessibility",
                kwargs={"artifact_id": "art_005"}
            ),
            Action(
                name="RecordAccessibilityAuditFindings",
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
                name="GenerateAuditReport",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="UpdateAuditStatus",
                kwargs={"audit_id": "audit_013", "status": "COMPLETED"}
            ),
            Action(
                name="LinkAuditReportAsset",
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
            "You are handling a combined design system and accessibility audit using workflow 3c. You intend to coordinate a thorough audit of the 'Marketing Website' artifact to detect both design system mapping issues and accessibility violations. The audit should assess component adherence to the design system and check for accessibility standards including RTL support, touch targets, and design component clarity."
        ),
        actions=[
            Action(
                name="GetArtifactIdFromName",
                kwargs={"artifact_name": "Marketing Website"}
            ),
            Action(
                name="CreateAuditSession",
                kwargs={"artifact_id": "art_006", "audit_type": "COMBINED_DS_A11Y"}
            ),
            Action(
                name="IdentifyCustomGroupsAndMapToDsComponents",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="RecordDsAuditFindings",
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
                name="EvaluateAccessibility",
                kwargs={"artifact_id": "art_006"}
            ),
            Action(
                name="RecordAccessibilityAuditFindings",
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
                name="GenerateAuditReport",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="UpdateAuditStatus",
                kwargs={"audit_id": "audit_013", "status": "COMPLETED"}
            ),
            Action(
                name="LinkAuditReportAsset",
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
            "You intend to conduct a combined design system and accessibility audit on the Pricing Page artifact. This comprehensive audit will examine both design system compliance and accessibility standards, pinpointing component mapping issues and accessibility violations that need attention."
        ),
        actions=[
            Action(
                name="GetArtifactIdFromName",
                kwargs={"artifact_name": "Pricing Page"}
            ),
            Action(
                name="CreateAuditSession",
                kwargs={"artifact_id": "art_007", "audit_type": "COMBINED_DS_A11Y"}
            ),
            Action(
                name="IdentifyCustomGroupsAndMapToDsComponents",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="RecordDsAuditFindings",
                kwargs={"audit_id": "audit_013", "layer_id": "3:2", "layer_name": "Pricing Page", "finding_type": "SUBSTITUTE_RECOMMENDED", "recommended_component_id_nullable": "Pricing-v1.8", "severity": "LOW"}
            ),
            Action(
                name="EvaluateAccessibility",
                kwargs={"artifact_id": "art_007"}
            ),
            Action(
                name="RecordAccessibilityAuditFindings",
                kwargs={"audit_id": "audit_013", "layer_id": "3:2", "layer_name": "Pricing Page", "violation_type": "TOUCH_TARGET", "violation_details_json": {"current_size": "32x32px", "required_size": "44x44px", "description": "Touch target too small for mobile accessibility"}, "severity": "HIGH", "recommended_fix_summary": "Increase button size to minimum 44x44px for touch accessibility"}
            ),
            Action(
                name="GenerateAuditReport",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="UpdateAuditStatus",
                kwargs={"audit_id": "audit_013", "status": "COMPLETED"}
            ),
            Action(
                name="LinkAuditReportAsset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            )
        ],
        outputs=[{"audit_id": "audit_013", "finding_ds_id": "finding_ds_016", "finding_a11y_id": "finding_a11y_016", "report_asset_id": "asset_019"}]
    ),
    Task(
        annotator="0",
        user_id="task_077",
        instruction=(
            "You intend to handle a combined design system and accessibility audit on the Admin Panel Header artifact. This thorough audit will evaluate both design system compliance and accessibility standards, pinpointing component mapping issues and accessibility violations that must be rectified."
        ),
        actions=[
            Action(
                name="GetArtifactIdFromName",
                kwargs={"artifact_name": "Admin Panel Header"}
            ),
            Action(
                name="CreateAuditSession",
                kwargs={"artifact_id": "art_008", "audit_type": "COMBINED_DS_A11Y"}
            ),
            Action(
                name="IdentifyCustomGroupsAndMapToDsComponents",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="RecordDsAuditFindings",
                kwargs={"audit_id": "audit_013", "layer_id": "4:1", "layer_name": "Admin Panel Header", "finding_type": "UNMAPPED", "recommended_component_id_nullable": "Admin-v2.9", "severity": "LOW"}
            ),
            Action(
                name="EvaluateAccessibility",
                kwargs={"artifact_id": "art_008"}
            ),
            Action(
                name="RecordAccessibilityAuditFindings",
                kwargs={"audit_id": "audit_013", "layer_id": "4:1", "layer_name": "Admin Panel Header", "violation_type": "CONTRAST", "violation_details_json": {"current_ratio": "2.8:1", "required_ratio": "4.5:1", "colors": {"foreground": "#666666", "background": "#ffffff"}}, "severity": "HIGH", "recommended_fix_summary": "Increase text color contrast to meet WCAG AA standards"}
            ),
            Action(
                name="GenerateAuditReport",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="UpdateAuditStatus",
                kwargs={"audit_id": "audit_013", "status": "COMPLETED"}
            ),
            Action(
                name="LinkAuditReportAsset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            )
        ],
        outputs=[{"audit_id": "audit_013", "finding_ds_id": "finding_ds_016", "finding_a11y_id": "finding_a11y_016", "report_asset_id": "asset_019"}]
    ),
    Task(
        annotator="0",
        user_id="task_078",
        instruction=(
            "You aim to coordinate a combined design system and accessibility audit on the Data Table Component artifact. This extensive audit will assess both design system compliance and accessibility standards, identifying component mapping issues and accessibility violations that require correction."
        ),
        actions=[
            Action(
                name="GetArtifactIdFromName",
                kwargs={"artifact_name": "Data Table Component"}
            ),
            Action(
                name="CreateAuditSession",
                kwargs={"artifact_id": "art_009", "audit_type": "COMBINED_DS_A11Y"}
            ),
            Action(
                name="IdentifyCustomGroupsAndMapToDsComponents",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="RecordDsAuditFindings",
                kwargs={"audit_id": "audit_013", "layer_id": "4:1", "layer_name": "Data Table Component", "finding_type": "AMBIGUOUS", "recommended_component_id_nullable": "Data-v1.0", "severity": "LOW"}
            ),
            Action(
                name="EvaluateAccessibility",
                kwargs={"artifact_id": "art_009"}
            ),
            Action(
                name="RecordAccessibilityAuditFindings",
                kwargs={"audit_id": "audit_013", "layer_id": "4:1", "layer_name": "Data Table Component", "violation_type": "TEXT_SIZING", "violation_details_json": {"current_size": "12px", "required_size": "16px", "description": "Text too small for readability"}, "severity": "HIGH", "recommended_fix_summary": "Increase font size to minimum 16px for better readability"}
            ),
            Action(
                name="GenerateAuditReport",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="UpdateAuditStatus",
                kwargs={"audit_id": "audit_013", "status": "COMPLETED"}
            ),
            Action(
                name="LinkAuditReportAsset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            )
        ],
        outputs=[{"audit_id": "audit_013", "finding_ds_id": "finding_ds_016", "finding_a11y_id": "finding_a11y_016", "report_asset_id": "asset_019"}]
    ),
    Task(
        annotator="0",
        user_id="task_079",
        instruction=(
            "Handle a joint design system and accessibility review on the Brand Guidelines artifact. This review will assess compliance with design system component mapping and accessibility standards to ensure a thorough quality evaluation."
        ),
        actions=[
            Action(
                name="GetArtifactIdFromName",
                kwargs={"artifact_name": "Brand Guidelines"}
            ),
            Action(
                name="CreateAuditSession",
                kwargs={"artifact_id": "art_010", "audit_type": "COMBINED_DS_A11Y"}
            ),
            Action(
                name="IdentifyCustomGroupsAndMapToDsComponents",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="RecordDsAuditFindings",
                kwargs={"audit_id": "audit_013", "layer_id": "5:1", "layer_name": "Brand Guidelines", "finding_type": "SUBSTITUTE_RECOMMENDED", "recommended_component_id_nullable": "Brand-v1.2", "severity": "LOW"}
            ),
            Action(
                name="EvaluateAccessibility",
                kwargs={"artifact_id": "art_010"}
            ),
            Action(
                name="RecordAccessibilityAuditFindings",
                kwargs={"audit_id": "audit_013", "layer_id": "5:1", "layer_name": "Brand Guidelines", "violation_type": "TOUCH_TARGET", "violation_details_json": {"current_size": "40x40px", "required_size": "44x44px", "description": "Touch target too small for mobile accessibility"}, "severity": "MEDIUM", "recommended_fix_summary": "Increase button size to minimum 44x44px for touch accessibility"}
            ),
            Action(
                name="GenerateAuditReport",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="UpdateAuditStatus",
                kwargs={"audit_id": "audit_013", "status": "COMPLETED"}
            ),
            Action(
                name="LinkAuditReportAsset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            )
        ],
        outputs=[{"audit_id": "audit_013", "finding_ds_id": "finding_ds_016", "finding_a11y_id": "finding_a11y_016", "report_asset_id": "asset_019"}]
    ),
    Task(
        annotator="0",
        user_id="task_080",
        instruction=(
            "Conduct a combined design system and accessibility review on the Contact Form Component artifact. This assessment will check both compliance with design system component mapping and adherence to accessibility standards for a comprehensive quality evaluation."
        ),
        actions=[
            Action(
                name="GetArtifactIdFromName",
                kwargs={"artifact_name": "Contact Form Component"}
            ),
            Action(
                name="CreateAuditSession",
                kwargs={"artifact_id": "art_011", "audit_type": "COMBINED_DS_A11Y"}
            ),
            Action(
                name="IdentifyCustomGroupsAndMapToDsComponents",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="RecordDsAuditFindings",
                kwargs={"audit_id": "audit_013", "layer_id": "1:2", "layer_name": "Contact Form Component", "finding_type": "UNMAPPED", "recommended_component_id_nullable": "Contact-v2.3", "severity": "LOW"}
            ),
            Action(
                name="EvaluateAccessibility",
                kwargs={"artifact_id": "art_011"}
            ),
            Action(
                name="RecordAccessibilityAuditFindings",
                kwargs={"audit_id": "audit_013", "layer_id": "1:2", "layer_name": "Contact Form Component", "violation_type": "CONTRAST", "violation_details_json": {"current_ratio": "2.1:1", "required_ratio": "4.5:1", "colors": {"foreground": "#666666", "background": "#ffffff"}}, "severity": "MEDIUM", "recommended_fix_summary": "Increase text color contrast to meet WCAG AA standards"}
            ),
            Action(
                name="GenerateAuditReport",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="UpdateAuditStatus",
                kwargs={"audit_id": "audit_013", "status": "COMPLETED"}
            ),
            Action(
                name="LinkAuditReportAsset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            )
        ],
        outputs=[{"audit_id": "audit_013", "finding_ds_id": "finding_ds_016", "finding_a11y_id": "finding_a11y_016", "report_asset_id": "asset_019"}]
    ),
    Task(
        annotator="0",
        user_id="task_081",
        instruction=(
            "Handle a joint design system and accessibility review for the Settings Screen. Your aim is to inspect both the design system component integration and accessibility adherence to verify that the artifact complies with standards. Detect any components not yet mapped and accessibility breaches to deliver a comprehensive audit summary."
        ),
        actions=[
            Action(
                name="GetArtifactIdFromName",
                kwargs={"artifact_name": "Settings Screen"}
            ),
            Action(
                name="CreateAuditSession",
                kwargs={"artifact_id": "art_012", "audit_type": "COMBINED_DS_A11Y"}
            ),
            Action(
                name="IdentifyCustomGroupsAndMapToDsComponents",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="RecordDsAuditFindings",
                kwargs={"audit_id": "audit_013", "layer_id": "2:1", "layer_name": "Settings Screen", "finding_type": "AMBIGUOUS", "recommended_component_id_nullable": "Settings-v1.4", "severity": "LOW"}
            ),
            Action(
                name="EvaluateAccessibility",
                kwargs={"artifact_id": "art_012"}
            ),
            Action(
                name="RecordAccessibilityAuditFindings",
                kwargs={"audit_id": "audit_013", "layer_id": "2:1", "layer_name": "Settings Screen", "violation_type": "TEXT_SIZING", "violation_details_json": {"current_size": "12px", "required_size": "16px", "description": "Text too small for readability"}, "severity": "MEDIUM", "recommended_fix_summary": "Increase font size to minimum 16px for better readability"}
            ),
            Action(
                name="GenerateAuditReport",
                kwargs={"audit_id": "audit_013"}
            ),
            Action(
                name="UpdateAuditStatus",
                kwargs={"audit_id": "audit_013", "status": "COMPLETED"}
            ),
            Action(
                name="LinkAuditReportAsset",
                kwargs={"audit_id": "audit_013", "report_asset_id": "asset_019"}
            )
        ],
        outputs=[{"audit_id": "audit_013", "finding_ds_id": "finding_ds_016", "finding_a11y_id": "finding_a11y_016", "report_asset_id": "asset_019"}]
    ),

    Task(
        annotator="0",
        user_id="task_082",
        instruction=(
            "Coordinate the execution of the fix plan and transition workflow for finalized accessibility audits. Load the results from audit 'audit_001' and manage the remediation with 'designer@company.com' as the responsible party. The notification to stakeholders must involve 'manager@company.com' and 'ux-lead@company.com'."
        ),
        actions=[
            Action(
                name="LoadAuditFindings",
                kwargs={"audit_id": "audit_001"}
            ),
            Action(
                name="PrioritizeAuditFindings",
                kwargs={"finding_ids_list": ["finding_a11y_005", "finding_a11y_009"]}
            ),
            Action(
                name="CreateFixPlan",
                kwargs={"audit_id": "audit_001", "owner_email": "designer@company.com"}
            ),
            Action(
                name="CreateFixItem",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_a11y_005"}
            ),
            Action(
                name="CreateFixItem",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_a11y_009"}
            ),
            Action(
                name="CreateAndDeliverFixPlan",
                kwargs={"plan_id": "plan_013"}
            ),
            Action(
                name="NotifyStakeholders",
                kwargs={"plan_id": "plan_013", "stakeholder_emails": ["manager@company.com", "ux-lead@company.com"], "audit_id": "audit_001", "status": "DRAFTED", "owner_email": "designer@company.com"}
            )
        ],
        outputs=[{"plan_id": "plan_013", "item_id_1": "item_021", "item_id_2": "item_022", "asset_id": "asset_019", "thread_id": "thread_015", "message_id": "msg_017"}]
    ),

    Task(
        annotator="0",
        user_id="task_083",
        instruction=(
            "Handle the fix plan and handoff workflow for design system and accessibility findings 'finding_ds_010' and 'finding_a11y_007' from audit 'audit_005'. Collaborate with 'lead-designer@company.com' who is the owner and inform 'product-manager@company.com' and 'design-lead@company.com' as stakeholders."
        ),
        actions=[
            Action(
                name="LoadAuditFindings",
                kwargs={"audit_id": "audit_005"}
            ),
            Action(
                name="PrioritizeAuditFindings",
                kwargs={"finding_ids_list": ["finding_ds_010", "finding_a11y_007"]}
            ),
            Action(
                name="CreateFixPlan",
                kwargs={"audit_id": "audit_005", "owner_email": "lead-designer@company.com"}
            ),
            Action(
                name="CreateFixItem",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_ds_010"}
            ),
            Action(
                name="CreateFixItem",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_a11y_007"}
            ),
            Action(
                name="CreateAndDeliverFixPlan",
                kwargs={"plan_id": "plan_013"}
            ),
            Action(
                name="NotifyStakeholders",
                kwargs={"plan_id": "plan_013", "stakeholder_emails": ["product-manager@company.com", "design-lead@company.com"], "audit_id": "audit_005", "status": "DRAFTED", "owner_email": "lead-designer@company.com"}
            )
        ],
        outputs=[{"plan_id": "plan_013", "item_id_1": "item_021", "item_id_2": "item_022", "comment_id": "comment_019", "thread_id": "thread_015", "message_id": "msg_017"}]
    ),
    Task(
        annotator="0",
        user_id="task_084",
        instruction=(
            "Carry out the fix plan and handoff workflow for design system findings 'finding_ds_001' and 'finding_ds_002' from audit 'audit_003'. Work with 'senior-designer@company.com' as the owner and keep 'qa-lead@company.com' and 'dev-team@company.com' in the loop as stakeholders."
        ),
        actions=[
            Action(
                name="LoadAuditFindings",
                kwargs={"audit_id": "audit_003"}
            ),
            Action(
                name="PrioritizeAuditFindings",
                kwargs={"finding_ids_list": ["finding_ds_001", "finding_ds_002"]}
            ),
            Action(
                name="CreateFixPlan",
                kwargs={"audit_id": "audit_003", "owner_email": "senior-designer@company.com"}
            ),
            Action(
                name="CreateFixItem",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_ds_001"}
            ),
            Action(
                name="CreateFixItem",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_ds_002"}
            ),
            Action(
                name="CreateAndDeliverFixPlan",
                kwargs={"plan_id": "plan_013"}
            ),
            Action(
                name="NotifyStakeholders",
                kwargs={"plan_id": "plan_013", "stakeholder_emails": ["qa-lead@company.com", "dev-team@company.com"], "audit_id": "audit_003", "status": "DRAFTED", "owner_email": "senior-designer@company.com"}
            )
        ],
        outputs=[{"plan_id": "plan_013", "item_id_1": "item_021", "item_id_2": "item_022", "asset_id": "asset_019", "thread_id": "thread_015", "message_id": "msg_017"}]
    ),
    Task(
        annotator="0",
        user_id="task_085",
        instruction=(
            "Handle the fix plan and transfer workflow for accessibility findings 'finding_a11y_003' and 'finding_a11y_007' from audit 'audit_004'. Coordinate with 'accessibility-lead@company.com' as the owner and notify 'ux-team@company.com' and 'compliance-officer@company.com' as stakeholders."
        ),
        actions=[
            Action(
                name="LoadAuditFindings",
                kwargs={"audit_id": "audit_004"}
            ),
            Action(
                name="PrioritizeAuditFindings",
                kwargs={"finding_ids_list": ["finding_a11y_003", "finding_a11y_007"]}
            ),
            Action(
                name="CreateFixPlan",
                kwargs={"audit_id": "audit_004", "owner_email": "accessibility-lead@company.com"}
            ),
            Action(
                name="CreateFixItem",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_a11y_003"}
            ),
            Action(
                name="CreateFixItem",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_a11y_007"}
            ),
            Action(
                name="CreateAndDeliverFixPlan",
                kwargs={"plan_id": "plan_013"}
            ),
            Action(
                name="NotifyStakeholders",
                kwargs={"plan_id": "plan_013", "stakeholder_emails": ["ux-team@company.com", "compliance-officer@company.com"], "audit_id": "audit_004", "status": "DRAFTED", "owner_email": "accessibility-lead@company.com"}
            )
        ],
        outputs=[{"plan_id": "plan_013", "item_id_1": "item_021", "item_id_2": "item_022", "ticket_id": "JIRA-9215", "thread_id": "thread_015", "message_id": "msg_017"}]
    ),
    Task(
        annotator="0",
        user_id="task_086",
        instruction=(
            "Manage the fix plan and transition workflow for accessibility findings 'finding_a11y_005' and 'finding_a11y_009' from audit 'audit_001'. Coordinate with 'ux-designer@company.com' as the owner and notify 'design-system@company.com' and 'product-owner@company.com' as stakeholders."
        ),
        actions=[
            Action(
                name="LoadAuditFindings",
                kwargs={"audit_id": "audit_001"}
            ),
            Action(
                name="PrioritizeAuditFindings",
                kwargs={"finding_ids_list": ["finding_a11y_005", "finding_a11y_009"]}
            ),
            Action(
                name="CreateFixPlan",
                kwargs={"audit_id": "audit_001", "owner_email": "ux-designer@company.com"}
            ),
            Action(
                name="CreateFixItem",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_a11y_005"}
            ),
            Action(
                name="CreateFixItem",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_a11y_009"}
            ),
            Action(
                name="CreateAndDeliverFixPlan",
                kwargs={"plan_id": "plan_013"}
            ),
            Action(
                name="NotifyStakeholders",
                kwargs={"plan_id": "plan_013", "stakeholder_emails": ["design-system@company.com", "product-owner@company.com"], "audit_id": "audit_001", "status": "DRAFTED", "owner_email": "ux-designer@company.com"}
            )
        ],
        outputs=[{"plan_id": "plan_013", "item_id_1": "item_021", "item_id_2": "item_022", "ticket_id": "JIRA-9215", "thread_id": "thread_015", "message_id": "msg_017"}]
    ),
    Task(
        annotator="0",
        user_id="task_087",
        instruction=(
            "Handle the development and delivery of a detailed fix plan for the accessibility violations highlighted in a touch target accessibility audit. Your assignment consists of reviewing the findings from audit_002, identifying and prioritizing the high-severity touch target issues, and formulating a comprehensive remediation plan. Emphasize resolving the critical admin header button touch target issue and the search input touch target problem. Construct fix items for these two findings, provide the plan through Figma comments, and inform ui-team@company.com and accessibility-expert@company.com of its completion. The plan is to be managed by frontend-dev@company.com and stakeholders must be apprised that the plan is in the draft stage."
        ),
        actions=[
            Action(
                name="LoadAuditFindings",
                kwargs={"audit_id": "audit_002"}
            ),
            Action(
                name="PrioritizeAuditFindings",
                kwargs={"finding_ids_list": ["finding_a11y_001", "finding_a11y_006"]}
            ),
            Action(
                name="CreateFixPlan",
                kwargs={"audit_id": "audit_002", "owner_email": "frontend-dev@company.com"}
            ),
            Action(
                name="CreateFixItem",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_a11y_001"}
            ),
            Action(
                name="CreateFixItem",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_a11y_006"}
            ),
            Action(
                name="CreateAndDeliverFixPlan",
                kwargs={"plan_id": "plan_013"}
            ),
            Action(
                name="NotifyStakeholders",
                kwargs={"plan_id": "plan_013", "stakeholder_emails": ["ui-team@company.com", "accessibility-expert@company.com"], "audit_id": "audit_002", "status": "DRAFTED", "owner_email": "frontend-dev@company.com"}
            )
        ],
        outputs=[{"plan_id": "plan_013", "item_id_1": "item_021", "item_id_2": "item_022", "comment_id": "comment_019", "thread_id": "thread_015", "message_id": "msg_017"}]
    ),
    Task(
        annotator="0",
        user_id="task_088",
        instruction=(
            "Coordinate the creation and submission of a fix plan addressing design system mapping issues identified in a component audit. Your role requires examining audit findings for audit_006, prioritizing design system infractions, and drafting a remediation strategy. Concentrate on the data table header substitute recommendation and the pagination controls unmapped component issues. Develop fix items for these findings, submit the plan in a PDF document, and update design-system@company.com and component-library@company.com regarding the plan. The plan is to be managed by component-dev@company.com with stakeholders being notified of the draft status."
        ),
        actions=[
            Action(
                name="LoadAuditFindings",
                kwargs={"audit_id": "audit_006"}
            ),
            Action(
                name="PrioritizeAuditFindings",
                kwargs={"finding_ids_list": ["finding_ds_003", "finding_ds_007"]}
            ),
            Action(
                name="CreateFixPlan",
                kwargs={"audit_id": "audit_006", "owner_email": "component-dev@company.com"}
            ),
            Action(
                name="CreateFixItem",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_ds_003"}
            ),
            Action(
                name="CreateFixItem",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_ds_007"}
            ),
            Action(
                name="CreateAndDeliverFixPlan",
                kwargs={"plan_id": "plan_013"}
            ),
            Action(
                name="NotifyStakeholders",
                kwargs={"plan_id": "plan_013", "stakeholder_emails": ["design-system@company.com", "component-library@company.com"], "audit_id": "audit_006", "status": "DRAFTED", "owner_email": "component-dev@company.com"}
            )
        ],
        outputs=[{"plan_id": "plan_013", "item_id_1": "item_021", "item_id_2": "item_022", "asset_id": "asset_019", "thread_id": "thread_015", "message_id": "msg_017"}]
    ),
    Task(
        annotator="0",
        user_id="task_089",
        instruction=(
            "Handle the creation and delivery of a corrective plan for internationalization accessibility problems identified in an RTL and text sizing audit. This task requires loading the audit findings from audit_007, with a focus on prioritizing the compliance of RTL in the navigation menu and addressing footer link text sizing issues. Establish fix entries for both areas of concern, provide the plan in PDF format, and inform i18n-team@company.com and accessibility-qa@company.com of the plan. Ensure internationalization-dev@company.com is the owner of the plan and update stakeholders about the drafted status."
        ),
        actions=[
            Action(
                name="LoadAuditFindings",
                kwargs={"audit_id": "audit_007"}
            ),
            Action(
                name="PrioritizeAuditFindings",
                kwargs={"finding_ids_list": ["finding_a11y_004", "finding_a11y_008"]}
            ),
            Action(
                name="CreateFixPlan",
                kwargs={"audit_id": "audit_007", "owner_email": "internationalization-dev@company.com"}
            ),
            Action(
                name="CreateFixItem",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_a11y_004"}
            ),
            Action(
                name="CreateFixItem",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_a11y_008"}
            ),
            Action(
                name="CreateAndDeliverFixPlan",
                kwargs={"plan_id": "plan_013"}
            ),
            Action(
                name="NotifyStakeholders",
                kwargs={"plan_id": "plan_013", "stakeholder_emails": ["i18n-team@company.com", "accessibility-qa@company.com"], "audit_id": "audit_007", "status": "DRAFTED", "owner_email": "internationalization-dev@company.com"}
            )
        ],
        outputs=[{"plan_id": "plan_013", "item_id_1": "item_021", "item_id_2": "item_022", "asset_id": "asset_019", "thread_id": "thread_015", "message_id": "msg_017"}]
    ),
    Task(
        annotator="0",
        user_id="task_090",
        instruction=(
            "Coordinate the creation and submission of a corrective strategy for design system component mapping issues detected in a profile and form interface audit. This involves accessing audit findings from audit_008, prioritizing the unresolved profile avatar component and unclear form input mapping issues. Develop resolution items for both findings, submit the strategy through comments in Figma, and alert ds-governance@company.com and product-design@company.com about the plan. Ensure platform-team@company.com assumes ownership of the plan and notify stakeholders about its drafted status."
        ),
        actions=[
            Action(
                name="LoadAuditFindings",
                kwargs={"audit_id": "audit_008"}
            ),
            Action(
                name="PrioritizeAuditFindings",
                kwargs={"finding_ids_list": ["finding_ds_004", "finding_ds_008"]}
            ),
            Action(
                name="CreateFixPlan",
                kwargs={"audit_id": "audit_008", "owner_email": "platform-team@company.com"}
            ),
            Action(
                name="CreateFixItem",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_ds_004"}
            ),
            Action(
                name="CreateFixItem",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_ds_008"}
            ),
            Action(
                name="CreateAndDeliverFixPlan",
                kwargs={"plan_id": "plan_013"}
            ),
            Action(
                name="NotifyStakeholders",
                kwargs={"plan_id": "plan_013", "stakeholder_emails": ["ds-governance@company.com", "product-design@company.com"], "audit_id": "audit_008", "status": "DRAFTED", "owner_email": "platform-team@company.com"}
            )
        ],
        outputs=[{"plan_id": "plan_013", "item_id_1": "item_021", "item_id_2": "item_022", "comment_id": "comment_019", "thread_id": "thread_015", "message_id": "msg_017"}]
    ),
    Task(
        annotator="0",
        user_id="task_091",
        instruction=(
            "Handle the issues of brand consistency and design system compliance highlighted in audit_010. Your task involves loading the audit findings, assessing their impact on brand integrity to prioritize them, and developing a thorough fix plan. Give precedence to the Brand Logo ambiguous mapping (finding_ds_005) and Typography Heading substitution recommendation (finding_ds_009). Aim to formulate a fix plan managed by brand-team@company.com and produce fix items for both findings to guarantee accurate brand representation. Your plan ought to entail delivering the fixes through tickets and informing vital stakeholders including brand-guidelines@company.com and marketing-design@company.com. Ensure the output delivers the plan ID, specific fix item IDs, ticket details, and verification of stakeholder notifications."
        ),
        actions=[
            Action(
                name="LoadAuditFindings",
                kwargs={"audit_id": "audit_010"}
            ),
            Action(
                name="PrioritizeAuditFindings",
                kwargs={"finding_ids_list": ["finding_ds_005", "finding_ds_009"]}
            ),
            Action(
                name="CreateFixPlan",
                kwargs={"audit_id": "audit_010", "owner_email": "brand-team@company.com"}
            ),
            Action(
                name="CreateFixItem",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_ds_005"}
            ),
            Action(
                name="CreateFixItem",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_ds_009"}
            ),
            Action(
                name="CreateAndDeliverFixPlan",
                kwargs={"plan_id": "plan_013"}
            ),
            Action(
                name="NotifyStakeholders",
                kwargs={"plan_id": "plan_013", "stakeholder_emails": ["brand-guidelines@company.com", "marketing-design@company.com"], "audit_id": "audit_010", "status": "DRAFTED", "owner_email": "brand-team@company.com"}
            )
        ],
        outputs=[{"plan_id": "plan_013", "item_id_1": "item_021", "item_id_2": "item_022", "ticket_id": "JIRA-9215", "thread_id": "thread_015", "message_id": "msg_017"}]
    ),
    Task(
        annotator="0",
        user_id="task_092",
        instruction=(
            "Address the design issues of the contact form identified in audit_011 by creating a fix plan. Your role is to load the audit findings, prioritize the Contact Form Input unmapped component (finding_ds_011) and Submit Button touch target issue (finding_a11y_012). Develop a fix plan in the ownership of form-team@company.com and initiate fix items for these high-priority findings. Your strategy should involve executing fixes through tickets and notifying crucial stakeholders such as contact-form-dev@company.com and ui-accessibility@company.com."
        ),
        actions=[
            Action(
                name="LoadAuditFindings",
                kwargs={"audit_id": "audit_011"}
            ),
            Action(
                name="PrioritizeAuditFindings",
                kwargs={"finding_ids_list": ["finding_ds_011", "finding_a11y_012"]}
            ),
            Action(
                name="CreateFixPlan",
                kwargs={"audit_id": "audit_011", "owner_email": "form-team@company.com"}
            ),
            Action(
                name="CreateFixItem",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_ds_011"}
            ),
            Action(
                name="CreateFixItem",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_a11y_012"}
            ),
            Action(
                name="CreateAndDeliverFixPlan",
                kwargs={"plan_id": "plan_013"}
            ),
            Action(
                name="NotifyStakeholders",
                kwargs={"plan_id": "plan_013", "stakeholder_emails": ["contact-form-dev@company.com", "ui-accessibility@company.com"], "audit_id": "audit_011", "status": "DRAFTED", "owner_email": "form-team@company.com"}
            )
        ],
        outputs=[{"plan_id": "plan_013", "item_id_1": "item_021", "item_id_2": "item_022", "ticket_id": "JIRA-9215", "thread_id": "thread_015", "message_id": "msg_017"}]
    ),
    Task(
        annotator="0",
        user_id="task_093",
        instruction=(
            "Handle Workflow 4 - Fix Plan & Handoff to transform audit findings into actionable remediation steps. Process audit_011 which involves contact form design issues, with designer@company.com as the owner. Concentrate on the development of fix items for the top two priority findings and deliver the plan marked with DELIVERED status to reviewer@company.com for implementation tracking."
        ),
        actions=[
            Action(
                name="LoadAuditFindings",
                kwargs={"audit_id": "audit_011"}
            ),
            Action(
                name="PrioritizeAuditFindings",
                kwargs={"finding_ids_list": ["finding_ds_011", "finding_ds_012", "finding_ds_013", "finding_a11y_011", "finding_a11y_012", "finding_a11y_013"]}
            ),
            Action(
                name="CreateFixPlan",
                kwargs={"audit_id": "audit_011", "owner_email": "designer@company.com"}
            ),
            Action(
                name="CreateFixItem",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_ds_011"}
            ),
            Action(
                name="CreateFixItem",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_a11y_011"}
            ),
            Action(
                name="CreateAndDeliverFixPlan",
                kwargs={"plan_id": "plan_013"}
            ),
            Action(
                name="NotifyStakeholders",
                kwargs={"plan_id": "plan_013", "stakeholder_emails": ["reviewer@company.com"], "audit_id": "audit_011", "status": "DELIVERED", "owner_email": "designer@company.com"}
            )
        ],
        outputs=[{"plan_id": "plan_013", "item_ids": ["item_021", "item_022"], "asset_id": "asset_019", "thread_id": "thread_015", "message_id": "msg_017"}]
    ),
    Task(
        annotator="0",
        user_id="task_094",
        instruction=(
            "Coordinate Workflow 4 - Fix Plan & Handoff to transform audit findings into actionable remediation steps. Address audit_012 which encompasses settings interface design issues, with ux-lead@company.com as the owner. Focus on crafting fix items for the top two priority findings and submit the plan with DELIVERED status to product-manager@company.com for monitoring implementation."
        ),
        actions=[
            Action(
                name="LoadAuditFindings",
                kwargs={"audit_id": "audit_012"}
            ),
            Action(
                name="PrioritizeAuditFindings",
                kwargs={"finding_ids_list": ["finding_ds_014", "finding_ds_015", "finding_a11y_014", "finding_a11y_015"]}
            ),
            Action(
                name="CreateFixPlan",
                kwargs={"audit_id": "audit_012", "owner_email": "ux-lead@company.com"}
            ),
            Action(
                name="CreateFixItem",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_ds_014"}
            ),
            Action(
                name="CreateFixItem",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_a11y_014"}
            ),
            Action(
                name="CreateAndDeliverFixPlan",
                kwargs={"plan_id": "plan_013"}
            ),
            Action(
                name="NotifyStakeholders",
                kwargs={"plan_id": "plan_013", "stakeholder_emails": ["product-manager@company.com"], "audit_id": "audit_012", "status": "DELIVERED", "owner_email": "ux-lead@company.com"}
            )
        ],
        outputs=[{"plan_id": "plan_013", "item_ids": ["item_021", "item_022"], "asset_id": "asset_019", "thread_id": "thread_015", "message_id": "msg_017"}]
    ),
    Task(
        annotator="0",
        user_id="task_095",
        instruction=(
            "Handle the implementation of Workflow 4 - Fix Plan & Handoff to transform audit findings into practical remediation measures. Process audit_010, which pertains to issues in the brand and typography design system, with brand-manager@company.com designated as the owner. Emphasize the creation of multiple fix items for each finding and provide the plan marked as DELIVERED to design-team@company.com for tracking the implementation."
        ),
        actions=[
            Action(
                name="LoadAuditFindings",
                kwargs={"audit_id": "audit_010"}
            ),
            Action(
                name="PrioritizeAuditFindings",
                kwargs={"finding_ids_list": ["finding_ds_005", "finding_ds_009"]}
            ),
            Action(
                name="CreateFixPlan",
                kwargs={"audit_id": "audit_010", "owner_email": "brand-manager@company.com"}
            ),
            Action(
                name="CreateFixItem",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_ds_005"}
            ),
            Action(
                name="CreateFixItem",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_ds_009"}
            ),
            # Action(
            #     name="CreateFixItem",
            #     kwargs={"plan_id": "plan_013", "finding_id": "finding_ds_005"}
            # ),
            Action(
                name="CreateAndDeliverFixPlan",
                kwargs={"plan_id": "plan_013"}
            ),
            Action(
                name="NotifyStakeholders",
                kwargs={"plan_id": "plan_013", "stakeholder_emails": ["design-team@company.com"], "audit_id": "audit_010", "status": "DELIVERED", "owner_email": "brand-manager@company.com"}
            )
        ],
        outputs=[{"plan_id": "plan_013", "item_ids": ["item_021", "item_022"], "ticket_id": "JIRA-9215", "thread_id": "thread_015", "message_id": "msg_017"}]
    ),
    Task(
        annotator="0",
        user_id="task_096",
        instruction=(
            "Coordinate the implementation of Workflow 4 Fix Plan & Handoff for audit_007 with accessibility.lead@company.com appointed as the owner. Aim to convert accessibility audit findings into practical remediation measures and inform stakeholders (accessibility.lead@othercompany.com) with the status set to DELIVERED."
        ),
        actions=[
            Action(
                name="LoadAuditFindings",
                kwargs={"audit_id": "audit_007"}
            ),
            Action(
                name="PrioritizeAuditFindings",
                kwargs={"finding_ids_list": ["finding_a11y_004", "finding_a11y_008"]}
            ),
            Action(
                name="CreateFixPlan",
                kwargs={"audit_id": "audit_007", "owner_email": "accessibility.lead@company.com"}
            ),
            Action(
                name="CreateFixItem",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_a11y_004"}
            ),
            Action(
                name="CreateFixItem",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_a11y_008"}
            ),
            # Action(
            #     name="CreateFixItem",
            #     kwargs={"plan_id": "plan_013", "finding_id": "finding_a11y_004"}
            # ),
            Action(
                name="CreateAndDeliverFixPlan",
                kwargs={"plan_id": "plan_013"}
            ),
            Action(
                name="NotifyStakeholders",
                kwargs={"plan_id": "plan_013", "stakeholder_emails": ["accessibility.lead@othercompany.com"], "audit_id": "audit_007", "status": "DELIVERED", "owner_email": "accessibility.lead@company.com"}
            )
        ],
        outputs=[{"plan_id": "plan_013", "item_ids": ["item_021", "item_022"], "ticket_id": "JIRA-9215", "thread_id": "thread_015", "message_id": "msg_017"}]
    ),
    Task(
        annotator="0",
        user_id="task_097",
        instruction=(
            "Handle the execution of Workflow 4 Fix Plan & Handoff for audit_004, designating ux.engineer@company.com as the owner. Transform accessibility audit findings into practical remediation steps and inform stakeholders (ux.engineer@othercompany.com) with the status set to DELIVERED."
        ),
        actions=[
            Action(
                name="LoadAuditFindings",
                kwargs={"audit_id": "audit_004"}
            ),
            Action(
                name="PrioritizeAuditFindings",
                kwargs={"finding_ids_list": ["finding_a11y_003", "finding_a11y_007"]}
            ),
            Action(
                name="CreateFixPlan",
                kwargs={"audit_id": "audit_004", "owner_email": "ux.engineer@company.com"}
            ),
            Action(
                name="CreateFixItem",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_a11y_003"}
            ),
            Action(
                name="CreateFixItem",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_a11y_007"}
            ),
            # Action(
            #     name="CreateFixItem",
            #     kwargs={"plan_id": "plan_013", "finding_id": "finding_a11y_003"}
            # ),
            Action(
                name="CreateAndDeliverFixPlan",
                kwargs={"plan_id": "plan_013"}
            ),
            Action(
                name="NotifyStakeholders",
                kwargs={"plan_id": "plan_013", "stakeholder_emails": ["ux.engineer@othercompany.com"], "audit_id": "audit_004", "status": "DELIVERED", "owner_email": "ux.engineer@company.com"}
            )
        ],
        outputs=[{"plan_id": "plan_013", "item_ids": ["item_021", "item_022"], "comment_id": "comment_019", "thread_id": "thread_015", "message_id": "msg_017"}]
    ),
    Task(
        annotator="0",
        user_id="task_098",
        instruction=(
            "Coordinate the implementation of Workflow 4 Fix Plan & Handoff for audit_010, appointing design.lead@company.com as the owner. Adapt design system mapping audit findings into practical remediation steps and communicate with stakeholders (design.lead@company.com) ensuring the status is DELIVERED."
        ),
        actions=[
            Action(
                name="LoadAuditFindings",
                kwargs={"audit_id": "audit_010"}
            ),
            Action(
                name="PrioritizeAuditFindings",
                kwargs={"finding_ids_list": ["finding_ds_005", "finding_ds_009"]}
            ),
            Action(
                name="CreateFixPlan",
                kwargs={"audit_id": "audit_010", "owner_email": "design.lead@company.com"}
            ),
            Action(
                name="CreateFixItem",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_ds_005"}
            ),
            Action(
                name="CreateFixItem",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_ds_009"}
            ),
            # Action(
            #     name="CreateFixItem",
            #     kwargs={"plan_id": "plan_013", "finding_id": "finding_ds_005"}
            # ),
            Action(
                name="CreateAndDeliverFixPlan",
                kwargs={"plan_id": "plan_013"}
            ),
            Action(
                name="NotifyStakeholders",
                kwargs={"plan_id": "plan_013", "stakeholder_emails": ["design.lead@company.com"], "audit_id": "audit_010", "status": "DELIVERED", "owner_email": "design.lead@company.com"}
            )
        ],
        outputs=[{"plan_id": "plan_013", "item_ids": ["item_021", "item_022"], "comment_id": "comment_019", "thread_id": "thread_015", "message_id": "msg_017"}]
    ),
    Task(
        annotator="0",
        user_id="task_099",
        instruction=(
            "Carry out Workflow 4 Fix Plan & Handoff for audit_003 with senior.dev@company.com as the designated owner. Convert design system mapping audit findings into actionable remediation steps and inform stakeholders (senior.dev@othercompany.com) with a DELIVERED status."
        ),
        actions=[
            Action(
                name="LoadAuditFindings",
                kwargs={"audit_id": "audit_003"}
            ),
            Action(
                name="PrioritizeAuditFindings",
                kwargs={"finding_ids_list": ["finding_ds_001", "finding_ds_002", "finding_ds_006", "finding_ds_010"]}
            ),
            Action(
                name="CreateFixPlan",
                kwargs={"audit_id": "audit_003", "owner_email": "senior.dev@company.com"}
            ),
            Action(
                name="CreateFixItem",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_ds_001"}
            ),
            Action(
                name="CreateFixItem",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_ds_002"}
            ),
            Action(
                name="CreateFixItem",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_ds_006"}
            ),
            Action(
                name="CreateFixItem",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_ds_010"}
            ),
            Action(
                name="CreateAndDeliverFixPlan",
                kwargs={"plan_id": "plan_013"}
            ),
            Action(
                name="NotifyStakeholders",
                kwargs={"plan_id": "plan_013", "stakeholder_emails": ["senior.dev@othercompany.com"], "audit_id": "audit_003", "status": "DELIVERED", "owner_email": "senior.dev@company.com"}
            )
        ],
        outputs=[{"plan_id": "plan_013", "item_ids": ["item_021", "item_022", "item_023", "item_024"], "ticket_id": "JIRA-9215", "thread_id": "thread_015", "message_id": "msg_017"}]
    ),
    Task(
        annotator="0",
        user_id="task_100",
        instruction=(
            "Carry out Workflow 4 Fix Plan & Handoff for audit_002 with ui.accessibility@company.com as the designated owner. Convert accessibility audit findings into actionable remediation steps and inform stakeholders with a DELIVERED status."
        ),
        actions=[
            Action(
                name="LoadAuditFindings",
                kwargs={"audit_id": "audit_002"}
            ),
            Action(
                name="PrioritizeAuditFindings",
                kwargs={"finding_ids_list": ["finding_a11y_001", "finding_a11y_002", "finding_a11y_006", "finding_a11y_010"]}
            ),
            Action(
                name="CreateFixPlan",
                kwargs={"audit_id": "audit_002", "owner_email": "ui.accessibility@company.com"}
            ),
            Action(
                name="CreateFixItem",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_a11y_001"}
            ),
            Action(
                name="CreateFixItem",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_a11y_002"}
            ),
            Action(
                name="CreateFixItem",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_a11y_006"}
            ),
            Action(
                name="CreateFixItem",
                kwargs={"plan_id": "plan_013", "finding_id": "finding_a11y_010"}
            ),
            Action(
                name="CreateAndDeliverFixPlan",
                kwargs={"plan_id": "plan_013"}
            ),
            Action(
                name="NotifyStakeholders",
                kwargs={"plan_id": "plan_013", "stakeholder_emails": ["ui.accessibility@company.com"], "audit_id": "audit_002", "status": "DELIVERED", "owner_email": "ui.accessibility@company.com"}
            )
        ],
        outputs=[{"plan_id": "plan_013", "item_ids": ["item_021", "item_022", "item_023", "item_024"], "comment_id": "comment_019", "thread_id": "thread_015", "message_id": "msg_017"}]
    ),


]
