from domains.dto import Task, Action

TASKS = [
    Task(
        annotator="0",
        user_id="new_manuscript_onboarding_and_project_creation",
        instruction="""Execute editorial assistance to onboard the new manuscript 'Advanced Federated Learning Protocols' by Dr. Anna Petrov. Register the article (art_f1a2) with the topic 'AI' and the abstract: 'This paper details new, secure protocols for federated learning across distributed devices.' and create a submission record for it. To track this research, create a new project titled 'Federated Learning Protocols Research' led by Dr. Khan (res_06) and link 'art_f1a2'. Display the final project details for confirmation.""",
        actions=[
            Action(name="FetchUsers", kwargs={"name": "Dr. Anna Petrov"}),
            Action(name="RegisterNewArticle", kwargs={"title": "Advanced Federated Learning Protocols", "authors": ["Dr. Anna Petrov"], "topic": "AI", "abstract": "This paper details new, secure protocols for federated learning across distributed devices.", "article_id_override": "art_f1a2"}), # 'abstract' e 'topic' agora são especificados na instrução.
            Action(name="CreateReviewSubmission", kwargs={"article_id": "art_f1a2", "author_user_id": "res_06"}),
            Action(name="CreateNewProject", kwargs={"project_name": "Federated Learning Protocols Research", "lead_researcher_id": "res_06", "linked_article_ids": ["art_f1a2"]}),
            Action(name="FetchArticles", kwargs={"title": "Advanced Federated Learning Protocols"}),
            Action(name="FetchSubmissionInfo", kwargs={"article_id": "art_f1a2"}),
            Action(name="FetchUsers", kwargs={"user_id": "res_06"}),
        ],
        outputs=[
            '"project_name": "Federated Learning Protocols Research"',
            '"lead_researcher_id": "res_06"',
            '"linked_articles": ["art_f1a2"]'
        ]
    ),
    Task(
        annotator="0",
        user_id="processing_minor_revisions_request",
        instruction="""Conduct editorial management to process the 'minor_revisions' recommendation for the submission of 'Limits of Quantum Computing...' (art_02 / sub_01). Update the submission's status to 'revisions_requested'. Dispatch an alert to the author, Prof. James Wilson (res_03), with the exact message: 'Your submission for 'Limits of Quantum Computing...' requires minor revisions before acceptance. Please see the reviewer comments.'. After a simulated revision period, update 'art_02's abstract to: 'This paper presents a revised analysis on the practical limits of quantum computing for optimization problems, with new data on qubit decoherence.'. Finally, set the submission's outcome to 'accepted'. Display the final submission details.""",
        actions=[
            Action(name="FetchSubmissionInfo", kwargs={"article_id": "art_02"}),
            Action(name="ListReviewsForSubmission", kwargs={"submission_id": "sub_01"}),
            Action(name="SetSubmissionOutcome", kwargs={"submission_id": "sub_01", "new_status": "revisions_requested"}),
            Action(name="FetchUsers", kwargs={"user_id": "res_03"}),
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_03", "message": "Your submission for 'Limits of Quantum Computing...' requires minor revisions before acceptance. Please see the reviewer comments."}),
            Action(name="ReviseArticleDetails", kwargs={"article_id": "art_02", "abstract": "This paper presents a revised analysis on the practical limits of quantum computing for optimization problems, with new data on qubit decoherence."}),
            Action(name="SetSubmissionOutcome", kwargs={"submission_id": "sub_01", "new_status": "accepted"}),
            Action(name="FetchSubmissionInfo", kwargs={"submission_id": "sub_01"})
        ],
        outputs=[
            '"submission_id": "sub_01"',
            '"status": "accepted"'
        ]
    ),
    Task(
        annotator="0",
        user_id="end_to_end_peer_review_validation",
        instruction="""Handle new editorial management by configuring your workflow to receive 'email' notifications. Then, process the submission for 'New Biomarkers for Early Detection...' (art_04 / sub_02). Identify and assign an expert reviewer (Dr. Sarah Johnson - res_02), excluding the author (Dr. Thomas Anderson - res_04). After a simulated review, post an 'accept' recommendation with the comment: 'This is a high-impact study with a solid methodology. I recommend it for publication.'. Set the submission's final outcome to 'accepted'. Finally, dispatch an alert to Dr. Thomas Anderson (res_04) with the exact message: 'Congratulations! Your article 'New Biomarkers for Early Detection...' (art_04) has been accepted for publication.'. Display the final, accepted submission details.""",
        actions=[
            Action(name="FetchUsers", kwargs={"name": "Dr. Sarah Johnson"}),
            Action(name="AdjustUserSettings", kwargs={"user_id": "res_02", "notification_channel": "email"}),
            # Action(name="SetTopicInterest", kwargs={"user_id": "res_02", "topic": "Biomedicine", "action": "add"}), # Removido conforme feedback
            Action(name="FetchArticles", kwargs={"title": "New Biomarkers for Early Detection..."}),
            Action(name="FetchSubmissionInfo", kwargs={"article_id": "art_04"}),
            Action(name="IdentifyPotentialReviewers", kwargs={"article_id": "art_04", "exclude_user_ids": ["res_04"]}),
            Action(name="AssignReviewer", kwargs={"submission_id": "sub_02", "reviewer_user_id": "res_02"}),
            Action(name="PostNewReview", kwargs={"submission_id": "sub_02", "reviewer_user_id": "res_02", "recommendation": "accept", "comments": "This is a high-impact study with a solid methodology. I recommend it for publication."}),
            Action(name="SetSubmissionOutcome", kwargs={"submission_id": "sub_02", "new_status": "accepted"}),
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_04", "message": "Congratulations! Your article 'New Biomarkers for Early Detection...' (art_04) has been accepted for publication."}),
            Action(name="FetchSubmissionInfo", kwargs={"submission_id": "sub_02"})
        ],
        outputs=[
            '"submission_id": "sub_02"',
            '"status": "accepted"',
            '"assigned_reviewers": ["res_02"]'
        ]
    ),
    Task(
        annotator="0",
        user_id="smart_reviewer_assignment_by_keyword",
        instruction="""Perform editorial duties to find a suitable reviewer for the niche submission 'Personalized Cancer Treatment with AI-Driven Drug Discovery' (art_14 / sub_05). Extract keywords from 'art_14's abstract. Use a key term, like 'cancer', to find other relevant articles, such as one by Dr. Liu Wei. Assign Dr. Liu Wei (res_05) as a reviewer for 'sub_05'. Dispatch an alert to Dr. Tanaka (res_05) with the exact message: 'You have been assigned to review the submission 'Personalized Cancer Treatment with AI-Driven Drug Discovery' due to your expertise in the area.'.""",
        actions=[
            Action(name="FetchArticles", kwargs={"title": "Personalized Cancer Treatment with AI-Driven Drug Discovery"}),
            Action(name="GetArticleKeywords", kwargs={"article_id": "art_14"}),
            Action(name="FetchArticles", kwargs={"title": "cancer"}), # Usando "cancer" como key term conforme instrução modificada
            Action(name="FetchSubmissionInfo", kwargs={"article_id": "art_14"}),
            Action(name="FetchUsers", kwargs={"name": "Dr. Liu Wei"}),
            Action(name="AssignReviewer", kwargs={"submission_id": "sub_05", "reviewer_user_id": "res_05"}),
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_05", "message": "You have been assigned to review the submission 'Personalized Cancer Treatment with AI-Driven Drug Discovery' due to your expertise in the area."})
        ],
        outputs=[
            '"success": true',
        ]
    ),
    Task(
        annotator="0",
        user_id="researcher_changes_focus_and_profile_update",
        instruction="""Execute profile updates as Dr. Liu Wei to update your user profile to reflect a shift in research focus from 'Astrophysics' to 'AI'. Adjust your UI theme setting to 'dark'. Remove your subscription to 'Astrophysics' and add a new subscription to 'AI'. To begin exploring the new field, find 'Advances in Language Models for Code Generation' (art_01) and retrieve its keywords.""",
        actions=[
            Action(name="FetchUsers", kwargs={"name": "Dr. Liu Wei"}),
            Action(name="AdjustUserSettings", kwargs={"user_id": "res_05", "ui_theme": "dark"}),
            Action(name="AdjustUserSettings", kwargs={"user_id": "res_05", "research_field": "AI"}), # Adicionado conforme feedback
            Action(name="SetTopicInterest", kwargs={"user_id": "res_05", "topic": "Astrophysics", "action": "remove"}),
            Action(name="SetTopicInterest", kwargs={"user_id": "res_05", "topic": "AI", "action": "add"}),
            Action(name="FetchArticles", kwargs={"title": "Advances in Language Models for Code Generation"}),
            Action(name="GetArticleKeywords", kwargs={"article_id": "art_01"}),
            Action(name="FetchUsers", kwargs={"user_id": "res_05"}),
        ],
        outputs=[
            'transformer',
            'code',
            'generation',
            'models'
        ]
    ),
    Task(
        annotator="0",
        user_id="keyword_based_topic_validation",
        instruction="""Conduct editorial quality verification to verify that the article 'Gene Editing Techniques with CRISPR-Cas9' (art_03) is correctly categorized. Extract its keywords from the abstract. Update 'art_03's topic to 'Biology / AI'. Dispatch an alert to the lead author, Dr. Sarah Johnson (res_02), with the exact message: 'To improve discoverability, the topic for your article 'Gene Editing Techniques...' has been updated to 'Biology / AI' based on keyword analysis.'. Finally, subscribe yourself (res_01) to the 'Biology' topic. Display the updated article details.""", # Instrução ajustada
        actions=[
            Action(name="FetchArticles", kwargs={"title": "Gene Editing Techniques with CRISPR-Cas9"}), # Corrigido para título completo
            Action(name="GetArticleKeywords", kwargs={"article_id": "art_03"}),
            Action(name="ReviseArticleDetails", kwargs={"article_id": "art_03", "topic": "Biology / AI"}),
            Action(name="FetchUsers", kwargs={"name": "Dr. Sarah Johnson"}),
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_02", "message": "To improve discoverability, the topic for your article 'Gene Editing Techniques...' has been updated to 'Biology / AI' based on keyword analysis."}),
            Action(name="FetchUsers", kwargs={"user_id": "res_01"}),
            Action(name="SetTopicInterest", kwargs={"user_id": "res_01", "topic": "Biology", "action": "add"}),
            Action(name="FetchArticles", kwargs={"article_id": "art_03"}),
        ],
        outputs=[
            '"article_id": "art_03"',
            '"topic": "Biology / AI"'
        ]
    ),
    Task(
        annotator="0",
        user_id="conflicting_reviews_and_tie_breaker",
        instruction="""Execute editor-in-chief duties to handle a complex review case for the submission associated with 'Multimodal AI for Medical Imaging Analysis' (art_12 / sub_03). Assign two initial reviewers: Dr. Anna Petrov (res_06) and Lia Costa (res_15). Simulate their conflicting reviews: 'accept' (from res_06, comment: 'The work is solid and presents a novel framework.') and 'reject' (from res_15, comment: 'The validation methodology is flawed and does not support the conclusions.'). Due to conflicting feedback, identify and assign a third, tie-breaker reviewer (Dr. Maria Santos - res_09). Dispatch an alert to the lead author, Dr. Kenji Tanaka (res_01), with the exact message: 'Regarding your submission for 'Multimodal AI...', the initial reviews were conflicting. A third tie-breaker reviewer has been assigned to ensure a fair assessment. We will update you soon.'. Display the submission details to confirm all three reviewers are assigned.""",
        actions=[
            Action(name="FetchArticles", kwargs={"title": "Multimodal AI for Medical Imaging Analysis"}),
            Action(name="FetchSubmissionInfo", kwargs={"article_id": "art_12"}),
            Action(name="IdentifyPotentialReviewers", kwargs={"article_id": "art_12", "exclude_user_ids": ["res_01", "res_04"]}),
            Action(name="AssignReviewer", kwargs={"submission_id": "sub_03", "reviewer_user_id": "res_06", "overwrite": True}), # Explicitly assign as first reviewer.
            Action(name="AssignReviewer", kwargs={"submission_id": "sub_03", "reviewer_user_id": "res_15"}), # Explicitly assign as second reviewer.
            Action(name="PostNewReview", kwargs={"submission_id": "sub_03", "reviewer_user_id": "res_06", "recommendation": "accept", "comments": "The work is solid and presents a novel framework."}),
            Action(name="PostNewReview", kwargs={"submission_id": "sub_03", "reviewer_user_id": "res_15", "recommendation": "reject", "comments": "The validation methodology is flawed and does not support the conclusions."}),
            Action(name="IdentifyPotentialReviewers", kwargs={"article_id": "art_12", "exclude_user_ids": ["res_01", "res_04", "res_06", "res_15"]}),
            Action(name="AssignReviewer", kwargs={"submission_id": "sub_03", "reviewer_user_id": "res_09"}),
            Action(name="FetchUsers", kwargs={"name": "Dr. Kenji Tanaka"}),
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_01", "message": "Regarding your submission for 'Multimodal AI...', the initial reviews were conflicting. A third tie-breaker reviewer has been assigned to ensure a fair assessment. We will update you soon."}),
            Action(name="FetchSubmissionInfo", kwargs={"submission_id": "sub_03"})
        ],
        outputs=[
            '"submission_id": "sub_03"',
            '"assigned_reviewers": [\n    "res_06",\n    "res_15",\n    "res_09"\n  ]'
        ]
    ),
    Task(
        annotator="0",
        user_id="author_requested_retraction_workflow",
        instruction="""Handle editorial processing for Dr. Sarah Johnson's (res_02) request to retract his paper, 'Gene Editing Techniques with CRISPR-Cas9' (art_03), due to a data error. Officially mark 'art_03's status as 'retracted_by_author'. Find all articles that cite 'art_03' (e.g., 'New Biomarkers for Early Detection...' - art_04) and dispatch an alert to their lead authors with the exact message: 'URGENT: An article you cited, 'Gene Editing Techniques with CRISPR-Cas9' (art_03), has been retracted by its author. Please review your work for impact.'. If there is a pending submission for 'art_03' (sub_06), withdraw it. Finally, create a new project titled 'Ethics Review: art_03 Retraction' (proj_a1b2) led by Dr. Mendes (res_02) and link 'art_03' to it. Display the details of the updated article.""",
        actions=[
            Action(name="FetchUsers", kwargs={"name": "Dr. Sarah Johnson"}),
            Action(name="FetchArticles", kwargs={"title": "Gene Editing Techniques with CRISPR-Cas9"}), # Título completo
            Action(name="ReviseArticleDetails", kwargs={"article_id": "art_03", "status": "retracted_by_author"}),
            Action(name="FindCitations", kwargs={"article_id": "art_03"}),
            # Alertas para autores de artigos citantes
            Action(name="FetchArticles", kwargs={"article_id": "art_04"}), # Action to identify the citing paper explicitly.
            Action(name="FetchUsers", kwargs={"user_id": "res_04"}), # Action to identify the author of the citing paper.
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_04", "message": "URGENT: An article you cited, 'Gene Editing Techniques with CRISPR-Cas9' (art_03), has been retracted by its author. Please review your work for impact."}),
            Action(name="FetchArticles", kwargs={"article_id": "art_01"}), # Para art_01
            Action(name="FetchUsers", kwargs={"user_id": "res_01"}), # Para Dr. Kenji Tanaka (autor de art_01)
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_01", "message": "URGENT: An article you cited, 'Gene Editing Techniques with CRISPR-Cas9' (art_03), has been retracted by its author. Please review your work for impact."}),
            Action(name="FetchArticles", kwargs={"article_id": "art_11"}), # Para art_11
            Action(name="FetchUsers", kwargs={"user_id": "res_10"}), # Para Dr. Ana Oliveira (co-autor de art_11)
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_10", "message": "URGENT: An article you cited, 'Gene Editing Techniques with CRISPR-Cas9' (art_03), has been retracted by its author. Please review your work for impact."}),

            Action(name="CreateReviewSubmission", kwargs={"article_id": "art_03", "author_user_id": "res_02", "submission_id_override": "sub_06"}), # Criar sub_06 se não existir
            Action(name="FetchSubmissionInfo", kwargs={"article_id": "art_03"}),
            Action(name="SetSubmissionOutcome", kwargs={"submission_id": "sub_06", "new_status": "withdrawn"}),
            Action(name="CreateNewProject", kwargs={"project_name": "Ethics Review: art_03 Retraction", "lead_researcher_id": "res_02", "project_id_override": "proj_a1b2"}),
            Action(name="UpdateProjectDetails", kwargs={"project_id": "proj_a1b2", "linked_article_ids": ["art_03"]}),
            Action(name="FetchArticles", kwargs={"article_id": "art_03"})
        ],
        outputs=[
            '"article_id": "art_03"',
            '"status": "retracted_by_author"'
        ]
    ),
    Task(
        annotator="0",
        user_id="manage_special_issue_submission",
        instruction="""Manage guest editorial responsibilities for a special issue on 'AI in Healthcare', process a new manuscript from Dr. Elena Rossi (res_16) titled 'AI-Powered Diagnostic Imaging'. Register the article (art_special_01) with the abstract: 'A new method for diagnostic imaging using CNNs.' and create a submission record (sub_special_01) for it. Assign two reviewers: Dr. Anna Petrov (res_06), an AI expert, and Dr. Thomas Anderson (res_04), a Biomedicine expert. After assigning them, create a project for the special issue titled 'Special Issue: AI in Healthcare' (proj_special_01) led by yourself (res_02), and update it to link 'art_special_01'. Finally, dispatch an alert to Dr. Silva (res_16) with the exact message: 'Your submission 'AI-Powered Diagnostic Imaging' has been received for the special issue and is now under review.'. Display the new submission record with the assigned reviewers.""",
        actions=[
            Action(name="FetchUsers", kwargs={"name": "Dr. Elena Rossi"}),
            Action(name="RegisterNewArticle", kwargs={"title": "AI-Powered Diagnostic Imaging", "authors": ["Dr. Elena Rossi"], "topic": "AI", "abstract": "A new method for diagnostic imaging using CNNs.", "article_id_override": "art_special_01"}), # Abstract adicionado à instrução
            Action(name="CreateReviewSubmission", kwargs={"article_id": "art_special_01", "author_user_id": "res_16", "submission_id_override": "sub_special_01"}),
            Action(name="IdentifyPotentialReviewers", kwargs={"article_id": "art_special_01", "exclude_user_ids": ["res_16"]}),
            Action(name="FetchUsers", kwargs={"research_field": "Biomedicine"}),
            Action(name="FetchUsers", kwargs={"research_field": "AI"}),
            Action(name="AssignReviewer", kwargs={"submission_id": "sub_special_01", "reviewer_user_id": "res_06"}),
            Action(name="AssignReviewer", kwargs={"submission_id": "sub_special_01", "reviewer_user_id": "res_04"}),
            Action(name="CreateNewProject", kwargs={"project_name": "Special Issue: AI in Healthcare", "lead_researcher_id": "res_02", "project_id_override": "proj_special_01"}),
            Action(name="UpdateProjectDetails", kwargs={"project_id": "proj_special_01", "linked_article_ids": ["art_special_01"]}),
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_16", "message": "Your submission 'AI-Powered Diagnostic Imaging' has been received for the special issue and is now under review."}),
            Action(name="FetchSubmissionInfo", kwargs={"submission_id": "sub_special_01"}),
        ],
        outputs=[
            '"status": "under_review"',
            '"assigned_reviewers": [\n    "res_06",\n    "res_04"\n  ]'
        ]
    ),
    Task(
        annotator="0",
        user_id="full_major_revisions_cycle",
        instruction="""Conduct editorial management of the full major revisions cycle for the 'Quantum Cryptography' paper (art_10 / sub_04). Update the submission status to 'revisions_requested'. Dispatch an alert to the author, Prof. James Wilson (res_03), with the exact message: 'Your submission for 'Quantum Cryptography...' requires major revisions. Please review the feedback and submit a revised version.'.
    Assume the author submits a revised version titled 'Revised: Quantum Cryptography Protocols' (art_c5d6) by Prof. James Wilson and Dr. Wei Zhang, on the topic 'Quantum Physics' with the abstract: 'A revised version addressing reviewer feedback on protocol security.'. Register this new article and link it to the original submission. Reassign the original reviewers (Dr. Sarah Johnson - res_02, Dr. Anna Petrov - res_06) to assess the new version. Post a new 'accept' review from Dr. Mendes (res_02) with the comment: 'The revisions are satisfactory and address all major concerns.'. Finally, set the final submission outcome to 'accepted'. Display the final submission details.""", # Instrução ajustada com detalhes completos
        actions=[
            Action(name="FetchSubmissionInfo", kwargs={"article_id": "art_10"}),
            Action(name="ListReviewsForSubmission", kwargs={"submission_id": "sub_04"}),
            Action(name="SetSubmissionOutcome", kwargs={"submission_id": "sub_04", "new_status": "revisions_requested"}),
            Action(name="FetchUsers", kwargs={"name": "Prof. James Wilson"}),
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_03", "message": "Your submission for 'Quantum Cryptography...' requires major revisions. Please review the feedback and submit a revised version."}),
            Action(name="RegisterNewArticle", kwargs={"title": "Revised: Quantum Cryptography Protocols", "authors": ["Prof. James Wilson", "Dr. Wei Zhang"], "topic": "Quantum Physics", "abstract": "A revised version addressing reviewer feedback on protocol security.", "article_id_override": "art_c5d6"}), # Detalhes completos adicionados
            Action(name="ConnectRevisedVersion", kwargs={"submission_id": "sub_04", "revised_article_id": "art_c5d6"}),
            Action(name="AssignReviewer", kwargs={"submission_id": "sub_04", "reviewer_user_id": "res_02"}),
            Action(name="AssignReviewer", kwargs={"submission_id": "sub_04", "reviewer_user_id": "res_06"}),
            Action(name="PostNewReview", kwargs={"submission_id": "sub_04", "reviewer_user_id": "res_02", "recommendation": "accept", "comments": "The revisions are satisfactory and address all major concerns."}),
            Action(name="SetSubmissionOutcome", kwargs={"submission_id": "sub_04", "new_status": "accepted"}),
            Action(name="FetchSubmissionInfo", kwargs={"submission_id": "sub_04"}),
        ],
        outputs=[
            '"submission_id": "sub_04"',
            '"status": "accepted"',
            '"revised_version_article_id": "art_c5d6"'
        ]
    ),
    Task(
        annotator="0",
        user_id="handling_improper_review",
        instruction="""Execute editor-in-chief duties to handle an unprofessional and non-constructive review submitted for 'New Biomarkers...' (sub_02 / art_04). After identifying the problematic review (rev_02 from Dr. Anna Petrov - res_06), delete it. Find and assign a new 'Biomedicine' expert reviewer (Dr. Ricardo Mendes - res_07), excluding the author and the previous reviewer, to the submission. Update the submission status back to 'under_review'. Dispatch an alert to the author, Dr. Thomas Anderson (res_04), with the exact message: 'Regarding submission sub_02, a review was found to be unprofessional and has been removed. A new reviewer has been assigned to ensure a fair process.'. Display the updated submission details.""", # Corrigida a identificação do revisor em instrução
        actions=[
            Action(name="FetchSubmissionInfo", kwargs={"submission_id": "sub_02"}),
            Action(name="ListReviewsForSubmission", kwargs={"submission_id": "sub_02"}),
            Action(name="RemoveReview", kwargs={"review_id": "rev_02"}),
            Action(name="IdentifyPotentialReviewers", kwargs={"article_id": "art_04", "exclude_user_ids": ["res_04", "res_06"]}), # Corrigido para res_06 como revisor anterior
            Action(name="FetchUsers", kwargs={"user_id": "res_07"}),
            Action(name="AssignReviewer", kwargs={"submission_id": "sub_02", "reviewer_user_id": "res_07"}),
            Action(name="SetSubmissionOutcome", kwargs={"submission_id": "sub_02", "new_status": "under_review"}),
            Action(name="FetchUsers", kwargs={"user_id": "res_04"}), # Usando user_id
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_04", "message": "Regarding submission sub_02, a review was found to be unprofessional and has been removed. A new reviewer has been assigned to ensure a fair process."}),
            Action(name="FetchSubmissionInfo", kwargs={"submission_id": "sub_02"})
        ],
        outputs=[
            '"submission_id": "sub_02"',
            '"status": "under_review"',
            '"assigned_reviewers": [\n    "res_07"\n  ]'
        ]
    ),
    Task(
        annotator="0",
        user_id="vip_author_submission_and_profile_setup",
        instruction="""Execute research assistance for Dr. James Wilson (res_08), a new VIP author, set up his profile and fast-track his first paper submission. Configure his user settings for 'in_app' notifications and a 'dark' theme. Subscribe him to the 'Astrophysics' research topic. Register his new paper, 'Tidal Forces in Exoplanetary Systems' (art_vip_01), with the abstract: 'A study of tidal forces on exoplanets in close orbit around red dwarfs.', and create a submission (sub_vip_01), setting its status to 'expedited_review'. Identify and assign two reviewers (Prof. James Wilson - res_03, Dr. Liu Wei - res_05). Dispatch urgent alerts to Prof. James Wilson (res_03) with the exact message: 'URGENT: You have been assigned to an expedited review for the high-impact paper 'Tidal Forces in Exoplanetary Systems'.' and to Dr. Liu Wei (res_05) with the exact message: 'URGENT: You have been assigned to an expedited review for the high-impact paper 'Tidal Forces in Exoplanetary Systems'.'. Display the final submission details.""", # Abstract adicionado à instrução
        actions=[
            Action(name="FetchUsers", kwargs={"name": "Dr. Ahmed Hassan"}),
            Action(name="AdjustUserSettings", kwargs={"user_id": "res_08", "notification_channel": "in_app", "ui_theme": "dark"}),
            Action(name="SetTopicInterest", kwargs={"user_id": "res_08", "topic": "Astrophysics", "action": "add"}),
            Action(name="RegisterNewArticle", kwargs={"title": "Tidal Forces in Exoplanetary Systems", "authors": ["Dr. Ahmed Hassan"], "topic": "Astrophysics", "abstract": "A study of tidal forces on exoplanets in close orbit around red dwarfs.", "article_id_override": "art_vip_01"}),
            Action(name="CreateReviewSubmission", kwargs={"article_id": "art_vip_01", "author_user_id": "res_08", "submission_id_override": "sub_vip_01"}),
            Action(name="SetSubmissionOutcome", kwargs={"submission_id": "sub_vip_01", "new_status": "expedited_review"}),
            Action(name="IdentifyPotentialReviewers", kwargs={"article_id": "art_vip_01", "exclude_user_ids": ["res_08"]}),
            Action(name="AssignReviewer", kwargs={"submission_id": "sub_vip_01", "reviewer_user_id": "res_03"}),
            Action(name="AssignReviewer", kwargs={"submission_id": "sub_vip_01", "reviewer_user_id": "res_05"}),
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_03", "message": "URGENT: You have been assigned to an expedited review for the high-impact paper 'Tidal Forces in Exoplanetary Systems'."}),
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_05", "message": "URGENT: You have been assigned to an expedited review for the high-impact paper 'Tidal Forces in Exoplanetary Systems'."}),
            Action(name="FetchSubmissionInfo", kwargs={"submission_id": "sub_vip_01"}),
        ],
        outputs=[
            '"status": "expedited_review"',
            '"assigned_reviewers": [\n    "res_03",\n    "res_05"\n  ]'
        ]
    ),
    Task(
        annotator="0",
        user_id="handle_author_retraction_request", # Essa task é um duplicata, foi corrigida como author_requested_retraction_workflow
        instruction="""Execute editor-in-chief duties to process Dr. Sarah Johnson's (res_02) formal request to retract his paper, 'Gene Editing Techniques with CRISPR-Cas9' (art_03), due to a data error. Officially mark 'art_03's status as 'retracted_by_author'. Find all articles that cited 'art_03' (e.g., 'New Biomarkers for Early Detection...' - art_04) and dispatch an alert to the lead author of each citing paper with the exact message: 'URGENT: A paper you cited, 'Gene Editing Techniques with CRISPR-Cas9' (art_03), has been retracted by its author. Please review your work.'. If there is a pending submission for 'art_03' (sub_06), withdraw it. Finally, create a new project titled 'Ethics Review: art_03 Retraction' (proj_1a2b) led by Dr. Mendes (res_02) and link 'art_03' to it. Display the details of the updated article.""", # Instrução ajustada
        actions=[
            Action(name="FetchUsers", kwargs={"name": "Dr. Sarah Johnson"}),
            Action(name="FetchArticles", kwargs={"title": "Gene Editing Techniques with CRISPR-Cas9"}), # Título completo
            Action(name="ReviseArticleDetails", kwargs={"article_id": "art_03", "status": "retracted_by_author"}),
            Action(name="FindCitations", kwargs={"article_id": "art_03"}),
            # Alertas para autores de artigos citantes
            Action(name="FetchArticles", kwargs={"article_id": "art_04"}), # Para art_04
            Action(name="FetchUsers", kwargs={"user_id": "res_04"}), # Para Dr. Thomas Anderson
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_04", "message": "URGENT: A paper you cited, 'Gene Editing Techniques with CRISPR-Cas9' (art_03), has been retracted by its author. Please review your work."}),
            Action(name="FetchArticles", kwargs={"article_id": "art_01"}), # Para art_01
            Action(name="FetchUsers", kwargs={"user_id": "res_01"}), # Para Dr. Kenji Tanaka
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_01", "message": "URGENT: A paper you cited, 'Gene Editing Techniques with CRISPR-Cas9' (art_03), has been retracted by its author. Please review your work."}),
            Action(name="FetchArticles", kwargs={"article_id": "art_11"}), # Para art_11
            Action(name="FetchUsers", kwargs={"user_id": "res_10"}), # Para Dr. Ana Oliveira
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_10", "message": "URGENT: A paper you cited, 'Gene Editing Techniques with CRISPR-Cas9' (art_03), has been retracted by its author. Please review your work."}),

            Action(name="CreateReviewSubmission", kwargs={"article_id": "art_03", "author_user_id": "res_02", "submission_id_override": "sub_06"}), # Criar sub_06 se não existir
            Action(name="FetchSubmissionInfo", kwargs={"article_id": "art_03"}),
            Action(name="SetSubmissionOutcome", kwargs={"submission_id": "sub_06", "new_status": "withdrawn"}),
            Action(name="CreateNewProject", kwargs={"project_name": "Ethics Review: art_03 Retraction", "lead_researcher_id": "res_02", "project_id_override": "proj_1a2b"}),
            Action(name="UpdateProjectDetails", kwargs={"project_id": "proj_1a2b", "linked_article_ids": ["art_03"]}),
            Action(name="FetchArticles", kwargs={"article_id": "art_03"})
        ],
        outputs=[
            '"article_id": "art_03"',
            '"status": "retracted_by_author"'
        ]
    ),
    Task(
        annotator="0",
        user_id="full_major_revision_and_re_review_cycle", # Essa task é um duplicata, foi corrigida como full_major_revisions_cycle
        instruction="""Conduct editorial management of the full major revision and re-review cycle for the submission 'Quantum Cryptography Protocols...' (art_10 / sub_04). Update the submission status to 'revisions_requested'. Dispatch an alert to the author, Prof. James Wilson (res_03), with the exact message: 'Your submission for 'Quantum Cryptography...' requires major revisions. Please review the feedback and submit a revised version.'.
    Assume the author submits a revised version titled 'Revised: Quantum Cryptography Protocols' (art_c5d6) by Prof. James Wilson and Dr. Wei Zhang, on the topic 'Quantum Physics' with the abstract: 'A revised version addressing reviewer feedback on protocol security.'. Register this new article and link it to the original submission. Reassign the original reviewers (Dr. Sarah Johnson - res_02, Dr. Anna Petrov - res_06) to assess the new version. Post a new 'accept' review from Dr. Mendes (res_02) with the comment: 'The revisions are satisfactory and address all major concerns.'. Finally, set the final submission outcome to 'accepted'. Display the final submission details.""", # Instrução ajustada com detalhes completos
        actions=[
            Action(name="FetchSubmissionInfo", kwargs={"article_id": "art_10"}),
            Action(name="ListReviewsForSubmission", kwargs={"submission_id": "sub_04"}),
            Action(name="SetSubmissionOutcome", kwargs={"submission_id": "sub_04", "new_status": "revisions_requested"}),
            Action(name="FetchUsers", kwargs={"name": "Prof. James Wilson"}),
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_03", "message": "Your submission for 'Quantum Cryptography...' requires major revisions. Please review the feedback and submit a revised version."}),
            Action(name="RegisterNewArticle", kwargs={"title": "Revised: Quantum Cryptography Protocols", "authors": ["Prof. James Wilson", "Dr. Wei Zhang"], "topic": "Quantum Physics", "abstract": "A revised version addressing reviewer feedback on protocol security.", "article_id_override": "art_c5d6"}), # Detalhes completos adicionados
            Action(name="ConnectRevisedVersion", kwargs={"submission_id": "sub_04", "revised_article_id": "art_c5d6"}),
            Action(name="AssignReviewer", kwargs={"submission_id": "sub_04", "reviewer_user_id": "res_02"}),
            Action(name="AssignReviewer", kwargs={"submission_id": "sub_04", "reviewer_user_id": "res_06"}),
            Action(name="PostNewReview", kwargs={"submission_id": "sub_04", "reviewer_user_id": "res_02", "recommendation": "accept", "comments": "The revisions are satisfactory and address all major concerns."}),
            Action(name="SetSubmissionOutcome", kwargs={"submission_id": "sub_04", "new_status": "accepted"}),
            Action(name="FetchSubmissionInfo", kwargs={"submission_id": "sub_04"}),
        ],
        outputs=[
            '"submission_id": "sub_04"',
            '"status": "accepted"',
            '"revised_version_article_id": "art_c5d6"'
        ]
    ),
    Task(
        annotator="0",
        user_id="thematic_collection_curation",
        instruction="""Execute senior editorial duties as Dr. Sarah Johnson (res_02), curate a new thematic collection on 'Federated Learning'. Identify two relevant articles: 'Federated Learning for Privacy-Preserving AI' (art_06) and 'Robotic Process Automation with Large Language Models' (art_15). Create a new project titled 'Thematic Collection: Federated Learning' (proj_collection_01) led by yourself, linking both articles. Subscribe yourself to the 'AI' topic to monitor for new papers. Dispatch alerts to the authors of both selected articles: Dr. Anna Petrov (res_06) with the exact message: 'Your paper 'Federated Learning...' has been selected for our new Thematic Collection.' and Lia Costa (res_15) with the exact message: 'Your paper on federated systems has been selected for our new Thematic Collection.'. Display your updated user profile.""",
        actions=[
            Action(name="FetchUsers", kwargs={"name": "Dr. Sarah Johnson"}),
            Action(name="SetTopicInterest", kwargs={"user_id": "res_02", "topic": "AI", "action": "add"}),
            Action(name="FetchArticles", kwargs={"title": "Federated Learning for Privacy-Preserving AI"}), # Título completo
            Action(name="FetchArticles", kwargs={"title": "Robotic Process Automation with Large Language Models"}), # Adicionado fetch para verificar a existência de art_15
            Action(name="CreateNewProject", kwargs={"project_name": "Thematic Collection: Federated Learning", "lead_researcher_id": "res_02", "project_id_override": "proj_collection_01"}),
            Action(name="UpdateProjectDetails", kwargs={"project_id": "proj_collection_01", "linked_article_ids": ["art_06", "art_15"]}),
            Action(name="FetchUsers", kwargs={"name": "Dr. Anna Petrov"}),
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_06", "sender_user_id": "res_02", "message": "Your paper 'Federated Learning...' has been selected for our new Thematic Collection."}),
            Action(name="FetchUsers", kwargs={"name": "Lia Costa"}),
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_15", "sender_user_id": "res_02", "message": "Your paper on federated systems has been selected for our new Thematic Collection."}),
            Action(name="FetchUsers", kwargs={"user_id": "res_02"})
        ],
        outputs=[
            '"user_id": "res_02"'
        ]
    ),
    Task(
        annotator="0",
        user_id="handle_conflict_of_interest_complaint",
        instruction="""Execute editor-in-chief duties to resolve a conflict of interest complaint for submission 'sub_03', where the reviewer Dr. Liu Wei (res_05) shares the same institution as the author, Dr. Kenji Tanaka (res_01). If their institutions match, put the submission on 'on_hold_conflict_review'. Delete the conflicted review (rev_03). Then, reset the reviewer panel by assigning Dr. Thomas Anderson (res_04) as the sole reviewer. Dispatch an alert to Dr. Souza (res_01) with the exact message: 'An investigation found a conflict of interest in your submission's review process. The conflicted reviewer has been removed and their review deleted. The process will resume shortly.'. Concurrently, dispatch an alert to Dr. Tanaka (res_05) with the exact message: 'You have been removed from the review of sub_03 due to a conflict of interest (shared institution with an author). Thank you for your understanding.'. Display the updated submission details.""",
        actions=[
            Action(name="FetchSubmissionInfo", kwargs={"submission_id": "sub_03"}),
            Action(name="FetchUsers", kwargs={"name": "Dr. Kenji Tanaka"}),
            Action(name="FetchUsers", kwargs={"name": "Dr. Liu Wei"}),
            Action(name="ListReviewsForSubmission", kwargs={"submission_id": "sub_03"}),
            Action(name="RemoveReview", kwargs={"review_id": "rev_03"}),
            Action(name="AssignReviewer", kwargs={"submission_id": "sub_03", "reviewer_user_id": "res_04", "overwrite": True}),
            Action(name="SetSubmissionOutcome", kwargs={"submission_id": "sub_03", "new_status": "on_hold_conflict_review"}),
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_01", "message": "An investigation found a conflict of interest in your submission's review process. The conflicted reviewer has been removed and their review deleted. The process will resume shortly."}),
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_05", "message": "You have been removed from the review of sub_03 due to a conflict of interest (shared institution with an author). Thank you for your understanding."}),
            Action(name="FetchSubmissionInfo", kwargs={"submission_id": "sub_03"}),
        ],
        outputs=[
            '"submission_id": "sub_03"',
            '"status": "on_hold_conflict_review"',
            '"assigned_reviewers": [\n    "res_04"\n  ]'
        ]
    ),
    Task(
        annotator="0",
        user_id="expedited_review_for_linked_project",
        instruction="""Conduct editorial management to fast-track the new submission for 'AI applications in diagnosing...' (art_09 / sub_09), given its link to a high-priority grant. Update the submission status to 'expedited_review'. Assign two available AI expert reviewers (Dr. Kenji Tanaka - res_01, Dr. Anna Petrov - res_06). Dispatch urgent alerts to the author, Dr. Sarah Johnson (res_02), with the exact message: 'Due to its link to a priority grant, your submission for 'AI applications...' has been fast-tracked for expedited review.'. Concurrently, dispatch urgent alerts to Dr. Souza (res_01) and Dr. Khan (res_06) with the exact message: 'URGENT: You have been assigned to an expedited review for high-impact submission sub_09.'. Display the updated submission record.""",
        actions=[
            Action(name="FetchArticles", kwargs={"title": "AI applications in diagnosing"}),
            Action(name="FetchUsers", kwargs={"name": "Dr. Sarah Johnson"}),
            Action(name="CreateReviewSubmission", kwargs={"article_id": "art_09", "author_user_id": "res_02", "submission_id_override": "sub_09"}),
            Action(name="SetSubmissionOutcome", kwargs={"submission_id": "sub_09", "new_status": "expedited_review"}),
            Action(name="IdentifyPotentialReviewers", kwargs={"article_id": "art_09", "exclude_user_ids": ["res_02"]}),
            Action(name="AssignReviewer", kwargs={"submission_id": "sub_09", "reviewer_user_id": "res_01"}),
            Action(name="AssignReviewer", kwargs={"submission_id": "sub_09", "reviewer_user_id": "res_06"}),
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_02", "message": "Due to its link to a priority grant, your submission for 'AI applications...' has been fast-tracked for expedited review."}),
            Action(name="FetchUsers", kwargs={"user_id": "res_01"}),
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_01", "message": "URGENT: You have been assigned to an expedited review for high-impact submission sub_09."}),
            Action(name="FetchUsers", kwargs={"user_id": "res_06"}),
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_06", "message": "URGENT: You have been assigned to an expedited review for high-impact submission sub_09."}),
            Action(name="FetchSubmissionInfo", kwargs={"submission_id": "sub_09"})
        ],
        outputs=[
            '"status": "expedited_review"',
            '"assigned_reviewers": [\n    "res_01",\n    "res_06"\n  ]'
        ]
    ),
    Task(
        annotator="0",
        user_id="cross_institutional_collaboration_setup",
        instruction="""Execute program management to foster collaboration between Dr. Anna Petrov (res_06) from 'AI' and Dr. Thomas Anderson (res_04) from 'Biomedicine'. Create a new project titled 'AI in Modern Biomedicine Initiative' (proj_collab_01) with Dr. Khan as the lead. Link their key papers: 'Federated Learning for Privacy-Preserving AI' (art_06) and 'New Biomarkers for Early Detection of Neurodegenerative Diseases' (art_04). Subscribe Dr. Bauer (res_04) to the 'AI' topic. Dispatch an alert to Dr. Khan (res_06) with the exact message: 'You have been assigned as the lead for a new cross-disciplinary project: 'AI in Modern Biomedicine Initiative'.'. Concurrently, dispatch an alert to Dr. Bauer (res_04) with the exact message: 'You have been invited to collaborate on a new project, 'AI in Modern Biomedicine Initiative', led by Dr. Anna Petrov.'. Display the updated user profile for Dr. Thomas Anderson.""",
        actions=[
            Action(name="FetchUsers", kwargs={"name": "Dr. Anna Petrov"}),
            Action(name="FetchUsers", kwargs={"name": "Dr. Thomas Anderson"}),
            Action(name="CreateNewProject", kwargs={"project_name": "AI in Modern Biomedicine Initiative", "lead_researcher_id": "res_06", "project_id_override": "proj_collab_01"}),
            Action(name="FetchArticles", kwargs={"title": "Federated Learning for Privacy-Preserving AI"}), # Título completo
            Action(name="FetchArticles", kwargs={"title": "New Biomarkers for Early Detection of Neurodegenerative Diseases"}), # Título completo
            Action(name="UpdateProjectDetails", kwargs={"project_id": "proj_collab_01", "linked_article_ids": ["art_06", "art_04"]}),
            Action(name="SetTopicInterest", kwargs={"user_id": "res_04", "topic": "AI", "action": "add"}),
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_06", "message": "You have been assigned as the lead for a new cross-disciplinary project: 'AI in Modern Biomedicine Initiative'."}),
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_04", "message": "You have been invited to collaborate on a new project, 'AI in Modern Biomedicine Initiative', led by Dr. Anna Petrov."}),
            Action(name="FetchUsers", kwargs={"user_id": "res_04"}),
        ],
        outputs=[
            '"user_id": "res_04"',
        ]
    ),
    Task(
        annotator="0",
        user_id="grant_justification_and_impact_report",
        instruction="""Manage academic activities as Dr. Prof. James Wilson (res_03), justify a grant renewal for your 'Quantum Computing Applications' project by demonstrating the cross-disciplinary impact of your main article (art_02). Identify all papers citing 'art_02', and for each, extract its keywords. After identifying a clear cross-disciplinary citation, such as 'Advances in Language Models for Code Generation' (art_01) from the 'AI' field, create a new project titled 'Impact Report: Quantum Applications' (proj_impact_01) led by yourself. Link 'art_02' and 'art_01' to this new project. Finally, dispatch an alert to the author of 'art_01', Dr. Kenji Tanaka (res_01), with the exact message: 'Just a note to say your paper was highlighted as a key example of cross-disciplinary impact in a grant renewal report for my project. Great work!'. Display your updated user profile (res_03).""",
        actions=[
            Action(name="FetchUsers", kwargs={"name": "Prof. James Wilson"}),
            Action(name="FetchArticles", kwargs={"article_id": "art_02"}),
            Action(name="FindCitations", kwargs={"article_id": "art_02"}),
            Action(name="GetArticleKeywords", kwargs={"article_id": "art_01"}),
            Action(name="GetArticleKeywords", kwargs={"article_id": "art_05"}), # To get keywords for art_05 too, consistent with original actions.
            Action(name="FetchArticles", kwargs={"article_id": "art_01"}),
            Action(name="CreateNewProject", kwargs={"project_name": "Impact Report: Quantum Applications", "lead_researcher_id": "res_03", "project_id_override": "proj_impact_01"}),
            Action(name="UpdateProjectDetails", kwargs={"project_id": "proj_impact_01", "linked_article_ids": ["art_02", "art_01"]}),
            Action(name="FetchUsers", kwargs={"name": "Dr. Kenji Tanaka"}),
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_01", "sender_user_id": "res_03", "message": "Just a note to say your paper was highlighted as a key example of cross-disciplinary impact in a grant renewal report for my project. Great work!"}),
            Action(name="FetchUsers", kwargs={"user_id": "res_03"}),
        ],
        outputs=[
            '"user_id": "res_03"'
        ]
    ),
    Task(
        annotator="0",
        user_id="handle_reviewer_unavailability_and_reassignment",
        instruction="""Conduct editorial reassignment management for submission 'Limits of Quantum Computing...' (art_02 / sub_01) after reviewer Dr. Kenji Tanaka (res_01) becomes unavailable. Find and assign a new available 'Artificial Intelligence' reviewer (Dr. Anna Petrov - res_06), ensuring the author Prof. James Wilson (res_03) is not reassigned. Overwrite previous reviewer assignments to keep the panel clean. Dispatch an alert to Dr. Souza (res_01) with the exact message: 'You have been unassigned from the review for submission 'sub_01'. Thank you for your time.'. Concurrently, dispatch an alert to Dr. Khan (res_06) with the exact message: 'You have been assigned to review submission 'sub_01'.'. Finally, dispatch an alert to Prof. James Wilson (res_03) with the exact message: 'Due to unforeseen circumstances, a new reviewer has been assigned to your submission 'sub_01'.'. Display the updated submission details.""",
        actions=[
            Action(name="FetchSubmissionInfo", kwargs={"article_id": "art_02"}),
            Action(name="FetchUsers", kwargs={"user_id": "res_01"}),
            Action(name="FetchUsers", kwargs={"research_field": "Artificial Intelligence"}), # To find Dr. Anna Petrov.
            Action(name="FetchUsers", kwargs={"user_id": "res_06"}), # To ensure getting Aisha Khan's user_id.
            Action(name="AssignReviewer", kwargs={"submission_id": "sub_01", "reviewer_user_id": "res_06", "overwrite": True}),
            Action(name="FetchUsers", kwargs={"user_id": "res_03"}),
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_03", "message": "Due to unforeseen circumstances, a new reviewer has been assigned to your submission 'sub_01'."}),
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_01", "message": "You have been unassigned from the review for submission 'sub_01'. Thank you for your time."}),
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_06", "message": "You have been assigned to review submission 'sub_01'."}),
            Action(name="FetchSubmissionInfo", kwargs={"submission_id": "sub_01"}),
        ],
        outputs=[
            '"submission_id": "sub_01"',
            '"assigned_reviewers": [\n    "res_06"\n  ]'
        ]
    ),
    Task(
        annotator="0",
        user_id="investigate_suspiciously_high_review_score",
        instruction="""As editor-in-chief, address a suspiciously high review score (perfect score with generic comments) for the submission of 'New Biomarkers for Early Detection...' (art_04 / sub_02). List the reviews for the submission. Find a new reviewer (Dr. Ricardo Mendes - res_07) from the 'Biomedicine' field, excluding the author (res_04) and the original reviewer (res_02). Assign her to the submission. Set the submission status to 'pending_second_opinion'. Dispatch an alert to the author, Dr. Thomas Anderson (res_04), with the exact message: 'To ensure the highest quality review, we are seeking a second opinion for your submission 'sub_02'. We will provide an update shortly.'. Concurrently, dispatch an alert to Dr. Santos (res_07) with the exact message: 'You have been assigned to provide a second review for submission 'sub_02'.'. Display the updated user settings for Dr. Sarah Johnson (res_02).""",
        actions=[
            Action(name="FetchSubmissionInfo", kwargs={"article_id": "art_04"}),
            Action(name="ListReviewsForSubmission", kwargs={"submission_id": "sub_02"}),
            Action(name="FetchUsers", kwargs={"user_id": "res_02"}),
            Action(name="FetchUsers", kwargs={"user_id": "res_04"}),
            Action(name="IdentifyPotentialReviewers", kwargs={"article_id": "art_04", "exclude_user_ids": ["res_04", "res_02"]}),
            Action(name="AssignReviewer", kwargs={"submission_id": "sub_02", "reviewer_user_id": "res_07"}),
            Action(name="SetSubmissionOutcome", kwargs={"submission_id": "sub_02", "new_status": "pending_second_opinion"}),
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_04", "message": "To ensure the highest quality review, we are seeking a second opinion for your submission 'sub_02'. We will provide an update shortly."}),
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_07", "message": "You have been assigned to provide a second review for submission 'sub_02'."}),
            # Removida a ação adjust_user_settings, pois não é especificada na instrução e é não determinística.
            # Se fosse necessário mostrar o user_id de res_02, seria apenas um fetch_users.
            Action(name="FetchUsers", kwargs={"user_id": "res_02"}), # Apenas para exibir o perfil de res_02 como output final
        ],
        outputs=[
            '"user_id": "res_02"', # Ajustado para o que fetch_users realmente retorna
        ]
    ),
    Task(
        annotator="0",
        user_id="curate_thematic_project_and_invite_authors",
        instruction="""Execute senior editorial duties as Dr. Sarah Johnson (res_02), curate a new project titled 'AI Applications in Medicine' (proj_themed_01). Find two articles that fit this theme: 'Multimodal AI for Medical Imaging Analysis' (art_12) about 'diagnostic imaging' and 'Personalized Cancer Treatment with AI-Driven Drug Discovery' (art_14) about 'drug discovery'. Link both articles to 'proj_themed_01'. Dispatch alerts to the lead authors of both papers: Dr. Kenji Tanaka (res_01) with the exact message: 'Your paper has been selected to be featured in our new 'AI Applications in Medicine' collection.' and Dr. Thomas Anderson (res_04) with the exact message: 'Your paper has been selected to be featured in our new 'AI Applications in Medicine' collection.'. Display the details of 'art_12' to confirm.""",
        actions=[
            Action(name="FetchArticles", kwargs={"title": "Multimodal AI for Medical Imaging Analysis"}), # Título completo para art_12
            Action(name="FetchArticles", kwargs={"title": "Personalized Cancer Treatment with AI-Driven Drug Discovery"}), # Título completo para art_14
            Action(name="FetchUsers", kwargs={"name": "Dr. Sarah Johnson"}),
            Action(name="CreateNewProject", kwargs={"project_name": "AI Applications in Medicine", "lead_researcher_id": "res_02", "project_id_override": "proj_themed_01"}),
            Action(name="UpdateProjectDetails", kwargs={"project_id": "proj_themed_01", "linked_article_ids": ["art_12", "art_14"]}),
            Action(name="FetchUsers", kwargs={"name": "Dr. Kenji Tanaka"}),
            Action(name="FetchUsers", kwargs={"name": "Dr. Thomas Anderson"}),
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_01", "sender_user_id": "res_02", "message": "Your paper has been selected to be featured in our new 'AI Applications in Medicine' collection."}),
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_04", "sender_user_id": "res_02", "message": "Your paper has been selected to be featured in our new 'AI Applications in Medicine' collection."}),
            Action(name="FetchArticles", kwargs={"article_id": "art_12"}),
        ],
        outputs=[
            '"article_id": "art_12"'
        ]
    ),
    Task(
        annotator="0",
        user_id="grant_application_support_and_review",
        instruction="""As an editor helping Dr. Thomas Anderson (res_04) prepare for a grant application, create a new project titled 'Grant Application: Biomarkers' (proj_grant_01) and link her paper 'New Biomarkers for Early Detection...' (art_04) to it. Identify two 'Biomedicine' experts from different institutions (Dr. Sarah Johnson - res_02, Dr. Ricardo Mendes - res_07) to act as informal reviewers for 'art_04'. Dispatch alerts to Dr. Mendes (res_02) with the exact message: 'Would you be available to provide an informal peer review for 'New Biomarkers...' to support a grant application?' and to Dr. Santos (res_07) with the exact message: 'Would you be available to provide an informal peer review for 'New Biomarkers...' to support a grant application?'. Finally, subscribe Dr. Bauer (res_04) to the 'AI' topic, as the grant encourages interdisciplinary work. Display the updated user profile for Dr. Thomas Anderson.""",
        actions=[
            Action(name="FetchUsers", kwargs={"name": "Dr. Thomas Anderson"}),
            Action(name="FetchArticles", kwargs={"title": "New Biomarkers for Early Detection of Neurodegenerative Diseases"}), # Título completo
            Action(name="CreateNewProject", kwargs={"project_name": "Grant Application: Biomarkers", "lead_researcher_id": "res_04", "project_id_override": "proj_grant_01"}),
            Action(name="UpdateProjectDetails", kwargs={"project_id": "proj_grant_01", "linked_article_ids": ["art_04"]}),
            Action(name="IdentifyPotentialReviewers", kwargs={"article_id": "art_04", "exclude_user_ids": ["res_04"]}),
            Action(name="FetchUsers", kwargs={"user_id": "res_02"}),
            Action(name="FetchUsers", kwargs={"user_id": "res_07"}),
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_02", "message": "Would you be available to provide an informal peer review for 'New Biomarkers...' to support a grant application?"}),
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_07", "message": "Would you be available to provide an informal peer review for 'New Biomarkers...' to support a grant application?"}),
            Action(name="SetTopicInterest", kwargs={"user_id": "res_04", "topic": "AI", "action": "add"}),
            Action(name="FetchUsers", kwargs={"user_id": "res_04"}),
        ],
        outputs=[
            '"user_id": "res_04"',
        ]
    ),
    Task(
        annotator="0",
        user_id="expert_conflict_resolution_and_review_cycle",
        instruction="""As editor-in-chief Dr. Sarah Johnson (res_02), handle the critical submission 'Multimodal AI for Medical Imaging Analysis' (art_12 / sub_03). Assign two initial reviewers: Dr. Anna Petrov (res_06) and Lia Costa (res_15). Simulate their conflicting reviews: 'accept' (from res_06, comment: 'An excellent and timely contribution to the field.') and 'reject' (from res_15, comment: 'The conclusions are not well supported by the experimental data.'). Update your user settings to switch to the 'light' theme. Identify and assign a new, third, neutral reviewer (Dr. Maria Santos - res_09). Dispatch an alert to Dr. Kenji Tanaka (res_01) with the exact message: 'Regarding your submission, the initial reviews were conflicting, so a third reviewer has been assigned to ensure a thorough assessment. We appreciate your patience.'. Dispatch alerts to Dr. Khan (res_06) and Dr. Anderson (res_15) with the exact message: 'Thank you for your review of sub_03. Due to conflicting feedback, a tie-breaker has been engaged. No further action is needed from you at this time.'. Display the profile details of the new tie-breaker reviewer (res_09).""",
        actions=[
            Action(name="FetchUsers", kwargs={"name": "Dr. Sarah Johnson"}),
            Action(name="AdjustUserSettings", kwargs={"user_id": "res_02", "ui_theme": "light"}),
            Action(name="FetchSubmissionInfo", kwargs={"article_id": "art_12"}),
            Action(name="AssignReviewer", kwargs={"submission_id": "sub_03", "reviewer_user_id": "res_06", "overwrite": True}), # Assign Dr. Anna Petrov.
            Action(name="AssignReviewer", kwargs={"submission_id": "sub_03", "reviewer_user_id": "res_15"}), # Assign Lia Costa.
            Action(name="PostNewReview", kwargs={"submission_id": "sub_03", "reviewer_user_id": "res_06", "recommendation": "accept", "comments": "An excellent and timely contribution to the field."}),
            Action(name="PostNewReview", kwargs={"submission_id": "sub_03", "reviewer_user_id": "res_15", "recommendation": "reject", "comments": "The conclusions are not well supported by the experimental data."}),
            Action(name="IdentifyPotentialReviewers", kwargs={"article_id": "art_12", "exclude_user_ids": ["res_01", "res_04", "res_06", "res_15"]}), # Exclude authors and initial reviewers.
            Action(name="AssignReviewer", kwargs={"submission_id": "sub_03", "reviewer_user_id": "res_09"}),
            Action(name="FetchUsers", kwargs={"name": "Dr. Kenji Tanaka"}),
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_01", "sender_user_id": "res_02", "message": "Regarding your submission, the initial reviews were conflicting, so a third reviewer has been assigned to ensure a thorough assessment. We appreciate your patience."}),
            Action(name="FetchUsers", kwargs={"name": "Dr. Anna Petrov"}),
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_06", "sender_user_id": "res_02", "message": "Thank you for your review of sub_03. Due to conflicting feedback, a tie-breaker has been engaged. No further action is needed from you at this time."}),
            Action(name="FetchUsers", kwargs={"name": "Lia Costa"}),
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_15", "sender_user_id": "res_02", "message": "Thank you for your review of sub_03. Due to conflicting feedback, a tie-breaker has been engaged. No further action is needed from you at this time."}),
            Action(name="FetchUsers", kwargs={"user_id": "res_09"}) # Display profile details of the new reviewer.
        ],
        outputs=[
            '"user_id": "res_09"',
            '"name": "Dr. Maria Santos"',
            '"research_field": "Artificial Intelligence"'
        ]
    ),
    Task(
        annotator="0",
        user_id="full_lifecycle_with_major_revision",
        instruction="""Conduct editorial management of the full major revision and re-review cycle for the submission 'Quantum Cryptography Protocols...' (art_10 / sub_04). Update the submission status to 'revisions_requested'. Dispatch an alert to the author, Prof. James Wilson (res_03), with the exact message: 'Your submission for 'Quantum Cryptography...' requires major revisions. Please review the feedback and submit a revised version.'.
    Assume the author submits a revised version titled 'Revised: Quantum Cryptography Protocols' (art_c5d6) by Prof. James Wilson and Dr. Wei Zhang, on the topic 'Quantum Physics' with the abstract: 'A revised version addressing reviewer feedback on protocol security.'. Register this new article and link it to the original submission. Reassign the original reviewers (Dr. Sarah Johnson - res_02, Dr. Anna Petrov - res_06) to assess the new version. Post a new 'accept' review from Dr. Mendes (res_02) with the comment: 'The revisions are satisfactory and address all major concerns.'. Finally, set the final submission outcome to 'accepted'. Display the final submission details.""",
        actions=[
            Action(name="FetchSubmissionInfo", kwargs={"article_id": "art_10"}),
            Action(name="ListReviewsForSubmission", kwargs={"submission_id": "sub_04"}),
            Action(name="SetSubmissionOutcome", kwargs={"submission_id": "sub_04", "new_status": "revisions_requested"}),
            Action(name="FetchUsers", kwargs={"name": "Prof. James Wilson"}),
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_03", "message": "Your submission for 'Quantum Cryptography...' requires major revisions. Please review the feedback and submit a revised version."}),
            Action(name="RegisterNewArticle", kwargs={"title": "Revised: Quantum Cryptography Protocols", "authors": ["Prof. James Wilson", "Dr. Wei Zhang"], "topic": "Quantum Physics", "abstract": "A revised version addressing reviewer feedback on protocol security.", "article_id_override": "art_c5d6"}), # Detalhes completos adicionados
            Action(name="ConnectRevisedVersion", kwargs={"submission_id": "sub_04", "revised_article_id": "art_c5d6"}),
            Action(name="AssignReviewer", kwargs={"submission_id": "sub_04", "reviewer_user_id": "res_02"}),
            Action(name="AssignReviewer", kwargs={"submission_id": "sub_04", "reviewer_user_id": "res_06"}),
            Action(name="PostNewReview", kwargs={"submission_id": "sub_04", "reviewer_user_id": "res_02", "recommendation": "accept", "comments": "The revisions are satisfactory and address all major concerns."}),
            Action(name="SetSubmissionOutcome", kwargs={"submission_id": "sub_04", "new_status": "accepted"}),
            Action(name="FetchSubmissionInfo", kwargs={"submission_id": "sub_04"}),
        ],
        outputs=[
            '"submission_id": "sub_04"',
            '"status": "accepted"',
            '"revised_version_article_id": "art_c5d6"'
        ]
    ),
    Task(
        annotator="0",
        user_id="audit_and_remediate_compromised_project",
        instruction="""As an auditor, remediate the 'Quantum Computing Applications' project (proj_01), which is compromised due to the retraction of its key paper, 'Limits of Quantum Computing...' (art_02). Update the project's status to 'on_hold'. Find and link a suitable replacement paper on 'Quantum Physics', specifically 'Quantum Cryptography Protocols' (art_10), to the project. As the original lead is unavailable, reassign leadership to an available expert (Prof. James Wilson - res_03). Dispatch an alert to Prof. James Wilson (res_03) with the exact message: 'You have been assigned as the new lead for the project 'Quantum Computing Applications' following its remediation.'. Concurrently, dispatch an alert to Dr. Anna Petrov (res_06), author of 'art_10', with the exact message: 'Your paper 'Quantum Cryptography Protocols...' has been linked to the 'Quantum Computing Applications' project as a new foundational article.'. Display the details of 'art_10' to confirm.""",
        actions=[
            Action(name="FetchArticles", kwargs={"title": "Limits of Quantum Computing in Optimization Problems"}),
            Action(name="ReviseArticleDetails", kwargs={"article_id": "art_02", "status": "retracted"}),
            Action(name="FetchArticles", kwargs={"topic": "Quantum"}), # Action to find replacement paper.
            Action(name="UpdateProjectDetails", kwargs={"project_id": "proj_01", "status": "on_hold"}),
            Action(name="FetchArticles", kwargs={"title": "Quantum Cryptography Protocols"}), # Action to specify which paper is used for replacement.
            Action(name="UpdateProjectDetails", kwargs={"project_id": "proj_01", "linked_article_ids": ["art_10"]}), # Only link the new one if the old one is effectively removed.
            Action(name="FetchUsers", kwargs={"research_field": "Quantum Physics", "availability": "available"}), # Action to find new lead.
            Action(name="UpdateProjectDetails", kwargs={"project_id": "proj_01", "lead_researcher_id": "res_03"}), # Reassign to Prof. James Wilson.
            Action(name="FetchUsers", kwargs={"name": "Dr. Anna Petrov"}), # To get user_id of the author of art_10
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_03", "message": "You have been assigned as the new lead for the project 'Quantum Computing Applications' following its remediation."}),
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_06", "message": "Your paper 'Quantum Cryptography Protocols...' has been linked to the 'Quantum Computing Applications' project as a new foundational article."}),
            Action(name="FetchArticles", kwargs={"article_id": "art_10"}),
        ],
        outputs=[
            '"article_id": "art_10"'
        ]
    ),
    Task(
        annotator="0",
        user_id="onboard_new_user_and_fast_track_submission",
        instruction="""As an admin, onboard Dr. Ricardo Mendes (res_07), a new VIP user, by setting up her profile and fast-tracking her first paper submission. Adjust her user settings to a 'light' theme and subscribe her to the 'Biomedicine' research topic. Register her paper, 'Advanced Gene Therapy Applications' (art_expert_03), with the abstract: 'A novel approach to gene therapy.', and create a submission (sub_expert_03), setting its status to 'expedited_review'. Identify and assign two reviewers (Dr. Sarah Johnson - res_02, Dr. Thomas Anderson - res_04). Dispatch alerts to Dr. Santos (res_07) with the exact message: 'Welcome! Your first submission has been received and is being fast-tracked for review.'; to Dr. Mendes (res_02) with the exact message: 'URGENT: You have been assigned to an expedited review for sub_expert_03.'; and to Dr. Bauer (res_04) with the exact message: 'URGENT: You have been assigned to an expedited review for sub_expert_03.'. Display the final submission status.""", # Abstract adicionado à instrução
        actions=[
            Action(name="FetchUsers", kwargs={"name": "Dr. Ricardo Mendes"}),
            Action(name="AdjustUserSettings", kwargs={"user_id": "res_07", "ui_theme": "light"}),
            Action(name="SetTopicInterest", kwargs={"user_id": "res_07", "topic": "Biomedicine", "action": "add"}),
            Action(name="RegisterNewArticle", kwargs={"title": "Advanced Gene Therapy Applications", "authors": ["Dr. Ricardo Mendes"], "topic": "Biomedicine", "abstract": "A novel approach to gene therapy.", "article_id_override": "art_expert_03"}),
            Action(name="CreateReviewSubmission", kwargs={"article_id": "art_expert_03", "author_user_id": "res_07", "submission_id_override": "sub_expert_03"}),
            Action(name="SetSubmissionOutcome", kwargs={"submission_id": "sub_expert_03", "new_status": "expedited_review"}),
            Action(name="IdentifyPotentialReviewers", kwargs={"article_id": "art_expert_03", "exclude_user_ids": ["res_07"]}),
            Action(name="AssignReviewer", kwargs={"submission_id": "sub_expert_03", "reviewer_user_id": "res_02"}),
            Action(name="AssignReviewer", kwargs={"submission_id": "sub_expert_03", "reviewer_user_id": "res_04"}),
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_07", "message": "Welcome! Your first submission has been received and is being fast-tracked for review."}),
            Action(name="FetchUsers", kwargs={"user_id": "res_02"}),
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_02", "message": "URGENT: You have been assigned to an expedited review for sub_expert_03."}),
            Action(name="FetchUsers", kwargs={"user_id": "res_04"}),
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_04", "message": "URGENT: You have been assigned to an expedited review for sub_expert_03."}),
            Action(name="FetchSubmissionInfo", kwargs={"submission_id": "sub_expert_03"}),
        ],
        outputs=[
            '"status": "expedited_review"'
        ]
    ),
    Task(
        annotator="0",
        user_id="second_order_citation_analysis",
        instruction="""As a scientometrics analyst, perform a 'second-order' citation analysis on the foundational paper 'Gene Editing Techniques with CRISPR-Cas9' (art_03). Identify papers that directly cite 'art_03', such as 'New Biomarkers for Early Detection...' (art_04). Then, find papers that cite 'art_04', such as 'Personalized Cancer Treatment with AI-Driven Drug Discovery' (art_14). Create a new project titled 'Gene Editing Research Lineage' (proj_lineage_01) led by Dr. Sarah Johnson (res_02) to map this influence, linking 'art_03', 'art_04', and 'art_14'. Dispatch alerts to the author of 'art_03', Dr. Sarah Johnson (res_02), with the exact message: 'Our analysis shows your paper 'art_03' has a second-order citation impact via art_04 to art_14. A project has been created to track this.'; and to the author of 'art_14', Dr. Elena Rossi (res_16), with the exact message: 'Our analysis shows your paper 'art_14' is part of a research lineage tracing back to the foundational work 'art_03'.'. Display the updated user profile for Dr. Sarah Johnson.""",
        actions=[
            Action(name="FetchArticles", kwargs={"title": "Gene Editing Techniques"}),
            Action(name="FindCitations", kwargs={"article_id": "art_03"}),
            Action(name="FetchArticles", kwargs={"article_id": "art_04"}),
            Action(name="FindCitations", kwargs={"article_id": "art_04"}),
            Action(name="FetchArticles", kwargs={"article_id": "art_14"}),
            Action(name="FetchUsers", kwargs={"name": "Dr. Sarah Johnson"}),
            Action(name="CreateNewProject", kwargs={"project_name": "Gene Editing Research Lineage", "lead_researcher_id": "res_02", "project_id_override": "proj_lineage_01"}),
            Action(name="UpdateProjectDetails", kwargs={"project_id": "proj_lineage_01", "linked_article_ids": ["art_03", "art_04", "art_14"]}),
            Action(name="FetchUsers", kwargs={"name": "Dr. Elena Rossi"}),
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_02", "message": "Our analysis shows your paper 'art_03' has a second-order citation impact via art_04 to art_14. A project has been created to track this."}),
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_16", "message": "Our analysis shows your paper 'art_14' is part of a research lineage tracing back to the foundational work 'art_03'."}),
            Action(name="FetchUsers", kwargs={"user_id": "res_02"}),
        ],
        outputs=[
            '"user_id": "res_02"'
        ]
    ),
    Task(
        annotator="0",
        user_id="curate_and_fund_new_project_from_keywords",
        instruction="""As a program director, launch a new initiative focused on 'transformer architectures'. Identify two relevant articles: 'Advances in Language Models for Code Generation' (art_01) and 'AI applications in diagnosing neurodegenerative diseases' (art_09). Create a new project titled 'Advanced Transformer Applications' (proj_transformer_01) and link these two papers to it. Assign Dr. Kenji Tanaka (res_01) as the lead for 'proj_transformer_01'. Dispatch alerts to Dr. Souza (res_01) with the exact message: 'You have been assigned as lead for the new 'Advanced Transformer Applications' project.' and to Dr. Sarah Johnson (res_02) with the exact message: 'Your paper 'AI applications in diagnosing neurodegenerative diseases' has been linked to the 'Advanced Transformer Applications' project as a key foundational article.'. Display the updated user profile for Dr. Kenji Tanaka.""", # Instrução ajustada: removida a parte de "fund", ajustada a co-liderança para um único líder formal, e ajustada a mensagem para Dr. Mendes.
        actions=[
            Action(name="FetchArticles", kwargs={"title": "Advances in Language Models for Code Generation"}), # Título completo
            Action(name="FetchArticles", kwargs={"title": "AI applications in diagnosing neurodegenerative diseases"}), # Título completo
            # Action(name="FetchArticles", kwargs={"topic": "AI"}), # Removida chamada extrânea
            Action(name="FetchUsers", kwargs={"name": "Dr. Kenji Tanaka"}),
            Action(name="CreateNewProject", kwargs={"project_name": "Advanced Transformer Applications", "lead_researcher_id": "res_01", "project_id_override": "proj_transformer_01"}),
            Action(name="UpdateProjectDetails", kwargs={"project_id": "proj_transformer_01", "linked_article_ids": ["art_01", "art_09"]}), # Corrigido linked_articles_ids para linked_articles
            Action(name="FetchUsers", kwargs={"name": "Dr. Sarah Johnson"}),
            # Action(name="UpdateProjectDetails", kwargs={"project_id": "proj_transformer_01", "lead_researcher_id": ["res_01", "res_02"]}), # Removida tentativa de co-liderança não suportada
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_01", "message": "You have been assigned as lead for the new 'Advanced Transformer Applications' project."}),
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_02", "message": "Your paper 'AI applications in diagnosing neurodegenerative diseases' has been linked to the 'Advanced Transformer Applications' project as a key foundational article."}),
            Action(name="FetchUsers", kwargs={"user_id": "res_01"}),
        ],
        outputs=[
            '"user_id": "res_01"',
        ]
    ),
    Task(
        annotator="0",
        user_id="comprehensive_integrity_audit_and_remediation",
        instruction="""As an ethics officer, address an integrity alert for the submission of 'Limits of Quantum Computing...' (art_02 / sub_01), alleging high keyword overlap with 'Advances in Language Models...' (art_01). Verify the keyword overlap between 'art_02' and 'art_01'. If the overlap is significant, set the submission status to 'on_hold_integrity_check'. Dispatch an alert to the author, Prof. James Wilson (res_03), with the exact message: 'Your submission 'sub_01' is on hold pending an integrity review due to content overlap concerns.'. Concurrently, dispatch an alert to the reviewer, Dr. Kenji Tanaka (res_01), with the exact message: 'The review for submission 'sub_01' has been temporarily paused pending an integrity check.'. Require the author to submit a revised version by linking 'Revised: Limits of Quantum Computing' (art_07) to the submission. Update the abstract of the original article 'art_02' to: 'This version has been updated to properly attribute and differentiate from prior work in related fields.'. Finally, update the submission status back to 'under_review' to restart the process. Display the updated submission details.""",
        actions=[
            Action(name="FetchSubmissionInfo", kwargs={"article_id": "art_02"}),
            Action(name="GetArticleKeywords", kwargs={"article_id": "art_02"}),
            Action(name="FetchArticles", kwargs={"title": "Advances in Language Models"}),
            Action(name="GetArticleKeywords", kwargs={"article_id": "art_01"}),
            Action(name="SetSubmissionOutcome", kwargs={"submission_id": "sub_01", "new_status": "on_hold_integrity_check"}),
            Action(name="FetchUsers", kwargs={"name": "Prof. James Wilson"}),
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_03", "message": "Your submission 'sub_01' is on hold pending an integrity review due to content overlap concerns."}),
            Action(name="FetchUsers", kwargs={"user_id": "res_01"}),
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_01", "message": "The review for submission 'sub_01' has been temporarily paused pending an integrity check."}),
            Action(name="FetchArticles", kwargs={"title": "Revised: Limits of Quantum Computing"}),
            Action(name="ConnectRevisedVersion", kwargs={"submission_id": "sub_01", "revised_article_id": "art_07"}),
            Action(name="ReviseArticleDetails", kwargs={"article_id": "art_02", "abstract": "This version has been updated to properly attribute and differentiate from prior work in related fields."}),
            Action(name="SetSubmissionOutcome", kwargs={"submission_id": "sub_01", "new_status": "under_review"}),
            Action(name="FetchSubmissionInfo", kwargs={"submission_id": "sub_01"}),
        ],
        outputs=[
            '"status": "under_review"',
            '"revised_version_article_id": "art_07"'
        ]
    ),
    Task(
        annotator="0",
        user_id="revitalize_legacy_research_with_new_team",
        instruction="""As a program director, revitalize legacy research by creating a new project titled 'Next-Generation Gene Therapies' (proj_expert_02) based on 'Gene Editing Techniques with CRISPR-Cas9' (art_03). Appoint Dr. Thomas Anderson (res_04), an available researcher from a different institution than Dr. Sarah Johnson (res_02), as the new lead for 'proj_expert_02'. Link both 'art_03' and a recent, relevant paper, 'CRISPR-Cas12 Evolution for Enhanced Precision' (art_11), to the new project. Dispatch an alert to Dr. Bauer (res_04) with the exact message: 'You have been assigned to lead the new 'Next-Generation Gene Therapies' project, building on the work of Dr. Mendes.'. Concurrently, dispatch an alert to Dr. Mendes (res_02) with the exact message: 'Your foundational work on art_03 is being used as the basis for a new initiative, 'Next-Generation Gene Therapies'.'. Display the updated user profile for Dr. Sarah Johnson.""", # Removida a parte de notificação channel da instrução para res_04
        actions=[
            Action(name="FetchArticles", kwargs={"title": "Gene Editing Techniques with CRISPR-Cas9"}), # Título completo
            Action(name="FetchUsers", kwargs={"name": "Dr. Sarah Johnson"}),
            Action(name="FetchUsers", kwargs={"name": "Dr. Thomas Anderson"}),
            Action(name="CreateNewProject", kwargs={"project_name": "Next-Generation Gene Therapies", "lead_researcher_id": "res_04", "project_id_override": "proj_expert_02"}),
            Action(name="UpdateProjectDetails", kwargs={"project_id": "proj_expert_02", "linked_article_ids": ["art_03"]}),
            Action(name="FetchArticles", kwargs={"title": "CRISPR-Cas12 Evolution for Enhanced Precision"}), # Título completo
            Action(name="UpdateProjectDetails", kwargs={"project_id": "proj_expert_02", "linked_article_ids": ["art_03", "art_11"]}),
            # Removida a ação adjust_user_settings para notification_channel para res_04, pois não estava na instrução
            # Action(name="AdjustUserSettings", kwargs={"user_id": "res_04", "notification_channel": "email"}),
            Action(name="SetTopicInterest", kwargs={"user_id": "res_04", "topic": "Biology", "action": "add"}), # Mantida essa ação, pois é uma preferência de interesse do usuário.
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_04", "message": "You have been assigned to lead the new 'Next-Generation Gene Therapies' project, building on the work of Dr. Mendes."}),
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_02", "message": "Your foundational work on art_03 is being used as the basis for a new initiative, 'Next-Generation Gene Therapies'."}),
            Action(name="FetchUsers", kwargs={"user_id": "res_02"}),
        ],
        outputs=[
            '"user_id": "res_02"'
        ]
    ),
    Task(
        annotator="0",
        user_id="full_cleanup_after_invalid_submission",
        instruction="""As an admin, fully clean up records associated with the invalid submission of 'AI in Algorithmic Trading' (art_expert_04 / sub_expert_04), as it was submitted by an unregistered author (Dr. Elena Rossi - res_16). First, register 'art_expert_04' with the abstract: 'A study on AI applications in high-frequency trading.', and create 'sub_expert_04' to simulate the invalid entry. Then, delete 'sub_expert_04' and update 'art_expert_04's status to 'archived_invalid_submission'. Create default user settings for Dr. Elena Rossi (res_16) with 'email' notifications and a 'light' UI theme, and subscribe him to the 'AI' topic. Finally, dispatch an alert to Dr. Silva (res_16) with the exact message: 'Your recent submission for 'AI in Algorithmic Trading' was invalid and has been removed. Please resubmit through the proper channels. A user profile has been created for you.'. Display the final article details for 'art_expert_04'.""", # Abstract adicionado à instrução
        actions=[
            Action(name="RegisterNewArticle", kwargs={"title": "AI in Algorithmic Trading", "authors": ["Dr. Elena Rossi"], "topic": "AI", "abstract": "A study on AI applications in high-frequency trading.", "article_id_override": "art_expert_04"}),
            Action(name="CreateReviewSubmission", kwargs={"article_id": "art_expert_04", "author_user_id": "res_16", "submission_id_override": "sub_expert_04"}),
            Action(name="FetchSubmissionInfo", kwargs={"submission_id": "sub_expert_04"}),
            Action(name="SetSubmissionOutcome", kwargs={"submission_id": "sub_expert_04", "new_status": "deleted"}),
            Action(name="ReviseArticleDetails", kwargs={"article_id": "art_expert_04", "status": "archived_invalid_submission"}),
            Action(name="FetchUsers", kwargs={"name": "Dr. Elena Rossi"}),
            Action(name="AdjustUserSettings", kwargs={"user_id": "res_16", "notification_channel": "email", "ui_theme": "light"}),
            Action(name="SetTopicInterest", kwargs={"user_id": "res_16", "topic": "AI", "action": "add"}),
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_16", "message": "Your recent submission for 'AI in Algorithmic Trading' was invalid and has been removed. Please resubmit through the proper channels. A user profile has been created for you."}),
            Action(name="FetchArticles", kwargs={"article_id": "art_expert_04"}),
        ],
        outputs=[
            '"article_id": "art_expert_04"',
            '"status": "archived_invalid_submission"'
        ]
    ),
    Task(
        annotator="0",
        user_id="comprehensive_article_lifecycle_management",
        instruction="""As a senior editor, manage the full lifecycle of a new submission. First, register a new article 'The Future of Quantum Machine Learning' (art_QM_01) by Dr. Kenji Tanaka (res_01) on 'Quantum Physics', with the abstract: 'This paper explores advanced algorithms for quantum machine learning and their potential applications.'. Create a submission for it (sub_QM_01). Assign two reviewers: Dr. Wei Zhang (res_03) and Dr. Anna Petrov (res_06). After initial reviews (simulate 'minor_revisions' from res_03, comment: 'Good work, minor clarity issues.'; and 'major_revisions' from res_06, comment: 'Requires substantial rewrite of methodology section.'), set the submission status to 'revisions_requested'. Alert Dr. Kenji Tanaka (res_01) with the message: 'Your submission for 'The Future of Quantum Machine Learning' requires revisions. Please review the feedback.'. Assume a revised version is submitted, titled 'Revised: Quantum ML Algorithms' (art_QM_01_rev) with abstract: 'An improved analysis of quantum machine learning algorithms, addressing reviewer feedback.'. Connect this revised version to sub_QM_01. Assign Dr. Sarah Johnson (res_02) as an additional reviewer for the revised version. Finally, post a new 'accept' review from Dr. Mendes (res_02, comment: 'The revisions fully address all concerns.'). Set the final outcome to 'accepted'. Display the final submission details.""",
        actions=[
            Action(name="FetchUsers", kwargs={"user_id": "res_01"}), # Edge 1 (from prompt)
            Action(name="RegisterNewArticle", kwargs={"title": "The Future of Quantum Machine Learning", "authors": ["Dr. Kenji Tanaka"], "topic": "Quantum Physics", "abstract": "This paper explores advanced algorithms for quantum machine learning and their potential applications.", "article_id_override": "art_QM_01"}), # Edge 2 (from prompt)
            Action(name="CreateReviewSubmission", kwargs={"article_id": "art_QM_01", "author_user_id": "res_01", "submission_id_override": "sub_QM_01"}), # Edge 3 (from prompt)
            Action(name="FetchUsers", kwargs={"user_id": "res_03"}), # Edge 4 (from prompt)
            Action(name="FetchUsers", kwargs={"user_id": "res_06"}), # Edge 5 (from prompt)
            Action(name="AssignReviewer", kwargs={"submission_id": "sub_QM_01", "reviewer_user_id": "res_03"}), # Edge 6 (from prior action)
            Action(name="AssignReviewer", kwargs={"submission_id": "sub_QM_01", "reviewer_user_id": "res_06"}), # Edge 7 (from prior action)
            Action(name="PostNewReview", kwargs={"submission_id": "sub_QM_01", "reviewer_user_id": "res_03", "recommendation": "minor_revisions", "comments": "Good work, minor clarity issues."}), # Edge 8 (from prior action)
            Action(name="PostNewReview", kwargs={"submission_id": "sub_QM_01", "reviewer_user_id": "res_06", "recommendation": "major_revisions", "comments": "Requires substantial rewrite of methodology section."}), # Edge 9 (from prior action)
            Action(name="SetSubmissionOutcome", kwargs={"submission_id": "sub_QM_01", "new_status": "revisions_requested"}), # Edge 10 (from prior action)
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_01", "message": "Your submission for 'The Future of Quantum Machine Learning' requires revisions. Please review the feedback."}), # Edge 11 (from prompt)
            Action(name="RegisterNewArticle", kwargs={"title": "Revised: Quantum ML Algorithms", "authors": ["Dr. Kenji Tanaka"], "topic": "Quantum Physics", "abstract": "An improved analysis of quantum machine learning algorithms, addressing reviewer feedback.", "article_id_override": "art_QM_01_rev"}), # Edge 12 (from prompt)
            Action(name="ConnectRevisedVersion", kwargs={"submission_id": "sub_QM_01", "revised_article_id": "art_QM_01_rev"}), # Edge 13 (from prior actions)
            Action(name="FetchUsers", kwargs={"user_id": "res_02"}), # Edge 14 (from prompt)
            Action(name="AssignReviewer", kwargs={"submission_id": "sub_QM_01", "reviewer_user_id": "res_02"}), # Edge 15 (from prior actions)
            Action(name="PostNewReview", kwargs={"submission_id": "sub_QM_01", "reviewer_user_id": "res_02", "recommendation": "accept", "comments": "The revisions fully address all concerns."}), # Edge 16 (from prior actions)
            Action(name="SetSubmissionOutcome", kwargs={"submission_id": "sub_QM_01", "new_status": "accepted"}), # Edge 17 (from prior action)
            Action(name="FetchSubmissionInfo", kwargs={"submission_id": "sub_QM_01"}) # Edge 18 (from prior action)
        ],
        outputs=[
            '"submission_id": "sub_QM_01"',
            '"status": "accepted"',
            '"revised_version_article_id": "art_QM_01_rev"'
        ]
    ),
    Task(
        annotator="0",
        user_id="advanced_project_lifecycle",
        instruction="""As a research program manager, initiate a new project focusing on 'AI Ethics in Healthcare'. Identify 'Personalized Cancer Treatment with AI-Driven Drug Discovery' (art_14) as a foundational paper. Retrieve its keywords. Find all articles that cite 'art_14'. Create a new project named 'AI Ethics in Healthcare Research' (proj_AI_Ethics_01) led by Dr. Sarah Johnson (res_02), linking 'art_14'. Set the project status to 'active'. Display the final project details, including linked articles and status.""",
        actions=[
            Action(name="FetchUsers", kwargs={"name": "Dr. Sarah Johnson"}),
            Action(name="FetchArticles", kwargs={"article_id": "art_14"}),
            Action(name="GetArticleKeywords", kwargs={"article_id": "art_14"}),
            Action(name="FindCitations", kwargs={"article_id": "art_14"}), # This returns [] based on citations.json
            Action(name="CreateNewProject", kwargs={"project_name": "AI Ethics in Healthcare Research", "lead_researcher_id": "res_02", "project_id_override": "proj_AI_Ethics_01"}),
            Action(name="UpdateProjectDetails", kwargs={"project_id": "proj_AI_Ethics_01", "linked_article_ids": ["art_14"]}), # Only art_14 is linked as no citing articles are found
            Action(name="UpdateProjectDetails", kwargs={"project_id": "proj_AI_Ethics_01", "status": "active"}),
            Action(name="FetchArticles", kwargs={"article_id": "art_14"}),
            Action(name="FetchUsers", kwargs={"user_id": "res_02"}),
            Action(name="FetchArticles", kwargs={"title": "AI Ethics in Healthcare Research"})
        ],
        outputs=[
            '"project_name": "AI Ethics in Healthcare Research"',
            '"status": "active"',
            '"linked_articles": [\n    "art_14"\n  ]'
        ]
    ),
    Task(
        annotator="0",
        user_id="author_profile_and_impact_analysis",
        instruction="""As a research assistant, help Dr. Thomas Anderson (res_04) enhance her professional profile and understand the impact of her work. Adjust her UI theme to 'light' and ensure she receives 'email' notifications. Remove any existing 'Biomedicine' topic subscriptions she might have, then add a new subscription to 'AI Ethics' (assuming this is a new sub-topic in the system). Find all articles that cite her foundational paper 'New Biomarkers for Early Detection of Neurodegenerative Diseases' (art_04). For each citing article, retrieve its keywords. Create a project titled 'Biomarker Impact Analysis' (proj_impact_bau) led by Dr. Bauer, and link 'art_04' and all identified citing articles to it. Finally, display Dr. Thomas Anderson's updated user profile.""",
        actions=[
            Action(name="FetchUsers", kwargs={"user_id": "res_04"}),
            Action(name="AdjustUserSettings", kwargs={"user_id": "res_04", "ui_theme": "light", "notification_channel": "email"}),
            Action(name="SetTopicInterest", kwargs={"user_id": "res_04", "topic": "Biomedicine", "action": "remove"}),
            Action(name="SetTopicInterest", kwargs={"user_id": "res_04", "topic": "AI Ethics", "action": "add"}),
            Action(name="FetchArticles", kwargs={"article_id": "art_04"}),
            Action(name="FindCitations", kwargs={"article_id": "art_04"}), # This returns ["art_14"]
            Action(name="FetchArticles", kwargs={"article_id": "art_14"}), # Fetching the actual citing article art_14
            Action(name="GetArticleKeywords", kwargs={"article_id": "art_14"}), # Get keywords for art_14
            Action(name="CreateNewProject", kwargs={"project_name": "Biomarker Impact Analysis", "lead_researcher_id": "res_04", "project_id_override": "proj_impact_bau"}),
            Action(name="UpdateProjectDetails", kwargs={"project_id": "proj_impact_bau", "linked_article_ids": ["art_04", "art_14"]}), # Linking art_04 and its citing article art_14
            Action(name="FetchUsers", kwargs={"user_id": "res_04"})
        ],
        outputs=[
            '"user_id": "res_04"',
            '"notification_channel": "email"',
            '"ui_theme": "light"'
        ]
    ),
    Task(
        annotator="0",
        user_id="post_acceptance_project_creation",
        instruction="""As an administrator, finalize the acceptance of 'Gene Editing Techniques with CRISPR-Cas9' (art_03) and create a project for it. Set the outcome of its submission (sub_06) to 'accepted'. Dispatch an alert to the author, Dr. Sarah Johnson (res_02), with the exact message: 'Congratulations, your paper 'Gene Editing Techniques with CRISPR-Cas9' has been accepted for publication.'. Create a new research project titled 'CRISPR-Cas9 Therapeutic Applications' led by Dr. Mendes (res_02) and link 'art_03'. Concurrently, dispatch another alert to Dr. Mendes (res_02) with the exact message: 'A new project, 'CRISPR-Cas9 Therapeutic Applications', has been created to track your work related to your recent publication.'. Display the details of 'art_03' to confirm.""",
        actions=[
            Action(name="FetchArticles", kwargs={"article_id": "art_03"}), # Adicionado para verificar a existência do artigo
            Action(name="CreateReviewSubmission", kwargs={"article_id": "art_03", "author_user_id": "res_02", "submission_id_override": "sub_06"}),
            Action(name="FetchSubmissionInfo", kwargs={"article_id": "art_03"}),
            Action(name="SetSubmissionOutcome", kwargs={"submission_id": "sub_06", "new_status": "accepted"}),
            Action(name="FetchUsers", kwargs={"name": "Dr. Sarah Johnson"}),
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_02", "message": "Congratulations, your paper 'Gene Editing Techniques with CRISPR-Cas9' has been accepted for publication."}),
            Action(name="CreateNewProject", kwargs={"project_name": "CRISPR-Cas9 Therapeutic Applications", "lead_researcher_id": "res_02", "linked_article_ids": ["art_03"]}),
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_02", "message": "A new project, 'CRISPR-Cas9 Therapeutic Applications', has been created to track your work related to your recent publication."}),
            Action(name="FetchArticles", kwargs={"title": "Gene Editing Techniques with CRISPR-Cas9"})
        ],
        outputs=[
            '"article_id": "art_03"',
            '"title": "Gene Editing Techniques with CRISPR-Cas9"'
        ]
    ),
    Task(
        annotator="0",
        user_id="reviewer_reassignment_after_decline",
        instruction="""As a managing editor, manage the reassignment of a reviewer for the submission 'Personalized Cancer Treatment...' (art_14 / sub_05) after a previous reviewer declined. Identify a new, available 'Biomedicine' expert (res_13), excluding the authors (Dr. Sarah Johnson - res_02, Dr. Thomas Anderson - res_04, Dr. Elena Rossi - res_16) and the declining reviewer, and assign them to the submission, overwriting the previous assignment. Dispatch an alert to the newly assigned reviewer (res_13) with the exact message: 'You have been assigned to review submission sub_05, as the original reviewer was unavailable. Your time is appreciated.'. Display the updated submission details.""",
        actions=[
            Action(name="FetchSubmissionInfo", kwargs={"article_id": "art_14"}),
            Action(name="FetchArticles", kwargs={"article_id": "art_14"}),
            # Os IDs dos autores (res_02, res_04, res_16) são agora explicitamente mencionados na instrução,
            # tornando sua derivação determinística.
            Action(name="IdentifyPotentialReviewers", kwargs={"article_id": "art_14", "exclude_user_ids": ["res_02", "res_04", "res_16"]}),
            Action(name="FetchUsers", kwargs={"user_id": "res_13"}),
            Action(name="AssignReviewer", kwargs={"submission_id": "sub_05", "reviewer_user_id": "res_13", "overwrite": True}),
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_13", "message": "You have been assigned to review submission sub_05, as the original reviewer was unavailable. Your time is appreciated."}),
            Action(name="FetchSubmissionInfo", kwargs={"submission_id": "sub_05"}),
        ],
        outputs=[
            '"submission_id": "sub_05"',
            '"assigned_reviewers": [\n    "res_13"\n  ]'
        ]
    ),
    Task(
        annotator="0",
        user_id="fast_track_review_and_profile_management",
        instruction="""As editor-in-chief, fast-track the submission for 'Federated Learning for Privacy-Preserving AI' (art_06). Create a new submission record for it (sub_art_06) and update its status to 'expedited_review'. Assign Dr. Kenji Tanaka (res_01), an AI expert not Dr. Anna Petrov (res_06), as the reviewer. Adjust Dr. Souza's user settings to receive 'email' notifications. Finally, dispatch alerts to Dr. Khan (res_06) with the exact message: 'Your paper 'Federated Learning...' has been selected for an expedited review.' and to Dr. Souza (res_01) with the exact message: 'URGENT: You have been assigned to an expedited review for submission sub_art_06. Please prioritize.'. Display the final submission details.""",
        actions=[
            Action(name="FetchArticles", kwargs={"title": "Federated Learning for Privacy-Preserving AI"}), # Título completo, verifica existência de art_06
            Action(name="CreateReviewSubmission", kwargs={"article_id": "art_06", "author_user_id": "res_06", "submission_id_override": "sub_art_06"}), # Cria a SUBMISSÃO ALVO sub_art_06 para art_06
            Action(name="SetSubmissionOutcome", kwargs={"submission_id": "sub_art_06", "new_status": "expedited_review"}), # Define status para a submissão ALVO
            Action(name="FetchUsers", kwargs={"name": "Dr. Anna Petrov"}), # Busca autor (res_06)
            Action(name="FetchUsers", kwargs={"name": "Dr. Kenji Tanaka"}), # Busca revisor (res_01)
            Action(name="AdjustUserSettings", kwargs={"user_id": "res_01", "notification_channel": "email"}),
            Action(name="AssignReviewer", kwargs={"submission_id": "sub_art_06", "reviewer_user_id": "res_01"}), # Atribui revisor à submissão ALVO
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_06", "message": "Your paper 'Federated Learning...' has been selected for an expedited review."}),
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_01", "message": "URGENT: You have been assigned to an expedited review for submission sub_art_06. Please prioritize."}),
            Action(name="FetchSubmissionInfo", kwargs={"submission_id": "sub_art_06"}), # Busca informações da submissão ALVO para output
        ],
        outputs=[
            '"status": "expedited_review"',
            '"assigned_reviewers": [\n    "res_01"\n  ]'
        ]
    ),
    Task(
        annotator="0",
        user_id="special_issue_editor",
        instruction="""As a special issue editor for 'AI in Medical Imaging', onboard a new manuscript: 'Advanced Deep Learning for Diagnostic Accuracy' (art_DL_01) authored by Dr. Helena Souza (res_14) and Dr. Maria Santos (res_09). The article is on 'AI' with the abstract: 'This paper proposes novel deep learning architectures to improve diagnostic accuracy in medical imaging, focusing on explainability.'. Create a submission for it (sub_DL_01). Adjust Dr. Helena Souza's (res_14) user settings to receive 'in_app' notifications and set her UI theme to 'dark'. Assign two expert reviewers: Dr. Kenji Tanaka (res_01) and Dr. Anna Petrov (res_06), ensuring they are AI experts. Create a new project titled 'Medical Imaging AI Advances' (proj_DL_01) led by Dr. Maria Santos (res_09), linking 'art_DL_01' to it. Dispatch an alert to Dr. Helena Souza (res_14) with the exact message: 'Your submission for 'Advanced Deep Learning for Diagnostic Accuracy' has been received and is now under review for the Special Issue.'. Display the final submission details.""",
        actions=[
            Action(name="FetchUsers", kwargs={"name": "Dr. Helena Souza"}), # Edge 1 (from prompt)
            Action(name="FetchUsers", kwargs={"name": "Dr. Maria Santos"}), # Edge 2 (from prompt)
            Action(name="RegisterNewArticle", kwargs={"title": "Advanced Deep Learning for Diagnostic Accuracy", "authors": ["Dr. Helena Souza", "Dr. Maria Santos"], "topic": "AI", "abstract": "This paper proposes novel deep learning architectures to improve diagnostic accuracy in medical imaging, focusing on explainability.", "article_id_override": "art_DL_01"}), # Edge 3 (from prompt)
            Action(name="CreateReviewSubmission", kwargs={"article_id": "art_DL_01", "author_user_id": "res_14", "submission_id_override": "sub_DL_01"}), # Edge 4 (from prompt)
            Action(name="AdjustUserSettings", kwargs={"user_id": "res_14", "notification_channel": "in_app", "ui_theme": "dark"}), # Edge 5 (from prompt)
            Action(name="FetchArticles", kwargs={"article_id": "art_DL_01"}), # Edge 6 (from prior action, to get topic for reviewer identification)
            Action(name="IdentifyPotentialReviewers", kwargs={"article_id": "art_DL_01", "exclude_user_ids": ["res_14", "res_09"]}), # Edge 7 (from prior action and prompt - exclude authors)
            Action(name="FetchUsers", kwargs={"name": "Dr. Kenji Tanaka"}), # Edge 8 (from prompt)
            Action(name="FetchUsers", kwargs={"name": "Dr. Anna Petrov"}), # Edge 9 (from prompt)
            Action(name="AssignReviewer", kwargs={"submission_id": "sub_DL_01", "reviewer_user_id": "res_01"}), # Edge 10 (from prior action)
            Action(name="AssignReviewer", kwargs={"submission_id": "sub_DL_01", "reviewer_user_id": "res_06"}), # Edge 11 (from prior action)
            Action(name="FetchUsers", kwargs={"user_id": "res_09"}), # Edge 12 (from prompt, for project lead)
            Action(name="CreateNewProject", kwargs={"project_name": "Medical Imaging AI Advances", "lead_researcher_id": "res_09", "linked_article_ids": ["art_DL_01"], "project_id_override": "proj_DL_01"}), # Edge 13 (from prompt, and prior action for art_DL_01)
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_14", "message": "Your submission for 'Advanced Deep Learning for Diagnostic Accuracy' has been received and is now under review for the Special Issue."}), # Edge 14 (from prompt)
            Action(name="FetchSubmissionInfo", kwargs={"submission_id": "sub_DL_01"}), # Edge 15 (from prior action)
            Action(name="FetchArticles", kwargs={"article_id": "art_DL_01"}), # Edge 16 (confirm article details for output)
            Action(name="FetchUsers", kwargs={"user_id": "res_09"}), # Edge 17 (confirm project lead details for output)
            Action(name="FetchArticles", kwargs={"title": "Medical Imaging AI Advances"}) # Edge 18 (confirm project details for output, assuming project can be fetched by title)
        ],
        outputs=[
            '"submission_id": "sub_DL_01"',
            '"status": "under_review"',
            '"assigned_reviewers": [\n    "res_01",\n    "res_06"\n  ]'
        ]
    ),
    Task(
        annotator="0",
        user_id="complex_submission_workflow",
        instruction="""As editor-in-chief, manage the full lifecycle of a new submission: 'Quantum Computing Algorithms for Optimization' (art_QC_01) by Dr. Thomas Anderson (res_04). The article is on 'Quantum Computing' with the abstract: 'This paper explores novel quantum algorithms for solving complex optimization problems.'. First, register the article and create a submission (sub_QC_01). Assign Dr. Sarah Johnson (res_02) and Dr. Liu Wei (res_05) as initial reviewers, ensuring they are experts in 'Quantum Computing'. Simulate their reviews: Dr. Mendes gives 'minor_revisions' ('Good work, needs minor clarity improvements.') and Dr. Tanaka gives 'major_revisions' ('Significant improvements needed on methodology.'). Based on these, set the submission status to 'revisions_requested'. Dr. Bauer then submits revisions, updating the article's abstract to: 'This revised paper presents enhanced quantum algorithms for optimization, with improved clarity and methodological rigor.'. After revisions, reset the review panel to include only Dr. Sarah Johnson (res_02) as the primary reviewer, and then add Dr. Helena Souza (res_14) as a new reviewer. Simulate Dr. Mendes' new review as 'accept' ('Revisions addressed, ready for publication.') and Dr. Rossi's as 'accept' ('Excellent paper, clear and robust.'). Finally, set the submission status to 'accepted'. Create a new project titled 'Quantum Algorithms Research' (proj_QC_01) led by Dr. Thomas Anderson (res_04), linking 'art_QC_01' to it. Dispatch an alert to Dr. Thomas Anderson (res_04) with the exact message: 'Your submission 'Quantum Computing Algorithms for Optimization' has been accepted! Congratulations!'. Display the final submission details.""", # Instrução ajustada para justificar o reset do painel de revisão
        actions=[
            # 1. Register new article
            Action(name="RegisterNewArticle", kwargs={"title": "Quantum Computing Algorithms for Optimization", "authors": ["Dr. Thomas Anderson"], "topic": "Quantum Computing", "abstract": "This paper explores novel quantum algorithms for solving complex optimization problems.", "article_id_override": "art_QC_01"}),

            # 2. Create submission
            Action(name="CreateReviewSubmission", kwargs={"article_id": "art_QC_01", "author_user_id": "res_04", "submission_id_override": "sub_QC_01"}),

            # 3. Identify and assign initial reviewers
            Action(name="FetchArticles", kwargs={"article_id": "art_QC_01"}),
            Action(name="IdentifyPotentialReviewers", kwargs={"article_id": "art_QC_01", "exclude_user_ids": ["res_04"]}),
            Action(name="FetchUsers", kwargs={"name": "Dr. Sarah Johnson"}),
            Action(name="FetchUsers", kwargs={"name": "Dr. Liu Wei"}),
            Action(name="AssignReviewer", kwargs={"submission_id": "sub_QC_01", "reviewer_user_id": "res_02"}), # Adiciona Mendes (default overwrite=False)
            Action(name="AssignReviewer", kwargs={"submission_id": "sub_QC_01", "reviewer_user_id": "res_05"}), # Adiciona Tanaka (default overwrite=False)

            # 4. Simulate initial reviews
            Action(name="PostNewReview", kwargs={"submission_id": "sub_QC_01", "reviewer_user_id": "res_02", "recommendation": "minor_revisions", "comments": "Good work, needs minor clarity improvements."}),
            Action(name="PostNewReview", kwargs={"submission_id": "sub_QC_01", "reviewer_user_id": "res_05", "recommendation": "major_revisions", "comments": "Significant improvements needed on methodology."}),

            # 5. Set status to revisions_requested
            Action(name="SetSubmissionOutcome", kwargs={"submission_id": "sub_QC_01", "new_status": "revisions_requested"}),

            # 6. Author submits revisions (update article abstract)
            Action(name="ReviseArticleDetails", kwargs={"article_id": "art_QC_01", "abstract": "This revised paper presents enhanced quantum algorithms for optimization, with improved clarity and methodological rigor."}),

            # 7. Re-assign reviewers (reset panel to Mendes, then add Rossi)
            Action(name="AssignReviewer", kwargs={"submission_id": "sub_QC_01", "reviewer_user_id": "res_02", "overwrite": True}), # Justificado pela instrução: "reset the review panel to include only Dr. Sarah Johnson"
            Action(name="FetchUsers", kwargs={"name": "Dr. Helena Souza"}),
            Action(name="AssignReviewer", kwargs={"submission_id": "sub_QC_01", "reviewer_user_id": "res_14"}), # Adiciona Rossi (default overwrite=False)

            # 8. Simulate new reviews
            Action(name="PostNewReview", kwargs={"submission_id": "sub_QC_01", "reviewer_user_id": "res_02", "recommendation": "accept", "comments": "Revisions addressed, ready for publication."}),
            Action(name="PostNewReview", kwargs={"submission_id": "sub_QC_01", "reviewer_user_id": "res_14", "recommendation": "accept", "comments": "Excellent paper, clear and robust."}),

            # 9. Set final status to accepted
            Action(name="SetSubmissionOutcome", kwargs={"submission_id": "sub_QC_01", "new_status": "accepted"}),

            # 10. Create new project and link article
            Action(name="FetchUsers", kwargs={"user_id": "res_04"}),
            Action(name="CreateNewProject", kwargs={"project_name": "Quantum Algorithms Research", "lead_researcher_id": "res_04", "linked_article_ids": ["art_QC_01"], "project_id_override": "proj_QC_01"}),

            # 11. Dispatch alert to author
            Action(name="AlertUser", kwargs={"recipient_user_id": "res_04", "message": "Your submission 'Quantum Computing Algorithms for Optimization' has been accepted! Congratulations!"}),

            # 12. Display final submission details
            Action(name="FetchSubmissionInfo", kwargs={"submission_id": "sub_QC_01"}),
        ],
        outputs=[
            '"submission_id": "sub_QC_01"',
            '"status": "accepted"',
            '"assigned_reviewers": [\n    "res_02",\n    "res_14"\n  ]'
        ]
    )
]
