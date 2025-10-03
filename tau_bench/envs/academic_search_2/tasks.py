
tasks = [
    {
        "annotator": 0,
        "user_id": "simple_submission_review",
        "instruction": "Execute article processing for 'New Biomarkers for Early Detection of Neurodegenerative Diseases' by 'Dr. Thomas Anderson'. Create a submission record for it, assign 'Prof. James Wilson' as a reviewer, and set the submission's status to 'under_review'. Display the final submission details.",
        "actions": [
            {
                "name": "RetrievePapers",
                "arguments": {
                    "title": "New Biomarkers for Early Detection of Neurodegenerative Diseases"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Thomas Anderson"
                },
            },
            {
                "name": "CreateSubmission",
                "arguments": {
                    "article_id": "art_04",
                    "author_user_id": "res_04",
                    "submission_id_override": "sub_08"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Prof. James Wilson"
                },
            },
            {
                "name": "UpdateSubmission",
                "arguments": {
                    "submission_id": "sub_08",
                    "reviewers": [
                        "res_03"
                    ]
                },
            },
            {
                "name": "UpdateSubmission",
                "arguments": {
                    "submission_id": "sub_08",
                    "status": "under_review"
                },
            },
            {
                "name": "SearchSubmissions",
                "arguments": {
                    "submission_id": "sub_08"
                }
            }
        ],
        "outputs": [
                "\"submission_id\": \"sub_08\"",
                "\"status\": \"under_review\"",
                "\"assigned_reviewers\": [\n      \"res_03\"\n    ]"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "research_influence_and_project_update",
        "instruction": "Perform research impact analysis to assess the influence of Dr. Sarah Johnson's article 'AI applications in diagnosing neurodegenerative diseases' (art_09). First, ensure the project 'Review of AI in Diagnostics - 2025' (proj_review_01) exists, led by Dr. Sarah Johnson and linked to 'art_09'. Then, retrieve details of 'art_09'. Get its full citation graph to identify all citing articles and their primary authors. Find out how many unique articles cite 'art_09'. Then, identify 'Dr. Sarah Johnson's most cited article. If 'AI applications in diagnosing neurodegenerative diseases' (art_09) is NOT his most cited article, create a high-relevance research note for him stating: 'Your article 'AI applications in diagnosing neurodegenerative diseases' is highly cited, but not your top cited work. Consider promoting it further.'. The research note should be linked to art_09. Update the project 'Review of AI in Diagnostics - 2025' (proj_review_01) by adding Dr. Kenji Tanaka and Dr. Anna Petrov as collaborators. Finally, display the details of the updated project.",
        "actions": [
            {
                "name": "RegisterProject",
                "arguments": {
                    "project_name": "Review of AI in Diagnostics - 2025",
                    "lead_researcher_id": "res_02",
                    "linked_article_id": "art_09",
                    "project_id_override": "proj_review_01"
                },
            },
            {
                "name": "RetrievePapers",
                "arguments": {
                    "article_id": "art_09"
                },
            },
            {
                "name": "GetCitationGraph",
                "arguments": {
                    "article_id": "art_09"
                },
            },
            {
                "name": "GetAuthorMetrics",
                "arguments": {
                    "author_name": "Dr. Sarah Johnson"
                },
            },
            {
                "name": "GetMostCitedArticles",
                "arguments": {
                {}
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Sarah Johnson"
                },
            },
            {
                "name": "AddResearchNote",
                "arguments": {
                    "researcher_id": "res_02",
                    "article_id": "art_09",
                    "notes": "Your article 'AI applications in diagnosing neurodegenerative diseases' is highly cited, but not your top cited work. Consider promoting it further.",
                    "relevance": "high"
                },
            },
            {
                "name": "GetProjectDetails",
                "arguments": {
                    "project_name": "Review of AI in Diagnostics - 2025"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Kenji Tanaka"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Anna Petrov"
                },
            },
            {
                "name": "UpdateProject",
                "arguments": {
                    "project_id": "proj_review_01",
                    "add_collaborators": [
                        "res_01",
                        "res_06"
                    ]
                },
            },
            {
                "name": "GetProjectDetails",
                "arguments": {
                    "project_id": "proj_review_01"
                }
            }
        ],
        "outputs": [
                "\"project_id\": \"proj_review_01\"",
                "\"lead_researcher_id\": \"res_02\"",
                "\"linked_articles\": [\n      \"art_09\"\n    ]",
                "\"collaborators\": [\n      \"res_01\",\n      \"res_06\"\n    ]"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "proactive_collaboration_setup",
        "instruction": "Facilitate collaborative partnerships between Dr. Kenji Tanaka (AI) and Dr. Thomas Anderson (Biomedicine), given they have both cited 'art_03'. Prepare Dr. Bauer's profile by subscribing her to the 'AI' topic and setting her notification channel to 'in_app'. Dispatch an alert to Dr. Bauer with the message: 'To help you explore new connections, I've subscribed you to the 'AI' topic and set your alerts to in-app. Dr. Kenji Tanaka's work shows synergy with yours.'. Concurrently, send an alert to Dr. Souza with the message: 'A potential for interdisciplinary synergy was identified between your work and research from Dr. Thomas Anderson in Biomedicine.'. Display Dr. Thomas Anderson's collaboration network.",
        "actions": [
            {
                "name": "GetCitationGraph",
                "arguments": {
                    "article_id": "art_03"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Thomas Anderson"
                },
            },
            {
                "name": "UpdateTopicSubscription",
                "arguments": {
                    "user_id": "res_04",
                    "topic": "AI",
                    "action": "add"
                },
            },
            {
                "name": "ConfigureProfileSettings",
                "arguments": {
                    "user_id": "res_04",
                    "notification_channel": "in_app"
                },
            },
            {
                "name": "DispatchUserAlert",
                "arguments": {
                    "recipient_user_id": "res_04",
                    "sender_user_id": "system",
                    "message_content": "To help you explore new connections, I've subscribed you to the 'AI' topic and set your alerts to in-app. Dr. Kenji Tanaka's work shows synergy with yours."
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Kenji Tanaka"
                },
            },
            {
                "name": "DispatchUserAlert",
                "arguments": {
                    "recipient_user_id": "res_01",
                    "sender_user_id": "system",
                    "message_content": "A potential for interdisciplinary synergy was identified between your work and research from Dr. Thomas Anderson in Biomedicine."
                },
            },
            {
                "name": "FindCollaborationNetwork",
                "arguments": {
                    "author_name": "Dr. Thomas Anderson"
                }
            }
        ],
        "outputs": [
                "\"Dr. Sarah Johnson\": 1",
                "\"Dr. Ana Oliveira\": 1",
                "\"Dr. Kenji Tanaka\": 1",
                "\"Dr. Elena Rossi\": 1"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "funding_compliance_check",
        "instruction": "Execute grant management tasks to ensure the 'Quantum Computing Applications' project reflects its funding source. If the project is funded by the 'National Science Foundation', update its name to '[NSF] Quantum Computing Applications'. Concurrently, create a research note for the project lead, Prof. James Wilson, stating 'Project name updated to reflect NSF funding.'. Display the final, updated project details.",
        "actions": [
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Prof. James Wilson"
                },
            },
            {
                "name": "GetProjectDetails",
                "arguments": {
                    "project_name": "Quantum Computing Applications"
                },
            },
            {
                "name": "RetrieveFundingInfo",
                "arguments": {
                    "funding_source_id": "fs_02"
                },
            },
            {
                "name": "RetrievePapers",
                "arguments": {
                    "author_name": "Prof. James Wilson"
                },
            },
            {
                "name": "UpdateProject",
                "arguments": {
                    "project_id": "proj_01",
                    "project_name": "[NSF] Quantum Computing Applications"
                },
            },
            {
                "name": "RetrievePapers",
                "arguments": {
                    "article_id": "art_02"
                },
            },
            {
                "name": "GetProjectDetails",
                "arguments": {
                    "project_name": "[NSF] Quantum Computing Applications"
                },
            },
            {
                "name": "AddResearchNote",
                "arguments": {
                    "researcher_id": "res_03",
                    "article_id": "art_02",
                    "notes": "Project name updated to reflect NSF funding."
                },
            },
            {
                "name": "GetProjectDetails",
                "arguments": {
                    "project_id": "proj_01"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "user_id": "res_03"
                },
            },
            {
                "name": "RetrieveFundingInfo",
                "arguments": {
                    "funding_source_id": "fs_02"
                }
            }
        ],
        "outputs": [
                "\"project_id\": \"proj_01\"",
                "\"project_name\": \"[NSF] Quantum Computing Applications\"",
                "\"funding_source_id\": \"fs_02\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "review_completion_and_notification",
        "instruction": "Conduct editorial processing for review 'rev_01' for submission 'sub_01', which recommends 'minor_revisions'. Update the associated article's status to 'pending_revision'. Dispatch an alert to the article's author, Prof. James Wilson, with the exact message: 'Your article, \"Limits of Quantum Computing...\", has received a review. Minor revisions requested.'. Display the updated article details.",
        "actions": [
            {
                "name": "SearchSubmissions",
                "arguments": {
                    "submission_id": "sub_01"
                },
            },
            {
                "name": "RetrievePapers",
                "arguments": {
                    "article_id": "art_02"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Prof. James Wilson"
                },
            },
            {
                "name": "UpdateArticleMetadata",
                "arguments": {
                    "article_id": "art_02",
                    "status": "pending_revision"
                },
            },
            {
                "name": "RetrievePapers",
                "arguments": {
                    "author_name": "Prof. James Wilson"
                },
            },
            {
                "name": "DispatchUserAlert",
                "arguments": {
                    "recipient_user_id": "res_03",
                    "sender_user_id": "system",
                    "message_content": "Your article, \"Limits of Quantum Computing...\", has received a review. Minor revisions requested."
                },
            },
            {
                "name": "RetrievePapers",
                "arguments": {
                    "title": "Limits of Quantum Computing in Optimization Problems"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "user_id": "res_03"
                },
            },
            {
                "name": "SearchSubmissions",
                "arguments": {
                    "article_id": "art_02"
                },
            },
            {
                "name": "SearchSubmissions",
                "arguments": {
                    "submission_id": "sub_01"
                },
            },
            {
                "name": "RetrievePapers",
                "arguments": {
                    "article_id": "art_02"
                }
            }
        ],
        "outputs": [
                "\"article_id\": \"art_02\"",
                "\"status\": \"pending_revision\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "topical_bridge_finding",
        "instruction": "Execute research analysis to identify Dr. Sarah Johnson as a potential bridge between AI and Biomedicine. Confirm if he has collaborated with 'Dr. Ana Oliveira' or 'Dr. Thomas Anderson'. After this check, create a research note for AI researcher Dr. Anna Petrov, with the exact content: 'Dr. Sarah Johnson could be a potential bridge to the field of Biomedicine.'. Display the collaboration check result for Dr. Sarah Johnson with 'Dr. Ana Oliveira' and 'Dr. Thomas Anderson'.",
        "actions": [
            {
                "name": "RetrievePapers",
                "arguments": {
                    "title": "Federated Learning for Privacy-Preserving AI"
                },
            },
            {
                "name": "RetrievePapers",
                "arguments": {
                    "title": "New Biomarkers for Early Detection of Neurodegenerative Diseases"
                },
            },
            {
                "name": "GetCitationGraph",
                "arguments": {
                    "article_id": "art_06",
                    "compare_with_article_id": "art_04"
                },
            },
            {
                "name": "RetrievePapers",
                "arguments": {
                    "author_name": "Dr. Sarah Johnson"
                },
            },
            {
                "name": "FindCollaborationNetwork",
                "arguments": {
                    "author_name": "Dr. Sarah Johnson",
                    "authors_to_check": [
                        "Dr. Ana Oliveira",
                        "Dr. Thomas Anderson"
                    ]
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Anna Petrov"
                },
            },
            {
                "name": "AddResearchNote",
                "arguments": {
                    "researcher_id": "res_06",
                    "article_id": "art_06",
                    "notes": "Dr. Sarah Johnson could be a potential bridge to the field of Biomedicine."
                },
            },
            {
                "name": "FindCollaborationNetwork",
                "arguments": {
                    "author_name": "Dr. Sarah Johnson",
                    "authors_to_check": [
                        "Dr. Ana Oliveira",
                        "Dr. Thomas Anderson"
                    ]
                }
            }
        ],
        "outputs": [
                "\"Dr. Ana Oliveira\": 1",
                "\"Dr. Thomas Anderson\": 1"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "user_account_management_and_outreach",
        "instruction": "Configure your profile as Prof. James Wilson. Set up your profile. Configure your settings to receive notifications via 'email' and use the 'dark' UI theme. Subscribe to both 'Astrophysics' and 'Quantum Physics' topics. After profile setup, dispatch an alert to Dr. Liu Wei with the exact message: 'Hi Kenji, I saw your latest paper on atmospheric signatures. Fascinating work! Would love to chat about it sometime.'. Finally, display Dr. Liu Wei's author metrics.",
        "actions": [
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Prof. James Wilson"
                },
            },
            {
                "name": "ConfigureProfileSettings",
                "arguments": {
                    "user_id": "res_03",
                    "notification_channel": "email",
                    "ui_theme": "dark"
                },
            },
            {
                "name": "UpdateTopicSubscription",
                "arguments": {
                    "user_id": "res_03",
                    "topic": "Astrophysics",
                    "action": "add"
                },
            },
            {
                "name": "UpdateTopicSubscription",
                "arguments": {
                    "user_id": "res_03",
                    "topic": "Quantum Physics",
                    "action": "add"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Liu Wei"
                },
            },
            {
                "name": "DispatchUserAlert",
                "arguments": {
                    "recipient_user_id": "res_05",
                    "sender_user_id": "res_03",
                    "message_content": "Hi Kenji, I saw your latest paper on atmospheric signatures. Fascinating work! Would love to chat about it sometime."
                },
            },
            {
                "name": "GetAuthorMetrics",
                "arguments": {
                    "author_name": "Dr. Liu Wei"
                }
            }
        ],
        "outputs": [
                "\"total_publications\": 3",
                "\"total_citations\": 1",
                "\"h_index\": 1"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "collaboration_pathway_analysis",
        "instruction": "Conduct collaboration exploration as Dr. Kenji Tanaka to explore collaboration pathways with Dr. Sarah Johnson. Attempt to find common collaborators. If no common collaborators are found, verify if your main papers ('Advances in Language...') and his ('Gene Editing...') share any common citations. If no direct link is identified through common citations, create a high-relevance research note for yourself regarding Dr. Mendes's paper 'AI applications in diagnosing neurodegenerative diseases', with the exact content: 'Review Dr. Mendes's AI article as a potential collaboration entry point.'. Display the confirmation of the created log entry. If common collaborators or common citations ARE found, simply display the result of the common collaborator/citation check and DO NOT create a research note.",
        "actions": [
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Kenji Tanaka"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Sarah Johnson"
                },
            },
            {
                "name": "FindCommonCollaborators",
                "arguments": {
                    "author1_name": "Dr. Kenji Tanaka",
                    "author2_name": "Dr. Sarah Johnson"
                },
            },
            {
                "name": "RetrievePapers",
                "arguments": {
                    "title": "Advances in Language Models for Code Generation"
                },
            },
            {
                "name": "RetrievePapers",
                "arguments": {
                    "title": "Gene Editing Techniques with CRISPR-Cas9"
                },
            },
            {
                "name": "GetCitationGraph",
                "arguments": {
                    "article_id": "art_01",
                    "compare_with_article_id": "art_03"
                },
            },
            {
                "name": "RetrievePapers",
                "arguments": {
                    "title": "AI applications in diagnosing neurodegenerative diseases"
                },
            },
            {
                "name": "RetrievePapers",
                "arguments": {
                    "author_name": "Dr. Kenji Tanaka"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Thomas Anderson"
                },
            },
            {
                "name": "RetrievePapers",
                "arguments": {
                    "author_name": "Dr. Thomas Anderson"
                },
            },
            {
                "name": "RetrievePapers",
                "arguments": {
                    "author_name": "Dr. Sarah Johnson"
                },
            },
            {
                "name": "FindCollaborationNetwork",
                "arguments": {
                    "author_name": "Dr. Thomas Anderson"
                }
            }
        ],
        "outputs": [
                "\"Dr. Sarah Johnson\": 1",
                "\"Dr. Ana Oliveira\": 1",
                "\"Dr. Kenji Tanaka\": 1",
                "\"Dr. Elena Rossi\": 1"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "citation_linkage_and_network_expansion",
        "instruction": "Execute research assistance duties for Dr. Kenji Tanaka to formally establish a citation link where Dr. Anna Petrov's 'Federated Learning for Privacy-Preserving AI' cites Dr. Souza's 'Advances in Language Models for Code Generation', using the context: 'This work builds on foundational transformer architectures.'. Subsequently, assess the collaboration network between Dr. Kenji Tanaka and Dr. Anna Petrov. If no common collaborators exist, suggest potential reviewers for Dr. Khan's article to bridge any research gaps. Retrieve the author metrics for 'Dr. Elena Rossi' and 'Dr. Kenji Tanaka' from the suggested reviewers. Conclude by updating Dr. Khan's article's topic to 'AI / Scientometrics' and display the final, updated article details.",
        "actions": [
            {
                "name": "RetrievePapers",
                "arguments": {
                    "title": "Federated Learning for Privacy-Preserving AI"
                },
            },
            {
                "name": "RetrievePapers",
                "arguments": {
                    "title": "Advances in Language Models for Code Generation"
                },
            },
            {
                "name": "AddCitation",
                "arguments": {
                    "source_article_id": "art_06",
                    "cited_article_id": "art_01",
                    "context": "This work builds on foundational transformer architectures."
                },
            },
            {
                "name": "GetCitationGraph",
                "arguments": {
                    "article_id": "art_01"
                },
            },
            {
                "name": "FindCommonCollaborators",
                "arguments": {
                    "author1_name": "Dr. Kenji Tanaka",
                    "author2_name": "Dr. Anna Petrov"
                },
            },
            {
                "name": "SuggestReviewers",
                "arguments": {
                    "article_id": "art_06"
                },
            },
            {
                "name": "GetAuthorMetrics",
                "arguments": {
                    "author_name": "Dr. Elena Rossi"
                },
            },
            {
                "name": "GetAuthorMetrics",
                "arguments": {
                    "author_name": "Dr. Kenji Tanaka"
                },
            },
            {
                "name": "UpdateArticleMetadata",
                "arguments": {
                    "article_id": "art_06",
                    "topic": "AI / Scientometrics"
                },
            },
            {
                "name": "RetrievePapers",
                "arguments": {
                    "title": "Federated Learning for Privacy-Preserving AI"
                }
            }
        ],
        "outputs": [
                "\"article_id\": \"art_06\"",
                "\"title\": \"Federated Learning for Privacy-Preserving AI\"",
                "\"authors\": [\n      \"Dr. Anna Petrov\"\n    ]",
                "\"publication_year\": 2024",
                "\"topic\": \"AI / Scientometrics\"",
                "\"abstract\": \"A novel framework for federated learning that enhances data privacy without compromising model accuracy. We introduce a new aggregation protocol.\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "retraction_impact_analysis",
        "instruction": "Handle integrity management by processing the retraction of 'Limits of Quantum Computing in Optimization Problems' (art_02) due to a critical flaw. Update its status to 'retracted'. For each article citing 'art_02', specifically 'Advances in Language Models for Code Generation' (art_01), dispatch a research note to its primary author (Dr. Kenji Tanaka) with the exact message: 'Critical Citation Alert: An article you cited (art_02) has been retracted. Please review your work.'. Concurrently, update the status of the research project linked to 'art_02', 'Quantum Computing Applications', to 'under_review'. Display both the updated retracted article and the project details.",
        "actions": [
            {
                "name": "UpdateArticleMetadata",
                "arguments": {
                    "article_id": "art_02",
                    "status": "retracted"
                },
            },
            {
                "name": "GetCitationGraph",
                "arguments": {
                    "article_id": "art_02"
                },
            },
            {
                "name": "RetrievePapers",
                "arguments": {
                    "title": "Advances in Language Models for Code Generation"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Kenji Tanaka"
                },
            },
            {
                "name": "AddResearchNote",
                "arguments": {
                    "researcher_id": "res_01",
                    "article_id": "art_02",
                    "notes": "Critical Citation Alert: An article you cited (art_02) has been retracted. Please review your work."
                },
            },
            {
                "name": "GetProjectDetails",
                "arguments": {
                    "linked_article_id": "art_02"
                },
            },
            {
                "name": "UpdateProject",
                "arguments": {
                    "project_id": "proj_01",
                    "status": "under_review"
                },
            },
            {
                "name": "RetrievePapers",
                "arguments": {
                    "title": "Limits of Quantum Computing in Optimization Problems"
                },
            },
            {
                "name": "GetProjectDetails",
                "arguments": {
                    "project_name": "Quantum Computing Applications"
                }
            }
        ],
        "outputs": [
                "\"article_id\": \"art_02\"",
                "\"status\": \"retracted\"",
                "\"project_id\": \"proj_01\"",
                "\"status\": \"under_review\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "collaboration_and_funding_setup",
        "instruction": "Manage National Science Foundation programs to integrate AI expertise into the 'Quantum Computing Applications' project by adding 'Dr. Kenji Tanaka' as a collaborator. Provisionally set the project status to 'pending_collaboration' with her inclusion. Create a research note for Dr. Souza, linking it to the project's main article ('art_02'), with the exact content: 'You have been provisionally added to the Quantum Computing Applications project.'. Subsequently, link the 'AI Advancement Grant' to the project and finalize its status to 'active_collaboration'. Display the final, fully configured project details.",
        "actions": [
            {
                "name": "GetProjectDetails",
                "arguments": {
                    "project_name": "Quantum Computing Applications"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "research_field": "Artificial Intelligence"
                },
            },
            {
                "name": "RetrievePapers",
                "arguments": {
                    "article_id": "art_02"
                },
            },
            {
                "name": "UpdateProject",
                "arguments": {
                    "project_id": "proj_01",
                    "add_collaborators": [
                        "res_01"
                    ],
                    "status": "pending_collaboration"
                },
            },
            {
                "name": "AddResearchNote",
                "arguments": {
                    "researcher_id": "res_01",
                    "article_id": "art_02",
                    "notes": "You have been provisionally added to the Quantum Computing Applications project."
                },
            },
            {
                "name": "RetrieveFundingInfo",
                "arguments": {
                    "source_name": "AI Advancement Grant"
                },
            },
            {
                "name": "UpdateProject",
                "arguments": {
                    "project_id": "proj_01",
                    "funding_source_id": "fs_01",
                    "status": "active_collaboration"
                },
            },
            {
                "name": "GetProjectDetails",
                "arguments": {
                    "project_id": "proj_01"
                }
            }
        ],
        "outputs": [
                "\"project_id\": \"proj_01\"",
                "\"status\": \"active_collaboration\"",
                "\"funding_source_id\": \"fs_01\"",
                "\"collaborators\": [\n      \"res_01\"\n    ]"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "funding_renewal_justification",
        "instruction": "Manage funding justification as Prof. James Wilson to justify funding renewal for the 'Quantum Computing Applications' project. Link your most recent 2024 publication, 'Revised: Limits of Quantum Computing' (art_07), to the project. Demonstrate impact by identifying papers that cited your original article ('art_02') and retrieving author metrics for yourself and the author of the first citing paper, 'Dr. Kenji Tanaka'. Conclude by creating a research note for yourself with the exact content: 'Funding renewal justification: New article art_07 linked, demonstrated impact via citation by Dr. Souza.'. Display the updated project details.",
        "actions": [
            {
                "name": "GetProjectDetails",
                "arguments": {
                    "project_name": "Quantum Computing Applications"
                },
            },
            {
                "name": "RetrievePapers",
                "arguments": {
                    "author_name": "Prof. James Wilson",
                    "year": 2024
                },
            },
            {
                "name": "UpdateProject",
                "arguments": {
                    "project_id": "proj_01",
                    "linked_articles": [
                        "art_02",
                        "art_07"
                    ]
                },
            },
            {
                "name": "GetCitationGraph",
                "arguments": {
                    "article_id": "art_02"
                },
            },
            {
                "name": "RetrievePapers",
                "arguments": {
                    "article_id": "art_01"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Kenji Tanaka"
                },
            },
            {
                "name": "GetAuthorMetrics",
                "arguments": {
                    "author_name": "Prof. James Wilson"
                },
            },
            {
                "name": "GetAuthorMetrics",
                "arguments": {
                    "author_name": "Dr. Kenji Tanaka"
                },
            },
            {
                "name": "AddResearchNote",
                "arguments": {
                    "researcher_id": "res_03",
                    "article_id": "art_07",
                    "notes": "Funding renewal justification: New article art_07 linked, demonstrated impact via citation by Dr. Souza."
                },
            },
            {
                "name": "GetProjectDetails",
                "arguments": {
                    "project_id": "proj_01"
                }
            }
        ],
        "outputs": [
                "\"project_id\": \"proj_01\"",
                "\"linked_articles\": [\n      \"art_02\",\n      \"art_07\"\n    ]"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "audit_of_high_impact_author",
        "instruction": "Conduct institutional auditing to review the impact of Dr. Sarah Johnson. Obtain his author metrics and identify his most cited article ('Gene Editing Techniques with CRISPR-Cas9' - art_03). Identify articles that cite his most cited work, noting the interdisciplinary citation from 'Advances in Language Models for Code Generation' (art_01). Dispatch an alert to Dr. Kenji Tanaka (author of 'art_01') with the exact message: 'Your work is bridging to Biomedicine by citing Dr. Mendes. Consider direct collaboration.'. Concurrently, dispatch an alert to Dr. Sarah Johnson with the exact message: 'Your work is having cross-disciplinary impact on the AI field.'. Finally, display Dr. Mendes's author metrics.",
        "actions": [
            {
                "name": "GetAuthorMetrics",
                "arguments": {
                    "author_name": "Dr. Sarah Johnson"
                },
            },
            {
                "name": "GetMostCitedArticles",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetCitationGraph",
                "arguments": {
                    "article_id": "art_03"
                },
            },
            {
                "name": "RetrievePapers",
                "arguments": {
                    "article_id": "art_01"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Kenji Tanaka"
                },
            },
            {
                "name": "DispatchUserAlert",
                "arguments": {
                    "recipient_user_id": "res_01",
                    "sender_user_id": "system",
                    "message_content": "Your work is bridging to Biomedicine by citing Dr. Mendes. Consider direct collaboration."
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Sarah Johnson"
                },
            },
            {
                "name": "DispatchUserAlert",
                "arguments": {
                    "recipient_user_id": "res_02",
                    "sender_user_id": "system",
                    "message_content": "Your work is having cross-disciplinary impact on the AI field."
                },
            },
            {
                "name": "GetAuthorMetrics",
                "arguments": {
                    "author_name": "Dr. Sarah Johnson"
                }
            }
        ],
        "outputs": [
                "\"total_publications\": 3",
                "\"total_citations\": 3",
                "\"h_index\": 1"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "citation_correction_and_notification",
        "instruction": "Execute academic corrections as Dr. Kenji Tanaka to correct your paper 'Advances in Language Models for Code Generation' (art_01) by adding a citation to Dr. Thomas Anderson's 'New Biomarkers for Early Detection of Neurodegenerative Diseases' (art_04) with the exact context: 'Biomarker detection parallels token prediction.'. Update 'art_01' keywords to include 'Biomedicine'. Create a research note for your primary collaborator, Dr. Elena Rossi, with the exact content: 'Article 'Advances in Language...' has been updated with a new citation and keywords.'. Display your updated article.",
        "actions": [
            {
                "name": "RetrievePapers",
                "arguments": {
                    "title": "Advances in Language Models for Code Generation"
                },
            },
            {
                "name": "RetrievePapers",
                "arguments": {
                    "title": "New Biomarkers for Early Detection of Neurodegenerative Diseases"
                },
            },
            {
                "name": "AddCitation",
                "arguments": {
                    "source_article_id": "art_01",
                    "cited_article_id": "art_04",
                    "context": "Biomarker detection parallels token prediction."
                },
            },
            {
                "name": "UpdateArticleMetadata",
                "arguments": {
                    "article_id": "art_01",
                    "keywords": [
                        "transformer",
                        "code-generation",
                        "Biomedicine"
                    ]
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Elena Rossi"
                },
            },
            {
                "name": "AddResearchNote",
                "arguments": {
                    "researcher_id": "res_16",
                    "article_id": "art_01",
                    "notes": "Article 'Advances in Language...' has been updated with a new citation and keywords."
                },
            },
            {
                "name": "RetrievePapers",
                "arguments": {
                    "article_id": "art_01"
                }
            }
        ],
        "outputs": [
                "\"article_id\": \"art_01\"",
                "\"keywords\": [\n      \"transformer\",\n      \"code-generation\",\n      \"Biomedicine\"\n    ]"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "review_transfer_and_justification",
        "instruction": "Conduct editorial reassignment to reassign the reviewer for submission 'sub_01' (article 'art_02') due to a topical mismatch (reviewer Dr. Kenji Tanaka is AI, article is Quantum Physics). Identify an expert in 'Astrophysics', excluding the author Prof. James Wilson, and assign 'Dr. Liu Wei' as the new reviewer. Dispatch an alert to Dr. Souza with the exact message: 'You have been unassigned from review sub_01 due to a topic mismatch.'. Concurrently, dispatch an alert to Prof. James Wilson with the exact message: 'Reviewer for your submission sub_01 has been changed to Dr. Liu Wei.'. Display the updated submission details.",
        "actions": [
            {
                "name": "SearchSubmissions",
                "arguments": {
                    "submission_id": "sub_01"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "user_id": "res_01"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "user_id": "res_03"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "research_field": "Astrophysics"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Liu Wei"
                },
            },
            {
                "name": "UpdateSubmission",
                "arguments": {
                    "submission_id": "sub_01",
                    "reviewers": [
                        "res_05"
                    ]
                },
            },
            {
                "name": "DispatchUserAlert",
                "arguments": {
                    "recipient_user_id": "res_01",
                    "sender_user_id": "system",
                    "message_content": "You have been unassigned from review sub_01 due to a topic mismatch."
                },
            },
            {
                "name": "DispatchUserAlert",
                "arguments": {
                    "recipient_user_id": "res_03",
                    "sender_user_id": "system",
                    "message_content": "Reviewer for your submission sub_01 has been changed to Dr. Liu Wei."
                },
            },
            {
                "name": "SearchSubmissions",
                "arguments": {
                    "submission_id": "sub_01"
                }
            }
        ],
        "outputs": [
                "\"submission_id\": \"sub_01\"",
                "\"assigned_reviewers\": [\n      \"res_05\"\n    ]"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "reviewer_expertise_verification",
        "instruction": "Perform editor-in-chief verification to verify the suitability of Dr. Kenji Tanaka as a reviewer for submission 'sub_02' (article 'New Biomarkers for Early Detection...'). After obtaining reviewer suggestions (excluding author Dr. Thomas Anderson), determine if Dr. Souza has directly cited Dr. Bauer's work. If no direct citation exists, create a research note for Dr. Thomas Anderson with the exact content: 'Reviewer Dr. Kenji Tanaka has been assigned based on topical expertise.'. Assign Dr. Kenji Tanaka as the reviewer for the submission and set the submission status to 'under_review'. Display the updated submission details.",
        "actions": [
            {
                "name": "RetrievePapers",
                "arguments": {
                    "title": "New Biomarkers for Early Detection of Neurodegenerative Diseases"
                },
            },
            {
                "name": "SearchSubmissions",
                "arguments": {
                    "article_id": "art_04"
                },
            },
            {
                "name": "SuggestReviewers",
                "arguments": {
                    "article_id": "art_04",
                    "exclude_authors": [
                        "Dr. Thomas Anderson"
                    ]
                },
            },
            {
                "name": "RetrievePapers",
                "arguments": {
                    "author_name": "Dr. Kenji Tanaka"
                },
            },
            {
                "name": "GetCitationGraph",
                "arguments": {
                    "article_id": "art_01"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Thomas Anderson"
                },
            },
            {
                "name": "AddResearchNote",
                "arguments": {
                    "researcher_id": "res_04",
                    "article_id": "art_04",
                    "notes": "Reviewer Dr. Kenji Tanaka has been assigned based on topical expertise."
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Kenji Tanaka"
                },
            },
            {
                "name": "UpdateSubmission",
                "arguments": {
                    "submission_id": "sub_02",
                    "reviewers": [
                        "res_01"
                    ]
                },
            },
            {
                "name": "UpdateSubmission",
                "arguments": {
                    "submission_id": "sub_02",
                    "status": "under_review"
                },
            },
            {
                "name": "SearchSubmissions",
                "arguments": {
                    "submission_id": "sub_02"
                }
            }
        ],
        "outputs": [
                "\"submission_id\": \"sub_02\"",
                "\"status\": \"under_review\"",
                "\"assigned_reviewers\": [\n      \"res_01\"\n    ]"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "cross_institutional_project_funding",
        "instruction": "Execute program management to fund a new project to bridge AI and Biomedicine. Identify Dr. Anna Petrov (AI) and Dr. Thomas Anderson (Biomedicine) as experts, and retrieve their author metrics. Create a new project titled 'AI-Biomed Bridge', led by Dr. Khan, linking her main article ('Federated Learning for Privacy-Preserving AI' - art_06). Add Dr. Bauer as a collaborator to this project. Secure funding by assigning the 'AI Advancement Grant' to the project. Display the final, funded project details.",
        "actions": [
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Anna Petrov"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Thomas Anderson"
                },
            },
            {
                "name": "GetAuthorMetrics",
                "arguments": {
                    "author_name": "Dr. Anna Petrov"
                },
            },
            {
                "name": "GetAuthorMetrics",
                "arguments": {
                    "author_name": "Dr. Thomas Anderson"
                },
            },
            {
                "name": "RetrievePapers",
                "arguments": {
                    "author_name": "Dr. Anna Petrov"
                },
            },
            {
                "name": "RegisterProject",
                "arguments": {
                    "project_name": "AI-Biomed Bridge",
                    "lead_researcher_id": "res_06",
                    "linked_article_id": "art_06",
                    "project_id_override": "proj_bridge_01"
                },
            },
            {
                "name": "UpdateProject",
                "arguments": {
                    "project_id": "proj_bridge_01",
                    "add_collaborators": [
                        "res_04"
                    ]
                },
            },
            {
                "name": "RetrieveFundingInfo",
                "arguments": {
                    "source_name": "AI Advancement Grant"
                },
            },
            {
                "name": "UpdateProject",
                "arguments": {
                    "project_id": "proj_bridge_01",
                    "funding_source_id": "fs_01"
                },
            },
            {
                "name": "GetProjectDetails",
                "arguments": {
                    "project_id": "proj_bridge_01"
                }
            }
        ],
        "outputs": [
                "\"project_id\": \"proj_bridge_01\"",
                "\"funding_source_id\": \"fs_01\"",
                "\"collaborators\": [\n      \"res_04\"\n    ]"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "reviewer_conflict_resolution",
        "instruction": "Conduct editorial reassignment to reassign the reviewer for submission 'sub_01' (article 'art_02') due to a topical mismatch (reviewer Dr. Kenji Tanaka is AI, article is Quantum Physics). Identify a new reviewer expert in 'Astrophysics', excluding the author Prof. James Wilson, and assign 'Dr. Liu Wei' as the new reviewer. Dispatch an alert to Dr. Souza with the exact message: 'You have been unassigned from review sub_01 due to a topic mismatch.'. Concurrently, dispatch an alert to Prof. James Wilson with the exact message: 'Reviewer for your submission sub_01 has been changed to Dr. Liu Wei.'. Display the updated submission details.",
        "actions": [
            {
                "name": "SearchSubmissions",
                "arguments": {
                    "submission_id": "sub_01"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "user_id": "res_01"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "user_id": "res_03"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "research_field": "Astrophysics"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Liu Wei"
                },
            },
            {
                "name": "UpdateSubmission",
                "arguments": {
                    "submission_id": "sub_01",
                    "reviewers": [
                        "res_05"
                    ]
                },
            },
            {
                "name": "DispatchUserAlert",
                "arguments": {
                    "recipient_user_id": "res_01",
                    "sender_user_id": "system",
                    "message_content": "You have been unassigned from review sub_01 due to a topic mismatch."
                },
            },
            {
                "name": "DispatchUserAlert",
                "arguments": {
                    "recipient_user_id": "res_03",
                    "sender_user_id": "system",
                    "message_content": "Reviewer for your submission sub_01 has been changed to Dr. Liu Wei."
                },
            },
            {
                "name": "SearchSubmissions",
                "arguments": {
                    "submission_id": "sub_01"
                }
            }
        ],
        "outputs": [
                "\"submission_id\": \"sub_01\"",
                "\"assigned_reviewers\": [\n      \"res_05\"\n    ]"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "validate_promotion_claims",
        "instruction": "Manage university administration to validate Prof. James Wilson's promotion case by confirming her co-authorship with Dr. Wei Zhang on 'Revised: Limits of Quantum Computing' (art_07). Retrieve author metrics for both researchers. After confirmation, update the status of Prof. James Wilson's main project, 'Quantum Computing Applications', to 'promotion_review_complete'. Create a research note on her profile with the exact content: 'Promotion package validated: Co-authorship with Dr. Wei Zhang confirmed.'. Display the updated project details.",
        "actions": [
            {
                "name": "RetrievePapers",
                "arguments": {
                    "title": "Revised: Limits of Quantum Computing"
                },
            },
            {
                "name": "GetAuthorMetrics",
                "arguments": {
                    "author_name": "Prof. James Wilson"
                },
            },
            {
                "name": "GetAuthorMetrics",
                "arguments": {
                    "author_name": "Dr. Wei Zhang"
                },
            },
            {
                "name": "GetProjectDetails",
                "arguments": {
                    "project_name": "Quantum Computing Applications"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "user_id": "res_03"
                },
            },
            {
                "name": "UpdateProject",
                "arguments": {
                    "project_id": "proj_01",
                    "status": "promotion_review_complete"
                },
            },
            {
                "name": "AddResearchNote",
                "arguments": {
                    "researcher_id": "res_03",
                    "article_id": "art_07",
                    "notes": "Promotion package validated: Co-authorship with Dr. Wei Zhang confirmed."
                },
            },
            {
                "name": "GetProjectDetails",
                "arguments": {
                    "project_id": "proj_01"
                }
            }
        ],
        "outputs": [
                "\"project_id\": \"proj_01\"",
                "\"status\": \"promotion_review_complete\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "citation_error_correction",
        "instruction": "Execute citation corrections as Dr. Liu Wei to correct a citation error in your paper 'Dark Matter and the Large-Scale Structure of the Universe' (art_05). Add a new citation from 'art_05' to 'Advances in Language Models for Code Generation' (art_01) with the exact context: 'Correcting citation from original publication.'. Update 'art_05's status to 'correction_pending'. Create a research note for Dr. Kenji Tanaka, author of the correctly cited paper, with the exact content: 'Note: A corrective citation to your paper was added from 'Dark Matter...' (art_05).'. Display the final citation graph for 'art_05'.",
        "actions": [
            {
                "name": "RetrievePapers",
                "arguments": {
                    "title": "Dark Matter and the Large-Scale Structure of the Universe"
                },
            },
            {
                "name": "RetrievePapers",
                "arguments": {
                    "title": "Advances in Language Models for Code Generation"
                },
            },
            {
                "name": "AddCitation",
                "arguments": {
                    "source_article_id": "art_05",
                    "cited_article_id": "art_01",
                    "context": "Correcting citation from original publication."
                },
            },
            {
                "name": "UpdateArticleMetadata",
                "arguments": {
                    "article_id": "art_05",
                    "status": "correction_pending"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Kenji Tanaka"
                },
            },
            {
                "name": "AddResearchNote",
                "arguments": {
                    "researcher_id": "res_01",
                    "article_id": "art_01",
                    "notes": "Note: A corrective citation to your paper was added from 'Dark Matter...' (art_05)."
                },
            },
            {
                "name": "GetCitationGraph",
                "arguments": {
                    "article_id": "art_05"
                }
            }
        ],
        "outputs": [
                "\"article_id\": \"art_05\"",
                "\"cites\": [\n    \"art_02\",\n    \"art_01\"\n  ]"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "conference_panel_curation",
        "instruction": "Organize conference activities for 'AI Summit 2025', assemble a panel by identifying two Artificial Intelligence experts: Dr. Kenji Tanaka and Dr. Anna Petrov. Retrieve their author metrics for introductions and their most recent articles. Create a new project titled 'AI Summit 2025 Panel' with project ID 'proj_panel_01', led by Dr. Souza, linking her most recent article ('Advances in Language Models for Code Generation' - art_01). Add Dr. Khan as a collaborator to this project. Create a research note for Dr. Khan, linking it to her main article 'Federated Learning for Privacy-Preserving AI' (art_06), with the exact content: 'You have been invited to join the 'AI Summit 2025 Panel' project.'. Display the final project details.",
        "actions": [
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "research_field": "Artificial Intelligence"
                },
            },
            {
                "name": "GetAuthorMetrics",
                "arguments": {
                    "author_name": "Dr. Kenji Tanaka"
                },
            },
            {
                "name": "GetAuthorMetrics",
                "arguments": {
                    "author_name": "Dr. Anna Petrov"
                },
            },
            {
                "name": "RetrievePapers",
                "arguments": {
                    "author_name": "Dr. Kenji Tanaka"
                },
            },
            {
                "name": "RetrievePapers",
                "arguments": {
                    "author_name": "Dr. Anna Petrov"
                },
            },
            {
                "name": "RegisterProject",
                "arguments": {
                    "project_name": "AI Summit 2025 Panel",
                    "lead_researcher_id": "res_01",
                    "linked_article_id": "art_01",
                    "project_id_override": "proj_panel_01"
                },
            },
            {
                "name": "UpdateProject",
                "arguments": {
                    "project_id": "proj_panel_01",
                    "add_collaborators": [
                        "res_06"
                    ]
                },
            },
            {
                "name": "AddResearchNote",
                "arguments": {
                    "researcher_id": "res_06",
                    "article_id": "art_06",
                    "notes": "You have been invited to join the 'AI Summit 2025 Panel' project."
                },
            },
            {
                "name": "GetProjectDetails",
                "arguments": {
                    "project_id": "proj_panel_01"
                }
            }
        ],
        "outputs": [
                "\"project_id\": \"proj_panel_01\"",
                "\"lead_researcher_id\": \"res_01\"",
                "\"collaborators\": [\n      \"res_06\"\n    ]"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "review_conflict_followup",
        "instruction": "Conduct editorial processing for review 'rev_01' for submission 'sub_01' (article 'art_02'), involving reviewer Dr. Kenji Tanaka ('res_01') and author Prof. James Wilson ('res_03'). Verify if Dr. Souza and Prof. James Wilson have common collaborators. Since no common collaborators exist, update the article's status to 'pending_revision'. To foster future connection, create a research note for Prof. James Wilson with the exact content: 'Review by Dr. Kenji Tanaka is complete. Consider her for future collaboration.'. Concurrently, create a research note for Dr. Souza with the exact content: 'Your review for art_02 is complete. Consider Prof. James Wilson for future collaboration.'. Display the updated article details.",
        "actions": [
            {
                "name": "SearchSubmissions",
                "arguments": {
                    "review_id": "rev_01"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "user_id": "res_01"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "user_id": "res_03"
                },
            },
            {
                "name": "FindCommonCollaborators",
                "arguments": {
                    "author1_name": "Dr. Kenji Tanaka",
                    "author2_name": "Prof. James Wilson"
                },
            },
            {
                "name": "UpdateArticleMetadata",
                "arguments": {
                    "article_id": "art_02",
                    "status": "pending_revision"
                },
            },
            {
                "name": "AddResearchNote",
                "arguments": {
                    "researcher_id": "res_03",
                    "article_id": "art_02",
                    "notes": "Review by Dr. Kenji Tanaka is complete. Consider her for future collaboration."
                },
            },
            {
                "name": "AddResearchNote",
                "arguments": {
                    "researcher_id": "res_01",
                    "article_id": "art_02",
                    "notes": "Your review for art_02 is complete. Consider Prof. James Wilson for future collaboration."
                },
            },
            {
                "name": "RetrievePapers",
                "arguments": {
                    "article_id": "art_02"
                }
            }
        ],
        "outputs": [
                "\"article_id\": \"art_02\"",
                "\"status\": \"pending_revision\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "peer_review_and_project_creation",
        "instruction": "Conduct journal editorial activities to establish the peer review process for the new submission 'AI applications in diagnosing neurodegenerative diseases' by Dr. Sarah Johnson. Create a submission record for it, then identify and assign 'Dr. Kenji Tanaka' and 'Dr. Anna Petrov' as reviewers, excluding the author from suggestions. Set the status of both the submission and the article to 'under_review'. To formally track this review, create a new project titled 'Review of AI in Diagnostics - 2025', with Dr. Mendes as the lead researcher and 'art_09' linked. Display the details of the updated submission.",
        "actions": [
            {
                "name": "RetrievePapers",
                "arguments": {
                    "title": "AI applications in diagnosing neurodegenerative diseases"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Sarah Johnson"
                },
            },
            {
                "name": "CreateSubmission",
                "arguments": {
                    "article_id": "art_09",
                    "author_user_id": "res_02",
                    "submission_id_override": "sub_09"
                },
            },
            {
                "name": "SuggestReviewers",
                "arguments": {
                    "article_id": "art_09",
                    "exclude_authors": [
                        "Dr. Sarah Johnson"
                    ]
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Kenji Tanaka"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Anna Petrov"
                },
            },
            {
                "name": "UpdateSubmission",
                "arguments": {
                    "submission_id": "sub_09",
                    "reviewers": [
                        "res_01",
                        "res_06"
                    ]
                },
            },
            {
                "name": "UpdateSubmission",
                "arguments": {
                    "submission_id": "sub_09",
                    "status": "under_review"
                },
            },
            {
                "name": "UpdateArticleMetadata",
                "arguments": {
                    "article_id": "art_09",
                    "status": "under_review"
                },
            },
            {
                "name": "RegisterProject",
                "arguments": {
                    "project_name": "Review of AI in Diagnostics - 2025",
                    "lead_researcher_id": "res_02",
                    "linked_article_id": "art_09",
                    "project_id_override": "proj_review_01"
                },
            },
            {
                "name": "SearchSubmissions",
                "arguments": {
                    "submission_id": "sub_09"
                }
            }
        ],
        "outputs": [
                "\"submission_id\": \"sub_09\"",
                "\"article_id\": \"art_09\"",
                "\"status\": \"under_review\"",
                "\"assigned_reviewers\": [\n      \"res_01\",\n      \"res_06\"\n    ]"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "preemptive_review_initiation",
        "instruction": "Execute journal integrity protocols to initiate a preemptive quality check for 'Dark Matter and the Large-Scale Structure of the Universe' (art_05) due to its heavy citation of 'Limits of Quantum Computing...' (art_02). Confirm this citation linkage. Create a submission record for 'art_05', setting both the submission and article status to 'internal_review'. Assign an external expert, Dr. Anna Petrov, as reviewer. Create a research note for both authors of 'art_05' (Tanaka and Costa) with the exact content: 'Your article is undergoing a standard internal quality check.'. Display the new submission details.",
        "actions": [
            {
                "name": "RetrievePapers",
                "arguments": {
                    "title": "Dark Matter and the Large-Scale Structure of the Universe"
                },
            },
            {
                "name": "GetCitationGraph",
                "arguments": {
                    "article_id": "art_05"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Liu Wei"
                },
            },
            {
                "name": "CreateSubmission",
                "arguments": {
                    "article_id": "art_05",
                    "author_user_id": "res_05",
                    "submission_id_override": "sub_07"
                },
            },
            {
                "name": "UpdateSubmission",
                "arguments": {
                    "submission_id": "sub_07",
                    "status": "internal_review"
                },
            },
            {
                "name": "UpdateArticleMetadata",
                "arguments": {
                    "article_id": "art_05",
                    "status": "internal_review"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Anna Petrov"
                },
            },
            {
                "name": "UpdateSubmission",
                "arguments": {
                    "submission_id": "sub_07",
                    "reviewers": [
                        "res_06"
                    ]
                },
            },
            {
                "name": "AddResearchNote",
                "arguments": {
                    "researcher_id": "res_05",
                    "article_id": "art_05",
                    "notes": "Your article is undergoing a standard internal quality check."
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Prof. James Wilson"
                },
            },
            {
                "name": "AddResearchNote",
                "arguments": {
                    "researcher_id": "res_03",
                    "article_id": "art_05",
                    "notes": "Your article is undergoing a standard internal quality check."
                },
            },
            {
                "name": "SearchSubmissions",
                "arguments": {
                    "submission_id": "sub_07"
                }
            }
        ],
        "outputs": [
                "\"submission_id\": \"sub_07\"",
                "\"status\": \"internal_review\"",
                "\"assigned_reviewers\": [\n      \"res_06\"\n    ]"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "legacy_article_revitalization",
        "instruction": "Manage editorial revitalization to revitalize older research by identifying 'Limits of Quantum Computing in Optimization Problems' (art_02), a highly cited article published before 2024, and its authors, Dr. Wei Zhang and Prof. James Wilson. Create a new draft article titled 'Revised: Limits of Quantum Computing V2' co-authored by Dr. Zhang and Prof. James Wilson, with the topic 'Quantum Physics' and publication year 2025. Subsequently, create a new project called 'Quantum Computing Review 2025', led by Dr. Zhang, linking this new draft article. Finally, create a research note for Prof. James Wilson with the exact content: 'You have been added to a new project: 'Quantum Computing Review 2025'.'. Display the new project details.",
        "actions": [
            {
                "name": "GetMostCitedArticles",
                "arguments": {
                {}
                },
            },
            {
                "name": "RetrievePapers",
                "arguments": {
                    "article_id": "art_02"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Wei Zhang"
                },
            },
            {
                "name": "FindCollaborationNetwork",
                "arguments": {
                    "author_name": "Dr. Wei Zhang"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Prof. James Wilson"
                },
            },
            {
                "name": "CreateArticle",
                "arguments": {
                    "title": "Revised: Limits of Quantum Computing V2",
                    "authors": [
                        "Dr. Wei Zhang",
                        "Prof. James Wilson"
                    ],
                    "topic": "Quantum Physics",
                    "publication_year": 2025,
                    "article_id_override": "art_10"
                },
            },
            {
                "name": "RegisterProject",
                "arguments": {
                    "project_name": "Quantum Computing Review 2025",
                    "lead_researcher_id": "res_03",
                    "linked_article_id": "art_10",
                    "project_id_override": "proj_qcr_25"
                },
            },
            {
                "name": "AddResearchNote",
                "arguments": {
                    "researcher_id": "res_03",
                    "article_id": "art_10",
                    "notes": "You have been added to a new project: 'Quantum Computing Review 2025'."
                },
            },
            {
                "name": "GetProjectDetails",
                "arguments": {
                    "project_id": "proj_qcr_25"
                }
            }
        ],
        "outputs": [
                "\"project_id\": \"proj_qcr_25\"",
                "\"lead_researcher_id\": \"res_03\"",
                "\"linked_articles\": [\n      \"art_10\"\n    ]"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "preemptive_integrity_check",
        "instruction": "Handle integrity management to initiate a preemptive integrity review for 'Advances in Language Models for Code Generation' (art_01), due to its citation of 'Limits of Quantum Computing...' (art_02), an article under suspicion. Create a submission for 'art_01' with status 'preemptive_integrity_review' and assign Dr. Anna Petrov as the reviewer. Create a research note for Dr. Kenji Tanaka, author of 'art_01', with the exact content: 'Your article is undergoing a preemptive integrity review based on its citation of art_02.'. Concurrently, update 'art_02's status to 'under_investigation'. Display the new submission details.",
        "actions": [
            {
                "name": "RetrievePapers",
                "arguments": {
                    "title": "Limits of Quantum Computing in Optimization Problems"
                },
            },
            {
                "name": "GetCitationGraph",
                "arguments": {
                    "article_id": "art_02"
                },
            },
            {
                "name": "RetrievePapers",
                "arguments": {
                    "article_id": "art_01"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Kenji Tanaka"
                },
            },
            {
                "name": "CreateSubmission",
                "arguments": {
                    "article_id": "art_01",
                    "author_user_id": "res_01",
                    "submission_id_override": "sub_06"
                },
            },
            {
                "name": "UpdateSubmission",
                "arguments": {
                    "submission_id": "sub_06",
                    "status": "preemptive_integrity_review"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Anna Petrov"
                },
            },
            {
                "name": "UpdateSubmission",
                "arguments": {
                    "submission_id": "sub_06",
                    "reviewers": [
                        "res_06"
                    ]
                },
            },
            {
                "name": "AddResearchNote",
                "arguments": {
                    "researcher_id": "res_01",
                    "article_id": "art_01",
                    "notes": "Your article is undergoing a preemptive integrity review based on its citation of art_02."
                },
            },
            {
                "name": "UpdateArticleMetadata",
                "arguments": {
                    "article_id": "art_02",
                    "status": "under_investigation"
                },
            },
            {
                "name": "SearchSubmissions",
                "arguments": {
                    "submission_id": "sub_06"
                }
            }
        ],
        "outputs": [
                "\"submission_id\": \"sub_06\"",
                "\"status\": \"preemptive_integrity_review\"",
                "\"assigned_reviewers\": [\n      \"res_06\"\n    ]"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "full_retraction_and_impact_audit",
        "instruction": "Execute institutional integrity protocols to fully retract 'Limits of Quantum Computing in Optimization Problems' (art_02) due to flawed data by updating its status to 'retracted'. For each article citing 'art_02', specifically 'Advances in Language Models for Code Generation' (art_01) and 'Dark Matter and the Large-Scale Structure of the Universe' (art_05), dispatch a high-relevance alert to their respective primary authors (Dr. Kenji Tanaka and Dr. Liu Wei) with the exact message: 'URGENT: An article you cited (art_02) has been retracted due to flawed data. Please review your work.'. Simultaneously, update the status of the 'Quantum Computing Applications' project, which is associated with 'art_02', to 'halted_pending_investigation'. Create a research note for the project lead, Prof. James Wilson, with the exact content: 'Project 'Quantum Computing Applications' has been halted pending investigation due to retraction of a key article.'. Display the final state of both the retracted article and the halted project.",
        "actions": [
            {
                "name": "UpdateArticleMetadata",
                "arguments": {
                    "article_id": "art_02",
                    "status": "retracted"
                },
            },
            {
                "name": "GetCitationGraph",
                "arguments": {
                    "article_id": "art_02"
                },
            },
            {
                "name": "RetrievePapers",
                "arguments": {
                    "article_id": "art_01"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Kenji Tanaka"
                },
            },
            {
                "name": "DispatchUserAlert",
                "arguments": {
                    "recipient_user_id": "res_01",
                    "sender_user_id": "system",
                    "message_content": "URGENT: An article you cited (art_02) has been retracted due to flawed data. Please review your work."
                },
            },
            {
                "name": "RetrievePapers",
                "arguments": {
                    "article_id": "art_05"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Liu Wei"
                },
            },
            {
                "name": "DispatchUserAlert",
                "arguments": {
                    "recipient_user_id": "res_05",
                    "sender_user_id": "system",
                    "message_content": "URGENT: An article you cited (art_02) has been retracted due to flawed data. Please review your work."
                },
            },
            {
                "name": "GetProjectDetails",
                "arguments": {
                    "linked_article_id": "art_02"
                },
            },
            {
                "name": "UpdateProject",
                "arguments": {
                    "project_id": "proj_01",
                    "status": "halted_pending_investigation"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "user_id": "res_03"
                },
            },
            {
                "name": "AddResearchNote",
                "arguments": {
                    "researcher_id": "res_03",
                    "article_id": "art_02",
                    "notes": "Project 'Quantum Computing Applications' has been halted pending investigation due to retraction of a key article."
                },
            },
            {
                "name": "RetrievePapers",
                "arguments": {
                    "article_id": "art_02"
                },
            },
            {
                "name": "GetProjectDetails",
                "arguments": {
                    "project_id": "proj_01"
                }
            }
        ],
        "outputs": [
                "\"article_id\": \"art_02\"",
                "\"status\": \"retracted\"",
                "\"project_id\": \"proj_01\"",
                "\"status\": \"halted_pending_investigation\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "publication_and_review_pipeline",
        "instruction": "Execute paper submission as Dr. Prof. James Wilson to submit your new co-authored paper with Dr. Liu Wei, 'Advanced Dark Matter Simulations'. Create a new article record for it (art_17) with the topic 'Astrophysics' and publication year 2025, then create a submission record (sub_11). Identify and assign Dr. Anna Petrov as a reviewer from Astrophysics, excluding yourself and Dr. Tanaka from suggestions. Set the status of both the submission and the article to 'awaiting_review'. Create a research note for Dr. Tanaka with the exact content: 'Our paper 'Advanced Dark Matter Simulations' has been submitted and is awaiting review.'. Display the new submission details.",
        "actions": [
            {
                "name": "CreateArticle",
                "arguments": {
                    "title": "Advanced Dark Matter Simulations",
                    "authors": [
                        "Prof. James Wilson",
                        "Dr. Liu Wei"
                    ],
                    "topic": "Astrophysics",
                    "publication_year": 2025,
                    "article_id_override": "art_17"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Prof. James Wilson"
                },
            },
            {
                "name": "CreateSubmission",
                "arguments": {
                    "article_id": "art_17",
                    "author_user_id": "res_03",
                    "submission_id_override": "sub_11"
                },
            },
            {
                "name": "SuggestReviewers",
                "arguments": {
                    "article_id": "art_17",
                    "exclude_authors": [
                        "Prof. James Wilson",
                        "Dr. Liu Wei"
                    ]
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Anna Petrov"
                },
            },
            {
                "name": "UpdateSubmission",
                "arguments": {
                    "submission_id": "sub_11",
                    "reviewers": [
                        "res_06"
                    ]
                },
            },
            {
                "name": "UpdateSubmission",
                "arguments": {
                    "submission_id": "sub_11",
                    "status": "awaiting_review"
                },
            },
            {
                "name": "UpdateArticleMetadata",
                "arguments": {
                    "article_id": "art_17",
                    "status": "awaiting_review"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Liu Wei"
                },
            },
            {
                "name": "AddResearchNote",
                "arguments": {
                    "researcher_id": "res_05",
                    "article_id": "art_17",
                    "notes": "Our paper 'Advanced Dark Matter Simulations' has been submitted and is awaiting review."
                },
            },
            {
                "name": "SearchSubmissions",
                "arguments": {
                    "submission_id": "sub_11"
                }
            }
        ],
        "outputs": [
                "\"submission_id\": \"sub_11\"",
                "\"status\": \"awaiting_review\"",
                "\"assigned_reviewers\": [\n      \"res_06\"\n    ]"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "complete_author_departure_protocol",
        "instruction": "Handle administrative processing to process the complete departure protocol for Dr. Wei Zhang. Archive all articles he authored by updating their status to 'archived_author_departed'. Unassign him as a reviewer from submission 'sub_01'. Identify and assign a new reviewer for 'sub_01' from the 'Quantum Physics' field, specifically Dr. Kenji Tanaka. Create a research note for the submission's author, Prof. James Wilson, with the exact content: 'Reviewer for sub_01 has been changed to Dr. Kenji Tanaka due to unforeseen circumstances.'. Display the updated submission details.",
        "actions": [
            {
                "name": "RetrievePapers",
                "arguments": {
                    "author_name": "Dr. Wei Zhang"
                },
            },
            {
                "name": "UpdateArticleMetadata",
                "arguments": {
                    "article_id": "art_02",
                    "status": "archived_author_departed"
                },
            },
            {
                "name": "UpdateArticleMetadata",
                "arguments": {
                    "article_id": "art_07",
                    "status": "archived_author_departed"
                },
            },
            {
                "name": "UpdateArticleMetadata",
                "arguments": {
                    "article_id": "art_10",
                    "status": "archived_author_departed"
                },
            },
            {
                "name": "SearchSubmissions",
                "arguments": {
                    "submission_id": "sub_01"
                },
            },
            {
                "name": "UpdateSubmission",
                "arguments": {
                    "submission_id": "sub_01",
                    "reviewers": []
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Kenji Tanaka"
                },
            },
            {
                "name": "UpdateSubmission",
                "arguments": {
                    "submission_id": "sub_01",
                    "reviewers": [
                        "res_01"
                    ]
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "user_id": "res_03"
                },
            },
            {
                "name": "AddResearchNote",
                "arguments": {
                    "researcher_id": "res_03",
                    "article_id": "art_02",
                    "notes": "Reviewer for sub_01 has been changed to Dr. Kenji Tanaka due to unforeseen circumstances."
                },
            },
            {
                "name": "SearchSubmissions",
                "arguments": {
                    "submission_id": "sub_01"
                }
            }
        ],
        "outputs": [
                "\"submission_id\": \"sub_01\"",
                "\"assigned_reviewers\": [\n      \"res_01\"\n    ]"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "advanced_research_project_initiation",
        "instruction": "Manage research project initiation as Dr. Thomas Anderson. You're initiating a new project focused on \"Precision Cancer Diagnostics using AI\". Your primary article for this project is 'Personalized Cancer Treatment with AI-Driven Drug Discovery' (art_14). You need to register this project with yourself as the lead researcher. This project will collaborate with Dr. Sarah Johnson and Dr. Anna Petrov. Ensure the project is funded by the 'Medical Research Council'. Update your profile to include 'Oncology' as a new research topic subscription, and set your UI theme to 'dark'. Concurrently, dispatch an alert to Dr. Sarah Johnson with the message: 'New project 'Precision Cancer Diagnostics using AI' initiated. Your expertise is key.'. Retrieve the author metrics for Dr. Anna Petrov, and finally, display the full details of the newly created project.",
        "actions": [
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Thomas Anderson"
                },
            },
            {
                "name": "RetrievePapers",
                "arguments": {
                    "title": "Personalized Cancer Treatment with AI-Driven Drug Discovery"
                },
            },
            {
                "name": "RegisterProject",
                "arguments": {
                    "project_name": "Precision Cancer Diagnostics using AI",
                    "lead_researcher_id": "res_04",
                    "linked_article_id": "art_14",
                    "project_id_override": "proj_cancer_ai"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Sarah Johnson"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Anna Petrov"
                },
            },
            {
                "name": "UpdateProject",
                "arguments": {
                    "project_id": "proj_cancer_ai",
                    "add_collaborators": [
                        "res_02",
                        "res_06"
                    ]
                },
            },
            {
                "name": "RetrieveFundingInfo",
                "arguments": {
                    "source_name": "Medical Research Council"
                },
            },
            {
                "name": "UpdateProject",
                "arguments": {
                    "project_id": "proj_cancer_ai",
                    "funding_source_id": "fs_03"
                },
            },
            {
                "name": "UpdateTopicSubscription",
                "arguments": {
                    "user_id": "res_04",
                    "topic": "Oncology",
                    "action": "add"
                },
            },
            {
                "name": "ConfigureProfileSettings",
                "arguments": {
                    "user_id": "res_04",
                    "ui_theme": "dark"
                },
            },
            {
                "name": "DispatchUserAlert",
                "arguments": {
                    "recipient_user_id": "res_02",
                    "sender_user_id": "res_04",
                    "message_content": "New project 'Precision Cancer Diagnostics using AI' initiated. Your expertise is key."
                },
            },
            {
                "name": "GetAuthorMetrics",
                "arguments": {
                    "author_name": "Dr. Anna Petrov"
                },
            },
            {
                "name": "GetProjectDetails",
                "arguments": {
                    "project_id": "proj_cancer_ai"
                }
            }
        ],
        "outputs": [
                "\"project_id\": \"proj_cancer_ai\"",
                "\"project_name\": \"Precision Cancer Diagnostics using AI\"",
                "\"lead_researcher_id\": \"res_04\"",
                "\"funding_source_id\": \"fs_03\"",
                "\"collaborators\": [\n      \"res_02\",\n      \"res_06\"\n    ]",
                "\"linked_articles\": [\n      \"art_14\"\n    ]"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "interdisciplinary_review_workflow",
        "instruction": "Conduct editorial management to manage a new submission for 'Multimodal AI for Medical Imaging Analysis' (art_12) by Dr. Kenji Tanaka. Create a submission record. Assign Dr. Sarah Johnson (Biomedicine) and Dr. Liu Wei (Astrophysics) as initial reviewers. Their availability should be checked first. If either is unavailable, find a suitable alternative reviewer from their respective fields who has collaborated with the article's co-author, Dr. Thomas Anderson. Create review assignments for the chosen reviewers, with the exact content 'Review initiated for interdisciplinary relevance.' and recommendation 'pending'. Log a research note for Dr. Kenji Tanaka with the exact content: 'Your article (art_12) has entered the review process.'. Finally, display the updated submission details.",
        "actions": [
            {
                "name": "RetrievePapers",
                "arguments": {
                    "title": "Multimodal AI for Medical Imaging Analysis"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Kenji Tanaka"
                },
            },
            {
                "name": "CreateSubmission",
                "arguments": {
                    "article_id": "art_12",
                    "author_user_id": "res_01",
                    "submission_id_override": "sub_multi_ai"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Sarah Johnson"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Liu Wei"
                },
            },
            {
                "name": "UpdateSubmission",
                "arguments": {
                    "submission_id": "sub_multi_ai",
                    "reviewers": [
                        "res_02",
                        "res_05"
                    ]
                },
            },
            {
                "name": "CreateReview",
                "arguments": {
                    "submission_id": "sub_multi_ai",
                    "reviewer_user_id": "res_02",
                    "content": "Review initiated for interdisciplinary relevance.",
                    "recommendation": "pending",
                    "review_id_override": "rev_multi_ai_mendes"
                },
            },
            {
                "name": "CreateReview",
                "arguments": {
                    "submission_id": "sub_multi_ai",
                    "reviewer_user_id": "res_05",
                    "content": "Review initiated for interdisciplinary relevance.",
                    "recommendation": "pending",
                    "review_id_override": "rev_multi_ai_tanaka"
                },
            },
            {
                "name": "AddResearchNote",
                "arguments": {
                    "researcher_id": "res_01",
                    "article_id": "art_12",
                    "notes": "Your article (art_12) has entered the review process."
                },
            },
            {
                "name": "SearchSubmissions",
                "arguments": {
                    "submission_id": "sub_multi_ai"
                }
            }
        ],
        "outputs": [
                "\"submission_id\": \"sub_multi_ai\"",
                "\"status\": \"submitted\"",
                "\"assigned_reviewers\": [\n      \"res_02\",\n      \"res_05\"\n    ]"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "cross_disciplinary_impact_audit_full",
        "instruction": "Assess the cross-disciplinary impact of the 'Quantum Computing Applications' project. Begin by retrieving its details and lead researcher. Identify all articles that cite its main article ('art_02'). For each citing article, determine its primary author's research field. If any citing author's research field is different from the project lead's field, and the citing article has an 'AI' keyword, dispatch an alert to the project lead (Prof. James Wilson) confirming this cross-disciplinary impact. The alert message should be: 'Your work is having a significant cross-disciplinary impact on [Citing Author's Field] through [Citing Article Title].'. Display Prof. James Wilson's full user profile. Also, suggest potential reviewers for the project's main article (art_02), excluding Prof. James Wilson herself.",
        "actions": [
            {
                "name": "GetProjectDetails",
                "arguments": {
                    "project_name": "Quantum Computing Applications"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "user_id": "res_03"
                },
            },
            {
                "name": "GetCitationGraph",
                "arguments": {
                    "article_id": "art_02"
                },
            },
            {
                "name": "RetrievePapers",
                "arguments": {
                    "article_id": "art_01"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Kenji Tanaka"
                },
            },
            {
                "name": "RetrievePapers",
                "arguments": {
                    "article_id": "art_05"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Liu Wei"
                },
            },
            {
                "name": "DispatchUserAlert",
                "arguments": {
                    "recipient_user_id": "res_03",
                    "sender_user_id": "system",
                    "message_content": "Your work is having a significant cross-disciplinary impact on Artificial Intelligence through Advances in Language Models for Code Generation."
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "user_id": "res_03"
                },
            },
            {
                "name": "SuggestReviewers",
                "arguments": {
                    "article_id": "art_02",
                    "exclude_authors": [
                        "Prof. James Wilson"
                    ]
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"res_03\"",
                "\"name\": \"Prof. James Wilson\"",
                "\"research_field\": \"Astrophysics\"",
                "\"suggested_reviewers\": [\n      \"Dr. Sarah Johnson\",\n      \"Dr. Ana Oliveira\",\n      \"Dr. Thomas Anderson\",\n      \"Dr. Ricardo Mendes\",\n      \"Dr. Ahmed Hassan\",\n      \"Dr. Maria Santos\",\n      \"Dr. Carlos Ruiz\",\n      \"Dr. Carlos Silva\",\n      \"Dr. Sofia Bauer\",\n      \"Dr. Aisha Khan\",\n      \"Dr. Helena Souza\",\n      \"Lia Costa\",\n      \"Dr. Elena Rossi\"\n    ]"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "comprehensive_project_audit_and_update",
        "instruction": "Execute university administration duties to conduct a comprehensive audit for the 'Federated AI Systems' project. First, retrieve its full details. Then, verify its current funding source and its status. If the project's status is 'planning' and its funding source is 'AI Advancement Grant', update the project's status to 'active' and link 'Robotic Process Automation with Large Language Models' (art_15) as a secondary linked article. Create a research note for the lead researcher, Dr. Anna Petrov, with the exact content: 'Project status updated to active; new article linked.'. Additionally, retrieve the author metrics for Dr. Anna Petrov and her co-author Dr. Kenji Tanaka. Finally, display the updated project details.",
        "actions": [
            {
                "name": "GetProjectDetails",
                "arguments": {
                    "project_name": "Federated AI Systems"
                },
            },
            {
                "name": "RetrieveFundingInfo",
                "arguments": {
                    "funding_source_id": "fs_01"
                },
            },
            {
                "name": "RetrievePapers",
                "arguments": {
                    "title": "Robotic Process Automation with Large Language Models"
                },
            },
            {
                "name": "UpdateProject",
                "arguments": {
                    "project_id": "proj_04",
                    "status": "active"
                },
            },
            {
                "name": "UpdateProject",
                "arguments": {
                    "project_id": "proj_04",
                    "linked_articles": [
                        "art_06",
                        "art_15"
                    ]
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Anna Petrov"
                },
            },
            {
                "name": "AddResearchNote",
                "arguments": {
                    "researcher_id": "res_06",
                    "article_id": "art_15",
                    "notes": "Project status updated to active; new article linked."
                },
            },
            {
                "name": "GetAuthorMetrics",
                "arguments": {
                    "author_name": "Dr. Anna Petrov"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Kenji Tanaka"
                },
            },
            {
                "name": "GetAuthorMetrics",
                "arguments": {
                    "author_name": "Dr. Kenji Tanaka"
                },
            },
            {
                "name": "GetProjectDetails",
                "arguments": {
                    "project_id": "proj_04"
                }
            }
        ],
        "outputs": [
                "\"project_id\": \"proj_04\"",
                "\"status\": \"active\"",
                "\"funding_source_id\": \"fs_01\"",
                "\"linked_articles\": [\n      \"art_06\",\n      \"art_15\"\n    ]"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "journal_publication_tracking",
        "instruction": "As a journal editor, track the full publication process for 'Advanced Dark Matter Simulations' (art_17). First, ensure a submission record exists for this article. If the submission status is 'awaiting_review', update it to 'under_review' and assign Dr. Anna Petrov as reviewer. Then, simulate a review from Dr. Anna Petrov with the exact content 'Minor revisions required for clarity.' and recommendation 'minor_revisions'. Update the submission status to 'minor_revisions_requested'. Dispatch an alert to the article's author, Prof. James Wilson, with the message: 'Your article, \"Advanced Dark Matter Simulations\", has received a review. Minor revisions requested.'. Display the final submission details.",
        "actions": [
            {
                "name": "CreateSubmission",
                "arguments": {
                    "article_id": "art_17",
                    "author_user_id": "res_03",
                    "submission_id_override": "sub_11"
                },
            },
            {
                "name": "SearchSubmissions",
                "arguments": {
                    "article_id": "art_17"
                },
            },
            {
                "name": "UpdateSubmission",
                "arguments": {
                    "submission_id": "sub_11",
                    "status": "under_review"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Anna Petrov"
                },
            },
            {
                "name": "UpdateSubmission",
                "arguments": {
                    "submission_id": "sub_11",
                    "reviewers": [
                        "res_06"
                    ]
                },
            },
            {
                "name": "CreateReview",
                "arguments": {
                    "submission_id": "sub_11",
                    "reviewer_user_id": "res_06",
                    "content": "Minor revisions required for clarity.",
                    "recommendation": "minor_revisions"
                },
            },
            {
                "name": "UpdateSubmission",
                "arguments": {
                    "submission_id": "sub_11",
                    "status": "minor_revisions_requested"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Prof. James Wilson"
                },
            },
            {
                "name": "DispatchUserAlert",
                "arguments": {
                    "recipient_user_id": "res_03",
                    "sender_user_id": "system",
                    "message_content": "Your article, \"Advanced Dark Matter Simulations\", has received a review. Minor revisions requested."
                },
            },
            {
                "name": "SearchSubmissions",
                "arguments": {
                    "submission_id": "sub_11"
                }
            }
        ],
        "outputs": [
                "\"submission_id\": \"sub_11\"",
                "\"status\": \"minor_revisions_requested\"",
                "\"assigned_reviewers\": [\n      \"res_06\"\n    ]"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "researcher_onboarding_and_integration",
        "instruction": "As an institutional support specialist, onboard a new researcher, Dr. Carlos Silva (Astrophysics). Create his hypothetical new article 'Advanced Galaxy Formation Models' (art_18, year 2025). Then, create a new research note for him, linking it to this article (art_18), with the content: 'Welcome to Galaxy Studies Inc.!'. Subscribe him to the 'Astrophysics' topic and configure his profile settings to use the 'light' UI theme and receive 'in_app' notifications. Then, create a new project named 'Ruiz Onboarding: Galaxy Simulations', led by Dr. Carlos Silva, linking his hypothetical new article 'Advanced Galaxy Formation Models' (art_18). Concurrently, identify his collaboration network to help him connect with peers. Display Dr. Carlos Silva's full user profile, including user_id, name, and research_field, at the end.",
        "actions": [
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Carlos Silva"
                },
            },
            {
                "name": "CreateArticle",
                "arguments": {
                    "title": "Advanced Galaxy Formation Models",
                    "authors": [
                        "Dr. Carlos Silva"
                    ],
                    "topic": "Astrophysics",
                    "publication_year": 2025,
                    "article_id_override": "art_18"
                },
            },
            {
                "name": "AddResearchNote",
                "arguments": {
                    "researcher_id": "res_11",
                    "article_id": "art_18",
                    "notes": "Welcome to Galaxy Studies Inc.!"
                },
            },
            {
                "name": "UpdateTopicSubscription",
                "arguments": {
                    "user_id": "res_11",
                    "topic": "Astrophysics",
                    "action": "add"
                },
            },
            {
                "name": "ConfigureProfileSettings",
                "arguments": {
                    "user_id": "res_11",
                    "ui_theme": "light",
                    "notification_channel": "in_app"
                },
            },
            {
                "name": "RegisterProject",
                "arguments": {
                    "project_name": "Ruiz Onboarding: Galaxy Simulations",
                    "lead_researcher_id": "res_11",
                    "linked_article_id": "art_18",
                    "project_id_override": "proj_ruiz_onboard"
                },
            },
            {
                "name": "FindCollaborationNetwork",
                "arguments": {
                    "author_name": "Dr. Carlos Silva"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Carlos Silva"
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"res_11\"",
                "\"name\": \"Dr. Carlos Silva\"",
                "\"research_field\": \"Astrophysics\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "comprehensive_project_closure",
        "instruction": "As a project manager, you need to formally close the 'Next-Generation CRISPR Technologies' project (proj_03). Update its status to 'completed_successfully' and set the end date to today's date (2025-07-24). For all articles linked to this project ('art_03' and 'art_11'), update their status to 'published'. Create a research note for the project lead, Dr. Sarah Johnson, linking it to article 'art_03', stating: 'Project proj_03 has been successfully closed. All linked articles are now published.'. Concurrently, dispatch an alert to Dr. Sarah Johnson informing him: 'The Next-Generation CRISPR Technologies project is now officially closed. Congratulations on your publications!'. Display the final updated project details.",
        "actions": [
            {
                "name": "GetProjectDetails",
                "arguments": {
                    "project_name": "Next-Generation CRISPR Technologies"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Sarah Johnson"
                },
            },
            {
                "name": "UpdateProject",
                "arguments": {
                    "project_id": "proj_03",
                    "status": "completed_successfully",
                    "end_date": "2025-07-24"
                },
            },
            {
                "name": "RetrievePapers",
                "arguments": {
                    "article_id": "art_03"
                },
            },
            {
                "name": "UpdateArticleMetadata",
                "arguments": {
                    "article_id": "art_03",
                    "status": "published"
                },
            },
            {
                "name": "RetrievePapers",
                "arguments": {
                    "article_id": "art_11"
                },
            },
            {
                "name": "UpdateArticleMetadata",
                "arguments": {
                    "article_id": "art_11",
                    "status": "published"
                },
            },
            {
                "name": "AddResearchNote",
                "arguments": {
                    "researcher_id": "res_02",
                    "article_id": "art_03",
                    "notes": "Project proj_03 has been successfully closed. All linked articles are now published."
                },
            },
            {
                "name": "DispatchUserAlert",
                "arguments": {
                    "recipient_user_id": "res_02",
                    "sender_user_id": "system",
                    "message_content": "The Next-Generation CRISPR Technologies project is now officially closed. Congratulations on your publications!"
                },
            },
            {
                "name": "GetProjectDetails",
                "arguments": {
                    "project_id": "proj_03"
                }
            }
        ],
        "outputs": [
                "\"project_id\": \"proj_03\"",
                "\"status\": \"completed_successfully\"",
                "\"end_date\": \"2025-07-24\"",
                "\"linked_articles\": [\n      \"art_03\",\n      \"art_11\"\n    ]"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "advanced_submission_rejection_protocol",
        "instruction": "As an editor-in-chief, you need to process the rejection of submission 'sub_02' for the article 'New Biomarkers for Early Detection of Neurodegenerative Diseases' (art_04) by Dr. Thomas Anderson. Update the submission's status to 'rejected' and the article's status to 'archived'. Retrieve the review content for review 'rev_02' of 'sub_02'. Based on this exact review content, dispatch a detailed rejection alert to Dr. Thomas Anderson. The alert message should be: 'Your submission for \"New Biomarkers for Early Detection of Neurodegenerative Diseases\" has been rejected. Key feedback: [EXACT REVIEW CONTENT]. We encourage you to revise and resubmit.'. Unassign all reviewers from 'sub_02'. Create a research note for Dr. Thomas Anderson stating: 'Submission sub_02 rejected due to review feedback.'. Display the final submission details.",
        "actions": [
            {
                "name": "SearchSubmissions",
                "arguments": {
                    "submission_id": "sub_02"
                },
            },
            {
                "name": "UpdateSubmission",
                "arguments": {
                    "submission_id": "sub_02",
                    "status": "rejected"
                },
            },
            {
                "name": "UpdateArticleMetadata",
                "arguments": {
                    "article_id": "art_04",
                    "status": "archived"
                },
            },
            {
                "name": "SearchSubmissions",
                "arguments": {
                    "review_id": "rev_02"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Thomas Anderson"
                },
            },
            {
                "name": "DispatchUserAlert",
                "arguments": {
                    "recipient_user_id": "res_04",
                    "sender_user_id": "system",
                    "message_content": "Your submission for \"New Biomarkers for Early Detection of Neurodegenerative Diseases\" has been rejected. Key feedback: Innovative approach to biomarker detection. The statistical analysis is robust, though the sample size could be larger for more definitive conclusions.. We encourage you to revise and resubmit."
                },
            },
            {
                "name": "UpdateSubmission",
                "arguments": {
                    "submission_id": "sub_02",
                    "reviewers": []
                },
            },
            {
                "name": "AddResearchNote",
                "arguments": {
                    "researcher_id": "res_04",
                    "article_id": "art_04",
                    "notes": "Submission sub_02 rejected due to review feedback."
                },
            },
            {
                "name": "SearchSubmissions",
                "arguments": {
                    "submission_id": "sub_02"
                }
            }
        ],
        "outputs": [
                "\"submission_id\": \"sub_02\"",
                "\"status\": \"rejected\"",
                "\"assigned_reviewers\": []"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "inter_institutional_research_proposal",
        "instruction": "As a grant coordinator, you are preparing a joint research proposal between FutureML and MediCore. Identify a key AI researcher from FutureML, Dr. Kenji Tanaka, and a key Biomedicine researcher from MediCore, Dr. Sarah Johnson. Retrieve their latest articles and author metrics. Identify any common collaborators between them. Create a new research project titled 'AI in Healthcare Diagnostics', led by Dr. Kenji Tanaka, linking her latest article 'Multimodal AI for Medical Imaging Analysis' (art_12) and Dr. Sarah Johnson's latest article 'AI applications in diagnosing neurodegenerative diseases' (art_09). Formally add Dr. Sarah Johnson as a collaborator. This project should be initially set to 'proposal' status. Secure funding for this project with the 'Machine Learning Excellence Award'. Display the final, fully configured project details.",
        "actions": [
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Kenji Tanaka",
                    "institution": "FutureML"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Sarah Johnson",
                    "institution": "MediCore"
                },
            },
            {
                "name": "RetrievePapers",
                "arguments": {
                    "author_name": "Dr. Kenji Tanaka",
                    "publication_year": 2025
                },
            },
            {
                "name": "RetrievePapers",
                "arguments": {
                    "author_name": "Dr. Sarah Johnson",
                    "publication_year": 2025
                },
            },
            {
                "name": "GetAuthorMetrics",
                "arguments": {
                    "author_name": "Dr. Kenji Tanaka"
                },
            },
            {
                "name": "GetAuthorMetrics",
                "arguments": {
                    "author_name": "Dr. Sarah Johnson"
                },
            },
            {
                "name": "FindCommonCollaborators",
                "arguments": {
                    "author1_name": "Dr. Kenji Tanaka",
                    "author2_name": "Dr. Sarah Johnson"
                },
            },
            {
                "name": "RegisterProject",
                "arguments": {
                    "project_name": "AI in Healthcare Diagnostics",
                    "lead_researcher_id": "res_01",
                    "linked_article_id": "art_12",
                    "project_id_override": "proj_health_diag"
                },
            },
            {
                "name": "UpdateProject",
                "arguments": {
                    "project_id": "proj_health_diag",
                    "add_collaborators": [
                        "res_02"
                    ]
                },
            },
            {
                "name": "UpdateProject",
                "arguments": {
                    "project_id": "proj_health_diag",
                    "linked_articles": [
                        "art_12",
                        "art_09"
                    ]
                },
            },
            {
                "name": "UpdateProject",
                "arguments": {
                    "project_id": "proj_health_diag",
                    "status": "proposal"
                },
            },
            {
                "name": "RetrieveFundingInfo",
                "arguments": {
                    "source_name": "Machine Learning Excellence Award"
                },
            },
            {
                "name": "UpdateProject",
                "arguments": {
                    "project_id": "proj_health_diag",
                    "funding_source_id": "fs_08"
                },
            },
            {
                "name": "GetProjectDetails",
                "arguments": {
                    "project_id": "proj_health_diag"
                }
            }
        ],
        "outputs": [
                "\"project_id\": \"proj_health_diag\"",
                "\"project_name\": \"AI in Healthcare Diagnostics\"",
                "\"lead_researcher_id\": \"res_01\"",
                "\"collaborators\": [\n      \"res_02\"\n    ]",
                "\"linked_articles\": [\n      \"art_12\",\n      \"art_09\"\n    ]",
                "\"status\": \"proposal\"",
                "\"funding_source_id\": \"fs_08\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "research_influence_and_project_update",
        "instruction": "Perform research impact analysis to assess the influence of Dr. Sarah Johnson's article 'AI applications in diagnosing neurodegenerative diseases' (art_09). First, ensure the project 'Review of AI in Diagnostics - 2025' (proj_review_01) exists, led by Dr. Sarah Johnson and linked to 'art_09'. Then, retrieve details of 'art_09'. Get its full citation graph to identify all citing articles and their primary authors. Find out how many unique articles cite 'art_09'. Then, identify 'Dr. Sarah Johnson's most cited article. If 'AI applications in diagnosing neurodegenerative diseases' (art_09) is NOT his most cited article, create a high-relevance research note for him stating: 'Your article 'AI applications in diagnosing neurodegenerative diseases' is highly cited, but not your top cited work. Consider promoting it further.'. The research note should be linked to art_09. Update the project 'Review of AI in Diagnostics - 2025' (proj_review_01) by adding Dr. Kenji Tanaka and Dr. Anna Petrov as collaborators. Finally, display the details of the updated project.",
        "actions": [
            {
                "name": "RegisterProject",
                "arguments": {
                    "project_name": "Review of AI in Diagnostics - 2025",
                    "lead_researcher_id": "res_02",
                    "linked_article_id": "art_09",
                    "project_id_override": "proj_review_01"
                },
            },
            {
                "name": "RetrievePapers",
                "arguments": {
                    "article_id": "art_09"
                },
            },
            {
                "name": "GetCitationGraph",
                "arguments": {
                    "article_id": "art_09"
                },
            },
            {
                "name": "GetAuthorMetrics",
                "arguments": {
                    "author_name": "Dr. Sarah Johnson"
                },
            },
            {
                "name": "GetMostCitedArticles",
                "arguments": {
                {}
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Sarah Johnson"
                },
            },
            {
                "name": "AddResearchNote",
                "arguments": {
                    "researcher_id": "res_02",
                    "article_id": "art_09",
                    "notes": "Your article 'AI applications in diagnosing neurodegenerative diseases' is highly cited, but not your top cited work. Consider promoting it further.",
                    "relevance": "high"
                },
            },
            {
                "name": "GetProjectDetails",
                "arguments": {
                    "project_name": "Review of AI in Diagnostics - 2025"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Kenji Tanaka"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Anna Petrov"
                },
            },
            {
                "name": "UpdateProject",
                "arguments": {
                    "project_id": "proj_review_01",
                    "add_collaborators": [
                        "res_01",
                        "res_06"
                    ]
                },
            },
            {
                "name": "GetProjectDetails",
                "arguments": {
                    "project_id": "proj_review_01"
                }
            }
        ],
        "outputs": [
                "\"project_id\": \"proj_review_01\"",
                "\"lead_researcher_id\": \"res_02\"",
                "\"linked_articles\": [\n      \"art_09\"\n    ]",
                "\"collaborators\": [\n      \"res_01\",\n      \"res_06\"\n    ]"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "research_field_expansion_and_collaboration_alert",
        "instruction": "As Dr. Kenji Tanaka (AI researcher), you want to expand your research focus to include 'Biomedicine'. Update your topic subscriptions to include 'Biomedicine' and remove 'Quantum Physics'. Ensure your UI theme is 'light' and notifications are 'in_app'. Then, identify Dr. Thomas Anderson (Biomedicine researcher) and Dr. Sarah Johnson (Biomedicine researcher) as potential collaborators. Retrieve their author metrics. If Dr. Thomas Anderson has a publication in 2025 related to 'Biomedicine' (art_04), log a high-relevance research note for yourself: 'Potential collaboration with Dr. Thomas Anderson on Biomarkers.'. Dispatch an alert to Dr. Sarah Johnson: 'Exploring new collaborations in Biomedicine. Your work is highly relevant.'. Display your updated profile settings.",
        "actions": [
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Kenji Tanaka"
                },
            },
            {
                "name": "UpdateTopicSubscription",
                "arguments": {
                    "user_id": "res_01",
                    "topic": "Biomedicine",
                    "action": "add"
                },
            },
            {
                "name": "UpdateTopicSubscription",
                "arguments": {
                    "user_id": "res_01",
                    "topic": "Quantum Physics",
                    "action": "remove"
                },
            },
            {
                "name": "ConfigureProfileSettings",
                "arguments": {
                    "user_id": "res_01",
                    "ui_theme": "light",
                    "notification_channel": "in_app"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Thomas Anderson"
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Sarah Johnson"
                },
            },
            {
                "name": "GetAuthorMetrics",
                "arguments": {
                    "author_name": "Dr. Thomas Anderson"
                },
            },
            {
                "name": "GetAuthorMetrics",
                "arguments": {
                    "author_name": "Dr. Sarah Johnson"
                },
            },
            {
                "name": "RetrievePapers",
                "arguments": {
                    "author_name": "Dr. Thomas Anderson",
                    "year": 2025,
                    "topic": "Biomedicine"
                },
            },
            {
                "name": "AddResearchNote",
                "arguments": {
                    "researcher_id": "res_01",
                    "article_id": "art_04",
                    "notes": "Potential collaboration with Dr. Thomas Anderson on Biomarkers.",
                    "relevance": "high"
                },
            },
            {
                "name": "DispatchUserAlert",
                "arguments": {
                    "recipient_user_id": "res_02",
                    "sender_user_id": "res_01",
                    "message_content": "Exploring new collaborations in Biomedicine. Your work is highly relevant."
                },
            },
            {
                "name": "FindResearcherProfiles",
                "arguments": {
                    "name": "Dr. Kenji Tanaka"
                }
            }
        ],
        "outputs": [
                "\"user_id\": \"res_01\"",
                "\"notification_channel\": \"in_app\"",
                "\"ui_theme\": \"light\"",
                "\"topic\": \"Biomedicine\""
        ]
    }
]
