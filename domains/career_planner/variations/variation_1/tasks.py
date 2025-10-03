# Copyright Sierra

tasks = [
    {
        "annotator": 0,
        "user_id": "res_70",
        "instruction": "For the 'UX Design Lead' role, manage the applications submitted by Alexander Adams and Emily Johnson. Start by conducting skill evaluations for each candidate in relation to the position. Subsequently, suggest 'Design Operations' training for Chloe and 'Accessibility' training for Emily. Lastly, change Chloe's application status to 'Interview Scheduled' and arrange her interview, while changing Emily's status to 'Waitlist'.",
        "actions": [
            {
                "name": "GetJobIdByTitle",
                "arguments": {
                    "job_title": "UX Design Lead"
                },
            },
            {
                "name": "GetJobApplications",
                "arguments": {
                    "job_id": "J002"
                },
            },
            {
                "name": "AnalyzeApplicantSkillFit",
                "arguments": {
                    "applicant_id": "U307",
                    "role": "UX Design Lead"
                },
            },
            {
                "name": "AnalyzeExternalCandidateSkillFit",
                "arguments": {
                    "candidate_id": "EXT003",
                    "role": "UX Design Lead"
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "U307",
                    "skill": "Design Operations"
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "EXT003",
                    "skill": "Accessibility"
                },
            },
            {
                "name": "UpdateApplicationStatus",
                "arguments": {
                    "application_id": "APP005",
                    "new_status": "Interview Scheduled"
                },
            },
            {
                "name": "UpdateApplicationStatus",
                "arguments": {
                    "application_id": "APP006",
                    "new_status": "Waitlist"
                },
            },
            {
                "name": "ScheduleTechnicalInterview",
                "arguments": {
                    "application_id": "APP005"
                }
            }
        ],
        "outputs": [
                "U307 needs Design Operations training",
                "EXT003 needs Accessibility training",
                "APP005 Interview Scheduled",
                "APP006 Waitlist",
                "Technical interview scheduled for application APP005"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_71",
        "instruction": "Examine and handle application APP007 (DevOps Engineer candidate U306) for position J003 by conducting a skill assessment, offering Infrastructure as Code training to U306, evaluating the external candidate EXT004 as a backup pipeline option with Monitoring & Logging training, updating APP007 to Training-Plan status, and arranging a technical interview.",
        "actions": [
            {
                "name": "GetJobApplications",
                "arguments": {
                    "job_id": "J003"
                },
            },
            {
                "name": "GetJobPosting",
                "arguments": {
                    "job_id": "J003"
                },
            },
            {
                "name": "GetRoleSkills",
                "arguments": {
                    "role": "DevOps Engineer"
                },
            },
            {
                "name": "AnalyzeApplicantSkillFit",
                "arguments": {
                    "applicant_id": "U306",
                    "role": "DevOps Engineer"
                },
            },
            {
                "name": "SearchExternalCandidatesBySkills",
                "arguments": {
                    "required_skills": [
                        "CI/CD",
                        "Containerization",
                        "Cloud Platforms",
                        "Infrastructure as Code",
                        "Monitoring & Logging"
                    ]
                },
            },
            {
                "name": "AnalyzeExternalCandidateSkillFit",
                "arguments": {
                    "candidate_id": "EXT004",
                    "role": "DevOps Engineer"
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "U306",
                    "skill": "Infrastructure as Code"
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "EXT004",
                    "skill": "Monitoring & Logging"
                },
            },
            {
                "name": "UpdateApplicationStatus",
                "arguments": {
                    "application_id": "APP007",
                    "new_status": "Training-Plan"
                },
            },
            {
                "name": "ScheduleTechnicalInterview",
                "arguments": {
                    "application_id": "APP007"
                }
            }
        ],
        "outputs": [
                "U306 needs Infrastructure as Code training",
                "EXT004 needs Monitoring & Logging training",
                "APP007 Training-Plan",
                "Interview scheduled for APP007"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_72",
        "instruction": "Review applications APP001 (Harper Bennett, U302) and APP002 (Alexander Adams, U310) for the Senior Data Scientist role (J001). Evaluate their skills and promote the more qualified candidate to the final interview stage.",
        "actions": [
            {
                "name": "GetJobPosting",
                "arguments": {
                    "job_id": "J001"
                },
            },
            {
                "name": "GetRoleSkills",
                "arguments": {
                    "role": "Senior Data Scientist"
                },
            },
            {
                "name": "GetJobApplications",
                "arguments": {
                    "job_id": "J001"
                },
            },
            {
                "name": "AnalyzeApplicantSkillFit",
                "arguments": {
                    "applicant_id": "U302",
                    "role": "Senior Data Scientist"
                },
            },
            {
                "name": "AnalyzeApplicantSkillFit",
                "arguments": {
                    "applicant_id": "U310",
                    "role": "Senior Data Scientist"
                },
            },
            {
                "name": "SearchExternalCandidatesBySkills",
                "arguments": {
                    "required_skills": [
                        "Machine Learning",
                        "Programming Languages",
                        "Data Visualization",
                        "Statistical Analysis"
                    ]
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "U302",
                    "skill": "Machine Learning"
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "U310",
                    "skill": "Machine Learning"
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "U310",
                    "skill": "Programming Languages"
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "U310",
                    "skill": "Data Visualization"
                },
            },
            {
                "name": "UpdateApplicationStatus",
                "arguments": {
                    "application_id": "APP001",
                    "new_status": "Final-Interview"
                },
            },
            {
                "name": "UpdateApplicationStatus",
                "arguments": {
                    "application_id": "APP002",
                    "new_status": "Rejected-Skill-Fit"
                },
            },
            {
                "name": "ScheduleTechnicalInterview",
                "arguments": {
                    "application_id": "APP001"
                }
            }
        ],
        "outputs": [
                "U302 needs Machine Learning training",
                "U310 needs Machine Learning training",
                "U310 needs Programming Languages training",
                "U310 needs Data Visualization training",
                "APP001 Final-Interview",
                "APP002 Rejected-Skill-Fit",
                "Interview scheduled for APP001"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_73",
        "instruction": "Handle application APP010 (external candidate EXT006) for the Security Analyst role (J005) by performing a skill evaluation, ensuring EXT006 qualifies as a shortlisted candidate, applying specific training suggestions in Cloud Security and Compliance, broadening the candidate pool with focused skill searching, and updating APP010 to indicate Interview-Pending status.",
        "actions": [
            {
                "name": "GetJobApplications",
                "arguments": {
                    "job_id": "J005"
                },
            },
            {
                "name": "GetJobPosting",
                "arguments": {
                    "job_id": "J005"
                },
            },
            {
                "name": "GetRoleSkills",
                "arguments": {
                    "role": "Security Analyst"
                },
            },
            {
                "name": "AnalyzeExternalCandidateSkillFit",
                "arguments": {
                    "candidate_id": "EXT006",
                    "role": "Security Analyst"
                },
            },
            {
                "name": "ShortlistExternalCandidate",
                "arguments": {
                    "candidate_id": "EXT006",
                    "job_id": "J005"
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "EXT006",
                    "skill": "Cloud Security"
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "EXT006",
                    "skill": "Compliance"
                },
            },
            {
                "name": "SearchExternalCandidatesBySkills",
                "arguments": {
                    "required_skills": [
                        "Cloud Security",
                        "Compliance"
                    ]
                },
            },
            {
                "name": "UpdateApplicationStatus",
                "arguments": {
                    "application_id": "APP010",
                    "new_status": "Interview-Pending"
                },
            },
            {
                "name": "ScheduleTechnicalInterview",
                "arguments": {
                    "application_id": "APP010"
                }
            }
        ],
        "outputs": [
                "EXT006 shortlisted",
                "EXT006 needs Cloud Security training",
                "EXT006 needs Compliance training",
                "APP010 Interview-Pending",
                "Interview scheduled for APP010"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_74",
        "instruction": "Initiate an expansion of the candidate pipeline for the Senior Data Scientist role (J001). Discover and create a shortlist of external candidates with knowledge in Machine Learning, Programming Languages, and Data Visualization, and subsequently design specific training programs to address any skill deficiencies.",
        "actions": [
            {
                "name": "GetJobPosting",
                "arguments": {
                    "job_id": "J001"
                },
            },
            {
                "name": "GetJobApplications",
                "arguments": {
                    "job_id": "J001"
                },
            },
            {
                "name": "GetRoleSkills",
                "arguments": {
                    "role": "Senior Data Scientist"
                },
            },
            {
                "name": "SearchExternalCandidatesBySkills",
                "arguments": {
                    "required_skills": [
                        "Machine Learning",
                        "Programming Languages",
                        "Data Visualization"
                    ]
                },
            },
            {
                "name": "AnalyzeExternalCandidateSkillFit",
                "arguments": {
                    "candidate_id": "EXT001",
                    "role": "Senior Data Scientist"
                },
            },
            {
                "name": "AnalyzeExternalCandidateSkillFit",
                "arguments": {
                    "candidate_id": "EXT002",
                    "role": "Senior Data Scientist"
                },
            },
            {
                "name": "ShortlistExternalCandidate",
                "arguments": {
                    "candidate_id": "EXT001",
                    "job_id": "J001"
                },
            },
            {
                "name": "ShortlistExternalCandidate",
                "arguments": {
                    "candidate_id": "EXT002",
                    "job_id": "J001"
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "EXT001",
                    "skill": "Data Visualization"
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "EXT002",
                    "skill": "Data Visualization"
                },
            },
            {
                "name": "ScheduleTechnicalInterview",
                "arguments": {
                    "application_id": "APP003"
                },
            },
            {
                "name": "ScheduleTechnicalInterview",
                "arguments": {
                    "application_id": "APP004"
                }
            }
        ],
        "outputs": [
                "EXT001 shortlisted",
                "EXT002 shortlisted",
                "EXT001 needs Data Visualization training",
                "EXT002 needs Data Visualization training",
                "Interview scheduled for APP003",
                "Interview scheduled for APP004"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_75",
        "instruction": "To aid David Adams's career shift, coordinate the establishment of a development plan. Initially, find a mentor with expertise in 'Policy' and 'Leadership' and create an 'Active' mentoring relationship. Subsequently, register him for the 'Climate Science & Policy' course. Lastly, add a goal to his profile with ID 'G303-2', type 'Role Transition', and description 'Develop policy and leadership skills for cloud compliance role.'",
        "actions": [
            {
                "name": "GetUserIdFromName",
                "arguments": {
                    "first_name": "Logan",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "FindMentors",
                "arguments": {
                    "mentee_id": "U303",
                    "focus_areas": [
                        "Policy",
                        "Leadership"
                    ]
                },
            },
            {
                "name": "GetCourseIdByName",
                "arguments": {
                    "course_name": "Climate Science & Policy"
                },
            },
            {
                "name": "GetTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "EnrollInCourse",
                "arguments": {
                    "user_id": "U303",
                    "course_id": "C1007",
                    "enroll_date": "2025-10-02"
                },
            },
            {
                "name": "AddMentorshipRelationship",
                "arguments": {
                    "mentor_id": "M102",
                    "mentee_id": "U303",
                    "start_date": "2025-10-02",
                    "status": "Active",
                    "focus_areas": [
                        "Policy",
                        "Leadership"
                    ]
                },
            },
            {
                "name": "AddGoal",
                "arguments": {
                    "user_id": "U303",
                    "goal": {
                        "goal_id": "G303-2",
                        "goal_type": "Role Transition",
                        "description": "Develop policy and leadership skills for cloud compliance role."
                    }
                }
            }
        ],
        "outputs": [
                "User U303 enrolled in course C1007",
                "Mentorship relationship MR011 created",
                "goal G303-2 added for U303"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_76",
        "instruction": "Delegate the task to Hiring manager Ava Nguyen to evaluate the application from internal candidate Harper Bennett for the 'Senior Data Scientist' role. He identifies potential but observes a skill gap in 'Machine Learning'. He aims to devise a development plan by enrolling her in the 'Machine Learning Specialization' course. Once she is enrolled, update her application status to 'Interview with Development Plan', arrange her technical interview, and add a new objective to her profile with ID 'G302-2', type 'Skill Mastery', and description 'Complete Machine Learning Specialization to support transition to Data Science.'",
        "actions": [
            {
                "name": "GetJobIdByTitle",
                "arguments": {
                    "job_title": "Senior Data Scientist"
                },
            },
            {
                "name": "GetJobApplications",
                "arguments": {
                    "job_id": "J001"
                },
            },
            {
                "name": "GetUserIdFromName",
                "arguments": {
                    "first_name": "Ava",
                    "last_name": "Nguyen"
                },
            },
            {
                "name": "AnalyzeApplicantSkillFit",
                "arguments": {
                    "applicant_id": "U302",
                    "role": "Senior Data Scientist"
                },
            },
            {
                "name": "GetCourseIdByName",
                "arguments": {
                    "course_name": "Machine Learning Specialization"
                },
            },
            {
                "name": "GetTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "EnrollInCourse",
                "arguments": {
                    "user_id": "U302",
                    "course_id": "C1005",
                    "enroll_date": "2025-10-02"
                },
            },
            {
                "name": "UpdateApplicationStatus",
                "arguments": {
                    "application_id": "APP001",
                    "new_status": "Interview with Development Plan"
                },
            },
            {
                "name": "ScheduleTechnicalInterview",
                "arguments": {
                    "application_id": "APP001"
                },
            },
            {
                "name": "AddGoal",
                "arguments": {
                    "user_id": "U302",
                    "goal": {
                        "goal_id": "G302-2",
                        "goal_type": "Skill Mastery",
                        "goal_description": "Complete Machine Learning Specialization to support transition to Data Science."
                    }
                }
            }
        ],
        "outputs": [
                "User U302 enrolled in course C1005",
                "APP001 Interview with Development Plan",
                "Technical interview scheduled for application APP001.",
                "goal G302-2 added for U302"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_77",
        "instruction": "Facilitate Manager Michael Rodriguez in starting a new data visualization initiative. Initially, enlist his entire engineering team, including himself and Robert Thompson, in the 'Data Visualization with Tableau' course. To bolster his leadership, identify a mentor for Mason with proficiency in 'Engineering' and 'Career Growth' and establish an 'Active' relationship. Then, amend Mason's 'Backend Tech Lead' goal to reflect 40% progress and include the note: 'Leading new team-wide data visualization project.' Conclude by scheduling their initial mentorship session for December 12, 2025.",
        "actions": [
            {
                "name": "GetUserIdFromName",
                "arguments": {
                    "first_name": "Mason",
                    "last_name": "Desai"
                },
            },
            {
                "name": "GetUserProfile",
                "arguments": {
                    "user_id": "U312"
                },
            },
            {
                "name": "GetTeam",
                "arguments": {
                    "team_id": "T003"
                },
            },
            {
                "name": "GetCourseIdByName",
                "arguments": {
                    "course_name": "Data Visualization with Tableau"
                },
            },
            {
                "name": "GetTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "EnrollInCourse",
                "arguments": {
                    "user_id": "U312",
                    "course_id": "C1003",
                    "enroll_date": "2025-10-02"
                },
            },
            {
                "name": "EnrollInCourse",
                "arguments": {
                    "user_id": "U306",
                    "course_id": "C1003",
                    "enroll_date": "2025-10-02"
                },
            },
            {
                "name": "FindMentors",
                "arguments": {
                    "mentee_id": "U312",
                    "focus_areas": [
                        "Engineering",
                        "Career Growth"
                    ]
                },
            },
            {
                "name": "AddMentorshipRelationship",
                "arguments": {
                    "mentor_id": "M101",
                    "mentee_id": "U312",
                    "start_date": "2025-10-02",
                    "status": "Active",
                    "focus_areas": [
                        "Engineering",
                        "Career Growth"
                    ]
                },
            },
            {
                "name": "ListUserGoals",
                "arguments": {
                    "user_id": "U312"
                },
            },
            {
                "name": "UpdateGoal",
                "arguments": {
                    "user_id": "U312",
                    "goal_id": "G312-1",
                    "progress_percent": 40,
                    "notes_to_append": "Leading new team-wide data visualization project.",
                    "last_updated_date": "2025-10-02"
                },
            },
            {
                "name": "ScheduleMentorshipSession",
                "arguments": {
                    "relationship_id": "MR011",
                    "session_date": "2025-12-12"
                }
            }
        ],
        "outputs": [
                "User U312 enrolled in course C1003",
                "User U306 enrolled in course C1003",
                "Mentorship relationship MR011 created",
                "Goal G312-1 updated for user U312",
                "scheduled_for: 2025-12-12"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_78",
        "instruction": "Broaden the candidate pipeline for the Marketing Specialist position (J004) by thoroughly identifying and evaluating external candidates, carry out skill assessments for EXT005, initiate focused Product Marketing and Brand Strategy training programs, create a shortlist for candidates with progression to EXT005, and move them from Skill-Enhanced to Interview-Ready status by scheduling technical interviews.",
        "actions": [
            {
                "name": "GetJobPosting",
                "arguments": {
                    "job_id": "J004"
                },
            },
            {
                "name": "GetRoleSkills",
                "arguments": {
                    "role": "Marketing Specialist"
                },
            },
            {
                "name": "GetJobApplications",
                "arguments": {
                    "job_id": "J004"
                },
            },
            {
                "name": "SearchExternalCandidatesBySkills",
                "arguments": {
                    "required_skills": [
                        "Product Marketing",
                        "Brand Strategy"
                    ]
                },
            },
            {
                "name": "AnalyzeExternalCandidateSkillFit",
                "arguments": {
                    "candidate_id": "EXT005",
                    "role": "Marketing Specialist"
                },
            },
            {
                "name": "ShortlistExternalCandidate",
                "arguments": {
                    "candidate_id": "EXT005",
                    "job_id": "J004"
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "EXT005",
                    "skill": "Product Marketing"
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "EXT005",
                    "skill": "Brand Strategy"
                },
            },
            {
                "name": "UpdateApplicationStatus",
                "arguments": {
                    "application_id": "APP009",
                    "new_status": "Skill-Enhanced"
                },
            },
            {
                "name": "UpdateApplicationStatus",
                "arguments": {
                    "application_id": "APP009",
                    "new_status": "Interview-Ready"
                },
            },
            {
                "name": "ScheduleTechnicalInterview",
                "arguments": {
                    "application_id": "APP009"
                }
            }
        ],
        "outputs": [
                "EXT005 shortlisted",
                "EXT005 needs Product Marketing training",
                "EXT005 needs Brand Strategy training",
                "APP009 Skill-Enhanced",
                "APP009 Interview-Ready",
                "Interview scheduled for APP009"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_79",
        "instruction": "Michael Rodriguez, the Team Lead, needs to enhance his engineering team's skills for a new data visualization project. Begin by enrolling his whole team in the 'Data Visualization with Tableau' course, ensuring that no one is enrolled more than once. Then, locate a mentor for Mason who has proficiency in 'Engineering' and 'Career Growth,' and set up an 'Active' mentorship. Lastly, include this note to Mason's current career goal: 'Leading new data-viz project to build team leadership skills.'",
        "actions": [
            {
                "name": "GetUserIdFromName",
                "arguments": {
                    "first_name": "Mason",
                    "last_name": "Desai"
                },
            },
            {
                "name": "GetUserProfile",
                "arguments": {
                    "user_id": "U312"
                },
            },
            {
                "name": "GetTeam",
                "arguments": {
                    "team_id": "T003"
                },
            },
            {
                "name": "GetCourseIdByName",
                "arguments": {
                    "course_name": "Data Visualization with Tableau"
                },
            },
            {
                "name": "GetTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "ListUserCourses",
                "arguments": {
                    "user_id": "U306"
                },
            },
            {
                "name": "ListUserCourses",
                "arguments": {
                    "user_id": "U312"
                },
            },
            {
                "name": "EnrollInCourse",
                "arguments": {
                    "user_id": "U306",
                    "course_id": "C1003",
                    "enroll_date": "2025-10-02"
                },
            },
            {
                "name": "EnrollInCourse",
                "arguments": {
                    "user_id": "U312",
                    "course_id": "C1003",
                    "enroll_date": "2025-10-02"
                },
            },
            {
                "name": "FindMentors",
                "arguments": {
                    "mentee_id": "U312",
                    "focus_areas": [
                        "Engineering",
                        "Career Growth"
                    ]
                },
            },
            {
                "name": "AddMentorshipRelationship",
                "arguments": {
                    "mentor_id": "M101",
                    "mentee_id": "U312",
                    "start_date": "2025-10-02",
                    "status": "Active",
                    "focus_areas": [
                        "Engineering",
                        "Career Growth"
                    ]
                },
            },
            {
                "name": "ListUserGoals",
                "arguments": {
                    "user_id": "U312"
                },
            },
            {
                "name": "UpdateGoal",
                "arguments": {
                    "user_id": "U312",
                    "goal_id": "G312-1",
                    "notes_to_append": "Leading new data-viz project to build team leadership skills.",
                    "last_updated_date": "2025-10-02"
                }
            }
        ],
        "outputs": [
                "User U306 enrolled in course C1003",
                "User U312 enrolled in course C1003",
                "Mentorship relationship MR011 created",
                "Goal G312-1 updated for user U312"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_80",
        "instruction": "For the Senior Data Scientist role (J001), ensure that the qualified external candidates EXT001 and EXT002 are shortlisted and arranged for technical interviews with the current applicants.",
        "actions": [
            {
                "name": "GetJobPosting",
                "arguments": {
                    "job_id": "J001"
                },
            },
            {
                "name": "GetRoleSkills",
                "arguments": {
                    "role": "Senior Data Scientist"
                },
            },
            {
                "name": "GetJobApplications",
                "arguments": {
                    "job_id": "J001"
                },
            },
            {
                "name": "SearchExternalCandidatesBySkills",
                "arguments": {
                    "required_skills": [
                        "Machine Learning",
                        "Programming Languages",
                        "Data Visualization"
                    ]
                },
            },
            {
                "name": "ShortlistExternalCandidate",
                "arguments": {
                    "candidate_id": "EXT001",
                    "job_id": "J001"
                },
            },
            {
                "name": "ShortlistExternalCandidate",
                "arguments": {
                    "candidate_id": "EXT002",
                    "job_id": "J001"
                },
            },
            {
                "name": "ScheduleTechnicalInterview",
                "arguments": {
                    "application_id": "APP003"
                },
            },
            {
                "name": "ScheduleTechnicalInterview",
                "arguments": {
                    "application_id": "APP004"
                }
            }
        ],
        "outputs": [
                "EXT001 shortlisted",
                "EXT002 shortlisted",
                "Interview scheduled for APP003",
                "Interview scheduled for APP004"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_81",
        "instruction": "Facilitate the progression of Advance UX Designer role (J002) applications APP005 (Alexander Adams, U307) and APP006 (Emily Johnson, EXT003) through detailed skill assessments, propose training to address Design Operations and Accessibility deficiencies, implement development plans, and set up interviews.",
        "actions": [
            {
                "name": "GetJobPosting",
                "arguments": {
                    "job_id": "J002"
                },
            },
            {
                "name": "GetRoleSkills",
                "arguments": {
                    "role": "UX Designer"
                },
            },
            {
                "name": "GetJobApplications",
                "arguments": {
                    "job_id": "J002"
                },
            },
            {
                "name": "AnalyzeApplicantSkillFit",
                "arguments": {
                    "applicant_id": "U307",
                    "role": "UX Designer"
                },
            },
            {
                "name": "AnalyzeExternalCandidateSkillFit",
                "arguments": {
                    "candidate_id": "EXT003",
                    "role": "UX Designer"
                },
            },
            {
                "name": "ShortlistExternalCandidate",
                "arguments": {
                    "candidate_id": "EXT003",
                    "job_id": "J002"
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "U307",
                    "skill": "Design Operations"
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "EXT003",
                    "skill": "Accessibility"
                },
            },
            {
                "name": "UpdateApplicationStatus",
                "arguments": {
                    "application_id": "APP005",
                    "new_status": "Development-Plan"
                },
            },
            {
                "name": "UpdateApplicationStatus",
                "arguments": {
                    "application_id": "APP006",
                    "new_status": "Development-Plan"
                },
            },
            {
                "name": "ScheduleTechnicalInterview",
                "arguments": {
                    "application_id": "APP005"
                },
            },
            {
                "name": "ScheduleTechnicalInterview",
                "arguments": {
                    "application_id": "APP006"
                }
            }
        ],
        "outputs": [
                "EXT003 shortlisted",
                "U307 needs Design Operations training",
                "EXT003 needs Accessibility training",
                "APP005 Development-Plan",
                "APP006 Development-Plan",
                "Interview scheduled for APP005",
                "Interview scheduled for APP006"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_82",
        "instruction": "Coordinate the creation of thorough cross-functional training programs for Harper Bennett (U302, Data Scientist) and candidate U306 (DevOps Engineer) based on detailed skill assessments, analysis of the external candidate pipeline, implementation of training, and progress through interview scheduling.",
        "actions": [
            {
                "name": "GetJobApplications",
                "arguments": {
                    "job_id": "J001"
                },
            },
            {
                "name": "GetJobApplications",
                "arguments": {
                    "job_id": "J003"
                },
            },
            {
                "name": "GetJobPosting",
                "arguments": {
                    "job_id": "J001"
                },
            },
            {
                "name": "GetJobPosting",
                "arguments": {
                    "job_id": "J003"
                },
            },
            {
                "name": "GetRoleSkills",
                "arguments": {
                    "role": "Senior Data Scientist"
                },
            },
            {
                "name": "GetRoleSkills",
                "arguments": {
                    "role": "DevOps Engineer"
                },
            },
            {
                "name": "AnalyzeApplicantSkillFit",
                "arguments": {
                    "applicant_id": "U302",
                    "role": "Senior Data Scientist"
                },
            },
            {
                "name": "AnalyzeApplicantSkillFit",
                "arguments": {
                    "applicant_id": "U306",
                    "role": "DevOps Engineer"
                },
            },
            {
                "name": "SearchExternalCandidatesBySkills",
                "arguments": {
                    "required_skills": [
                        "Machine Learning",
                        "Data Visualization"
                    ]
                },
            },
            {
                "name": "SearchExternalCandidatesBySkills",
                "arguments": {
                    "required_skills": [
                        "Infrastructure as Code",
                        "Monitoring & Logging"
                    ]
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "U302",
                    "skill": "Machine Learning"
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "U302",
                    "skill": "Data Visualization"
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "U306",
                    "skill": "Infrastructure as Code"
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "U306",
                    "skill": "Monitoring & Logging"
                },
            },
            {
                "name": "UpdateApplicationStatus",
                "arguments": {
                    "application_id": "APP001",
                    "new_status": "Training-Program"
                },
            },
            {
                "name": "UpdateApplicationStatus",
                "arguments": {
                    "application_id": "APP007",
                    "new_status": "Training-Program"
                },
            },
            {
                "name": "ScheduleTechnicalInterview",
                "arguments": {
                    "application_id": "APP001"
                },
            },
            {
                "name": "ScheduleTechnicalInterview",
                "arguments": {
                    "application_id": "APP007"
                }
            }
        ],
        "outputs": [
                "U302 needs Machine Learning training",
                "U302 needs Data Visualization training",
                "U306 needs Infrastructure as Code training",
                "U306 needs Monitoring & Logging training",
                "APP001 Training-Program",
                "APP007 Training-Program",
                "Interview scheduled for APP001",
                "Interview scheduled for APP007"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_84",
        "instruction": "David Adams is progressing toward his objective of transitioning to cloud compliance. To support him, identify a mentor with expertise in 'Policy' and 'Leadership' and establish an 'Active' mentorship. After forming the relationship, update his main career goal by adding the note: 'Mentorship with M102 started to build leadership skills.' Lastly, arrange their initial session for October 24, 2025.",
        "actions": [
            {
                "name": "GetUserIdFromName",
                "arguments": {
                    "first_name": "Logan",
                    "last_name": "Garcia"
                },
            },
            {
                "name": "ListUserCourses",
                "arguments": {
                    "user_id": "U303"
                },
            },
            {
                "name": "ListUserGoals",
                "arguments": {
                    "user_id": "U303"
                },
            },
            {
                "name": "FindMentors",
                "arguments": {
                    "mentee_id": "U303",
                    "focus_areas": [
                        "Policy",
                        "Leadership"
                    ]
                },
            },
            {
                "name": "GetTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddMentorshipRelationship",
                "arguments": {
                    "mentor_id": "M102",
                    "mentee_id": "U303",
                    "start_date": "2025-10-02",
                    "status": "Active",
                    "focus_areas": [
                        "Policy",
                        "Leadership"
                    ]
                },
            },
            {
                "name": "UpdateGoal",
                "arguments": {
                    "user_id": "U303",
                    "goal_id": "G303-1",
                    "notes_to_append": "Mentorship with M102 started to build leadership skills.",
                    "last_updated_date": "2025-10-02"
                },
            },
            {
                "name": "ScheduleMentorshipSession",
                "arguments": {
                    "relationship_id": "MR011",
                    "session_date": "2025-10-24"
                }
            }
        ],
        "outputs": [
                "Mentorship relationship MR011 created",
                "Goal G303-1 updated for user U303",
                "scheduled_for: 2025-10-24"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_85",
        "instruction": "Alexander Adams has completed the 'UX Design Fundamentals' course and is set to explore her leadership potential. Locate a mentor with 'Policy' and 'Design' expertise to form an 'Active' mentorship partnership with her. Subsequently, initiate a career goal for her with ID 'G307-3', type 'Leadership Development', and description 'Develop leadership skills for future Design Lead roles.' Conclude by planning their initial session for November 14, 2025.",
        "actions": [
            {
                "name": "GetUserIdFromName",
                "arguments": {
                    "first_name": "Chloe",
                    "last_name": "Scott"
                },
            },
            {
                "name": "GetCourseIdByName",
                "arguments": {
                    "course_name": "UX Design Fundamentals"
                },
            },
            {
                "name": "ListUserCourses",
                "arguments": {
                    "user_id": "U307"
                },
            },
            {
                "name": "FindMentors",
                "arguments": {
                    "mentee_id": "U307",
                    "focus_areas": [
                        "Policy",
                        "Design"
                    ]
                },
            },
            {
                "name": "GetTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "AddMentorshipRelationship",
                "arguments": {
                    "mentor_id": "M100",
                    "mentee_id": "U307",
                    "start_date": "2025-10-02",
                    "status": "Active",
                    "focus_areas": [
                        "Policy",
                        "Design"
                    ]
                },
            },
            {
                "name": "AddGoal",
                "arguments": {
                    "user_id": "U307",
                    "goal": {
                        "goal_id": "G307-3",
                        "goal_type": "Leadership Development",
                        "description": "Develop leadership skills for future Design Lead roles."
                    }
                },
            },
            {
                "name": "ScheduleMentorshipSession",
                "arguments": {
                    "relationship_id": "MR011",
                    "session_date": "2025-11-14"
                }
            }
        ],
        "outputs": [
                "Mentorship relationship MR011 created",
                "goal G307-3 added for U307",
                "scheduled_for: 2025-11-14"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_86",
        "instruction": "Promote application APP001 (Harper Bennett, U302) for the Senior Data Scientist role (J001) through a detailed skill evaluation, pinpoint specific skill deficiencies, apply focused training guidance for Machine Learning and Data Visualization, update status to Final-Interview, and arrange a technical interview.",
        "actions": [
            {
                "name": "GetJobPosting",
                "arguments": {
                    "job_id": "J001"
                },
            },
            {
                "name": "GetRoleSkills",
                "arguments": {
                    "role": "Senior Data Scientist"
                },
            },
            {
                "name": "GetJobApplications",
                "arguments": {
                    "job_id": "J001"
                },
            },
            {
                "name": "AnalyzeApplicantSkillFit",
                "arguments": {
                    "applicant_id": "U302",
                    "role": "Senior Data Scientist"
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "U302",
                    "skill": "Machine Learning"
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "U302",
                    "skill": "Data Visualization"
                },
            },
            {
                "name": "UpdateApplicationStatus",
                "arguments": {
                    "application_id": "APP001",
                    "new_status": "Skills-Enhanced"
                },
            },
            {
                "name": "UpdateApplicationStatus",
                "arguments": {
                    "application_id": "APP001",
                    "new_status": "Final-Interview"
                },
            },
            {
                "name": "ScheduleTechnicalInterview",
                "arguments": {
                    "application_id": "APP001"
                },
            },
            {
                "name": "AnalyzeApplicantSkillFit",
                "arguments": {
                    "applicant_id": "U302",
                    "role": "Senior Data Scientist"
                }
            }
        ],
        "outputs": [
                "U302 needs Machine Learning training",
                "U302 needs Data Visualization training",
                "APP001 Skills-Enhanced",
                "APP001 Final-Interview",
                "Interview scheduled for APP001"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_87",
        "instruction": "Handle detailed multi-position application processing for APP001 (U302, Senior Data Scientist), APP005 (U307, UX Designer), and APP007 (U306, DevOps Engineer) by conducting thorough skill assessments, delivering targeted training (Machine Learning for U302, Design Thinking for U307, Infrastructure as Code for U306), progressing candidates to an Interview-Ready status, and coordinating the scheduling of technical interviews.",
        "actions": [
            {
                "name": "GetJobApplications",
                "arguments": {
                    "job_id": "J001"
                },
            },
            {
                "name": "GetJobApplications",
                "arguments": {
                    "job_id": "J002"
                },
            },
            {
                "name": "GetJobApplications",
                "arguments": {
                    "job_id": "J003"
                },
            },
            {
                "name": "GetJobPosting",
                "arguments": {
                    "job_id": "J001"
                },
            },
            {
                "name": "GetJobPosting",
                "arguments": {
                    "job_id": "J002"
                },
            },
            {
                "name": "GetJobPosting",
                "arguments": {
                    "job_id": "J003"
                },
            },
            {
                "name": "GetRoleSkills",
                "arguments": {
                    "role": "Senior Data Scientist"
                },
            },
            {
                "name": "GetRoleSkills",
                "arguments": {
                    "role": "UX Designer"
                },
            },
            {
                "name": "GetRoleSkills",
                "arguments": {
                    "role": "DevOps Engineer"
                },
            },
            {
                "name": "AnalyzeApplicantSkillFit",
                "arguments": {
                    "applicant_id": "U302",
                    "role": "Senior Data Scientist"
                },
            },
            {
                "name": "AnalyzeApplicantSkillFit",
                "arguments": {
                    "applicant_id": "U307",
                    "role": "UX Designer"
                },
            },
            {
                "name": "AnalyzeApplicantSkillFit",
                "arguments": {
                    "applicant_id": "U306",
                    "role": "DevOps Engineer"
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "U302",
                    "skill": "Machine Learning"
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "U307",
                    "skill": "Design Thinking"
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "U306",
                    "skill": "Infrastructure as Code"
                },
            },
            {
                "name": "UpdateApplicationStatus",
                "arguments": {
                    "application_id": "APP001",
                    "new_status": "Interview-Ready"
                },
            },
            {
                "name": "UpdateApplicationStatus",
                "arguments": {
                    "application_id": "APP005",
                    "new_status": "Interview-Ready"
                },
            },
            {
                "name": "UpdateApplicationStatus",
                "arguments": {
                    "application_id": "APP007",
                    "new_status": "Interview-Ready"
                },
            },
            {
                "name": "ScheduleTechnicalInterview",
                "arguments": {
                    "application_id": "APP001"
                },
            },
            {
                "name": "ScheduleTechnicalInterview",
                "arguments": {
                    "application_id": "APP005"
                },
            },
            {
                "name": "ScheduleTechnicalInterview",
                "arguments": {
                    "application_id": "APP007"
                }
            }
        ],
        "outputs": [
                "U302 needs Machine Learning training",
                "U307 needs Design Thinking training",
                "U306 needs Infrastructure as Code training",
                "APP001 Interview-Ready",
                "APP005 Interview-Ready",
                "APP007 Interview-Ready",
                "Interview scheduled for APP001",
                "Interview scheduled for APP005",
                "Interview scheduled for APP007"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_88",
        "instruction": "Ava Nguyen, the manager, is aiming to create a development plan for his direct report, Harper Bennett, to ready her for a Senior Data Scientist position. Please arrange her enrollment in two courses: 'Advanced Python' and 'Data Visualization with Tableau'. Next, add a new career objective for her with the ID 'G302-3', type 'Role Transition', and the description 'Complete Python and Tableau training for Senior Data Scientist path.' Lastly, set up a new mentorship pairing with Ava Nguyen as the mentor and Harper Bennett as the mentee, concentrating on 'Python' and 'Data Science'.",
        "actions": [
            {
                "name": "GetUserIdFromName",
                "arguments": {
                    "first_name": "Jack",
                    "last_name": "Wang"
                },
            },
            {
                "name": "GetUserIdFromName",
                "arguments": {
                    "first_name": "Ava",
                    "last_name": "Nguyen"
                },
            },
            {
                "name": "GetCourseIdByName",
                "arguments": {
                    "course_name": "Advanced Python"
                },
            },
            {
                "name": "GetCourseIdByName",
                "arguments": {
                    "course_name": "Data Visualization with Tableau"
                },
            },
            {
                "name": "GetTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "EnrollInCourse",
                "arguments": {
                    "user_id": "U302",
                    "course_id": "C1001",
                    "enroll_date": "2025-10-02"
                },
            },
            {
                "name": "EnrollInCourse",
                "arguments": {
                    "user_id": "U302",
                    "course_id": "C1003",
                    "enroll_date": "2025-10-02"
                },
            },
            {
                "name": "AddGoal",
                "arguments": {
                    "user_id": "U302",
                    "goal": {
                        "goal_id": "G302-3",
                        "goal_type": "Role Transition",
                        "goal_description": "Complete Python and Tableau training for Senior Data Scientist path."
                    }
                },
            },
            {
                "name": "AddMentorshipRelationship",
                "arguments": {
                    "mentor_id": "U301",
                    "mentee_id": "U302",
                    "start_date": "2025-10-02",
                    "status": "Active",
                    "focus_areas": [
                        "Python",
                        "Data Science"
                    ]
                }
            }
        ],
        "outputs": [
                "User U302 enrolled in course C1001",
                "User U302 enrolled in course C1003",
                "goal G302-3 added for U302",
                "Mentorship relationship MR011 created"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_89",
        "instruction": "Manager Michael Rodriguez is overseeing a new data visualization project. Register both him and his team member Robert Thompson in the 'Data Visualization with Tableau' course. To aid his leadership in this project, locate a new mentor for Mason experienced in 'Engineering' and 'Career Growth' and form an 'Active' relationship. Next, revise Mason's primary career goal with the note 'Leading team data-viz upskilling initiative.' Lastly, arrange their initial mentorship session for November 7, 2025.",
        "actions": [
            {
                "name": "GetUserIdFromName",
                "arguments": {
                    "first_name": "Mason",
                    "last_name": "Desai"
                },
            },
            {
                "name": "GetUserIdFromName",
                "arguments": {
                    "first_name": "Alexander",
                    "last_name": "Adams"
                },
            },
            {
                "name": "GetCourseIdByName",
                "arguments": {
                    "course_name": "Data Visualization with Tableau"
                },
            },
            {
                "name": "GetTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "EnrollInCourse",
                "arguments": {
                    "user_id": "U312",
                    "course_id": "C1003",
                    "enroll_date": "2025-10-02"
                },
            },
            {
                "name": "EnrollInCourse",
                "arguments": {
                    "user_id": "U306",
                    "course_id": "C1003",
                    "enroll_date": "2025-10-02"
                },
            },
            {
                "name": "FindMentors",
                "arguments": {
                    "mentee_id": "U312",
                    "focus_areas": [
                        "Engineering",
                        "Career Growth"
                    ]
                },
            },
            {
                "name": "AddMentorshipRelationship",
                "arguments": {
                    "mentor_id": "M101",
                    "mentee_id": "U312",
                    "start_date": "2025-10-02",
                    "status": "Active",
                    "focus_areas": [
                        "Engineering",
                        "Career Growth"
                    ]
                },
            },
            {
                "name": "ListUserGoals",
                "arguments": {
                    "user_id": "U312"
                },
            },
            {
                "name": "UpdateGoal",
                "arguments": {
                    "user_id": "U312",
                    "goal_id": "G312-1",
                    "notes_to_append": "Leading team data-viz upskilling initiative.",
                    "last_updated_date": "2025-10-02"
                },
            },
            {
                "name": "ScheduleMentorshipSession",
                "arguments": {
                    "relationship_id": "MR011",
                    "session_date": "2025-11-07"
                }
            }
        ],
        "outputs": [
                "User U312 enrolled in course C1003",
                "User U306 enrolled in course C1003",
                "Mentorship relationship MR011 created",
                "Goal G312-1 updated for user U312",
                "scheduled_for: 2025-11-07"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_90",
        "instruction": "Handle comprehensive advancement for Security Analyst position (J005) for application APP010 (external candidate EXT006) by executing a detailed skill assessment, delivering targeted Cloud Security and Compliance training, enhancing the candidate pipeline with skill-based search, shortlisting EXT006, progressing through multiple stages from Skills-Enhanced to Interview-Pending to Background-Check status, and scheduling the technical interview.",
        "actions": [
            {
                "name": "GetJobApplications",
                "arguments": {
                    "job_id": "J005"
                },
            },
            {
                "name": "GetJobPosting",
                "arguments": {
                    "job_id": "J005"
                },
            },
            {
                "name": "GetRoleSkills",
                "arguments": {
                    "role": "Security Analyst"
                },
            },
            {
                "name": "AnalyzeExternalCandidateSkillFit",
                "arguments": {
                    "candidate_id": "EXT006",
                    "role": "Security Analyst"
                },
            },
            {
                "name": "SearchExternalCandidatesBySkills",
                "arguments": {
                    "required_skills": [
                        "Cloud Security",
                        "Compliance"
                    ]
                },
            },
            {
                "name": "ShortlistExternalCandidate",
                "arguments": {
                    "candidate_id": "EXT006",
                    "job_id": "J005"
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "EXT006",
                    "skill": "Cloud Security"
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "EXT006",
                    "skill": "Compliance"
                },
            },
            {
                "name": "UpdateApplicationStatus",
                "arguments": {
                    "application_id": "APP010",
                    "new_status": "Skills-Enhanced"
                },
            },
            {
                "name": "UpdateApplicationStatus",
                "arguments": {
                    "application_id": "APP010",
                    "new_status": "Interview-Pending"
                },
            },
            {
                "name": "UpdateApplicationStatus",
                "arguments": {
                    "application_id": "APP010",
                    "new_status": "Background-Check"
                },
            },
            {
                "name": "ScheduleTechnicalInterview",
                "arguments": {
                    "application_id": "APP010"
                }
            }
        ],
        "outputs": [
                "EXT006 shortlisted",
                "EXT006 needs Cloud Security training",
                "EXT006 needs Compliance training",
                "APP010 Skills-Enhanced",
                "APP010 Interview-Pending",
                "APP010 Background-Check",
                "Interview scheduled for APP010"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_91",
        "instruction": "Broaden the candidate pool for the Senior Data Scientist role (J001) by including external candidates EXT001 and EXT002 with strong technical expertise, administer skill evaluations, and execute tailored training suggestions.",
        "actions": [
            {
                "name": "GetRoleSkills",
                "arguments": {
                    "role": "Senior Data Scientist"
                },
            },
            {
                "name": "GetJobPosting",
                "arguments": {
                    "job_id": "J001"
                },
            },
            {
                "name": "SearchExternalCandidatesBySkills",
                "arguments": {
                    "required_skills": [
                        "Machine Learning",
                        "Programming Languages",
                        "Data Visualization"
                    ]
                },
            },
            {
                "name": "ShortlistExternalCandidate",
                "arguments": {
                    "candidate_id": "EXT001",
                    "job_id": "J001"
                },
            },
            {
                "name": "ShortlistExternalCandidate",
                "arguments": {
                    "candidate_id": "EXT002",
                    "job_id": "J001"
                },
            },
            {
                "name": "AnalyzeExternalCandidateSkillFit",
                "arguments": {
                    "candidate_id": "EXT001",
                    "role": "Senior Data Scientist"
                },
            },
            {
                "name": "AnalyzeExternalCandidateSkillFit",
                "arguments": {
                    "candidate_id": "EXT002",
                    "role": "Senior Data Scientist"
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "EXT001",
                    "skill": "Data Visualization"
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "EXT002",
                    "skill": "Data Visualization"
                }
            }
        ],
        "outputs": [
                "EXT001 shortlisted",
                "EXT002 shortlisted",
                "EXT001 needs Data Visualization training",
                "EXT002 needs Data Visualization training"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_92",
        "instruction": "Manager Michael Rodriguez is evaluating the progress on Alexander Adams's objective to 'Publish company-wide accessibility guidelines'. Initially, update this objective to indicate 50% completion and add the note: 'Guideline draft complete. Next step: training plan.' Subsequently, modify her current mentorship engagement to concentrate on 'Policy Writing' and 'Teamwork'. Then, register her for the 'Climate Science & Policy' course to aid this new focus. Conclude by arranging their next meeting for December 5, 2025.",
        "actions": [
            {
                "name": "GetUserIdFromName",
                "arguments": {
                    "first_name": "David",
                    "last_name": "Adams"
                },
            },
            {
                "name": "GetUserIdFromName",
                "arguments": {
                    "first_name": "Chloe",
                    "last_name": "Scott"
                },
            },
            {
                "name": "ListUserGoals",
                "arguments": {
                    "user_id": "U307"
                },
            },
            {
                "name": "ListUserMentorships",
                "arguments": {
                    "user_id": "U307"
                },
            },
            {
                "name": "GetCourseIdByName",
                "arguments": {
                    "course_name": "Climate Science & Policy"
                },
            },
            {
                "name": "GetTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "UpdateGoal",
                "arguments": {
                    "user_id": "U307",
                    "goal_id": "G307-1",
                    "progress_percent": 50,
                    "notes_to_append": "Guideline draft complete. Next step: training plan.",
                    "last_updated_date": "2025-10-02"
                },
            },
            {
                "name": "UpdateMentorshipRelationship",
                "arguments": {
                    "relationship_id": "MR003",
                    "updates": {
                        "focus_areas": [
                            "Policy Writing",
                            "Teamwork"
                        ]
                    }
                },
            },
            {
                "name": "EnrollInCourse",
                "arguments": {
                    "user_id": "U307",
                    "course_id": "C1007",
                    "enroll_date": "2025-10-02"
                },
            },
            {
                "name": "ScheduleMentorshipSession",
                "arguments": {
                    "relationship_id": "MR003",
                    "session_date": "2025-12-05"
                }
            }
        ],
        "outputs": [
                "Goal G307-1 updated for user U307",
                "relationship MR003 updated",
                "User U307 enrolled in course C1007",
                "scheduled_for: 2025-12-05"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_93",
        "instruction": "Ava Nguyen, the hiring manager, has assessed the application from internal candidate Alexander Adams for the 'Senior Data Scientist' position. He has opted to reject her for the present role but intends to place her on a developmental path for prospects. Initially, alter her application status to 'Rejected - Future Consideration with Dev Plan'. Subsequently, register her in two courses: 'Advanced Python' and 'Machine Learning Specialization'. Finally, incorporate a new goal into her profile with ID 'G310-2', type 'Role Transition', and description 'Complete Python and ML training for future Data Scientist opportunities.'",
        "actions": [
            {
                "name": "GetUserIdFromName",
                "arguments": {
                    "first_name": "Jack",
                    "last_name": "Wang"
                },
            },
            {
                "name": "GetUserIdFromName",
                "arguments": {
                    "first_name": "Harper",
                    "last_name": "Bennett"
                },
            },
            {
                "name": "GetJobIdByTitle",
                "arguments": {
                    "job_title": "Senior Data Scientist"
                },
            },
            {
                "name": "GetJobApplications",
                "arguments": {
                    "job_id": "J001"
                },
            },
            {
                "name": "UpdateApplicationStatus",
                "arguments": {
                    "application_id": "APP002",
                    "new_status": "Rejected - Future Consideration with Dev Plan"
                },
            },
            {
                "name": "GetCourseIdByName",
                "arguments": {
                    "course_name": "Advanced Python"
                },
            },
            {
                "name": "GetCourseIdByName",
                "arguments": {
                    "course_name": "Machine Learning Specialization"
                },
            },
            {
                "name": "GetTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "EnrollInCourse",
                "arguments": {
                    "user_id": "U310",
                    "course_id": "C1001",
                    "enroll_date": "2025-10-02"
                },
            },
            {
                "name": "EnrollInCourse",
                "arguments": {
                    "user_id": "U310",
                    "course_id": "C1005",
                    "enroll_date": "2025-10-02"
                },
            },
            {
                "name": "AddGoal",
                "arguments": {
                    "user_id": "U310",
                    "goal": {
                        "goal_id": "G310-2",
                        "goal_type": "Role Transition",
                        "description": "Complete Python and ML training for future Data Scientist opportunities."
                    }
                }
            }
        ],
        "outputs": [
                "APP002 Rejected - Future Consideration with Dev Plan",
                "User U310 enrolled in course C1001",
                "User U310 enrolled in course C1005",
                "goal G310-2 added for U310"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_94",
        "instruction": "To facilitate Ava Nguyen's ambition of ascending to Director of Data Science, please register him for two pivotal courses: the 'Machine Learning Specialization' and the 'Project Management Professional' course. Upon his enrollment, update his main career goal to reflect 40% progress and include the note: 'Enrolled in ML and PMP courses to build technical and leadership skills.' Lastly, revise his current mentorship connection to introduce 'Team Leadership' as a new focus area.",
        "actions": [
            {
                "name": "GetUserIdFromName",
                "arguments": {
                    "first_name": "Jack",
                    "last_name": "Wang"
                },
            },
            {
                "name": "ListUserGoals",
                "arguments": {
                    "user_id": "U301"
                },
            },
            {
                "name": "ListUserMentorships",
                "arguments": {
                    "user_id": "U301"
                },
            },
            {
                "name": "GetCourseIdByName",
                "arguments": {
                    "course_name": "Machine Learning Specialization"
                },
            },
            {
                "name": "GetCourseIdByName",
                "arguments": {
                    "course_name": "Project Management Professional"
                },
            },
            {
                "name": "GetTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "EnrollInCourse",
                "arguments": {
                    "user_id": "U301",
                    "course_id": "C1005",
                    "enroll_date": "2025-10-02"
                },
            },
            {
                "name": "EnrollInCourse",
                "arguments": {
                    "user_id": "U301",
                    "course_id": "C1004",
                    "enroll_date": "2025-10-02"
                },
            },
            {
                "name": "UpdateGoal",
                "arguments": {
                    "user_id": "U301",
                    "goal_id": "G301-1",
                    "progress_percent": 40,
                    "notes_to_append": "Enrolled in ML and PMP courses to build technical and leadership skills.",
                    "last_updated_date": "2025-10-02"
                },
            },
            {
                "name": "UpdateMentorshipRelationship",
                "arguments": {
                    "relationship_id": "MR001",
                    "updates": {
                        "focus_areas": [
                            "Leadership",
                            "Data Science",
                            "Career Growth",
                            "Team Leadership"
                        ]
                    }
                }
            }
        ],
        "outputs": [
                "User U301 enrolled in course C1005",
                "User U301 enrolled in course C1004",
                "Goal G301-1 updated for user U301",
                "relationship MR001 updated"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_95",
        "instruction": "Facilitate the progression of application APP002 (Alexander Adams, U310) for the Senior Data Scientist role (J001) by conducting an advancement assessment, creating a skill development plan, and ensuring she is ready for the interview phase.",
        "actions": [
            {
                "name": "GetJobPosting",
                "arguments": {
                    "job_id": "J001"
                },
            },
            {
                "name": "GetRoleSkills",
                "arguments": {
                    "role": "Senior Data Scientist"
                },
            },
            {
                "name": "GetJobApplications",
                "arguments": {
                    "job_id": "J001"
                },
            },
            {
                "name": "AnalyzeApplicantSkillFit",
                "arguments": {
                    "applicant_id": "U310",
                    "role": "Senior Data Scientist"
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "U310",
                    "skill": "Machine Learning"
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "U310",
                    "skill": "Programming Languages"
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "U310",
                    "skill": "Data Visualization"
                },
            },
            {
                "name": "UpdateApplicationStatus",
                "arguments": {
                    "application_id": "APP002",
                    "new_status": "Advancement-Assessment"
                },
            },
            {
                "name": "ScheduleTechnicalInterview",
                "arguments": {
                    "application_id": "APP002"
                }
            }
        ],
        "outputs": [
                "U310 needs Machine Learning training",
                "U310 needs Programming Languages training",
                "U310 needs Data Visualization training",
                "APP002 Advancement-Assessment",
                "Interview scheduled for APP002"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_96",
        "instruction": "The hiring manager, Michael Rodriguez, is evaluating Alexander Adams's application for the 'UX Design Lead' position. He intends to move forward but wishes to first address her knowledge gap in Design Operations. Please register Chloe for the 'Project Management Professional' course. Subsequently, modify her application status to 'Interview with Dev Plan'. Then, arrange her technical interview. Lastly, add a new goal to her profile with ID 'G307-4', type 'Skill Mastery', and description 'Complete PMP to build Design Operations skills for UX Lead role.'",
        "actions": [
            {
                "name": "GetUserIdFromName",
                "arguments": {
                    "first_name": "David",
                    "last_name": "Adams"
                },
            },
            {
                "name": "GetUserIdFromName",
                "arguments": {
                    "first_name": "Chloe",
                    "last_name": "Scott"
                },
            },
            {
                "name": "GetJobIdByTitle",
                "arguments": {
                    "job_title": "UX Design Lead"
                },
            },
            {
                "name": "GetJobApplications",
                "arguments": {
                    "job_id": "J002"
                },
            },
            {
                "name": "AnalyzeApplicantSkillFit",
                "arguments": {
                    "applicant_id": "U307",
                    "role": "UX Design Lead"
                },
            },
            {
                "name": "GetCourseIdByName",
                "arguments": {
                    "course_name": "Project Management Professional"
                },
            },
            {
                "name": "GetTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "EnrollInCourse",
                "arguments": {
                    "user_id": "U307",
                    "course_id": "C1004",
                    "enroll_date": "2025-10-02"
                },
            },
            {
                "name": "UpdateApplicationStatus",
                "arguments": {
                    "application_id": "APP005",
                    "new_status": "Interview with Dev Plan"
                },
            },
            {
                "name": "ScheduleTechnicalInterview",
                "arguments": {
                    "application_id": "APP005"
                },
            },
            {
                "name": "AddGoal",
                "arguments": {
                    "user_id": "U307",
                    "goal": {
                        "goal_id": "G307-4",
                        "goal_type": "Skill Mastery",
                        "description": "Complete PMP to build Design Operations skills for UX Lead role."
                    }
                }
            }
        ],
        "outputs": [
                "User U307 enrolled in course C1004",
                "APP005 Interview with Dev Plan",
                "Technical interview scheduled for application APP005.",
                "goal G307-4 added for U307"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_97",
        "instruction": "Handle the thorough review of the UX Designer pipeline (J002) alongside scheduling technical interviews for applicants APP005 (Alexander Adams, U307) and APP006 (Emily Johnson, EXT003).",
        "actions": [
            {
                "name": "GetJobPosting",
                "arguments": {
                    "job_id": "J002"
                },
            },
            {
                "name": "GetRoleSkills",
                "arguments": {
                    "role": "UX Designer"
                },
            },
            {
                "name": "GetJobApplications",
                "arguments": {
                    "job_id": "J002"
                },
            },
            {
                "name": "AnalyzeApplicantSkillFit",
                "arguments": {
                    "applicant_id": "U307",
                    "role": "UX Designer"
                },
            },
            {
                "name": "AnalyzeExternalCandidateSkillFit",
                "arguments": {
                    "candidate_id": "EXT003",
                    "role": "UX Designer"
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "U307",
                    "skill": "Design Operations"
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "EXT003",
                    "skill": "Design Thinking"
                },
            },
            {
                "name": "UpdateApplicationStatus",
                "arguments": {
                    "application_id": "APP005",
                    "new_status": "Screen-Scheduled"
                },
            },
            {
                "name": "ScheduleTechnicalInterview",
                "arguments": {
                    "application_id": "APP005"
                },
            },
            {
                "name": "UpdateApplicationStatus",
                "arguments": {
                    "application_id": "APP006",
                    "new_status": "Screen-Scheduled"
                },
            },
            {
                "name": "ScheduleTechnicalInterview",
                "arguments": {
                    "application_id": "APP006"
                }
            }
        ],
        "outputs": [
                "U307 needs Design Operations training",
                "EXT003 needs Design Thinking training",
                "APP005 Screen-Scheduled",
                "Interview scheduled for APP005",
                "APP006 Screen-Scheduled",
                "Interview scheduled for APP006"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_98",
        "instruction": "Michael Rodriguez has appointed Robert Thompson as the technical lead for an upcoming project that demands advanced Python skills. Firstly, register Alexander in the 'Advanced Python' course. Secondly, identify a mentor with proficiency in 'Engineering' and 'Career Growth' to build an 'Active' mentorship relationship. Thirdly, amend Alexander's main career objective by including the note: 'Leading technical implementation for new Python project.' Finally, arrange their initial mentorship session for November 21, 2025.",
        "actions": [
            {
                "name": "GetUserIdFromName",
                "arguments": {
                    "first_name": "Mason",
                    "last_name": "Desai"
                },
            },
            {
                "name": "GetUserIdFromName",
                "arguments": {
                    "first_name": "Alexander",
                    "last_name": "Adams"
                },
            },
            {
                "name": "GetCourseIdByName",
                "arguments": {
                    "course_name": "Advanced Python"
                },
            },
            {
                "name": "GetTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "EnrollInCourse",
                "arguments": {
                    "user_id": "U306",
                    "course_id": "C1001",
                    "enroll_date": "2025-10-02"
                },
            },
            {
                "name": "FindMentors",
                "arguments": {
                    "mentee_id": "U306",
                    "focus_areas": [
                        "Engineering",
                        "Career Growth"
                    ]
                },
            },
            {
                "name": "AddMentorshipRelationship",
                "arguments": {
                    "mentor_id": "M101",
                    "mentee_id": "U306",
                    "start_date": "2025-10-02",
                    "status": "Active",
                    "focus_areas": [
                        "Engineering",
                        "Career Growth"
                    ]
                },
            },
            {
                "name": "ListUserGoals",
                "arguments": {
                    "user_id": "U306"
                },
            },
            {
                "name": "UpdateGoal",
                "arguments": {
                    "user_id": "U306",
                    "goal_id": "G306-1",
                    "notes_to_append": "Leading technical implementation for new Python project.",
                    "last_updated_date": "2025-10-02"
                },
            },
            {
                "name": "ScheduleMentorshipSession",
                "arguments": {
                    "relationship_id": "MR011",
                    "session_date": "2025-11-21"
                }
            }
        ],
        "outputs": [
                "User U306 enrolled in course C1001",
                "Mentorship relationship MR011 created",
                "Goal G306-1 updated for user U306",
                "scheduled_for: 2025-11-21"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_99",
        "instruction": "To aid Alexander Adams in establishing a People-Analytics function, kindly develop a structured training plan. Begin by checking if she is not already registered, then proceed to enroll her in the courses: 'Machine Learning Specialization' and 'Advanced Python'. Once she is enrolled, modify her main career objective to reflect 25% progress, mark its status as 'In Progress', and add the note: 'Enrolled in foundational ML and Python courses.'",
        "actions": [
            {
                "name": "GetUserIdFromName",
                "arguments": {
                    "first_name": "Harper",
                    "last_name": "Bennett"
                },
            },
            {
                "name": "ListUserGoals",
                "arguments": {
                    "user_id": "U310"
                },
            },
            {
                "name": "GetCourseIdByName",
                "arguments": {
                    "course_name": "Machine Learning Specialization"
                },
            },
            {
                "name": "GetCourseIdByName",
                "arguments": {
                    "course_name": "Advanced Python"
                },
            },
            {
                "name": "ListUserCourses",
                "arguments": {
                    "user_id": "U310"
                },
            },
            {
                "name": "GetTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "EnrollInCourse",
                "arguments": {
                    "user_id": "U310",
                    "course_id": "C1005",
                    "enroll_date": "2025-10-02"
                },
            },
            {
                "name": "EnrollInCourse",
                "arguments": {
                    "user_id": "U310",
                    "course_id": "C1001",
                    "enroll_date": "2025-10-02"
                },
            },
            {
                "name": "UpdateGoal",
                "arguments": {
                    "user_id": "U310",
                    "goal_id": "G310-1",
                    "progress_percent": 25,
                    "status": "In Progress",
                    "notes_to_append": "Enrolled in foundational ML and Python courses.",
                    "last_updated_date": "2025-10-02"
                }
            }
        ],
        "outputs": [
                "User U310 enrolled in course C1005",
                "User U310 enrolled in course C1001",
                "Goal G310-1 updated for user U310"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_110",
        "instruction": "Coordinate a complete advancement process for the DevOps Engineer role (J003) for applications APP007 (candidate U306) and APP008 by conducting detailed skill assessments, expanding the external candidate pipeline through EXT004 evaluation and selection, implementing multi-level training to address all recognized skill deficiencies, optimizing the pipeline, and organizing technical screenings along with interview arrangements.",
        "actions": [
            {
                "name": "GetJobApplications",
                "arguments": {
                    "job_id": "J003"
                },
            },
            {
                "name": "GetJobPosting",
                "arguments": {
                    "job_id": "J003"
                },
            },
            {
                "name": "GetRoleSkills",
                "arguments": {
                    "role": "DevOps Engineer"
                },
            },
            {
                "name": "AnalyzeApplicantSkillFit",
                "arguments": {
                    "applicant_id": "U306",
                    "role": "DevOps Engineer"
                },
            },
            {
                "name": "SearchExternalCandidatesBySkills",
                "arguments": {
                    "required_skills": [
                        "CI/CD",
                        "Containerization",
                        "Cloud Platforms",
                        "Infrastructure as Code",
                        "Monitoring & Logging"
                    ]
                },
            },
            {
                "name": "AnalyzeExternalCandidateSkillFit",
                "arguments": {
                    "candidate_id": "EXT004",
                    "role": "DevOps Engineer"
                },
            },
            {
                "name": "ShortlistExternalCandidate",
                "arguments": {
                    "candidate_id": "EXT004",
                    "job_id": "J003"
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "EXT004",
                    "skill": "CI/CD"
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "EXT004",
                    "skill": "Monitoring & Logging"
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "U306",
                    "skill": "Infrastructure as Code"
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "U306",
                    "skill": "Monitoring & Logging"
                },
            },
            {
                "name": "UpdateApplicationStatus",
                "arguments": {
                    "application_id": "APP007",
                    "new_status": "Training-Enhanced"
                },
            },
            {
                "name": "UpdateApplicationStatus",
                "arguments": {
                    "application_id": "APP007",
                    "new_status": "Tech-Screen"
                },
            },
            {
                "name": "UpdateApplicationStatus",
                "arguments": {
                    "application_id": "APP008",
                    "new_status": "Pipeline-Optimized"
                },
            },
            {
                "name": "UpdateApplicationStatus",
                "arguments": {
                    "application_id": "APP008",
                    "new_status": "Tech-Screen"
                },
            },
            {
                "name": "ScheduleTechnicalInterview",
                "arguments": {
                    "application_id": "APP007"
                },
            },
            {
                "name": "ScheduleTechnicalInterview",
                "arguments": {
                    "application_id": "APP008"
                }
            }
        ],
        "outputs": [
                "EXT004 shortlisted",
                "EXT004 needs CI/CD training",
                "EXT004 needs Monitoring & Logging training",
                "U306 needs Infrastructure as Code training",
                "U306 needs Monitoring & Logging training",
                "APP007 Training-Enhanced",
                "APP007 Tech-Screen",
                "APP008 Pipeline-Optimized",
                "APP008 Tech-Screen",
                "Interview scheduled for APP007",
                "Interview scheduled for APP008"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_101",
        "instruction": "Handle the expansion of the UX Designer position (J002) candidate pipeline by thoroughly evaluating candidates, carrying out skill assessments for EXT003 and U307, implementing focused training to address detected skill gaps, moving candidates forward with EXT003 shortlisting, and organizing interview schedules.",
        "actions": [
            {
                "name": "GetRoleSkills",
                "arguments": {
                    "role": "UX Designer"
                },
            },
            {
                "name": "GetJobPosting",
                "arguments": {
                    "job_id": "J002"
                },
            },
            {
                "name": "GetJobApplications",
                "arguments": {
                    "job_id": "J002"
                },
            },
            {
                "name": "AnalyzeExternalCandidateSkillFit",
                "arguments": {
                    "candidate_id": "EXT003",
                    "role": "UX Designer"
                },
            },
            {
                "name": "AnalyzeApplicantSkillFit",
                "arguments": {
                    "applicant_id": "U307",
                    "role": "UX Designer"
                },
            },
            {
                "name": "ShortlistExternalCandidate",
                "arguments": {
                    "candidate_id": "EXT003",
                    "job_id": "J002"
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "EXT003",
                    "skill": "Leadership"
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "U307",
                    "skill": "Leadership"
                },
            },
            {
                "name": "UpdateApplicationStatus",
                "arguments": {
                    "application_id": "APP005",
                    "new_status": "Pipeline-Expanded"
                },
            },
            {
                "name": "ScheduleTechnicalInterview",
                "arguments": {
                    "application_id": "APP005"
                }
            }
        ],
        "outputs": [
                "EXT003 shortlisted",
                "EXT003 needs Leadership training",
                "U307 needs Leadership training",
                "APP005 Pipeline-Expanded",
                "Interview scheduled for APP005"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_102",
        "instruction": "Manager Ava Nguyen is assessing the progress of his report, Harper Bennett. He observes that she has advanced on her Python goal. He intends to update her 'Python for clinical-analytics' goal to reflect 40% progress and include the note: 'Basic Python syntax mastered. Next step: data visualization.' He also plans to reactivate their mentorship to concentrate on 'Tableau' and 'Data-Viz Best Practices'. To facilitate this, enroll Ava in the 'Data Visualization with Tableau' course. Conclude by arranging their next mentorship session for October 31, 2025.",
        "actions": [
            {
                "name": "GetUserIdFromName",
                "arguments": {
                    "first_name": "Jack",
                    "last_name": "Wang"
                },
            },
            {
                "name": "GetUserIdFromName",
                "arguments": {
                    "first_name": "Ava",
                    "last_name": "Nguyen"
                },
            },
            {
                "name": "ListUserGoals",
                "arguments": {
                    "user_id": "U302"
                },
            },
            {
                "name": "ListUserMentorships",
                "arguments": {
                    "user_id": "U302"
                },
            },
            {
                "name": "GetCourseIdByName",
                "arguments": {
                    "course_name": "Data Visualization with Tableau"
                },
            },
            {
                "name": "GetTodayDate",
                "arguments": {
                {}
                },
            },
            {
                "name": "UpdateGoal",
                "arguments": {
                    "user_id": "U302",
                    "goal_id": "G302-1",
                    "progress_percent": 40,
                    "notes_to_append": "Basic Python syntax mastered. Next step: data visualization.",
                    "last_updated_date": "2025-10-02"
                },
            },
            {
                "name": "UpdateMentorshipRelationship",
                "arguments": {
                    "relationship_id": "MR008",
                    "updates": {
                        "status": "Active",
                        "focus_areas": [
                            "Tableau",
                            "Data-Viz Best Practices"
                        ]
                    }
                },
            },
            {
                "name": "EnrollInCourse",
                "arguments": {
                    "user_id": "U302",
                    "course_id": "C1003",
                    "enroll_date": "2025-10-02"
                },
            },
            {
                "name": "ScheduleMentorshipSession",
                "arguments": {
                    "relationship_id": "MR008",
                    "session_date": "2025-10-31"
                }
            }
        ],
        "outputs": [
                "Goal G302-1 updated for user U302",
                "relationship MR008 updated",
                "User U302 enrolled in course C1003",
                "scheduled_for: 2025-10-31"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_103",
        "instruction": "Manage the progression of application APP001 (Harper Bennett, U302) for the Senior Data Scientist role (J001) including a Machine Learning skill enhancement plan, candidate shortlisting for EXT001, and Data Visualization training, along with arranging interviews for both APP001 and APP003.",
        "actions": [
            {
                "name": "GetJobPosting",
                "arguments": {
                    "job_id": "J001"
                },
            },
            {
                "name": "GetRoleSkills",
                "arguments": {
                    "role": "Senior Data Scientist"
                },
            },
            {
                "name": "GetJobApplications",
                "arguments": {
                    "job_id": "J001"
                },
            },
            {
                "name": "AnalyzeApplicantSkillFit",
                "arguments": {
                    "applicant_id": "U302",
                    "role": "Senior Data Scientist"
                },
            },
            {
                "name": "SearchExternalCandidatesBySkills",
                "arguments": {
                    "required_skills": [
                        "Machine Learning",
                        "Programming Languages",
                        "Data Visualization"
                    ]
                },
            },
            {
                "name": "AnalyzeExternalCandidateSkillFit",
                "arguments": {
                    "candidate_id": "EXT001",
                    "role": "Senior Data Scientist"
                },
            },
            {
                "name": "ShortlistExternalCandidate",
                "arguments": {
                    "candidate_id": "EXT001",
                    "job_id": "J001"
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "U302",
                    "skill": "Machine Learning"
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "EXT001",
                    "skill": "Data Visualization"
                },
            },
            {
                "name": "UpdateApplicationStatus",
                "arguments": {
                    "application_id": "APP001",
                    "new_status": "Skill-Plan-Active"
                },
            },
            {
                "name": "ScheduleTechnicalInterview",
                "arguments": {
                    "application_id": "APP001"
                },
            },
            {
                "name": "ScheduleTechnicalInterview",
                "arguments": {
                    "application_id": "APP003"
                }
            }
        ],
        "outputs": [
                "EXT001 shortlisted",
                "U302 needs Machine Learning training",
                "EXT001 needs Data Visualization training",
                "APP001 Skill-Plan-Active",
                "Interview scheduled for APP001",
                "Interview scheduled for APP003"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_104",
        "instruction": "Review and promote application APP010 (external candidate EXT006) for the Security Analyst role (J005) to primary candidate status by providing skill development recommendations, executing candidate shortlisting, and organizing a technical interview.",
        "actions": [
            {
                "name": "GetJobApplications",
                "arguments": {
                    "job_id": "J005"
                },
            },
            {
                "name": "GetJobPosting",
                "arguments": {
                    "job_id": "J005"
                },
            },
            {
                "name": "GetRoleSkills",
                "arguments": {
                    "role": "Security Analyst"
                },
            },
            {
                "name": "AnalyzeExternalCandidateSkillFit",
                "arguments": {
                    "candidate_id": "EXT006",
                    "role": "Security Analyst"
                },
            },
            {
                "name": "SearchExternalCandidatesBySkills",
                "arguments": {
                    "required_skills": [
                        "Cloud Security",
                        "Compliance"
                    ]
                },
            },
            {
                "name": "ShortlistExternalCandidate",
                "arguments": {
                    "candidate_id": "EXT006",
                    "job_id": "J005"
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "EXT006",
                    "skill": "Cloud Security"
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "EXT006",
                    "skill": "Compliance"
                },
            },
            {
                "name": "UpdateApplicationStatus",
                "arguments": {
                    "application_id": "APP010",
                    "new_status": "Primary-Candidate"
                },
            },
            {
                "name": "ScheduleTechnicalInterview",
                "arguments": {
                    "application_id": "APP010"
                }
            }
        ],
        "outputs": [
                "EXT006 shortlisted",
                "EXT006 needs Cloud Security training",
                "EXT006 needs Compliance training",
                "APP010 Primary-Candidate",
                "Interview scheduled for APP010"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_105",
        "instruction": "Handle the progression of UX Designer position (J002) candidates by optimizing the external candidate pipeline, oversee skill assessments for EXT003, execute Design Thinking and Accessibility training programs, move from Portfolio-Review to Technical-Assessment status, and arrange technical interviews.",
        "actions": [
            {
                "name": "GetJobPosting",
                "arguments": {
                    "job_id": "J002"
                },
            },
            {
                "name": "GetRoleSkills",
                "arguments": {
                    "role": "UX Designer"
                },
            },
            {
                "name": "GetJobApplications",
                "arguments": {
                    "job_id": "J002"
                },
            },
            {
                "name": "AnalyzeExternalCandidateSkillFit",
                "arguments": {
                    "candidate_id": "EXT003",
                    "role": "UX Designer"
                },
            },
            {
                "name": "ShortlistExternalCandidate",
                "arguments": {
                    "candidate_id": "EXT003",
                    "job_id": "J002"
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "EXT003",
                    "skill": "Design Thinking"
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "EXT003",
                    "skill": "Accessibility"
                },
            },
            {
                "name": "UpdateApplicationStatus",
                "arguments": {
                    "application_id": "APP006",
                    "new_status": "Portfolio-Review"
                },
            },
            {
                "name": "UpdateApplicationStatus",
                "arguments": {
                    "application_id": "APP006",
                    "new_status": "Technical-Assessment"
                },
            },
            {
                "name": "ScheduleTechnicalInterview",
                "arguments": {
                    "application_id": "APP006"
                }
            }
        ],
        "outputs": [
                "EXT003 shortlisted",
                "EXT003 needs Design Thinking training",
                "EXT003 needs Accessibility training",
                "APP006 Portfolio-Review",
                "APP006 Technical-Assessment",
                "Interview scheduled for APP006"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_106",
        "instruction": "Manage the process for application APP007 (candidate U306) for the DevOps Engineer position (J003) to reach offer finalization, including arranging technical interviews, enhancing skills in Monitoring & Logging, and identifying as well as shortlisting backup candidate EXT004.",
        "actions": [
            {
                "name": "GetJobPosting",
                "arguments": {
                    "job_id": "J003"
                },
            },
            {
                "name": "GetRoleSkills",
                "arguments": {
                    "role": "DevOps Engineer"
                },
            },
            {
                "name": "GetJobApplications",
                "arguments": {
                    "job_id": "J003"
                },
            },
            {
                "name": "AnalyzeApplicantSkillFit",
                "arguments": {
                    "applicant_id": "U306",
                    "role": "DevOps Engineer"
                },
            },
            {
                "name": "AnalyzeExternalCandidateSkillFit",
                "arguments": {
                    "candidate_id": "EXT004",
                    "role": "DevOps Engineer"
                },
            },
            {
                "name": "UpdateApplicationStatus",
                "arguments": {
                    "application_id": "APP007",
                    "new_status": "Offer-Finalization"
                },
            },
            {
                "name": "ScheduleTechnicalInterview",
                "arguments": {
                    "application_id": "APP007"
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "U306",
                    "skill": "Monitoring & Logging"
                },
            },
            {
                "name": "ShortlistExternalCandidate",
                "arguments": {
                    "candidate_id": "EXT004",
                    "job_id": "J003"
                }
            }
        ],
        "outputs": [
                "APP007 Offer-Finalization",
                "Interview scheduled for APP007",
                "U306 needs Monitoring & Logging training",
                "EXT004 shortlisted"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_107",
        "instruction": "Handle the Marketing Specialist position (J004) by verifying applications, carrying out skill assessment for candidate EXT005, expanding the candidate pool through searching for Product Marketing skills and shortlisting EXT005, organizing targeted training programs in Product Marketing and Brand Strategy, and updating application records to show progress in skill development.",
        "actions": [
            {
                "name": "GetJobApplications",
                "arguments": {
                    "job_id": "J004"
                },
            },
            {
                "name": "GetRoleSkills",
                "arguments": {
                    "role": "Marketing Specialist"
                },
            },
            {
                "name": "GetJobPosting",
                "arguments": {
                    "job_id": "J004"
                },
            },
            {
                "name": "AnalyzeExternalCandidateSkillFit",
                "arguments": {
                    "candidate_id": "EXT005",
                    "role": "Marketing Specialist"
                },
            },
            {
                "name": "SearchExternalCandidatesBySkills",
                "arguments": {
                    "required_skills": [
                        "Product Marketing"
                    ]
                },
            },
            {
                "name": "ShortlistExternalCandidate",
                "arguments": {
                    "candidate_id": "EXT005",
                    "job_id": "J004"
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "EXT005",
                    "skill": "Product Marketing"
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "EXT005",
                    "skill": "Brand Strategy"
                },
            },
            {
                "name": "UpdateApplicationStatus",
                "arguments": {
                    "application_id": "APP009",
                    "new_status": "Skills-Enhanced"
                },
            },
            {
                "name": "UpdateApplicationStatus",
                "arguments": {
                    "application_id": "APP009",
                    "new_status": "Pipeline-Expanded"
                },
            },
            {
                "name": "ScheduleTechnicalInterview",
                "arguments": {
                    "application_id": "APP009"
                }
            }
        ],
        "outputs": [
                "EXT005 shortlisted",
                "EXT005 needs Product Marketing training",
                "EXT005 needs Brand Strategy training",
                "APP009 Skills-Enhanced",
                "APP009 Pipeline-Expanded",
                "Interview scheduled for APP009"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_108",
        "instruction": "Coordinate the progression of application APP005 (Alexander Adams, U307) for the UX Designer position (J002) by conducting a thorough skill assessment, implementing leadership development training, and advancing to the portfolio review stage with scheduling of a technical interview.",
        "actions": [
            {
                "name": "GetJobPosting",
                "arguments": {
                    "job_id": "J002"
                },
            },
            {
                "name": "GetRoleSkills",
                "arguments": {
                    "role": "UX Designer"
                },
            },
            {
                "name": "GetJobApplications",
                "arguments": {
                    "job_id": "J002"
                },
            },
            {
                "name": "AnalyzeApplicantSkillFit",
                "arguments": {
                    "applicant_id": "U307",
                    "role": "UX Designer"
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "U307",
                    "skill": "Leadership"
                },
            },
            {
                "name": "UpdateApplicationStatus",
                "arguments": {
                    "application_id": "APP005",
                    "new_status": "Leadership-Enhanced"
                },
            },
            {
                "name": "UpdateApplicationStatus",
                "arguments": {
                    "application_id": "APP005",
                    "new_status": "Portfolio-Review"
                },
            },
            {
                "name": "ScheduleTechnicalInterview",
                "arguments": {
                    "application_id": "APP005"
                }
            }
        ],
        "outputs": [
                "U307 needs Leadership training",
                "APP005 Leadership-Enhanced",
                "APP005 Portfolio-Review",
                "Interview scheduled for APP005"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_109",
        "instruction": "Enhance the candidate pool for the Senior Data Scientist position (J001) by pinpointing experts in Machine Learning and SQL, creating a shortlist that includes candidates EXT001 and EXT002, and setting up specialized Machine Learning and SQL training sessions for EXT002.",
        "actions": [
            {
                "name": "GetRoleSkills",
                "arguments": {
                    "role": "Senior Data Scientist"
                },
            },
            {
                "name": "GetJobPosting",
                "arguments": {
                    "job_id": "J001"
                },
            },
            {
                "name": "GetJobApplications",
                "arguments": {
                    "job_id": "J001"
                },
            },
            {
                "name": "SearchExternalCandidatesBySkills",
                "arguments": {
                    "required_skills": [
                        "Machine Learning",
                        "SQL"
                    ]
                },
            },
            {
                "name": "ShortlistExternalCandidate",
                "arguments": {
                    "candidate_id": "EXT001",
                    "job_id": "J001"
                },
            },
            {
                "name": "ShortlistExternalCandidate",
                "arguments": {
                    "candidate_id": "EXT002",
                    "job_id": "J001"
                },
            },
            {
                "name": "AnalyzeExternalCandidateSkillFit",
                "arguments": {
                    "candidate_id": "EXT002",
                    "role": "Senior Data Scientist"
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "EXT002",
                    "skill": "Machine Learning"
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "EXT002",
                    "skill": "SQL"
                }
            }
        ],
        "outputs": [
                "EXT001 shortlisted",
                "EXT002 shortlisted",
                "EXT002 needs Machine Learning training",
                "EXT002 needs SQL training"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_111",
        "instruction": "Handle the DevOps Engineer position (J003) by confirming applications, performing skill evaluations for internal candidate U306 and external candidate EXT004, executing Infrastructure as Code training for U306 and extensive CI/CD and Monitoring & Logging training for EXT004, selecting EXT004 for the shortlist, changing APP007 to Training-Complete status, and arranging a technical interview.",
        "actions": [
            {
                "name": "GetJobApplications",
                "arguments": {
                    "job_id": "J003"
                },
            },
            {
                "name": "GetJobPosting",
                "arguments": {
                    "job_id": "J003"
                },
            },
            {
                "name": "GetRoleSkills",
                "arguments": {
                    "role": "DevOps Engineer"
                },
            },
            {
                "name": "AnalyzeApplicantSkillFit",
                "arguments": {
                    "applicant_id": "U306",
                    "role": "DevOps Engineer"
                },
            },
            {
                "name": "AnalyzeExternalCandidateSkillFit",
                "arguments": {
                    "candidate_id": "EXT004",
                    "role": "DevOps Engineer"
                },
            },
            {
                "name": "ShortlistExternalCandidate",
                "arguments": {
                    "candidate_id": "EXT004",
                    "job_id": "J003"
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "U306",
                    "skill": "Infrastructure as Code"
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "EXT004",
                    "skill": "CI/CD"
                },
            },
            {
                "name": "RecommendSkillTraining",
                "arguments": {
                    "user_id": "EXT004",
                    "skill": "Monitoring & Logging"
                },
            },
            {
                "name": "UpdateApplicationStatus",
                "arguments": {
                    "application_id": "APP007",
                    "new_status": "Training-Complete"
                },
            },
            {
                "name": "ScheduleTechnicalInterview",
                "arguments": {
                    "application_id": "APP007"
                }
            }
        ],
        "outputs": [
                "EXT004 shortlisted",
                "U306 needs Infrastructure as Code training",
                "EXT004 needs CI/CD training",
                "EXT004 needs Monitoring & Logging training",
                "APP007 Training-Complete",
                "Interview scheduled for APP007"
        ]
    }
]
