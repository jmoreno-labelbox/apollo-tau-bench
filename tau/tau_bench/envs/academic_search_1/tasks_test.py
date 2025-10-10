from tau_bench.types import Action, Task

TASKS = [
    Task(
        annotator="0",
        user_id="cross_disciplinary_impact_audit",
        instruction="""Conduct National Science Foundation audit to verify the cross-disciplinary impact of the 'Quantum Computing Applications' project. Success is defined as confirming that a core article from this project has been cited by a researcher from a different research field. To ensure a deterministic audit, you must analyze the citation whose citing paper has the most recent publication year. If impact is confirmed, create a structured log entry for the project's lead researcher with the override ID 'log_audit_impact_02'. The note must follow the format: 'IMPACT_AUDIT: Confirmed. Your work was cited by an author in the [Citing Author's Field] field.'. If the citation is from the same field or no citations exist, the note must state: 'IMPACT_AUDIT: No new cross-disciplinary impact found in latest citation.'. As final confirmation, return the content of the log entry you created.""",
        actions=[
            Action(name="SearchProjects", kwargs={"project_name": "Quantum Computing Applications"}),
            Action(name="SearchCitations", kwargs={"article_id": "art_02", "direction": "to"}),
            Action(name="GetCitationDetails", kwargs={"citation_id": "cit_01"}),
            Action(name="SearchArticles", kwargs={"article_id": "art_01"}),
            Action(name="GetCitationDetails", kwargs={"citation_id": "cit_03"}),
            Action(name="SearchArticles", kwargs={"article_id": "art_05"}),
            Action(name="SearchUsers", kwargs={"name": "Dr. Ricardo Mendes"}),
            Action(name="SearchUsers", kwargs={"user_id": "res_03"}),
            Action(name="CreateLogEntry", kwargs={
                "user_id": "res_03",
                "notes": "IMPACT_AUDIT: Confirmed. Your work was cited by an author in the Artificial Intelligence field.",
                "log_id_override": "log_audit_impact_02"
            }),
            Action(name="GetLogDetails", kwargs={"log_id": "log_audit_impact_02"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="funding_and_citation_audit",
        instruction="""Perform grant administration duties by auditing and updating the status of the most recently started project funded by the 'National Science Foundation'. The project's status should be set to 'impact_verified' if, and only if, its primary linked article (the first in its list) has been cited by a work from the 'Artificial Intelligence' field. To ensure a consistent audit, your analysis must be based on the citation whose citing article has the most recent publication year. If the criteria are not met, set the project's status to 'impact_audit_failed'. As final confirmation, return the project's new status.""",
        actions=[
            Action(name="SearchFundingSources", kwargs={"source_name": "National Science Foundation"}),
            Action(name="SearchProjects", kwargs={"funding_source_id": "fs_02"}),
            Action(name="GetProjectDetails", kwargs={"project_id": "proj_01"}),
            Action(name="SearchCitations", kwargs={"article_id": "art_02", "direction": "to"}),
            Action(name="SearchArticles", kwargs={"article_id": "art_01"}),
            Action(name="SearchArticles", kwargs={"article_id": "art_05"}),
            Action(name="SearchUsers", kwargs={"name": "Dr. Ricardo Mendes"}),
            Action(name="UpdateProjectStatus", kwargs={"project_id": "proj_01", "new_status": "impact_verified"}),
            Action(name="GetProjectDetails", kwargs={"project_id": "proj_01"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="resolve_unassigned_submission",
        instruction="""Handle submissions management by ensuring the submission for 'New Biomarkers for Early Detection of Neurodegenerative Diseases' is fully staffed with two qualified reviewers and its status updated to 'under_review'. The primary reviewer must be the user named 'Dr. Ricardo Mendes'. The secondary reviewer must be an expert from the 'Biomedicine' field (who is not the author or primary reviewer) with the lightest current workload, defined as the one with the fewest articles in their personal log. After assigning both reviewers, you must log this action for your own records (as Dr. Ricardo Mendes) using the override ID 'log_staffing_01' and the format: 'STAFFING: Submission [Submission ID] assigned to primary:[Primary Reviewer ID] and secondary:[Secondary Reviewer ID].'. As final confirmation, return the submission's updated list of assigned reviewers.""",
        actions=[
            Action(name="SearchArticles", kwargs={"title": "New Biomarkers for Early Detection"}),
            Action(name="GetSubmissionByArticle", kwargs={"article_id": "art_04"}),
            Action(name="SearchUsers", kwargs={"name": "Dr. Ricardo Mendes"}),
            Action(name="AssignReviewerToSubmission", kwargs={"submission_id": "sub_02", "reviewer_user_id": "res_01"}),
            Action(name="SearchUsers", kwargs={"research_field": "Biomedicine"}),
            Action(name="AssignReviewerToSubmission", kwargs={"submission_id": "sub_02", "reviewer_user_id": "res_04"}),
            Action(name="UpdateSubmissionStatus", kwargs={"submission_id": "sub_02", "new_status": "under_review"}),
            Action(name="CreateLogEntry", kwargs={"user_id": "res_01", "notes": "STAFFING: Submission sub_02 assigned to primary:res_01 and secondary:res_04.", "log_id_override": "log_staffing_01"}),
            Action(name="GetSubmissionDetails", kwargs={"submission_id": "sub_02"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="cross_field_literature_discovery",
        instruction="""Execute influential works mapping as Dr. Helena Souza, an AI researcher. Your goal is to find the most recently published paper on 'medical imaging' authored by 'Dr. Ricardo Mendes' and analyze its first listed citation. After identifying the source article and the cited article, you must determine if it is a self-citation (i.e., if Dr. Ricardo Mendes is an author on both papers). Based on this, you must create a log entry with override ID 'log_influence_mapping_02'. If it is a self-citation, the note's format must be: 'INFLUENCE_MAP: Self-citation link found between [Source Article ID] and [Cited Article ID].'. If it is not a self-citation, the format must be: 'INFLUENCE_MAP: Intra-field citation found between [Source Article ID] and [Cited Article ID].'. As final confirmation, return the content of the log entry.""",
        actions=[
            Action(name="SearchUsers", kwargs={"name": "Aisha Khan"}),
            Action(name="SearchArticles", kwargs={"author_name": "Dr. Ricardo Mendes", "abstract_keyword": "medical imaging"}),
            Action(name="SearchCitations", kwargs={"article_id": "art_12", "direction": "from"}),
            Action(name="SearchArticles", kwargs={"article_id": "art_01"}),
            Action(name="SearchUsers", kwargs={"name": "Dr. Ricardo Mendes"}),
            Action(name="SearchArticles", kwargs={"author_name": "Dr. Ricardo Mendes", "topic": "AI"}),
            Action(name="CreateLogEntry", kwargs={
                "user_id": "res_06",
                "notes": "INFLUENCE_MAP: Self-citation link found between art_12 and art_01.",
                "log_id_override": "log_influence_mapping_02"
            }),
            Action(name="GetLogDetails", kwargs={"log_id": "log_influence_mapping_02"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="interdisciplinary_funding_audit_v3",
        instruction="""Perform National Science Foundation audit duties to verify and log the cross-disciplinary impact of the 'Quantum Computing Applications' project. You must check the project's primary linked article (the first in its list) and analyze its most recent citation, defined as the one whose citing article has the most recent publication year. A cross-disciplinary impact is confirmed if the citing author's primary research field is different from the project lead's field. You must create a log entry for the project lead with the override ID 'log_impact_audit_02'. If impact is confirmed, the note's format must be: 'IMPACT_AUDIT: Confirmed. Your work was cited by an author in the [Citing Author's Field] field.'. If the citation is from the same field or no citations exist, the note must state: 'IMPACT_AUDIT: No new cross-disciplinary impact found in latest citation.'. As final confirmation, return the content of the log entry you created.""",
        actions=[
            Action(name="SearchProjects", kwargs={"project_name": "Quantum Computing Applications"}),
            Action(name="GetProjectDetails", kwargs={"project_id": "proj_01"}),
            Action(name="SearchUsers", kwargs={"user_id": "res_03"}),
            Action(name="SearchCitations", kwargs={"article_id": "art_02", "direction": "to"}),
            Action(name="SearchArticles", kwargs={"article_id": "art_01"}),
            Action(name="SearchArticles", kwargs={"article_id": "art_05"}),
            Action(name="SearchUsers", kwargs={"name": "Dr. Ricardo Mendes"}),
            Action(name="CreateLogEntry", kwargs={
                "user_id": "res_03",
                "notes": "IMPACT_AUDIT: Confirmed. Your work was cited by an author in the Artificial Intelligence field.",
                "log_id_override": "log_impact_audit_02"
            }),
            Action(name="GetLogDetails", kwargs={"log_id": "log_impact_audit_02"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="validate_and_archive_project_legacy",
        instruction="""Execute project auditing duties to perform a final legacy audit on the 'Quantum Computing Applications' project. First, you must update the project's status to 'Completed'. Then, you must determine if it qualifies for 'Archived' status. The project qualifies if its primary article (the first in its linked list) has at least one cross-disciplinary citation from an author in a different field. To ensure a deterministic audit, you must base your analysis on the cross-disciplinary citation whose citing article has the most recent publication year. If the project qualifies, you must update its status to 'Archived' and create a single log entry for the project lead with override ID 'log_legacy_audit_01' and the format: 'LEGACY_AUDIT: Project archived. Legacy confirmed via citation from field [Citing Author's Field].'. If it does not qualify, its status remains 'Completed' and the note should state: 'LEGACY_AUDIT: Project completed. No qualifying legacy citation found.'. As final confirmation, return the project's final status.""",
        actions=[
            Action(name="SearchProjects", kwargs={"project_name": "Quantum Computing Applications"}),
            Action(name="UpdateProjectStatus", kwargs={"project_id": "proj_01", "new_status": "Completed"}),
            Action(name="GetProjectDetails", kwargs={"project_id": "proj_01"}),
            Action(name="SearchUsers", kwargs={"user_id": "res_03"}),
            Action(name="SearchCitations", kwargs={"article_id": "art_02", "direction": "to"}),
            Action(name="SearchArticles", kwargs={"article_id": "art_01"}),
            Action(name="SearchUsers", kwargs={"name": "Dr. Ricardo Mendes"}),
            Action(name="SearchArticles", kwargs={"article_id": "art_05"}),
            Action(name="SearchUsers", kwargs={"name": "Dr. Ricardo Mendes"}),
            Action(name="UpdateProjectStatus", kwargs={"project_id": "proj_01", "new_status": "Archived"}),
            Action(name="CreateLogEntry", kwargs={
                "user_id": "res_03",
                "notes": "LEGACY_AUDIT: Project archived. Legacy confirmed via citation from field Artificial Intelligence.",
                "log_id_override": "log_legacy_audit_01"
            }),
            Action(name="GetProjectDetails", kwargs={"project_id": "proj_01"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="validate_multi_citation_impact",
        instruction="""Perform grant administration functions as Dr. Ricardo Mendes to validate the impact of the 'Quantum Computing Applications' project. A project has validated impact if its primary linked article has been cited by at least two different authors from the 'Artificial Intelligence' field. You must verify this by checking the authors of each citing paper and their respective research fields. If this condition is met, you must update the project's status to 'impact_validated' and create a log for your records with the override ID 'log_impact_validation_01' and format: 'AUDIT: Impact validated based on [Number] relevant citations.'. If the condition is not met, update the status to 'impact_validation_failed'. As final confirmation, return the project's final status.""",
        actions=[
            Action(name="SearchUsers", kwargs={"name": "Dr. Ricardo Mendes"}),
            Action(name="SearchProjects", kwargs={"project_name": "Quantum Computing Applications"}),
            Action(name="GetProjectDetails", kwargs={"project_id": "proj_01"}),
            Action(name="SearchCitations", kwargs={"article_id": "art_02", "direction": "to"}),
            Action(name="SearchArticles", kwargs={"article_id": "art_01"}),
            Action(name="SearchUsers", kwargs={"name": "Dr. Helena Souza"}),
            Action(name="SearchArticles", kwargs={"article_id": "art_05"}),
            Action(name="UpdateProjectStatus", kwargs={"project_id": "proj_01", "new_status": "impact_validated"}),
            Action(name="CreateLogEntry", kwargs={
                "user_id": "res_01",
                "notes": "AUDIT: Impact validated based on 2 relevant citations.",
                "log_id_override": "log_impact_validation_01"
            }),
            Action(name="GetProjectDetails", kwargs={"project_id": "proj_01"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="project_pivot_based_on_citation_v3",
        instruction="""Conduct lead research duties for the 'Quantum Computing Applications' project to update it and reflect new, strategic interdisciplinary influence. You must analyze the citations received by your project's primary linked article. From all citations by authors in a different research field, you must identify the one from the citing article with the most recent publication year. If such a citation exists, you must perform two actions: First, update your project by linking this new citing article to it. Second, create a log entry for your own records with the override ID 'log_pivot_01' and the format: 'STRATEGIC_PIVOT: Project updated to reflect influence from field [Citing Author's Field] via article [Citing Article ID].'. As final confirmation, return the updated list of linked articles for your project.""",
        actions=[
            Action(name="SearchProjects", kwargs={"project_name": "Quantum Computing Applications"}),
            Action(name="GetProjectDetails", kwargs={"project_id": "proj_01"}),
            Action(name="SearchUsers", kwargs={"user_id": "res_03"}),
            Action(name="SearchCitations", kwargs={"article_id": "art_02", "direction": "to"}),
            Action(name="SearchArticles", kwargs={"article_id": "art_01"}),
            Action(name="SearchUsers", kwargs={"name": "Dr. Ricardo Mendes"}),
            Action(name="SearchArticles", kwargs={"article_id": "art_05"}),
            Action(name="SearchUsers", kwargs={"name": "Dr. Ricardo Mendes"}),
            Action(name="UpdateProjectLinks", kwargs={"project_id": "proj_01", "add_article_id": "art_01"}),
            Action(name="CreateLogEntry", kwargs={
                "user_id": "res_03",
                "notes": "STRATEGIC_PIVOT: Project updated to reflect influence from field Artificial Intelligence via article art_01.",
                "log_id_override": "log_pivot_01"
            }),
            Action(name="GetProjectDetails", kwargs={"project_id": "proj_01"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="verify_reviewer_expertise_and_bias_v4",
        instruction="""Perform submissions management tasks as Dr. Helena Souza by auditing the reviewer assignment for submission 'sub_01'. Your objective is to validate this assignment based on two strict criteria: 1. Expertise Confirmed: The assigned reviewer must have at least one published article that cites the submitted article. 2. No Reciprocal Citation: The author of the submission must not have cited any work by the assigned reviewer. If both conditions are met, a record of this validation must be made for your records (using override ID 'log_audit_sub01') stating: 'AUDIT_VALIDATION: Assignment for sub_01 is valid. Expertise confirmed and no reciprocal citation found.'. If either condition fails, the submission's status must reflect a need for secondary review, and a record of this audit finding must be made (using the same ID) stating: 'AUDIT_FLAG: Assignment for sub_01 is invalid and requires secondary review.'. As final confirmation, return the content of the record you created.""",
        actions=[
            Action(name="SearchUsers", kwargs={"name": "Dr. Helena Souza"}),
            Action(name="GetSubmissionDetails", kwargs={"submission_id": "sub_01"}),
            Action(name="SearchUsers", kwargs={"user_id": "res_01"}),
            Action(name="SearchArticles", kwargs={"author_name": "Dr. Ricardo Mendes"}),
            Action(name="SearchCitations", kwargs={"article_id": "art_01", "direction": "from"}),
            Action(name="SearchUsers", kwargs={"user_id": "res_03"}),
            Action(name="SearchArticles", kwargs={"author_name": "Dr. Anna Petrov"}),
            Action(name="SearchCitations", kwargs={"article_id": "art_05", "direction": "from"}),
            Action(name="SearchCitations", kwargs={"article_id": "art_07", "direction": "from"}),
            Action(name="CreateLogEntry", kwargs={
                "user_id": "res_06",
                "notes": "AUDIT_VALIDATION: Assignment for sub_01 is valid. Expertise confirmed and no reciprocal citation found.",
                "log_id_override": "log_audit_sub01"
            }),
            Action(name="GetLogDetails", kwargs={"log_id": "log_audit_sub01"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="re_evaluate_completed_project_after_new_impact_v3",
        instruction="""Execute project auditing tasks to re-evaluate the 'Quantum Computing Applications' project. First, you must formally mark the project as 'Completed' with an end year of 2025-03-31. After this, you must determine if it has demonstrated post-completion impact. This is confirmed if the project's primary linked article received any citations from articles published in a year after the project's end year. If multiple such citations exist, you must focus on the one from the citing article with the most recent publication year. If post-completion impact is confirmed, you must update the project's status to 'impact_verified', link the citing article as new evidence, and create a log for the project lead with override ID 'log_post_impact_01' and format: 'AUDIT: Post-completion impact verified via article [Citing Article ID].'. As final confirmation, return the project's new status.""",
        actions=[
            Action(name="SearchProjects", kwargs={"project_name": "Quantum Computing Applications"}),
            Action(name="UpdateProjectStatus", kwargs={"project_id": "proj_01", "new_status": "Completed", "new_end_date": "2025-03-31"}),
            Action(name="SearchCitations", kwargs={"article_id": "art_02", "direction": "to"}),
            Action(name="SearchArticles", kwargs={"article_id": "art_01"}),
            Action(name="SearchArticles", kwargs={"article_id": "art_05"}),
            Action(name="UpdateProjectStatus", kwargs={"project_id": "proj_01", "new_status": "impact_verified", "new_end_date": None}),
            Action(name="UpdateProjectLinks", kwargs={"project_id": "proj_01", "add_article_id": "art_01"}),
            Action(name="CreateLogEntry", kwargs={
                "user_id": "res_03",
                "notes": "AUDIT: Post-completion impact verified via article art_01.",
                "log_id_override": "log_post_impact_01"
            }),
            Action(name="GetProjectDetails", kwargs={"project_id": "proj_01"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="grant_application_and_collaboration_prospecting_v3",
        instruction="""Manage research projects as Dr. Helena Souza by creating a new project for your research on 'Federated Learning for Privacy-Preserving AI' to apply for the 'AI Advancement Grant'. To strengthen the proposal, you must also identify a potential collaborator. You must select another expert from the 'Artificial Intelligence' field (not yourself) based on their recent activity; specifically, the one with the most recently published article. In case of a tie in publication year, select the expert whose name comes first alphabetically. After identifying the expert and their most recent article, you must create the new project with the override ID 'proj_grant_khan_01' and the specific name 'Collaborative Research in Privacy-Preserving AI', linking both your article and the collaborator's article to it. Finally, send a notification to the selected expert with the format: 'COLLAB_INVITE: I am creating a new project, [Project Name], and would like to invite you to collaborate given your recent work on [Collaborator's Article Title].'. As final confirmation, return the project's details.""",
        actions=[
            Action(name="SearchUsers", kwargs={"name": "Aisha Khan"}),
            Action(name="SearchArticles", kwargs={"title": "Federated Learning for Privacy-Preserving AI"}),
            Action(name="SearchFundingSources", kwargs={"source_name": "AI Advancement Grant"}),
            Action(name="SearchArticles", kwargs={"topic": "AI"}),
            Action(name="SearchUsers", kwargs={"name": "Dr. Ricardo Mendes"}),
            Action(name="CreateProject", kwargs={
                "project_id_override": "proj_grant_khan_01",
                "project_name": "Collaborative Research in Privacy-Preserving AI",
                "lead_researcher_id": "res_06",
                "linked_articles": ["art_06", "art_12"],
                "funding_source_id": "fs_01"
            }),
            Action(name="SendNotification", kwargs={
                "recipient_user_id": "res_01",
                "sender_user_id": "res_06",
                "message_content": "COLLAB_INVITE: I am creating a new project, Collaborative Research in Privacy-Preserving AI, and would like to invite you to collaborate given your recent work on Multimodal AI for Medical Imaging Analysis."
            }),
            Action(name="GetProjectDetails", kwargs={"project_id": "proj_grant_khan_01"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="complete_new_researcher_onboarding_v3",
        instruction="""Handle administrative duties to complete the onboarding for the researcher 'Dr. Anna Petrov'. You must ensure her profile is correctly configured by performing two main tasks. First, her personal article log must be synchronized; this means you must add all articles where she is an author and all articles from projects where she is the lead researcher, but only if they are not already present in her log. Second, you must add a welcome log suggesting a collaboration. To do this, find another researcher in her field ('Astrophysics') with the most recently published article. In case of a tie in publication year, select the one whose name comes first alphabetically. Finally, you must create a single summary log for 'Dr. Anna Petrov' with the override ID 'log_onboarding_summary_lc' and the format: 'ONBOARDING_SUMMARY: Profile complete. Articles added: [List of added Article IDs]. Suggested collaborator: [Collaborator Name] ([Collaborator ID]).'. As final confirmation, return the content of this summary log.""",
        actions=[
            Action(name="SearchUsers", kwargs={"name": "Dr. Anna Petrov"}),
            Action(name="SearchArticles", kwargs={"author_name": "Dr. Anna Petrov"}),
            Action(name="SearchProjects", kwargs={"chief_researcher_id": "res_03"}),
            Action(name="CreateLogEntry", kwargs={"user_id": "res_03", "article_id": "art_05", "notes": "System: Automatically added your publication to your log."}),
            Action(name="CreateLogEntry", kwargs={"user_id": "res_03", "article_id": "art_07", "notes": "System: Automatically added your publication to your log."}),
            Action(name="CreateLogEntry", kwargs={"user_id": "res_03", "article_id": "art_02", "notes": "System: Automatically added your project's core article to your log."}),
            Action(name="CreateLogEntry", kwargs={"user_id": "res_03", "article_id": "art_10", "notes": "System: Automatically added your project's core article to your log."}),
            Action(name="SearchUsers", kwargs={"research_field": "Astrophysics"}),
            Action(name="SearchArticles", kwargs={"author_name": "Dr. Ricardo Mendes"}),
            Action(name="CreateLogEntry", kwargs={
                "user_id": "res_03",
                "notes": "ONBOARDING_SUMMARY: Profile complete. Articles added: ['art_05', 'art_07', 'art_02', 'art_10']. Suggested collaborator: Dr. Ricardo Mendes (res_05).",
                "log_id_override": "log_onboarding_summary_lc"
            }),
            Action(name="GetLogDetails", kwargs={"log_id": "log_onboarding_summary_lc"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="comparative_grant_analysis_and_proposal_v3",
        instruction="""Conduct research planning as Dr. Helena Souza to decide if you should create a new project for your paper 'Federated Learning for Privacy-Preserving AI' to apply for the 'AI Advancement Grant'. To make this decision, you must perform a comparative analysis. First, gauge the typical impact of a 'National Science Foundation' grant by finding the citation count of the primary article from its most recently started project. Second, you must verify the novelty of your own article by confirming it has zero citations. If your work is novel (has zero citations), you must create a new project named 'Federated Learning Grant Proposal' with override ID 'proj_grant_app_01'. If your work is not novel, you must not create the project. In either case, as final confirmation, you must create a log entry with override ID 'log_grant_choice_01' and format: 'GRANT_ANALYSIS: Project creation proceeded: [True/False]. NSF impact: [Citation Count] citations. Own work novelty: [Number] citations found.'. Then, return the content of this log.""",
        actions=[
            Action(name="SearchUsers", kwargs={"name": "Aisha Khan"}),
            Action(name="SearchFundingSources", kwargs={"source_name": "National Science Foundation"}),
            Action(name="SearchProjects", kwargs={"funding_source_id": "fs_02"}),
            Action(name="SearchCitations", kwargs={"article_id": "art_02", "direction": "to"}),
            Action(name="SearchArticles", kwargs={"title": "Federated Learning for Privacy-Preserving AI"}),
            Action(name="SearchCitations", kwargs={"article_id": "art_06", "direction": "to"}),
            Action(name="CreateLogEntry", kwargs={
                "user_id": "res_06",
                "notes": "GRANT_ANALYSIS: Project creation proceeded: False. NSF impact: 2 citations. Own work novelty: 1 citations found.",
                "log_id_override": "log_grant_choice_01"
            }),
            Action(name="GetLogDetails", kwargs={"log_id": "log_grant_choice_01"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="expand_reviewer_pool_from_citations_v3",
        instruction="""Execute journal management duties (user 'res_01') to expand the reviewer pool for the 'Biology' topic. Your goal is to identify and invite active researchers by analyzing who cites seminal works. You must find all unique authors who have cited the paper 'Gene Editing Techniques with CRISPR-Cas9'. For each unique citing author found, who is not yourself, you must create a log entry for them with the format: 'REVIEWER_INVITE: Your work citing foundational biology research shows your expertise. We invite you to our journal's reviewer pool.'. As final confirmation, create a summary log for your own records with override ID 'log_expansion_summary_01' and format: 'EXPANSION_SUMMARY: Invitations sent to the following user IDs: [List of unique user IDs, sorted alphabetically].'. Then, return the content of this summary log.""",
        actions=[
            Action(name="SearchArticles", kwargs={"title": "Gene Editing Techniques with CRISPR-Cas9"}),
            Action(name="SearchCitations", kwargs={"article_id": "art_03", "direction": "to"}),
            Action(name="SearchArticles", kwargs={"article_id": "art_04"}),
            Action(name="SearchUsers", kwargs={"name": "Prof. James Wilson"}),
            Action(name="SearchArticles", kwargs={"article_id": "art_11"}),
            Action(name="SearchArticles", kwargs={"article_id": "art_01"}),
            Action(name="SearchUsers", kwargs={"name": "Dr. Ricardo Mendes"}),
            Action(name="SearchUsers", kwargs={"name": "Dr. Helena Souza"}),
            Action(name="CreateLogEntry", kwargs={
                "user_id": "res_04",
                "notes": "REVIEWER_INVITE: Your work citing foundational biology research shows your expertise. We invite you to our journal's reviewer pool."
            }),
            Action(name="CreateLogEntry", kwargs={
                "user_id": "res_16",
                "notes": "REVIEWER_INVITE: Your work citing foundational biology research shows your expertise. We invite you to our journal's reviewer pool."
            }),
            Action(name="CreateLogEntry", kwargs={
                "user_id": "res_01",
                "notes": "EXPANSION_SUMMARY: Invitations sent to the following user IDs: ['res_04', 'res_16'].",
                "log_id_override": "log_expansion_summary_01"
            }),
            Action(name="GetLogDetails", kwargs={"log_id": "log_expansion_summary_01"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="trace_and_flag_retraction_impact_v2",
        instruction="""Manage academic records as a system editor following the official retraction of the 2023 paper titled 'Limits of Quantum Computing in Optimization Problems'. You must ensure two conditions are met: 1. The status of the retracted article is updated to 'retracted'. 2. For every article in the database that cites this retracted work, you must create a log entry for that article's primary author. The log entry must use the format: 'RETRACTION_NOTICE: Your article [Citing Article ID] cites a work that has been retracted. Please review the impact on your research.'. As final confirmation, return the status of the retracted article.""",
        actions=[
            Action(name="SearchArticles", kwargs={"title": "Limits of Quantum Computing in Optimization Problems", "year": 2023}),
            Action(name="UpdateArticleDetails", kwargs={"article_id": "art_02", "new_status": "retracted"}),
            Action(name="SearchCitations", kwargs={"article_id": "art_02", "direction": "to"}),
            Action(name="SearchArticles", kwargs={"article_id": "art_01"}),
            Action(name="SearchUsers", kwargs={"user_id": "res_01"}),
            Action(name="CreateLogEntry", kwargs={
                "user_id": "res_01",
                "notes": "RETRACTION_NOTICE: Your article art_01 cites a work that has been retracted. Please review the impact on your research."
            }),
            Action(name="SearchArticles", kwargs={"article_id": "art_05"}),
            Action(name="SearchUsers", kwargs={"user_id": "res_05"}),
            Action(name="CreateLogEntry", kwargs={
                "user_id": "res_05",
                "notes": "RETRACTION_NOTICE: Your article art_05 cites a work that has been retracted. Please review the impact on your research."
            }),
            Action(name="SearchArticles", kwargs={"article_id": "art_02"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="cross_field_reviewer_vetting_v2",
        instruction="""Perform submissions management duties as Dr. Helena Souza to assign a cross-field reviewer to the submission for 'New Biomarkers for Early Detection of Neurodegenerative Diseases'. You must select one expert from the 'Artificial Intelligence' field based on the following criteria: they must have cited at least one work by the submission's author, Dr. Thomas Anderson. If multiple experts meet this criterion, select the one whose name comes first alphabetically. After selecting the expert, you must assign them as a reviewer and update the submission's status to 'under_review'. As final confirmation, create a log for your records with override ID 'log_vetting_01' and format: 'VETTING: Cross-field reviewer [Reviewer ID] assigned to submission [Submission ID] based on prior citation link.'. Then, return the content of this log.""",
        actions=[
            Action(name="SearchUsers", kwargs={"name": "Dr. Helena Souza"}),
            Action(name="SearchArticles", kwargs={"title": "New Biomarkers for Early Detection of Neurodegenerative Diseases"}), # art_04
            Action(name="GetSubmissionByArticle", kwargs={"article_id": "art_04"}), # function_02
            Action(name="SearchUsers", kwargs={"name": "Dr. Thomas Anderson"}), # res_02 (creator of art_04)
            Action(name="SearchArticles", kwargs={"author_name": "Dr. Thomas Anderson"}), # Outputs art_03, art_09, art_14
            Action(name="SearchCitations", kwargs={"article_id": "art_03", "direction": "to"}), # Returns cit_02, cit_04, and cit_08.
            Action(name="SearchArticles", kwargs={"article_id": "art_01"}), # Provides information on 'Advances in Language Models for Code Generation' authored by Dr. Ricardo Mendes and Dr. Helena Souza, focusing on AI.
            Action(name="SearchUsers", kwargs={"name": "Dr. Ricardo Mendes"}), # Verifies that res_01 originates from the AI domain.
            Action(name="AssignReviewerToSubmission", kwargs={"submission_id": "sub_02", "reviewer_user_id": "res_01"}),
            Action(name="UpdateSubmissionStatus", kwargs={"submission_id": "sub_02", "new_status": "under_review"}),
            Action(name="CreateLogEntry", kwargs={
                "user_id": "res_06",
                "notes": "VETTING: Cross-field reviewer res_01 assigned to submission sub_02 based on prior citation link.",
                "log_id_override": "log_vetting_01"
            }),
            Action(name="GetLogDetails", kwargs={"log_id": "log_vetting_01"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="project_expansion_from_citation_analysis_v2",
        instruction="""Execute project leadership duties as Dr. Anna Petrov, lead of the 'Quantum Computing Applications' project, to expand the project's interdisciplinary scope. To do this, you must analyze the citations received by your project's primary article and identify a potential collaborator from the 'Astrophysics' field. If multiple such citations exist, select the one from the citing article with the most recent publication year. After identifying the collaborator and their article, you must perform three actions: 1. Update your project to link their article. 2. Create a log for your own records with override ID 'log_expansion_idea_01' and format: 'EXPANSION_IDEA: Project updated with [Citing Article ID], new research into quantum cosmology models seems promising.'. 3. Send a notification to the collaborator with the format: 'COLLABORATION_PROPOSAL: Your work on [Citing Article Title] has inspired a new direction for my project. I would be interested in discussing a potential collaboration.'. As final confirmation, return the updated list of linked articles for your project.""",
        actions=[
            Action(name="SearchUsers", kwargs={"name": "Dr. Anna Petrov"}),
            Action(name="SearchProjects", kwargs={"project_name": "Quantum Computing Applications"}),
            Action(name="SearchCitations", kwargs={"article_id": "art_02", "direction": "to"}),
            Action(name="SearchArticles", kwargs={"article_id": "art_05"}),
            Action(name="SearchUsers", kwargs={"user_id": "res_05"}),
            Action(name="UpdateProjectLinks", kwargs={"project_id": "proj_01", "add_article_id": "art_05"}),
            Action(name="CreateLogEntry", kwargs={
                "user_id": "res_03",
                "notes": "EXPANSION_IDEA: Project updated with art_05, new research into quantum cosmology models seems promising.",
                "log_id_override": "log_expansion_idea_01"
            }),
            Action(name="SendNotification", kwargs={
                "recipient_user_id": "res_05",
                "sender_user_id": "res_03",
                "message_content": "COLLABORATION_PROPOSAL: Your work on Dark Matter and the Large-Scale Structure of the Universe has inspired a new direction for my project. I would be interested in discussing a potential collaboration."
            }),
            Action(name="GetProjectDetails", kwargs={"project_id": "proj_01"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="propose_new_interdisciplinary_project_v2",
        instruction="""Conduct formal research proposal development as Dr. Ricardo Mendes to propose a new interdisciplinary project named 'Astro-Quantum Computational Analysis'. This project should bridge your research with quantum computing. To do this, you must create a new project record with the override ID 'proj_astro_quantum_01'. The project must link your most recently published article with the 2023 paper titled 'Limits of Quantum Computing in Optimization Problems'. You must also link it to the 'National Science Foundation' as a potential funding source. As final confirmation, return the complete details of the newly created project.""",
        actions=[
            Action(name="SearchUsers", kwargs={"name": "Dr. Ricardo Mendes"}),
            Action(name="SearchArticles", kwargs={"author_name": "Dr. Ricardo Mendes"}),
            Action(name="SearchArticles", kwargs={"title": "Limits of Quantum Computing in Optimization Problems", "year": 2023}),
            Action(name="SearchFundingSources", kwargs={"source_name": "National Science Foundation"}),
            Action(name="CreateProject", kwargs={
                "project_id_override": "proj_astro_quantum_01",
                "project_name": "Astro-Quantum Computational Analysis",
                "lead_researcher_id": "res_05",
                "linked_articles": ["art_08", "art_02"],
                "funding_source_id": "fs_02"
            }),
            Action(name="GetProjectDetails", kwargs={"project_id": "proj_astro_quantum_01"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="grant_proposal_with_novelty_check_v2",
        instruction="""Develop project proposals as Dr. Thomas Anderson to draft a novel collaboration between gene editing and AI. First, you must identify a potential collaborator by finding the author of the most recently published article from the 'AI' topic that mentions 'transformer architecture' and 'medical' topics. Before proceeding, you must verify the novelty of this collaboration by confirming that there is no overlap in the set of articles that cite your main paper ('Gene Editing Techniques with CRISPR-Cas9') and the set that cites the expert's identified paper. If the collaboration is novel, you must create a draft project with override ID 'proj_draft_genai', associating it with the 'AI Advancement Grant', and linking both foundational papers. Then, send a notification to the expert with the format: 'COLLAB_PROPOSAL: Our research seems to have novel synergistic potential. I have drafted a preliminary project (proj_draft_genai) and would be interested in discussing it.'. If the collaboration is NOT novel, you must NOT create the project. As final confirmation, return the details of the created project.""",
        actions=[
            Action(name="SearchUsers", kwargs={"name": "Dr. Thomas Anderson"}),
            Action(name="SearchArticles", kwargs={"title": "Gene Editing Techniques with CRISPR-Cas9"}),
            Action(name="SearchArticles", kwargs={"abstract_keyword": "medical", "full_text_keyword": "transformer"}),
            Action(name="SearchCitations", kwargs={"article_id": "art_03", "direction": "to"}),
            Action(name="SearchCitations", kwargs={"article_id": "art_12", "direction": "to"}),
            Action(name="SearchArticles", kwargs={"article_id": "art_12"}),
            Action(name="SearchUsers", kwargs={"name": "Dr. Ricardo Mendes"}),
            Action(name="SearchFundingSources", kwargs={"source_name": "AI Advancement Grant"}),
            Action(name="CreateProject", kwargs={
                "project_id_override": "proj_draft_genai",
                "project_name": "Draft: AI-Enhanced Gene Editing Analysis",
                "lead_researcher_id": "res_02",
                "linked_articles": ["art_03", "art_12"],
                "funding_source_id": "fs_01"
            }),
            Action(name="SendNotification", kwargs={
                "recipient_user_id": "res_01",
                "sender_user_id": "res_02",
                "message_content": "COLLAB_PROPOSAL: Our research seems to have novel synergistic potential. I have drafted a preliminary project (proj_draft_genai) and would be interested in discussing it."
            }),
            Action(name="GetProjectDetails", kwargs={"project_id": "proj_draft_genai"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="find_indirect_literature_link_v2",
        instruction="""Perform literature review research to discover an indirect academic link between the 'Biomedicine' and 'AI' fields. To do this, you must first identify the most recently published article from each of these two fields. In case of a tie in publication year, select the one with the fewest authors. Then, you must verify if these two articles cite any of the same foundational papers. If a shared citation is found, you must create a log for your records with override ID 'log_lit_bridge_01' and format: 'LIT_BRIDGE: Indirect link found between [Biomedicine Article ID] and [AI Article ID] via shared citation to [Cited Article ID].'. If no shared citation is found, the note must state: 'LIT_BRIDGE: No indirect link found between the selected articles.'. As final confirmation, return the content of the log.""",
        actions=[
            Action(name="SearchUsers", kwargs={"name": "Dr. Thomas Anderson"}),
            Action(name="SearchArticles", kwargs={"topic": "Biomedicine"}),
            Action(name="SearchArticles", kwargs={"topic": "AI"}),
            Action(name="SearchCitations", kwargs={"article_id": "art_04", "direction": "from"}),
            Action(name="SearchCitations", kwargs={"article_id": "art_09", "direction": "from"}),
            Action(name="CreateLogEntry", kwargs={
                "user_id": "res_02",
                "notes": "LIT_BRIDGE: No indirect link found between the selected articles.",
                "log_id_override": "log_lit_bridge_01"
            }),
            Action(name="GetLogDetails", kwargs={"log_id": "log_lit_bridge_01"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="citation_ripple_effect_proposal_v2",
        instruction="""Execute interdisciplinary project development as Prof. James Wilson by proposing a new project through tracing your paper's academic lineage. Start with your article 'New Biomarkers for Early Detection of Neurodegenerative Diseases'. Identify the first foundational paper it cites. Then, find all other articles that also cite that same foundational paper, and from this list, select the most recently published one from the 'AI' field. Having identified a potential collaborator, you must find a suitable grant from the 'AI Advancement Grant' source and create a new project with override ID 'proj_bioai_01', linking your article and the collaborator's article. As final confirmation, return the details of the new project.""",
        actions=[
            Action(name="SearchUsers", kwargs={"name": "Prof. James Wilson"}),
            Action(name="SearchArticles", kwargs={"title": "New Biomarkers for Early Detection of Neurodegenerative Diseases"}),
            Action(name="SearchCitations", kwargs={"article_id": "art_04", "direction": "from"}),
            Action(name="SearchCitations", kwargs={"article_id": "art_03", "direction": "to"}),
            Action(name="SearchArticles", kwargs={"article_id": "art_01"}),
            Action(name="SearchFundingSources", kwargs={"source_name": "AI Advancement Grant"}),
            Action(name="CreateProject", kwargs={
                "project_id_override": "proj_bioai_01",
                "project_name": "AI-Enhanced Biomarker Analysis",
                "lead_researcher_id": "res_04",
                "linked_articles": ["art_04", "art_01"],
                "funding_source_id": "fs_01"
            }),
            Action(name="GetProjectDetails", kwargs={"project_id": "proj_bioai_01"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="longitudinal_researcher_impact_audit_v2",
        instruction="""Conduct auditing tasks to create a single, comprehensive project named 'Impact Map: Dr. Thomas Anderson' that maps the full citation impact of researcher Dr. Thomas Anderson. To do this, you must first find all articles authored by Dr. Mendes. Then, for each of his articles, you must find all other articles that cite them. The new project, which you will create with the override ID 'proj_mendes_impact_01', must have a complete list of linked articles, including every paper authored by Dr. Mendes and every paper that cites one of his works. As final confirmation, return the full list of linked articles from the newly created project.""",
        actions=[
            Action(name="SearchUsers", kwargs={"name": "Dr. Thomas Anderson"}),
            Action(name="SearchArticles", kwargs={"author_name": "Dr. Thomas Anderson"}),
            Action(name="SearchCitations", kwargs={"article_id": "art_03", "direction": "to"}),
            Action(name="SearchCitations", kwargs={"article_id": "art_09", "direction": "to"}),
            Action(name="SearchCitations", kwargs={"article_id": "art_14", "direction": "to"}),
            Action(name="CreateProject", kwargs={
                "project_id_override": "proj_mendes_impact_01",
                "project_name": "Impact Map: Dr. Thomas Anderson",
                "lead_researcher_id": "res_02",
                "linked_articles": ["art_03", "art_09", "art_14", "art_04", "art_11", "art_01"]
            }),
            Action(name="GetProjectDetails", kwargs={"project_id": "proj_mendes_impact_01"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="advanced_project_restructuring_and_impact_update",
        instruction="""Manage project restructuring as Dr. Anna Petrov, lead researcher for the 'Quantum Computing Applications' project. You need to temporarily put your project on hold, setting its end date to 2025-12-31. Then, you must find the most recently published article from the 'Astrophysics' field that cites your project's primary linked article ('Limits of Quantum Computing in Optimization Problems'). If such an article is found, you must link it to your project, activate the project again (status 'active'), and remove its provisional end date. Then, send a notification to the lead author of this newly linked article, with the exact message content 'COLLABORATION_PROPOSAL: Your work on Dark Matter and the Large-Scale Structure of the Universe has inspired a new direction for my project. I would be interested in discussing a potential collaboration.'. Finally, create a detailed log entry for your records with override ID 'log_restructure_01' that states: 'PROJECT_RESTRUCTURE: Project [Project Name] updated. Article [New Article ID] from [New Article Topic] linked. Collaboration proposal sent to [Collaborator Name].'. If no such article is found, the project status remains 'on_hold' and the log note should state: 'PROJECT_RESTRUCTURE: Project [Project Name] remains on_hold. No new interdisciplinary citation found.'. As final confirmation, return the project's details.""",
        actions=[
            Action(name="SearchUsers", kwargs={"name": "Dr. Anna Petrov"}),
            Action(name="SearchProjects", kwargs={"project_name": "Quantum Computing Applications"}),
            Action(name="UpdateProjectStatus", kwargs={"project_id": "proj_01", "new_status": "on_hold", "new_end_date": "2025-12-31"}),
            Action(name="GetProjectDetails", kwargs={"project_id": "proj_01"}),
            Action(name="SearchArticles", kwargs={"article_id": "art_02"}),
            Action(name="SearchCitations", kwargs={"article_id": "art_02", "direction": "to"}),
            Action(name="SearchArticles", kwargs={"article_id": "art_05"}),
            Action(name="SearchUsers", kwargs={"name": "Dr. Ricardo Mendes"}),
            Action(name="UpdateProjectLinks", kwargs={"project_id": "proj_01", "add_article_id": "art_05"}),
            Action(name="UpdateProjectStatus", kwargs={"project_id": "proj_01", "new_status": "active", "new_end_date": None}),
            Action(name="SendNotification", kwargs={"recipient_user_id": "res_05", "sender_user_id": "res_03", "message_content": "COLLABORATION_PROPOSAL: Your work on Dark Matter and the Large-Scale Structure of the Universe has inspired a new direction for my project. I would be interested in discussing a potential collaboration."}),
            Action(name="CreateLogEntry", kwargs={"user_id": "res_03", "notes": "PROJECT_RESTRUCTURE: Project Quantum Computing Applications updated. Article art_05 from Astrophysics linked. Collaboration proposal sent to Dr. Ricardo Mendes.", "log_id_override": "log_restructure_01"}),
            Action(name="GetProjectDetails", kwargs={"project_id": "proj_01"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="comprehensive_reviewer_onboarding_and_monitoring",
        instruction="""Perform submissions management duties as Dr. Ricardo Mendes to onboard a new reviewer, Dr. Helena Souza, for a pending submission and set up their monitoring. First, find the submission for 'New Biomarkers for Early Detection of Neurodegenerative Diseases' and assign Dr. Helena Souza as a reviewer. Then, ensure Dr. Helena Souza is subscribed to the 'AI' topic. Next, synchronize Dr. Helena Souza's personal article log by adding all articles where he is an author. After these steps, update the submission status to 'under_review'. Create a comprehensive log entry for Dr. Helena Souza with override ID 'log_carlos_onboarding_01' and format: 'ONBOARDING_SUMMARY: Dr. Helena Souza onboarded. Articles logged: [List of Article IDs]. Subscribed to: [Topic]. Assigned to submission [Submission ID].'. Finally, create a separate log entry for yourself (as Dr. Ricardo Mendes) with override ID 'log_my_monitoring_01' stating: 'MONITORING_SETUP: Reviewer [Reviewer ID] assigned to [Submission ID]. Monitoring initiated.'. As final confirmation, return the content of your personal monitoring log.""",
        actions=[
            Action(name="SearchUsers", kwargs={"name": "Dr. Ricardo Mendes"}),
            Action(name="SearchArticles", kwargs={"title": "New Biomarkers for Early Detection of Neurodegenerative Diseases"}),
            Action(name="GetSubmissionByArticle", kwargs={"article_id": "art_04"}),
            Action(name="SearchUsers", kwargs={"name": "Dr. Helena Souza"}),
            Action(name="AssignReviewerToSubmission", kwargs={"submission_id": "sub_02", "reviewer_user_id": "res_16"}),
            Action(name="ManageUserSubscriptions", kwargs={"user_id": "res_16", "topic": "AI", "action": "add"}),
            Action(name="SearchArticles", kwargs={"author_name": "Dr. Helena Souza"}),
            Action(name="CreateLogEntry", kwargs={"user_id": "res_16", "article_id": "art_01", "notes": "System: Automatically added your publication to your log."}),
            Action(name="CreateLogEntry", kwargs={"user_id": "res_16", "article_id": "art_14", "notes": "System: Automatically added your publication to your log."}),
            Action(name="UpdateSubmissionStatus", kwargs={"submission_id": "sub_02", "new_status": "under_review"}),
            Action(name="CreateLogEntry", kwargs={
                "user_id": "res_16",
                "notes": "ONBOARDING_SUMMARY: Dr. Helena Souza onboarded. Articles logged: ['art_01', 'art_14']. Subscribed to: AI. Assigned to submission sub_02.",
                "log_id_override": "log_carlos_onboarding_01"
            }),
            Action(name="CreateLogEntry", kwargs={
                "user_id": "res_01",
                "notes": "MONITORING_SETUP: Reviewer res_16 assigned to sub_02. Monitoring initiated.",
                "log_id_override": "log_my_monitoring_01"
            }),
            Action(name="GetLogDetails", kwargs={"log_id": "log_my_monitoring_01"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="multi_criteria_collaborator_identification_and_project_launch",
        instruction="""Execute collaborative research planning as Dr. Helena Souza, an AI researcher, to identify a suitable collaborator for a new project focused on 'Robotic Process Automation with Large Language Models' and then launch the project under the 'AI Advancement Grant'. The collaborator must be another AI researcher, whose most recently published article is titled 'Multimodal AI for Medical Imaging Analysis', and has fewer than 2 articles currently in their personal log. In case of a tie in publication year, select the one whose name comes first alphabetically. After identifying the collaborator and their most recent relevant article, create a new project with override ID 'proj_llm_rpa_01', linking your own article on 'Robotic Process Automation with Large Language Models' and the collaborator's identified article. Finally, send a notification to the collaborator with the exact message content 'COLLABORATION_INVITATION: Your recent work on Multimodal AI for Medical Imaging Analysis aligns perfectly with my new project on Robotic Process Automation with Large Language Models. I'd like to invite you to collaborate.' and create a log for your records with override ID 'log_rpa_collab_01' and the exact note 'Project 'Collaborative RPA with LLMs' launched with Dr. Helena Souza as collaborator, linking art_15 and art_12. Invitation sent.'. As final confirmation, return the details of the newly created project.""",
        actions=[
            Action(name="SearchUsers", kwargs={"name": "Dr. Helena Souza"}),
            Action(name="SearchArticles", kwargs={"title": "Robotic Process Automation with Large Language Models"}),
            Action(name="SearchUsers", kwargs={"research_field": "Artificial Intelligence"}),
            Action(name="SearchUsers", kwargs={"name": "Dr. Ricardo Mendes"}),
            Action(name="SearchArticles", kwargs={"title": "Multimodal AI for Medical Imaging Analysis"}),
            Action(name="SearchFundingSources", kwargs={"source_name": "AI Advancement Grant"}),
            Action(name="CreateProject", kwargs={
                "project_id_override": "proj_llm_rpa_01",
                "project_name": "Collaborative RPA with LLMs",
                "lead_researcher_id": "res_06",
                "linked_articles": ["art_15", "art_12"],
                "funding_source_id": "fs_01"
            }),
            Action(name="SendNotification", kwargs={
                "recipient_user_id": "res_01",
                "sender_user_id": "res_06",
                "message_content": "COLLABORATION_INVITATION: Your recent work on Multimodal AI for Medical Imaging Analysis aligns perfectly with my new project on Robotic Process Automation with Large Language Models. I'd like to invite you to collaborate."
            }),
            Action(name="CreateLogEntry", kwargs={
                "user_id": "res_06",
                "notes": "Project 'Collaborative RPA with LLMs' launched with Dr. Ricardo Mendes as collaborator, linking art_15 and art_12. Invitation sent.",
                "log_id_override": "log_rpa_collab_01"
            }),
            Action(name="GetProjectDetails", kwargs={"project_id": "proj_llm_rpa_01"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="dynamic_review_process_audit_and_reassignment",
        instruction="""Conduct review process auditing duties as Dr. Ricardo Mendes, the submissions manager, for the submission 'sub_02' (for 'New Biomarkers for Early Detection of Neurodegenerative Diseases'). Your primary goal is to ensure it has at least one reviewer from 'Biomedicine' and that the submission status is 'under_review'. If no reviewer is assigned, or if the assigned reviewer is not from 'Biomedicine', you must assign a new reviewer: select the 'Biomedicine' researcher with the fewest articles in their personal log, prioritizing alphabetically in case of a tie. After assigning, update the submission status to 'under_review' and create a log entry for yourself with override ID 'log_audit_reassign_01' that states: 'REVIEW_AUDIT: Submission [Submission ID] reviewed. Status updated to [New Status]. Reviewer [Reviewer ID] assigned.'. As final confirmation, return the submission's updated status and assigned reviewers.""",
        actions=[
            Action(name="SearchUsers", kwargs={"name": "Dr. Ricardo Mendes"}),
            Action(name="GetSubmissionDetails", kwargs={"submission_id": "sub_02"}),
            Action(name="SearchUsers", kwargs={"research_field": "Biomedicine"}),
            Action(name="SearchUsers", kwargs={"name": "Dr. Thomas Anderson"}),
            Action(name="SearchUsers", kwargs={"name": "Prof. James Wilson"}),
            Action(name="SearchUsers", kwargs={"name": "Dr. Sarah Johnson"}),
            Action(name="SearchUsers", kwargs={"name": "Dr. Helena Souza"}),
            Action(name="SearchUsers", kwargs={"name": "Dr. Anna Petrov"}),
            Action(name="AssignReviewerToSubmission", kwargs={"submission_id": "sub_02", "reviewer_user_id": "res_04"}),
            Action(name="UpdateSubmissionStatus", kwargs={"submission_id": "sub_02", "new_status": "under_review"}),
            Action(name="CreateLogEntry", kwargs={"user_id": "res_01", "notes": "REVIEW_AUDIT: Submission sub_02 reviewed. Status updated to under_review. Reviewer res_04 assigned.", "log_id_override": "log_audit_reassign_01"}),
            Action(name="GetSubmissionDetails", kwargs={"submission_id": "sub_02"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="cross_project_dependency_and_status_synchronization",
        instruction="""Perform project synchronization duties as Dr. Thomas Anderson to synchronize the status of two projects: 'Next-Generation CRISPR Technologies' (your lead project) and 'Quantum Computing Applications'. Your goal is to mark 'Next-Generation CRISPR Technologies' as 'completed' with an end date of 2025-12-31 if, and only if, the primary linked article of 'Quantum Computing Applications' ('Limits of Quantum Computing in Optimization Problems') has been cited by at least one article from the 'Biomedicine' field, published after 2023. If this condition is met, also update 'Quantum Computing Applications' to 'impact_verified'. Otherwise, mark 'Next-Generation CRISPR Technologies' as 'delayed' with no end date. Create a log entry for your records with override ID 'log_sync_01' stating the final status of both projects and the reason. As final confirmation, return the details of both projects.""",
        actions=[
            Action(name="SearchUsers", kwargs={"name": "Dr. Thomas Anderson"}),
            Action(name="SearchProjects", kwargs={"project_name": "Next-Generation CRISPR Technologies"}),
            Action(name="GetProjectDetails", kwargs={"project_id": "proj_03"}),
            Action(name="SearchProjects", kwargs={"project_name": "Quantum Computing Applications"}),
            Action(name="GetProjectDetails", kwargs={"project_id": "proj_01"}),
            Action(name="SearchArticles", kwargs={"article_id": "art_02"}),
            Action(name="SearchCitations", kwargs={"article_id": "art_02", "direction": "to"}),
            Action(name="SearchArticles", kwargs={"article_id": "art_01"}),
            Action(name="SearchArticles", kwargs={"article_id": "art_05"}),
            Action(name="UpdateProjectStatus", kwargs={"project_id": "proj_03", "new_status": "delayed", "new_end_date": None}),
            Action(name="CreateLogEntry", kwargs={
                "user_id": "res_02",
                "notes": "PROJECT_SYNC: 'Next-Generation CRISPR Technologies' set to 'delayed'. 'Quantum Computing Applications' remains 'active'. Reason: No qualifying Biomedicine citation found for 'Limits of Quantum Computing in Optimization Problems'.",
                "log_id_override": "log_sync_01"
            }),
            Action(name="GetProjectDetails", kwargs={"project_id": "proj_03"}),
            Action(name="GetProjectDetails", kwargs={"project_id": "proj_01"})
        ],
        outputs=[]
    ),
    Task(
            annotator="0",
            user_id="comprehensive_literature_analysis_and_author_profiling",
            instruction="""Execute comprehensive literature analysis duties as Dr. Ricardo Mendes, an AI researcher. Your objective is to perform a comprehensive analysis of the article 'Advances in Language Models for Code Generation'. First, find this article and its primary author. Then, find all other articles authored by this primary author. For each article authored by them (including the initial one), create a log entry for your own records, using the note format: 'ANALYSIS: Article [Article ID] by [Author Name]. Topic: [Article Topic].'. For the article 'Advances in Language Models for Code Generation' specifically, also generate a summary of its full text and log this summary as a separate entry with override ID 'log_summary_art01', using the note format: 'SUMMARY: [First three sentences of summary].'. Finally, return the details of the article 'Advances in Language Models for Code Generation' and the content of your summary log entry.""",
            actions=[
                Action(name="SearchUsers", kwargs={"name": "Dr. Ricardo Mendes"}),
                Action(name="SearchArticles", kwargs={"title": "Advances in Language Models for Code Generation"}),
                Action(name="SearchUsers", kwargs={"name": "Dr. Ricardo Mendes"}),
                Action(name="SearchArticles", kwargs={"author_name": "Dr. Ricardo Mendes"}),
                Action(name="CreateLogEntry", kwargs={"user_id": "res_09", "article_id": "art_01", "notes": "ANALYSIS: Article art_01 by Dr. Ricardo Mendes. Topic: AI."}),
                Action(name="CreateLogEntry", kwargs={"user_id": "res_09", "article_id": "art_12", "notes": "ANALYSIS: Article art_12 by Dr. Ricardo Mendes. Topic: AI."}),
                Action(name="CreateLogEntry", kwargs={"user_id": "res_09", "article_id": "art_15", "notes": "ANALYSIS: Article art_15 by Dr. Ricardo Mendes. Topic: AI."}),
                Action(name="SummarizeArticle", kwargs={"article_id": "art_01"}),
                Action(name="CreateLogEntry", kwargs={"user_id": "res_09", "notes": "SUMMARY: The evolution of transformer architectures has marked a significant milestone in artificial intelligence. Initially designed for natural language processing, their application has expanded to diverse domains, including code generation. This paper provides a comprehensive analysis of state-of-the-art models, such as GPT-4 and AlphaCode, detailing their underlying mechanisms and performance benchmarks.", "log_id_override": "log_summary_art01"}),
                Action(name="SearchArticles", kwargs={"article_id": "art_01"}),
                Action(name="GetLogDetails", kwargs={"log_id": "log_summary_art01"})
            ],
            outputs=[]
        ),
    Task(
        annotator="0",
        user_id="grant_audit_and_reallocation_strategy",
        instruction="""Execute grant administration duties as Dr. Helena Souza to audit the 'Federated AI Systems' project and propose a funding reallocation strategy. First, retrieve the details of the 'Federated AI Systems' project and its current funding source. Then, identify all available grants in the 'AI' focus area. If the project's current funding source is 'depleted', or if there is an available grant with a larger amount than its current grant, you must send a notification to the project's lead researcher (Dr. Helena Souza herself) with the exact message content 'FUNDING_REALLOCATION_PROPOSAL: Project [Project Name] requires reallocation. Recommend grant [Recommended Grant Name] ([Recommended Grant ID]) with amount [Recommended Grant Amount].'. If reallocation is not needed, send a notification with the exact message content 'FUNDING_AUDIT: Project [Project Name] funding is currently optimal.'. Finally, create a log entry for your records with override ID 'log_funding_audit_01' stating the outcome: 'FUNDING_AUDIT_OUTCOME: Reallocation proposed: [True/False].'. As final confirmation, return the content of this log entry.""",
        actions=[
            Action(name="SearchUsers", kwargs={"name": "Dr. Helena Souza"}),
            Action(name="SearchProjects", kwargs={"project_name": "Federated AI Systems"}),
            Action(name="GetProjectDetails", kwargs={"project_id": "proj_04"}),
            Action(name="SearchFundingSources", kwargs={"funding_source_id": "fs_01"}),
            Action(name="SearchFundingSources", kwargs={"focus_area": "AI", "status": "available"}),
            Action(name="SearchFundingSources", kwargs={"source_name": "Quantum Computing Initiative"}),
            Action(name="SendNotification", kwargs={
                "recipient_user_id": "res_06",
                "sender_user_id": "res_06",
                "message_content": "FUNDING_REALLOCATION_PROPOSAL: Project Federated AI Systems requires reallocation. Recommend grant Quantum Computing Initiative (fs_10) with amount 800000."
            }),
            Action(name="CreateLogEntry", kwargs={
                "user_id": "res_06",
                "notes": "FUNDING_AUDIT_OUTCOME: Reallocation proposed: True.",
                "log_id_override": "log_funding_audit_01"
            }),
            Action(name="GetLogDetails", kwargs={"log_id": "log_funding_audit_01"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="interdisciplinary_reviewer_recruitment_and_assignment",
        instruction="""Manage reviewer recruitment and assignment duties as Dr. Thomas Anderson, a submissions manager, to recruit and assign a new interdisciplinary reviewer for the submission for 'New Biomarkers for Early Detection of Neurodegenerative Diseases'. The reviewer must be from the 'Artificial Intelligence' field, have cited a paper by Prof. James Wilson (the article's author), and have a current logged articles count of 0 (indicating light workload). In case of a tie in logged articles, select the one whose name comes first alphabetically. After identifying the reviewer, assign them to the submission, and update the submission status to 'under_review'. Then, send a personalized welcome notification to the new reviewer with the exact message content 'REVIEWER_WELCOME: Welcome! You've been assigned to review the submission for 'New Biomarkers for Early Detection of Neurodegenerative Diseases' (art_04). We value your interdisciplinary perspective.'. Finally, create a log entry for your own records with override ID 'log_recruitment_01' stating: 'RECRUITMENT_LOG: Reviewer [Reviewer ID] assigned to [Submission ID].'. As final confirmation, return the submission's updated list of assigned reviewers.""",
        actions=[
            Action(name="SearchUsers", kwargs={"name": "Dr. Thomas Anderson"}),
            Action(name="SearchArticles", kwargs={"title": "New Biomarkers for Early Detection of Neurodegenerative Diseases"}), # Detecta art_04
            Action(name="GetSubmissionByArticle", kwargs={"article_id": "art_04"}), # Identificar sub_02
            Action(name="SearchUsers", kwargs={"name": "Prof. James Wilson"}), # Detecta res_04
            Action(name="SearchCitations", kwargs={"article_id": "art_04", "direction": "to"}), # Isso deve devolver cit_06 (origem: art_14)
            Action(name="SearchArticles", kwargs={"article_id": "art_14"}), # Localiza art_14 (autores: Dr. Thomas Anderson, Prof. James Wilson, Dr. Helena Souza)
            Action(name="SearchUsers", kwargs={"name": "Dr. Helena Souza"}), # Detecta res_16
            Action(name="AssignReviewerToSubmission", kwargs={"submission_id": "sub_02", "reviewer_user_id": "res_16"}), # Designates Dr. Helena Souza
            Action(name="UpdateSubmissionStatus", kwargs={"submission_id": "sub_02", "new_status": "under_review"}),
            Action(name="SendNotification", kwargs={
                "recipient_user_id": "res_16",
                "sender_user_id": "res_02",
                "message_content": "REVIEWER_WELCOME: Welcome! You've been assigned to review the submission for 'New Biomarkers for Early Detection of Neurodegenerative Diseases' (art_04). We value your interdisciplinary perspective."
            }),
            Action(name="CreateLogEntry", kwargs={
                "user_id": "res_02",
                "notes": "RECRUITMENT_LOG: Reviewer res_16 assigned to sub_02.",
                "log_id_override": "log_recruitment_01"
            }),
            Action(name="GetSubmissionDetails", kwargs={"submission_id": "sub_02"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="cross_disciplinary_impact_validation_and_reporting",
        instruction="""Execute cross-disciplinary impact validation duties as Dr. Anna Petrov, an Astrophysics researcher, to validate the cross-disciplinary impact of the 'Quantum Computing Applications' project's primary linked article ('Limits of Quantum Computing in Optimization Problems'). Determine if this article has been cited by at least two unique authors from fields other than 'Quantum Physics' and 'Astrophysics'. For each such valid citing author, find their primary institution and determine if they are currently 'available'. If both of these authors are found and are 'available', update the project status to 'cross_impact_verified'. Otherwise, set the project status to 'impact_validation_failed'. Create a log entry for your records with override ID 'log_cross_impact_01' detailing the outcome: 'CROSS_IMPACT_AUDIT: Project [Project ID] status updated to [New Status]. [Number] relevant cross-disciplinary contacts identified.'. As final confirmation, return the project's new status and the content of the log entry.""",
        actions=[
            Action(name="SearchUsers", kwargs={"name": "Dr. Anna Petrov"}),
            Action(name="SearchProjects", kwargs={"project_name": "Quantum Computing Applications"}),
            Action(name="GetProjectDetails", kwargs={"project_id": "proj_01"}),
            Action(name="SearchArticles", kwargs={"article_id": "art_02"}),
            Action(name="SearchCitations", kwargs={"article_id": "art_02", "direction": "to"}),
            Action(name="SearchArticles", kwargs={"article_id": "art_01"}),
            Action(name="SearchUsers", kwargs={"name": "Dr. Ricardo Mendes"}), # Localiza res_01 (acessível)
            Action(name="SearchUsers", kwargs={"name": "Dr. Helena Souza"}), # Identifies res_16 (available)
            Action(name="UpdateProjectStatus", kwargs={"project_id": "proj_01", "new_status": "cross_impact_verified"}),
            Action(name="CreateLogEntry", kwargs={
                "user_id": "res_03",
                "notes": "CROSS_IMPACT_AUDIT: Project proj_01 status updated to cross_impact_verified. 2 relevant cross-disciplinary contacts identified.",
                "log_id_override": "log_cross_impact_01"
            }),
            Action(name="GetProjectDetails", kwargs={"project_id": "proj_01"}),
            Action(name="GetLogDetails", kwargs={"log_id": "log_cross_impact_01"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="funding_source_analysis_and_strategic_project_creation",
        instruction="""Conduct strategic project development as Dr. Ricardo Mendes, an Astrophysics researcher, to create a new strategic project by leveraging available funding. First, identify all available funding sources in 'Astrophysics'. Select the one with the largest 'grant_amount' for your project. Then, find your most recently published article. Create a new project with override ID 'proj_astro_vision_01', naming it 'Cosmic Vision Initiative', with yourself as the lead researcher, linking your identified article and associating it with the selected funding source. Finally, send a notification to the funding source manager (if applicable, or the system if no specific manager) with the exact message content 'PROJECT_PROPOSAL: Initiating project Cosmic Vision Initiative (proj_astro_vision_01) with funding from [Funding Source Name].'. As final confirmation, return the details of the newly created project.""",
        actions=[
            Action(name="SearchUsers", kwargs={"name": "Dr. Ricardo Mendes"}),
            Action(name="SearchFundingSources", kwargs={"focus_area": "Astrophysics", "status": "available"}),
            Action(name="SearchArticles", kwargs={"author_name": "Dr. Ricardo Mendes"}),
            Action(name="CreateProject", kwargs={
                "project_id_override": "proj_astro_vision_01",
                "project_name": "Cosmic Vision Initiative",
                "lead_researcher_id": "res_05",
                "linked_articles": ["art_08"],
                "funding_source_id": "fs_04"
            }),
            Action(name="SendNotification", kwargs={
                "recipient_user_id": "system",
                "sender_user_id": "res_05",
                "message_content": "PROJECT_PROPOSAL: Initiating project Cosmic Vision Initiative (proj_astro_vision_01) with funding from Space Exploration Fund."
            }),
            Action(name="GetProjectDetails", kwargs={"project_id": "proj_astro_vision_01"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="interdisciplinary_research_collaboration_and_funding_acquisition",
        instruction="""Initiate interdisciplinary research collaboration as Prof. James Wilson, a Biomedicine researcher, to initiate a new interdisciplinary research project. First, find your article titled 'Gene Editing Techniques with CRISPR-Cas9'. Then, identify a suitable collaborator from the 'Astrophysics' field who has the most recently published article and currently has 0 articles in their personal log. In case of a tie in publication year, select the one whose name comes first alphabetically. After identifying the collaborator and their most relevant article, you must secure funding for this project. Find all available funding sources in 'Astrophysics' and select the one with the largest 'grant_amount'. Create a new project with override ID 'proj_interdisciplinary_01', naming it 'Biomedicine-Astrophysics Synergy', with yourself as the lead researcher, linking your article ('Gene Editing Techniques with CRISPR-Cas9') and the collaborator's identified article ('Atmospheric Signatures of Exoplanets'). Associate this project with the selected funding source. Finally, send a collaboration invitation to the identified collaborator with the exact message content 'COLLABORATION_INVITATION: Your work on Atmospheric Signatures of Exoplanets aligns perfectly with a new interdisciplinary project. I invite you to collaborate on 'Biomedicine-Astrophysics Synergy'.'. Create a log entry for your records with override ID 'log_interdisciplinary_01' stating: 'INTERDISCIPLINARY_PROJECT: Project [Project ID] launched with [Collaborator ID] and funding from [Funding Source Name].'. As final confirmation, return the details of the newly created project.""",
        actions=[
            Action(name="SearchUsers", kwargs={"name": "Prof. James Wilson"}),
            Action(name="SearchArticles", kwargs={"title": "Gene Editing Techniques with CRISPR-Cas9"}), # art_03
            Action(name="SearchUsers", kwargs={"research_field": "Astrophysics"}), # results_03, results_05, results_11
            Action(name="SearchUsers", kwargs={"name": "Dr. Ricardo Mendes"}), # res_05 (0 articles recorded)
            Action(name="SearchArticles", kwargs={"author_name": "Dr. Ricardo Mendes"}), # art_08 (2025) -> a versão mais atual dele
            Action(name="SearchUsers", kwargs={"name": "Dr. Anna Petrov"}), # res_03 (0 articles logged)
            Action(name="SearchArticles", kwargs={"author_name": "Dr. Anna Petrov"}), # art_05 (2023)
            Action(name="SearchUsers", kwargs={"name": "Dr. Helena Souza"}), # res_11 (0 recorded articles)
            Action(name="SearchArticles", kwargs={"author_name": "Dr. Helena Souza"}), # Sem publicações dele.
            Action(name="SearchFundingSources", kwargs={"focus_area": "Astrophysics", "status": "available"}), # fs_04 (1.2MB)
            Action(name="CreateProject", kwargs={
                "project_id_override": "proj_interdisciplinary_01",
                "project_name": "Biomedicine-Astrophysics Synergy",
                "lead_researcher_id": "res_04",
                "linked_articles": ["art_03", "art_08"], # Conectando art_08 de Dr. Ricardo Mendes
                "funding_source_id": "fs_04"
            }),
            Action(name="SendNotification", kwargs={
                "recipient_user_id": "res_05",
                "sender_user_id": "res_04",
                "message_content": "COLLABORATION_INVITATION: Your work on Atmospheric Signatures of Exoplanets aligns perfectly with a new interdisciplinary project. I invite you to collaborate on 'Biomedicine-Astrophysics Synergy'."
            }),
            Action(name="CreateLogEntry", kwargs={
                "user_id": "res_04",
                "notes": "INTERDISCIPLINARY_PROJECT: Project proj_interdisciplinary_01 launched with res_05 and funding from Space Exploration Fund.",
                "log_id_override": "log_interdisciplinary_01"
            }),
            Action(name="GetProjectDetails", kwargs={"project_id": "proj_interdisciplinary_01"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="research_log_consistency_audit_and_notification",
        instruction="""You are Dr. Helena Souza, an academic integrity officer. Your objective is to audit research log consistency for a specific researcher, Dr. Ricardo Mendes. First, identify all articles where Dr. Ricardo Mendes is an author. Then, for each of these articles, verify if an entry for that article exists in Dr. Ricardo Mendes's personal research log. If any article authored by her is NOT found in her log, create a new log entry for her with the exact note 'LOG_CONSISTENCY_AUDIT: Article [Article ID] was not found in your log. It has been added automatically.' and link the missing article. If all authored articles are already logged, create a single log entry for yourself (as Dr. Helena Souza) with override ID 'log_audit_complete_01' stating 'AUDIT_COMPLETE: All articles by Dr. Ricardo Mendes found in her log.'. As final confirmation, return the content of the log entry created for yourself (if any).""",
        actions=[
            Action(name="SearchUsers", kwargs={"name": "Dr. Helena Souza"}),
            Action(name="SearchUsers", kwargs={"name": "Dr. Ricardo Mendes"}),
            Action(name="SearchArticles", kwargs={"author_name": "Dr. Ricardo Mendes"}),
            Action(name="CreateLogEntry", kwargs={"user_id": "res_01", "article_id": "art_12", "notes": "LOG_CONSISTENCY_AUDIT: Article art_12 was not found in your log. It has been added automatically."}),
            Action(name="CreateLogEntry", kwargs={"user_id": "res_01", "article_id": "art_15", "notes": "LOG_CONSISTENCY_AUDIT: Article art_15 was not found in your log. It has been added automatically."}),
            Action(name="CreateLogEntry", kwargs={
                "user_id": "res_06",
                "notes": "AUDIT_COMPLETE: All articles by Dr. Ricardo Mendes found in her log.",
                "log_id_override": "log_audit_complete_01"
            }),
            Action(name="GetLogDetails", kwargs={"log_id": "log_audit_complete_01"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="strategic_collaboration_identification_and_project_initiation",
        instruction="""You are Dr. Ricardo Mendes, an AI researcher. Your objective is to initiate a strategic collaborative project to explore AI applications in Astrophysics. Identify a potential collaborator from the 'Astrophysics' field who has published an article in 2025 and currently has 0 articles in their personal log. In case of a tie in publication year, select the one whose name comes first alphabetically. After identifying the collaborator and their relevant article ('Atmospheric Signatures of Exoplanets'), create a new project named 'AI in Astrophysics Explorations' with override ID 'proj_ai_astro_01'. Link your own article 'Advances in Language Models for Code Generation' and the collaborator's identified article. Secure funding for this project from the 'Quantum Computing Initiative'. Finally, send a collaboration invitation to the identified collaborator with the exact message content 'COLLABORATION_INVITATION: Your recent work on Atmospheric Signatures of Exoplanets aligns with a new project: AI in Astrophysics Explorations. I invite you to collaborate.'. Create a log entry for your records with override ID 'log_ai_astro_collab_01' stating: 'STRATEGIC_COLLAB: Project [Project ID] launched with [Collaborator ID].'. As final confirmation, return the details of the newly created project.""",
        actions=[
            Action(name="SearchUsers", kwargs={"name": "Dr. Ricardo Mendes"}),
            Action(name="SearchArticles", kwargs={"title": "Advances in Language Models for Code Generation"}),
            Action(name="SearchUsers", kwargs={"research_field": "Astrophysics"}),
            Action(name="SearchUsers", kwargs={"name": "Dr. Ricardo Mendes"}),
            Action(name="SearchArticles", kwargs={"author_name": "Dr. Ricardo Mendes", "year": 2025}),
            Action(name="SearchUsers", kwargs={"name": "Dr. Anna Petrov"}),
            Action(name="SearchArticles", kwargs={"author_name": "Dr. Anna Petrov", "year": 2025}),
            Action(name="SearchUsers", kwargs={"name": "Dr. Helena Souza"}),
            Action(name="SearchArticles", kwargs={"author_name": "Dr. Helena Souza", "year": 2025}),
            Action(name="SearchFundingSources", kwargs={"source_name": "Quantum Computing Initiative"}),
            Action(name="CreateProject", kwargs={
                "project_id_override": "proj_ai_astro_01",
                "project_name": "AI in Astrophysics Explorations",
                "lead_researcher_id": "res_01",
                "linked_articles": ["art_01", "art_08"],
                "funding_source_id": "fs_10"
            }),
            Action(name="SendNotification", kwargs={
                "recipient_user_id": "res_05",
                "sender_user_id": "res_01",
                "message_content": "COLLABORATION_INVITATION: Your recent work on Atmospheric Signatures of Exoplanets aligns with a new project: AI in Astrophysics Explorations. I invite you to collaborate."
            }),
            Action(name="CreateLogEntry", kwargs={
                "user_id": "res_01",
                "notes": "STRATEGIC_COLLAB: Project proj_ai_astro_01 launched with res_05.",
                "log_id_override": "log_ai_astro_collab_01"
            }),
            Action(name="GetProjectDetails", kwargs={"project_id": "proj_ai_astro_01"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="interdisciplinary_review_impact_assessment_and_feedback",
        instruction="""You are Dr. Ricardo Mendes, an AI researcher. Your objective is to assess the interdisciplinary impact of a foundational Biology article and provide targeted feedback. First, identify the article 'Gene Editing Techniques with CRISPR-Cas9'. Then, find the specific article authored by you ('Advances in Language Models for Code Generation') that cites this foundational Biology paper. Summarize your citing article's full text. Create a log entry for your records with override ID 'log_ai_impact_on_bio_01' stating: 'INTERDISCIPLINARY_IMPACT: Article [Citing Article ID] links AI to Biology. Summary: [First three sentences of summary].'. Finally, return the content of this log entry.""",
        actions=[
            Action(name="SearchUsers", kwargs={"name": "Dr. Ricardo Mendes"}),
            Action(name="SearchArticles", kwargs={"title": "Gene Editing Techniques with CRISPR-Cas9"}),
            Action(name="SearchArticles", kwargs={"title": "Advances in Language Models for Code Generation"}),
            Action(name="SearchCitations", kwargs={"article_id": "art_01", "direction": "from"}),
            Action(name="SummarizeArticle", kwargs={"article_id": "art_01"}),
            Action(name="CreateLogEntry", kwargs={
                "user_id": "res_01",
                "notes": "INTERDISCIPLINARY_IMPACT: Article art_01 links AI to Biology. Summary: The evolution of transformer architectures has marked a significant milestone in artificial intelligence. Initially designed for natural language processing, their application has expanded to diverse domains, including code generation. This paper provides a comprehensive analysis of state-of-the-art models, such as GPT-4 and AlphaCode, detailing their underlying mechanisms and performance benchmarks.",
                "log_id_override": "log_ai_impact_on_bio_01"
            }),
            Action(name="GetLogDetails", kwargs={"log_id": "log_ai_impact_on_bio_01"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="project_milestone_validation_and_reporting",
        instruction="""You are Dr. Ricardo Mendes. Your objective is to validate a project milestone for the 'Quantum Computing Applications' project. You must ensure its primary linked article ('Limits of Quantum Computing in Optimization Problems') has been cited by at least one 'AI' article published in 2024 or later, and that the project's other linked article ('Revised: Limits of Quantum Computing') has a status of 'new'. If both conditions are met, update the project status to 'validated' and create a log entry for the project lead (Dr. Anna Petrov) with override ID 'log_project_milestone_01' stating: 'PROJECT_MILESTONE: Project [Project Name] validated. AI citation confirmed and revised article status is new.'. As final confirmation, return the project's new status.""",
        actions=[
            Action(name="SearchUsers", kwargs={"name": "Dr. Ricardo Mendes"}),
            Action(name="SearchProjects", kwargs={"project_name": "Quantum Computing Applications"}),
            Action(name="GetProjectDetails", kwargs={"project_id": "proj_01"}),
            Action(name="SearchArticles", kwargs={"article_id": "art_02"}),
            Action(name="SearchCitations", kwargs={"article_id": "art_02", "direction": "to"}),
            Action(name="SearchArticles", kwargs={"article_id": "art_01"}),
            # Ação implementada para identificar 'art_07'
            Action(name="SearchArticles", kwargs={"title": "Revised: Limits of Quantum Computing"}),
            Action(name="UpdateProjectStatus", kwargs={"project_id": "proj_01", "new_status": "validated"}),
            Action(name="SearchUsers", kwargs={"name": "Dr. Anna Petrov"}),
            Action(name="CreateLogEntry", kwargs={
                "user_id": "res_03",
                "notes": "PROJECT_MILESTONE: Project Quantum Computing Applications validated. AI citation confirmed and revised article status is new.",
                "log_id_override": "log_project_milestone_01"
            }),
            Action(name="GetProjectDetails", kwargs={"project_id": "proj_01"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="submission_lifecycle_management_and_reviewer_feedback_automation",
        instruction="""You are Dr. Thomas Anderson, the submissions manager. Your objective is to automate part of the submission lifecycle by processing a review for submission 'sub_04'. If the review for 'sub_04' recommends 'accept', you must update the submission status to 'Accepted'. Then, send a congratulatory notification to the author of the submitted article ('Quantum Cryptography Protocols for Secure Communications') with the exact message content 'SUBMISSION_ACCEPTED: Congratulations! Your submission for 'Quantum Cryptography Protocols for Secure Communications' has been accepted!'. Also, create a log entry for the primary reviewer of 'sub_04' (Dr. Thomas Anderson himself) with override ID 'log_review_completed_01' stating: 'REVIEW_COMPLETED: Review for submission [Submission ID] processed. Status updated.'. As final confirmation, return the submission's updated status and its assigned reviewers.""",
        actions=[
            Action(name="SearchUsers", kwargs={"name": "Dr. Thomas Anderson"}),
            Action(name="GetSubmissionDetails", kwargs={"submission_id": "sub_04"}),
            Action(name="GetReviewBySubmission", kwargs={"submission_id": "sub_04"}),
            Action(name="UpdateSubmissionStatus", kwargs={"submission_id": "sub_04", "new_status": "Accepted"}),
            Action(name="SearchArticles", kwargs={"title": "Quantum Cryptography Protocols for Secure Communications"}), # Detecta art_10
            Action(name="SearchUsers", kwargs={"name": "Dr. Wei Zhang"}), # Localiza res_03
            Action(name="SendNotification", kwargs={
                "recipient_user_id": "res_03", # Inform Dr. Wei Zhang.
                "sender_user_id": "res_02",
                "message_content": "SUBMISSION_ACCEPTED: Congratulations! Your submission for 'Quantum Cryptography Protocols for Secure Communications' has been accepted!"
            }),
            Action(name="CreateLogEntry", kwargs={
                "user_id": "res_02",
                "notes": "REVIEW_COMPLETED: Review for submission sub_04 processed. Status updated.",
                "log_id_override": "log_review_completed_01"
            }),
            Action(name="GetSubmissionDetails", kwargs={"submission_id": "sub_04"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="comprehensive_project_audit_and_reconciliation",
         instruction="""Conduct comprehensive project auditing duties as Dr. Ricardo Mendes, an AI researcher, to audit the 'Federated AI Systems' project and reconcile its linked articles. First, retrieve the project's details. Then, identify all articles authored by the project's lead researcher, Dr. Helena Souza. For each article authored by Dr. Helena Souza, ensure it is linked to the 'Federated AI Systems' project; if not, add it. After ensuring all relevant articles are linked, update the project's status to 'audited'. Finally, create a log entry for your records with override ID 'log_project_audit_01' stating: 'PROJECT_AUDIT: Project [Project ID] updated and audited. All authored articles by [Lead Researcher Name] linked.'. As final confirmation, return the project's updated details and the content of your audit log.""",
        actions=[
            Action(name="SearchUsers", kwargs={"user_id": "res_01"}),
            Action(name="SearchProjects", kwargs={"project_name": "Federated AI Systems"}),
            Action(name="GetProjectDetails", kwargs={"project_id": "proj_04"}),
            Action(name="SearchUsers", kwargs={"name": "Dr. Helena Souza"}),
            Action(name="SearchArticles", kwargs={"author_name": "Dr. Helena Souza"}),
            Action(name="UpdateProjectLinks", kwargs={"project_id": "proj_04", "add_article_id": "art_06"}),
            Action(name="UpdateProjectLinks", kwargs={"project_id": "proj_04", "add_article_id": "art_15"}),
            Action(name="UpdateProjectStatus", kwargs={"project_id": "proj_04", "new_status": "audited"}),
            Action(name="CreateLogEntry", kwargs={
                "user_id": "res_01",
                "notes": "PROJECT_AUDIT: Project proj_04 updated and audited. All authored articles by Dr. Helena Souza linked.",
                "log_id_override": "log_project_audit_01"
            }),
            Action(name="GetProjectDetails", kwargs={"project_id": "proj_04"}),
            Action(name="GetLogDetails", kwargs={"log_id": "log_project_audit_01"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="collaborative_network_expansion_and_notification_campaign",
        instruction="""Execute collaborative network expansion duties as Dr. Anna Petrov, an Astrophysics researcher, to expand your collaborative network by identifying new potential collaborators through citation analysis and initiating a notification campaign. First, find your latest article, 'Dark Matter and the Large-Scale Structure of the Universe'. Then, identify all unique authors who have cited this article from a field different from 'Astrophysics'. For each such author, send a personalized notification inviting them to collaborate, using the exact message content 'COLLABORATION_INVITATION: Your work citing Dark Matter and the Large-Scale Structure of the Universe demonstrates a synergy with my research. I invite you to explore collaboration opportunities.'. Additionally, ensure each notified collaborator is subscribed to the 'Astrophysics' topic. Finally, create a log entry for your records with override ID 'log_collab_network_01' stating: 'NETWORK_EXPANSION: [Number] new collaborators contacted. User IDs: [List of User IDs, sorted alphabetically].'. As final confirmation, return the content of this log entry.""",
        actions=[
            Action(name="SearchUsers", kwargs={"user_id": "res_03"}),
            Action(name="SearchArticles", kwargs={"title": "Dark Matter and the Large-Scale Structure of the Universe"}),
            Action(name="SearchCitations", kwargs={"article_id": "art_05", "direction": "to"}),
            Action(name="SearchArticles", kwargs={"article_id": "art_13"}),
            Action(name="SearchUsers", kwargs={"name": "Dr. Sarah Johnson"}),
            Action(name="SendNotification", kwargs={
                "recipient_user_id": "res_07",
                "sender_user_id": "res_03",
                "message_content": "COLLABORATION_INVITATION: Your work citing Dark Matter and the Large-Scale Structure of the Universe demonstrates a synergy with my research. I invite you to explore collaboration opportunities."
            }),
            Action(name="ManageUserSubscriptions", kwargs={"user_id": "res_07", "topic": "Astrophysics", "action": "add"}),
            Action(name="CreateLogEntry", kwargs={
                "user_id": "res_03",
                "notes": "NETWORK_EXPANSION: 1 new collaborators contacted. User IDs: ['res_07'].",
                "log_id_override": "log_collab_network_01"
            }),
            Action(name="GetLogDetails", kwargs={"log_id": "log_collab_network_01"})
        ],
        outputs=[]
    )
]
