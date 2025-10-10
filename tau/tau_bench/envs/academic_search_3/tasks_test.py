from tau_bench.types import Action, Task

TASKS = [
    Task(
        annotator="0",
        user_id="citation_audit_and_correction",
        instruction="""Handle research integrity duties to rectify a citation oversight for the 'Exoplanet Atmospheric Analysis' project. Its main publication, 'Atmospheric Signatures of Exoplanets' (art_08), failed to cite 'Dark Matter and the Large-Scale Structure of the Universe' (art_05), a foundational work co-authored by the project's lead, Dr. Liu Wei, and Prof. James Wilson. Create this missing citation from 'art_08' to 'art_05' with the exact context: 'Citation added during internal audit for contextual completeness.'. Create a research note on the project's record (proj_02) with the exact content: 'Citation audit complete. Added link from art_08 to art_05.'. Additionally, create a research note for Prof. James Wilson (res_03) with the exact content: 'Your co-authored paper art_05 was recently cited by art_08 as part of a data integrity review.'. Display the details of the newly created citation.""",
        actions=[
            Action(name="QueryProjects", kwargs={"project_name": "Exoplanet Atmospheric Analysis"}),
            Action(name="LocatePapers", kwargs={"title": "Dark Matter and the Large-Scale Structure of the Universe"}),
            Action(name="FindUsersByCriteria", kwargs={"name": "Prof. James Wilson"}),
            Action(name="LinkCitedArticle", kwargs={"source_article_id": "art_08", "cited_article_id": "art_05", "citation_context": "Citation added during internal audit for contextual completeness."}),
            Action(name="AddEntryToLog", kwargs={"project_id": "proj_02", "notes": "Citation audit complete. Added link from art_08 to art_05."}),
            Action(name="AddEntryToLog", kwargs={"user_id": "res_03", "notes": "Your co-authored paper art_05 was recently cited by art_08 as part of a data integrity review."}),
            Action(name="RetrieveCitationData", kwargs={"citation_id": "cit_11"}) # MODIFICADO DE cit_05 A cit_11
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="proactive_project_deduplication",
        instruction="""Execute data integrity management to consolidate duplicate entries for the 'Exoplanet Atmospheric Analysis' project led by Dr. Liu Wei. If duplicate projects are found, merge unique articles from the older project (proj_02) into the more recent, primary one (proj_05). Archive the older project. Create a research note on the main project record (proj_05) with the exact content: 'Duplicate project proj_02 merged into this record during data cleanup. Articles consolidated.'. Concurrently, create a research note for Dr. Tanaka (res_05) with the exact content: 'Duplicate records for your project 'Exoplanet Atmospheric Analysis' were found and have been consolidated into a single entry (proj_05).'. Display the details of the main, active project (proj_05).""",
        actions=[
            Action(name="QueryProjects", kwargs={"project_name": "Exoplanet Atmospheric Analysis"}),
            Action(name="FindUsersByCriteria", kwargs={"name": "Dr. Liu Wei"}),
            Action(name="QueryProjects", kwargs={"project_id": "proj_05"}),
            Action(name="QueryProjects", kwargs={"project_id": "proj_02"}),
            Action(name="ModifyRecord", kwargs={"record_type": "project", "record_id": "proj_05", "linked_articles": ["art_08", "art_13"]}), # MODIFICADO: Eliminado "art_02"
            Action(name="ModifyRecord", kwargs={"record_type": "project", "record_id": "proj_02", "status": "archived"}),
            Action(name="AddEntryToLog", kwargs={"project_id": "proj_05", "notes": "Duplicate project proj_02 merged into this record during data cleanup. Articles consolidated."}),
            Action(name="AddEntryToLog", kwargs={"user_id": "res_05", "notes": "Duplicate records for your project 'Exoplanet Atmospheric Analysis' were found and have been consolidated into a single entry (proj_05)."}),
            Action(name="QueryProjects", kwargs={"project_id": "proj_05"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="submit_and_initiate_project",
        instruction="""Execute research assistance for Dr. Elena Rossi to process his new paper 'AI in Algorithmic Trading' with the abstract 'An analysis of reinforcement learning models for high-frequency trading.'. Create a new article record (art_16) for this paper, and concurrently initiate a new project titled 'AI Trading Strategies' (proj_07) for him, linking this new article to it. Create the official submission record (sub_06) for 'art_16'. Display the final submission details.""",
        actions=[
            Action(name="FindUsersByCriteria", kwargs={"name": "Dr. Elena Rossi"}), # Esta operação exibiria res_16.
            Action(name="RegisterArticleRecord", kwargs={"title": "AI in Algorithmic Trading", "authors": ["Dr. Elena Rossi"], "topic": "AI", "abstract": "An analysis of reinforcement learning models for high-frequency trading."}),
            Action(name="InitiateProject", kwargs={"project_name": "AI Trading Strategies", "lead_researcher_id": "res_16"}), # MODIFICADO: res_09 a res_16
            Action(name="ModifyRecord", kwargs={"record_type": "project", "record_id": "proj_07", "linked_articles": ["art_16"]}),
            Action(name="SubmitArticleForReview", kwargs={"article_id": "art_16", "author_user_id": "res_16"}), # MODIFIED: res_09 to res_16
            Action(name="QuerySubmissions", kwargs={"submission_id": "sub_06"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="find_and_assign_funding",
        instruction="""Manage grant acquisition to secure funding for the 'Exoplanet Atmospheric Analysis' project (proj_02), which currently lacks funding. Find an available grant in the 'Astrophysics' category. If the 'Space Exploration Fund' (fs_04) is found, assign it to the project, update the project's status to 'funded'. Dispatch a system notification to the project lead, Dr. Liu Wei (res_05), with the exact message: 'Your project 'Exoplanet Atmospheric Analysis' has been successfully funded by the Space Exploration Fund (fs_04).'. Display the updated project details.""",
        actions=[
            Action(name="QueryProjects", kwargs={"project_name": "Exoplanet Atmospheric Analysis"}),
            Action(name="FindUsersByCriteria", kwargs={"name": "Dr. Liu Wei"}),
            Action(name="LocateFundingSources", kwargs={"area": "Astrophysics", "status": "available"}),
            Action(name="ModifyRecord", kwargs={"record_type": "project", "record_id": "proj_02", "funding_source_id": "fs_04", "status": "funded"}),
            Action(name="DispatchSystemNotification", kwargs={"recipient_user_id": "res_05", "sender_user_id": "system", "message_content": "Your project 'Exoplanet Atmospheric Analysis' has been successfully funded by the Space Exploration Fund (fs_04)."}),
            Action(name="QueryProjects", kwargs={"project_id": "proj_02"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="check_review_and_reviewer_status",
        instruction="""Conduct editorial verification to verify the status of the review for the submission regarding 'Limits of Quantum Computing...' (sub_01) by Dr. Kenji Tanaka (res_01). If Dr. Souza is available, create a research note on the submission record (sub_01) with the exact content: 'Thank you note sent to reviewer res_01 for timely feedback.'. Display the updated submission record.""",
        actions=[
            Action(name="LocatePapers", kwargs={"title": "Limits of Quantum Computing in Optimization Problems"}),
            Action(name="QuerySubmissions", kwargs={"article_id": "art_02"}),
            Action(name="FindUsersByCriteria", kwargs={"name": "Dr. Kenji Tanaka"}),
            Action(name="SearchReviews", kwargs={"submission_id": "sub_01", "reviewer_user_id": "res_01"}),
            Action(name="FindUsersByCriteria", kwargs={"user_id": "res_01"}),
            Action(name="AddEntryToLog", kwargs={"submission_id": "sub_01", "notes": "Thank you note sent to reviewer res_01 for timely feedback."}),
            Action(name="QuerySubmissions", kwargs={"submission_id": "sub_01"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="audit_project_content",
        instruction="""Execute auditing procedures to verify the content of the 'Next-Generation CRISPR Technologies' project (proj_03), ensuring it has two linked articles. Specifically, confirm the title of the first article (art_03) and the abstract content of the second article ('CRISPR-Cas12 Evolution' - art_11). After this verification, create a research note for the project lead, Dr. Sarah Johnson (res_02), with the exact content: 'Content audit for your project 'Next-Generation CRISPR Technologies' is complete.'. Display the updated user profile for Dr. Sarah Johnson, including the new log.""",
        actions=[
            Action(name="QueryProjects", kwargs={"project_name": "Next-Generation CRISPR Technologies"}),
            Action(name="LocatePapers", kwargs={"article_id": "art_03"}),
            Action(name="LocatePapers", kwargs={"article_id": "art_11"}),
            Action(name="SummarizeAbstract", kwargs={"article_id": "art_11"}),
            Action(name="FindUsersByCriteria", kwargs={"name": "Dr. Sarah Johnson"}),
            Action(name="AddEntryToLog", kwargs={"user_id": "res_02", "notes": "Content audit for your project 'Next-Generation CRISPR Technologies' is complete."}),
            Action(name="FindUsersByCriteria", kwargs={"user_id": "res_02"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="submission_review_reminder",
        instruction="""Handle journal editorial duties for the submission 'Multimodal AI for Medical Imaging Analysis' (sub_03), dispatch polite reminders to its assigned reviewers (res_05 and res_04) to complete their feedback soon, with the exact message: 'Gentle reminder to complete your review for submission sub_03.'. Concurrently, create a research note on the submission record (sub_03) with the exact content: 'Reminders sent to reviewers res_05 and res_04.'. Display the updated submission record.""",
        actions=[
            Action(name="LocatePapers", kwargs={"title": "Multimodal AI for Medical Imaging Analysis"}),
            Action(name="QuerySubmissions", kwargs={"article_id": "art_12"}),
            Action(name="FindUsersByCriteria", kwargs={"user_id": "res_05"}),
            Action(name="FindUsersByCriteria", kwargs={"user_id": "res_04"}),
            Action(name="DispatchSystemNotification", kwargs={"recipient_user_id": "res_05", "sender_user_id": "system", "message_content": "Gentle reminder to complete your review for submission sub_03."}),
            Action(name="DispatchSystemNotification", kwargs={"recipient_user_id": "res_04", "sender_user_id": "system", "message_content": "Gentle reminder to complete your review for submission sub_03."}),
            Action(name="AddEntryToLog", kwargs={"submission_id": "sub_03", "notes": "Reminders sent to reviewers res_05 and res_04."}),
            Action(name="QuerySubmissions", kwargs={"submission_id": "sub_03"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="project_funding_workflow",
        instruction="""Handle research coordination to process Dr. Sarah Johnson's project proposal for 'AI applications in diagnosing neurodegenerative diseases'. If a similar project does not already exist, create it with Dr. Mendes (res_02) as lead researcher. Secure funding by finding and assigning an available 'AI' grant (fs_01) to this project, and set its status to 'funded'. After successfully setting up the project and funding, create a research note on the project record with the exact content: 'Project created, funded, and lead researcher confirmed.'. Display the project's final status and funding details.""",
        actions=[
            Action(name="FindUsersByCriteria", kwargs={"name": "Dr. Sarah Johnson"}),
            Action(name="QueryProjects", kwargs={"project_name": "AI applications in diagnosing neurodegenerative diseases"}),
            Action(name="InitiateProject", kwargs={"project_name": "AI applications in diagnosing neurodegenerative diseases", "lead_researcher_id": "res_02"}),
            Action(name="LocateFundingSources", kwargs={"area": "AI", "status": "available"}),
            Action(name="ModifyRecord", kwargs={"record_type": "project", "record_id": "proj_07", "funding_source_id": "fs_01", "status": "funded"}),
            Action(name="AddEntryToLog", kwargs={"project_id": "proj_07", "notes": "Project created, funded, and lead researcher confirmed."}),
            Action(name="QueryProjects", kwargs={"project_id": "proj_07"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="post_review_approval_workflow",
        instruction="""Execute journal administration to process the successful publication of 'Quantum Cryptography Protocols for Secure Communications' (art_10) after its peer review (sub_04) has concluded. Update the article's status to 'published', setting today's date ('2025-06-25') as the publication date. Create a research note for the author, Prof. James Wilson (res_03), with the exact content: 'Congratulations, your submission sub_04 for article art_10 has been approved and published.'. Concurrently, create research notes for the reviewers, Dr. Sarah Johnson (res_02) and Dr. Anna Petrov (res_06), with the exact content: 'Thank you for completing the review for submission sub_04. The review process is now closed.'. Display the official, updated record for the published article (art_10).""",
        actions=[
            Action(name="QuerySubmissions", kwargs={"submission_id": "sub_04"}),
            Action(name="ModifyRecord", kwargs={"record_type": "submission", "record_id": "sub_04", "status": "approved"}),
            Action(name="ModifyRecord", kwargs={"record_type": "article", "record_id": "art_10", "status": "published", "publication_date": "2025-06-25"}),
            Action(name="AddEntryToLog", kwargs={"user_id": "res_03", "notes": "Congratulations, your submission sub_04 for article art_10 has been approved and published."}),
            Action(name="AddEntryToLog", kwargs={"user_id": "res_02", "notes": "Thank you for completing the review for submission sub_04. The review process is now closed."}),
            Action(name="AddEntryToLog", kwargs={"user_id": "res_06", "notes": "Thank you for completing the review for submission sub_04. The review process is now closed."}),
            Action(name="LocatePapers", kwargs={"article_id": "art_10"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="plagiarism_investigation_and_retraction",
        instruction="""Conduct ethics committee investigation to investigate the allegation that Dr. Kenji Tanaka's paper 'Advances in Language Models for Code Generation' (art_01) improperly used concepts from Dr. Sarah Johnson's 'Gene Editing Techniques with CRISPR-Cas9' (art_03), noting the weak citation (cit_04). If the claim holds, retract 'art_01' by updating its status to 'retracted' and delete citation 'cit_04'. Create a research note on 'art_01' with the exact content: 'Article retracted on 2025-06-25 due to improper citation and content overlap with art_03.'. Dispatch a system notification to Dr. Souza (res_01) with the exact message: 'Your article 'art_01' has been formally retracted due to an ethics investigation concerning citation cit_04.'. Concurrently, dispatch a system notification to Dr. Mendes (res_02) with the exact message: 'An improper citation (cit_04) from art_01 to your article art_03 has been investigated and removed as part of an ethics review.'. Display the updated record for the retracted paper (art_01).""",
        actions=[
            Action(name="LocatePapers", kwargs={"article_id": "art_01"}),
            Action(name="LocatePapers", kwargs={"article_id": "art_03"}),
            Action(name="RetrieveCitationData", kwargs={"citation_id": "cit_04"}),
            Action(name="FindUsersByCriteria", kwargs={"name": "Dr. Kenji Tanaka"}),
            Action(name="FindUsersByCriteria", kwargs={"name": "Dr. Sarah Johnson"}),
            Action(name="ModifyRecord", kwargs={"record_type": "article", "record_id": "art_01", "status": "retracted"}),
            Action(name="DeleteCitation", kwargs={"citation_id": "cit_04"}),
            Action(name="AddEntryToLog", kwargs={"article_id": "art_01", "notes": "Article retracted on 2025-06-25 due to improper citation and content overlap with art_03."}),
            Action(name="DispatchSystemNotification", kwargs={"recipient_user_id": "res_01", "sender_user_id": "system", "message_content": "Your article 'art_01' has been formally retracted due to an ethics investigation concerning citation cit_04."}),
            Action(name="DispatchSystemNotification", kwargs={"recipient_user_id": "res_02", "sender_user_id": "system", "message_content": "An improper citation (cit_04) from art_01 to your article art_03 has been investigated and removed as part of an ethics review."}),
            Action(name="LocatePapers", kwargs={"article_id": "art_01"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="legacy_project_revitalization",
        instruction="""Manage program direction to revitalize the archived 'Quantum Computing Applications' project (proj_01) by linking it to a new, high-impact paper, 'Gravitational Wave Detection from Binary Black Holes' (art_13), due to its relevant machine learning techniques. Update the project by changing its status to 'active', assigning Dr. Ahmed Hassan (res_08) as the new lead, and adding 'art_13' to its linked articles. Secure new funding from an available 'Astrophysics' grant (fs_04). Create a research note on the project record (proj_01) with the exact content: 'Project revitalized with new lead (res_08), new funding (fs_04), and linked to new relevant article (art_13).'. Concurrently, create a research note for Prof. Wilson (res_08) with the exact content: 'You have been assigned as the new lead for the revitalized project 'Quantum Computing Applications' (proj_01).'. Display the updated project details.""",
        actions=[
            Action(name="QueryProjects", kwargs={"project_name": "Quantum Computing Applications"}),
            Action(name="LocatePapers", kwargs={"title": "Gravitational Wave Detection from Binary Black Holes"}),
            Action(name="FindUsersByCriteria", kwargs={"name": "Dr. Ahmed Hassan"}),
            Action(name="LocateFundingSources", kwargs={"area": "Astrophysics", "status": "available"}),
            Action(name="ModifyRecord", kwargs={"record_type": "project", "record_id": "proj_01", "status": "active", "lead_researcher_id": ["res_08"], "linked_articles": ["art_02", "art_13"], "funding_source_id": "fs_04"}),
            Action(name="AddEntryToLog", kwargs={"project_id": "proj_01", "notes": "Project revitalized with new lead (res_08), new funding (fs_04), and linked to new relevant article (art_13)."}),
            Action(name="AddEntryToLog", kwargs={"user_id": "res_08", "notes": "You have been assigned as the new lead for the revitalized project 'Quantum Computing Applications' (proj_01)."}),
            Action(name="QueryProjects", kwargs={"project_id": "proj_01"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="retracted_citation_cleanup",
        instruction="""Execute publications management to clean up citations to retracted works. The paper 'Multimodal AI for Medical Imaging Analysis' (art_12) is citing 'Advances in Language Models for Code Generation' (art_01), which has been retracted. Find the citation record (cit_05) linking these two articles. If it exists, delete it. Create a research note on 'art_12' with the exact content: 'Citation to retracted article art_01 was removed during audit.'. Concurrently, create research notes for the authors of 'art_12', Dr. Kenji Tanaka (res_01) and Dr. Thomas Anderson (res_04), with the exact content: 'A citation in your article 'Multimodal AI for Medical Imaging Analysis' (art_12) pointing to a retracted work was removed.'. Display the updated record for 'art_12', including the new log.""",
        actions=[
            Action(name="LocatePapers", kwargs={"title": "Advances in Language Models for Code Generation"}),
            Action(name="LocatePapers", kwargs={"title": "Multimodal AI for Medical Imaging Analysis"}),
            Action(name="QueryCitationConnections", kwargs={"source_article_id": "art_12", "cited_article_id": "art_01"}),
            Action(name="FindUsersByCriteria", kwargs={"name": "Dr. Kenji Tanaka"}),
            Action(name="FindUsersByCriteria", kwargs={"name": "Dr. Thomas Anderson"}),
            Action(name="DeleteCitation", kwargs={"citation_id": "cit_05"}),
            Action(name="AddEntryToLog", kwargs={"article_id": "art_12", "notes": "Citation to retracted article art_01 was removed during audit."}),
            Action(name="AddEntryToLog", kwargs={"user_id": "res_01", "notes": "A citation in your article 'Multimodal AI for Medical Imaging Analysis' (art_12) pointing to a retracted work was removed."}),
            Action(name="AddEntryToLog", kwargs={"user_id": "res_04", "notes": "A citation in your article 'Multimodal AI for Medical Imaging Analysis' (art_12) pointing to a retracted work was removed."}),
            Action(name="LocatePapers", kwargs={"article_id": "art_12"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="cross_citation_opportunity",
        instruction="""Provide strategic publication advisory to create a cross-citation between 'Personalized Cancer Treatment with AI-Driven Drug Discovery' (art_14) and 'CRISPR-Cas12 Evolution for Enhanced Precision' (art_11), as they are complementary. Add a citation from 'art_14' to 'art_11' with the exact context: 'Strategic citation added to link complementary research.'. Create a research note on the source article (art_14) with the exact content: 'Cross-citation to art_11 added to improve research linkage.'. Concurrently, create research notes for the lead authors, Dr. Sarah Johnson (res_02) and Dr. Carlos Ruiz (res_10), with the exact contents: 'Your paper art_14 now cites art_11 to highlight a research synergy.' (for Dr. Mendes) and 'Your paper art_11 has been cited by art_14 to highlight a research synergy.' (for Dr. Petrov). Display the details of the newly created citation.""",
        actions=[
            Action(name="LocatePapers", kwargs={"title": "Personalized Cancer Treatment with AI-Driven Drug Discovery"}),
            Action(name="LocatePapers", kwargs={"title": "CRISPR-Cas12 Evolution for Enhanced Precision"}),
            Action(name="FindUsersByCriteria", kwargs={"name": "Dr. Sarah Johnson"}),
            Action(name="FindUsersByCriteria", kwargs={"name": "Dr. Carlos Ruiz"}), # Modificado: "Dr. Ana Oliveira" para "Dr. Carlos Ruiz"
            Action(name="LinkCitedArticle", kwargs={"source_article_id": "art_14", "cited_article_id": "art_11", "citation_context": "Strategic citation added to link complementary research."}),
            Action(name="AddEntryToLog", kwargs={"article_id": "art_14", "notes": "Cross-citation to art_11 added to improve research linkage."}),
            Action(name="AddEntryToLog", kwargs={"user_id": "res_02", "notes": "Your paper art_14 now cites art_11 to highlight a research synergy."}),
            Action(name="AddEntryToLog", kwargs={"user_id": "res_10", "notes": "Your paper art_11 has been cited by art_14 to highlight a research synergy."}), # res_10 is the identifier for Dr. Carlos Ruiz.
            Action(name="RetrieveCitationData", kwargs={"citation_id": "cit_11"}) # Assuma que cit_11 será o ID atribuído à nova citação. Confirme se esse ID está sequencialmente correto após as atualizações em citation_audit_and_correction. O último ID em `citations.json` é `cit_10`, portanto, o próximo deve ser `cit_11`.
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="reviewer_capacity_check",
        instruction="""Execute journal administration to assign reviewers for the submission 'New Biomarkers for Early Detection...' (sub_02). Assign Dr. Sarah Johnson (res_02) and Dr. Ricardo Mendes (res_07) as reviewers, ensuring they are available 'Biomedicine' experts from different institutions. Update the submission status to 'under_review'. Create a research note for the author (res_04) with the exact content: 'Your submission for 'New Biomarkers for Early Detection...' is now under review.'. Concurrently, create research notes for Dr. Mendes (res_02) and Dr. Santos (res_07) with the exact content: 'You have been assigned to review submission sub_02.'. Display the updated submission record.""",
        actions=[
            Action(name="QuerySubmissions", kwargs={"submission_id": "sub_02"}),
            Action(name="FindUsersByCriteria", kwargs={"name": "Dr. Sarah Johnson"}),
            Action(name="FindUsersByCriteria", kwargs={"name": "Dr. Ricardo Mendes"}),
            Action(name="ModifyRecord", kwargs={"record_type": "submission", "record_id": "sub_02", "status": "under_review", "assigned_reviewers": ["res_02", "res_07"]}),
            Action(name="AddEntryToLog", kwargs={"user_id": "res_04", "notes": "Your submission for 'New Biomarkers for Early Detection...' is now under review."}),
            Action(name="AddEntryToLog", kwargs={"user_id": "res_02", "notes": "You have been assigned to review submission sub_02."}),
            Action(name="AddEntryToLog", kwargs={"user_id": "res_07", "notes": "You have been assigned to review submission sub_02."}),
            Action(name="QuerySubmissions", kwargs={"submission_id": "sub_02"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="project_refocus_and_reassignment",
        instruction="""Manage program direction to revitalize the 'Federated AI Systems' project (proj_04), which stalled due to the unavailability of its lead, Dr. Anna Petrov. Appoint Dr. Maria Santos (res_09), an available 'Artificial Intelligence' expert from 'NextGen Research', as the new lead. Refocus the project's scope by replacing 'Robotic Process Automation with Large Language Models' (art_15) with 'Multimodal AI for Medical Imaging Analysis' (art_12) in its linked articles, while retaining 'Federated Learning for Privacy-Preserving AI' (art_06). Create a research note on the project record (proj_04) with the exact content: 'Project refocused. New lead is res_09. Article scope updated to art_06 and art_12.'. Concurrently, create a research note for Dr. Maria Santos (res_09) with the exact content: 'You have been assigned as the new lead for the refocused project 'Federated AI Systems' (proj_04).'. Display the updated project details.""",
        actions=[
            Action(name="QueryProjects", kwargs={"project_name": "Federated AI Systems"}),
            Action(name="FindUsersByCriteria", kwargs={"name": "Dr. Maria Santos", "research_field": "Artificial Intelligence", "availability": "available"}), # MODIFIED: Added 'name' and removed 'institution'
            Action(name="LocatePapers", kwargs={"title": "Multimodal AI for Medical Imaging Analysis"}),
            Action(name="ModifyRecord", kwargs={"record_type": "project", "record_id": "proj_04", "lead_researcher_id": ["res_09"], "linked_articles": ["art_06", "art_12"]}),
            Action(name="AddEntryToLog", kwargs={"project_id": "proj_04", "notes": "Project refocused. New lead is res_09. Article scope updated to art_06 and art_12."}),
            Action(name="AddEntryToLog", kwargs={"user_id": "res_09", "notes": "You have been assigned as the new lead for the refocused project 'Federated AI Systems' (proj_04)."}),
            Action(name="QueryProjects", kwargs={"project_id": "proj_04"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="funding_realignment_for_scope_change",
        instruction="""Coordinate funding management to realign the 'Next-Generation CRISPR Technologies' project (proj_03) due to its expanded scope towards 'Biomedicine'. Reassign the project to a more appropriate, available 'Biomedicine' funding source, the 'Medical Research Council' (fs_03). Add Dr. Thomas Anderson (res_04), a Biomedicine expert, as a second project lead alongside Dr. Sarah Johnson (res_02). Create a research note on the project record (proj_03) with the exact content: 'Project funding realigned to fs_03 and co-lead res_04 added to reflect new 'Biomedicine' focus.'. Concurrently, create research notes for Dr. Mendes (res_02) with the exact content: 'Your project proj_03 has been realigned with new funding and a new co-lead (res_04) to better suit its scope.' and for Dr. Bauer (res_04) with the exact content: 'You have been added as co-lead to project proj_03 to help guide its new 'Biomedicine' focus.'. Display the updated project details.""",
        actions=[
            Action(name="QueryProjects", kwargs={"project_name": "Next-Generation CRISPR Technologies"}),
            Action(name="FindUsersByCriteria", kwargs={"name": "Dr. Thomas Anderson"}),
            Action(name="FindUsersByCriteria", kwargs={"name": "Dr. Sarah Johnson"}),
            Action(name="LocateFundingSources", kwargs={"area": "Biomedicine", "status": "available"}),
            Action(name="ModifyRecord", kwargs={"record_type": "project", "record_id": "proj_03", "funding_source_id": "fs_03", "lead_researcher_id": ["res_02", "res_04"]}),
            Action(name="AddEntryToLog", kwargs={"project_id": "proj_03", "notes": "Project funding realigned to fs_03 and co-lead res_04 added to reflect new 'Biomedicine' focus."}),
            Action(name="AddEntryToLog", kwargs={"user_id": "res_02", "notes": "Your project proj_03 has been realigned with new funding and a new co-lead (res_04) to better suit its scope."}),
            Action(name="AddEntryToLog", kwargs={"user_id": "res_04", "notes": "You have been added as co-lead to project proj_03 to help guide its new 'Biomedicine' focus."}),
            Action(name="QueryProjects", kwargs={"project_id": "proj_03"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="finalize_approved_submission",
        instruction="""Handle publication management to finalize the publication of 'Quantum Cryptography Protocols for Secure Communications' (art_10) after its submission (sub_04) has been fully approved. Update 'art_10's status to 'published', setting today's date ('2025-06-25') as the publication date. Update the associated project, 'Quantum Cryptography Networks' (proj_06), to 'completed'. Create a research note on the project record (proj_06) with the exact content: 'Project completed with successful publication of primary article art_10.'. Concurrently, create a research note for the author, Prof. James Wilson (res_03), with the exact content: 'Congratulations, your article 'Quantum Cryptography Protocols for Secure Communications' has been published!'. Display the updated project record.""",
        actions=[
            Action(name="QuerySubmissions", kwargs={"submission_id": "sub_04"}),
            Action(name="QueryProjects", kwargs={"project_name": "Quantum Cryptography Networks"}),
            Action(name="FindUsersByCriteria", kwargs={"name": "Prof. James Wilson"}),
            Action(name="ModifyRecord", kwargs={"record_type": "article", "record_id": "art_10", "status": "published", "publication_date": "2025-06-25"}),
            Action(name="ModifyRecord", kwargs={"record_type": "project", "record_id": "proj_06", "status": "completed"}),
            Action(name="AddEntryToLog", kwargs={"project_id": "proj_06", "notes": "Project completed with successful publication of primary article art_10."}),
            Action(name="AddEntryToLog", kwargs={"user_id": "res_03", "notes": "Congratulations, your article 'Quantum Cryptography Protocols for Secure Communications' has been published!"}),
            Action(name="QueryProjects", kwargs={"project_id": "proj_06"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="suggested_citation_addition",
        instruction="""Conduct editorial integration to incorporate a suggested citation to 'Federated Learning for Privacy-Preserving AI' (art_06) from an external expert, linking it to 'Robotic Process Automation with Large Language Models' (art_15) for related automation principles. If the citation does not exist, create it with the exact context: 'Citation added based on external expert recommendation to link related concepts.'. Create a research note on 'art_06' with the exact content: 'Citation to art_15 added based on expert feedback.'. Concurrently, create a research note for the lead author, Dr. Anna Petrov (res_06), with the exact content: 'A citation to 'Robotic Process Automation...' was added to your article 'Federated Learning...' to strengthen its context.'. Display the details of the newly created citation.""",
        actions=[
            Action(name="LocatePapers", kwargs={"title": "Federated Learning for Privacy-Preserving AI"}),
            Action(name="LocatePapers", kwargs={"title": "Robotic Process Automation with Large Language Models"}),
            Action(name="FindUsersByCriteria", kwargs={"name": "Dr. Anna Petrov"}),
            Action(name="QueryCitationConnections", kwargs={"source_article_id": "art_06", "cited_article_id": "art_15"}), # Operação para checar se a referência já está presente.
            Action(name="LinkCitedArticle", kwargs={"source_article_id": "art_06", "cited_article_id": "art_15", "citation_context": "Citation added based on external expert recommendation to link related concepts."}),
            Action(name="AddEntryToLog", kwargs={"article_id": "art_06", "notes": "Citation to art_15 added based on expert feedback."}),
            Action(name="AddEntryToLog", kwargs={"user_id": "res_06", "notes": "A citation to 'Robotic Process Automation...' was added to your article 'Federated Learning...' to strengthen its context."}),
            Action(name="RetrieveCitationData", kwargs={"citation_id": "cit_11"}) # Assuma que cit_11 será o identificador gerado para a nova referência.
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="finalize_approved_submission_and_project",
        instruction="""Handle publication management to finalize the publication of 'Quantum Cryptography Protocols for Secure Communications' (art_10) after its submission (sub_04) has been fully approved. Update 'art_10's status to 'published', setting today's date ('2025-06-25') as the publication date. Update the associated project, 'Quantum Cryptography Networks' (proj_06), to 'completed'. Create a research note on the project record (proj_06) with the exact content: 'Project completed with successful publication of primary article art_10.'. Concurrently, create a research note for the author, Prof. James Wilson (res_03), with the exact content: 'Congratulations, your article 'Quantum Cryptography Protocols for Secure Communications' has been published!'. Display the updated project record.""",
        actions=[
            Action(name="QuerySubmissions", kwargs={"submission_id": "sub_04"}),
            Action(name="QueryProjects", kwargs={"project_name": "Quantum Cryptography Networks"}),
            Action(name="FindUsersByCriteria", kwargs={"name": "Prof. James Wilson"}),
            Action(name="ModifyRecord", kwargs={"record_type": "article", "record_id": "art_10", "status": "published", "publication_date": "2025-06-25"}),
            Action(name="ModifyRecord", kwargs={"record_type": "project", "record_id": "proj_06", "status": "completed"}),
            Action(name="AddEntryToLog", kwargs={"project_id": "proj_06", "notes": "Project completed with successful publication of primary article art_10."}),
            Action(name="AddEntryToLog", kwargs={"user_id": "res_03", "notes": "Congratulations, your article 'Quantum Cryptography Protocols for Secure Communications' has been published!"}),
            Action(name="QueryProjects", kwargs={"project_id": "proj_06"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="funding_source_audit",
        instruction="""Execute financial auditing to conduct an audit on the 'AI Advancement Grant' (fs_01). For each project it funds, specifically 'Federated AI Systems' (proj_04), if its status is 'planning', update it to 'pending_review' and create a research note on the project record with the exact content: 'Project flagged for re-evaluation during audit of funding source fs_01 due to 'planning' status.'. Concurrently, update the funding source record (fs_01) with the log: 'Project proj_04 flagged for re-evaluation.'. Finally, create a research note for the project lead, Dr. Anna Petrov (res_06), with the exact content: 'Your project, 'Federated AI Systems', has been placed under financial review due to an audit of its funding source.'. Display the updated project details (proj_04).""",
        actions=[
            Action(name="LocateFundingSources", kwargs={"area": "AI", "status": "available"}), # Esta operação pode ser "find_funding_sources", em vez de "locate".
            Action(name="QueryProjects", kwargs={"funding_source_id": "fs_01"}),
            Action(name="FindUsersByCriteria", kwargs={"user_id": "res_06"}),
            Action(name="ModifyRecord", kwargs={"record_type": "project", "record_id": "proj_04", "status": "pending_review"}),
            Action(name="AddEntryToLog", kwargs={"project_id": "proj_04", "notes": "Project flagged for re-evaluation during audit of funding source fs_01 due to 'planning' status."}),
            Action(name="ModifyRecord", kwargs={"record_type": "funding_source", "record_id": "fs_01", "logs": ["Project proj_04 flagged for re-evaluation."]}), # Alterar um campo 'logs' que não está presente na ferramenta RetrieveFundingInfo.
            Action(name="AddEntryToLog", kwargs={"user_id": "res_06", "notes": "Your project, 'Federated AI Systems', has been placed under financial review due to an audit of its funding source."}),
            Action(name="QueryProjects", kwargs={"project_id": "proj_04"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="project_continuation_funding",
        instruction="""Manage grant processing to process the continuation funding for the 'Next-Generation CRISPR Technologies' project (proj_03). If the project is active and both leads (Dr. Sarah Johnson - res_02, Dr. Ricardo Mendes - res_07) are available, secure its future by assigning an available 'Biomedicine' grant, the 'Healthcare Innovation Fund' (fs_06). Extend the project's end date by two years to '2029-01-14'. Create a research note on the project record (proj_03) with the exact content: 'Project extended for two years with new funding from fs_06.'. Concurrently, create research notes for Dr. Mendes (res_02) and Dr. Santos (res_07) with the exact content: 'Your project 'Next-Generation CRISPR Technologies' has been approved for a two-year extension with new funding.'. Display the updated project details.""",
        actions=[
            Action(name="QueryProjects", kwargs={"project_name": "Next-Generation CRISPR Technologies"}),
            Action(name="FindUsersByCriteria", kwargs={"name": "Dr. Sarah Johnson"}),
            Action(name="FindUsersByCriteria", kwargs={"name": "Dr. Ricardo Mendes"}),
            Action(name="LocateFundingSources", kwargs={"area": "Biomedicine", "status": "available"}),
            Action(name="ModifyRecord", kwargs={"record_type": "project", "record_id": "proj_03", "end_date": "2029-01-14", "funding_source_id": "fs_06"}),
            Action(name="AddEntryToLog", kwargs={"project_id": "proj_03", "notes": "Project extended for two years with new funding from fs_06."}),
            Action(name="AddEntryToLog", kwargs={"user_id": "res_02", "notes": "Your project 'Next-Generation CRISPR Technologies' has been approved for a two-year extension with new funding."}),
            Action(name="AddEntryToLog", kwargs={"user_id": "res_07", "notes": "Your project 'Next-Generation CRISPR Technologies' has been approved for a two-year extension with new funding."}),
            Action(name="QueryProjects", kwargs={"project_id": "proj_03"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="collaborative_grant_application",
        instruction="""Develop research funding strategy to set up a new collaborative project, 'Astro-AI Analytics for Signal Processing' (proj_07), for Dr. Liu Wei (res_05) from 'AstroMetrics' and Dr. Anna Petrov (res_06) from 'SecureVault Corp.'. Assign both researchers as co-leads. Link their key papers: 'Atmospheric Signatures of Exoplanets' (art_08) and 'Federated Learning for Privacy-Preserving AI' (art_06). Target the 'Deep Space Research Grant' (fs_07). As part of the proposal formalization, add a note to the grant's record (fs_07) with the exact content: 'Proposal incoming from project proj_07 (Astro-AI Analytics).'. Display the new project's record to confirm its correct setup.""",
        actions=[
            Action(name="FindUsersByCriteria", kwargs={"name": "Dr. Liu Wei"}),
            Action(name="FindUsersByCriteria", kwargs={"name": "Dr. Anna Petrov"}),
            Action(name="LocateFundingSources", kwargs={"area": "Astrophysics", "status": "available"}), # Ação para emular a posição do grant.
            Action(name="LocatePapers", kwargs={"article_id": "art_08"}),
            Action(name="LocatePapers", kwargs={"article_id": "art_06"}),
            Action(name="InitiateProject", kwargs={"project_name": "Astro-AI Analytics for Signal Processing", "lead_researcher_id": ["res_05", "res_06"]}),
            Action(name="ModifyRecord", kwargs={"record_type": "project", "record_id": "proj_07", "linked_articles": ["art_08", "art_06"], "funding_source_id": "fs_07"}),
            Action(name="ModifyRecord", kwargs={"record_type": "funding_source", "record_id": "fs_07", "logs": ["Proposal incoming from project proj_07 (Astro-AI Analytics)."]}), # Alterar o campo 'logs', que não está presente na ferramenta, mas é simulado para garantir unicidade.
            Action(name="QueryProjects", kwargs={"project_id": "proj_07"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="conflict_of_interest_review",
        instruction="""Execute editor-in-chief duties to resolve a major conflict of interest for the submission 'Multimodal AI for Medical Imaging Analysis' (sub_03), where Dr. Thomas Anderson (res_04) reviewed her own paper. Replace Dr. Bauer with Dr. Sofia Bauer (res_12), an available 'Artificial Intelligence' expert from 'DeepMind Systems'. Remove Dr. Bauer as a reviewer, delete her invalid review (rev_03), and assign Dr. Johnson as the new reviewer. Create a research note on the submission record (sub_03) with the exact content: 'Reviewer res_04 removed due to conflict of interest. Replaced with res_12. Invalid review rev_03 deleted.'. Concurrently, create research notes for Dr. Bauer (res_04) with the exact content: 'Your review (rev_03) for submission sub_03 has been removed due to a direct conflict of interest (author of the work).' and for Dr. Johnson (res_12) with the exact content: 'You have been assigned to review submission sub_03. Please access the manuscript and submit your feedback.'. Display the updated list of reviewers for the submission.""",
        actions=[
            Action(name="QuerySubmissions", kwargs={"submission_id": "sub_03"}),
            Action(name="LocatePapers", kwargs={"article_id": "art_12"}),
            Action(name="FindUsersByCriteria", kwargs={"name": "Dr. Thomas Anderson"}),
            Action(name="FindUsersByCriteria", kwargs={"name": "Dr. Sofia Bauer", "research_field": "Artificial Intelligence", "availability": "available"}), # MODIFICADO: O parâmetro 'institution' foi retirado para prevenir a exclusão, e o nome foi incluído para garantir a determinística.
            Action(name="ModifyRecord", kwargs={"record_type": "submission", "record_id": "sub_03", "assigned_reviewers": ["res_05", "res_12"]}),
            Action(name="DeleteReview", kwargs={"review_id": "rev_03"}),
            Action(name="AddEntryToLog", kwargs={"submission_id": "sub_03", "notes": "Reviewer res_04 removed due to conflict of interest. Replaced with res_12. Invalid review rev_03 deleted."}),
            Action(name="AddEntryToLog", kwargs={"user_id": "res_04", "notes": "Your review (rev_03) for submission sub_03 has been removed due to a direct conflict of interest (author of the work)."}),
            Action(name="AddEntryToLog", kwargs={"user_id": "res_12", "notes": "You have been assigned to review submission sub_03. Please access the manuscript and submit your feedback."}),
            Action(name="QuerySubmissions", kwargs={"submission_id": "sub_03"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="project_merger_and_rebranding",
        instruction="""Direct research operations to merge the overlapping projects 'Federated AI Systems' (proj_04) and 'Exoplanet Atmospheric Analysis' (proj_05) into a new consolidated project titled 'Federated Analytics for Space Science' (proj_07). Assign Dr. Maria Santos (res_09) from 'NextGen Research' as the new, neutral lead. The new project should combine all articles from both original projects ('art_06', 'art_15', 'art_08', 'art_13') and be funded by the 'Deep Space Research Grant' (fs_07). After creating the new project, archive the two original projects (proj_04, proj_05). Create research notes for the original leads, Dr. Anna Petrov (res_06) with the exact content: 'Your project proj_04 has been merged into a new initiative, 'Federated Analytics for Space Science' (proj_07), led by Dr. Maria Santos.', and Dr. Liu Wei (res_05) with the exact content: 'Your project proj_05 has been merged into a new initiative, 'Federated Analytics for Space Science' (proj_07), led by Dr. Maria Santos.'. Concurrently, create a research note for the new lead, Dr. Maria Santos (res_09) with the exact content: 'You have been assigned as the lead for the new merged project 'Federated Analytics for Space Science' (proj_07).'. Display the details of the new consolidated project.""",
        actions=[
            Action(name="QueryProjects", kwargs={"project_name": "Federated AI Systems"}),
            Action(name="QueryProjects", kwargs={"project_name": "Exoplanet Atmospheric Analysis"}),
            Action(name="FindUsersByCriteria", kwargs={"name": "Dr. Maria Santos"}),
            Action(name="FindUsersByCriteria", kwargs={"name": "Dr. Anna Petrov"}),
            Action(name="FindUsersByCriteria", kwargs={"name": "Dr. Liu Wei"}),
            Action(name="LocateFundingSources", kwargs={"area": "Astrophysics"}),
            Action(name="InitiateProject", kwargs={"project_name": "Federated Analytics for Space Science", "lead_researcher_id": "res_09"}), # CORRIGIDO: lead_researcher_id como string, excluídos linked_articles e funding_source_id.
            Action(name="ModifyRecord", kwargs={"record_type": "project", "record_id": "proj_07", "linked_articles": ["art_06", "art_15", "art_08", "art_13"], "funding_source_id": "fs_07"}), # PRÓXIMO PASSO: Para estabelecer articles e funding_source
            Action(name="ModifyRecord", kwargs={"record_type": "project", "record_id": "proj_04", "status": "archived"}),
            Action(name="ModifyRecord", kwargs={"record_type": "project", "record_id": "proj_05", "status": "archived"}),
            Action(name="AddEntryToLog", kwargs={"user_id": "res_06", "notes": "Your project proj_04 has been merged into a new initiative, 'Federated Analytics for Space Science' (proj_07), led by Dr. Maria Santos."}),
            Action(name="AddEntryToLog", kwargs={"user_id": "res_05", "notes": "Your project proj_05 has been merged into a new initiative, 'Federated Analytics for Space Science' (proj_07), led by Dr. Maria Santos."}),
            Action(name="AddEntryToLog", kwargs={"user_id": "res_09", "notes": "You have been assigned as the lead for the new merged project 'Federated Analytics for Space Science' (proj_07)."}),
            Action(name="QueryProjects", kwargs={"project_id": "proj_07"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="fast_track_high_impact_submission",
        instruction="""As editor-in-chief, fast-track the high-impact submission 'Personalized Cancer Treatment with AI-Driven Drug Discovery' (sub_05) by Dr. Sarah Johnson. Assign three available 'Biomedicine' expert reviewers from different institutions (e.g., 'MediCore' - res_02, 'LifeTech' - res_04, 'HealthTech Innovations' - res_07). Immediately update the submission status to 'expedited review' and assign these reviewers. Create a new high-priority project titled 'High-Impact Cancer Therapeutics' (proj_07) with Dr. Mendes (res_02) as the lead. Create urgent research notes for Dr. Mendes (res_02) with the exact content: 'URGENT: Your submission sub_05 has been selected for an expedited review process due to its high potential impact. A new project (proj_07) has been created.', and for each reviewer (res_04, res_07) with the exact content: 'URGENT: You have been assigned to an expedited review for high-impact submission sub_05. Please prioritize this review.'. Display the updated submission record with the new reviewers.""",
        actions=[
            Action(name="QuerySubmissions", kwargs={"submission_id": "sub_05"}),
            Action(name="FindUsersByCriteria", kwargs={"name": "Dr. Sarah Johnson"}),
            Action(name="FindUsersByCriteria", kwargs={"research_field": "Biomedicine", "availability": "available", "institution": "MediCore"}),
            Action(name="FindUsersByCriteria", kwargs={"research_field": "Biomedicine", "availability": "available", "institution": "LifeTech"}),
            Action(name="FindUsersByCriteria", kwargs={"research_field": "Biomedicine", "availability": "available", "institution": "HealthTech Innovations"}),
            Action(name="ModifyRecord", kwargs={"record_type": "submission", "record_id": "sub_05", "status": "expedited_review", "assigned_reviewers": ["res_02", "res_04", "res_07"]}),
            Action(name="InitiateProject", kwargs={"project_name": "High-Impact Cancer Therapeutics", "lead_researcher_id": ["res_02"]}),
            Action(name="AddEntryToLog", kwargs={"user_id": "res_02", "notes": "URGENT: Your submission sub_05 has been selected for an expedited review process due to its high potential impact. A new project (proj_07) has been created."}),
            Action(name="AddEntryToLog", kwargs={"user_id": "res_04", "notes": "URGENT: You have been assigned to an expedited review for high-impact submission sub_05. Please prioritize this review."}),
            Action(name="AddEntryToLog", kwargs={"user_id": "res_07", "notes": "URGENT: You have been assigned to an expedited review for high-impact submission sub_05. Please prioritize this review."}),
            Action(name="QuerySubmissions", kwargs={"submission_id": "sub_05"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="erroneous_citation_correction",
        instruction="""As a database curator, correct an erroneous citation between 'Advances in Language Models for Code Generation' (art_01) and 'Limits of Quantum Computing...' (art_02), identified as irrelevant. Delete the citation record (cit_01) linking these two articles. Create research notes on both 'art_01' with the exact content: 'Citation cit_01 to art_02 removed during audit for relevance.' and 'art_02' with the exact content: 'Citation cit_01 from art_01 removed during audit for relevance.'. Concurrently, create research notes for the lead authors, Dr. Kenji Tanaka (res_01) with the exact content: 'A citation from your article art_01 to art_02 was removed during a relevance audit.' and Prof. James Wilson (res_03) with the exact content: 'A citation from art_01 to your article art_02 was removed during a relevance audit.'. Display the updated record for 'art_01', including the new log entry.""",
        actions=[
            Action(name="QueryCitationConnections", kwargs={"source_article_id": "art_01", "cited_article_id": "art_02"}),
            Action(name="FindUsersByCriteria", kwargs={"name": "Dr. Kenji Tanaka"}),
            Action(name="FindUsersByCriteria", kwargs={"name": "Prof. James Wilson"}),
            Action(name="DeleteCitation", kwargs={"citation_id": "cit_01"}),
            Action(name="AddEntryToLog", kwargs={"article_id": "art_01", "notes": "Citation cit_01 to art_02 removed during audit for relevance."}),
            Action(name="AddEntryToLog", kwargs={"article_id": "art_02", "notes": "Citation cit_01 from art_01 removed during audit for relevance."}),
            Action(name="AddEntryToLog", kwargs={"user_id": "res_01", "notes": "A citation from your article art_01 to art_02 was removed during a relevance audit."}),
            Action(name="AddEntryToLog", kwargs={"user_id": "res_03", "notes": "A citation from art_01 to your article art_02 was removed during a relevance audit."}),
            Action(name="LocatePapers", kwargs={"article_id": "art_01"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="author_institution_transfer",
        instruction="""As an HR and publications manager, process Dr. Kenji Tanaka's (res_01) institutional transfer from 'FutureML' to 'NextGen Research'. Update her user profile to reflect her new institution. For her project, 'Federated AI Systems' (proj_04), assign Dr. Maria Santos (res_09), a senior expert from 'NextGen Research', as the new lead, while retaining Dr. Souza as a team member. Create a research note on the project record (proj_04) with the exact content: 'Lead changed from res_01 to res_09 due to institutional transfer. res_01 remains a contributor.'. Concurrently, create research notes for Dr. Souza (res_01) with the exact content: 'Your lead role on proj_04 has been transferred to Dr. Maria Santos following your move to NextGen Research. You remain a contributor.' and for Dr. Maria Santos (res_09) with the exact content: 'You have been assigned as the new lead for project proj_04.'. Display the updated project details.""",
        actions=[
            Action(name="FindUsersByCriteria", kwargs={"name": "Dr. Kenji Tanaka"}),
            Action(name="QueryProjects", kwargs={"project_name": "Federated AI Systems"}),
            Action(name="FindUsersByCriteria", kwargs={"name": "Dr. Maria Santos"}),
            Action(name="ModifyRecord", kwargs={"record_type": "user", "record_id": "res_01", "institution": "NextGen Research"}),
            Action(name="ModifyRecord", kwargs={"record_type": "project", "record_id": "proj_04", "lead_researcher_id": ["res_09"], "team_members": ["res_01"]}),
            Action(name="AddEntryToLog", kwargs={"project_id": "proj_04", "notes": "Lead changed from res_01 to res_09 due to institutional transfer. res_01 remains a contributor."}),
            Action(name="AddEntryToLog", kwargs={"user_id": "res_01", "notes": "Your lead role on proj_04 has been transferred to Dr. Maria Santos following your move to NextGen Research. You remain a contributor."}),
            Action(name="AddEntryToLog", kwargs={"user_id": "res_09", "notes": "You have been assigned as the new lead for project proj_04."}),
            Action(name="QueryProjects", kwargs={"project_id": "proj_04"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="interdisciplinary_review_setup",
        instruction="""As an editor, set up a special interdisciplinary review for 'Robotic Process Automation with Large Language Models' (art_15) by Dr. Anna Petrov (res_06) and Dr. Kenji Tanaka (res_01). Create a submission record for 'art_15'. Assign Lia Costa (res_15), an 'Artificial Intelligence' expert from outside the authors' institutions, and Dr. Aisha Khan (res_13), a 'Biomedicine' expert, as reviewers. If a project for this research does not exist, create one titled 'Applied LLM Automation' (proj_07) with both authors as leads. Create research notes for Dr. Khan (res_06) with the exact content: 'Your paper 'Robotic Process Automation...' has been submitted for review (sub_06) and assigned to an interdisciplinary panel.', for Dr. Souza (res_01) with the exact content: 'Your paper 'Robotic Process Automation...' has been submitted for review (sub_06) and assigned to an interdisciplinary panel.', for Dr. Anderson (res_15) with the exact content: 'You have been assigned to an interdisciplinary review panel for submission sub_06.', and for Dr. Hassan (res_13) with the exact content: 'You have been assigned to an interdisciplinary review panel for submission sub_06.'. Display the new submission record with the assigned reviewers.""",
        actions=[
            Action(name="LocatePapers", kwargs={"title": "Robotic Process Automation with Large Language Models"}),
            Action(name="FindUsersByCriteria", kwargs={"name": "Dr. Anna Petrov"}),
            Action(name="FindUsersByCriteria", kwargs={"name": "Dr. Kenji Tanaka"}),
            Action(name="SubmitArticleForReview", kwargs={"article_id": "art_15", "author_user_id": "res_06"}),
            Action(name="FindUsersByCriteria", kwargs={"name": "Lia Costa", "research_field": "Artificial Intelligence"}),
            Action(name="FindUsersByCriteria", kwargs={"name": "Dr. Aisha Khan", "research_field": "Biomedicine"}),
            Action(name="ModifyRecord", kwargs={"record_type": "submission", "record_id": "sub_06", "assigned_reviewers": ["res_15", "res_13"]}),
            Action(name="InitiateProject", kwargs={"project_name": "Applied LLM Automation", "lead_researcher_id": ["res_06", "res_01"]}),
            Action(name="AddEntryToLog", kwargs={"user_id": "res_06", "notes": "Your paper 'Robotic Process Automation...' has been submitted for review (sub_06) and assigned to an interdisciplinary panel."}),
            Action(name="AddEntryToLog", kwargs={"user_id": "res_01", "notes": "Your paper 'Robotic Process Automation...' has been submitted for review (sub_06) and assigned to an interdisciplinary panel."}),
            Action(name="AddEntryToLog", kwargs={"user_id": "res_15", "notes": "You have been assigned to an interdisciplinary review panel for submission sub_06."}),
            Action(name="AddEntryToLog", kwargs={"user_id": "res_13", "notes": "You have been assigned to an interdisciplinary review panel for submission sub_06."}),
            Action(name="QuerySubmissions", kwargs={"submission_id": "sub_06"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="authorship_dispute_and_resubmission",
        instruction="""As a collaborations manager, resolve an authorship dispute concerning 'Multimodal AI for Medical Imaging Analysis' (art_12), where Dr. Thomas Anderson (res_04) claims she was unfairly left off the submission (sub_03) by Dr. Kenji Tanaka (res_01). If Dr. Bauer is listed as an author on 'art_12' but not on 'sub_03', retract the original submission ('sub_03'). Create a new project (proj_07) for Dr. Bauer at 'LifeTech' titled 'BioGen Medical Imaging Initiative', funded by the 'Medical Research Council' (fs_03), and link 'art_12' to it. Create a new, corrected submission (sub_06) under Dr. Bauer's name for 'art_12'. Create a research note on the retracted submission (sub_03) with the exact content: 'Submission retracted due to authorship dispute. Superseded by sub_06.'. Concurrently, create research notes for Dr. Souza (res_01) with the exact content: 'Your submission sub_03 was retracted to correct an authorship issue. Please coordinate with co-authors for future submissions.' and for Dr. Bauer (res_04) with the exact content: 'To resolve an authorship dispute, a new project (proj_07) and submission (sub_06) have been created for your work on 'Multimodal AI for Medical Imaging Analysis'.'. Display the new submission (sub_06).""",
        actions=[
            Action(name="LocatePapers", kwargs={"title": "Multimodal AI for Medical Imaging Analysis"}),
            Action(name="FindUsersByCriteria", kwargs={"name": "Dr. Kenji Tanaka"}),
            Action(name="FindUsersByCriteria", kwargs={"name": "Dr. Thomas Anderson"}),
            Action(name="QuerySubmissions", kwargs={"article_id": "art_12"}),
            Action(name="ModifyRecord", kwargs={"record_type": "submission", "record_id": "sub_03", "status": "retracted"}),
            Action(name="LocateFundingSources", kwargs={"area": "Biomedicine", "status": "available"}), # Operação para emular a posição do grant.
            Action(name="InitiateProject", kwargs={"project_name": "BioGen Medical Imaging Initiative", "lead_researcher_id": ["res_04"], "funding_source_id": "fs_03"}),
            Action(name="ModifyRecord", kwargs={"record_type": "project", "record_id": "proj_07", "linked_articles": ["art_12"]}),
            Action(name="SubmitArticleForReview", kwargs={"article_id": "art_12", "author_user_id": "res_04"}),
            Action(name="AddEntryToLog", kwargs={"submission_id": "sub_03", "notes": "Submission retracted due to authorship dispute. Superseded by sub_06."}),
            Action(name="AddEntryToLog", kwargs={"user_id": "res_01", "notes": "Your submission sub_03 was retracted to correct an authorship issue. Please coordinate with co-authors for future submissions."}),
            Action(name="AddEntryToLog", kwargs={"user_id": "res_04", "notes": "To resolve an authorship dispute, a new project (proj_07) and submission (sub_06) have been created for your work on 'Multimodal AI for Medical Imaging Analysis'."}),
            Action(name="QuerySubmissions", kwargs={"submission_id": "sub_06"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="proactive_collaboration_suggestion",
        instruction="""As a program manager, foster synergy between 'Quantum Computing Applications' (proj_01) and 'Quantum Cryptography Networks' (proj_06). Verify their collaboration potential by extracting keywords from their primary articles ('art_02' and 'art_10'). Suggest a formal collaboration. Create a research note on proj_01 with the exact content: 'Proactive collaboration suggested with project proj_06 based on shared research keywords.'. Concurrently, create a research note on proj_06 with the exact content: 'Proactive collaboration suggested with project proj_01 based on shared research keywords.'. Create research notes for the respective project leads, Dr. Kenji Tanaka (res_01) with the exact content: 'A potential collaboration opportunity has been identified between your project (proj_01) and 'Quantum Cryptography Networks' (proj_06).' and Prof. James Wilson (res_03) with the exact content: 'A potential collaboration opportunity has been identified between your project (proj_06) and 'Quantum Computing Applications' (proj_01).'. Display the updated record for 'Quantum Computing Applications' (proj_01).'""",
        actions=[
            Action(name="QueryProjects", kwargs={"project_name": "Quantum Computing Applications"}),
            Action(name="QueryProjects", kwargs={"project_name": "Quantum Cryptography Networks"}),
            Action(name="ExtractKeywords", kwargs={"article_id": "art_02"}), # Returns ["quantum computing"]
            Action(name="ExtractKeywords", kwargs={"article_id": "art_10"}), # Devuelve []
            Action(name="FindUsersByCriteria", kwargs={"name": "Dr. Kenji Tanaka"}),
            Action(name="FindUsersByCriteria", kwargs={"name": "Prof. James Wilson"}),
            Action(name="AddEntryToLog", kwargs={"project_id": "proj_01", "notes": "Proactive collaboration suggested with project proj_06 based on shared research keywords."}),
            Action(name="AddEntryToLog", kwargs={"project_id": "proj_06", "notes": "Proactive collaboration suggested with project proj_01 based on shared research keywords."}),
            Action(name="AddEntryToLog", kwargs={"user_id": "res_01", "notes": "A potential collaboration opportunity has been identified between your project (proj_01) and 'Quantum Cryptography Networks' (proj_06)."}),
            Action(name="AddEntryToLog", kwargs={"user_id": "res_03", "notes": "A potential collaboration opportunity has been identified between your project (proj_06) and 'Quantum Computing Applications' (proj_01)."}),
            Action(name="QueryProjects", kwargs={"project_id": "proj_01"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="urgent_review_reassignment_and_author_notification",
        instruction="""As a journal manager, urgently reassign the review for 'Personalized Cancer Treatment with AI-Driven Drug Discovery' (sub_05) because Dr. Sarah Johnson (res_02), an assigned reviewer, has become unavailable. Replace Dr. Mendes with Dr. Elena Rossi (res_16), an available 'Artificial Intelligence' expert not from 'MediCore'. Remove Dr. Mendes from the assigned reviewers and add Dr. Silva. Update the status of sub_05 to 'expedited_review' if it's not already. Create a research note on the submission record (sub_05) with the exact content: 'Reviewer res_02 replaced by res_16 due to unavailability.'. Dispatch a system notification to the author, Dr. Thomas Anderson (res_04), with the exact message: 'Your submission sub_05 has had a reviewer change. The review process remains expedited.'. Concurrently, dispatch a notification to Dr. Sarah Johnson (res_02) with the message: 'You have been unassigned from submission sub_05 due to your unavailability.'. Finally, dispatch a notification to Dr. Elena Rossi (res_16) with the message: 'You have been assigned as a new reviewer for expedited submission sub_05. Please prioritize.'. Display the updated submission record for sub_05.""",
        actions=[
            Action(name="QuerySubmissions", kwargs={"submission_id": "sub_05"}),
            Action(name="FindUsersByCriteria", kwargs={"user_id": "res_02"}),
            Action(name="FindUsersByCriteria", kwargs={"name": "Dr. Elena Rossi", "research_field": "Artificial Intelligence", "availability": "available", "institution": "MediCore"}),
            Action(name="FindUsersByCriteria", kwargs={"user_id": "res_04"}),
            Action(name="ModifyRecord", kwargs={"record_type": "submission", "record_id": "sub_05", "assigned_reviewers": ["res_16"]}), # Adjusted to include solely the specified reviewer.
            Action(name="ModifyRecord", kwargs={"record_type": "submission", "record_id": "sub_05", "status": "expedited_review"}),
            Action(name="AddEntryToLog", kwargs={"submission_id": "sub_05", "notes": "Reviewer res_02 replaced by res_16 due to unavailability."}),
            Action(name="DispatchSystemNotification", kwargs={"recipient_user_id": "res_04", "sender_user_id": "system", "message_content": "Your submission sub_05 has had a reviewer change. The review process remains expedited."}),
            Action(name="DispatchSystemNotification", kwargs={"recipient_user_id": "res_02", "sender_user_id": "system", "message_content": "You have been unassigned from submission sub_05 due to your unavailability."}),
            Action(name="DispatchSystemNotification", kwargs={"recipient_user_id": "res_16", "sender_user_id": "system", "message_content": "You have been assigned as a new reviewer for expedited submission sub_05. Please prioritize."}),
            Action(name="QuerySubmissions", kwargs={"submission_id": "sub_05"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="funding_source_reallocation_and_researcher_support",
        instruction="""As a grants officer, realign funding for Dr. Anna Petrov's (res_06) stalled project 'Federated AI Systems' (proj_04) due to its current 'planning' status and the depletion of its 'AI Advancement Grant' (fs_01). Find an available 'AI' grant, specifically the 'Machine Learning Excellence Award' (fs_08), and reassign proj_04 to it. Change proj_04's status to 'active'. Due to the funding change, Dr. Anna Petrov (res_06) expresses unavailability. Reassign the lead of proj_04 to Dr. Maria Santos (res_09), an available 'Artificial Intelligence' expert from 'NextGen Research'. Create a research note on proj_04 with the exact content: 'Funding reallocated to fs_08. Status changed to active. Lead reassigned to res_09.'. Concurrently, create a research note for Dr. Khan (res_06) with the exact content: 'Your project proj_04 funding reallocated and lead reassigned to res_09.'. Create a research note for Dr. Maria Santos (res_09) with the exact content: 'You are now the lead for project proj_04.'. Display the updated project details for proj_04.""",
        actions=[
            Action(name="QueryProjects", kwargs={"project_id": "proj_04"}), # 1 connection (input)
            Action(name="FindUsersByCriteria", kwargs={"user_id": "res_06"}), # 1 connection (prompt)
            Action(name="LocateFundingSources", kwargs={"funding_source_id": "fs_01"}), # 1 edge (prompt) - verify depletion if necessary (tools do not reveal it explicitly)
            Action(name="LocateFundingSources", kwargs={"source_name": "Machine Learning Excellence Award", "area": "AI", "status": "available"}), # Three edges (input)
            Action(name="FindUsersByCriteria", kwargs={"name": "Dr. Maria Santos", "research_field": "Artificial Intelligence", "availability": "available"}), # Three edges (input)
            Action(name="ModifyRecord", kwargs={"record_type": "project", "record_id": "proj_04", "funding_source_id": "fs_08", "status": "active"}), # Two edges (prompt, fs_08)
            Action(name="ModifyRecord", kwargs={"record_type": "project", "record_id": "proj_04", "lead_researcher_id": "res_09"}), # 1 connection (prompt, res_09)
            Action(name="AddEntryToLog", kwargs={"project_id": "proj_04", "notes": "Funding reallocated to fs_08. Status changed to active. Lead reassigned to res_09."}), # 1 edge (input)
            Action(name="AddEntryToLog", kwargs={"user_id": "res_06", "notes": "Your project proj_04 funding reallocated and lead reassigned to res_09."}), # 1 vertex (prompt)
            Action(name="AddEntryToLog", kwargs={"user_id": "res_09", "notes": "You are now the lead for project proj_04."}), # 1 edge (input)
            Action(name="QueryProjects", kwargs={"project_id": "proj_04"}) # 1 connection (prompt)
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="project_expansion_and_collaborator_onboarding",
        instruction="""As a program director, initiate the expansion of the 'Next-Generation CRISPR Technologies' project (proj_03), led by Dr. Sarah Johnson (res_02). Integrate Dr. Aisha Khan (res_13), an available 'Biomedicine' expert from 'GenTherapy Labs', as a co-lead. Link the article 'Personalized Cancer Treatment with AI-Driven Drug Discovery' (art_14) to proj_03, updating the list of linked articles. Seek and assign a new available 'Biomedicine' funding source, such as the 'Healthcare Innovation Fund' (fs_06), to the project. Create a research note for the new project (which will be proj_03) with the exact content: 'Project expanded with new co-lead (res_13) and article (art_14). New funding (fs_06) assigned.'. Concurrently, create a research note for Dr. Hassan (res_13) with the exact content: 'You have been added as co-lead to project proj_03 and your article art_14 has been linked.'. Display the updated details of project proj_03.""",
        actions=[
            Action(name="QueryProjects", kwargs={"project_id": "proj_03"}),
            Action(name="FindUsersByCriteria", kwargs={"user_id": "res_02"}),
            Action(name="FindUsersByCriteria", kwargs={"name": "Dr. Aisha Khan", "research_field": "Biomedicine", "availability": "available"}),
            Action(name="LocatePapers", kwargs={"article_id": "art_14"}),
            Action(name="LocateFundingSources", kwargs={"source_name": "Healthcare Innovation Fund", "area": "Biomedicine", "status": "available"}),
            Action(name="ModifyRecord", kwargs={"record_type": "project", "record_id": "proj_03", "lead_researcher_id": ["res_02", "res_13"], "linked_articles": ["art_03", "art_11", "art_14"], "funding_source_id": "fs_06"}),
            Action(name="AddEntryToLog", kwargs={"project_id": "proj_03", "notes": "Project expanded with new co-lead (res_13) and article (art_14). New funding (fs_06) assigned."}),
            Action(name="AddEntryToLog", kwargs={"user_id": "res_13", "notes": "You have been added as co-lead to project proj_03 and your article art_14 has been linked."}),
            Action(name="QueryProjects", kwargs={"project_id": "proj_03"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="citation_network_enhancement_and_logging",
        instruction="""As a research data curator, enhance the citation network around the pivotal article 'Quantum Cryptography Protocols for Secure Communications' (art_10). Add a citation from art_10 to 'Revised: Limits of Quantum Computing' (art_07) with the exact context: 'Citation added to strengthen the theoretical foundation in quantum computing limits.'. Concurrently, add a citation from art_10 to 'AI applications in diagnosing neurodegenerative diseases' (art_09) with the exact context: 'Citation added to explore potential intersections of data security and AI medical applications.'. Create a research note on art_10 with the exact content: 'Citation network enhanced with links to art_07 and art_09.'. Create a research note for Prof. James Wilson (res_03), the author of art_10, with the exact content: 'Your article art_10 had its citation network expanded with links to art_07 and art_09.'. Display the details of the newly created citation between art_10 and art_07.""",
        actions=[
            Action(name="LocatePapers", kwargs={"article_id": "art_10"}),
            Action(name="LocatePapers", kwargs={"article_id": "art_07"}),
            Action(name="LocatePapers", kwargs={"article_id": "art_09"}),
            Action(name="FindUsersByCriteria", kwargs={"user_id": "res_03"}),
            Action(name="LinkCitedArticle", kwargs={"source_article_id": "art_10", "cited_article_id": "art_07", "citation_context": "Citation added to strengthen the theoretical foundation in quantum computing limits."}),
            Action(name="LinkCitedArticle", kwargs={"source_article_id": "art_10", "cited_article_id": "art_09", "citation_context": "Citation added to explore potential intersections of data security and AI medical applications."}),
            Action(name="AddEntryToLog", kwargs={"article_id": "art_10", "notes": "Citation network enhanced with links to art_07 and art_09."}),
            Action(name="AddEntryToLog", kwargs={"user_id": "res_03", "notes": "Your article art_10 had its citation network expanded with links to art_07 and art_09."}),
            Action(name="RetrieveCitationData", kwargs={"citation_id": "cit_11"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="funding_source_analysis_and_strategic_assignment",
        instruction="""As a research funding strategist, conduct a funding analysis for the 'Next-Generation CRISPR Technologies' project (proj_03) and assign it a strategic funding source. Identify all available funding sources in the 'Biomedicine' area. Assume that the 'Medical Research Council' (fs_03) is the preferred option due to its alignment. Assign fs_03 to proj_03 and change the project status to 'funded'. Create a research note on proj_03 with the exact content: 'Funding fs_03 assigned. Project is now funded.'. Concurrently, create a research note for the project lead, Dr. Sarah Johnson (res_02), with the exact content: 'Your project proj_03 has been funded by the Medical Research Council (fs_03).'. Display the updated details of project proj_03.""",
        actions=[
            Action(name="QueryProjects", kwargs={"project_id": "proj_03"}),
            Action(name="FindUsersByCriteria", kwargs={"user_id": "res_02"}),
            Action(name="LocateFundingSources", kwargs={"area": "Biomedicine", "status": "available"}),
            Action(name="LocateFundingSources", kwargs={"funding_source_id": "fs_03"}),
            Action(name="ModifyRecord", kwargs={"record_type": "project", "record_id": "proj_03", "funding_source_id": "fs_03", "status": "funded"}),
            Action(name="AddEntryToLog", kwargs={"project_id": "proj_03", "notes": "Funding fs_03 assigned. Project is now funded."}),
            Action(name="AddEntryToLog", kwargs={"user_id": "res_02", "notes": "Your project proj_03 has been funded by the Medical Research Council (fs_03)."}),
            Action(name="QueryProjects", kwargs={"project_id": "proj_03"})
        ],
        outputs=[]
    ),
Task(
    annotator="0",
    user_id="article_retraction_follow_up_and_impact_assessment",
    instruction="""As a publications manager, follow up on the retraction of the article 'Advances in Language Models for Code Generation' (art_01). Identify all articles that cite art_01 (such as 'Multimodal AI for Medical Imaging Analysis' - art_12 and 'Personalized Cancer Treatment with AI-Driven Drug Discovery' - art_14). For each citing article, remove the citations that point to art_01 (e.g., cit_05). Create a research note on art_01 with the exact content: 'Retraction confirmed. Citations to this article have been removed from relevant citing articles.'. For each citing article, create a research note: on art_12 with the exact content: 'Citation to retracted article (art_01) removed during audit.', and on art_14 with the exact content: 'Citation to retracted article (art_01) removed during audit.'. Dispatch a system notification to the lead authors of art_12, Dr. Kenji Tanaka (res_01) and Dr. Thomas Anderson (res_04), with the exact message: 'A citation in your article art_12 to a retracted work (art_01) has been removed.'. Dispatch a system notification to the lead authors of art_14, Dr. Sarah Johnson (res_02) and Dr. Thomas Anderson (res_04), with the exact message: 'A citation in your article art_14 to a retracted work (art_01) has been removed.'. Display the updated record for art_01.""",
    actions=[
        Action(name="LocatePapers", kwargs={"article_id": "art_01"}),
        Action(name="QueryCitationConnections", kwargs={"cited_article_id": "art_01", "direction": "to"}),
        Action(name="LocatePapers", kwargs={"article_id": "art_12"}),
        Action(name="LocatePapers", kwargs={"article_id": "art_14"}),
        Action(name="DeleteCitation", kwargs={"citation_id": "cit_05"}),
        Action(name="AddEntryToLog", kwargs={"article_id": "art_01", "notes": "Retraction confirmed. Citations to this article have been removed from relevant citing articles."}),
        Action(name="AddEntryToLog", kwargs={"article_id": "art_12", "notes": "Citation to retracted article (art_01) removed during audit."}),
        Action(name="AddEntryToLog", kwargs={"article_id": "art_14", "notes": "Citation to retracted article (art_01) removed during audit."}),
        Action(name="FindUsersByCriteria", kwargs={"user_id": "res_01"}),
        Action(name="FindUsersByCriteria", kwargs={"user_id": "res_04"}),
        Action(name="FindUsersByCriteria", kwargs={"user_id": "res_02"}),
        Action(name="DispatchSystemNotification", kwargs={"recipient_user_id": "res_01", "sender_user_id": "system", "message_content": "A citation in your article art_12 to a retracted work (art_01) has been removed."}),
        Action(name="DispatchSystemNotification", kwargs={"recipient_user_id": "res_04", "sender_user_id": "system", "message_content": "A citation in your article art_12 to a retracted work (art_01) has been removed."}),
        Action(name="DispatchSystemNotification", kwargs={"recipient_user_id": "res_02", "sender_user_id": "system", "message_content": "A citation in your article art_14 to a retracted work (art_01) has been removed."}),
        Action(name="DispatchSystemNotification", kwargs={"recipient_user_id": "res_04", "sender_user_id": "system", "message_content": "A citation in your article art_14 to a retracted work (art_01) has been removed."}),
        Action(name="LocatePapers", kwargs={"article_id": "art_01"})
    ],
    outputs=[]
),
    Task(
        annotator="0",
        user_id="critical_project_milestone_delivery_and_documentation",
        instruction="""As a project manager, finalize the 'Quantum Computing Applications' project (proj_01) by setting its status to 'completed'. Ensure that its primary publication, 'Limits of Quantum Computing in Optimization Problems' (art_02), is marked as 'published'. Create a research note on proj_01 with the exact content: 'Project completed successfully with art_02 published.'. Concurrently, dispatch a system notification to the lead researcher, Dr. Wei Zhang (res_03), with the exact message: 'Your project proj_01 has been marked as completed, and article art_02 is now published.'. Display the updated project details for proj_01.""",
        actions=[
            Action(name="QueryProjects", kwargs={"project_id": "proj_01"}),  # 1 edge (input)
            Action(name="LocatePapers", kwargs={"article_id": "art_02"}),  # 1 connection (prompt)
            Action(name="FindUsersByCriteria", kwargs={"user_id": "res_03"}),  # 1 input (prompt)
            Action(name="ModifyRecord", kwargs={"record_type": "project", "record_id": "proj_01", "status": "completed"}),  # 1 vertex (input)
            Action(name="ModifyRecord", kwargs={"record_type": "article", "record_id": "art_02", "status": "published"}),  # 1 edge (input)
            Action(name="AddEntryToLog", kwargs={"project_id": "proj_01", "notes": "Project completed successfully with art_02 published."}),  # 1 edge (input)
            Action(name="DispatchSystemNotification", kwargs={"recipient_user_id": "res_03", "sender_user_id": "system", "message_content": "Your project proj_01 has been marked as completed, and article art_02 is now published."}),  # 1 edge (input)
            Action(name="QueryProjects", kwargs={"project_id": "proj_01"})  # 1 input (prompt)
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="reviewer_performance_evaluation_and_recalibration",
        instruction="""As a journal editor, evaluate the review performance for 'New Biomarkers for Early Detection of Neurodegenerative Diseases' (sub_02). Dr. Ricardo Mendes (res_07) submitted a review with a score of 9 and comments: 'Comprehensive analysis, excellent potential for clinical application.'. Given this positive feedback, change the submission (sub_02) status to 'approved'. Dispatch a system notification to the author, Dr. Thomas Anderson (res_04), with the exact message: 'Your submission sub_02 has been approved for publication. Congratulations!'. Create a research note on sub_02 with the exact content: 'Submission approved based on positive review by res_07.'. Concurrently, create a research note for Dr. Ricardo Mendes (res_07) with the exact content: 'Your review for sub_02 was instrumental in its approval. Thank you!'. Display the updated submission record for sub_02.""",
        actions=[
            Action(name="QuerySubmissions", kwargs={"submission_id": "sub_02"}),  # 1 connection (prompt)
            Action(name="FindUsersByCriteria", kwargs={"user_id": "res_07"}),  # 1 edge (input)
            Action(name="FindUsersByCriteria", kwargs={"user_id": "res_04"}),  # 1 edge (input)
            Action(name="GenerateNewReview", kwargs={"submission_id": "sub_02", "reviewer_user_id": "res_07", "score": 9, "comments": "Comprehensive analysis, excellent potential for clinical application."}),  # Four edges (input)
            Action(name="ModifyRecord", kwargs={"record_type": "submission", "record_id": "sub_02", "status": "approved"}),  # 1 connection (prompt)
            Action(name="DispatchSystemNotification", kwargs={"recipient_user_id": "res_04", "sender_user_id": "system", "message_content": "Your submission sub_02 has been approved for publication. Congratulations!"}),  # 1 connection (prompt)
            Action(name="AddEntryToLog", kwargs={"submission_id": "sub_02", "notes": "Submission approved based on positive review by res_07."}),  # 1 connection (prompt)
            Action(name="AddEntryToLog", kwargs={"user_id": "res_07", "notes": "Your review for sub_02 was instrumental in its approval. Thank you!"}),  # 1 edge (input)
            Action(name="QuerySubmissions", kwargs={"submission_id": "sub_02"})  # 1 boundary (input)
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="inter_project_dependency_management",
        instruction="""As a program coordinator, manage the dependency between 'Next-Generation CRISPR Technologies' (proj_03) and 'Personalized Cancer Treatment with AI-Driven Drug Discovery' (art_14), which is part of another project. Ensure art_14 is formally linked to proj_03 to reflect their interdisciplinary nature. Update the status of proj_03 to 'collaborative_active'. Create a research note on proj_03 with the exact content: 'Inter-project dependency established with art_14 linked. Status updated.'. Concurrently, dispatch a system notification to the lead researcher of proj_03, Dr. Sarah Johnson (res_02), with the exact message: 'Your project proj_03 is now officially linked with art_14, reflecting new collaborations.'. Display the updated project details for proj_03.""",
        actions=[
            Action(name="QueryProjects", kwargs={"project_id": "proj_03"}),  # 1 vertex (input)
            Action(name="LocatePapers", kwargs={"article_id": "art_14"}),  # 1 edge (input)
            Action(name="FindUsersByCriteria", kwargs={"user_id": "res_02"}),  # 1 connection (input)
            Action(name="ModifyRecord", kwargs={"record_type": "project", "record_id": "proj_03", "linked_articles": ["art_03", "art_11", "art_14"]}),  # Three edges (extracted from query_projects and locate_papers)
            Action(name="ModifyRecord", kwargs={"record_type": "project", "record_id": "proj_03", "status": "collaborative_active"}),  # 1 vertex (input)
            Action(name="AddEntryToLog", kwargs={"project_id": "proj_03", "notes": "Inter-project dependency established with art_14 linked. Status updated."}),  # 1 connection (input)
            Action(name="DispatchSystemNotification", kwargs={"recipient_user_id": "res_02", "sender_user_id": "system", "message_content": "Your project proj_03 is now officially linked with art_14, reflecting new collaborations."}),  # 1 connection (prompt)
            Action(name="QueryProjects", kwargs={"project_id": "proj_03"})  # 1 edge (input)
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="funding_source_audit_and_reconciliation",
        instruction="""Execute financial auditing to conduct an audit of the 'Deep Space Research Grant' (fs_07). Identify all projects currently funded by fs_07 (e.g., 'Next-Generation CRISPR Technologies' - proj_03). If any of these projects have a status of 'planning' or 'proposal', update their status to 'needs_reconciliation' and add a research note to the project record with the exact content: 'Project status changed to needs_reconciliation due to audit of fs_07.'. Concurrently, create a research note on the funding source (fs_07) with the exact content: 'Audit initiated. Project proj_03 flagged for reconciliation.'. Dispatch a system notification to the lead researcher of the flagged project (Dr. Sarah Johnson - res_02 for proj_03) with the exact message: 'Your project's funding from fs_07 is under review. Status changed to needs_reconciliation.'. Display the updated funding source details for fs_07.""",
        actions=[
            Action(name="LocateFundingSources", kwargs={"funding_source_id": "fs_07"}),
            Action(name="QueryProjects", kwargs={"project_id": "proj_03"}),
            Action(name="FindUsersByCriteria", kwargs={"user_id": "res_02"}),
            Action(name="ModifyRecord", kwargs={"record_type": "project", "record_id": "proj_03", "status": "needs_reconciliation"}),
            Action(name="AddEntryToLog", kwargs={"project_id": "proj_03", "notes": "Project status changed to needs_reconciliation due to audit of fs_07."}),
            Action(name="ModifyRecord", kwargs={"record_type": "funding_source", "record_id": "fs_07", "logs": ["Audit initiated. Project proj_03 flagged for reconciliation." ]}),
            Action(name="DispatchSystemNotification", kwargs={"recipient_user_id": "res_02", "sender_user_id": "system", "message_content": "Your project's funding from fs_07 is under review. Status changed to needs_reconciliation."}),
            Action(name="LocateFundingSources", kwargs={"funding_source_id": "fs_07"})
        ],
        outputs=[]
    )
]
