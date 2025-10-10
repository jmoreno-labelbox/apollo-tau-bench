from domains.dto import Task, Action

# ───────────────────────────── TASK DEFINITIONS ──────────────────────────────
TASKS = [
    # 1 REPLACED
    Task(
        annotator="0",
        user_id="res_70",
        instruction="For the 'UX Design Lead' position, process the applications submitted by Chloe Scott and Emily Johnson. First, conduct skill assessments for both candidates against the role. Then, recommend 'Design Operations' training for Chloe and 'Accessibility' training for Emily. Finally, update Chloe's application status to 'Interview Scheduled' and schedule her interview, while updating Emily's status to 'Waitlist'.",
        actions=[
            Action(name="get_job_id_by_title", kwargs={"job_title": "UX Design Lead"}),
            Action(name="get_job_applications", kwargs={"job_id": "J002"}),
            Action(
                name="analyze_applicant_skill_fit",
                kwargs={"applicant_id": "U307", "role": "UX Design Lead"},
            ),
            Action(
                name="analyze_external_candidate_skill_fit",
                kwargs={"candidate_id": "EXT003", "role": "UX Design Lead"},
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "U307", "skill": "Design Operations"},
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "EXT003", "skill": "Accessibility"},
            ),
            Action(
                name="update_application_status",
                kwargs={
                    "application_id": "APP005",
                    "new_status": "Interview Scheduled",
                },
            ),
            Action(
                name="update_application_status",
                kwargs={"application_id": "APP006", "new_status": "Waitlist"},
            ),
            Action(
                name="schedule_technical_interview",
                kwargs={"application_id": "APP005"},
            ),
        ],
        outputs=[
            "U307 needs Design Operations training",
            "EXT003 needs Accessibility training",
            "APP005 Interview Scheduled",
            "APP006 Waitlist",
            "Technical interview scheduled for application APP005",
        ],
    ),
    # 2
    Task(
        annotator="0",
        user_id="res_71",
        instruction="Verify and process application APP007 (DevOps Engineer candidate U306) for position J003 by conducting skill assessment, providing Infrastructure as Code training for U306, analyzing external candidate EXT004 as backup pipeline option with Monitoring & Logging training, updating APP007 to Training-Plan status, and scheduling technical interview.",
        actions=[
            Action(name="get_job_applications", kwargs={"job_id": "J003"}),
            Action(name="get_job_posting", kwargs={"job_id": "J003"}),
            Action(name="get_role_skills", kwargs={"role": "DevOps Engineer"}),
            Action(
                name="analyze_applicant_skill_fit",
                kwargs={"applicant_id": "U306", "role": "DevOps Engineer"},
            ),
            Action(
                name="search_external_candidates_by_skills",
                kwargs={
                    "required_skills": [
                        "CI/CD",
                        "Containerization",
                        "Cloud Platforms",
                        "Infrastructure as Code",
                        "Monitoring & Logging",
                    ]
                },
            ),
            Action(
                name="analyze_external_candidate_skill_fit",
                kwargs={"candidate_id": "EXT004", "role": "DevOps Engineer"},
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "U306", "skill": "Infrastructure as Code"},
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "EXT004", "skill": "Monitoring & Logging"},
            ),
            Action(
                name="update_application_status",
                kwargs={"application_id": "APP007", "new_status": "Training-Plan"},
            ),
            Action(
                name="schedule_technical_interview", kwargs={"application_id": "APP007"}
            ),
        ],
        outputs=[
            "U306 needs Infrastructure as Code training",
            "EXT004 needs Monitoring & Logging training",
            "APP007 Training-Plan",
            "Interview scheduled for APP007",
        ],
    ),
    # 3
    Task(
        annotator="0",
        user_id="res_72",
        instruction="Applications APP001 (Ava Nguyen, U302) and APP002 (Harper Bennett, U310) compete for Senior Data Scientist position (J001). Assess skills and advance the stronger candidate to final interview.",
        actions=[
            Action(name="get_job_posting", kwargs={"job_id": "J001"}),
            Action(name="get_role_skills", kwargs={"role": "Senior Data Scientist"}),
            Action(name="get_job_applications", kwargs={"job_id": "J001"}),
            Action(
                name="analyze_applicant_skill_fit",
                kwargs={"applicant_id": "U302", "role": "Senior Data Scientist"},
            ),
            Action(
                name="analyze_applicant_skill_fit",
                kwargs={"applicant_id": "U310", "role": "Senior Data Scientist"},
            ),
            Action(
                name="search_external_candidates_by_skills",
                kwargs={
                    "required_skills": [
                        "Machine Learning",
                        "Programming Languages",
                        "Data Visualization",
                        "Statistical Analysis",
                    ]
                },
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "U302", "skill": "Machine Learning"},
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "U310", "skill": "Machine Learning"},
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "U310", "skill": "Programming Languages"},
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "U310", "skill": "Data Visualization"},
            ),
            Action(
                name="update_application_status",
                kwargs={"application_id": "APP001", "new_status": "Final-Interview"},
            ),
            Action(
                name="update_application_status",
                kwargs={"application_id": "APP002", "new_status": "Rejected-Skill-Fit"},
            ),
            Action(
                name="schedule_technical_interview", kwargs={"application_id": "APP001"}
            ),
        ],
        outputs=[
            "U302 needs Machine Learning training",
            "U310 needs Machine Learning training",
            "U310 needs Programming Languages training",
            "U310 needs Data Visualization training",
            "APP001 Final-Interview",
            "APP002 Rejected-Skill-Fit",
            "Interview scheduled for APP001",
        ],
    ),
    # 4
    Task(
        annotator="0",
        user_id="res_73",
        instruction="Process application APP010 (external candidate EXT006) for Security Analyst position (J005) by conducting skill assessment, shortlisting EXT006 as qualified candidate, implementing specific Cloud Security and Compliance training recommendations, expanding candidate pipeline through targeted skill search, and updating APP010 to Interview-Pending status.",
        actions=[
            Action(name="get_job_applications", kwargs={"job_id": "J005"}),
            Action(name="get_job_posting", kwargs={"job_id": "J005"}),
            Action(name="get_role_skills", kwargs={"role": "Security Analyst"}),
            Action(
                name="analyze_external_candidate_skill_fit",
                kwargs={"candidate_id": "EXT006", "role": "Security Analyst"},
            ),
            Action(
                name="shortlist_external_candidate",
                kwargs={"candidate_id": "EXT006", "job_id": "J005"},
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "EXT006", "skill": "Cloud Security"},
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "EXT006", "skill": "Compliance"},
            ),
            Action(
                name="search_external_candidates_by_skills",
                kwargs={"required_skills": ["Cloud Security", "Compliance"]},
            ),
            Action(
                name="update_application_status",
                kwargs={"application_id": "APP010", "new_status": "Interview-Pending"},
            ),
            Action(
                name="schedule_technical_interview", kwargs={"application_id": "APP010"}
            ),
        ],
        outputs=[
            "EXT006 shortlisted",
            "EXT006 needs Cloud Security training",
            "EXT006 needs Compliance training",
            "APP010 Interview-Pending",
            "Interview scheduled for APP010",
        ],
    ),
    # 5
    Task(
        annotator="0",
        user_id="res_74",
        instruction="Senior Data Scientist position (J001) requires candidate pipeline expansion. Identify and shortlist external candidates with Machine Learning, Programming Languages, and Data Visualization expertise, then establish targeted training programs for skill gaps.",
        actions=[
            Action(name="get_job_posting", kwargs={"job_id": "J001"}),
            Action(name="get_job_applications", kwargs={"job_id": "J001"}),
            Action(name="get_role_skills", kwargs={"role": "Senior Data Scientist"}),
            Action(
                name="search_external_candidates_by_skills",
                kwargs={
                    "required_skills": [
                        "Machine Learning",
                        "Programming Languages",
                        "Data Visualization",
                    ]
                },
            ),
            Action(
                name="analyze_external_candidate_skill_fit",
                kwargs={"candidate_id": "EXT001", "role": "Senior Data Scientist"},
            ),
            Action(
                name="analyze_external_candidate_skill_fit",
                kwargs={"candidate_id": "EXT002", "role": "Senior Data Scientist"},
            ),
            Action(
                name="shortlist_external_candidate",
                kwargs={"candidate_id": "EXT001", "job_id": "J001"},
            ),
            Action(
                name="shortlist_external_candidate",
                kwargs={"candidate_id": "EXT002", "job_id": "J001"},
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "EXT001", "skill": "Data Visualization"},
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "EXT002", "skill": "Data Visualization"},
            ),
            Action(
                name="schedule_technical_interview", kwargs={"application_id": "APP003"}
            ),
            Action(
                name="schedule_technical_interview", kwargs={"application_id": "APP004"}
            ),
        ],
        outputs=[
            "EXT001 shortlisted",
            "EXT002 shortlisted",
            "EXT001 needs Data Visualization training",
            "EXT002 needs Data Visualization training",
            "Interview scheduled for APP003",
            "Interview scheduled for APP004",
        ],
    ),
    # 6 REPLACED
    Task(
        annotator="0",
        user_id="res_75",
        instruction="To support Logan Garcia's career pivot, please set up a development plan. First, find him a mentor with expertise in 'Policy' and 'Leadership' and establish an 'Active' relationship. Second, enroll him in the 'Climate Science & Policy' course. Finally, add a new goal to his profile with ID 'G303-2', type 'Role Transition', and description 'Develop policy and leadership skills for cloud compliance role.'",
        actions=[
            Action(
                name="get_user_id_from_name",
                kwargs={"first_name": "Logan", "last_name": "Garcia"},
            ),
            Action(
                name="find_mentors",
                kwargs={"mentee_id": "U303", "focus_areas": ["Policy", "Leadership"]},
            ),
            Action(
                name="get_course_id_by_name",
                kwargs={"course_name": "Climate Science & Policy"},
            ),
            Action(name="get_today_date", kwargs={}),
            Action(
                name="enroll_in_course",
                kwargs={
                    "user_id": "U303",
                    "course_id": "C1007",
                    "enroll_date": "2025-10-02",
                },
            ),
            Action(
                name="add_mentorship_relationship",
                kwargs={
                    "mentor_id": "M102",
                    "mentee_id": "U303",
                    "start_date": "2025-10-02",
                    "status": "Active",
                    "focus_areas": ["Policy", "Leadership"],
                },
            ),
            Action(
                name="add_goal",
                kwargs={
                    "user_id": "U303",
                    "goal": {
                        "goal_id": "G303-2",
                        "goal_type": "Role Transition",
                        "description": "Develop policy and leadership skills for cloud compliance role.",
                    },
                },
            ),
        ],
        outputs=[
            "User U303 enrolled in course C1007",
            "Mentorship relationship MR011 created",
            "goal G303-2 added for U303",
        ],
    ),
    # 7 REPLACED
    Task(
        annotator="0",
        user_id="res_76",
        instruction="Hiring manager Jack Wang is reviewing the application from internal candidate Ava Nguyen for the 'Senior Data Scientist' role. He sees potential but notes a skill gap in 'Machine Learning'. He wants to create a development plan by enrolling her in the 'Machine Learning Specialization' course. After enrolling her, please update her application status to 'Interview with Development Plan', schedule her technical interview, and add a new goal to her profile with ID 'G302-2', type 'Skill Mastery', and description 'Complete Machine Learning Specialization to support transition to Data Science.'",
        actions=[
            Action(
                name="get_job_id_by_title",
                kwargs={"job_title": "Senior Data Scientist"},
            ),
            Action(name="get_job_applications", kwargs={"job_id": "J001"}),
            Action(
                name="get_user_id_from_name",
                kwargs={"first_name": "Ava", "last_name": "Nguyen"},
            ),
            Action(
                name="analyze_applicant_skill_fit",
                kwargs={"applicant_id": "U302", "role": "Senior Data Scientist"},
            ),
            Action(
                name="get_course_id_by_name",
                kwargs={"course_name": "Machine Learning Specialization"},
            ),
            Action(name="get_today_date", kwargs={}),
            Action(
                name="enroll_in_course",
                kwargs={
                    "user_id": "U302",
                    "course_id": "C1005",
                    "enroll_date": "2025-10-02",
                },
            ),
            Action(
                name="update_application_status",
                kwargs={
                    "application_id": "APP001",
                    "new_status": "Interview with Development Plan",
                },
            ),
            Action(
                name="schedule_technical_interview", kwargs={"application_id": "APP001"}
            ),
            Action(
                name="add_goal",
                kwargs={
                    "user_id": "U302",
                    "goal": {
                        "goal_id": "G302-2",
                        "goal_type": "Skill Mastery",
                        "goal_description": "Complete Machine Learning Specialization to support transition to Data Science.",
                    },
                },
            ),
        ],
        outputs=[
            "User U302 enrolled in course C1005",
            "APP001 Interview with Development Plan",
            "Technical interview scheduled for application APP001.",
            "goal G302-2 added for U302",
        ],
    ),
    # 8
    Task(
        annotator="0",
        user_id="res_77",
        instruction="Manager Mason Desai is launching a new data visualization initiative. First, enroll his entire engineering team, including himself and Alexander Adams, in the 'Data Visualization with Tableau' course. To support his leadership, find a mentor for Mason with expertise in 'Engineering' and 'Career Growth' and establish an 'Active' relationship. Then, update Mason's 'Backend Tech Lead' goal to 40% progress and append the note: 'Leading new team-wide data visualization project.' Finally, schedule their first mentorship session for December 12, 2025.",
        actions=[
            Action(
                name="get_user_id_from_name",
                kwargs={"first_name": "Mason", "last_name": "Desai"},
            ),
            Action(name="get_user_profile", kwargs={"user_id": "U312"}),
            Action(name="get_team", kwargs={"team_id": "T003"}),
            Action(
                name="get_course_id_by_name",
                kwargs={"course_name": "Data Visualization with Tableau"},
            ),
            Action(name="get_today_date", kwargs={}),
            Action(
                name="enroll_in_course",
                kwargs={
                    "user_id": "U312",
                    "course_id": "C1003",
                    "enroll_date": "2025-10-02",
                },
            ),
            Action(
                name="enroll_in_course",
                kwargs={
                    "user_id": "U306",
                    "course_id": "C1003",
                    "enroll_date": "2025-10-02",
                },
            ),
            Action(
                name="find_mentors",
                kwargs={
                    "mentee_id": "U312",
                    "focus_areas": ["Engineering", "Career Growth"],
                },
            ),
            Action(
                name="add_mentorship_relationship",
                kwargs={
                    "mentor_id": "M101",
                    "mentee_id": "U312",
                    "start_date": "2025-10-02",
                    "status": "Active",
                    "focus_areas": ["Engineering", "Career Growth"],
                },
            ),
            Action(name="list_user_goals", kwargs={"user_id": "U312"}),
            Action(
                name="update_goal",
                kwargs={
                    "user_id": "U312",
                    "goal_id": "G312-1",
                    "progress_percent": 40,
                    "notes_to_append": "Leading new team-wide data visualization project.",
                    "last_updated_date": "2025-10-02",
                },
            ),
            Action(
                name="schedule_mentorship_session",
                kwargs={"relationship_id": "MR011", "session_date": "2025-12-12"},
            ),
        ],
        outputs=[
            "User U312 enrolled in course C1003",
            "User U306 enrolled in course C1003",
            "Mentorship relationship MR011 created",
            "Goal G312-1 updated for user U312",
            "scheduled_for: 2025-12-12",
        ],
    ),
    # 9
    Task(
        annotator="0",
        user_id="res_78",
        instruction="Expand Marketing Specialist position (J004) candidate pipeline through comprehensive external candidate identification and assessment, conduct skill evaluations for EXT005, implement targeted Product Marketing and Brand Strategy training programs, establish candidate shortlisting with EXT005 advancement, and progress through Skill-Enhanced to Interview-Ready status with technical interview scheduling.",
        actions=[
            Action(name="get_job_posting", kwargs={"job_id": "J004"}),
            Action(name="get_role_skills", kwargs={"role": "Marketing Specialist"}),
            Action(name="get_job_applications", kwargs={"job_id": "J004"}),
            Action(
                name="search_external_candidates_by_skills",
                kwargs={"required_skills": ["Product Marketing", "Brand Strategy"]},
            ),
            Action(
                name="analyze_external_candidate_skill_fit",
                kwargs={"candidate_id": "EXT005", "role": "Marketing Specialist"},
            ),
            Action(
                name="shortlist_external_candidate",
                kwargs={"candidate_id": "EXT005", "job_id": "J004"},
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "EXT005", "skill": "Product Marketing"},
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "EXT005", "skill": "Brand Strategy"},
            ),
            Action(
                name="update_application_status",
                kwargs={"application_id": "APP009", "new_status": "Skill-Enhanced"},
            ),
            Action(
                name="update_application_status",
                kwargs={"application_id": "APP009", "new_status": "Interview-Ready"},
            ),
            Action(
                name="schedule_technical_interview", kwargs={"application_id": "APP009"}
            ),
        ],
        outputs=[
            "EXT005 shortlisted",
            "EXT005 needs Product Marketing training",
            "EXT005 needs Brand Strategy training",
            "APP009 Skill-Enhanced",
            "APP009 Interview-Ready",
            "Interview scheduled for APP009",
        ],
    ),
    # 10 REPLACED
    Task(
        annotator="0",
        user_id="res_79",
        instruction="Team Lead Mason Desai needs to upskill his engineering team for a new data visualization project. First, enroll his entire team in the 'Data Visualization with Tableau' course, but check first to ensure no one is enrolled twice. After that, find a mentor for Mason with expertise in 'Engineering' and 'Career Growth' and establish an 'Active' mentorship. Finally, add the following note to Mason's existing career goal: 'Leading new data-viz project to build team leadership skills.'",
        actions=[
            Action(
                name="get_user_id_from_name",
                kwargs={"first_name": "Mason", "last_name": "Desai"},
            ),
            Action(name="get_user_profile", kwargs={"user_id": "U312"}),
            Action(name="get_team", kwargs={"team_id": "T003"}),
            Action(
                name="get_course_id_by_name",
                kwargs={"course_name": "Data Visualization with Tableau"},
            ),
            Action(name="get_today_date", kwargs={}),
            Action(name="list_user_courses", kwargs={"user_id": "U306"}),
            Action(name="list_user_courses", kwargs={"user_id": "U312"}),
            Action(
                name="enroll_in_course",
                kwargs={
                    "user_id": "U306",
                    "course_id": "C1003",
                    "enroll_date": "2025-10-02",
                },
            ),
            Action(
                name="enroll_in_course",
                kwargs={
                    "user_id": "U312",
                    "course_id": "C1003",
                    "enroll_date": "2025-10-02",
                },
            ),
            Action(
                name="find_mentors",
                kwargs={
                    "mentee_id": "U312",
                    "focus_areas": ["Engineering", "Career Growth"],
                },
            ),
            Action(
                name="add_mentorship_relationship",
                kwargs={
                    "mentor_id": "M101",
                    "mentee_id": "U312",
                    "start_date": "2025-10-02",
                    "status": "Active",
                    "focus_areas": ["Engineering", "Career Growth"],
                },
            ),
            Action(name="list_user_goals", kwargs={"user_id": "U312"}),
            Action(
                name="update_goal",
                kwargs={
                    "user_id": "U312",
                    "goal_id": "G312-1",
                    "notes_to_append": "Leading new data-viz project to build team leadership skills.",
                    "last_updated_date": "2025-10-02",
                },
            ),
        ],
        outputs=[
            "User U306 enrolled in course C1003",
            "User U312 enrolled in course C1003",
            "Mentorship relationship MR011 created",
            "Goal G312-1 updated for user U312",
        ],
    ),
    # 11
    Task(
        annotator="0",
        user_id="res_80",
        instruction="Senior Data Scientist position (J001) requires qualified external candidates EXT001 and EXT002 to be shortlisted and scheduled for technical interviews alongside existing applications.",
        actions=[
            Action(name="get_job_posting", kwargs={"job_id": "J001"}),
            Action(name="get_role_skills", kwargs={"role": "Senior Data Scientist"}),
            Action(name="get_job_applications", kwargs={"job_id": "J001"}),
            Action(
                name="search_external_candidates_by_skills",
                kwargs={
                    "required_skills": [
                        "Machine Learning",
                        "Programming Languages",
                        "Data Visualization",
                    ]
                },
            ),
            Action(
                name="shortlist_external_candidate",
                kwargs={"candidate_id": "EXT001", "job_id": "J001"},
            ),
            Action(
                name="shortlist_external_candidate",
                kwargs={"candidate_id": "EXT002", "job_id": "J001"},
            ),
            Action(
                name="schedule_technical_interview", kwargs={"application_id": "APP003"}
            ),
            Action(
                name="schedule_technical_interview", kwargs={"application_id": "APP004"}
            ),
        ],
        outputs=[
            "EXT001 shortlisted",
            "EXT002 shortlisted",
            "Interview scheduled for APP003",
            "Interview scheduled for APP004",
        ],
    ),
    # 12
    Task(
        annotator="0",
        user_id="res_81",
        instruction="Advance UX Designer position (J002) applications APP005 (Chloe Scott, U307) and APP006 (Emily Johnson, EXT003) through comprehensive skill assessments, targeted training recommendations for Design Operations and Accessibility gaps, development plan implementation, and interview scheduling.",
        actions=[
            Action(name="get_job_posting", kwargs={"job_id": "J002"}),
            Action(name="get_role_skills", kwargs={"role": "UX Designer"}),
            Action(name="get_job_applications", kwargs={"job_id": "J002"}),
            Action(
                name="analyze_applicant_skill_fit",
                kwargs={"applicant_id": "U307", "role": "UX Designer"},
            ),
            Action(
                name="analyze_external_candidate_skill_fit",
                kwargs={"candidate_id": "EXT003", "role": "UX Designer"},
            ),
            Action(
                name="shortlist_external_candidate",
                kwargs={"candidate_id": "EXT003", "job_id": "J002"},
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "U307", "skill": "Design Operations"},
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "EXT003", "skill": "Accessibility"},
            ),
            Action(
                name="update_application_status",
                kwargs={"application_id": "APP005", "new_status": "Development-Plan"},
            ),
            Action(
                name="update_application_status",
                kwargs={"application_id": "APP006", "new_status": "Development-Plan"},
            ),
            Action(
                name="schedule_technical_interview", kwargs={"application_id": "APP005"}
            ),
            Action(
                name="schedule_technical_interview", kwargs={"application_id": "APP006"}
            ),
        ],
        outputs=[
            "EXT003 shortlisted",
            "U307 needs Design Operations training",
            "EXT003 needs Accessibility training",
            "APP005 Development-Plan",
            "APP006 Development-Plan",
            "Interview scheduled for APP005",
            "Interview scheduled for APP006",
        ],
    ),
    # 13
    Task(
        annotator="0",
        user_id="res_82",
        instruction="Establish comprehensive cross-functional training programs for Ava Nguyen (U302, Data Scientist) and candidate U306 (DevOps Engineer) based on thorough skill assessments, external candidate pipeline evaluation, training implementation, and advancement through interview scheduling.",
        actions=[
            Action(name="get_job_applications", kwargs={"job_id": "J001"}),
            Action(name="get_job_applications", kwargs={"job_id": "J003"}),
            Action(name="get_job_posting", kwargs={"job_id": "J001"}),
            Action(name="get_job_posting", kwargs={"job_id": "J003"}),
            Action(name="get_role_skills", kwargs={"role": "Senior Data Scientist"}),
            Action(name="get_role_skills", kwargs={"role": "DevOps Engineer"}),
            Action(
                name="analyze_applicant_skill_fit",
                kwargs={"applicant_id": "U302", "role": "Senior Data Scientist"},
            ),
            Action(
                name="analyze_applicant_skill_fit",
                kwargs={"applicant_id": "U306", "role": "DevOps Engineer"},
            ),
            Action(
                name="search_external_candidates_by_skills",
                kwargs={"required_skills": ["Machine Learning", "Data Visualization"]},
            ),
            Action(
                name="search_external_candidates_by_skills",
                kwargs={
                    "required_skills": [
                        "Infrastructure as Code",
                        "Monitoring & Logging",
                    ]
                },
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "U302", "skill": "Machine Learning"},
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "U302", "skill": "Data Visualization"},
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "U306", "skill": "Infrastructure as Code"},
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "U306", "skill": "Monitoring & Logging"},
            ),
            Action(
                name="update_application_status",
                kwargs={"application_id": "APP001", "new_status": "Training-Program"},
            ),
            Action(
                name="update_application_status",
                kwargs={"application_id": "APP007", "new_status": "Training-Program"},
            ),
            Action(
                name="schedule_technical_interview", kwargs={"application_id": "APP001"}
            ),
            Action(
                name="schedule_technical_interview", kwargs={"application_id": "APP007"}
            ),
        ],
        outputs=[
            "U302 needs Machine Learning training",
            "U302 needs Data Visualization training",
            "U306 needs Infrastructure as Code training",
            "U306 needs Monitoring & Logging training",
            "APP001 Training-Program",
            "APP007 Training-Program",
            "Interview scheduled for APP001",
            "Interview scheduled for APP007",
        ],
    ),
    # 14 REPLACED
    Task(
        annotator="0",
        user_id="res_84",
        instruction="Logan Garcia is working towards his goal of pivoting to cloud compliance. To help him, find a mentor with expertise in 'Policy' and 'Leadership' and establish an 'Active' relationship. After creating the relationship, update his primary career goal by appending the note: 'Mentorship with M102 started to build leadership skills.' Finally, schedule their first session for October 24, 2025.",
        actions=[
            Action(
                name="get_user_id_from_name",
                kwargs={"first_name": "Logan", "last_name": "Garcia"},
            ),
            Action(name="list_user_courses", kwargs={"user_id": "U303"}),
            Action(name="list_user_goals", kwargs={"user_id": "U303"}),
            Action(
                name="find_mentors",
                kwargs={"mentee_id": "U303", "focus_areas": ["Policy", "Leadership"]},
            ),
            Action(name="get_today_date", kwargs={}),
            Action(
                name="add_mentorship_relationship",
                kwargs={
                    "mentor_id": "M102",
                    "mentee_id": "U303",
                    "start_date": "2025-10-02",
                    "status": "Active",
                    "focus_areas": ["Policy", "Leadership"],
                },
            ),
            Action(
                name="update_goal",
                kwargs={
                    "user_id": "U303",
                    "goal_id": "G303-1",
                    "notes_to_append": "Mentorship with M102 started to build leadership skills.",
                    "last_updated_date": "2025-10-02",
                },
            ),
            Action(
                name="schedule_mentorship_session",
                kwargs={"relationship_id": "MR011", "session_date": "2025-10-24"},
            ),
        ],
        outputs=[
            "Mentorship relationship MR011 created",
            "Goal G303-1 updated for user U303",
            "scheduled_for: 2025-10-24",
        ],
    ),
    # 15 REPLACED
    Task(
        annotator="0",
        user_id="res_85",
        instruction="Chloe Scott has successfully completed the 'UX Design Fundamentals' course and is now ready to focus on her leadership potential. Please find an available mentor for her with expertise in 'Policy' and 'Design' and establish an 'Active' mentorship relationship. Then, create a new career goal for her with ID 'G307-3', type 'Leadership Development', and description 'Develop leadership skills for future Design Lead roles.' Finally, schedule their first session for November 14, 2025.",
        actions=[
            Action(
                name="get_user_id_from_name",
                kwargs={"first_name": "Chloe", "last_name": "Scott"},
            ),
            Action(
                name="get_course_id_by_name",
                kwargs={"course_name": "UX Design Fundamentals"},
            ),
            Action(name="list_user_courses", kwargs={"user_id": "U307"}),
            Action(
                name="find_mentors",
                kwargs={"mentee_id": "U307", "focus_areas": ["Policy", "Design"]},
            ),
            Action(name="get_today_date", kwargs={}),
            Action(
                name="add_mentorship_relationship",
                kwargs={
                    "mentor_id": "M100",
                    "mentee_id": "U307",
                    "start_date": "2025-10-02",
                    "status": "Active",
                    "focus_areas": ["Policy", "Design"],
                },
            ),
            Action(
                name="add_goal",
                kwargs={
                    "user_id": "U307",
                    "goal": {
                        "goal_id": "G307-3",
                        "goal_type": "Leadership Development",
                        "description": "Develop leadership skills for future Design Lead roles.",
                    },
                },
            ),
            Action(
                name="schedule_mentorship_session",
                kwargs={"relationship_id": "MR011", "session_date": "2025-11-14"},
            ),
        ],
        outputs=[
            "Mentorship relationship MR011 created",
            "goal G307-3 added for U307",
            "scheduled_for: 2025-11-14",
        ],
    ),
    # 16
    Task(
        annotator="0",
        user_id="res_86",
        instruction="Advance application APP001 (Ava Nguyen, U302) for Senior Data Scientist position (J001) through comprehensive skill assessment, identify specific skill gaps, implement targeted training recommendations for Machine Learning and Data Visualization, update status to Final-Interview, and schedule technical interview.",
        actions=[
            Action(name="get_job_posting", kwargs={"job_id": "J001"}),
            Action(name="get_role_skills", kwargs={"role": "Senior Data Scientist"}),
            Action(name="get_job_applications", kwargs={"job_id": "J001"}),
            Action(
                name="analyze_applicant_skill_fit",
                kwargs={"applicant_id": "U302", "role": "Senior Data Scientist"},
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "U302", "skill": "Machine Learning"},
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "U302", "skill": "Data Visualization"},
            ),
            Action(
                name="update_application_status",
                kwargs={"application_id": "APP001", "new_status": "Skills-Enhanced"},
            ),
            Action(
                name="update_application_status",
                kwargs={"application_id": "APP001", "new_status": "Final-Interview"},
            ),
            Action(
                name="schedule_technical_interview", kwargs={"application_id": "APP001"}
            ),
            Action(
                name="analyze_applicant_skill_fit",
                kwargs={"applicant_id": "U302", "role": "Senior Data Scientist"},
            ),
        ],
        outputs=[
            "U302 needs Machine Learning training",
            "U302 needs Data Visualization training",
            "APP001 Skills-Enhanced",
            "APP001 Final-Interview",
            "Interview scheduled for APP001",
        ],
    ),
    # 17
    Task(
        annotator="0",
        user_id="res_87",
        instruction="Execute comprehensive multi-position application processing for APP001 (U302, Senior Data Scientist), APP005 (U307, UX Designer), and APP007 (U306, DevOps Engineer) through thorough skill assessments, targeted training delivery (Machine Learning for U302, Design Thinking for U307, Infrastructure as Code for U306), advancement to Interview-Ready status, and technical interview scheduling coordination.",
        actions=[
            Action(name="get_job_applications", kwargs={"job_id": "J001"}),
            Action(name="get_job_applications", kwargs={"job_id": "J002"}),
            Action(name="get_job_applications", kwargs={"job_id": "J003"}),
            Action(name="get_job_posting", kwargs={"job_id": "J001"}),
            Action(name="get_job_posting", kwargs={"job_id": "J002"}),
            Action(name="get_job_posting", kwargs={"job_id": "J003"}),
            Action(name="get_role_skills", kwargs={"role": "Senior Data Scientist"}),
            Action(name="get_role_skills", kwargs={"role": "UX Designer"}),
            Action(name="get_role_skills", kwargs={"role": "DevOps Engineer"}),
            Action(
                name="analyze_applicant_skill_fit",
                kwargs={"applicant_id": "U302", "role": "Senior Data Scientist"},
            ),
            Action(
                name="analyze_applicant_skill_fit",
                kwargs={"applicant_id": "U307", "role": "UX Designer"},
            ),
            Action(
                name="analyze_applicant_skill_fit",
                kwargs={"applicant_id": "U306", "role": "DevOps Engineer"},
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "U302", "skill": "Machine Learning"},
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "U307", "skill": "Design Thinking"},
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "U306", "skill": "Infrastructure as Code"},
            ),
            Action(
                name="update_application_status",
                kwargs={"application_id": "APP001", "new_status": "Interview-Ready"},
            ),
            Action(
                name="update_application_status",
                kwargs={"application_id": "APP005", "new_status": "Interview-Ready"},
            ),
            Action(
                name="update_application_status",
                kwargs={"application_id": "APP007", "new_status": "Interview-Ready"},
            ),
            Action(
                name="schedule_technical_interview", kwargs={"application_id": "APP001"}
            ),
            Action(
                name="schedule_technical_interview", kwargs={"application_id": "APP005"}
            ),
            Action(
                name="schedule_technical_interview", kwargs={"application_id": "APP007"}
            ),
        ],
        outputs=[
            "U302 needs Machine Learning training",
            "U307 needs Design Thinking training",
            "U306 needs Infrastructure as Code training",
            "APP001 Interview-Ready",
            "APP005 Interview-Ready",
            "APP007 Interview-Ready",
            "Interview scheduled for APP001",
            "Interview scheduled for APP005",
            "Interview scheduled for APP007",
        ],
    ),
    # 18 REPLACED
    Task(
        annotator="0",
        user_id="res_88",
        instruction="Manager Jack Wang wants to create a development plan for his direct report, Ava Nguyen, to prepare her for a Senior Data Scientist role. Please enroll her in two courses: 'Advanced Python' and 'Data Visualization with Tableau'. Then, add a new career goal for her with the ID 'G302-3', type 'Role Transition', and the description 'Complete Python and Tableau training for Senior Data Scientist path.' Finally, establish a new mentorship relationship with Jack Wang as the mentor and Ava Nguyen as the mentee, focusing on 'Python' and 'Data Science'.",
        actions=[
            Action(
                name="get_user_id_from_name",
                kwargs={"first_name": "Jack", "last_name": "Wang"},
            ),
            Action(
                name="get_user_id_from_name",
                kwargs={"first_name": "Ava", "last_name": "Nguyen"},
            ),
            Action(
                name="get_course_id_by_name", kwargs={"course_name": "Advanced Python"}
            ),
            Action(
                name="get_course_id_by_name",
                kwargs={"course_name": "Data Visualization with Tableau"},
            ),
            Action(name="get_today_date", kwargs={}),
            Action(
                name="enroll_in_course",
                kwargs={
                    "user_id": "U302",
                    "course_id": "C1001",
                    "enroll_date": "2025-10-02",
                },
            ),
            Action(
                name="enroll_in_course",
                kwargs={
                    "user_id": "U302",
                    "course_id": "C1003",
                    "enroll_date": "2025-10-02",
                },
            ),
            Action(
                name="add_goal",
                kwargs={
                    "user_id": "U302",
                    "goal": {
                        "goal_id": "G302-3",
                        "goal_type": "Role Transition",
                        "goal_description": "Complete Python and Tableau training for Senior Data Scientist path.",
                    },
                },
            ),
            Action(
                name="add_mentorship_relationship",
                kwargs={
                    "mentor_id": "U301",
                    "mentee_id": "U302",
                    "start_date": "2025-10-02",
                    "status": "Active",
                    "focus_areas": ["Python", "Data Science"],
                },
            ),
        ],
        outputs=[
            "User U302 enrolled in course C1001",
            "User U302 enrolled in course C1003",
            "goal G302-3 added for U302",
            "Mentorship relationship MR011 created",
        ],
    ),
    # 19 REPLACED
    Task(
        annotator="0",
        user_id="res_89",
        instruction="Manager Mason Desai is leading a new data visualization project. Enroll both him and his team member Alexander Adams in the 'Data Visualization with Tableau' course. To support his leadership on this project, find a new mentor for Mason with expertise in 'Engineering' and 'Career Growth' and establish an 'Active' relationship. Then, update Mason's primary career goal with the note 'Leading team data-viz upskilling initiative.' Finally, schedule their first mentorship session for November 7, 2025.",
        actions=[
            Action(
                name="get_user_id_from_name",
                kwargs={"first_name": "Mason", "last_name": "Desai"},
            ),
            Action(
                name="get_user_id_from_name",
                kwargs={"first_name": "Alexander", "last_name": "Adams"},
            ),
            Action(
                name="get_course_id_by_name",
                kwargs={"course_name": "Data Visualization with Tableau"},
            ),
            Action(name="get_today_date", kwargs={}),
            Action(
                name="enroll_in_course",
                kwargs={
                    "user_id": "U312",
                    "course_id": "C1003",
                    "enroll_date": "2025-10-02",
                },
            ),
            Action(
                name="enroll_in_course",
                kwargs={
                    "user_id": "U306",
                    "course_id": "C1003",
                    "enroll_date": "2025-10-02",
                },
            ),
            Action(
                name="find_mentors",
                kwargs={
                    "mentee_id": "U312",
                    "focus_areas": ["Engineering", "Career Growth"],
                },
            ),
            Action(
                name="add_mentorship_relationship",
                kwargs={
                    "mentor_id": "M101",
                    "mentee_id": "U312",
                    "start_date": "2025-10-02",
                    "status": "Active",
                    "focus_areas": ["Engineering", "Career Growth"],
                },
            ),
            Action(name="list_user_goals", kwargs={"user_id": "U312"}),
            Action(
                name="update_goal",
                kwargs={
                    "user_id": "U312",
                    "goal_id": "G312-1",
                    "notes_to_append": "Leading team data-viz upskilling initiative.",
                    "last_updated_date": "2025-10-02",
                },
            ),
            Action(
                name="schedule_mentorship_session",
                kwargs={"relationship_id": "MR011", "session_date": "2025-11-07"},
            ),
        ],
        outputs=[
            "User U312 enrolled in course C1003",
            "User U306 enrolled in course C1003",
            "Mentorship relationship MR011 created",
            "Goal G312-1 updated for user U312",
            "scheduled_for: 2025-11-07",
        ],
    ),
    # 20
    Task(
        annotator="0",
        user_id="res_90",
        instruction="Execute comprehensive Security Analyst position (J005) advancement for application APP010 (external candidate EXT006) through thorough skill assessment, targeted Cloud Security and Compliance training implementation, candidate pipeline enhancement through skill-based search, EXT006 shortlisting, multi-stage progression through Skills-Enhanced to Interview-Pending to Background-Check status, and technical interview scheduling.",
        actions=[
            Action(name="get_job_applications", kwargs={"job_id": "J005"}),
            Action(name="get_job_posting", kwargs={"job_id": "J005"}),
            Action(name="get_role_skills", kwargs={"role": "Security Analyst"}),
            Action(
                name="analyze_external_candidate_skill_fit",
                kwargs={"candidate_id": "EXT006", "role": "Security Analyst"},
            ),
            Action(
                name="search_external_candidates_by_skills",
                kwargs={"required_skills": ["Cloud Security", "Compliance"]},
            ),
            Action(
                name="shortlist_external_candidate",
                kwargs={"candidate_id": "EXT006", "job_id": "J005"},
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "EXT006", "skill": "Cloud Security"},
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "EXT006", "skill": "Compliance"},
            ),
            Action(
                name="update_application_status",
                kwargs={"application_id": "APP010", "new_status": "Skills-Enhanced"},
            ),
            Action(
                name="update_application_status",
                kwargs={"application_id": "APP010", "new_status": "Interview-Pending"},
            ),
            Action(
                name="update_application_status",
                kwargs={"application_id": "APP010", "new_status": "Background-Check"},
            ),
            Action(
                name="schedule_technical_interview", kwargs={"application_id": "APP010"}
            ),
        ],
        outputs=[
            "EXT006 shortlisted",
            "EXT006 needs Cloud Security training",
            "EXT006 needs Compliance training",
            "APP010 Skills-Enhanced",
            "APP010 Interview-Pending",
            "APP010 Background-Check",
            "Interview scheduled for APP010",
        ],
    ),
    # 21
    Task(
        annotator="0",
        user_id="res_91",
        instruction="Expand Senior Data Scientist position (J001) candidate pipeline with external candidates EXT001 and EXT002 having strong technical backgrounds, conduct skill assessments, and implement targeted training recommendations.",
        actions=[
            Action(name="get_role_skills", kwargs={"role": "Senior Data Scientist"}),
            Action(name="get_job_posting", kwargs={"job_id": "J001"}),
            Action(
                name="search_external_candidates_by_skills",
                kwargs={
                    "required_skills": [
                        "Machine Learning",
                        "Programming Languages",
                        "Data Visualization",
                    ]
                },
            ),
            Action(
                name="shortlist_external_candidate",
                kwargs={"candidate_id": "EXT001", "job_id": "J001"},
            ),
            Action(
                name="shortlist_external_candidate",
                kwargs={"candidate_id": "EXT002", "job_id": "J001"},
            ),
            Action(
                name="analyze_external_candidate_skill_fit",
                kwargs={"candidate_id": "EXT001", "role": "Senior Data Scientist"},
            ),
            Action(
                name="analyze_external_candidate_skill_fit",
                kwargs={"candidate_id": "EXT002", "role": "Senior Data Scientist"},
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "EXT001", "skill": "Data Visualization"},
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "EXT002", "skill": "Data Visualization"},
            ),
        ],
        outputs=[
            "EXT001 shortlisted",
            "EXT002 shortlisted",
            "EXT001 needs Data Visualization training",
            "EXT002 needs Data Visualization training",
        ],
    ),
    # 22 REPLACED
    Task(
        annotator="0",
        user_id="res_92",
        instruction="Manager David Adams is reviewing progress on Chloe Scott's goal to 'Publish company-wide accessibility guidelines'. First, update this goal to 50% progress and append the note: 'Guideline draft complete. Next step: training plan.' Second, update her active mentorship relationship to refocus on 'Policy Writing' and 'Teamwork'. Third, enroll her in the 'Climate Science & Policy' course to support this new focus. Finally, schedule their next meeting for December 5, 2025.",
        actions=[
            Action(
                name="get_user_id_from_name",
                kwargs={"first_name": "David", "last_name": "Adams"},
            ),
            Action(
                name="get_user_id_from_name",
                kwargs={"first_name": "Chloe", "last_name": "Scott"},
            ),
            Action(name="list_user_goals", kwargs={"user_id": "U307"}),
            Action(name="list_user_mentorships", kwargs={"user_id": "U307"}),
            Action(
                name="get_course_id_by_name",
                kwargs={"course_name": "Climate Science & Policy"},
            ),
            Action(name="get_today_date", kwargs={}),
            Action(
                name="update_goal",
                kwargs={
                    "user_id": "U307",
                    "goal_id": "G307-1",
                    "progress_percent": 50,
                    "notes_to_append": "Guideline draft complete. Next step: training plan.",
                    "last_updated_date": "2025-10-02",
                },
            ),
            Action(
                name="update_mentorship_relationship",
                kwargs={
                    "relationship_id": "MR003",
                    "updates": {"focus_areas": ["Policy Writing", "Teamwork"]},
                },
            ),
            Action(
                name="enroll_in_course",
                kwargs={
                    "user_id": "U307",
                    "course_id": "C1007",
                    "enroll_date": "2025-10-02",
                },
            ),
            Action(
                name="schedule_mentorship_session",
                kwargs={"relationship_id": "MR003", "session_date": "2025-12-05"},
            ),
        ],
        outputs=[
            "Goal G307-1 updated for user U307",
            "relationship MR003 updated",
            "User U307 enrolled in course C1007",
            "scheduled_for: 2025-12-05",
        ],
    ),
    # 23 REPLACED
    Task(
        annotator="0",
        user_id="res_93",
        instruction="Hiring manager Jack Wang has reviewed the application from internal candidate Harper Bennett for the 'Senior Data Scientist' role. He has decided to reject her for the current opening but wants to put her on a development track for the future. First, update her application status to 'Rejected - Future Consideration with Dev Plan'. Then, enroll her in two courses: 'Advanced Python' and 'Machine Learning Specialization'. Finally, add a new goal to her profile with ID 'G310-2', type 'Role Transition', and description 'Complete Python and ML training for future Data Scientist opportunities.'",
        actions=[
            Action(
                name="get_user_id_from_name",
                kwargs={"first_name": "Jack", "last_name": "Wang"},
            ),
            Action(
                name="get_user_id_from_name",
                kwargs={"first_name": "Harper", "last_name": "Bennett"},
            ),
            Action(
                name="get_job_id_by_title",
                kwargs={"job_title": "Senior Data Scientist"},
            ),
            Action(name="get_job_applications", kwargs={"job_id": "J001"}),
            Action(
                name="update_application_status",
                kwargs={
                    "application_id": "APP002",
                    "new_status": "Rejected - Future Consideration with Dev Plan",
                },
            ),
            Action(
                name="get_course_id_by_name", kwargs={"course_name": "Advanced Python"}
            ),
            Action(
                name="get_course_id_by_name",
                kwargs={"course_name": "Machine Learning Specialization"},
            ),
            Action(name="get_today_date", kwargs={}),
            Action(
                name="enroll_in_course",
                kwargs={
                    "user_id": "U310",
                    "course_id": "C1001",
                    "enroll_date": "2025-10-02",
                },
            ),
            Action(
                name="enroll_in_course",
                kwargs={
                    "user_id": "U310",
                    "course_id": "C1005",
                    "enroll_date": "2025-10-02",
                },
            ),
            Action(
                name="add_goal",
                kwargs={
                    "user_id": "U310",
                    "goal": {
                        "goal_id": "G310-2",
                        "goal_type": "Role Transition",
                        "description": "Complete Python and ML training for future Data Scientist opportunities.",
                    },
                },
            ),
        ],
        outputs=[
            "APP002 Rejected - Future Consideration with Dev Plan",
            "User U310 enrolled in course C1001",
            "User U310 enrolled in course C1005",
            "goal G310-2 added for U310",
        ],
    ),
    # 24 REPLACED
    Task(
        annotator="0",
        user_id="res_94",
        instruction="To support Jack Wang's goal of becoming Director of Data Science, please enroll him in two key courses: the 'Machine Learning Specialization' and the 'Project Management Professional' course. After enrolling him, update his primary career goal to 40% progress and append the note: 'Enrolled in ML and PMP courses to build technical and leadership skills.' Finally, update his existing mentorship relationship to add 'Team Leadership' as a new focus area.",
        actions=[
            Action(
                name="get_user_id_from_name",
                kwargs={"first_name": "Jack", "last_name": "Wang"},
            ),
            Action(name="list_user_goals", kwargs={"user_id": "U301"}),
            Action(name="list_user_mentorships", kwargs={"user_id": "U301"}),
            Action(
                name="get_course_id_by_name",
                kwargs={"course_name": "Machine Learning Specialization"},
            ),
            Action(
                name="get_course_id_by_name",
                kwargs={"course_name": "Project Management Professional"},
            ),
            Action(name="get_today_date", kwargs={}),
            Action(
                name="enroll_in_course",
                kwargs={
                    "user_id": "U301",
                    "course_id": "C1005",
                    "enroll_date": "2025-10-02",
                },
            ),
            Action(
                name="enroll_in_course",
                kwargs={
                    "user_id": "U301",
                    "course_id": "C1004",
                    "enroll_date": "2025-10-02",
                },
            ),
            Action(
                name="update_goal",
                kwargs={
                    "user_id": "U301",
                    "goal_id": "G301-1",
                    "progress_percent": 40,
                    "notes_to_append": "Enrolled in ML and PMP courses to build technical and leadership skills.",
                    "last_updated_date": "2025-10-02",
                },
            ),
            Action(
                name="update_mentorship_relationship",
                kwargs={
                    "relationship_id": "MR001",
                    "updates": {
                        "focus_areas": [
                            "Leadership",
                            "Data Science",
                            "Career Growth",
                            "Team Leadership",
                        ]
                    },
                },
            ),
        ],
        outputs=[
            "User U301 enrolled in course C1005",
            "User U301 enrolled in course C1004",
            "Goal G301-1 updated for user U301",
            "relationship MR001 updated",
        ],
    ),
    # 25
    Task(
        annotator="0",
        user_id="res_95",
        instruction="Advance application APP002 (Harper Bennett, U310) for Senior Data Scientist position (J001) through advancement assessment, skill development planning, and progression to interview readiness status.",
        actions=[
            Action(name="get_job_posting", kwargs={"job_id": "J001"}),
            Action(name="get_role_skills", kwargs={"role": "Senior Data Scientist"}),
            Action(name="get_job_applications", kwargs={"job_id": "J001"}),
            Action(
                name="analyze_applicant_skill_fit",
                kwargs={"applicant_id": "U310", "role": "Senior Data Scientist"},
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "U310", "skill": "Machine Learning"},
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "U310", "skill": "Programming Languages"},
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "U310", "skill": "Data Visualization"},
            ),
            Action(
                name="update_application_status",
                kwargs={
                    "application_id": "APP002",
                    "new_status": "Advancement-Assessment",
                },
            ),
            Action(
                name="schedule_technical_interview", kwargs={"application_id": "APP002"}
            ),
        ],
        outputs=[
            "U310 needs Machine Learning training",
            "U310 needs Programming Languages training",
            "U310 needs Data Visualization training",
            "APP002 Advancement-Assessment",
            "Interview scheduled for APP002",
        ],
    ),
    # 26 REPLACED
    Task(
        annotator="0",
        user_id="res_96",
        instruction="Hiring manager David Adams is reviewing Chloe Scott's application for the 'UX Design Lead' role. He wants to proceed, but first wants to address her skill gap in Design Operations. Please enroll Chloe in the 'Project Management Professional' course. Then, update her application status to 'Interview with Dev Plan'. After that, schedule her technical interview. Finally, add a new goal to her profile with ID 'G307-4', type 'Skill Mastery', and description 'Complete PMP to build Design Operations skills for UX Lead role.'",
        actions=[
            Action(
                name="get_user_id_from_name",
                kwargs={"first_name": "David", "last_name": "Adams"},
            ),
            Action(
                name="get_user_id_from_name",
                kwargs={"first_name": "Chloe", "last_name": "Scott"},
            ),
            Action(name="get_job_id_by_title", kwargs={"job_title": "UX Design Lead"}),
            Action(name="get_job_applications", kwargs={"job_id": "J002"}),
            Action(
                name="analyze_applicant_skill_fit",
                kwargs={"applicant_id": "U307", "role": "UX Design Lead"},
            ),
            Action(
                name="get_course_id_by_name",
                kwargs={"course_name": "Project Management Professional"},
            ),
            Action(name="get_today_date", kwargs={}),
            Action(
                name="enroll_in_course",
                kwargs={
                    "user_id": "U307",
                    "course_id": "C1004",
                    "enroll_date": "2025-10-02",
                },
            ),
            Action(
                name="update_application_status",
                kwargs={
                    "application_id": "APP005",
                    "new_status": "Interview with Dev Plan",
                },
            ),
            Action(
                name="schedule_technical_interview", kwargs={"application_id": "APP005"}
            ),
            Action(
                name="add_goal",
                kwargs={
                    "user_id": "U307",
                    "goal": {
                        "goal_id": "G307-4",
                        "goal_type": "Skill Mastery",
                        "description": "Complete PMP to build Design Operations skills for UX Lead role.",
                    },
                },
            ),
        ],
        outputs=[
            "User U307 enrolled in course C1004",
            "APP005 Interview with Dev Plan",
            "Technical interview scheduled for application APP005.",
            "goal G307-4 added for U307",
        ],
    ),
    # 27
    Task(
        annotator="0",
        user_id="res_97",
        instruction="Conduct comprehensive UX Designer pipeline (J002) audit with technical interview scheduling for applications APP005 (Chloe Scott, U307) and APP006 (Emily Johnson, EXT003).",
        actions=[
            Action(name="get_job_posting", kwargs={"job_id": "J002"}),
            Action(name="get_role_skills", kwargs={"role": "UX Designer"}),
            Action(name="get_job_applications", kwargs={"job_id": "J002"}),
            Action(
                name="analyze_applicant_skill_fit",
                kwargs={"applicant_id": "U307", "role": "UX Designer"},
            ),
            Action(
                name="analyze_external_candidate_skill_fit",
                kwargs={"candidate_id": "EXT003", "role": "UX Designer"},
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "U307", "skill": "Design Operations"},
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "EXT003", "skill": "Design Thinking"},
            ),
            Action(
                name="update_application_status",
                kwargs={"application_id": "APP005", "new_status": "Screen-Scheduled"},
            ),
            Action(
                name="schedule_technical_interview", kwargs={"application_id": "APP005"}
            ),
            Action(
                name="update_application_status",
                kwargs={"application_id": "APP006", "new_status": "Screen-Scheduled"},
            ),
            Action(
                name="schedule_technical_interview", kwargs={"application_id": "APP006"}
            ),
        ],
        outputs=[
            "U307 needs Design Operations training",
            "EXT003 needs Design Thinking training",
            "APP005 Screen-Scheduled",
            "Interview scheduled for APP005",
            "APP006 Screen-Scheduled",
            "Interview scheduled for APP006",
        ],
    ),
    # 28 REPLACED
    Task(
        annotator="0",
        user_id="res_98",
        instruction="Manager Mason Desai has selected his team member, Alexander Adams, to be the technical lead for a new project requiring advanced Python. First, enroll Alexander in the 'Advanced Python' course. Second, find a mentor for him with expertise in 'Engineering' and 'Career Growth' and establish an 'Active' relationship. Third, update Alexander's primary career goal with the note: 'Leading technical implementation for new Python project.' Finally, schedule their first mentorship session for November 21, 2025.",
        actions=[
            Action(
                name="get_user_id_from_name",
                kwargs={"first_name": "Mason", "last_name": "Desai"},
            ),
            Action(
                name="get_user_id_from_name",
                kwargs={"first_name": "Alexander", "last_name": "Adams"},
            ),
            Action(
                name="get_course_id_by_name", kwargs={"course_name": "Advanced Python"}
            ),
            Action(name="get_today_date", kwargs={}),
            Action(
                name="enroll_in_course",
                kwargs={
                    "user_id": "U306",
                    "course_id": "C1001",
                    "enroll_date": "2025-10-02",
                },
            ),
            Action(
                name="find_mentors",
                kwargs={
                    "mentee_id": "U306",
                    "focus_areas": ["Engineering", "Career Growth"],
                },
            ),
            Action(
                name="add_mentorship_relationship",
                kwargs={
                    "mentor_id": "M101",
                    "mentee_id": "U306",
                    "start_date": "2025-10-02",
                    "status": "Active",
                    "focus_areas": ["Engineering", "Career Growth"],
                },
            ),
            Action(name="list_user_goals", kwargs={"user_id": "U306"}),
            Action(
                name="update_goal",
                kwargs={
                    "user_id": "U306",
                    "goal_id": "G306-1",
                    "notes_to_append": "Leading technical implementation for new Python project.",
                    "last_updated_date": "2025-10-02",
                },
            ),
            Action(
                name="schedule_mentorship_session",
                kwargs={"relationship_id": "MR011", "session_date": "2025-11-21"},
            ),
        ],
        outputs=[
            "User U306 enrolled in course C1001",
            "Mentorship relationship MR011 created",
            "Goal G306-1 updated for user U306",
            "scheduled_for: 2025-11-21",
        ],
    ),
    # 29 REPLACED
    Task(
        annotator="0",
        user_id="res_99",
        instruction="To support Harper Bennett's goal of standing up a People-Analytics function, please create a formal training plan. First, verify she is not already enrolled, then enroll her in two courses: 'Machine Learning Specialization' and 'Advanced Python'. After enrolling her, update her primary career goal to 25% progress, set its status to 'In Progress', and append the note: 'Enrolled in foundational ML and Python courses.'",
        actions=[
            Action(
                name="get_user_id_from_name",
                kwargs={"first_name": "Harper", "last_name": "Bennett"},
            ),
            Action(name="list_user_goals", kwargs={"user_id": "U310"}),
            Action(
                name="get_course_id_by_name",
                kwargs={"course_name": "Machine Learning Specialization"},
            ),
            Action(
                name="get_course_id_by_name", kwargs={"course_name": "Advanced Python"}
            ),
            Action(name="list_user_courses", kwargs={"user_id": "U310"}),
            Action(name="get_today_date", kwargs={}),
            Action(
                name="enroll_in_course",
                kwargs={
                    "user_id": "U310",
                    "course_id": "C1005",
                    "enroll_date": "2025-10-02",
                },
            ),
            Action(
                name="enroll_in_course",
                kwargs={
                    "user_id": "U310",
                    "course_id": "C1001",
                    "enroll_date": "2025-10-02",
                },
            ),
            Action(
                name="update_goal",
                kwargs={
                    "user_id": "U310",
                    "goal_id": "G310-1",
                    "progress_percent": 25,
                    "status": "In Progress",
                    "notes_to_append": "Enrolled in foundational ML and Python courses.",
                    "last_updated_date": "2025-10-02",
                },
            ),
        ],
        outputs=[
            "User U310 enrolled in course C1005",
            "User U310 enrolled in course C1001",
            "Goal G310-1 updated for user U310",
        ],
    ),
    # 30
    Task(
        annotator="0",
        user_id="res_110",
        instruction="Execute comprehensive DevOps Engineer position (J003) advancement for applications APP007 (candidate U306) and APP008 through thorough skill assessments, external candidate pipeline expansion with EXT004 evaluation and shortlisting, multi-level training implementation for all identified skill gaps, pipeline optimization, and coordinated technical screening with interview scheduling.",
        actions=[
            Action(name="get_job_applications", kwargs={"job_id": "J003"}),
            Action(name="get_job_posting", kwargs={"job_id": "J003"}),
            Action(name="get_role_skills", kwargs={"role": "DevOps Engineer"}),
            Action(
                name="analyze_applicant_skill_fit",
                kwargs={"applicant_id": "U306", "role": "DevOps Engineer"},
            ),
            Action(
                name="search_external_candidates_by_skills",
                kwargs={
                    "required_skills": [
                        "CI/CD",
                        "Containerization",
                        "Cloud Platforms",
                        "Infrastructure as Code",
                        "Monitoring & Logging",
                    ]
                },
            ),
            Action(
                name="analyze_external_candidate_skill_fit",
                kwargs={"candidate_id": "EXT004", "role": "DevOps Engineer"},
            ),
            Action(
                name="shortlist_external_candidate",
                kwargs={"candidate_id": "EXT004", "job_id": "J003"},
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "EXT004", "skill": "CI/CD"},
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "EXT004", "skill": "Monitoring & Logging"},
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "U306", "skill": "Infrastructure as Code"},
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "U306", "skill": "Monitoring & Logging"},
            ),
            Action(
                name="update_application_status",
                kwargs={"application_id": "APP007", "new_status": "Training-Enhanced"},
            ),
            Action(
                name="update_application_status",
                kwargs={"application_id": "APP007", "new_status": "Tech-Screen"},
            ),
            Action(
                name="update_application_status",
                kwargs={"application_id": "APP008", "new_status": "Pipeline-Optimized"},
            ),
            Action(
                name="update_application_status",
                kwargs={"application_id": "APP008", "new_status": "Tech-Screen"},
            ),
            Action(
                name="schedule_technical_interview", kwargs={"application_id": "APP007"}
            ),
            Action(
                name="schedule_technical_interview", kwargs={"application_id": "APP008"}
            ),
        ],
        outputs=[
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
            "Interview scheduled for APP008",
        ],
    ),
    # 31
    Task(
        annotator="0",
        user_id="res_101",
        instruction="Expand UX Designer position (J002) candidate pipeline through comprehensive candidate evaluation, conduct skill assessments for EXT003 and U307, implement targeted training for identified skill gaps, advance candidate pipeline with EXT003 shortlisting, and coordinate interview scheduling.",
        actions=[
            Action(name="get_role_skills", kwargs={"role": "UX Designer"}),
            Action(name="get_job_posting", kwargs={"job_id": "J002"}),
            Action(name="get_job_applications", kwargs={"job_id": "J002"}),
            Action(
                name="analyze_external_candidate_skill_fit",
                kwargs={"candidate_id": "EXT003", "role": "UX Designer"},
            ),
            Action(
                name="analyze_applicant_skill_fit",
                kwargs={"applicant_id": "U307", "role": "UX Designer"},
            ),
            Action(
                name="shortlist_external_candidate",
                kwargs={"candidate_id": "EXT003", "job_id": "J002"},
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "EXT003", "skill": "Leadership"},
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "U307", "skill": "Leadership"},
            ),
            Action(
                name="update_application_status",
                kwargs={"application_id": "APP005", "new_status": "Pipeline-Expanded"},
            ),
            Action(
                name="schedule_technical_interview", kwargs={"application_id": "APP005"}
            ),
        ],
        outputs=[
            "EXT003 shortlisted",
            "EXT003 needs Leadership training",
            "U307 needs Leadership training",
            "APP005 Pipeline-Expanded",
            "Interview scheduled for APP005",
        ],
    ),
    # 32 REPLACED
    Task(
        annotator="0",
        user_id="res_102",
        instruction="Manager Jack Wang is reviewing the progress of his report, Ava Nguyen. He notes she has made progress on her Python goal. He wants to update her 'Python for clinical-analytics' goal to 40% progress and append the note: 'Basic Python syntax mastered. Next step: data visualization.' He also wants to reactivate their mentorship to focus on 'Tableau' and 'Data-Viz Best Practices'. To support this, enroll Ava in the 'Data Visualization with Tableau' course. Finally, schedule their next mentorship session for October 31, 2025.",
        actions=[
            Action(
                name="get_user_id_from_name",
                kwargs={"first_name": "Jack", "last_name": "Wang"},
            ),
            Action(
                name="get_user_id_from_name",
                kwargs={"first_name": "Ava", "last_name": "Nguyen"},
            ),
            Action(name="list_user_goals", kwargs={"user_id": "U302"}),
            Action(name="list_user_mentorships", kwargs={"user_id": "U302"}),
            Action(
                name="get_course_id_by_name",
                kwargs={"course_name": "Data Visualization with Tableau"},
            ),
            Action(name="get_today_date", kwargs={}),
            Action(
                name="update_goal",
                kwargs={
                    "user_id": "U302",
                    "goal_id": "G302-1",
                    "progress_percent": 40,
                    "notes_to_append": "Basic Python syntax mastered. Next step: data visualization.",
                    "last_updated_date": "2025-10-02",
                },
            ),
            Action(
                name="update_mentorship_relationship",
                kwargs={
                    "relationship_id": "MR008",
                    "updates": {
                        "status": "Active",
                        "focus_areas": ["Tableau", "Data-Viz Best Practices"],
                    },
                },
            ),
            Action(
                name="enroll_in_course",
                kwargs={
                    "user_id": "U302",
                    "course_id": "C1003",
                    "enroll_date": "2025-10-02",
                },
            ),
            Action(
                name="schedule_mentorship_session",
                kwargs={"relationship_id": "MR008", "session_date": "2025-10-31"},
            ),
        ],
        outputs=[
            "Goal G302-1 updated for user U302",
            "relationship MR008 updated",
            "User U302 enrolled in course C1003",
            "scheduled_for: 2025-10-31",
        ],
    ),
    # 33
    Task(
        annotator="0",
        user_id="res_103",
        instruction="Advance application APP001 (Ava Nguyen, U302) for Senior Data Scientist position (J001) with Machine Learning skill development plan, EXT001 candidate shortlisting and Data Visualization training, and interview scheduling for both APP001 and APP003.",
        actions=[
            Action(name="get_job_posting", kwargs={"job_id": "J001"}),
            Action(name="get_role_skills", kwargs={"role": "Senior Data Scientist"}),
            Action(name="get_job_applications", kwargs={"job_id": "J001"}),
            Action(
                name="analyze_applicant_skill_fit",
                kwargs={"applicant_id": "U302", "role": "Senior Data Scientist"},
            ),
            Action(
                name="search_external_candidates_by_skills",
                kwargs={
                    "required_skills": [
                        "Machine Learning",
                        "Programming Languages",
                        "Data Visualization",
                    ]
                },
            ),
            Action(
                name="analyze_external_candidate_skill_fit",
                kwargs={"candidate_id": "EXT001", "role": "Senior Data Scientist"},
            ),
            Action(
                name="shortlist_external_candidate",
                kwargs={"candidate_id": "EXT001", "job_id": "J001"},
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "U302", "skill": "Machine Learning"},
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "EXT001", "skill": "Data Visualization"},
            ),
            Action(
                name="update_application_status",
                kwargs={"application_id": "APP001", "new_status": "Skill-Plan-Active"},
            ),
            Action(
                name="schedule_technical_interview", kwargs={"application_id": "APP001"}
            ),
            Action(
                name="schedule_technical_interview", kwargs={"application_id": "APP003"}
            ),
        ],
        outputs=[
            "EXT001 shortlisted",
            "U302 needs Machine Learning training",
            "EXT001 needs Data Visualization training",
            "APP001 Skill-Plan-Active",
            "Interview scheduled for APP001",
            "Interview scheduled for APP003",
        ],
    ),
    # 34
    Task(
        annotator="0",
        user_id="res_104",
        instruction="Verify and advance application APP010 (external candidate EXT006) for Security Analyst position (J005) to primary candidate status with skill development recommendations, shortlisting, and technical interview scheduling.",
        actions=[
            Action(name="get_job_applications", kwargs={"job_id": "J005"}),
            Action(name="get_job_posting", kwargs={"job_id": "J005"}),
            Action(name="get_role_skills", kwargs={"role": "Security Analyst"}),
            Action(
                name="analyze_external_candidate_skill_fit",
                kwargs={"candidate_id": "EXT006", "role": "Security Analyst"},
            ),
            Action(
                name="search_external_candidates_by_skills",
                kwargs={"required_skills": ["Cloud Security", "Compliance"]},
            ),
            Action(
                name="shortlist_external_candidate",
                kwargs={"candidate_id": "EXT006", "job_id": "J005"},
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "EXT006", "skill": "Cloud Security"},
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "EXT006", "skill": "Compliance"},
            ),
            Action(
                name="update_application_status",
                kwargs={"application_id": "APP010", "new_status": "Primary-Candidate"},
            ),
            Action(
                name="schedule_technical_interview", kwargs={"application_id": "APP010"}
            ),
        ],
        outputs=[
            "EXT006 shortlisted",
            "EXT006 needs Cloud Security training",
            "EXT006 needs Compliance training",
            "APP010 Primary-Candidate",
            "Interview scheduled for APP010",
        ],
    ),
    # 35
    Task(
        annotator="0",
        user_id="res_105",
        instruction="Execute comprehensive UX Designer position (J002) candidate advancement through external candidate pipeline optimization, conduct skill assessments for EXT003, implement targeted Design Thinking and Accessibility training programs, advance through Portfolio-Review to Technical-Assessment status, and coordinate technical interview scheduling.",
        actions=[
            Action(name="get_job_posting", kwargs={"job_id": "J002"}),
            Action(name="get_role_skills", kwargs={"role": "UX Designer"}),
            Action(name="get_job_applications", kwargs={"job_id": "J002"}),
            Action(
                name="analyze_external_candidate_skill_fit",
                kwargs={"candidate_id": "EXT003", "role": "UX Designer"},
            ),
            Action(
                name="shortlist_external_candidate",
                kwargs={"candidate_id": "EXT003", "job_id": "J002"},
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "EXT003", "skill": "Design Thinking"},
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "EXT003", "skill": "Accessibility"},
            ),
            Action(
                name="update_application_status",
                kwargs={"application_id": "APP006", "new_status": "Portfolio-Review"},
            ),
            Action(
                name="update_application_status",
                kwargs={
                    "application_id": "APP006",
                    "new_status": "Technical-Assessment",
                },
            ),
            Action(
                name="schedule_technical_interview", kwargs={"application_id": "APP006"}
            ),
        ],
        outputs=[
            "EXT003 shortlisted",
            "EXT003 needs Design Thinking training",
            "EXT003 needs Accessibility training",
            "APP006 Portfolio-Review",
            "APP006 Technical-Assessment",
            "Interview scheduled for APP006",
        ],
    ),
    # 36
    Task(
        annotator="0",
        user_id="res_106",
        instruction="Advance application APP007 (candidate U306) for DevOps Engineer position (J003) to offer finalization status with technical interview scheduling, Monitoring & Logging skill enhancement, and backup candidate EXT004 identification and shortlisting.",
        actions=[
            Action(name="get_job_posting", kwargs={"job_id": "J003"}),
            Action(name="get_role_skills", kwargs={"role": "DevOps Engineer"}),
            Action(name="get_job_applications", kwargs={"job_id": "J003"}),
            Action(
                name="analyze_applicant_skill_fit",
                kwargs={"applicant_id": "U306", "role": "DevOps Engineer"},
            ),
            Action(
                name="analyze_external_candidate_skill_fit",
                kwargs={"candidate_id": "EXT004", "role": "DevOps Engineer"},
            ),
            Action(
                name="update_application_status",
                kwargs={"application_id": "APP007", "new_status": "Offer-Finalization"},
            ),
            Action(
                name="schedule_technical_interview", kwargs={"application_id": "APP007"}
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "U306", "skill": "Monitoring & Logging"},
            ),
            Action(
                name="shortlist_external_candidate",
                kwargs={"candidate_id": "EXT004", "job_id": "J003"},
            ),
        ],
        outputs=[
            "APP007 Offer-Finalization",
            "Interview scheduled for APP007",
            "U306 needs Monitoring & Logging training",
            "EXT004 shortlisted",
        ],
    ),
    # 37
    Task(
        annotator="0",
        user_id="res_107",
        instruction="Process Marketing Specialist position (J004) by verifying applications, conducting skill assessment for candidate EXT005, expanding candidate pool through Product Marketing skill search and EXT005 shortlisting, implementing targeted Product Marketing and Brand Strategy training programs, and updating application records to reflect skill development progress.",
        actions=[
            Action(name="get_job_applications", kwargs={"job_id": "J004"}),
            Action(name="get_role_skills", kwargs={"role": "Marketing Specialist"}),
            Action(name="get_job_posting", kwargs={"job_id": "J004"}),
            Action(
                name="analyze_external_candidate_skill_fit",
                kwargs={"candidate_id": "EXT005", "role": "Marketing Specialist"},
            ),
            Action(
                name="search_external_candidates_by_skills",
                kwargs={"required_skills": ["Product Marketing"]},
            ),
            Action(
                name="shortlist_external_candidate",
                kwargs={"candidate_id": "EXT005", "job_id": "J004"},
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "EXT005", "skill": "Product Marketing"},
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "EXT005", "skill": "Brand Strategy"},
            ),
            Action(
                name="update_application_status",
                kwargs={"application_id": "APP009", "new_status": "Skills-Enhanced"},
            ),
            Action(
                name="update_application_status",
                kwargs={"application_id": "APP009", "new_status": "Pipeline-Expanded"},
            ),
            Action(
                name="schedule_technical_interview", kwargs={"application_id": "APP009"}
            ),
        ],
        outputs=[
            "EXT005 shortlisted",
            "EXT005 needs Product Marketing training",
            "EXT005 needs Brand Strategy training",
            "APP009 Skills-Enhanced",
            "APP009 Pipeline-Expanded",
            "Interview scheduled for APP009",
        ],
    ),
    # 38
    Task(
        annotator="0",
        user_id="res_108",
        instruction="Advance application APP005 (Chloe Scott, U307) for UX Designer position (J002) through comprehensive skill assessment, leadership development training implementation, and portfolio review stage advancement with technical interview scheduling.",
        actions=[
            Action(name="get_job_posting", kwargs={"job_id": "J002"}),
            Action(name="get_role_skills", kwargs={"role": "UX Designer"}),
            Action(name="get_job_applications", kwargs={"job_id": "J002"}),
            Action(
                name="analyze_applicant_skill_fit",
                kwargs={"applicant_id": "U307", "role": "UX Designer"},
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "U307", "skill": "Leadership"},
            ),
            Action(
                name="update_application_status",
                kwargs={
                    "application_id": "APP005",
                    "new_status": "Leadership-Enhanced",
                },
            ),
            Action(
                name="update_application_status",
                kwargs={"application_id": "APP005", "new_status": "Portfolio-Review"},
            ),
            Action(
                name="schedule_technical_interview", kwargs={"application_id": "APP005"}
            ),
        ],
        outputs=[
            "U307 needs Leadership training",
            "APP005 Leadership-Enhanced",
            "APP005 Portfolio-Review",
            "Interview scheduled for APP005",
        ],
    ),
    # 39
    Task(
        annotator="0",
        user_id="res_109",
        instruction="Expand Senior Data Scientist position (J001) candidate pipeline by identifying Machine Learning and SQL experts, shortlisting candidates EXT001 and EXT002, and establishing targeted Machine Learning and SQL training programs for EXT002.",
        actions=[
            Action(name="get_role_skills", kwargs={"role": "Senior Data Scientist"}),
            Action(name="get_job_posting", kwargs={"job_id": "J001"}),
            Action(name="get_job_applications", kwargs={"job_id": "J001"}),
            Action(
                name="search_external_candidates_by_skills",
                kwargs={"required_skills": ["Machine Learning", "SQL"]},
            ),
            Action(
                name="shortlist_external_candidate",
                kwargs={"candidate_id": "EXT001", "job_id": "J001"},
            ),
            Action(
                name="shortlist_external_candidate",
                kwargs={"candidate_id": "EXT002", "job_id": "J001"},
            ),
            Action(
                name="analyze_external_candidate_skill_fit",
                kwargs={"candidate_id": "EXT002", "role": "Senior Data Scientist"},
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "EXT002", "skill": "Machine Learning"},
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "EXT002", "skill": "SQL"},
            ),
        ],
        outputs=[
            "EXT001 shortlisted",
            "EXT002 shortlisted",
            "EXT002 needs Machine Learning training",
            "EXT002 needs SQL training",
        ],
    ),
    # 40
    Task(
        annotator="0",
        user_id="res_111",
        instruction="Process DevOps Engineer position (J003) by verifying applications, conducting skill assessments for internal candidate U306 and external candidate EXT004, implementing Infrastructure as Code training for U306 and comprehensive CI/CD and Monitoring & Logging training for EXT004, shortlisting EXT004, updating APP007 to Training-Complete status, and scheduling technical interview.",
        actions=[
            Action(name="get_job_applications", kwargs={"job_id": "J003"}),
            Action(name="get_job_posting", kwargs={"job_id": "J003"}),
            Action(name="get_role_skills", kwargs={"role": "DevOps Engineer"}),
            Action(
                name="analyze_applicant_skill_fit",
                kwargs={"applicant_id": "U306", "role": "DevOps Engineer"},
            ),
            Action(
                name="analyze_external_candidate_skill_fit",
                kwargs={"candidate_id": "EXT004", "role": "DevOps Engineer"},
            ),
            Action(
                name="shortlist_external_candidate",
                kwargs={"candidate_id": "EXT004", "job_id": "J003"},
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "U306", "skill": "Infrastructure as Code"},
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "EXT004", "skill": "CI/CD"},
            ),
            Action(
                name="recommend_skill_training",
                kwargs={"user_id": "EXT004", "skill": "Monitoring & Logging"},
            ),
            Action(
                name="update_application_status",
                kwargs={"application_id": "APP007", "new_status": "Training-Complete"},
            ),
            Action(
                name="schedule_technical_interview", kwargs={"application_id": "APP007"}
            ),
        ],
        outputs=[
            "EXT004 shortlisted",
            "U306 needs Infrastructure as Code training",
            "EXT004 needs CI/CD training",
            "EXT004 needs Monitoring & Logging training",
            "APP007 Training-Complete",
            "Interview scheduled for APP007",
        ],
    ),
]
