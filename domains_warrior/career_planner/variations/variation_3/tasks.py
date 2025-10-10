from domains.dto import Task, Action

TASKS = [
    # 1
    Task(
        annotator="0",
        user_id="res_101",
        instruction="""Alexander Adams needs a comprehensive succession plan established for the Backend Tech Lead role. Identify the most qualified candidate from the Engineering Team (T003)""",
        actions=[
            Action(name="get_team_members", kwargs={"team_id": "T003"}),
            Action(
                name="get_users_with_leadership_goals",
                kwargs={"user_ids": ["U306", "U312"]},
            ),
            Action(
                name="validate_user_goal_alignment",
                kwargs={"user_id": "U306", "target_role": "Backend Tech Lead"},
            ),
            Action(
                name="validate_user_goal_alignment",
                kwargs={"user_id": "U312", "target_role": "Backend Tech Lead"},
            ),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U312", "target_role": "Backend Tech Lead"},
            ),
            Action(
                name="check_training_needed",
                kwargs={"user_id": "U312", "target_role": "Backend Tech Lead"},
            ),
            Action(
                name="recommend_course_for_gap",
                kwargs={"user_id": "U312", "target_role": "Backend Tech Lead"},
            ),
            Action(
                name="assign_course_to_user",
                kwargs={
                    "user_id": "U312",
                    "course_id": "C1004",
                },
            ),
            Action(
                name="shortlist_successor_candidate",
                kwargs={
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead",
                },
            ),
        ],
        outputs=["Course assigned to user.", "Candidate shortlisted."],
    ),
    # 2
    Task(
        annotator="0",
        user_id="res_102",
        instruction="Accelerate David Adams's (U304) career advancement to DesignOps Lead by performing a comprehensive readiness assessment and formally establishing his succession pathway.",
        actions=[
            Action(
                name="validate_user_goal_alignment",
                kwargs={"user_id": "U304", "target_role": "DesignOps Lead"},
            ),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U304", "target_role": "DesignOps Lead"},
            ),
            Action(
                name="check_training_needed",
                kwargs={"user_id": "U304", "target_role": "DesignOps Lead"},
            ),
            Action(
                name="assess_soft_skill_alignment",
                kwargs={"user_id": "U304", "target_role": "DesignOps Lead"},
            ),
            Action(
                name="shortlist_successor_candidate",
                kwargs={
                    "user_id": "U304",
                    "target_role": "DesignOps Lead",
                },
            ),
        ],
        outputs=[],
    ),
    # 3
    Task(
        annotator="0",
        user_id="res_103",
        instruction="Jack Wang, the lead of the Data Analytics Team (T001), needs a successor promotion pipeline established for Clinical Analytics Lead with team analysis, leadership identification, and qualified candidate preparation.",
        actions=[
            Action(name="get_team_members", kwargs={"team_id": "T001"}),
            Action(
                name="get_users_with_leadership_goals",
                kwargs={"user_ids": ["U301", "U302"]},
            ),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U301", "target_role": "Clinical Analytics Lead"},
            ),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U302", "target_role": "Clinical Analytics Lead"},
            ),
            Action(
                name="check_training_needed",
                kwargs={"user_id": "U302", "target_role": "Clinical Analytics Lead"},
            ),
            Action(
                name="recommend_course_for_gap",
                kwargs={"user_id": "U302", "target_role": "Clinical Analytics Lead"},
            ),
            Action(
                name="assign_course_to_user",
                kwargs={"user_id": "U302", "course_id": "C1001"},
            ),
            Action(
                name="shortlist_successor_candidate",
                kwargs={
                    "user_id": "U302",
                    "target_role": "Clinical Analytics Lead",
                },
            ),
        ],
        outputs=["Course assigned to user.", "Candidate shortlisted."],
    ),
    # 4
    Task(
        annotator="0",
        user_id="res_104",
        instruction="As the manager of the Product Design Team (T002), I need to identify potential leaders. For David Adams (U304), perform a comprehensive readiness assessment for the DesignOps Lead role and, if he is a suitable candidate, formally shortlist him for succession.",
        actions=[
            Action(
                name="get_team_members",
                kwargs={"team_id": "T002"},
            ),
            Action(
                name="get_users_with_leadership_goals",
                kwargs={"user_ids": ["U304", "U307"]},
            ),
            Action(
                name="validate_user_goal_alignment",
                kwargs={"user_id": "U304", "target_role": "DesignOps Lead"},
            ),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U304", "target_role": "DesignOps Lead"},
            ),
            Action(
                name="assess_soft_skill_alignment",
                kwargs={"user_id": "U304", "target_role": "DesignOps Lead"},
            ),
            Action(
                name="check_training_needed",
                kwargs={"user_id": "U304", "target_role": "DesignOps Lead"},
            ),
            Action(
                name="shortlist_successor_candidate",
                kwargs={
                    "user_id": "U304",
                    "target_role": "DesignOps Lead",
                },
            ),
        ],
        outputs=[],
    ),
    # 5
    Task(
        annotator="0",
        user_id="res_105",
        instruction="Perform a comprehensive readiness assessment for Harper Bennett for the People Analytics Lead role, including goal alignment and skill gaps. Attempt to assign a validated course for her highest-priority skill gap. Conclude by formally tracking her candidacy by shortlisting her for the role.",
        actions=[
            Action(name="get_user_id", kwargs={"user_name": "Harper Bennett"}),
            Action(
                name="validate_user_goal_alignment",
                kwargs={"user_id": "U310", "target_role": "People Analytics Lead"},
            ),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U310", "target_role": "People Analytics Lead"},
            ),
            Action(
                name="assess_soft_skill_alignment",
                kwargs={"user_id": "U310", "target_role": "People Analytics Lead"},
            ),
            Action(
                name="check_training_needed",
                kwargs={"user_id": "U310", "target_role": "People Analytics Lead"},
            ),
            Action(
                name="recommend_course_for_gap",
                kwargs={"user_id": "U310", "target_role": "People Analytics Lead"},
            ),
            Action(
                name="validate_course_skill_mapping",
                kwargs={"course_id": "C1005", "skill_name": "Statistical Modeling"},
            ),
            Action(
                name="shortlist_successor_candidate",
                kwargs={
                    "user_id": "U310",
                    "target_role": "People Analytics Lead",
                },
            ),
        ],
        outputs=[],
    ),
    # 6
    Task(
        annotator="0",
        user_id="res_106",
        instruction="Position David Adams (U304) for the DesignOps Lead role. Perform a comprehensive assessment of his goal alignment and skill gaps, then prepare him for the role by assigning targeted training and shortlisting him for succession.",
        actions=[
            Action(
                name="validate_user_goal_alignment",
                kwargs={"user_id": "U304", "target_role": "DesignOps Lead"},
            ),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U304", "target_role": "DesignOps Lead"},
            ),
            Action(
                name="assess_soft_skill_alignment",
                kwargs={"user_id": "U304", "target_role": "DesignOps Lead"},
            ),
            Action(
                name="recommend_course_for_gap",
                kwargs={"user_id": "U304", "target_role": "DesignOps Lead"},
            ),
            Action(
                name="assign_course_to_user",
                kwargs={"user_id": "U304", "course_id": "C1004"},
            ),
            Action(
                name="shortlist_successor_candidate",
                kwargs={
                    "user_id": "U304",
                    "target_role": "DesignOps Lead",
                },
            ),
        ],
        outputs=["Course assigned to user.", "Candidate shortlisted."],
    ),
    # 7
    Task(
        annotator="0",
        user_id="res_107",
        instruction="Launch a leadership development initiative for the Engineering Team (T003). First, identify all team members with formal leadership goals. For each of these candidates, perform a comprehensive readiness assessment for their respective target role. If training is needed and a valid course exists, assign it. Conclude by formally shortlisting each candidate for their target role.",
        actions=[
            Action(name="get_team_members", kwargs={"team_id": "T003"}),
            Action(
                name="get_users_with_leadership_goals",
                kwargs={"user_ids": ["U306", "U312"]},
            ),
            # --- Process Alexander Adams (U306) ---
            Action(name="get_user_goals", kwargs={"user_id": "U306"}),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U306", "target_role": "Staff SRE"},
            ),
            Action(
                name="check_training_needed",
                kwargs={"user_id": "U306", "target_role": "Staff SRE"},
            ),
            Action(
                name="shortlist_successor_candidate",
                kwargs={
                    "user_id": "U306",
                    "target_role": "Staff SRE",
                    "succession_for_role": "DevOps Engineer",
                },
            ),
            # --- Process Mason Desai (U312) ---
            Action(name="get_user_goals", kwargs={"user_id": "U312"}),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U312", "target_role": "Backend Tech Lead"},
            ),
            Action(
                name="check_training_needed",
                kwargs={"user_id": "U312", "target_role": "Backend Tech Lead"},
            ),
            Action(
                name="recommend_course_for_gap",
                kwargs={"user_id": "U312", "target_role": "Backend Tech Lead"},
            ),
            Action(
                name="validate_course_skill_mapping",
                kwargs={"course_id": "C1004", "skill_name": "Team Leadership"},
            ),
            Action(
                name="shortlist_successor_candidate",
                kwargs={
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead",
                    "succession_for_role": "Software Engineer",
                },
            ),
        ],
        outputs=[],
    ),
    # 8
    Task(
        annotator="0",
        user_id="res_108",
        instruction="Launch a skill development initiative for the Data Analytics Team (T001). For each team member (Jack Wang and Ava Nguyen), identify their formal target role. If a target role exists, perform a comprehensive readiness assessment and shortlist them. If training is needed for any of their goals and a valid course exists, assign it.",
        actions=[
            Action(name="get_user_id", kwargs={"user_name": "Jack Wang"}),
            Action(name="get_user_id", kwargs={"user_name": "Ava Nguyen"}),
            # --- Process Jack Wang (U301) ---
            Action(name="get_user_target_role", kwargs={"user_id": "U301"}),
            Action(name="get_user_profile", kwargs={"user_id": "U301"}),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U301", "target_role": "Director of Data Science"},
            ),
            Action(
                name="check_training_needed",
                kwargs={"user_id": "U301", "target_role": "Director of Data Science"},
            ),
            Action(
                name="recommend_course_for_gap",
                kwargs={"user_id": "U301", "target_role": "Director of Data Science"},
            ),
            Action(
                name="validate_course_skill_mapping",
                kwargs={"course_id": "C1005", "skill_name": "Machine Learning"},
            ),
            Action(
                name="log_team_training",
                kwargs={
                    "user_id": "U301",
                    "skill_name": "Machine Learning",
                    "course_id": "C1005",
                },
            ),
            Action(
                name="assign_course_to_user",
                kwargs={"user_id": "U301", "course_id": "C1005"},
            ),
            Action(
                name="shortlist_successor_candidate",
                kwargs={
                    "user_id": "U301",
                    "target_role": "Director of Data Science",
                    "succession_for_role": "Analytics Manager",
                },
            ),
            # --- Process Ava Nguyen (U302) ---
            Action(name="get_user_target_role", kwargs={"user_id": "U302"}),
        ],
        outputs=[],
    ),
    # 9
    Task(
        annotator="0",
        user_id="res_109",
        instruction="For each member of the Engineering Team (T003), perform a readiness assessment. If a member requires training, recommend and assign a validated course for their highest-priority skill gap.",
        actions=[
            Action(name="get_team_members", kwargs={"team_id": "T003"}),
            # --- Process Alexander Adams (U306) ---
            Action(name="get_user_goals", kwargs={"user_id": "U306"}),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U306", "target_role": "Staff SRE"},
            ),
            Action(
                name="check_training_needed",
                kwargs={"user_id": "U306", "target_role": "Staff SRE"},
            ),
            # --- Process Mason Desai (U312) ---
            Action(name="get_user_goals", kwargs={"user_id": "U312"}),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U312", "target_role": "Backend Tech Lead"},
            ),
            Action(
                name="check_training_needed",
                kwargs={"user_id": "U312", "target_role": "Backend Tech Lead"},
            ),
            Action(
                name="recommend_course_for_gap",
                kwargs={"user_id": "U312", "target_role": "Backend Tech Lead"},
            ),
            Action(
                name="validate_course_skill_mapping",
                kwargs={"course_id": "C1004", "skill_name": "Team Leadership"},
            ),
        ],
        outputs=[],
    ),
    # 10
    Task(
        annotator="0",
        user_id="res_110",
        instruction="Launch a leadership development initiative for the Engineering Team (T003). Identify all team members with formal leadership goals. For each of these candidates, perform a comprehensive readiness assessment for their respective target role. If training is needed and a valid course exists, assign it. Conclude by formally shortlisting each candidate for their target role.",
        actions=[
            Action(name="get_team_members", kwargs={"team_id": "T003"}),
            Action(
                name="get_users_with_leadership_goals",
                kwargs={"user_ids": ["U306", "U312"]},
            ),
            # --- Process Alexander Adams (U306) ---
            Action(name="get_user_goals", kwargs={"user_id": "U306"}),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U306", "target_role": "Staff SRE"},
            ),
            Action(
                name="check_training_needed",
                kwargs={"user_id": "U306", "target_role": "Staff SRE"},
            ),
            Action(
                name="shortlist_successor_candidate",
                kwargs={
                    "user_id": "U306",
                    "target_role": "Staff SRE",
                    "succession_for_role": "DevOps Engineer",
                },
            ),
            # --- Process Mason Desai (U312) ---
            Action(name="get_user_goals", kwargs={"user_id": "U312"}),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U312", "target_role": "Backend Tech Lead"},
            ),
            Action(
                name="check_training_needed",
                kwargs={"user_id": "U312", "target_role": "Backend Tech Lead"},
            ),
            Action(
                name="recommend_course_for_gap",
                kwargs={"user_id": "U312", "target_role": "Backend Tech Lead"},
            ),
            Action(
                name="validate_course_skill_mapping",
                kwargs={"course_id": "C1004", "skill_name": "Team Leadership"},
            ),
            Action(
                name="shortlist_successor_candidate",
                kwargs={
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead",
                    "succession_for_role": "Software Engineer",
                },
            ),
        ],
        outputs=[],
    ),
    # 11 - ENHANCED COMPLEXITY: Added team validation, goal alignment, and multi-step assessment
    Task(
        annotator="0",
        user_id="res_111",
        instruction="Create a comprehensive development plan for Jack Wang to become Director of Data Science. The plan must include goal alignment validation, skill gap analysis, a check for training needs, assignment of a validated course, and formal shortlisting for the role.",
        actions=[
            Action(name="get_user_id", kwargs={"user_name": "Jack Wang"}),
            Action(
                name="validate_user_goal_alignment",
                kwargs={"user_id": "U301", "target_role": "Director of Data Science"},
            ),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U301", "target_role": "Director of Data Science"},
            ),
            Action(
                name="check_training_needed",
                kwargs={"user_id": "U301", "target_role": "Director of Data Science"},
            ),
            Action(
                name="recommend_course_for_gap",
                kwargs={"user_id": "U301", "target_role": "Director of Data Science"},
            ),
            Action(
                name="validate_course_skill_mapping",
                kwargs={"course_id": "C1005", "skill_name": "Machine Learning"},
            ),
            Action(
                name="log_team_training",
                kwargs={
                    "user_id": "U301",
                    "skill_name": "Machine Learning",
                    "course_id": "C1005",
                },
            ),
            Action(
                name="assign_course_to_user",
                kwargs={"user_id": "U301", "course_id": "C1005"},
            ),
            Action(
                name="shortlist_successor_candidate",
                kwargs={
                    "user_id": "U301",
                    "target_role": "Director of Data Science",
                },
            ),
        ],
        outputs=[],
    ),
    # 12 - ENHANCED COMPLEXITY: Added comprehensive validation and assessment workflow
    Task(
        annotator="0",
        user_id="res_112",
        instruction="Create a comprehensive readiness plan for David Adams (U304) to transition to the DesignOps Lead role. Validate his alignment, assess his technical and soft skill gaps, assign suitable training, and formally track his candidacy.",
        actions=[
            Action(
                name="validate_user_goal_alignment",
                kwargs={"user_id": "U304", "target_role": "DesignOps Lead"},
            ),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U304", "target_role": "DesignOps Lead"},
            ),
            Action(
                name="assess_soft_skill_alignment",
                kwargs={"user_id": "U304", "target_role": "DesignOps Lead"},
            ),
            Action(
                name="recommend_course_for_gap",
                kwargs={"user_id": "U304", "target_role": "DesignOps Lead"},
            ),
            Action(
                name="assign_course_to_user",
                kwargs={"user_id": "U304", "course_id": "C1004"},
            ),
            Action(
                name="shortlist_successor_candidate",
                kwargs={
                    "user_id": "U304",
                    "target_role": "DesignOps Lead",
                },
            ),
        ],
        outputs=["Candidate shortlisted."],
    ),
    # 13 - ENHANCED COMPLEXITY: Added comprehensive team analysis and multi-user assessment
    Task(
        annotator="0",
        user_id="res_113",
        instruction="Create a comprehensive development plan for Jack Wang to transition to Director of Data Science. The plan must validate his readiness, assign validated training for his skill gaps, and formally shortlist him for the role.",
        actions=[
            Action(name="get_user_id", kwargs={"user_name": "Jack Wang"}),
            Action(
                name="validate_user_goal_alignment",
                kwargs={"user_id": "U301", "target_role": "Director of Data Science"},
            ),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U301", "target_role": "Director of Data Science"},
            ),
            Action(
                name="check_training_needed",
                kwargs={"user_id": "U301", "target_role": "Director of Data Science"},
            ),
            Action(
                name="recommend_course_for_gap",
                kwargs={"user_id": "U301", "target_role": "Director of Data Science"},
            ),
            Action(
                name="validate_course_skill_mapping",
                kwargs={"course_id": "C1005", "skill_name": "Machine Learning"},
            ),
            Action(
                name="log_team_training",
                kwargs={
                    "user_id": "U301",
                    "skill_name": "Machine Learning",
                    "course_id": "C1005",
                },
            ),
            Action(
                name="assign_course_to_user",
                kwargs={"user_id": "U301", "course_id": "C1005"},
            ),
            Action(
                name="shortlist_successor_candidate",
                kwargs={
                    "user_id": "U301",
                    "target_role": "Director of Data Science",
                },
            ),
        ],
        outputs=[],
    ),
    # 14 - ENHANCED COMPLEXITY: Added comprehensive design team analysis and multi-step assessment
    Task(
        annotator="0",
        user_id="res_114",
        instruction="Establish a comprehensive DesignOps leadership development plan for David Adams. The plan must include goal alignment validation, skill gap assessment, and formal succession planning.",
        actions=[
            Action(name="get_user_id", kwargs={"user_name": "David Adams"}),
            Action(
                name="validate_user_goal_alignment",
                kwargs={"user_id": "U304", "target_role": "DesignOps Lead"},
            ),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U304", "target_role": "DesignOps Lead"},
            ),
            Action(
                name="assess_soft_skill_alignment",
                kwargs={"user_id": "U304", "target_role": "DesignOps Lead"},
            ),
            Action(
                name="check_training_needed",
                kwargs={"user_id": "U304", "target_role": "DesignOps Lead"},
            ),
            Action(
                name="shortlist_successor_candidate",
                kwargs={
                    "user_id": "U304",
                    "target_role": "DesignOps Lead",
                },
            ),
        ],
        outputs=[],
    ),
    # 15 - ENHANCED COMPLEXITY: Added comprehensive engineering team analysis and multi-step assessment
    Task(
        annotator="0",
        user_id="res_115",
        instruction="Perform a comprehensive readiness assessment for Mason Desai for the Backend Tech Lead role by validating his goals and analyzing his skill gaps. After attempting to find a valid training course, conclude the process by using the shortlisting him to formally record his development pathway.",
        actions=[
            Action(name="get_user_id", kwargs={"user_name": "Mason Desai"}),
            Action(
                name="validate_user_goal_alignment",
                kwargs={"user_id": "U312", "target_role": "Backend Tech Lead"},
            ),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U312", "target_role": "Backend Tech Lead"},
            ),
            Action(
                name="assess_soft_skill_alignment",
                kwargs={"user_id": "U312", "target_role": "Backend Tech Lead"},
            ),
            Action(
                name="check_training_needed",
                kwargs={"user_id": "U312", "target_role": "Backend Tech Lead"},
            ),
            Action(
                name="recommend_course_for_gap",
                kwargs={"user_id": "U312", "target_role": "Backend Tech Lead"},
            ),
            Action(
                name="validate_course_skill_mapping",
                kwargs={"course_id": "C1004", "skill_name": "Team Leadership"},
            ),
            Action(
                name="shortlist_successor_candidate",
                kwargs={
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead",
                },
            ),
        ],
        outputs=[],
    ),
    # 16 - ENHANCED COMPLEXITY: Added comprehensive HR analytics assessment and multi-step process
    Task(
        annotator="0",
        user_id="res_116",
        instruction="Perform a comprehensive readiness assessment for Henry Hassan's transition to UX Writer by validating his goal alignment and skill gaps. Conclude the process by formalizing his candidacy for the role by shortlisting him.",
        actions=[
            Action(name="get_user_id", kwargs={"user_name": "Henry Hassan"}),
            Action(
                name="validate_user_goal_alignment",
                kwargs={"user_id": "U308", "target_role": "UX Writer"},
            ),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U308", "target_role": "UX Writer"},
            ),
            Action(
                name="assess_soft_skill_alignment",
                kwargs={"user_id": "U308", "target_role": "UX Writer"},
            ),
            Action(
                name="check_training_needed",
                kwargs={"user_id": "U308", "target_role": "UX Writer"},
            ),
            Action(
                name="shortlist_successor_candidate",
                kwargs={
                    "user_id": "U308",
                    "target_role": "UX Writer",
                },
            ),
        ],
        outputs=[],
    ),
    # 17 - ENHANCED COMPLEXITY: Added comprehensive cross-team mentorship assessment
    Task(
        annotator="0",
        user_id="res_117",
        instruction="Perform a comprehensive readiness assessment for Harper Bennett's transition to People Analytics Lead by validating her goal alignment and skill gaps. Attempt to find and validate a suitable training course. Conclude the process by formally shortlisting her for the role.",
        actions=[
            Action(name="get_user_id", kwargs={"user_name": "Harper Bennett"}),
            Action(
                name="validate_user_goal_alignment",
                kwargs={"user_id": "U310", "target_role": "People Analytics Lead"},
            ),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U310", "target_role": "People Analytics Lead"},
            ),
            Action(
                name="assess_soft_skill_alignment",
                kwargs={"user_id": "U310", "target_role": "People Analytics Lead"},
            ),
            Action(
                name="check_training_needed",
                kwargs={"user_id": "U310", "target_role": "People Analytics Lead"},
            ),
            Action(
                name="recommend_course_for_gap",
                kwargs={"user_id": "U310", "target_role": "People Analytics Lead"},
            ),
            Action(
                name="validate_course_skill_mapping",
                kwargs={"course_id": "C1005", "skill_name": "Statistical Modeling"},
            ),
            Action(
                name="shortlist_successor_candidate",
                kwargs={
                    "user_id": "U310",
                    "target_role": "People Analytics Lead",
                },
            ),
        ],
        outputs=[],
    ),
    # 18 - ENHANCED COMPLEXITY: Added comprehensive data science team readiness program
    Task(
        annotator="0",
        user_id="res_118",
        instruction="Establish a comprehensive data-science readiness sprint for the Analytics Team (T001). For each member, validate their readiness for their documented target role, assign the highest-priority training, and establish a succession plan for the team's leadership.",
        actions=[
            Action(name="get_team_members", kwargs={"team_id": "T001"}),
            Action(
                name="validate_user_goal_alignment",
                kwargs={"user_id": "U301", "target_role": "Director of Data Science"},
            ),
            Action(
                name="check_training_needed",
                kwargs={"user_id": "U301", "target_role": "Director of Data Science"},
            ),
            Action(
                name="recommend_course_for_gap",
                kwargs={"user_id": "U301", "target_role": "Director of Data Science"},
            ),
            Action(
                name="assign_course_to_user",
                kwargs={"user_id": "U301", "course_id": "C1005"},
            ),
            Action(
                name="validate_user_goal_alignment",
                kwargs={"user_id": "U302", "target_role": "Clinical Analytics Lead"},
            ),
            Action(
                name="check_training_needed",
                kwargs={"user_id": "U302", "target_role": "Clinical Analytics Lead"},
            ),
            Action(
                name="recommend_course_for_gap",
                kwargs={"user_id": "U302", "target_role": "Clinical Analytics Lead"},
            ),
            Action(
                name="assign_course_to_user",
                kwargs={"user_id": "U302", "course_id": "C1001"},
            ),
            Action(
                name="shortlist_successor_candidate",
                kwargs={
                    "user_id": "U302",
                    "target_role": "Clinical Analytics Lead",
                },
            ),
        ],
        outputs=["Course assigned to user.", "Candidate shortlisted."],
    ),
    # 19 - ENHANCED COMPLEXITY: Added comprehensive engineering succession planning
    Task(
        annotator="0",
        user_id="res_119",
        instruction="Create a comprehensive succession plan for the Engineering Team (T003). For the two members with leadership goals, Mason Desai (U312) and Alexander Adams (U306), validate their career goals, assign the highest-priority training to close their skill gaps, and formally shortlist them for their respective target roles.",
        actions=[
            Action(name="get_team_members", kwargs={"team_id": "T003"}),
            Action(
                name="get_users_with_leadership_goals",
                kwargs={"user_ids": ["U306", "U312"]},
            ),
            # --- Process Alexander Adams (U306) ---
            Action(name="get_user_goals", kwargs={"user_id": "U306"}),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U306", "target_role": "Staff SRE"},
            ),
            Action(
                name="check_training_needed",
                kwargs={"user_id": "U306", "target_role": "Staff SRE"},
            ),
            Action(
                name="shortlist_successor_candidate",
                kwargs={
                    "user_id": "U306",
                    "target_role": "Staff SRE",
                },
            ),
            # --- Process Mason Desai (U312) ---
            Action(name="get_user_goals", kwargs={"user_id": "U312"}),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U312", "target_role": "Backend Tech Lead"},
            ),
            Action(
                name="check_training_needed",
                kwargs={"user_id": "U312", "target_role": "Backend Tech Lead"},
            ),
            Action(
                name="recommend_course_for_gap",
                kwargs={"user_id": "U312", "target_role": "Backend Tech Lead"},
            ),
            Action(
                name="validate_course_skill_mapping",
                kwargs={"course_id": "C1004", "skill_name": "Team Leadership"},
            ),
            Action(
                name="shortlist_successor_candidate",
                kwargs={
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead",
                },
            ),
        ],
        outputs=[],
    ),
    # 20 - COMPLEX: Conditional skill assessment and targeted training
    Task(
        annotator="0",
        user_id="res_170",
        instruction="Prepare Jack Wang for the Director of Data Science role. Validate his career goals, assess his skill gaps, and assign a validated course to develop his machine learning capabilities.",
        actions=[
            Action(name="get_user_id", kwargs={"user_name": "Jack Wang"}),
            Action(
                name="validate_user_goal_alignment",
                kwargs={"user_id": "U301", "target_role": "Director of Data Science"},
            ),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U301", "target_role": "Director of Data Science"},
            ),
            Action(
                name="check_training_needed",
                kwargs={"user_id": "U301", "target_role": "Director of Data Science"},
            ),
            Action(
                name="recommend_course_for_gap",
                kwargs={"user_id": "U301", "target_role": "Director of Data Science"},
            ),
            Action(
                name="validate_course_skill_mapping",
                kwargs={"course_id": "C1005", "skill_name": "Machine Learning"},
            ),
            Action(
                name="log_team_training",
                kwargs={
                    "user_id": "U301",
                    "skill_name": "Machine Learning",
                    "course_id": "C1005",
                },
            ),
            Action(
                name="assign_course_to_user",
                kwargs={"user_id": "U301", "course_id": "C1005"},
            ),
        ],
        outputs=[],
    ),
    # 21 - COMPLEX: Role transition with skill assessment
    Task(
        annotator="0",
        user_id="res_171",
        instruction="Launch a company-wide career transition initiative. For all employees with a 'Role Transition' goal (Jack Wang, David Adams, Harper King, Alexander Adams, Henry Hassan, Harper Bennett, and Mason Desai), first identify their formal target role and current role. Then, perform a comprehensive readiness assessment. If training is needed and a valid course exists, assign it. Conclude by formalizing each employee's transition plan by shortlisting them.",
        actions=[
            Action(name="get_user_id", kwargs={"user_name": "Jack Wang"}),
            Action(name="get_user_id", kwargs={"user_name": "David Adams"}),
            Action(name="get_user_id", kwargs={"user_name": "Harper King"}),
            Action(name="get_user_id", kwargs={"user_name": "Alexander Adams"}),
            Action(name="get_user_id", kwargs={"user_name": "Henry Hassan"}),
            Action(name="get_user_id", kwargs={"user_name": "Harper Bennett"}),
            Action(name="get_user_id", kwargs={"user_name": "Mason Desai"}),
            # --- Process Jack Wang (U301) ---
            Action(name="get_user_target_role", kwargs={"user_id": "U301"}),
            Action(name="get_user_profile", kwargs={"user_id": "U301"}),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U301", "target_role": "Director of Data Science"},
            ),
            Action(
                name="check_training_needed",
                kwargs={"user_id": "U301", "target_role": "Director of Data Science"},
            ),
            Action(
                name="recommend_course_for_gap",
                kwargs={"user_id": "U301", "target_role": "Director of Data Science"},
            ),
            Action(
                name="validate_course_skill_mapping",
                kwargs={"course_id": "C1005", "skill_name": "Machine Learning"},
            ),
            Action(
                name="log_team_training",
                kwargs={
                    "user_id": "U301",
                    "skill_name": "Machine Learning",
                    "course_id": "C1005",
                },
            ),
            Action(
                name="assign_course_to_user",
                kwargs={"user_id": "U301", "course_id": "C1005"},
            ),
            Action(
                name="shortlist_successor_candidate",
                kwargs={
                    "user_id": "U301",
                    "target_role": "Director of Data Science",
                    "succession_for_role": "Analytics Manager",
                },
            ),
            # --- Process David Adams (U304) ---
            Action(name="get_user_target_role", kwargs={"user_id": "U304"}),
            Action(name="get_user_profile", kwargs={"user_id": "U304"}),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U304", "target_role": "DesignOps Lead"},
            ),
            Action(
                name="check_training_needed",
                kwargs={"user_id": "U304", "target_role": "DesignOps Lead"},
            ),
            Action(
                name="shortlist_successor_candidate",
                kwargs={
                    "user_id": "U304",
                    "target_role": "DesignOps Lead",
                    "succession_for_role": "UX Designer",
                },
            ),
            # --- Process Harper King (U305) ---
            Action(name="get_user_target_role", kwargs={"user_id": "U305"}),
            Action(name="get_user_profile", kwargs={"user_id": "U305"}),
            Action(
                name="get_user_skill_gap",
                kwargs={
                    "user_id": "U305",
                    "target_role": "Product Marketing Specialist",
                },
            ),
            Action(
                name="check_training_needed",
                kwargs={
                    "user_id": "U305",
                    "target_role": "Product Marketing Specialist",
                },
            ),
            Action(
                name="recommend_course_for_gap",
                kwargs={
                    "user_id": "U305",
                    "target_role": "Product Marketing Specialist",
                },
            ),
            Action(
                name="validate_course_skill_mapping",
                kwargs={"course_id": "C1006", "skill_name": "Product Marketing"},
            ),
            Action(
                name="shortlist_successor_candidate",
                kwargs={
                    "user_id": "U305",
                    "target_role": "Product Marketing Specialist",
                    "succession_for_role": "Brand Strategist",
                },
            ),
            # --- Process Alexander Adams (U306) ---
            Action(name="get_user_target_role", kwargs={"user_id": "U306"}),
            Action(name="get_user_profile", kwargs={"user_id": "U306"}),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U306", "target_role": "Staff SRE"},
            ),
            Action(
                name="check_training_needed",
                kwargs={"user_id": "U306", "target_role": "Staff SRE"},
            ),
            Action(
                name="shortlist_successor_candidate",
                kwargs={
                    "user_id": "U306",
                    "target_role": "Staff SRE",
                    "succession_for_role": "DevOps Engineer",
                },
            ),
            # --- Process Henry Hassan (U308) ---
            Action(name="get_user_target_role", kwargs={"user_id": "U308"}),
            Action(name="get_user_profile", kwargs={"user_id": "U308"}),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U308", "target_role": "UX Writer"},
            ),
            Action(
                name="check_training_needed",
                kwargs={"user_id": "U308", "target_role": "UX Writer"},
            ),
            Action(
                name="shortlist_successor_candidate",
                kwargs={
                    "user_id": "U308",
                    "target_role": "UX Writer",
                    "succession_for_role": "Technical Writer",
                },
            ),
            # --- Process Harper Bennett (U310) ---
            Action(name="get_user_target_role", kwargs={"user_id": "U310"}),
            Action(name="get_user_profile", kwargs={"user_id": "U310"}),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U310", "target_role": "People Analytics Lead"},
            ),
            Action(
                name="check_training_needed",
                kwargs={"user_id": "U310", "target_role": "People Analytics Lead"},
            ),
            Action(
                name="recommend_course_for_gap",
                kwargs={"user_id": "U310", "target_role": "People Analytics Lead"},
            ),
            Action(
                name="validate_course_skill_mapping",
                kwargs={"course_id": "C1005", "skill_name": "Statistical Modeling"},
            ),
            Action(
                name="shortlist_successor_candidate",
                kwargs={
                    "user_id": "U310",
                    "target_role": "People Analytics Lead",
                    "succession_for_role": "HR Partner",
                },
            ),
            # --- Process Mason Desai (U312) ---
            Action(name="get_user_target_role", kwargs={"user_id": "U312"}),
            Action(name="get_user_profile", kwargs={"user_id": "U312"}),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U312", "target_role": "Backend Tech Lead"},
            ),
            Action(
                name="check_training_needed",
                kwargs={"user_id": "U312", "target_role": "Backend Tech Lead"},
            ),
            Action(
                name="recommend_course_for_gap",
                kwargs={"user_id": "U312", "target_role": "Backend Tech Lead"},
            ),
            Action(
                name="validate_course_skill_mapping",
                kwargs={"course_id": "C1004", "skill_name": "Team Leadership"},
            ),
            Action(
                name="shortlist_successor_candidate",
                kwargs={
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead",
                    "succession_for_role": "Software Engineer",
                },
            ),
        ],
        outputs=[],
    ),
    # 22 - COMPLEX: Succession planning with skill validation
    Task(
        annotator="0",
        user_id="res_172",
        instruction="Assess Harper Bennett's candidacy for the People Analytics Lead role. Perform a comprehensive assessment of her development needs, attempt to assign validated training, and conclude by positioning her for succession from her current HR Partner role by shortlisting her.",
        actions=[
            Action(name="get_user_id", kwargs={"user_name": "Harper Bennett"}),
            Action(
                name="validate_user_goal_alignment",
                kwargs={"user_id": "U310", "target_role": "People Analytics Lead"},
            ),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U310", "target_role": "People Analytics Lead"},
            ),
            Action(
                name="assess_soft_skill_alignment",
                kwargs={"user_id": "U310", "target_role": "People Analytics Lead"},
            ),
            Action(
                name="check_training_needed",
                kwargs={"user_id": "U310", "target_role": "People Analytics Lead"},
            ),
            Action(
                name="recommend_course_for_gap",
                kwargs={"user_id": "U310", "target_role": "People Analytics Lead"},
            ),
            Action(
                name="validate_course_skill_mapping",
                kwargs={"course_id": "C1005", "skill_name": "Statistical Modeling"},
            ),
            Action(
                name="shortlist_successor_candidate",
                kwargs={
                    "user_id": "U310",
                    "target_role": "People Analytics Lead",
                },
            ),
        ],
        outputs=[],
    ),
    # 23 - COMPLEX: Leadership readiness with skill prioritization
    Task(
        annotator="0",
        user_id="res_173",
        instruction="Launch a cross-functional leadership initiative. Compare the readiness of Alexander Adams from the Engineering team for the 'Staff SRE' role and David Adams from the Product Design team for the 'DesignOps Lead' role. For each candidate, perform a comprehensive readiness assessment and, if they are deemed ready, formally establish their succession pathway by shortlisting them.",
        actions=[
            Action(name="get_user_id", kwargs={"user_name": "Alexander Adams"}),
            Action(name="get_user_id", kwargs={"user_name": "David Adams"}),
            # --- Process Alexander Adams (U306) ---
            Action(
                name="validate_user_goal_alignment",
                kwargs={"user_id": "U306", "target_role": "Staff SRE"},
            ),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U306", "target_role": "Staff SRE"},
            ),
            Action(
                name="check_training_needed",
                kwargs={"user_id": "U306", "target_role": "Staff SRE"},
            ),
            Action(
                name="shortlist_successor_candidate",
                kwargs={
                    "user_id": "U306",
                    "target_role": "Staff SRE",
                    "succession_for_role": "DevOps Engineer",
                },
            ),
            # --- Process David Adams (U304) ---
            Action(
                name="validate_user_goal_alignment",
                kwargs={"user_id": "U304", "target_role": "DesignOps Lead"},
            ),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U304", "target_role": "DesignOps Lead"},
            ),
            Action(
                name="check_training_needed",
                kwargs={"user_id": "U304", "target_role": "DesignOps Lead"},
            ),
            Action(
                name="shortlist_successor_candidate",
                kwargs={
                    "user_id": "U304",
                    "target_role": "DesignOps Lead",
                    "succession_for_role": "UX Designer",
                },
            ),
        ],
        outputs=[],
    ),
    # 24 - COMPLEX: Technical leadership with team assessment
    Task(
        annotator="0",
        user_id="res_174",
        instruction="Perform a competitive leadership evaluation for the Engineering Team (T003). Identify all members with leadership goals. For each candidate, perform a comprehensive readiness assessment for their respective target role. If training is needed and a valid course exists, assign it. Conclude by formally shortlisting each valid candidate for their target role.",
        actions=[
            Action(name="get_user_id", kwargs={"user_name": "Mason Desai"}),
            Action(name="get_user_id", kwargs={"user_name": "Alexander Adams"}),
            Action(name="get_team_members", kwargs={"team_id": "T003"}),
            Action(
                name="get_users_with_leadership_goals",
                kwargs={"user_ids": ["U306", "U312"]},
            ),
            # --- Process Mason Desai (U312) ---
            Action(name="get_user_target_role", kwargs={"user_id": "U312"}),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U312", "target_role": "Backend Tech Lead"},
            ),
            Action(
                name="check_training_needed",
                kwargs={"user_id": "U312", "target_role": "Backend Tech Lead"},
            ),
            Action(
                name="recommend_course_for_gap",
                kwargs={"user_id": "U312", "target_role": "Backend Tech Lead"},
            ),
            Action(
                name="validate_course_skill_mapping",
                kwargs={"course_id": "C1004", "skill_name": "Team Leadership"},
            ),
            Action(
                name="shortlist_successor_candidate",
                kwargs={
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead",
                    "succession_for_role": "Software Engineer",
                },
            ),
            # --- Process Alexander Adams (U306) ---
            Action(name="get_user_target_role", kwargs={"user_id": "U306"}),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U306", "target_role": "Staff SRE"},
            ),
            Action(
                name="check_training_needed",
                kwargs={"user_id": "U306", "target_role": "Staff SRE"},
            ),
            Action(
                name="shortlist_successor_candidate",
                kwargs={
                    "user_id": "U306",
                    "target_role": "Staff SRE",
                    "succession_for_role": "DevOps Engineer",
                },
            ),
        ],
        outputs=[],
    ),
    # 25 - COMPLEX: Succession planning with conditional enrollment
    Task(
        annotator="0",
        user_id="res_175",
        instruction="Evaluate Harper King's fit for the Product Marketing Specialist role. Perform a comprehensive assessment of her development needs, attempt to assign a validated course, and conclude by positioning her for succession from her current Brand Strategist role by shortlisting her.",
        actions=[
            Action(name="get_user_id", kwargs={"user_name": "Harper King"}),
            Action(
                name="validate_user_goal_alignment",
                kwargs={
                    "user_id": "U305",
                    "target_role": "Product Marketing Specialist",
                },
            ),
            Action(
                name="get_user_skill_gap",
                kwargs={
                    "user_id": "U305",
                    "target_role": "Product Marketing Specialist",
                },
            ),
            Action(
                name="assess_soft_skill_alignment",
                kwargs={
                    "user_id": "U305",
                    "target_role": "Product Marketing Specialist",
                },
            ),
            Action(
                name="check_training_needed",
                kwargs={
                    "user_id": "U305",
                    "target_role": "Product Marketing Specialist",
                },
            ),
            Action(
                name="recommend_course_for_gap",
                kwargs={
                    "user_id": "U305",
                    "target_role": "Product Marketing Specialist",
                },
            ),
            Action(
                name="validate_course_skill_mapping",
                kwargs={"course_id": "C1006", "skill_name": "Product Marketing"},
            ),
            Action(
                name="shortlist_successor_candidate",
                kwargs={
                    "user_id": "U305",
                    "target_role": "Product Marketing Specialist",
                },
            ),
        ],
        outputs=[],
    ),
    # 26 - COMPLEX: Design leadership with skill prioritization
    Task(
        annotator="0",
        user_id="res_176",
        instruction="Perform a comparative leadership readiness assessment for key candidates from the Product Design and Engineering teams. For David Adams, assess his readiness for the 'DesignOps Lead' role. For Mason Desai, assess his readiness for the 'Backend Tech Lead' role. For each, if they are deemed ready, formally establish their succession pathway by shortlisting them. If training is needed but no valid course exists, still proceed with shortlisting.",
        actions=[
            Action(name="get_user_id", kwargs={"user_name": "David Adams"}),
            Action(name="get_user_id", kwargs={"user_name": "Mason Desai"}),
            # --- Process David Adams (U304) ---
            Action(name="get_user_target_role", kwargs={"user_id": "U304"}),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U304", "target_role": "DesignOps Lead"},
            ),
            Action(
                name="check_training_needed",
                kwargs={"user_id": "U304", "target_role": "DesignOps Lead"},
            ),
            Action(
                name="shortlist_successor_candidate",
                kwargs={
                    "user_id": "U304",
                    "target_role": "DesignOps Lead",
                    "succession_for_role": "UX Designer",
                },
            ),
            # --- Process Mason Desai (U312) ---
            Action(name="get_user_target_role", kwargs={"user_id": "U312"}),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U312", "target_role": "Backend Tech Lead"},
            ),
            Action(
                name="check_training_needed",
                kwargs={"user_id": "U312", "target_role": "Backend Tech Lead"},
            ),
            Action(
                name="recommend_course_for_gap",
                kwargs={"user_id": "U312", "target_role": "Backend Tech Lead"},
            ),
            Action(
                name="validate_course_skill_mapping",
                kwargs={"course_id": "C1004", "skill_name": "Team Leadership"},
            ),
            Action(
                name="shortlist_successor_candidate",
                kwargs={
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead",
                    "succession_for_role": "Software Engineer",
                },
            ),
        ],
        outputs=[],
    ),
    # 27 - COMPLEX: Technical leadership with experience assessment
    Task(
        annotator="0",
        user_id="res_177",
        instruction="Perform a comparative leadership readiness assessment for key candidates from the Engineering and Product Design teams. For Alexander Adams, assess his readiness for the 'Staff SRE' role. For David Adams, assess his readiness for the 'DesignOps Lead' role. For each, formally establish their succession pathway by shortlisting them.",
        actions=[
            Action(name="get_user_id", kwargs={"user_name": "Alexander Adams"}),
            Action(name="get_user_id", kwargs={"user_name": "David Adams"}),
            # --- Process Alexander Adams (U306) ---
            Action(name="get_user_target_role", kwargs={"user_id": "U306"}),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U306", "target_role": "Staff SRE"},
            ),
            Action(
                name="check_training_needed",
                kwargs={"user_id": "U306", "target_role": "Staff SRE"},
            ),
            Action(
                name="shortlist_successor_candidate",
                kwargs={
                    "user_id": "U306",
                    "target_role": "Staff SRE",
                    "succession_for_role": "DevOps Engineer",
                },
            ),
            # --- Process David Adams (U304) ---
            Action(name="get_user_target_role", kwargs={"user_id": "U304"}),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U304", "target_role": "DesignOps Lead"},
            ),
            Action(
                name="check_training_needed",
                kwargs={"user_id": "U304", "target_role": "DesignOps Lead"},
            ),
            Action(
                name="shortlist_successor_candidate",
                kwargs={
                    "user_id": "U304",
                    "target_role": "DesignOps Lead",
                    "succession_for_role": "UX Designer",
                },
            ),
        ],
        outputs=[],
    ),
    # 28 - COMPLEX: Dual career development with skill comparison
    Task(
        annotator="0",
        user_id="res_178",
        instruction="Perform a comparative career development assessment for Ava Nguyen and Mason Desai. For each, validate their leadership goals. For Mason Desai, assess his readiness for the Backend Tech Lead role, attempt to validate a training course for his skill gaps, and formally shortlist him for the position.",
        actions=[
            Action(name="get_user_id", kwargs={"user_name": "Ava Nguyen"}),
            Action(name="get_user_id", kwargs={"user_name": "Mason Desai"}),
            # --- Process Ava Nguyen (U302) ---
            Action(name="get_user_goals", kwargs={"user_id": "U302"}),
            # --- Process Mason Desai (U312) ---
            Action(name="get_user_goals", kwargs={"user_id": "U312"}),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U312", "target_role": "Backend Tech Lead"},
            ),
            Action(
                name="check_training_needed",
                kwargs={"user_id": "U312", "target_role": "Backend Tech Lead"},
            ),
            Action(
                name="recommend_course_for_gap",
                kwargs={"user_id": "U312", "target_role": "Backend Tech Lead"},
            ),
            Action(
                name="validate_course_skill_mapping",
                kwargs={"course_id": "C1004", "skill_name": "Team Leadership"},
            ),
            Action(
                name="shortlist_successor_candidate",
                kwargs={
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead",
                },
            ),
        ],
        outputs=[],
    ),
    # 29 - COMPLEX: Cross-functional leadership development
    Task(
        annotator="0",
        user_id="res_179",
        instruction="For cross-functional leadership development, identify the strongest candidates for the DesignOps Lead and People Analytics Lead roles from their respective teams (T002 and T008). Assess their expertise, evaluate their backgrounds, and enroll them in targeted training.",
        actions=[
            Action(name="get_team_members", kwargs={"team_id": "T002"}),
            Action(name="get_team_members", kwargs={"team_id": "T008"}),
            Action(
                name="get_users_with_leadership_goals",
                kwargs={"user_ids": ["U304", "U307", "U310"]},
            ),
            Action(
                name="validate_user_goal_alignment",
                kwargs={"user_id": "U304", "target_role": "DesignOps Lead"},
            ),
            Action(
                name="validate_user_goal_alignment",
                kwargs={"user_id": "U310", "target_role": "People Analytics Lead"},
            ),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U304", "target_role": "DesignOps Lead"},
            ),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U310", "target_role": "People Analytics Lead"},
            ),
            Action(
                name="recommend_course_for_gap",
                kwargs={"user_id": "U304", "target_role": "DesignOps Lead"},
            ),
            Action(
                name="recommend_course_for_gap",
                kwargs={"user_id": "U310", "target_role": "People Analytics Lead"},
            ),
            Action(
                name="assign_course_to_user",
                kwargs={"user_id": "U304", "course_id": "C1004"},
            ),
            Action(
                name="assign_course_to_user",
                kwargs={"user_id": "U310", "course_id": "C1005"},
            ),
        ],
        outputs=["Course assigned to user.", "DesignOps Lead"],
    ),
    # 30 - COMPLEX: Certification pathway with skill validation
    Task(
        annotator="0",
        user_id="res_190",
        instruction="Establish a promotion pathway for Jack Wang (U301) to become Director of Data Science. Assess his foundational skills, assign the appropriate specialization training, and formally track his candidacy.",
        actions=[
            Action(
                name="validate_user_goal_alignment",
                kwargs={"user_id": "U301", "target_role": "Director of Data Science"},
            ),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U301", "target_role": "Director of Data Science"},
            ),
            Action(
                name="check_training_needed",
                kwargs={"user_id": "U301", "target_role": "Director of Data Science"},
            ),
            Action(
                name="recommend_course_for_gap",
                kwargs={"user_id": "U301", "target_role": "Director of Data Science"},
            ),
            Action(
                name="assign_course_to_user",
                kwargs={"user_id": "U301", "course_id": "C1005"},
            ),
            Action(
                name="shortlist_successor_candidate",
                kwargs={
                    "user_id": "U301",
                    "target_role": "Director of Data Science",
                },
            ),
        ],
        outputs=["Course assigned to user."],
    ),
    # 31 - COMPLEX: Role transition with skill assessment
    Task(
        annotator="0",
        user_id="res_191",
        instruction="Perform a comparative career transition assessment for Harper King and Mason Desai. For each, perform a comprehensive readiness evaluation for their respective target role (Product Marketing Specialist and Backend Tech Lead). If training is needed but no valid course can be found, proceed to formally establish their transition pathway by shortlisting them.",
        actions=[
            Action(name="get_user_id", kwargs={"user_name": "Harper King"}),
            Action(name="get_user_id", kwargs={"user_name": "Mason Desai"}),
            # --- Process Harper King (U305) ---
            Action(name="get_user_target_role", kwargs={"user_id": "U305"}),
            Action(
                name="get_user_skill_gap",
                kwargs={
                    "user_id": "U305",
                    "target_role": "Product Marketing Specialist",
                },
            ),
            Action(
                name="check_training_needed",
                kwargs={
                    "user_id": "U305",
                    "target_role": "Product Marketing Specialist",
                },
            ),
            Action(
                name="recommend_course_for_gap",
                kwargs={
                    "user_id": "U305",
                    "target_role": "Product Marketing Specialist",
                },
            ),
            Action(
                name="validate_course_skill_mapping",
                kwargs={"course_id": "C1006", "skill_name": "Product Marketing"},
            ),
            Action(
                name="shortlist_successor_candidate",
                kwargs={
                    "user_id": "U305",
                    "target_role": "Product Marketing Specialist",
                    "succession_for_role": "Brand Strategist",
                },
            ),
            # --- Process Mason Desai (U312) ---
            Action(name="get_user_target_role", kwargs={"user_id": "U312"}),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U312", "target_role": "Backend Tech Lead"},
            ),
            Action(
                name="check_training_needed",
                kwargs={"user_id": "U312", "target_role": "Backend Tech Lead"},
            ),
            Action(
                name="recommend_course_for_gap",
                kwargs={"user_id": "U312", "target_role": "Backend Tech Lead"},
            ),
            Action(
                name="validate_course_skill_mapping",
                kwargs={"course_id": "C1004", "skill_name": "Team Leadership"},
            ),
            Action(
                name="shortlist_successor_candidate",
                kwargs={
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead",
                    "succession_for_role": "Software Engineer",
                },
            ),
        ],
        outputs=[],
    ),
    # 32 - COMPLEX: Leadership readiness with skill prioritization
    Task(
        annotator="0",
        user_id="res_192",
        instruction="Evaluate Mason Desai's (U312) fit for the Backend Tech Lead role. Assess his technical skills and development needs, then position him for succession by assigning targeted training and shortlisting him.",
        actions=[
            Action(
                name="validate_user_goal_alignment",
                kwargs={"user_id": "U312", "target_role": "Backend Tech Lead"},
            ),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U312", "target_role": "Backend Tech Lead"},
            ),
            Action(
                name="assess_soft_skill_alignment",
                kwargs={"user_id": "U312", "target_role": "Backend Tech Lead"},
            ),
            Action(
                name="check_training_needed",
                kwargs={"user_id": "U312", "target_role": "Backend Tech Lead"},
            ),
            Action(
                name="recommend_course_for_gap",
                kwargs={"user_id": "U312", "target_role": "Backend Tech Lead"},
            ),
            Action(
                name="validate_course_skill_mapping",
                kwargs={"course_id": "C1004", "skill_name": "Team Leadership"},
            ),
            Action(
                name="shortlist_successor_candidate",
                kwargs={
                    "user_id": "U312",
                    "target_role": "Backend Tech Lead",
                },
            ),
        ],
        outputs=[],
    ),
    # 33 - COMPLEX: Design leadership with skill prioritization
    Task(
        annotator="0",
        user_id="res_193",
        instruction="Perform a comparative leadership readiness assessment for key candidates from Product Design and Analytics: David Adams for the 'DesignOps Lead' role and Jack Wang for the 'Director of Data Science' role. For each, perform a comprehensive assessment, assign validated training if needed, and formally establish their succession pathway by shortlisting them.",
        actions=[
            Action(name="get_user_id", kwargs={"user_name": "David Adams"}),
            Action(name="get_user_id", kwargs={"user_name": "Jack Wang"}),
            # --- Process David Adams (U304) - No Training Needed ---
            Action(name="get_user_target_role", kwargs={"user_id": "U304"}),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U304", "target_role": "DesignOps Lead"},
            ),
            Action(
                name="assess_soft_skill_alignment",
                kwargs={"user_id": "U304", "target_role": "DesignOps Lead"},
            ),
            Action(
                name="check_training_needed",
                kwargs={"user_id": "U304", "target_role": "DesignOps Lead"},
            ),
            Action(
                name="shortlist_successor_candidate",
                kwargs={
                    "user_id": "U304",
                    "target_role": "DesignOps Lead",
                    "succession_for_role": "UX Designer",
                },
            ),
            # --- Process Jack Wang (U301) - Training Needed & Valid ---
            Action(name="get_user_target_role", kwargs={"user_id": "U301"}),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U301", "target_role": "Director of Data Science"},
            ),
            Action(
                name="assess_soft_skill_alignment",
                kwargs={"user_id": "U301", "target_role": "Director of Data Science"},
            ),
            Action(
                name="check_training_needed",
                kwargs={"user_id": "U301", "target_role": "Director of Data Science"},
            ),
            Action(
                name="recommend_course_for_gap",
                kwargs={"user_id": "U301", "target_role": "Director of Data Science"},
            ),
            Action(
                name="validate_course_skill_mapping",
                kwargs={"course_id": "C1005", "skill_name": "Machine Learning"},
            ),
            Action(
                name="log_team_training",
                kwargs={
                    "user_id": "U301",
                    "skill_name": "Machine Learning",
                    "course_id": "C1005",
                },
            ),
            Action(
                name="assign_course_to_user",
                kwargs={"user_id": "U301", "course_id": "C1005"},
            ),
            Action(
                name="shortlist_successor_candidate",
                kwargs={
                    "user_id": "U301",
                    "target_role": "Director of Data Science",
                    "succession_for_role": "Analytics Manager",
                },
            ),
        ],
        outputs=[],
    ),
    # 34 - COMPLEX: Technical leadership with experience assessment
    Task(
        annotator="0",
        user_id="res_194",
        instruction="Create a development plan for Jack Wang to transition to Director of Data Science. Assess his readiness, assign validated training for his highest-priority skill gap, and formalize his career path by shortlisting him.",
        actions=[
            Action(name="get_user_id", kwargs={"user_name": "Jack Wang"}),
            Action(
                name="validate_user_goal_alignment",
                kwargs={"user_id": "U301", "target_role": "Director of Data Science"},
            ),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U301", "target_role": "Director of Data Science"},
            ),
            Action(
                name="check_training_needed",
                kwargs={"user_id": "U301", "target_role": "Director of Data Science"},
            ),
            Action(
                name="recommend_course_for_gap",
                kwargs={"user_id": "U301", "target_role": "Director of Data Science"},
            ),
            Action(
                name="validate_course_skill_mapping",
                kwargs={"course_id": "C1005", "skill_name": "Machine Learning"},
            ),
            Action(
                name="log_team_training",
                kwargs={
                    "user_id": "U301",
                    "skill_name": "Machine Learning",
                    "course_id": "C1005",
                },
            ),
            Action(
                name="assign_course_to_user",
                kwargs={"user_id": "U301", "course_id": "C1005"},
            ),
            Action(
                name="shortlist_successor_candidate",
                kwargs={
                    "user_id": "U301",
                    "target_role": "Director of Data Science",
                },
            ),
        ],
        outputs=[],
    ),
    # 35 - COMPLEX: Technical milestone with skill assessment
    Task(
        annotator="0",
        user_id="res_195",
        instruction="Establish a promotion track for Jack Wang (U301) to Director of Data Science. The plan must validate his readiness, assign validated training for his highest-priority skill gap, and formally shortlist him for the role.",
        actions=[
            Action(
                name="validate_user_goal_alignment",
                kwargs={"user_id": "U301", "target_role": "Director of Data Science"},
            ),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U301", "target_role": "Director of Data Science"},
            ),
            Action(
                name="check_training_needed",
                kwargs={"user_id": "U301", "target_role": "Director of Data Science"},
            ),
            Action(
                name="recommend_course_for_gap",
                kwargs={"user_id": "U301", "target_role": "Director of Data Science"},
            ),
            Action(
                name="validate_course_skill_mapping",
                kwargs={"course_id": "C1005", "skill_name": "Machine Learning"},
            ),
            Action(
                name="log_team_training",
                kwargs={
                    "user_id": "U301",
                    "skill_name": "Machine Learning",
                    "course_id": "C1005",
                },
            ),
            Action(
                name="assign_course_to_user",
                kwargs={"user_id": "U301", "course_id": "C1005"},
            ),
            Action(
                name="shortlist_successor_candidate",
                kwargs={
                    "user_id": "U301",
                    "target_role": "Director of Data Science",
                },
            ),
        ],
        outputs=[],
    ),
    # 36 - COMPLEX: Conditional training pathway with comprehensive assessment
    Task(
        annotator="0",
        user_id="res_196",
        instruction="Perform a comprehensive readiness assessment for Ava Nguyen's (U302) transition to Clinical Analytics Lead. Validate her background on the Data Analytics Team (T001), evaluate her development needs, assign targeted training, and formally position her for succession.",
        actions=[
            Action(
                name="validate_team_membership",
                kwargs={"user_id": "U302", "team_id": "T001"},
            ),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U302", "target_role": "Clinical Analytics Lead"},
            ),
            Action(
                name="check_training_needed",
                kwargs={"user_id": "U302", "target_role": "Clinical Analytics Lead"},
            ),
            Action(
                name="assess_soft_skill_alignment",
                kwargs={"user_id": "U302", "target_role": "Clinical Analytics Lead"},
            ),
            Action(
                name="recommend_course_for_gap",
                kwargs={"user_id": "U302", "target_role": "Clinical Analytics Lead"},
            ),
            Action(
                name="assign_course_to_user",
                kwargs={"user_id": "U302", "course_id": "C1001"},
            ),
            Action(
                name="shortlist_successor_candidate",
                kwargs={
                    "user_id": "U302",
                    "target_role": "Clinical Analytics Lead",
                },
            ),
        ],
        outputs=["Course assigned to user.", "Candidate shortlisted."],
    ),
    # 37 - COMPLEX: Leadership communication milestone with comprehensive evaluation
    Task(
        annotator="0",
        user_id="res_197",
        instruction="For Alexander Adams of the Engineering Team (T003), perform a comprehensive readiness assessment for the Staff SRE role. Attempt to assign validated training for his highest-priority skill gap. Conclude by formally establishing his succession pathway by shortlisting him.",
        actions=[
            Action(name="get_user_id", kwargs={"user_name": "Alexander Adams"}),
            Action(
                name="validate_team_membership",
                kwargs={"user_id": "U306", "team_id": "T003"},
            ),
            Action(
                name="validate_user_goal_alignment",
                kwargs={"user_id": "U306", "target_role": "Staff SRE"},
            ),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U306", "target_role": "Staff SRE"},
            ),
            Action(
                name="assess_soft_skill_alignment",
                kwargs={"user_id": "U306", "target_role": "Staff SRE"},
            ),
            Action(
                name="check_training_needed",
                kwargs={"user_id": "U306", "target_role": "Staff SRE"},
            ),
            Action(
                name="shortlist_successor_candidate",
                kwargs={
                    "user_id": "U306",
                    "target_role": "Staff SRE",
                },
            ),
        ],
        outputs=[],
    ),
    # 38 - COMPLEX: Senior data scientist accelerator with comprehensive assessment
    Task(
        annotator="0",
        user_id="res_198",
        instruction="Jack Wang (U301) needs to close his skill gaps for the Director of Data Science role. Create a development plan that identifies his highest-priority training need, validates the recommended course, and assigns it to him.",
        actions=[
            Action(
                name="get_user_goals",
                kwargs={"user_id": "U301"},
            ),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U301", "target_role": "Director of Data Science"},
            ),
            Action(
                name="check_training_needed",
                kwargs={"user_id": "U301", "target_role": "Director of Data Science"},
            ),
            Action(
                name="recommend_course_for_gap",
                kwargs={"user_id": "U301", "target_role": "Director of Data Science"},
            ),
            Action(
                name="validate_course_skill_mapping",
                kwargs={"course_id": "C1005", "skill_name": "Machine Learning"},
            ),
            Action(
                name="log_team_training",
                kwargs={
                    "user_id": "U301",
                    "skill_name": "Machine Learning",
                    "course_id": "C1005",
                },
            ),
            Action(
                name="assign_course_to_user",
                kwargs={"user_id": "U301", "course_id": "C1005"},
            ),
        ],
        outputs=[],
    ),
    # 39 - COMPLEX: DesignOps accelerator with stakeholder alignment and comprehensive evaluation
    Task(
        annotator="0",
        user_id="res_199",
        instruction="For David Adams of the Product Design Team (T002), perform a comprehensive readiness assessment for the DesignOps Lead role. If the assessment shows training is needed, assign a suitable course. Finally, formalize his succession plan by shortlisting him.",
        actions=[
            Action(name="get_user_id", kwargs={"user_name": "David Adams"}),
            Action(
                name="validate_team_membership",
                kwargs={"user_id": "U304", "team_id": "T002"},
            ),
            Action(
                name="validate_user_goal_alignment",
                kwargs={"user_id": "U304", "target_role": "DesignOps Lead"},
            ),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U304", "target_role": "DesignOps Lead"},
            ),
            Action(
                name="assess_soft_skill_alignment",
                kwargs={"user_id": "U304", "target_role": "DesignOps Lead"},
            ),
            Action(
                name="check_training_needed",
                kwargs={"user_id": "U304", "target_role": "DesignOps Lead"},
            ),
            Action(
                name="shortlist_successor_candidate",
                kwargs={
                    "user_id": "U304",
                    "target_role": "DesignOps Lead",
                },
            ),
        ],
        outputs=[],
    ),
    # 40 - COMPLEX: Cloud security architect track with comprehensive assessment
    Task(
        annotator="0",
        user_id="res_230",
        instruction="Establish a promotion track for Jack Wang (U301) to Director of Data Science. Perform a comprehensive assessment of his foundational needs, assign advanced training, and formalize his succession plan.",
        actions=[
            Action(
                name="validate_user_goal_alignment",
                kwargs={"user_id": "U301", "target_role": "Director of Data Science"},
            ),
            Action(
                name="get_user_skill_gap",
                kwargs={"user_id": "U301", "target_role": "Director of Data Science"},
            ),
            Action(
                name="assess_soft_skill_alignment",
                kwargs={"user_id": "U301", "target_role": "Director of Data Science"},
            ),
            Action(
                name="check_training_needed",
                kwargs={"user_id": "U301", "target_role": "Director of Data Science"},
            ),
            Action(
                name="recommend_course_for_gap",
                kwargs={"user_id": "U301", "target_role": "Director of Data Science"},
            ),
            Action(
                name="validate_course_skill_mapping",
                kwargs={"course_id": "C1005", "skill_name": "Machine Learning"},
            ),
            Action(
                name="log_team_training",
                kwargs={
                    "user_id": "U301",
                    "skill_name": "Machine Learning",
                    "course_id": "C1005",
                },
            ),
            Action(
                name="assign_course_to_user",
                kwargs={"user_id": "U301", "course_id": "C1005"},
            ),
            Action(
                name="shortlist_successor_candidate",
                kwargs={
                    "user_id": "U301",
                    "target_role": "Director of Data Science",
                },
            ),
        ],
        outputs=[],
    ),
]
