
tasks = [
    {
        "annotator": 0,
        "user_id": "project_manager_01",
        "instruction": "Execute project management to establish a new research project: 'AI for Drug Discovery' (proj_ai_drug_discovery), led by Dr. Sarah Johnson (res_02), focusing on Biomedicine. Secure the 'Medical Research Council' (fs_03), an available 'Biomedicine' funding source with at least $500,000. If the assigned grant's amount is under $700,000 (which it will be if fs_03 is chosen), create a research log for Dr. Mendes (res_02) noting the need for co-funding (exact log content: 'Grant amount under $700,000. Co-funding required.', relevance: 'medium', for article art_14). Link Dr. Mendes's articles, 'Gene Editing Techniques with CRISPR-Cas9' (art_03) and 'Personalized Cancer Treatment with AI-Driven Drug Discovery' (art_14), to this project. Finally, notify Dr. Mendes (res_02) with the exact message: 'Your new project 'AI for Drug Discovery' has been created with project ID proj_ai_drug_discovery. It is funded by the 'Medical Research Council'.'. Display the final project details.",
        "actions": [
            {
                "name": "FindUsers",
                "arguments": {
                    "name": "Dr. Sarah Johnson"
                },
            },
            {
                "name": "FindPublications",
                "arguments": {
                    "author_name": "Dr. Sarah Johnson",
                    "title": "Gene Editing Techniques"
                },
            },
            {
                "name": "FindPublications",
                "arguments": {
                    "author_name": "Dr. Sarah Johnson",
                    "title": "Personalized Cancer Treatment"
                },
            },
            {
                "name": "FindGrants",
                "arguments": {
                    "funding_source_id": "fs_03"
                },
            },
            {
                "name": "LaunchProject",
                "arguments": {
                    "project_name": "AI for Drug Discovery",
                    "lead_researcher_id": "res_02",
                    "funding_source_id": "fs_03",
                    "project_id_override": "proj_ai_drug_discovery"
                },
            },
            {
                "name": "CreateResearchLog",
                "arguments": {
                    "researcher_id": "res_02",
                    "article_id": "art_14",
                    "notes": "Grant amount under $700,000. Co-funding required.",
                    "relevance": "medium"
                },
            },
            {
                "name": "LinkArticleToProject",
                "arguments": {
                    "project_id": "proj_ai_drug_discovery",
                    "article_id": "art_03"
                },
            },
            {
                "name": "LinkArticleToProject",
                "arguments": {
                    "project_id": "proj_ai_drug_discovery",
                    "article_id": "art_14"
                },
            },
            {
                "name": "NotifyUser",
                "arguments": {
                    "recipient_user_id": "res_02",
                    "message_content": "Your new project 'AI for Drug Discovery' has been created with project ID proj_ai_drug_discovery. It is funded by the 'Medical Research Council'."
                },
            },
            {
                "name": "FindProjects",
                "arguments": {
                    "project_id": "proj_ai_drug_discovery"
                }
            }
        ],
        "outputs": [
                "\"project_name\": \"AI for Drug Discovery\"",
                "\"lead_researcher_id\": \"res_02\"",
                "\"funding_source_id\": \"fs_03\"",
                "\"linked_articles\": [\n    \"art_03\",\n    \"art_14\"\n  ]"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "manager_01",
        "instruction": "Handle management duties to assign a new reviewer for the submission 'New Biomarkers for Early Detection' (art_04 / sub_02). Identify an available 'Biomedicine' expert (Dr. Ricardo Mendes - res_07), excluding the author. Set her notification preference to 'email' to ensure her profile is complete. Based on the reviewer's notification preferences, send a notification (res_07) with the exact message: 'You have been assigned to review the submission 'New Biomarkers for Early Detection'.'. Update the submission status to 'under_review'. Dispatch a notification to the author (res_02) with the exact message: 'A reviewer has been assigned to your submission regarding 'New Biomarkers for Early Detection'.'. Create a research log for the author (res_02) with the exact content: 'Submission status updated to 'under_review' after assigning a new reviewer.', with 'medium' relevance, for article art_04. Display the updated submission details.",
        "actions": [
            {
                "name": "FindPublications",
                "arguments": {
                    "title": "New Biomarkers for Early Detection"
                },
            },
            {
                "name": "LookupSubmissions",
                "arguments": {
                    "article_id": "art_04"
                },
            },
            {
                "name": "FindUsers",
                "arguments": {
                    "user_id": "res_02"
                },
            },
            {
                "name": "FindUsers",
                "arguments": {
                    "research_field": "Biomedicine",
                    "availability": "available"
                },
            },
            {
                "name": "UpdateUserPreferences",
                "arguments": {
                    "user_id": "res_07",
                    "notification_channel": "email"
                },
            },
            {
                "name": "AppointReviewer",
                "arguments": {
                    "submission_id": "sub_02",
                    "reviewer_user_id": "res_07"
                },
            },
            {
                "name": "GetUserPreferences",
                "arguments": {
                    "user_id": "res_07"
                },
            },
            {
                "name": "NotifyUser",
                "arguments": {
                    "recipient_user_id": "res_07",
                    "message_content": "You have been assigned to review the submission 'New Biomarkers for Early Detection'."
                },
            },
            {
                "name": "ModifySubmissionStatus",
                "arguments": {
                    "submission_id": "sub_02",
                    "new_status": "under_review"
                },
            },
            {
                "name": "NotifyUser",
                "arguments": {
                    "recipient_user_id": "res_02",
                    "message_content": "A reviewer has been assigned to your submission regarding 'New Biomarkers for Early Detection'."
                },
            },
            {
                "name": "CreateResearchLog",
                "arguments": {
                    "researcher_id": "res_02",
                    "article_id": "art_04",
                    "notes": "Submission status updated to 'under_review' after assigning a new reviewer.",
                    "relevance": "medium"
                },
            },
            {
                "name": "LookupSubmissions",
                "arguments": {
                    "submission_id": "sub_02"
                }
            }
        ],
        "outputs": [
                "\"status\": \"under_review\"",
                "\"assigned_reviewers\": [\n    \"res_07\"\n  ]"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "ethics_officer_01",
        "instruction": "Conduct ethics oversight to verify a potential academic connection between Dr. Kenji Tanaka (res_01), author of 'Advances in Language Models for Code Generation' (art_01), and Dr. Sarah Johnson (res_02). Determine if Dr. Souza has cited any articles by Dr. Mendes. If a citation exists (e.g., art_01 citing art_02), create a research log for Dr. Souza (res_01) with the exact content: 'Potential conflict of interest: Cited article by Dr. Sarah Johnson.', relevance 'high', for article art_01. Provide a summary of the citing article (art_01). Also, confirm if Dr. Souza is subscribed to the 'Biomedicine' topic. If she is not, update her subscription to include 'Biomedicine'. Display the full user details for both Dr. Souza and Dr. Mendes for your records, along with a summary of Dr. Souza's article 'Advances in Language Models for Code Generation' (art_01).",
        "actions": [
            {
                "name": "FindUsers",
                "arguments": {
                    "name": "Dr. Kenji Tanaka"
                },
            },
            {
                "name": "FindUsers",
                "arguments": {
                    "name": "Dr. Sarah Johnson"
                },
            },
            {
                "name": "FindPublications",
                "arguments": {
                    "author_name": "Dr. Kenji Tanaka"
                },
            },
            {
                "name": "FindReferences",
                "arguments": {
                    "article_id": "art_01",
                    "direction": "from"
                },
            },
            {
                "name": "CreateResearchLog",
                "arguments": {
                    "researcher_id": "res_01",
                    "article_id": "art_01",
                    "notes": "Potential conflict of interest: Cited article by Dr. Sarah Johnson.",
                    "relevance": "high"
                },
            },
            {
                "name": "SummarizeArticleText",
                "arguments": {
                    "article_id": "art_01"
                },
            },
            {
                "name": "GetUserSubscriptions",
                "arguments": {
                    "user_id": "res_01"
                },
            },
            {
                "name": "UpdateUserSubscriptions",
                "arguments": {
                    "user_id": "res_01",
                    "topic": "Biomedicine",
                    "action": "add"
                },
            },
            {
                "name": "FindUsers",
                "arguments": {
                    "user_id": "res_01"
                },
            },
            {
                "name": "FindUsers",
                "arguments": {
                    "user_id": "res_02"
                }
            }
        ],
        "outputs": [
                "\"summary\": \"This paper explores the evolution of transformer architectures and their application in generating code across multiple programming languages. We analyze the efficiency and accuracy of the latest models.\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "funder_manager_01",
        "instruction": "Manage funding operations to re-establish funding for the 'Quantum Computing Applications' project (proj_01) after its original grant was depleted. Find and assign a new, available 'General Science' funding source, the 'Environmental Science Foundation' (fs_09), to 'proj_01'. Temporarily set the project status to 'on_hold'. Dispatch a notification to the lead researcher (res_03) with the exact message: 'Funding for project 'Quantum Computing Applications' has been changed. Status is now 'on_hold'.'. Create a research log for the lead researcher (res_03) with the exact content: 'Project funding source depleted and replaced. Status moved to on_hold pending confirmation.', with relevance 'high', for article art_02. Display the updated project details.",
        "actions": [
            {
                "name": "FindProjects",
                "arguments": {
                    "project_name": "Quantum Computing Applications"
                },
            },
            {
                "name": "FindProjects",
                "arguments": {
                    "project_id": "proj_01"
                },
            },
            {
                "name": "FindGrants",
                "arguments": {
                    "focus_area": "General Science",
                    "status": "available"
                },
            },
            {
                "name": "AssignFundingToProject",
                "arguments": {
                    "project_id": "proj_01",
                    "funding_source_id": "fs_09"
                },
            },
            {
                "name": "ModifyProjectStatus",
                "arguments": {
                    "project_id": "proj_01",
                    "new_status": "on_hold"
                },
            },
            {
                "name": "FindUsers",
                "arguments": {
                    "user_id": "res_03"
                },
            },
            {
                "name": "NotifyUser",
                "arguments": {
                    "recipient_user_id": "res_03",
                    "message_content": "Funding for project 'Quantum Computing Applications' has been changed. Status is now 'on_hold'."
                },
            },
            {
                "name": "CreateResearchLog",
                "arguments": {
                    "researcher_id": "res_03",
                    "article_id": "art_02",
                    "notes": "Project funding source depleted and replaced. Status moved to on_hold pending confirmation.",
                    "relevance": "high"
                },
            },
            {
                "name": "FindProjects",
                "arguments": {
                    "project_id": "proj_01"
                }
            }
        ],
        "outputs": [
                "\"status\": \"on_hold\"",
                "\"funding_source_id\": \"fs_09\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "mentor_01",
        "instruction": "Provide mentorship guidance to help Dr. Thomas Anderson (res_04) expand her research scope by subscribing her to the 'AI' topic. Identify a highly-cited AI article from 2024, such as 'Advances in Language Models for Code Generation' (art_01). If she hasn't created a research log about it, create one for her (res_04) with the exact content: 'Recommendation: This is a highly-cited article in your new field of interest (AI).', with relevance 'medium', for article art_01. Dispatch a notification to Dr. Bauer (res_04) with a summary of 'art_01' and the exact message: 'Based on your new interest in AI, you may find this article interesting: 'Advances in Language Models for Code Generation'...'. Display her updated topic subscriptions.",
        "actions": [
            {
                "name": "FindUsers",
                "arguments": {
                    "name": "Dr. Thomas Anderson"
                },
            },
            {
                "name": "UpdateUserSubscriptions",
                "arguments": {
                    "user_id": "res_04",
                    "topic": "AI",
                    "action": "add"
                },
            },
            {
                "name": "FindPublications",
                "arguments": {
                    "topic": "AI",
                    "publication_year": 2024
                },
            },
            {
                "name": "FindReferences",
                "arguments": {
                    "article_id": "art_01",
                    "direction": "to"
                },
            },
            {
                "name": "SearchResearchLogs",
                "arguments": {
                    "researcher_id": "res_04",
                    "article_id": "art_01"
                },
            },
            {
                "name": "CreateResearchLog",
                "arguments": {
                    "researcher_id": "res_04",
                    "article_id": "art_01",
                    "notes": "Recommendation: This is a highly-cited article in your new field of interest (AI).",
                    "relevance": "medium"
                },
            },
            {
                "name": "SummarizeArticleText",
                "arguments": {
                    "article_id": "art_01"
                },
            },
            {
                "name": "NotifyUser",
                "arguments": {
                    "recipient_user_id": "res_04",
                    "message_content": "Based on your new interest in AI, you may find this article interesting: 'Advances in Language Models for Code Generation'..."
                },
            },
            {
                "name": "GetUserSubscriptions",
                "arguments": {
                    "user_id": "res_04"
                }
            }
        ],
        "outputs": [
                "\"topic\": \"Biomedicine\"",
                "\"topic\": \"AI\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "admin_01",
        "instruction": "Execute administrative duties to finalize the 'Next-Generation CRISPR Technologies' project (proj_03). Update its status to 'completed' and set the end date to '2025-06-28'. Create a final research log for the lead researcher, Dr. Sarah Johnson (res_02), with the exact content: 'Project 'Next-Generation CRISPR Technologies' has been marked as completed.', with relevance 'high', for article art_03. Unsubscribe Dr. Mendes (res_02) from the 'Biomedicine' topic and change his notification preference to 'none'. Dispatch a notification to him (res_02) with the exact message: 'Your project 'Next-Generation CRISPR Technologies' is complete. Your preferences and subscriptions have been updated.'. Display the final project details.",
        "actions": [
            {
                "name": "FindProjects",
                "arguments": {
                    "project_name": "Next-Generation CRISPR Technologies"
                },
            },
            {
                "name": "ModifyProjectStatus",
                "arguments": {
                    "project_id": "proj_03",
                    "new_status": "completed",
                    "end_date": "2025-06-28"
                },
            },
            {
                "name": "FindUsers",
                "arguments": {
                    "name": "Dr. Sarah Johnson"
                },
            },
            {
                "name": "CreateResearchLog",
                "arguments": {
                    "researcher_id": "res_02",
                    "article_id": "art_03",
                    "notes": "Project 'Next-Generation CRISPR Technologies' has been marked as completed.",
                    "relevance": "high"
                },
            },
            {
                "name": "UpdateUserSubscriptions",
                "arguments": {
                    "user_id": "res_02",
                    "topic": "Biomedicine",
                    "action": "remove"
                },
            },
            {
                "name": "UpdateUserPreferences",
                "arguments": {
                    "user_id": "res_02",
                    "notification_channel": "none"
                },
            },
            {
                "name": "NotifyUser",
                "arguments": {
                    "recipient_user_id": "res_02",
                    "message_content": "Your project 'Next-Generation CRISPR Technologies' is complete. Your preferences and subscriptions have been updated."
                },
            },
            {
                "name": "FindProjects",
                "arguments": {
                    "project_id": "proj_03"
                }
            }
        ],
        "outputs": [
                "\"project_id\": \"proj_03\"",
                "\"status\": \"completed\"",
                "\"end_date\": \"2025-06-28\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "auditor_01",
        "instruction": "Conduct auditing procedures to generate a full activity report for Dr. Kenji Tanaka (res_01). The report should include all articles she has authored, review recommendations for any of her submissions, all her personal research logs (log_001, log_008), and her current topic subscriptions. Additionally, find all projects she leads. After compiling this report, create a research log for Dr. Souza (res_01) with the exact content: 'Activity report compiled for audit.', with relevance 'medium', for article art_01. Display the IDs of all her personal research logs as part of the confirmation.",
        "actions": [
            {
                "name": "FindUsers",
                "arguments": {
                    "name": "Dr. Kenji Tanaka"
                },
            },
            {
                "name": "FindPublications",
                "arguments": {
                    "author_name": "Dr. Kenji Tanaka"
                },
            },
            {
                "name": "LookupSubmissions",
                "arguments": {
                    "author_user_id": "res_01"
                },
            },
            {
                "name": "GetReviewsForSubmission",
                "arguments": {
                    "submission_id": "sub_03"
                },
            },
            {
                "name": "SearchResearchLogs",
                "arguments": {
                    "researcher_id": "res_01"
                },
            },
            {
                "name": "FindProjects",
                "arguments": {
                    "lead_researcher_id": "res_01"
                },
            },
            {
                "name": "GetUserSubscriptions",
                "arguments": {
                    "user_id": "res_01"
                },
            },
            {
                "name": "FindUsers",
                "arguments": {
                    "user_id": "res_01"
                },
            },
            {
                "name": "CreateResearchLog",
                "arguments": {
                    "researcher_id": "res_01",
                    "article_id": "art_01",
                    "notes": "Activity report compiled for audit.",
                    "relevance": "medium"
                }
            }
        ],
        "outputs": [
                "\"log_id\": \"log_001\"",
                "\"log_id\": \"log_008\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "collaboration_manager_01",
        "instruction": "Manage collaboration initiatives to foster a new interdisciplinary collaboration. Identify an available 'Astrophysics' researcher (Dr. Carlos Silva - res_11) and an available 'Artificial Intelligence' researcher (Dr. Sofia Bauer - res_12). If they are not already collaborating on a project, create a new project titled 'Astro-AI Research Initiative' (proj_astro_ai_initiative), with Dr. Ruiz (res_11) as the lead and Dr. Johnson (res_12) as a team member. Assign an available 'General Science' grant, the 'Environmental Science Foundation' (fs_09), to this project. Dispatch a notification to Dr. Ruiz (res_11) with the exact message: 'You have been assigned as lead on a new project: 'Astro-AI Research Initiative'.'. Concurrently, dispatch a notification to Dr. Johnson (res_12) with the exact message: 'You have been added to the team for a new project: 'Astro-AI Research Initiative'.'. Display the final project details.",
        "actions": [
            {
                "name": "FindUsers",
                "arguments": {
                    "research_field": "Astrophysics",
                    "availability": "available"
                },
            },
            {
                "name": "FindUsers",
                "arguments": {
                    "research_field": "Artificial Intelligence",
                    "availability": "available"
                },
            },
            {
                "name": "FindProjects",
                "arguments": {
                    "lead_researcher_id": "res_11"
                },
            },
            {
                "name": "LaunchProject",
                "arguments": {
                    "project_name": "Astro-AI Research Initiative",
                    "lead_researcher_id": "res_11",
                    "project_id_override": "proj_astro_ai_initiative"
                },
            },
            {
                "name": "AddResearcherToProjectTeam",
                "arguments": {
                    "project_id": "proj_astro_ai_initiative",
                    "user_id": "res_12"
                },
            },
            {
                "name": "FindGrants",
                "arguments": {
                    "focus_area": "General Science",
                    "status": "available"
                },
            },
            {
                "name": "AssignFundingToProject",
                "arguments": {
                    "project_id": "proj_astro_ai_initiative",
                    "funding_source_id": "fs_09"
                },
            },
            {
                "name": "NotifyUser",
                "arguments": {
                    "recipient_user_id": "res_11",
                    "message_content": "You have been assigned as lead on a new project: 'Astro-AI Research Initiative'."
                },
            },
            {
                "name": "NotifyUser",
                "arguments": {
                    "recipient_user_id": "res_12",
                    "message_content": "You have been added to the team for a new project: 'Astro-AI Research Initiative'."
                },
            },
            {
                "name": "FindProjects",
                "arguments": {
                    "project_id": "proj_astro_ai_initiative"
                }
            }
        ],
        "outputs": [
                "\"project_name\": \"Astro-AI Research Initiative\"",
                "\"lead_researcher_id\": \"res_11\"",
                "\"team_members\": [\n    \"res_12\"\n  ]",
                "\"funding_source_id\": \"fs_09\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "submissions_manager_02",
        "instruction": "Handle submissions management to assign a reviewer for 'Multimodal AI for Medical Imaging Analysis' (art_12 / sub_03). Identify an available 'Artificial Intelligence' expert (Dr. Kenji Tanaka - res_01) not from the author. Perform a conflict of interest check: if Dr. Souza (res_01) has co-authored with Dr. Thomas Anderson (res_04), create a research log for Dr. Souza (res_01) with the exact content: 'Potential conflict of interest detected: Reviewer Dr. Kenji Tanaka (res_01) has co-authored with Dr. Thomas Anderson.'. Then, assign a different suitable expert (Dr. Sofia Bauer - res_12) as reviewer. Update the submission's status to 'under_review'. Notify the author (Dr. Kenji Tanaka - res_01) with the exact message: 'A reviewer has been assigned to your submission 'Multimodal AI for Medical Imaging Analysis'.'. Display the updated submission details.",
        "actions": [
            {
                "name": "FindPublications",
                "arguments": {
                    "title": "Multimodal AI for Medical Imaging Analysis"
                },
            },
            {
                "name": "LookupSubmissions",
                "arguments": {
                    "article_id": "art_12"
                },
            },
            {
                "name": "FindUsers",
                "arguments": {
                    "user_id": "res_01"
                },
            },
            {
                "name": "FindUsers",
                "arguments": {
                    "research_field": "Artificial Intelligence",
                    "availability": "available"
                },
            },
            {
                "name": "FindPublications",
                "arguments": {
                    "author_name": "Dr. Kenji Tanaka"
                },
            },
            {
                "name": "FindPublications",
                "arguments": {
                    "author_name": "Dr. Thomas Anderson"
                },
            },
            {
                "name": "CreateResearchLog",
                "arguments": {
                    "researcher_id": "res_01",
                    "article_id": "art_12",
                    "notes": "Potential conflict of interest detected: Reviewer Dr. Kenji Tanaka (res_01) has co-authored with Dr. Thomas Anderson.",
                    "relevance": "high"
                },
            },
            {
                "name": "AppointReviewer",
                "arguments": {
                    "submission_id": "sub_03",
                    "reviewer_user_id": "res_12"
                },
            },
            {
                "name": "ModifySubmissionStatus",
                "arguments": {
                    "submission_id": "sub_03",
                    "new_status": "under_review"
                },
            },
            {
                "name": "NotifyUser",
                "arguments": {
                    "recipient_user_id": "res_01",
                    "message_content": "A reviewer has been assigned to your submission 'Multimodal AI for Medical Imaging Analysis'."
                },
            },
            {
                "name": "LookupSubmissions",
                "arguments": {
                    "submission_id": "sub_03"
                }
            }
        ],
        "outputs": [
                "\"status\": \"under_review\"",
                "\"assigned_reviewers\": [\n    \"res_05\",\n    \"res_04\",\n    \"res_12\"\n  ]"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "funder_manager_02",
        "instruction": "Manage funding operations to secure funding for the 'Federated AI Systems' project (proj_04). Identify and assign an available 'AI' funding source with at least $200,000, specifically the 'Quantum Computing Initiative' (fs_10). Assign 'fs_10' to 'proj_04' and set the project status to 'active'. Create a research log for the lead researcher, Dr. Anna Petrov (res_06), with the exact content: 'Project fully funded and activated.', with relevance 'high', for article art_06. Dispatch a notification to Dr. Khan (res_06) with the exact message: 'Project 'Federated AI Systems' has been fully funded by 'Quantum Computing Initiative' and is now active.'. Display the final project details.",
        "actions": [
            {
                "name": "FindProjects",
                "arguments": {
                    "project_name": "Federated AI Systems"
                },
            },
            {
                "name": "FindGrants",
                "arguments": {
                    "focus_area": "AI",
                    "status": "available"
                },
            },
            {
                "name": "AssignFundingToProject",
                "arguments": {
                    "project_id": "proj_04",
                    "funding_source_id": "fs_10"
                },
            },
            {
                "name": "ModifyProjectStatus",
                "arguments": {
                    "project_id": "proj_04",
                    "new_status": "active"
                },
            },
            {
                "name": "FindProjects",
                "arguments": {
                    "project_id": "proj_04"
                },
            },
            {
                "name": "FindUsers",
                "arguments": {
                    "user_id": "res_06"
                },
            },
            {
                "name": "NotifyUser",
                "arguments": {
                    "recipient_user_id": "res_06",
                    "message_content": "Project 'Federated AI Systems' has been fully funded by 'Quantum Computing Initiative' and is now active."
                },
            },
            {
                "name": "CreateResearchLog",
                "arguments": {
                    "researcher_id": "res_06",
                    "article_id": "art_06",
                    "notes": "Project fully funded and activated.",
                    "relevance": "high"
                },
            },
            {
                "name": "FindProjects",
                "arguments": {
                    "project_id": "proj_04"
                }
            }
        ],
        "outputs": [
                "\"status\": \"active\"",
                "\"funding_source_id\": \"fs_10\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "project_lead_02",
        "instruction": "Execute lead researcher duties for 'Quantum Cryptography Networks' (proj_06), reactivate the project. Find all articles authored by Dr. Wei Zhang (res_17) on 'Quantum Physics' (art_02, art_07, art_10) and link them to the project. Add Dr. Anna Petrov (res_06) to the project team. Update the project status from 'proposal' to 'active'. Dispatch a notification to yourself (res_03) with the exact message: 'Your project 'Quantum Cryptography Networks' is now active and updated with new articles.'. Concurrently, dispatch a notification to Dr. Khan (res_06) with a summary of 'Revised: Limits of Quantum Computing' (art_07) and the exact message: 'You've been added to the 'Quantum Cryptography Networks' project. Here is a summary of a key article: An updated analysis of quantum computing...'. Display the final project details.",
        "actions": [
            {
                "name": "FindProjects",
                "arguments": {
                    "project_name": "Quantum Cryptography Networks"
                },
            },
            {
                "name": "FindUsers",
                "arguments": {
                    "name": "Dr. Wei Zhang"
                },
            },
            {
                "name": "FindPublications",
                "arguments": {
                    "author_name": "Dr. Wei Zhang",
                    "topic": "Quantum Physics"
                },
            },
            {
                "name": "LinkArticleToProject",
                "arguments": {
                    "project_id": "proj_06",
                    "article_id": "art_02"
                },
            },
            {
                "name": "LinkArticleToProject",
                "arguments": {
                    "project_id": "proj_06",
                    "article_id": "art_07"
                },
            },
            {
                "name": "FindUsers",
                "arguments": {
                    "name": "Dr. Anna Petrov"
                },
            },
            {
                "name": "AddResearcherToProjectTeam",
                "arguments": {
                    "project_id": "proj_06",
                    "user_id": "res_06"
                },
            },
            {
                "name": "ModifyProjectStatus",
                "arguments": {
                    "project_id": "proj_06",
                    "new_status": "active"
                },
            },
            {
                "name": "SummarizeArticleText",
                "arguments": {
                    "article_id": "art_07"
                },
            },
            {
                "name": "NotifyUser",
                "arguments": {
                    "recipient_user_id": "res_03",
                    "message_content": "Your project 'Quantum Cryptography Networks' is now active and updated with new articles."
                },
            },
            {
                "name": "NotifyUser",
                "arguments": {
                    "recipient_user_id": "res_06",
                    "message_content": "You've been added to the 'Quantum Cryptography Networks' project. Here is a summary of a key article: An updated analysis of quantum computing..."
                },
            },
            {
                "name": "FindProjects",
                "arguments": {
                    "project_id": "proj_06"
                }
            }
        ],
        "outputs": [
                "\"status\": \"active\"",
                "\"linked_articles\": [\n    \"art_10\",\n    \"art_02\",\n    \"art_07\"\n  ]",
                "\"team_members\": [\n    \"res_06\"\n  ]"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "journal_editor_01",
        "instruction": "Conduct journal editorial duties to perform a conflict of interest check for Dr. Sarah Johnson (res_02) as a potential reviewer for an article by Dr. Kenji Tanaka (res_01). Determine if Dr. Mendes has ever co-authored an article with Dr. Souza, or if he is a member of any projects she leads. Additionally, check if any article authored by Dr. Souza cites an article by Dr. Mendes. If any of these conditions indicate a potential conflict (e.g. mutual authorship, project leadership overlap, or a direct citation), create a research log documenting this potential conflict for Dr. Mendes (res_02) with the exact content: 'Potential conflict of interest identified with Dr. Kenji Tanaka.', for article art_01, with relevance 'high'. Regardless of the conflict check outcome, retrieve all research logs written by Dr. Mendes. Also, display the full details of both researchers, including their topic subscriptions, for your records.",
        "actions": [
            {
                "name": "FindUsers",
                "arguments": {
                    "name": "Dr. Sarah Johnson"
                },
            },
            {
                "name": "FindUsers",
                "arguments": {
                    "name": "Dr. Kenji Tanaka"
                },
            },
            {
                "name": "FindPublications",
                "arguments": {
                    "author_name": "Dr. Kenji Tanaka"
                },
            },
            {
                "name": "FindProjects",
                "arguments": {
                    "lead_researcher_id": "res_01"
                },
            },
            {
                "name": "FindReferences",
                "arguments": {
                    "article_id": "art_01",
                    "direction": "from"
                },
            },
            {
                "name": "CreateResearchLog",
                "arguments": {
                    "researcher_id": "res_02",
                    "article_id": "art_01",
                    "notes": "Potential conflict of interest identified with Dr. Kenji Tanaka.",
                    "relevance": "high"
                },
            },
            {
                "name": "SearchResearchLogs",
                "arguments": {
                    "researcher_id": "res_02"
                },
            },
            {
                "name": "FindUsers",
                "arguments": {
                    "user_id": "res_01"
                },
            },
            {
                "name": "FindUsers",
                "arguments": {
                    "user_id": "res_02"
                },
            },
            {
                "name": "GetUserSubscriptions",
                "arguments": {
                    "user_id": "res_01"
                },
            },
            {
                "name": "GetUserSubscriptions",
                "arguments": {
                    "user_id": "res_02"
                }
            }
        ],
        "outputs": [
                "\"log_id\": \"log_002\"",
                "\"log_id\": \"log_003\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "academic_advisor_01",
        "instruction": "Provide academic advisory services to identify Dr. Liu Wei (res_05), a researcher subscribed to the 'Astrophysics' topic. For Dr. Tanaka, find his most recent article. Identify 'Gravitational Wave Detection from Binary Black Holes' (art_13) that he has not yet logged. If such an article exists, dispatch a notification to him (res_05) including a summary of 'art_13' and the exact message: 'Recommendation based on your interest in Astrophysics: 'Gravitational Wave Detection... A new study on...''. As part of a system-wide UI update, ensure his UI theme preference is 'dark'. Display the updated user preferences for Dr. Tanaka.",
        "actions": [
            {
                "name": "FindUsers",
                "arguments": {
                    "user_id": "res_05"
                },
            },
            {
                "name": "FindPublications",
                "arguments": {
                    "author_name": "Dr. Liu Wei"
                },
            },
            {
                "name": "SearchResearchLogs",
                "arguments": {
                    "researcher_id": "res_05",
                    "article_id": "art_13"
                },
            },
            {
                "name": "SummarizeArticleText",
                "arguments": {
                    "article_id": "art_13"
                },
            },
            {
                "name": "NotifyUser",
                "arguments": {
                    "recipient_user_id": "res_05",
                    "message_content": "Recommendation based on your interest in Astrophysics: 'Gravitational Wave Detection... A new study on...'."
                },
            },
            {
                "name": "UpdateUserPreferences",
                "arguments": {
                    "user_id": "res_05",
                    "ui_theme": "dark"
                },
            },
            {
                "name": "GetUserPreferences",
                "arguments": {
                    "user_id": "res_05"
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"res_05\"",
                "\"ui_theme\": \"dark\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "editor_in_chief_01",
        "instruction": "Execute editor-in-chief duties to finalize the decision for the article 'Quantum Cryptography Protocols' (art_10 / sub_04). Assign two available 'AI' expert reviewers: Dr. Kenji Tanaka (res_01) and Dr. Sofia Bauer (res_12). Create two positive 'accept' reviews from them (from res_01 with 'Excellent work, clear accept.' and from res_12 with 'A significant contribution to the field.'). Update the submission status to 'accepted'. Find the linked project ('Quantum Cryptography Networks' - proj_06) and update its status to 'completed'. Dispatch a notification to the lead author, Prof. James Wilson (res_03), with the exact message: 'Congratulations, your submission 'Quantum Cryptography Protocols' has been accepted for publication!'. Display the final submission details.",
        "actions": [
            {
                "name": "FindPublications",
                "arguments": {
                    "title": "Quantum Cryptography Protocols"
                },
            },
            {
                "name": "LookupSubmissions",
                "arguments": {
                    "article_id": "art_10"
                },
            },
            {
                "name": "FindUsers",
                "arguments": {
                    "research_field": "AI",
                    "availability": "available"
                },
            },
            {
                "name": "FindUsers",
                "arguments": {
                    "research_field": "AI"
                },
            },
            {
                "name": "AppointReviewer",
                "arguments": {
                    "submission_id": "sub_04",
                    "reviewer_user_id": "res_01"
                },
            },
            {
                "name": "AppointReviewer",
                "arguments": {
                    "submission_id": "sub_04",
                    "reviewer_user_id": "res_12"
                },
            },
            {
                "name": "SubmitReview",
                "arguments": {
                    "submission_id": "sub_04",
                    "reviewer_user_id": "res_01",
                    "review_content": "Excellent work, clear accept.",
                    "recommendation": "accept"
                },
            },
            {
                "name": "SubmitReview",
                "arguments": {
                    "submission_id": "sub_04",
                    "reviewer_user_id": "res_12",
                    "review_content": "A significant contribution to the field.",
                    "recommendation": "accept"
                },
            },
            {
                "name": "ModifySubmissionStatus",
                "arguments": {
                    "submission_id": "sub_04",
                    "new_status": "accepted"
                },
            },
            {
                "name": "FindProjects",
                "arguments": {
                    "project_name": "Quantum Cryptography Networks"
                },
            },
            {
                "name": "ModifyProjectStatus",
                "arguments": {
                    "project_id": "proj_06",
                    "new_status": "completed"
                },
            },
            {
                "name": "FindUsers",
                "arguments": {
                    "user_id": "res_03"
                },
            },
            {
                "name": "NotifyUser",
                "arguments": {
                    "recipient_user_id": "res_03",
                    "message_content": "Congratulations, your submission 'Quantum Cryptography Protocols' has been accepted for publication!"
                },
            },
            {
                "name": "LookupSubmissions",
                "arguments": {
                    "submission_id": "sub_04"
                }
            }
        ],
        "outputs": [
                "\"submission_id\": \"sub_04\"",
                "\"status\": \"accepted\"",
                "\"assigned_reviewers\": [\n    \"res_02\",\n    \"res_06\",\n    \"res_01\",\n    \"res_12\"\n  ]"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "collaborator_02",
        "instruction": "Manage collaboration initiatives to foster future collaboration for Dr. Sarah Johnson (res_02) on his article 'Personalized Cancer Treatment with AI-Driven Drug Discovery' (art_14). Identify an available 'Biomedicine' researcher with relevant recent publications, such as Dr. Thomas Anderson (res_04). If Dr. Bauer (res_04) is not subscribed to the 'Biomedicine' topic, ensure she is subscribed. Dispatch a notification to Dr. Mendes (res_02) with the exact message: 'For future collaboration, consider Dr. Thomas Anderson. She recently published 'CRISPR-Cas12 Evolution...': A comparative analysis...'. Create a research log for Dr. Mendes (res_02) with the exact content: 'Suggested Dr. Thomas Anderson for collaboration on art_14.', with 'medium' relevance, for article art_14. Display the notification details, including its message content.",
        "actions": [
            {
                "name": "FindPublications",
                "arguments": {
                    "title": "Personalized Cancer Treatment"
                },
            },
            {
                "name": "LookupSubmissions",
                "arguments": {
                    "article_id": "art_14"
                },
            },
            {
                "name": "FindUsers",
                "arguments": {
                    "name": "Dr. Sarah Johnson"
                },
            },
            {
                "name": "FindUsers",
                "arguments": {
                    "research_field": "Biomedicine",
                    "availability": "available"
                },
            },
            {
                "name": "FindPublications",
                "arguments": {
                    "author_name": "Dr. Thomas Anderson"
                },
            },
            {
                "name": "GetUserSubscriptions",
                "arguments": {
                    "user_id": "res_04"
                },
            },
            {
                "name": "UpdateUserSubscriptions",
                "arguments": {
                    "user_id": "res_04",
                    "topic": "Biomedicine",
                    "action": "add"
                },
            },
            {
                "name": "SummarizeArticleText",
                "arguments": {
                    "article_id": "art_11"
                },
            },
            {
                "name": "NotifyUser",
                "arguments": {
                    "recipient_user_id": "res_02",
                    "message_content": "For future collaboration, consider Dr. Thomas Anderson. She recently published 'CRISPR-Cas12 Evolution...': A comparative analysis..."
                },
            },
            {
                "name": "CreateResearchLog",
                "arguments": {
                    "researcher_id": "res_02",
                    "article_id": "art_14",
                    "notes": "Suggested Dr. Thomas Anderson for collaboration on art_14.",
                    "relevance": "medium"
                }
            }
        ],
        "outputs": [
                "\"recipient_user_id\": \"res_02\"",
                "\"message_content\": \"For future collaboration, consider Dr. Thomas Anderson. She recently published 'CRISPR-Cas12 Evolution...': A comparative analysis...\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "editor_02",
        "instruction": "Conduct editorial duties to diversify the review panel for the submission 'Limits of Quantum Computing in Optimization Problems' (art_02 / sub_01), which already has an AI expert assigned. Add an available 'Quantum Physics' reviewer, Dr. Wei Zhang (res_17), to complete the interdisciplinary perspective. After assigning Dr. Zhang (res_17), update the submission's status to 'under_review'. Dispatch a notification to the author (Prof. James Wilson - res_03) with the exact message: 'Your submission 'Limits of Quantum Computing...' is now under review by a full panel.'. Dispatch a notification to the existing AI reviewer (Dr. Kenji Tanaka - res_01) with the exact message: 'A second reviewer has been assigned to 'Limits of Quantum Computing...''. Concurrently, dispatch a notification to Dr. Zhang (res_17) with the exact message: 'You have been assigned to review 'Limits of Quantum Computing...''. Display the updated submission details.",
        "actions": [
            {
                "name": "LookupSubmissions",
                "arguments": {
                    "submission_id": "sub_01"
                },
            },
            {
                "name": "FindUsers",
                "arguments": {
                    "research_field": "Quantum Physics",
                    "availability": "available"
                },
            },
            {
                "name": "AppointReviewer",
                "arguments": {
                    "submission_id": "sub_01",
                    "reviewer_user_id": "res_17"
                },
            },
            {
                "name": "ModifySubmissionStatus",
                "arguments": {
                    "submission_id": "sub_01",
                    "new_status": "under_review"
                },
            },
            {
                "name": "NotifyUser",
                "arguments": {
                    "recipient_user_id": "res_03",
                    "message_content": "Your submission 'Limits of Quantum Computing...' is now under review by a full panel."
                },
            },
            {
                "name": "NotifyUser",
                "arguments": {
                    "recipient_user_id": "res_01",
                    "message_content": "A second reviewer has been assigned to 'Limits of Quantum Computing...'."
                },
            },
            {
                "name": "NotifyUser",
                "arguments": {
                    "recipient_user_id": "res_17",
                    "message_content": "You have been assigned to review 'Limits of Quantum Computing...'."
                },
            },
            {
                "name": "LookupSubmissions",
                "arguments": {
                    "submission_id": "sub_01"
                }
            }
        ],
        "outputs": [
                "\"status\": \"under_review\"",
                "\"assigned_reviewers\": [\n    \"res_01\",\n    \"res_17\"\n  ]"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "submissions_manager_02",
        "instruction": "Handle submissions management to assign a reviewer for 'Multimodal AI for Medical Imaging Analysis' (art_12 / sub_03). Identify an available 'Artificial Intelligence' expert (Dr. Sofia Bauer - res_12) who is not the author. Perform a conflict of interest check: if Dr. Sofia Bauer (res_12) has co-authored with Dr. Kenji Tanaka (res_01), create a research log for Dr. Kenji Tanaka (res_01) with the exact content: 'Potential conflict of interest detected: Reviewer Dr. Sofia Bauer (res_12) has co-authored with Dr. Kenji Tanaka.', with 'high' relevance, for article art_12. Then, assign Dr. Sofia Bauer (res_12) as reviewer. Update the submission's status to 'under_review'. Notify the author (Dr. Kenji Tanaka - res_01) with the exact message: 'A reviewer has been assigned to your submission 'Multimodal AI for Medical Imaging Analysis'.'. Display the updated submission details.",
        "actions": [
            {
                "name": "FindPublications",
                "arguments": {
                    "title": "Multimodal AI for Medical Imaging Analysis"
                },
            },
            {
                "name": "LookupSubmissions",
                "arguments": {
                    "article_id": "art_12"
                },
            },
            {
                "name": "FindUsers",
                "arguments": {
                    "user_id": "res_01"
                },
            },
            {
                "name": "FindUsers",
                "arguments": {
                    "research_field": "Artificial Intelligence",
                    "availability": "available"
                },
            },
            {
                "name": "FindPublications",
                "arguments": {
                    "author_name": "Dr. Sofia Bauer"
                },
            },
            {
                "name": "FindPublications",
                "arguments": {
                    "author_name": "Dr. Kenji Tanaka"
                },
            },
            {
                "name": "AppointReviewer",
                "arguments": {
                    "submission_id": "sub_03",
                    "reviewer_user_id": "res_12"
                },
            },
            {
                "name": "ModifySubmissionStatus",
                "arguments": {
                    "submission_id": "sub_03",
                    "new_status": "under_review"
                },
            },
            {
                "name": "NotifyUser",
                "arguments": {
                    "recipient_user_id": "res_01",
                    "message_content": "A reviewer has been assigned to your submission 'Multimodal AI for Medical Imaging Analysis'."
                },
            },
            {
                "name": "LookupSubmissions",
                "arguments": {
                    "submission_id": "sub_03"
                }
            }
        ],
        "outputs": [
                "\"status\": \"under_review\"",
                "\"assigned_reviewers\": [\n    \"res_05\",\n    \"res_04\",\n    \"res_12\"\n  ]"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "research_director_01",
        "instruction": "Direct research operations to establish the new 'CRISPR Gene Therapy Trials' project (proj_crispr_trials). Assign Dr. Ana Oliveira (res_10) as the lead researcher, with Dr. Sarah Johnson (res_02) and Dr. Thomas Anderson (res_04) as team members. Find and assign an available 'Biomedicine' grant over $500,000, specifically the 'Medical Research Council' (fs_03), to 'proj_crispr_trials'. Link 'Gene Editing Techniques with CRISPR-Cas9' (art_03) to the project, and set its status to 'active'. Dispatch notifications to Dr. Oliveira (res_10) with the exact message: 'Your new project 'CRISPR Gene Therapy Trials' is active.'; to Dr. Mendes (res_02) with the exact message: 'You have been added to project 'CRISPR Gene Therapy Trials'.'; and to Dr. Bauer (res_04) with the exact message: 'You have been added to project 'CRISPR Gene Therapy Trials'.'. Display the final project details.",
        "actions": [
            {
                "name": "FindUsers",
                "arguments": {
                    "user_id": "res_10"
                },
            },
            {
                "name": "FindUsers",
                "arguments": {
                    "name": "Dr. Sarah Johnson"
                },
            },
            {
                "name": "FindUsers",
                "arguments": {
                    "name": "Dr. Thomas Anderson"
                },
            },
            {
                "name": "LaunchProject",
                "arguments": {
                    "project_name": "CRISPR Gene Therapy Trials",
                    "lead_researcher_id": "res_10",
                    "project_id_override": "proj_crispr_trials"
                },
            },
            {
                "name": "AddResearcherToProjectTeam",
                "arguments": {
                    "project_id": "proj_crispr_trials",
                    "user_id": "res_02"
                },
            },
            {
                "name": "AddResearcherToProjectTeam",
                "arguments": {
                    "project_id": "proj_crispr_trials",
                    "user_id": "res_04"
                },
            },
            {
                "name": "FindGrants",
                "arguments": {
                    "funding_source_id": "fs_03"
                },
            },
            {
                "name": "AssignFundingToProject",
                "arguments": {
                    "project_id": "proj_crispr_trials",
                    "funding_source_id": "fs_03"
                },
            },
            {
                "name": "FindPublications",
                "arguments": {
                    "title": "Gene Editing Techniques with CRISPR-Cas9"
                },
            },
            {
                "name": "LinkArticleToProject",
                "arguments": {
                    "project_id": "proj_crispr_trials",
                    "article_id": "art_03"
                },
            },
            {
                "name": "ModifyProjectStatus",
                "arguments": {
                    "project_id": "proj_crispr_trials",
                    "new_status": "active"
                },
            },
            {
                "name": "NotifyUser",
                "arguments": {
                    "recipient_user_id": "res_10",
                    "message_content": "Your new project 'CRISPR Gene Therapy Trials' is active."
                },
            },
            {
                "name": "NotifyUser",
                "arguments": {
                    "recipient_user_id": "res_02",
                    "message_content": "You have been added to project 'CRISPR Gene Therapy Trials'."
                },
            },
            {
                "name": "NotifyUser",
                "arguments": {
                    "recipient_user_id": "res_04",
                    "message_content": "You have been added to project 'CRISPR Gene Therapy Trials'."
                },
            },
            {
                "name": "FindProjects",
                "arguments": {
                    "project_id": "proj_crispr_trials"
                }
            }
        ],
        "outputs": [
                "\"project_name\": \"CRISPR Gene Therapy Trials\"",
                "\"lead_researcher_id\": \"res_10\"",
                "\"funding_source_id\": \"fs_03\"",
                "\"status\": \"active\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "submissions_manager_03",
        "instruction": "Handle submissions management to assign a reviewer for the submission 'New Biomarkers for Early Detection' (art_04 / sub_02). Identify an available 'Biomedicine' expert (Dr. Thomas Anderson - res_04) who is not the author (Dr. Sarah Johnson - res_02). Assess her capacity by checking if she leads more than one project. If suitable, assign Dr. Bauer (res_04) as the reviewer. Update the submission's status to 'under_review'. Dispatch a notification to the author (res_02) with the exact message: 'A reviewer has been assigned to your submission 'New Biomarkers for Early Detection'.'. Concurrently, dispatch a notification to Dr. Bauer (res_04) with the exact message: 'You have been assigned to review the submission 'New Biomarkers for Early Detection'.'. Display the updated submission details.",
        "actions": [
            {
                "name": "FindPublications",
                "arguments": {
                    "title": "New Biomarkers for Early Detection"
                },
            },
            {
                "name": "LookupSubmissions",
                "arguments": {
                    "article_id": "art_04"
                },
            },
            {
                "name": "FindUsers",
                "arguments": {
                    "research_field": "Biomedicine",
                    "availability": "available"
                },
            },
            {
                "name": "FindProjects",
                "arguments": {
                    "lead_researcher_id": "res_04"
                },
            },
            {
                "name": "FindProjects",
                "arguments": {
                    "lead_researcher_id": "res_07"
                },
            },
            {
                "name": "AppointReviewer",
                "arguments": {
                    "submission_id": "sub_02",
                    "reviewer_user_id": "res_04"
                },
            },
            {
                "name": "ModifySubmissionStatus",
                "arguments": {
                    "submission_id": "sub_02",
                    "new_status": "under_review"
                },
            },
            {
                "name": "FindUsers",
                "arguments": {
                    "user_id": "res_02"
                },
            },
            {
                "name": "NotifyUser",
                "arguments": {
                    "recipient_user_id": "res_02",
                    "message_content": "A reviewer has been assigned to your submission 'New Biomarkers for Early Detection'."
                },
            },
            {
                "name": "NotifyUser",
                "arguments": {
                    "recipient_user_id": "res_04",
                    "message_content": "You have been assigned to review the submission 'New Biomarkers for Early Detection'."
                },
            },
            {
                "name": "LookupSubmissions",
                "arguments": {
                    "submission_id": "sub_02"
                }
            }
        ],
        "outputs": [
                "\"submission_id\": \"sub_02\"",
                "\"status\": \"under_review\"",
                "\"assigned_reviewers\": [\n    \"res_04\"\n  ]"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "editor_in_chief_02",
        "instruction": "Execute editor-in-chief duties to process a new 'major_revisions' review submitted by Dr. Liu Wei (res_05) for 'Multimodal AI for Medical Imaging Analysis' (art_12 / sub_03). Create a research log for the author, Dr. Kenji Tanaka (res_01), with the exact content: 'Received 'major_revisions' from reviewer Dr. Liu Wei.', with 'high' relevance, for article art_12. Check if this is the second 'major_revisions' or 'reject' review for 'sub_03'. If so, update the submission status to 'rejected'. Otherwise (as is the case here, it's the first such review), dispatch a notification to Dr. Souza (res_01) with the exact message: 'A new review with 'major_revisions' has been submitted for your article 'Multimodal AI...'. Please revise your manuscript.'. Display the updated submission details.",
        "actions": [
            {
                "name": "FindPublications",
                "arguments": {
                    "title": "Multimodal AI for Medical Imaging Analysis"
                },
            },
            {
                "name": "LookupSubmissions",
                "arguments": {
                    "article_id": "art_12"
                },
            },
            {
                "name": "FindUsers",
                "arguments": {
                    "name": "Dr. Kenji Tanaka"
                },
            },
            {
                "name": "CreateResearchLog",
                "arguments": {
                    "researcher_id": "res_01",
                    "article_id": "art_12",
                    "notes": "Received 'major_revisions' from reviewer Dr. Liu Wei.",
                    "relevance": "high"
                },
            },
            {
                "name": "GetReviewsForSubmission",
                "arguments": {
                    "submission_id": "sub_03"
                },
            },
            {
                "name": "NotifyUser",
                "arguments": {
                    "recipient_user_id": "res_01",
                    "message_content": "A new review with 'major_revisions' has been submitted for your article 'Multimodal AI...'. Please revise your manuscript."
                },
            },
            {
                "name": "LookupSubmissions",
                "arguments": {
                    "submission_id": "sub_03"
                }
            }
        ],
        "outputs": [
                "\"submission_id\": \"sub_03\"",
                "\"status\": \"under_review\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "hr_admin_01",
        "instruction": "Handle HR administration to standardize profiles for researchers from 'FutureML' and integrate them into the 'Federated AI Systems' project. For each researcher from 'FutureML' (e.g., Dr. Kenji Tanaka - res_01, Dr. Elena Rossi - res_16), update their notification channel preference to 'email'. Add these researchers to the team of 'Federated AI Systems' (proj_04), if they are not already on it. Dispatch notifications to Dr. Souza (res_01) with the exact message: 'Your profile has been updated and you've been added to the 'Federated AI Systems' project.' and to Dr. Silva (res_16) with the exact message: 'Your profile has been updated and you've been added to the 'Federated AI Systems' project.'. Display the updated project details.",
        "actions": [
            {
                "name": "FindUsers",
                "arguments": {
                    "research_field": "Artificial Intelligence"
                },
            },
            {
                "name": "UpdateUserPreferences",
                "arguments": {
                    "user_id": "res_01",
                    "notification_channel": "email"
                },
            },
            {
                "name": "UpdateUserPreferences",
                "arguments": {
                    "user_id": "res_16",
                    "notification_channel": "email"
                },
            },
            {
                "name": "FindProjects",
                "arguments": {
                    "project_name": "Federated AI Systems"
                },
            },
            {
                "name": "AddResearcherToProjectTeam",
                "arguments": {
                    "project_id": "proj_04",
                    "user_id": "res_01"
                },
            },
            {
                "name": "AddResearcherToProjectTeam",
                "arguments": {
                    "project_id": "proj_04",
                    "user_id": "res_16"
                },
            },
            {
                "name": "NotifyUser",
                "arguments": {
                    "recipient_user_id": "res_01",
                    "message_content": "Your profile has been updated and you've been added to the 'Federated AI Systems' project."
                },
            },
            {
                "name": "NotifyUser",
                "arguments": {
                    "recipient_user_id": "res_16",
                    "message_content": "Your profile has been updated and you've been added to the 'Federated AI Systems' project."
                },
            },
            {
                "name": "FindProjects",
                "arguments": {
                    "project_id": "proj_04"
                }
            }
        ],
        "outputs": [
                "\"project_id\": \"proj_04\"",
                "\"team_members\": [\n    \"res_01\",\n    \"res_16\"\n  ]"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "researcher_06",
        "instruction": "Execute research activities as Dr. Anna Petrov (res_06), prepare a project proposal for the 'Machine Learning Excellence Award'. Create a new project titled 'Next-Gen Federated Learning' (proj_next_gen_fl) led by yourself. If you are not already subscribed to the 'General Science' topic, subscribe yourself. Link your article 'Federated Learning for Privacy-Preserving AI' (art_06) to the project. Assign the 'Machine Learning Excellence Award' (fs_08) grant to the project, setting its status to 'planning' as it is an application. Finally, dispatch a notification to yourself (res_06) with the exact message: 'Your project proposal 'Next-Gen Federated Learning' has been created.'. Display the final project details.",
        "actions": [
            {
                "name": "FindUsers",
                "arguments": {
                    "name": "Dr. Anna Petrov"
                },
            },
            {
                "name": "FindGrants",
                "arguments": {
                    "source_name": "Machine Learning Excellence Award"
                },
            },
            {
                "name": "GetUserSubscriptions",
                "arguments": {
                    "user_id": "res_06"
                },
            },
            {
                "name": "UpdateUserSubscriptions",
                "arguments": {
                    "user_id": "res_06",
                    "topic": "General Science",
                    "action": "add"
                },
            },
            {
                "name": "LaunchProject",
                "arguments": {
                    "project_name": "Next-Gen Federated Learning",
                    "lead_researcher_id": "res_06",
                    "project_id_override": "proj_next_gen_fl"
                },
            },
            {
                "name": "FindPublications",
                "arguments": {
                    "author_name": "Dr. Anna Petrov",
                    "title": "Federated Learning"
                },
            },
            {
                "name": "LinkArticleToProject",
                "arguments": {
                    "project_id": "proj_next_gen_fl",
                    "article_id": "art_06"
                },
            },
            {
                "name": "AssignFundingToProject",
                "arguments": {
                    "project_id": "proj_next_gen_fl",
                    "funding_source_id": "fs_08"
                },
            },
            {
                "name": "ModifyProjectStatus",
                "arguments": {
                    "project_id": "proj_next_gen_fl",
                    "new_status": "planning"
                },
            },
            {
                "name": "NotifyUser",
                "arguments": {
                    "recipient_user_id": "res_06",
                    "message_content": "Your project proposal 'Next-Gen Federated Learning' has been created."
                },
            },
            {
                "name": "FindProjects",
                "arguments": {
                    "project_id": "proj_next_gen_fl"
                }
            }
        ],
        "outputs": [
                "\"project_name\": \"Next-Gen Federated Learning\"",
                "\"status\": \"planning\"",
                "\"funding_source_id\": \"fs_08\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "research_director_03",
        "instruction": "Direct research operations to manage the allocation of the 'Medical Research Council' grant (fs_03). Identify the project 'Next-Generation CRISPR Technologies' (proj_03), which is an active project in Biomedicine led by Dr. Sarah Johnson (res_02). Ensure proj_03 is assigned to 'fs_03'. Then, based on Dr. Mendes's (res_02) notification preferences, dispatch a notification (e.g., in-app if 'in_app', otherwise email) about their newly assigned funding. Additionally, dispatch a notification to the head of the AI department, Dr. Kenji Tanaka (res_01), with the exact message: 'FYI: A new major grant from the Medical Research Council is now funding projects in Biomedicine.'. Create a research log for Dr. Souza (res_01) with the exact content: 'Noted new funding in Biomedicine (Medical Research Council grant) for collaboration potential.', with 'medium' relevance, for article art_01. Display the notification details for Dr. Souza.",
        "actions": [
            {
                "name": "FindGrants",
                "arguments": {
                    "funding_source_id": "fs_03"
                },
            },
            {
                "name": "FindProjects",
                "arguments": {
                    "project_id": "proj_03"
                },
            },
            {
                "name": "AssignFundingToProject",
                "arguments": {
                    "project_id": "proj_03",
                    "funding_source_id": "fs_03"
                },
            },
            {
                "name": "FindUsers",
                "arguments": {
                    "user_id": "res_02"
                },
            },
            {
                "name": "GetUserPreferences",
                "arguments": {
                    "user_id": "res_02"
                },
            },
            {
                "name": "NotifyUser",
                "arguments": {
                    "recipient_user_id": "res_02",
                    "message_content": "Your project 'Next-Generation CRISPR Technologies' has been assigned funding from the 'Medical Research Council'."
                },
            },
            {
                "name": "FindUsers",
                "arguments": {
                    "name": "Dr. Kenji Tanaka"
                },
            },
            {
                "name": "NotifyUser",
                "arguments": {
                    "recipient_user_id": "res_01",
                    "message_content": "FYI: A new major grant from the Medical Research Council is now funding projects in Biomedicine."
                },
            },
            {
                "name": "CreateResearchLog",
                "arguments": {
                    "researcher_id": "res_01",
                    "article_id": "art_01",
                    "notes": "Noted new funding in Biomedicine (Medical Research Council grant) for collaboration potential.",
                    "relevance": "medium"
                }
            }
        ],
        "outputs": [
                "\"recipient_user_id\": \"res_01\"",
                "\"message_content\": \"FYI: A new major grant from the Medical Research Council is now funding projects in Biomedicine.\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "submissions_manager_04",
        "instruction": "Handle submissions management to assign three reviewers for the new submission 'Personalized Cancer Treatment with AI-Driven Drug Discovery' (art_14 / sub_05). Identify three available 'Biomedicine' experts (Dr. Ricardo Mendes - res_07, Dr. Ana Oliveira - res_10, Dr. Aisha Khan - res_13). For each potential reviewer, verify no conflict of interest (co-authorship) with the article's authors (Dr. Mendes, Dr. Bauer, Dr. Silva). Assign these eligible reviewers to 'sub_05'. Update the submission's status to 'under_review'. Dispatch a notification to the lead author, Dr. Sarah Johnson (res_02), with the exact message: 'Three reviewers have been assigned to your submission 'Personalized Cancer Treatment...''. Concurrently, dispatch notifications to each reviewer (res_07, res_10, res_13) with the exact message: 'You have been assigned to review 'Personalized Cancer Treatment...''. Display the updated submission details.",
        "actions": [
            {
                "name": "FindPublications",
                "arguments": {
                    "title": "Personalized Cancer Treatment with AI-Driven Drug Discovery"
                },
            },
            {
                "name": "LookupSubmissions",
                "arguments": {
                    "article_id": "art_14"
                },
            },
            {
                "name": "FindUsers",
                "arguments": {
                    "name": "Dr. Sarah Johnson"
                },
            },
            {
                "name": "FindPublications",
                "arguments": {
                    "author_name": "Dr. Thomas Anderson"
                },
            },
            {
                "name": "FindPublications",
                "arguments": {
                    "author_name": "Dr. Elena Rossi"
                },
            },
            {
                "name": "FindUsers",
                "arguments": {
                    "research_field": "Biomedicine",
                    "availability": "available"
                },
            },
            {
                "name": "AppointReviewer",
                "arguments": {
                    "submission_id": "sub_05",
                    "reviewer_user_id": "res_07"
                },
            },
            {
                "name": "AppointReviewer",
                "arguments": {
                    "submission_id": "sub_05",
                    "reviewer_user_id": "res_10"
                },
            },
            {
                "name": "AppointReviewer",
                "arguments": {
                    "submission_id": "sub_05",
                    "reviewer_user_id": "res_13"
                },
            },
            {
                "name": "ModifySubmissionStatus",
                "arguments": {
                    "submission_id": "sub_05",
                    "new_status": "under_review"
                },
            },
            {
                "name": "NotifyUser",
                "arguments": {
                    "recipient_user_id": "res_02",
                    "message_content": "Three reviewers have been assigned to your submission 'Personalized Cancer Treatment...'."
                },
            },
            {
                "name": "NotifyUser",
                "arguments": {
                    "recipient_user_id": "res_07",
                    "message_content": "You have been assigned to review 'Personalized Cancer Treatment...'."
                },
            },
            {
                "name": "NotifyUser",
                "arguments": {
                    "recipient_user_id": "res_10",
                    "message_content": "You have been assigned to review 'Personalized Cancer Treatment...'."
                },
            },
            {
                "name": "NotifyUser",
                "arguments": {
                    "recipient_user_id": "res_13",
                    "message_content": "You have been assigned to review 'Personalized Cancer Treatment...'."
                },
            },
            {
                "name": "LookupSubmissions",
                "arguments": {
                    "submission_id": "sub_05"
                }
            }
        ],
        "outputs": [
                "\"status\": \"under_review\"",
                "\"assigned_reviewers\": [\n    \"res_07\",\n    \"res_10\",\n    \"res_13\"\n  ]"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "analyst_02",
        "instruction": "As an analyst, analyze the research impact of the 'MediCore' institution. Identify all researchers from this institution (e.g., Dr. Sarah Johnson - res_02). For each researcher, find all their published articles and count the total number of times they have been cited across all their papers. Identify the researcher from MediCore with the most total citations. If this top researcher (Dr. Mendes) is not subscribed to the 'AI' topic, a major related field, create a research log for him (res_02) with the exact content: 'Strategic Gap: As a highly cited researcher, should consider subscribing to the 'AI' topic due to its growing relevance in Biomedicine.', with 'high' relevance, for article art_09. Finally, list all projects this top researcher is currently leading.",
        "actions": [
            {
                "name": "FindUsers",
                "arguments": {
                    "research_field": "Biomedicine"
                },
            },
            {
                "name": "FindPublications",
                "arguments": {
                    "author_name": "Dr. Sarah Johnson"
                },
            },
            {
                "name": "FindReferences",
                "arguments": {
                    "article_id": "art_03",
                    "direction": "to"
                },
            },
            {
                "name": "FindReferences",
                "arguments": {
                    "article_id": "art_09",
                    "direction": "to"
                },
            },
            {
                "name": "FindReferences",
                "arguments": {
                    "article_id": "art_14",
                    "direction": "to"
                },
            },
            {
                "name": "GetUserSubscriptions",
                "arguments": {
                    "user_id": "res_02"
                },
            },
            {
                "name": "CreateResearchLog",
                "arguments": {
                    "researcher_id": "res_02",
                    "article_id": "art_09",
                    "notes": "Strategic Gap: As a highly cited researcher, should consider subscribing to the 'AI' topic due to its growing relevance in Biomedicine.",
                    "relevance": "high"
                },
            },
            {
                "name": "FindProjects",
                "arguments": {
                    "lead_researcher_id": "res_02"
                }
            }
        ],
        "outputs": [
                "\"project_id\": \"proj_03\"",
                "\"project_name\": \"Next-Generation CRISPR Technologies\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "collaborator_03",
        "instruction": "As a collaboration manager, establish a new project titled 'Quantum AI Synergy' (proj_quantum_ai_synergy), led by Dr. Kenji Tanaka (res_01). Add Prof. James Wilson (res_03) to the project team and assign the 'Quantum Computing Initiative' grant (fs_10). Find all articles co-authored by both researchers; if none exist, create a research log for Dr. Souza (res_01) with the exact content: 'New collaboration established with Prof. James Wilson on project Quantum AI Synergy.', with 'high' relevance, for article art_01. Finally, set the project status to 'active' and dispatch notifications to Dr. Souza (res_01) with the exact message: 'Your new project 'Quantum AI Synergy' is active.' and to Prof. James Wilson (res_03) with the exact message: 'You've been added to the 'Quantum AI Synergy' project.'. Display the final project details.",
        "actions": [
            {
                "name": "FindUsers",
                "arguments": {
                    "name": "Dr. Kenji Tanaka"
                },
            },
            {
                "name": "FindUsers",
                "arguments": {
                    "name": "Prof. James Wilson"
                },
            },
            {
                "name": "FindGrants",
                "arguments": {
                    "source_name": "Quantum Computing Initiative"
                },
            },
            {
                "name": "LaunchProject",
                "arguments": {
                    "project_name": "Quantum AI Synergy",
                    "lead_researcher_id": "res_01",
                    "project_id_override": "proj_quantum_ai_synergy"
                },
            },
            {
                "name": "AssignFundingToProject",
                "arguments": {
                    "project_id": "proj_quantum_ai_synergy",
                    "funding_source_id": "fs_10"
                },
            },
            {
                "name": "AddResearcherToProjectTeam",
                "arguments": {
                    "project_id": "proj_quantum_ai_synergy",
                    "user_id": "res_03"
                },
            },
            {
                "name": "FindPublications",
                "arguments": {
                    "author_name": "Dr. Kenji Tanaka"
                },
            },
            {
                "name": "FindPublications",
                "arguments": {
                    "author_name": "Prof. James Wilson"
                },
            },
            {
                "name": "CreateResearchLog",
                "arguments": {
                    "researcher_id": "res_01",
                    "article_id": "art_01",
                    "notes": "New collaboration established with Prof. James Wilson on project Quantum AI Synergy.",
                    "relevance": "high"
                },
            },
            {
                "name": "ModifyProjectStatus",
                "arguments": {
                    "project_id": "proj_quantum_ai_synergy",
                    "new_status": "active"
                },
            },
            {
                "name": "NotifyUser",
                "arguments": {
                    "recipient_user_id": "res_01",
                    "message_content": "Your new project 'Quantum AI Synergy' is active."
                },
            },
            {
                "name": "NotifyUser",
                "arguments": {
                    "recipient_user_id": "res_03",
                    "message_content": "You've been added to the 'Quantum AI Synergy' project."
                },
            },
            {
                "name": "FindProjects",
                "arguments": {
                    "project_id": "proj_quantum_ai_synergy"
                }
            }
        ],
        "outputs": [
                "\"project_name\": \"Quantum AI Synergy\"",
                "\"status\": \"active\"",
                "\"team_members\": [\n    \"res_03\"\n  ]"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "editor_03",
        "instruction": "As an editor, process the 'minor_revisions' review for the submission 'New Biomarkers for Early Detection' (art_04 / sub_02). Dispatch a notification to the author, Dr. Sarah Johnson (res_02), with the exact message: 'A 'minor_revisions' review was submitted for your article 'New Biomarkers for Early Detection'.'. Update his UI theme preference to 'light' to ensure he sees it. After a hypothetical revision period, update the submission status to 'under_review' and then immediately to 'accepted'. Update the linked project 'Next-Generation CRISPR Technologies' (proj_03) status to 'completed'. Create a research log for Dr. Mendes (res_02) with the exact content: 'Congratulations on navigating the review process. Your article 'New Biomarkers for Early Detection' is now accepted.', with 'high' relevance, for article art_04. Display the final submission details.",
        "actions": [
            {
                "name": "FindPublications",
                "arguments": {
                    "title": "New Biomarkers for Early Detection"
                },
            },
            {
                "name": "LookupSubmissions",
                "arguments": {
                    "submission_id": "sub_02"
                },
            },
            {
                "name": "FindUsers",
                "arguments": {
                    "name": "Dr. Sarah Johnson"
                },
            },
            {
                "name": "NotifyUser",
                "arguments": {
                    "recipient_user_id": "res_02",
                    "message_content": "A 'minor_revisions' review was submitted for your article 'New Biomarkers for Early Detection'."
                },
            },
            {
                "name": "UpdateUserPreferences",
                "arguments": {
                    "user_id": "res_02",
                    "ui_theme": "light"
                },
            },
            {
                "name": "ModifySubmissionStatus",
                "arguments": {
                    "submission_id": "sub_02",
                    "new_status": "under_review"
                },
            },
            {
                "name": "ModifySubmissionStatus",
                "arguments": {
                    "submission_id": "sub_02",
                    "new_status": "accepted"
                },
            },
            {
                "name": "FindProjects",
                "arguments": {
                    "project_name": "Next-Generation CRISPR Technologies"
                },
            },
            {
                "name": "ModifyProjectStatus",
                "arguments": {
                    "project_id": "proj_03",
                    "new_status": "completed"
                },
            },
            {
                "name": "CreateResearchLog",
                "arguments": {
                    "researcher_id": "res_02",
                    "article_id": "art_04",
                    "notes": "Congratulations on navigating the review process. Your article 'New Biomarkers for Early Detection' is now accepted.",
                    "relevance": "high"
                },
            },
            {
                "name": "LookupSubmissions",
                "arguments": {
                    "submission_id": "sub_02"
                }
            }
        ],
        "outputs": [
                "\"submission_id\": \"sub_02\"",
                "\"status\": \"accepted\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "funding_coordinator_01",
        "instruction": "As a funding coordinator, perform a funding-opportunity match for active projects lacking funding. For 'Exoplanet Atmospheric Analysis' (proj_02), identify its lead researcher's (Dr. Liu Wei - res_05) primary research field ('Astrophysics'). Find an available funding source matching this field, specifically the 'Space Exploration Fund' (fs_04), and assign it to 'proj_02'. Dispatch a notification to Dr. Tanaka (res_05) with the exact message: 'Your project 'Exoplanet Atmospheric Analysis' has been assigned funding from the 'Space Exploration Fund'.'. Create a research log for Dr. Tanaka (res_05) with the exact content: 'Project has been automatically matched and assigned funding source fs_04.', with 'high' relevance, for article art_08. Display the updated project details.",
        "actions": [
            {
                "name": "FindProjects",
                "arguments": {
                    "status": "active"
                },
            },
            {
                "name": "FindProjects",
                "arguments": {
                    "project_id": "proj_02"
                },
            },
            {
                "name": "FindUsers",
                "arguments": {
                    "user_id": "res_05"
                },
            },
            {
                "name": "FindGrants",
                "arguments": {
                    "focus_area": "Astrophysics",
                    "status": "available"
                },
            },
            {
                "name": "AssignFundingToProject",
                "arguments": {
                    "project_id": "proj_02",
                    "funding_source_id": "fs_04"
                },
            },
            {
                "name": "FindGrants",
                "arguments": {
                    "funding_source_id": "fs_04"
                },
            },
            {
                "name": "NotifyUser",
                "arguments": {
                    "recipient_user_id": "res_05",
                    "message_content": "Your project 'Exoplanet Atmospheric Analysis' has been assigned funding from the 'Space Exploration Fund'."
                },
            },
            {
                "name": "CreateResearchLog",
                "arguments": {
                    "researcher_id": "res_05",
                    "article_id": "art_08",
                    "notes": "Project has been automatically matched and assigned funding source fs_04.",
                    "relevance": "high"
                },
            },
            {
                "name": "FindProjects",
                "arguments": {
                    "project_id": "proj_02"
                }
            }
        ],
        "outputs": [
                "\"project_id\": \"proj_02\"",
                "\"funding_source_id\": \"fs_04\""
        ]
    }
    ,
    {
        "annotator": new_task_creator,
        "user_id": "data_governance_officer_01",
        "instruction": "As a data governance officer, ensure compliance and update researcher profiles. For Dr. Kenji Tanaka (res_01), retrieve her current user preferences. Change her UI theme preference to 'light'. Ensure she is subscribed to the 'AI' topic. Find her article 'Multimodal AI for Medical Imaging Analysis' (art_12) and retrieve its submission details. If the submission status is 'submitted', change it to 'under_review'. Create a research log for yourself (data_governance_officer_01) with the exact content: 'Profile and submission compliance reviewed for Dr. Souza.', with 'high' relevance, for article art_12. Finally, notify Dr. Kenji Tanaka (res_01) with the exact message: 'Your profile and article submission status have been updated for compliance.'. Display Dr. Souza's updated user preferences and the article's submission details.",
        "actions": [
            {
                "name": "FindUsers",
                "arguments": {
                    "user_id": "res_01"
                },
            },
            {
                "name": "GetUserPreferences",
                "arguments": {
                    "user_id": "res_01"
                },
            },
            {
                "name": "UpdateUserPreferences",
                "arguments": {
                    "user_id": "res_01",
                    "ui_theme": "light"
                },
            },
            {
                "name": "GetUserSubscriptions",
                "arguments": {
                    "user_id": "res_01"
                },
            },
            {
                "name": "UpdateUserSubscriptions",
                "arguments": {
                    "user_id": "res_01",
                    "topic": "AI",
                    "action": "add"
                },
            },
            {
                "name": "FindPublications",
                "arguments": {
                    "article_id": "art_12"
                },
            },
            {
                "name": "LookupSubmissions",
                "arguments": {
                    "article_id": "art_12"
                },
            },
            {
                "name": "ModifySubmissionStatus",
                "arguments": {
                    "submission_id": "sub_03",
                    "new_status": "under_review"
                },
            },
            {
                "name": "CreateResearchLog",
                "arguments": {
                    "researcher_id": "data_governance_officer_01",
                    "article_id": "art_12",
                    "notes": "Profile and submission compliance reviewed for Dr. Souza.",
                    "relevance": "high"
                },
            },
            {
                "name": "NotifyUser",
                "arguments": {
                    "recipient_user_id": "res_01",
                    "message_content": "Your profile and article submission status have been updated for compliance."
                },
            },
            {
                "name": "GetUserPreferences",
                "arguments": {
                    "user_id": "res_01"
                },
            },
            {
                "name": "LookupSubmissions",
                "arguments": {
                    "article_id": "art_12"
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"res_01\"",
                "\"ui_theme\": \"light\"",
                "\"submission_id\": \"sub_03\"",
                "\"status\": \"under_review\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "research_evaluator_01",
        "instruction": "As a research evaluator, assess the publication impact of Dr. Thomas Anderson (res_04) focusing on her Biomedicine articles. Find all articles she has authored on 'Biomedicine'. For each such article, retrieve all articles that cite it, and identify the topics of those citing articles. Then, for the most cited Biomedicine article by Dr. Bauer, get its submission details and summarize its content. If this article is not yet 'published', change its status to 'accepted'. Create a research log for Dr. Bauer (res_04) with the exact content: 'Impact analysis completed for your Biomedicine publications. Most cited article processed.', with 'high' relevance, for her most cited Biomedicine article. Finally, ensure Dr. Bauer (res_04) is subscribed to the 'General Science' topic. Display the updated submission details for the processed article.",
        "actions": [
            {
                "name": "FindUsers",
                "arguments": {
                    "name": "Dr. Thomas Anderson"
                },
            },
            {
                "name": "FindPublications",
                "arguments": {
                    "author_name": "Dr. Thomas Anderson",
                    "topic": "Biomedicine"
                },
            },
            {
                "name": "FindReferences",
                "arguments": {
                    "article_id": "art_04",
                    "direction": "to"
                },
            },
            {
                "name": "FindPublications",
                "arguments": {
                    "article_id": "art_14"
                },
            },
            {
                "name": "LookupSubmissions",
                "arguments": {
                    "article_id": "art_04"
                },
            },
            {
                "name": "SummarizeArticleText",
                "arguments": {
                    "article_id": "art_04"
                },
            },
            {
                "name": "ModifySubmissionStatus",
                "arguments": {
                    "submission_id": "sub_02",
                    "new_status": "accepted"
                },
            },
            {
                "name": "CreateResearchLog",
                "arguments": {
                    "researcher_id": "res_04",
                    "article_id": "art_04",
                    "notes": "Impact analysis completed for your Biomedicine publications. Most cited article processed.",
                    "relevance": "high"
                },
            },
            {
                "name": "UpdateUserSubscriptions",
                "arguments": {
                    "user_id": "res_04",
                    "topic": "General Science",
                    "action": "add"
                },
            },
            {
                "name": "LookupSubmissions",
                "arguments": {
                    "submission_id": "sub_02"
                }
            }
        ],
        "outputs": [
                "\"submission_id\": \"sub_02\"",
                "\"status\": \"accepted\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "reviewer_coordinator_01",
        "instruction": "As a reviewer coordinator, manage the review process for 'Limits of Quantum Computing in Optimization Problems' (art_02 / sub_01). Retrieve all current reviews for this submission. Based on the reviews, if there is at least one 'major_revisions' recommendation, dispatch a notification to the lead author, Prof. James Wilson (res_03), with the exact message: 'Your submission 'Limits of Quantum Computing...' requires major revisions. Please check the review details.'. If there is no 'major_revisions' but at least one 'minor_revisions', notify Prof. James Wilson (res_03) with: 'Your submission 'Limits of Quantum Computing...' requires minor revisions.'. Otherwise, if all reviews recommend 'accept', change the submission status to 'accepted' and notify Prof. James Wilson (res_03) with: 'Congratulations, your submission 'Limits of Quantum Computing...' has been accepted for publication!'. Finally, create a research log for yourself (reviewer_coordinator_01) with the exact content: 'Review process managed for sub_01.', with 'medium' relevance, for article art_02. Display the final submission details.",
        "actions": [
            {
                "name": "LookupSubmissions",
                "arguments": {
                    "article_id": "art_02"
                },
            },
            {
                "name": "GetReviewsForSubmission",
                "arguments": {
                    "submission_id": "sub_01"
                },
            },
            {
                "name": "FindUsers",
                "arguments": {
                    "name": "Prof. James Wilson"
                },
            },
            {
                "name": "GetUserPreferences",
                "arguments": {
                    "user_id": "res_03"
                },
            },
            {
                "name": "NotifyUser",
                "arguments": {
                    "recipient_user_id": "res_03",
                    "message_content": "Your submission 'Limits of Quantum Computing...' requires minor revisions."
                },
            },
            {
                "name": "CreateResearchLog",
                "arguments": {
                    "researcher_id": "reviewer_coordinator_01",
                    "article_id": "art_02",
                    "notes": "Review process managed for sub_01.",
                    "relevance": "medium"
                },
            },
            {
                "name": "LookupSubmissions",
                "arguments": {
                    "submission_id": "sub_01"
                },
            },
            {
                "name": "LookupSubmissions",
                "arguments": {
                    "submission_id": "sub_01",
                    "status": "under_review"
                },
            },
            {
                "name": "FindUsers",
                "arguments": {
                    "user_id": "res_01"
                },
            },
            {
                "name": "FindPublications",
                "arguments": {
                    "article_id": "art_02"
                }
            }
        ],
        "outputs": [
                "\"submission_id\": \"sub_01\"",
                "\"status\": \"under_review\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "collaboration_facilitator_01",
        "instruction": "As a collaboration facilitator, identify a potential inter-institutional collaboration between 'MediCore' and 'OrbitX' focused on Quantum Physics. Identify Dr. Sarah Johnson (res_02) from MediCore and Prof. James Wilson (res_03) from OrbitX. Check if they have co-authored any articles. If they haven't, create a research log for Dr. Mendes (res_02) with the exact content: 'Potential inter-institutional collaboration with Prof. James Wilson of OrbitX identified. No prior co-authorship found.', with 'medium' relevance, for article art_09. If Dr. Mendes is not subscribed to 'Astrophysics' (Prof. James Wilson's field), subscribe him to it. Propose a new joint project named 'Quantum Health Horizons' (proj_quantum_health) with Dr. Mendes as lead and Prof. James Wilson as a team member. Assign 'Innovation Technology Grant' (fs_05) as funding. Notify Dr. Mendes (res_02) with the exact message: 'New collaboration opportunity: 'Quantum Health Horizons' project initiated with Prof. James Wilson.'. Display the final project details.",
        "actions": [
            {
                "name": "FindUsers",
                "arguments": {
                    "name": "Dr. Sarah Johnson",
                    "institution": "MediCore"
                },
            },
            {
                "name": "FindUsers",
                "arguments": {
                    "name": "Prof. James Wilson",
                    "institution": "OrbitX"
                },
            },
            {
                "name": "FindPublications",
                "arguments": {
                    "author_name": "Dr. Sarah Johnson"
                },
            },
            {
                "name": "FindPublications",
                "arguments": {
                    "author_name": "Prof. James Wilson"
                },
            },
            {
                "name": "CreateResearchLog",
                "arguments": {
                    "researcher_id": "res_02",
                    "article_id": "art_09",
                    "notes": "Potential inter-institutional collaboration with Prof. James Wilson of OrbitX identified. No prior co-authorship found.",
                    "relevance": "medium"
                },
            },
            {
                "name": "GetUserSubscriptions",
                "arguments": {
                    "user_id": "res_02"
                },
            },
            {
                "name": "UpdateUserSubscriptions",
                "arguments": {
                    "user_id": "res_02",
                    "topic": "Astrophysics",
                    "action": "add"
                },
            },
            {
                "name": "LaunchProject",
                "arguments": {
                    "project_name": "Quantum Health Horizons",
                    "lead_researcher_id": "res_02",
                    "project_id_override": "proj_quantum_health"
                },
            },
            {
                "name": "AddResearcherToProjectTeam",
                "arguments": {
                    "project_id": "proj_quantum_health",
                    "user_id": "res_03"
                },
            },
            {
                "name": "FindGrants",
                "arguments": {
                    "source_name": "Innovation Technology Grant"
                },
            },
            {
                "name": "AssignFundingToProject",
                "arguments": {
                    "project_id": "proj_quantum_health",
                    "funding_source_id": "fs_05"
                },
            },
            {
                "name": "NotifyUser",
                "arguments": {
                    "recipient_user_id": "res_02",
                    "message_content": "New collaboration opportunity: 'Quantum Health Horizons' project initiated with Prof. James Wilson."
                },
            },
            {
                "name": "FindProjects",
                "arguments": {
                    "project_id": "proj_quantum_health"
                }
            }
        ],
        "outputs": [
                "\"project_name\": \"Quantum Health Horizons\"",
                "\"lead_researcher_id\": \"res_02\"",
                "\"team_members\": [\n    \"res_03\"\n  ]",
                "\"funding_source_id\": \"fs_05\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "compliance_auditor_01",
        "instruction": "As a compliance auditor, review funding allocation for the 'Federated AI Systems' project (proj_04). Verify its current funding source. If it is still funded by 'AI Advancement Grant' (fs_01), update its funding to 'Quantum Computing Initiative' (fs_10). Then, for the lead researcher of proj_04, Dr. Anna Petrov (res_06), update her notification preference to 'in_app' and ensure she is subscribed to 'General Science'. Dispatch a notification to Dr. Khan (res_06) with the exact message: 'Your project 'Federated AI Systems' funding has been reviewed for compliance and updated.'. Create a research log for Dr. Khan (res_06) with the exact content: 'Project funding compliance verified and updated.', with 'high' relevance, for article art_06. Display the final project details.",
        "actions": [
            {
                "name": "FindProjects",
                "arguments": {
                    "project_id": "proj_04"
                },
            },
            {
                "name": "FindGrants",
                "arguments": {
                    "funding_source_id": "fs_01"
                },
            },
            {
                "name": "FindGrants",
                "arguments": {
                    "funding_source_id": "fs_10"
                },
            },
            {
                "name": "AssignFundingToProject",
                "arguments": {
                    "project_id": "proj_04",
                    "funding_source_id": "fs_10"
                },
            },
            {
                "name": "FindUsers",
                "arguments": {
                    "user_id": "res_06"
                },
            },
            {
                "name": "GetUserPreferences",
                "arguments": {
                    "user_id": "res_06"
                },
            },
            {
                "name": "UpdateUserPreferences",
                "arguments": {
                    "user_id": "res_06",
                    "notification_channel": "in_app"
                },
            },
            {
                "name": "GetUserSubscriptions",
                "arguments": {
                    "user_id": "res_06"
                },
            },
            {
                "name": "UpdateUserSubscriptions",
                "arguments": {
                    "user_id": "res_06",
                    "topic": "General Science",
                    "action": "add"
                },
            },
            {
                "name": "NotifyUser",
                "arguments": {
                    "recipient_user_id": "res_06",
                    "message_content": "Your project 'Federated AI Systems' funding has been reviewed for compliance and updated."
                },
            },
            {
                "name": "CreateResearchLog",
                "arguments": {
                    "researcher_id": "res_06",
                    "article_id": "art_06",
                    "notes": "Project funding compliance verified and updated.",
                    "relevance": "high"
                },
            },
            {
                "name": "FindProjects",
                "arguments": {
                    "project_id": "proj_04"
                }
            }
        ],
        "outputs": [
                "\"project_id\": \"proj_04\"",
                "\"funding_source_id\": \"fs_10\"",
                "\"notification_channel\": \"in_app\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "ethics_committee_member_02",
        "instruction": "As an ethics committee member, investigate a complaint regarding potential plagiarism in 'Advances in Language Models for Code Generation' (art_01). Compare its content against 'Limits of Quantum Computing in Optimization Problems' (art_02) and 'Revised: Limits of Quantum Computing' (art_07). If there's significant overlap in concepts or phrasing with 'art_02' or 'art_07', create a critical research log for Dr. Kenji Tanaka (res_01) with the exact content: 'Plagiarism concern identified in article art_01 related to quantum computing articles.', with 'high' relevance, for article art_01. Additionally, revoke Dr. Souza's subscription to 'Quantum Physics'. Dispatch a notification to Dr. Souza (res_01) with the exact message: 'URGENT: A plagiarism concern has been raised regarding your article 'Advances in Language Models for Code Generation'.'. Display Dr. Souza's updated topic subscriptions.",
        "actions": [
            {
                "name": "FindPublications",
                "arguments": {
                    "article_id": "art_01"
                },
            },
            {
                "name": "FindPublications",
                "arguments": {
                    "article_id": "art_02"
                },
            },
            {
                "name": "FindPublications",
                "arguments": {
                    "article_id": "art_07"
                },
            },
            {
                "name": "SummarizeArticleText",
                "arguments": {
                    "article_id": "art_01"
                },
            },
            {
                "name": "SummarizeArticleText",
                "arguments": {
                    "article_id": "art_02"
                },
            },
            {
                "name": "SummarizeArticleText",
                "arguments": {
                    "article_id": "art_07"
                },
            },
            {
                "name": "CreateResearchLog",
                "arguments": {
                    "researcher_id": "res_01",
                    "article_id": "art_01",
                    "notes": "Plagiarism concern identified in article art_01 related to quantum computing articles.",
                    "relevance": "high"
                },
            },
            {
                "name": "GetUserSubscriptions",
                "arguments": {
                    "user_id": "res_01"
                },
            },
            {
                "name": "UpdateUserSubscriptions",
                "arguments": {
                    "user_id": "res_01",
                    "topic": "Quantum Physics",
                    "action": "remove"
                },
            },
            {
                "name": "NotifyUser",
                "arguments": {
                    "recipient_user_id": "res_01",
                    "message_content": "URGENT: A plagiarism concern has been raised regarding your article 'Advances in Language Models for Code Generation'."
                },
            },
            {
                "name": "GetUserSubscriptions",
                "arguments": {
                    "user_id": "res_01"
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"res_01\"",
                "\"topic\": \"AI\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "interdisciplinary_lead_01",
        "instruction": "As an interdisciplinary lead, identify a potential inter-institutional collaboration between 'MediCore' and 'OrbitX' focused on Quantum Physics. Identify Dr. Sarah Johnson (res_02) from MediCore and Prof. James Wilson (res_03) from OrbitX. Check if they have co-authored any articles. If they haven't co-authored but Dr. Souza (res_01) has cited Dr. Mendes's article 'Gene Editing Techniques with CRISPR-Cas9' (art_03), or if Dr. Mendes has cited Dr. Souza's 'Advances in Language Models for Code Generation' (art_01), create a research log for Dr. Mendes (res_02) with the exact content: 'Potential inter-institutional collaboration with Prof. James Wilson of OrbitX identified. Reciprocal citation indicates research overlap.', with 'medium' relevance, for article art_09. If Dr. Mendes is not subscribed to 'Astrophysics' (Prof. James Wilson's field), subscribe him to it. Propose a new joint project named 'Quantum Health Horizons' (proj_quantum_health) with Dr. Mendes as lead and Prof. James Wilson as a team member. Assign 'Innovation Technology Grant' (fs_05) as funding. Notify Dr. Mendes (res_02) with the exact message: 'New collaboration opportunity: Project 'Quantum Health Horizons' initiated with Prof. James Wilson, funded by Innovation Technology Grant.'. Display the final project details.",
        "actions": [
            {
                "name": "FindUsers",
                "arguments": {
                    "name": "Dr. Sarah Johnson",
                    "institution": "MediCore"
                },
            },
            {
                "name": "FindUsers",
                "arguments": {
                    "name": "Prof. James Wilson",
                    "institution": "OrbitX"
                },
            },
            {
                "name": "FindPublications",
                "arguments": {
                    "author_name": "Dr. Sarah Johnson"
                },
            },
            {
                "name": "FindPublications",
                "arguments": {
                    "author_name": "Prof. James Wilson"
                },
            },
            {
                "name": "FindReferences",
                "arguments": {
                    "article_id": "art_01",
                    "direction": "from"
                },
            },
            {
                "name": "FindReferences",
                "arguments": {
                    "article_id": "art_03",
                    "direction": "from"
                },
            },
            {
                "name": "CreateResearchLog",
                "arguments": {
                    "researcher_id": "res_02",
                    "article_id": "art_09",
                    "notes": "Potential inter-institutional collaboration with Prof. James Wilson of OrbitX identified. Reciprocal citation indicates research overlap.",
                    "relevance": "medium"
                },
            },
            {
                "name": "GetUserSubscriptions",
                "arguments": {
                    "user_id": "res_02"
                },
            },
            {
                "name": "UpdateUserSubscriptions",
                "arguments": {
                    "user_id": "res_02",
                    "topic": "Astrophysics",
                    "action": "add"
                },
            },
            {
                "name": "LaunchProject",
                "arguments": {
                    "project_name": "Quantum Health Horizons",
                    "lead_researcher_id": "res_02",
                    "project_id_override": "proj_quantum_health"
                },
            },
            {
                "name": "AddResearcherToProjectTeam",
                "arguments": {
                    "project_id": "proj_quantum_health",
                    "user_id": "res_03"
                },
            },
            {
                "name": "FindGrants",
                "arguments": {
                    "source_name": "Innovation Technology Grant"
                },
            },
            {
                "name": "AssignFundingToProject",
                "arguments": {
                    "project_id": "proj_quantum_health",
                    "funding_source_id": "fs_05"
                },
            },
            {
                "name": "NotifyUser",
                "arguments": {
                    "recipient_user_id": "res_02",
                    "message_content": "New collaboration opportunity: Project 'Quantum Health Horizons' initiated with Prof. James Wilson, funded by Innovation Technology Grant."
                },
            },
            {
                "name": "FindProjects",
                "arguments": {
                    "project_id": "proj_quantum_health"
                }
            }
        ],
        "outputs": [
                "\"project_name\": \"Quantum Health Horizons\"",
                "\"lead_researcher_id\": \"res_02\"",
                "\"team_members\": [\n    \"res_03\"\n  ]",
                "\"funding_source_id\": \"fs_05\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "research_lifecycle_manager_01",
        "instruction": "As a research lifecycle manager, ensure all recently 'completed' projects have their lead researchers' preferences updated and summary logs created. Specifically for 'Next-Generation CRISPR Technologies' (proj_03), ensure its end date is set to '2025-06-28'. For its lead researcher, Dr. Sarah Johnson (res_02), change his UI theme preference to 'dark'. Then, create a research log for Dr. Mendes (res_02) with the exact content: 'Project proj_03 completed and profile updated.', with 'low' relevance, for article art_03 (a linked article). Finally, dispatch a notification to Dr. Mendes (res_02) with the exact message: 'Your completed project status and profile have been updated.'. Display the final project details for proj_03.",
        "actions": [
            {
                "name": "FindProjects",
                "arguments": {
                    "project_id": "proj_03"
                },
            },
            {
                "name": "ModifyProjectStatus",
                "arguments": {
                    "project_id": "proj_03",
                    "new_status": "completed",
                    "end_date": "2025-06-28"
                },
            },
            {
                "name": "FindUsers",
                "arguments": {
                    "user_id": "res_02"
                },
            },
            {
                "name": "GetUserPreferences",
                "arguments": {
                    "user_id": "res_02"
                },
            },
            {
                "name": "UpdateUserPreferences",
                "arguments": {
                    "user_id": "res_02",
                    "ui_theme": "dark"
                },
            },
            {
                "name": "CreateResearchLog",
                "arguments": {
                    "researcher_id": "res_02",
                    "article_id": "art_03",
                    "notes": "Project proj_03 completed and profile updated.",
                    "relevance": "low"
                },
            },
            {
                "name": "NotifyUser",
                "arguments": {
                    "recipient_user_id": "res_02",
                    "message_content": "Your completed project status and profile have been updated."
                },
            },
            {
                "name": "FindProjects",
                "arguments": {
                    "project_id": "proj_03"
                }
            }
        ],
        "outputs": [
                "\"project_id\": \"proj_03\"",
                "\"status\": \"completed\"",
                "\"end_date\": \"2025-06-28\""
        ]
    }
    ,
    {
        "annotator": new_task_creator,
        "user_id": "research_data_manager_01",
        "instruction": "As a research data manager, ensure data integrity for 'Quantum Computing Applications' (proj_01). Verify its current status and lead researcher (Prof. James Wilson - res_03). If the project status is not 'active', change it to 'active'. For all articles linked to proj_01, ensure their submission status is 'accepted'. If not, update them to 'accepted'. Create a research log for Prof. James Wilson (res_03) with the exact content: 'Project proj_01 data integrity review completed.', with 'high' relevance, for article art_02. Notify Prof. James Wilson (res_03) with the exact message: 'Project 'Quantum Computing Applications' data integrity review complete. Status and linked articles updated.'. Display the final project details for proj_01.",
        "actions": [
            {
                "name": "FindProjects",
                "arguments": {
                    "project_id": "proj_01"
                },
            },
            {
                "name": "FindUsers",
                "arguments": {
                    "user_id": "res_03"
                },
            },
            {
                "name": "ModifyProjectStatus",
                "arguments": {
                    "project_id": "proj_01",
                    "new_status": "active"
                },
            },
            {
                "name": "FindPublications",
                "arguments": {
                    "article_id": "art_02"
                },
            },
            {
                "name": "LookupSubmissions",
                "arguments": {
                    "article_id": "art_02"
                },
            },
            {
                "name": "ModifySubmissionStatus",
                "arguments": {
                    "submission_id": "sub_01",
                    "new_status": "accepted"
                },
            },
            {
                "name": "CreateResearchLog",
                "arguments": {
                    "researcher_id": "res_03",
                    "article_id": "art_02",
                    "notes": "Project proj_01 data integrity review completed.",
                    "relevance": "high"
                },
            },
            {
                "name": "NotifyUser",
                "arguments": {
                    "recipient_user_id": "res_03",
                    "message_content": "Project 'Quantum Computing Applications' data integrity review complete. Status and linked articles updated."
                },
            },
            {
                "name": "FindProjects",
                "arguments": {
                    "project_id": "proj_01"
                }
            }
        ],
        "outputs": [
                "\"project_id\": \"proj_01\"",
                "\"status\": \"active\""
        ]
    }
    ,
    {
        "annotator": new_task_creator,
        "user_id": "user_onboarding_specialist_01",
        "instruction": "As a user onboarding specialist, set up an existing researcher, Dr. John Smith (res_09), who is currently 'available'. Ensure his UI theme preference is 'dark' and his notification channel is 'email'. Subscribe him to the 'Biomedicine' topic. Create a research log for yourself (user_onboarding_specialist_01) with the exact content: 'Onboarding complete for Dr. John Smith (res_09).', with 'low' relevance, for article art_03 (as a general reference). Notify Dr. John Smith (res_09) with the exact message: 'Welcome to the platform, Dr. Smith! Your profile setup is complete.'. Display Dr. Smith's updated user preferences and topic subscriptions.",
        "actions": [
            {
                "name": "FindUsers",
                "arguments": {
                    "user_id": "res_09",
                    "availability": "available"
                },
            },
            {
                "name": "UpdateUserPreferences",
                "arguments": {
                    "user_id": "res_09",
                    "ui_theme": "dark",
                    "notification_channel": "email"
                },
            },
            {
                "name": "UpdateUserSubscriptions",
                "arguments": {
                    "user_id": "res_09",
                    "topic": "Biomedicine",
                    "action": "add"
                },
            },
            {
                "name": "CreateResearchLog",
                "arguments": {
                    "researcher_id": "user_onboarding_specialist_01",
                    "article_id": "art_03",
                    "notes": "Onboarding complete for Dr. John Smith (res_09).",
                    "relevance": "low"
                },
            },
            {
                "name": "NotifyUser",
                "arguments": {
                    "recipient_user_id": "res_09",
                    "message_content": "Welcome to the platform, Dr. Smith! Your profile setup is complete."
                },
            },
            {
                "name": "GetUserPreferences",
                "arguments": {
                    "user_id": "res_09"
                },
            },
            {
                "name": "GetUserSubscriptions",
                "arguments": {
                    "user_id": "res_09"
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"res_09\"",
                "\"ui_theme\": \"dark\"",
                "\"notification_channel\": \"email\"",
                "\"topic\": \"Biomedicine\""
        ]
    }
    ,
    {
        "annotator": new_task_creator,
        "user_id": "research_data_manager_01",
        "instruction": "As a research data manager, ensure data integrity for 'Quantum Computing Applications' (proj_01). Verify its current status and lead researcher (Prof. James Wilson - res_03). If the project status is not 'active', change it to 'active'. For all articles linked to proj_01, ensure their submission status is 'accepted'. If not, update them to 'accepted'. Create a research log for Prof. James Wilson (res_03) with the exact content: 'Project proj_01 data integrity review completed.', with 'high' relevance, for article art_02. Notify Prof. James Wilson (res_03) with the exact message: 'Project 'Quantum Computing Applications' data integrity review complete. Status and linked articles updated.'. Display the final project details for proj_01.",
        "actions": [
            {
                "name": "FindProjects",
                "arguments": {
                    "project_id": "proj_01"
                },
            },
            {
                "name": "FindUsers",
                "arguments": {
                    "user_id": "res_03"
                },
            },
            {
                "name": "ModifyProjectStatus",
                "arguments": {
                    "project_id": "proj_01",
                    "new_status": "active"
                },
            },
            {
                "name": "FindPublications",
                "arguments": {
                    "article_id": "art_02"
                },
            },
            {
                "name": "LookupSubmissions",
                "arguments": {
                    "article_id": "art_02"
                },
            },
            {
                "name": "ModifySubmissionStatus",
                "arguments": {
                    "submission_id": "sub_01",
                    "new_status": "accepted"
                },
            },
            {
                "name": "CreateResearchLog",
                "arguments": {
                    "researcher_id": "res_03",
                    "article_id": "art_02",
                    "notes": "Project proj_01 data integrity review completed.",
                    "relevance": "high"
                },
            },
            {
                "name": "NotifyUser",
                "arguments": {
                    "recipient_user_id": "res_03",
                    "message_content": "Project 'Quantum Computing Applications' data integrity review complete. Status and linked articles updated."
                },
            },
            {
                "name": "FindProjects",
                "arguments": {
                    "project_id": "proj_01"
                }
            }
        ],
        "outputs": [
                "\"project_id\": \"proj_01\"",
                "\"status\": \"active\""
        ]
    }
    ,
    {
        "annotator": new_task_creator,
        "user_id": "user_onboarding_specialist_01",
        "instruction": "As a user onboarding specialist, set up an existing researcher, Dr. John Smith (res_09), who is currently 'available'. Ensure his UI theme preference is 'dark' and his notification channel is 'email'. Subscribe him to the 'Biomedicine' topic. Create a research log for yourself (user_onboarding_specialist_01) with the exact content: 'Onboarding complete for Dr. John Smith (res_09).', with 'low' relevance, for article art_03 (as a general reference). Notify Dr. John Smith (res_09) with the exact message: 'Welcome to the platform, Dr. Smith! Your profile setup is complete.'. Display Dr. Smith's updated user preferences and topic subscriptions.",
        "actions": [
            {
                "name": "FindUsers",
                "arguments": {
                    "user_id": "res_09",
                    "availability": "available"
                },
            },
            {
                "name": "UpdateUserPreferences",
                "arguments": {
                    "user_id": "res_09",
                    "ui_theme": "dark",
                    "notification_channel": "email"
                },
            },
            {
                "name": "UpdateUserSubscriptions",
                "arguments": {
                    "user_id": "res_09",
                    "topic": "Biomedicine",
                    "action": "add"
                },
            },
            {
                "name": "CreateResearchLog",
                "arguments": {
                    "researcher_id": "user_onboarding_specialist_01",
                    "article_id": "art_03",
                    "notes": "Onboarding complete for Dr. John Smith (res_09).",
                    "relevance": "low"
                },
            },
            {
                "name": "NotifyUser",
                "arguments": {
                    "recipient_user_id": "res_09",
                    "message_content": "Welcome to the platform, Dr. Smith! Your profile setup is complete."
                },
            },
            {
                "name": "GetUserPreferences",
                "arguments": {
                    "user_id": "res_09"
                },
            },
            {
                "name": "GetUserSubscriptions",
                "arguments": {
                    "user_id": "res_09"
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"res_09\"",
                "\"ui_theme\": \"dark\"",
                "\"notification_channel\": \"email\"",
                "\"topic\": \"Biomedicine\""
        ]
    }
]
